# SPDX-FileCopyrightText: 2026 Kerim Bavcic
# SPDX-License-Identifier: AGPL-3.0-or-later

from pathlib import Path

import cocotb
import cocotb_test.simulator
from cocotb.clock import Clock
from cocotb.triggers import FallingEdge, RisingEdge, Timer


# ----------------------------------------------------------------------
# Testbench helpers: drive CSR commands and sample stream handshakes
# ----------------------------------------------------------------------


class TB:
    def __init__(self, dut):
        self.d = dut
        self.outputs = []
        self.inputs = []
        self.state = dict(
            rst=0, tx_frame_done=0, tx_valid=0, tx_last=0, tx_data=0, tx_keep=15,
            tx_event_enable=0, rx_ready=0, m_ready=1, s_valid=0, s_last=0,
            s_data=0, s_keep=15, tx_admit_ready=0, tx_admit_reserved=0,
            tx_commit_ready=0, rx_admit_ready=0, rx_admit_reserved=0,
            rx_commit_ready=0,
        )
        dut.clk.value = 0
        for name, value in self.state.items():
            getattr(dut, name).value = value
        cocotb.start_soon(Clock(dut.clk, 10, unit="ns").start())

    def read(self):
        return {
            name: int(getattr(self.d, name).value)
            for name in (
                "tx_clear_valid", "tx_ready", "rx_clear_ready", "rx_valid",
                "rx_last", "rx_keep", "rx_data", "tx_admit_valid",
                "tx_admit_source", "tx_admit_enable", "tx_commit_valid",
                "tx_commit_source", "tx_commit_peer_idx", "rx_admit_valid",
                "rx_admit_source", "rx_admit_enable", "rx_commit_valid",
                "rx_commit_source", "rx_commit_peer_idx", "m_valid", "m_ready",
                "m_data", "m_keep", "m_strb", "m_last", "m_dest", "m_id",
                "m_user", "s_ready", "s_valid", "s_data", "s_keep", "s_last",
            )
        }

    async def step(self, **changes):
        """Sample transfers before the rising edge and CSR status after it."""
        self.state.update(changes)
        await FallingEdge(self.d.clk)
        for name, value in self.state.items():
            getattr(self.d, name).value = value
        await Timer(1, unit="ns")
        before = self.read()
        if before["m_valid"] and before["m_ready"]:
            self.outputs.append(tuple(before[n] for n in
                                      ("m_data", "m_keep", "m_strb", "m_last",
                                       "m_dest", "m_id", "m_user")))
        if before["s_valid"] and before["s_ready"]:
            self.inputs.append(tuple(before[n] for n in ("s_data", "s_keep", "s_last")))
        await RisingEdge(self.d.clk)
        await Timer(1, unit="ns")
        return before, self.read()

    async def wait(self, name, value=1, limit=24, **changes):
        for _ in range(limit):
            _, after = await self.step(**changes)
            if after[name] == value:
                return after
        assert False, f"{name} never became {value}"

    async def reset(self):
        for _ in range(3):
            await self.step(rst=1, tx_valid=0, s_valid=0, rx_ready=0,
                            tx_frame_done=0)
        _, after = await self.step(rst=0)
        assert after["tx_commit_valid"] == after["rx_commit_valid"] == 0
        assert after["tx_ready"] == after["rx_valid"] == 0

    async def tx_beat(self, data, keep, last):
        await self.wait("tx_clear_valid", tx_valid=1, tx_data=data,
                        tx_keep=keep, tx_last=int(last))
        await self.step(tx_valid=0)

    async def rx_beat(self, data, keep, last):
        for _ in range(16):
            before, _ = await self.step(s_valid=1, s_data=data,
                                        s_keep=keep, s_last=int(last))
            if before["s_ready"]:
                break
        else:
            assert False, "RX input register did not accept beat"
        await self.step(s_valid=0)
        visible = await self.wait("rx_valid", rx_ready=0)
        assert (visible["rx_data"], visible["rx_keep"], visible["rx_last"]) == (
            data, keep, int(last))
        await self.wait("rx_clear_ready", rx_ready=1)
        await self.step(rx_ready=0)


