# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: AGPL-3.0-or-later

TOPLEVEL_LANG = verilog

override SIM := verilator

COCOTB_HDL_TIMEUNIT = 1ns
COCOTB_HDL_TIMEPRECISION = 1ps

# PeakRDL outputs
ENDPOINT = openenoc_endpoint_full
BUILDDIR = $(abspath $(CURDIR)/../../../build/hal)
ENDPOINT_BUILDDIR = $(BUILDDIR)/$(ENDPOINT)
PEAKRDLRTL = $(ENDPOINT_BUILDDIR)/rtl
PEAKRDLPYTHON = $(ENDPOINT_BUILDDIR)/python

# Top-level module
CSR_MODULE = $(ENDPOINT)_csr
TOPLEVEL = test_$(CSR_MODULE)

# RTL sources
VERILOG_SOURCES += $(PEAKRDLRTL)/$(CSR_MODULE)_pkg.sv
VERILOG_SOURCES += $(PEAKRDLRTL)/$(CSR_MODULE).sv
VERILOG_SOURCES += $(CURDIR)/$(TOPLEVEL).sv

# cocotb test module (without .py)
COCOTB_TEST_MODULES = testbench

# Build outputs
SIM_OUTPUT = $(abspath $(CURDIR)/../../../build/dv/hal/$(ENDPOINT))
SIM_BUILD = $(SIM_OUTPUT)/sim_build

# Verilator flags
EXTRA_ARGS += --sv
EXTRA_ARGS += --trace
EXTRA_ARGS += --trace-fst
EXTRA_ARGS += --trace-structs
EXTRA_ARGS += -Wall $(CURDIR)/../../common/config.vlt

# Python path
export PYTHONPATH := $(CURDIR):$(PEAKRDLPYTHON):$(PYTHONPATH)

# cocotb
include $(shell cocotb-config --makefiles)/Makefile.sim

# View waveform
wave:
	gtkwave dump.fst

# Hardware test
hwtest: $(PEAKRDLPYTHON)
	python -m hardware_test

# Extended clean
clean::
	@rm -rf __pycache__
	@rm -f *.pyc
