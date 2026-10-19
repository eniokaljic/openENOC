<!-- SPDX-FileCopyrightText: 2026 Kerim Bavcic -->
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# openENOC Forwarding Table Test Suite

## Configuration

Edit `Makefile` to configure parameters.

```Makefile
export PARAM_NUM_OF_INTERFACES := 8
export PARAM_TABLE_DEPTH := 32
```

`ADDR_WIDTH` is derived from `TABLE_DEPTH` (`$clog2(TABLE_DEPTH * 16)`) and is
not configurable.

## Running Tests

### Option 1: Pytest

Uses `pytest` + `cocotb_test` to sweep multiple configurations (`NUM_OF_INTERFACES`, `TABLE_DEPTH`).

```bash
./run_tests.sh pytest
```

### Option 2: Waveforms
Builds and runs simulation with waveform dumping enabled.

```bash
./run_tests.sh waves
```
