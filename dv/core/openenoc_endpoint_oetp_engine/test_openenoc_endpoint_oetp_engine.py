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
from cocotb.queue import Queue
from cocotb.triggers import FallingEdge, RisingEdge, Timer, with_timeout
from cocotbext.axi import AxiStreamBus, AxiStreamSource, AxiStreamSink, AxiStreamFrame

LOCAL = 0x020E0C000001
GROUP = 0x030E0C000001
MACS = [0x020E0C000010, 0x020E0C000011, 0x020E0C000012, GROUP]
MODES = [2, 3, 1, 3]
EOD = struct.pack("<I", 0xE0D0E0D0)


def words(*values):
    return struct.pack("<" + "I" * len(values), *values)


def frame(cmd, *params, data=b"", dst=LOCAL, src=MACS[0], padded=False, eod=False):
    result = (
        dst.to_bytes(6, "big")
        + src.to_bytes(6, "big")
        + b"\x88\xb5\x0e"
        + bytes([cmd])
        + words(*params)
    )
    if data:
        result += data + bytes((-len(data)) % 4)
    if eod:
        result += EOD
    return result + bytes(max(0, 60 - len(result))) if padded else result


def raw(dst=LOCAL, src=MACS[0], ethertype=b"\x08\x00", data=b"raw"):
    return dst.to_bytes(6, "big") + src.to_bytes(6, "big") + ethertype + data


