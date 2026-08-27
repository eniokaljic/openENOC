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
from cocotb.triggers import FallingEdge, ReadOnly, RisingEdge, Timer
from cocotbext.axi import AxiLiteBus, AxiLiteMaster
from cocotb.regression import TestFactory
TestFactory.__test__ = False

def parameter_int(name):
    return int(os.environ[f"PARAM_{name}"])


def initialization_file():
    return os.environ.get("PARAM_INIT_FILE", "").strip('"')


def cycle_pause(pattern=(1, 1, 1, 0)):
    return itertools.cycle(pattern)


def random_pause(seed, pause_probability=0.35):
    rng = random.Random(seed)
    while True:
        yield rng.random() < pause_probability


def assert_okay(response):
    assert int(response.resp) == 0, f"Expected AXI OKAY response, got {response.resp}"


class TB:
    def __init__(self, dut, create_master=True):
        self.dut = dut

        self.log = logging.getLogger("cocotb.tb")
        self.log.setLevel(logging.DEBUG)

        cocotb.start_soon(Clock(dut.clk, 10, unit="ns").start())

        self.axil_master = None
        if create_master:
            self.axil_master = AxiLiteMaster(
                AxiLiteBus.from_entity(dut.s_axil), dut.clk, dut.rst
            )
        else:
            self.drive_axil_idle()

    @property
    def aperture(self):
        return 1 << parameter_int("ADDR_W")

    @property
    def byte_lanes(self):
        return parameter_int("STRB_W")

    def set_stress_pause_generators(self):
        # Different request patterns exercise independent AW, W, and AR channels.
        self.axil_master.write_if.aw_channel.set_pause_generator(
            cycle_pause((1, 0, 0, 0))
        )
        self.axil_master.write_if.w_channel.set_pause_generator(
            cycle_pause((0, 1, 0, 0))
        )
        self.axil_master.read_if.ar_channel.set_pause_generator(
            cycle_pause((1, 0, 1, 0, 0))
        )
        self.axil_master.write_if.b_channel.set_pause_generator(cycle_pause())
        self.axil_master.read_if.r_channel.set_pause_generator(
            cycle_pause((1, 0, 1, 1, 0))
        )

    def set_random_pause_generators(self):
        self.axil_master.write_if.aw_channel.set_pause_generator(
            random_pause(0xA001)
        )
        self.axil_master.write_if.w_channel.set_pause_generator(
            random_pause(0xA002)
        )
        self.axil_master.read_if.ar_channel.set_pause_generator(
            random_pause(0xA003)
        )
        self.axil_master.write_if.b_channel.set_pause_generator(
            random_pause(0xB001)
        )
        self.axil_master.read_if.r_channel.set_pause_generator(
            random_pause(0xB002)
        )

    def drive_axil_idle(self):
        self.dut.s_axil.awaddr.value = 0
        self.dut.s_axil.awprot.value = 0
        self.dut.s_axil.awuser.value = 0
        self.dut.s_axil.awvalid.value = 0
        self.dut.s_axil.wdata.value = 0
        self.dut.s_axil.wstrb.value = 0
        self.dut.s_axil.wuser.value = 0
        self.dut.s_axil.wvalid.value = 0
        self.dut.s_axil.bready.value = 0
        self.dut.s_axil.araddr.value = 0
        self.dut.s_axil.arprot.value = 0
        self.dut.s_axil.aruser.value = 0
        self.dut.s_axil.arvalid.value = 0
        self.dut.s_axil.rready.value = 0

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


@cocotb.test()
async def test_001_initial_contents(dut):
    tb = TB(dut)
    await tb.reset()

    init_file = initialization_file()

    if init_file:
        with open(init_file, encoding="ascii") as source:
            words = [int(line, 16) for line in source if line.strip()]

        expected = b"".join(word.to_bytes(4, "little") for word in words)
        response = await tb.axil_master.read(0, len(expected))
        assert_okay(response)
        assert response.data == expected

        # The initialization file is intentionally shorter than the RAM.
        tail = await tb.axil_master.read(len(expected), 4 * tb.byte_lanes)
        assert_okay(tail)
        assert tail.data == bytes(4 * tb.byte_lanes)
    else:
        response = await tb.axil_master.read(0, 8 * tb.byte_lanes)
        assert_okay(response)
        assert response.data == bytes(8 * tb.byte_lanes)


