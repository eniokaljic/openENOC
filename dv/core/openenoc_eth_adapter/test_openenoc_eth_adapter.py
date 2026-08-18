# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: CERN-OHL-S-2.0

import itertools
import logging
import os
import random

import cocotb_test.simulator
import pytest

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge
from cocotb.regression import TestFactory
TestFactory.__test__ = False

from cocotbext.axi import AxiStreamBus, AxiStreamFrame, AxiStreamSource, AxiStreamSink

class TB(object):
    def __init__(self, dut):
        self.dut = dut

        self.log = logging.getLogger("cocotb.tb")
        self.log.setLevel(logging.DEBUG)

        clk_a_period = int(os.getenv("CLK_A_PERIOD", "10"))
        clk_b_period = int(os.getenv("CLK_B_PERIOD", "40"))

        cocotb.start_soon(Clock(dut.clk_a, clk_a_period, units="ns").start())
        cocotb.start_soon(Clock(dut.clk_b, clk_b_period, units="ns").start())

        # A -> B direction:
        #   A drives eth_a.a2b
        #   B receives eth_b.a2b
        self.source_a2b = AxiStreamSource(
            AxiStreamBus.from_entity(dut.eth_a.a2b),
            dut.clk_a,
            dut.rst_a
        )

        self.sink_a2b = AxiStreamSink(
            AxiStreamBus.from_entity(dut.eth_b.a2b),
            dut.clk_b,
            dut.rst_b
        )

        # B -> A direction:
        #   B drives eth_b.b2a
        #   A receives eth_a.b2a
        self.source_b2a = AxiStreamSource(
            AxiStreamBus.from_entity(dut.eth_b.b2a),
            dut.clk_b,
            dut.rst_b
        )

        self.sink_b2a = AxiStreamSink(
            AxiStreamBus.from_entity(dut.eth_a.b2a),
            dut.clk_a,
            dut.rst_a
        )

    def set_idle_generator_a2b(self, generator=None):
        if generator:
            self.source_a2b.set_pause_generator(generator())

    def set_backpressure_generator_a2b(self, generator=None):
        if generator:
            self.sink_a2b.set_pause_generator(generator())

    def set_idle_generator_b2a(self, generator=None):
        if generator:
            self.source_b2a.set_pause_generator(generator())

    def set_backpressure_generator_b2a(self, generator=None):
        if generator:
            self.sink_b2a.set_pause_generator(generator())

    async def reset(self):
        self.dut.rst_a.setimmediatevalue(0)
        self.dut.rst_b.setimmediatevalue(0)

        for _ in range(10):
            await RisingEdge(self.dut.clk_a)

        self.dut.rst_a.value = 1
        self.dut.rst_b.value = 1

        for _ in range(10):
            await RisingEdge(self.dut.clk_a)

        self.dut.rst_a.value = 0
        self.dut.rst_b.value = 0

        for _ in range(10):
            await RisingEdge(self.dut.clk_a)

    async def reset_a(self):
        self.dut.rst_a.setimmediatevalue(0)

        for _ in range(10):
            await RisingEdge(self.dut.clk_a)

        self.dut.rst_a.value = 1

        for _ in range(10):
            await RisingEdge(self.dut.clk_a)

        self.dut.rst_a.value = 0

        for _ in range(10):
            await RisingEdge(self.dut.clk_a)

    async def reset_b(self):
        self.dut.rst_b.setimmediatevalue(0)

        for _ in range(10):
            await RisingEdge(self.dut.clk_b)

        self.dut.rst_b.value = 1

        for _ in range(10):
            await RisingEdge(self.dut.clk_b)

        self.dut.rst_b.value = 0

        for _ in range(10):
            await RisingEdge(self.dut.clk_b)

# Common single-direction transfer test helper.
# Sends a sequence of AXI4-Stream frames through one selected source/sink path
# and checks that payload, TID, TDEST, and TUSER are preserved.
async def run_direction_test(
        dut,
        source,
        sink,
        payload_lengths=None,
        payload_data=None,
        idle_inserter=None,
        backpressure_inserter=None):

    if idle_inserter:
        source.set_pause_generator(idle_inserter())

    if backpressure_inserter:
        sink.set_pause_generator(backpressure_inserter())

    id_count = 2**len(source.bus.tid) if hasattr(source.bus, "tid") else 1
    cur_id = 1

    test_frames = []

    for test_data in [payload_data(x) for x in payload_lengths()]:
        test_frame = AxiStreamFrame(test_data)

        if hasattr(source.bus, "tid"):
            test_frame.tid = cur_id

        if hasattr(source.bus, "tdest"):
            test_frame.tdest = cur_id

        test_frames.append(test_frame)
        await source.send(test_frame)

        cur_id = (cur_id + 1) % id_count

    for test_frame in test_frames:
        rx_frame = await sink.recv()

        assert rx_frame.tdata == test_frame.tdata

        if hasattr(source.bus, "tid") and hasattr(sink.bus, "tid"):
            assert rx_frame.tid == test_frame.tid

        if hasattr(source.bus, "tdest") and hasattr(sink.bus, "tdest"):
            assert rx_frame.tdest == test_frame.tdest

        assert not rx_frame.tuser

    assert sink.empty()

