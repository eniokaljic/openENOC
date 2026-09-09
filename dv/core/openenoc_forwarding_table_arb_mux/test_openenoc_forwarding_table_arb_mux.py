# SPDX-FileCopyrightText: 2026 Kerim Bavcic
# SPDX-License-Identifier: AGPL-3.0-or-later

import os
import random
from dataclasses import dataclass

import cocotb
import cocotb_test.simulator
import pytest
from cocotb.triggers import Timer
from cocotb.regression import TestFactory

TestFactory.__test__ = False


# ----------------------------------------------------------------------
# Helper functions and reference model
# ----------------------------------------------------------------------

def field(value, index, width):
    return (int(value) >> (index * width)) & ((1 << width) - 1)


@dataclass
class ArbMuxTransaction:
    """One expected request and its progress through the arb-mux."""

    channel: int
    port: int
    mac: int
    bitmap: int
    result: int
    delay: int
    submitted: int | None = None
    started: int | None = None
    completed: int | None = None


class TB:
    def __init__(self, dut, latency="alternating"):
        self.dut = dut
        self.n = int(os.environ.get("PARAM_NUM_OF_INTERFACES", 4))
        self.index_w = (self.n - 1).bit_length()
        self.mask = (1 << self.n) - 1
        self.latency = latency
        self.rng = random.Random(0xA4B170 + self.n)
        self.serial = 0
        self.cycle = 0
        self.clear_model()

    def clear_model(self):
        self.queued = [{}, {}]
        self.outstanding = [{}, {}]
        self.active = [None, None]
        self.jobs = [None, None]
        self.pointer = [0, 0]
        self.launches = [[], []]
        self.accepted = [0, 0]
        self.returned = [0, 0]
        self.previous_source_req = 0
        self.previous_slave_req = 0
        self.overlap_cycles = 0

    def transaction(self, channel, port, delay=None):
        self.serial += 1
        if delay is None:
            if self.latency == "minimum":
                delay = 1
            elif self.latency == "alternating":
                delay = (1, 19, 2, 7, 31)[self.serial % 5]
            elif self.latency == "random":
                delay = self.rng.randint(1, 40)
            elif self.latency == "long":
                delay = self.rng.randint(64, 128)
            else:
                raise ValueError(self.latency)
        assert delay >= 1
        mac = (channel << 47) | (port << 32) | self.serial
        # Exercise zero, all-ones, multiport and high-bit payloads, not just onehot.
        bitmap = (
            0,
            self.mask,
            1 << (self.n - 1),
            self.rng.getrandbits(self.n),
        )[self.serial % 4]
        result = (mac ^ (mac >> 32) ^ (self.serial * 0x9E3779B9)) & self.mask
        return ArbMuxTransaction(channel, port, mac, bitmap, result, delay)

    async def tick(self, transactions=(), reset=False):
        """Drive one cycle; repeated transactions hold req high until released."""
        d, n = self.dut, self.n
        d.clk.value = 0
        d.rst.value = int(reset)
        driven = {(t.channel, t.port): t for t in transactions}
        assert len(driven) == len(transactions), (
            "two requests for one source in one cycle"
        )
        req, macs, bitmaps = 0, 0, 0
        for ch in range(2):
            for port in range(n):
                t = driven.get((ch, port))
                # Poison inactive payloads immediately after each strobe. This
                # exposes muxes that use live data instead of captured requests.
                mac = (
                    t.mac
                    if t
                    else 0xBAD000000000 | (self.cycle << 8) | port | (ch << 7)
                )
                macs |= mac << ((ch * n + port) * 48)
                if t:
                    req |= 1 << (ch * n + port)
                if ch:
                    bitmap = t.bitmap if t else (self.cycle ^ 0x55555555) & self.mask
                    bitmaps |= bitmap << (port * n)
        d.source_req.value = req if not reset else 0
        d.source_mac.value = macs
        d.source_learning_bitmap.value = bitmaps

        ack, result = 0, (self.cycle ^ 0xAAAAAAAA) & self.mask
        if not reset:
            for ch, job in enumerate(self.jobs):
                if job is not None and self.cycle == job.started + job.delay:
                    ack |= 1 << ch
                    if ch == 0:
                        result = job.result
        d.slave_ack.value = ack
        d.slave_lookup_bitmap.value = result
        await Timer(5, units="ns")

        if reset:
            assert int(d.source_ack.value) == 0
            assert int(d.slave_req.value) == 0
            self.clear_model()
        else:
            slave_req = int(d.slave_req.value)
            assert not (slave_req & self.previous_slave_req), "slave req longer than one cycle"
            self.previous_slave_req = slave_req
            self.overlap_cycles += all(t is not None for t in self.active)

            for ch in range(2):
                # Independent reference queue records SOURCE captures, not DUT
                # pending state. Compare both occupancy and RR winner every cycle.
                expected_pending = sum(1 << p for p in self.queued[ch])
                assert field(d.pending.value, ch, n) == expected_pending, (
                    "pending request lost/duplicated"
                )
                was_busy = self.active[ch] is not None
                assert bool(int(d.busy.value) & (1 << ch)) == was_busy
                expected_launch = bool(self.queued[ch]) and not was_busy
                assert bool(int(d.launch.value) & (1 << ch)) == expected_launch

                if was_busy:
                    t = self.active[ch]
                    assert field(d.owner.value, ch, self.index_w) == t.port, "active owner changed"
                    assert field(d.slave_mac.value, ch, 48) == t.mac, "active MAC changed"
                    if ch:
                        assert int(d.slave_learning_bitmap.value) == t.bitmap

                if slave_req & (1 << ch):
                    t = self.active[ch]
                    assert t is not None and self.jobs[ch] is None, (
                        "duplicate or unsolicited slave req"
                    )
                    assert t.started is None
                    t.started = self.cycle
                    self.jobs[ch] = t

                source_ack = field(d.source_ack.value, ch, n)
                if ack & (1 << ch):
                    t = self.jobs[ch]
                    assert t is self.active[ch] and t is not None
                    assert source_ack == 1 << t.port, "ack sent to wrong source"
                    assert self.cycle - t.started == t.delay
                    if ch == 0:
                        assert field(d.source_lookup_bitmap.value, t.port, n) == t.result
                    t.completed = self.cycle
                    del self.outstanding[ch][t.port]
                    self.returned[ch] += 1
                    self.active[ch] = self.jobs[ch] = None
                else:
                    assert source_ack == 0, "early, duplicate or unsolicited ack"

                if ch == 0:
                    for port in range(n):
                        if not (source_ack & (1 << port)):
                            assert field(d.source_lookup_bitmap.value, port, n) == 0

                if expected_launch:
                    winner = next(
                        (self.pointer[ch] + offset) % n
                        for offset in range(n)
                        if (self.pointer[ch] + offset) % n in self.queued[ch]
                    )
                    assert field(d.selected.value, ch, self.index_w) == winner, (
                        "non-RR grant"
                    )
                    self.active[ch] = self.queued[ch].pop(winner)
                    self.pointer[ch] = (winner + 1) % n
                    self.launches[ch].append(winner)

            # Captures happen at this edge AFTER selection from previously
            # queued work. Same-cycle ack + new pulse is legal for that source.
            capture = req & ~self.previous_source_req
            for (ch, port), t in driven.items():
                if capture & (1 << (ch * n + port)):
                    assert port not in self.outstanding[ch], "source reissued before ack"
                    assert t.submitted is None
                    t.submitted = self.cycle
                    self.outstanding[ch][port] = self.queued[ch][port] = t
                    self.accepted[ch] += 1
            self.previous_source_req = req

        d.clk.value = 1
        await Timer(5, units="ns")
        self.cycle += 1

    async def reset(self):
        for _ in range(4):
            await self.tick(reset=True)
        await self.tick()

    async def wait_started(self, transaction):
        for _ in range(10000):
            if transaction.started is not None:
                return
            await self.tick()
        raise AssertionError("timeout waiting for downstream request")

    async def drain(self, limit=20000):
        for _ in range(limit):
            if not any(self.outstanding):
                break
            await self.tick()
        else:
            raise AssertionError("lost/starved request: bounded drain timed out")
        # Quiet tail detects duplicate launches/responses after apparent success.
        for _ in range(8):
            await self.tick()
        assert self.accepted == self.returned
        assert not any(self.queued) and self.active == [None, None]


    # ----------------------------------------------------------------------
    # TestFactory traffic scenarios
    # ----------------------------------------------------------------------

