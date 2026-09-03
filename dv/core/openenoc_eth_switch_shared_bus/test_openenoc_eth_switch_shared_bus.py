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

MANAGED = 1
UNMANAGED = 0

WORD_MAC_LO = 0
WORD_MAC_HI = 1
WORD_IFACE = 2
WORD_CONFIG = 3
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

class TB:
    def __init__(self, dut):
        self.dut = dut
        self.num_ports = int(os.environ.get("PARAM_NUM_OF_INTERFACES", 4))
        self.table_depth = int(os.environ.get("PARAM_TABLE_DEPTH", 8))

        cocotb.start_soon(Clock(dut.clk, 10, units="ns").start())

        # The wrapper exposes constant-index bridges around the nested eth_if
        # array because Verilator cannot reliably address its members from VPI.
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
        dut = self.dut

        dut.rst.setimmediatevalue(0)
        dut.operation_mode.setimmediatevalue(operation_mode)
        dut.pause_request.setimmediatevalue(0)
        dut.default_forwarding.setimmediatevalue(default_forwarding)
        dut.cpuif_req.setimmediatevalue(0)
        dut.cpuif_addr.setimmediatevalue(0)
        dut.cpuif_req_is_wr.setimmediatevalue(0)
        dut.cpuif_wr_data.setimmediatevalue(0)
        dut.cpuif_wr_biten.setimmediatevalue(0)

        await self.cycle(3)
        dut.rst.value = 1
        await self.cycle(4)
        dut.rst.value = 0
        await self.cycle(6)

    async def set_pause(self, paused):
        self.dut.pause_request.value = int(paused)

        if paused:
            await self.wait_asserted(self.dut.pause_done, "pause_done")
        else:
            await self.cycle(2)
            assert not int(self.dut.pause_done.value)

    async def cpu_write(self, index, word, data, biten=ALL_BITS):
        dut = self.dut

        dut.cpuif_addr.value = index * 16 + word * 4
        dut.cpuif_req_is_wr.value = 1
        dut.cpuif_wr_data.value = data
        dut.cpuif_wr_biten.value = biten
        dut.cpuif_req.value = 1

        await self.cycle()
        dut.cpuif_req.value = 0
        dut.cpuif_addr.value = 0
        dut.cpuif_req_is_wr.value = 0
        dut.cpuif_wr_data.value = 0
        dut.cpuif_wr_biten.value = 0

        await self.wait_asserted(dut.cpuif_wr_ack, "cpuif_wr_ack")

        assert not int(dut.cpuif_rd_ack.value)
        await self.cycle()

    async def cpu_read(self, index, word):
        dut = self.dut

        dut.cpuif_addr.value = index * 16 + word * 4
        dut.cpuif_req_is_wr.value = 0
        dut.cpuif_req.value = 1

        await self.cycle()
        dut.cpuif_req.value = 0
        dut.cpuif_addr.value = 0

        await self.wait_asserted(dut.cpuif_rd_ack, "cpuif_rd_ack")

        assert not int(dut.cpuif_wr_ack.value)
        data = int(dut.cpuif_rd_data.value)
        await self.cycle()

        return data

    async def cpu_write_entry(self, index, mac, bitmap, enabled=True):
        await self.cpu_write(index, WORD_MAC_LO, mac & 0xFFFFFFFF)
        await self.cpu_write(index, WORD_MAC_HI, (mac >> 32) & 0xFFFF)
        await self.cpu_write(index, WORD_IFACE, bitmap)
        await self.cpu_write(index, WORD_CONFIG, int(enabled))

    async def cpu_read_entry(self, index):
        mac_lo = await self.cpu_read(index, WORD_MAC_LO)
        mac_hi = await self.cpu_read(index, WORD_MAC_HI)
        bitmap = await self.cpu_read(index, WORD_IFACE)
        enabled = await self.cpu_read(index, WORD_CONFIG)

        return ((mac_hi << 32) | mac_lo, bitmap, enabled)

    async def send(self, port, data, tdest=0x5A, tid=0):
        frame = AxiStreamFrame(data)
        frame.tid = tid
        frame.tdest = tdest
        frame.tuser = 0
        await self.sources[port].send(frame)

    async def send_all(self, port, frames, tdest=0x5A, tid=0):
        for frame in frames:
            await self.send(port, frame, tdest=tdest, tid=tid)

    async def recv(self, port, timeout_us=100):
        try:
            return await with_timeout(self.sinks[port].recv(), timeout_us, "us")
        except SimTimeoutError:
            self.dut._log.error(
                "timeout waiting for port %d: ingress valid/ready=%s/%s, "
                "arb=%s/%s, forwarding=%s/%s, egress=%s/%s",
                port,
                self.dut.ingress_tvalid.value,
                self.dut.ingress_tready.value,
                self.dut.arb_tvalid.value,
                self.dut.arb_tready.value,
                self.dut.forwarding_tvalid.value,
                self.dut.forwarding_tready.value,
                self.dut.egress_tvalid.value,
                self.dut.egress_tready.value,
            )
            raise

    async def assert_only_ports_received(
        self,
        expected_ports,
        expected_data,
        expected_tdest=0x5A,
        expected_tid=None,
    ):
        for port in expected_ports:
            frame = await self.recv(port)
            assert bytes(frame.tdata) == bytes(expected_data)
            assert int(frame.tdest) == expected_tdest
            if expected_tid is not None:
                assert int(frame.tid) == expected_tid

        await self.cycle(10)
        for port, sink in enumerate(self.sinks):
            assert sink.empty(), f"unexpected frame queued on egress port {port}"

    async def capture_arbiter_frame_order(self, frame_count):
        order = []
        at_frame_start = True

        while len(order) < frame_count:
            await RisingEdge(self.dut.clk)

            if int(self.dut.arb_tvalid.value) and int(self.dut.arb_tready.value):
                if at_frame_start:
                    order.append(int(self.dut.arb_tid.value))
                at_frame_start = bool(int(self.dut.arb_tlast.value))

        return order

    async def assert_no_ingress_idle_between_frames(self, port, frame_count):
        axis = self.dut.port_rx_axis_if[port]
        completed_frames = 0
        expect_next_frame = False

        while completed_frames < frame_count:
            await self.cycle()

            if expect_next_frame:
                assert int(axis.tvalid.value), (
                    f"ingress port {port} inserted an idle cycle after frame "
                    f"{completed_frames}"
                )
                expect_next_frame = False

            if (
                int(axis.tvalid.value)
                and int(axis.tready.value)
                and int(axis.tlast.value)
            ):
                completed_frames += 1
                expect_next_frame = completed_frames < frame_count

