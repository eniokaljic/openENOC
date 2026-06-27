<!-- SPDX-FileCopyrightText: 2026 Enio Kaljic -->
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# openENOC Ethernet Adapter Test Suite

## Overview

This test suite validates the `openenoc_eth_adapter` module, which connects two symmetric `openenoc_eth_if` interfaces through bidirectional AXI4-Stream asynchronous FIFOs.

The adapter provides clock-domain crossing and data-width adaptation between two Ethernet-like openENOC links. Traffic in the A-to-B direction is transferred from `eth_a.a2b` to `eth_b.a2b`, while traffic in the B-to-A direction is transferred from `eth_b.b2a` to `eth_a.b2a`.

## Tooling

This project uses the following tooling:

* **[oss-cad-suite-build](https://github.com/yosyshq/oss-cad-suite-build)** - Open source CAD tools suite
* **OS:** Ubuntu 24.04

## Test Structure

The verification environment consists of:

* `test_openenoc_eth_adapter.sv` - SystemVerilog wrapper around the DUT
* `test_openenoc_eth_adapter.py` - cocotb testbench and pytest runner
* `Makefile` - direct cocotb simulation entry point
* `openenoc_eth_adapter.sv` - device under test
* `openenoc_eth_if.sv` - bidirectional openENOC Ethernet-like interface
* `taxi_axis_if.sv` - AXI4-Stream interface definition
* `taxi_axis_async_fifo.sv` - asynchronous FIFO used inside the adapter

## Adapter Configuration

The adapter connects two independently parameterized interface instances. Side A and side B can use different AXI4-Stream data widths.

Example Makefile configuration:

```Makefile
export PARAM_A_DATA_W := 8
export PARAM_A_KEEP_EN := $(shell expr $(PARAM_A_DATA_W) \> 8)
export PARAM_A_KEEP_W := $(shell expr \( $(PARAM_A_DATA_W) + 7 \) / 8)

export PARAM_B_DATA_W := 512
export PARAM_B_KEEP_EN := $(shell expr $(PARAM_B_DATA_W) \> 8)
export PARAM_B_KEEP_W := $(shell expr \( $(PARAM_B_DATA_W) + 7 \) / 8)
```

The FIFO depth is specified in FIFO words. When `KEEP_EN` is enabled, this effectively corresponds to byte-lane units. The depth should therefore scale with the widest interface to avoid creating a degenerate FIFO with only one internal storage cycle.

```Makefile
export PARAM_DEPTH := $(shell python -c "print(2 * max($(PARAM_A_KEEP_W), $(PARAM_B_KEEP_W)))")
```

For streaming operation, the test configuration uses cycle-based FIFO mode:

```Makefile
export PARAM_FRAME_FIFO := 0
export PARAM_DROP_OVERSIZE_FRAME := 0
export PARAM_DROP_BAD_FRAME := 0
export PARAM_DROP_WHEN_FULL := 0
export PARAM_MARK_WHEN_FULL := 0
export PARAM_FRAME_PAUSE := 0
```

This allows frames larger than the FIFO depth to pass through the adapter as streaming data, provided that the downstream side eventually accepts the traffic.

## Running Tests

### Option 1: Pytest

Uses `pytest` and `cocotb_test` to sweep multiple A/B data-width combinations.

```bash
pytest -s -vv test_openenoc_eth_adapter.py
```

The pytest configuration verifies asymmetric data-width combinations using:

```python
@pytest.mark.parametrize(
    ("a_data_w", "b_data_w"),
    itertools.combinations([8, 16, 32, 64, 128, 256, 512], 2)
)
```

Since the adapter is symmetric and both directions are tested internally, equal-width and reversed-width combinations do not need to be tested separately in the full regression.

### Option 2: Makefile

Runs a single configuration selected through Makefile parameters.

```bash
make
```

To enable waveform dumping:

```bash
make WAVES=1
```

## Running Tests

### Option 1: Pytest

Uses `pytest` + `cocotb_test` to sweep multiple data-width configurations between side A and side B.

```bash
./run_tests.sh pytest
```

### Option 2: Waves

Builds and runs simulation with waveform dumping enabled.

```bash
./run_tests.sh waves
```

## Pytest Configuration

The pytest configuration verifies asymmetric data-width combinations using:

```python
@pytest.mark.parametrize(
    ("a_data_w", "b_data_w"),
    itertools.combinations([8, 16, 32, 64, 128, 256, 512], 2)
)
```

Since the adapter is symmetric and both directions are tested internally, equal-width and reversed-width combinations do not need to be tested separately in the full regression.


## Test Coverage

The test suite covers the following scenarios:

### A-to-B Transfer

Verifies that frames transmitted on `eth_a.a2b` are received correctly on `eth_b.a2b`.

Coverage includes:

* Multiple payload lengths
* Width adaptation
* Clock-domain crossing
* Optional source idle insertion
* Optional sink backpressure
* TID, TDEST, and TUSER preservation

### B-to-A Transfer

Verifies that frames transmitted on `eth_b.b2a` are received correctly on `eth_a.b2a`.

Coverage includes:

* Multiple payload lengths
* Width adaptation
* Clock-domain crossing
* Optional source idle insertion
* Optional sink backpressure
* TID, TDEST, and TUSER preservation

### Bidirectional Transfer

Verifies that both adapter directions can operate correctly at the same time.

This test sends frames through both independent AXI4-Stream paths and checks that traffic in one direction does not corrupt or block traffic in the opposite direction.

### Initial Sink Backpressure

Verifies that the adapter correctly buffers data when the receiving side is paused before a frame is transmitted.

Separate tests are used for:

* A-to-B initial sink pause
* B-to-A initial sink pause

### Bidirectional Stress Test

Sends mixed frame sizes in both directions to exercise the adapter under sustained traffic.

The stress test generates:

* 30 frames with random payload lengths between 20 and 256 bytes
* 2 jumbo frames with payload length of 9000 bytes

This checks that the adapter can handle both normal Ethernet-sized traffic and jumbo-frame transfers in streaming FIFO mode.

## Directed Frame Lengths

Directed transfer tests use a fixed set of 16 frame lengths independent of the AXI4-Stream data width:

```python
[20, 21, 31, 32, 33, 63, 64, 65, 127, 128, 129, 255, 256, 257, 511, 512]
```

The list covers the minimum frame length used by the testbench, boundary lengths around common power-of-two sizes, and the maximum directed-test frame length of 512 bytes.

## Notes

For very wide data buses, such as 512-bit AXI4-Stream, simulation time can increase significantly if the FIFO depth or the number of generated frames is too large. The regression therefore avoids unnecessary full cross-product testing and uses targeted asymmetric width combinations.

For very narrow buses, such as 8-bit AXI4-Stream, jumbo frames require many simulation cycles because each byte is transferred as a separate AXI4-Stream beat. For this reason, jumbo frames are covered only by a single bidirectional stress test.
