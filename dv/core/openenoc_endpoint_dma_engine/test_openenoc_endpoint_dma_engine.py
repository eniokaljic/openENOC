# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: AGPL-3.0-or-later

import os

import cocotb
import cocotb_test.simulator
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer, with_timeout
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

NUM_OF_PEERS = 4
MAX_DMA_FRAME_SIZE_BYTES = 64


def packed_field(signal, index, width):
    return (int(signal.value) >> (index * width)) & ((1 << width) - 1)


class TB:
    def __init__(self, dut):
        self.dut = dut
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
        self.dut.peer_lookup_rsp_local_addr.value = (
            peer["local_addr"] if hit else 0
        )
        self.dut.peer_lookup_rsp_remote_addr.value = (
            peer["remote_addr"] if hit else 0
        )
        self.dut.peer_lookup_rsp_size.value = peer["size"] if hit else 0
        self.dut.peer_lookup_rsp_dma_mode.value = peer["mode"] if hit else 0
        self.dut.peer_lookup_rsp_irq_enable.value = (
            peer["irq_enable"] if hit else 0
        )

    async def peer_lookup_responder(self):
        while True:
            await RisingEdge(self.dut.clk)

            reset = int(self.dut.rst.value)
            request_fire = (
                int(self.dut.peer_lookup_req_valid.value)
                and int(self.dut.peer_lookup_req_ready.value)
            )
            response_fire = (
                int(self.dut.peer_lookup_rsp_valid.value)
                and int(self.dut.peer_lookup_rsp_ready.value)
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
        self.dut.non_tx_buffer_address.setimmediatevalue(0)
        self.dut.non_tx_frame_length.setimmediatevalue(0)
        self.dut.non_tx_request.setimmediatevalue(0)
        self.dut.non_rx_buffer_address.setimmediatevalue(0)
        self.dut.non_rx_buffer_capacity.setimmediatevalue(0)
        self.dut.non_rx_request.setimmediatevalue(0)
        self.dut.peer_request.setimmediatevalue(0)
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
        self.dut.initiator_cpl_transferred_len.setimmediatevalue(0)
        self.dut.initiator_cpl_peer_idx.setimmediatevalue(0)
        self.dut.initiator_cpl_sequence.setimmediatevalue(0)
        self.dut.initiator_cpl_last.setimmediatevalue(0)
        self.dut.initiator_cpl_error.setimmediatevalue(0)
        self.dut.initiator_cpl_error_code.setimmediatevalue(0)

        self.dut.responder_req_valid.setimmediatevalue(0)
        self.dut.responder_req_op.setimmediatevalue(0)
        self.dut.responder_req_addr.setimmediatevalue(0)
        self.dut.responder_req_len.setimmediatevalue(0)
        self.dut.responder_req_peer_idx.setimmediatevalue(0)
        self.dut.responder_req_sequence.setimmediatevalue(0)
        self.dut.responder_req_last.setimmediatevalue(0)
        self.dut.responder_cpl_ready.setimmediatevalue(1)

        self.dut.irq_admit_ready.setimmediatevalue(0b111)
        self.dut.irq_admit_reserved.setimmediatevalue(0b111)
        self.dut.irq_commit_ready.setimmediatevalue(0b111)

        cocotb.start_soon(self.peer_lookup_responder())

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

    async def wait_peer_status(self, index, *, done=0, error=0, idle=1,
                               cycles=4000):
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

    async def receive_initiator_request(self):
        for _ in range(1000):
            await RisingEdge(self.dut.clk)
            if int(self.dut.initiator_req_valid.value):
                return {
                    "op": int(self.dut.initiator_req_op.value),
                    "addr": int(self.dut.initiator_req_addr.value),
                    "len": int(self.dut.initiator_req_len.value),
                    "peer_idx": int(self.dut.initiator_req_peer_idx.value),
                    "sequence": int(self.dut.initiator_req_sequence.value),
                    "last": int(self.dut.initiator_req_last.value),
                }
        raise AssertionError("initiator request timed out")

    async def complete_initiator(
        self, request, *, error=0, error_code=0, transferred_len=None
    ):
        if transferred_len is None:
            transferred_len = request["len"]

        self.dut.initiator_cpl_op.value = request["op"]
        self.dut.initiator_cpl_transferred_len.value = transferred_len
        self.dut.initiator_cpl_peer_idx.value = request["peer_idx"]
        self.dut.initiator_cpl_sequence.value = request["sequence"]
        self.dut.initiator_cpl_last.value = request["last"]
        self.dut.initiator_cpl_error.value = error
        self.dut.initiator_cpl_error_code.value = error_code
        self.dut.initiator_cpl_valid.value = 1

        for _ in range(1000):
            await RisingEdge(self.dut.clk)
            if int(self.dut.initiator_cpl_ready.value):
                break
        else:
            raise AssertionError("initiator completion timed out")

        self.dut.initiator_cpl_valid.value = 0

    async def send_responder_request(
        self, *, op, addr, length, peer_idx, sequence, last
    ):
        self.dut.responder_req_op.value = op
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
                    "transferred_len": int(
                        self.dut.responder_cpl_transferred_len.value
                    ),
                    "peer_idx": int(self.dut.responder_cpl_peer_idx.value),
                    "sequence": int(self.dut.responder_cpl_sequence.value),
                    "last": int(self.dut.responder_cpl_last.value),
                    "error": int(self.dut.responder_cpl_error.value),
                    "error_code": int(self.dut.responder_cpl_error_code.value),
                }
        raise AssertionError("responder completion timed out")

    async def send_oetp_frame(self, data, *, peer_idx=0, sequence=0, last=1):
        frame = AxiStreamFrame(data)
        frame.tid = sequence
        frame.tdest = peer_idx
        frame.tuser = last
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
    tx_data = bytes((index * 13 + 7) & 0xFF for index in range(53))
    tb.ram.write(tx_addr, tx_data)

    dut.irq_commit_ready.value = 0
    await tb.request_non_tx(tx_addr, len(tx_data))

    tx_frame = await tb.receive_oetp_frame()
    assert frame_bytes(tx_frame) == tx_data

    await tb.wait_signal(dut.non_tx_idle)
    assert int(dut.non_tx_done.value) == 1
    assert int(dut.non_tx_error.value) == 0
    assert int(dut.non_tx_transferred_length.value) == len(tx_data)
    assert int(dut.irq_commit_valid.value) == 0b010
    assert (int(dut.irq_commit_source.value) >> 4) & 0xF == 1

    dut.irq_commit_ready.value = 0b111
    await RisingEdge(dut.clk)

    rx_addr = 0x0205
    rx_data = bytes((index * 9 + 3) & 0xFF for index in range(47))
    dut.irq_commit_ready.value = 0
    await tb.request_non_rx(rx_addr, 60)
    await tb.wait_signal(dut.non_rx_armed)

    await tb.send_oetp_frame(rx_data)
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
    await tb.send_oetp_frame(overflow_data)
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
        assert frame_bytes(frame) == payload[offset:offset + length]
        assert frame_sideband(frame.tid) == sequence
        assert frame_sideband(frame.tdest) == peer_idx
        assert frame_sideband(frame.tuser) == int(sequence == 2)
        await tb.complete_initiator(request)
        offset += length

    await tb.wait_peer_status(peer_idx, done=1)
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
            payload[offset:offset + length],
            peer_idx=peer_idx,
            sequence=sequence,
            last=int(sequence == 2),
        )
        await tb.complete_initiator(request)
        offset += length

    await tb.wait_peer_status(peer_idx, done=1)
    assert tb.ram.read(local_addr, len(payload)) == payload
    assert int(dut.irq_commit_valid.value) == 0b001
    assert packed_field(dut.irq_commit_peer_idx, 0, 2) == peer_idx


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
    assert frame_sideband(frame.tuser) == 1
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

    await tb.send_oetp_frame(armed_rx_data)
    await tb.wait_signal(dut.non_rx_idle)
    assert tb.ram.read(armed_rx_addr, len(armed_rx_data)) == armed_rx_data
    await RisingEdge(dut.clk)

    await tb.send_responder_request(
        op=DMA_OP_READ,
        addr=0x3200,
        length=MAX_DMA_FRAME_SIZE_BYTES + 1,
        peer_idx=1,
        sequence=13,
        last=1,
    )
    completion = await tb.receive_responder_completion()
    assert completion["error"] == 1
    assert completion["error_code"] == 1
    assert completion["transferred_len"] == 0


