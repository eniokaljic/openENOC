# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: AGPL-3.0-or-later

.DEFAULT_GOAL := all

VERBOSE ?= 0
AWK ?= awk

ifeq ($(VERBOSE),1)
Q :=
else
Q := @
endif

LOG := @printf '  %-37s %s\n'

SW_DIR := $(abspath $(dir $(lastword $(MAKEFILE_LIST))))
ROOT_DIR := $(abspath $(SW_DIR)/..)

APPS_DIR := $(SW_DIR)/apps
LIB_DIR := $(SW_DIR)/lib
LIB_DIRS := $(wildcard $(LIB_DIR)/*)
PLATFORMS_DIR := $(SW_DIR)/platform
HAL_DIR := $(ROOT_DIR)/hal
HAL_EPS_DIR := $(HAL_DIR)/endpoints
HAL_INCLUDE_DIR := $(HAL_DIR)/interfaces
HAL_BUILD_DIR := $(ROOT_DIR)/build/hal

APP ?=
EP ?=
PLATFORM ?= picorv32
BUILD_ROOT ?= $(ROOT_DIR)/build/sw
BUILD_ROOT_ABS := $(abspath $(BUILD_ROOT))

CROSS_COMPILE ?= riscv64-unknown-elf-
MARCH ?= rv32i
MABI ?= ilp32

CC = $(CROSS_COMPILE)gcc
OBJCOPY = $(CROSS_COMPILE)objcopy
OBJDUMP = $(CROSS_COMPILE)objdump
SIZE = $(CROSS_COMPILE)size
XXD ?= xxd

AVAILABLE_EPS := $(basename $(notdir $(sort $(wildcard $(HAL_EPS_DIR)/*.rdl))))

COMMON_CPPFLAGS := \
	-I$(PLATFORMS_DIR)/$(PLATFORM)/include \
	-I$(HAL_BUILD_DIR)/$(EP)/sw \
	$(addprefix -I,$(LIB_DIRS))

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
ifeq ($(wildcard $(PLATFORMS_DIR)/$(PLATFORM)/sections.lds.in),)
$(error Platform '$(PLATFORM)' does not provide sections.lds.in)
endif
ifeq ($(wildcard $(HAL_EPS_DIR)/$(EP).rdl),)
$(error Endpoint '$(EP)' does not provide $(HAL_EPS_DIR)/$(EP).rdl)
endif
endif

APP_DIR := $(APPS_DIR)/$(APP)
PLATFORM_DIR := $(PLATFORMS_DIR)/$(PLATFORM)
LINKER_SCRIPT_TEMPLATE := $(PLATFORM_DIR)/sections.lds.in
EP_SPEC := $(HAL_EPS_DIR)/$(EP).rdl
RDL_INCLUDES := $(sort $(wildcard $(HAL_INCLUDE_DIR)/*.rdl))
CSR_HEADER := $(HAL_BUILD_DIR)/$(EP)/sw/csr.h
MEMORY_MAP_HEADER := $(HAL_BUILD_DIR)/$(EP)/sw/memory_map.h
HAL_SW_HEADERS := $(CSR_HEADER) $(MEMORY_MAP_HEADER)

APP_C_SOURCES := $(wildcard $(APP_DIR)/*.c)
APP_S_SOURCES := $(wildcard $(APP_DIR)/*.s)
APP_CAP_S_SOURCES := $(wildcard $(APP_DIR)/*.S)

PLATFORM_C_SOURCES := $(wildcard $(PLATFORM_DIR)/*.c)
PLATFORM_S_SOURCES := $(wildcard $(PLATFORM_DIR)/*.s)
PLATFORM_CAP_S_SOURCES := $(wildcard $(PLATFORM_DIR)/*.S)

LIB_C_SOURCES := $(wildcard $(LIB_DIR)/*/*.c)
LIB_S_SOURCES := $(wildcard $(LIB_DIR)/*/*.s)
LIB_CAP_S_SOURCES := $(wildcard $(LIB_DIR)/*/*.S)

