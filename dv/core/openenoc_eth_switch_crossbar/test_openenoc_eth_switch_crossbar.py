# SPDX-FileCopyrightText: 2026 Kerim Bavcic
# SPDX-License-Identifier: AGPL-3.0-or-later

import itertools
import os

import cocotb
import cocotb_test.simulator
import pytest
from cocotb.clock import Clock
from cocotb.regression import TestFactory
from cocotb.triggers import RisingEdge, SimTimeoutError, Timer, with_timeout
from cocotbext.axi import AxiStreamBus, AxiStreamFrame, AxiStreamSink, AxiStreamSource

TestFactory.__test__ = False
MANAGED, UNMANAGED = 1, 0
WORD_MAC_LO, WORD_MAC_HI, WORD_IFACE, WORD_CONFIG = range(4)
ALL_BITS = 0xFFFFFFFF

# ----------------------------------------------------------------------
# Helper functions for test frame generation
# ----------------------------------------------------------------------

def ethernet_frame(da, sa, payload, ether_type=None):
    header = da.to_bytes(6, "big") + sa.to_bytes(6, "big")
    if ether_type is not None:
        header += ether_type.to_bytes(2, "big")
    return header + bytes(payload)

def cycle_pause(pattern=(1, 1, 0, 0, 0)):
    return itertools.cycle(pattern)

def factory_payload_lengths():
    return [0, 1, 3, 16, 47, 128]

def incrementing_payload(length):
    return bytes(itertools.islice(itertools.cycle(range(256)), length))


def field(value, index, width):
    return (int(value) >> (index * width)) & ((1 << width) - 1)

