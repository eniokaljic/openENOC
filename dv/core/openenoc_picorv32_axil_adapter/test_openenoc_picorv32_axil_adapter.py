# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: AGPL-3.0-or-later

import os
import random

import cocotb
import cocotb_test.simulator
from cocotb.clock import Clock
from cocotb.triggers import FallingEdge, ReadOnly, RisingEdge, Timer


def signal_integer(signal):
    return int(signal.value)


class TB:
    def __init__(self, dut):
        self.dut = dut
        cocotb.start_soon(Clock(dut.clk, 10, unit="ns").start())
        self.drive_idle()

    def drive_idle(self):
        self.dut.resetn.value = 0

        self.dut.mem_axi_awready.value = 0
        self.dut.mem_axi_wready.value = 0
        self.dut.mem_axi_bvalid.value = 0
        self.dut.mem_axi_arready.value = 0
        self.dut.mem_axi_rvalid.value = 0
        self.dut.mem_axi_rdata.value = 0

        self.dut.mem_valid.value = 0
        self.dut.mem_instr.value = 0
        self.dut.mem_addr.value = 0
        self.dut.mem_wdata.value = 0
        self.dut.mem_wstrb.value = 0

        self.dut.mem_la_read.value = 0
        self.dut.mem_la_write.value = 0
        self.dut.mem_la_addr.value = 0
        self.dut.mem_la_wdata.value = 0
        self.dut.mem_la_wstrb.value = 0

    async def reset(self):
        for _ in range(2):
            await RisingEdge(self.dut.clk)

        self.dut.resetn.value = 1
        await RisingEdge(self.dut.clk)
        await ReadOnly()

        assert signal_integer(self.dut.mem_axi_awvalid) == 0
        assert signal_integer(self.dut.mem_axi_wvalid) == 0
        assert signal_integer(self.dut.mem_axi_arvalid) == 0
        assert signal_integer(self.dut.mem_axi_bready) == 0
        assert signal_integer(self.dut.mem_axi_rready) == 0
        assert signal_integer(self.dut.mem_ready) == 0

        await FallingEdge(self.dut.clk)

    async def drive_lookahead(self, *, address, data=0, strobe=0, instr=False):
        await FallingEdge(self.dut.clk)
        self.dut.mem_la_read.value = int(strobe == 0)
        self.dut.mem_la_write.value = int(strobe != 0)
        self.dut.mem_la_addr.value = address
        self.dut.mem_la_wdata.value = data
        self.dut.mem_la_wstrb.value = strobe
        self.dut.mem_instr.value = int(instr)

        await RisingEdge(self.dut.clk)
        await ReadOnly()

        await FallingEdge(self.dut.clk)
        self.dut.mem_la_read.value = 0
        self.dut.mem_la_write.value = 0
        self.dut.mem_valid.value = 1
        self.dut.mem_addr.value = address
        self.dut.mem_wdata.value = data
        self.dut.mem_wstrb.value = strobe
        self.dut.mem_instr.value = int(instr)
        await Timer(1, unit="ns")

    async def finish_native_request(self):
        await RisingEdge(self.dut.clk)
        await ReadOnly()
        await FallingEdge(self.dut.clk)
        self.dut.mem_valid.value = 0
        self.dut.mem_axi_bvalid.value = 0
        self.dut.mem_axi_rvalid.value = 0


