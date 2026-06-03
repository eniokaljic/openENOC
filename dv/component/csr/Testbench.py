# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: AGPL-3.0-or-later

import cocotb
import threading
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotbext.axi import AxiLiteBus, AxiLiteMaster

from csr.lib import NormalCallbackSet
from csr.reg_model.csr import csr_cls

from RTLSimulator import RTLSimulator
from Tests import *

async def create_csr(dut):
    cocotb.start_soon(Clock(dut.clk, 10, unit="ns").start())

    dut.rst.value = 1
    await Timer(100, unit="ns")
    dut.rst.value = 0

    axi_bus = AxiLiteBus.from_prefix(dut, "s_axil")
    axi_master = AxiLiteMaster(axi_bus, dut.clk, dut.rst)

    hw = RTLSimulator(axi_master)
    cocotb.start_soon(hw.worker())

    csr = csr_cls(
        callbacks=NormalCallbackSet(
            read_callback=hw.read,
            write_callback=hw.write
        )
    )

    return csr


async def run_reg_test(dut, test_func):
    csr = await create_csr(dut)

    exc = None

    def worker():
        nonlocal exc

        try:
            test_func(csr)

        except Exception as e:
            exc = e

    t = threading.Thread(target=worker)
    t.start()

    while t.is_alive():
        await Timer(1, unit="ns")

    t.join()

    if exc is not None:
        raise exc


@cocotb.test()
async def test1(dut):
    await run_reg_test(dut, Test1)


@cocotb.test()
async def test2(dut):
    await run_reg_test(dut, Test2)