class TB:
    def __init__(self, dut):
        self.dut = dut
        cocotb.start_soon(Clock(dut.clk, 10, unit="ns").start())
        self.eth_source = AxiStreamSource(AxiStreamBus.from_entity(dut.eth_rx_if), dut.clk, dut.rst)
        self.eth_sink = AxiStreamSink(AxiStreamBus.from_entity(dut.eth_tx_if), dut.clk, dut.rst)
        self.data_source = AxiStreamSource(
            AxiStreamBus.from_entity(dut.local_tx_if), dut.clk, dut.rst
        )
        self.data_sink = AxiStreamSink(AxiStreamBus.from_entity(dut.local_rx_if), dut.clk, dut.rst)
        for stream in [self.eth_source, self.eth_sink, self.data_source, self.data_sink]:
            stream.log.setLevel(logging.WARNING)
        self.requests = Queue()
        self.completions = Queue()
        self.rx_status = Queue()
        self.raw_claims = 0
        self.modes = MODES.copy()
        self.macs = MACS.copy()
        cocotb.start_soon(self.lookup())
        cocotb.start_soon(self.monitor())

    async def cycles(self, count=1):
        for _ in range(count):
            await RisingEdge(self.dut.clk)
        await Timer(1, unit="ns")

    async def reset(self):
        d = self.dut
        for name in [n for n in dir(d) if n.startswith(("initiator_", "responder_", "lookup_"))]:
            driven = (
                (name.startswith("initiator_req_") and name != "initiator_req_ready")
                or (
                    name.startswith(("initiator_tx_status_", "initiator_rx_status_"))
                    and not name.endswith("_ready")
                )
                or name == "initiator_cpl_ready"
                or name == "responder_req_ready"
                or (name.startswith("responder_cpl_") and name != "responder_cpl_ready")
                or name
                in [
                    "responder_rx_status_ready",
                    "responder_tx_status_ready",
                    "lookup_req_ready",
                ]
                or (name.startswith("lookup_rsp_") and name != "lookup_rsp_ready")
            )
            if not driven:
                continue
            handle = getattr(d, name)
            try:
                handle.value = 0
            except (TypeError, AttributeError):
                pass
        d.mac_address.value = LOCAL
        d.multicast_address.value = GROUP
        d.peer_mac.value = sum(mac << (48 * n) for n, mac in enumerate(self.macs))
        d.rmem_timeout.value = 0
        d.dma_timeout.value = 0
        d.receive_mode.value = 3
        d.initiator_cpl_ready.value = 1
        d.responder_req_ready.value = 1
        d.responder_rx_status_ready.value = 1
        d.lookup_req_ready.value = 1
        d.raw_available.value = 0
        d.raw_claim_ready.value = 1
        d.rst.value = 1
        await self.cycles(5)
        d.rst.value = 0
        await self.cycles(5)

    async def lookup(self):
        d = self.dut
        while True:
            await RisingEdge(d.clk)
            if int(d.rst.value):
                await Timer(1, unit="ns")
                d.lookup_rsp_valid.value = 0
                continue
            req = int(d.lookup_req_valid.value) and int(d.lookup_req_ready.value)
            rsp = int(d.lookup_rsp_valid.value) and int(d.lookup_rsp_ready.value)
            if req:
                typ = int(d.lookup_req_type.value)
                key = int(d.lookup_req_peer_idx.value)
                mac = int(d.lookup_req_mac_addr.value)
                mask = int(d.lookup_req_mode_mask.value)
                index = next(
                    (
                        n
                        for n in range(4)
                        if mask & (1 << self.modes[n])
                        and self.modes[n] != 0
                        and (n == key if typ == 0 else self.macs[n] == mac)
                    ),
                    None,
                )
            await Timer(1, unit="ns")
            if rsp:
                d.lookup_rsp_valid.value = 0
            if req:
                d.lookup_rsp_hit.value = index is not None
                d.lookup_rsp_peer_idx.value = index or 0
                d.lookup_rsp_mac_addr.value = self.macs[index] if index is not None else 0
                d.lookup_rsp_dma_mode.value = self.modes[index] if index is not None else 0
                d.lookup_rsp_size.value = 0x10000
                d.lookup_rsp_local_addr.value = 0x1000
                d.lookup_rsp_valid.value = 1

    def read_fields(self, prefix, names):
        return {n: int(getattr(self.dut, prefix + n).value) for n in names}

    async def monitor(self):
        d = self.dut
        while True:
            await RisingEdge(d.clk)
            if int(d.rst.value):
                continue
            if int(d.responder_req_valid.value) and int(d.responder_req_ready.value):
                self.requests.put_nowait(
                    self.read_fields(
                        "responder_req_",
                        [
                            "kind",
                            "op",
                            "addr",
                            "len",
                            "peer_idx",
                            "sequence",
                            "last",
                            "biten",
                            "wdata",
                            "error_code",
                            "rx_status",
                        ],
                    )
                )
            if int(d.initiator_cpl_valid.value) and int(d.initiator_cpl_ready.value):
                self.completions.put_nowait(
                    self.read_fields(
                        "initiator_cpl_",
                        [
                            "kind",
                            "op",
                            "peer_idx",
                            "sequence",
                            "last",
                            "transferred_len",
                            "error",
                            "error_code",
                            "rdata",
                        ],
                    )
                )
            if int(d.responder_rx_status_valid.value) and int(d.responder_rx_status_ready.value):
                self.rx_status.put_nowait(
                    self.read_fields(
                        "responder_rx_status_", ["peer_idx", "sequence", "len", "error_code"]
                    )
                )
            if int(d.raw_claim_valid.value) and int(d.raw_claim_ready.value):
                self.raw_claims += 1

    async def command(
        self,
        kind=0,
        op=0,
        peer=0,
        addr=0x1000,
        length=4,
        sequence=17,
        last=1,
        biten=0xFFFFFFFF,
        data=0,
    ):
        d = self.dut
        for key, value in dict(
            kind=kind,
            op=op,
            peer_idx=peer,
            addr=addr,
            len=length,
            sequence=sequence,
            last=last,
            biten=biten,
            wdata=data,
        ).items():
            getattr(d, "initiator_req_" + key).value = value
        d.initiator_req_valid.value = 1
        for _ in range(1000):
            await RisingEdge(d.clk)
            fire = int(d.initiator_req_ready.value)
            await Timer(1, unit="ns")
            if fire:
                d.initiator_req_valid.value = 0
                return
        raise AssertionError("Command handshake did not complete")

    async def source_status(self, length, code=0, peer=1, sequence=17):
        d = self.dut
        for key, value in dict(
            peer_idx=peer, sequence=sequence, len=length, error_code=code
        ).items():
            getattr(d, "initiator_tx_status_" + key).value = value
        d.initiator_tx_status_valid.value = 1
        for _ in range(50000):
            await RisingEdge(d.clk)
            fire = int(d.initiator_tx_status_ready.value)
            await Timer(1, unit="ns")
            if fire:
                d.initiator_tx_status_valid.value = 0
                return
        raise AssertionError("TX status handshake did not complete")

    async def respond(self, req, code=0, data=0, length=None):
        d = self.dut
        values = dict(
            kind=req["kind"],
            op=req["op"],
            peer_idx=req["peer_idx"],
            sequence=req["sequence"],
            last=req["last"],
            transferred_len=req["len"] if length is None else length,
            error=bool(code),
            error_code=code,
            rdata=data,
        )
        for key, value in values.items():
            getattr(d, "responder_cpl_" + key).value = value
        d.responder_cpl_valid.value = 1
        for _ in range(50000):
            await RisingEdge(d.clk)
            fire = int(d.responder_cpl_ready.value)
            await Timer(1, unit="ns")
            if fire:
                d.responder_cpl_valid.value = 0
                return
        raise AssertionError("Responder completion handshake did not complete")

    async def recv_eth(self):
        return bytes((await with_timeout(self.eth_sink.recv(), 2, "ms")).tdata)

    async def recv_data(self):
        return await with_timeout(self.data_sink.recv(), 2, "ms")

    async def completion(self):
        return await with_timeout(self.completions.get(), 2, "ms")

    async def request(self):
        return await with_timeout(self.requests.get(), 2, "ms")