# ----------------------------------------------------------------------
# Standalone cocotb test cases: simple routing and forwarding scenarios
# ----------------------------------------------------------------------

@cocotb.test()
async def test_default_forwarding(dut):
    """An unknown destination uses the CSR default-forwarding bitmap."""
    tb = TB(dut)
    await tb.reset(operation_mode=MANAGED, default_forwarding=0b0010)

    data = ethernet_frame(
        da=0x001122334455,
        sa=0x102030405060,
        payload=range(32),
    )

    await tb.send(0, data)
    await tb.assert_only_ports_received({1}, data)


@cocotb.test()
async def test_managed_multicast_hit(dut):
    """Software programs a managed table entry and routes one frame to two ports."""
    tb = TB(dut)
    await tb.reset(operation_mode=MANAGED)

    destination = 0xAABBCCDDEEFF

    # Software pauses forwarding before modifying the managed table.
    await tb.set_pause(True)
    await tb.cpu_write_entry(0, destination, bitmap=0b1100)
    await tb.set_pause(False)

    data = ethernet_frame(
        da=destination,
        sa=0x020000000001,
        payload=bytes(range(48)),
    )

    await tb.send(0, data, tdest=0x33)
    await tb.assert_only_ports_received({2, 3}, data, expected_tdest=0x33)


