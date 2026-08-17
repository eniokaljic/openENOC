<!-- SPDX-FileCopyrightText: 2026 Kerim Bavcic -->
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# openENOC Axis Switch Test Suite

## Overview

This test suite validates the `openenoc_axis_switch` module, which routes AXI Stream traffic from multiple inputs to multiple outputs.

## Routing Modes

The switch verification currently targets two routing modes:

### 1. **Unicast (TDEST-based Routing)**
- Routes each frame to one output port based on TDEST MSBs
- Useful for classical single-destination forwarding
- Activated when `PARAM_TUSER_BITMAP_ROUTE := 0`

### 2. **Multicast (TUSER Bitmap Routing)**
- Routes each frame based on TUSER bitmap bits
- Supports one-to-many delivery from one input to multiple outputs
- Includes empty-bitmap drop behavior
- Includes scheduler/contention scenarios between multiple inputs
- Activated when `PARAM_TUSER_BITMAP_ROUTE := 1`

## Configuration

Edit `Makefile` to configure parameters.

```Makefile
export PARAM_S_COUNT := 4
export PARAM_M_COUNT := 4
export PARAM_DATA_W := 8
export PARAM_TUSER_BITMAP_ROUTE := 1   # 0 = unicast (TDEST), 1 = multicast (TUSER bitmap)
export PARAM_S_REG_TYPE := 2
export PARAM_M_REG_TYPE := 0
```

**Important:** `PARAM_USER_W` should track `PARAM_M_COUNT` in multicast mode so every output has a matching bitmap bit.

## Running Tests

### Option 1: Pytest
Uses `pytest` + `cocotb_test` to sweep multiple configurations (`S_COUNT`, `M_COUNT`, `DATA_W`, and routing mode).

```bash
./run_tests.sh pytest
```

### Option 2: Waves
Builds and runs simulation with waveform dumping enabled.

```bash
./run_tests.sh waves
```

## Test Coverage

**Unicast (TDEST) tests:**
- Single-destination forwarding checks
- Multiple frame sizes
- Idle insertion and backpressure scenarios

**Multicast (TUSER bitmap) tests:**
- Multiple bitmap combinations (including all-target and subset delivery)
- Empty bitmap drop behavior
- Scheduler/contention scenario with overlapping output targets
- Idle insertion and backpressure scenarios