@cocotb.test(timeout_time=3000, timeout_unit="us")
async def test_rmem_initiator_and_error_mapping(dut):
    tb = TB(dut)
    await tb.reset()
    for op in [0, 1]:
        await tb.command(kind=1, op=op, peer=2, addr=0x1004, data=0x12345678, biten=5)
        packet = await tb.recv_eth()
        rid = int.from_bytes(packet[16:20], "little")
        assert packet == frame(
            0x20 if op else 0x10,
            rid,
            0x1004,
            *([5, 0x12345678] if op else []),
            dst=MACS[2],
            src=LOCAL
        )
        await tb.eth_source.send(
            AxiStreamFrame(
                frame(
                    0x21 if op else 0x11,
                    rid,
                    *([] if op else [0x89ABCDEF]),
                    src=MACS[2],
                    padded=True
                )
            )
        )
        done = await tb.completion()
        assert not done["error"]
        if not op:
            assert done["rdata"] == 0x89ABCDEF
    for cause in [1, 2, 3, 4, 5, 6, 7, 0, 8, 0x10000006]:
        await tb.command(kind=1, peer=2)
        packet = await tb.recv_eth()
        rid = int.from_bytes(packet[16:20], "little")
        await tb.eth_source.send(AxiStreamFrame(frame(0xFF, rid, cause, src=MACS[2])))
        done = await tb.completion()
        assert done["error_code"] == (cause + 8 if 1 <= cause <= 7 else 1)


@cocotb.test(timeout_time=3000, timeout_unit="us")
async def test_dma_initiator_streaming_and_terminal_status(dut):
    tb = TB(dut)
    await tb.reset()
    tb.eth_sink.set_pause_generator(cycle([0, 1, 0, 0]))
    for length in [1, 3, 4, 5, 31, 64, 8160]:
        payload = bytes((n * 17 + 3) & 255 for n in range(length))
        await tb.command(op=1, peer=1, length=length, last=0)
        await tb.data_source.send(AxiStreamFrame(payload, tid=17, tdest=1, tuser=0))
        await with_timeout(tb.data_source.wait(), 500, "us")
        await tb.cycles(10)
        assert tb.eth_sink.empty(), "EndOfData was emitted before final memory status"
        await tb.source_status(length)
        packet = await tb.recv_eth()
        rid = int.from_bytes(packet[16:20], "little")
        assert packet == frame(
            0x40, rid, 0x1000, length, data=payload, eod=True, dst=MACS[1], src=LOCAL
        )
        await tb.eth_source.send(AxiStreamFrame(frame(0x41, rid, src=MACS[1])))
        done = await tb.completion()
        assert not done["error"] and done["transferred_len"] == length
    for cause in [4, 5, 2]:
        await tb.command(op=1, peer=1, length=12)
        await tb.data_source.send(AxiStreamFrame(b"abcdefghijkl", tid=17, tdest=1, tuser=1))
        await with_timeout(tb.data_source.wait(), 500, "us")
        await tb.source_status(12, cause)
        packet = await tb.recv_eth()
        assert not packet.endswith(EOD)
        done = await tb.completion()
        assert done["error_code"] == cause


