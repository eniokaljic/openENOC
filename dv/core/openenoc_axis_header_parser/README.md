<!-- SPDX-FileCopyrightText: 2026 Kerim Bavcic -->
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# openENOC Axis Header Parser Test Suite

## Overview

This test suite validates the `openenoc_axis_header_parser` module, which snoops
the first 16 bytes of every AXI Stream frame and presents them as a stable
128-bit header on `m_axis.tuser`. The frame payload (`tdata`) passes through
unchanged, delayed by the header so that `tuser` is valid from the first output
beat. No field splitting is performed — the raw 128-bit header is exposed on
`tuser` for a later block to parse.

Header layout (byte 0 = first byte on the wire = MSB of `tuser`):

| Field           | Bits           |
| --------------- | -------------- |
| Destination MAC | `tuser[127:80]` |
| Source MAC      | `tuser[79:32]`  |
| EtherType       | `tuser[31:16]`  |
| oETP Magic      | `tuser[15:8]`   |
| oETP Cmd        | `tuser[7:0]`    |

## Tooling

This project uses the following tooling:

- **[oss-cad-suite-build](https://github.com/yosyshq/oss-cad-suite-build)** - Open source CAD tools suite
- **OS:** Ubuntu 24.04

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

## Test Coverage

**Functional checks (per frame):**
- Payload (`tdata`) passes through unchanged
- 128-bit header is correct and stable on `tuser` for the whole frame

**Scenarios (TestFactory):**
- Multiple payload sizes, including header-only frames (0-byte payload)
- Back-to-back frames with distinct headers (header alignment under overlap)
- Idle insertion and backpressure combinations

**Parameter sweep (pytest):**
- `DATA_W` in {8, 16, 32, 64}
