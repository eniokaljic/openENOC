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
├── templates/
│   ├── openenoc_csr_bridge.sv.j2
│   └── openenoc_if.sv.j2
├── tools/
│   ├── export_openenoc_csr_bridge.py
│   ├── export_openenoc_if.py
│   ├── inject_rdl_parameters.py
│   └── openenoc_hwif.py
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
* SystemVerilog RTL named `<endpoint>_csr.sv`, `<endpoint>_csr_pkg.sv`,
  `<endpoint>_csr_bridge.sv`, and `<endpoint>_pkg.sv`
* PeakRDL Python model in the `csr` package
* HTML register documentation for each endpoint CSR address map
* Markdown documentation for each endpoint top-level address map and the shared interfaces

It also generates the project-level, parameterized hardware interfaces directly
from the shared SystemRDL definitions:

* `build/hal/rtl/openenoc_endpoint_if.sv`
* `build/hal/rtl/openenoc_switch_if.sv`

Run `make interfaces` to generate only these two interfaces. The exporter walks
the RDL model rather than maintaining a fixed signal list: hardware-readable and
hardware-writable fields, field widths, instance arrays, component parameters,
and external register-file handshake signals are reflected automatically. The
signals retain the PeakRDL hierarchy in the directional `core_to_csr` and
`csr_to_core` bundles.

Run `make bridges` to generate the endpoint-specific adapters between PeakRDL's
concrete `hwif_in`/`hwif_out` types and the parameterized project interfaces.
Each bridge is generated from its endpoint RDL specification, so changes to the
shared interface hierarchy or array sizes also update the bridge connections.
Instantiate the interfaces with the constants from the endpoint CSR package,
for example:

```systemverilog
openenoc_endpoint_if #(
    .NUM_OF_PEERS(openenoc_full_endpoint_csr_pkg::NUM_OF_PEERS),
    .RMEM_TOTAL_DEPTH(openenoc_full_endpoint_csr_pkg::RMEM_TOTAL_DEPTH)
) endpoint_if (.*);

openenoc_switch_if #(
    .NUM_OF_INTERFACES(openenoc_full_endpoint_csr_pkg::NUM_OF_INTERFACES),
    .TABLE_DEPTH(openenoc_full_endpoint_csr_pkg::TABLE_DEPTH)
) switch_if (.*);
```

Parameters declared on the endpoint's `csr` addrmap are emitted by PeakRDL in
`<endpoint>_csr_pkg.sv`. The same values are added to `sw/csr.h` with a `CSR__`
prefix, for example `CSR__NUM_OF_INTERFACES` and `CSR__TABLE_DEPTH`.

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