@cocotb.test(timeout_time=3000, timeout_unit="us")
async def test_dma_read_response_framing(dut):
    tb = TB(dut)
    await tb.reset()
    for length in [1, 3, 4, 5, 63, 8160]:
        payload = bytes((n * 7 + 11) & 255 for n in range(length))
        await tb.command(peer=0, length=length, last=0)
        packet = await tb.recv_eth()
        rid = int.from_bytes(packet[16:20], "little")
        assert packet == frame(0x30, rid, 0x1000, length, dst=MACS[0], src=LOCAL)
        await tb.eth_source.send(
            AxiStreamFrame(frame(0x31, rid, data=payload, eod=True, padded=True))
        )
        data = await tb.recv_data()
        assert bytes(data.tdata) == payload and data.tid == 17 and data.tuser == 0
        done = await tb.completion()
        assert not done["error"] and done["transferred_len"] == length
    for bad in ["short", "marker", "extra"]:
        await tb.command(peer=0, length=12)
        packet = await tb.recv_eth()
        rid = int.from_bytes(packet[16:20], "little")
        reply = frame(0x31, rid, data=b"abcdefghijkl", eod=True)
        reply = (
            reply[:-8]
            if bad == "short"
            else reply[:-4] + b"bad!" if bad == "marker" else reply + b"extra"
        )
        await tb.eth_source.send(AxiStreamFrame(reply))
        done = await tb.completion()
        assert done["error_code"] == 10
        while not tb.data_sink.empty():
            await tb.data_sink.recv()


@cocotb.test(timeout_time=3000, timeout_unit="us")
async def test_responder_rmem_bulk_and_multicast(dut):
    tb = TB(dut)
    await tb.reset()
    for cmd, params in [(0x10, [41, 0x1004]), (0x20, [42, 0x1004, 5, 0x12345678])]:
        await tb.eth_source.send(AxiStreamFrame(frame(cmd, *params, src=MACS[2], padded=True)))
        req = await tb.request()
        assert req["kind"] == 1 and req["biten"] == (5 if cmd == 0x20 else req["biten"])
        await tb.respond(req, data=0xFEDCBA98)
        assert await tb.recv_eth() == frame(
            cmd | 1, params[0], *([0xFEDCBA98] if cmd == 0x10 else []), dst=MACS[2], src=LOCAL
        )
    for multicast in [False, True]:
        await tb.eth_source.send(
            AxiStreamFrame(
                frame(
                    0x40,
                    51,
                    0x1003,
                    7,
                    data=b"1234567",
                    eod=True,
                    src=MACS[0],
                    dst=GROUP if multicast else LOCAL,
                )
            )
        )
        req = await tb.request()
        assert req["rx_status"] == 1 and req["addr"] == 0x1003 and req["len"] == 7
        data = await tb.recv_data()
        assert bytes(data.tdata) == b"1234567" and data.tuser == 3
        status = await with_timeout(tb.rx_status.get(), 100, "us")
        assert status["error_code"] == 0 and status["len"] == 7
        await tb.respond(req)
        if multicast:
            await tb.cycles(50)
            assert tb.eth_sink.empty()
        else:
            assert await tb.recv_eth() == frame(0x41, 51, dst=MACS[0], src=LOCAL)
    await tb.eth_source.send(AxiStreamFrame(frame(0x30, 61, 0x1000, 5, src=MACS[1])))
    req = await tb.request()
    await tb.data_source.send(AxiStreamFrame(b"abcde", tid=req["sequence"], tdest=1, tuser=3))
    await with_timeout(tb.data_source.wait(), 500, "us")
    await tb.cycles(5)
    assert tb.eth_sink.empty()
    await tb.respond(req)
    assert await tb.recv_eth() == frame(0x31, 61, data=b"abcde", eod=True, dst=MACS[1], src=LOCAL)


@cocotb.test(timeout_time=3000, timeout_unit="us")
async def test_busy_responder_does_not_block_reply(dut):
    tb = TB(dut)
    await tb.reset()
    await tb.command(kind=1, peer=2)
    pkt = await tb.recv_eth()
    rid = int.from_bytes(pkt[16:20], "little")
    dut.responder_req_ready.value = 0
    await tb.eth_source.send(AxiStreamFrame(frame(0x10, 999, 0x1000, src=MACS[2])))
    await tb.eth_source.send(AxiStreamFrame(frame(0x11, rid, 0x12345678, src=MACS[2])))
    done = await tb.completion()
    assert not done["error"] and done["rdata"] == 0x12345678
    assert tb.requests.empty() and tb.eth_sink.empty()


@cocotb.test(timeout_time=3000, timeout_unit="us")
async def test_timeout_snapshot_late_reply_and_reset(dut):
    tb = TB(dut)
    await tb.reset()
    dut.rmem_timeout.value = 50
    tb.eth_sink.pause = True
    await tb.command(kind=1, peer=2)
    await tb.cycles(100)
    assert tb.completions.empty()
    dut.rmem_timeout.value = 0
    tb.eth_sink.pause = False
    pkt = await tb.recv_eth()
    rid = int.from_bytes(pkt[16:20], "little")
    assert (await tb.completion())["error_code"] == 8
    await tb.eth_source.send(AxiStreamFrame(frame(0x11, rid, 0x11111111, src=MACS[2])))
    await tb.command(kind=1, peer=2)
    pkt = await tb.recv_eth()
    rid2 = int.from_bytes(pkt[16:20], "little")
    assert rid2 == rid + 1
    await tb.cycles(100)
    assert tb.completions.empty()
    await tb.eth_source.send(AxiStreamFrame(frame(0x11, rid2, 0x22222222, src=MACS[2])))
    assert (await tb.completion())["rdata"] == 0x22222222
    await tb.reset()
    await tb.command(kind=1, peer=2)
    assert int.from_bytes((await tb.recv_eth())[16:20], "little") == 0


