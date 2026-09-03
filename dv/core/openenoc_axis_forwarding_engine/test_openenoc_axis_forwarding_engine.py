# SPDX-FileCopyrightText: 2026 Kerim Bavcic
# SPDX-License-Identifier: AGPL-3.0-or-later

import itertools
import logging
import os

import cocotb
import cocotb_test.simulator
import pytest
from cocotb.clock import Clock
from cocotb.regression import TestFactory
from cocotb.triggers import RisingEdge, Timer
TestFactory.__test__ = False

from cocotbext.axi import AxiStreamBus, AxiStreamFrame, AxiStreamSource, AxiStreamSink


STATION_MAC = 0x020E0C000010
OETP_ETHERTYPE = 0x88B5
OETP_MAGIC = 0xA0
OETP_COMMAND = 0x01


# ----------------------------------------------------------------------
# Helper functions for test frame generation
# ----------------------------------------------------------------------

def mac_bytes(mac):
    return bytes((mac >> shift) & 0xff for shift in range(40, -1, -8))


def make_frame(da, sa, length=60):
    header = bytearray(
        mac_bytes(da)
        + mac_bytes(sa)
        + OETP_ETHERTYPE.to_bytes(2, "big")
        + bytes([OETP_MAGIC, OETP_COMMAND])
    )
    if length <= len(header):
        return header[:length]
    payload = itertools.islice(itertools.cycle(range(256)), length - len(header))
    return header + bytearray(payload)


def cycle_pause():
    return itertools.cycle([1, 1, 1, 0])


# ----------------------------------------------------------------------
# Standalone forwarding-table handshake model
# ----------------------------------------------------------------------

class ForwardingTableModel:
    """Standalone model of the forwarding table handshake only."""

    def __init__(self, tb, entries=None, default_bitmap=None,
                 lookup_latency=2, learning_latency=2):
        self.tb = tb
        self.dut = tb.dut
        self.entries = dict(entries or {})
        self.default_bitmap = tb.interface_mask if default_bitmap is None else default_bitmap
        self.lookup_latency = lookup_latency
        self.learning_latency = learning_latency
        self.lookups = []
        self.learnings = []

    def start(self):
        cocotb.start_soon(self._lookup_worker())
        cocotb.start_soon(self._learning_worker())

    async def _lookup_worker(self):
        while True:
            await self.tb.cycle()
            if self.dut.rst.value or not self.dut.lookup_if.req.value:
                continue

            mac = int(self.dut.lookup_if.mac_addr.value)
            self.lookups.append(mac)

            # Hold off the acknowledge long enough to verify that the engine
            # stalls its input and does not release output while lookup waits.
            for _ in range(self.lookup_latency):
                await self.tb.cycle()
                assert int(self.dut.lookup_if.mac_addr.value) == mac
                assert not self.dut.s_axis_if.tready.value
                assert not self.dut.m_axis_if.tvalid.value

            self.dut.lookup_if.port_bitmap.value = self.entries.get(mac, self.default_bitmap)
            self.dut.lookup_if.ack.value = 1
            await self.tb.cycle()
            self.dut.lookup_if.ack.value = 0
            self.dut.lookup_if.port_bitmap.value = 0

    async def _learning_worker(self):
        while True:
            await self.tb.cycle()
            if self.dut.rst.value or not self.dut.learning_if.req.value:
                continue

            mac = int(self.dut.learning_if.mac_addr.value)
            bitmap = int(self.dut.learning_if.port_bitmap.value)
            self.learnings.append((mac, bitmap))

            # No beat may enter or leave before learning is acknowledged, and
            # the request payload must remain stable throughout the wait.
            for _ in range(self.learning_latency):
                await self.tb.cycle()
                assert int(self.dut.learning_if.mac_addr.value) == mac
                assert int(self.dut.learning_if.port_bitmap.value) == bitmap
                assert not self.dut.s_axis_if.tready.value
                assert not self.dut.m_axis_if.tvalid.value

            self.dut.learning_if.ack.value = 1
            await self.tb.cycle()
            self.dut.learning_if.ack.value = 0


