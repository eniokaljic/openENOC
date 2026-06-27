# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: AGPL-3.0-or-later

TOPLEVEL_LANG = verilog

SIM ?= verilator
WAVES ?= 0

COCOTB_HDL_TIMEUNIT = 1ns
COCOTB_HDL_TIMEPRECISION = 1ps

HW_DIR = ../../../hw
CORE_DIR = $(HW_DIR)/src/core
TAXI_AXIS_DIR = $(HW_DIR)/libs/taxi/src/axis/rtl
TAXI_SYNC_DIR = $(HW_DIR)/libs/taxi/src/sync/rtl

DUT = openenoc_eth_adapter

COCOTB_TEST_MODULES = test_$(DUT)
COCOTB_TOPLEVEL = test_$(DUT)

MODULE = $(COCOTB_TEST_MODULES)
TOPLEVEL = $(COCOTB_TOPLEVEL)

VERILOG_SOURCES += $(TAXI_AXIS_DIR)/taxi_axis_if.sv
VERILOG_SOURCES += $(TAXI_AXIS_DIR)/taxi_axis_async_fifo_adapter.sv
VERILOG_SOURCES += $(TAXI_AXIS_DIR)/taxi_axis_async_fifo.sv
VERILOG_SOURCES += $(TAXI_AXIS_DIR)/taxi_axis_adapter.sv
VERILOG_SOURCES += $(TAXI_SYNC_DIR)/taxi_sync_reset.sv
VERILOG_SOURCES += $(TAXI_SYNC_DIR)/taxi_sync_signal.sv
VERILOG_SOURCES += $(CORE_DIR)/openenoc_eth_if.sv
VERILOG_SOURCES += $(CORE_DIR)/$(DUT).sv
VERILOG_SOURCES += $(COCOTB_TOPLEVEL).sv

# handle file list files
process_f_file = $(call process_f_files,$(addprefix $(dir $1),$(shell cat $1)))
process_f_files = $(foreach f,$1,$(if $(filter %.f,$f),$(call process_f_file,$f),$f))
uniq_base = $(if $1,$(call uniq_base,$(foreach f,$1,$(if $(filter-out $(notdir $(lastword $1)),$(notdir $f)),$f,))) $(lastword $1))

VERILOG_SOURCES := $(call uniq_base,$(call process_f_files,$(VERILOG_SOURCES)))

# clock periods used by cocotb testbench
export CLK_A_PERIOD := 10
export CLK_B_PERIOD := 40

# ----------------------------------------------------------------------
# Side A interface parameters
# ----------------------------------------------------------------------

export PARAM_A_DATA_W := 8
export PARAM_A_KEEP_EN := $(shell expr $(PARAM_A_DATA_W) \> 8)
export PARAM_A_KEEP_W := $(shell expr \( $(PARAM_A_DATA_W) + 7 \) / 8)
export PARAM_A_STRB_EN := 0
export PARAM_A_LAST_EN := 1
export PARAM_A_ID_EN := 1
export PARAM_A_ID_W := 8
export PARAM_A_DEST_EN := 1
export PARAM_A_DEST_W := 8
export PARAM_A_USER_EN := 1
export PARAM_A_USER_W := 1

# ----------------------------------------------------------------------
# Side B interface parameters
# ----------------------------------------------------------------------

export PARAM_B_DATA_W := 32
export PARAM_B_KEEP_EN := $(shell expr $(PARAM_B_DATA_W) \> 8)
export PARAM_B_KEEP_W := $(shell expr \( $(PARAM_B_DATA_W) + 7 \) / 8)
export PARAM_B_STRB_EN := 0
export PARAM_B_LAST_EN := 1
export PARAM_B_ID_EN := 1
export PARAM_B_ID_W := 8
export PARAM_B_DEST_EN := 1
export PARAM_B_DEST_W := 8
export PARAM_B_USER_EN := 1
export PARAM_B_USER_W := 1

# ----------------------------------------------------------------------
# FIFO parameters
# ----------------------------------------------------------------------

export PARAM_DEPTH := $(shell python -c "print(2 * max($(PARAM_A_KEEP_W), $(PARAM_B_KEEP_W)))")
export PARAM_RAM_PIPELINE := 1
export PARAM_OUTPUT_FIFO_EN := 0
export PARAM_FRAME_FIFO := 0
export PARAM_USER_BAD_FRAME_VALUE := 1
export PARAM_USER_BAD_FRAME_MASK := 1
export PARAM_DROP_OVERSIZE_FRAME := 0
export PARAM_DROP_BAD_FRAME := 0
export PARAM_DROP_WHEN_FULL := 0
export PARAM_MARK_WHEN_FULL := 0
export PARAM_FRAME_PAUSE := 1

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