# ----------------------------------------------------------------------
# TX: CSR-to-stream framing and completion events
# ----------------------------------------------------------------------


@cocotb.test()
async def tx_reserved_framing_and_backpressure(dut):
    tb = TB(dut)
    await tb.reset()
    assert (await tb.step(tx_valid=1, tx_event_enable=1, m_ready=0))[1]["tx_ready"] == 0
    event = await tb.wait("tx_admit_valid")
    assert (event["tx_admit_source"], event["tx_admit_enable"]) == (3, 1)
    for _ in range(3):
        _, state = await tb.step()
        assert not state["tx_clear_valid"] and not state["m_valid"]
    await tb.step(tx_admit_ready=1, tx_admit_reserved=1)
    await tb.wait("tx_clear_valid", tx_admit_ready=0)
    await tb.step(tx_valid=0)
    await tb.tx_beat(0x12345678, 0x5, True)

    # Both beats are buffered while the sink is stalled.
    for _ in range(4):
        _, state = await tb.step()
        assert state["tx_ready"] == 0
        assert state["tx_commit_valid"] == 0
        assert state["m_valid"] == 1
        assert (state["m_data"], state["m_last"]) == (0, 0)
    assert tb.outputs == []
    await tb.step(m_ready=1)
    for _ in range(5):
        await tb.step()
    assert tb.outputs == [
        (0, 15, 15, 0, 0b100000, 0, 0),
        (0x12345678, 5, 5, 1, 0b100000, 0, 0),
    ]

    # Draining the local stream is not the downstream frame completion.
    await tb.step(tx_frame_done=1)
    event = await tb.wait("tx_commit_valid", tx_frame_done=0)
    assert (event["tx_commit_source"], event["tx_commit_peer_idx"]) == (3, 0)
    for _ in range(3):
        assert (await tb.step())[1]["tx_commit_valid"] == 1
    assert (await tb.step(tx_valid=1))[1]["tx_admit_valid"] == 0
    await tb.step(tx_valid=0, tx_commit_ready=1)
    assert (await tb.step(tx_commit_ready=0))[1]["tx_commit_valid"] == 0


@cocotb.test()
async def tx_unreserved_and_reset(dut):
    tb = TB(dut)
    await tb.reset()
    await tb.wait("tx_admit_valid", tx_valid=1, tx_event_enable=0,
                  tx_data=0xABCDEF12, tx_keep=3, tx_last=1)
    assert (await tb.step(tx_admit_ready=1, tx_admit_reserved=0))[1]["tx_ready"]
    await tb.wait("tx_clear_valid", tx_admit_ready=0)

    # Leave the CSR command asserted after its clear pulse to check for duplicates.
    for _ in range(3):
        state = (await tb.step())[1]
        assert state["tx_clear_valid"] == 0
    await tb.step(tx_valid=0)
    for _ in range(4):
        await tb.step()
    assert tb.outputs == [(0xABCDEF12, 3, 3, 1, 0b100000, 0, 0)]
    await tb.step(tx_frame_done=1)
    assert (await tb.step(tx_frame_done=0))[1]["tx_commit_valid"] == 0
    await tb.wait("tx_admit_valid", tx_valid=1, tx_event_enable=1)
    await tb.step(tx_admit_ready=1, tx_admit_reserved=1)
    await tb.step(tx_admit_ready=0, tx_valid=0)
    await tb.step(tx_frame_done=1)
    assert (await tb.step(tx_frame_done=0))[1]["tx_commit_valid"] == 1
    await tb.reset()
    assert (await tb.step())[1]["tx_admit_valid"] == 0


# ----------------------------------------------------------------------
# RX: stream-to-CSR delivery and availability events
# ----------------------------------------------------------------------


