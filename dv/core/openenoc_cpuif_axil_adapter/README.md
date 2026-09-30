<!-- SPDX-FileCopyrightText: 2026 Enio Kaljic -->
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# openENOC CPUIF to AXI4-Lite Adapter Test Suite

## Overview

This cocotb suite verifies `openenoc_cpuif_axil_adapter` in isolation. The
SystemVerilog wrapper instantiates only the DUT, one `openenoc_cpuif_if`, and
one `taxi_axil_if`; no CSR block, memory, crossbar, processor, or endpoint
component is included.

The adapter accepts one native CPUIF operation at a time and converts it into
an AXI4-Lite read or write transaction. A request can fall through directly to
the AXI request channels, while internal state retains any channel that is not
accepted immediately. The next CPUIF request may launch in the acknowledgement
cycle of the preceding operation, avoiding an idle pipeline cycle.

CPUIF write bit enables must be byte-uniform. Each fully enabled byte maps to
one AXI `WSTRB` bit. AXI `OKAY` responses clear the corresponding CPUIF error;
all other response values set it.

## Test Coverage

The cocotb suite covers:

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

## Default Configuration

The isolated SystemVerilog wrapper uses:

```text
DATA_W=32
ADDR_W=32
```

The AXI strobe width is derived as `DATA_W/8`. CPUIF and AXI4-Lite address,
data, and strobe widths must agree.

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
