<!-- SPDX-FileCopyrightText: 2026 Enio Kaljic -->
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# openENOC AXI4-Lite to CPUIF Adapter Test Suite

## Overview

This cocotb suite verifies `openenoc_axil_cpuif_adapter` in isolation. The
SystemVerilog wrapper instantiates only the DUT, one `taxi_axil_if`, and one
`openenoc_cpuif_if`; no CSR block, memory, crossbar, processor, or endpoint
component is included.

The adapter buffers AXI write-address and write-data channels independently
and arbitrates complete writes against buffered reads. Read and write requests
use round-robin selection when both are available. Only one CPUIF operation is
outstanding, but its completion can be replaced by the next request in the same
cycle.

An ordered response FIFO retains CPUIF completions under AXI backpressure and
reserves space for the outstanding operation before it is dispatched. This
preserves bubble-free CPUIF throughput without risking response loss. Both a
combinational acknowledgement in the CPUIF request cycle and an acknowledgement
after an arbitrary delay are supported.

## Test Coverage

The cocotb suite covers:

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

## Default Configuration

The isolated SystemVerilog wrapper uses:

```text
DATA_W=32
ADDR_W=32
RESPONSE_FIFO_DEPTH=2
```

The AXI strobe width is derived as `DATA_W/8`. `RESPONSE_FIFO_DEPTH` must be at
least two so one queued response and one active CPUIF operation can coexist
during a bubble-free handoff.

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
