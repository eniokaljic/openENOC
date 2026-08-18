<!-- SPDX-FileCopyrightText: 2026 Enio Kaljic -->
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# openENOC Design Verification

This directory contains the simulation and verification environments for
openENOC RTL, generated HAL blocks, and reusable traffic infrastructure. Test
suites are grouped by the type of design they exercise.

Each test directory contains its own build entry points, testbench sources, and
detailed README. Shared simulator configuration is kept separately so that the
individual test suites use a consistent tool setup.

## Directory Structure

```text
dv/
├── common/
│   └── config.vlt
├── core/
│   ├── openenoc_axil_ram/
│   ├── openenoc_axis_demux/
│   ├── openenoc_axis_header_parser/
│   ├── openenoc_axis_switch/
│   ├── openenoc_eth_adapter/
│   └── openenoc_forwarding_table/
├── examples/
├── hal/
│   └── openenoc_full_endpoint/
├── traffic/
├── README.md
└── requirements.txt
```

The `core/` directory contains unit-level RTL verification environments. The
`hal/` directory verifies generated endpoint CSR RTL and its Python register
model. The `traffic/` directory validates the reusable PCAP replay and capture
infrastructure, while `common/` contains simulator configuration shared across
test suites. The `examples/` directory is reserved for example verification
environments.

## Environment Setup

The documented verification environment targets Ubuntu 24.04 and uses the OSS
CAD Suite as its source of open-source RTL tooling, including Verilator. The
verification environments require Python 3, GNU Make, Bash, and Verilator.
GTKWave is optional and is only needed when opening generated waveforms. The
Ubuntu system dependencies can be installed with:

```bash
sudo apt install bash make python3 python3-pip python3-venv gtkwave
```

Verilator can be installed separately or as part of the
[OSS CAD Suite](https://github.com/YosysHQ/oss-cad-suite-build). When using the
suite, download and extract the appropriate archive from its
[release page](https://github.com/YosysHQ/oss-cad-suite-build/releases), then
load its environment before activating the Python virtual environment:

```bash
source <extracted-location>/oss-cad-suite/environment
```

See the OSS CAD Suite README for the complete platform-specific installation
instructions.

### Python Virtual Environment

Create the virtual environment from the repository root and install the Python
packages listed in `dv/requirements.txt`:

```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r dv/requirements.txt
```

The requirements install cocotb, its pytest integration, the AXI bus models
used by the HAL test, and pytest itself. Keep the virtual environment activated
when invoking cocotb, Verilator, or the test Makefiles. The general cocotb
prerequisites and installation options are documented in the
[cocotb installation guide](https://docs.cocotb.org/en/stable/install.html).

The installed tools can be checked with:

```bash
python -m pip check
verilator --version
cocotb-config --version
```

## Test-Specific Tools

The tests under `core/` and `traffic/` use Verilator through cocotb-test and
pytest. Their `run_tests.sh waves` commands additionally invoke GTKWave. The
HAL test under `hal/openenoc_full_endpoint/` uses cocotb, cocotbext-axi, GNU
Make, and Verilator directly; its optional `make wave` target invokes GTKWave.

Before running the HAL test, generate the endpoint RTL and Python register model
from the repository root:

```bash
python -m pip install -r hal/requirements.txt
make -C hal all
```

Run each suite from its own directory using the commands documented in its
README.
