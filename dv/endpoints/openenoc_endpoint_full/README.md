<!-- SPDX-FileCopyrightText: 2026 Enio Kaljic -->
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# openENOC Full Endpoint Test Suite

## Overview

This test suite verifies the `openenoc_full_endpoint` SoC wrapper with the
`csr_smoke` PicoRV32 firmware from
`build/sw/openenoc_full_endpoint/imem.mem`.

The endpoint contains a 3-by-3 Taxi AXI4-Lite crossbar. System initiators are
ordered as PicoRV32, the reserved endpoint-interface master, and the reserved
debug/program master. Targets are ordered as DMEM, IMEM, and CSR. The two
reserved initiators are tied inactive, while the crossbar keeps all target
connections enabled for the later integration steps.

The crossbar arrays are connected through individually named internal Taxi
interfaces: `cpu_axil`, `endpoint_axil`, `debug_axil`, `dmem_axil`,
`imem_axil`, and `csr_axil`.

## Address Map

| Target | Base address | Decode aperture |
| --- | ---: | ---: |
| IMEM | `0x0000_0000` | 32 KiB |
| DMEM | `0x1000_0000` | 32 KiB |
| CSR | `0x2000_0000` | 8 KiB |

IMEM and DMEM sizes are derived from `openenoc_full_endpoint_pkg`. The CSR
aperture uses `OPENENOC_FULL_ENDPOINT_CSR_MIN_ADDR_WIDTH` from the generated
CSR package.

## Test Coverage

The cocotb test verifies that:

- IMEM is initialized from the generated `csr_smoke` image;
- PicoRV32 fetches and executes the firmware without entering its trap state;
- execution reaches IMEM, DMEM, and CSR through the crossbar;
- the CSR write/read test stores `0xa5a55a5a` in `csr.test_reg`;
- firmware reports success by storing `0x600d600d` in DMEM;
- both reserved AXI4-Lite initiators remain inactive; and
- the future endpoint Ethernet bridge signals remain inactive.

## Running Tests

Activate the project virtual environment, change to this directory, and run:

```bash
./run_tests.sh pytest
```

Run the same test with FST waveforms:

```bash
./run_tests.sh waves
```

Remove generated simulation artifacts:

```bash
./run_tests.sh clean
```