@cocotb.test(timeout_time=3000, timeout_unit="us")
async def test_raw_filters_claim_and_passthrough(dut):
    tb = TB(dut)
    await tb.reset()
    for mode in range(4):
        dut.receive_mode.value = mode
        for dst in [LOCAL, 0xFFFFFFFFFFFF, GROUP, MACS[1]]:
            packet = raw(dst=dst, data=bytes(range(77)))
            accepted = (
                mode == 3
                or mode >= 1
                and dst in [LOCAL, 0xFFFFFFFFFFFF]
                or mode == 2
                and dst == GROUP
            )
            await tb.eth_source.send(AxiStreamFrame(packet))
            await tb.eth_source.wait()
            if accepted:
                assert bytes((await tb.recv_data()).tdata) == packet
            else:
                await tb.cycles(10)
                assert tb.data_sink.empty()
    dut.receive_mode.value = 3
    dut.raw_available.value = 1
    packet = raw(data=b"claimed")
    await tb.eth_source.send(AxiStreamFrame(packet))
    data = await tb.recv_data()
    assert bytes(data.tdata) == packet and data.tdest == 4 and tb.raw_claims == 1
    packet = raw(data=b"wrong magic", ethertype=b"\x88\xb5")
    await tb.eth_source.send(AxiStreamFrame(packet))
    assert bytes((await tb.recv_data()).tdata) == packet
    packet = raw(data=bytes(range(89)))
    await tb.data_source.send(AxiStreamFrame(packet, tdest=8))
    assert await tb.recv_eth() == packet


@cocotb.test(timeout_time=3000, timeout_unit="us")
async def test_multicast_initiator_and_local_failure(dut):
    tb = TB(dut)
    await tb.reset()
    dut.dma_timeout.value = 1
    await tb.command(op=1, peer=3, length=5)
    await tb.data_source.send(AxiStreamFrame(b"hello", tid=17, tdest=3, tuser=1))
    await with_timeout(tb.data_source.wait(), 500, "us")
    await tb.source_status(5, peer=3)
    pkt = await tb.recv_eth()
    assert pkt == frame(0x40, 0, 0x1000, 5, data=b"hello", eod=True, dst=GROUP, src=LOCAL)
    done = await tb.completion()
    assert not done["error"] and done["transferred_len"] == 5
    await tb.command(op=0, peer=3, length=4)
    assert (await tb.completion())["error_code"] == 1
    assert tb.eth_sink.empty()
    tb.macs[2] = GROUP
    dut.peer_mac.value = sum(mac << (48 * n) for n, mac in enumerate(tb.macs))
    dut.rmem_timeout.value = 1
    await tb.command(kind=1, op=1, peer=2, biten=5, data=0xDEADBEEF)
    pkt = await tb.recv_eth()
    assert pkt == frame(0x20, 2, 0x1000, 5, 0xDEADBEEF, dst=GROUP, src=LOCAL)
    assert not (await tb.completion())["error"]


@cocotb.test(timeout_time=3000, timeout_unit="us")
async def test_malformed_requests_and_response_headers(dut):
    tb = TB(dut)
    await tb.reset()
    for packet in [
        frame(0x10, 77, src=MACS[2]),
        frame(0x10, 78, 0x1000, src=MACS[2]) + b"extra",
        frame(0x30, 79, 0x1000, 0, src=MACS[1]),
        frame(0x30, 80, 0x1000, 8161, src=MACS[1]),
        frame(0x10, 81, 0x1001, src=MACS[2]),
    ]:
        await tb.eth_source.send(AxiStreamFrame(packet))
        req = await tb.request()
        assert req["error_code"] in [1, 2, 3]
        await tb.respond(req, code=req["error_code"], length=0)
        assert await tb.recv_eth() == frame(
            0xFF,
            int.from_bytes(packet[16:20], "little"),
            req["error_code"],
            dst=int.from_bytes(packet[6:12], "big"),
            src=LOCAL,
        )
    await tb.command(kind=1, peer=2)
    pkt = await tb.recv_eth()
    rid = int.from_bytes(pkt[16:20], "little")
    await tb.eth_source.send(AxiStreamFrame(frame(0x11, rid, src=MACS[2])))
    assert (await tb.completion())["error_code"] == 2
    await tb.eth_source.send(AxiStreamFrame(frame(0x10, 100, 0x1000, src=0x020E0CABCDEF)))
    await tb.eth_source.send(AxiStreamFrame(frame(0x80, 101, src=MACS[2])))
    await tb.eth_source.wait()
    await tb.cycles(40)
    assert tb.requests.empty() and tb.eth_sink.empty() and tb.data_sink.empty()


