# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: AGPL-3.0-or-later

TOPLEVEL_LANG = verilog
SIM = verilator

# PeakRDL outputs
BUILDDIR      = $(PWD)/../../../build/hal
PEAKRDLRTL    = $(BUILDDIR)/rtl/
PEAKRDLPYTHON = $(BUILDDIR)/python/

# Top-level module
TOPLEVEL = csr

# RTL sources
VERILOG_SOURCES += $(PEAKRDLRTL)/$(TOPLEVEL)_pkg.sv
VERILOG_SOURCES += $(PEAKRDLRTL)/$(TOPLEVEL).sv

# cocotb test module (without .py)
MODULE = Testbench

# Build outputs
SIM_OUTPUT = $(PWD)/../../../build/dv/component/$(TOPLEVEL)
SIM_BUILD = $(SIM_OUTPUT)/sim_build

# Verilator flags
EXTRA_ARGS += --sv
EXTRA_ARGS += --trace
EXTRA_ARGS += --trace-fst
EXTRA_ARGS += --trace-structs
#EXTRA_ARGS += -Wno-fatal
EXTRA_ARGS += -Wall ../../common/config.vlt

# Python path
export PYTHONPATH := $(PWD):$(PYTHONPATH):$(PEAKRDLPYTHON)

# cocotb
include $(shell cocotb-config --makefiles)/Makefile.sim

# View waveform
wave:
	gtkwave dump.fst

# Hardware test
hwtest: $(PEAKRDLPYTHON)
	python -m HardwareTest

# Extended clean
clean::
	@rm -rf __pycache__
	@rm -f *.pyc
