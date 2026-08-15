<!-- SPDX-FileCopyrightText: 2026 Enio Kaljic -->
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# openENOC HAL CSR Generation

This directory contains a Makefile for generating openENOC HAL artifacts from the endpoint SystemRDL specifications located under `ep/`. Reusable SystemRDL component definitions are located under `include/`.

The build automatically discovers every endpoint specification in `ep/`. Each
specification defines an endpoint top-level address map named after the endpoint
and a nested address map named `csr`. The current specification therefore
provides:

* `openenoc`
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

* C header named `include/csr.h` with the root type `csr_t`
* SystemVerilog RTL named `<endpoint>_csr.sv` and `<endpoint>_csr_pkg.sv`
* PeakRDL Python model in the `csr` package
* HTML register documentation for each endpoint CSR address map
* Markdown documentation for each endpoint top-level address map and the shared interfaces

The endpoint directory keeps each `include/csr.h` separate, allowing software to
select an endpoint through its include path while always using:

```c
#include "csr.h"
```

Generated declarations use the common CSR namespace, including `csr_t` and its
`csr__*` subtypes.

Only the generated RTL keeps the endpoint prefix. This prevents module and
package name collisions when CSR blocks from multiple endpoints are instantiated
in the same RTL project.

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
