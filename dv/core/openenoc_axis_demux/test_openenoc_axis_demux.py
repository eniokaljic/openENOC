# SPDX-FileCopyrightText: 2026 Kerim Bavcic
# SPDX-License-Identifier: AGPL-3.0-or-later

import itertools
import logging
import os

import cocotb
import cocotb_test.simulator
import pytest
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

        cocotb.start_soon(Clock(dut.clk, 10, units="ns").start())

        self.source = AxiStreamSource(AxiStreamBus.from_entity(dut.s_axis_if), dut.clk, dut.rst)
        self.sink = [AxiStreamSink(AxiStreamBus.from_entity(bus), dut.clk, dut.rst) for bus in dut.m_axis_if]

        dut.enable.setimmediatevalue(0)
        dut.drop.setimmediatevalue(0)
        dut.select.setimmediatevalue(0)

    def set_idle_generator(self, generator=None):
        if generator:
            self.source.set_pause_generator(generator())

    def set_backpressure_generator(self, generator=None):
        if generator:
            for sink in self.sink:
                sink.set_pause_generator(generator())

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

# ----------------------------------------------------------------------
# UNICAST (TDEST_ROUTE) test logic
# ----------------------------------------------------------------------

async def run_test(dut, payload_lengths=None, payload_data=None, idle_inserter=None, backpressure_inserter=None, port=0):
    tb = TB(dut)

    id_width = len(tb.sink[0].bus.tid)
    id_count = 2**id_width
    id_mask = id_count-1

    dest_width = len(tb.sink[0].bus.tdest)
    dest_count = 2**dest_width
    dest_mask = dest_count-1

    cur_id = 1

    await tb.reset()

    tb.set_idle_generator(idle_inserter)
    tb.set_backpressure_generator(backpressure_inserter)

    test_frames = []

    dut.enable.setimmediatevalue(1)
    dut.drop.setimmediatevalue(0)
    dut.select.setimmediatevalue(port)

    for test_data in [payload_data(x) for x in payload_lengths()]:
        test_frame = AxiStreamFrame(test_data)
        test_frame.tid = cur_id
        test_frame.tdest = cur_id | (port << dest_width)

        test_frames.append(test_frame)
        await tb.source.send(test_frame)

        cur_id = (cur_id + 1) % id_count

    for test_frame in test_frames:
        rx_frame = await tb.sink[port].recv()

        assert rx_frame.tdata == test_frame.tdata
        assert rx_frame.tid == test_frame.tid
        assert rx_frame.tdest == (test_frame.tdest & dest_mask)
        assert not rx_frame.tuser

    assert tb.sink[port].empty()

    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)

# ----------------------------------------------------------------------
# MULTICAST (TUSER_BITMAP_ROUTE) test logic
# ----------------------------------------------------------------------

async def run_test_multicast(dut, payload_lengths=None, payload_data=None, idle_inserter=None, backpressure_inserter=None, mask=1):
    tb = TB(dut)

    id_width = len(tb.sink[0].bus.tid)
    id_count = 2**id_width

    target_ports = [p for p in range(len(tb.sink)) if mask & (1 << p)]
    cur_id = 1

    await tb.reset()

    tb.set_idle_generator(idle_inserter)
    tb.set_backpressure_generator(backpressure_inserter)

    test_frames = []

    dut.enable.setimmediatevalue(1)
    dut.drop.setimmediatevalue(0)
    dut.select.setimmediatevalue(0)

    for test_data in [payload_data(x) for x in payload_lengths()]:
        test_frame = AxiStreamFrame(test_data)
        test_frame.tid = cur_id
        test_frame.tuser = mask

        test_frames.append(test_frame)
        await tb.source.send(test_frame)

        cur_id = (cur_id + 1) % id_count

    # each frame must arrive at EACH targeted port, with the same content
    for test_frame in test_frames:
        for port in target_ports:
            rx_frame = await tb.sink[port].recv()

            assert rx_frame.tdata == test_frame.tdata
            assert rx_frame.tid == test_frame.tid
            assert rx_frame.tuser == mask

    # not one port (including targeted ones, after drain) should have excess
    for port in range(len(tb.sink)):
        assert tb.sink[port].empty()

    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)

