# SPDX-FileCopyrightText: 2026 Kerim Bavcic
# SPDX-License-Identifier: AGPL-3.0-or-later

import os
import struct

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge
from cocotb.utils import get_sim_time
from cocotbext.axi import AxiLiteBus, AxiLiteMaster

from openenoc_iss import IssLibrary, RequestKind, ResponseStatus, RunState
from openenoc_iss import load_elf

EXECUTION_TIMEOUT_CYCLES = 1000
FIRMWARE_TIMEOUT_CYCLES = 100_000
DMEM_BASE = 0x10000000
DMEM_SIZE = 0x00008000
CSR_SMOKE_PATTERN = 0xA5A55A5A
CSR_SMOKE_PASSED = 0x600D600D
CSR_SMOKE_FAILED = 0xBAD0BAD0
ISS_STARTUP_PASSED = 0x51A7C0DE
ISS_STARTUP_FAILED = 0xFA11ED00
STARTUP_INITIALIZED_WORDS = (0x12345678, 0x89ABCDEF)


def load_boot_image(endpoint, boot_image):
    for segment in boot_image.segments:
        endpoint.load_image(segment.data, address=segment.load_address)


def request_value(request):
    return int.from_bytes(request.data, byteorder="little")


async def read_word(axi_master, address):
    result = await axi_master.read(address, 4, prot=0)
    assert int(result.resp) == 0
    return int.from_bytes(result.data, byteorder="little")


async def write_word(axi_master, address, value):
    result = await axi_master.write(address, struct.pack("<I", value), prot=0)
    assert int(result.resp) == 0


async def wait_for_stop(endpoint, dut):
    for _ in range(1000):
        state = endpoint.state()
        if state.run_state == RunState.STOPPED:
            return
        await RisingEdge(dut.clk)
    raise AssertionError("Spike worker did not stop after firmware passed")


async def service_request(endpoint, axi_master, request):
    accepted_tick = int(get_sim_time(unit="ns"))

    if request.kind == RequestKind.DATA_READ:
        result = await axi_master.read(request.address, request.size_bytes, prot=0)
        data = bytes(result.data)
    else:
        result = await axi_master.write(request.address, request.data, prot=0)
        data = b""

    completed_tick = int(get_sim_time(unit="ns"))
    axi_resp = int(result.resp)
    endpoint.complete(
        request,
        data=data,
        status=(
            ResponseStatus.OK
            if axi_resp == 0
            else ResponseStatus.BUS_ERROR
        ),
        axi_resp=axi_resp,
        accepted_sim_tick=accepted_tick,
        completed_sim_tick=completed_tick,
    )


@cocotb.test()
async def test_spike_accesses_rtl_dmem(dut):
    cocotb.start_soon(Clock(dut.clk, 10, unit="ns").start())
    axi_master = AxiLiteMaster(
        AxiLiteBus.from_prefix(dut, "iss_axil"), dut.clk, dut.rst
    )

    dut.rst.value = 1
    for _ in range(5):
        await RisingEdge(dut.clk)
    dut.rst.value = 0

    image = struct.pack(
        "<5I",
        0x100000B7,
        0x02A00113,
        0x0020A023,
        0x0000A183,
        0x00118213,
    )
    library = IssLibrary(os.environ["OPENENOC_ISS_LIBRARY"])

    with library.create_endpoint(0) as endpoint:
        endpoint.load_image(image)
        endpoint.start(entry_pc=0, max_steps=5)
        requests = []

        for _ in range(EXECUTION_TIMEOUT_CYCLES):
            await RisingEdge(dut.clk)

            request = endpoint.poll()
            if request is not None:
                requests.append(request)
                await service_request(endpoint, axi_master, request)

            state = endpoint.state()
            assert state.run_state != RunState.ERROR
            if state.run_state == RunState.COMPLETED:
                break
        else:
            raise AssertionError("Spike did not complete the RTL DMEM smoke test")

        assert [request.kind for request in requests] == [
            RequestKind.DATA_WRITE,
            RequestKind.DATA_READ,
        ]
        assert [request.address for request in requests] == [
            0x10000000,
            0x10000000,
        ]
        assert endpoint.read_register(3) == 42
        assert endpoint.read_register(4) == 43

    assert int(dut.dmem_word0.value) == 42
    assert int(dut.imem_active.value) == 0