class TB:
    def __init__(self, dut):
        self.dut = dut
        self.num_ports = int(os.environ.get("PARAM_NUM_OF_INTERFACES", 4))
        self.table_depth = int(os.environ.get("PARAM_TABLE_DEPTH", 8))
        self.index_w = (self.num_ports - 1).bit_length()
        self.mask = (1 << self.num_ports) - 1

        cocotb.start_soon(Clock(dut.clk, 10, units="ns").start())

        self.sources = [
            AxiStreamSource(
                AxiStreamBus.from_entity(bus),
                dut.clk,
                dut.rst,
            )
            for bus in dut.port_rx_axis_if
        ]

        self.sinks = [
            AxiStreamSink(
                AxiStreamBus.from_entity(bus),
                dut.clk,
                dut.rst,
            )
            for bus in dut.port_tx_axis_if
        ]
        self.monitor_enabled = False
        self.clear_observations()
        self.monitor_task = cocotb.start_soon(self.monitor())

    def clear_observations(self):
        self.outstanding = [{}, {}]
        self.active = [None, None]
        self.pointer = [0, 0]
        self.requests = [[0] * self.num_ports for _ in range(2)]
        self.responses = [[0] * self.num_ports for _ in range(2)]
        self.launch_order = [[], []]
        self.max_simultaneous_requests = [0, 0]
        self.concurrent_channels = False
        self.parallel_transfers = 0
        self.previous_table_req = 0

    async def monitor(self):
        """Passive pre-edge protocol checks; real engines/table drive all traffic."""
        d, n = self.dut, self.num_ports
        while True:
            await RisingEdge(d.clk)
            if not self.monitor_enabled:
                continue
            if int(d.rst.value):
                self.clear_observations()
                continue

            req = int(d.table_req.value)
            assert not (req & self.previous_table_req), "downstream req must be a strobe"
            self.previous_table_req = req
            self.concurrent_channels |= int(d.arb_busy.value) == 3
            transfers = int(d.forwarding_tvalid.value) & int(d.forwarding_tready.value)
            self.parallel_transfers += transfers.bit_count() > 1
            for port in range(n):
                assert field(d.engine_tid.value, port, self.index_w) == port

            for channel in range(2):
                requests = field(d.source_req.value, channel, n)
                acks = field(d.source_ack.value, channel, n)
                self.max_simultaneous_requests[channel] = max(
                    self.max_simultaneous_requests[channel], requests.bit_count()
                )
                # Check the RR choice against the pre-launch pending snapshot.
                if int(d.arb_launch.value) & (1 << channel):
                    pending = field(d.arb_pending.value, channel, n)
                    expected = next(
                        (self.pointer[channel] + offset) % n
                        for offset in range(n)
                        if pending & (1 << ((self.pointer[channel] + offset) % n))
                    )
                    selected = field(d.arb_selected.value, channel, self.index_w)
                    assert selected == expected, (channel, pending, selected, expected)
                    self.pointer[channel] = (selected + 1) % n
                    self.launch_order[channel].append(selected)

                for port in range(n):
                    if requests & (1 << port):
                        assert port not in self.outstanding[channel], "request overwritten"
                        mac = field(d.source_mac.value, channel * n + port, 48)
                        bitmap = field(d.learning_bitmap.value, port, n) if channel else None
                        self.outstanding[channel][port] = (mac, bitmap)
                        self.requests[channel][port] += 1

                if req & (1 << channel):
                    assert self.active[channel] is None, "second downstream request before ack"
                    owner = field(d.arb_owner.value, channel, self.index_w)
                    assert owner in self.outstanding[channel]
                    mac, bitmap = self.outstanding[channel][owner]
                    assert field(d.table_mac.value, channel, 48) == mac
                    if channel:
                        assert int(d.table_learning_bitmap.value) == bitmap
                        assert bitmap == 1 << owner
                    self.active[channel] = owner

                if int(d.table_ack.value) & (1 << channel):
                    owner = self.active[channel]
                    assert owner is not None, "unsolicited table response"
                    assert acks == 1 << owner, "response routed to wrong source"
                    if channel == 0:
                        assert field(d.lookup_bitmap.value, owner, n) == int(d.table_lookup_bitmap.value)
                    del self.outstanding[channel][owner]
                    self.responses[channel][owner] += 1
                    self.active[channel] = None
                else:
                    assert acks == 0, "source ack without table ack"

            if int(d.pause_done.value):
                assert int(d.engine_pause_done.value) == self.mask
                assert not any(self.outstanding)
                assert int(d.arb_busy.value) == 0

    def set_idle_generator(self, generator=None):
        if generator:
            for source in self.sources:
                source.set_pause_generator(generator())

    def set_backpressure_generator(self, generator=None):
        if generator:
            for sink in self.sinks:
                sink.set_pause_generator(generator())

    async def cycle(self, count=1):
        for _ in range(count):
            await RisingEdge(self.dut.clk)
            await Timer(1, units="ns")

    async def wait_asserted(self, signal, description, timeout_cycles=10000):
        for _ in range(timeout_cycles):
            if int(signal.value):
                return
            await self.cycle()
        raise AssertionError(f"timeout waiting for {description}")

    async def reset(self, operation_mode=MANAGED, default_forwarding=0):
        d = self.dut
        self.monitor_enabled = False
        d.rst.value = 0
        d.operation_mode.value = operation_mode
        d.default_forwarding.value = default_forwarding
        for name in ("pause_request", "cpuif_req", "cpuif_addr", "cpuif_req_is_wr",
                     "cpuif_wr_data", "cpuif_wr_biten"):
            getattr(d, name).value = 0
        await self.cycle(3)
        d.rst.value = 1
        self.monitor_enabled = True
        await self.cycle(4)
        # Agents can observe residual traffic before reset when the preceding
        # cocotb case failed mid-frame. Do not carry it into the next case.
        for source in self.sources:
            source.clear()
        for sink in self.sinks:
            sink.clear()
        d.rst.value = 0
        await self.cycle(6)

    async def set_pause(self, paused):
        self.dut.pause_request.value = int(paused)
        if paused:
            await self.wait_asserted(self.dut.pause_done, "pause_done")
        else:
            await self.cycle(2)
            assert not int(self.dut.pause_done.value)

    async def cpu_write(self, index, word, data, biten=ALL_BITS):
        d = self.dut
        d.cpuif_addr.value = index * 16 + word * 4
        d.cpuif_req_is_wr.value = 1
        d.cpuif_wr_data.value = data
        d.cpuif_wr_biten.value = biten
        d.cpuif_req.value = 1

        await self.cycle()
        d.cpuif_req.value = 0
        d.cpuif_addr.value = 0
        d.cpuif_req_is_wr.value = 0
        d.cpuif_wr_data.value = 0
        d.cpuif_wr_biten.value = 0

        await self.wait_asserted(d.cpuif_wr_ack, "cpuif_wr_ack")

        assert not int(d.cpuif_rd_ack.value)
        await self.cycle()

    async def cpu_read(self, index, word):
        d = self.dut
        d.cpuif_addr.value = index * 16 + word * 4
        d.cpuif_req_is_wr.value = 0
        d.cpuif_req.value = 1

        await self.cycle()
        d.cpuif_req.value = 0
        d.cpuif_addr.value = 0

        await self.wait_asserted(d.cpuif_rd_ack, "cpuif_rd_ack")
        
        assert not int(d.cpuif_wr_ack.value)
        data = int(d.cpuif_rd_data.value)
        await self.cycle()

        return data

    async def cpu_write_entry(self, index, mac, bitmap, enabled=True):
        for word, value in enumerate((mac & ALL_BITS, mac >> 32, bitmap, int(enabled))):
            await self.cpu_write(index, word, value)

    async def cpu_read_entry(self, index):
        words = [await self.cpu_read(index, word) for word in range(4)]
        return ((words[1] << 32) | words[0], words[2], words[3])

    async def program(self, entries):
        await self.set_pause(True)
        for index, (mac, bitmap) in enumerate(entries):
            await self.cpu_write_entry(index, mac, bitmap)
        await self.set_pause(False)

    async def send(self, port, data, tdest=0x5A, tid=0):
        frame = AxiStreamFrame(data)
        frame.tid, frame.tdest, frame.tuser = tid, tdest, 0
        await self.sources[port].send(frame)

    async def send_all(self, port, frames, tdest=0x5A, tid=0):
        for frame in frames:
            await self.send(port, frame, tdest, tid)

    async def recv(self, port, timeout_us=100):
        try:
            return await with_timeout(self.sinks[port].recv(), timeout_us, "us")
        except SimTimeoutError:
            self.dut._log.error(
                "port %d timeout: ingress=%s/%s forwarding=%s/%s egress=%s/%s pending=%s busy=%s",
                port, self.dut.ingress_tvalid.value, self.dut.ingress_tready.value,
                self.dut.forwarding_tvalid.value, self.dut.forwarding_tready.value,
                self.dut.egress_tvalid.value, self.dut.egress_tready.value,
                self.dut.arb_pending.value, self.dut.arb_busy.value,
            )
            raise

    async def check_frame(self, port, data, tid=None, tdest=0x5A, timeout_us=200):
        frame = await self.recv(port, timeout_us)
        assert bytes(frame.tdata) == bytes(data)
        assert int(frame.tdest) == tdest
        if tid is not None:
            assert int(frame.tid) == tid

    async def check_empty(self, cycles=30):
        await self.cycle(cycles)
        assert all(sink.empty() for sink in self.sinks), "unexpected egress frame"
        assert not any(self.outstanding), "lost or unfinished forwarding request"
        assert self.requests == self.responses

    async def assert_only_ports_received(self, ports, data, expected_tdest=0x5A, expected_tid=None):
        for port in ports:
            await self.check_frame(port, data, expected_tid, expected_tdest)
        await self.check_empty()

    async def assert_no_ingress_idle_between_frames(self, port, frame_count):
        axis = self.dut.port_rx_axis_if[port]
        completed, expect_next = 0, False
        while completed < frame_count:
            await self.cycle()
            if expect_next:
                assert int(axis.tvalid.value), "source inserted an inter-frame idle cycle"
                expect_next = False
            if int(axis.tvalid.value) and int(axis.tready.value) and int(axis.tlast.value):
                completed += 1
                expect_next = completed < frame_count

