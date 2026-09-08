# SPDX-FileCopyrightText: 2026 Kerim Bavcic
# SPDX-License-Identifier: AGPL-3.0-or-later

TOPLEVEL_LANG = verilog
SIM ?= verilator
WAVES ?= 0
COCOTB_HDL_TIMEUNIT = 1ns
COCOTB_HDL_TIMEPRECISION = 1ps

REPO_DIR = ../../..
CORE_DIR = $(REPO_DIR)/hw/rtl/core
TAXI_AXIS_DIR = $(REPO_DIR)/libs/taxi/src/axis/rtl
TAXI_SYNC_DIR = $(REPO_DIR)/libs/taxi/src/sync/rtl
DUT = openenoc_eth_switch_crossbar
COCOTB_TEST_MODULES = test_$(DUT)
COCOTB_TOPLEVEL = test_$(DUT)
MODULE = $(COCOTB_TEST_MODULES)
TOPLEVEL = $(COCOTB_TOPLEVEL)

VERILOG_SOURCES += $(TAXI_AXIS_DIR)/taxi_axis_if.sv
VERILOG_SOURCES += $(TAXI_AXIS_DIR)/taxi_axis_register.sv
VERILOG_SOURCES += $(TAXI_AXIS_DIR)/taxi_axis_pipeline_register.sv
VERILOG_SOURCES += $(TAXI_AXIS_DIR)/taxi_axis_adapter.sv
VERILOG_SOURCES += $(TAXI_AXIS_DIR)/taxi_axis_async_fifo.sv
VERILOG_SOURCES += $(TAXI_AXIS_DIR)/taxi_axis_async_fifo_adapter.sv
VERILOG_SOURCES += $(TAXI_SYNC_DIR)/taxi_sync_reset.sv
VERILOG_SOURCES += $(TAXI_SYNC_DIR)/taxi_sync_signal.sv
VERILOG_SOURCES += $(REPO_DIR)/build/hal/rtl/openenoc_switch_if.sv
VERILOG_SOURCES += $(CORE_DIR)/openenoc_eth_if.sv
VERILOG_SOURCES += $(CORE_DIR)/openenoc_lookup_if.sv
VERILOG_SOURCES += $(CORE_DIR)/openenoc_learning_if.sv
VERILOG_SOURCES += $(CORE_DIR)/openenoc_axil_crossbar_arbiter.sv
VERILOG_SOURCES += $(CORE_DIR)/openenoc_forwarding_table_arb_mux.sv
VERILOG_SOURCES += $(CORE_DIR)/openenoc_axis_forwarding_engine.sv
VERILOG_SOURCES += $(CORE_DIR)/openenoc_forwarding_table.sv
VERILOG_SOURCES += $(CORE_DIR)/openenoc_axis_switch.sv
VERILOG_SOURCES += $(CORE_DIR)/$(DUT).sv
VERILOG_SOURCES += $(COCOTB_TOPLEVEL).sv

export PARAM_NUM_OF_INTERFACES := 4
export PARAM_TABLE_DEPTH := 8
export PARAM_DATA_W := 32
export PARAM_KEEP_W := 4
export PARAM_KEEP_EN := 1
export PARAM_FABRIC_DATA_W := 32
export PARAM_PORT_FIFO_DEPTH := 64
export PARAM_PORT_SIDE := 15

ifeq ($(SIM), verilator)
COMPILE_ARGS += $(foreach v,$(filter PARAM_%,$(.VARIABLES)),-G$(subst PARAM_,,$(v))=$($(v)))
EXTRA_ARGS += -Wall -Wno-DECLFILENAME ../../common/config.vlt
ifeq ($(WAVES), 1)
EXTRA_ARGS += --trace --trace-fst
endif
endif

include $(shell cocotb-config --makefiles)/Makefile.sim