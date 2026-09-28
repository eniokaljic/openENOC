# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: AGPL-3.0-or-later

import os

import cocotb
import cocotb_test.simulator
import pytest
from cocotb.clock import Clock
from cocotb.triggers import FallingEdge, ReadOnly, RisingEdge, Timer


class TB:
    def __init__(self, dut):
        self.dut = dut
        self.ports = int(os.environ.get("PARAM_EVENT_PORTS", 4))
        self.depth = int(os.environ.get("PARAM_FIFO_DEPTH", 4))
        self.peer_w = int(os.environ.get("PARAM_PEER_IDX_W", 5))
        self.sequence_w = int(os.environ.get("PARAM_SEQUENCE_W", 4))
        self.port_mask = (1 << self.ports) - 1
        self.peer_mask = (1 << self.peer_w) - 1
        self.sequence_mask = (1 << self.sequence_w) - 1
        self.enables = 0
        self.global_enable = 0
        self.clock_task = None

    def _drive_transient_idle(self):
        d = self.dut
        d.clear_errors.value = 0
        d.complete_valid.value = 0
        d.complete_peer_idx.value = 0
        d.complete_source.value = 0
        d.complete_sequence.value = 0
        d.admit_valid.value = 0
        d.admit_source.value = 0
        d.admit_enable.value = 0
        d.commit_valid.value = 0
        d.commit_source.value = 0
        d.commit_peer_idx.value = 0

    def _drive_config(self):
        self.dut.event_enable.value = self.enables
        self.dut.global_enable.value = self.global_enable

    async def reset(self):
        d = self.dut
        if self.clock_task is None:
            d.clk.value = 0
            d.rst.value = 1
            self._drive_transient_idle()
            self._drive_config()
            self.clock_task = cocotb.start_soon(Clock(d.clk, 10, unit="ns").start())
        else:
            await FallingEdge(d.clk)
            d.rst.value = 1
            self._drive_transient_idle()
            self._drive_config()

        for _ in range(3):
            await RisingEdge(d.clk)

        await FallingEdge(d.clk)
        d.rst.value = 0
        self._drive_transient_idle()
        self._drive_config()
        await RisingEdge(d.clk)
        await ReadOnly()

        assert int(d.claim_valid.value) == 0
        assert int(d.claim_pending.value) == 0
        assert int(d.credit_full.value) == 0
        assert int(d.overflow.value) == 0
        assert int(d.invalid_complete.value) == 0
        assert int(d.fifo_level.value) == 0
        assert int(d.reserved_count.value) == 0
        assert int(d.irq.value) == 0

    async def cycle(self, admits=None, commits=None, complete=None, clear_errors=False):
        """Drive one complete cycle and return the pre-edge handshake values."""
        admits = admits or {}
        commits = commits or {}
        d = self.dut

        await FallingEdge(d.clk)
        self._drive_transient_idle()
        self._drive_config()

        admit_valid = 0
        admit_source = 0
        admit_enable = 0
        for port, (source, local_enable) in admits.items():
            admit_valid |= 1 << port
            admit_source |= (source & 0xF) << (port * 4)
            admit_enable |= int(local_enable) << port
        d.admit_valid.value = admit_valid
        d.admit_source.value = admit_source
        d.admit_enable.value = admit_enable

        commit_valid = 0
        commit_source = 0
        commit_peer_idx = 0
        for port, (source, peer_idx) in commits.items():
            commit_valid |= 1 << port
            commit_source |= (source & 0xF) << (port * 4)
            commit_peer_idx |= (peer_idx & self.peer_mask) << (port * self.peer_w)
        d.commit_valid.value = commit_valid
        d.commit_source.value = commit_source
        d.commit_peer_idx.value = commit_peer_idx

        if complete is not None:
            peer_idx, source, sequence = complete
            d.complete_valid.value = 1
            d.complete_peer_idx.value = peer_idx
            d.complete_source.value = source
            d.complete_sequence.value = sequence

        d.clear_errors.value = int(clear_errors)
        await Timer(1, unit="ns")

        handshake = {
            "admit_ready": int(d.admit_ready.value),
            "admit_reserved": int(d.admit_reserved.value),
            "commit_ready": int(d.commit_ready.value),
            "complete_hwclr": int(d.complete_valid_hwclr.value),
            "clear_hwclr": int(d.clear_errors_hwclr.value),
        }

        await RisingEdge(d.clk)
        await ReadOnly()
        return handshake

    async def admit(self, port, source, local_enable=True, reserved=True):
        handshake = await self.cycle(
            admits={port: (source, local_enable)},
        )
        assert handshake["admit_ready"] & (1 << port)
        assert bool(handshake["admit_reserved"] & (1 << port)) == reserved
        return handshake

    async def commit(self, port, source, peer_idx):
        handshake = await self.cycle(
            commits={port: (source, peer_idx)},
        )
        assert handshake["commit_ready"] & (1 << port)
        return handshake

    def claim(self):
        d = self.dut
        return (
            int(d.claim_peer_idx.value),
            int(d.claim_source.value),
            int(d.claim_sequence.value),
        )

    async def wait_claim(self, limit=16):
        for _ in range(limit):
            if int(self.dut.claim_valid.value):
                return
            await self.cycle()
        raise AssertionError("timeout waiting for claim FIFO output")

    async def complete_claim(self):
        claim = self.claim()
        handshake = await self.cycle(complete=claim)
        assert handshake["complete_hwclr"] == 1
        return claim