@cocotb.test(timeout_time=3000, timeout_unit="us")
async def test_late_receive_error_after_payload_last(dut):
    tb = TB(dut)
    await tb.reset()
    for multicast in [False, True]:
        packet = frame(
            0x40,
            123,
            0x1000,
            8,
            data=EOD + b"ABCD",
            eod=True,
            src=MACS[0],
            dst=GROUP if multicast else LOCAL,
        )
        packet = packet[:-4] + b"bad!"
        await tb.eth_source.send(AxiStreamFrame(packet))
        req = await tb.request()
        assert req["error_code"] == 0
        assert bytes((await tb.recv_data()).tdata) == EOD + b"ABCD"
        status = await with_timeout(tb.rx_status.get(), 100, "us")
        assert status["error_code"] == 2 and status["len"] == 8
        await tb.respond(req, code=2)
        if multicast:
            await tb.cycles(40)
            assert tb.eth_sink.empty()
        else:
            assert await tb.recv_eth() == frame(0xFF, 123, 2, dst=MACS[0], src=LOCAL)
    await tb.eth_source.send(AxiStreamFrame(frame(0x30, 124, 0x1000, 4, src=MACS[1])))
    req = await tb.request()
    await tb.respond(req, code=4, length=0)
    assert await tb.recv_eth() == frame(0xFF, 124, 4, dst=MACS[1], src=LOCAL)


@cocotb.test(timeout_time=3000, timeout_unit="us")
async def test_response_timeout_during_stream_and_completion_stall(dut):
    tb = TB(dut)
    await tb.reset()
    dut.dma_timeout.value = 80
    await tb.command(peer=0, length=128)
    pkt = await tb.recv_eth()
    rid = int.from_bytes(pkt[16:20], "little")
    tb.eth_source.set_pause_generator(cycle([0] * 30 + [1] * 160))
    await tb.eth_source.send(AxiStreamFrame(frame(0x31, rid, data=bytes(range(128)), eod=True)))
    done = await tb.completion()
    assert done["error_code"] == 8
    data = await tb.recv_data()
    assert 0 < len(data.tdata) < 128
    tb.eth_source.set_pause_generator(None)
    dut.dma_timeout.value = 0
    dut.initiator_cpl_ready.value = 0
    await tb.command(peer=0, length=4)
    pkt = await tb.recv_eth()
    rid = int.from_bytes(pkt[16:20], "little")
    await tb.eth_source.send(AxiStreamFrame(frame(0x31, rid, data=b"next", eod=True)))
    await tb.recv_data()
    await tb.cycles(40)
    assert int(dut.initiator_cpl_valid.value)
    saved = tb.read_fields(
        "initiator_cpl_", ["peer_idx", "sequence", "last", "transferred_len", "error_code"]
    )
    await tb.cycles(20)
    assert (
        tb.read_fields(
            "initiator_cpl_", ["peer_idx", "sequence", "last", "transferred_len", "error_code"]
        )
        == saved
    )
    dut.initiator_cpl_ready.value = 1
    assert not (await tb.completion())["error"]