# A-to-B unidirectional data path test.
# Verifies that frames transmitted on eth_a.a2b are received correctly on
# eth_b.a2b, with optional source idle insertion and sink backpressure.
async def run_test_a2b(
        dut,
        payload_lengths=None,
        payload_data=None,
        idle_inserter=None,
        backpressure_inserter=None):

    tb = TB(dut)

    await tb.reset()

    await run_direction_test(
        dut,
        tb.source_a2b,
        tb.sink_a2b,
        payload_lengths=payload_lengths,
        payload_data=payload_data,
        idle_inserter=idle_inserter,
        backpressure_inserter=backpressure_inserter
    )

    await RisingEdge(dut.clk_a)
    await RisingEdge(dut.clk_a)

# B-to-A unidirectional data path test.
# Verifies that frames transmitted on eth_b.b2a are received correctly on
# eth_a.b2a, with optional source idle insertion and sink backpressure.
async def run_test_b2a(
        dut,
        payload_lengths=None,
        payload_data=None,
        idle_inserter=None,
        backpressure_inserter=None):

    tb = TB(dut)

    await tb.reset()

    await run_direction_test(
        dut,
        tb.source_b2a,
        tb.sink_b2a,
        payload_lengths=payload_lengths,
        payload_data=payload_data,
        idle_inserter=idle_inserter,
        backpressure_inserter=backpressure_inserter
    )

    await RisingEdge(dut.clk_b)
    await RisingEdge(dut.clk_b)

# Bidirectional transfer test.
# Sends frames in both directions through the adapter and verifies that the two
# independent AXI4-Stream paths operate correctly at the same time.
async def run_test_bidirectional(
        dut,
        payload_lengths=None,
        payload_data=None,
        idle_inserter=None,
        backpressure_inserter=None):

    tb = TB(dut)

    await tb.reset()

    tb.set_idle_generator_a2b(idle_inserter)
    tb.set_backpressure_generator_a2b(backpressure_inserter)
    tb.set_idle_generator_b2a(idle_inserter)
    tb.set_backpressure_generator_b2a(backpressure_inserter)

    id_count_a2b = 2**len(tb.source_a2b.bus.tid) if hasattr(tb.source_a2b.bus, "tid") else 1
    id_count_b2a = 2**len(tb.source_b2a.bus.tid) if hasattr(tb.source_b2a.bus, "tid") else 1

    cur_id_a2b = 1
    cur_id_b2a = 1

    test_frames_a2b = []
    test_frames_b2a = []

    for length in payload_lengths():
        test_data_a2b = payload_data(length)
        test_frame_a2b = AxiStreamFrame(test_data_a2b)

        if hasattr(tb.source_a2b.bus, "tid"):
            test_frame_a2b.tid = cur_id_a2b

        if hasattr(tb.source_a2b.bus, "tdest"):
            test_frame_a2b.tdest = cur_id_a2b

        test_frames_a2b.append(test_frame_a2b)
        await tb.source_a2b.send(test_frame_a2b)

        cur_id_a2b = (cur_id_a2b + 1) % id_count_a2b

        test_data_b2a = payload_data(length)
        test_frame_b2a = AxiStreamFrame(test_data_b2a)

        if hasattr(tb.source_b2a.bus, "tid"):
            test_frame_b2a.tid = cur_id_b2a

        if hasattr(tb.source_b2a.bus, "tdest"):
            test_frame_b2a.tdest = cur_id_b2a

        test_frames_b2a.append(test_frame_b2a)
        await tb.source_b2a.send(test_frame_b2a)

        cur_id_b2a = (cur_id_b2a + 1) % id_count_b2a

    for test_frame in test_frames_a2b:
        rx_frame = await tb.sink_a2b.recv()

        assert rx_frame.tdata == test_frame.tdata

        if hasattr(tb.source_a2b.bus, "tid") and hasattr(tb.sink_a2b.bus, "tid"):
            assert rx_frame.tid == test_frame.tid

        if hasattr(tb.source_a2b.bus, "tdest") and hasattr(tb.sink_a2b.bus, "tdest"):
            assert rx_frame.tdest == test_frame.tdest

        assert not rx_frame.tuser

    for test_frame in test_frames_b2a:
        rx_frame = await tb.sink_b2a.recv()

        assert rx_frame.tdata == test_frame.tdata

        if hasattr(tb.source_b2a.bus, "tid") and hasattr(tb.sink_b2a.bus, "tid"):
            assert rx_frame.tid == test_frame.tid

        if hasattr(tb.source_b2a.bus, "tdest") and hasattr(tb.sink_b2a.bus, "tdest"):
            assert rx_frame.tdest == test_frame.tdest

        assert not rx_frame.tuser

    assert tb.sink_a2b.empty()
    assert tb.sink_b2a.empty()

    await RisingEdge(dut.clk_a)
    await RisingEdge(dut.clk_b)

