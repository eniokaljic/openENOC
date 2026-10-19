<!-- SPDX-FileCopyrightText: 2026 Enio Kaljic -->
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# openENOC Full Endpoint Test Suite

## Running Tests

The DV Makefile builds `endpoint_test` for `openenoc_endpoint_full` with `DEBUG=1`
before simulation. Pytest invokes the same `firmware` target once per session.
The software build's default `DEBUG=0` therefore does not disable DV assertions;
a firmware build failure stops the tests before simulation.

The testbench loads `build/sw/openenoc_endpoint_full/imem.mem`.

Activate the project virtual environment, change to this directory, and run
all loopback and assertion cases. The suite builds the required debug firmware
automatically:

```bash
./run_tests.sh pytest
```

To build the firmware separately:

```bash
make -C ../../../sw APP=endpoint_test EP=openenoc_endpoint_full DEBUG=1
```

Run the default configuration and generate an FST waveform:

```bash
./run_tests.sh waves
```

Remove generated simulation artifacts:

```bash
./run_tests.sh clean
```

Generated simulation artifacts use
`build/dv/endpoints/openenoc_endpoint_full/sim_build/` for Make and
`sim_build/pytest/<case>/` under the same component directory for pytest.
Results and FST waveforms stay with each simulation build. Python bytecode and
temporary files also stay under the component's build directory; see the
[shared output layout](../../README.md#generated-artifacts).
