# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: AGPL-3.0-or-later

TOPLEVEL_LANG = verilog
SIM = verilator

#
# RTL sources
#
VERILOG_SOURCES += $(PWD)/../build/rtl/csr_pkg.sv
VERILOG_SOURCES += $(PWD)/../build/rtl/csr.sv
VERILOG_SOURCES += $(PWD)/csr_wrapper.sv

#
# Top-level module
#
TOPLEVEL = csr_wrapper

#
# cocotb test module (without .py)
#
MODULE = Testbench

#
# Verilator flags
#
EXTRA_ARGS += --sv
EXTRA_ARGS += --trace
EXTRA_ARGS += --trace-structs
EXTRA_ARGS += -Wno-fatal

#
# Optional waveform dump
#
PLUSARGS += +trace

#
# Python path
#
export PYTHONPATH := $(PWD):$(PYTHONPATH)

#
# cocotb
#
include $(shell cocotb-config --makefiles)/Makefile.sim