async def run_traffic(dut, traffic="sequential", latency="alternating", channels=(0, 1)):
    tb = TB(dut, latency)
    await tb.reset()
    if traffic == "sequential":
        # Adjacent-cycle pulses from DIFFERENT sources while the channel queues.
        for port in range(tb.n):
            await tb.tick([tb.transaction(ch, port) for ch in channels])
        await tb.drain()
        # Same source must await ack. Reissue on the first following cycle.
        for _ in range(6):
            batch = [tb.transaction(ch, 0) for ch in channels]
            await tb.tick(batch)
            for _ in range(1000):
                if all(t.completed is not None for t in batch):
                    break
                await tb.tick()
            else:
                raise AssertionError("back-to-back request did not complete")
        await tb.drain()
    elif traffic == "midflight":
        # Inject a different source at the midpoint of each slave service time.
        # Repeat for multiple delays even under the minimum-latency profile.
        for delay in (8, 23, 64):
            first = [tb.transaction(ch, 0, delay) for ch in channels]
            await tb.tick(first)
            for t in first:
                await tb.wait_started(t)
            while tb.cycle < first[0].started + delay // 2:
                await tb.tick()
            assert all(t.completed is None for t in first)
            second = [tb.transaction(ch, 1) for ch in channels]
            await tb.tick(second)
            await tb.drain()
            for a, b in zip(first, second):
                assert a.started < b.submitted < a.completed
                assert b.started > a.completed
    elif traffic == "simultaneous":
        # Prime the pointer to a nonzero position, then all ports request at once.
        await tb.tick([tb.transaction(ch, 0) for ch in channels])
        await tb.drain()
        for _ in range(3):
            expected = {
                ch: [(tb.pointer[ch] + port) % tb.n for port in range(tb.n)]
                for ch in channels
            }
            offsets = {ch: len(tb.launches[ch]) for ch in channels}
            await tb.tick([
                tb.transaction(ch, port)
                for ch in channels
                for port in range(tb.n)
            ])
            await tb.drain()
            for ch in channels:
                assert tb.launches[ch][offsets[ch]:] == expected[ch]
    else:
        raise ValueError(traffic)
    for ch in set((0, 1)) - set(channels):
        assert tb.accepted[ch] == 0, "inactive channel was affected"


