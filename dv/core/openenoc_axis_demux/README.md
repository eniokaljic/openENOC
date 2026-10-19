<!-- SPDX-FileCopyrightText: 2026 Kerim Bavcic -->
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# openENOC Axis Demux Test Suite

## Configuration

Edit `Makefile` to set routing mode and parameters:

```Makefile
export PARAM_TID_ROUTE := 0              # ID-based routing (not tested)
export PARAM_TDEST_ROUTE := 0            # Set to 1 for unicast tests
export PARAM_TUSER_BITMAP_ROUTE := 1     # Set to 1 for multicast tests
```

**Note:** Only one of TDEST_ROUTE or TUSER_BITMAP_ROUTE should be set to 1 at a time.

**Module parameters** (can be customized):
- `PARAM_M_COUNT` - Number of output ports (default: 4)
- `PARAM_DATA_W` - Data width in bits (default: 8)
- `PARAM_TDEST_ROUTE` - Use TDEST_ROUTE (default: 1)
- `PARAM_TUSER_BITMAP_ROUTE ` - Use TUSER_BITMAP_ROUTE (default: 0)

## Running Tests

### Option 1: Cocotb (with waveform generation)
Runs Cocotb tests based on the module configuration specified in the Makefile.
```bash
./run_tests.sh waves
# Generates waveforms and opens gtkwave
```

### Option 2: Pytest
Uses the pytest framework (test_openenoc_axis_demux.py) to iterate through different configurations and run the Cocotb tests for each configuration.
```bash
./run_tests.sh pytest
# Uses pytest parameterization to run all configurations
```

### Configuration Validation
The test suite validates that exactly one routing mode is enabled:
- If neither TDEST_ROUTE nor TUSER_BITMAP_ROUTE is set → **ERROR: Makefile is misconfigured**
