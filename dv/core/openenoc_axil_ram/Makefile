# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: AGPL-3.0-or-later

TOPLEVEL_LANG = verilog

SIM ?= verilator
WAVES ?= 0

COCOTB_HDL_TIMEUNIT = 1ns
COCOTB_HDL_TIMEPRECISION = 1ps

HW_DIR = ../../../hw
CORE_DIR = $(HW_DIR)/src/core
TAXI_AXI_DIR = $(HW_DIR)/libs/taxi/src/axi/rtl

DUT = openenoc_axil_ram
COCOTB_TEST_MODULES = test_$(DUT)
COCOTB_TOPLEVEL = test_$(DUT)
MODULE = $(COCOTB_TEST_MODULES)
TOPLEVEL = $(COCOTB_TOPLEVEL)

VERILOG_SOURCES += $(TAXI_AXI_DIR)/taxi_axil_if.sv
VERILOG_SOURCES += $(CORE_DIR)/$(DUT).sv
VERILOG_SOURCES += $(COCOTB_TOPLEVEL).sv

# Module parameters
export PARAM_DATA_W := 32
export PARAM_ADDR_W := 10
export PARAM_AXIL_ADDR_W := 32
export PARAM_STRB_W := $(shell expr $(PARAM_DATA_W) / 8)
export PARAM_PIPELINE_OUTPUT := 0
export PARAM_INIT_FILE := "$(abspath imem.mem)"

ifeq ($(SIM), icarus)
	PLUSARGS += -fst
	COMPILE_ARGS += $(foreach v,$(filter PARAM_%,$(.VARIABLES)),-P $(COCOTB_TOPLEVEL).$(subst PARAM_,,$(v))=$($(v)))
else ifeq ($(SIM), verilator)
	COMPILE_ARGS += $(foreach v,$(filter PARAM_%,$(.VARIABLES)),-G$(subst PARAM_,,$(v))=$($(v)))
	EXTRA_ARGS += -Wall ../../common/config.vlt
	ifeq ($(WAVES), 1)
		EXTRA_ARGS += --trace
		EXTRA_ARGS += --trace-fst
	endif
endif

include $(shell cocotb-config --makefiles)/Makefile.sim
