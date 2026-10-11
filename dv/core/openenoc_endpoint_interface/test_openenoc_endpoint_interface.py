# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: AGPL-3.0-or-later

from pathlib import Path
from itertools import cycle
import struct
import logging

import pytest
import cocotb
import cocotb_test.simulator
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Timer, with_timeout
from cocotbext.axi import (
    AxiBus,
    AxiRam,
    AxiStreamBus,
    AxiStreamSource,
    AxiStreamSink,
    AxiStreamFrame,
)

LOCAL = 0x020E0C000001
REMOTE = 0x020E0C000010
GROUP = 0x030E0C000001
EOD = struct.pack("<I", 0xE0D0E0D0)


def frame(cmd, *params, data=b"", eod=False, dst=LOCAL, src=REMOTE, padded=False):
    packet = dst.to_bytes(6, "big") + src.to_bytes(6, "big") + b"\x88\xb5\x0e" + bytes([cmd])
    packet += struct.pack("<" + "I" * len(params), *params)
    if data:
        packet += data + bytes((-len(data)) % 4)
    if eod:
        packet += EOD
    return packet + bytes(max(0, 60 - len(packet))) if padded else packet


def raw(data, dst=LOCAL):
    return dst.to_bytes(6, "big") + REMOTE.to_bytes(6, "big") + b"\x08\x00" + data


def decode(packet):
    data = bytes(packet.tdata)
    assert data[12:15] == b"\x88\xb5\x0e"
    return data[15], struct.unpack_from("<I", data, 16)[0], data


