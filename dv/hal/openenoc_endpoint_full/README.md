<!-- SPDX-FileCopyrightText: 2026 Enio Kaljic -->
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# openENOC CSR-Based Test Suite

## Overview

This cocotb suite verifies the generated full-endpoint CSR RTL through AXI4-Lite
using the generated PeakRDL Python register model. A thin SV wrapper supplies
hardware status and command acknowledgements. Seven existing cases run through
the cocotb Makefile flow; this suite has no pytest parameter sweep. FST
tracing is enabled on every simulation run.

Generate the RTL and register model from the repository root before running:

```bash
make -C hal all
```

Register-bank operation is described in the
[RTL Reference](../../../docs/src/rtl/openenoc_endpoint_full_csr.rst), and the
callback/backend arrangement in
[Verification Infrastructure](../../../docs/src/verification.rst).

## Test Coverage

The suite covers:

- callback-driven Python register-model access to actual AXI4-Lite RTL;
- test register and multi-field register writes, readback, and defaults;
- full-width RMEM/DMA timeout storage and neighboring-register preservation;
- independent unicast/multicast MAC configuration and RMEM_ERROR IRQ enable;
- fragment-size reset, generated register ordering, and unrounded readback;
- per-peer sticky error status and independently acknowledged clear commands;
- independent raw TX/RX error records and held `clear_errors` acknowledgements.

## Running Tests

Run the full CSR RTL suite:

```bash
make
```

Run the default configuration and generate an FST waveform:

```bash
make
```

Remove generated simulation artifacts:

```bash
make clean
```
