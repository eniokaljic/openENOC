<!-- SPDX-FileCopyrightText: 2026 Kerim Bavcic -->
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# openENOC Shared-Bus Switch Test Suite

## Configuration

Edit `Makefile` to configure the direct cocotb run:

```Makefile
export PARAM_NUM_OF_INTERFACES := 4
export PARAM_TABLE_DEPTH := 8
export PARAM_DATA_W := 32
export PARAM_KEEP_W := 4
export PARAM_KEEP_EN := 1
export PARAM_FABRIC_DATA_W := 32
export PARAM_PORT_FIFO_DEPTH := 64
export PARAM_PORT_SIDE := 15
```

`NUM_OF_INTERFACES` must be in the range 2 to 32, `TABLE_DEPTH` must be at
least one, and `FABRIC_DATA_W` must be a multiple of eight. Each external port
must use 8-bit byte lanes, and its byte-lane count and the fabric byte-lane
count must have an integer ratio. `PORT_FIFO_DEPTH` is expressed in bytes. It
must be an exact multiple of the wider stream's byte-lane count, and the
resulting number of widest-side words must be a power of two and at least two.
Bit `n` of `PORT_SIDE` selects side A (`0`) or side B (`1`) for port `n`. The
default configuration gives all external ports the same clock and 32-bit data
width.

## Running Tests

### Option 1: Cocotb (with waveform generation)
Runs Cocotb tests based on the module configuration specified in the Makefile.
```bash
./run_tests.sh waves
# Generates waveforms and opens gtkwave
```

### Option 2: Pytest
Uses the pytest framework to iterate through different configurations and run the Cocotb tests for each configuration.
```bash
./run_tests.sh pytest
# Uses pytest parameterization to run all configurations
```