@cocotb.test()
async def test_001_independent_write_channels_and_stability(dut):
    tb = TB(dut)
    await tb.reset()

    address = 0x1234_5678
    data = 0xA55A_C33C
    strobe = 0b0101

    # W is accepted first while AW and its payload remain stalled.
    dut.mem_axi_awready.value = 0
    dut.mem_axi_wready.value = 1
    await tb.drive_lookahead(address=address, data=data, strobe=strobe)

    assert signal_integer(dut.mem_axi_awvalid) == 1
    assert signal_integer(dut.mem_axi_wvalid) == 1
    assert signal_integer(dut.mem_axi_awaddr) == address
    assert signal_integer(dut.mem_axi_wdata) == data
    assert signal_integer(dut.mem_axi_wstrb) == strobe
    assert signal_integer(dut.mem_axi_awprot) == 0

    await RisingEdge(dut.clk)
    await ReadOnly()
    assert signal_integer(dut.mem_axi_wvalid) == 0
    assert signal_integer(dut.mem_axi_awvalid) == 1

    # Native payload changes must not affect a stalled AXI request.
    await FallingEdge(dut.clk)
    dut.mem_addr.value = 0xDEAD_BEEF
    dut.mem_wdata.value = 0x1122_3344
    dut.mem_wstrb.value = 0b1111
    await Timer(1, unit="ns")
    stalled_payload = (
        signal_integer(dut.mem_axi_awaddr),
        signal_integer(dut.mem_axi_awprot),
    )

    for _ in range(3):
        await RisingEdge(dut.clk)
        await ReadOnly()
        assert signal_integer(dut.mem_axi_awvalid) == 1
        assert (
            signal_integer(dut.mem_axi_awaddr),
            signal_integer(dut.mem_axi_awprot),
        ) == stalled_payload

    await FallingEdge(dut.clk)
    dut.mem_axi_awready.value = 1
    await RisingEdge(dut.clk)
    await ReadOnly()
    assert signal_integer(dut.mem_axi_awvalid) == 0

    await FallingEdge(dut.clk)
    dut.mem_axi_bvalid.value = 1
    await Timer(1, unit="ns")
    assert signal_integer(dut.mem_axi_bready) == 1
    assert signal_integer(dut.mem_ready) == 1
    await tb.finish_native_request()

    # Repeat with AW accepted first and W held under backpressure.
    second_address = address + 4
    second_data = 0x5AA5_3CC3
    second_strobe = 0b1010
    dut.mem_axi_awready.value = 1
    dut.mem_axi_wready.value = 0
    await tb.drive_lookahead(
        address=second_address,
        data=second_data,
        strobe=second_strobe,
    )

    await RisingEdge(dut.clk)
    await ReadOnly()
    assert signal_integer(dut.mem_axi_awvalid) == 0
    assert signal_integer(dut.mem_axi_wvalid) == 1

    for _ in range(2):
        assert signal_integer(dut.mem_axi_wdata) == second_data
        assert signal_integer(dut.mem_axi_wstrb) == second_strobe
        await RisingEdge(dut.clk)
        await ReadOnly()

    await FallingEdge(dut.clk)
    dut.mem_axi_wready.value = 1
    await RisingEdge(dut.clk)
    await ReadOnly()
    assert signal_integer(dut.mem_axi_wvalid) == 0

    await FallingEdge(dut.clk)
    dut.mem_axi_bvalid.value = 1
    await Timer(1, unit="ns")
    assert signal_integer(dut.mem_ready) == 1
    await tb.finish_native_request()


@cocotb.test()
async def test_002_read_backpressure_response_and_protection(dut):
    tb = TB(dut)
    await tb.reset()

    address = 0x0040_0100
    read_data = 0xCAFE_F00D

    dut.mem_axi_arready.value = 0
    await tb.drive_lookahead(address=address, instr=True)

    stalled_payload = (
        signal_integer(dut.mem_axi_araddr),
        signal_integer(dut.mem_axi_arprot),
    )
    assert stalled_payload == (address, 0b100)

    for _ in range(4):
        await RisingEdge(dut.clk)
        await ReadOnly()
        assert signal_integer(dut.mem_axi_arvalid) == 1
        assert (
            signal_integer(dut.mem_axi_araddr),
            signal_integer(dut.mem_axi_arprot),
        ) == stalled_payload

    await FallingEdge(dut.clk)
    dut.mem_axi_arready.value = 1
    await RisingEdge(dut.clk)
    await ReadOnly()
    assert signal_integer(dut.mem_axi_arvalid) == 0

    await FallingEdge(dut.clk)
    dut.mem_axi_rdata.value = read_data
    dut.mem_axi_rvalid.value = 1
    await Timer(1, unit="ns")
    assert signal_integer(dut.mem_axi_rready) == 1
    assert signal_integer(dut.mem_ready) == 1
    assert signal_integer(dut.mem_rdata) == read_data
    await tb.finish_native_request()


