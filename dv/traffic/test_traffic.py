# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: AGPL-3.0-or-later

import logging
import os

import cocotb_test.simulator
import pytest

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge
from cocotb.regression import TestFactory
from cocotb.handle import Immediate

from cocotbext.axi import AxiStreamBus, AxiStreamFrame, AxiStreamSource, AxiStreamSink

class TB(object):
    def __init__(self, dut):
        self.dut = dut

        self.log = logging.getLogger("cocotb.tb")
        self.log.setLevel(logging.DEBUG)

        cocotb.start_soon(Clock(dut.clk, 10000, unit="ps").start())

    async def reset(self):
        self.dut.rst.value = Immediate(1)
        await RisingEdge(self.dut.clk)
        await RisingEdge(self.dut.clk)
        await RisingEdge(self.dut.clk)
        await RisingEdge(self.dut.clk)
        self.dut.rst.value = 0

@cocotb.test()
async def test(dut):
    tb = TB(dut)

    await tb.reset()

    await RisingEdge(dut.pcapfinished)

    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)

# ----------------------------------------------------------------------
# PyTest framework: test parameterization and test runner
# ----------------------------------------------------------------------

tests_dir = os.path.dirname(__file__)
hw_dir = os.path.abspath(os.path.join(tests_dir, '..', '..', 'hw'))
core_dir = os.path.join(hw_dir, 'src', 'core')
taxi_axis_dir = os.path.join(hw_dir, 'libs', 'taxi', 'src', 'axis', 'rtl')

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

@pytest.mark.parametrize("data_width", [8, 16, 32, 64, 128, 256, 512])
@pytest.mark.parametrize("pcap_in_filename", ["test1.pcap", "test2.pcap"])
def test_traffic(request, data_width, pcap_in_filename):
    module = os.path.splitext(os.path.basename(__file__))[0]
    toplevel = module

    verilog_sources = [
        os.path.join(tests_dir, f"{toplevel}.sv"),
        os.path.join(tests_dir, "pcapreader.sv"),
        os.path.join(tests_dir, "pcapwriter.sv"),
        os.path.join(tests_dir, "avalon_if.sv"),
        os.path.join(taxi_axis_dir, "taxi_axis_if.sv"),
    ]

    verilog_sources = process_f_files(verilog_sources)

    sim_build = os.path.join(
        tests_dir,
        "sim_build",
        request.node.name.replace("[", "-").replace("]", "")
    )

    pcap_in_path = os.path.abspath(os.path.join(tests_dir, pcap_in_filename))
    pcap_out_path = os.path.abspath(os.path.join(sim_build, "output.pcap"))

    parameters = {
        "DATA_WIDTH": data_width,
        "CLOCK_PERIOD": 10000,
        "PCAP_IN_FILENAME": f'"{pcap_in_path}"',
        "PCAP_OUT_FILENAME": f'"{pcap_out_path}"',
    }

    extra_env = {
        f"PARAM_{k}": str(v).strip('"')
        for k, v in parameters.items()
    }

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
