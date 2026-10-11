<!-- SPDX-FileCopyrightText: 2026 Enio Kaljic -->
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# openENOC CPUIF to AXI4-Lite Adapter Test Suite

## Overview

This cocotb suite verifies `openenoc_cpuif_axil_adapter` in isolation with
native CPUIF and AXI4-Lite bus fixtures. The default fixture uses 32-bit
addresses and data. Component architecture and operation are described in
the [RTL Reference](../../../docs/src/rtl/openenoc_cpuif_axil_adapter.rst).

## Test Coverage

The suite covers:

- independent AXI write-address and write-data handshakes;
- write-data acceptance before write-address acceptance;
- stable AXI addresses and write payloads while stalled;
- CPUIF bit-enable to AXI byte-strobe conversion;
- AXI read-data delivery to CPUIF;
- propagation of AXI read and write response errors;
- one-cycle CPUIF acknowledgement strobes;
- simultaneous completion of one request and launch of the next request;
- bubble-free read-to-write handoff;
- suppression of AXI transfers and CPUIF acknowledgements during reset; and
- clearing a stalled transaction on reset.

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
