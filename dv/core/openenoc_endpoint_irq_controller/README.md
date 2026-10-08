<!-- SPDX-FileCopyrightText: 2026 Enio Kaljic -->
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# openENOC Endpoint IRQ Controller Test Suite

## Overview

This cocotb suite verifies the IRQ controller in isolation from the processor,
CSR register block, and event producers. The wrapper flattens CSR fields and
event interfaces for cocotb. Eight cases run in eight configurations covering
1–7 producer ports, FIFO depths 1, 3, 4, 7, 8, 16, and 260, peer widths up to
11 bits, and sequence widths up to 16 bits.

Component architecture and operation are described in the
[RTL Reference](../../../docs/src/rtl/openenoc_endpoint_irq_controller.rst).

## Test Coverage

The suite covers:

- reset of claims, reservations, sequence state, and sticky diagnostics;
- locally disabled admissions and all six source enables, including RMEM_ERROR;
- per-producer reservations, including independent initiator/responder ports
  sharing source 0;
- independent round-robin admission and commit arbitration;
- FIFO-full backpressure, capacity reuse, and simultaneous claim
  enqueue/dequeue;
- ordered, stable claims with preserved peer indices and exact completion-token
  matching;
- invalid tokens, nonzero unused token bits, and commits without reservations;
- global IRQ masking, sequence wraparound, arbitrary FIFO depths, and 8-bit
  status saturation;
- registered output stability and one application of held CSR completion/clear
  commands.

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
