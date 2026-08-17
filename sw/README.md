<!-- SPDX-FileCopyrightText: 2026 Enio Kaljic -->
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# openENOC Bare-Metal Software

This directory contains the bare-metal software build flow for RISC-V CPUs used
with openENOC endpoints. Each build combines one application, one endpoint CSR
interface, and one CPU platform into a standalone firmware image.

Application-specific verification code is kept together with the corresponding
application. Unit tests and scenario-level hardware/software verification belong
under `dv/` together with the RTL verification environment.

## Directory Structure

```text
sw/
├── apps/
│   └── <application>/
│       └── main.c
├── lib/
│   └── <library>/
│       ├── include/
│       └── src/
├── platform/
│   └── <platform>/
│       ├── boot.s
│       └── sections.lds.in
├── Makefile
└── README.md
```

The application and platform directories may also contain additional `.c`, `.s`,
or preprocessed `.S` source files. Internal library sources are discovered under
`lib/*/src`, while their public headers are exposed from `lib/*/include`.

## Environment Setup

The software build requires GNU Make, an AWK-compatible text processor, `xxd`,
and a bare-metal RISC-V GNU toolchain. The default toolchain prefix is
`riscv64-unknown-elf-`. The build can also invoke the HAL generation flow, so
its Python dependencies must be installed in the active virtual environment.

On Ubuntu, the system dependencies can be installed with:

```bash
sudo apt install binutils-riscv64-unknown-elf gcc-riscv64-unknown-elf \
    make mawk python3 python3-pip python3-venv xxd
```

The Ubuntu packages provide the
[RISC-V GCC cross compiler](https://packages.ubuntu.com/noble/gcc-riscv64-unknown-elf)
and the corresponding `objcopy`, `objdump`, and `size` utilities. A different
installed toolchain can be selected by overriding `CROSS_COMPILE`.

### Python Virtual Environment

Create the virtual environment from the repository root and install the HAL
generation dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r hal/requirements.txt
```

The same virtual environment can be reused by the HAL and DV flows. Keep it
activated while building software so that missing or outdated generated headers
can be regenerated automatically.

The installed tools can be checked with:

```bash
python -m pip check
peakrdl --version
riscv64-unknown-elf-gcc --version
riscv64-unknown-elf-objcopy --version
xxd -v
awk 'BEGIN { print "awk OK" }'
```

Run the remaining commands below from the `sw/` directory.

## Selecting an Application and Endpoint

List the available applications and endpoints:

```bash
make list-apps
make list-eps
```

Applications are discovered from `apps/*/main.c`. Endpoints are discovered from
the SystemRDL specifications under `../hal/ep/*.rdl`.

Both `APP` and `EP` are mandatory for every build:

```bash
make APP=csr_smoke EP=openenoc_full_endpoint
```

The selected endpoint provides generated SW headers at:

```text
build/hal/<endpoint>/sw/csr.h
build/hal/<endpoint>/sw/memory_map.h
```

If either header is missing or older than its SystemRDL inputs, the software build
invokes the HAL build flow to regenerate it. The build exposes only the selected
endpoint directory, so applications use the endpoint-independent include:

```c
#include "csr.h"
#include "memory_map.h"
```

The generated root type is always `csr_t`, while its nested declarations use the
common `csr__*` namespace.

## Build Configuration

The default configuration is equivalent to:

```bash
make APP=csr_smoke EP=openenoc_full_endpoint \
    PLATFORM=picorv32 MARCH=rv32i MABI=ilp32
```

The main configuration variables are:

| Variable | Default | Purpose |
|---|---|---|
| `APP` | none | Application directory name under `apps/` |
| `EP` | none | Endpoint name derived from `hal/ep/<endpoint>.rdl` |
| `PLATFORM` | `picorv32` | CPU startup code, linker script, and platform headers |
| `MARCH` | `rv32i` | RISC-V ISA passed to the compiler and linker |
| `MABI` | `ilp32` | RISC-V ABI passed to the compiler and linker |
| `CROSS_COMPILE` | `riscv64-unknown-elf-` | GNU toolchain command prefix |
| `VERBOSE` | `0` | Set to `1` to print commands in addition to concise build-step messages |

All sources are compiled and linked in one compiler invocation. No persistent
object or dependency directories are generated. The complete firmware is rebuilt
for each build request so that configuration changes cannot reuse an artifact made
for a different platform or ISA.

## Generated Artifacts

Build outputs are written to the repository path `build/sw/<endpoint>/`. The
application is identified by the artifact file names, while the platform and ISA
are intentionally not encoded in this path.

For example, `APP=csr_smoke EP=openenoc_full_endpoint` generates:

```text
build/sw/openenoc_full_endpoint/
├── csr_smoke.elf
├── csr_smoke.bin
├── csr_smoke.hex
├── csr_smoke.lst
├── csr_smoke.map
├── sections.lds
└── imem.mem
```

| Artifact | Description |
|---|---|
| `.elf` | Linked firmware image with symbols and section information |
| `.bin` | Raw loadable firmware image |
| `.hex` | Verilog-format image generated by GNU `objcopy` |
| `.lst` | Disassembly and source listing |
| `.map` | Linker memory map |
| `sections.lds` | Endpoint-specific linker script preprocessed from the platform template and generated memory map |
| `imem.mem` | 32-bit hexadecimal words for Verilog `$readmemh` |

The `imem.mem` file contains one 32-bit word per line. Firmware bytes are converted
from their little-endian binary representation before each word is written as eight
hexadecimal digits. The build rejects images that are not word-aligned or exceed
the `IMEM_DEPTH` value generated from the endpoint SystemRDL specification.
Because this file has an endpoint-scoped name, building another application for
the same endpoint replaces `imem.mem` with the newly selected firmware image.

## Cleaning Generated Files

Remove all software build outputs with:

```bash
make clean
```
