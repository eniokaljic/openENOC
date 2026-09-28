<!-- SPDX-FileCopyrightText: 2026 Enio Kaljic -->
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# openENOC Endpoint IRQ Controller Test Suite

## Overview

This cocotb suite verifies the `openenoc_endpoint_irq_controller` in isolation
from the endpoint processor, generated CSR block, and event producers. The
SystemVerilog wrapper exposes the CSR-facing signals directly and converts the
flattened cocotb producer signals to an array of `openenoc_irq_event_if`
instances.

The controller reserves FIFO credits during event admission and converts each
reservation into an interrupt claim when its producer commits. Claim payloads
are stored in `taxi_axis_fifo`, while a separate logical occupancy count keeps
the configured FIFO capacity exact for non-power-of-two depths.

## Test Coverage

The cocotb suite covers:

- reset of FIFO, reservations, sequence state, and sticky error flags;
- transparent admission of locally disabled events and event classes disabled
  through `event_enable`;
- independent event enables for all five event sources;
- per-producer credit reservation and commit accounting;
- independent round-robin arbitration of simultaneous admission and commit
  requests;
- FIFO-full backpressure and same-cycle credit reuse during claim completion;
- simultaneous claim enqueue and dequeue;
- ordered claim delivery through `taxi_axis_fifo`;
- peer-index preservation for peer DMA events and zeroing for non-peer events;
- stable claims until an exact peer, source, and sequence completion match;
- rejection of invalid completion tokens;
- overflow detection for commits without reservations;
- IRQ masking through `global_enable` without removing pending claims;
- sequence-number increment and wraparound; and
- saturation of the 8-bit FIFO and reservation status fields.

## Default Configuration

The direct Makefile flow uses:

```Makefile
export PARAM_EVENT_PORTS := 4
export PARAM_FIFO_DEPTH := 4
export PARAM_PEER_IDX_W := 5
export PARAM_SEQUENCE_W := 4
```

`EVENT_PORTS`, `FIFO_DEPTH`, `PEER_IDX_W`, and `SEQUENCE_W` must all be at
least one. FIFO depths do not have to be powers of two.

The pytest parameter sweep uses:

| `EVENT_PORTS` | `FIFO_DEPTH` | `PEER_IDX_W` | `SEQUENCE_W` |
| ------------- | ------------ | ------------ | ------------ |
| 1 | 1 | 1 | 4 |
| 2 | 3 | 3 | 4 |
| 4 | 4 | 5 | 4 |
| 5 | 7 | 11 | 5 |
| 4 | 260 | 11 | 8 |

The sweep covers single-port and multi-port arbitration, minimum and
non-power-of-two FIFO depths, sequence wraparound, wide peer indices, and
8-bit status saturation for FIFO depths greater than 255.

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