@cocotb.test()
async def test_unmanaged_learning(dut):
    """A source learned on port 0 is subsequently reached from port 1."""
    tb = TB(dut)
    await tb.reset(operation_mode=UNMANAGED, default_forwarding=0b0010)

    learned_mac = 0x0A0B0C0D0E0F
    first = ethernet_frame(
        da=0xFFFFFFFFFFFF,
        sa=learned_mac,
        payload=b"learn-this-source" * 2,
    )

    await tb.send(0, first)
    await tb.assert_only_ports_received({1}, first)

    second = ethernet_frame(
        da=learned_mac,
        sa=0x112233445566,
        payload=b"lookup-the-learned-source" * 2,
    )

    await tb.send(1, second)
    await tb.assert_only_ports_received({0}, second)


@cocotb.test()
async def test_ingress_port_suppression(dut):
    """The forwarding engine removes the ingress port from the egress bitmap."""
    tb = TB(dut)
    await tb.reset(operation_mode=MANAGED)

    destination = 0x123456789ABC

    await tb.set_pause(True)
    await tb.cpu_write_entry(0, destination, bitmap=0b0011)
    await tb.set_pause(False)

    data = ethernet_frame(
        da=destination,
        sa=0x665544332211,
        payload=range(24),
    )

    # Entry selects ports 0 and 1, but port 0 is the ingress and must be removed.
    await tb.send(0, data)
    await tb.assert_only_ports_received({1}, data)


@cocotb.test()
async def test_arbiter_overwrites_source_tid(dut):
    """The arbiter replaces source tid with the physical ingress-port index."""
    tb = TB(dut)
    await tb.reset(operation_mode=MANAGED)

    destination = 0x223344556677

    await tb.set_pause(True)
    await tb.cpu_write_entry(0, destination, bitmap=0b1111)
    await tb.set_pause(False)

    data = ethernet_frame(
        da=destination,
        sa=0x102030405060,
        payload=b"arbiter-must-replace-source-tid",
    )

    # Deliberately provide tid=0 on physical port 2. UPDATE_TID must replace it
    # with 2, so forwarding suppresses port 2 rather than port 0.
    await tb.send(2, data, tid=0)
    await tb.assert_only_ports_received({0, 1, 3}, data, expected_tid=2)


@cocotb.test()
async def test_round_robin_between_active_ingresses(dut):
    """Two continuously active inputs are served alternately, one frame at a time."""
    tb = TB(dut)
    await tb.reset(operation_mode=MANAGED)

    destination_0 = 0x300000000001
    destination_1 = 0x300000000002

    await tb.set_pause(True)
    await tb.cpu_write_entry(0, destination_0, bitmap=0b0100)
    await tb.cpu_write_entry(1, destination_1, bitmap=0b1000)

    frames_0 = [
        ethernet_frame(destination_0, 0x400000000001, bytes([index]) * 40)
        for index in range(2)
    ]
    frames_1 = [
        ethernet_frame(destination_1, 0x400000000002, bytes([index + 2]) * 40)
        for index in range(2)
    ]

    async def send_all(port, frames, source_tid):
        for frame in frames:
            await tb.send(port, frame, tid=source_tid)

    # Fill both ingress paths while forwarding is paused so both requesters are
    # active when arbitration resumes.
    send_0 = cocotb.start_soon(send_all(0, frames_0, source_tid=3))
    send_1 = cocotb.start_soon(send_all(1, frames_1, source_tid=3))
    await tb.cycle(12)

    order_task = cocotb.start_soon(tb.capture_arbiter_frame_order(4))
    await tb.set_pause(False)

    await send_0
    await send_1
    order = await with_timeout(order_task, 100, "us")

    assert set(order) == {0, 1}
    assert all(first != second for first, second in zip(order, order[1:])), order

    for expected in frames_0:
        received = await tb.recv(2)
        assert bytes(received.tdata) == expected
        assert int(received.tid) == 0

    for expected in frames_1:
        received = await tb.recv(3)
        assert bytes(received.tdata) == expected
        assert int(received.tid) == 1

    await tb.cycle(10)
    assert all(sink.empty() for sink in tb.sinks)


