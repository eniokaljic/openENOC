# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: AGPL-3.0-or-later

import cocotb
from cocotb.clock import Clock
from cocotb.task import bridge
from cocotb.triggers import Timer
from cocotbext.axi import AxiLiteBus, AxiLiteMaster

from csr.lib import NormalCallbackSet
from csr.reg_model.csr import csr_cls

from rtl_simulator import RTLSimulator
from tests import *


async def create_csr(dut):
    cocotb.start_soon(Clock(dut.clk, 10, unit="ns").start())

    dut.rst.value = 1
    await Timer(100, unit="ns")
    dut.rst.value = 0

    axi_bus = AxiLiteBus.from_prefix(dut, "s_axil")
    axi_master = AxiLiteMaster(axi_bus, dut.clk, dut.rst)

    hw = RTLSimulator(axi_master)

    csr = csr_cls(
        callbacks=NormalCallbackSet(
            read_callback=hw.read,
            write_callback=hw.write
        )
    )

    return csr


async def run_reg_test(dut, test_func):
    csr = await create_csr(dut)
    await bridge(test_func)(csr)


@cocotb.test()
async def test_1(dut):
    await run_reg_test(dut, test1)


@cocotb.test()
async def test_2(dut):
    await run_reg_test(dut, test2)
