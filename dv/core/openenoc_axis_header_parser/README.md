<!-- SPDX-FileCopyrightText: 2026 Kerim Bavcic -->
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# openENOC Axis Header Parser Test Suite

## Configuration

Edit `Makefile` to configure parameters.

```Makefile
export PARAM_DATA_W := 32
export PARAM_KEEP_EN := 1
export PARAM_KEEP_W := 4
export PARAM_STRB_EN := 0
export PARAM_LAST_EN := 1
export PARAM_USER_W := 128
export PARAM_DEPTH := 0
export PARAM_M_REG_TYPE := 2
```

**Important:** `PARAM_USER_W` must be at least 128 so the full header fits on
`m_axis.tuser`, and `PARAM_DATA_W` must be a multiple of 8.

## Running Tests

### Option 1: Make
Builds and runs the default configuration from the `Makefile` (the TestFactory
sweep of frame sizes, idle and backpressure combinations).

```bash
./run_tests.sh
```

### Option 2: Pytest
Uses `pytest` + `cocotb_test` to sweep multiple `DATA_W` configurations.

```bash
./run_tests.sh pytest
```

### Option 3: Waves
Builds and runs simulation with waveform dumping enabled.

```bash
./run_tests.sh waves
```