@cocotb.test()
async def test_002_unaligned_and_partial_writes(dut):
    tb = TB(dut)
    await tb.reset()

    byte_lanes = tb.byte_lanes
    base = tb.aperture // 2

    for length in range(1, byte_lanes * 2):
        for offset in range(byte_lanes):
            address = base + offset
            test_data = bytes(
                (0x31 + length + offset + index) & 0xff
                for index in range(length)
            )

            guard = await tb.axil_master.write(address - 1, b"\xaa" * (length + 2))
            assert_okay(guard)

            write = await tb.axil_master.write(address, test_data)
            assert_okay(write)

            read = await tb.axil_master.read(address - 1, length + 2)
            assert_okay(read)
            assert read.data == b"\xaa" + test_data + b"\xaa"


@cocotb.test()
async def test_003_address_boundaries_and_upper_bits(dut):
    tb = TB(dut)
    await tb.reset()

    byte_lanes = tb.byte_lanes
    boundary_data = bytes((0x80 + index) & 0xff for index in range(2 * byte_lanes))
    boundary_address = tb.aperture - len(boundary_data)

    write = await tb.axil_master.write(boundary_address, boundary_data)
    assert_okay(write)
    read = await tb.axil_master.read(boundary_address, len(boundary_data))
    assert_okay(read)
    assert read.data == boundary_data

    # The RAM consumes the low ADDR_W aperture bits. A crossbar may therefore
    # pass a full system address without first subtracting the target base.
    local_address = 3 * byte_lanes
    upper_address = (1 << (parameter_int("ADDR_W") + 2)) | local_address
    alias_data = bytes((0xd0 + index) & 0xff for index in range(byte_lanes))

    write = await tb.axil_master.write(upper_address, alias_data)
    assert_okay(write)
    read = await tb.axil_master.read(local_address, len(alias_data))
    assert_okay(read)
    assert read.data == alias_data


@cocotb.test()
async def test_004_reset_preserves_memory(dut):
    tb = TB(dut)
    await tb.reset()

    address = tb.aperture - 4 * tb.byte_lanes
    test_data = bytes((0x55 ^ index) & 0xff for index in range(2 * tb.byte_lanes))

    write = await tb.axil_master.write(address, test_data)
    assert_okay(write)

    await tb.reset()

    assert int(tb.dut.s_axil.bvalid.value) == 0
    assert int(tb.dut.s_axil.rvalid.value) == 0

    read = await tb.axil_master.read(address, len(test_data))
    assert_okay(read)
    assert read.data == test_data


@cocotb.test()
async def test_005_concurrent_read_and_write_channels(dut):
    tb = TB(dut)
    await tb.reset()
    tb.set_stress_pause_generators()

    byte_lanes = tb.byte_lanes
    stable_address = tb.aperture // 4
    stable_data = bytes((0x20 + index) & 0xff for index in range(8 * byte_lanes))
    writer_address = 5 * tb.aperture // 8
    writer_words = 12
    writer_data = bytes(
        (0xa0 + index) & 0xff for index in range(writer_words * byte_lanes)
    )

    response = await tb.axil_master.write(stable_address, stable_data)
    assert_okay(response)

    async def writer():
        for index in range(writer_words):
            start = index * byte_lanes
            response = await tb.axil_master.write(
                writer_address + start,
                writer_data[start:start + byte_lanes],
            )
            assert_okay(response)

    async def reader():
        for _ in range(writer_words * 2):
            response = await tb.axil_master.read(stable_address, len(stable_data))
            assert_okay(response)
            assert response.data == stable_data

    writer_task = cocotb.start_soon(writer())
    reader_task = cocotb.start_soon(reader())
    await writer_task
    await reader_task

    response = await tb.axil_master.read(writer_address, len(writer_data))
    assert_okay(response)
    assert response.data == writer_data