class TB:
    def __init__(self, dut):
        self.dut = dut
        cocotb.start_soon(Clock(dut.clk, 10, unit="ns").start())
        self.ram = AxiRam(AxiBus.from_entity(dut.m_axi_if), dut.clk, dut.rst, size=0x10000)
        self.source = AxiStreamSource(
            AxiStreamBus.from_entity(dut.eth_if.b2a_axis_if), dut.clk, dut.rst
        )
        self.sink = AxiStreamSink(
            AxiStreamBus.from_entity(dut.eth_if.a2b_axis_if), dut.clk, dut.rst
        )
        for model in (self.source, self.sink):
            model.log.setLevel(logging.WARNING)

    async def reset(self):
        for name in [
            "tx_data",
            "tx_keep",
            "tx_last",
            "tx_valid",
            "rx_ready",
            "irq_enable",
            "event_enable",
            "complete",
            "clear_errors",
            "non_tx_address",
            "non_tx_length",
            "non_tx_request",
            "non_rx_address",
            "non_rx_capacity",
            "non_rx_request",
            "peer_mode",
            "peer_local_addr",
            "peer_remote_addr",
            "peer_size",
            "peer_request",
            "peer_irq_enable",
            "rmem_req",
            "rmem_req_is_wr",
            "rmem_addr",
            "rmem_wr_data",
            "rmem_wr_biten",
            "rmem_timeout_cycles",
            "mac_address",
            "multicast_address",
            "peer_mac",
            "receive_mode",
            "dma_timeout_cycles",
            "fragment_size",
            "peer_rmem_offset",
            "peer_clear_error",
            "local_wr_ack",
            "local_rd_ack",
            "local_wr_err",
            "local_rd_err",
            "local_rd_data",
            "peer1_mac",
            "peer1_mode",
            "peer1_local_addr",
            "peer1_remote_addr",
            "peer1_size",
            "peer1_rmem_offset",
        ]:
            getattr(self.dut, name).value = 0
        self.dut.mac_address.value = LOCAL
        self.dut.multicast_address.value = GROUP
        self.dut.peer_mac.value = REMOTE
        self.dut.receive_mode.value = 3
        self.dut.fragment_size.value = 32
        self.dut.rst.value = 1
        await self.cycles(5)
        self.dut.rst.value = 0
        await self.cycles(5)

    async def cycles(self, count):
        for _ in range(count):
            await RisingEdge(self.dut.clk)
        await Timer(1, unit="ns")

    async def wait(self, name, value=1):
        for _ in range(4000):
            await self.cycles(1)
            if int(getattr(self.dut, name).value) == value:
                return
        raise AssertionError(f"Timed out waiting for {name}={value}")

    async def send_direct(self, data):
        for offset in range(0, len(data), 4):
            word = data[offset : offset + 4]
            self.dut.tx_data.value = int.from_bytes(word, "little")
            self.dut.tx_keep.value = (1 << len(word)) - 1
            self.dut.tx_last.value = offset + 4 >= len(data)
            self.dut.tx_valid.value = 1
            for _ in range(4000):
                await RisingEdge(self.dut.clk)
                fire = int(self.dut.tx_hwclr.value)
                await Timer(1, unit="ns")
                if fire:
                    break
            else:
                raise AssertionError("Direct TX handshake timed out")
            self.dut.tx_valid.value = 0
            await self.cycles(2)

    async def receive_direct(self):
        data = bytearray()
        for _ in range(4000):
            if not int(self.dut.rx_valid.value):
                await self.cycles(1)
                continue
            word = int(self.dut.rx_data.value).to_bytes(4, "little")
            keep = int(self.dut.rx_keep.value)
            last = int(self.dut.rx_last.value)
            self.dut.rx_ready.value = 1
            await self.wait("rx_hwclr")
            data.extend(b for lane, b in enumerate(word) if keep & (1 << lane))
            await Timer(1, unit="ns")
            self.dut.rx_ready.value = 0
            await self.cycles(2)
            if last:
                return bytes(data)
        raise AssertionError("Direct RX timed out")

    async def finish_claim(self):
        await self.wait("claim_valid")
        token = int(self.dut.claim.value)
        self.dut.complete.value = token
        await self.cycles(1)
        self.dut.complete.value = 0
        await self.cycles(5)
        return token

    async def configure_peer(self, mode, local=0x300, remote=0x900, size=120, irq=0):
        d = self.dut
        d.peer_mode.value = mode
        d.peer_local_addr.value = local
        d.peer_remote_addr.value = remote
        d.peer_size.value = size
        d.peer_irq_enable.value = irq
        await self.cycles(1)

    async def start_peer(self):
        self.dut.peer_request.value = 1
        await self.wait("peer_hwclr")
        self.dut.peer_request.value = 0

    async def receive_wire(self):
        return decode(await with_timeout(self.sink.recv(), 100, "us"))

    async def send_wire(self, packet):
        await self.source.send(AxiStreamFrame(packet))
        await with_timeout(self.source.wait(), 100, "us")

    async def clear_peer_error(self):
        self.dut.peer_clear_error.value = 1
        await self.cycles(1)
        self.dut.peer_clear_error.value = 0
        await self.cycles(1)
        assert not int(self.dut.peer_error.value)

    async def request_rmem(self, addr, write=False, data=0, biten=0xFFFFFFFF):
        d = self.dut
        await FallingEdge(d.clk)
        d.rmem_addr.value = addr
        d.rmem_req_is_wr.value = write
        d.rmem_wr_data.value = data
        d.rmem_wr_biten.value = biten
        d.rmem_req.value = 1
        await self.cycles(1)
        d.rmem_req.value = 0

    async def service_local(self, data=0, error=False):
        d = self.dut
        await self.wait("local_req")
        result = {
            k: int(getattr(d, "local_" + k).value)
            for k in ("req_is_wr", "addr", "wr_data", "wr_biten")
        }
        await self.cycles(3)
        d.local_rd_data.value = data
        d.local_wr_err.value = error
        d.local_rd_err.value = error
        d.local_wr_ack.value = result["req_is_wr"]
        d.local_rd_ack.value = not result["req_is_wr"]
        await self.cycles(1)
        d.local_wr_ack.value = 0
        d.local_rd_ack.value = 0
        return result


