# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: CERN-OHL-S-2.0

RDLTOP    = openENOC
RDLCSR    = csr
RDLSRC    = $(SOURCEDIR)/$(RDLTOP).rdl

SOURCEDIR = src
BUILDDIR  = ../build/hal

PEAKRDLHEADER = $(BUILDDIR)/$(RDLTOP).h
PEAKRDLRTL    = $(BUILDDIR)/rtl/
PEAKRDLPYTHON = $(BUILDDIR)/python/
PEAKRDLHTML   = $(BUILDDIR)/html/
PEAKRDLMD     = $(BUILDDIR)/$(RDLTOP).md

all: $(PEAKRDLHEADER) $(PEAKRDLRTL) $(PEAKRDLPYTHON) $(PEAKRDLHTML) $(PEAKRDLMD)

$(PEAKRDLHEADER): $(RDLSRC)
	mkdir -p $(BUILDDIR)
	peakrdl c-header $^ -b ltoh -o $@

$(PEAKRDLRTL): $(RDLSRC)
	peakrdl regblock $^ -o $@ --cpuif axi4-lite-flat --top $(RDLCSR)

$(PEAKRDLPYTHON): $(RDLSRC)
	peakrdl python $^ -t $(RDLCSR) -o $@

$(PEAKRDLHTML): $(RDLSRC)
	peakrdl html $^ -o $@ --top $(RDLCSR)

$(PEAKRDLMD): $(RDLSRC)
	peakrdl markdown $^ -o $@ --top $(RDLTOP)

unittest: $(PEAKRDLPYTHON)
	python -W ignore::DeprecationWarning -m unittest discover -s $(PEAKRDLPYTHON)$(RDLCSR)/tests -t $(PEAKRDLPYTHON) -v

clean:
	rm -rf $(PEAKRDLHEADER) $(PEAKRDLRTL) $(PEAKRDLPYTHON) $(PEAKRDLHTML) $(PEAKRDLMD)
