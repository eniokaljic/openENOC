# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: AGPL-3.0-or-later

TOPLEVEL_LANG = verilog
SIM = verilator

# PeakRDL outputs
ENDPOINT          = openenoc
BUILDDIR          = $(abspath $(CURDIR)/../../../build/hal)
ENDPOINT_BUILDDIR = $(BUILDDIR)/$(ENDPOINT)
PEAKRDLRTL        = $(ENDPOINT_BUILDDIR)/rtl
PEAKRDLPYTHON     = $(ENDPOINT_BUILDDIR)/python

# Top-level module
TOPLEVEL = $(ENDPOINT)_csr

# RTL sources
VERILOG_SOURCES += $(PEAKRDLRTL)/$(TOPLEVEL)_pkg.sv
VERILOG_SOURCES += $(PEAKRDLRTL)/$(TOPLEVEL).sv

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