async def run_test_multicast_drop(dut):
    tb = TB(dut)

    await tb.reset()

    dut.enable.setimmediatevalue(1)
    dut.drop.setimmediatevalue(0)
    dut.select.setimmediatevalue(0)

    payload = incrementing_payload(4)
    test_frame = AxiStreamFrame(payload)
    test_frame.tid = 1
    test_frame.tuser = 0 # empty M_COUNT-bit mask -> drop, regardless of port count

    await tb.source.send(test_frame)

    for _ in range(10):
        await RisingEdge(dut.clk)

    for port in range(len(tb.sink)):
        assert tb.sink[port].empty()

    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)

async def run_test_multicast_all_or_nothing(dut, case=None):
    mask, hold_cycles = case  # case = (mask, {port: hold_cycles, ...})

    tb = TB(dut)

    await tb.reset()

    dut.enable.setimmediatevalue(1)
    dut.drop.setimmediatevalue(0)
    dut.select.setimmediatevalue(0)

    target_ports = [p for p in range(len(tb.sink)) if mask & (1 << p)]

    for port, cycles in hold_cycles.items():
        tb.sink[port].set_pause_generator(hold_then_release(cycles))

    payload = incrementing_payload(8)
    test_frame = AxiStreamFrame(payload)
    test_frame.tid = 1
    test_frame.tuser = mask

    await tb.source.send(test_frame)

    max_hold = max(hold_cycles.values())

    # until the moment when the slowest targeted port becomes ready, NONE of the targeted ports should receive anything
    for cycle in range(max_hold - 1):
        await RisingEdge(dut.clk)
        for port in target_ports:
            assert tb.sink[port].empty()

    # when the slowest targeted port becomes ready, ALL of the targeted ports should receive the frame
    for port in target_ports:
        rx_frame = await tb.sink[port].recv()
        assert rx_frame.tdata == test_frame.tdata
        assert rx_frame.tid == test_frame.tid

    for port in range(len(tb.sink)):
        if port not in target_ports:
            assert tb.sink[port].empty()

    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)

# ----------------------------------------------------------------------
# Helper functions for test parameterization
# ----------------------------------------------------------------------

def multicast_mask_list():
    ports = len(cocotb.top.m_axis_if)
    return list(range(1, (1 << ports), 2))

def cycle_pause():
    return itertools.cycle([1, 1, 1, 0])

def size_list():
    data_width = len(cocotb.top.s_axis_if.tdata)
    byte_width = data_width // 8
    return list(range(1, byte_width*4+1))+[512]+[1]*64

def incrementing_payload(length):
    return bytearray(itertools.islice(itertools.cycle(range(256)), length))

def hold_then_release(hold_cycles):
    return itertools.chain([1]*hold_cycles, itertools.repeat(0))

# returns the list of (mask, hold_cycles) tuples for all_or_nothing test cases
def all_or_nothing_cases(ports):
    ports = len(cocotb.top.m_axis_if)
    cases = []

    if ports < 2:
        return cases

    # first and last port, slower port 0
    cases.append(((1 << 0) | (1 << (ports - 1)), {0: 7, ports - 1: 5}))

    # same pair, reversed order of which is slower (to cover both variants)
    cases.append(((1 << 0) | (1 << (ports - 1)), {0: 5, ports - 1: 7}))

    if ports >= 4:
        # port 1 and 2, slower port 2
        cases.append(((1 << 1) | (1 << 2), {1: 5, 2: 7}))
        # port 0 and 2, slower port 0
        cases.append(((1 << 0) | (1 << 2), {0: 7, 2: 5}))

    # all ports, each with different hold cycles (stress variant)
    all_mask = (1 << ports) - 1
    cases.append((all_mask, {p: 5 + p for p in range(ports)}))

    return cases