# ----------------------------------------------------------------------
# Standalone cocotb test cases: simple routing and forwarding scenarios
# ----------------------------------------------------------------------

@cocotb.test()
async def test_default_forwarding(dut):
    tb = TB(dut)
    await tb.reset(default_forwarding=0b0010)
    data = ethernet_frame(0x001122334455, 0x102030405060, range(32))
    await tb.send(0, data)
    await tb.assert_only_ports_received({1}, data)


@cocotb.test()
async def test_managed_multicast_hit(dut):
    tb = TB(dut)
    await tb.reset()
    da = 0xAABBCCDDEEFF
    await tb.program([(da, 0b1100)])
    data = ethernet_frame(da, 0x020000000001, range(48))
    await tb.send(0, data, tdest=0x33)
    await tb.assert_only_ports_received({2, 3}, data, expected_tdest=0x33)


@cocotb.test()
async def test_unmanaged_learning(dut):
    tb = TB(dut)
    await tb.reset(UNMANAGED, 0b0010)
    learned = 0x0A0B0C0D0E0F
    first = ethernet_frame(0xFFFFFFFFFFFF, learned, b"learn-this-source" * 2)
    await tb.send(0, first)
    await tb.assert_only_ports_received({1}, first)
    second = ethernet_frame(learned, 0x112233445566, b"lookup-the-learned-source" * 2)
    await tb.send(1, second)
    await tb.assert_only_ports_received({0}, second)


