<!-- SPDX-FileCopyrightText: 2026 Enio Kaljic -->
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# openENOC PicoRV32 AXI4-Lite Adapter Test Suite

## Overview

This cocotb suite verifies the `openenoc_picorv32_axil_adapter` bridge between
the native PicoRV32 memory interface, its look-ahead interface, and an
AXI4-Lite master port.

## Test Coverage

The suite covers:

- independent AW and W handshakes in either order;
- stable AXI request payloads while `VALID && !READY`;
- instruction/data `ARPROT` generation;
- partial writes through all non-zero `WSTRB` values;
- read and write response delivery to the native interface;
- randomized independent AW, W, and AR backpressure;
- response ordering with one native request outstanding;
- back-to-back look-ahead capture on a response cycle;
- direct native requests without look-ahead; and
- reset during a stalled transaction and recovery after reset.

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
