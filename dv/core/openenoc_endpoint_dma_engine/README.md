<!-- SPDX-FileCopyrightText: 2026 Enio Kaljic -->
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# openENOC Endpoint DMA Engine Test Suite

## Overview

This cocotb suite verifies the DMA engine in isolation using AXI memory and
AXI4-Stream models, a behavioral peer-lookup responder, and driven IRQ and
transaction handshakes. The fixture uses four peers, eight fragment slots,
and 32-bit data. Pytest runs 18 cases at raw-frame ceilings of 96 and 8192
bytes; compact transfer cases use a 64-byte local fragment size. The fixture
also enables concurrent scheduler requests to exercise reordered completions.

Component architecture and operation are described in the
[RTL Reference](../../../docs/src/rtl/openenoc_endpoint_dma_engine.rst).

## Test Coverage

The suite covers:

- raw TX/RX with unaligned addresses, full Ethernet frames, descriptor claims,
  and length/status reporting;
- peer mirror-to-remote writes and mirror-to-local reads with exact payload and
  guard-byte checks;
- fragmentation, slot reuse, concurrent peers, reordered completions, and
  final-fragment metadata;
- fragment-size rounding, configuration snapshots, valid boundaries, and
  invalid-setting rejection;
- 8192-byte unaligned raw TX across two local reads, including source errors in
  either part;
- scalar RMEM validation, command kinds, BitEnable, error recording, and
  separate IRQ notification;
- received READ/WRITE servicing, local windows, role disambiguation, and
  simultaneous initiator/responder traffic;
- local/remote error encoding, full-width wire causes, and original AXI-cause
  precedence;
- partial writes, late framing errors, terminal-status joins, and bilateral
  failure reporting;
- sticky peer/raw errors, independent clear commands, simultaneous new failure,
  and clearing during active transfers;
- IRQ gating, retained event metadata, admission/commit stalls, and one commit
  per admitted event;
- command, CSR, IRQ, AXIS, and AXI output stability under backpressure and
  between clock edges.

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
