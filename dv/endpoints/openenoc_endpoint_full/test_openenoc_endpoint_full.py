# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: AGPL-3.0-or-later

import os

import pytest
import cocotb
import cocotb_test.simulator
from cocotb.clock import Clock
from cocotb.triggers import FallingEdge, RisingEdge
from cocotb.regression import TestFactory

TestFactory.__test__ = False

CSR_SMOKE_PATTERN = 0xA5A55A5A
CSR_SMOKE_PASSED = 0x600D600D
CSR_SMOKE_FAILED = 0xBAD0BAD0
SWITCH_DEFAULT_FORWARDING = 0xA
EXECUTION_TIMEOUT_CYCLES = 60000
ENDPOINT_CPU_IRQ_MASK = 1 << 3
AXIS_LOOPBACK_WORDS = [
    0xFFFFFFFF,
    0x0122FFFF,
    0x89ABCDEF,
    0xFFFFFFFF,
    0xA5A55A5A,
    0x5A5AA5A5,
    0x00000001,
    0x80000000,
    0x11111111,
    0x22222222,
    0x33333333,
    0x44444444,
    0xDEADBEEF,
    0xC001D00D,
    0x13579BDF,
    0x2468ACE0,
    0x0000BEEF,
]
AXIS_LOOPBACK_FULL_KEEP = 0xF
AXIS_LOOPBACK_LAST_KEEP = 0x3


def signal_integer(signal):
    return int(signal.value)


def assert_reserved_interfaces_inactive(dut):
    assert signal_integer(dut.reserved_masters_inactive) == 1
    assert signal_integer(dut.rmem_master_inactive) == 1
    assert signal_integer(dut.endpoint_mac_lo_hwif) == 0


def assert_csr_bridge_connected(dut):
    assert signal_integer(dut.switch_table_depth) == 8
    assert signal_integer(dut.switch_num_interfaces) == 4
    assert signal_integer(dut.switch_pause_done_hwif) == 1


def assert_switch_configuration(dut):
    assert signal_integer(dut.switch_operation_mode) == 1
    assert signal_integer(dut.switch_pause_request) == 1
    assert signal_integer(dut.switch_default_forwarding) == SWITCH_DEFAULT_FORWARDING


async def pause_loopback(dut):
    cycle = 0
    while True:
        await FallingEdge(dut.clk)
        # A beat already presented to the receiver remains valid until accepted.
        stalled = signal_integer(dut.eth_if.b2a_axis_if.tvalid) and not signal_integer(
            dut.eth_if.b2a_axis_if.tready
        )
        dut.loopback_pause.value = 0 if stalled else cycle % 31 < 13
        cycle += 1


