<!-- SPDX-FileCopyrightText: 2026 Enio Kaljic -->
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# openENOC Endpoint Peer Lookup Test Suite

## Overview

This cocotb suite verifies peer lookup with the generated CSR block and bridge.
All peer configuration uses AXI4-Lite transactions. Five cases run with two
clients, four peers, two-bit peer indices, and 32-bit addresses.

Component architecture and operation are described in the
[RTL Reference](../../../docs/src/rtl/openenoc_endpoint_peer_lookup.rst).

## Test Coverage

The suite covers:

- generated CSR configuration, readback, and complete coherent peer snapshots;
- index, RMEM-address, and MAC-address lookup with DMA-mode filtering;
- disabled entries, mode masks, deterministic misses, and lowest-index match
  priority;
- half-open and zero-sized regions, overlaps, and address-wrap protection;
- registered grants, round-robin arbitration, and sustained one-response-per-
  cycle traffic;
- two buffered responses, stable backpressured data, and same-cycle
  replacement;
- configuration changes after acceptance and output stability between clock
  edges.

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
