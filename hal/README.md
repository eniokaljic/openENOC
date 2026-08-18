<!-- SPDX-FileCopyrightText: 2026 Enio Kaljic -->
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# openENOC HAL CSR Generation

This directory contains the SystemRDL-based HAL generation flow for openENOC
endpoints. Each build converts endpoint specifications into software headers,
SystemVerilog RTL, register models, and documentation.

Endpoint specifications are the source of truth for endpoint memory maps and
configuration parameters. Reusable SystemRDL components shared by multiple
endpoints are maintained separately from the endpoint definitions.

## Directory Structure

```text
hal/
├── endpoint/
│   └── <endpoint>.rdl
├── include/
│   ├── openenoc_endpoint_interface.rdl
│   └── openenoc_switch_interface.rdl
├── Makefile
├── README.md
└── requirements.txt
```

Endpoint specifications are discovered from `endpoint/*.rdl`. Shared component
definitions under `include/` are included by endpoint specifications as needed.

## SystemRDL Organization

The build automatically discovers every endpoint specification in `endpoint/`. Each
specification defines an endpoint top-level address map named after the endpoint
and a nested address map named `csr`. The current specification therefore
provides:

* `openenoc_full_endpoint`
* `csr`

Shared interface definitions are provided by:

* `openenoc_endpoint_interface`
* `openenoc_switch_interface`

## Environment Setup

The HAL generation flow requires Python 3, GNU Make, and an AWK-compatible text
processor. On Ubuntu, the system dependencies can be installed with:

```bash
sudo apt install make mawk python3 python3-pip python3-venv
```

### Python Virtual Environment

Create the virtual environment from the repository root and install the Python
packages listed in `hal/requirements.txt`:

```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r hal/requirements.txt
```

The requirements install [PeakRDL](https://peakrdl.readthedocs.io/en/latest/)
and the exporters used for Markdown documentation and Python model generation.
The same virtual environment can be reused by other repository flows. Keep it
activated when invoking the HAL Makefile.

The installed tools can be checked with:

```bash
python -m pip check
peakrdl --version
awk 'BEGIN { print "awk OK" }'
```

## Running the Build

Run the Makefile from the directory that contains it:

```bash
make
```

The default output shows one concise status line per build step. Use
`make VERBOSE=1` to also print the commands being executed.

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
