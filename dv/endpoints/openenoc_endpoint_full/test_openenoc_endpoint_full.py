# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: AGPL-3.0-or-later

import os

import cocotb
import cocotb_test.simulator
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge
from cocotb.regression import TestFactory
TestFactory.__test__ = False

CSR_SMOKE_PATTERN = 0xA5A55A5A
CSR_SMOKE_PASSED = 0x600D600D
CSR_SMOKE_FAILED = 0xBAD0BAD0
EXECUTION_TIMEOUT_CYCLES = 5000


def signal_integer(signal):
    return int(signal.value)


def assert_reserved_interfaces_inactive(dut):
    assert signal_integer(dut.reserved_masters_inactive) == 1
    assert signal_integer(dut.endpoint_eth_inactive) == 1


@cocotb.test()
async def test_csr_smoke_firmware(dut):
    cocotb.start_soon(Clock(dut.clk, 10, unit="ns").start())

    dut.rst.value = 1

    for _ in range(5):
        await RisingEdge(dut.clk)
        assert signal_integer(dut.cpu_trap) == 0
        assert_reserved_interfaces_inactive(dut)

    with open(os.environ["PARAM_IMEM_INIT_FILE"], encoding="ascii") as source:
        expected_first_word = int(next(line for line in source if line.strip()), 16)

    assert signal_integer(dut.imem_word0) == expected_first_word
    assert signal_integer(dut.dmem_status) == 0
    assert signal_integer(dut.csr_test_value) == 0

    dut.rst.value = 0

    for _ in range(EXECUTION_TIMEOUT_CYCLES):
        await RisingEdge(dut.clk)

        assert signal_integer(dut.cpu_trap) == 0, "PicoRV32 entered trap state"
        assert_reserved_interfaces_inactive(dut)

        status = signal_integer(dut.dmem_status)
        assert status != CSR_SMOKE_FAILED, "csr_smoke firmware reported failure"

        if status == CSR_SMOKE_PASSED:
            break
    else:
        raise AssertionError(
            f"csr_smoke did not finish within {EXECUTION_TIMEOUT_CYCLES} cycles"
        )

    assert signal_integer(dut.csr_test_value) == CSR_SMOKE_PATTERN

    # The firmware returns into its terminal loop; the result must remain stable.
    for _ in range(10):
        await RisingEdge(dut.clk)
        assert signal_integer(dut.dmem_status) == CSR_SMOKE_PASSED
        assert signal_integer(dut.csr_test_value) == CSR_SMOKE_PATTERN
        assert signal_integer(dut.cpu_trap) == 0
        assert_reserved_interfaces_inactive(dut)


tests_dir = os.path.abspath(os.path.dirname(__file__))
repo_dir = os.path.abspath(os.path.join(tests_dir, "..", "..", ".."))
hw_dir = os.path.join(repo_dir, "hw")
libs_dir = os.path.join(repo_dir, "libs")
core_dir = os.path.join(hw_dir, "rtl", "core")
endpoint_dir = os.path.join(hw_dir, "rtl", "endpoints")
taxi_axi_dir = os.path.join(libs_dir, "taxi", "src", "axi", "rtl")
taxi_axis_dir = os.path.join(libs_dir, "taxi", "src", "axis", "rtl")
picorv32_dir = os.path.join(libs_dir, "picorv32")
hal_rtl_dir = os.path.join(repo_dir, "build", "hal", "openenoc_endpoint_full", "rtl")
common_dir = os.path.join(repo_dir, "dv", "common")


def process_f_files(files):
    sources = {}

    for filename in files:
        if filename.lower().endswith(".f"):
            with open(filename, encoding="ascii") as source_file:
                nested_files = source_file.read().split()

            nested_paths = [
                os.path.join(os.path.dirname(filename), nested_file)
                for nested_file in nested_files
            ]

            for nested_source in process_f_files(nested_paths):
                sources[os.path.basename(nested_source)] = nested_source
        else:
            sources[os.path.basename(filename)] = filename

    return list(sources.values())


def test_openenoc_full_endpoint(request):
    module = os.path.splitext(os.path.basename(__file__))[0]
    toplevel = module
    imem_init_file = os.path.join(
        repo_dir, "build", "sw", "openenoc_full_endpoint", "imem.mem"
    )

    verilog_sources = [
        os.path.join(hal_rtl_dir, "openenoc_endpoint_full_pkg.sv"),
        os.path.join(hal_rtl_dir, "openenoc_endpoint_full_csr_pkg.sv"),
        os.path.join(taxi_axis_dir, "taxi_axis_if.sv"),
        os.path.join(taxi_axi_dir, "taxi_axil_crossbar.f"),
        os.path.join(picorv32_dir, "picorv32.v"),
        os.path.join(core_dir, "openenoc_eth_if.sv"),
        os.path.join(core_dir, "openenoc_axil_ram.sv"),
        os.path.join(hal_rtl_dir, "openenoc_endpoint_full_csr.sv"),
        os.path.join(endpoint_dir, "openenoc_endpoint_full.sv"),
        os.path.join(tests_dir, f"{toplevel}.sv"),
    ]
    verilog_sources = process_f_files(verilog_sources)

    parameters = {
        "IMEM_INIT_FILE": f'"{imem_init_file}"',
    }
    extra_env = {
        "PARAM_IMEM_INIT_FILE": imem_init_file,
    }

    sim_build = os.path.join(tests_dir, "sim_build", request.node.name)

    cocotb_test.simulator.run(
        simulator="verilator",
        python_search=[tests_dir],
        verilog_sources=verilog_sources,
        toplevel=toplevel,
        module=module,
        parameters=parameters,
        extra_args=[
            "-Wno-TIMESCALEMOD",
            os.path.join(common_dir, "config.vlt"),
        ],
        sim_build=sim_build,
        extra_env=extra_env,
    )