@cocotb.test()
async def test_cut_through_direct_irq_and_backpressure(dut):
    tb = TB(dut)
    await tb.reset()
    dut.event_enable.value = (1 << 3) | (1 << 4)
    dut.irq_enable.value = 1
    payload = bytes((n * 13 + 7) & 255 for n in range(511))
    await tb.source.send(AxiStreamFrame(payload))
    await tb.wait("claim_valid")
    assert (int(dut.claim.value) >> 11) & 15 == 4
    assert not tb.source.idle(), "RX notification waited for the whole frame"
    assert int(dut.irq.value) == 1
    assert await tb.receive_direct() == payload
    await tb.finish_claim()
    await tb.wait("irq", 0)
    assert not int(dut.overflow.value)

    tb.sink.pause = True
    send = cocotb.start_soon(tb.send_direct(payload))
    await tb.cycles(60)
    assert not send.done(), "TX did not apply backpressure through the FIFO"
    assert not int(dut.claim_valid.value), "TX IRQ preceded the final oETP input beat"
    tb.sink.pause = False
    tb.sink.set_pause_generator(cycle([0, 1, 0, 0]))
    frame = await with_timeout(tb.sink.recv(), 100, "us")
    assert bytes(frame.tdata) == payload
    await send
    await tb.wait("claim_valid")
    assert (int(dut.claim.value) >> 11) & 15 == 3
    await tb.finish_claim()
    await tb.wait("irq", 0)
    assert int(dut.reserved_count.value) == 0


@cocotb.test()
async def test_full_irq_fifo_blocks_next_frame_without_loss(dut):
    tb = TB(dut)
    await tb.reset()
    dut.event_enable.value = 1 << 4
    # Masking the physical IRQ still collects events.
    for data in [b"first", b"second"]:
        await tb.source.send(AxiStreamFrame(data))
        assert await tb.receive_direct() == data
    await tb.wait("fifo_level", 2)
    assert int(dut.credit_full.value) == 1
    assert int(dut.irq.value) == 0
    await tb.source.send(AxiStreamFrame(b"third"))
    await tb.cycles(30)
    assert int(dut.rx_valid.value) == 0
    dut.irq_enable.value = 1
    await tb.wait("irq")
    tokens = [await tb.finish_claim()]
    assert await tb.receive_direct() == b"third"
    tokens += [await tb.finish_claim(), await tb.finish_claim()]
    assert [t >> 15 & 0xFFFF for t in tokens] == [0, 1, 2]
    await tb.wait("fifo_level", 0)
    assert not int(dut.overflow.value)
    assert not int(dut.invalid_complete.value)


@cocotb.test(timeout_time=1000, timeout_unit="us")
async def test_raw_dma_routing_and_filter(dut):
    tb = TB(dut)
    await tb.reset()
    payload = raw(bytes((n * 3 + 9) & 255 for n in range(39)))
    tb.ram.write(0x113, payload)
    dut.non_tx_address.value = 0x113
    dut.non_tx_length.value = len(payload)
    dut.non_tx_request.value = 1
    await tb.wait("non_tx_hwclr")
    dut.non_tx_request.value = 0
    assert bytes((await with_timeout(tb.sink.recv(), 100, "us")).tdata) == payload
    await tb.wait("non_tx_done")
    assert not int(dut.non_tx_error.value)
    dut.non_rx_address.value = 0x200
    dut.non_rx_capacity.value = 64
    dut.non_rx_request.value = 1
    await tb.wait("non_rx_hwclr")
    dut.non_rx_request.value = 0
    await tb.source.send(AxiStreamFrame(payload))
    await tb.wait("non_rx_idle")
    assert tb.ram.read(0x200, len(payload)) == payload
    assert not int(dut.rx_valid.value) and not int(dut.non_rx_armed.value)
    dut.receive_mode.value = 1
    await tb.source.send(AxiStreamFrame(raw(b"filtered", dst=REMOTE)))
    await tb.cycles(80)
    assert not int(dut.rx_valid.value)
    await tb.source.send(AxiStreamFrame(raw(b"accepted")))
    assert await tb.receive_direct() == raw(b"accepted")