@cocotb.test()
async def test_disabled_admission_and_error_maintenance(dut):
    """Disabled events are transparent; malformed requests set sticky errors."""
    tb = TB(dut)
    await tb.reset()

    admits = {
        port: (port % 5, True)
        for port in range(tb.ports)
    }
    handshake = await tb.cycle(admits=admits)
    assert handshake["admit_ready"] == tb.port_mask
    assert handshake["admit_reserved"] == 0
    assert int(dut.reserved_count.value) == 0

    # A local producer enable of zero and reserved source values are also
    # accepted without consuming a credit.
    handshake = await tb.cycle(admits={0: (0, False)})
    assert handshake["admit_ready"] & 1
    assert handshake["admit_reserved"] == 0
    handshake = await tb.cycle(admits={0: (15, True)})
    assert handshake["admit_ready"] & 1
    assert handshake["admit_reserved"] == 0

    # Each event class is controlled by its corresponding enable bit.
    for source in range(5):
        tb.enables = 1 << source
        await tb.admit(0, source=source)
        await tb.commit(0, source=source, peer_idx=tb.peer_mask)
        await tb.wait_claim()
        assert int(dut.claim_source.value) == source
        expected_peer = tb.peer_mask if source == 0 else 0
        assert int(dut.claim_peer_idx.value) == expected_peer
        await tb.complete_claim()

        disabled_source = (source + 1) % 5
        await tb.admit(0, source=disabled_source, reserved=False)

    # A commit without a reservation is consumed and reported as overflow.
    handshake = await tb.cycle(commits={0: (0, 3)})
    assert handshake["commit_ready"] == 1
    assert int(dut.overflow.value) == 1
    assert int(dut.fifo_level.value) == 0

    handshake = await tb.cycle(clear_errors=True)
    assert handshake["clear_hwclr"] == 1
    assert int(dut.overflow.value) == 0

    # Completing an empty FIFO is a protocol error and must not invent a claim.
    handshake = await tb.cycle(complete=(0, 0, 0))
    assert handshake["complete_hwclr"] == 1
    assert int(dut.invalid_complete.value) == 1
    assert int(dut.claim_valid.value) == 0

    handshake = await tb.cycle(clear_errors=True)
    assert handshake["clear_hwclr"] == 1
    assert int(dut.invalid_complete.value) == 0


@cocotb.test()
async def test_claim_completion_and_irq_mask(dut):
    """A reservation becomes a stable claim and only an exact token removes it."""
    tb = TB(dut)
    await tb.reset()
    tb.enables = 0x1F

    port = min(1, tb.ports - 1)
    peer = min(0x15, tb.peer_mask)
    await tb.admit(port, source=0)
    assert int(dut.reserved_count.value) == 1
    assert int(dut.fifo_level.value) == 0

    await tb.admit(0, source=0, local_enable=False, reserved=False)
    assert int(dut.reserved_count.value) == 1

    if tb.ports > 1:
        wrong_port = (port + 1) % tb.ports
        await tb.commit(wrong_port, source=0, peer_idx=peer)
        assert int(dut.overflow.value) == 1
        assert int(dut.reserved_count.value) == 1
        assert int(dut.fifo_level.value) == 0
        await tb.cycle(clear_errors=True)
        assert int(dut.overflow.value) == 0

    await tb.commit(port, source=0, peer_idx=peer)
    await tb.wait_claim()
    assert int(dut.reserved_count.value) == 0
    assert int(dut.fifo_level.value) == 1
    assert tb.claim() == (peer, 0, 0)

    tb.global_enable = 0
    await tb.cycle()
    assert int(dut.claim_pending.value) == 1
    assert int(dut.irq.value) == 0
    assert int(dut.irq_asserted.value) == 0

    tb.global_enable = 1
    await tb.cycle()
    assert int(dut.irq.value) == 1
    assert int(dut.irq_asserted.value) == 1

    original_claim = tb.claim()
    await tb.cycle()
    await tb.cycle()
    assert tb.claim() == original_claim

    wrong_sequence = (original_claim[2] + 1) & tb.sequence_mask
    handshake = await tb.cycle(
        complete=(original_claim[0], original_claim[1], wrong_sequence)
    )
    assert handshake["complete_hwclr"] == 1
    assert int(dut.invalid_complete.value) == 1
    assert tb.claim() == original_claim
    assert int(dut.fifo_level.value) == 1

    await tb.complete_claim()
    assert int(dut.claim_valid.value) == 0
    assert int(dut.fifo_level.value) == 0
    assert int(dut.irq.value) == 0

    await tb.cycle(clear_errors=True)
    assert int(dut.invalid_complete.value) == 0

    # Non-peer claims have deterministic peer_idx=0 regardless of producer data.
    await tb.admit(0, source=3)
    await tb.commit(0, source=3, peer_idx=tb.peer_mask)
    await tb.wait_claim()
    assert tb.claim() == (0, 3, 1 & tb.sequence_mask)


