# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: AGPL-3.0-or-later

.DEFAULT_GOAL := all

VERBOSE ?= 0
CC = gcc
TIMEOUT ?= timeout
TEST_TIMEOUT ?= 10s

ifeq ($(VERBOSE), 1)
	Q :=
else
	Q := @
endif

LOG := @printf '  %-37s %s\n'

TEST_DIR := $(abspath $(dir $(lastword $(MAKEFILE_LIST))))
ROOT_DIR := $(abspath $(TEST_DIR)/../../..)
HAL_DIR := $(ROOT_DIR)/hal
HAL_LIB_DIR := $(ROOT_DIR)/sw/lib/hal
PLATFORM_DIR := $(ROOT_DIR)/sw/platform/picorv32
HAL_BUILD_DIR := $(ROOT_DIR)/build/hal/openenoc_endpoint_full/sw

BUILD_ROOT ?= $(ROOT_DIR)/build/dv/sw
OUTPUT_DIR := $(abspath $(BUILD_ROOT))/openenoc_endpoint_irq

CSR_HEADER := $(HAL_BUILD_DIR)/csr.h
EP_SPEC := $(HAL_DIR)/endpoints/openenoc_endpoint_full.rdl
RDL_INCLUDES := $(sort $(wildcard $(HAL_DIR)/interfaces/*.rdl))
HAL_SOURCE := $(HAL_LIB_DIR)/openenoc_endpoint_irq.c
HAL_HEADER := $(HAL_LIB_DIR)/openenoc_endpoint_irq.h
PLATFORM_SOURCE := $(PLATFORM_DIR)/irq.c
PLATFORM_HEADER := $(PLATFORM_DIR)/irq.h

PLATFORM_TEST := $(OUTPUT_DIR)/test_openenoc_endpoint_irq
PORTABLE_TEST := $(OUTPUT_DIR)/test_openenoc_endpoint_irq_portable
TESTS := $(PLATFORM_TEST) $(PORTABLE_TEST)

COMMON_CPPFLAGS := -I$(HAL_BUILD_DIR) -I$(HAL_LIB_DIR)
COMMON_CFLAGS := -std=c11 -O2 -Wall -Wextra -Werror

.PHONY: all build test clean help force-rebuild toolchain-check test-tool-check

all: test

build: $(TESTS)

test: build | test-tool-check
	$(LOG) 'Running host IRQ test:' '$(notdir $(PLATFORM_TEST))'
	$(Q)$(TIMEOUT) $(TEST_TIMEOUT) $(PLATFORM_TEST)
	$(LOG) 'Running host IRQ test:' '$(notdir $(PORTABLE_TEST))'
	$(Q)$(TIMEOUT) $(TEST_TIMEOUT) $(PORTABLE_TEST)
	$(LOG) 'Host IRQ tests passed:' '2/2'

force-rebuild:

toolchain-check:
	$(Q)command -v $(CC) >/dev/null 2>&1 || { \
		echo "Missing tool: $(CC)" >&2; exit 1; \
	}

test-tool-check:
	$(Q)command -v $(TIMEOUT) >/dev/null 2>&1 || { \
		echo "Missing tool: $(TIMEOUT)" >&2; exit 1; \
	}

$(CSR_HEADER): $(EP_SPEC) $(RDL_INCLUDES)
	$(LOG) 'Generating HAL software header:' '$@'
	$(Q)$(MAKE) --no-print-directory -C $(HAL_DIR) VERBOSE=$(VERBOSE) $@
	$(Q)test -f $@ || { echo "HAL generation did not create $@" >&2; exit 1; }

$(PLATFORM_TEST): \
	force-rebuild \
	$(TEST_DIR)/test_openenoc_endpoint_irq.c \
	$(HAL_SOURCE) \
	$(HAL_HEADER) \
	$(PLATFORM_SOURCE) \
	$(PLATFORM_HEADER) \
	$(CSR_HEADER) \
	| toolchain-check
	$(LOG) 'Building host IRQ test:' '$@'
	$(Q)mkdir -p $(dir $@)
	$(Q)$(CC) $(COMMON_CPPFLAGS) -I$(PLATFORM_DIR) $(CPPFLAGS) \
		$(COMMON_CFLAGS) $(CFLAGS) $(LDFLAGS) -o $@ \
		$(TEST_DIR)/test_openenoc_endpoint_irq.c $(HAL_SOURCE) $(PLATFORM_SOURCE) $(LDLIBS)

$(PORTABLE_TEST): \
	force-rebuild \
	$(TEST_DIR)/test_openenoc_endpoint_irq_portable.c \
	$(HAL_SOURCE) \
	$(HAL_HEADER) \
	$(CSR_HEADER) \
	| toolchain-check
	$(LOG) 'Building portable IRQ HAL test:' '$@'
	$(Q)mkdir -p $(dir $@)
	$(Q)$(CC) $(COMMON_CPPFLAGS) $(CPPFLAGS) $(COMMON_CFLAGS) $(CFLAGS) \
		$(LDFLAGS) -o $@ $(TEST_DIR)/test_openenoc_endpoint_irq_portable.c \
		$(HAL_SOURCE) $(LDLIBS)

clean::
	$(LOG) 'Removing host IRQ test output from:' '$(OUTPUT_DIR)'
	$(Q)$(RM) -r $(OUTPUT_DIR)

help:
	$(Q)echo "Usage: make [target] [variables...]"
	$(Q)echo
	$(Q)echo "Targets:"
	$(Q)echo "  all    Build and run both host IRQ tests (default)"
	$(Q)echo "  build  Build both host IRQ test executables"
	$(Q)echo "  test   Build and run both host IRQ tests"
	$(Q)echo "  clean  Remove this suite's build outputs"
	$(Q)echo "  help   Show this message"
	$(Q)echo
	$(Q)echo "Variables:"
	$(Q)echo "  CC            Native C compiler (default: gcc)"
	$(Q)echo "  BUILD_ROOT    Test output root (default: $(ROOT_DIR)/build/dv/sw)"
	$(Q)echo "  TEST_TIMEOUT  Per-test execution timeout (default: 10s)"
	$(Q)echo "  VERBOSE       Print build and test commands when set to 1"

# Extended clean
clean::
	@rm -rf __pycache__
	@rm -f *.pyc
