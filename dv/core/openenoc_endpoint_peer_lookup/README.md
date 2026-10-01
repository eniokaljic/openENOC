<!-- SPDX-FileCopyrightText: 2026 Enio Kaljic -->
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# openENOC Endpoint Peer Lookup Test Suite

## Overview

This cocotb suite verifies the `openenoc_endpoint_peer_lookup` module and its
ready/valid client interfaces. The endpoint processor and datapath engines are
not instantiated, but the test wrapper includes the generated full-endpoint
CSR block and connects it through `openenoc_endpoint_full_csr_bridge` and
`openenoc_endpoint_if` as intended in the endpoint integration.

The testbench configures the peer table exclusively through AXI4-Lite CSR
transactions. The lookup module supports requests by peer index, RMEM address,
and MAC address. Mode-zero entries are disabled, overlapping matches select the
lowest peer index, and `req_mode_mask` can further restrict eligible entries.

## Test Coverage

The cocotb suite covers:

- peer-table configuration and readback through the generated CSR block,
  `openenoc_endpoint_full_csr_bridge`, and `openenoc_endpoint_if`;
- index lookup restricted to peer-DMA modes 2 and 3;
- RMEM lookup restricted to transparent-RMEM mode 1;
- MAC lookup across all enabled DMA modes;
- additional mode filtering through `req_mode_mask`;
- disabled entries and deterministic zero-valued miss responses;
- lowest-index priority for duplicate MAC addresses and overlapping RMEM
  regions;
- half-open RMEM region boundaries and zero-sized regions;
- extended-width RMEM arithmetic that prevents false matches after 32-bit
  address wraparound;
- complete peer-entry snapshots containing MAC, RMEM offset, local and remote
  addresses, size, DMA mode, and IRQ enable;
- one-cycle registered response latency;
- stable response data while backpressured;
- request backpressure while a response is pending;
- same-cycle response consumption and replacement without a pipeline bubble;
- round-robin arbitration between lookup clients; and
- sustained throughput of one lookup response per cycle.

## Default Configuration

The direct Makefile flow uses:

```text
LOOKUP_PORTS=2
NUM_OF_PEERS=4
PEER_IDX_W=2
ADDR_W=32
```

`NUM_OF_PEERS` is provided by the generated full-endpoint CSR package. The
SystemVerilog wrapper flattens the two `openenoc_peer_lookup_if` instances only
at the cocotb boundary.

## Running Tests

Run the full pytest regression:

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