@cocotb.test()
async def test_ingress_port_suppression(dut):
    tb = TB(dut)
    await tb.reset()
    da = 0x123456789ABC
    await tb.program([(da, 0b0011)])
    data = ethernet_frame(da, 0x665544332211, range(24))
    await tb.send(0, data)
    await tb.assert_only_ports_received({1}, data)


@cocotb.test()
async def test_ingress_overwrites_source_tid(dut):
    """Equivalent to shared-bus UPDATE_TID, now before each engine."""
    tb = TB(dut)
    await tb.reset()
    da = 0x223344556677
    await tb.program([(da, 0b1111)])
    data = ethernet_frame(da, 0x102030405060, b"ingress-must-replace-source-tid")
    await tb.send(2, data, tid=0)
    await tb.assert_only_ports_received({0, 1, 3}, data, expected_tid=2)


@cocotb.test()
async def test_round_robin_between_active_ingresses(dut):
    """RR on table transactions; independent frames need not alternate."""
    tb = TB(dut)
    await tb.reset()
    destinations = [0x300000000001, 0x300000000002]
    await tb.set_pause(True)
    for port, da in enumerate(destinations):
        await tb.cpu_write_entry(port, da, 1 << (port + 2))
    frames = [[ethernet_frame(destinations[p], 0x400000000001 + p, bytes([i+p*2])*40)
               for i in range(2)] for p in range(2)]
    for port in range(2):
        await tb.send_all(port, frames[port], tid=3)
    await tb.cycle(12)
    await tb.set_pause(False)
    for port in range(2):
        for data in frames[port]:
            await tb.check_frame(port+2, data, port)
    await tb.check_empty()
    # The monitor checks every grant against its pending set and RR pointer.
    for channel in range(2):
        assert tb.responses[channel][:2] == [2, 2]
        assert set(tb.launch_order[channel]) == {0, 1}
    assert tb.max_simultaneous_requests[0] == 2


@cocotb.test()
async def test_zero_bitmap_drops_frame(dut):
    tb = TB(dut)
    await tb.reset()
    await tb.send(3, ethernet_frame(0x500000000001, 0x500000000002, b"must-be-dropped"))
    await tb.check_empty(300)


@cocotb.test()
async def test_incomplete_destination_address_drops_frame(dut):
    tb = TB(dut)
    await tb.reset(default_forwarding=0b0010)
    da = (0x504000000001).to_bytes(6, "big")
    await tb.send_all(0, [da[:length] for length in range(1, 6)])
    await tb.check_empty(300)
    assert sum(tb.requests[0]) == 0


@cocotb.test()
async def test_incomplete_ethernet_header_drops_frame(dut):
    tb = TB(dut)
    await tb.reset()
    da = 0x505000000001
    await tb.program([(da, 0b0010)])
    header = ethernet_frame(da, 0x505000000002, b"")
    await tb.send_all(0, [header[:length] for length in range(6, 12)])
    await tb.check_empty(500)
    assert tb.responses[0][0] == 6
    assert sum(tb.requests[1]) == 0


@cocotb.test()
async def test_header_only_and_unaligned_frames(dut):
    tb = TB(dut)
    await tb.reset()
    da = 0x510000000001
    await tb.program([(da, 0b0010)])
    frames = [ethernet_frame(da, 0x510000000002, range(length)) for length in (0, 1, 2, 3, 5, 17, 65)]
    await tb.send_all(0, frames)
    for data in frames:
        await tb.check_frame(1, data, 0)
    await tb.check_empty()


@cocotb.test()
async def test_back_to_back_frame_burst(dut):
    tb = TB(dut)
    await tb.reset()
    da = 0x520000000001
    await tb.program([(da, 0b0100)])
    frames = [ethernet_frame(da, 0x520000000100+i, bytes([i])*(20+i*7)) for i in range(12)]
    await tb.send_all(1, frames, tdest=0x44, tid=3)
    for data in frames:
        await tb.check_frame(2, data, 1, 0x44)
    await tb.check_empty()


