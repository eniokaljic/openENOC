<!-- SPDX-FileCopyrightText: 2026 Enio Kaljic -->
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# openENOC Full Endpoint Test Suite

## Overview

This test suite verifies the `openenoc_endpoint_full` SoC wrapper with the
`csr_smoke` PicoRV32 firmware from
`build/sw/openenoc_endpoint_full/imem.mem`.

The endpoint contains a 3-by-3 pipelined `openenoc_axil_crossbar`. System
initiators are ordered as PicoRV32, the reserved endpoint-interface master,
and the reserved debug/program master. Targets are ordered as DMEM, IMEM, and
CSR. The two reserved initiators are tied inactive, while the crossbar keeps
all target connections enabled for the later integration steps.

The generated CSR `hwif` is internal to the endpoint. An
`openenoc_endpoint_if` instance connects the generated CSR bridge to
`openenoc_endpoint_interface`, while the module exposes the bridge's
`openenoc_switch_if` side.

The endpoint interface converts the CSR AXI4-Stream source and sink registers
to the Ethernet-like link through two `taxi_axis_async_fifo_adapter`
instances. The testbench loops the transmit direction back into the receive
direction.

The crossbar arrays are connected through individually named internal Taxi
interfaces: `cpu_axil`, `endpoint_axil`, `debug_axil`, `dmem_axil`,
`imem_axil`, and `csr_axil`.

The CPU initiator uses the `openenoc_picorv32` drop-in wrapper around the
original PicoRV32 core and the project AXI4-Lite adapter. Consequently this
suite is also the integration acceptance test for the wrapper and adapter;
they do not have a separate wrapper-only testbench.

## Address Map

| Target | Base address | Decode aperture |
| --- | ---: | ---: |
| IMEM | `0x0000_0000` | 32 KiB |
| DMEM | `0x1000_0000` | 32 KiB |
| CSR | `0x2000_0000` | 8 KiB |

IMEM and DMEM sizes are derived from `openenoc_endpoint_full_pkg`. The CSR
aperture uses `OPENENOC_ENDPOINT_FULL_CSR_MIN_ADDR_WIDTH` from the generated
CSR package.

## Test Coverage

The cocotb test verifies that:

- IMEM is initialized from the generated `csr_smoke` image;
- PicoRV32 fetches and executes the firmware without entering its trap state;
- execution reaches IMEM, DMEM, and CSR through the crossbar;
- the CSR write/read test stores `0xa5a55a5a` in `csr.test_reg`;
- the bridge presents generated switch parameters and software-written switch
  configuration on `openenoc_switch_if`, and propagates `pause_done` back into
  the CSR `hwif` and firmware readback;
- firmware sends and receives 66 bytes in 17 AXI4-Stream transfers through the
  CSR HAL;
- the Ethernet loopback and CSR sink each transfer the expected words in
  order, with `TKEEP=0xf` on the first 16 words, `TKEEP=0x3` on the final
  partially used word, and `TLAST` asserted only on that final word;
- firmware reports success by storing `0x600d600d` in DMEM;
- both reserved AXI4-Lite initiators remain inactive.

## Running Tests

Activate the project virtual environment, change to this directory, and run:

```bash
make -C ../../../sw APP=csr_smoke EP=openenoc_endpoint_full
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
