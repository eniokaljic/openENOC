# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: AGPL-3.0-or-later

import os

import cocotb
import cocotb_test.simulator
from cocotb.clock import Clock
from cocotb.triggers import FallingEdge, ReadOnly, RisingEdge, Timer


def expanded_biten(strobe, lanes=4):
    value = 0
    for lane in range(lanes):
        if strobe & (1 << lane):
            value |= 0xFF << (lane * 8)
    return value


class TB:
    def __init__(self, dut):
        self.dut = dut
        self.axil = dut.axil
        self.cpuif = dut.cpuif
        cocotb.start_soon(Clock(dut.clk, 10, unit="ns").start())
        self.drive_idle()

    def drive_idle(self):
        self.dut.rst.value = 1

        self.axil.awvalid.value = 0
        self.axil.awaddr.value = 0
        self.axil.awprot.value = 0
        self.axil.awuser.value = 0
        self.axil.wvalid.value = 0
        self.axil.wdata.value = 0
        self.axil.wstrb.value = 0
        self.axil.wuser.value = 0
        self.axil.bready.value = 0
        self.axil.arvalid.value = 0
        self.axil.araddr.value = 0
        self.axil.arprot.value = 0
        self.axil.aruser.value = 0
        self.axil.rready.value = 0

        self.cpuif.wr_ack.value = 0
        self.cpuif.wr_err.value = 0
        self.cpuif.rd_ack.value = 0
        self.cpuif.rd_err.value = 0
        self.cpuif.rd_data.value = 0

    async def reset(self):
        for _ in range(3):
            await RisingEdge(self.dut.clk)
        self.dut.rst.value = 0
        await RisingEdge(self.dut.clk)
        await ReadOnly()
        assert int(self.axil.awready.value) == 1
        assert int(self.axil.wready.value) == 1
        assert int(self.axil.arready.value) == 1
        assert int(self.axil.bvalid.value) == 0
        assert int(self.axil.rvalid.value) == 0
        assert int(self.cpuif.req.value) == 0


@cocotb.test()
async def test_001_independent_write_and_completion_handoff(dut):
    tb = TB(dut)
    await tb.reset()

    write_addr = 0x1000_0020
    write_data = 0xA55A_C33C
    write_strb = 0b0101
    read_addr = 0x2000_0040

    # Accept AW without W; no complete write request exists yet.
    await FallingEdge(dut.clk)
    tb.axil.awvalid.value = 1
    tb.axil.awaddr.value = write_addr
    await RisingEdge(dut.clk)
    await FallingEdge(dut.clk)
    tb.axil.awvalid.value = 0
    await Timer(1, unit="ns")
    assert int(tb.cpuif.req.value) == 0

    # W completes the request and falls through directly to CPUIF.
    tb.axil.wvalid.value = 1
    tb.axil.wdata.value = write_data
    tb.axil.wstrb.value = write_strb
    await Timer(1, unit="ns")
    assert int(tb.axil.wready.value) == 1
    assert int(tb.cpuif.req.value) == 1
    assert int(tb.cpuif.req_is_wr.value) == 1
    assert int(tb.cpuif.addr.value) == write_addr
    assert int(tb.cpuif.wr_data.value) == write_data
    assert int(tb.cpuif.wr_biten.value) == expanded_biten(write_strb)

    await RisingEdge(dut.clk)
    await FallingEdge(dut.clk)
    tb.axil.wvalid.value = 0
    await Timer(1, unit="ns")
    assert int(tb.cpuif.req.value) == 0

    # The next read is dispatched in the same cycle as the write ack.
    tb.cpuif.wr_ack.value = 1
    tb.axil.arvalid.value = 1
    tb.axil.araddr.value = read_addr
    await Timer(1, unit="ns")
    assert int(tb.cpuif.req.value) == 1
    assert int(tb.cpuif.req_is_wr.value) == 0
    assert int(tb.cpuif.addr.value) == read_addr

    await RisingEdge(dut.clk)
    await FallingEdge(dut.clk)
    tb.cpuif.wr_ack.value = 0
    tb.axil.arvalid.value = 0
    await Timer(1, unit="ns")
    assert int(tb.axil.bvalid.value) == 1
    assert int(tb.axil.bresp.value) == 0

    # The read may complete while the earlier B response is backpressured.
    read_data = 0xCAFE_F00D
    tb.cpuif.rd_data.value = read_data
    tb.cpuif.rd_ack.value = 1
    await RisingEdge(dut.clk)
    await FallingEdge(dut.clk)
    tb.cpuif.rd_ack.value = 0
    await Timer(1, unit="ns")
    assert int(tb.axil.bvalid.value) == 1
    assert int(tb.axil.rvalid.value) == 0

    # Fill request buffers while both response slots are occupied.
    third_addr = 0x3000_0080
    third_data = 0x1122_3344
    tb.axil.awvalid.value = 1
    tb.axil.awaddr.value = third_addr
    tb.axil.wvalid.value = 1
    tb.axil.wdata.value = third_data
    tb.axil.wstrb.value = 0b1111
    await RisingEdge(dut.clk)
    await FallingEdge(dut.clk)
    tb.axil.awvalid.value = 0
    tb.axil.wvalid.value = 0
    await Timer(1, unit="ns")
    assert int(tb.cpuif.req.value) == 0

    # Popping B frees a reserved slot and launches the buffered write at once.
    tb.axil.bready.value = 1
    await Timer(1, unit="ns")
    assert int(tb.axil.bvalid.value) == 1
    assert int(tb.cpuif.req.value) == 1
    assert int(tb.cpuif.req_is_wr.value) == 1
    assert int(tb.cpuif.addr.value) == third_addr
    assert int(tb.cpuif.wr_data.value) == third_data

    await RisingEdge(dut.clk)
    await FallingEdge(dut.clk)
    tb.axil.bready.value = 0
    await Timer(1, unit="ns")
    assert int(tb.axil.rvalid.value) == 1
    assert int(tb.axil.rdata.value) == read_data