@cocotb.test()
async def test_003_back_to_back_lookahead_requests(dut):
    tb = TB(dut)
    await tb.reset()

    first_address = 0x0000_1000
    second_address = 0x0000_1004

    dut.mem_axi_arready.value = 1
    await tb.drive_lookahead(address=first_address, instr=True)

    assert signal_integer(dut.mem_axi_arvalid) == 1
    await RisingEdge(dut.clk)
    await ReadOnly()
    assert signal_integer(dut.mem_axi_arvalid) == 0

    # Complete request 0 while PicoRV32 presents request 1 look-ahead.
    await FallingEdge(dut.clk)
    dut.mem_axi_rvalid.value = 1
    dut.mem_axi_rdata.value = 0x1111_1111
    dut.mem_la_read.value = 1
    dut.mem_la_addr.value = second_address
    dut.mem_la_wstrb.value = 0
    await Timer(1, unit="ns")
    assert signal_integer(dut.mem_ready) == 1

    await RisingEdge(dut.clk)
    await ReadOnly()
    assert signal_integer(dut.mem_axi_arvalid) == 1
    assert signal_integer(dut.mem_axi_araddr) == second_address

    # The second AR transfer follows on the immediately next AXI clock edge.
    await FallingEdge(dut.clk)
    dut.mem_axi_rvalid.value = 0
    dut.mem_la_read.value = 0
    dut.mem_addr.value = second_address
    await RisingEdge(dut.clk)
    await ReadOnly()
    assert signal_integer(dut.mem_axi_arvalid) == 0

    await FallingEdge(dut.clk)
    dut.mem_axi_rvalid.value = 1
    dut.mem_axi_rdata.value = 0x2222_2222
    await Timer(1, unit="ns")
    assert signal_integer(dut.mem_ready) == 1
    assert signal_integer(dut.mem_rdata) == 0x2222_2222
    await tb.finish_native_request()


@cocotb.test()
async def test_004_reset_clears_stalled_transaction(dut):
    tb = TB(dut)
    await tb.reset()

    await tb.drive_lookahead(
        address=0x2000_0020,
        data=0x55AA_00FF,
        strobe=0b1111,
    )
    assert signal_integer(dut.mem_axi_awvalid) == 1
    assert signal_integer(dut.mem_axi_wvalid) == 1

    await FallingEdge(dut.clk)
    dut.resetn.value = 0
    await RisingEdge(dut.clk)
    await ReadOnly()
    assert signal_integer(dut.mem_axi_awvalid) == 0
    assert signal_integer(dut.mem_axi_wvalid) == 0
    assert signal_integer(dut.mem_axi_arvalid) == 0
    assert signal_integer(dut.mem_axi_bready) == 0
    assert signal_integer(dut.mem_axi_rready) == 0
    assert signal_integer(dut.mem_ready) == 0

    await FallingEdge(dut.clk)
    dut.mem_valid.value = 0
    dut.resetn.value = 1
    await RisingEdge(dut.clk)
    await ReadOnly()

    # Confirm normal operation after reset with the no-look-ahead fallback.
    await FallingEdge(dut.clk)
    dut.mem_valid.value = 1
    dut.mem_addr.value = 0x3000_0000
    dut.mem_wstrb.value = 0
    dut.mem_instr.value = 0
    dut.mem_axi_arready.value = 1
    await RisingEdge(dut.clk)
    await ReadOnly()
    assert signal_integer(dut.mem_axi_arvalid) == 1


