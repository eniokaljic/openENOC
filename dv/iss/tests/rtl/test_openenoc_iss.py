# SPDX-FileCopyrightText: 2026 Kerim Bavcic
# SPDX-License-Identifier: AGPL-3.0-or-later

import os
import struct
from asyncio import CancelledError
from contextlib import AsyncExitStack, ExitStack
from dataclasses import replace
from pathlib import Path
from types import SimpleNamespace

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ReadOnly, RisingEdge, SimTimeoutError, Timer, with_timeout
from cocotb.utils import get_sim_time
from cocotbext.axi import AxiLiteBus, AxiLiteMaster

from openenoc_iss import IssError, IssLibrary, RequestKind, ResponseStatus, RunState
from openenoc_iss import load_elf, load_memory_map

EXECUTION_TIMEOUT_CYCLES = 1000
FIRMWARE_TIMEOUT_CYCLES = 100_000
AXI_SERVICE_TIMEOUT_NS = 10_000
MEMORY_MAP = load_memory_map(os.environ["OPENENOC_MEMORY_MAP"])
DMEM_BASE = MEMORY_MAP.dmem_base
DMEM_SIZE = MEMORY_MAP.dmem_size
CSR_BASE = MEMORY_MAP.csr_base
CSR_SIZE = MEMORY_MAP.csr_size
CSR_SMOKE_PATTERN = 0xA5A55A5A
CSR_SMOKE_PASSED = 0x600D600D
CSR_SMOKE_FAILED = 0xBAD0BAD0
ISS_STARTUP_PASSED = 0x51A7C0DE
ISS_STARTUP_FAILED = 0xFA11ED00
STARTUP_INITIALIZED_WORDS = (0x12345678, 0x89ABCDEF)
IRQ_QUANTUM = 32
LINK_HEADER = tuple(
    (word, 0xF, False)
    for word in (0xFFFFFFFF, 0x0122FFFF, 0x89ABCDEF, 0x00000008)
)
LINK_REQUEST_PREFIX = LINK_HEADER + ((0x13579BDF, 0xF, False),)
LINK_REQUEST_FRAME = LINK_REQUEST_PREFIX + ((0x89ABCDEF, 0xF, True),)
LINK_REPLY_FRAME = LINK_HEADER + ((0x2468ACE0, 0xF, True),)
AXIS_LOOPBACK_WORDS = (
    0xFFFFFFFF, 0x0122FFFF, 0x89ABCDEF, 0xFFFFFFFF,
    0xA5A55A5A, 0x5A5AA5A5, 0x00000001, 0x80000000,
    0x11111111, 0x22222222, 0x33333333, 0x44444444,
    0xDEADBEEF, 0xC001D00D, 0x13579BDF, 0x2468ACE0,
    0x0000BEEF,
)


async def collect_axis_transfers(dut, prefix, transfers, clock=None):
    valid = getattr(dut, f"{prefix}_valid")
    ready = getattr(dut, f"{prefix}_ready")
    data = getattr(dut, f"{prefix}_data")
    keep = getattr(dut, f"{prefix}_keep")
    last = getattr(dut, f"{prefix}_last")
    while True:
        await RisingEdge(clock if clock is not None else dut.clk)
        if int(valid.value) and int(ready.value):
            transfers.append((int(data.value), int(keep.value), bool(int(last.value))))


async def collect_irq_completions(dut, tokens):
    previous_ack = False
    while True:
        await RisingEdge(dut.clk)
        assert not int(dut.irq_invalid_complete.value)
        ack = bool(int(dut.irq_complete_hwclr.value))
        if ack and not previous_ack:
            tokens.append(int(dut.irq_complete_token.value))
        previous_ack = ack


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

async def stop_firmware_tasks(endpoints, tasks, dut):
    for endpoint in endpoints:
        endpoint.request_stop()
    pending = [task for task in tasks if not task.done()]
    for task in pending:
        task.cancel()
    for task in pending:
        try:
            await task
        except CancelledError:
            pass
    for endpoint in endpoints:
        await wait_for_stop(endpoint, dut)


class IrqPublisher:
    def __init__(self, endpoint, level, clock):
        self.endpoint = endpoint
        self.level = level
        self.clock = clock
        self.epoch = endpoint.state().epoch
        self.sequence = 0
        self.seen_high = False
        self.seen_low_after_high = False

    async def sample(self, credit=0):
        await ReadOnly()
        self.publish(credit)

    def publish(self, credit=0):
        level = bool(int(self.level.value))
        self.seen_low_after_high |= self.seen_high and not level
        self.seen_high |= level
        self.sequence += 1
        self.endpoint.update_irq(
            level=level,
            epoch=self.epoch,
            sim_tick=int(get_sim_time(unit="ns")),
            sequence=self.sequence,
            step_budget=credit,
        )

    async def run(self):
        while True:
            await RisingEdge(self.clock)
            await self.sample(IRQ_QUANTUM)


