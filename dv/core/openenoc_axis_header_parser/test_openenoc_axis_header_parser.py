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

class TB:
    def __init__(self, dut):
        self.dut = dut

        self.log = logging.getLogger("cocotb.tb")
        self.log.setLevel(logging.DEBUG)

        cocotb.start_soon(Clock(dut.clk, 10, units="ns").start())

        self.source = AxiStreamSource(AxiStreamBus.from_entity(dut.s_axis), dut.clk, dut.rst)
        self.sink = AxiStreamSink(AxiStreamBus.from_entity(dut.m_axis), dut.clk, dut.rst)

    def set_idle_generator(self, generator=None):
        if generator:
            self.source.set_pause_generator(generator())

    def set_backpressure_generator(self, generator=None):
        if generator:
            self.sink.set_pause_generator(generator())

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
# Helper functions for test parameterization
# ----------------------------------------------------------------------

def make_payload(length):
    return bytes(itertools.islice(itertools.cycle(range(1, 256)), length))

def make_header(seed):
    # Distinct, easily recognizable 16-byte header per frame index.
    dst = [(seed + 1) & 0xFF] * 6
    src = [(0x10 + seed) & 0xFF] * 6
    etype = [0x88, 0xB5]
    oetp = [(0xA0 + seed) & 0xFF, seed & 0xFF]
    return bytes(dst + src + etype + oetp)

def cycle_pause():
    return itertools.cycle([1, 1, 1, 0])

def size_list():
    data_width = len(cocotb.top.s_axis.tdata)
    byte_width = data_width // 8
    # payload lengths (the 16-byte header is always prepended on top of these)
    return list(range(0, byte_width * 4 + 1)) + [64] + [0] * 4

def tuser_values(frame):
    tu = frame.tuser
    if isinstance(tu, (list, tuple)):
        return list(tu)
    return [tu]

def check_frame(rx_frame, tx_frame, expected_tuser):
    # payload passes through unchanged
    assert rx_frame.tdata == tx_frame.tdata, \
        f"tdata mismatch: {bytes(rx_frame.tdata).hex()} != {bytes(tx_frame.tdata).hex()}"
    # 128-bit header present and stable on tuser for the whole frame
    for tu in tuser_values(rx_frame):
        assert tu == expected_tuser, \
            f"tuser mismatch: {tu:032x} != {expected_tuser:032x}"


# ----------------------------------------------------------------------
# TestFactory logic: sweep payload sizes, idle and backpressure combos
# ----------------------------------------------------------------------

async def run_test_factory_frames(dut, payload_lengths=None, payload_data=None, idle_inserter=None, backpressure_inserter=None):
    tb = TB(dut)
    await tb.reset()

    tb.set_idle_generator(idle_inserter)
    tb.set_backpressure_generator(backpressure_inserter)

    test_frames = []

    for idx, length in enumerate(payload_lengths()):
        header = make_header(idx)
        data = bytearray(header) + payload_data(length)
        test_frame = AxiStreamFrame(data)
        expected = int.from_bytes(header, "big")

        test_frames.append((test_frame, expected))
        await tb.source.send(test_frame)

    for test_frame, expected in test_frames:
        rx_frame = await tb.sink.recv()
        check_frame(rx_frame, test_frame, expected)

    assert tb.sink.empty()

    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)


# ----------------------------------------------------------------------
# Dispatch: select test cases to run based on Makefile configuration
# ----------------------------------------------------------------------

if getattr(cocotb, 'top', None) is not None:
    factory = TestFactory(run_test_factory_frames)
    factory.add_option("payload_lengths", [size_list])
    factory.add_option("payload_data", [make_payload])
    factory.add_option("idle_inserter", [None, cycle_pause])
    factory.add_option("backpressure_inserter", [None, cycle_pause])
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
common_dir = os.path.abspath(os.path.join(tests_dir, '..', '..', 'common'))

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

@pytest.mark.parametrize("data_w", [8, 16, 32, 64])
def test_openenoc_axis_header_parser(request, data_w):
    dut = "openenoc_axis_header_parser"
    module = os.path.splitext(os.path.basename(__file__))[0]
    toplevel = module

    verilog_sources = [
        os.path.join(tests_dir, f"{toplevel}.sv"),
        os.path.join(core_dir, f"{dut}.sv"),
        os.path.join(taxi_axis_dir, "taxi_axis_if.sv"),
        os.path.join(taxi_axis_dir, "taxi_axis_fifo.sv"),
        os.path.join(taxi_axis_dir, "taxi_axis_register.sv"),
    ]

    verilog_sources = process_f_files(verilog_sources)

    parameters = {}
    parameters['DATA_W'] = data_w
    parameters['KEEP_EN'] = int(parameters['DATA_W'] > 8)
    parameters['KEEP_W'] = (parameters['DATA_W'] + 7) // 8
    parameters['STRB_EN'] = 0
    parameters['LAST_EN'] = 1
    parameters['USER_W'] = 128
    parameters['DEPTH'] = 0
    parameters['M_REG_TYPE'] = 2

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
        extra_args=[
            os.path.join(common_dir, "config.vlt"),
        ],
        sim_build=sim_build,
        extra_env=extra_env,
    )