@cocotb.test()
async def test_spike_runs_csr_smoke_firmware(dut):
    cocotb.start_soon(Clock(dut.clk, 10, unit="ns").start())
    axi_master = AxiLiteMaster(
        AxiLiteBus.from_prefix(dut, "iss_axil"), dut.clk, dut.rst
    )

    dut.rst.value = 1
    for _ in range(5):
        await RisingEdge(dut.clk)
    dut.rst.value = 0

    boot_image = load_elf(os.environ["OPENENOC_FIRMWARE_ELF"])
    status_address = boot_image.symbol_address("csr_smoke_status")
    assert boot_image.symbols["csr_smoke_status"].size == 4
    assert await read_word(axi_master, status_address) == 0
    library = IssLibrary(os.environ["OPENENOC_ISS_LIBRARY"])
    request_count = 0

    with library.create_endpoint(0) as endpoint:
        load_boot_image(endpoint, boot_image)
        endpoint.start(entry_pc=boot_image.entry_pc, max_steps=1_000_000)

        for _ in range(FIRMWARE_TIMEOUT_CYCLES):
            await RisingEdge(dut.clk)

            request = endpoint.poll()
            if request is not None:
                request_count += 1
                status_write = (
                    request.kind == RequestKind.DATA_WRITE
                    and request.address == status_address
                    and request.size_bytes == 4
                )
                status = request_value(request) if status_write else None
                await service_request(endpoint, axi_master, request)
                assert status != CSR_SMOKE_FAILED, (
                    f"csr_smoke reported failure after {request_count} requests"
                )
                if status == CSR_SMOKE_PASSED:
                    endpoint.request_stop()
                    break

            state = endpoint.state()
            assert state.run_state != RunState.ERROR
            assert state.run_state != RunState.COMPLETED, (
                "Spike exhausted its instruction budget before firmware completed"
            )
        else:
            raise AssertionError(
                "csr_smoke did not complete through the ISS/RTL bridge"
            )

        await wait_for_stop(endpoint, dut)

    cocotb.log.info(
        "csr_smoke completed through Spike after %d external requests",
        request_count,
    )
    assert await read_word(axi_master, status_address) == CSR_SMOKE_PASSED
    assert int(dut.csr_test_value.value) == CSR_SMOKE_PATTERN
    assert int(dut.switch_operation_mode.value) == 1
    assert int(dut.switch_pause_request.value) == 1
    assert int(dut.switch_default_forwarding.value) == 0xA
    assert int(dut.imem_active.value) == 0


@cocotb.test()
async def test_spike_qualifies_elf_startup(dut):
    cocotb.start_soon(Clock(dut.clk, 10, unit="ns").start())
    axi_master = AxiLiteMaster(
        AxiLiteBus.from_prefix(dut, "iss_axil"), dut.clk, dut.rst
    )

    dut.rst.value = 1
    for _ in range(5):
        await RisingEdge(dut.clk)
    dut.rst.value = 0

    boot_image = load_elf(os.environ["OPENENOC_STARTUP_FIRMWARE_ELF"])
    status_address = boot_image.symbol_address("iss_startup_status")
    initialized_address = boot_image.symbol_address("startup_initialized")
    bss_address = boot_image.symbol_address("startup_bss")
    rodata_address = boot_image.symbol_address("startup_rodata")
    stack_limit = boot_image.symbol_address("__stack_limit")
    stack_top = boot_image.symbol_address("__stack_top")

    assert 0 <= rodata_address < DMEM_BASE
    assert DMEM_BASE <= initialized_address < DMEM_BASE + DMEM_SIZE
    assert DMEM_BASE <= bss_address < DMEM_BASE + DMEM_SIZE
    assert DMEM_BASE <= status_address < DMEM_BASE + DMEM_SIZE
    assert any(
        segment.virtual_address == initialized_address
        and segment.load_address != segment.virtual_address
        for segment in boot_image.segments
    )

    dirty_value = 0xA5A5A5A5
    await write_word(axi_master, bss_address, dirty_value)
    await write_word(axi_master, status_address, dirty_value)
    assert await read_word(axi_master, bss_address) == dirty_value
    assert await read_word(axi_master, status_address) == dirty_value

    library = IssLibrary(os.environ["OPENENOC_ISS_LIBRARY"])
    request_count = 0
    observed_data_copy = False
    observed_bss_clear = False
    observed_stack_access = False

    with library.create_endpoint(0) as endpoint:
        load_boot_image(endpoint, boot_image)
        endpoint.start(entry_pc=boot_image.entry_pc, max_steps=100_000)

        for _ in range(FIRMWARE_TIMEOUT_CYCLES):
            await RisingEdge(dut.clk)

            request = endpoint.poll()
            if request is not None:
                request_count += 1
                value = (
                    request_value(request)
                    if request.kind == RequestKind.DATA_WRITE
                    else None
                )
                observed_data_copy |= (
                    request.kind == RequestKind.DATA_WRITE
                    and request.address == initialized_address
                    and value == STARTUP_INITIALIZED_WORDS[0]
                )
                observed_bss_clear |= (
                    request.kind == RequestKind.DATA_WRITE
                    and request.address == bss_address
                    and value == 0
                )
                observed_stack_access |= (
                    stack_limit <= request.address < stack_top
                )
                status_write = (
                    request.kind == RequestKind.DATA_WRITE
                    and request.address == status_address
                    and request.size_bytes == 4
                )

                await service_request(endpoint, axi_master, request)

                if status_write:
                    assert value != ISS_STARTUP_FAILED, (
                        "startup qualification firmware reported failure"
                    )
                    if value == ISS_STARTUP_PASSED:
                        endpoint.request_stop()
                        break

            state = endpoint.state()
            assert state.run_state != RunState.ERROR
            assert state.run_state != RunState.COMPLETED, (
                "Spike exhausted its instruction budget before startup completed"
            )
        else:
            raise AssertionError("startup qualification firmware timed out")

        await wait_for_stop(endpoint, dut)

    assert observed_data_copy
    assert observed_bss_clear
    assert observed_stack_access
    assert await read_word(axi_master, initialized_address) == (
        STARTUP_INITIALIZED_WORDS[0]
    )
    assert await read_word(axi_master, initialized_address + 4) == (
        STARTUP_INITIALIZED_WORDS[1]
    )
    assert await read_word(axi_master, bss_address) == 0
    assert await read_word(axi_master, status_address) == ISS_STARTUP_PASSED
    assert int(dut.imem_active.value) == 0

    cocotb.log.info(
        "ELF startup qualified through Spike after %d external requests",
        request_count,
    )