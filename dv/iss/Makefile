# SPDX-FileCopyrightText: 2026 Kerim Bavcic
# SPDX-License-Identifier: AGPL-3.0-or-later

.DEFAULT_GOAL := check

PYTHON ?= python3
CC ?= cc
CXX ?= c++
JOBS ?= 1

ISS_DIR := $(abspath $(dir $(lastword $(MAKEFILE_LIST))))
ROOT_DIR := $(abspath $(ISS_DIR)/../..)
SPIKE_SRC := $(ROOT_DIR)/libs/riscv-isa-sim
BUILD_DIR := $(ROOT_DIR)/build/dv/iss
SPIKE_BUILD_DIR := $(BUILD_DIR)/spike-build
SPIKE_INSTALL_DIR := $(BUILD_DIR)/spike-install
NATIVE_BUILD_DIR := $(BUILD_DIR)/native
ISS_LIB_DIR := $(BUILD_DIR)/lib
ISS_LIBRARY := $(ISS_LIB_DIR)/libopenenoc_iss.so
PYTHON_PACKAGE_DIR := $(ISS_DIR)/python
FIRMWARE_BIN := $(ROOT_DIR)/build/sw/openenoc_endpoint_full/csr_smoke.bin
SPIKE_COMMIT := $(shell $(PYTHON) -c 'import json; print(json.load(open("$(ISS_DIR)/compatibility.json"))["spike"]["commit"])')

.PHONY: c-api-smoke check check-all check-submodule clean configure firmware install iss-library link-smoke processor-smoke python-smoke rtl-firmware-smoke rtl-smoke spike test-native

check: test-native python-smoke

check-submodule:
	@test -f $(SPIKE_SRC)/configure || { \
		echo "Spike submodule is missing; run: git submodule update --init libs/riscv-isa-sim" >&2; \
		exit 1; \
	}
	@actual=$$(git -C $(SPIKE_SRC) rev-parse HEAD); \
	if test "$$actual" != "$(SPIKE_COMMIT)"; then \
		echo "Spike commit mismatch: expected $(SPIKE_COMMIT), found $$actual" >&2; \
		exit 1; \
	fi

$(SPIKE_BUILD_DIR)/Makefile: | check-submodule
	@mkdir -p $(SPIKE_BUILD_DIR) $(SPIKE_INSTALL_DIR)
	@cd $(SPIKE_BUILD_DIR) && \
		$(SPIKE_SRC)/configure --prefix=$(SPIKE_INSTALL_DIR)

configure: $(SPIKE_BUILD_DIR)/Makefile

$(SPIKE_INSTALL_DIR)/bin/spike: $(SPIKE_BUILD_DIR)/Makefile
	@$(MAKE) -C $(SPIKE_BUILD_DIR) -j$(JOBS)
	@$(MAKE) -C $(SPIKE_BUILD_DIR) install

spike install: check-submodule $(SPIKE_INSTALL_DIR)/bin/spike
	@$(SPIKE_INSTALL_DIR)/bin/spike --help >/dev/null 2>&1

$(NATIVE_BUILD_DIR)/openenoc_iss_link_smoke: tests/native/link_smoke.cpp $(SPIKE_INSTALL_DIR)/bin/spike
	@mkdir -p $(NATIVE_BUILD_DIR)
	@$(CXX) $(CPPFLAGS) $(CXXFLAGS) -std=c++20 -Wall -Wextra \
		-I$(SPIKE_INSTALL_DIR)/include $< \
		$(LDFLAGS) -L$(SPIKE_INSTALL_DIR)/lib \
		-Wl,-rpath,$(SPIKE_INSTALL_DIR)/lib \
		$(LDLIBS) -lriscv -o $@

link-smoke: check-submodule $(NATIVE_BUILD_DIR)/openenoc_iss_link_smoke
	@LD_LIBRARY_PATH=$(SPIKE_INSTALL_DIR)/lib$${LD_LIBRARY_PATH:+:$$LD_LIBRARY_PATH} \
		$(NATIVE_BUILD_DIR)/openenoc_iss_link_smoke

$(NATIVE_BUILD_DIR)/openenoc_iss_processor_smoke: tests/native/processor_smoke.cpp $(SPIKE_INSTALL_DIR)/bin/spike
	@mkdir -p $(NATIVE_BUILD_DIR)
	@$(CXX) $(CPPFLAGS) $(CXXFLAGS) -std=c++20 -Wall -Wextra \
		-I$(SPIKE_INSTALL_DIR)/include $< \
		$(LDFLAGS) -L$(SPIKE_INSTALL_DIR)/lib \
		-Wl,-rpath,$(SPIKE_INSTALL_DIR)/lib \
		$(LDLIBS) -lriscv -o $@

processor-smoke: check-submodule $(NATIVE_BUILD_DIR)/openenoc_iss_processor_smoke
	@LD_LIBRARY_PATH=$(SPIKE_INSTALL_DIR)/lib$${LD_LIBRARY_PATH:+:$$LD_LIBRARY_PATH} \
		$(NATIVE_BUILD_DIR)/openenoc_iss_processor_smoke

$(ISS_LIBRARY): src/openenoc_iss.cpp include/openenoc_iss.h $(SPIKE_INSTALL_DIR)/bin/spike
	@mkdir -p $(ISS_LIB_DIR)
	@$(CXX) $(CPPFLAGS) $(CXXFLAGS) -std=c++20 -Wall -Wextra -fPIC -shared -pthread \
		-Iinclude -I$(SPIKE_INSTALL_DIR)/include $< \
		$(LDFLAGS) -L$(SPIKE_INSTALL_DIR)/lib \
		-Wl,-rpath,$(SPIKE_INSTALL_DIR)/lib \
		$(LDLIBS) -lriscv -o $@

iss-library: check-submodule $(ISS_LIBRARY)

$(NATIVE_BUILD_DIR)/openenoc_iss_c_api_smoke: tests/native/c_api_smoke.c include/openenoc_iss.h $(ISS_LIBRARY)
	@mkdir -p $(NATIVE_BUILD_DIR)
	@$(CC) $(CPPFLAGS) $(CFLAGS) -std=c11 -Wall -Wextra \
		-Iinclude $< $(LDFLAGS) -L$(ISS_LIB_DIR) \
		-Wl,-rpath,$(ISS_LIB_DIR) $(LDLIBS) -lopenenoc_iss -o $@

c-api-smoke: check-submodule $(NATIVE_BUILD_DIR)/openenoc_iss_c_api_smoke
	@$(NATIVE_BUILD_DIR)/openenoc_iss_c_api_smoke

test-native: link-smoke processor-smoke c-api-smoke

python-smoke: iss-library
	@PYTHONPATH=$(PYTHON_PACKAGE_DIR) \
		OPENENOC_ISS_LIBRARY=$(ISS_LIBRARY) \
		$(PYTHON) -m unittest discover -s tests/python -p 'test_*.py'

rtl-smoke: iss-library
	@$(MAKE) -C tests/rtl COCOTB_TESTCASE=test_spike_accesses_rtl_dmem

firmware:
	@$(MAKE) -C $(ROOT_DIR)/sw APP=csr_smoke EP=openenoc_endpoint_full
	@test -f $(FIRMWARE_BIN)

rtl-firmware-smoke: iss-library firmware
	@$(MAKE) -C tests/rtl COCOTB_TESTCASE=test_spike_runs_csr_smoke_firmware

check-all: check rtl-smoke rtl-firmware-smoke

clean:
	@$(MAKE) -C tests/rtl clean >/dev/null 2>&1 || true
	@$(RM) -r $(BUILD_DIR)