<!-- SPDX-FileCopyrightText: 2026 Enio Kaljic -->
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# openENOC CSR-Based Test Suite

## Running Tests

Generate the RTL and register model from the repository root before running:

```bash
make -C hal all
```

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