@cocotb.test(timeout_time=1000, timeout_unit="us")
async def test_peer_dma_fragments_and_timeout_abort(dut):
    tb = TB(dut)
    await tb.reset()
    payload = bytes((n * 11 + 7) & 255 for n in range(101))
    tb.ram.write(0x303, payload)
    await tb.configure_peer(3, local=0x303, remote=0x903, size=len(payload), irq=1)
    dut.event_enable.value = 1
    dut.irq_enable.value = 1
    dut.fragment_size.value = 31  # Rounded to 28; the final fragment has 17 bytes.
    await tb.start_peer()
    position = 0
    ids = []
    while position < len(payload):
        cmd, rid, packet = await tb.receive_wire()
        ids.append(rid)
        addr, length = struct.unpack_from("<II", packet, 20)
        assert cmd == 0x40 and addr == 0x903 + position
        assert length == min(28, len(payload) - position)
        assert packet[:12] == REMOTE.to_bytes(6, "big") + LOCAL.to_bytes(6, "big")
        assert packet[28 : 28 + length] == payload[position : position + length]
        assert packet[-4:] == EOD
        await tb.cycles(20)
        assert tb.sink.empty(), "Next fragment preceded the reply"
        await tb.send_wire(frame(0x41, rid, padded=True))
        position += length
    assert ids == list(range(len(ids)))
    await tb.wait("peer_done")
    assert not int(dut.peer_error.value)
    assert (await tb.finish_claim() >> 11) & 15 == 0

    # A local timeout ends the block and cancels every unsent fragment.
    dut.dma_timeout_cycles.value = 100
    await tb.start_peer()
    cmd, rid, _ = await tb.receive_wire()
    assert cmd == 0x40 and rid == len(ids)
    await tb.wait("peer_idle")
    assert int(dut.peer_error_code.value) == 8 and not int(dut.peer_done.value)
    await tb.cycles(250)
    assert tb.sink.empty()
    await tb.finish_claim()
    await tb.send_wire(frame(0x41, rid))  # Late response cannot revive the block.
    await tb.clear_peer_error()
    await tb.start_peer()
    cmd, rid2, _ = await tb.receive_wire()
    assert cmd == 0x40 and rid2 == rid + 1
    await tb.send_wire(frame(0xFF, rid2, 6))
    await tb.wait("peer_idle")
    assert int(dut.peer_error_code.value) == 14
    await tb.cycles(50)
    assert tb.sink.empty()


@cocotb.test(timeout_time=1000, timeout_unit="us")
async def test_dma_read_memory_and_late_eod_error(dut):
    tb = TB(dut)
    await tb.reset()
    payload = bytes((n * 7 + 3) & 255 for n in range(73))
    await tb.configure_peer(2, local=0x501, remote=0x901, size=len(payload))
    await tb.start_peer()
    pos = 0
    while pos < len(payload):
        cmd, rid, packet = await tb.receive_wire()
        addr, length = struct.unpack_from("<II", packet, 20)
        assert cmd == 0x30 and addr == 0x901 + pos and length == min(32, len(payload) - pos)
        await tb.send_wire(
            frame(0x31, rid, data=payload[pos : pos + length], eod=True, padded=True)
        )
        pos += length
    await tb.wait("peer_done")
    assert tb.ram.read(0x501, len(payload)) == payload
    assert not int(dut.peer_error.value)

    await tb.configure_peer(2, local=0x701, remote=0xB01, size=12)
    await tb.start_peer()
    _, rid, _ = await tb.receive_wire()
    data = b"DATA" + EOD + b"TAIL"
    await tb.send_wire(frame(0x31, rid, data=data) + bytes(4))
    await tb.wait("peer_idle")
    assert int(dut.peer_error_code.value) == 10
    assert tb.ram.read(0x701, 12) == data  # Streaming writes are not rolled back.

    await tb.clear_peer_error()
    await tb.start_peer()
    _, rid, _ = await tb.receive_wire()
    await tb.send_wire(frame(0x31, rid, data=b"SHORT"))
    await tb.wait("peer_idle")
    assert int(dut.peer_error_code.value) == 10
    assert tb.ram.read(0x701, 5) == b"SHORT"


