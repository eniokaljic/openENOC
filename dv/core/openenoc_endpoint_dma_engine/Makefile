# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: AGPL-3.0-or-later

TOPLEVEL_LANG = verilog

override SIM := verilator
WAVES ?= 0

COCOTB_HDL_TIMEUNIT = 1ns
COCOTB_HDL_TIMEPRECISION = 1ps

REPO_DIR = ../../..
CORE_DIR = $(REPO_DIR)/hw/rtl/core
HAL_IF_DIR = $(REPO_DIR)/build/hal/rtl
TAXI_DIR = $(REPO_DIR)/libs/taxi/src

DUT = openenoc_endpoint_dma_engine
COCOTB_TEST_MODULES = test_$(DUT)
COCOTB_TOPLEVEL = test_$(DUT)
MODULE = $(COCOTB_TEST_MODULES)
TOPLEVEL = $(COCOTB_TOPLEVEL)

VERILOG_SOURCES += $(HAL_IF_DIR)/openenoc_endpoint_if.sv
VERILOG_SOURCES += $(TAXI_DIR)/axis/rtl/taxi_axis_if.sv
VERILOG_SOURCES += $(TAXI_DIR)/axis/rtl/taxi_axis_register.sv
VERILOG_SOURCES += $(TAXI_DIR)/axi/rtl/taxi_axi_if.sv
VERILOG_SOURCES += $(TAXI_DIR)/axi/rtl/taxi_axi_register_rd.sv
VERILOG_SOURCES += $(TAXI_DIR)/axi/rtl/taxi_axi_register_wr.sv
VERILOG_SOURCES += $(TAXI_DIR)/dma/rtl/taxi_dma_desc_if.sv
VERILOG_SOURCES += $(TAXI_DIR)/dma/rtl/taxi_axi_dma_rd.sv
VERILOG_SOURCES += $(TAXI_DIR)/dma/rtl/taxi_axi_dma_wr.sv
VERILOG_SOURCES += $(TAXI_DIR)/dma/rtl/taxi_axi_dma.sv
VERILOG_SOURCES += $(CORE_DIR)/openenoc_peer_lookup_if.sv
VERILOG_SOURCES += $(CORE_DIR)/openenoc_dma_transfer_if.sv
VERILOG_SOURCES += $(CORE_DIR)/openenoc_irq_event_if.sv
VERILOG_SOURCES += $(CORE_DIR)/openenoc_cpuif_if.sv
VERILOG_SOURCES += $(CORE_DIR)/$(DUT).sv
VERILOG_SOURCES += $(COCOTB_TOPLEVEL).sv

export PARAM_NUM_OF_PEERS := 4
export PARAM_AXI_DATA_W := 32
export PARAM_AXI_ADDR_W := 32
export PARAM_AXI_ID_W := 8
export PARAM_SEQUENCE_W := 32
export PARAM_MAX_RAW_FRAME_SIZE := 96
export PARAM_FRAGMENT_SLOTS := 8

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
