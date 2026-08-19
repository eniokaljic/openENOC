# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: CERN-OHL-S-2.0

VERBOSE ?= 0
AWK ?= awk
PYTHON ?= python

ifeq ($(VERBOSE),1)
Q :=
else
Q := @
endif

LOG := @printf '  %-37s %s\n'

HAL_DIR     := $(abspath $(dir $(lastword $(MAKEFILE_LIST))))
ENDPOINTS_DIR := $(HAL_DIR)/endpoints
INTERFACES_DIR := $(HAL_DIR)/interfaces
BUILDDIR    := $(abspath $(HAL_DIR)/../build/hal)
DOCSDIR     := $(abspath $(HAL_DIR)/../docs/src/generated)

ENDPOINT_SPECS  := $(sort $(wildcard $(ENDPOINTS_DIR)/*.rdl))
ENDPOINTS       := $(basename $(notdir $(ENDPOINT_SPECS)))
INTERFACE_SPECS := $(sort $(wildcard $(INTERFACES_DIR)/openenoc_*_interface.rdl))
CSR_NAME        := csr

INTERFACE_EXPORTER := $(HAL_DIR)/tools/export_openenoc_if.py
INTERFACE_TEMPLATE := $(HAL_DIR)/templates/openenoc_if.sv.j2
HWIF_HELPER := $(HAL_DIR)/tools/openenoc_hwif.py
BRIDGE_EXPORTER := $(HAL_DIR)/tools/export_openenoc_csr_bridge.py
BRIDGE_TEMPLATE := $(HAL_DIR)/templates/openenoc_csr_bridge.sv.j2
PARAMETER_INJECTOR := $(HAL_DIR)/tools/inject_rdl_parameters.py

ENDPOINT_HEADERS     := $(foreach endpoint,$(ENDPOINTS),$(BUILDDIR)/$(endpoint)/sw/$(CSR_NAME).h)
ENDPOINT_MEMORY_MAPS := $(foreach endpoint,$(ENDPOINTS),$(BUILDDIR)/$(endpoint)/sw/memory_map.h)
ENDPOINT_RTL         := $(foreach endpoint,$(ENDPOINTS),$(BUILDDIR)/$(endpoint)/rtl/$(endpoint)_$(CSR_NAME).sv)
ENDPOINT_CSR_PKGS    := $(foreach endpoint,$(ENDPOINTS),$(BUILDDIR)/$(endpoint)/rtl/$(endpoint)_$(CSR_NAME)_pkg.sv)
ENDPOINT_CSR_BRIDGES := $(foreach endpoint,$(ENDPOINTS),$(BUILDDIR)/$(endpoint)/rtl/$(endpoint)_$(CSR_NAME)_bridge.sv)
ENDPOINT_CONFIG_PKGS := $(foreach endpoint,$(ENDPOINTS),$(BUILDDIR)/$(endpoint)/rtl/$(endpoint)_pkg.sv)
ENDPOINT_PYTHON      := $(foreach endpoint,$(ENDPOINTS),$(BUILDDIR)/$(endpoint)/python/$(CSR_NAME)/__init__.py)
ENDPOINT_HTML        := $(foreach endpoint,$(ENDPOINTS),$(BUILDDIR)/$(endpoint)/html/index.html)
ENDPOINT_MARKDOWN    := $(foreach endpoint,$(ENDPOINTS),$(BUILDDIR)/$(endpoint)/markdown/$(endpoint).md)
INTERFACE_MARKDOWN   := $(patsubst $(INTERFACES_DIR)/%.rdl,$(DOCSDIR)/%.md,$(INTERFACE_SPECS))
PROJECT_INTERFACES   := $(patsubst $(INTERFACES_DIR)/openenoc_%_interface.rdl,$(BUILDDIR)/rtl/openenoc_%_if.sv,$(INTERFACE_SPECS))

.PHONY: all interfaces bridges unittest clean help awk-tool-check

all: $(PROJECT_INTERFACES) $(ENDPOINT_HEADERS) $(ENDPOINT_MEMORY_MAPS) $(ENDPOINT_RTL) $(ENDPOINT_CSR_PKGS) $(ENDPOINT_CSR_BRIDGES) $(ENDPOINT_CONFIG_PKGS) $(ENDPOINT_PYTHON) $(ENDPOINT_HTML) $(ENDPOINT_MARKDOWN) $(INTERFACE_MARKDOWN)

$(BUILDDIR)/rtl/openenoc_%_if.sv: $(INTERFACES_DIR)/openenoc_%_interface.rdl $(INTERFACE_EXPORTER) $(INTERFACE_TEMPLATE) $(HWIF_HELPER)
	$(LOG) 'Generating project RTL interface:' '$@'
	$(Q)mkdir -p $(dir $@)
	$(Q)$(PYTHON) -B $(INTERFACE_EXPORTER) -I $(INTERFACES_DIR) $< \
		--top openenoc_$*_interface_top \
		--component openenoc_$*_interface \
		--interface-name openenoc_$*_if \
		-o $@

define ENDPOINT_RULES
$(BUILDDIR)/$(1)/sw/$(CSR_NAME).h: $(ENDPOINTS_DIR)/$(1).rdl $(INTERFACE_SPECS) $(PARAMETER_INJECTOR) $(HWIF_HELPER)
	$(LOG) 'Generating C CSR header:' '$$@'
	$(Q)mkdir -p $$(dir $$@)
	$(Q)$$(RM) -r $$@.tmp.dir
	$(Q)mkdir -p $$@.tmp.dir
	$(Q)peakrdl c-header -I $(INTERFACES_DIR) $$< -b ltoh -o $$@.tmp.dir/$(CSR_NAME).h --type-style hier --top $(CSR_NAME)
	$(Q)$(PYTHON) -B $(PARAMETER_INJECTOR) -I $(INTERFACES_DIR) $$< \
		--top $(CSR_NAME) \
		--header $$@.tmp.dir/$(CSR_NAME).h \
		-o $$@
	$(Q)$$(RM) -r $$@.tmp.dir

$(BUILDDIR)/$(1)/rtl/$(1)_$(CSR_NAME).sv $(BUILDDIR)/$(1)/rtl/$(1)_$(CSR_NAME)_pkg.sv &: $(ENDPOINTS_DIR)/$(1).rdl $(INTERFACE_SPECS)
	$(LOG) 'Generating CSR RTL files in:' '$(BUILDDIR)/$(1)/rtl'
	$(Q)mkdir -p $(BUILDDIR)/$(1)/rtl
	$(Q)peakrdl regblock -I $(INTERFACES_DIR) $$< -o $(BUILDDIR)/$(1)/rtl --cpuif axi4-lite-flat --top $(CSR_NAME) --rename $(1)_$(CSR_NAME)

$(BUILDDIR)/$(1)/rtl/$(1)_$(CSR_NAME)_bridge.sv: $(ENDPOINTS_DIR)/$(1).rdl $(INTERFACE_SPECS) $(BUILDDIR)/$(1)/rtl/$(1)_$(CSR_NAME)_pkg.sv $(PROJECT_INTERFACES) $(BRIDGE_EXPORTER) $(BRIDGE_TEMPLATE) $(HWIF_HELPER)
	$(LOG) 'Generating endpoint CSR bridge:' '$$@'
	$(Q)mkdir -p $$(dir $$@)
	$(Q)$(PYTHON) -B $(BRIDGE_EXPORTER) -I $(INTERFACES_DIR) $$< \
		--top $(CSR_NAME) \
		--module-name $(1)_$(CSR_NAME) \
		-o $$@

$(BUILDDIR)/$(1)/rtl/$(1)_pkg.sv: $(ENDPOINTS_DIR)/$(1).rdl $(INTERFACE_SPECS)
	$(LOG) 'Generating endpoint RTL package:' '$$@'
	$(Q)mkdir -p $$(dir $$@)
	$(Q)$$(RM) $$@.tmp
	$(Q)$$(RM) -r $$@.tmp.dir
	$(Q)peakrdl regblock -I $(INTERFACES_DIR) $$< -o $$@.tmp.dir --cpuif axi4-lite-flat --top $(1) --module-name $(1) --package-name $(1)_pkg --type-style hier
	$(Q)mv $$@.tmp.dir/$(1)_pkg.sv $$@.tmp
	$(Q)$$(RM) -r $$@.tmp.dir
	$(Q)mv $$@.tmp $$@

$(BUILDDIR)/$(1)/sw/memory_map.h: $(BUILDDIR)/$(1)/rtl/$(1)_pkg.sv | awk-tool-check
	$(LOG) 'Generating SW memory map:' '$$@'
	$(Q)mkdir -p $$(dir $$@)
	$(Q)$$(RM) $$@.tmp
	$(Q)$(AWK) 'BEGIN { \
		wanted["IMEM_DEPTH"] = 1; \
		wanted["IMEM_BASE_ADDR"] = 1; \
		wanted["DMEM_DEPTH"] = 1; \
		wanted["DMEM_BASE_ADDR"] = 1; \
		wanted["CSR_BASE_ADDR"] = 1; \
		print "/* Generated from the endpoint SystemRDL address map. */"; \
		print "#ifndef MEMORY_MAP_H"; \
		print "#define MEMORY_MAP_H"; \
		print ""; \
	} \
	$$$$1 == "localparam" && ($$$$2 in wanted) { \
		value = $$$$4; \
		sub(/;$$$$/, "", value); \
		sub(/^\047h/, "0x", value); \
		printf "#define %-19s %s\n", $$$$2, value; \
		found[$$$$2] = 1; \
		count++; \
	} \
	END { \
		if (count != 5) { \
			print "Expected endpoint memory-map parameters were not found" > "/dev/stderr"; \
			exit 1; \
		} \
		print "#define IMEM_SIZE_BYTES     (IMEM_DEPTH * 4)"; \
		print "#define DMEM_SIZE_BYTES     (DMEM_DEPTH * 4)"; \
		print ""; \
		print "#endif /* MEMORY_MAP_H */"; \
	}' $$< > $$@.tmp
	$(Q)mv $$@.tmp $$@

$(BUILDDIR)/$(1)/python/$(CSR_NAME)/__init__.py: $(ENDPOINTS_DIR)/$(1).rdl $(INTERFACE_SPECS)
	$(LOG) 'Generating Python CSR model in:' '$(BUILDDIR)/$(1)/python/csr'
	$(Q)mkdir -p $(BUILDDIR)/$(1)/python
	$(Q)peakrdl python -I $(INTERFACES_DIR) $$< -t $(CSR_NAME) -o $(BUILDDIR)/$(1)/python

$(BUILDDIR)/$(1)/html/index.html: $(ENDPOINTS_DIR)/$(1).rdl $(INTERFACE_SPECS)
	$(LOG) 'Generating HTML CSR docs in:' '$(BUILDDIR)/$(1)/html'
	$(Q)mkdir -p $(BUILDDIR)/$(1)
	$(Q)peakrdl html -I $(INTERFACES_DIR) $$< -o $(BUILDDIR)/$(1)/html --top $(CSR_NAME)

$(BUILDDIR)/$(1)/markdown/$(1).md: $(ENDPOINTS_DIR)/$(1).rdl $(INTERFACE_SPECS)
	$(LOG) 'Generating endpoint Markdown docs:' '$$@'
	$(Q)mkdir -p $$(dir $$@)
	$(Q)peakrdl markdown -I $(INTERFACES_DIR) $$< -o $$@ --top $(1)

.PHONY: unittest-$(1)
unittest-$(1): $(BUILDDIR)/$(1)/python/$(CSR_NAME)/__init__.py
	$(LOG) 'Running generated CSR unit tests in:' '$(BUILDDIR)/$(1)/python/$(CSR_NAME)/tests'
	$(Q)python -W ignore::DeprecationWarning -m unittest discover -s $(BUILDDIR)/$(1)/python/$(CSR_NAME)/tests -t $(BUILDDIR)/$(1)/python -v
endef

$(foreach endpoint,$(ENDPOINTS),$(eval $(call ENDPOINT_RULES,$(endpoint))))

awk-tool-check:
	$(Q)command -v $(AWK) >/dev/null 2>&1 || { \
		echo "Missing tool: $(AWK)" >&2; \
		exit 1; \
	}
	$(LOG) 'Using AWK processing tool:' "$$(command -v $(AWK))"

$(DOCSDIR)/%.md: $(INTERFACES_DIR)/%.rdl
	$(LOG) 'Generating interface Markdown docs:' '$@'
	$(Q)mkdir -p $(DOCSDIR)
	$(Q)peakrdl markdown $< -o $@ --top $*_top

unittest: $(addprefix unittest-,$(ENDPOINTS))

help:
	$(Q)echo "Usage: make [target] [variables...]"
	$(Q)echo
	$(Q)echo "Targets:"
	$(Q)echo "  all       Generate HAL RTL, C API, Python models, interfaces, bridges and documentation"
	$(Q)echo "  unittest  Run generated CSR model unit tests"
	$(Q)echo "  clean     Remove generated HAL and interface documentation outputs"
	$(Q)echo "  help      Show this message"
	$(Q)echo
	$(Q)echo "Variables:"
	$(Q)echo "  AWK       AWK-compatible executable (default: awk)"
	$(Q)echo "  PYTHON    Python executable used by the interface exporter (default: python)"
	$(Q)echo "  VERBOSE   Command output mode: 0 hides commands, 1 prints them (default: 0)"

clean:
	$(LOG) 'Removing project RTL interfaces from:' '$(BUILDDIR)/rtl'
	$(Q)$(RM) $(PROJECT_INTERFACES)
	$(LOG) 'Removing endpoint HAL output from:' '$(BUILDDIR)'
	$(Q)rm -rf $(foreach endpoint,$(ENDPOINTS),$(BUILDDIR)/$(endpoint))
	$(LOG) 'Removing generated docs from:' '$(DOCSDIR)'
	$(Q)rm -f $(INTERFACE_MARKDOWN)