# ----------------------------------------------------------------------
# Dispatch: select test cases to run based on Makefile configuration
# ----------------------------------------------------------------------

if getattr(cocotb, 'top', None) is not None:

    ports = len(cocotb.top.m_axis_if)

    if os.environ.get('PARAM_TUSER_BITMAP_ROUTE', '0') == '1':
        factory = TestFactory(run_test_multicast)
        factory.add_option("payload_lengths", [size_list])
        factory.add_option("payload_data", [incrementing_payload])
        factory.add_option("idle_inserter", [None, cycle_pause])
        factory.add_option("backpressure_inserter", [None, cycle_pause])
        factory.add_option("mask", multicast_mask_list())
        factory.generate_tests()

        factory_drop = TestFactory(run_test_multicast_drop)
        factory_drop.generate_tests()

        factory_atomic = TestFactory(run_test_multicast_all_or_nothing)
        factory_atomic.add_option("case", all_or_nothing_cases(ports))
        factory_atomic.generate_tests()
    elif os.environ.get('PARAM_TDEST_ROUTE', '0') == '1':
        factory = TestFactory(run_test)
        factory.add_option("payload_lengths", [size_list])
        factory.add_option("payload_data", [incrementing_payload])
        factory.add_option("idle_inserter", [None, cycle_pause])
        factory.add_option("backpressure_inserter", [None, cycle_pause])
        factory.add_option("port", list(range(ports)))
        factory.generate_tests()
    else:
        raise RuntimeError("ERROR: Makefile is misconfigured - neither PARAM_TUSER_BITMAP_ROUTE nor PARAM_TDEST_ROUTE is set to 1")

# ----------------------------------------------------------------------
# PyTest framework: test parameterization and test runner
# ----------------------------------------------------------------------

tests_dir = os.path.dirname(__file__)
repo_dir = os.path.abspath(os.path.join(tests_dir, '..', '..', '..'))
hw_dir = os.path.join(repo_dir, 'hw')
libs_dir = os.path.join(repo_dir, 'libs')
core_dir = os.path.join(hw_dir, 'rtl', 'core')
taxi_axis_dir = os.path.join(libs_dir, 'taxi', 'src', 'axis', 'rtl')

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

@pytest.mark.parametrize("tuser_bitmap_route", [0, 1])
@pytest.mark.parametrize("data_w", [8, 16])
@pytest.mark.parametrize("m_count", [4, 6])
def test_openenoc_axis_demux(request, m_count, data_w, tuser_bitmap_route):
    dut = "openenoc_axis_demux"
    module = os.path.splitext(os.path.basename(__file__))[0]
    toplevel = module

    verilog_sources = [
        os.path.join(tests_dir, f"{toplevel}.sv"),
        os.path.join(core_dir, f"{dut}.sv"),
        os.path.join(taxi_axis_dir, "taxi_axis_if.sv"),
    ]

    verilog_sources = process_f_files(verilog_sources)

    parameters = {}

    parameters['M_COUNT'] = m_count
    parameters['DATA_W'] = data_w
    parameters['KEEP_EN'] = int(parameters['DATA_W'] > 8)
    parameters['KEEP_W'] = (parameters['DATA_W'] + 7) // 8
    parameters['STRB_EN'] = 0
    parameters['LAST_EN'] = 1
    parameters['ID_EN'] = 1
    parameters['M_ID_W'] = 8
    parameters['S_ID_W'] = parameters['M_ID_W'] + (m_count-1).bit_length()
    parameters['DEST_EN'] = 1
    parameters['M_DEST_W'] = 8
    parameters['S_DEST_W'] = parameters['M_DEST_W'] + (m_count-1).bit_length()
    parameters['USER_EN'] = 1
    parameters['USER_W'] = m_count
    parameters['TID_ROUTE'] = 0
    parameters['TDEST_ROUTE'] = 1 - tuser_bitmap_route
    parameters['TUSER_BITMAP_ROUTE'] = tuser_bitmap_route

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
