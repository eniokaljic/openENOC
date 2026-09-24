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

EXECUTION_TIMEOUT_CYCLES = 1000
FIRMWARE_TIMEOUT_CYCLES = 100_000
CSR_SMOKE_PATTERN = 0xA5A55A5A
CSR_SMOKE_PASSED = 0x600D600D
CSR_SMOKE_FAILED = 0xBAD0BAD0


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
    assert int(dut.dmem_word0.value) == 0
    dut.rst.value = 0

    with open(os.environ["OPENENOC_FIRMWARE_BIN"], "rb") as firmware_file:
        image = firmware_file.read()

    library = IssLibrary(os.environ["OPENENOC_ISS_LIBRARY"])
    request_count = 0

    with library.create_endpoint(0) as endpoint:
        endpoint.load_image(image)
        endpoint.start(entry_pc=0, max_steps=1_000_000)

        for _ in range(FIRMWARE_TIMEOUT_CYCLES):
            await RisingEdge(dut.clk)

            request = endpoint.poll()
            if request is not None:
                request_count += 1
                await service_request(endpoint, axi_master, request)

            status = int(dut.dmem_word0.value)
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

        for _ in range(1000):
            state = endpoint.state()
            if state.run_state == RunState.STOPPED:
                break
            await RisingEdge(dut.clk)
        else:
            raise AssertionError("Spike worker did not stop after firmware passed")

    cocotb.log.info(
        "csr_smoke completed through Spike after %d external requests",
        request_count,
    )
    assert int(dut.csr_test_value.value) == CSR_SMOKE_PATTERN
    assert int(dut.switch_operation_mode.value) == 1
    assert int(dut.switch_pause_request.value) == 1
    assert int(dut.switch_default_forwarding.value) == 0xA
    assert int(dut.imem_active.value) == 0