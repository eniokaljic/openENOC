# SPDX-FileCopyrightText: 2026 Kerim Bavcic
# SPDX-License-Identifier: AGPL-3.0-or-later

TOPLEVEL_LANG = verilog

SIM ?= verilator
WAVES ?= 0

COCOTB_HDL_TIMEUNIT = 1ns
COCOTB_HDL_TIMEPRECISION = 1ps

REPO_DIR = ../../..
HW_DIR = $(REPO_DIR)/hw
LIBS_DIR = $(REPO_DIR)/libs
CORE_DIR = $(HW_DIR)/rtl/core
TAXI_AXIS_DIR = $(LIBS_DIR)/taxi/src/axis/rtl

DUT = openenoc_axis_forwarding_engine
COCOTB_TEST_MODULES = test_$(DUT)
COCOTB_TOPLEVEL = test_$(DUT)
MODULE = $(COCOTB_TEST_MODULES)
TOPLEVEL = $(COCOTB_TOPLEVEL)
VERILOG_SOURCES += $(COCOTB_TOPLEVEL).sv
VERILOG_SOURCES += $(CORE_DIR)/openenoc_lookup_if.sv
VERILOG_SOURCES += $(CORE_DIR)/openenoc_learning_if.sv
VERILOG_SOURCES += $(CORE_DIR)/$(DUT).sv
VERILOG_SOURCES += $(TAXI_AXIS_DIR)/taxi_axis_pipeline_register.sv
VERILOG_SOURCES += $(TAXI_AXIS_DIR)/taxi_axis_register.sv
VERILOG_SOURCES += $(TAXI_AXIS_DIR)/taxi_axis_if.sv

# handle file list files
process_f_file = $(call process_f_files,$(addprefix $(dir $1),$(shell cat $1)))
process_f_files = $(foreach f,$1,$(if $(filter %.f,$f),$(call process_f_file,$f),$f))
uniq_base = $(if $1,$(call uniq_base,$(foreach f,$1,$(if $(filter-out $(notdir $(lastword $1)),$(notdir $f)),$f,))) $(lastword $1))
VERILOG_SOURCES := $(call uniq_base,$(call process_f_files,$(VERILOG_SOURCES)))

# module parameters
export PARAM_NUM_OF_INTERFACES := 8
export PARAM_DATA_W := 8
export PARAM_KEEP_EN := $(shell expr $(PARAM_DATA_W) \> 8 )
export PARAM_KEEP_W := $(shell expr \( $(PARAM_DATA_W) + 7 \) / 8 )
export PARAM_STRB_EN := 0
export PARAM_LAST_EN := 1
export PARAM_ID_EN := 1
export PARAM_ID_W := 8
export PARAM_DEST_EN := 1
export PARAM_DEST_W := 8
export PARAM_USER_EN := 1
export PARAM_USER_W := $(PARAM_NUM_OF_INTERFACES)

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
