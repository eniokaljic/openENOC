# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: AGPL-3.0-or-later

TOPLEVEL_LANG = verilog

override SIM := verilator
WAVES ?= 0

COCOTB_HDL_TIMEUNIT = 1ns
COCOTB_HDL_TIMEPRECISION = 1ps

REPO_DIR = ../../..
CORE_DIR = $(REPO_DIR)/hw/rtl/core
TAXI_DIR = $(REPO_DIR)/libs/taxi/src

DUT = openenoc_endpoint_oetp_engine
COCOTB_TEST_MODULES = test_$(DUT)
COCOTB_TOPLEVEL = test_$(DUT)
MODULE = $(COCOTB_TEST_MODULES)
TOPLEVEL = $(COCOTB_TOPLEVEL)

VERILOG_SOURCES += $(REPO_DIR)/build/hal/rtl/openenoc_endpoint_if.sv
VERILOG_SOURCES += $(TAXI_DIR)/axis/rtl/taxi_axis_if.sv
VERILOG_SOURCES += $(TAXI_DIR)/axis/rtl/taxi_axis_adapter.sv
VERILOG_SOURCES += $(TAXI_DIR)/axis/rtl/taxi_axis_register.sv
VERILOG_SOURCES += $(CORE_DIR)/openenoc_peer_lookup_if.sv
VERILOG_SOURCES += $(CORE_DIR)/openenoc_dma_transfer_if.sv
VERILOG_SOURCES += $(CORE_DIR)/$(DUT).sv
VERILOG_SOURCES += $(COCOTB_TOPLEVEL).sv

export PARAM_LOCAL_DATA_W := 32
export PARAM_ETH_DATA_W := 32

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
	@rm -rf __pycache__
	@rm -f *.pyc
