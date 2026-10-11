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
    dut.peer_error.value = 0
    dut.peer_error_code.value = 0
    dut.peer_clear_error_hwclr.value = 0
    dut.non_error.value = 0
    dut.non_error_code.value = 0
    dut.non_clear_errors_hwclr.value = 0
    cocotb.start_soon(Clock(dut.clk, 10, unit="ns").start())

    dut.rst.value = 1
    await Timer(100, unit="ns")
    dut.rst.value = 0

    axi_bus = AxiLiteBus.from_prefix(dut, "s_axil")
    axi_master = AxiLiteMaster(axi_bus, dut.clk, dut.rst)

    hw = RTLSimulator(axi_master)

    csr = csr_cls(callbacks=NormalCallbackSet(read_callback=hw.read, write_callback=hw.write))

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


@cocotb.test()
async def test_rmem_timeout_config(dut):
    await run_reg_test(dut, test_rmem_timeout_cycles)


@cocotb.test()
async def test_config_addresses_and_timeouts(dut):
    await run_reg_test(dut, test_config_mac_and_timeouts)


@cocotb.test()
async def test_fragment_size_config(dut):
    await run_reg_test(dut, test_dma_max_fragment_size_bytes)


@cocotb.test()
async def test_peer_failure_record_and_clear_command(dut):
    csr = await create_csr(dut)
    peers = csr.endpoint_interface.peers.entry

    def snapshot():
        return (
            peers[1].dma.error.read(),
            peers[1].dma.error_code.read(),
            peers[2].dma.error.read(),
            peers[2].dma.error_code.read(),
        )

    def request_clear():
        peers[1].dma.clear_error.write(1)

    assert await bridge(snapshot)() == (0, 0, 0, 0)
    dut.peer_error.value = (1 << 1) | (1 << 2)
    dut.peer_error_code.value = (8 << 4) | (12 << 8)
    await Timer(20, unit="ns")
    assert await bridge(snapshot)() == (1, 8, 1, 12)
    await bridge(request_clear)()
    assert await bridge(lambda: peers[1].dma.clear_error.read())() == 1
    assert await bridge(snapshot)() == (1, 8, 1, 12)

    dut.peer_clear_error_hwclr.value = 1 << 1
    dut.peer_error.value = 1 << 2
    dut.peer_error_code.value = 12 << 8
    await Timer(20, unit="ns")
    dut.peer_clear_error_hwclr.value = 0
    assert await bridge(lambda: peers[1].dma.clear_error.read())() == 0
    assert await bridge(snapshot)() == (0, 0, 1, 12)
    assert await bridge(lambda: peers[2].dma.clear_error.read())() == 0


@cocotb.test()
async def test_non_oetp_failure_records_and_clear_commands(dut):
    csr = await create_csr(dut)
    tx = csr.endpoint_interface.non_oetp_dma.tx.command_status
    rx = csr.endpoint_interface.non_oetp_dma.rx.command_status

    def snapshot():
        return (
            tx.error.read(),
            tx.error_code.read(),
            tx.clear_errors.read(),
            rx.error.read(),
            rx.error_code.read(),
            rx.clear_errors.read(),
        )

    assert await bridge(snapshot)() == (0, 0, 0, 0, 0, 0)
    dut.non_error.value = 0b11
    dut.non_error_code.value = 4 | (6 << 4)
    await Timer(20, unit="ns")

    await bridge(lambda: tx.clear_errors.write(1))()
    assert await bridge(snapshot)() == (1, 4, 1, 1, 6, 0)
    dut.non_clear_errors_hwclr.value = 0b01
    dut.non_error.value = 0b10
    dut.non_error_code.value = 6 << 4
    await Timer(20, unit="ns")
    dut.non_clear_errors_hwclr.value = 0
    assert await bridge(snapshot)() == (0, 0, 0, 1, 6, 0)

    await bridge(lambda: rx.clear_errors.write(1))()
    assert await bridge(snapshot)() == (0, 0, 0, 1, 6, 1)
    dut.non_clear_errors_hwclr.value = 0b10
    dut.non_error.value = 0
    dut.non_error_code.value = 0
    await Timer(20, unit="ns")
    dut.non_clear_errors_hwclr.value = 0
    assert await bridge(snapshot)() == (0, 0, 0, 0, 0, 0)