@cocotb.test()
async def test_csr_smoke_firmware(dut):
    cocotb.start_soon(Clock(dut.clk, 10, unit="ns").start())

    dut.rst.value = 1
    dut.loopback_pause.value = 0
    if os.environ.get("LOOPBACK_STALLS", "0") == "1":
        cocotb.start_soon(pause_loopback(dut))

    for _ in range(5):
        await RisingEdge(dut.clk)
        assert signal_integer(dut.cpu_trap) == 0
        assert_reserved_interfaces_inactive(dut)
        assert_csr_bridge_connected(dut)

    with open(os.environ["PARAM_IMEM_INIT_FILE"], encoding="ascii") as source:
        expected_first_word = int(next(line for line in source if line.strip()), 16)

    assert signal_integer(dut.imem_word0) == expected_first_word
    assert signal_integer(dut.dmem_status) == 0
    assert signal_integer(dut.csr_test_value) == 0

    dut.rst.value = 0

    eth_transfers = []
    csr_sink_transfers = []
    completed_tokens = []
    irq_entries = 0
    previous_eoi = 0
    previous_claim_token = 0
    previous_complete_ack = 0
    rx_available_before_tlast = False
    backpressure_cycles = 0

    for execution_cycles in range(1, EXECUTION_TIMEOUT_CYCLES + 1):
        await RisingEdge(dut.clk)

        if signal_integer(dut.endpoint_tx_valid) and not signal_integer(dut.endpoint_tx_ready):
            backpressure_cycles += 1

        eoi = signal_integer(dut.cpu_eoi)
        assert eoi in (0, ENDPOINT_CPU_IRQ_MASK)
        assert signal_integer(dut.cpu_irq) == (
            ENDPOINT_CPU_IRQ_MASK if signal_integer(dut.endpoint_irq) else 0
        )
        assert not signal_integer(dut.irq_overflow)
        assert not signal_integer(dut.irq_invalid_complete)
        if eoi and not previous_eoi:
            irq_entries += 1
        previous_eoi = eoi
        token = signal_integer(dut.irq_claim_token)
        if token >> 31 and (token >> 11) & 0xF == 4:
            rx_available_before_tlast |= not any(last for _, _, last in eth_transfers)
        complete_ack = signal_integer(dut.irq_complete_hwclr)
        if complete_ack and not previous_complete_ack:
            assert signal_integer(dut.cpu_irq_active), "Claim was completed outside the ISR"
            # The registered acknowledgement accompanies the newly exposed queue head.
            assert signal_integer(dut.irq_complete_token) == previous_claim_token
            completed_tokens.append(previous_claim_token)
        previous_complete_ack = complete_ack
        previous_claim_token = token

        if signal_integer(dut.endpoint_tx_valid) and signal_integer(dut.endpoint_tx_ready):
            eth_transfers.append(
                (
                    signal_integer(dut.endpoint_tx_data),
                    signal_integer(dut.endpoint_tx_keep),
                    signal_integer(dut.endpoint_tx_last),
                )
            )

        if signal_integer(dut.endpoint_csr_sink_valid) and signal_integer(
            dut.endpoint_csr_sink_ready
        ):
            assert signal_integer(dut.cpu_irq_active), "RX payload was read outside the ISR"
            csr_sink_transfers.append(
                (
                    signal_integer(dut.endpoint_csr_sink_data),
                    signal_integer(dut.endpoint_csr_sink_keep),
                    signal_integer(dut.endpoint_csr_sink_last),
                )
            )

        assert signal_integer(dut.cpu_trap) == 0, "PicoRV32 entered trap state"
        assert_reserved_interfaces_inactive(dut)
        assert_csr_bridge_connected(dut)

        status = signal_integer(dut.dmem_status)
        assert status != CSR_SMOKE_FAILED, (
            "csr_smoke firmware reported failure; "
            f"ETH transfers={eth_transfers!r}, "
            f"CSR sink transfers={csr_sink_transfers!r}"
        )

        if status == CSR_SMOKE_PASSED:
            cocotb.log.info("csr_smoke completed in %d execution cycles", execution_cycles)
            break
    else:
        raise AssertionError(f"csr_smoke did not finish within {EXECUTION_TIMEOUT_CYCLES} cycles")

    assert signal_integer(dut.csr_test_value) == CSR_SMOKE_PATTERN
    assert_switch_configuration(dut)
    expected_transfers = [
        (
            word,
            (
                AXIS_LOOPBACK_LAST_KEEP
                if index == len(AXIS_LOOPBACK_WORDS) - 1
                else AXIS_LOOPBACK_FULL_KEEP
            ),
            index == len(AXIS_LOOPBACK_WORDS) - 1,
        )
        for index, word in enumerate(AXIS_LOOPBACK_WORDS)
    ]
    assert eth_transfers == expected_transfers
    assert csr_sink_transfers == expected_transfers
    assert rx_available_before_tlast, "RX notification waited for the complete frame"
    assert irq_entries >= 1, "CPU never entered its IRQ handler"
    assert [(token >> 11) & 0xF for token in completed_tokens] == [4, 3]
    assert [(token >> 15) & 0xFFFF for token in completed_tokens] == [0, 1]
    assert all(token & 0x7FF == 0 for token in completed_tokens)
    assert signal_integer(dut.cpu_irq_active) == 0, "retirq did not return to main"
    assert signal_integer(dut.endpoint_irq) == 0
    assert signal_integer(dut.irq_fifo_level) == 0
    assert signal_integer(dut.irq_reserved_count) == 0
    if os.environ.get("LOOPBACK_STALLS", "0") == "1":
        assert backpressure_cycles > 0, "Stalled loopback never applied backpressure"
    cocotb.log.info(
        "Observed %d CPU IRQ entries and %d Ethernet stall cycles", irq_entries, backpressure_cycles
    )

    # The firmware returns into its terminal loop; the result must remain stable.
    for _ in range(10):
        await RisingEdge(dut.clk)
        assert signal_integer(dut.dmem_status) == CSR_SMOKE_PASSED
        assert signal_integer(dut.csr_test_value) == CSR_SMOKE_PATTERN
        assert signal_integer(dut.cpu_trap) == 0
        assert_reserved_interfaces_inactive(dut)
        assert_csr_bridge_connected(dut)
        assert_switch_configuration(dut)


