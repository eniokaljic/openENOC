# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: AGPL-3.0-or-later

import os

import cocotb
import cocotb_test.simulator
from cocotb.clock import Clock
from cocotb.triggers import FallingEdge, ReadOnly, RisingEdge, Timer


def expand_strobe(strobe, lanes=4):
    biten = 0
    for lane in range(lanes):
        if strobe & (1 << lane):
            biten |= 0xFF << (lane * 8)
    return biten


class TB:
    def __init__(self, dut):
        self.dut = dut
        self.cpuif = dut.cpuif
        self.axil = dut.axil
        cocotb.start_soon(Clock(dut.clk, 10, unit="ns").start())
        self.drive_idle()

    def drive_idle(self):
        self.dut.rst.value = 1

        self.cpuif.req.value = 0
        self.cpuif.addr.value = 0
        self.cpuif.req_is_wr.value = 0
        self.cpuif.wr_data.value = 0
        self.cpuif.wr_biten.value = 0

        self.axil.awready.value = 0
        self.axil.wready.value = 0
        self.axil.bvalid.value = 0
        self.axil.bresp.value = 0
        self.axil.buser.value = 0
        self.axil.arready.value = 0
        self.axil.rvalid.value = 0
        self.axil.rdata.value = 0
        self.axil.rresp.value = 0
        self.axil.ruser.value = 0

    async def reset(self):
        for _ in range(3):
            await RisingEdge(self.dut.clk)
        self.dut.rst.value = 0
        await RisingEdge(self.dut.clk)
        await ReadOnly()
        assert int(self.axil.awvalid.value) == 0
        assert int(self.axil.wvalid.value) == 0
        assert int(self.axil.arvalid.value) == 0
        assert int(self.axil.bready.value) == 0
        assert int(self.axil.rready.value) == 0
        assert int(self.cpuif.wr_ack.value) == 0
        assert int(self.cpuif.rd_ack.value) == 0
        await FallingEdge(self.dut.clk)

    async def drive_request(self, address, *, data=0, strobe=0):
        await FallingEdge(self.dut.clk)
        self.cpuif.req.value = 1
        self.cpuif.addr.value = address
        self.cpuif.req_is_wr.value = int(strobe != 0)
        self.cpuif.wr_data.value = data
        self.cpuif.wr_biten.value = expand_strobe(strobe)
        await Timer(1, unit="ns")

    async def retire_request_strobe(self):
        await RisingEdge(self.dut.clk)
        await ReadOnly()
        await FallingEdge(self.dut.clk)
        self.cpuif.req.value = 0


@cocotb.test()
async def test_001_independent_write_channels_and_error(dut):
    tb = TB(dut)
    await tb.reset()

    address = 0x1234_5678
    data = 0xA55A_C33C
    strobe = 0b0101

    tb.axil.awready.value = 0
    tb.axil.wready.value = 1
    await tb.drive_request(address, data=data, strobe=strobe)

    assert int(tb.axil.awvalid.value) == 1
    assert int(tb.axil.wvalid.value) == 1
    assert int(tb.axil.awaddr.value) == address
    assert int(tb.axil.awprot.value) == 0
    assert int(tb.axil.wdata.value) == data
    assert int(tb.axil.wstrb.value) == strobe

    await tb.retire_request_strobe()
    assert int(tb.axil.awvalid.value) == 1
    assert int(tb.axil.wvalid.value) == 0

    # CPUIF payload changes cannot disturb a stalled AXI request.
    tb.cpuif.addr.value = 0xDEAD_BEEF
    tb.cpuif.wr_data.value = 0x1122_3344
    tb.cpuif.wr_biten.value = 0xFFFF_FFFF
    for _ in range(3):
        await RisingEdge(dut.clk)
        await ReadOnly()
        assert int(tb.axil.awvalid.value) == 1
        assert int(tb.axil.awaddr.value) == address

    await FallingEdge(dut.clk)
    tb.axil.awready.value = 1
    await RisingEdge(dut.clk)
    await ReadOnly()
    assert int(tb.axil.awvalid.value) == 0

    await FallingEdge(dut.clk)
    tb.axil.bresp.value = 0b10
    tb.axil.bvalid.value = 1
    await Timer(1, unit="ns")
    assert int(tb.axil.bready.value) == 1
    assert int(tb.cpuif.wr_ack.value) == 1
    assert int(tb.cpuif.wr_err.value) == 1
    assert int(tb.cpuif.rd_ack.value) == 0

    await RisingEdge(dut.clk)
    await FallingEdge(dut.clk)
    tb.axil.bvalid.value = 0
    await Timer(1, unit="ns")
    assert int(tb.cpuif.wr_ack.value) == 0


