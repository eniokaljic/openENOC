# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: AGPL-3.0-or-later

TOPLEVEL_LANG = verilog

SIM ?= verilator
WAVES ?= 0

COCOTB_HDL_TIMEUNIT = 1ns
COCOTB_HDL_TIMEPRECISION = 1ps

REPO_DIR = ../../..
CORE_DIR = $(REPO_DIR)/hw/rtl/core
TAXI_AXI_RTL_DIR = $(REPO_DIR)/libs/taxi/src/axi/rtl

DUT = openenoc_cpuif_axil_adapter
COCOTB_TEST_MODULES = test_$(DUT)
COCOTB_TOPLEVEL = test_$(DUT)
MODULE = $(COCOTB_TEST_MODULES)
TOPLEVEL = $(COCOTB_TOPLEVEL)

VERILOG_SOURCES += $(TAXI_AXI_RTL_DIR)/taxi_axil_if.sv
VERILOG_SOURCES += $(CORE_DIR)/openenoc_cpuif_if.sv
VERILOG_SOURCES += $(CORE_DIR)/$(DUT).sv
VERILOG_SOURCES += $(COCOTB_TOPLEVEL).sv

ifeq ($(SIM), verilator)
	EXTRA_ARGS += -Wall ../../common/config.vlt
	ifeq ($(WAVES), 1)
		EXTRA_ARGS += --trace
		EXTRA_ARGS += --trace-fst
		EXTRA_ARGS += --trace-structs
	endif
endif

include $(shell cocotb-config --makefiles)/Makefile.sim
