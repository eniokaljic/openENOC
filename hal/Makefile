# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: CERN-OHL-S-2.0 OR AGPL-3.0-or-later OR CC-BY-SA-4.0

RDLTOP    = openENOC
RDLCSR    = csr
RDLSRC    = $(SOURCEDIR)/$(RDLTOP).rdl

SOURCEDIR = src
BUILDDIR  = build

PEAKRDLHEADER = $(BUILDDIR)/$(RDLTOP).h
PEAKRDLRTL    = $(BUILDDIR)/rtl/
PEAKRDLPYTHON = $(BUILDDIR)/python/
PEAKRDLHTML   = $(BUILDDIR)/html/
PEAKRDLMD     = $(BUILDDIR)/$(RDLTOP).md

all: $(PEAKRDLHEADER) $(PEAKRDLRTL) $(PEAKRDLPYTHON) $(PEAKRDLHTML) $(PEAKRDLMD)

$(PEAKRDLHEADER): $(RDLSRC)
	peakrdl c-header $^ -b ltoh -o $@

$(PEAKRDLRTL): $(RDLSRC)
	peakrdl regblock $^ -o $@ --cpuif passthrough --top $(RDLCSR)

$(PEAKRDLPYTHON): $(RDLSRC)
	peakrdl python $^ -t $(RDLCSR) -o $@
	
$(PEAKRDLHTML): $(RDLSRC)
	peakrdl html $^ -o $@ --top $(RDLCSR)

$(PEAKRDLMD): $(RDLSRC)
	peakrdl markdown $^ -o $@ --top $(RDLTOP)

test: $(PEAKRDLPYTHON)
	python -m unittest discover -s $(PEAKRDLPYTHON)$(RDLCSR)/tests -t .

clean:
	@rm -rf $(PEAKRDLHEADER) $(PEAKRDLRTL) $(PEAKRDLPYTHON) $(PEAKRDLHTML) $(PEAKRDLMD)
