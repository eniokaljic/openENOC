# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: AGPL-3.0-or-later

DV_ROOT := $(abspath $(dir $(lastword $(MAKEFILE_LIST)))/..)
DV_SUITE_DIR := $(abspath $(dir $(firstword $(MAKEFILE_LIST))))
DV_SUITE_PATH := $(patsubst $(DV_ROOT)/%,%,$(DV_SUITE_DIR))
SIM_OUTPUT := $(abspath $(DV_ROOT)/../build/dv/$(DV_SUITE_PATH))
SIM_BUILD := $(SIM_OUTPUT)/sim_build
COCOTB_RESULTS_FILE := $(SIM_BUILD)/results.xml
SIM_ARGS += --trace-file "$(SIM_BUILD)/dump.fst"

export PYTHONPYCACHEPREFIX := $(SIM_OUTPUT)/__pycache__
export TMPDIR := $(SIM_OUTPUT)/tmp

.DEFAULT_GOAL := sim
$(TMPDIR):
	@mkdir -p "$@"

$(SIM_BUILD): | $(TMPDIR)
$(COCOTB_RESULTS_FILE): | $(TMPDIR)
