<!-- SPDX-FileCopyrightText: 2026 Enio Kaljic -->
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# openENOC Endpoint Interface Test Suite

## Overview

This cocotb suite verifies the integrated endpoint interface without a CPU or
generated CSR register block. It uses AXI memory and Ethernet stream models,
an acknowledged local CPUIF fixture, and memory-error injection. Ten cases run
at AXI/Ethernet widths 32/32, 64/32, 32/64, and 64/8. The fixture has two peers,
128-byte transport FIFOs, two IRQ credits, four fragment slots, and a 64-byte
raw-frame ceiling.

Component architecture and operation are described in the
[RTL Reference](../../../docs/src/rtl/openenoc_endpoint_interface.rst).

## Test Coverage

The suite covers:

- direct RX availability before frame completion and direct TX completion after
  the transport FIFO;
- Ethernet/CSR backpressure and complete IRQ admission/commit accounting;
- raw DMA TX/RX, descriptor claims, and receive MAC filtering;
- sequential fragmented reads/writes, little-endian metadata, rounded MFS, and
  partial tails;
- fragment timeout, unsent-fragment cancellation, late responses, software
  restart, and remote errors;
- incoming memory requests, range checks, multicast writes, response
  suppression, and local events;
- bad EndOfData after memory TLAST, partial writes, and absence of rollback;
- initiating RMEM translation, BitEnable, failed-read ACK/data, timeout, and
  independent error notification;
- received RMEM access, delayed ACK, local errors, and zero-BitEnable writes;
- RMEM priority between bulk fragments and original AXI-cause preservation;
- full IRQ queue, independent CPUIF/ERROR_RSP completion, per-peer notification
  retention/coalescing, and enable changes;
- a new one-cycle CPUIF request on the preceding ACK cycle and recovery after
  failures.

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