tests_dir = os.path.abspath(os.path.dirname(__file__))
repo_dir = os.path.abspath(os.path.join(tests_dir, "..", "..", ".."))
core_dir = os.path.join(repo_dir, "hw", "rtl", "core")
hal_if_dir = os.path.join(repo_dir, "build", "hal", "rtl")
taxi_dir = os.path.join(repo_dir, "libs", "taxi", "src")
common_dir = os.path.join(repo_dir, "dv", "common")


def test_openenoc_endpoint_dma_engine(request):
    module = os.path.splitext(os.path.basename(__file__))[0]
    parameters = {
        "NUM_OF_PEERS": NUM_OF_PEERS,
        "AXI_DATA_W": 32,
        "AXI_ADDR_W": 32,
        "AXI_ID_W": 8,
        "SEQUENCE_W": 32,
        "MAX_DMA_FRAME_SIZE_BYTES": MAX_DMA_FRAME_SIZE_BYTES,
    }
    extra_env = {f"PARAM_{key}": str(value) for key, value in parameters.items()}
    sim_build = os.path.join(tests_dir, "sim_build", request.node.name)

    verilog_sources = [
        os.path.join(hal_if_dir, "openenoc_endpoint_if.sv"),
        os.path.join(taxi_dir, "axis", "rtl", "taxi_axis_if.sv"),
        os.path.join(taxi_dir, "axi", "rtl", "taxi_axi_if.sv"),
        os.path.join(taxi_dir, "dma", "rtl", "taxi_dma_desc_if.sv"),
        os.path.join(taxi_dir, "dma", "rtl", "taxi_axi_dma_rd.sv"),
        os.path.join(taxi_dir, "dma", "rtl", "taxi_axi_dma_wr.sv"),
        os.path.join(taxi_dir, "dma", "rtl", "taxi_axi_dma.sv"),
        os.path.join(core_dir, "openenoc_peer_lookup_if.sv"),
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
        extra_args=[
            "-Wno-TIMESCALEMOD",
            os.path.join(common_dir, "config.vlt"),
        ],
        sim_build=sim_build,
        extra_env=extra_env,
    )
