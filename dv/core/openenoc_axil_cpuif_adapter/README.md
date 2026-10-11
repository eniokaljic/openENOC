<!-- SPDX-FileCopyrightText: 2026 Enio Kaljic -->
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# openENOC AXI4-Lite to CPUIF Adapter Test Suite

## Overview

This cocotb suite verifies `openenoc_axil_cpuif_adapter` in isolation with
native CPUIF and AXI4-Lite bus fixtures. The default fixture uses 32-bit
addresses and data. Component architecture and operation are described in
the [RTL Reference](../../../docs/src/rtl/openenoc_axil_cpuif_adapter.rst).

## Test Coverage

The suite covers:

- independent AXI write-address and write-data arrival;
- fall-through dispatch when the second write channel arrives;
- AXI byte-strobe expansion to CPUIF bit enables;
- round-robin arbitration of simultaneous read and write requests;
- same-cycle CPUIF completion and dispatch of the next operation;
- zero-latency and delayed CPUIF acknowledgements;
- ordered read and write response delivery;
- simultaneous response dequeue and replacement;
- response-FIFO saturation and CPUIF backpressure;
- stable AXI read responses while backpressured;
- CPUIF read and write error conversion to AXI `SLVERR`;
- preservation of read response data; and
- reset of AXI request buffers, the active CPUIF operation, and queued
  responses.

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
