# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: CERN-OHL-S-2.0

SOURCEDIR = $(PWD)/src
BUILDDIR  = $(PWD)/../build/hal
DOCSDIR   = $(PWD)/../docs/src/generated

RDLTOP    = openenoc
RDLCSR    = openenoc_csr
RDLSW     = openenoc_switch
RDLSRC    = $(SOURCEDIR)/$(RDLTOP).rdl

PEAKRDLHEADER = $(BUILDDIR)/$(RDLCSR).h
PEAKRDLRTL    = $(BUILDDIR)/rtl/
PEAKRDLPYTHON = $(BUILDDIR)/python/
PEAKRDLHTML   = $(BUILDDIR)/html/
PEAKRDLMD_TOP = $(DOCSDIR)/$(RDLTOP).md
PEAKRDLMD_SW  = $(DOCSDIR)/$(RDLSW).md

all: $(PEAKRDLHEADER) $(PEAKRDLRTL) $(PEAKRDLPYTHON) $(PEAKRDLHTML) $(PEAKRDLMD_TOP) $(PEAKRDLMD_SW)

$(PEAKRDLHEADER): $(RDLSRC)
	mkdir -p $(BUILDDIR)
	peakrdl c-header $^ -b ltoh -o $@

$(PEAKRDLRTL): $(RDLSRC)
	peakrdl regblock $^ -o $@ --cpuif axi4-lite-flat --top $(RDLCSR)

$(PEAKRDLPYTHON): $(RDLSRC)
	peakrdl python $^ -t $(RDLCSR) -o $@

$(PEAKRDLHTML): $(RDLSRC)
	peakrdl html $^ -o $@ --top $(RDLCSR)

$(PEAKRDLMD_TOP): $(RDLSRC)
	peakrdl markdown $^ -o $@ --top $(RDLTOP)
	
$(PEAKRDLMD_SW): $(RDLSRC)
	mkdir -p $(DOCSDIR)
	peakrdl markdown $^ -o $@ --top $(RDLSW)

unittest: $(PEAKRDLPYTHON)
	python -W ignore::DeprecationWarning -m unittest discover -s $(PEAKRDLPYTHON)$(RDLCSR)/tests -t $(PEAKRDLPYTHON) -v

clean:
	rm -rf $(PEAKRDLHEADER) $(PEAKRDLRTL) $(PEAKRDLPYTHON) $(PEAKRDLHTML) $(PEAKRDLMD_TOP) $(PEAKRDLMD_SW)