@cocotb.test()
async def test_zero_bitmap_drops_frame(dut):
    """A lookup result with no selected egress interfaces drops the frame."""
    tb = TB(dut)
    await tb.reset(operation_mode=MANAGED, default_forwarding=0)

    data = ethernet_frame(
        da=0x500000000001,
        sa=0x500000000002,
        payload=b"this-frame-must-be-dropped",
    )

    await tb.send(3, data)
    await tb.cycle(100)
    assert all(sink.empty() for sink in tb.sinks)


@cocotb.test()
async def test_incomplete_destination_address_drops_frame(dut):
    """Frames ending before the complete DA never reach an egress."""
    tb = TB(dut)
    await tb.reset(operation_mode=MANAGED, default_forwarding=0b0010)

    destination = 0x504000000001
    destination_bytes = destination.to_bytes(6, "big")
    frames = [destination_bytes[:length] for length in range(1, 6)]

    await tb.send_all(0, frames)
    await tb.cycle(300)
    assert all(sink.empty() for sink in tb.sinks)


@cocotb.test()
async def test_incomplete_ethernet_header_drops_frame(dut):
    """Frames with a complete DA but incomplete SA never reach an egress."""
    tb = TB(dut)
    await tb.reset(operation_mode=MANAGED)

    destination = 0x505000000001
    await tb.set_pause(True)
    await tb.cpu_write_entry(0, destination, bitmap=0b0010)
    await tb.set_pause(False)

    complete_header = ethernet_frame(destination, 0x505000000002, b"")
    frames = [complete_header[:length] for length in range(6, 12)]

    await tb.send_all(0, frames)
    await tb.cycle(300)
    assert all(sink.empty() for sink in tb.sinks)


@cocotb.test()
async def test_header_only_and_unaligned_frames(dut):
    """Header-only and non-word-aligned frames retain every valid byte."""
    tb = TB(dut)
    await tb.reset(operation_mode=MANAGED)

    destination = 0x510000000001
    await tb.set_pause(True)
    await tb.cpu_write_entry(0, destination, bitmap=0b0010)
    await tb.set_pause(False)

    frames = [
        ethernet_frame(destination, 0x510000000002, bytes(range(payload_length)))
        for payload_length in (0, 1, 2, 3, 5, 17, 65)
    ]

    await tb.send_all(0, frames)

    for expected in frames:
        received = await tb.recv(1)
        assert bytes(received.tdata) == expected
        assert int(received.tid) == 0

    await tb.cycle(10)
    assert all(sink.empty() for sink in tb.sinks)


@cocotb.test()
async def test_back_to_back_frame_burst(dut):
    """A long back-to-back burst preserves frame boundaries, data, and order."""
    tb = TB(dut)
    await tb.reset(operation_mode=MANAGED)

    destination = 0x520000000001
    await tb.set_pause(True)
    await tb.cpu_write_entry(0, destination, bitmap=0b0100)
    await tb.set_pause(False)

    frames = [
        ethernet_frame(
            destination,
            0x520000000100 + index,
            bytes([index]) * (20 + index * 7),
        )
        for index in range(12)
    ]

    send_task = cocotb.start_soon(tb.send_all(1, frames, tdest=0x44, tid=3))

    for expected in frames:
        received = await tb.recv(2)
        assert bytes(received.tdata) == expected
        assert int(received.tdest) == 0x44
        assert int(received.tid) == 1

    await send_task
    await tb.cycle(10)
    assert all(sink.empty() for sink in tb.sinks)


@cocotb.test()
async def test_no_idle_cycle_between_back_to_back_frames(dut):
    """The next frame is presented immediately after each accepted tlast."""
    tb = TB(dut)
    await tb.reset(operation_mode=MANAGED, default_forwarding=0b0010)

    destination = 0x521000000001
    frames = [
        ethernet_frame(
            destination,
            0x521000000100 + index,
            bytes([0xA0 + index]) * (65 + index * 7),
        )
        for index in range(4)
    ]

    boundary_task = cocotb.start_soon(
        tb.assert_no_ingress_idle_between_frames(0, len(frames))
    )
    await tb.send_all(0, frames, tdest=0x46, tid=3)
    await with_timeout(boundary_task, 200, "us")

    for expected in frames:
        received = await tb.recv(1)
        assert bytes(received.tdata) == expected
        assert int(received.tdest) == 0x46
        assert int(received.tid) == 0

    await tb.cycle(10)
    assert all(sink.empty() for sink in tb.sinks)