C_SOURCES := $(sort $(APP_C_SOURCES) $(PLATFORM_C_SOURCES) $(LIB_C_SOURCES))
S_SOURCES := $(sort $(APP_S_SOURCES) $(PLATFORM_S_SOURCES) $(LIB_S_SOURCES))
CAP_S_SOURCES := $(sort $(APP_CAP_S_SOURCES) $(PLATFORM_CAP_S_SOURCES) $(LIB_CAP_S_SOURCES))
SOURCES := $(C_SOURCES) $(S_SOURCES) $(CAP_S_SOURCES)

OUTPUT_DIR := $(BUILD_ROOT_ABS)/$(EP)
OUTPUT_BASE := $(OUTPUT_DIR)/$(APP)
LINKER_SCRIPT := $(OUTPUT_DIR)/sections.lds

ELF := $(OUTPUT_BASE).elf
BIN := $(OUTPUT_BASE).bin
HEX := $(OUTPUT_BASE).hex
MAP := $(OUTPUT_BASE).map
LISTING := $(OUTPUT_BASE).lst
IMEM_MEM := $(OUTPUT_DIR)/imem.mem

.PHONY: all clean force-rebuild help imem-init imem-tool-check list-apps list-eps toolchain-check

all: $(ELF) $(BIN) $(HEX) $(LISTING) $(IMEM_MEM)
	$(LOG) 'Reporting firmware size for:' '$(ELF)'
	$(Q)$(SIZE) $(ELF)

force-rebuild:

toolchain-check:
	$(LOG) 'Checking RISC-V build tools:' '$(CC), $(OBJCOPY), $(OBJDUMP), $(SIZE)'
	$(Q)for tool in $(CC) $(OBJCOPY) $(OBJDUMP) $(SIZE); do \
		command -v $$tool >/dev/null 2>&1 || { \
			echo "Missing tool: $$tool" >&2; \
			exit 1; \
		}; \
	done

imem-tool-check:
	$(Q)for tool in $(XXD) $(AWK); do \
		command -v $$tool >/dev/null 2>&1 || { \
			echo "Missing tool: $$tool" >&2; \
			exit 1; \
		}; \
	done
	$(LOG) 'Using IMEM conversion tool:' "$$(command -v $(XXD))"
	$(LOG) 'Using AWK processing tool:' "$$(command -v $(AWK))"

$(HAL_SW_HEADERS): $(EP_SPEC) $(RDL_INCLUDES)
	$(LOG) 'Generating HAL software header:' '$@'
	$(Q)$(MAKE) --no-print-directory -C $(HAL_DIR) VERBOSE=$(VERBOSE) AWK=$(AWK) $@
	$(Q)test -f $@ || { echo "HAL generation did not create $@" >&2; exit 1; }

$(LINKER_SCRIPT): $(LINKER_SCRIPT_TEMPLATE) $(MEMORY_MAP_HEADER) | toolchain-check
	$(LOG) 'Generating linker script:' '$@'
	$(Q)mkdir -p $(dir $@)
	$(Q)$(RM) $@.tmp
	$(Q)$(CC) -E -P -x c $(COMMON_CPPFLAGS) $(CPPFLAGS) $< -o $@.tmp
	$(Q)mv $@.tmp $@

$(ELF): force-rebuild $(SOURCES) $(HAL_SW_HEADERS) $(LINKER_SCRIPT) | toolchain-check
	$(LOG) 'Linking firmware ELF:' '$@'
	$(Q)mkdir -p $(dir $@)
	$(Q)$(CC) $(COMMON_CPPFLAGS) $(CPPFLAGS) $(COMMON_CFLAGS) $(CFLAGS) \
		$(COMMON_LDFLAGS) $(LDFLAGS) \
		-Wl,-T,$(LINKER_SCRIPT),-Map,$(MAP) \
		-o $@ $(SOURCES) $(LDLIBS) -lgcc

