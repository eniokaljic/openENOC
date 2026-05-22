# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: AGPL-3.0-or-later

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

import cocotb
import threading
import queue
from cocotb.clock import Clock
from cocotb.triggers import Timer
from cocotbext.axi import AxiLiteBus, AxiLiteMaster

from build.python.csr.lib import NormalCallbackSet
from build.python.csr.reg_model.csr import csr_cls

from RTLSimulator import RTLSimulator
from Application import Application

error_q = queue.Queue()

def reg_thread(csr):
    try:
        Application(csr)

    except Exception as e:
        error_q.put(e)


@cocotb.test()
async def test_csr(dut):

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
    
    t = threading.Thread(target=reg_thread, args=(csr,))
    t.start()

    while t.is_alive():
        await Timer(1, unit="ns")

        if not error_q.empty():
            exc = error_q.get()
            raise exc

    t.join()

