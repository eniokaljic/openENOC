# SPDX-FileCopyrightText: 2026 Kerim Bavcic
# SPDX-License-Identifier: AGPL-3.0-or-later

TOPLEVEL_LANG = verilog

SIM ?= verilator
WAVES ?= 0

COCOTB_HDL_TIMEUNIT = 1ns
COCOTB_HDL_TIMEPRECISION = 1ps

REPO_DIR = ../../../..
ISS_DIR = ../..
HW_DIR = $(REPO_DIR)/hw
LIBS_DIR = $(REPO_DIR)/libs
CORE_DIR = $(HW_DIR)/rtl/core
ENDPOINT_DIR = $(HW_DIR)/rtl/endpoints
TAXI_AXI_DIR = $(LIBS_DIR)/taxi/src/axi/rtl
TAXI_AXIS_DIR = $(LIBS_DIR)/taxi/src/axis/rtl
TAXI_SYNC_DIR = $(LIBS_DIR)/taxi/src/sync/rtl
HAL_RTL_DIR = $(REPO_DIR)/build/hal/openenoc_endpoint_full/rtl
HAL_IF_DIR = $(REPO_DIR)/build/hal/rtl

COCOTB_TEST_MODULES = test_openenoc_iss
COCOTB_TOPLEVEL = test_openenoc_iss
MODULE = $(COCOTB_TEST_MODULES)
TOPLEVEL = $(COCOTB_TOPLEVEL)

VERILOG_SOURCES += $(HAL_RTL_DIR)/openenoc_endpoint_full_pkg.sv
VERILOG_SOURCES += $(HAL_RTL_DIR)/openenoc_endpoint_full_csr_pkg.sv
VERILOG_SOURCES += $(HAL_IF_DIR)/openenoc_endpoint_if.sv
VERILOG_SOURCES += $(HAL_IF_DIR)/openenoc_switch_if.sv
VERILOG_SOURCES += $(TAXI_AXIS_DIR)/taxi_axis_if.sv
VERILOG_SOURCES += $(TAXI_SYNC_DIR)/taxi_sync_reset.sv
VERILOG_SOURCES += $(TAXI_SYNC_DIR)/taxi_sync_signal.sv
VERILOG_SOURCES += $(TAXI_AXIS_DIR)/taxi_axis_adapter.sv
VERILOG_SOURCES += $(TAXI_AXIS_DIR)/taxi_axis_async_fifo.sv
VERILOG_SOURCES += $(TAXI_AXIS_DIR)/taxi_axis_async_fifo_adapter.sv
VERILOG_SOURCES += $(TAXI_AXI_DIR)/taxi_axil_if.sv
VERILOG_SOURCES += $(CORE_DIR)/openenoc_axil_crossbar_skid_buffer.sv
VERILOG_SOURCES += $(CORE_DIR)/openenoc_rr_arbiter.sv
VERILOG_SOURCES += $(CORE_DIR)/openenoc_axil_crossbar_addr.sv
VERILOG_SOURCES += $(CORE_DIR)/openenoc_axil_crossbar_wr.sv
VERILOG_SOURCES += $(CORE_DIR)/openenoc_axil_crossbar_rd.sv
VERILOG_SOURCES += $(CORE_DIR)/openenoc_axil_crossbar.sv
VERILOG_SOURCES += $(CORE_DIR)/openenoc_eth_if.sv
VERILOG_SOURCES += $(CORE_DIR)/openenoc_endpoint_interface.sv
VERILOG_SOURCES += $(CORE_DIR)/openenoc_axil_ram.sv
VERILOG_SOURCES += $(HAL_RTL_DIR)/openenoc_endpoint_full_csr.sv
VERILOG_SOURCES += $(HAL_RTL_DIR)/openenoc_endpoint_full_csr_bridge.sv
VERILOG_SOURCES += $(ISS_DIR)/rtl/openenoc_iss_cpu_proxy.sv
VERILOG_SOURCES += $(ENDPOINT_DIR)/openenoc_endpoint_full.sv
VERILOG_SOURCES += test_openenoc_iss.sv

export PYTHONPATH := $(abspath $(ISS_DIR)/python):$(PYTHONPATH)
export OPENENOC_ISS_LIBRARY := $(abspath $(REPO_DIR)/build/dv/iss/lib/libopenenoc_iss.so)
export OPENENOC_FIRMWARE_BIN := $(abspath $(REPO_DIR)/build/sw/openenoc_endpoint_full/csr_smoke.bin)

ifeq ($(SIM), verilator)
	EXTRA_ARGS += -Wall -Wno-TIMESCALEMOD -Wno-SYNCASYNCNET -Wno-MULTIDRIVEN $(REPO_DIR)/dv/common/config.vlt
	ifeq ($(WAVES), 1)
		EXTRA_ARGS += --trace
		EXTRA_ARGS += --trace-fst
	endif
endif

include $(shell cocotb-config --makefiles)/Makefile.sim