# ----------------------------------------------------------------------
# Standalone Cocotb test cases
# ----------------------------------------------------------------------

@cocotb.test()
async def test_independent_response_timing(dut):
    """Fast channel repeatedly completes while the other slave response is held."""
    for slow in (0, 1):
        tb = TB(dut)
        await tb.reset()
        slow_request = tb.transaction(slow, 0, delay=128)
        fast = 1 - slow
        fast_request = tb.transaction(fast, 1, delay=1)
        await tb.tick([slow_request, fast_request])
        await tb.wait_started(slow_request)
        for _ in range(8):
            while fast_request.completed is None:
                await tb.tick()
            assert slow_request.completed is None, "slow channel did not remain active"
            fast_request = tb.transaction(fast, 1, delay=1)
            await tb.tick([fast_request])
        await tb.drain()
        assert tb.overlap_cycles > 0
        assert tb.returned[fast] == 9 and tb.returned[slow] == 1


@cocotb.test()
async def test_new_request_on_ack_edge(dut):
    """Capture new sources AND same-owner reissues on the exact response edge."""
    tb = TB(dut)
    await tb.reset()
    first = [tb.transaction(ch, 0, delay=13) for ch in (0, 1)]
    await tb.tick(first)
    for t in first:
        await tb.wait_started(t)
    while tb.cycle < first[0].started + first[0].delay:
        await tb.tick()
    replacements = [
        tb.transaction(ch, port, delay=1 + port * 3)
        for ch in (0, 1)
        for port in range(tb.n)
    ]
    await tb.tick(replacements)
    assert all(t.completed is not None for t in first)
    assert all(t.submitted == first[0].completed for t in replacements)
    await tb.drain()
    assert tb.returned == [tb.n + 1, tb.n + 1]


@cocotb.test()
async def test_held_request_single_transaction(dut):
    """Optional held-until-ack compatibility must not produce duplicates."""
    tb = TB(dut)
    await tb.reset()
    batch = [
        tb.transaction(ch, port, delay=2 + port % 7)
        for ch in (0, 1)
        for port in range(tb.n)
    ]
    await tb.tick(batch)
    for _ in range(20000):
        held = [t for t in batch if t.completed is None]
        if not held:
            break
        await tb.tick(held)
    else:
        raise AssertionError("held request failed to complete")
    await tb.drain()
    assert tb.returned == [tb.n, tb.n]
    # A low req cycle rearms capture; another complete round must still work.
    await tb.tick([
        tb.transaction(ch, port)
        for ch in (0, 1)
        for port in range(tb.n)
    ])
    await tb.drain()
    assert tb.returned == [2 * tb.n, 2 * tb.n]


