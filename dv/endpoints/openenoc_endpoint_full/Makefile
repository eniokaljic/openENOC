# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: AGPL-3.0-or-later

TOPLEVEL_LANG = verilog

SIM ?= verilator
WAVES ?= 0

COCOTB_HDL_TIMEUNIT = 1ns
COCOTB_HDL_TIMEPRECISION = 1ps

REPO_DIR = ../../..
HW_DIR = $(REPO_DIR)/hw
LIBS_DIR = $(REPO_DIR)/libs
CORE_DIR = $(HW_DIR)/rtl/core
ENDPOINT_DIR = $(HW_DIR)/rtl/endpoints
TAXI_AXI_DIR = $(LIBS_DIR)/taxi/src/axi/rtl
TAXI_AXIS_DIR = $(LIBS_DIR)/taxi/src/axis/rtl
TAXI_PRIM_DIR = $(TAXI_AXI_DIR)/../lib/taxi/src/prim/rtl
PICORV32_DIR = $(LIBS_DIR)/picorv32
HAL_RTL_DIR = $(REPO_DIR)/build/hal/openenoc_endpoint_full/rtl
HAL_IF_DIR = $(REPO_DIR)/build/hal/rtl
SW_BUILD_DIR = $(REPO_DIR)/build/sw/openenoc_endpoint_full

DUT = openenoc_endpoint_full
COCOTB_TEST_MODULES = test_$(DUT)
COCOTB_TOPLEVEL = test_$(DUT)
MODULE = $(COCOTB_TEST_MODULES)
TOPLEVEL = $(COCOTB_TOPLEVEL)

VERILOG_SOURCES += $(HAL_RTL_DIR)/openenoc_endpoint_full_pkg.sv
VERILOG_SOURCES += $(HAL_RTL_DIR)/openenoc_endpoint_full_csr_pkg.sv
VERILOG_SOURCES += $(HAL_IF_DIR)/openenoc_endpoint_if.sv
VERILOG_SOURCES += $(HAL_IF_DIR)/openenoc_switch_if.sv
VERILOG_SOURCES += $(TAXI_AXIS_DIR)/taxi_axis_if.sv
VERILOG_SOURCES += $(TAXI_AXI_DIR)/taxi_axil_if.sv
VERILOG_SOURCES += $(TAXI_PRIM_DIR)/taxi_arbiter.sv
VERILOG_SOURCES += $(TAXI_PRIM_DIR)/taxi_penc.sv
VERILOG_SOURCES += $(TAXI_AXI_DIR)/taxi_axil_register_wr.sv
VERILOG_SOURCES += $(TAXI_AXI_DIR)/taxi_axil_register_rd.sv
VERILOG_SOURCES += $(TAXI_AXI_DIR)/taxi_axil_crossbar_addr.sv
VERILOG_SOURCES += $(TAXI_AXI_DIR)/taxi_axil_crossbar_wr.sv
VERILOG_SOURCES += $(TAXI_AXI_DIR)/taxi_axil_crossbar_rd.sv
VERILOG_SOURCES += $(TAXI_AXI_DIR)/taxi_axil_crossbar.sv
VERILOG_SOURCES += $(PICORV32_DIR)/picorv32.v
VERILOG_SOURCES += $(CORE_DIR)/openenoc_eth_if.sv
VERILOG_SOURCES += $(CORE_DIR)/openenoc_axil_ram.sv
VERILOG_SOURCES += $(HAL_RTL_DIR)/openenoc_endpoint_full_csr.sv
VERILOG_SOURCES += $(HAL_RTL_DIR)/openenoc_endpoint_full_csr_bridge.sv
VERILOG_SOURCES += $(ENDPOINT_DIR)/$(DUT).sv
VERILOG_SOURCES += $(COCOTB_TOPLEVEL).sv

export PARAM_IMEM_INIT_FILE := $(abspath $(SW_BUILD_DIR)/imem.mem)

ifeq ($(SIM), verilator)
	COMPILE_ARGS += '-GIMEM_INIT_FILE="$(PARAM_IMEM_INIT_FILE)"'
	EXTRA_ARGS += -Wall -Wno-TIMESCALEMOD ../../common/config.vlt
	ifeq ($(WAVES), 1)
		EXTRA_ARGS += --trace
		EXTRA_ARGS += --trace-fst
		EXTRA_ARGS += --trace-structs
	endif
endif

include $(shell cocotb-config --makefiles)/Makefile.sim