@cocotb.test()
async def test_no_idle_cycle_between_back_to_back_frames(dut):
    tb = TB(dut)
    await tb.reset(default_forwarding=0b0010)
    frames = [ethernet_frame(0x521000000001, 0x521000000100+i, bytes([0xA0+i])*(65+i*7))
              for i in range(4)]
    task = cocotb.start_soon(tb.assert_no_ingress_idle_between_frames(0, len(frames)))
    await tb.send_all(0, frames, tdest=0x46, tid=3)
    await with_timeout(task, 200, "us")
    for data in frames:
        await tb.check_frame(1, data, 0, 0x46)
    await tb.check_empty()


@cocotb.test()
async def test_standard_and_jumbo_payloads(dut):
    tb = TB(dut)
    await tb.reset()
    da = 0x525400000001
    await tb.program([(da, 0b0100)])
    frames = [ethernet_frame(da, 0x525400000100+i, incrementing_payload(length), 0x88B5)
              for i, length in enumerate((1500, 9000))]
    assert [len(data) for data in frames] == [1514, 9014]
    await tb.send_all(0, frames, tdest=0x45, tid=3)
    for data in frames:
        await tb.check_frame(2, data, 0, 0x45)
    await tb.check_empty()


@cocotb.test()
async def test_all_ingress_ports_simultaneously(dut):
    tb = TB(dut)
    await tb.reset()
    await tb.set_pause(True)
    frames = []
    for port in range(tb.num_ports):
        da = 0x530000000000 + port
        await tb.cpu_write_entry(port, da, 1 << ((port+1) % tb.num_ports))
        frames.append([ethernet_frame(da, 0x540000000000+port, bytes([port, seq])*(20+seq))
                       for seq in range(3)])
        await tb.send_all(port, frames[-1], tid=(port+2) % tb.num_ports)
    await tb.cycle(20)
    await tb.set_pause(False)
    for port in range(tb.num_ports):
        for data in frames[port]:
            await tb.check_frame((port+1) % tb.num_ports, data, port)
    await tb.check_empty()
    assert tb.requests == [[3]*tb.num_ports, [3]*tb.num_ports]
    assert tb.max_simultaneous_requests[0] == tb.num_ports
    assert tb.concurrent_channels


@cocotb.test()
async def test_unmanaged_mac_moves_to_new_port(dut):
    tb = TB(dut)
    await tb.reset(UNMANAGED, 0b1000)
    mac, da = 0x550000000001, 0x550000000002
    for port, payload in ((0, b"first-location"), (2, b"new-location")):
        data = ethernet_frame(da, mac, payload)
        await tb.send(port, data)
        await tb.assert_only_ports_received({3}, data)
    data = ethernet_frame(mac, 0x550000000003, b"use-updated-location")
    await tb.send(1, data)
    await tb.assert_only_ports_received({2}, data, expected_tid=1)


@cocotb.test()
async def test_multicast_with_output_backpressure(dut):
    tb = TB(dut)
    await tb.reset()
    da = 0x560000000001
    await tb.program([(da, 0b1100)])
    tb.sinks[2].set_pause_generator(cycle_pause((1, 0, 0, 0)))
    tb.sinks[3].set_pause_generator(cycle_pause((1, 1, 1, 0, 0)))
    frames = [ethernet_frame(da, 0x560000000100+i, bytes([i])*(80+i*13)) for i in range(8)]
    await tb.send_all(0, frames, tdest=0x66)
    for data in frames:
        for port in (2, 3):
            await tb.check_frame(port, data, 0, 0x66)
    await tb.check_empty()


@cocotb.test()
async def test_managed_table_cpu_readback(dut):
    tb = TB(dut)
    await tb.reset()
    index, mac, bitmap = tb.table_depth-1, 0x570000000001, (1 << (tb.num_ports-1)) | 1
    await tb.set_pause(True)
    await tb.cpu_write_entry(index, mac, bitmap)
    assert await tb.cpu_read_entry(index) == (mac, bitmap, 1)
    await tb.set_pause(False)


