# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: AGPL-3.0-or-later

TOPLEVEL_LANG = verilog

SIM ?= verilator
WAVES ?= 0

COCOTB_HDL_TIMEUNIT = 1ns
COCOTB_HDL_TIMEPRECISION = 1ps

REPO_DIR = ../../..
CORE_DIR = $(REPO_DIR)/hw/rtl/core
TAXI_AXIS_DIR = $(REPO_DIR)/libs/taxi/src/axis/rtl

DUT = openenoc_endpoint_irq_controller
COCOTB_TEST_MODULES = test_$(DUT)
COCOTB_TOPLEVEL = test_$(DUT)
MODULE = $(COCOTB_TEST_MODULES)
TOPLEVEL = $(COCOTB_TOPLEVEL)

VERILOG_SOURCES += $(COCOTB_TOPLEVEL).sv
VERILOG_SOURCES += $(TAXI_AXIS_DIR)/taxi_axis_if.sv
VERILOG_SOURCES += $(TAXI_AXIS_DIR)/taxi_axis_fifo.sv
VERILOG_SOURCES += $(CORE_DIR)/openenoc_irq_event_if.sv
VERILOG_SOURCES += $(CORE_DIR)/openenoc_rr_arbiter.sv
VERILOG_SOURCES += $(CORE_DIR)/$(DUT).sv

export PARAM_EVENT_PORTS := 4
export PARAM_FIFO_DEPTH := 4
export PARAM_PEER_IDX_W := 5
export PARAM_SEQUENCE_W := 4

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