tests_dir = os.path.abspath(os.path.dirname(__file__))
repo_dir = os.path.abspath(os.path.join(tests_dir, "..", "..", ".."))
hw_dir = os.path.join(repo_dir, "hw")
libs_dir = os.path.join(repo_dir, "libs")
core_dir = os.path.join(hw_dir, "rtl", "core")
endpoint_dir = os.path.join(hw_dir, "rtl", "endpoints")
taxi_axi_dir = os.path.join(libs_dir, "taxi", "src", "axi", "rtl")
taxi_axis_dir = os.path.join(libs_dir, "taxi", "src", "axis", "rtl")
taxi_sync_dir = os.path.join(libs_dir, "taxi", "src", "sync", "rtl")
picorv32_dir = os.path.join(libs_dir, "picorv32")
hal_rtl_dir = os.path.join(repo_dir, "build", "hal", "openenoc_endpoint_full", "rtl")
hal_if_dir = os.path.join(repo_dir, "build", "hal", "rtl")
common_dir = os.path.join(repo_dir, "dv", "common")


def process_f_files(files):
    sources = {}

    for filename in files:
        if filename.lower().endswith(".f"):
            with open(filename, encoding="ascii") as source_file:
                nested_files = source_file.read().split()

            nested_paths = [
                os.path.join(os.path.dirname(filename), nested_file) for nested_file in nested_files
            ]

            for nested_source in process_f_files(nested_paths):
                sources[os.path.basename(nested_source)] = nested_source
        else:
            sources[os.path.basename(filename)] = filename

    return list(sources.values())


