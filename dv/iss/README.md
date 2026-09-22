<!-- SPDX-FileCopyrightText: 2026 Kerim Bavcic -->
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# openENOC ISS Co-Verification

This directory contains the host-side infrastructure for executing RISC-V
firmware with Spike while endpoint hardware is simulated with cocotb and
Verilator.

The current build milestone pins and builds Spike as a repository submodule,
installs it under `build/dv/iss/spike-install`, and compiles a small C++ link
test against Spike's internal API. It does not yet execute firmware or connect
Spike memory requests to RTL.

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
install` flow without installing anything globally. `JOBS` defaults to one to
limit memory use under WSL and can be overridden explicitly:

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