@cocotb.test(timeout_time=1000, timeout_unit="us")
async def test_incoming_dma_memory_windows_and_multicast(dut):
    tb = TB(dut)
    await tb.reset()
    await tb.configure_peer(2, local=0x800, size=64, irq=1)
    dut.event_enable.value = 1
    dut.irq_enable.value = 1
    for rid, length in enumerate([1, 3, 4, 5, 31, 32]):
        data = bytes((n + rid * 7) & 255 for n in range(length))
        await tb.send_wire(frame(0x40, rid, 0x803, length, data=data, eod=True, padded=True))
        cmd, rsp_id, _ = await tb.receive_wire()
        assert cmd == 0x41 and rsp_id == rid
        assert tb.ram.read(0x803, length) == data
        assert not int(dut.claim_valid.value)

    # EndOfData is checked after the memory payload TLAST.
    await tb.send_wire(frame(0x40, 10, 0x803, 12, data=b"written-data") + bytes(4))
    cmd, rid, packet = await tb.receive_wire()
    assert cmd == 0xFF and rid == 10 and struct.unpack_from("<I", packet, 20)[0] == 2
    assert int(dut.peer_error_code.value) == 10
    assert tb.ram.read(0x803, 12) == b"written-data"
    assert (await tb.finish_claim() >> 11) & 15 == 0
    await tb.clear_peer_error()

    before = tb.ram.read(0x840, 16)
    await tb.send_wire(frame(0x40, 11, 0x83F, 8, data=b"outside!", eod=True))
    cmd, rid, packet = await tb.receive_wire()
    assert cmd == 0xFF and rid == 11 and struct.unpack_from("<I", packet, 20)[0] == 1
    assert tb.ram.read(0x840, 16) == before
    assert int(dut.peer_error_code.value) == 1
    await tb.finish_claim()
    await tb.clear_peer_error()

    await tb.send_wire(frame(0x40, 12, 0x810, 5, data=b"group", eod=True, dst=GROUP))
    await tb.cycles(150)
    assert tb.ram.read(0x810, 5) == b"group" and tb.sink.empty()
    await tb.send_wire(frame(0x40, 13, 0x810, 12, data=b"bad-marker!!", dst=GROUP) + bytes(4))
    await tb.wait("peer_error")
    assert int(dut.peer_error_code.value) == 10 and tb.sink.empty()
    await tb.finish_claim()

    await tb.clear_peer_error()
    await tb.configure_peer(3, local=0x800, size=64)
    await tb.send_wire(frame(0x30, 14, 0x810, 5))
    cmd, rid, packet = await tb.receive_wire()
    assert cmd == 0x31 and rid == 14 and packet[20:25] == b"bad-m"
    assert packet[-4:] == EOD


@cocotb.test(timeout_time=1000, timeout_unit="us")
async def test_rmem_wire_cpuif_and_error_irq(dut):
    tb = TB(dut)
    await tb.reset()
    await tb.configure_peer(1, local=0x500, remote=0x900, size=16)
    dut.peer_rmem_offset.value = 0x100
    dut.event_enable.value = 1 << 5
    dut.irq_enable.value = 1
    await tb.request_rmem(0x104)
    cmd, rid, packet = await tb.receive_wire()
    assert cmd == 0x10 and struct.unpack_from("<I", packet, 20)[0] == 0x904
    await tb.send_wire(frame(0x11, rid, 0x12345678, padded=True))
    await tb.wait("rmem_ack")
    assert int(dut.rmem_rd_data.value) == 0x12345678
    assert not int(dut.claim_valid.value)
    await tb.cycles(2)

    await tb.request_rmem(0x108, write=True, data=0xABCD1234, biten=0x00FF00FF)
    cmd, rid, packet = await tb.receive_wire()
    assert cmd == 0x20 and struct.unpack_from("<III", packet, 20) == (0x908, 0x00FF00FF, 0xABCD1234)
    await tb.send_wire(frame(0xFF, rid, 6))
    await tb.wait("rmem_wr_ack")
    assert int(dut.peer_error_code.value) == 14
    assert (await tb.finish_claim() >> 11) & 15 == 5
    await tb.clear_peer_error()

    dut.rmem_timeout_cycles.value = 100
    await tb.request_rmem(0x100)
    _, _, _ = await tb.receive_wire()
    await tb.wait("rmem_ack")
    assert int(dut.rmem_rd_data.value) == 0xFFFFFFFF
    assert int(dut.peer_error_code.value) == 8
    await tb.finish_claim()
    await tb.clear_peer_error()
    await tb.request_rmem(0x10E)  # Misaligned word crosses the configured RMEM window.
    await tb.wait("rmem_ack")
    assert int(dut.rmem_rd_data.value) == 0xFFFFFFFF and tb.sink.empty()
    await tb.finish_claim()
    await tb.clear_peer_error()

    service = cocotb.start_soon(tb.service_local(data=0xDEADBEEF))
    await tb.send_wire(frame(0x10, 100, 0x504))
    local = await with_timeout(service, 100, "us")
    assert local["addr"] == 0x504 and not local["req_is_wr"]
    cmd, rid, packet = await tb.receive_wire()
    assert cmd == 0x11 and rid == 100 and struct.unpack_from("<I", packet, 20)[0] == 0xDEADBEEF

    service = cocotb.start_soon(tb.service_local(error=True))
    await tb.send_wire(frame(0x20, 101, 0x508, 0x00FF00FF, 0x12345678))
    local = await with_timeout(service, 100, "us")
    assert local["req_is_wr"] and local["wr_biten"] == 0x00FF00FF and local["wr_data"] == 0x12345678
    cmd, rid, packet = await tb.receive_wire()
    assert cmd == 0xFF and rid == 101 and struct.unpack_from("<I", packet, 20)[0] == 6
    assert int(dut.peer_error_code.value) == 6
    await tb.finish_claim()
    await tb.clear_peer_error()

    await tb.send_wire(frame(0x20, 102, 0x508, 0, 0xAABBCCDD))
    cmd, rid, _ = await tb.receive_wire()
    assert cmd == 0x21 and rid == 102 and not int(dut.local_req.value)


