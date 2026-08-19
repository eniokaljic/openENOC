<!-- SPDX-FileCopyrightText: 2026 Enio Kaljic -->
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# openENOC AXI4-Lite RAM Test Suite

## Overview

This test suite verifies the `openenoc_axil_ram` generic AXI4-Lite memory.
The DUT derives its data and strobe widths from `taxi_axil_if`, implements a
byte-addressed power-of-two aperture, and optionally initializes its contents
from a `$readmemh`-compatible file.

The bundled `imem.mem` is copied from `build/sw/openenoc_full_endpoint/imem.mem` and contains
the current PicoRV32 CSR smoke-test firmware. It is intentionally shorter than
the test RAM so that the tests also verify zero-filled locations following the
loaded image.

## Test Coverage

The cocotb suite covers:

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
- request idle insertion and response backpressure;
- deterministic randomized read/write stress;
- `OKAY` read and write responses.

Simultaneous read and write operations to the same memory word are not assigned
a portable read-during-write value. Such collisions should be prevented or
resolved by the integrating system when a specific behavior is required.

## Default Configuration

The direct Makefile flow uses:

```text
DATA_W=32
ADDR_W=10
AXIL_ADDR_W=32
PIPELINE_OUTPUT=0
INIT_FILE=<absolute path to imem.mem>
```

`ADDR_W` is the width of the byte-addressed local aperture. The internal word
depth is therefore `2**ADDR_W / (DATA_W/8)`.

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