@cocotb.test()
async def test_randomized_arrivals_and_delays(dut):
    """Repeatable mixed bursts, refill after ack, variable latencies per channel."""
    tb = TB(dut, "random")
    await tb.reset()
    remaining = [[12] * tb.n for _ in range(2)]
    for _ in range(30000):
        if not any(any(counts) for counts in remaining):
            break
        batch = []
        for ch in (0, 1):
            for port in range(tb.n):
                if (
                    remaining[ch][port]
                    and port not in tb.outstanding[ch]
                    and tb.rng.random() < 0.3
                ):
                    batch.append(tb.transaction(ch, port))
                    remaining[ch][port] -= 1
        await tb.tick(batch)
    else:
        raise AssertionError("random traffic source starved")
    await tb.drain()
    assert tb.returned == [12 * tb.n, 12 * tb.n]
    assert tb.overlap_cycles > 0


@cocotb.test()
async def test_reset_active_and_pending(dut):
    """Reset cancels queued and active transactions in DUT and simulated slave."""
    tb = TB(dut)
    await tb.reset()
    old = [
        tb.transaction(ch, port, delay=40)
        for ch in (0, 1)
        for port in range(tb.n)
    ]
    await tb.tick(old)
    await tb.wait_started(old[0])
    assert all(tb.queued) and all(tb.jobs)
    await tb.reset()
    assert all(t.completed is None for t in old)
    for _ in range(50):
        await tb.tick()
    assert tb.returned == [0, 0]
    await tb.tick([
        tb.transaction(ch, port)
        for ch in (0, 1)
        for port in range(tb.n)
    ])
    await tb.drain()
    assert tb.returned == [tb.n, tb.n]
    assert tb.launches == [list(range(tb.n)), list(range(tb.n))]


# ----------------------------------------------------------------------
# TestFactory dispatch
# ----------------------------------------------------------------------

if getattr(cocotb, "top", None) is not None:
    factory = TestFactory(run_traffic)
    factory.add_option("traffic", ["sequential", "midflight", "simultaneous"])
    factory.add_option("latency", ["minimum", "alternating", "random", "long"])
    factory.add_option("channels", [(0,), (1,), (0, 1)])
    factory.generate_tests()


# ----------------------------------------------------------------------
# Pytest framework: parameter sweep and simulator runner
# ----------------------------------------------------------------------

tests_dir = os.path.dirname(__file__)
hw_dir = os.path.abspath(os.path.join(tests_dir, '..', '..', '..', 'hw'))
core_dir = os.path.join(hw_dir, 'rtl', 'core')
common_dir = os.path.abspath(os.path.join(tests_dir, '..', '..', 'common'))


@pytest.mark.parametrize("num_of_interfaces", [2, 4, 5, 8, 32])
def test_openenoc_forwarding_table_arb_mux(request, num_of_interfaces):
    dut = "openenoc_forwarding_table_arb_mux"
    module = os.path.splitext(os.path.basename(__file__))[0]
    toplevel = module

    verilog_sources = [
        os.path.join(tests_dir, f"{toplevel}.sv"),
        os.path.join(core_dir, "openenoc_lookup_if.sv"),
        os.path.join(core_dir, "openenoc_learning_if.sv"),
        os.path.join(core_dir, "openenoc_rr_arbiter.sv"),
        os.path.join(core_dir, f"{dut}.sv"),
    ]

    parameters = {}
    parameters["NUM_OF_INTERFACES"] = num_of_interfaces

    extra_env = {f'PARAM_{k}': str(v) for k, v in parameters.items()}

    sim_build = os.path.join(tests_dir, "sim_build",
        request.node.name.replace('[', '-').replace(']', ''))

    cocotb_test.simulator.run(
        simulator="verilator",
        python_search=[tests_dir],
        verilog_sources=verilog_sources,
        toplevel=toplevel,
        module=module,
        parameters=parameters,
        extra_args=[
            os.path.join(common_dir, "config.vlt"),
        ],
        sim_build=sim_build,
        extra_env=extra_env,
    )
