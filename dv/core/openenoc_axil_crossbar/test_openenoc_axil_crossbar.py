# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: AGPL-3.0-or-later

import itertools
import logging
import os
import random

import cocotb
import cocotb_test.simulator
import pytest
from cocotb.clock import Clock
from cocotb.triggers import ReadOnly, RisingEdge
from cocotbext.axi import AxiLiteBus, AxiLiteMaster, AxiLiteRam
from cocotb.regression import TestFactory

TestFactory.__test__ = False


def parameter_int(name):
    return int(os.environ[f"PARAM_{name}"])


def target_base(index):
    return index << parameter_int("TARGET_ADDR_W")


def cycle_pause(pattern=(1, 1, 1, 0)):
    return itertools.cycle(pattern)


def random_pause(seed, probability=0.3):
    rng = random.Random(seed)
    while True:
        yield rng.random() < probability


def assert_okay(response):
    assert int(response.resp) == 0, f"Expected AXI OKAY, got {response.resp}"


class TB:
    def __init__(self, dut):
        self.dut = dut
        self.log = logging.getLogger("cocotb.tb")
        self.log.setLevel(logging.INFO)

        cocotb.start_soon(Clock(dut.clk, 10, unit="ns").start())

        self.masters = [
            AxiLiteMaster(AxiLiteBus.from_entity(channel), dut.clk, dut.rst)
            for channel in dut.s_axil_if
        ]
        self.rams = [
            AxiLiteRam(
                AxiLiteBus.from_entity(channel),
                dut.clk,
                dut.rst,
                size=1 << parameter_int("TARGET_ADDR_W"),
            )
            for channel in dut.m_axil_if
        ]

    async def reset(self):
        self.dut.rst.setimmediatevalue(0)
        await RisingEdge(self.dut.clk)
        await RisingEdge(self.dut.clk)
        self.dut.rst.value = 1
        await RisingEdge(self.dut.clk)
        await RisingEdge(self.dut.clk)
        self.dut.rst.value = 0
        await RisingEdge(self.dut.clk)
        await RisingEdge(self.dut.clk)

        for source in self.dut.s_axil_if:
            assert int(source.bvalid.value) == 0
            assert int(source.rvalid.value) == 0
        for target in self.dut.m_axil_if:
            assert int(target.awvalid.value) == 0
            assert int(target.wvalid.value) == 0
            assert int(target.arvalid.value) == 0

    def set_random_backpressure(self):
        for index, master in enumerate(self.masters):
            master.write_if.aw_channel.set_pause_generator(
                random_pause(0xA100 + index)
            )
            master.write_if.w_channel.set_pause_generator(
                random_pause(0xA200 + index)
            )
            master.read_if.ar_channel.set_pause_generator(
                random_pause(0xA300 + index)
            )
            master.write_if.b_channel.set_pause_generator(
                random_pause(0xB100 + index)
            )
            master.read_if.r_channel.set_pause_generator(
                random_pause(0xB200 + index)
            )

        for index, ram in enumerate(self.rams):
            ram.write_if.aw_channel.set_pause_generator(
                random_pause(0xC100 + index)
            )
            ram.write_if.w_channel.set_pause_generator(
                random_pause(0xC200 + index)
            )
            ram.write_if.b_channel.set_pause_generator(
                random_pause(0xC300 + index)
            )
            ram.read_if.ar_channel.set_pause_generator(
                random_pause(0xD100 + index)
            )
            ram.read_if.r_channel.set_pause_generator(
                random_pause(0xD200 + index)
            )


async def collect_handshake_cycles(clock, channel, valid_name, ready_name, count):
    cycles = []
    cycle = 0

    while len(cycles) < count:
        await RisingEdge(clock)
        cycle += 1
        if int(getattr(channel, valid_name).value) and int(
            getattr(channel, ready_name).value
        ):
            cycles.append(cycle)

    return cycles