@cocotb.test()
async def test_standard_and_jumbo_payloads(dut):
    """Standard and jumbo Ethernet payloads cross the shared fabric intact."""
    tb = TB(dut)
    await tb.reset(operation_mode=MANAGED)

    destination = 0x525400000001
    await tb.set_pause(True)
    await tb.cpu_write_entry(0, destination, bitmap=0b0100)
    await tb.set_pause(False)

    payload_lengths = (1500, 9000)
    frames = [
        ethernet_frame(
            destination,
            0x525400000100 + index,
            incrementing_payload(payload_length),
            ether_type=0x88B5,
        )
        for index, payload_length in enumerate(payload_lengths)
    ]
    assert [len(frame) for frame in frames] == [1514, 9014]

    send_task = cocotb.start_soon(tb.send_all(0, frames, tdest=0x45, tid=3))

    for expected in frames:
        received = await tb.recv(2, timeout_us=200)
        assert bytes(received.tdata) == expected
        assert int(received.tdest) == 0x45
        assert int(received.tid) == 0

    await send_task
    await tb.cycle(10)
    assert all(sink.empty() for sink in tb.sinks)


@cocotb.test()
async def test_all_ingress_ports_simultaneously(dut):
    """Every ingress can queue traffic simultaneously without starvation or loss."""
    tb = TB(dut)
    await tb.reset(operation_mode=MANAGED)

    destinations = [0x530000000000 + port for port in range(tb.num_ports)]
    output_ports = [(port + 1) % tb.num_ports for port in range(tb.num_ports)]

    await tb.set_pause(True)
    for index, (destination, output_port) in enumerate(zip(destinations, output_ports)):
        await tb.cpu_write_entry(index, destination, bitmap=1 << output_port)

    frames_by_port = [
        [
            ethernet_frame(
                destinations[port],
                0x540000000000 + port,
                bytes([port, sequence]) * (20 + sequence),
            )
            for sequence in range(3)
        ]
        for port in range(tb.num_ports)
    ]

    send_tasks = [
        cocotb.start_soon(tb.send_all(port, frames, tid=(port + 2) % tb.num_ports))
        for port, frames in enumerate(frames_by_port)
    ]
    await tb.cycle(20)

    frame_count = tb.num_ports * 3
    order_task = cocotb.start_soon(tb.capture_arbiter_frame_order(frame_count))
    await tb.set_pause(False)

    for task in send_tasks:
        await task
    order = await with_timeout(order_task, 200, "us")

    # With all four FIFOs preloaded, each round must serve every ingress once.
    for offset in range(0, frame_count, tb.num_ports):
        assert set(order[offset:offset + tb.num_ports]) == set(range(tb.num_ports)), order

    for ingress_port, output_port in enumerate(output_ports):
        for expected in frames_by_port[ingress_port]:
            received = await tb.recv(output_port)
            assert bytes(received.tdata) == expected
            assert int(received.tid) == ingress_port

    await tb.cycle(10)
    assert all(sink.empty() for sink in tb.sinks)


@cocotb.test()
async def test_unmanaged_mac_moves_to_new_port(dut):
    """Learning an existing source on a new ingress updates its port bitmap."""
    tb = TB(dut)
    await tb.reset(operation_mode=UNMANAGED, default_forwarding=0b1000)

    moving_mac = 0x550000000001
    unknown_destination = 0x550000000002

    learn_on_port_0 = ethernet_frame(unknown_destination, moving_mac, b"first-location")
    await tb.send(0, learn_on_port_0)
    await tb.assert_only_ports_received({3}, learn_on_port_0)

    learn_on_port_2 = ethernet_frame(unknown_destination, moving_mac, b"new-location")
    await tb.send(2, learn_on_port_2)
    await tb.assert_only_ports_received({3}, learn_on_port_2)

    lookup = ethernet_frame(moving_mac, 0x550000000003, b"use-updated-location")
    await tb.send(1, lookup)
    await tb.assert_only_ports_received({2}, lookup, expected_tid=1)