@cocotb.test(timeout_time=3000, timeout_unit="us")
async def test_local_read_failure_before_and_after_frame_start(dut):
    tb = TB(dut)
    await tb.reset()
    await tb.command(op=1, peer=1, length=12)
    await tb.source_status(0, 4)
    done = await tb.completion()
    assert done["error_code"] == 4 and tb.eth_sink.empty()
    await tb.command(op=1, peer=1, length=12)
    await tb.data_source.send(AxiStreamFrame(b"abcd", tid=17, tdest=1, tuser=1))
    await with_timeout(tb.data_source.wait(), 100, "us")
    for _ in range(100):
        await RisingEdge(dut.clk)
        await Timer(1, unit="ns")
        if int(dut.eth_tx_if.tvalid.value):
            break
    else:
        raise AssertionError("TX did not start before the injected late read error")
    await tb.source_status(4, 5)
    assert not (await tb.recv_eth()).endswith(EOD)
    assert (await tb.completion())["error_code"] == 5
    await tb.eth_source.send(AxiStreamFrame(frame(0x30, 150, 0x1000, 4, src=MACS[1])))
    req = await tb.request()
    await tb.respond(req, code=4, length=4)
    await tb.data_source.send(AxiStreamFrame(b"data", tid=req["sequence"], tdest=1, tuser=3))
    assert await tb.recv_eth() == frame(0xFF, 150, 4, dst=MACS[1], src=LOCAL)
    await tb.eth_source.send(AxiStreamFrame(frame(0x30, 151, 0x1000, 4, src=MACS[1])))
    req = await tb.request()
    await tb.data_source.send(AxiStreamFrame(b"next", tid=req["sequence"], tdest=1, tuser=3))
    await with_timeout(tb.data_source.wait(), 100, "us")
    await tb.respond(req)
    assert await tb.recv_eth() == frame(0x31, 151, data=b"next", eod=True, dst=MACS[1], src=LOCAL)


@cocotb.test(timeout_time=3000, timeout_unit="us")
async def test_independent_roles_with_equal_peer_and_sequence(dut):
    tb = TB(dut)
    await tb.reset()
    await tb.command(peer=0, length=7, sequence=17)
    own = await tb.recv_eth()
    rid = int.from_bytes(own[16:20], "little")
    dut.dut.responder_sequence_reg.value = 17
    await tb.eth_source.send(AxiStreamFrame(frame(0x40, 200, 0x1000, 7, data=b"write!!", eod=True)))
    req = await tb.request()
    assert req["peer_idx"] == 0 and req["sequence"] == 17
    data = await tb.recv_data()
    assert bytes(data.tdata) == b"write!!" and data.tid == 17 and data.tuser == 3
    await with_timeout(tb.rx_status.get(), 100, "us")
    await tb.respond(req)
    assert await tb.recv_eth() == frame(0x41, 200, dst=MACS[0], src=LOCAL)
    assert tb.completions.empty()
    await tb.eth_source.send(AxiStreamFrame(frame(0x31, rid, data=b"read!!!", eod=True)))
    data = await tb.recv_data()
    assert bytes(data.tdata) == b"read!!!" and data.tid == 17 and data.tuser == 1
    assert not (await tb.completion())["error"]


@cocotb.test(timeout_time=3000, timeout_unit="us")
async def test_request_id_wrap_and_response_on_timeout_edge(dut):
    tb = TB(dut)
    await tb.reset()
    dut.dut.request_id_reg.value = 0xFFFFFFFF
    for expected in [0xFFFFFFFF, 0]:
        await tb.command(kind=1, peer=2)
        pkt = await tb.recv_eth()
        assert int.from_bytes(pkt[16:20], "little") == expected
        await tb.eth_source.send(AxiStreamFrame(frame(0x11, expected, 1, src=MACS[2])))
        assert not (await tb.completion())["error"]
    dut.rmem_timeout.value = 500
    await tb.command(kind=1, peer=2)
    pkt = await tb.recv_eth()
    rid = int.from_bytes(pkt[16:20], "little")
    await tb.eth_source.send(AxiStreamFrame(frame(0x11, rid, 0x1234, src=MACS[2])))
    for _ in range(1000):
        await tb.cycles()
        if int(dut.dut.rx_state_reg.value) == 13:
            break
    else:
        raise AssertionError("Response did not reach terminal validation")
    dut.dut.timer_count_reg.value = 499
    assert not (await tb.completion())["error"]


