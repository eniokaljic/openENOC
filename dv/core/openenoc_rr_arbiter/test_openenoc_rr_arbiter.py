# SPDX-FileCopyrightText: 2026 Kerim Bavcic
# SPDX-License-Identifier: AGPL-3.0-or-later

import os
import random

import cocotb
import cocotb_test.simulator
import pytest
from cocotb.clock import Clock
from cocotb.triggers import FallingEdge, RisingEdge, Timer


# ----------------------------------------------------------------------
# Testbench helpers: compare grants against a round-robin model
# ----------------------------------------------------------------------


class TB:
    def __init__(self, dut):
        self.dut = dut
        self.ports = len(dut.request)
        self.pointer = 0
        self.mask = (1 << self.ports) - 1

    async def reset(self):
        dut = self.dut
        dut.clk.value = 0
        dut.rst.value = 1
        dut.request.value = 0
        dut.accept.value = 0
        cocotb.start_soon(Clock(dut.clk, 10, unit="ns").start())
        for _ in range(2):
            await RisingEdge(dut.clk)
        await FallingEdge(dut.clk)
        dut.rst.value = 0
        self.pointer = 0
        await Timer(1, unit="ns")
        self.check(0)

    def expected(self, requests):
        for offset in range(self.ports):
            index = (self.pointer + offset) % self.ports
            if requests & (1 << index):
                return 1 << index, 1, index
        # With no grant, the index still exposes the current priority.
        return 0, 0, self.pointer

    def check(self, requests):
        dut = self.dut
        actual = (
            int(dut.grant.value),
            int(dut.grant_valid.value),
            int(dut.grant_index.value),
        )
        expected = self.expected(requests)
        assert actual == expected, (
            f"ports={self.ports} pointer={self.pointer} requests={requests:#x}: "
            f"got {actual}, expected {expected}"
        )

    async def cycle(self, requests, accept):
        """Check the combinational winner before and after the acceptance edge."""
        dut = self.dut
        await FallingEdge(dut.clk)
        dut.request.value = requests
        dut.accept.value = int(accept)
        await Timer(1, unit="ns")
        self.check(requests)
        grant, valid, index = self.expected(requests)
        await RisingEdge(dut.clk)
        if accept and valid:
            self.pointer = (index + 1) % self.ports
        await Timer(1, unit="ns")
        self.check(requests)
        return grant


# ----------------------------------------------------------------------
# Arbitration tests: idle, reset, priority, and fairness
# ----------------------------------------------------------------------


@cocotb.test()
async def test_idle_accept_and_reset(dut):
    tb = TB(dut)
    await tb.reset()
    await tb.cycle(0, True)
    await tb.cycle(1 << (tb.ports - 1), False)
    await tb.cycle(0, True)
    await tb.cycle(tb.mask, True)
    await tb.cycle(0, True)

    await FallingEdge(dut.clk)
    dut.rst.value = 1
    await RisingEdge(dut.clk)
    tb.pointer = 0
    await Timer(1, unit="ns")
    tb.check(0)
    await FallingEdge(dut.clk)
    dut.rst.value = 0
    await tb.cycle(tb.mask, False)


@cocotb.test()
async def test_priority_for_every_request_mask(dut):
    tb = TB(dut)
    await tb.reset()
    # Sweep smaller configurations exhaustively; sample masks for eight ports.
    masks = range(tb.mask + 1) if tb.ports <= 5 else range(256)
    rng = random.Random(0xA8B1)
    for mask in masks:
        requests = mask if tb.ports <= 5 else rng.randrange(tb.mask + 1)
        await tb.cycle(requests, False)
        await tb.cycle(requests, True)
        await tb.cycle(requests, False)


@cocotb.test()
async def test_rotation_and_fairness(dut):
    tb = TB(dut)
    await tb.reset()
    for _ in range(3):
        for index in range(tb.ports):
            assert await tb.cycle(tb.mask, False) == 1 << index
            assert await tb.cycle(tb.mask, True) == 1 << index

    if tb.ports > 2:
        # Requests at the ends of the vector exercise skipping and wraparound.
        requests = (1 << 0) | (1 << (tb.ports - 1))
        for _ in range(4):
            await tb.cycle(requests, True)
            await tb.cycle(requests, False)


# ----------------------------------------------------------------------
# Pytest runner: sweep the number of requester ports
# ----------------------------------------------------------------------

tests_dir = os.path.dirname(__file__)
repo_dir = os.path.abspath(os.path.join(tests_dir, "..", "..", ".."))
core_dir = os.path.join(repo_dir, "hw", "rtl", "core")
common_dir = os.path.join(repo_dir, "dv", "common")


@pytest.mark.parametrize("ports", [1, 2, 3, 4, 5, 8])
def test_openenoc_rr_arbiter(sim_build_dir, sim_trace_args, ports):
    module = os.path.splitext(os.path.basename(__file__))[0]
    verilog_sources = [
        os.path.join(tests_dir, f"{module}.sv"),
        os.path.join(core_dir, "openenoc_rr_arbiter.sv"),
    ]

    cocotb_test.simulator.run(
        simulator="verilator",
        python_search=[tests_dir],
        verilog_sources=verilog_sources,
        toplevel=module,
        module=module,
        parameters={"PORTS": ports},
        timescale="1ns/1ps",
        extra_args=["-Wall", os.path.join(common_dir, "config.vlt")],
        plus_args=sim_trace_args,
        sim_build=sim_build_dir,
        extra_env={"PARAM_PORTS": str(ports)},
    )