@cocotb.test()
async def test_006_randomized_access_with_backpressure(dut):
    tb = TB(dut)
    await tb.reset()
    tb.set_random_pause_generators()

    rng = random.Random(0x0E10C)
    region_address = tb.aperture // 4
    region_size = tb.aperture // 4
    model = bytearray([0x5a] * region_size)

    response = await tb.axil_master.write(region_address, model)
    assert_okay(response)

    for operation in range(64):
        length = rng.randint(1, min(3 * tb.byte_lanes + 1, region_size))
        offset = rng.randint(0, region_size - length)
        test_data = bytes(rng.randrange(256) for _ in range(length))

        response = await tb.axil_master.write(region_address + offset, test_data)
        assert_okay(response)
        model[offset:offset + length] = test_data

        if operation % 3 == 0:
            read_offset = rng.randint(0, region_size - length)
            response = await tb.axil_master.read(region_address + read_offset, length)
            assert_okay(response)
            assert response.data == model[read_offset:read_offset + length]

    response = await tb.axil_master.read(region_address, region_size)
    assert_okay(response)
    assert response.data == model


async def manual_read_words(tb, addresses):
    dut = tb.dut
    responses = []
    request_index = 0

    dut.s_axil.rready.value = 1

    while len(responses) < len(addresses):
        await FallingEdge(dut.clk)

        if request_index < len(addresses):
            dut.s_axil.arvalid.value = 1
            dut.s_axil.araddr.value = addresses[request_index]
        else:
            dut.s_axil.arvalid.value = 0

        await Timer(1, unit="ns")

        ar_fire = (
            int(dut.s_axil.arvalid.value) and
            int(dut.s_axil.arready.value)
        )
        if int(dut.s_axil.rvalid.value):
            assert int(dut.s_axil.rresp.value) == 0
            responses.append(int(dut.s_axil.rdata.value))

        if request_index < len(addresses):
            assert int(dut.s_axil.arready.value) == 1, (
                "ARREADY inserted a bubble with no read-response backpressure"
            )

        await RisingEdge(dut.clk)
        await ReadOnly()

        if ar_fire:
            request_index += 1

    await FallingEdge(dut.clk)
    dut.s_axil.arvalid.value = 0
    dut.s_axil.rready.value = 0
    return responses


@cocotb.test()
async def test_007_bubble_free_read_and_write_throughput(dut):
    tb = TB(dut, create_master=False)
    await tb.reset()

    word_count = 24
    byte_lanes = tb.byte_lanes
    data_mask = (1 << parameter_int("DATA_W")) - 1
    base_address = tb.aperture // 2
    addresses = [base_address + index * byte_lanes for index in range(word_count)]
    values = [
        (0x31_4159_26 ^ (index * 0x0101_0101)) & data_mask
        for index in range(word_count)
    ]

    dut.s_axil.bready.value = 1
    response_count = 0

    for address, value in zip(addresses, values):
        await FallingEdge(dut.clk)
        dut.s_axil.awaddr.value = address
        dut.s_axil.awvalid.value = 1
        dut.s_axil.wdata.value = value
        dut.s_axil.wstrb.value = (1 << byte_lanes) - 1
        dut.s_axil.wvalid.value = 1
        await Timer(1, unit="ns")

        assert int(dut.s_axil.awready.value) == 1, (
            "AWREADY inserted a bubble with no write-response backpressure"
        )
        assert int(dut.s_axil.wready.value) == 1, (
            "WREADY inserted a bubble with no write-response backpressure"
        )
        if int(dut.s_axil.bvalid.value):
            assert int(dut.s_axil.bresp.value) == 0
            response_count += 1

        await RisingEdge(dut.clk)
        await ReadOnly()
        assert int(dut.s_axil.bvalid.value) == 1

    await FallingEdge(dut.clk)
    dut.s_axil.awvalid.value = 0
    dut.s_axil.wvalid.value = 0
    await Timer(1, unit="ns")
    if int(dut.s_axil.bvalid.value):
        response_count += 1
    await RisingEdge(dut.clk)
    await ReadOnly()
    assert response_count == word_count
    assert int(dut.s_axil.bvalid.value) == 0

    await FallingEdge(dut.clk)
    dut.s_axil.bready.value = 0

    responses = await manual_read_words(tb, addresses)
    assert responses == values


