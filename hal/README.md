<!-- SPDX-FileCopyrightText: 2026 Enio Kaljic -->
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# openENOC HAL CSR Generation

This directory contains a Makefile for generating openENOC HAL artifacts from the endpoint SystemRDL specifications located under `ep/`. Reusable SystemRDL component definitions are located under `include/`.

The build automatically discovers every endpoint specification in `ep/`. Each
specification defines an endpoint top-level address map named after the endpoint
and a nested address map named `csr`. The current specification therefore
provides:

* `openenoc_full_endpoint`
* `csr`

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

This generates a separate artifact tree for each endpoint under
`build/hal/<endpoint>/`, including:

* C headers named `sw/csr.h` and `sw/memory_map.h`
* SystemVerilog RTL named `<endpoint>_csr.sv`, `<endpoint>_csr_pkg.sv`, and `<endpoint>_pkg.sv`
* PeakRDL Python model in the `csr` package
* HTML register documentation for each endpoint CSR address map
* Markdown documentation for each endpoint top-level address map and the shared interfaces

The endpoint directory keeps each set of SW headers separate, allowing software
to select an endpoint through its include path while always using:

```c
#include "csr.h"
#include "memory_map.h"
```

Generated declarations use the common CSR namespace, including `csr_t` and its
`csr__*` subtypes. Memory-map macros are endpoint-independent and provide the
IMEM and DMEM depths, base addresses and byte sizes, together with the CSR base
address.

Only the generated RTL keeps the endpoint prefix. This prevents module and
package name collisions when blocks from multiple endpoints are instantiated in
the same RTL project. The `<endpoint>_pkg` package also exports the elaborated
top-level address-map parameters for use by endpoint RTL.

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