@cocotb.test(timeout_time=1000, timeout_unit="us")
async def test_rmem_priority_between_bulk_fragments(dut):
    tb = TB(dut)
    await tb.reset()
    data = bytes(range(65))
    tb.ram.write(0x300, data)
    await tb.configure_peer(3, size=len(data))
    mac = REMOTE + 1
    dut.peer1_mac.value = mac
    dut.peer1_mode.value = 1
    dut.peer1_local_addr.value = 0x500
    dut.peer1_remote_addr.value = 0xB00
    dut.peer1_rmem_offset.value = 0x100
    dut.peer1_size.value = 16
    await tb.start_peer()
    cmd, rid, packet = await tb.receive_wire()
    assert cmd == 0x40 and packet[28:60] == data[:32]
    await tb.request_rmem(0x104)
    await tb.cycles(30)
    assert tb.sink.empty() and not int(dut.rmem_ack.value)
    await tb.send_wire(frame(0x41, rid))
    cmd, rrid, packet = await tb.receive_wire()
    assert cmd == 0x10 and packet[:6] == mac.to_bytes(6, "big")
    assert struct.unpack_from("<I", packet, 20)[0] == 0xB04
    await tb.send_wire(frame(0x11, rrid, 0xABCDEF01, src=mac))
    await tb.wait("rmem_ack")
    assert int(dut.rmem_rd_data.value) == 0xABCDEF01
    for pos in [32, 64]:
        cmd, rid, packet = await tb.receive_wire()
        assert cmd == 0x40 and packet[28 : 28 + min(32, 65 - pos)] == data[pos : pos + 32]
        await tb.send_wire(frame(0x41, rid))
    await tb.wait("peer_done")
    assert not int(dut.peer_error.value)


