# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: AGPL-3.0-or-later

TOPLEVEL_LANG = verilog

SIM ?= verilator
WAVES ?= 0

COCOTB_HDL_TIMEUNIT = 1ns
COCOTB_HDL_TIMEPRECISION = 1ps

REPO_DIR = ../../..
CORE_DIR = $(REPO_DIR)/hw/rtl/core
HAL_IF_DIR = $(REPO_DIR)/build/hal/rtl
HAL_RTL_DIR = $(REPO_DIR)/build/hal/openenoc_endpoint_full/rtl

DUT = openenoc_endpoint_peer_lookup
COCOTB_TEST_MODULES = test_$(DUT)
COCOTB_TOPLEVEL = test_$(DUT)
MODULE = $(COCOTB_TEST_MODULES)
TOPLEVEL = $(COCOTB_TOPLEVEL)

VERILOG_SOURCES += $(HAL_RTL_DIR)/openenoc_endpoint_full_csr_pkg.sv
VERILOG_SOURCES += $(HAL_IF_DIR)/openenoc_endpoint_if.sv
VERILOG_SOURCES += $(HAL_IF_DIR)/openenoc_switch_if.sv
VERILOG_SOURCES += $(CORE_DIR)/openenoc_peer_lookup_if.sv
VERILOG_SOURCES += $(CORE_DIR)/openenoc_rr_arbiter.sv
VERILOG_SOURCES += $(CORE_DIR)/$(DUT).sv
VERILOG_SOURCES += $(HAL_RTL_DIR)/openenoc_endpoint_full_csr.sv
VERILOG_SOURCES += $(HAL_RTL_DIR)/openenoc_endpoint_full_csr_bridge.sv
VERILOG_SOURCES += $(COCOTB_TOPLEVEL).sv

export PARAM_LOOKUP_PORTS := 2

ifeq ($(SIM), icarus)
	PLUSARGS += -fst
	COMPILE_ARGS += $(foreach v,$(filter PARAM_%,$(.VARIABLES)),-P $(COCOTB_TOPLEVEL).$(subst PARAM_,,$(v))=$($(v)))
else ifeq ($(SIM), verilator)
	COMPILE_ARGS += $(foreach v,$(filter PARAM_%,$(.VARIABLES)),-G$(subst PARAM_,,$(v))=$($(v)))
	EXTRA_ARGS += -Wall -Wno-TIMESCALEMOD ../../common/config.vlt
	ifeq ($(WAVES), 1)
		EXTRA_ARGS += --trace
		EXTRA_ARGS += --trace-fst
		EXTRA_ARGS += --trace-structs
	endif
endif

include $(shell cocotb-config --makefiles)/Makefile.sim