@cocotb.test()
async def test_002_round_robin_and_error_responses(dut):
    tb = TB(dut)
    await tb.reset()

    # A simultaneous read and complete write select read after reset.
    await FallingEdge(dut.clk)
    tb.axil.arvalid.value = 1
    tb.axil.araddr.value = 0x100
    tb.axil.awvalid.value = 1
    tb.axil.awaddr.value = 0x200
    tb.axil.wvalid.value = 1
    tb.axil.wdata.value = 0xDEAD_BEEF
    tb.axil.wstrb.value = 0b1010
    await Timer(1, unit="ns")
    assert int(tb.cpuif.req.value) == 1
    assert int(tb.cpuif.req_is_wr.value) == 0
    assert int(tb.cpuif.addr.value) == 0x100

    await RisingEdge(dut.clk)
    await FallingEdge(dut.clk)
    tb.axil.arvalid.value = 0
    tb.axil.awvalid.value = 0
    tb.axil.wvalid.value = 0

    # Read error is queued while the buffered write is dispatched immediately.
    tb.cpuif.rd_ack.value = 1
    tb.cpuif.rd_err.value = 1
    tb.cpuif.rd_data.value = 0xBAD0_0001
    await Timer(1, unit="ns")
    assert int(tb.cpuif.req.value) == 1
    assert int(tb.cpuif.req_is_wr.value) == 1
    assert int(tb.cpuif.addr.value) == 0x200
    assert int(tb.cpuif.wr_data.value) == 0xDEAD_BEEF
    assert int(tb.cpuif.wr_biten.value) == expanded_biten(0b1010)

    await RisingEdge(dut.clk)
    await FallingEdge(dut.clk)
    tb.cpuif.rd_ack.value = 0
    tb.cpuif.rd_err.value = 0
    await Timer(1, unit="ns")
    assert int(tb.axil.rvalid.value) == 1
    assert int(tb.axil.rresp.value) == 0b10
    assert int(tb.axil.rdata.value) == 0xBAD0_0001

    tb.axil.rready.value = 1
    tb.cpuif.wr_ack.value = 1
    tb.cpuif.wr_err.value = 1
    await RisingEdge(dut.clk)
    await FallingEdge(dut.clk)
    tb.axil.rready.value = 0
    tb.cpuif.wr_ack.value = 0
    tb.cpuif.wr_err.value = 0
    await Timer(1, unit="ns")
    assert int(tb.axil.bvalid.value) == 1
    assert int(tb.axil.bresp.value) == 0b10


@cocotb.test()
async def test_003_stable_responses_under_backpressure(dut):
    tb = TB(dut)
    await tb.reset()

    await FallingEdge(dut.clk)
    tb.axil.arvalid.value = 1
    tb.axil.araddr.value = 0x400
    await RisingEdge(dut.clk)
    await FallingEdge(dut.clk)
    tb.axil.arvalid.value = 0
    tb.cpuif.rd_ack.value = 1
    tb.cpuif.rd_data.value = 0x1234_ABCD
    await RisingEdge(dut.clk)
    await FallingEdge(dut.clk)
    tb.cpuif.rd_ack.value = 0

    for _ in range(4):
        await Timer(1, unit="ns")
        assert int(tb.axil.rvalid.value) == 1
        assert int(tb.axil.rdata.value) == 0x1234_ABCD
        assert int(tb.axil.rresp.value) == 0
        await RisingEdge(dut.clk)
        await FallingEdge(dut.clk)