# Initial sink backpressure test for the A-to-B path.
# Holds the B-side sink paused before sending a frame, then releases it and
# checks that the buffered frame is delivered without corruption.
async def run_test_init_sink_pause_a2b(dut):

    tb = TB(dut)

    await tb.reset()

    tb.sink_a2b.pause = True

    test_data = bytearray(itertools.islice(itertools.cycle(range(256)), 32))
    test_frame = AxiStreamFrame(test_data)

    await tb.source_a2b.send(test_frame)

    for _ in range(64):
        await RisingEdge(dut.clk_a)

    tb.sink_a2b.pause = False

    rx_frame = await tb.sink_a2b.recv()

    assert rx_frame.tdata == test_data
    assert not rx_frame.tuser

    assert tb.sink_a2b.empty()

    await RisingEdge(dut.clk_a)
    await RisingEdge(dut.clk_a)

# Initial sink backpressure test for the B-to-A path.
# Holds the A-side sink paused before sending a frame, then releases it and
# checks that the buffered frame is delivered without corruption.
async def run_test_init_sink_pause_b2a(dut):

    tb = TB(dut)

    await tb.reset()

    tb.sink_b2a.pause = True

    test_data = bytearray(itertools.islice(itertools.cycle(range(256)), 32))
    test_frame = AxiStreamFrame(test_data)

    await tb.source_b2a.send(test_frame)

    for _ in range(64):
        await RisingEdge(dut.clk_b)

    tb.sink_b2a.pause = False

    rx_frame = await tb.sink_b2a.recv()

    assert rx_frame.tdata == test_data
    assert not rx_frame.tuser

    assert tb.sink_b2a.empty()

    await RisingEdge(dut.clk_b)
    await RisingEdge(dut.clk_b)

# Bidirectional stress test with mixed frame sizes.
# Sends multiple random-size frames and one jumbo frame in both
# directions to exercise CDC, width adaptation, buffering, and backpressure.
async def run_stress_test_bidirectional(
        dut,
        idle_inserter=None,
        backpressure_inserter=None):

    tb = TB(dut)

    id_count_a2b = 2**len(tb.source_a2b.bus.tid) if hasattr(tb.source_a2b.bus, "tid") else 1
    id_count_b2a = 2**len(tb.source_b2a.bus.tid) if hasattr(tb.source_b2a.bus, "tid") else 1

    cur_id_a2b = 1
    cur_id_b2a = 1

    await tb.reset()

    tb.set_idle_generator_a2b(idle_inserter)
    tb.set_backpressure_generator_a2b(backpressure_inserter)
    tb.set_idle_generator_b2a(idle_inserter)
    tb.set_backpressure_generator_b2a(backpressure_inserter)

    test_frames_a2b = []
    test_frames_b2a = []

    payload_lengths = [random.randint(20, 256) for _ in range(15)] + [9000]

    for length in payload_lengths:
        test_data_a2b = bytearray(itertools.islice(itertools.cycle(range(256)), length))
        test_frame_a2b = AxiStreamFrame(test_data_a2b)

        if hasattr(tb.source_a2b.bus, "tid"):
            test_frame_a2b.tid = cur_id_a2b

        if hasattr(tb.source_a2b.bus, "tdest"):
            test_frame_a2b.tdest = cur_id_a2b

        test_frames_a2b.append(test_frame_a2b)
        await tb.source_a2b.send(test_frame_a2b)

        cur_id_a2b = (cur_id_a2b + 1) % id_count_a2b

        test_data_b2a = bytearray(itertools.islice(itertools.cycle(range(256)), length))
        test_frame_b2a = AxiStreamFrame(test_data_b2a)

        if hasattr(tb.source_b2a.bus, "tid"):
            test_frame_b2a.tid = cur_id_b2a

        if hasattr(tb.source_b2a.bus, "tdest"):
            test_frame_b2a.tdest = cur_id_b2a

        test_frames_b2a.append(test_frame_b2a)
        await tb.source_b2a.send(test_frame_b2a)

        cur_id_b2a = (cur_id_b2a + 1) % id_count_b2a

    for test_frame in test_frames_a2b:
        rx_frame = await tb.sink_a2b.recv()

        assert rx_frame.tdata == test_frame.tdata

        if hasattr(tb.source_a2b.bus, "tid") and hasattr(tb.sink_a2b.bus, "tid"):
            assert rx_frame.tid == test_frame.tid

        if hasattr(tb.source_a2b.bus, "tdest") and hasattr(tb.sink_a2b.bus, "tdest"):
            assert rx_frame.tdest == test_frame.tdest

        assert not rx_frame.tuser

    for test_frame in test_frames_b2a:
        rx_frame = await tb.sink_b2a.recv()

        assert rx_frame.tdata == test_frame.tdata

        if hasattr(tb.source_b2a.bus, "tid") and hasattr(tb.sink_b2a.bus, "tid"):
            assert rx_frame.tid == test_frame.tid

        if hasattr(tb.source_b2a.bus, "tdest") and hasattr(tb.sink_b2a.bus, "tdest"):
            assert rx_frame.tdest == test_frame.tdest

        assert not rx_frame.tuser

    assert tb.sink_a2b.empty()
    assert tb.sink_b2a.empty()

    await RisingEdge(dut.clk_a)
    await RisingEdge(dut.clk_b)

