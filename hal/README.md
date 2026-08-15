<!-- SPDX-FileCopyrightText: 2026 Enio Kaljic -->
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# openENOC HAL CSR Generation

This directory contains a Makefile for generating openENOC HAL artifacts from the endpoint SystemRDL specifications located under `ep/`. Reusable SystemRDL component definitions are located under `include/`.

The build automatically discovers every endpoint specification in `ep/`. Each specification uses the same base name for its endpoint top-level address map and appends `_csr` for its CSR address map. The current endpoint therefore provides:

* `openenoc`
* `openenoc_csr`

Shared interface definitions are provided by:

* `openenoc_endpoint_interface`
* `openenoc_switch_interface`

## Requirements

Create and activate a Python virtual environment, then install the required Python packages:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

The required packages are PeakRDL and the exporters used for Markdown and Python model generation.

## Running the Build

Run the Makefile from the directory that contains it:

```bash
make
```

This generates a separate artifact tree for each endpoint under `build/hal/<endpoint>/`, including:

* C header file for each endpoint top-level address map
* SystemVerilog RTL for each endpoint CSR address map
* PeakRDL Python model for each endpoint CSR address map
* HTML register documentation for each endpoint CSR address map
* Markdown documentation for each endpoint top-level address map and the shared interfaces

## Running Unit Tests

After generating the Python model, run:

```bash
make unittest
```

This executes the unit tests generated together with the PeakRDL Python model.

## Cleaning Generated Files

To remove generated artifacts, run:

```bash
make clean
```

## Notes

The Makefile uses paths relative to the current working directory, so it should be executed directly from this directory.
