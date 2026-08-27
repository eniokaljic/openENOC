<!-- SPDX-FileCopyrightText: 2026 Enio Kaljic -->
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# openENOC AXI4-Lite Crossbar Test Suite

This cocotb suite verifies the pipelined `openenoc_axil_crossbar` and its
internal `openenoc_axil_crossbar_*` components.

The tests cover address routing, simultaneous initiators, independent AW/W
backpressure, response ordering across targets, DECERR generation, reset,
payload stability while stalled, and sustained read/write traffic.  The
throughput tests require consecutive target-side AR, AW, and W handshakes when
there is no contention or downstream backpressure.

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