class TB:
    def __init__(self, dut):
        self.dut = dut
        self.log = logging.getLogger("cocotb.tb")
        self.log.setLevel(logging.DEBUG)

        cocotb.start_soon(Clock(dut.clk, 10, units="ns").start())

        self.source = AxiStreamSource(AxiStreamBus.from_entity(dut.s_axis_if), dut.clk, dut.rst)
        self.sink = AxiStreamSink(AxiStreamBus.from_entity(dut.m_axis_if), dut.clk, dut.rst)

        self.num_interfaces = len(dut.lookup_if.port_bitmap)
        self.interface_mask = (1 << self.num_interfaces) - 1

        dut.pause_request.setimmediatevalue(0)
        dut.lookup_if.ack.setimmediatevalue(0)
        dut.lookup_if.port_bitmap.setimmediatevalue(0)
        dut.learning_if.ack.setimmediatevalue(0)

    def set_idle_generator(self, generator=None):
        if generator:
            self.source.set_pause_generator(generator())

    def set_backpressure_generator(self, generator=None):
        if generator:
            self.sink.set_pause_generator(generator())

    async def cycle(self, count=1):
        for _ in range(count):
            await RisingEdge(self.dut.clk)
            await Timer(1, units="ns")

    async def reset(self):
        self.dut.rst.setimmediatevalue(0)
        await self.cycle(2)
        self.dut.rst.value = 1
        await self.cycle(2)
        self.dut.rst.value = 0
        await self.cycle(2)

# ----------------------------------------------------------------------
# Standalone cocotb test cases
# ----------------------------------------------------------------------

@cocotb.test()
async def test_incomplete_destination_address_sets_zero_bitmap(dut):
    """Frames ending before the complete DA are not looked up or learned."""
    tb = TB(dut)
    await tb.reset()

    ingress = min(2, tb.num_interfaces - 1)
    model = ForwardingTableModel(tb, default_bitmap=tb.interface_mask)
    model.start()

    frames = []
    for length in range(1, 6):
        frame = AxiStreamFrame(make_frame(STATION_MAC + 0x30, 0, length))
        frame.tid = ingress
        frame.tdest = length
        frames.append(frame)
        await tb.source.send(frame)

    for expected in frames:
        received = await tb.sink.recv()
        assert received.tdata == expected.tdata
        assert received.tid == ingress
        assert received.tdest == expected.tdest
        assert received.tuser == 0

    await tb.cycle(16)

    assert model.lookups == []
    assert model.learnings == []
    assert tb.sink.empty()


@cocotb.test()
async def test_incomplete_source_address_sets_zero_bitmap(dut):
    """Frames with a complete DA but incomplete SA are not routed or learned."""
    tb = TB(dut)
    await tb.reset()

    destination = STATION_MAC + 0x30
    ingress = min(2, tb.num_interfaces - 1)
    egress = (ingress + 1) % tb.num_interfaces
    model = ForwardingTableModel(
        tb,
        entries={destination: 1 << egress},
        lookup_latency=2,
        learning_latency=2,
    )
    model.start()

    frames = []
    for length in range(6, 12):
        frame = AxiStreamFrame(make_frame(destination, STATION_MAC + length, length))
        frame.tid = ingress
        frame.tdest = length
        frames.append(frame)
        await tb.source.send(frame)

    for expected in frames:
        received = await tb.sink.recv()
        assert received.tdata == expected.tdata
        assert received.tid == ingress
        assert received.tdest == expected.tdest
        assert received.tuser == 0

    await tb.cycle(16)

    assert model.lookups == [destination] * len(frames)
    assert model.learnings == []
    assert tb.sink.empty()

# ----------------------------------------------------------------------
# TestFactory logic: idle and backpressure combinations
# ----------------------------------------------------------------------

async def run_test_factory_lookup_learning_and_forwarding( dut, idle_inserter=None, backpressure_inserter=None, handshake_latency=2):
    """Basic data path, MAC parsing, request payloads and tuser assignment."""

    tb = TB(dut)
    await tb.reset()

    tb.set_idle_generator(idle_inserter)
    tb.set_backpressure_generator(backpressure_inserter)

    known_da = STATION_MAC + 0x20
    unknown_da = STATION_MAC + 0x21
    ingress = min(2, tb.num_interfaces - 1)
    known_egress = min(3, tb.num_interfaces - 1)
    known_bitmap = 1 << known_egress
    default_bitmap = tb.interface_mask

    model = ForwardingTableModel(
        tb,
        entries={known_da: known_bitmap},
        default_bitmap=default_bitmap,
        lookup_latency=handshake_latency,
        learning_latency=handshake_latency,
    )
    model.start()

    # Each tuple contains:
    # (destination MAC, source MAC, ingress port index carried by TID,
    #  total frame length in bytes).
    frames = [
        (known_da, STATION_MAC + 1, ingress, 60),
        (unknown_da, STATION_MAC + 2, 0, 79),
        (known_da, STATION_MAC + 3, min(1, tb.num_interfaces - 1), 128),
        (known_da, STATION_MAC + 4, 0, 32),
    ]

    for index, (da, sa, port, length) in enumerate(frames):
        frame = AxiStreamFrame(make_frame(da, sa, length))
        frame.tid = port
        frame.tdest = index + 10
        await tb.source.send(frame)

    for index, (da, _sa, port, length) in enumerate(frames):
        rx_frame = await tb.sink.recv()
        expected_lookup = model.entries.get(da, model.default_bitmap)
        expected_bitmap = expected_lookup & ~(1 << port) & tb.interface_mask

        assert rx_frame.tdata == make_frame(da, frames[index][1], length)
        assert rx_frame.tid == port
        assert rx_frame.tdest == index + 10
        assert rx_frame.tuser == expected_bitmap

    await tb.cycle(16)

    assert model.lookups == [item[0] for item in frames]
    # Every complete source address is learned.
    assert model.learnings == [(sa, 1 << port) for _, sa, port, _ in frames]
    assert tb.sink.empty()