@cocotb.test()
async def test_multicast_with_output_backpressure(dut):
    """Multicast bursts remain identical on all targets under independent stalls."""
    tb = TB(dut)
    await tb.reset(operation_mode=MANAGED)

    destination = 0x560000000001
    await tb.set_pause(True)
    await tb.cpu_write_entry(0, destination, bitmap=0b1100)
    await tb.set_pause(False)

    tb.sinks[2].set_pause_generator(cycle_pause((1, 0, 0, 0)))
    tb.sinks[3].set_pause_generator(cycle_pause((1, 1, 1, 0, 0)))

    frames = [
        ethernet_frame(
            destination,
            0x560000000100 + index,
            bytes([index]) * (80 + index * 13),
        )
        for index in range(8)
    ]

    send_task = cocotb.start_soon(tb.send_all(0, frames, tdest=0x66))

    received_2 = []
    received_3 = []
    for _ in frames:
        recv_2 = cocotb.start_soon(tb.sinks[2].recv())
        recv_3 = cocotb.start_soon(tb.sinks[3].recv())
        frame_2 = await with_timeout(recv_2, 200, "us")
        frame_3 = await with_timeout(recv_3, 200, "us")
        received_2.append(bytes(frame_2.tdata))
        received_3.append(bytes(frame_3.tdata))
        assert int(frame_2.tdest) == 0x66
        assert int(frame_3.tdest) == 0x66

    await send_task
    assert received_2 == frames
    assert received_3 == frames

    await tb.cycle(10)
    assert all(sink.empty() for sink in tb.sinks)


@cocotb.test()
async def test_managed_table_cpu_readback(dut):
    """The switch CSR bridge returns every word of a programmed table entry."""
    tb = TB(dut)
    await tb.reset(operation_mode=MANAGED)

    entry_index = tb.table_depth - 1
    mac = 0x570000000001
    bitmap = (1 << (tb.num_ports - 1)) | 1

    await tb.set_pause(True)
    await tb.cpu_write_entry(entry_index, mac, bitmap)
    read_mac, read_bitmap, read_enabled = await tb.cpu_read_entry(entry_index)
    await tb.set_pause(False)

    assert read_mac == mac
    assert read_bitmap == bitmap
    assert read_enabled == 1


@cocotb.test()
async def test_pause_completes_current_frame_and_blocks_next(dut):
    """A mid-frame pause drains the active frame and holds the following one."""
    tb = TB(dut)
    await tb.reset(operation_mode=MANAGED)

    destination = 0x580000000001
    await tb.set_pause(True)
    await tb.cpu_write_entry(0, destination, bitmap=0b0010)
    await tb.set_pause(False)

    first = ethernet_frame(destination, 0x580000000002, bytes(range(256)) * 2)
    second = ethernet_frame(destination, 0x580000000003, b"held-until-resume" * 4)
    send_task = cocotb.start_soon(tb.send_all(0, [first, second]))

    for _ in range(10000):
        await RisingEdge(dut.clk)
        if int(dut.arb_tvalid.value) and int(dut.arb_tready.value) and not int(dut.arb_tlast.value):
            break
    else:
        raise AssertionError("timeout waiting for the first frame to enter arbitration")

    dut.pause_request.value = 1
    await tb.wait_asserted(dut.pause_done, "mid-frame pause_done")

    received = await tb.recv(1)
    assert bytes(received.tdata) == first

    await tb.cycle(30)
    assert tb.sinks[1].empty(), "second frame escaped while forwarding was paused"
    assert int(dut.pause_done.value)

    await tb.set_pause(False)
    received = await tb.recv(1)
    assert bytes(received.tdata) == second

    await send_task
    await tb.cycle(10)
    assert all(sink.empty() for sink in tb.sinks)


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
    """Exercise unicast/multicast routes with optional AXI idle and stalls."""
    tb = TB(dut)
    await tb.reset(operation_mode=MANAGED)

    ingress_port, programmed_bitmap, destination = route_case
    expected_bitmap = programmed_bitmap & ~(1 << ingress_port)
    expected_ports = [
        port for port in range(tb.num_ports) if expected_bitmap & (1 << port)
    ]
    assert expected_ports

    await tb.set_pause(True)
    await tb.cpu_write_entry(0, destination, bitmap=programmed_bitmap)
    await tb.set_pause(False)

    tb.set_idle_generator(idle_inserter)
    tb.set_backpressure_generator(backpressure_inserter)

    frames = [
        ethernet_frame(
            destination,
            0x600000000000 + ingress_port,
            payload_data(length),
        )
        for length in payload_lengths()
    ]

    send_task = cocotb.start_soon(
        tb.send_all(ingress_port, frames, tdest=0x70 + ingress_port, tid=3)
    )

    received = {port: [] for port in expected_ports}
    for port in expected_ports:
        for _ in frames:
            frame = await tb.recv(port, timeout_us=200)
            received[port].append(bytes(frame.tdata))
            assert int(frame.tdest) == 0x70 + ingress_port
            assert int(frame.tid) == ingress_port

    await send_task
    for port in expected_ports:
        assert received[port] == frames

    await tb.cycle(10)
    assert all(sink.empty() for sink in tb.sinks)

