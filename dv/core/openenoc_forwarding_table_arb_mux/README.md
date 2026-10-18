<!-- SPDX-FileCopyrightText: 2026 Kerim Bavcic -->
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# openENOC Forwarding Table Arbiter Multiplexer Test Suite

## Configuration

Edit `Makefile` to configure a direct cocotb run:

```Makefile
export PARAM_NUM_OF_INTERFACES := 4
```

## Running Tests

### Option 1: Cocotb with waveform generation

```bash
./run_tests.sh waves
```

### Option 2: Pytest parameter sweep

```bash
./run_tests.sh pytest
```