# ----------------------------------------------------------------------
# Dispatch: select test cases to run based on Makefile configuration
# ----------------------------------------------------------------------

if getattr(cocotb, "top", None) is not None:
    factory = TestFactory(run_test_factory_lookup_learning_and_forwarding)
    factory.add_option("idle_inserter", [None, cycle_pause])
    factory.add_option("backpressure_inserter", [None, cycle_pause])
    factory.add_option("handshake_latency", [2, 4, 256])
    factory.generate_tests()


# ----------------------------------------------------------------------
# PyTest framework: parameter sweep and simulator runner
# ----------------------------------------------------------------------

tests_dir = os.path.dirname(__file__)
repo_dir = os.path.abspath(os.path.join(tests_dir, "..", "..", ".."))
hw_dir = os.path.join(repo_dir, "hw")
libs_dir = os.path.join(repo_dir, "libs")
core_dir = os.path.join(hw_dir, "rtl", "core")
taxi_axis_dir = os.path.join(libs_dir, "taxi", "src", "axis", "rtl")
common_dir = os.path.abspath(os.path.join(tests_dir, "..", "..", "common"))


def process_f_files(files):
    sources = {}
    for source in files:
        if source[-2:].lower() == ".f":
            with open(source, "r", encoding="utf-8") as file_list:
                nested_sources = file_list.read().split()
            nested_sources = [
                os.path.join(os.path.dirname(source), item)
                for item in nested_sources
            ]
            for nested_source in process_f_files(nested_sources):
                sources[os.path.basename(nested_source)] = nested_source
        else:
            sources[os.path.basename(source)] = source
    return list(sources.values())


@pytest.mark.parametrize("data_w", [8, 16, 24, 64, 128, 512])
def test_openenoc_axis_forwarding_engine(request, data_w):
    dut = "openenoc_axis_forwarding_engine"
    module = os.path.splitext(os.path.basename(__file__))[0]
    toplevel = module

    verilog_sources = [
        os.path.join(tests_dir, f"{toplevel}.sv"),
        os.path.join(core_dir, "openenoc_lookup_if.sv"),
        os.path.join(core_dir, "openenoc_learning_if.sv"),
        os.path.join(core_dir, f"{dut}.sv"),
        os.path.join(taxi_axis_dir, "taxi_axis_pipeline_register.sv"),
        os.path.join(taxi_axis_dir, "taxi_axis_register.sv"),
        os.path.join(taxi_axis_dir, "taxi_axis_if.sv"),
    ]
    verilog_sources = process_f_files(verilog_sources)

    parameters = {
        "NUM_OF_INTERFACES": 8,
        "DATA_W": data_w,
        "KEEP_EN": int(data_w > 8),
        "KEEP_W": (data_w + 7) // 8,
        "STRB_EN": 0,
        "LAST_EN": 1,
        "ID_EN": 1,
        "ID_W": 8,
        "DEST_EN": 1,
        "DEST_W": 8,
        "USER_EN": 1,
        "USER_W": 8,
    }

    extra_env = {f"PARAM_{key}": str(value) for key, value in parameters.items()}
    sim_build = os.path.join(
        tests_dir,
        "sim_build",
        request.node.name.replace("[", "-").replace("]", ""),
    )

    cocotb_test.simulator.run(
        simulator="verilator",
        python_search=[tests_dir],
        verilog_sources=verilog_sources,
        toplevel=toplevel,
        module=module,
        parameters=parameters,
        extra_args=[
            "-Wall",
            os.path.join(common_dir, "config.vlt"),
        ],
        sim_build=sim_build,
        extra_env=extra_env,
    )