$(BIN): $(ELF)
	$(LOG) 'Generating raw binary image:' '$@'
	$(Q)$(OBJCOPY) -O binary $< $@

$(HEX): $(ELF)
	$(LOG) 'Generating Verilog HEX image:' '$@'
	$(Q)$(OBJCOPY) -O verilog $< $@

$(LISTING): $(ELF)
	$(LOG) 'Generating disassembly listing:' '$@'
	$(Q)$(OBJDUMP) -drwC -S $< > $@

$(IMEM_MEM): $(BIN) $(MEMORY_MAP_HEADER) | imem-tool-check
	$(LOG) 'Generating IMEM initialization file:' '$@'
	$(Q)imem_depth=$$($(AWK) \
		'$$1 == "#define" && $$2 == "IMEM_DEPTH" { print $$3 }' \
		$(MEMORY_MAP_HEADER)); \
	if test -z "$$imem_depth"; then \
		echo "IMEM_DEPTH is missing from $(MEMORY_MAP_HEADER)" >&2; \
		exit 1; \
	fi; \
	imem_depth_value=$$((imem_depth)); \
	byte_count=$$(wc -c < $<); \
	if test $$((byte_count % 4)) -ne 0; then \
		echo "IMEM image size must be aligned to four bytes" >&2; \
		exit 1; \
	fi; \
	word_count=$$((byte_count / 4)); \
	if test $$word_count -gt $$imem_depth_value; then \
		echo "IMEM image has $$word_count words; limit is $$imem_depth_value" >&2; \
		exit 1; \
	fi; \
	$(XXD) -e -g 4 -c 4 $< | \
		$(AWK) '{ print toupper($$2); }' > $@

list-apps:
	$(Q)if test -d $(APPS_DIR); then \
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
	$(Q)if test -n "$(AVAILABLE_EPS)"; then \
		printf '%s\n' $(AVAILABLE_EPS); \
	else \
		echo "No endpoint specifications found under $(HAL_EPS_DIR)"; \
	fi

help:
	$(Q)echo "Usage:"
	$(Q)echo "  Build: make [all] APP=<application> EP=<endpoint> [variables...]"
	$(Q)echo "  Other: make <target> [variables...]"
	$(Q)echo
	$(Q)echo "Targets:"
	$(Q)echo "  list-apps  Print available application directory names"
	$(Q)echo "  list-eps   Print available endpoint names"
	$(Q)echo "  all        Build all software and IMEM initialization artifacts"
	$(Q)echo "  clean      Remove all software build outputs"
	$(Q)echo "  help       Show this message"
	$(Q)echo
	$(Q)echo "Variables:"
	$(Q)echo "  APP             Application directory name under $(APPS_DIR) (required for builds)"
	$(Q)echo "  EP              Endpoint name derived from $(HAL_EPS_DIR)/<endpoint>.rdl (required for builds)"
	$(Q)echo "  PLATFORM        Platform directory name under $(PLATFORMS_DIR) (default: picorv32)"
	$(Q)echo "  MARCH           RISC-V ISA passed to the toolchain (default: rv32i)"
	$(Q)echo "  MABI            RISC-V ABI passed to the toolchain (default: ilp32)"
	$(Q)echo "  CROSS_COMPILE   GNU toolchain command prefix (default: riscv64-unknown-elf-)"
	$(Q)echo "  BUILD_ROOT      Software output directory (default: $(ROOT_DIR)/build/sw)"
	$(Q)echo "  AWK             AWK-compatible executable (default: awk)"
	$(Q)echo "  XXD             Binary-to-hex conversion executable (default: xxd)"
	$(Q)echo "  VERBOSE         Command output mode: 0 hides commands, 1 prints them (default: 0)"

clean:
	$(LOG) 'Removing software build output from:' '$(BUILD_ROOT_ABS)'
	$(Q)$(RM) -r $(BUILD_ROOT_ABS)
