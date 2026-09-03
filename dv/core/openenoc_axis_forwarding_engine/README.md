<!-- SPDX-FileCopyrightText: 2026 Kerim Bavcic -->
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# openENOC Axis Forwarding Engine Test Suite

## Overview

This test suite validates the `openenoc_axis_forwarding_engine` module, which
parses the destination and source MAC addresses from each AXI Stream frame and
connects the stream data path to the lookup and learning interfaces of the
openENOC forwarding table.

The forwarding table is not instantiated. Its lookup and learning interfaces
are driven by a behavioral model in the Python testbench so that the forwarding
engine can be verified stand-alone.

The engine starts a lookup as soon as the six-byte destination MAC address is
complete. Source-address learning starts only after the destination lookup has
been acknowledged and the complete six-byte source MAC address has arrived. If
the source MAC is already present in a wide input beat, learning starts as soon
as the lookup completes; otherwise, the engine resumes parsing until the source
MAC is complete and then issues the learning request. Destination lookup and
source-address learning both apply backpressure as needed, and the buffered
frame is released only after all forwarding-table transactions associated with
its header have been acknowledged. This ordering prevents the next frame from
starting a new lookup while learning for the current frame is still pending on
the table's shared internal arbitration path.

The lookup result is attached to the released frame on `m_axis.tuser`. The
ingress interface index is carried on `s_axis.tid` and is removed from the
egress bitmap to prevent forwarding a frame back to its source interface.

## AXI Stream Input Contract

The MAC parser expects canonical packet-oriented `tkeep` usage:

- Every beat except the final beat of a frame must have all byte lanes valid.
- On the final beat (`tlast = 1`), valid bytes must be contiguous from the
	least-significant byte lane. Gaps in `tkeep` are not supported.
- When `KEEP_EN` is disabled, every byte lane is treated as valid.

The byte-counting and MAC-address extraction logic relies on this contract.
Frames with sparse `tkeep`, or with invalid lanes before valid lanes, are
outside the supported input format.

## Forwarding Table Model

The testbench implements the openENOC request/acknowledge handshake. The engine
asserts `lookup_if.req` or `learning_if.req` for one clock cycle and keeps the
associated payload stable while it waits. The model returns a single-cycle
acknowledge after a configurable latency. During each wait, the testbench checks
that the input is stalled and no buffered output beat is released.

Known destination MAC addresses are resolved using the model's entry map. A
lookup miss returns the configured default forwarding bitmap. Every accepted
lookup and learning request is recorded and checked for correct ordering and
contents.

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

## Test Coverage

**Functional checks:**

- Destination and source MAC extraction across different AXI Stream widths
- Lookup hit and miss handling
- Ingress interface removal from the forwarding bitmap
- Correct learning MAC address and one-hot ingress interface bitmap
- Frame payload integrity and `tid`/`tdest` pass-through
- Forwarding bitmap alignment on `m_axis.tuser`
- Zero forwarding bitmap with no lookup or learning for incomplete 1-5 byte
	destination addresses
- Zero forwarding bitmap and no learning for incomplete 6-11 byte headers
- Input stalling while lookup and learning acknowledgements are pending
- Stable request payloads throughout configurable acknowledgement latency

**Directed scenarios:**

- `test_incomplete_destination_address_sets_zero_bitmap`: frames ending before
	the complete six-byte destination address are released with `tuser = 0` and
	do not generate lookup or learning requests.
- `test_incomplete_source_address_sets_zero_bitmap`: frames containing a
	complete six-byte destination address but an incomplete source address are
	released with `tuser = 0` and do not generate learning requests.

**Scenarios (TestFactory):**

- Back-to-back frames with known and unknown destination MAC addresses
- Frame lengths of 32, 60, 79, and 128 bytes
- Idle insertion and output backpressure combinations
- Lookup and learning acknowledgement latencies of 2, 4, and 256 cycles

**Parameter sweep (pytest):**

- `DATA_W` in {8, 16, 24, 64, 128, 512}
