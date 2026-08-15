# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: CERN-OHL-S-2.0

HAL_DIR     := $(abspath $(dir $(lastword $(MAKEFILE_LIST))))
ENDPOINTDIR := $(HAL_DIR)/ep
INCLUDEDIR  := $(HAL_DIR)/include
BUILDDIR    := $(abspath $(HAL_DIR)/../build/hal)
DOCSDIR     := $(abspath $(HAL_DIR)/../docs/src/generated)

ENDPOINT_SPECS = $(sort $(wildcard $(ENDPOINTDIR)/*.rdl))
ENDPOINTS      = $(basename $(notdir $(ENDPOINT_SPECS)))
RDL_INCLUDES   = $(sort $(wildcard $(INCLUDEDIR)/*.rdl))

INTERFACES = openenoc_endpoint_interface openenoc_switch_interface
CSR_NAME   = csr

ENDPOINT_HEADERS  = $(foreach endpoint,$(ENDPOINTS),$(BUILDDIR)/$(endpoint)/include/$(CSR_NAME).h)
ENDPOINT_RTL      = $(foreach endpoint,$(ENDPOINTS),$(BUILDDIR)/$(endpoint)/rtl/$(endpoint)_$(CSR_NAME).sv)
ENDPOINT_PYTHON   = $(foreach endpoint,$(ENDPOINTS),$(BUILDDIR)/$(endpoint)/python/$(CSR_NAME)/__init__.py)
ENDPOINT_HTML     = $(foreach endpoint,$(ENDPOINTS),$(BUILDDIR)/$(endpoint)/html/index.html)
ENDPOINT_MARKDOWN = $(foreach endpoint,$(ENDPOINTS),$(BUILDDIR)/$(endpoint)/markdown/$(endpoint).md)
INTERFACE_MARKDOWN = $(foreach interface,$(INTERFACES),$(DOCSDIR)/$(interface).md)

.PHONY: all unittest clean

all: $(ENDPOINT_HEADERS) $(ENDPOINT_RTL) $(ENDPOINT_PYTHON) $(ENDPOINT_HTML) $(ENDPOINT_MARKDOWN) $(INTERFACE_MARKDOWN)

define ENDPOINT_RULES
$(BUILDDIR)/$(1)/include/$(CSR_NAME).h: $(ENDPOINTDIR)/$(1).rdl $(RDL_INCLUDES)
	mkdir -p $$(dir $$@)
	peakrdl c-header -I $(INCLUDEDIR) $$< -b ltoh -o $$@ --type-style hier --top $(CSR_NAME)

$(BUILDDIR)/$(1)/rtl/$(1)_$(CSR_NAME).sv: $(ENDPOINTDIR)/$(1).rdl $(RDL_INCLUDES)
	mkdir -p $(BUILDDIR)/$(1)/rtl
	peakrdl regblock -I $(INCLUDEDIR) $$< -o $(BUILDDIR)/$(1)/rtl --cpuif axi4-lite-flat --top $(CSR_NAME) --rename $(1)_$(CSR_NAME)

$(BUILDDIR)/$(1)/python/$(CSR_NAME)/__init__.py: $(ENDPOINTDIR)/$(1).rdl $(RDL_INCLUDES)
	mkdir -p $(BUILDDIR)/$(1)/python
	peakrdl python -I $(INCLUDEDIR) $$< -t $(CSR_NAME) -o $(BUILDDIR)/$(1)/python

$(BUILDDIR)/$(1)/html/index.html: $(ENDPOINTDIR)/$(1).rdl $(RDL_INCLUDES)
	mkdir -p $(BUILDDIR)/$(1)
	peakrdl html -I $(INCLUDEDIR) $$< -o $(BUILDDIR)/$(1)/html --top $(CSR_NAME)

$(BUILDDIR)/$(1)/markdown/$(1).md: $(ENDPOINTDIR)/$(1).rdl $(RDL_INCLUDES)
	mkdir -p $$(dir $$@)
	peakrdl markdown -I $(INCLUDEDIR) $$< -o $$@ --top $(1)

.PHONY: unittest-$(1)
unittest-$(1): $(BUILDDIR)/$(1)/python/$(CSR_NAME)/__init__.py
	python -W ignore::DeprecationWarning -m unittest discover -s $(BUILDDIR)/$(1)/python/$(CSR_NAME)/tests -t $(BUILDDIR)/$(1)/python -v
endef

$(foreach endpoint,$(ENDPOINTS),$(eval $(call ENDPOINT_RULES,$(endpoint))))

$(DOCSDIR)/%.md: $(INCLUDEDIR)/%.rdl
	mkdir -p $(DOCSDIR)
	peakrdl markdown $< -o $@ --top $*_top

unittest: $(addprefix unittest-,$(ENDPOINTS))

clean:
	rm -rf $(foreach endpoint,$(ENDPOINTS),$(BUILDDIR)/$(endpoint))
	rm -f $(INTERFACE_MARKDOWN)