@cocotb.test(timeout_time=1000, timeout_unit="us")
async def test_axi_errors_and_response_status(dut):
    tb = TB(dut)
    await tb.reset()
    await tb.configure_peer(2, local=0x800, size=64, irq=1)
    dut.event_enable.value = 1
    dut.irq_enable.value = 1
    write = tb.ram.write_if._write

    async def fail_write(address, data):
        raise IOError("Injected AXI write failure")

    tb.ram.write_if._write = fail_write
    await tb.send_wire(frame(0x40, 50, 0x803, 12, data=b"axi-failure!", eod=True))
    cmd, rid, packet = await tb.receive_wire()
    assert cmd == 0xFF and rid == 50 and struct.unpack_from("<I", packet, 20)[0] == 6
    assert int(dut.peer_error_code.value) == 6
    assert (await tb.finish_claim() >> 11) & 15 == 0
    await tb.clear_peer_error()
    # AXI root cause is retained even when the wire has a bad marker too.
    await tb.send_wire(frame(0x40, 51, 0x803, 12, data=b"axi-failure!") + bytes(4))
    cmd, rid, packet = await tb.receive_wire()
    assert cmd == 0xFF and rid == 51 and struct.unpack_from("<I", packet, 20)[0] == 6
    assert int(dut.peer_error_code.value) == 6
    await tb.finish_claim()
    tb.ram.write_if._write = write
    await tb.clear_peer_error()
    await tb.send_wire(frame(0x40, 52, 0x803, 5, data=b"fixed", eod=True))
    cmd, rid, _ = await tb.receive_wire()
    assert cmd == 0x41 and rid == 52 and tb.ram.read(0x803, 5) == b"fixed"

    read = tb.ram.read_if._read

    async def fail_read(address, length):
        raise IOError("Injected AXI read failure")

    tb.ram.read_if._read = fail_read
    await tb.configure_peer(3, local=0x803, size=73, irq=1)
    await tb.start_peer()
    await tb.wait("peer_error")
    await tb.wait("peer_idle")
    assert int(dut.peer_error_code.value) == 4 and not int(dut.peer_done.value)
    await tb.finish_claim()
    await tb.cycles(100)
    while not tb.sink.empty():
        cmd, _, packet = await tb.receive_wire()
        assert cmd == 0x40 and packet[-4:] != EOD
    tb.ram.read_if._read = read
    await tb.clear_peer_error()
    await tb.configure_peer(3, local=0x800, size=64, irq=1)
    tb.ram.read_if._read = fail_read
    await tb.send_wire(frame(0x30, 53, 0x803, 12))
    cmd, rid, packet = await tb.receive_wire()
    assert rid == 53 and (
        (cmd == 0xFF and struct.unpack_from("<I", packet, 20)[0] == 4)
        or (cmd == 0x31 and packet[-4:] != EOD)
    )
    await tb.wait("peer_error")
    assert int(dut.peer_error_code.value) == 4
    await tb.finish_claim()
    tb.ram.read_if._read = read
    await tb.clear_peer_error()
    await tb.send_wire(frame(0x30, 54, 0x803, 5))
    cmd, rid, packet = await tb.receive_wire()
    assert cmd == 0x31 and rid == 54 and packet[20:25] == b"fixed" and packet[-4:] == EOD


@cocotb.test(timeout_time=1000, timeout_unit="us")
async def test_error_irq_retention_under_full_fifo(dut):
    tb = TB(dut)
    await tb.reset()
    await tb.configure_peer(1, local=0x500, remote=0x900, size=16)
    dut.peer_rmem_offset.value = 0x100
    dut.rmem_timeout_cycles.value = 100
    dut.event_enable.value = (1 << 4) | (1 << 5)
    for data in [raw(b"one"), raw(b"two")]:
        await tb.send_wire(data)
        assert await tb.receive_direct() == data
    await tb.wait("credit_full")
    await tb.request_rmem(0x100)
    await tb.receive_wire()
    await tb.wait("rmem_ack")
    assert int(dut.peer_error_code.value) == 8
    assert int(dut.rmem_rd_data.value) == 0xFFFFFFFF
    # A second one-cycle CPUIF request must not disappear behind the pending IRQ.
    await tb.request_rmem(0x104)
    _, rid, _ = await tb.receive_wire()
    await tb.send_wire(frame(0xFF, rid, 6))
    await tb.wait("rmem_ack")
    assert int(dut.rmem_rd_data.value) == 0xFFFFFFFF
    assert int(dut.peer_error_code.value) == 14
    dut.peer1_mac.value = REMOTE + 1
    dut.peer1_mode.value = 1
    dut.peer1_remote_addr.value = 0xB00
    dut.peer1_rmem_offset.value = 0x200
    dut.peer1_size.value = 16
    await tb.request_rmem(0x200)
    _, rid, _ = await tb.receive_wire()
    await tb.send_wire(frame(0xFF, rid, 4, src=REMOTE + 1))
    await tb.wait("rmem_ack")
    assert int(dut.rmem_rd_data.value) == 0xFFFFFFFF
    assert int(dut.peer_error_code.value) == 14
    await tb.cycles(3)
    dut.event_enable.value = 0
    tokens = [await tb.finish_claim() for _ in range(4)]
    assert [(t >> 11) & 15 for t in tokens] == [4, 4, 5, 5]
    assert [t & 0x7FF for t in tokens[2:]] == [0, 1]
    assert not int(dut.claim_valid.value)
    await tb.clear_peer_error()
    await tb.configure_peer(2, local=0x800, size=32, irq=1)
    dut.event_enable.value = (1 << 4) | 1
    for data in [raw(b"three"), raw(b"four")]:
        await tb.send_wire(data)
        assert await tb.receive_direct() == data
    await tb.wait("credit_full")
    await tb.send_wire(frame(0x40, 123, 0x81F, 8, data=b"outside!", eod=True))
    cmd, rid, packet = await tb.receive_wire()
    assert cmd == 0xFF and rid == 123 and struct.unpack_from("<I", packet, 20)[0] == 1
    assert int(dut.peer_error_code.value) == 1
    tokens = [await tb.finish_claim()]
    dut.event_enable.value = 0
    tokens += [await tb.finish_claim(), await tb.finish_claim()]
    assert [(t >> 11) & 15 for t in tokens] == [4, 4, 0]
    assert not int(dut.overflow.value) and not int(dut.invalid_complete.value)


