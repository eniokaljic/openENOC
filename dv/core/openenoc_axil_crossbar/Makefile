# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: AGPL-3.0-or-later

TOPLEVEL_LANG = verilog

SIM ?= verilator
WAVES ?= 0

COCOTB_HDL_TIMEUNIT = 1ns
COCOTB_HDL_TIMEPRECISION = 1ps

REPO_DIR = ../../..
LIBS_DIR = $(REPO_DIR)/libs
CORE_DIR = $(REPO_DIR)/hw/rtl/core
TAXI_AXI_DIR = $(LIBS_DIR)/taxi/src/axi/rtl

DUT = openenoc_axil_crossbar
COCOTB_TEST_MODULES = test_$(DUT)
COCOTB_TOPLEVEL = test_$(DUT)
MODULE = $(COCOTB_TEST_MODULES)
TOPLEVEL = $(COCOTB_TOPLEVEL)

VERILOG_SOURCES += $(TAXI_AXI_DIR)/taxi_axil_if.sv
VERILOG_SOURCES += $(CORE_DIR)/openenoc_axil_crossbar_skid_buffer.sv
VERILOG_SOURCES += $(CORE_DIR)/openenoc_axil_crossbar_arbiter.sv
VERILOG_SOURCES += $(CORE_DIR)/openenoc_axil_crossbar_addr.sv
VERILOG_SOURCES += $(CORE_DIR)/openenoc_axil_crossbar_wr.sv
VERILOG_SOURCES += $(CORE_DIR)/openenoc_axil_crossbar_rd.sv
VERILOG_SOURCES += $(CORE_DIR)/openenoc_axil_crossbar.sv
VERILOG_SOURCES += $(COCOTB_TOPLEVEL).sv

export PARAM_S_COUNT := 3
export PARAM_M_COUNT := 3
export PARAM_DATA_W := 32
export PARAM_ADDR_W := 32
export PARAM_STRB_W := $(shell expr $(PARAM_DATA_W) / 8)
export PARAM_TARGET_ADDR_W := 16

ifeq ($(SIM), verilator)
	COMPILE_ARGS += $(foreach v,$(filter PARAM_%,$(.VARIABLES)),-G$(subst PARAM_,,$(v))=$($(v)))
	EXTRA_ARGS += -Wall ../../common/config.vlt
	ifeq ($(WAVES), 1)
		EXTRA_ARGS += --trace
		EXTRA_ARGS += --trace-fst
	endif
endif

include $(shell cocotb-config --makefiles)/Makefile.sim
