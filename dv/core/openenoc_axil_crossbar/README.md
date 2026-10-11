<!-- SPDX-FileCopyrightText: 2026 Enio Kaljic -->
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# openENOC AXI4-Lite Crossbar Test Suite

## Overview

This cocotb suite verifies the AXI4-Lite crossbar and its address decoder,
read/write paths, and channel skid buffers.

Component architecture and operation are described in the
[RTL Reference](../../../docs/src/rtl/openenoc_axil_crossbar.rst).

## Test Coverage

The suite covers:

- address routing, decode errors, and reset;
- simultaneous initiators and response ordering across targets;
- independent AW/W backpressure and stable stalled payloads;
- sustained traffic with consecutive target-side AR, AW, and W handshakes when
  uncontended.

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
