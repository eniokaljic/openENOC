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

From this directory, run the full CSR RTL suite and generate an FST waveform:

```bash
make
```

After simulation, open the generated FST in GTKWave:

```bash
make wave
```

Run the two basic register checks through the hardware-oriented entry point:

```bash
make hwtest
```

This entry currently uses the generated simulator model through
`HardwareInterface`; it does not access a physical board.

Remove generated simulation artifacts:

```bash
make clean
```

Simulation builds, `results.xml`, and `dump.fst` are stored under
`build/dv/hal/openenoc_endpoint_full/sim_build/`. `make wave` opens this
FST in GTKWave. Python bytecode and temporary files use the same component's
build directory; see the [shared output layout](../../README.md#generated-artifacts).