@cocotb.test()
async def test_004_reset_clears_buffers_and_responses(dut):
    tb = TB(dut)
    await tb.reset()

    await FallingEdge(dut.clk)
    tb.axil.awvalid.value = 1
    tb.axil.awaddr.value = 0x500
    await RisingEdge(dut.clk)
    await FallingEdge(dut.clk)
    tb.axil.awvalid.value = 0
    tb.dut.rst.value = 1
    await RisingEdge(dut.clk)
    await ReadOnly()
    assert int(tb.axil.awready.value) == 0
    assert int(tb.axil.wready.value) == 0
    assert int(tb.axil.arready.value) == 0
    assert int(tb.axil.bvalid.value) == 0
    assert int(tb.axil.rvalid.value) == 0
    assert int(tb.cpuif.req.value) == 0


@cocotb.test()
async def test_005_zero_latency_cpuif_completion(dut):
    tb = TB(dut)
    await tb.reset()

    # Model a combinational CPUIF write acknowledgement.
    await FallingEdge(dut.clk)
    tb.axil.awvalid.value = 1
    tb.axil.awaddr.value = 0x600
    tb.axil.wvalid.value = 1
    tb.axil.wdata.value = 0x9876_5432
    tb.axil.wstrb.value = 0b1111
    tb.cpuif.wr_ack.value = 1
    await Timer(1, unit="ns")
    assert int(tb.cpuif.req.value) == 1
    assert int(tb.cpuif.req_is_wr.value) == 1

    await RisingEdge(dut.clk)
    await FallingEdge(dut.clk)
    tb.axil.awvalid.value = 0
    tb.axil.wvalid.value = 0
    tb.cpuif.wr_ack.value = 0
    await Timer(1, unit="ns")
    assert int(tb.cpuif.req.value) == 0
    assert int(tb.axil.bvalid.value) == 1
    assert int(tb.axil.bresp.value) == 0

    # Consume B while a zero-latency read takes its place in the FIFO.
    tb.axil.bready.value = 1
    tb.axil.arvalid.value = 1
    tb.axil.araddr.value = 0x604
    tb.cpuif.rd_ack.value = 1
    tb.cpuif.rd_err.value = 1
    tb.cpuif.rd_data.value = 0x0BAD_C0DE
    await Timer(1, unit="ns")
    assert int(tb.cpuif.req.value) == 1
    assert int(tb.cpuif.req_is_wr.value) == 0

    await RisingEdge(dut.clk)
    await FallingEdge(dut.clk)
    tb.axil.bready.value = 0
    tb.axil.arvalid.value = 0
    tb.cpuif.rd_ack.value = 0
    tb.cpuif.rd_err.value = 0
    await Timer(1, unit="ns")
    assert int(tb.cpuif.req.value) == 0
    assert int(tb.axil.rvalid.value) == 1
    assert int(tb.axil.rresp.value) == 0b10
    assert int(tb.axil.rdata.value) == 0x0BAD_C0DE


# Pytest simulation runner

tests_dir = os.path.abspath(os.path.dirname(__file__))
repo_dir = os.path.abspath(os.path.join(tests_dir, "..", "..", ".."))
core_dir = os.path.join(repo_dir, "hw", "rtl", "core")
taxi_axi_dir = os.path.join(repo_dir, "libs", "taxi", "src", "axi", "rtl")
common_dir = os.path.join(repo_dir, "dv", "common")


def test_openenoc_axil_cpuif_adapter(request):
    module = os.path.splitext(os.path.basename(__file__))[0]
    sim_build = os.path.join(tests_dir, "sim_build", request.node.name)

    cocotb_test.simulator.run(
        simulator="verilator",
        python_search=[tests_dir],
        verilog_sources=[
            os.path.join(taxi_axi_dir, "taxi_axil_if.sv"),
            os.path.join(core_dir, "openenoc_cpuif_if.sv"),
            os.path.join(core_dir, "openenoc_axil_cpuif_adapter.sv"),
            os.path.join(tests_dir, f"{module}.sv"),
        ],
        toplevel=module,
        module=module,
        timescale="1ns/1ps",
        extra_args=["-Wall", os.path.join(common_dir, "config.vlt")],
        sim_build=sim_build,
    )
