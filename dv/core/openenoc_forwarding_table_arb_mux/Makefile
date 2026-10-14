# SPDX-FileCopyrightText: 2026 Kerim Bavcic
# SPDX-License-Identifier: AGPL-3.0-or-later

TOPLEVEL_LANG = verilog

override SIM := verilator
WAVES ?= 0

COCOTB_HDL_TIMEUNIT = 1ns
COCOTB_HDL_TIMEPRECISION = 1ps

include ../../common/sim_paths.mk

HW_DIR = ../../../hw
CORE_DIR = $(HW_DIR)/rtl/core

DUT = openenoc_forwarding_table_arb_mux
COCOTB_TEST_MODULES = test_$(DUT)
COCOTB_TOPLEVEL = test_$(DUT)
MODULE = $(COCOTB_TEST_MODULES)
TOPLEVEL = $(COCOTB_TOPLEVEL)

VERILOG_SOURCES += $(COCOTB_TOPLEVEL).sv
VERILOG_SOURCES += $(CORE_DIR)/openenoc_lookup_if.sv
VERILOG_SOURCES += $(CORE_DIR)/openenoc_learning_if.sv
VERILOG_SOURCES += $(CORE_DIR)/openenoc_rr_arbiter.sv
VERILOG_SOURCES += $(CORE_DIR)/$(DUT).sv

# module parameters
export PARAM_NUM_OF_INTERFACES := 4

COMPILE_ARGS += $(foreach v,$(filter PARAM_%,$(.VARIABLES)),\
	-G$(subst PARAM_,,$(v))=$($(v)))
EXTRA_ARGS += -Wall ../../common/config.vlt
ifeq ($(WAVES), 1)
	EXTRA_ARGS += --trace
	EXTRA_ARGS += --trace-fst
	EXTRA_ARGS += --trace-structs
endif

include $(shell cocotb-config --makefiles)/Makefile.sim

# Extended clean
clean::
	@$(RM) -rf "$(SIM_OUTPUT)/sim_build" "$(SIM_OUTPUT)/__pycache__" "$(TMPDIR)"