@cocotb.test()
async def test_pause_completes_current_frame_and_blocks_next(dut):
    tb = TB(dut)
    await tb.reset()
    da = 0x580000000001
    await tb.program([(da, 0b0010)])
    first = ethernet_frame(da, 0x580000000002, bytes(range(256))*2)
    second = ethernet_frame(da, 0x580000000003, b"held-until-resume"*4)
    await tb.send_all(0, [first, second])
    for _ in range(10000):
        await RisingEdge(dut.clk)
        if int(dut.ingress_tvalid.value) & int(dut.ingress_tready.value) & ~int(dut.ingress_tlast.value) & 1:
            break
    else:
        raise AssertionError("timeout waiting for first frame at engine input")
    dut.pause_request.value = 1
    await tb.wait_asserted(dut.pause_done, "mid-frame pause_done")
    await tb.check_frame(1, first, 0)
    await tb.check_empty()
    assert int(dut.pause_done.value)
    await tb.set_pause(False)
    await tb.check_frame(1, second, 0)
    await tb.check_empty()

# ------------------------------------------------------------------------------
# Crossbar-specific cocotb test cases: simple routing and forwarding scenarios
# ------------------------------------------------------------------------------

@cocotb.test()
async def test_parallel_disjoint_paths(dut):
    tb = TB(dut)
    await tb.reset()
    await tb.set_pause(True)
    frames = []
    for port in (0, 1):
        da = 0x700000000000 + port
        await tb.cpu_write_entry(port, da, 1 << (port+2))
        frames.append(ethernet_frame(da, 0x710000000000+port, bytes([port])*4096))
        await tb.send(port, frames[-1])
    await tb.cycle(20)
    await tb.set_pause(False)
    for port in (0, 1):
        await tb.check_frame(port+2, frames[port], port)
    await tb.check_empty()
    assert tb.parallel_transfers > 0, "independent paths never transferred concurrently"


@cocotb.test()
async def test_contending_ingresses(dut):
    tb = TB(dut)
    await tb.reset(default_forwarding=0b1000)
    tb.sinks[3].set_pause_generator(cycle_pause())
    frames = {p: [ethernet_frame(0x720000000001, 0x720000000010+p,
                                bytes([p, seq])*150) for seq in range(3)] for p in (0, 1, 2)}
    for port in frames:
        await tb.send_all(port, frames[port])
    indices = dict.fromkeys(frames, 0)
    for _ in range(9):
        frame = await tb.recv(3)
        port = int(frame.tid)
        assert port in frames
        assert indices[port] < 3
        assert bytes(frame.tdata) == frames[port][indices[port]]
        assert int(frame.tdest) == 0x5A
        indices[port] += 1
    assert list(indices.values()) == [3, 3, 3]
    await tb.check_empty()


@cocotb.test()
async def test_concurrent_learning_and_cpu_reads(dut):
    """Both RR channels work with finite CPU contention; all learned MACs survive."""
    tb = TB(dut)
    await tb.reset(UNMANAGED, 0b1000)
    await tb.set_pause(True)
    frames = [ethernet_frame(0x730000000001, 0x730000000010+p, bytes([p])*80) for p in range(3)]
    for port, frame in enumerate(frames):
        await tb.send(port, frame)
    await tb.cycle(20)
    await tb.set_pause(False)
    for _ in range(12):
        await tb.cpu_read(tb.table_depth-1, WORD_CONFIG)
    received = set()
    for _ in range(3):
        frame = await tb.recv(3)
        port = int(frame.tid)
        assert port not in received and port < 3
        assert bytes(frame.tdata) == frames[port]
        received.add(port)
    await tb.check_empty()
    assert tb.concurrent_channels
    await tb.set_pause(True)
    entries = [await tb.cpu_read_entry(i) for i in range(tb.table_depth)]
    for port in range(3):
        assert (0x730000000010+port, 1 << port, 1) in entries
    await tb.set_pause(False)
    for port in range(3):
        data = ethernet_frame(0x730000000010+port, 0x730000000020, b"learned-route")
        await tb.send(3, data)
        await tb.assert_only_ports_received({port}, data, expected_tid=3)