def max_byte_lanes():
    data_width = max(
        len(cocotb.top.eth_a.a2b.tdata),
        len(cocotb.top.eth_b.a2b.tdata),
        len(cocotb.top.eth_b.b2a.tdata),
        len(cocotb.top.eth_a.b2a.tdata)
    )

    return data_width // 8

# Pause generator used to insert deterministic idle cycles or backpressure
# into cocotbext-axi source and sink drivers.
def cycle_pause():
    byte_lanes = max_byte_lanes()

    if byte_lanes >= 64:
        # 512-bit and wider: lighter pause pattern to reduce runtime
        return itertools.cycle([1, 0, 0, 0])

    if byte_lanes >= 32:
        return itertools.cycle([1, 0, 0])

    return itertools.cycle([1, 1, 1, 0])

# Generates a fixed set of 16 frame lengths used by directed transfer tests.
# The list is independent of the AXI4-Stream data width and covers the minimum
# Ethernet payload size used in this testbench, boundary lengths around common
# power-of-two sizes, and the maximum directed-test frame length of 512 bytes.
def size_list():
    return [20, 21, 31, 32, 33, 63, 64, 65, 127, 128, 129, 255, 256, 257, 511, 512]

# Generates an incrementing byte pattern of the requested length.
# This makes payload mismatches easy to detect and debug.
def incrementing_payload(length):
    return bytearray(itertools.islice(itertools.cycle(range(256)), length))

if getattr(cocotb, 'top', None) is not None:

    factory = TestFactory(run_test_a2b)
    factory.add_option("payload_lengths", [size_list])
    factory.add_option("payload_data", [incrementing_payload])
    factory.add_option("idle_inserter", [None, cycle_pause])
    factory.add_option("backpressure_inserter", [None, cycle_pause])
    factory.generate_tests()

    factory = TestFactory(run_test_b2a)
    factory.add_option("payload_lengths", [size_list])
    factory.add_option("payload_data", [incrementing_payload])
    factory.add_option("idle_inserter", [None, cycle_pause])
    factory.add_option("backpressure_inserter", [None, cycle_pause])
    factory.generate_tests()

    factory = TestFactory(run_test_bidirectional)
    factory.add_option("payload_lengths", [size_list])
    factory.add_option("payload_data", [incrementing_payload])
    factory.add_option("idle_inserter", [None, cycle_pause])
    factory.add_option("backpressure_inserter", [None, cycle_pause])
    factory.generate_tests()

    for test in [
        run_test_init_sink_pause_a2b,
        run_test_init_sink_pause_b2a,
    ]:
        factory = TestFactory(test)
        factory.generate_tests()

    factory = TestFactory(run_stress_test_bidirectional)
    factory.add_option("idle_inserter", [cycle_pause])
    factory.add_option("backpressure_inserter", [cycle_pause])
    factory.generate_tests()

# ----------------------------------------------------------------------
# PyTest framework: test parameterization and test runner
# ----------------------------------------------------------------------