# ----------------------------------------------------------------------
# Dispatch: select test cases to run based on Makefile configuration
# ----------------------------------------------------------------------

if getattr(cocotb, "top", None) is not None:
    factory = TestFactory(run_factory_routing)
    factory.add_option("route_case", [
        (0, 0b0010, 0x600000000001),  # unicast: port 0 -> port 1
        (3, 0b0011, 0x600000000002),  # multicast: port 3 -> ports 0 and 1
        (2, 0b1111, 0x600000000003),  # multicast with ingress suppression
    ])
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
taxi_prim_dir = os.path.join(libs_dir, "taxi", "src", "prim", "rtl")
taxi_sync_dir = os.path.join(libs_dir, "taxi", "src", "sync", "rtl")
hal_rtl_dir = os.path.join(repo_dir, "build", "hal", "rtl")


@pytest.mark.parametrize(
    (
        "num_interfaces",
        "data_w",
        "fabric_data_w",
        "table_depth",
        "port_fifo_depth",
        "port_side",
    ),
    [
        (4, 8, 32, 5, 64, 0b1111),
        (5, 24, 48, 8, 48, 0b10101),
        (4, 32, 32, 8, 64, 0b0000),
        (8, 64, 16, 8, 16, 0b10101010),
    ],
)
def test_openenoc_eth_switch_shared_bus(
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
        os.path.join(taxi_axis_dir, "taxi_axis_arb_mux.sv"),
        os.path.join(taxi_prim_dir, "taxi_penc.sv"),
        os.path.join(taxi_prim_dir, "taxi_arbiter.sv"),
        os.path.join(taxi_sync_dir, "taxi_sync_reset.sv"),
        os.path.join(taxi_sync_dir, "taxi_sync_signal.sv"),
        os.path.join(hal_rtl_dir, "openenoc_switch_if.sv"),
        os.path.join(core_dir, "openenoc_eth_if.sv"),
        os.path.join(core_dir, "openenoc_lookup_if.sv"),
        os.path.join(core_dir, "openenoc_learning_if.sv"),
        os.path.join(core_dir, "openenoc_axis_demux.sv"),
        os.path.join(core_dir, "openenoc_axis_forwarding_engine.sv"),
        os.path.join(core_dir, "openenoc_forwarding_table.sv"),
        os.path.join(core_dir, "openenoc_eth_switch_shared_bus.sv"),
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

    extra_env = {f"PARAM_{key}": str(value) for key, value in parameters.items()}
    sim_build = os.path.join(
        tests_dir,
        "sim_build",
        request.node.name.replace("[", "-").replace("]", ""),
    )

    cocotb_test.simulator.run(
        simulator="verilator",
        python_search=[tests_dir],
        verilog_sources=verilog_sources,
        toplevel=module,
        module=module,
        parameters=parameters,
        sim_build=sim_build,
        extra_env=extra_env,
        extra_args=[
            "-Wall",
            "-Wno-DECLFILENAME",
            os.path.join(repo_dir, "dv", "common", "config.vlt"),
        ],
    )