@cocotb.test()
async def test_pause_multiple_active_engines(dut):
    tb = TB(dut)
    await tb.reset()
    await tb.set_pause(True)
    frames = []
    for port in (0, 1):
        da = 0x740000000000 + port
        await tb.cpu_write_entry(port, da, 1 << (port+2))
        frames.append([ethernet_frame(da, 0x740000000010+port, bytes([port])*2048),
                       ethernet_frame(da, 0x740000000010+port, b"after-resume")])
        await tb.send_all(port, frames[-1])
    await tb.cycle(20)
    await tb.set_pause(False)
    seen = 0
    for _ in range(10000):
        await RisingEdge(dut.clk)
        seen |= int(dut.ingress_tvalid.value) & int(dut.ingress_tready.value) & 3
        if seen == 3:
            break
    else:
        raise AssertionError("both engines did not start")
    dut.pause_request.value = 1
    await tb.wait_asserted(dut.pause_done, "all engines paused")
    for port in (0, 1):
        await tb.check_frame(port+2, frames[port][0], port)
    await tb.check_empty()
    await tb.set_pause(False)
    for port in (0, 1):
        await tb.check_frame(port+2, frames[port][1], port)
    await tb.check_empty()


@cocotb.test()
async def test_reset_pending_transactions(dut):
    tb = TB(dut)
    await tb.reset(default_forwarding=0b1000)
    await tb.set_pause(True)
    for port in range(3):
        await tb.send(port, ethernet_frame(0x750000000001, 0x750000000010+port, bytes([port])*256))
    await tb.cycle(20)
    await tb.set_pause(False)
    await tb.wait_asserted(dut.arb_pending, "queued table requests")
    # Reset immediately: do not wait for normal transaction completion.
    dut.rst.value = 1
    await tb.cycle(6)
    for source in tb.sources:
        source.clear()
    for sink in tb.sinks:
        sink.clear()
    dut.rst.value = 0
    await tb.cycle(20)
    await tb.check_empty()
    data = ethernet_frame(0x750000000002, 0x750000000020, b"fresh-after-reset")
    await tb.send(1, data)
    await tb.assert_only_ports_received({3}, data, expected_tid=1)
    assert tb.responses == [[0, 1] + [0]*(tb.num_ports-2)] * 2


@cocotb.test()
async def test_overlapping_multicast_routes(dut):
    tb = TB(dut)
    await tb.reset()
    destinations = [0x760000000001, 0x760000000002]
    # Source 0 -> {2,3}; source 1 -> {0,3}. Output 3 is contested.
    await tb.program(list(zip(destinations, (0b1100, 0b1001))))
    tb.sinks[2].set_pause_generator(cycle_pause((1, 0, 0)))
    tb.sinks[3].set_pause_generator(cycle_pause((1, 1, 0, 0, 0)))
    frames = [[ethernet_frame(destinations[p], 0x760000000010+p, bytes([p, i])*120)
               for i in range(3)] for p in (0, 1)]
    for port in (0, 1):
        await tb.send_all(port, frames[port])
    for src, dst in ((0, 2), (1, 0)):
        for data in frames[src]:
            await tb.check_frame(dst, data, src)
    indices = [0, 0]
    for _ in range(6):
        frame = await tb.recv(3)
        src = int(frame.tid)
        assert src in (0, 1) and indices[src] < 3
        assert bytes(frame.tdata) == frames[src][indices[src]]
        indices[src] += 1
    assert indices == [3, 3]
    await tb.check_empty()

# ----------------------------------------------------------------------
# TestFactory logic: idle and backpressure combinations
# ----------------------------------------------------------------------

async def run_factory_routing(
    dut,
    route_case=None,
    payload_lengths=None,
    payload_data=None,
    idle_inserter=None,
    backpressure_inserter=None,
):
    tb = TB(dut)
    await tb.reset()
    ingress, bitmap, da = route_case
    ports = [p for p in range(tb.num_ports) if bitmap & ~(1 << ingress) & (1 << p)]
    await tb.program([(da, bitmap)])
    tb.set_idle_generator(idle_inserter)
    tb.set_backpressure_generator(backpressure_inserter)
    frames = [ethernet_frame(da, 0x600000000000+ingress, payload_data(length))
              for length in payload_lengths()]
    await tb.send_all(ingress, frames, tdest=0x70+ingress, tid=3)
    for port in ports:
        for data in frames:
            await tb.check_frame(port, data, ingress, 0x70+ingress)
    await tb.check_empty()

# ----------------------------------------------------------------------
# Dispatch: select test cases to run based on Makefile configuration
# ----------------------------------------------------------------------