async def service_request(endpoint, axi_master, request, irq_publisher=None):
    size = request.size_bytes
    address = request.address
    memory_map = endpoint.memory_map
    valid_region = any(
        base <= address and address - base <= length - size
        for base, length in (
            (memory_map.dmem_base, memory_map.dmem_size),
            (memory_map.csr_base, memory_map.csr_size),
        )
    )
    if (
        request.kind not in (RequestKind.DATA_READ, RequestKind.DATA_WRITE)
        or size not in (1, 2, 4)
        or address % size
        or request.byte_enable != (1 << size) - 1
        or (request.kind == RequestKind.DATA_WRITE and len(request.data) != size)
        or not valid_region
    ):
        endpoint.request_stop()
        raise ValueError("invalid ISS AXI request")

    accepted_tick = int(get_sim_time(unit="ns"))

    try:
        if request.kind == RequestKind.DATA_READ:
            result = await with_timeout(
                axi_master.read(request.address, request.size_bytes, prot=0),
                AXI_SERVICE_TIMEOUT_NS, "ns",
            )
        else:
            result = await with_timeout(
                axi_master.write(request.address, request.data, prot=0),
                AXI_SERVICE_TIMEOUT_NS, "ns",
            )
        if result is None:
            raise RuntimeError("AXI service was flushed by reset")
        data = bytes(result.data) if request.kind == RequestKind.DATA_READ else b""
    except BaseException:
        endpoint.request_stop()
        raise

    completed_tick = int(get_sim_time(unit="ns"))
    state = endpoint.state()
    if state.run_state == RunState.STOPPED or state.epoch != request.epoch:
        return
    if irq_publisher is not None:
        await irq_publisher.sample()
    axi_resp = int(result.resp)
    try:
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
    except IssError as error:
        if error.status != -2 or endpoint.state().run_state != RunState.STOPPED:
            raise
        cocotb.log.info(
            "Discarding AXI response for request %d after worker stop",
            request.request_id,
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
async def test_spike_subword_lanes_in_rtl_dmem(dut):
    cocotb.start_soon(Clock(dut.clk, 10, unit="ns").start())
    axi_master = AxiLiteMaster(
        AxiLiteBus.from_prefix(dut, "iss_axil"), dut.clk, dut.rst
    )

    dut.rst.value = 1
    for _ in range(5):
        await RisingEdge(dut.clk)
    dut.rst.value = 0
    await write_word(axi_master, DMEM_BASE, 0x11223344)

    image = struct.pack(
        "<9I",
        0x100000B7,
        0xFFF00113,
        0x002080A3,
        0x00108183,
        0x0010C203,
        0x00209123,
        0x00209283,
        0x0020D303,
        0x0000A383,
    )
    with IssLibrary(os.environ["OPENENOC_ISS_LIBRARY"]).create_endpoint(0) as endpoint:
        endpoint.load_image(image)
        endpoint.start(entry_pc=0, max_steps=9)
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
            raise AssertionError("Spike subword lane test timed out")

        assert [request.size_bytes for request in requests] == [1, 1, 1, 2, 2, 2, 4]
        assert [request.address for request in requests] == [
            DMEM_BASE + 1, DMEM_BASE + 1, DMEM_BASE + 1,
            DMEM_BASE + 2, DMEM_BASE + 2, DMEM_BASE + 2, DMEM_BASE,
        ]
        assert endpoint.read_register(3) == 0xFFFFFFFFFFFFFFFF
        assert endpoint.read_register(4) == 0xFF
        assert endpoint.read_register(5) == 0xFFFFFFFFFFFFFFFF
        assert endpoint.read_register(6) == 0xFFFF
        assert endpoint.read_register(7) & 0xFFFFFFFF == 0xFFFFFF44

    assert await read_word(axi_master, DMEM_BASE) == 0xFFFFFF44
    assert int(dut.imem_active.value) == 0


@cocotb.test()
async def test_spike_bridge_propagates_rtl_csr_slverr(dut):
    cocotb.start_soon(Clock(dut.clk, 10, unit="ns").start())
    axi_master = AxiLiteMaster(
        AxiLiteBus.from_prefix(dut, "iss_axil"), dut.clk, dut.rst
    )
    dut.rst.value = 1
    for _ in range(5):
        await RisingEdge(dut.clk)
    dut.rst.value = 0

    invalid_csr_address = CSR_BASE + CSR_SIZE - 4
    read_only_csr_address = CSR_BASE + 0x800
    information_before = await read_word(axi_master, read_only_csr_address)
    accesses = (
        (
            RequestKind.DATA_READ,
            invalid_csr_address,
            struct.pack("<3I", 0x200020B7, 0xFFC08093, 0x0000A103),
        ),
        (
            RequestKind.DATA_WRITE,
            read_only_csr_address,
            struct.pack("<3I", 0x200010B7, 0x80008093, 0x0000A023),
        ),
    )
    for expected_kind, expected_address, image in accesses:
        with IssLibrary(os.environ["OPENENOC_ISS_LIBRARY"]).create_endpoint(0) as endpoint:
            endpoint.load_image(image)
            endpoint.start(entry_pc=0, max_steps=3)
            for _ in range(EXECUTION_TIMEOUT_CYCLES):
                await RisingEdge(dut.clk)
                request = endpoint.poll()
                if request is not None:
                    break
            else:
                raise AssertionError("Spike did not issue the CSR access")

            assert request.kind == expected_kind
            assert request.address == expected_address
            await service_request(endpoint, axi_master, request)
            for _ in range(EXECUTION_TIMEOUT_CYCLES):
                if endpoint.state().run_state == RunState.ERROR:
                    break
                await RisingEdge(dut.clk)
            else:
                raise AssertionError("CSR SLVERR did not reach the ISS worker")

            assert endpoint.state().pending_request_id == 0
            assert endpoint.poll() is None

    rtl_result = await axi_master.read(invalid_csr_address, 4, prot=0)
    assert int(rtl_result.resp) == 2
    rtl_result = await axi_master.write(read_only_csr_address, bytes(4), prot=0)
    assert int(rtl_result.resp) == 2
    assert await read_word(axi_master, read_only_csr_address) == information_before
    assert int(dut.imem_active.value) == 0


@cocotb.test()
async def test_spike_bridge_waits_for_rtl_axi_handshakes(dut):
    cocotb.start_soon(Clock(dut.clk, 10, unit="ns").start())
    axi_master = AxiLiteMaster(
        AxiLiteBus.from_prefix(dut, "iss_axil"), dut.clk, dut.rst
    )
    dut.rst.value = 1
    for _ in range(5):
        await RisingEdge(dut.clk)
    dut.rst.value = 0

    image = struct.pack(
        "<5I", 0x100000B7, 0x02A00113, 0x0020A023, 0x0000A183, 0x00118213,
    )
    with IssLibrary(os.environ["OPENENOC_ISS_LIBRARY"]).create_endpoint(0) as endpoint:
        endpoint.load_image(image)
        endpoint.start(entry_pc=0, max_steps=5)
        delayed_channels = (
            (axi_master.write_if.aw_channel, axi_master.write_if.w_channel,
             axi_master.write_if.b_channel),
            (axi_master.read_if.ar_channel, axi_master.read_if.r_channel),
        )
        for channels in delayed_channels:
            for _ in range(EXECUTION_TIMEOUT_CYCLES):
                await RisingEdge(dut.clk)
                request = endpoint.poll()
                if request is not None:
                    break
            else:
                raise AssertionError("Spike did not issue the next AXI request")

            for channel in channels:
                channel.pause = True
            service = cocotb.start_soon(service_request(endpoint, axi_master, request))
            for channel in channels:
                await Timer(100, unit="ns")
                assert endpoint.state().run_state == RunState.WAITING_MMIO
                channel.pause = False
            await service

        for _ in range(EXECUTION_TIMEOUT_CYCLES):
            if endpoint.state().run_state == RunState.COMPLETED:
                break
            await RisingEdge(dut.clk)
        else:
            raise AssertionError("Spike did not complete after delayed AXI responses")
        assert endpoint.read_register(3) == 42
        assert endpoint.read_register(4) == 43

    assert await read_word(axi_master, DMEM_BASE) == 42
    assert int(dut.imem_active.value) == 0


@cocotb.test()
async def test_spike_bridge_rejects_invalid_request_before_axi(dut):
    cocotb.start_soon(Clock(dut.clk, 10, unit="ns").start())
    image = struct.pack("<3I", 0x100000B7, 0x02A00113, 0x0020A023)

    class UntouchedMaster:
        async def read(self, *args, **kwargs):
            raise AssertionError("invalid ISS request reached AXI read")

        async def write(self, *args, **kwargs):
            raise AssertionError("invalid ISS request reached AXI write")

    for invalid_fields in (
        {"address": DMEM_BASE + 1, "size_bytes": 4},
        {"address": DMEM_BASE + DMEM_SIZE},
        {"byte_enable": 0},
        {"size_bytes": 3},
    ):
        with IssLibrary(os.environ["OPENENOC_ISS_LIBRARY"]).create_endpoint(0) as endpoint:
            endpoint.load_image(image)
            endpoint.start(entry_pc=0, max_steps=3)
            for _ in range(EXECUTION_TIMEOUT_CYCLES):
                await RisingEdge(dut.clk)
                request = endpoint.poll()
                if request is not None:
                    break
            else:
                raise AssertionError("Spike did not issue its write")

            try:
                await service_request(
                    endpoint, UntouchedMaster(), replace(request, **invalid_fields)
                )
            except ValueError:
                pass
            else:
                raise AssertionError("invalid ISS request was accepted")

            await wait_for_stop(endpoint, dut)
            assert endpoint.state().pending_request_id == 0


@cocotb.test()
async def test_spike_bridge_reports_axi_error(dut):
    cocotb.start_soon(Clock(dut.clk, 10, unit="ns").start())

    class ErrorMaster:
        writes = 0
        reads = 0

        async def write(self, address, data, *, prot):
            assert address == DMEM_BASE and data == b"\x2a\x00\x00\x00"
            assert prot == 0
            self.writes += 1
            await Timer(100, unit="ns")
            return SimpleNamespace(resp=0)

        async def read(self, address, length, *, prot):
            assert address == DMEM_BASE and length == 4 and prot == 0
            self.reads += 1
            await Timer(100, unit="ns")
            return SimpleNamespace(resp=2, data=b"\x00" * length)

    image = struct.pack(
        "<5I", 0x100000B7, 0x02A00113, 0x0020A023, 0x0000A183, 0x00118213,
    )
    axi_master = ErrorMaster()
    with IssLibrary(os.environ["OPENENOC_ISS_LIBRARY"]).create_endpoint(0) as endpoint:
        endpoint.load_image(image)
        endpoint.start(entry_pc=0, max_steps=5)
        for _ in range(EXECUTION_TIMEOUT_CYCLES):
            await RisingEdge(dut.clk)
            request = endpoint.poll()
            if request is not None:
                service = cocotb.start_soon(service_request(endpoint, axi_master, request))
                await Timer(30, unit="ns")
                assert endpoint.state().run_state == RunState.WAITING_MMIO
                await service
            if endpoint.state().run_state == RunState.ERROR:
                break
        else:
            raise AssertionError("AXI error did not stop the ISS worker")

        assert axi_master.writes == 1
        assert axi_master.reads == 1
        assert endpoint.state().pending_request_id == 0


@cocotb.test()
async def test_spike_bridge_times_out_blocked_write(dut):
    cocotb.start_soon(Clock(dut.clk, 10, unit="ns").start())

    class StalledMaster:
        writes = 0

        async def write(self, address, data, *, prot):
            assert address == DMEM_BASE and data == b"\x2a\x00\x00\x00"
            assert prot == 0
            self.writes += 1
            await Timer(AXI_SERVICE_TIMEOUT_NS * 2, unit="ns")
            return SimpleNamespace(resp=0)

    image = struct.pack("<3I", 0x100000B7, 0x02A00113, 0x0020A023)
    axi_master = StalledMaster()
    with IssLibrary(os.environ["OPENENOC_ISS_LIBRARY"]).create_endpoint(0) as endpoint:
        endpoint.load_image(image)
        endpoint.start(entry_pc=0, max_steps=3)
        for _ in range(EXECUTION_TIMEOUT_CYCLES):
            await RisingEdge(dut.clk)
            request = endpoint.poll()
            if request is not None:
                break
        else:
            raise AssertionError("Spike did not issue its write")

        try:
            await service_request(endpoint, axi_master, request)
        except SimTimeoutError:
            pass
        else:
            raise AssertionError("AXI service did not time out")

        await wait_for_stop(endpoint, dut)
        assert axi_master.writes == 1
        assert endpoint.state().pending_request_id == 0
        assert endpoint.poll() is None


@cocotb.test()
async def test_spike_resets_blocked_axi_write(dut):
    cocotb.start_soon(Clock(dut.clk, 10, unit="ns").start())
    axi_master = AxiLiteMaster(
        AxiLiteBus.from_prefix(dut, "iss_axil"), dut.clk, dut.rst
    )
    dut.rst.value = 1
    for _ in range(5):
        await RisingEdge(dut.clk)
    dut.rst.value = 0

    image = struct.pack("<3I", 0x100000B7, 0x02A00113, 0x0020A023)
    with IssLibrary(os.environ["OPENENOC_ISS_LIBRARY"]).create_endpoint(0) as endpoint:
        endpoint.load_image(image)
        previous_epoch = 0
        for blocked_channel in ("aw", "w"):
            endpoint.start(entry_pc=0, max_steps=3)
            for _ in range(EXECUTION_TIMEOUT_CYCLES):
                await RisingEdge(dut.clk)
                request = endpoint.poll()
                if request is not None:
                    break
            else:
                raise AssertionError("Spike did not issue its write")
            assert request.epoch == previous_epoch + 1
            previous_epoch = request.epoch

            axi_master.write_if.w_channel.pause = True
            axi_master.write_if.aw_channel.pause = blocked_channel == "aw"
            service = cocotb.start_soon(service_request(endpoint, axi_master, request))
            if blocked_channel == "w":
                for _ in range(EXECUTION_TIMEOUT_CYCLES):
                    await RisingEdge(dut.clk)
                    if int(dut.iss_axil_awvalid.value) and int(dut.iss_axil_awready.value):
                        break
                else:
                    raise AssertionError("AW did not handshake before reset")
            await Timer(100, unit="ns")
            assert endpoint.state().run_state == RunState.WAITING_MMIO
            dut.rst.value = 1
            try:
                await service
            except RuntimeError as error:
                assert str(error) == "AXI service was flushed by reset"
            else:
                raise AssertionError("Reset-flushed AXI service was accepted")
            await wait_for_stop(endpoint, dut)
            for _ in range(5):
                await RisingEdge(dut.clk)
            axi_master.write_if.aw_channel.pause = False
            axi_master.write_if.w_channel.pause = False
            dut.rst.value = 0
            assert await read_word(axi_master, DMEM_BASE) == 0

        endpoint.start(entry_pc=0, max_steps=3)
        for _ in range(EXECUTION_TIMEOUT_CYCLES):
            await RisingEdge(dut.clk)
            next_request = endpoint.poll()
            if next_request is not None:
                break
        else:
            raise AssertionError("Spike did not restart after reset")
        assert next_request.epoch == previous_epoch + 1
        try:
            endpoint.complete(request)
        except IssError:
            pass
        else:
            raise AssertionError("Late response from the old epoch was accepted")
        assert endpoint.state().run_state == RunState.WAITING_MMIO
        assert endpoint.state().pending_request_id == next_request.request_id
        await service_request(endpoint, axi_master, next_request)
        for _ in range(EXECUTION_TIMEOUT_CYCLES):
            if endpoint.state().run_state == RunState.COMPLETED:
                break
            await RisingEdge(dut.clk)
        else:
            raise AssertionError("Spike did not complete after reset")

    assert await read_word(axi_master, DMEM_BASE) == 42
    assert int(dut.imem_active.value) == 0


@cocotb.test()
async def test_spike_resets_pending_axi_responses(dut):
    cocotb.start_soon(Clock(dut.clk, 10, unit="ns").start())
    axi_master = AxiLiteMaster(
        AxiLiteBus.from_prefix(dut, "iss_axil"), dut.clk, dut.rst
    )
    dut.rst.value = 1
    for _ in range(5):
        await RisingEdge(dut.clk)
    dut.rst.value = 0

    image = struct.pack(
        "<5I", 0x100000B7, 0x02A00113, 0x0020A023, 0x0000A183, 0x00118213,
    )
    with IssLibrary(os.environ["OPENENOC_ISS_LIBRARY"]).create_endpoint(0) as endpoint:
        endpoint.load_image(image)
        previous_epoch = 0
        for blocked_response in ("b", "r"):
            endpoint.start(entry_pc=0, max_steps=5)
            for _ in range(EXECUTION_TIMEOUT_CYCLES):
                await RisingEdge(dut.clk)
                request = endpoint.poll()
                if request is not None:
                    break
            else:
                raise AssertionError("Spike did not issue a write")
            assert request.kind == RequestKind.DATA_WRITE
            assert request.epoch == previous_epoch + 1
            previous_epoch = request.epoch

            if blocked_response == "r":
                await service_request(endpoint, axi_master, request)
                for _ in range(EXECUTION_TIMEOUT_CYCLES):
                    await RisingEdge(dut.clk)
                    request = endpoint.poll()
                    if request is not None:
                        break
                else:
                    raise AssertionError("Spike did not issue a read")
                assert request.kind == RequestKind.DATA_READ
                axi_master.read_if.r_channel.pause = True
                handshake_valid = dut.iss_axil_arvalid
                handshake_ready = dut.iss_axil_arready
            else:
                axi_master.write_if.b_channel.pause = True
                handshake_valid = dut.iss_axil_wvalid
                handshake_ready = dut.iss_axil_wready

            service = cocotb.start_soon(service_request(endpoint, axi_master, request))
            for _ in range(EXECUTION_TIMEOUT_CYCLES):
                await RisingEdge(dut.clk)
                if int(handshake_valid.value) and int(handshake_ready.value):
                    break
            else:
                raise AssertionError("AXI request did not handshake before reset")
            await Timer(100, unit="ns")
            assert endpoint.state().run_state == RunState.WAITING_MMIO
            if blocked_response == "r":
                dut.rst.value = 1
                try:
                    await service
                except RuntimeError as error:
                    assert str(error) == "AXI service was flushed by reset"
                else:
                    raise AssertionError("Reset-flushed AXI read was accepted")
                await wait_for_stop(endpoint, dut)
            else:
                endpoint.request_stop()
                await wait_for_stop(endpoint, dut)
                service.cancel()
                dut.rst.value = 1
            for _ in range(5):
                await RisingEdge(dut.clk)
            axi_master.write_if.b_channel.pause = False
            axi_master.read_if.r_channel.pause = False
            dut.rst.value = 0
            assert await read_word(axi_master, DMEM_BASE) == 42

        endpoint.start(entry_pc=0, max_steps=5)
        for _ in range(EXECUTION_TIMEOUT_CYCLES):
            await RisingEdge(dut.clk)
            request = endpoint.poll()
            if request is not None:
                assert request.epoch == previous_epoch + 1
                await service_request(endpoint, axi_master, request)
            if endpoint.state().run_state == RunState.COMPLETED:
                break
        else:
            raise AssertionError("Spike did not complete after response resets")
        assert endpoint.read_register(3) == 42
        assert endpoint.read_register(4) == 43

    assert await read_word(axi_master, DMEM_BASE) == 42
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

    boot_image = load_elf(os.environ["OPENENOC_IRQ_FIRMWARE_ELF"])
    imem_file = Path(os.environ["OPENENOC_IRQ_FIRMWARE_ELF"]).with_name("imem.mem")
    imem_image = b"".join(
        struct.pack("<I", int(word, 16))
        for word in imem_file.read_text(encoding="ascii").splitlines()
    )
    image_offset = 0
    for segment in boot_image.segments:
        assert segment.load_address == image_offset
        assert imem_image[image_offset:image_offset + len(segment.data)] == segment.data
        image_offset += len(segment.data)
    assert image_offset == len(imem_image)
    status_address = boot_image.symbol_address("csr_smoke_status")
    assert boot_image.symbols["csr_smoke_status"].size == 4
    assert await read_word(axi_master, status_address) == 0
    library = IssLibrary(os.environ["OPENENOC_ISS_LIBRARY"])
    request_count = 0
    eth_transfers = []
    csr_sink_transfers = []
    completed_tokens = []
    eth_monitor = cocotb.start_soon(
        collect_axis_transfers(dut, "endpoint_tx", eth_transfers)
    )
    csr_sink_monitor = cocotb.start_soon(
        collect_axis_transfers(dut, "endpoint_csr_sink", csr_sink_transfers)
    )
    completion_monitor = cocotb.start_soon(collect_irq_completions(dut, completed_tokens))

    with library.create_endpoint(0, irq=True) as endpoint:
        load_boot_image(endpoint, boot_image)
        endpoint.start(entry_pc=boot_image.entry_pc, max_steps=1_000_000)
        publisher = IrqPublisher(endpoint, dut.iss_irq, dut.clk)
        await publisher.sample(IRQ_QUANTUM)
        irq_monitor = cocotb.start_soon(publisher.run())

        try:
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
                    await service_request(endpoint, axi_master, request, publisher)
                    assert status != CSR_SMOKE_FAILED, (
                        f"csr_smoke reported failure after {request_count} requests"
                    )
                    if status == CSR_SMOKE_PASSED:
                        irq_monitor.cancel()
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
        finally:
            irq_monitor.cancel()

    assert publisher.seen_high, "endpoint never asserted IRQ"
    assert publisher.seen_low_after_high, "endpoint IRQ never deasserted"
    assert await read_word(axi_master, boot_image.symbol_address("iss_trap_fault_pc")) == 0
    irq_entries = await read_word(axi_master, boot_image.symbol_address("iss_irq_entries"))
    irq_returns = await read_word(axi_master, boot_image.symbol_address("iss_irq_returns"))
    assert irq_entries > 0 and irq_entries == irq_returns

    for _ in range(10):
        await RisingEdge(dut.clk)
        assert await read_word(axi_master, status_address) == CSR_SMOKE_PASSED
        assert int(dut.csr_test_value.value) == CSR_SMOKE_PATTERN

    eth_monitor.cancel()
    csr_sink_monitor.cancel()
    completion_monitor.cancel()
    expected_transfers = [
        (
            word,
            0x3 if index == len(AXIS_LOOPBACK_WORDS) - 1 else 0xF,
            index == len(AXIS_LOOPBACK_WORDS) - 1,
        )
        for index, word in enumerate(AXIS_LOOPBACK_WORDS)
    ]
    assert eth_transfers == expected_transfers
    assert csr_sink_transfers == expected_transfers
    assert sum(keep.bit_count() for _, keep, _ in eth_transfers) == 66
    assert [(token >> 11) & 0xF for token in completed_tokens] == [4, 3]
    assert [(token >> 15) & 0xFFFF for token in completed_tokens] == [0, 1]
    assert not int(dut.irq_invalid_complete.value)
    assert int(dut.irq_fifo_level.value) == 0

    cocotb.log.info(
        "csr_smoke ELF %s completed through Spike after %d external requests",
        boot_image.sha256, request_count,
    )
    assert await read_word(axi_master, status_address) == CSR_SMOKE_PASSED
    assert int(dut.csr_test_value.value) == CSR_SMOKE_PATTERN
    assert int(dut.switch_operation_mode.value) == 1
    assert int(dut.switch_pause_request.value) == 1
    assert int(dut.switch_default_forwarding.value) == 0xA
    assert int(dut.imem_active.value) == 0


@cocotb.test()
async def test_spike_irq_two_endpoints(dut):
    cocotb.start_soon(Clock(dut.clk, 10, unit="ns").start())
    masters = [
        AxiLiteMaster(AxiLiteBus.from_prefix(entity, prefix), dut.clk, dut.rst)
        for entity, prefix in ((dut, "iss_axil"), (dut.g_dual, "iss1_axil"))
    ]
    dut.rst.value = 1
    for _ in range(5):
        await RisingEdge(dut.clk)
    dut.rst.value = 0

    boot_image = load_elf(os.environ["OPENENOC_IRQ_FIRMWARE_ELF"])
    status_address = boot_image.symbol_address("csr_smoke_status")
    for master in masters:
        assert await read_word(master, status_address) == 0
    library = IssLibrary(os.environ["OPENENOC_ISS_LIBRARY"])
    transfers = [[], []]
    monitors = [
        cocotb.start_soon(collect_axis_transfers(dut, "endpoint_tx", transfers[0])),
        cocotb.start_soon(collect_axis_transfers(
            dut.g_dual, "endpoint1_tx", transfers[1], dut.clk
        )),
    ]
    publishers = []
    irq_monitors = []
    finished = set()
    try:
        with ExitStack() as stack:
            endpoints = [
                stack.enter_context(library.create_endpoint(index, irq=True))
                for index in range(2)
            ]
            for index, endpoint in enumerate(endpoints):
                load_boot_image(endpoint, boot_image)
                endpoint.start(entry_pc=boot_image.entry_pc, max_steps=1_000_000)
                level = dut.iss_irq if index == 0 else dut.g_dual.iss1_irq
                publisher = IrqPublisher(endpoint, level, dut.clk)
                publishers.append(publisher)
            await ReadOnly()
            for publisher in publishers:
                publisher.publish(IRQ_QUANTUM)
                irq_monitors.append(cocotb.start_soon(publisher.run()))

            for _ in range(FIRMWARE_TIMEOUT_CYCLES):
                await RisingEdge(dut.clk)
                for index, endpoint in enumerate(endpoints):
                    if index in finished:
                        continue
                    request = endpoint.poll()
                    if request is not None:
                        status_write = (
                            request.kind == RequestKind.DATA_WRITE
                            and request.address == status_address
                            and request.size_bytes == 4
                        )
                        status = request_value(request) if status_write else None
                        await service_request(endpoint, masters[index], request,
                                              publishers[index])
                        assert status != CSR_SMOKE_FAILED
                        if status == CSR_SMOKE_PASSED:
                            irq_monitors[index].cancel()
                            endpoint.request_stop()
                            finished.add(index)
                    state = endpoint.state()
                    assert state.run_state not in (RunState.ERROR, RunState.COMPLETED)
                if len(finished) == 2:
                    break
            else:
                raise AssertionError("two IRQ firmware instances did not complete")
            for endpoint in endpoints:
                await wait_for_stop(endpoint, dut)

        for index, master in enumerate(masters):
            assert publishers[index].seen_high
            assert publishers[index].seen_low_after_high
            assert await read_word(master, status_address) == CSR_SMOKE_PASSED
            assert await read_word(master, boot_image.symbol_address("iss_trap_fault_pc")) == 0
            entries = await read_word(master, boot_image.symbol_address("iss_irq_entries"))
            returns = await read_word(master, boot_image.symbol_address("iss_irq_returns"))
            assert entries > 0 and entries == returns
        expected = [
            (word, 0x3 if index == len(AXIS_LOOPBACK_WORDS) - 1 else 0xF,
             index == len(AXIS_LOOPBACK_WORDS) - 1)
            for index, word in enumerate(AXIS_LOOPBACK_WORDS)
        ]
        assert transfers == [expected, expected]
    finally:
        for monitor in monitors + irq_monitors:
            monitor.cancel()


@cocotb.test()
async def test_spike_endpoints_exchange_request_reply(dut):
    cocotb.start_soon(Clock(dut.clk, 10, unit="ns").start())
    masters = [
        AxiLiteMaster(AxiLiteBus.from_prefix(entity, prefix), dut.clk, dut.rst)
        for entity, prefix in ((dut, "iss_axil"), (dut.g_dual, "iss1_axil"))
    ]
    dut.rst.value = 1
    for _ in range(5):
        await RisingEdge(dut.clk)
    dut.rst.value = 0

    boot_image = load_elf(os.environ["OPENENOC_LINK_FIRMWARE_ELF"])
    status_address = boot_image.symbol_address("iss_link_status")
    received_address = boot_image.symbol_address("iss_link_received")
    release_address = boot_image.symbol_address("iss_link_release")
    for index, master in enumerate(masters):
        await write_word(master, DMEM_BASE + 0x4000, 0x12340000 + index)
        await write_word(master, CSR_BASE, index + 1)
        assert await read_word(master, status_address) == 0

    transfers = [[[], []] for _ in masters]
    monitors = [
        cocotb.start_soon(collect_axis_transfers(entity, prefix, stream, dut.clk))
        for index, entity in enumerate((dut, dut.g_dual))
        for prefix, stream in (
            (("endpoint_tx" if index == 0 else "endpoint1_tx"), transfers[index][0]),
            (("endpoint_csr_sink" if index == 0 else "endpoint1_csr_sink"),
             transfers[index][1]),
        )
    ]
    request_counts = [0, 0]

    async def run_firmware(index, endpoint):
        for _ in range(FIRMWARE_TIMEOUT_CYCLES):
            await RisingEdge(dut.clk)
            request = endpoint.poll()
            if request is not None:
                request_counts[index] += 1
                status_write = (
                    request.kind == RequestKind.DATA_WRITE
                    and request.address == status_address
                    and request.size_bytes == 4
                )
                status = request_value(request) if status_write else None
                await service_request(endpoint, masters[index], request)
                assert status != CSR_SMOKE_FAILED, f"endpoint {index} firmware failed"
                if status == 0x600D0001 + index:
                    endpoint.request_stop()
                    await wait_for_stop(endpoint, dut)
                    return
            state = endpoint.state()
            assert state.run_state not in (RunState.ERROR, RunState.COMPLETED)
        raise AssertionError(f"endpoint {index} firmware timed out")

    runners = []
    try:
        async with AsyncExitStack() as stack:
            library = IssLibrary(os.environ["OPENENOC_ISS_LIBRARY"])
            endpoints = [
                stack.enter_context(library.create_endpoint(index))
                for index in range(len(masters))
            ]
            masters[0].read_if.ar_channel.pause = True
            for endpoint in endpoints:
                load_boot_image(endpoint, boot_image)
                endpoint.start(entry_pc=boot_image.entry_pc, max_steps=1_000_000)
            runners = [
                cocotb.start_soon(run_firmware(index, endpoint))
                for index, endpoint in enumerate(endpoints)
            ]
            stack.push_async_callback(stop_firmware_tasks, endpoints, runners, dut)
            await Timer(1000, unit="ns")
            assert endpoints[0].state().run_state == RunState.WAITING_MMIO
            assert request_counts[1] > request_counts[0]
            masters[0].read_if.ar_channel.pause = False
            for _ in range(FIRMWARE_TIMEOUT_CYCLES):
                await RisingEdge(dut.clk)
                if len(transfers[0][0]) == len(LINK_REQUEST_PREFIX):
                    break
            else:
                raise AssertionError("Initiator did not send the request prefix")
            assert transfers[0][0] == list(LINK_REQUEST_PREFIX)
            assert await read_word(masters[0], release_address) == 0
            await write_word(masters[0], release_address, 1)
            for runner in runners:
                await with_timeout(runner, 1_000_000, "ns")
    finally:
        masters[0].read_if.ar_channel.pause = False
        for runner in runners:
            if not runner.done():
                runner.cancel()
        for monitor in monitors:
            monitor.cancel()

    for index, master in enumerate(masters):
        assert transfers[index] == (
            [list(LINK_REQUEST_FRAME), list(LINK_REPLY_FRAME)] if index == 0
            else [list(LINK_REPLY_FRAME), list(LINK_REQUEST_FRAME)]
        )
        assert await read_word(master, status_address) == 0x600D0001 + index
        assert await read_word(master, received_address) == (
            0x2468ACE0 if index == 0 else 0x13579BDF
        )
        assert await read_word(master, DMEM_BASE + 0x4000) == 0x12340000 + index
    assert int(dut.imem_active.value) == 0
    assert int(dut.g_dual.endpoint1_imem_active.value) == 0


@cocotb.test()
async def test_spike_recovers_after_mid_frame_stop(dut):
    cocotb.start_soon(Clock(dut.clk, 10, unit="ns").start())
    masters = [
        AxiLiteMaster(AxiLiteBus.from_prefix(entity, prefix), dut.clk, dut.rst)
        for entity, prefix in ((dut, "iss_axil"), (dut.g_dual, "iss1_axil"))
    ]
    dut.rst.value = 1
    for _ in range(5):
        await RisingEdge(dut.clk)
    dut.rst.value = 0

    image = load_elf(os.environ["OPENENOC_LINK_FIRMWARE_ELF"])
    status_address = image.symbol_address("iss_link_status")
    release_address = image.symbol_address("iss_link_release")
    tx_transfers = []
    sink_transfers = []
    monitors = [
        cocotb.start_soon(collect_axis_transfers(dut, "endpoint_tx", tx_transfers)),
        cocotb.start_soon(collect_axis_transfers(
            dut.g_dual, "endpoint1_csr_sink", sink_transfers, dut.clk,
        )),
    ]
    runners = []

    async def pump(index, endpoint):
        for _ in range(FIRMWARE_TIMEOUT_CYCLES):
            await RisingEdge(dut.clk)
            request = endpoint.poll()
            if request is not None:
                status_write = (
                    request.kind == RequestKind.DATA_WRITE
                    and request.address == status_address
                    and request.size_bytes == 4
                )
                status = request_value(request) if status_write else None
                await service_request(endpoint, masters[index], request)
                assert status != CSR_SMOKE_FAILED
                if status == 0x600D0001 + index:
                    endpoint.request_stop()
            state = endpoint.state()
            assert state.run_state != RunState.ERROR
            if state.run_state == RunState.STOPPED:
                return
        raise AssertionError(f"endpoint {index} did not stop")

    try:
        async with AsyncExitStack() as stack:
            library = IssLibrary(os.environ["OPENENOC_ISS_LIBRARY"])
            endpoints = [
                stack.enter_context(library.create_endpoint(index))
                for index in range(2)
            ]
            for endpoint in endpoints:
                load_boot_image(endpoint, image)

            for index, master in enumerate(masters):
                await write_word(master, CSR_BASE, index + 1)
            for endpoint in endpoints:
                endpoint.start(entry_pc=image.entry_pc, max_steps=1_000_000)
            runners = [
                cocotb.start_soon(pump(index, endpoint))
                for index, endpoint in enumerate(endpoints)
            ]
            stack.push_async_callback(stop_firmware_tasks, endpoints, runners, dut)

            for _ in range(FIRMWARE_TIMEOUT_CYCLES):
                await RisingEdge(dut.clk)
                if len(sink_transfers) == len(LINK_REQUEST_PREFIX):
                    break
            else:
                raise AssertionError("Request prefix did not reach endpoint 1")
            prefix = list(LINK_REQUEST_PREFIX)
            assert tx_transfers == prefix
            assert sink_transfers == prefix
            assert await read_word(masters[0], release_address) == 0
            endpoints[0].request_stop()
            await wait_for_stop(endpoints[0], dut)
            assert endpoints[1].state().run_state != RunState.STOPPED
            for _ in range(100):
                await RisingEdge(dut.clk)
            assert tx_transfers == prefix
            assert sink_transfers == prefix
            assert await read_word(masters[1], status_address) == 0
            endpoints[1].request_stop()
            await wait_for_stop(endpoints[1], dut)
            for runner in runners:
                await with_timeout(runner, AXI_SERVICE_TIMEOUT_NS, "ns")
            runners = []

            dut.rst.value = 1
            for _ in range(5):
                await RisingEdge(dut.clk)
            dut.rst.value = 0
            for _ in range(20):
                await RisingEdge(dut.clk)
            assert tx_transfers == prefix
            assert sink_transfers == prefix

            for index, master in enumerate(masters):
                await write_word(master, CSR_BASE, index + 1)
            for endpoint in endpoints:
                endpoint.start(entry_pc=image.entry_pc, max_steps=1_000_000)
            runners = [
                cocotb.start_soon(pump(index, endpoint))
                for index, endpoint in enumerate(endpoints)
            ]
            stack.push_async_callback(stop_firmware_tasks, endpoints, runners, dut)
            for _ in range(FIRMWARE_TIMEOUT_CYCLES):
                await RisingEdge(dut.clk)
                if len(tx_transfers) == 2 * len(prefix):
                    break
            else:
                raise AssertionError("Restarted initiator did not send a request")
            assert tx_transfers[len(prefix):] == prefix
            await write_word(masters[0], release_address, 1)
            for runner in runners:
                await with_timeout(runner, 1_000_000, "ns")

            assert tx_transfers == prefix + list(LINK_REQUEST_FRAME)
            assert sink_transfers == tx_transfers
            for index, master in enumerate(masters):
                assert await read_word(master, status_address) == 0x600D0001 + index
    finally:
        for runner in runners:
            if not runner.done():
                runner.cancel()
        for monitor in monitors:
            monitor.cancel()


@cocotb.test()
async def test_spike_stops_one_endpoint_without_stopping_other(dut):
    cocotb.start_soon(Clock(dut.clk, 10, unit="ns").start())
    master = AxiLiteMaster(
        AxiLiteBus.from_prefix(dut.g_dual, "iss1_axil"), dut.clk, dut.rst
    )
    dut.rst.value = 1
    for _ in range(5):
        await RisingEdge(dut.clk)
    dut.rst.value = 0

    image = struct.pack(
        "<5I", 0x100000B7, 0x02A00113, 0x0020A023, 0x0000A183, 0x00118213,
    )
    library = IssLibrary(os.environ["OPENENOC_ISS_LIBRARY"])
    with ExitStack() as stack:
        local_endpoint = stack.enter_context(library.create_endpoint(0))
        active_endpoint = stack.enter_context(library.create_endpoint(1))
        local_endpoint.load_image(struct.pack("<I", 0x0000006F))
        active_endpoint.load_image(image)
        local_endpoint.start(entry_pc=0, max_steps=1_000_000)
        active_endpoint.start(entry_pc=0, max_steps=5)

        for _ in range(EXECUTION_TIMEOUT_CYCLES):
            await RisingEdge(dut.clk)
            request = active_endpoint.poll()
            if request is not None:
                break
        else:
            raise AssertionError("Endpoint 1 did not issue its write")
        assert request.endpoint_id == 1
        assert request.kind == RequestKind.DATA_WRITE
        assert local_endpoint.state().run_state == RunState.RUNNING
        local_endpoint.request_stop()
        await wait_for_stop(local_endpoint, dut)
        assert active_endpoint.state().run_state == RunState.WAITING_MMIO

        await service_request(active_endpoint, master, request)
        for _ in range(EXECUTION_TIMEOUT_CYCLES):
            await RisingEdge(dut.clk)
            request = active_endpoint.poll()
            if request is not None:
                await service_request(active_endpoint, master, request)
            if active_endpoint.state().run_state == RunState.COMPLETED:
                break
        else:
            raise AssertionError("Endpoint 1 stopped with endpoint 0")
        assert active_endpoint.read_register(3) == 42
        assert active_endpoint.read_register(4) == 43

    assert await read_word(master, DMEM_BASE) == 42
    assert int(dut.imem_active.value) == 0
    assert int(dut.g_dual.endpoint1_imem_active.value) == 0


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
        segment.virtual_address <= initialized_address
        and initialized_address + len(STARTUP_INITIALIZED_WORDS) * 4
        <= segment.virtual_address + len(segment.data)
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