@cocotb.test()
async def test_credit_full_and_completion_edge_reuse(dut):
    """A full FIFO backpressures enabled work and reuses a completing credit."""
    tb = TB(dut)
    await tb.reset()
    tb.enables = 0x01

    for peer in range(tb.depth):
        await tb.admit(0, source=0)
        await tb.commit(0, source=0, peer_idx=peer)

    assert int(dut.fifo_level.value) == min(tb.depth, 255)
    assert int(dut.reserved_count.value) == 0
    assert int(dut.credit_full.value) == 1

    handshake = await tb.cycle(admits={0: (0, True)})
    assert (handshake["admit_ready"] & 1) == 0
    assert handshake["admit_reserved"] == 0

    # Disabled traffic is not blocked by an exhausted event FIFO.
    handshake = await tb.cycle(admits={0: (4, True)})
    assert handshake["admit_ready"] & 1
    assert handshake["admit_reserved"] == 0

    old_head = tb.claim()
    handshake = await tb.cycle(
        admits={0: (0, True)},
        complete=old_head,
    )
    assert handshake["admit_ready"] & 1
    assert handshake["admit_reserved"] & 1
    assert handshake["complete_hwclr"] == 1
    assert int(dut.fifo_level.value) == min(tb.depth - 1, 255)
    assert int(dut.reserved_count.value) == 1
    assert int(dut.credit_full.value) == 1

    replacement_peer = tb.peer_mask
    await tb.commit(0, source=0, peer_idx=replacement_peer)
    assert int(dut.fifo_level.value) == min(tb.depth, 255)
    assert int(dut.reserved_count.value) == 0

    expected_peers = list(range(1, tb.depth)) + [replacement_peer]
    expected_sequences = [
        sequence & tb.sequence_mask
        for sequence in range(1, tb.depth + 1)
    ]
    for peer, sequence in zip(expected_peers, expected_sequences):
        await tb.wait_claim()
        assert tb.claim() == (peer & tb.peer_mask, 0, sequence)
        await tb.complete_claim()

    assert int(dut.fifo_level.value) == 0
    assert int(dut.credit_full.value) == 0


@cocotb.test()
async def test_independent_round_robin_arbitration(dut):
    """Admission and commit channels independently rotate through contenders."""
    tb = TB(dut)
    await tb.reset()
    tb.enables = 0x01

    rounds = min(tb.ports, tb.depth)
    all_admits = {port: (0, True) for port in range(tb.ports)}
    for winner in range(rounds):
        handshake = await tb.cycle(admits=all_admits)
        assert handshake["admit_ready"] == 1 << winner
        assert handshake["admit_reserved"] == 1 << winner

    assert int(dut.reserved_count.value) == rounds

    all_commits = {
        port: (0, port + 1)
        for port in range(tb.ports)
    }
    for winner in range(rounds):
        handshake = await tb.cycle(commits=all_commits)
        assert handshake["commit_ready"] == 1 << winner

    assert int(dut.reserved_count.value) == 0
    assert int(dut.fifo_level.value) == rounds

    for port in range(rounds):
        await tb.wait_claim()
        assert tb.claim() == (
            (port + 1) & tb.peer_mask,
            0,
            port & tb.sequence_mask,
        )
        await tb.complete_claim()