@cocotb.test()
async def rx_admission_framing_and_commit(dut):
    tb = TB(dut)
    await tb.reset()
    await tb.step(rx_admit_ready=0)
    await tb.step(s_valid=1, s_data=0xA1B2C3D4, s_keep=15, s_last=0)
    await tb.step(s_valid=0)
    event = await tb.wait("rx_admit_valid")
    assert (event["rx_admit_source"], event["rx_admit_enable"]) == (4, 1)

    # The input slice can accept a beat before IRQ admission makes it visible.
    for _ in range(3):
        _, state = await tb.step()
        assert not state["rx_valid"] and not state["rx_clear_ready"]
    await tb.step(rx_admit_ready=1, rx_admit_reserved=1)
    event = (await tb.step(rx_admit_ready=0))[1]
    assert (event["rx_commit_valid"], event["rx_commit_source"],
            event["rx_commit_peer_idx"]) == (1, 4, 0)
    visible = await tb.wait("rx_valid")
    assert (visible["rx_data"], visible["rx_keep"], visible["rx_last"]) == (
        0xA1B2C3D4, 15, 0)
    await tb.wait("rx_clear_ready", rx_ready=1)
    await tb.step(rx_ready=0)
    assert (await tb.step())[1]["rx_commit_valid"] == 1
    await tb.rx_beat(0x12345678, 3, True)
    assert tb.inputs == [(0xA1B2C3D4, 15, 0), (0x12345678, 3, 1)]
    await tb.step(rx_commit_ready=1)
    assert (await tb.step(rx_commit_ready=0))[1]["rx_commit_valid"] == 0


@cocotb.test()
async def rx_unreserved_backpressure_and_reset(dut):
    tb = TB(dut)
    await tb.reset()
    await tb.step(s_valid=1, s_data=0xDEADBEEF, s_keep=8, s_last=1)
    await tb.step(s_valid=0)
    await tb.wait("rx_admit_valid")
    await tb.step(rx_admit_ready=1, rx_admit_reserved=0)
    await tb.step(rx_admit_ready=0)
    for _ in range(4):
        state = (await tb.step())[1]
        assert state["rx_commit_valid"] == 0
        assert state["rx_valid"] == 1
        assert (state["rx_data"], state["rx_keep"], state["rx_last"]) == (
            0xDEADBEEF, 8, 1)
    await tb.wait("rx_clear_ready", rx_ready=1)
    await tb.step(rx_ready=0)
    await tb.step(s_valid=1, s_data=0x56789ABC, s_keep=1, s_last=1)
    await tb.step(s_valid=0)
    await tb.wait("rx_admit_valid")
    await tb.step(rx_admit_ready=1, rx_admit_reserved=1)
    await tb.step(rx_admit_ready=0)
    assert (await tb.step())[1]["rx_commit_valid"] == 1
    await tb.reset()
    assert (await tb.step())[1]["rx_valid"] == 0


# ----------------------------------------------------------------------
# Pytest runner: production direct-route configuration
# ----------------------------------------------------------------------

tests_dir = Path(__file__).resolve().parent
repo_dir = tests_dir.parents[2]
core_dir = repo_dir / "hw/rtl/core"
hal_dir = repo_dir / "build/hal/rtl"
taxi_axis_dir = repo_dir / "libs/taxi/src/axis/rtl"


def test_openenoc_endpoint_direct_axis(sim_build_dir, sim_trace_args):
    module = Path(__file__).stem
    verilog_sources = [
        hal_dir / "openenoc_endpoint_if.sv",
        taxi_axis_dir / "taxi_axis_if.sv",
        taxi_axis_dir / "taxi_axis_register.sv",
        core_dir / "openenoc_irq_event_if.sv",
        core_dir / "openenoc_endpoint_direct_axis.sv",
        tests_dir / f"{module}.sv",
    ]

    cocotb_test.simulator.run(
        simulator="verilator",
        python_search=[str(tests_dir)],
        verilog_sources=[str(path) for path in verilog_sources],
        toplevel=module,
        module=module,
        timescale="1ns/1ps",
        extra_args=["-Wall", str(repo_dir / "dv/common/config.vlt")],
        plus_args=sim_trace_args,
        sim_build=sim_build_dir,
    )