if getattr(cocotb, "top", None) is not None:
    factory = TestFactory(run_factory_routing)
    factory.add_option(
        "route_case",
        [
            (0, 0b0010, 0x600000000001),
            (3, 0b0011, 0x600000000002),
            (2, 0b1111, 0x600000000003),
        ],
    )
    factory.add_option("payload_lengths", [factory_payload_lengths])
    factory.add_option("payload_data", [incrementing_payload])
    factory.add_option("idle_inserter", [None, cycle_pause])
    factory.add_option("backpressure_inserter", [None, cycle_pause])
    factory.generate_tests()

# ----------------------------------------------------------------------
# PyTest framework: parameter sweep and simulator runner
# ----------------------------------------------------------------------

tests_dir = os.path.dirname(__file__)
repo_dir = os.path.abspath(os.path.join(tests_dir, "..", "..", ".."))
hw_dir = os.path.join(repo_dir, "hw")
libs_dir = os.path.join(repo_dir, "libs")
core_dir = os.path.join(hw_dir, "rtl", "core")
taxi_axis_dir = os.path.join(libs_dir, "taxi", "src", "axis", "rtl")
taxi_sync_dir = os.path.join(libs_dir, "taxi", "src", "sync", "rtl")
hal_rtl_dir = os.path.join(repo_dir, "build", "hal", "rtl")


@pytest.mark.parametrize(
    "num_interfaces,data_w,fabric_data_w,table_depth,port_fifo_depth,port_side",
    [
        (4, 8, 32, 5, 64, 0b1111),
        (5, 24, 48, 8, 48, 0b10101),
        (4, 32, 32, 8, 64, 0b0000),
        (8, 64, 16, 8, 16, 0b10101010),
    ],
)
def test_openenoc_eth_switch_crossbar(
    request,
    num_interfaces,
    data_w,
    fabric_data_w,
    table_depth,
    port_fifo_depth,
    port_side,
):
    module = os.path.splitext(os.path.basename(__file__))[0]

    verilog_sources = [
        os.path.join(taxi_axis_dir, "taxi_axis_if.sv"),
        os.path.join(taxi_axis_dir, "taxi_axis_register.sv"),
        os.path.join(taxi_axis_dir, "taxi_axis_pipeline_register.sv"),
        os.path.join(taxi_axis_dir, "taxi_axis_adapter.sv"),
        os.path.join(taxi_axis_dir, "taxi_axis_async_fifo.sv"),
        os.path.join(taxi_axis_dir, "taxi_axis_async_fifo_adapter.sv"),
        os.path.join(taxi_sync_dir, "taxi_sync_reset.sv"),
        os.path.join(taxi_sync_dir, "taxi_sync_signal.sv"),
        os.path.join(hal_rtl_dir, "openenoc_switch_if.sv"),
        os.path.join(core_dir, "openenoc_eth_if.sv"),
        os.path.join(core_dir, "openenoc_lookup_if.sv"),
        os.path.join(core_dir, "openenoc_learning_if.sv"),
        os.path.join(core_dir, "openenoc_rr_arbiter.sv"),
        os.path.join(core_dir, "openenoc_forwarding_table_arb_mux.sv"),
        os.path.join(core_dir, "openenoc_axis_forwarding_engine.sv"),
        os.path.join(core_dir, "openenoc_forwarding_table.sv"),
        os.path.join(core_dir, "openenoc_axis_switch.sv"),
        os.path.join(core_dir, "openenoc_eth_switch_crossbar.sv"),
        os.path.join(tests_dir, f"{module}.sv"),
    ]

    parameters = {
        "NUM_OF_INTERFACES": num_interfaces,
        "TABLE_DEPTH": table_depth,
        "DATA_W": data_w,
        "KEEP_W": data_w // 8,
        "KEEP_EN": int(data_w > 8),
        "FABRIC_DATA_W": fabric_data_w,
        "PORT_FIFO_DEPTH": port_fifo_depth,
        "PORT_SIDE": port_side,
    }
    cocotb_test.simulator.run(
        simulator="verilator",
        python_search=[tests_dir],
        verilog_sources=verilog_sources,
        toplevel=module,
        module=module,
        parameters=parameters,
        sim_build=os.path.join(
            tests_dir,
            "sim_build",
            request.node.name.replace("[", "-").replace("]", ""),
        ),
        extra_env={f"PARAM_{key}": str(value) for key, value in parameters.items()},
        extra_args=[
            "-Wall",
            "-Wno-DECLFILENAME",
            os.path.join(repo_dir, "dv", "common", "config.vlt"),
        ],
    )