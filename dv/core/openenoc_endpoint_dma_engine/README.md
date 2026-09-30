<!-- SPDX-FileCopyrightText: 2026 Enio Kaljic -->
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# openENOC Endpoint DMA Engine Test Suite

## Overview

This cocotb suite verifies `openenoc_endpoint_dma_engine` in isolation with a
cocotb AXI4 memory model and AXI4-Stream source and sink models. Cocotb drives
DMA commands and peer configuration directly through flattened signals on
`openenoc_endpoint_if`, and implements a one-cycle behavioral responder for
the peer lookup handshake. The generated CSR block, its bridge, and the peer
lookup RTL are not part of this testbench.

The wrapper exposes one AXI4-Stream in each direction between the DMA and oETP
engines and one AXI4 Full master toward memory.

The IRQ event controller and oETP protocol engine are represented by their
ready/valid interfaces. This permits deterministic checking of DMA command,
completion, metadata, admission, and commit behavior without duplicating
their implementations in the testbench.

## Test Coverage

The cocotb suite covers:

- non-oETP TX DMA from unaligned local memory through the shared output AXIS;
- non-oETP RX DMA through the shared input AXIS into an unaligned buffer;
- endpoint request clearing, idle, armed, done, error, error code, and transferred
  or received length status;
- invalid non-oETP descriptors;
- peer mirror-to-remote DMA with local reads and remote WRITE commands;
- peer mirror-to-local DMA with remote READ commands and local writes;
- fragmentation above `MAX_DMA_FRAME_SIZE_BYTES` with sequence and final
  fragment metadata;
- one address translation at the initiating endpoint;
- peer lookup request/response handshakes and coherent configuration snapshots;
- responder READ and WRITE requests using final local addresses;
- responder completion metadata and invalid responder requests;
- unaligned AXI4 reads and writes; and
- IRQ credit admission and one completion commit per accepted operation.

## Default Configuration

The DV wrapper uses 32-bit AXI4 and AXI4-Stream data, 32-bit addresses and
sequence numbers, four peers, and a reduced 64-byte maximum DMA frame size so
multi-fragment transfers remain compact.
The production module default remains 8192 bytes.

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