@cocotb.test()
async def test_008_independent_write_buffers_and_response_holding(dut):
    tb = TB(dut, create_master=False)
    await tb.reset()

    byte_lanes = tb.byte_lanes
    data_mask = (1 << parameter_int("DATA_W")) - 1
    strobe = (1 << byte_lanes) - 1
    first_address = tb.aperture // 4
    second_address = first_address + byte_lanes
    first_data = 0xA5A5_5A5A & data_mask
    second_data = 0xC33C_0FF0 & data_mask

    # Capture AW first, then W several cycles later.
    await FallingEdge(dut.clk)
    dut.s_axil.awaddr.value = first_address
    dut.s_axil.awvalid.value = 1
    await Timer(1, unit="ns")
    assert int(dut.s_axil.awready.value) == 1
    assert int(dut.s_axil.wready.value) == 1
    await RisingEdge(dut.clk)
    await ReadOnly()

    await FallingEdge(dut.clk)
    dut.s_axil.awvalid.value = 0
    dut.s_axil.wdata.value = first_data
    dut.s_axil.wstrb.value = strobe
    dut.s_axil.wvalid.value = 1
    await Timer(1, unit="ns")
    assert int(dut.s_axil.wready.value) == 1
    await RisingEdge(dut.clk)
    await ReadOnly()
    assert int(dut.s_axil.bvalid.value) == 1

    # BVALID must remain asserted, and one additional AW/W pair may buffer.
    await FallingEdge(dut.clk)
    dut.s_axil.wvalid.value = 0
    dut.s_axil.awaddr.value = second_address
    dut.s_axil.awvalid.value = 1
    dut.s_axil.wdata.value = second_data
    dut.s_axil.wstrb.value = strobe
    dut.s_axil.wvalid.value = 1
    await Timer(1, unit="ns")
    assert int(dut.s_axil.awready.value) == 1
    assert int(dut.s_axil.wready.value) == 1
    await RisingEdge(dut.clk)
    await ReadOnly()

    await FallingEdge(dut.clk)
    dut.s_axil.awvalid.value = 0
    dut.s_axil.wvalid.value = 0
    held_response = (
        int(dut.s_axil.bvalid.value),
        int(dut.s_axil.bresp.value),
    )
    assert held_response == (1, 0)

    for _ in range(4):
        await RisingEdge(dut.clk)
        await ReadOnly()
        assert (
            int(dut.s_axil.bvalid.value),
            int(dut.s_axil.bresp.value),
        ) == held_response
        assert int(dut.s_axil.awready.value) == 0
        assert int(dut.s_axil.wready.value) == 0

    # Consuming response 0 simultaneously commits buffered write 1.
    await FallingEdge(dut.clk)
    dut.s_axil.bready.value = 1
    await RisingEdge(dut.clk)
    await ReadOnly()
    assert int(dut.s_axil.bvalid.value) == 1

    await RisingEdge(dut.clk)
    await ReadOnly()
    assert int(dut.s_axil.bvalid.value) == 0

    await FallingEdge(dut.clk)
    dut.s_axil.bready.value = 0
    responses = await manual_read_words(tb, [first_address, second_address])
    assert responses == [first_data, second_data]


