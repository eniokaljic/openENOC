# openENOC Axis Demux Test Suite

## Overview

This test suite validates the `openenoc_axis_demux` module, which demultiplexes AXI Stream input into multiple outputs based on routing configuration.

## Tooling

This project uses the following tooling:

- **[oss-cad-suite-build](https://github.com/yosyshq/oss-cad-suite-build)** - Open source CAD tools suite
- **OS:** Ubuntu 24.04

## Routing Modes

The demux supports three routing modes, but only two are currently tested:

### 1. **TID_ROUTE** (Unicast/ID-based Routing)
- Routes packets based on the TID (Transaction ID) field
- ⚠️ **Currently not tested** 

### 2. **TDEST_ROUTE** (Unicast/Destination-based Routing)
- Routes packets based on the TDEST field
- Packets are distributed to a single output port determined by TDEST
- Useful for traditional address-based routing

### 2. **TUSER_BITMAP_ROUTE** (Multicast/User-Bitmap Routing)
- Routes packets based on TUSER field interpreted as a bitmap
- Each bit in TUSER selects one or more output ports
- Supports multicast (one packet to multiple ports)
- Includes "all-or-nothing" atomic delivery: all targeted ports receive the packet simultaneously or none do

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

## Test Coverage

**TDEST_ROUTE Tests:**
- Single-port unicast delivery
- Idle insertion and backpressure handling
- Multiple data widths and output port counts

**TUSER_BITMAP_ROUTE Tests:**
- Multicast to multiple ports
- Idle insertion and backpressure handling
- Multiple data widths and output port counts
- Drop packets (empty bitmap)
- All-or-nothing atomic delivery with varying backpressure per port
