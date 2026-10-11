# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: AGPL-3.0-or-later

import os
from itertools import cycle

import pytest
import cocotb
import cocotb_test.simulator
from cocotb.clock import Clock
from cocotb.queue import Queue
from cocotb.triggers import FallingEdge, RisingEdge, Timer, with_timeout
from cocotbext.axi import (
    AxiBus,
    AxiRam,
    AxiStreamBus,
    AxiStreamFrame,
    AxiStreamSink,
    AxiStreamSource,
)

DMA_OP_READ = 0
DMA_OP_WRITE = 1
ROUTE_PEER = 0
ROUTE_NON_OETP_DMA = 1
TRANSFER_ROLE_INITIATOR = 0
TRANSFER_ROLE_RESPONDER = 1
PEER_IDX_W = 2

NUM_OF_PEERS = 4
MAX_RAW_FRAME_SIZE = int(os.getenv("PARAM_MAX_RAW_FRAME_SIZE", "96"))
MAX_DMA_FRAGMENT_SIZE_BYTES = ((MAX_RAW_FRAME_SIZE - 32) // 4) * 4


def packed_field(signal, index, width):
    return (int(signal.value) >> (index * width)) & ((1 << width) - 1)


class TB:
    def __init__(self, dut):
        self.dut = dut
        self.requests = Queue()
        self.peers = [
            {
                "local_addr": 0,
                "remote_addr": 0,
                "size": 0,
                "mode": 0,
                "irq_enable": 0,
            }
            for _ in range(NUM_OF_PEERS)
        ]

        cocotb.start_soon(Clock(dut.clk, 10, unit="ns").start())
        self.ram = AxiRam(
            AxiBus.from_entity(dut.m_axi_if),
            dut.clk,
            dut.rst,
            size=0x10000,
        )
        self.oetp_source = AxiStreamSource(
            AxiStreamBus.from_entity(dut.s_axis_oetp_if), dut.clk, dut.rst
        )
        self.oetp_sink = AxiStreamSink(
            AxiStreamBus.from_entity(dut.m_axis_oetp_if), dut.clk, dut.rst
        )

    def drive_peer_config(self):
        local_address = 0
        remote_address = 0
        size = 0
        dma_mode = 0
        irq_enable = 0

        for index, peer in enumerate(self.peers):
            local_address |= peer["local_addr"] << (index * 32)
            remote_address |= peer["remote_addr"] << (index * 32)
            size |= peer["size"] << (index * 32)
            dma_mode |= peer["mode"] << (index * 2)
            irq_enable |= peer["irq_enable"] << index

        self.dut.peer_local_address.value = local_address
        self.dut.peer_remote_address.value = remote_address
        self.dut.peer_size.value = size
        self.dut.peer_dma_mode.value = dma_mode
        self.dut.peer_irq_enable.value = irq_enable

    def drive_lookup_response(self, peer_idx, mode_mask):
        peer = self.peers[peer_idx]
        hit = bool(mode_mask & (1 << peer["mode"]))

        self.dut.peer_lookup_rsp_hit.value = hit
        self.dut.peer_lookup_rsp_peer_idx.value = peer_idx if hit else 0
        self.dut.peer_lookup_rsp_mac_addr.value = 0
        self.dut.peer_lookup_rsp_rmem_offset.value = 0
        self.dut.peer_lookup_rsp_local_addr.value = peer["local_addr"] if hit else 0
        self.dut.peer_lookup_rsp_remote_addr.value = peer["remote_addr"] if hit else 0
        self.dut.peer_lookup_rsp_size.value = peer["size"] if hit else 0
        self.dut.peer_lookup_rsp_dma_mode.value = peer["mode"] if hit else 0
        self.dut.peer_lookup_rsp_irq_enable.value = peer["irq_enable"] if hit else 0

    async def peer_lookup_responder(self):
        while True:
            await RisingEdge(self.dut.clk)

            reset = int(self.dut.rst.value)
            request_fire = int(self.dut.peer_lookup_req_valid.value) and int(
                self.dut.peer_lookup_req_ready.value
            )
            response_fire = int(self.dut.peer_lookup_rsp_valid.value) and int(
                self.dut.peer_lookup_rsp_ready.value
            )
            request_type = int(self.dut.peer_lookup_req_type.value)
            peer_idx = int(self.dut.peer_lookup_req_peer_idx.value)
            mode_mask = int(self.dut.peer_lookup_req_mode_mask.value)

            await Timer(1, unit="ns")

            if reset:
                self.dut.peer_lookup_rsp_valid.value = 0
                continue

            if response_fire:
                self.dut.peer_lookup_rsp_valid.value = 0

            if request_fire:
                assert request_type == 0
                assert peer_idx < NUM_OF_PEERS
                self.drive_lookup_response(peer_idx, mode_mask)
                self.dut.peer_lookup_rsp_valid.value = 1

    async def reset(self):
        self.dut.non_oetp_rx_claim_valid.setimmediatevalue(0)
        self.dut.non_tx_buffer_address.setimmediatevalue(0)
        self.dut.non_tx_frame_length.setimmediatevalue(0)
        self.dut.non_tx_request.setimmediatevalue(0)
        self.dut.non_tx_clear_errors.setimmediatevalue(0)
        self.dut.non_rx_buffer_address.setimmediatevalue(0)
        self.dut.non_rx_buffer_capacity.setimmediatevalue(0)
        self.dut.non_rx_request.setimmediatevalue(0)
        self.dut.non_rx_clear_errors.setimmediatevalue(0)
        self.dut.peer_request.setimmediatevalue(0)
        self.dut.dma_max_fragment_size_bytes.setimmediatevalue(64)
        self.dut.peer_clear_error.setimmediatevalue(0)
        self.dut.rmem_error_valid.setimmediatevalue(0)
        self.dut.rmem_error_peer_idx.setimmediatevalue(0)
        self.dut.rmem_error_code.setimmediatevalue(0)
        self.dut.wire_error_enable.setimmediatevalue(0)
        self.dut.wire_error_code.setimmediatevalue(0)
        self.drive_peer_config()

        self.dut.peer_lookup_req_ready.setimmediatevalue(1)
        self.dut.peer_lookup_rsp_valid.setimmediatevalue(0)
        self.dut.peer_lookup_rsp_hit.setimmediatevalue(0)
        self.dut.peer_lookup_rsp_peer_idx.setimmediatevalue(0)
        self.dut.peer_lookup_rsp_mac_addr.setimmediatevalue(0)
        self.dut.peer_lookup_rsp_rmem_offset.setimmediatevalue(0)
        self.dut.peer_lookup_rsp_local_addr.setimmediatevalue(0)
        self.dut.peer_lookup_rsp_remote_addr.setimmediatevalue(0)
        self.dut.peer_lookup_rsp_size.setimmediatevalue(0)
        self.dut.peer_lookup_rsp_dma_mode.setimmediatevalue(0)
        self.dut.peer_lookup_rsp_irq_enable.setimmediatevalue(0)

        self.dut.initiator_req_ready.setimmediatevalue(1)
        self.dut.initiator_cpl_valid.setimmediatevalue(0)
        self.dut.initiator_cpl_op.setimmediatevalue(0)
        self.dut.initiator_cpl_kind.setimmediatevalue(0)
        self.dut.initiator_cpl_transferred_len.setimmediatevalue(0)
        self.dut.initiator_cpl_peer_idx.setimmediatevalue(0)
        self.dut.initiator_cpl_sequence.setimmediatevalue(0)
        self.dut.initiator_cpl_last.setimmediatevalue(0)
        self.dut.initiator_cpl_error.setimmediatevalue(0)
        self.dut.initiator_cpl_error_code.setimmediatevalue(0)

        self.dut.responder_req_valid.setimmediatevalue(0)
        self.dut.responder_req_op.setimmediatevalue(0)
        self.dut.responder_req_kind.setimmediatevalue(0)
        self.dut.responder_req_biten.setimmediatevalue(0)
        self.dut.responder_req_wdata.setimmediatevalue(0)
        self.dut.responder_req_addr.setimmediatevalue(0)
        self.dut.responder_req_len.setimmediatevalue(0)
        self.dut.responder_req_peer_idx.setimmediatevalue(0)
        self.dut.responder_req_sequence.setimmediatevalue(0)
        self.dut.responder_req_last.setimmediatevalue(0)
        self.dut.responder_cpl_ready.setimmediatevalue(1)

        self.dut.irq_admit_ready.setimmediatevalue(0b111)
        self.dut.irq_admit_reserved.setimmediatevalue(0b111)
        self.dut.irq_commit_ready.setimmediatevalue(0b111)
        self.dut.event_enable.setimmediatevalue(0)
        self.dut.responder_irq_admit_ready.setimmediatevalue(1)
        self.dut.responder_irq_commit_ready.setimmediatevalue(1)

        cocotb.start_soon(self.peer_lookup_responder())
        cocotb.start_soon(self.monitor_requests())

        self.dut.rst.setimmediatevalue(1)
        for _ in range(5):
            await RisingEdge(self.dut.clk)
        self.dut.rst.value = 0
        for _ in range(3):
            await RisingEdge(self.dut.clk)
        await Timer(1, unit="ns")

    async def wait_signal(self, signal, value=1, cycles=4000):
        for _ in range(cycles):
            await RisingEdge(self.dut.clk)
            await Timer(1, unit="ns")
            if int(signal.value) == value:
                return
        raise AssertionError(f"{signal._name} did not reach {value}")

    async def request_non_tx(self, address, length):
        self.dut.non_tx_buffer_address.value = address
        self.dut.non_tx_frame_length.value = length
        self.dut.non_tx_request.value = 1
        await self.wait_signal(self.dut.non_tx_request_hwclr)
        self.dut.non_tx_request.value = 0

    async def request_non_rx(self, address, capacity):
        self.dut.non_rx_buffer_address.value = address
        self.dut.non_rx_buffer_capacity.value = capacity
        self.dut.non_rx_request.value = 1
        await self.wait_signal(self.dut.non_rx_request_hwclr)
        self.dut.non_rx_request.value = 0

    async def clear_non_errors(self, channel):
        command = getattr(self.dut, f"non_{channel}_clear_errors")
        acknowledge = getattr(self.dut, f"non_{channel}_clear_errors_hwclr")
        await FallingEdge(self.dut.clk)
        command.value = 1
        await Timer(1, unit="ns")
        assert int(acknowledge.value) == 0
        await RisingEdge(self.dut.clk)
        await Timer(1, unit="ns")
        assert int(acknowledge.value) == 1
        command.value = 0

    async def write_peer(
        self,
        index,
        *,
        local_addr,
        remote_addr,
        size,
        mode,
        irq_enable=1,
        request=0,
    ):
        self.peers[index] = {
            "local_addr": local_addr,
            "remote_addr": remote_addr,
            "size": size,
            "mode": mode,
            "irq_enable": irq_enable,
        }
        self.drive_peer_config()

        if request:
            self.dut.peer_request.value = 1 << index
            for _ in range(4000):
                await RisingEdge(self.dut.clk)
                await Timer(1, unit="ns")
                if (int(self.dut.peer_request_hwclr.value) >> index) & 1:
                    break
            else:
                raise AssertionError(f"peer {index} request was not accepted")
            self.dut.peer_request.value = 0

    async def wait_peer_status(self, index, *, done=0, error=0, idle=1, cycles=4000):
        for _ in range(cycles):
            await RisingEdge(self.dut.clk)
            await Timer(1, unit="ns")
            if (
                packed_field(self.dut.peer_done, index, 1) == done
                and packed_field(self.dut.peer_error, index, 1) == error
                and packed_field(self.dut.peer_idle, index, 1) == idle
            ):
                return
        raise AssertionError(f"peer {index} status did not reach expected state")

    async def report_rmem_error(self, index, code, *, clear=False):
        await FallingEdge(self.dut.clk)
        self.dut.rmem_error_peer_idx.value = index
        self.dut.rmem_error_code.value = code
        self.dut.rmem_error_valid.value = 1
        self.dut.peer_clear_error.value = (1 << index) if clear else 0
        await RisingEdge(self.dut.clk)
        await Timer(1, unit="ns")
        self.dut.rmem_error_valid.value = 0
        self.dut.peer_clear_error.value = 0

    async def clear_peer_error(self, index):
        await FallingEdge(self.dut.clk)
        self.dut.peer_clear_error.value = 1 << index
        await Timer(1, unit="ns")
        assert not ((int(self.dut.peer_clear_error_hwclr.value) >> index) & 1)
        await RisingEdge(self.dut.clk)
        await Timer(1, unit="ns")
        assert (int(self.dut.peer_clear_error_hwclr.value) >> index) & 1
        self.dut.peer_clear_error.value = 0

    async def monitor_requests(self):
        while True:
            await RisingEdge(self.dut.clk)
            if (
                not int(self.dut.rst.value)
                and int(self.dut.initiator_req_valid.value)
                and int(self.dut.initiator_req_ready.value)
            ):
                self.requests.put_nowait(
                    {
                        "op": int(self.dut.initiator_req_op.value),
                        "addr": int(self.dut.initiator_req_addr.value),
                        "len": int(self.dut.initiator_req_len.value),
                        "peer_idx": int(self.dut.initiator_req_peer_idx.value),
                        "sequence": int(self.dut.initiator_req_sequence.value),
                        "last": int(self.dut.initiator_req_last.value),
                    }
                )

    async def receive_initiator_request(self):
        return await with_timeout(self.requests.get(), 100, "us")

    async def claim_non_rx(self):
        await self.wait_signal(self.dut.non_oetp_rx_available)
        self.dut.non_oetp_rx_claim_valid.value = 1
        while True:
            await RisingEdge(self.dut.clk)
            if int(self.dut.non_oetp_rx_claim_ready.value):
                break
        self.dut.non_oetp_rx_claim_valid.value = 0
        await Timer(1, unit="ns")
        assert not int(self.dut.non_oetp_rx_available.value)
        assert not int(self.dut.non_rx_armed.value)

    async def complete_initiator(
        self, request, *, error=0, error_code=0, transferred_len=None, kind=0, wire_error=None
    ):
        if transferred_len is None:
            transferred_len = 0 if error else request["len"]

        self.dut.initiator_cpl_op.value = request["op"]
        self.dut.initiator_cpl_kind.value = kind
        self.dut.initiator_cpl_transferred_len.value = transferred_len
        self.dut.initiator_cpl_peer_idx.value = request["peer_idx"]
        self.dut.initiator_cpl_sequence.value = request["sequence"]
        self.dut.initiator_cpl_last.value = request["last"]
        self.dut.initiator_cpl_error.value = error
        self.dut.initiator_cpl_error_code.value = error_code
        self.dut.wire_error_enable.value = int(wire_error is not None)
        self.dut.wire_error_code.value = 0 if wire_error is None else wire_error
        self.dut.initiator_cpl_valid.value = 1

        for _ in range(1000):
            await RisingEdge(self.dut.clk)
            if int(self.dut.initiator_cpl_ready.value):
                break
        else:
            raise AssertionError("initiator completion timed out")

        self.dut.initiator_cpl_valid.value = 0
        self.dut.wire_error_enable.value = 0

    async def send_responder_request(
        self, *, op, addr, length, peer_idx, sequence, last, kind=0, biten=0, wdata=0
    ):
        if not kind and length and peer_idx < len(self.peers):
            config = self.peers[peer_idx]
            if (
                config["mode"] != (2 if op else 3)
                or addr < config["local_addr"]
                or addr + length > config["local_addr"] + config["size"]
            ):
                await self.write_peer(
                    peer_idx,
                    local_addr=addr,
                    remote_addr=0,
                    size=length,
                    mode=2 if op else 3,
                    irq_enable=config["irq_enable"],
                )
        self.dut.responder_req_op.value = op
        self.dut.responder_req_kind.value = kind
        self.dut.responder_req_biten.value = biten
        self.dut.responder_req_wdata.value = wdata
        self.dut.responder_req_addr.value = addr
        self.dut.responder_req_len.value = length
        self.dut.responder_req_peer_idx.value = peer_idx
        self.dut.responder_req_sequence.value = sequence
        self.dut.responder_req_last.value = last
        self.dut.responder_req_valid.value = 1

        for _ in range(1000):
            await RisingEdge(self.dut.clk)
            if int(self.dut.responder_req_ready.value):
                break
        else:
            raise AssertionError("responder request timed out")

        self.dut.responder_req_valid.value = 0

    async def receive_responder_completion(self):
        for _ in range(2000):
            await RisingEdge(self.dut.clk)
            if int(self.dut.responder_cpl_valid.value):
                return {
                    "op": int(self.dut.responder_cpl_op.value),
                    "transferred_len": int(self.dut.responder_cpl_transferred_len.value),
                    "peer_idx": int(self.dut.responder_cpl_peer_idx.value),
                    "sequence": int(self.dut.responder_cpl_sequence.value),
                    "last": int(self.dut.responder_cpl_last.value),
                    "error": int(self.dut.responder_cpl_error.value),
                    "error_code": int(self.dut.responder_cpl_error_code.value),
                }
        raise AssertionError("responder completion timed out")

    async def send_oetp_frame(
        self,
        data,
        *,
        peer_idx=0,
        sequence=0,
        last=1,
        route=ROUTE_PEER,
        role=TRANSFER_ROLE_INITIATOR,
    ):
        frame = AxiStreamFrame(data)
        frame.tid = sequence
        frame.tdest = (route << PEER_IDX_W) | peer_idx
        frame.tuser = (role << 1) | last
        await self.oetp_source.send(frame)
        await self.oetp_source.wait()

    async def receive_oetp_frame(self):
        return await with_timeout(self.oetp_sink.recv(), 100, "us")


def frame_bytes(frame):
    return bytes(frame.tdata)


def frame_sideband(value):
    if isinstance(value, (list, tuple)):
        assert value
        assert all(item == value[0] for item in value)
        return int(value[0])
    return int(value)


@cocotb.test()
async def test_non_oetp_dma_tx_rx_and_status(dut):
    tb = TB(dut)
    await tb.reset()

    tx_addr = 0x0113
    eth_header = bytes.fromhex("020e0c000002020e0c0000010800")
    tx_data = eth_header + bytes((index * 13 + 7) & 0xFF for index in range(39)) + bytes(7)
    tb.ram.write(tx_addr, tx_data)

    dut.irq_commit_ready.value = 0
    await tb.request_non_tx(tx_addr, len(tx_data))

    tx_frame = await tb.receive_oetp_frame()
    assert frame_bytes(tx_frame) == tx_data
    assert frame_sideband(tx_frame.tdest) == ROUTE_NON_OETP_DMA << PEER_IDX_W

    await tb.wait_signal(dut.non_tx_idle)
    assert int(dut.non_tx_done.value) == 1
    assert int(dut.non_tx_error.value) == 0
    assert int(dut.non_tx_transferred_length.value) == len(tx_data)
    assert int(dut.irq_commit_valid.value) == 0b010
    assert (int(dut.irq_commit_source.value) >> 4) & 0xF == 1

    dut.irq_commit_ready.value = 0b111
    await RisingEdge(dut.clk)

    rx_addr = 0x0205
    rx_data = eth_header + bytes((index * 9 + 3) & 0xFF for index in range(49))
    dut.irq_commit_ready.value = 0
    await tb.request_non_rx(rx_addr, 64)
    await tb.wait_signal(dut.non_rx_armed)

    await tb.claim_non_rx()
    # Reserving a descriptor does not depend on payload/FIFO readiness. A
    # delayed frame retains the reservation and a second claim cannot take it.
    dut.non_oetp_rx_claim_valid.value = 1
    for _ in range(10):
        await RisingEdge(dut.clk)
        await Timer(1, unit="ns")
        assert not int(dut.non_oetp_rx_available.value)
        assert not int(dut.non_oetp_rx_claim_ready.value)
        assert not int(dut.non_rx_idle.value)
        assert not int(dut.non_rx_done.value)
    dut.non_oetp_rx_claim_valid.value = 0
    await tb.send_oetp_frame(rx_data, route=ROUTE_NON_OETP_DMA)
    await tb.wait_signal(dut.non_rx_idle)
    assert int(dut.non_rx_done.value) == 1
    assert int(dut.non_rx_error.value) == 0
    assert int(dut.non_rx_armed.value) == 0
    assert int(dut.non_rx_received_length.value) == len(rx_data)
    assert tb.ram.read(rx_addr, len(rx_data)) == rx_data
    assert int(dut.irq_commit_valid.value) == 0b100
    assert (int(dut.irq_commit_source.value) >> 8) & 0xF == 2

    dut.irq_commit_ready.value = 0b111
    await RisingEdge(dut.clk)

    overflow_addr = 0x0281
    overflow_data = bytes((index * 3 + 0x55) & 0xFF for index in range(29))
    await tb.request_non_rx(overflow_addr, 20)
    await tb.wait_signal(dut.non_rx_armed)
    await tb.claim_non_rx()
    await tb.send_oetp_frame(overflow_data, route=ROUTE_NON_OETP_DMA)
    await tb.wait_signal(dut.non_rx_idle)
    assert int(dut.non_rx_error.value) == 1
    assert int(dut.non_rx_error_code.value) == 3
    assert int(dut.non_rx_received_length.value) == 20
    assert tb.ram.read(overflow_addr, 20) == overflow_data[:20]

    await tb.request_non_tx(tx_addr, 0)
    await tb.wait_signal(dut.non_tx_idle)
    assert int(dut.non_tx_error.value) == 1
    assert int(dut.non_tx_error_code.value) == 1


@cocotb.test()
async def test_non_oetp_sticky_errors_and_explicit_clear(dut):
    tb = TB(dut)
    await tb.reset()
    await tb.report_rmem_error(2, 8)

    await tb.request_non_tx(0x3A01, 0)
    await tb.wait_signal(dut.non_tx_error)
    assert int(dut.non_tx_error_code.value) == 1

    overflow_data = bytes(range(29))
    await tb.request_non_rx(0x3B01, 20)
    await tb.claim_non_rx()
    await tb.send_oetp_frame(overflow_data, route=ROUTE_NON_OETP_DMA)
    await tb.wait_signal(dut.non_rx_idle)
    assert int(dut.non_rx_error_code.value) == 3
    await tb.wait_signal(dut.irq_commit_valid, 0)

    # Successful transfers preserve both records and still report done/length.
    eth_header = bytes.fromhex("020e0c000002020e0c0000010800")
    data = eth_header + bytes(range(46))
    tb.ram.write(0x3A01, data)
    dut.irq_commit_ready.value = 0b001
    await tb.request_non_tx(0x3A01, len(data))
    assert int(dut.non_tx_error_code.value) == 1
    assert frame_bytes(await tb.receive_oetp_frame()) == data
    await tb.wait_signal(dut.non_tx_idle)

    await tb.request_non_rx(0x3B01, 64)
    assert int(dut.non_rx_error_code.value) == 3
    await tb.claim_non_rx()
    await tb.send_oetp_frame(data, route=ROUTE_NON_OETP_DMA)
    await tb.wait_signal(dut.non_rx_idle)
    assert tb.ram.read(0x3B01, len(data)) == data
    assert int(dut.irq_commit_valid.value) == 0b110
    assert int(dut.non_tx_done.value) == int(dut.non_rx_done.value) == 1
    assert int(dut.non_tx_error.value) == int(dut.non_rx_error.value) == 1

    await tb.clear_non_errors("tx")
    assert int(dut.non_tx_error.value) == int(dut.non_tx_error_code.value) == 0
    assert int(dut.non_rx_error_code.value) == 3
    assert int(dut.non_tx_done.value) == 1
    assert int(dut.non_tx_transferred_length.value) == len(data)
    assert int(dut.irq_commit_valid.value) == 0b110

    await tb.clear_non_errors("rx")
    assert int(dut.non_rx_error.value) == int(dut.non_rx_error_code.value) == 0
    assert int(dut.non_rx_done.value) == 1
    assert int(dut.non_rx_received_length.value) == len(data)
    assert int(dut.irq_commit_valid.value) == 0b110
    assert packed_field(dut.peer_error_code, 2, 4) == 8

    dut.irq_commit_ready.value = 0b111
    await tb.wait_signal(dut.irq_commit_valid, 0)
    await tb.request_non_tx(0x3A01, 0)
    await tb.request_non_rx(0x3B01, 0)
    await tb.wait_signal(dut.non_rx_error)

    # Clear during backpressured TX and armed RX without losing either transfer.
    tb.oetp_sink.pause = True
    await tb.request_non_tx(0x3A01, len(data))
    await tb.request_non_rx(0x3B01, 20)
    await tb.wait_signal(dut.non_rx_armed)
    await tb.clear_non_errors("tx")
    await tb.clear_non_errors("rx")
    assert int(dut.non_tx_idle.value) == 0
    assert int(dut.non_rx_idle.value) == 0
    assert int(dut.non_rx_armed.value) == 1
    assert int(dut.non_tx_error.value) == int(dut.non_rx_error.value) == 0
    await tb.claim_non_rx()
    tb.oetp_sink.pause = False
    assert frame_bytes(await tb.receive_oetp_frame()) == data
    await tb.wait_signal(dut.non_tx_idle)
    assert int(dut.non_tx_done.value) == 1
    assert int(dut.non_tx_error.value) == 0

    await tb.send_oetp_frame(overflow_data, route=ROUTE_NON_OETP_DMA)
    await tb.wait_signal(dut.non_rx_idle)
    assert int(dut.non_rx_error.value) == 1
    assert int(dut.non_rx_error_code.value) == 3
    assert int(dut.non_rx_received_length.value) == 20
    assert tb.ram.read(0x3B01, 20) == overflow_data[:20]


@cocotb.test()
async def test_non_oetp_new_failure_wins_over_clear(dut):
    tb = TB(dut)
    await tb.reset()

    for channel, irq_port, length_field in (
        ("tx", 1, "frame_length"),
        ("rx", 2, "buffer_capacity"),
    ):
        request = getattr(dut, f"non_{channel}_request")
        command = getattr(dut, f"non_{channel}_clear_errors")
        dut.irq_admit_ready.value = 0
        getattr(dut, f"non_{channel}_{length_field}").value = 0
        request.value = 1
        await tb.wait_signal(dut.irq_admit_valid, 1 << irq_port)
        await FallingEdge(dut.clk)
        command.value = 1
        dut.irq_admit_ready.value = 0b111
        await Timer(1, unit="ns")
        assert int(getattr(dut, f"non_{channel}_clear_errors_hwclr").value) == 0
        await RisingEdge(dut.clk)
        await Timer(1, unit="ns")
        assert int(getattr(dut, f"non_{channel}_clear_errors_hwclr").value) == 1
        assert int(getattr(dut, f"non_{channel}_request_hwclr").value) == 1
        assert int(getattr(dut, f"non_{channel}_error").value) == 1
        assert int(getattr(dut, f"non_{channel}_error_code").value) == 1
        command.value = 0
        request.value = 0
        await RisingEdge(dut.clk)
        await Timer(1, unit="ns")
        assert int(getattr(dut, f"non_{channel}_error").value) == 1

    dut.rst.value = 1
    dut.non_tx_clear_errors.value = dut.non_rx_clear_errors.value = 1
    await Timer(1, unit="ns")
    assert int(dut.non_tx_clear_errors_hwclr.value) == 0
    assert int(dut.non_rx_clear_errors_hwclr.value) == 0
    await RisingEdge(dut.clk)
    await Timer(1, unit="ns")
    assert int(dut.non_tx_error.value) == int(dut.non_tx_error_code.value) == 0
    assert int(dut.non_rx_error.value) == int(dut.non_rx_error_code.value) == 0


@cocotb.test()
async def test_peer_dma_fragmentation_in_both_modes(dut):
    tb = TB(dut)
    await tb.reset()

    peer_idx = 2
    local_addr = 0x1003
    remote_addr = 0x80001003
    payload = bytes((index * 17 + 5) & 0xFF for index in range(150))
    tb.ram.write(local_addr, payload)

    dut.irq_commit_ready.value = 0
    await tb.write_peer(
        peer_idx,
        local_addr=local_addr,
        remote_addr=remote_addr,
        size=len(payload),
        mode=3,
        irq_enable=1,
        request=1,
    )

    offset = 0
    for sequence, length in enumerate((64, 64, 22)):
        request = await tb.receive_initiator_request()
        assert request == {
            "op": DMA_OP_WRITE,
            "addr": remote_addr + offset,
            "len": length,
            "peer_idx": peer_idx,
            "sequence": sequence,
            "last": int(sequence == 2),
        }
        frame = await tb.receive_oetp_frame()
        assert frame_bytes(frame) == payload[offset : offset + length]
        assert frame_sideband(frame.tid) == sequence
        assert frame_sideband(frame.tdest) == peer_idx
        assert frame_sideband(frame.tuser) == int(sequence == 2)
        await tb.complete_initiator(request)
        offset += length

    await tb.wait_peer_status(peer_idx, done=1)
    await tb.wait_signal(dut.irq_commit_valid, 0b001)
    assert int(dut.irq_commit_valid.value) == 0b001
    assert packed_field(dut.irq_commit_peer_idx, 0, 2) == peer_idx

    dut.irq_commit_ready.value = 0b111
    await RisingEdge(dut.clk)

    peer_idx = 1
    local_addr = 0x2001
    remote_addr = 0x90002001
    payload = bytes((index * 7 + 0x41) & 0xFF for index in range(137))
    dut.irq_commit_ready.value = 0
    await tb.write_peer(
        peer_idx,
        local_addr=local_addr,
        remote_addr=remote_addr,
        size=len(payload),
        mode=2,
        irq_enable=1,
        request=1,
    )

    offset = 0
    for sequence, length in enumerate((64, 64, 9)):
        request = await tb.receive_initiator_request()
        assert request == {
            "op": DMA_OP_READ,
            "addr": remote_addr + offset,
            "len": length,
            "peer_idx": peer_idx,
            "sequence": sequence,
            "last": int(sequence == 2),
        }
        await tb.send_oetp_frame(
            payload[offset : offset + length],
            peer_idx=peer_idx,
            sequence=sequence,
            last=int(sequence == 2),
        )
        await tb.complete_initiator(request)
        offset += length

    await tb.wait_peer_status(peer_idx, done=1)
    await tb.wait_signal(dut.irq_commit_valid, 0b001)
    assert tb.ram.read(local_addr, len(payload)) == payload
    assert int(dut.irq_commit_valid.value) == 0b001
    assert packed_field(dut.irq_commit_peer_idx, 0, 2) == peer_idx


@cocotb.test()
async def test_configurable_fragment_size_and_snapshot(dut):
    tb = TB(dut)
    await tb.reset()
    dut.dma_max_fragment_size_bytes.value = 31
    payload = bytes((n * 13 + 7) & 255 for n in range(10 * 28 + 9))
    tb.ram.write(0x1801, payload)
    await tb.write_peer(
        0, local_addr=0x1801, remote_addr=0x80001801, size=len(payload), mode=3, request=1
    )

    # More fragments than slots ensures new descriptors are issued after the
    # CSR changes, rather than merely checking an already prepared batch.
    request = await tb.receive_initiator_request()
    pending = {request["sequence"]: request}
    dut.dma_max_fragment_size_bytes.value = 7
    observed = set()
    for _ in range(11):
        frame = await tb.receive_oetp_frame()
        sequence = frame_sideband(frame.tid)
        assert sequence not in observed and 0 <= sequence <= 10
        observed.add(sequence)
        while sequence not in pending:
            request = await tb.receive_initiator_request()
            pending[request["sequence"]] = request
        request = pending.pop(sequence)
        length = 9 if sequence == 10 else 28
        offset = sequence * 28
        assert request == {
            "op": DMA_OP_WRITE,
            "addr": 0x80001801 + offset,
            "len": length,
            "peer_idx": 0,
            "sequence": sequence,
            "last": int(sequence == 10),
        }
        assert frame_bytes(frame) == payload[offset : offset + length]
        assert frame_sideband(frame.tid) == sequence
        assert frame_sideband(frame.tuser) == int(sequence == 10)
        await tb.complete_initiator(request)
    assert observed == set(range(11)) and not pending
    await tb.wait_peer_status(0, done=1)

    # The next transfer rounds seven down to four, preserving the exact tail.
    payload = bytes(range(23))
    tb.ram.write(0x1900, b"!" * 25)
    await tb.write_peer(
        1, local_addr=0x1901, remote_addr=0x80001901, size=len(payload), mode=2, request=1
    )
    offset = 0
    for sequence, length in enumerate((4, 4, 4, 4, 4, 3)):
        request = await tb.receive_initiator_request()
        assert request == {
            "op": DMA_OP_READ,
            "addr": 0x80001901 + offset,
            "len": length,
            "peer_idx": 1,
            "sequence": sequence,
            "last": int(sequence == 5),
        }
        await tb.send_oetp_frame(
            payload[offset : offset + length], peer_idx=1, sequence=sequence, last=request["last"]
        )
        await tb.complete_initiator(request)
        offset += length
    await tb.wait_peer_status(1, done=1)
    assert tb.ram.read(0x1900, 25) == b"!" + payload + b"!"


@cocotb.test()
async def test_fragment_size_validation_and_independent_limits(dut):
    tb = TB(dut)
    await tb.reset()
    dut.irq_commit_ready.value = 0
    tb.ram.write(0x1A01, b"unchanged")
    for size in (0, 1, 2, 3, MAX_DMA_FRAGMENT_SIZE_BYTES + 4, 0xFFFFFFFF):
        dut.dma_max_fragment_size_bytes.value = size
        await tb.write_peer(2, local_addr=0x1A01, remote_addr=0x80001A01, size=9, mode=3, request=1)
        await tb.wait_peer_status(2, error=1)
        assert packed_field(dut.peer_error_code, 2, 4) == 1
        await tb.wait_signal(dut.irq_commit_valid, 1)
        assert tb.requests.empty() and tb.oetp_sink.empty()
        assert tb.ram.read(0x1A01, 9) == b"unchanged"
        dut.irq_commit_ready.value = 0b111
        await tb.wait_signal(dut.irq_commit_valid, 0)
        await tb.clear_peer_error(2)
        dut.irq_commit_ready.value = 0
    dut.irq_commit_ready.value = 0b111

    # Even an invalid local fragmentation preference cannot restrict an
    # incoming fragment up to the physical MFS, in either responder direction.
    payload = bytes(n & 255 for n in range(MAX_DMA_FRAGMENT_SIZE_BYTES))
    tb.ram.write(0x1B01, payload)
    await tb.send_responder_request(
        op=DMA_OP_READ, addr=0x1B01, length=len(payload), peer_idx=2, sequence=0x33, last=1
    )
    frame = await tb.receive_oetp_frame()
    assert frame_bytes(frame) == payload
    assert frame_sideband(frame.tuser) == 3
    completion = await tb.receive_responder_completion()
    assert completion["error"] == 0 and completion["transferred_len"] == len(payload)
    await RisingEdge(dut.clk)
    tb.ram.write(0x1C02, b"!" * (len(payload) + 2))
    await tb.send_responder_request(
        op=DMA_OP_WRITE, addr=0x1C03, length=len(payload), peer_idx=2, sequence=0x34, last=1
    )
    await tb.send_oetp_frame(payload, peer_idx=2, sequence=0x34, role=TRANSFER_ROLE_RESPONDER)
    completion = await tb.receive_responder_completion()
    assert completion["error"] == 0 and completion["transferred_len"] == len(payload)
    assert tb.ram.read(0x1C02, len(payload) + 2) == b"!" + payload + b"!"
    await RisingEdge(dut.clk)
    await tb.send_responder_request(
        op=DMA_OP_READ,
        addr=0x1B01,
        length=MAX_DMA_FRAGMENT_SIZE_BYTES + 1,
        peer_idx=2,
        sequence=0x35,
        last=1,
    )
    completion = await tb.receive_responder_completion()
    assert completion["error"] == 1 and completion["error_code"] == 1
    assert tb.oetp_sink.empty()

    # Raw frames use the synthesis-time raw ceiling and are never fragmented.
    payload = bytes(n & 255 for n in range(MAX_RAW_FRAME_SIZE))
    tb.ram.write(0x1D01, payload)
    await tb.request_non_tx(0x1D01, len(payload))
    assert frame_bytes(await tb.receive_oetp_frame()) == payload
    await tb.wait_signal(dut.non_tx_idle)
    assert int(dut.non_tx_done.value) == 1 and int(dut.non_tx_error.value) == 0
    await tb.request_non_rx(0x1E01, len(payload))
    await tb.claim_non_rx()
    await tb.send_oetp_frame(payload, route=ROUTE_NON_OETP_DMA)
    await tb.wait_signal(dut.non_rx_idle)
    assert int(dut.non_rx_done.value) == 1 and int(dut.non_rx_error.value) == 0
    assert tb.ram.read(0x1E01, len(payload)) == payload
    await tb.request_non_tx(0x1D01, MAX_RAW_FRAME_SIZE + 1)
    await tb.wait_signal(dut.non_tx_idle)
    assert int(dut.non_tx_error_code.value) == 1 and tb.oetp_sink.empty()
    await tb.request_non_rx(0x1E01, MAX_RAW_FRAME_SIZE + 1)
    await tb.wait_signal(dut.non_rx_idle)
    assert int(dut.non_rx_error_code.value) == 1 and not int(dut.non_rx_armed.value)


@cocotb.test()
async def test_fragment_size_rounding_boundaries(dut):
    tb = TB(dut)
    await tb.reset()
    for configured in (4, 5, 6, 7, MAX_DMA_FRAGMENT_SIZE_BYTES + 3):
        effective = configured & ~3
        lengths = (effective, 1) if effective == MAX_DMA_FRAGMENT_SIZE_BYTES else (4, 4, 4, 1)
        payload = bytes((n * 19 + configured) & 255 for n in range(sum(lengths)))
        tb.ram.write(0x2601, payload)
        dut.dma_max_fragment_size_bytes.value = configured
        await tb.write_peer(
            0, local_addr=0x2601, remote_addr=0x80002601, size=len(payload), mode=3, request=1
        )
        offset = 0
        for sequence, length in enumerate(lengths):
            request = await tb.receive_initiator_request()
            assert request == {
                "op": DMA_OP_WRITE,
                "addr": 0x80002601 + offset,
                "len": length,
                "peer_idx": 0,
                "sequence": sequence,
                "last": int(sequence == len(lengths) - 1),
            }
            frame = await tb.receive_oetp_frame()
            assert frame_bytes(frame) == payload[offset : offset + length]
            assert frame_sideband(frame.tuser) == request["last"]
            await tb.complete_initiator(request)
            offset += length
        await tb.wait_peer_status(0, done=1)
        assert int(dut.dma_max_fragment_size_bytes.value) == configured


@cocotb.test()
async def test_max_raw_read_chunks_preserve_errors(dut):
    if MAX_RAW_FRAME_SIZE < 8192:
        return
    tb = TB(dut)
    await tb.reset()
    payload = bytes((n * 17 + 3) & 255 for n in range(8192))
    base = 0x4D01
    tb.ram.write(base, payload)
    original_read = tb.ram.read_if._read
    tb.oetp_sink.set_pause_generator(cycle([0, 1, 0, 0]))
    dut.irq_commit_ready.value = 0

    # A read failure in either local chunk must survive the whole-frame result.
    for failure_addr in (base & ~3, (base + len(payload) - 1) & ~3):

        async def read_with_fault(address, length):
            if address == failure_addr:
                raise RuntimeError("injected AXI read failure")
            return await original_read(address, length)

        tb.ram.read_if._read = read_with_fault
        expected = bytearray(payload)
        for address in range(max(base, failure_addr), min(base + len(payload), failure_addr + 4)):
            expected[address - base] = 0
        await tb.request_non_tx(base, len(payload))
        frame = await tb.receive_oetp_frame()
        assert frame_bytes(frame) == expected
        assert frame_sideband(frame.tdest) == ROUTE_NON_OETP_DMA << PEER_IDX_W
        await tb.wait_signal(dut.non_tx_idle)
        assert int(dut.non_tx_done.value) == 0
        assert int(dut.non_tx_error_code.value) == 4
        assert int(dut.non_tx_transferred_length.value) == len(payload)
        await tb.wait_signal(dut.irq_commit_valid, 0b010)
        dut.irq_commit_ready.value = 0b111
        await tb.wait_signal(dut.irq_commit_valid, 0)
        await tb.clear_non_errors("tx")
        dut.irq_commit_ready.value = 0
    tb.ram.read_if._read = original_read


@cocotb.test()
async def test_dma_responder_read_write_and_invalid_request(dut):
    tb = TB(dut)
    await tb.reset()

    read_addr = 0x3002
    read_data = bytes((index * 5 + 0x22) & 0xFF for index in range(37))
    tb.ram.write(read_addr, read_data)

    await tb.send_responder_request(
        op=DMA_OP_READ,
        addr=read_addr,
        length=len(read_data),
        peer_idx=3,
        sequence=11,
        last=1,
    )
    frame = await tb.receive_oetp_frame()
    assert frame_bytes(frame) == read_data
    assert frame_sideband(frame.tid) == 11
    assert frame_sideband(frame.tdest) == 3
    assert frame_sideband(frame.tuser) == (TRANSFER_ROLE_RESPONDER << 1) | 1
    completion = await tb.receive_responder_completion()
    assert completion == {
        "op": DMA_OP_READ,
        "transferred_len": len(read_data),
        "peer_idx": 3,
        "sequence": 11,
        "last": 1,
        "error": 0,
        "error_code": 0,
    }
    await RisingEdge(dut.clk)

    armed_rx_addr = 0x3401
    armed_rx_data = bytes((index * 11 + 9) & 0xFF for index in range(23))
    await tb.request_non_rx(armed_rx_addr, 32)
    await tb.wait_signal(dut.non_rx_armed)

    write_addr = 0x3103
    write_data = bytes((index * 19 + 1) & 0xFF for index in range(39))
    await tb.send_responder_request(
        op=DMA_OP_WRITE,
        addr=write_addr,
        length=len(write_data),
        peer_idx=2,
        sequence=12,
        last=0,
    )
    await tb.send_oetp_frame(
        write_data,
        peer_idx=2,
        sequence=12,
        last=0,
        role=TRANSFER_ROLE_RESPONDER,
    )
    completion = await tb.receive_responder_completion()
    assert completion == {
        "op": DMA_OP_WRITE,
        "transferred_len": len(write_data),
        "peer_idx": 2,
        "sequence": 12,
        "last": 0,
        "error": 0,
        "error_code": 0,
    }
    assert tb.ram.read(write_addr, len(write_data)) == write_data
    assert int(dut.non_rx_armed.value) == 1
    assert int(dut.non_rx_done.value) == 0
    assert int(dut.non_rx_error.value) == 0

    await tb.claim_non_rx()
    await tb.send_oetp_frame(armed_rx_data, route=ROUTE_NON_OETP_DMA)
    await tb.wait_signal(dut.non_rx_idle)
    assert tb.ram.read(armed_rx_addr, len(armed_rx_data)) == armed_rx_data
    await RisingEdge(dut.clk)

    await tb.send_responder_request(
        op=DMA_OP_READ,
        addr=0x3200,
        length=MAX_DMA_FRAGMENT_SIZE_BYTES + 1,
        peer_idx=1,
        sequence=13,
        last=1,
    )
    completion = await tb.receive_responder_completion()
    assert completion["error"] == 1
    assert completion["error_code"] == 1
    assert completion["transferred_len"] == 0


@cocotb.test()
async def test_same_peer_sequence_initiator_and_responder(dut):
    """The role bit separates both contexts despite equal peer/sequence/LAST."""
    tb = TB(dut)
    await tb.reset()
    peer_idx = 1
    dut.responder_cpl_ready.value = 0

    # Mode 3 permits our write and the peer's read of our memory concurrently.
    initiator_data = bytes(range(17))
    responder_data = bytes(range(0x80, 0x80 + 17))
    tb.ram.write(0x6001, initiator_data)
    tb.ram.write(0x6103, responder_data)
    tb.oetp_sink.pause = True
    await tb.write_peer(
        peer_idx, local_addr=0x6001, remote_addr=0x80006001, size=17, mode=3, request=1
    )
    request = await tb.receive_initiator_request()
    assert request["sequence"] == 0 and request["last"] == 1
    await tb.send_responder_request(
        op=DMA_OP_READ, addr=0x6103, length=17, peer_idx=peer_idx, sequence=0, last=1
    )

    axis = dut.m_axis_oetp_if
    await tb.wait_signal(axis.tvalid)
    held = tuple(
        int(getattr(axis, field).value)
        for field in ("tdata", "tkeep", "tid", "tdest", "tuser", "tlast")
    )
    for _ in range(6):
        await RisingEdge(dut.clk)
        await Timer(1, unit="ns")
        assert int(axis.tvalid.value) and not int(axis.tready.value)
        assert held == tuple(
            int(getattr(axis, field).value)
            for field in ("tdata", "tkeep", "tid", "tdest", "tuser", "tlast")
        )
    tb.oetp_sink.pause = False

    frames = [await tb.receive_oetp_frame(), await tb.receive_oetp_frame()]
    payload_by_role = {}
    for frame in frames:
        assert frame_sideband(frame.tid) == 0
        assert frame_sideband(frame.tdest) == peer_idx
        user = frame_sideband(frame.tuser)
        assert user & 1 == 1
        assert user >> 1 not in payload_by_role
        payload_by_role[user >> 1] = frame_bytes(frame)
    assert payload_by_role == {
        TRANSFER_ROLE_INITIATOR: initiator_data,
        TRANSFER_ROLE_RESPONDER: responder_data,
    }
    completion = await tb.receive_responder_completion()
    assert completion["op"] == DMA_OP_READ
    assert completion["peer_idx"] == peer_idx and completion["sequence"] == 0
    assert completion["transferred_len"] == 17 and completion["error"] == 0
    dut.responder_cpl_ready.value = 1
    await tb.complete_initiator(request)
    await tb.wait_peer_status(peer_idx, done=1)
    await tb.wait_signal(dut.responder_req_ready)

    # Mode 2 permits our read response and the peer's write into our memory.
    # Deliver the responder data first: peer, sequence and LAST alone cannot
    # distinguish it from the waiting initiator destination.
    dut.responder_cpl_ready.value = 0
    initiator_data = bytes(range(0x20, 0x20 + 19))
    responder_data = bytes(range(0xA0, 0xA0 + 19))
    tb.ram.write(0x7000, b"!" * 21)
    tb.ram.write(0x7302, b"?" * 21)
    await tb.write_peer(
        peer_idx, local_addr=0x7001, remote_addr=0x80007001, size=19, mode=2, request=1
    )
    request = await tb.receive_initiator_request()
    assert request["sequence"] == 0 and request["last"] == 1
    await tb.send_responder_request(
        op=DMA_OP_WRITE, addr=0x7303, length=19, peer_idx=peer_idx, sequence=0, last=1
    )
    tb.oetp_source.set_pause_generator(cycle([1, 0, 0, 0]))
    tb.ram.write_if.aw_channel.set_pause_generator(cycle([1, 0, 0]))
    await tb.send_oetp_frame(
        responder_data, peer_idx=peer_idx, sequence=0, role=TRANSFER_ROLE_RESPONDER
    )
    await tb.send_oetp_frame(initiator_data, peer_idx=peer_idx, sequence=0)
    completion = await tb.receive_responder_completion()
    assert completion["op"] == DMA_OP_WRITE
    assert completion["peer_idx"] == peer_idx and completion["sequence"] == 0
    assert completion["transferred_len"] == 19 and completion["error"] == 0
    dut.responder_cpl_ready.value = 1
    await tb.complete_initiator(request)
    await tb.wait_peer_status(peer_idx, done=1)
    assert tb.ram.read(0x7000, 21) == b"!" + initiator_data + b"!"
    assert tb.ram.read(0x7302, 21) == b"?" + responder_data + b"?"


@cocotb.test()
async def test_concurrent_peers_reordered_fragments_and_snapshot(dut):
    tb = TB(dut)
    await tb.reset()
    dut.irq_commit_ready.value = 0
    dut.initiator_req_ready.value = 0
    tb.oetp_source.set_pause_generator(cycle([0, 1, 0, 0]))
    tb.oetp_sink.set_pause_generator(cycle([1, 0, 0, 0]))
    tb.ram.write_if.aw_channel.set_pause_generator(cycle([1, 0, 0]))
    tb.ram.read_if.r_channel.set_pause_generator(cycle([0, 1, 0]))
    payloads = {
        0: bytes((n * 3 + 7) & 255 for n in range(97)),
        1: bytes((n * 7 + 9) & 255 for n in range(150)),
        2: bytes((n * 11 + 13) & 255 for n in range(137)),
    }
    bases = {0: 0x4003, 1: 0x5001, 2: 0x6002}
    tb.ram.write(bases[0], payloads[0])
    for peer in payloads:
        await tb.write_peer(
            peer,
            local_addr=bases[peer],
            remote_addr=0x8000 + bases[peer],
            size=len(payloads[peer]),
            mode=3 if peer == 0 else 2,
            request=1,
        )
    assert int(dut.peer_idle.value) & 7 == 0
    await tb.wait_signal(dut.initiator_req_valid)
    held_request = tuple(
        int(getattr(dut, "initiator_req_" + field).value)
        for field in ("op", "addr", "len", "peer_idx", "sequence", "last")
    )
    for _ in range(20):
        await RisingEdge(dut.clk)
        await Timer(1, unit="ns")
        assert int(dut.initiator_req_valid.value)
        assert (
            tuple(
                int(getattr(dut, "initiator_req_" + field).value)
                for field in ("op", "addr", "len", "peer_idx", "sequence", "last")
            )
            == held_request
        )
    dut.initiator_req_ready.value = 1
    requests = {}
    for _ in range(8):
        req = await tb.receive_initiator_request()
        requests[req["peer_idx"], req["sequence"]] = req
    assert len(requests) == 8
    # Configuration changes after admission do not alter the saved contexts.
    for peer in payloads:
        tb.peers[peer].update(local_addr=0x7000, remote_addr=0, size=1, mode=0, irq_enable=0)
    tb.drive_peer_config()
    for seq in range(2):
        frame = await tb.receive_oetp_frame()
        req = requests[0, seq]
        assert frame_bytes(frame) == payloads[0][seq * 64 : seq * 64 + req["len"]]
        assert frame_sideband(frame.tdest) == 0  # Valid peer zero, route PEER.
        await tb.complete_initiator(req)
    # Final fragments arrive first, and frames from different peers interleave.
    for peer, seq in [(2, 2), (1, 1), (2, 0), (1, 2), (2, 1), (1, 0)]:
        req = requests[peer, seq]
        await tb.send_oetp_frame(
            payloads[peer][seq * 64 : seq * 64 + req["len"]],
            peer_idx=peer,
            sequence=seq,
            last=req["last"],
        )
        await tb.complete_initiator(req)
        if (peer, seq) == (2, 2):
            assert packed_field(dut.peer_done, peer, 1) == 0
    for peer in payloads:
        await tb.wait_peer_status(peer, done=1)
        assert tb.ram.read(bases[peer], len(payloads[peer])) == payloads[peer]
    await tb.wait_signal(dut.irq_commit_valid, 1)
    observed = []
    for _ in range(3):
        await tb.wait_signal(dut.irq_commit_valid, 1)
        idx = packed_field(dut.irq_commit_peer_idx, 0, PEER_IDX_W)
        for _ in range(4):
            await RisingEdge(dut.clk)
            await Timer(1, unit="ns")
            assert packed_field(dut.irq_commit_peer_idx, 0, PEER_IDX_W) == idx
        observed.append(idx)
        dut.irq_commit_ready.value = 1
        await RisingEdge(dut.clk)
        await Timer(1, unit="ns")
        dut.irq_commit_ready.value = 0
    assert sorted(observed) == [0, 1, 2]


@cocotb.test()
async def test_fragment_window_reuse_and_early_completion(dut):
    tb = TB(dut)
    await tb.reset()
    payload = bytes((n * 19 + 1) & 255 for n in range(11 * 64 - 7))
    await tb.write_peer(
        3, local_addr=0x7001, remote_addr=0x9001, size=len(payload), mode=2, request=1
    )
    window = [await tb.receive_initiator_request() for _ in range(8)]
    for _ in range(30):
        await RisingEdge(dut.clk)
    assert tb.requests.empty(), "The bounded fragment window exceeded its capacity"
    for req in reversed(window):
        # Completion can precede the payload. It must not finish the peer early.
        await tb.complete_initiator(req)
        assert packed_field(dut.peer_done, 3, 1) == 0
        offset = req["sequence"] * 64
        await tb.send_oetp_frame(
            payload[offset : offset + req["len"]],
            peer_idx=3,
            sequence=req["sequence"],
            last=req["last"],
        )
    for _ in range(3):
        req = await tb.receive_initiator_request()
        offset = req["sequence"] * 64
        await tb.send_oetp_frame(
            payload[offset : offset + req["len"]],
            peer_idx=3,
            sequence=req["sequence"],
            last=req["last"],
        )
        await tb.complete_initiator(req)
    await tb.wait_peer_status(3, done=1)
    assert tb.ram.read(0x7001, len(payload)) == payload


@cocotb.test()
async def test_shared_rmem_dma_errors_and_explicit_clear(dut):
    tb = TB(dut)
    await tb.reset()

    await tb.report_rmem_error(2, 8)
    await tb.report_rmem_error(1, 12)
    assert packed_field(dut.peer_error, 2, 1) == 1
    assert packed_field(dut.peer_error_code, 2, 4) == 8
    assert packed_field(dut.peer_error_code, 1, 4) == 12
    assert int(dut.irq_commit_valid.value) == 0  # RMEM keeps its separate IRQ path.

    await tb.report_rmem_error(2, 14, clear=True)
    assert packed_field(dut.peer_error, 2, 1) == 1
    assert packed_field(dut.peer_error_code, 2, 4) == 14
    assert packed_field(dut.peer_error_code, 1, 4) == 12

    # A successful bulk transfer preserves the older shared error record.
    await tb.write_peer(
        2, local_addr=0x4800, remote_addr=0x5800, size=12, mode=2, irq_enable=0, request=1
    )
    assert packed_field(dut.peer_error_code, 2, 4) == 14
    req = await tb.receive_initiator_request()
    data = bytes(range(12))
    await tb.send_oetp_frame(data, peer_idx=2, sequence=req["sequence"], last=req["last"])
    await tb.complete_initiator(req)
    await tb.wait_peer_status(2, done=1, error=1)
    assert tb.ram.read(0x4800, 12) == data
    assert packed_field(dut.peer_error_code, 2, 4) == 14

    await tb.clear_peer_error(2)
    assert packed_field(dut.peer_error, 2, 1) == 0
    assert packed_field(dut.peer_error_code, 2, 4) == 0
    assert packed_field(dut.peer_done, 2, 1) == 1
    assert packed_field(dut.peer_error_code, 1, 4) == 12

    # Clearing while active does not abort the transfer or hide a later failure.
    await tb.report_rmem_error(2, 8)
    await tb.write_peer(
        2, local_addr=0x4900, remote_addr=0x5900, size=12, mode=2, irq_enable=0, request=1
    )
    req = await tb.receive_initiator_request()
    await tb.clear_peer_error(2)
    assert packed_field(dut.peer_idle, 2, 1) == 0
    assert packed_field(dut.peer_error, 2, 1) == 0
    await tb.complete_initiator(req, error=1, error_code=13)
    await tb.wait_peer_status(2, error=1)
    assert packed_field(dut.peer_error_code, 2, 4) == 13
    await tb.clear_peer_error(1)
    assert packed_field(dut.peer_error_code, 1, 4) == 0
    assert packed_field(dut.peer_error_code, 2, 4) == 13


@cocotb.test()
async def test_local_remote_errors_and_full_width_wire_mapping(dut):
    tb = TB(dut)
    await tb.reset()

    for wire_code in range(1, 8):
        dut.wire_error_code.value = wire_code
        await Timer(1, unit="ns")
        assert int(dut.wire_error_csr_code.value) == wire_code + 8
        await tb.write_peer(
            0, local_addr=0x5000, remote_addr=0x6000, size=12, mode=2, irq_enable=0, request=1
        )
        req = await tb.receive_initiator_request()
        await tb.complete_initiator(req, error=1, wire_error=wire_code)
        await tb.wait_peer_status(0, error=1)
        assert packed_field(dut.peer_error_code, 0, 4) == wire_code + 8
        assert tb.ram.read(0x5000, 12) == bytes(12)
        await tb.report_rmem_error(1, wire_code + 8)
        assert packed_field(dut.peer_error_code, 1, 4) == wire_code + 8
        await tb.clear_peer_error(0)

    # High bits must be checked before narrowing to the four-bit CSR code.
    for wire_code in (0, 8, 9, 15, 16, 0x101, 0x10000001, 0xFFFFFFF7, 0xFFFFFFFF):
        dut.wire_error_code.value = wire_code
        await Timer(1, unit="ns")
        assert int(dut.wire_error_csr_code.value) == 1

    await tb.write_peer(
        0, local_addr=0x5000, remote_addr=0x6000, size=12, mode=2, irq_enable=0, request=1
    )
    req = await tb.receive_initiator_request()
    await tb.complete_initiator(req, error=1, wire_error=0x10000001)
    await tb.wait_peer_status(0, error=1)
    assert packed_field(dut.peer_error_code, 0, 4) == 1
    await tb.clear_peer_error(0)

    # Local errors on the same completion channel must not gain the remote offset.
    for local_code in (1, 2, 8):
        await tb.write_peer(
            0, local_addr=0x5000, remote_addr=0x6000, size=12, mode=2, irq_enable=0, request=1
        )
        req = await tb.receive_initiator_request()
        await tb.complete_initiator(req, error=1, error_code=local_code)
        await tb.wait_peer_status(0, error=1)
        assert packed_field(dut.peer_error_code, 0, 4) == local_code
        await tb.clear_peer_error(0)

    # A local short-payload failure keeps precedence over a reported remote cause.
    await tb.write_peer(
        0, local_addr=0x5000, remote_addr=0x6000, size=12, mode=2, irq_enable=0, request=1
    )
    req = await tb.receive_initiator_request()
    await tb.send_oetp_frame(
        bytes(range(10)), peer_idx=0, sequence=req["sequence"], last=req["last"]
    )
    await tb.complete_initiator(req, error=1, wire_error=7)
    await tb.wait_peer_status(0, error=1)
    assert packed_field(dut.peer_error_code, 0, 4) == 2
    assert tb.ram.read(0x5000, 10) == bytes(range(10))
    assert tb.ram.read(0x500A, 2) == bytes(2)

    # oETP's incomplete-peer-frame classification is canonical even when
    # the same truncation also makes the internal memory-data AXIS short.
    await tb.clear_peer_error(0)
    await tb.write_peer(
        0, local_addr=0x5000, remote_addr=0x6000, size=12, mode=2, irq_enable=0, request=1
    )
    req = await tb.receive_initiator_request()
    await tb.send_oetp_frame(
        bytes(range(10)), peer_idx=0, sequence=req["sequence"], last=req["last"]
    )
    await tb.complete_initiator(req, error=1, error_code=10)
    await tb.wait_peer_status(0, error=1)
    assert packed_field(dut.peer_error_code, 0, 4) == 10

    # A missing EndOfData can be detected after all expected data was forwarded
    # (e.g. zero MAC padding filled a prematurely terminated short frame).
    await tb.clear_peer_error(0)
    await tb.write_peer(
        0, local_addr=0x5000, remote_addr=0x6000, size=12, mode=2, irq_enable=0, request=1
    )
    req = await tb.receive_initiator_request()
    payload = b"DATA" + bytes.fromhex("d0e0d0e0") + b"TAIL"
    await tb.send_oetp_frame(payload, peer_idx=0, sequence=req["sequence"], last=req["last"])
    await tb.complete_initiator(req, error=1, error_code=10)
    await tb.wait_peer_status(0, error=1)
    assert packed_field(dut.peer_error_code, 0, 4) == 10
    assert tb.ram.read(0x5000, 12) == payload


@cocotb.test()
async def test_received_write_error_and_initiator_remote_error(dut):
    """Exercise B's received truncation and A's mapped completion at the boundary."""
    tb = TB(dut)
    await tb.reset()
    dut.event_enable.value = 1
    dut.irq_commit_ready.value = 0
    dut.responder_irq_admit_ready.value = 0
    dut.responder_irq_commit_ready.value = 0
    dut.responder_cpl_ready.value = 0

    # B can already have an independently initiated transfer to A in progress.
    tb.ram.write(0x1000, b"abcdefghijkl")
    await tb.write_peer(2, local_addr=0x1000, remote_addr=0x2000, size=12, mode=3, request=1)
    b_request = await tb.receive_initiator_request()
    assert frame_bytes(await tb.receive_oetp_frame()) == b"abcdefghijkl"
    assert packed_field(dut.peer_idle, 2, 1) == 0

    # Incoming B-side write ends early, after modifying ten of twelve bytes.
    tb.ram.write(0x3000, b"!" * 12)
    await tb.send_responder_request(
        op=DMA_OP_WRITE, addr=0x3000, length=12, peer_idx=2, sequence=0x1234, last=1
    )
    await tb.send_oetp_frame(
        bytes(range(10)), peer_idx=2, sequence=0x1234, role=TRANSFER_ROLE_RESPONDER
    )
    await tb.wait_signal(dut.responder_cpl_valid)
    b_completion = await tb.receive_responder_completion()
    assert b_completion["error"] == 1 and b_completion["error_code"] == 2
    assert b_completion["transferred_len"] == 10
    assert tb.ram.read(0x3000, 12) == bytes(range(10)) + b"!!"
    assert packed_field(dut.peer_error_code, 2, 4) == 10
    assert packed_field(dut.peer_error, 2, 1) == 1
    assert packed_field(dut.peer_idle, 2, 1) == 0
    assert packed_field(dut.peer_done, 2, 1) == 0

    # Reply completion proceeds even when IRQ capacity is unavailable.
    dut.responder_cpl_ready.value = 1
    for _ in range(4):
        await RisingEdge(dut.clk)
        await Timer(1, unit="ns")
        assert int(dut.responder_irq_admit_valid.value) == 1
        assert int(dut.responder_irq_admit_source.value) == 0
        assert int(dut.responder_irq_admit_enable.value) == 1
        assert int(dut.responder_req_ready.value) == 0
    assert int(dut.responder_cpl_valid.value) == 0

    dut.responder_irq_admit_ready.value = 1
    await tb.wait_signal(dut.responder_irq_commit_valid)
    # Captured events survive later enable changes and retain their peer index.
    dut.event_enable.value = 0
    for _ in range(4):
        await RisingEdge(dut.clk)
        await Timer(1, unit="ns")
        assert int(dut.responder_irq_commit_valid.value) == 1
        assert int(dut.responder_irq_commit_source.value) == 0
        assert int(dut.responder_irq_commit_peer_idx.value) == 2

    await tb.complete_initiator(b_request)
    await tb.wait_peer_status(2, done=1, error=1)
    assert packed_field(dut.peer_error_code, 2, 4) == 10
    await tb.wait_signal(dut.irq_commit_valid, 1)
    assert packed_field(dut.irq_commit_source, 0, 4) == 0
    assert packed_field(dut.irq_commit_peer_idx, 0, PEER_IDX_W) == 2
    dut.responder_irq_commit_ready.value = 1
    dut.irq_commit_ready.value = 0b111
    await tb.wait_signal(dut.responder_req_ready)
    await tb.wait_signal(dut.irq_commit_valid, 0)

    # Model A on another peer entry, feeding B's cause through the wire mapper.
    dut.event_enable.value = 1
    dut.irq_commit_ready.value = 0
    tb.ram.write(0x4000, b"ABCDEFGHIJKL")
    await tb.write_peer(1, local_addr=0x4000, remote_addr=0x3000, size=12, mode=3, request=1)
    a_request = await tb.receive_initiator_request()
    assert frame_bytes(await tb.receive_oetp_frame()) == b"ABCDEFGHIJKL"
    await tb.complete_initiator(a_request, error=1, wire_error=b_completion["error_code"])
    await tb.wait_peer_status(1, error=1)
    assert packed_field(dut.peer_error_code, 1, 4) == 10
    assert packed_field(dut.peer_error_code, 2, 4) == 10
    await tb.wait_signal(dut.irq_commit_valid, 1)
    assert packed_field(dut.irq_commit_peer_idx, 0, PEER_IDX_W) == 1


@cocotb.test()
async def test_received_error_irq_gates_and_rmem_source(dut):
    tb = TB(dut)
    await tb.reset()

    # Incoming bulk failures need both gates; RMEM retains source 5 and its
    # independent global gate, irrespective of the per-peer bulk enable.
    for kind, global_mask, peer_enable, expected_event in (
        (0, 0, 1, False),
        (0, 1, 0, False),
        (0, 1, 1, True),
        (1, 1 << 5, 0, True),
        (1, 1, 1, False),
    ):
        await tb.write_peer(
            3,
            local_addr=0x5000,
            remote_addr=0x6000,
            size=4,
            mode=1 if kind else 2,
            irq_enable=peer_enable,
        )
        dut.event_enable.value = global_mask
        dut.responder_irq_admit_ready.value = 0
        dut.responder_irq_commit_ready.value = 0
        await tb.send_responder_request(
            op=DMA_OP_WRITE, addr=0x5000, length=0, peer_idx=3, sequence=0x4567, last=1, kind=kind
        )
        # A fresh received error wins a clear on its recording edge.
        await FallingEdge(dut.clk)
        dut.peer_clear_error.value = 1 << 3
        await RisingEdge(dut.clk)
        await Timer(1, unit="ns")
        dut.peer_clear_error.value = 0
        assert packed_field(dut.peer_error, 3, 1) == 1
        assert packed_field(dut.peer_error_code, 3, 4) == 1
        cpl = await tb.receive_responder_completion()
        assert cpl["error"] == 1 and cpl["error_code"] == 1
        assert packed_field(dut.peer_idle, 3, 1) == 1
        assert packed_field(dut.peer_done, 3, 1) == 0
        assert int(dut.irq_commit_valid.value) == 0
        assert int(dut.responder_irq_admit_source.value) == (5 if kind else 0)
        assert int(dut.responder_irq_admit_enable.value) == (1 if kind else peer_enable)
        dut.responder_irq_admit_ready.value = 1
        for _ in range(3):
            await RisingEdge(dut.clk)
            await Timer(1, unit="ns")
        assert int(dut.responder_irq_commit_valid.value) == int(expected_event)
        if expected_event:
            assert int(dut.responder_irq_commit_source.value) == (5 if kind else 0)
            assert int(dut.responder_irq_commit_peer_idx.value) == 3
            await tb.clear_peer_error(3)
            assert packed_field(dut.peer_error, 3, 1) == 0
            assert int(dut.responder_irq_commit_valid.value) == 1
        dut.responder_irq_commit_ready.value = 1
        await tb.wait_signal(dut.responder_req_ready)
        await tb.clear_peer_error(3)
        for _ in range(3):
            await RisingEdge(dut.clk)
            await Timer(1, unit="ns")
            assert int(dut.responder_irq_commit_valid.value) == 0


@cocotb.test()
async def test_transfer_kind_and_exact_memory_payload(dut):
    tb = TB(dut)
    await tb.reset()

    # Length four is still bulk DMA: its word travels over AXIS without headers.
    tb.ram.write(0x6001, b"ABCD")
    await tb.send_responder_request(
        op=DMA_OP_READ, addr=0x6001, length=4, peer_idx=1, sequence=0x77, last=1
    )
    frame = await tb.receive_oetp_frame()
    assert frame_bytes(frame) == b"ABCD"
    cpl = await tb.receive_responder_completion()
    assert cpl["error"] == 0 and cpl["transferred_len"] == 4
    assert int(dut.responder_cpl_kind.value) == 0
    await RisingEdge(dut.clk)

    # Scalar RMEM is separately tagged; its retained placeholder rejects it
    # without touching memory or creating an AXIS payload.
    dut.responder_cpl_ready.value = 0
    await tb.send_responder_request(
        op=DMA_OP_WRITE,
        addr=0x6000,
        length=4,
        peer_idx=1,
        sequence=0x78,
        last=1,
        kind=1,
        biten=5,
        wdata=0xDEADBEEF,
    )
    cpl = await tb.receive_responder_completion()
    assert cpl["error"] == 1 and cpl["transferred_len"] == 0
    for _ in range(5):
        await RisingEdge(dut.clk)
        await Timer(1, unit="ns")
        assert int(dut.responder_cpl_kind.value) == 1
        assert int(dut.responder_cpl_sequence.value) == 0x78
        assert int(dut.responder_cpl_rdata.value) == 0
        assert tb.oetp_sink.empty()
    assert tb.ram.read(0x6001, 4) == b"ABCD"
    dut.responder_cpl_ready.value = 1
    await RisingEdge(dut.clk)

    tb.ram.write(0x7FF8, bytes([0xCC]) * 20)
    await tb.write_peer(
        0, local_addr=0x8000, remote_addr=0x9000, size=4, mode=2, irq_enable=0, request=1
    )
    req = await tb.receive_initiator_request()
    assert int(dut.initiator_req_kind.value) == 0
    # Matching peer/sequence metadata in an RMEM completion must not retire DMA.
    await tb.complete_initiator(req, error=1, error_code=8, kind=1)
    await Timer(20, unit="ns")
    assert packed_field(dut.peer_idle, 0, 1) == 0
    assert packed_field(dut.peer_error_code, 0, 4) == 8
    await tb.send_oetp_frame(b"WXYZ", peer_idx=0, sequence=req["sequence"], last=req["last"])
    await tb.complete_initiator(req)
    await tb.wait_peer_status(0, done=1, error=1)
    assert tb.ram.read(0x7FF8, 20) == bytes([0xCC]) * 8 + b"WXYZ" + bytes([0xCC]) * 8


@cocotb.test(timeout_time=3000, timeout_unit="us")
async def test_registered_outputs_between_clock_edges(dut):
    """Handshake, status, and payload outputs remain stable between rising edges."""
    tb = TB(dut)
    await tb.reset()
    output_names = [
        "non_tx_request_hwclr",
        "non_tx_clear_errors_hwclr",
        "non_tx_idle",
        "non_tx_done",
        "non_tx_error",
        "non_tx_error_code",
        "non_tx_transferred_length",
        "non_rx_request_hwclr",
        "non_rx_clear_errors_hwclr",
        "non_rx_idle",
        "non_rx_armed",
        "non_rx_done",
        "non_rx_error",
        "non_rx_error_code",
        "non_rx_received_length",
        "peer_request_hwclr",
        "peer_clear_error_hwclr",
        "peer_idle",
        "peer_done",
        "peer_error",
        "peer_error_code",
        "peer_lookup_req_valid",
        "peer_lookup_req_type",
        "peer_lookup_req_mode_mask",
        "peer_lookup_req_peer_idx",
        "peer_lookup_req_rmem_addr",
        "peer_lookup_req_mac_addr",
        "peer_lookup_rsp_ready",
        "initiator_req_valid",
        "initiator_req_op",
        "initiator_req_kind",
        "initiator_req_addr",
        "initiator_req_len",
        "initiator_req_peer_idx",
        "initiator_req_sequence",
        "initiator_req_last",
        "initiator_cpl_ready",
        "responder_req_ready",
        "responder_cpl_valid",
        "responder_cpl_op",
        "responder_cpl_kind",
        "responder_cpl_rdata",
        "responder_cpl_transferred_len",
        "responder_cpl_peer_idx",
        "responder_cpl_sequence",
        "responder_cpl_last",
        "responder_cpl_error",
        "responder_cpl_error_code",
        "non_oetp_rx_available",
        "non_oetp_rx_claim_ready",
        "irq_admit_valid",
        "irq_admit_source",
        "irq_admit_enable",
        "irq_commit_valid",
        "irq_commit_source",
        "irq_commit_peer_idx",
        "responder_irq_admit_source",
        "responder_irq_commit_valid",
        "responder_irq_commit_source",
        "responder_irq_commit_peer_idx",
        "responder_irq_admit_valid",
        "responder_irq_admit_enable",
        "responder_irq_admit_source",
    ]
    outputs = [getattr(dut, name) for name in output_names]
    outputs += [
        getattr(dut.m_axis_oetp_if, name)
        for name in ["tdata", "tkeep", "tstrb", "tvalid", "tlast", "tid", "tdest", "tuser"]
    ]
    outputs += [dut.s_axis_oetp_if.tready]
    for channel, fields in [
        (
            "ar",
            [
                "id",
                "addr",
                "len",
                "size",
                "burst",
                "lock",
                "cache",
                "prot",
                "qos",
                "region",
                "user",
                "valid",
            ],
        ),
        (
            "aw",
            [
                "id",
                "addr",
                "len",
                "size",
                "burst",
                "lock",
                "cache",
                "prot",
                "qos",
                "region",
                "user",
                "valid",
            ],
        ),
        ("w", ["data", "strb", "last", "user", "valid"]),
        ("r", ["ready"]),
        ("b", ["ready"]),
    ]:
        outputs += [getattr(dut.m_axi_if, channel + field) for field in fields]
    inputs = [
        getattr(dut, name)
        for name in [
            "non_tx_request",
            "non_rx_request",
            "non_tx_clear_errors",
            "non_rx_clear_errors",
            "peer_request",
            "peer_clear_error",
            "non_oetp_rx_claim_valid",
            "initiator_req_ready",
            "initiator_cpl_valid",
            "responder_req_valid",
            "responder_cpl_ready",
            "irq_admit_ready",
            "irq_commit_ready",
        ]
    ]
    inputs += [
        dut.m_axis_oetp_if.tready,
        dut.m_axi_if.arready,
        dut.m_axi_if.awready,
        dut.m_axi_if.wready,
        dut.m_axi_if.rvalid,
        dut.m_axi_if.bvalid,
    ]
    payload = bytes(range(60))
    tb.ram.write(0x1000, payload)
    await tb.request_non_tx(0x1000, len(payload))
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
    assert frame_bytes(await tb.receive_oetp_frame()) == payload
    await tb.wait_signal(dut.non_tx_idle)
    assert int(dut.non_tx_done.value) and not int(dut.non_tx_error.value)

    # A CSR command remains asserted until its registered hardware clear returns.
    await tb.request_non_tx(0x1000, 0)
    await tb.wait_signal(dut.non_tx_error)
    await FallingEdge(dut.clk)
    dut.non_tx_clear_errors.value = 1
    await RisingEdge(dut.clk)
    await Timer(1, unit="ns")
    assert not int(dut.non_tx_error.value)
    for _ in range(3):
        await RisingEdge(dut.clk)
    await tb.request_non_tx(0x1000, 0)
    await tb.wait_signal(dut.non_tx_error)
    for _ in range(3):
        await RisingEdge(dut.clk)
        await Timer(1, unit="ns")
        assert int(dut.non_tx_error.value), "A held clear erased a later failure"
    dut.non_tx_clear_errors.value = 0


tests_dir = os.path.abspath(os.path.dirname(__file__))
repo_dir = os.path.abspath(os.path.join(tests_dir, "..", "..", ".."))
core_dir = os.path.join(repo_dir, "hw", "rtl", "core")
hal_if_dir = os.path.join(repo_dir, "build", "hal", "rtl")
taxi_dir = os.path.join(repo_dir, "libs", "taxi", "src")
common_dir = os.path.join(repo_dir, "dv", "common")


@pytest.mark.parametrize("max_raw_frame_size", [96, 8192])
def test_openenoc_endpoint_dma_engine(request, max_raw_frame_size):
    module = os.path.splitext(os.path.basename(__file__))[0]
    parameters = {
        "NUM_OF_PEERS": NUM_OF_PEERS,
        "AXI_DATA_W": 32,
        "AXI_ADDR_W": 32,
        "AXI_ID_W": 8,
        "SEQUENCE_W": 32,
        "MAX_RAW_FRAME_SIZE": max_raw_frame_size,
        "FRAGMENT_SLOTS": 8,
    }
    extra_env = {f"PARAM_{key}": str(value) for key, value in parameters.items()}
    sim_build = os.path.join(tests_dir, "sim_build", request.node.name)

    verilog_sources = [
        os.path.join(hal_if_dir, "openenoc_endpoint_if.sv"),
        os.path.join(taxi_dir, "axis", "rtl", "taxi_axis_if.sv"),
        os.path.join(taxi_dir, "axis", "rtl", "taxi_axis_register.sv"),
        os.path.join(taxi_dir, "axi", "rtl", "taxi_axi_if.sv"),
        os.path.join(taxi_dir, "axi", "rtl", "taxi_axi_register_rd.sv"),
        os.path.join(taxi_dir, "axi", "rtl", "taxi_axi_register_wr.sv"),
        os.path.join(taxi_dir, "dma", "rtl", "taxi_dma_desc_if.sv"),
        os.path.join(taxi_dir, "dma", "rtl", "taxi_axi_dma_rd.sv"),
        os.path.join(taxi_dir, "dma", "rtl", "taxi_axi_dma_wr.sv"),
        os.path.join(taxi_dir, "dma", "rtl", "taxi_axi_dma.sv"),
        os.path.join(core_dir, "openenoc_peer_lookup_if.sv"),
        os.path.join(core_dir, "openenoc_cpuif_if.sv"),
        os.path.join(core_dir, "openenoc_dma_transfer_if.sv"),
        os.path.join(core_dir, "openenoc_irq_event_if.sv"),
        os.path.join(core_dir, "openenoc_endpoint_dma_engine.sv"),
        os.path.join(tests_dir, f"{module}.sv"),
    ]

    cocotb_test.simulator.run(
        simulator="verilator",
        python_search=[tests_dir],
        verilog_sources=verilog_sources,
        toplevel=module,
        module=module,
        parameters=parameters,
        timescale="1ns/1ps",
        extra_args=["-Wall", os.path.join(common_dir, "config.vlt")],
        sim_build=sim_build,
        extra_env=extra_env,
    )
