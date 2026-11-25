# SPDX-FileCopyrightText: 2026 Kerim Bavcic
# SPDX-License-Identifier: AGPL-3.0-or-later

TOPLEVEL_LANG = verilog

override SIM := verilator
WAVES ?= 0

COCOTB_HDL_TIMEUNIT = 1ns
COCOTB_HDL_TIMEPRECISION = 1ps

include ../../common/sim_paths.mk

REPO_DIR = ../../..
CORE_DIR = $(REPO_DIR)/hw/rtl/core
HAL_IF_DIR = $(REPO_DIR)/build/hal/rtl
TAXI_DIR = $(REPO_DIR)/libs/taxi/src

DUT = openenoc_endpoint_direct_axis
COCOTB_TEST_MODULES = test_$(DUT)
COCOTB_TOPLEVEL = test_$(DUT)
MODULE = $(COCOTB_TEST_MODULES)
TOPLEVEL = $(COCOTB_TOPLEVEL)

VERILOG_SOURCES += $(COCOTB_TOPLEVEL).sv
VERILOG_SOURCES += $(CORE_DIR)/$(DUT).sv
# Generated CSR interface and the stream register dependencies
VERILOG_SOURCES += $(HAL_IF_DIR)/openenoc_endpoint_if.sv
VERILOG_SOURCES += $(TAXI_DIR)/axis/rtl/taxi_axis_if.sv
VERILOG_SOURCES += $(TAXI_DIR)/axis/rtl/taxi_axis_register.sv
VERILOG_SOURCES += $(CORE_DIR)/openenoc_irq_event_if.sv

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