async def wait_for_stall(clock, channel, valid_name, ready_name, timeout=32):
    for _ in range(timeout):
        await RisingEdge(clock)
        await ReadOnly()
        if int(getattr(channel, valid_name).value) and not int(
            getattr(channel, ready_name).value
        ):
            return
    raise AssertionError(f"{valid_name} did not enter a stalled state")


def assert_consecutive(cycles, channel_name):
    gaps = [right - left for left, right in zip(cycles, cycles[1:])]
    assert all(gap == 1 for gap in gaps), (
        f"{channel_name} inserted bubbles; handshake cycles were {cycles}"
    )


@cocotb.test()
async def test_001_routing_partial_writes_and_decode_errors(dut):
    tb = TB(dut)
    await tb.reset()

    byte_lanes = parameter_int("STRB_W")

    for source_index, master in enumerate(tb.masters):
        for target_index, ram in enumerate(tb.rams):
            local_address = 0x1000 + source_index * 0x100 + target_index * 0x20 + 1
            data = bytes(
                (0x20 + source_index * 0x30 + target_index * 7 + offset) & 0xff
                for offset in range(2 * byte_lanes + 1)
            )

            write = await master.write(target_base(target_index) + local_address, data)
            assert_okay(write)
            read = await master.read(target_base(target_index) + local_address, len(data))
            assert_okay(read)
            assert read.data == data
            assert ram.read(local_address, len(data)) == data

    invalid_address = 0x8000_0100
    invalid_write = await tb.masters[0].write(invalid_address, b"\x11\x22\x33\x44")
    assert int(invalid_write.resp) == 3
    invalid_read = await tb.masters[0].read(invalid_address, byte_lanes)
    assert int(invalid_read.resp) == 3
    assert invalid_read.data == bytes(byte_lanes)


@cocotb.test()
async def test_002_bubble_free_single_target_throughput(dut):
    tb = TB(dut)
    await tb.reset()

    word_count = 24
    byte_lanes = parameter_int("STRB_W")
    target_index = min(1, len(tb.rams) - 1)
    local_address = 0x2000
    address = target_base(target_index) + local_address
    read_data = bytes((0x40 + index) & 0xff for index in range(word_count * byte_lanes))
    tb.rams[target_index].write(local_address, read_data)

    ar_monitor = cocotb.start_soon(
        collect_handshake_cycles(
            dut.clk, dut.m_axil_if[target_index], "arvalid", "arready", word_count
        )
    )
    read = await tb.masters[0].read(address, len(read_data))
    ar_cycles = await ar_monitor
    assert_okay(read)
    assert read.data == read_data
    assert_consecutive(ar_cycles, "AR")

    write_data = bytes(
        (0xA0 ^ (index * 13)) & 0xff for index in range(word_count * byte_lanes)
    )
    aw_monitor = cocotb.start_soon(
        collect_handshake_cycles(
            dut.clk, dut.m_axil_if[target_index], "awvalid", "awready", word_count
        )
    )
    w_monitor = cocotb.start_soon(
        collect_handshake_cycles(
            dut.clk, dut.m_axil_if[target_index], "wvalid", "wready", word_count
        )
    )
    write = await tb.masters[0].write(address, write_data)
    aw_cycles = await aw_monitor
    w_cycles = await w_monitor
    assert_okay(write)
    assert_consecutive(aw_cycles, "AW")
    assert_consecutive(w_cycles, "W")
    assert tb.rams[target_index].read(local_address, len(write_data)) == write_data


@cocotb.test()
async def test_003_concurrent_sources_and_response_ordering(dut):
    tb = TB(dut)
    await tb.reset()

    # Delay one target so later transactions to another target can respond first
    # internally.  The source must still observe responses in request order.
    tb.rams[0].write_if.b_channel.set_pause_generator(cycle_pause((1, 1, 1, 0)))
    tb.rams[0].read_if.r_channel.set_pause_generator(cycle_pause((1, 1, 1, 0)))

    async def worker(source_index):
        master = tb.masters[source_index]
        expected = []
        read_tasks = []

        for operation in range(18):
            target_index = (operation + source_index) % len(tb.rams)
            local_address = 0x3000 + source_index * 0x800 + operation * 4
            value = (
                0x5100_0000 | source_index << 16 | operation
            ).to_bytes(4, "little")
            write = await master.write(target_base(target_index) + local_address, value)
            assert_okay(write)
            expected.append(value)
            read_tasks.append(
                cocotb.start_soon(
                    master.read(target_base(target_index) + local_address, 4)
                )
            )

        for task, value in zip(read_tasks, expected):
            response = await task
            assert_okay(response)
            assert response.data == value

    workers = [
        cocotb.start_soon(worker(source_index))
        for source_index in range(len(tb.masters))
    ]
    for worker_task in workers:
        await worker_task


