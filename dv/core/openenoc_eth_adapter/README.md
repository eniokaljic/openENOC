<!-- SPDX-FileCopyrightText: 2026 Enio Kaljic -->
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# openENOC Ethernet Adapter Test Suite

## Overview

This cocotb suite verifies bidirectional Ethernet adaptation using independently
clocked stream fixtures. Pytest sweeps asymmetric pairs from widths 8, 16, 32,
64, 128, 256, and 512 bits. The default waveform configuration uses 8/512-bit
streams. The fixture uses two widest-side storage beats and streaming FIFO
policy.

Component architecture and operation are described in the
[RTL Reference](../../../docs/src/rtl/openenoc_eth_adapter.rst).

## Test Coverage

The suite covers:

- A-to-B and B-to-A frame preservation with width conversion and clock-domain
  crossing;
- source idle insertion, sink backpressure, and TID/TDEST/TUSER preservation;
- simultaneous traffic without cross-direction corruption;
- initial sink pauses in each direction;
- directed frame lengths 20, 21, 31, 32, 33, 63, 64, 65, 127, 128, 129, 255,
  256, 257, 511, and 512 bytes;
- bidirectional stress with 30 random 20–256-byte frames and two 9000-byte
  jumbo frames.

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