@pytest.mark.parametrize("loopback_stalls", [False, True], ids=["continuous", "stalled"])
def test_openenoc_endpoint_full(request, loopback_stalls):
    module = os.path.splitext(os.path.basename(__file__))[0]
    toplevel = module
    imem_init_file = os.path.join(repo_dir, "build", "sw", "openenoc_endpoint_full", "imem.mem")

    verilog_sources = [
        os.path.join(hal_rtl_dir, "openenoc_endpoint_full_pkg.sv"),
        os.path.join(hal_rtl_dir, "openenoc_endpoint_full_csr_pkg.sv"),
        os.path.join(hal_if_dir, "openenoc_endpoint_if.sv"),
        os.path.join(hal_if_dir, "openenoc_switch_if.sv"),
        os.path.join(taxi_axis_dir, "taxi_axis_if.sv"),
        os.path.join(taxi_axis_dir, "taxi_axis_adapter.sv"),
        os.path.join(taxi_axis_dir, "taxi_axis_register.sv"),
        os.path.join(taxi_axi_dir, "taxi_axil_if.sv"),
        os.path.join(core_dir, "openenoc_axil_crossbar.f"),
        os.path.join(picorv32_dir, "picorv32.v"),
        os.path.join(core_dir, "openenoc_picorv32_axil_adapter.sv"),
        os.path.join(core_dir, "openenoc_picorv32.sv"),
        os.path.join(core_dir, "openenoc_eth_if.sv"),
        os.path.join(core_dir, "openenoc_cpuif_if.sv"),
        os.path.join(core_dir, "openenoc_cpuif_axil_adapter.sv"),
        os.path.join(core_dir, "openenoc_peer_lookup_if.sv"),
        os.path.join(core_dir, "openenoc_dma_transfer_if.sv"),
        os.path.join(core_dir, "openenoc_irq_event_if.sv"),
        os.path.join(core_dir, "openenoc_endpoint_dma_engine.sv"),
        os.path.join(core_dir, "openenoc_endpoint_peer_lookup.sv"),
        os.path.join(core_dir, "openenoc_endpoint_irq_controller.sv"),
        os.path.join(core_dir, "openenoc_endpoint_direct_axis.sv"),
        os.path.join(core_dir, "openenoc_endpoint_oetp_engine.sv"),
        os.path.join(libs_dir, "taxi", "src", "axis", "rtl", "taxi_axis_fifo.sv"),
        os.path.join(libs_dir, "taxi", "src", "axis", "rtl", "taxi_axis_fifo_adapter.sv"),
        os.path.join(libs_dir, "taxi", "src", "axis", "rtl", "taxi_axis_arb_mux.sv"),
        os.path.join(libs_dir, "taxi", "src", "axis", "rtl", "taxi_axis_demux.sv"),
        os.path.join(libs_dir, "taxi", "src", "axi", "rtl", "taxi_axi_if.sv"),
        os.path.join(libs_dir, "taxi", "src", "axi", "rtl", "taxi_axi_register_rd.sv"),
        os.path.join(libs_dir, "taxi", "src", "axi", "rtl", "taxi_axi_register_wr.sv"),
        os.path.join(libs_dir, "taxi", "src", "axi", "rtl", "taxi_axi_axil_adapter.sv"),
        os.path.join(libs_dir, "taxi", "src", "axi", "rtl", "taxi_axi_axil_adapter_wr.sv"),
        os.path.join(libs_dir, "taxi", "src", "axi", "rtl", "taxi_axi_axil_adapter_rd.sv"),
        os.path.join(libs_dir, "taxi", "src", "dma", "rtl", "taxi_dma_desc_if.sv"),
        os.path.join(libs_dir, "taxi", "src", "dma", "rtl", "taxi_axi_dma.sv"),
        os.path.join(libs_dir, "taxi", "src", "dma", "rtl", "taxi_axi_dma_rd.sv"),
        os.path.join(libs_dir, "taxi", "src", "dma", "rtl", "taxi_axi_dma_wr.sv"),
        os.path.join(libs_dir, "taxi", "src", "prim", "rtl", "taxi_arbiter.sv"),
        os.path.join(libs_dir, "taxi", "src", "prim", "rtl", "taxi_penc.sv"),
        os.path.join(core_dir, "openenoc_endpoint_interface.sv"),
        os.path.join(core_dir, "openenoc_axil_ram.sv"),
        os.path.join(hal_rtl_dir, "openenoc_endpoint_full_csr.sv"),
        os.path.join(hal_rtl_dir, "openenoc_endpoint_full_csr_bridge.sv"),
        os.path.join(endpoint_dir, "openenoc_endpoint_full.sv"),
        os.path.join(tests_dir, f"{toplevel}.sv"),
    ]
    verilog_sources = process_f_files(verilog_sources)

    parameters = {
        "IMEM_INIT_FILE": f'"{imem_init_file}"',
    }
    extra_env = {
        "PARAM_IMEM_INIT_FILE": imem_init_file,
        "LOOPBACK_STALLS": "1" if loopback_stalls else "0",
    }

    sim_build = os.path.join(tests_dir, "sim_build", request.node.name)

    cocotb_test.simulator.run(
        simulator="verilator",
        python_search=[tests_dir],
        verilog_sources=verilog_sources,
        toplevel=toplevel,
        module=module,
        parameters=parameters,
        timescale="1ns/1ps",
        extra_args=["-Wall", os.path.join(common_dir, "config.vlt")],
        sim_build=sim_build,
        extra_env=extra_env,
    )
