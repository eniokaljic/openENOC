<!-- SPDX-FileCopyrightText: 2026 Kerim Bavcic -->
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# openENOC ISS Co-Verification

This directory contains the host-side infrastructure for executing RISC-V
firmware with Spike while endpoint hardware is simulated with cocotb and
Verilator.

Spike is embedded through its `processor_t` and `simif_t` APIs and hidden
behind a versioned C ABI in `include/openenoc_iss.h`. Each endpoint handle owns
one RV32I hart and one native worker thread. A worker publishes external data
accesses through a single request slot and waits while Python/cocotb services
the corresponding AXI4-Lite transaction. The cocotb simulator thread remains
free to advance RTL and service other endpoints.

The integration runs the existing, unchanged `csr_smoke` firmware on Spike
while the endpoint crossbar, DMEM, generated CSR block, endpoint logic, and
AXIS loopback remain RTL simulated by Verilator. A dedicated `iss_startup`
firmware also qualifies the platform's data initialization, BSS clearing,
read-only data, and stack behavior.

## Prerequisites

On Ubuntu, install the upstream Spike and bare-metal firmware build
dependencies:

```bash
sudo apt-get install \
	device-tree-compiler libboost-regex-dev libboost-system-dev \
	gcc-riscv64-unknown-elf binutils-riscv64-unknown-elf
```

Initialize the submodule after cloning the repository:

```bash
git submodule update --init libs/riscv-isa-sim
```

The RTL tests use the repository Python environment and OSS CAD Suite. Activate
them in this order before running an RTL target:

```bash
source /path/to/oss-cad-suite/environment
source venv/bin/activate
pip install -r dv/requirements.txt
```

## Build And Check

From the repository root, run:

```bash
make -C dv/iss check
```

This performs Spike's upstream out-of-tree `configure`, `make`, and `make
install` flow without installing anything globally. It then runs the C++ API,
C ABI, threaded request-channel, and Python `ctypes` smoke tests. Individual
targets include:

```bash
make -C dv/iss processor-smoke
make -C dv/iss c-api-smoke
make -C dv/iss python-smoke
make -C dv/iss elf-smoke
```

Run the short Spike-to-RTL DMEM test with:

```bash
make -C dv/iss rtl-smoke
```

Build and run the unchanged `csr_smoke` firmware through Spike and the RTL
endpoint with:

```bash
make -C dv/iss rtl-firmware-smoke
```

Qualify the real bare-metal startup path with initialized data, dirty BSS, and
stack traffic through RTL DMEM:

```bash
make -C dv/iss rtl-startup-smoke
```

Run every native, Python, and RTL check with:

```bash
make -C dv/iss check-all
```

`JOBS` defaults to one to limit memory use under WSL and can be overridden
explicitly:

```bash
make -C dv/iss check JOBS=4
```

Remove all ISS build products with:

```bash
make -C dv/iss clean
```

The supported upstream commit and initial CPU profile are recorded in
`compatibility.json`. The build rejects a submodule checked out at a different
commit.

## ELF Loading

The Python loader accepts only ELF32 little-endian RISC-V executables matching
the RV32I soft-float profile and 16-byte stack ABI. It validates program-header
bounds, address overflow, segment alignment and overlap, supported memory
regions, and an executable entry point before exposing an immutable boot
image.

Only file-backed bytes from `PT_LOAD` segments are copied into private ISS
IMEM, using each segment's physical/load address (`p_paddr`). Writable data
keeps its DMEM runtime address (`p_vaddr`), so `boot.s` must copy `.data` from
IMEM to RTL DMEM. The loader does not initialize the remaining `p_memsz`
bytes, which leaves `.bss` clearing to `boot.s`. Completion addresses are read
from ELF symbols rather than fixed testbench constants.

## Current Profile

- RV32I, machine privilege mode, one hart per endpoint handle.
- Private 32 KiB ISS IMEM at `0x00000000`.
- RTL DMEM at `0x10000000-0x10007fff`.
- RTL CSR aperture at `0x20000000-0x20001fff`.
- One pending 1-, 2-, or 4-byte data request per endpoint.
- No interrupts and no external instruction fetches.
- Validated ELF entry points, load segments, and symbols drive firmware tests.