@pytest.mark.parametrize("axi_data_w,eth_data_w", [(32, 32), (64, 32), (32, 64), (64, 8)])
def test_openenoc_endpoint_interface(request, axi_data_w, eth_data_w):
    tests = Path(__file__).resolve().parent
    repo = tests.parents[2]
    core = repo / "hw/rtl/core"
    taxi = repo / "libs/taxi/src"
    sources = [
        repo / "build/hal/rtl/openenoc_endpoint_if.sv",
        taxi / "axis/rtl/taxi_axis_if.sv",
        taxi / "axis/rtl/taxi_axis_adapter.sv",
        taxi / "axis/rtl/taxi_axis_register.sv",
        taxi / "axis/rtl/taxi_axis_fifo.sv",
        taxi / "axis/rtl/taxi_axis_fifo_adapter.sv",
        taxi / "axis/rtl/taxi_axis_arb_mux.sv",
        taxi / "axis/rtl/taxi_axis_demux.sv",
        taxi / "axi/rtl/taxi_axi_if.sv",
        taxi / "axi/rtl/taxi_axi_register_rd.sv",
        taxi / "axi/rtl/taxi_axi_register_wr.sv",
        taxi / "dma/rtl/taxi_dma_desc_if.sv",
        taxi / "dma/rtl/taxi_axi_dma_rd.sv",
        taxi / "dma/rtl/taxi_axi_dma_wr.sv",
        taxi / "dma/rtl/taxi_axi_dma.sv",
        taxi / "prim/rtl/taxi_arbiter.sv",
        taxi / "prim/rtl/taxi_penc.sv",
        core / "openenoc_eth_if.sv",
        core / "openenoc_cpuif_if.sv",
        core / "openenoc_peer_lookup_if.sv",
        core / "openenoc_dma_transfer_if.sv",
        core / "openenoc_irq_event_if.sv",
        core / "openenoc_rr_arbiter.sv",
        core / "openenoc_endpoint_dma_engine.sv",
        core / "openenoc_endpoint_peer_lookup.sv",
        core / "openenoc_endpoint_irq_controller.sv",
        core / "openenoc_endpoint_direct_axis.sv",
        core / "openenoc_endpoint_oetp_engine.sv",
        core / "openenoc_endpoint_interface.sv",
        tests / "test_openenoc_endpoint_interface.sv",
    ]
    cocotb_test.simulator.run(
        simulator="verilator",
        verilog_sources=[str(p) for p in sources],
        toplevel="test_openenoc_endpoint_interface",
        module="test_openenoc_endpoint_interface",
        python_search=[str(tests)],
        parameters={"AXI_DATA_W": axi_data_w, "ETH_DATA_W": eth_data_w},
        timescale="1ns/1ps",
        extra_args=["-Wall", str(repo / "dv/common/config.vlt")],
        sim_build=str(tests / "sim_build" / request.node.name),
    )
