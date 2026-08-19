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
├── endpoints/
│   └── openenoc_endpoint_full.rdl
├── interfaces/
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

Endpoint specifications are discovered from `endpoints/*.rdl`. Shared component
definitions under `interfaces/` are included by endpoint specifications as
needed.

## SystemRDL Organization

The build automatically discovers every endpoint specification in `endpoints/`.
Each specification defines an endpoint top-level address map named after the
endpoint and a nested address map named `csr`. The current specification
therefore provides:

* `openenoc_endpoint_full`
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

Run the Makefile from `hal/`:

```bash
make
```

Equivalently, run `make -C hal` from the repository root.

The default output shows one concise status line per build step. Use
`make VERBOSE=1` to also print the commands being executed.

The current endpoint generates the following artifact layout:

```text
build/hal/
├── openenoc_endpoint_full/
│   ├── html/
│   ├── markdown/
│   │   └── openenoc_endpoint_full.md
│   ├── python/
│   │   └── csr/
│   ├── rtl/
│   │   ├── openenoc_endpoint_full_csr.sv
│   │   ├── openenoc_endpoint_full_csr_bridge.sv
│   │   ├── openenoc_endpoint_full_csr_pkg.sv
│   │   └── openenoc_endpoint_full_pkg.sv
│   └── sw/
│       ├── csr.h
│       └── memory_map.h
└── rtl/
    ├── openenoc_endpoint_if.sv
    └── openenoc_switch_if.sv
```

The project-level interfaces under `build/hal/rtl/` are generated directly from
the shared SystemRDL definitions. The exporter walks the RDL model rather than
maintaining a fixed signal list: hardware-readable and hardware-writable fields,
field widths, instance arrays, component parameters, and external register-file
handshake signals are reflected automatically. The signals retain the PeakRDL
hierarchy in the directional `core_to_csr` and `csr_to_core` bundles.

The endpoint-specific
`build/hal/openenoc_endpoint_full/rtl/openenoc_endpoint_full_csr_bridge.sv`
adapts PeakRDL's concrete `hwif_in`/`hwif_out` types to the parameterized project
interfaces. It is regenerated from the endpoint RDL specification whenever the
shared interface hierarchy or array sizes change.

Instantiate the interfaces with the constants from the endpoint CSR package,
for example:

```systemverilog
openenoc_endpoint_if #(
    .NUM_OF_PEERS(openenoc_endpoint_full_csr_pkg::NUM_OF_PEERS),
    .RMEM_TOTAL_DEPTH(openenoc_endpoint_full_csr_pkg::RMEM_TOTAL_DEPTH)
) endpoint_if (.*);

openenoc_switch_if #(
    .NUM_OF_INTERFACES(openenoc_endpoint_full_csr_pkg::NUM_OF_INTERFACES),
    .TABLE_DEPTH(openenoc_endpoint_full_csr_pkg::TABLE_DEPTH)
) switch_if (.*);
```

In `openenoc_endpoint_full`, the `openenoc_endpoint_if` instance remains
internal, while the module exposes the `openenoc_switch_if.csr` modport. The
generated endpoint bridge connects both interfaces to the CSR instance's
internal `hwif_in` and `hwif_out` signals.

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