@cocotb.test()
async def test_009_read_response_holding_and_payload_stability(dut):
    tb = TB(dut, create_master=False)
    await tb.reset()

    address = 0
    dut.s_axil.rready.value = 0

    await FallingEdge(dut.clk)
    dut.s_axil.araddr.value = address
    dut.s_axil.arvalid.value = 1
    await Timer(1, unit="ns")
    assert int(dut.s_axil.arready.value) == 1
    await RisingEdge(dut.clk)
    await ReadOnly()

    await FallingEdge(dut.clk)
    dut.s_axil.arvalid.value = 0

    for _ in range(4):
        await Timer(1, unit="ns")
        if int(dut.s_axil.rvalid.value):
            break
        await RisingEdge(dut.clk)
        await ReadOnly()
        await FallingEdge(dut.clk)
    else:
        raise AssertionError("Read response did not reach the AXI output")

    held_payload = (
        int(dut.s_axil.rdata.value),
        int(dut.s_axil.rresp.value),
        int(dut.s_axil.ruser.value),
    )

    for _ in range(5):
        await RisingEdge(dut.clk)
        await ReadOnly()
        assert int(dut.s_axil.rvalid.value) == 1
        assert (
            int(dut.s_axil.rdata.value),
            int(dut.s_axil.rresp.value),
            int(dut.s_axil.ruser.value),
        ) == held_payload

    await FallingEdge(dut.clk)
    dut.s_axil.rready.value = 1
    await RisingEdge(dut.clk)
    await ReadOnly()
    assert int(dut.s_axil.rvalid.value) == 0


# Pytest simulation runner

tests_dir = os.path.abspath(os.path.dirname(__file__))
repo_dir = os.path.abspath(os.path.join(tests_dir, "..", "..", ".."))
hw_dir = os.path.join(repo_dir, "hw")
libs_dir = os.path.join(repo_dir, "libs")
core_dir = os.path.join(hw_dir, "rtl", "core")
taxi_axi_dir = os.path.join(libs_dir, "taxi", "src", "axi", "rtl")
common_dir = os.path.abspath(os.path.join(tests_dir, "..", "..", "common"))


CONFIGURATIONS = [
    (data_w, pipeline_output, False)
    for data_w in (8, 16, 32, 64)
    for pipeline_output in (0, 1)
] + [
    (32, pipeline_output, True)
    for pipeline_output in (0, 1)
]


@pytest.mark.parametrize(
    "data_w,pipeline_output,use_init_file",
    CONFIGURATIONS,
    ids=[
        f"data{data_w}-pipe{pipeline_output}-init{int(use_init_file)}"
        for data_w, pipeline_output, use_init_file in CONFIGURATIONS
    ],
)
def test_openenoc_axil_ram(request, data_w, pipeline_output, use_init_file):
    dut = "openenoc_axil_ram"
    module = os.path.splitext(os.path.basename(__file__))[0]
    toplevel = module

    verilog_sources = [
        os.path.join(taxi_axi_dir, "taxi_axil_if.sv"),
        os.path.join(core_dir, f"{dut}.sv"),
        os.path.join(tests_dir, f"{toplevel}.sv"),
    ]

    init_file = os.path.join(tests_dir, "imem.mem") if use_init_file else ""

    parameters = {
        "DATA_W": data_w,
        "ADDR_W": 10,
        "AXIL_ADDR_W": 32,
        "STRB_W": data_w // 8,
        "PIPELINE_OUTPUT": pipeline_output,
        "INIT_FILE": f'"{init_file}"',
    }

    extra_env = {
        f"PARAM_{key}": str(value).strip('"')
        for key, value in parameters.items()
    }

    sim_build = os.path.join(
        tests_dir,
        "sim_build",
        request.node.name.replace("[", "-").replace("]", ""),
    )

    cocotb_test.simulator.run(
        simulator="verilator",
        python_search=[tests_dir],
        verilog_sources=verilog_sources,
        toplevel=toplevel,
        module=module,
        parameters=parameters,
        extra_args=[os.path.join(common_dir, "config.vlt")],
        sim_build=sim_build,
        extra_env=extra_env,
    )
