# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: AGPL-3.0-or-later

.DEFAULT_GOAL := all

SW_DIR := $(abspath $(dir $(lastword $(MAKEFILE_LIST))))
ROOT_DIR := $(abspath $(SW_DIR)/..)

APPS_DIR := $(SW_DIR)/apps
LIB_DIR := $(SW_DIR)/lib
PLATFORMS_DIR := $(SW_DIR)/platform
HAL_DIR := $(ROOT_DIR)/hal
HAL_EPS_DIR := $(HAL_DIR)/ep
HAL_INCLUDE_DIR := $(HAL_DIR)/include
HAL_BUILD_DIR := $(ROOT_DIR)/build/hal

APP ?=
EP ?=
PLATFORM ?= picorv32
BUILD_ROOT ?= $(ROOT_DIR)/build/sw

CROSS_COMPILE ?= riscv64-unknown-elf-
MARCH ?= rv32i
MABI ?= ilp32

CC = $(CROSS_COMPILE)gcc
OBJCOPY = $(CROSS_COMPILE)objcopy
OBJDUMP = $(CROSS_COMPILE)objdump
SIZE = $(CROSS_COMPILE)size
XXD ?= xxd

IMEM_DEPTH ?= 8192

AVAILABLE_EPS := $(basename $(notdir $(sort $(wildcard $(HAL_EPS_DIR)/*.rdl))))

COMMON_CPPFLAGS := \
	-I$(PLATFORMS_DIR)/$(PLATFORM)/include \
	-I$(HAL_BUILD_DIR)/$(EP)/include \
	$(addprefix -I,$(wildcard $(LIB_DIR)/*/include))

COMMON_CFLAGS := \
	-march=$(MARCH) \
	-mabi=$(MABI) \
	-std=c11 \
	-Os \
	-Wall \
	-Wextra \
	-ffreestanding \
	-fno-builtin \
	-fno-common \
	-ffunction-sections \
	-fdata-sections

COMMON_LDFLAGS := \
	-march=$(MARCH) \
	-mabi=$(MABI) \
	-nostdlib \
	-nostartfiles \
	-static \
	-Wl,--build-id=none \
	-Wl,--gc-sections

# APP and EP are intentionally mandatory: the repository assumes neither a
# default application nor a default endpoint.
NON_BUILD_GOALS := help clean list-apps list-eps
REQUESTED_GOALS := $(if $(MAKECMDGOALS),$(MAKECMDGOALS),all)
BUILD_GOALS := $(filter-out $(NON_BUILD_GOALS),$(REQUESTED_GOALS))

ifneq ($(strip $(BUILD_GOALS)),)
ifeq ($(strip $(APP)),)
$(error APP is required; run 'make list-apps')
endif
ifeq ($(strip $(EP)),)
$(error EP is required; run 'make list-eps')
endif
ifneq ($(APP),$(notdir $(APP)))
$(error APP must be a direct child directory name under $(APPS_DIR))
endif
ifneq ($(EP),$(notdir $(EP)))
$(error EP must be an endpoint name listed by 'make list-eps')
endif
ifneq ($(PLATFORM),$(notdir $(PLATFORM)))
$(error PLATFORM must be a direct child directory name under $(PLATFORMS_DIR))
endif
ifeq ($(wildcard $(APPS_DIR)/$(APP)/main.c),)
$(error Application '$(APP)' must provide $(APPS_DIR)/$(APP)/main.c)
endif
ifeq ($(wildcard $(PLATFORMS_DIR)/$(PLATFORM)/sections.lds),)
$(error Platform '$(PLATFORM)' does not provide sections.lds)
endif
ifeq ($(wildcard $(HAL_EPS_DIR)/$(EP).rdl),)
$(error Endpoint '$(EP)' does not provide $(HAL_EPS_DIR)/$(EP).rdl)
endif
endif

APP_DIR := $(APPS_DIR)/$(APP)
PLATFORM_DIR := $(PLATFORMS_DIR)/$(PLATFORM)
LINKER_SCRIPT := $(PLATFORM_DIR)/sections.lds
EP_SPEC := $(HAL_EPS_DIR)/$(EP).rdl
RDL_INCLUDES := $(sort $(wildcard $(HAL_INCLUDE_DIR)/*.rdl))
CSR_HEADER := $(HAL_BUILD_DIR)/$(EP)/include/csr.h

APP_C_SOURCES := $(wildcard $(APP_DIR)/*.c)
APP_S_SOURCES := $(wildcard $(APP_DIR)/*.s)
APP_CAP_S_SOURCES := $(wildcard $(APP_DIR)/*.S)

PLATFORM_C_SOURCES := $(wildcard $(PLATFORM_DIR)/*.c)
PLATFORM_S_SOURCES := $(wildcard $(PLATFORM_DIR)/*.s)
PLATFORM_CAP_S_SOURCES := $(wildcard $(PLATFORM_DIR)/*.S)

LIB_C_SOURCES := $(wildcard $(LIB_DIR)/*/src/*.c)
LIB_S_SOURCES := $(wildcard $(LIB_DIR)/*/src/*.s)
LIB_CAP_S_SOURCES := $(wildcard $(LIB_DIR)/*/src/*.S)

C_SOURCES := $(sort $(APP_C_SOURCES) $(PLATFORM_C_SOURCES) $(LIB_C_SOURCES))
S_SOURCES := $(sort $(APP_S_SOURCES) $(PLATFORM_S_SOURCES) $(LIB_S_SOURCES))
CAP_S_SOURCES := $(sort $(APP_CAP_S_SOURCES) $(PLATFORM_CAP_S_SOURCES) $(LIB_CAP_S_SOURCES))
SOURCES := $(C_SOURCES) $(S_SOURCES) $(CAP_S_SOURCES)

OUTPUT_DIR := $(BUILD_ROOT)/$(EP)
OUTPUT_BASE := $(OUTPUT_DIR)/$(APP)

ELF := $(OUTPUT_BASE).elf
BIN := $(OUTPUT_BASE).bin
HEX := $(OUTPUT_BASE).hex
MAP := $(OUTPUT_BASE).map
LISTING := $(OUTPUT_BASE).lst
IMEM_MEM := $(OUTPUT_DIR)/imem.mem

.PHONY: all clean force-rebuild help imem-init imem-tool-check list-apps list-eps toolchain-check

all: $(ELF) $(BIN) $(HEX) $(LISTING) $(IMEM_MEM)
	$(SIZE) $(ELF)

imem-init: $(IMEM_MEM)

force-rebuild:

toolchain-check:
	@for tool in $(CC) $(OBJCOPY) $(OBJDUMP) $(SIZE); do \
		command -v $$tool >/dev/null 2>&1 || { \
			echo "Missing tool: $$tool" >&2; \
			exit 1; \
		}; \
	done

imem-tool-check:
	@command -v $(XXD) >/dev/null 2>&1 || { \
		echo "Missing tool: $(XXD)" >&2; \
		exit 1; \
	}

$(CSR_HEADER): $(EP_SPEC) $(RDL_INCLUDES)
	$(MAKE) -C $(HAL_DIR) $@
	@test -f $@ || { echo "CSR generation did not create $@" >&2; exit 1; }

$(ELF): force-rebuild $(SOURCES) $(CSR_HEADER) $(LINKER_SCRIPT) | toolchain-check
	@mkdir -p $(dir $@)
	$(CC) $(COMMON_CPPFLAGS) $(CPPFLAGS) $(COMMON_CFLAGS) $(CFLAGS) \
		$(COMMON_LDFLAGS) $(LDFLAGS) \
		-Wl,-T,$(LINKER_SCRIPT),-Map,$(MAP) \
		-o $@ $(SOURCES) $(LDLIBS) -lgcc

$(BIN): $(ELF)
	$(OBJCOPY) -O binary $< $@

$(HEX): $(ELF)
	$(OBJCOPY) -O verilog $< $@

$(LISTING): $(ELF)
	$(OBJDUMP) -drwC -S $< > $@

$(IMEM_MEM): $(BIN) | imem-tool-check
	@byte_count=$$(wc -c < $<); \
	if test $$((byte_count % 4)) -ne 0; then \
		echo "IMEM image size must be aligned to four bytes" >&2; \
		exit 1; \
	fi; \
	word_count=$$((byte_count / 4)); \
	if test $$word_count -gt $(IMEM_DEPTH); then \
		echo "IMEM image has $$word_count words; limit is $(IMEM_DEPTH)" >&2; \
		exit 1; \
	fi; \
	$(XXD) -e -g 4 -c 4 $< | \
		awk '{ print toupper($$2); }' > $@

list-apps:
	@if test -d $(APPS_DIR); then \
		apps=$$(find $(APPS_DIR) -mindepth 2 -maxdepth 2 -type f \
			-name main.c -printf '%h\n' | sed 's|.*/||' | sort); \
		if test -n "$$apps"; then \
			printf '%s\n' "$$apps"; \
		else \
			echo "No applications with main.c found under $(APPS_DIR)"; \
		fi; \
	else \
		echo "No applications with main.c found under $(APPS_DIR)"; \
	fi

list-eps:
	@if test -n "$(AVAILABLE_EPS)"; then \
		printf '%s\n' $(AVAILABLE_EPS); \
	else \
		echo "No endpoint specifications found under $(HAL_EPS_DIR)"; \
	fi

help:
	@echo "Usage: make APP=<application> EP=<endpoint> [PLATFORM=picorv32] [MARCH=rv32i]"
	@echo
	@echo "Targets:"
	@echo "  all        Build all software and IMEM initialization artifacts"
	@echo "  imem-init  Build only the 32-bit \$$readmemh IMEM data file"
	@echo "  list-apps  Print available application directory names"
	@echo "  list-eps   Print available endpoint names"
	@echo "  clean      Remove all software build outputs"
	@echo "  help       Show this message"

clean:
	$(RM) -r $(BUILD_ROOT)