tests_dir = os.path.dirname(__file__)
repo_dir = os.path.abspath(os.path.join(tests_dir, '..', '..', '..'))
hw_dir = os.path.join(repo_dir, 'hw')
libs_dir = os.path.join(repo_dir, 'libs')
core_dir = os.path.join(hw_dir, 'rtl', 'core')
taxi_axis_dir = os.path.join(libs_dir, 'taxi', 'src', 'axis', 'rtl')
taxi_sync_dir = os.path.join(libs_dir, 'taxi', 'src', 'sync', 'rtl')

def process_f_files(files):
    lst = {}

    for f in files:
        if f[-2:].lower() == '.f':
            with open(f, 'r') as fp:
                l = fp.read().split()

            for f in process_f_files([os.path.join(os.path.dirname(f), x) for x in l]):
                lst[os.path.basename(f)] = f
        else:
            lst[os.path.basename(f)] = f

    return list(lst.values())

@pytest.mark.parametrize(
    ("a_data_w", "b_data_w"),
    itertools.combinations([8, 16, 32, 64, 128, 256, 512], 2)
)
def test_openenoc_eth_adapter(request, a_data_w, b_data_w):
    dut = "openenoc_eth_adapter"
    module = os.path.splitext(os.path.basename(__file__))[0]
    toplevel = module

    verilog_sources = [
        os.path.join(taxi_axis_dir, "taxi_axis_if.sv"),
        os.path.join(taxi_axis_dir, "taxi_axis_async_fifo_adapter.sv"),
        os.path.join(taxi_axis_dir, "taxi_axis_async_fifo.sv"),
        os.path.join(taxi_axis_dir, "taxi_axis_adapter.sv"),
        os.path.join(taxi_sync_dir, "taxi_sync_reset.sv"),
        os.path.join(taxi_sync_dir, "taxi_sync_signal.sv"),
        os.path.join(core_dir, "openenoc_eth_if.sv"),
        os.path.join(core_dir, f"{dut}.sv"),
        os.path.join(tests_dir, f"{toplevel}.sv"),
    ]

    verilog_sources = process_f_files(verilog_sources)

    parameters = {}

    parameters['A_DATA_W'] = a_data_w
    parameters['A_KEEP_EN'] = int(parameters['A_DATA_W'] > 8)
    parameters['A_KEEP_W'] = (parameters['A_DATA_W'] + 7) // 8
    parameters['A_STRB_EN'] = 0
    parameters['A_LAST_EN'] = 1
    parameters['A_ID_EN'] = 1
    parameters['A_ID_W'] = 8
    parameters['A_DEST_EN'] = 1
    parameters['A_DEST_W'] = 8
    parameters['A_USER_EN'] = 1
    parameters['A_USER_W'] = 1

    parameters['B_DATA_W'] = b_data_w
    parameters['B_KEEP_EN'] = int(parameters['B_DATA_W'] > 8)
    parameters['B_KEEP_W'] = (parameters['B_DATA_W'] + 7) // 8
    parameters['B_STRB_EN'] = 0
    parameters['B_LAST_EN'] = 1
    parameters['B_ID_EN'] = 1
    parameters['B_ID_W'] = 8
    parameters['B_DEST_EN'] = 1
    parameters['B_DEST_W'] = 8
    parameters['B_USER_EN'] = 1
    parameters['B_USER_W'] = 1

    parameters['DEPTH'] = 2 * max(parameters['A_KEEP_W'], parameters['B_KEEP_W'])
    parameters['RAM_PIPELINE'] = 1
    parameters['OUTPUT_FIFO_EN'] = 0
    parameters['FRAME_FIFO'] = 0
    parameters['USER_BAD_FRAME_VALUE'] = 1
    parameters['USER_BAD_FRAME_MASK'] = 1
    parameters['DROP_OVERSIZE_FRAME'] = 0
    parameters['DROP_BAD_FRAME'] = 0
    parameters['DROP_WHEN_FULL'] = 0
    parameters['MARK_WHEN_FULL'] = 0
    parameters['FRAME_PAUSE'] = 1

    extra_env = {f'PARAM_{k}': str(v) for k, v in parameters.items()}

    sim_build = os.path.join(tests_dir, "sim_build",
        request.node.name.replace('[', '-').replace(']', ''))

    cocotb_test.simulator.run(
        simulator="verilator",
        python_search=[tests_dir],
        verilog_sources=verilog_sources,
        toplevel=toplevel,
        module=module,
        parameters=parameters,
        sim_build=sim_build,
        extra_env=extra_env,
    )