@cocotb.test()
async def test_004_randomized_independent_backpressure(dut):
    tb = TB(dut)
    await tb.reset()
    tb.set_random_backpressure()

    async def worker(source_index):
        rng = random.Random(0xE100 + source_index)
        master = tb.masters[source_index]

        for operation in range(32):
            target_index = rng.randrange(len(tb.rams))
            length = rng.randint(1, 13)
            local_address = 0x6000 + source_index * 0x1000 + operation * 16
            data = bytes(rng.randrange(256) for _ in range(length))
            address = target_base(target_index) + local_address

            write = await master.write(address, data)
            assert_okay(write)
            read = await master.read(address, length)
            assert_okay(read)
            assert read.data == data

    workers = [
        cocotb.start_soon(worker(source_index))
        for source_index in range(len(tb.masters))
    ]
    for worker_task in workers:
        await worker_task


@cocotb.test()
async def test_005_stalled_payload_stability(dut):
    tb = TB(dut)
    await tb.reset()

    target_index = 0
    address = target_base(target_index) + 0x4200
    data = bytes.fromhex("78563412")

    tb.rams[target_index].read_if.ar_channel.set_pause_generator(
        itertools.repeat(True)
    )
    tb.rams[target_index].write_if.aw_channel.set_pause_generator(
        itertools.repeat(True)
    )
    tb.rams[target_index].write_if.w_channel.set_pause_generator(
        itertools.repeat(True)
    )

    read_task = cocotb.start_soon(tb.masters[0].read(address, len(data)))
    await wait_for_stall(dut.clk, dut.m_axil_if[target_index], "arvalid", "arready")
    held_ar = (
        int(dut.m_axil_if[target_index].araddr.value),
        int(dut.m_axil_if[target_index].arprot.value),
    )
    for _ in range(5):
        await RisingEdge(dut.clk)
        await ReadOnly()
        assert int(dut.m_axil_if[target_index].arvalid.value) == 1
        assert (
            int(dut.m_axil_if[target_index].araddr.value),
            int(dut.m_axil_if[target_index].arprot.value),
        ) == held_ar

    tb.masters[0].read_if.r_channel.set_pause_generator(itertools.repeat(True))
    tb.rams[target_index].read_if.ar_channel.set_pause_generator(None)
    tb.rams[target_index].read_if.ar_channel.pause = False
    await wait_for_stall(dut.clk, dut.s_axil_if[0], "rvalid", "rready")
    held_r = (
        int(dut.s_axil_if[0].rdata.value),
        int(dut.s_axil_if[0].rresp.value),
    )
    for _ in range(5):
        await RisingEdge(dut.clk)
        await ReadOnly()
        assert int(dut.s_axil_if[0].rvalid.value) == 1
        assert (
            int(dut.s_axil_if[0].rdata.value),
            int(dut.s_axil_if[0].rresp.value),
        ) == held_r
    tb.masters[0].read_if.r_channel.set_pause_generator(None)
    tb.masters[0].read_if.r_channel.pause = False
    read = await read_task
    assert_okay(read)

    write_task = cocotb.start_soon(tb.masters[0].write(address, data))
    await wait_for_stall(dut.clk, dut.m_axil_if[target_index], "awvalid", "awready")
    await wait_for_stall(dut.clk, dut.m_axil_if[target_index], "wvalid", "wready")
    held_aw = (
        int(dut.m_axil_if[target_index].awaddr.value),
        int(dut.m_axil_if[target_index].awprot.value),
    )
    held_w = (
        int(dut.m_axil_if[target_index].wdata.value),
        int(dut.m_axil_if[target_index].wstrb.value),
    )
    for _ in range(5):
        await RisingEdge(dut.clk)
        await ReadOnly()
        assert int(dut.m_axil_if[target_index].awvalid.value) == 1
        assert int(dut.m_axil_if[target_index].wvalid.value) == 1
        assert (
            int(dut.m_axil_if[target_index].awaddr.value),
            int(dut.m_axil_if[target_index].awprot.value),
        ) == held_aw
        assert (
            int(dut.m_axil_if[target_index].wdata.value),
            int(dut.m_axil_if[target_index].wstrb.value),
        ) == held_w

    # Release the independent channels in different cycles.
    tb.masters[0].write_if.b_channel.set_pause_generator(itertools.repeat(True))
    tb.rams[target_index].write_if.w_channel.set_pause_generator(None)
    tb.rams[target_index].write_if.w_channel.pause = False
    for _ in range(3):
        await RisingEdge(dut.clk)
    tb.rams[target_index].write_if.aw_channel.set_pause_generator(None)
    tb.rams[target_index].write_if.aw_channel.pause = False
    await wait_for_stall(dut.clk, dut.s_axil_if[0], "bvalid", "bready")
    held_b = int(dut.s_axil_if[0].bresp.value)
    for _ in range(5):
        await RisingEdge(dut.clk)
        await ReadOnly()
        assert int(dut.s_axil_if[0].bvalid.value) == 1
        assert int(dut.s_axil_if[0].bresp.value) == held_b
    tb.masters[0].write_if.b_channel.set_pause_generator(None)
    tb.masters[0].write_if.b_channel.pause = False
    write = await write_task
    assert_okay(write)
    assert tb.rams[target_index].read(0x4200, len(data)) == data


