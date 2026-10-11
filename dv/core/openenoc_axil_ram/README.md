<!-- SPDX-FileCopyrightText: 2026 Enio Kaljic -->
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# openENOC AXI4-Lite RAM Test Suite

## Overview

This cocotb suite verifies AXI4-Lite RAM with and without file initialization.
The bundled `imem.mem` provides a partial firmware image so the tests can
check zero-filled locations after the loaded contents. The default fixture
uses 32-bit data, a 10-bit local aperture, and 32-bit bus addresses.

Component architecture and operation are described in the
[RTL Reference](../../../docs/src/rtl/openenoc_axil_ram.rst).

## Test Coverage

The suite covers:

- zero initialization when `INIT_FILE` is empty;
- little-endian initialization from `imem.mem`;
- zero filling after a partial initialization file;
- 8-, 16-, 32-, and 64-bit AXI4-Lite data widths;
- read-response pipeline disabled and enabled;
- aligned and unaligned accesses;
- byte-strobe behavior through partial and cross-word writes;
- first and last locations in the configured aperture;
- truncation of upper system-address bits to the local RAM aperture;
- memory-content preservation across reset;
- independent and concurrent AXI read and write channels;
- independent AW and W arrival timing;
- bubble-free back-to-back AW/W and AR transfers when responses are accepted;
- stable `B` and `R` responses while backpressured;
- request idle insertion and randomized channel/response backpressure;
- deterministic randomized read/write stress;
- `OKAY` read and write responses.

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