@cocotb.test()
async def test_002_read_stability_and_response(dut):
    tb = TB(dut)
    await tb.reset()

    address = 0x0040_0100
    read_data = 0xCAFE_F00D

    tb.axil.arready.value = 0
    await tb.drive_request(address)
    assert int(tb.axil.arvalid.value) == 1
    assert int(tb.axil.araddr.value) == address
    assert int(tb.axil.arprot.value) == 0

    await tb.retire_request_strobe()
    tb.cpuif.addr.value = 0xFFFF_0000
    for _ in range(3):
        await RisingEdge(dut.clk)
        await ReadOnly()
        assert int(tb.axil.arvalid.value) == 1
        assert int(tb.axil.araddr.value) == address

    await FallingEdge(dut.clk)
    tb.axil.arready.value = 1
    await RisingEdge(dut.clk)
    await ReadOnly()
    assert int(tb.axil.arvalid.value) == 0

    await FallingEdge(dut.clk)
    tb.axil.rdata.value = read_data
    tb.axil.rresp.value = 0
    tb.axil.rvalid.value = 1
    await Timer(1, unit="ns")
    assert int(tb.axil.rready.value) == 1
    assert int(tb.cpuif.rd_ack.value) == 1
    assert int(tb.cpuif.rd_err.value) == 0
    assert int(tb.cpuif.rd_data.value) == read_data


@cocotb.test()
async def test_003_bubble_free_completion_to_next_request(dut):
    tb = TB(dut)
    await tb.reset()

    first_address = 0x1000
    second_address = 0x2000
    second_data = 0x55AA_0FF0

    tb.axil.arready.value = 1
    await tb.drive_request(first_address)
    await tb.retire_request_strobe()
    assert int(tb.axil.arvalid.value) == 0

    # Complete the read and present the next CPUIF request in the same cycle.
    tb.axil.awready.value = 1
    tb.axil.wready.value = 1
    tb.axil.rdata.value = 0x1234_5678
    tb.axil.rvalid.value = 1
    tb.cpuif.req.value = 1
    tb.cpuif.req_is_wr.value = 1
    tb.cpuif.addr.value = second_address
    tb.cpuif.wr_data.value = second_data
    tb.cpuif.wr_biten.value = expand_strobe(0b1111)
    await Timer(1, unit="ns")

    assert int(tb.cpuif.rd_ack.value) == 1
    assert int(tb.axil.awvalid.value) == 1
    assert int(tb.axil.wvalid.value) == 1
    assert int(tb.axil.awaddr.value) == second_address
    assert int(tb.axil.wdata.value) == second_data

    await RisingEdge(dut.clk)
    await FallingEdge(dut.clk)
    tb.axil.rvalid.value = 0
    tb.cpuif.req.value = 0
    await Timer(1, unit="ns")
    assert int(tb.axil.awvalid.value) == 0
    assert int(tb.axil.wvalid.value) == 0
    assert int(tb.axil.bready.value) == 1

    tb.axil.bvalid.value = 1
    await Timer(1, unit="ns")
    assert int(tb.cpuif.wr_ack.value) == 1
    assert int(tb.cpuif.wr_err.value) == 0


@cocotb.test()
async def test_004_reset_clears_stalled_request(dut):
    tb = TB(dut)
    await tb.reset()

    await tb.drive_request(0x3000, data=0xABCD_EF01, strobe=0b1111)
    await tb.retire_request_strobe()
    assert int(tb.axil.awvalid.value) == 1
    assert int(tb.axil.wvalid.value) == 1

    tb.dut.rst.value = 1
    await RisingEdge(dut.clk)
    await ReadOnly()
    assert int(tb.axil.awvalid.value) == 0
    assert int(tb.axil.wvalid.value) == 0
    assert int(tb.axil.arvalid.value) == 0
    assert int(tb.axil.bready.value) == 0
    assert int(tb.axil.rready.value) == 0
    assert int(tb.cpuif.wr_ack.value) == 0
    assert int(tb.cpuif.rd_ack.value) == 0


# Pytest simulation runner

tests_dir = os.path.abspath(os.path.dirname(__file__))
repo_dir = os.path.abspath(os.path.join(tests_dir, "..", "..", ".."))
core_dir = os.path.join(repo_dir, "hw", "rtl", "core")
taxi_axi_dir = os.path.join(repo_dir, "libs", "taxi", "src", "axi", "rtl")
common_dir = os.path.join(repo_dir, "dv", "common")


def test_openenoc_cpuif_axil_adapter(request):
    module = os.path.splitext(os.path.basename(__file__))[0]
    sim_build = os.path.join(tests_dir, "sim_build", request.node.name)

    cocotb_test.simulator.run(
        simulator="verilator",
        python_search=[tests_dir],
        verilog_sources=[
            os.path.join(taxi_axi_dir, "taxi_axil_if.sv"),
            os.path.join(core_dir, "openenoc_cpuif_if.sv"),
            os.path.join(core_dir, "openenoc_cpuif_axil_adapter.sv"),
            os.path.join(tests_dir, f"{module}.sv"),
        ],
        toplevel=module,
        module=module,
        timescale="1ns/1ps",
        extra_args=["-Wall", os.path.join(common_dir, "config.vlt")],
        sim_build=sim_build,
    )
