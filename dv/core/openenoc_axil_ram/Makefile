# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: AGPL-3.0-or-later

TOPLEVEL_LANG = verilog

override SIM := verilator
WAVES ?= 0

COCOTB_HDL_TIMEUNIT = 1ns
COCOTB_HDL_TIMEPRECISION = 1ps

REPO_DIR = ../../..
HW_DIR = $(REPO_DIR)/hw
LIBS_DIR = $(REPO_DIR)/libs
CORE_DIR = $(HW_DIR)/rtl/core
TAXI_AXI_DIR = $(LIBS_DIR)/taxi/src/axi/rtl

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
export PARAM_INIT_FILE := $(abspath imem.mem)

NONSTRING_PARAM_VARS = $(filter-out PARAM_INIT_FILE,$(filter PARAM_%,$(.VARIABLES)))

COMPILE_ARGS += $(foreach v,$(NONSTRING_PARAM_VARS),-G$(subst PARAM_,,$(v))=$($(v)))
COMPILE_ARGS += '-GINIT_FILE="$(PARAM_INIT_FILE)"'
EXTRA_ARGS += -Wall ../../common/config.vlt
ifeq ($(WAVES), 1)
	EXTRA_ARGS += --trace
	EXTRA_ARGS += --trace-fst
	EXTRA_ARGS += --trace-structs
endif

include $(shell cocotb-config --makefiles)/Makefile.sim

# Extended clean
clean::
	@rm -rf __pycache__
	@rm -f *.pyc