@cocotb.test(timeout_time=3000, timeout_unit="us")
async def test_registered_outputs_between_clock_edges(dut):
    """Handshake, status, and payload outputs remain stable between rising edges."""
    tb = TB(dut)
    await tb.reset()
    output_names = [
        "initiator_req_ready",
        "initiator_cpl_valid",
        "initiator_cpl_kind",
        "initiator_cpl_op",
        "initiator_cpl_peer_idx",
        "initiator_cpl_sequence",
        "initiator_cpl_last",
        "initiator_cpl_transferred_len",
        "initiator_cpl_error",
        "initiator_cpl_error_code",
        "initiator_cpl_rdata",
        "initiator_tx_status_ready",
        "initiator_rx_status_ready",
        "responder_req_valid",
        "responder_req_kind",
        "responder_req_op",
        "responder_req_addr",
        "responder_req_len",
        "responder_req_peer_idx",
        "responder_req_sequence",
        "responder_req_last",
        "responder_req_biten",
        "responder_req_wdata",
        "responder_req_error_code",
        "responder_req_rx_status",
        "responder_cpl_ready",
        "responder_tx_status_valid",
        "responder_tx_status_peer_idx",
        "responder_tx_status_sequence",
        "responder_tx_status_len",
        "responder_tx_status_error_code",
        "responder_rx_status_valid",
        "responder_rx_status_peer_idx",
        "responder_rx_status_sequence",
        "responder_rx_status_len",
        "responder_rx_status_error_code",
        "lookup_req_valid",
        "lookup_req_type",
        "lookup_req_mode_mask",
        "lookup_req_peer_idx",
        "lookup_req_rmem_addr",
        "lookup_req_mac_addr",
        "lookup_rsp_ready",
        "raw_claim_valid",
    ]
    outputs = [getattr(dut, name) for name in output_names]
    for bus in [dut.eth_tx_if, dut.local_rx_if]:
        outputs += [
            getattr(bus, name)
            for name in ["tdata", "tkeep", "tstrb", "tvalid", "tlast", "tid", "tdest", "tuser"]
        ]
    outputs += [dut.eth_rx_if.tready, dut.local_tx_if.tready]
    inputs = [
        getattr(dut, name)
        for name in [
            "raw_available",
            "raw_claim_ready",
            "initiator_req_valid",
            "initiator_cpl_ready",
            "initiator_rx_status_valid",
            "responder_req_ready",
            "responder_cpl_valid",
            "responder_rx_status_ready",
            "lookup_req_ready",
        ]
    ]
    inputs += [dut.eth_tx_if.tready, dut.local_rx_if.tready]
    await tb.command(op=1, peer=1, length=64)
    payload = bytes(range(64))

    async def source():
        await tb.data_source.send(AxiStreamFrame(payload, tid=17, tdest=1, tuser=1))
        await tb.data_source.wait()
        await tb.source_status(len(payload))

    work = cocotb.start_soon(source())
    for _ in range(64):
        await FallingEdge(dut.clk)
        await Timer(1, unit="ns")
        before = [int(signal.value) for signal in outputs]
        saved = [int(signal.value) for signal in inputs]
        for signal, value in zip(inputs, saved):
            signal.value = value ^ ((1 << len(signal)) - 1)
        await Timer(1, unit="ns")
        assert [int(signal.value) for signal in outputs] == before
        for signal, value in zip(inputs, saved):
            signal.value = value
        await Timer(1, unit="ns")
        assert [int(signal.value) for signal in outputs] == before
    await work
    packet = await tb.recv_eth()
    rid = int.from_bytes(packet[16:20], "little")
    assert packet == frame(0x40, rid, 0x1000, 64, data=payload, eod=True, dst=MACS[1], src=LOCAL)
    await tb.eth_source.send(AxiStreamFrame(frame(0x41, rid, src=MACS[1])))
    assert not (await tb.completion())["error"]


@pytest.mark.parametrize("local_data_w,eth_data_w", [(32, 32), (64, 8), (32, 64)])
def test_openenoc_endpoint_oetp_engine(request, local_data_w, eth_data_w):
    tests = Path(__file__).resolve().parent
    repo = tests.parents[2]
    core = repo / "hw/rtl/core"
    taxi = repo / "libs/taxi/src"
    sources = [
        repo / "build/hal/rtl/openenoc_endpoint_if.sv",
        taxi / "axis/rtl/taxi_axis_if.sv",
        taxi / "axis/rtl/taxi_axis_adapter.sv",
        core / "openenoc_peer_lookup_if.sv",
        taxi / "axis/rtl/taxi_axis_register.sv",
        core / "openenoc_dma_transfer_if.sv",
        core / "openenoc_endpoint_oetp_engine.sv",
        tests / "test_openenoc_endpoint_oetp_engine.sv",
    ]
    cocotb_test.simulator.run(
        simulator="verilator",
        verilog_sources=[str(p) for p in sources],
        toplevel="test_openenoc_endpoint_oetp_engine",
        module="test_openenoc_endpoint_oetp_engine",
        python_search=[str(tests)],
        parameters={"LOCAL_DATA_W": local_data_w, "ETH_DATA_W": eth_data_w},
        timescale="1ns/1ps",
        extra_args=["-Wall", str(repo / "dv/common/config.vlt")],
        sim_build=str(tests / "sim_build" / request.node.name),
    )
