<!-- SPDX-FileCopyrightText: 2026 Kerim Bavcic -->
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# openENOC Axis Forwarding Engine Test Suite

## Configuration

Edit `Makefile` to configure parameters.

```Makefile
export PARAM_NUM_OF_INTERFACES := 8
export PARAM_DATA_W := 8
export PARAM_KEEP_EN := 0
export PARAM_KEEP_W := 1
export PARAM_STRB_EN := 0
export PARAM_LAST_EN := 1
export PARAM_ID_EN := 1
export PARAM_ID_W := 8
export PARAM_DEST_EN := 1
export PARAM_DEST_W := 8
export PARAM_USER_EN := 1
export PARAM_USER_W := 8
```

**Important:** `PARAM_DATA_W` must be a multiple of 8 in the range 8 to 512.
`PARAM_ID_W` must be wide enough to represent every ingress interface, and
`PARAM_USER_W` must be at least `PARAM_NUM_OF_INTERFACES` so the complete
forwarding bitmap fits on `m_axis.tuser`.

## Running Tests

### Option 1: Cocotb (with waveform generation)
Runs Cocotb tests based on the module configuration specified in the Makefile.
```bash
./run_tests.sh waves
# Generates waveforms and opens gtkwave
```

### Option 2: Pytest
Uses the pytest framework (test_openenoc_axis_forwarding_engine.py) to iterate through different configurations and run the Cocotb tests for each configuration.
```bash
./run_tests.sh pytest
```
