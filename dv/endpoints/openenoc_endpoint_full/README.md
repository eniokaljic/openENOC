<!-- SPDX-FileCopyrightText: 2026 Enio Kaljic -->
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# openENOC Full Endpoint Test Suite

## Overview

This cocotb suite boots the full endpoint with the existing `csr_smoke`
PicoRV32 firmware and loops Ethernet TX back to RX. It runs continuous and
periodically stalled loopback. Firmware/HAL behavior is described in the
[csr_smoke README](../../../sw/apps/csr_smoke/README.md). Build the firmware
from the repository root before running the suite:

```bash
make -C sw APP=csr_smoke EP=openenoc_endpoint_full
```

The testbench loads `build/sw/openenoc_endpoint_full/imem.mem` and observes
the final firmware status in DMEM.

Component architecture and operation are described in the
[RTL Reference](../../../docs/src/rtl/openenoc_endpoint_full.rst).

## Test Coverage

The suite covers:

- firmware initialization, instruction execution without traps, and
  IMEM/DMEM/CSR access;
- CSR test-register readback of `0xa5a55a5a`;
- switch configuration, capability fields, pause status, and generated bridge
  wiring;
- 66-byte direct frame loopback in 17 beats with exact byte masks and final
  TLAST;
- RX IRQ availability before the last Ethernet beat and CSR payload reads
  inside the IRQ handler;
- IRQ entry/return and ordered RX-available/TX-complete token completion
  without accounting errors;
- complete frame preservation with continuous and stalled transport;
- firmware success status `0x600d600d` and inactive DMA, debug, and local RMEM
  masters.

## Running Tests

Run the full pytest parameter sweep:

```bash
./run_tests.sh pytest
```

Run the default configuration and generate an FST waveform:

```bash
./run_tests.sh waves
```

Remove generated simulation artifacts:

```bash
./run_tests.sh clean
```
