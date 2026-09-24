<!-- SPDX-FileCopyrightText: 2026 Kerim Bavcic -->
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# openENOC ISS Co-Verification

This directory contains the host-side infrastructure for executing RISC-V
firmware with Spike while endpoint hardware is simulated with cocotb and
Verilator.

The current build milestone pins and builds Spike as a repository submodule,
installs it under `build/dv/iss/spike-install`, and embeds a single RV32I hart
through Spike's `processor_t` and `simif_t` APIs. A native smoke test executes
instructions from private ISS memory and routes accesses to `0x10000000`
through the external-memory callbacks. The callbacks are not connected to RTL
yet.

## Prerequisites

On Ubuntu, install the upstream Spike build dependencies:

```bash
sudo apt-get install device-tree-compiler libboost-regex-dev libboost-system-dev
```

Initialize the submodule after cloning the repository:

```bash
git submodule update --init libs/riscv-isa-sim
```

## Build And Check

From the repository root, run:

```bash
make -C dv/iss check
```

This performs Spike's upstream out-of-tree `configure`, `make`, and `make
install` flow without installing anything globally, then runs the API link and
processor smoke tests. The processor test can also be run independently:

```bash
make -C dv/iss processor-smoke
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