@cocotb.test()
async def test_simultaneous_commit_and_completion(dut):
    """A FIFO pop and reserved commit can replace the head without a bubble."""
    tb = TB(dut)
    await tb.reset()
    if tb.depth < 2:
        return

    tb.enables = 0x01
    first_peer = min(3, tb.peer_mask)
    second_peer = min(7, tb.peer_mask)

    await tb.admit(0, source=0)
    await tb.commit(0, source=0, peer_idx=first_peer)
    await tb.wait_claim()
    await tb.admit(0, source=0)
    assert int(dut.fifo_level.value) == 1
    assert int(dut.reserved_count.value) == 1

    old_head = tb.claim()
    handshake = await tb.cycle(
        commits={0: (0, second_peer)},
        complete=old_head,
    )
    assert handshake["commit_ready"] & 1
    assert handshake["complete_hwclr"] == 1
    assert int(dut.fifo_level.value) == 1
    assert int(dut.reserved_count.value) == 0
    await tb.wait_claim()
    assert tb.claim() == (second_peer, 0, 1 & tb.sequence_mask)


@cocotb.test()
async def test_sequence_wrap_and_reset(dut):
    """Sequence numbers wrap modulo their width; reset clears all state."""
    tb = TB(dut)
    await tb.reset()
    tb.enables = 0x01

    if tb.sequence_w <= 8:
        for sequence in range((1 << tb.sequence_w) + 2):
            await tb.admit(0, source=0)
            await tb.commit(0, source=0, peer_idx=0)
            await tb.wait_claim()
            assert tb.claim() == (0, 0, sequence & tb.sequence_mask)
            await tb.complete_claim()

    # Populate every class of state that reset is required to clear.
    await tb.admit(0, source=0)
    await tb.commit(0, source=0, peer_idx=1)
    if tb.depth > 1:
        await tb.admit(0, source=0)
    await tb.cycle(complete=(0, 0, 1))
    await tb.cycle(commits={0: (0, 0)})
    await tb.cycle(commits={0: (0, 0)})
    assert int(dut.claim_valid.value) == 1
    assert int(dut.invalid_complete.value) == 1
    assert int(dut.overflow.value) == 1

    await tb.reset()
    tb.enables = 0x01
    await tb.admit(0, source=0)
    await tb.commit(0, source=0, peer_idx=0)
    await tb.wait_claim()
    assert tb.claim() == (0, 0, 0)


tests_dir = os.path.dirname(__file__)
repo_dir = os.path.abspath(os.path.join(tests_dir, "..", "..", ".."))
core_dir = os.path.join(repo_dir, "hw", "rtl", "core")
taxi_axis_dir = os.path.join(repo_dir, "libs", "taxi", "src", "axis", "rtl")
common_dir = os.path.abspath(os.path.join(tests_dir, "..", "..", "common"))


@pytest.mark.parametrize(
    "event_ports,fifo_depth,peer_idx_w,sequence_w",
    [
        (1, 1, 1, 4),
        (2, 3, 3, 4),
        (4, 4, 5, 4),
        (5, 7, 11, 5),
        (4, 260, 11, 8),
    ],
)
def test_openenoc_endpoint_irq_controller(
    request,
    event_ports,
    fifo_depth,
    peer_idx_w,
    sequence_w,
):
    module = os.path.splitext(os.path.basename(__file__))[0]
    parameters = {
        "EVENT_PORTS": event_ports,
        "FIFO_DEPTH": fifo_depth,
        "PEER_IDX_W": peer_idx_w,
        "SEQUENCE_W": sequence_w,
    }
    extra_env = {f"PARAM_{key}": str(value) for key, value in parameters.items()}
    sim_build = os.path.join(
        tests_dir,
        "sim_build",
        request.node.name.replace("[", "-").replace("]", ""),
    )

    cocotb_test.simulator.run(
        simulator="verilator",
        python_search=[tests_dir],
        verilog_sources=[
            os.path.join(taxi_axis_dir, "taxi_axis_if.sv"),
            os.path.join(taxi_axis_dir, "taxi_axis_fifo.sv"),
            os.path.join(tests_dir, f"{module}.sv"),
            os.path.join(core_dir, "openenoc_irq_event_if.sv"),
            os.path.join(core_dir, "openenoc_rr_arbiter.sv"),
            os.path.join(core_dir, "openenoc_endpoint_irq_controller.sv"),
        ],
        toplevel=module,
        module=module,
        parameters=parameters,
        extra_args=[os.path.join(common_dir, "config.vlt")],
        sim_build=sim_build,
        extra_env=extra_env,
    )