tests_dir = os.path.abspath(os.path.dirname(__file__))
repo_dir = os.path.abspath(os.path.join(tests_dir, "..", "..", ".."))
core_dir = os.path.join(repo_dir, "hw", "rtl", "core")
taxi_axi_dir = os.path.join(repo_dir, "libs", "taxi", "src", "axi", "rtl")
common_dir = os.path.join(repo_dir, "dv", "common")


@pytest.mark.parametrize(("s_count", "m_count"), [(1, 1), (3, 3)])
def test_openenoc_axil_crossbar(request, s_count, m_count):
    module = os.path.splitext(os.path.basename(__file__))[0]
    toplevel = module

    verilog_sources = [
        os.path.join(taxi_axi_dir, "taxi_axil_if.sv"),
        os.path.join(core_dir, "openenoc_axil_crossbar_skid_buffer.sv"),
        os.path.join(core_dir, "openenoc_axil_crossbar_arbiter.sv"),
        os.path.join(core_dir, "openenoc_axil_crossbar_addr.sv"),
        os.path.join(core_dir, "openenoc_axil_crossbar_wr.sv"),
        os.path.join(core_dir, "openenoc_axil_crossbar_rd.sv"),
        os.path.join(core_dir, "openenoc_axil_crossbar.sv"),
        os.path.join(tests_dir, f"{toplevel}.sv"),
    ]

    parameters = {
        "S_COUNT": s_count,
        "M_COUNT": m_count,
        "DATA_W": 32,
        "ADDR_W": 32,
        "STRB_W": 4,
        "TARGET_ADDR_W": 16,
    }
    extra_env = {f"PARAM_{name}": str(value) for name, value in parameters.items()}

    sim_build = os.path.join(tests_dir, "sim_build", request.node.name)
    cocotb_test.simulator.run(
        simulator="verilator",
        python_search=[tests_dir],
        verilog_sources=verilog_sources,
        toplevel=toplevel,
        module=module,
        parameters=parameters,
        extra_args=["-Wall", os.path.join(common_dir, "config.vlt")],
        sim_build=sim_build,
        extra_env=extra_env,
    )