@cocotb.test()
async def test_005_randomized_channel_backpressure_and_ordering(dut):
    tb = TB(dut)
    await tb.reset()

    rng = random.Random(0xA41_1E)

    for index in range(48):
        is_write = rng.choice((False, True))
        address = 0x1000 + 4 * index
        data = rng.randrange(1 << 32)
        strobe = rng.randrange(1, 16) if is_write else 0
        instr = not is_write and index % 3 == 0

        await tb.drive_lookahead(
            address=address,
            data=data,
            strobe=strobe,
            instr=instr,
        )

        aw_seen = False
        w_seen = False
        ar_seen = False
        stalled_aw = None
        stalled_w = None
        stalled_ar = None

        for _ in range(80):
            dut.mem_axi_awready.value = rng.randrange(2)
            dut.mem_axi_wready.value = rng.randrange(2)
            dut.mem_axi_arready.value = rng.randrange(2)
            await Timer(1, unit="ns")

            awvalid = signal_integer(dut.mem_axi_awvalid)
            wvalid = signal_integer(dut.mem_axi_wvalid)
            arvalid = signal_integer(dut.mem_axi_arvalid)

            if awvalid and not signal_integer(dut.mem_axi_awready):
                payload = signal_integer(dut.mem_axi_awaddr)
                if stalled_aw is not None:
                    assert payload == stalled_aw
                stalled_aw = payload

            if wvalid and not signal_integer(dut.mem_axi_wready):
                payload = (
                    signal_integer(dut.mem_axi_wdata),
                    signal_integer(dut.mem_axi_wstrb),
                )
                if stalled_w is not None:
                    assert payload == stalled_w
                stalled_w = payload

            if arvalid and not signal_integer(dut.mem_axi_arready):
                payload = (
                    signal_integer(dut.mem_axi_araddr),
                    signal_integer(dut.mem_axi_arprot),
                )
                if stalled_ar is not None:
                    assert payload == stalled_ar
                stalled_ar = payload

            aw_fire = awvalid and signal_integer(dut.mem_axi_awready)
            w_fire = wvalid and signal_integer(dut.mem_axi_wready)
            ar_fire = arvalid and signal_integer(dut.mem_axi_arready)

            await RisingEdge(dut.clk)
            await ReadOnly()

            aw_seen |= bool(aw_fire)
            w_seen |= bool(w_fire)
            ar_seen |= bool(ar_fire)

            if (is_write and aw_seen and w_seen) or (not is_write and ar_seen):
                break

            await FallingEdge(dut.clk)
        else:
            raise AssertionError("AXI request did not complete under randomized READY")

        await FallingEdge(dut.clk)
        if is_write:
            dut.mem_axi_bvalid.value = 1
        else:
            dut.mem_axi_rvalid.value = 1
            dut.mem_axi_rdata.value = data
        await Timer(1, unit="ns")

        assert signal_integer(dut.mem_ready) == 1
        if not is_write:
            assert signal_integer(dut.mem_rdata) == data

        await tb.finish_native_request()


# Pytest simulation runner

tests_dir = os.path.abspath(os.path.dirname(__file__))
repo_dir = os.path.abspath(os.path.join(tests_dir, "..", "..", ".."))
core_dir = os.path.join(repo_dir, "hw", "rtl", "core")
common_dir = os.path.join(repo_dir, "dv", "common")


def test_openenoc_picorv32_axil_adapter(request):
    module = os.path.splitext(os.path.basename(__file__))[0]
    toplevel = module

    verilog_sources = [
        os.path.join(core_dir, "openenoc_picorv32_axil_adapter.sv"),
        os.path.join(tests_dir, f"{toplevel}.sv"),
    ]

    sim_build = os.path.join(tests_dir, "sim_build", request.node.name)

    cocotb_test.simulator.run(
        simulator="verilator",
        python_search=[tests_dir],
        verilog_sources=verilog_sources,
        toplevel=toplevel,
        module=module,
        extra_args=[os.path.join(common_dir, "config.vlt")],
        sim_build=sim_build,
    )
