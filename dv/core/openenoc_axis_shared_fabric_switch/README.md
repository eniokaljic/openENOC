<!-- SPDX-FileCopyrightText: 2026 Kerim Bavcic -->
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# openENOC Shared-Fabric Switch Test Suite

## Overview

This integration suite validates the `openenoc_axis_shared_fabric_switch`
module. The switch combines per-port clock-domain and data-width adapters, a
frame-aware round-robin AXI Stream arbiter/multiplexer, the openENOC forwarding
engine and forwarding table, and a bitmap-routed AXI Stream demultiplexer.

The test wrapper instantiates the switch, four `openenoc_eth_if` links, and one
`openenoc_switch_if`. The generated CSR register block is intentionally not
instantiated. Flattened testbench signals drive the control fields of
`openenoc_switch_if` directly from cocotb and expose the corresponding status
and acknowledge signals.

All ports use side A externally while the switch uses side B. Cocotb therefore
transmits frames through `a2b` and receives them through `b2a`. Constant-index
AXI Stream bridges expose these directions as `port_rx_axis` and
`port_tx_axis`; this avoids unreliable VPI access to nested interface arrays
with Verilator.

## Datapath Under Test

For each input frame, the test exercises the complete shared datapath:

1. The ingress asynchronous FIFO adapter moves the frame into the fabric clock
     domain and adapts it to `FABRIC_DATA_W`.
2. `taxi_axis_arb_mux` selects one ingress using frame-aware round-robin
     arbitration and writes the selected port index into `tid`.
3. `openenoc_axis_forwarding_engine` extracts the destination and source MAC
     addresses, requests lookup and learning operations, removes the ingress port
     from the forwarding result, and writes the egress bitmap into `tuser`.
4. `openenoc_forwarding_table` returns either a matching table bitmap or the
     configured default bitmap. In unmanaged mode it also learns source MAC
     addresses automatically.
5. `openenoc_axis_demux` uses the `tuser` bitmap to replicate the frame to all
     selected outputs with all-or-none multicast backpressure.
6. The egress asynchronous FIFO adapters return the frames to the individual
     port clock domains.

## Control Interface Model

The wrapper exposes the following CSR-equivalent controls to cocotb:

- managed or unmanaged operation mode,
- pause request and pause-done status,
- default forwarding bitmap,
- forwarding-table CPU address, write data, bit enables, request, and
    acknowledge signals.

Each forwarding-table entry occupies 16 bytes and contains four 32-bit words:

| Word | Byte offset | Contents |
|---|---:|---|
| MAC low | 0 | MAC address bits 31:0 |
| MAC high | 4 | MAC address bits 47:32 |
| Interface bitmap | 8 | Egress-port bitmap |
| Configuration | 12 | Entry-enable bit |

The managed-mode tests assert `pause_request` and wait for `pause_done` before
programming the table. This models the intended software sequence and ensures
that modification occurs at a frame boundary.

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
```

`NUM_OF_INTERFACES` must be in the range 2 to 32, `TABLE_DEPTH` must be at
least one, and `FABRIC_DATA_W` must be a multiple of eight. The current basic
configuration gives all external ports the same clock and 32-bit data width.

## Running Tests

### Option 1: Make

Runs the cocotb tests using the configuration in `Makefile` and prints the
simulator log and timestamps directly:

```bash
make clean
make
```

Generate and open waveforms with:

```bash
./run_tests.sh waves
```

### Option 2: Pytest

Runs the simulator through the pytest/cocotb-test runner:

```bash
./run_tests.sh pytest
```

Remove generated test artifacts with:

```bash
./run_tests.sh clean
```

## Test Coverage

**Functional checks:**

- End-to-end frame transfer through ingress adaptation, arbitration,
    forwarding, demultiplexing, and egress adaptation
- Lookup misses using the CSR default-forwarding bitmap
- Managed forwarding-table programming through the CPU request/acknowledge
    interface
- Lookup hits and multicast replication
- Autonomous source-MAC learning in unmanaged mode
- Removal of the ingress interface from the egress bitmap
- Preservation of frame data and `tdest`
- Detection of frames delivered to unexpected egress ports
- Pause request and pause-done sequencing before managed table updates

**Scenarios:**

- `test_default_forwarding`: an unknown destination arriving on port 0 uses
    default bitmap `0010` and exits only through port 1.
- `test_managed_multicast_hit`: software programs a destination with bitmap
    `1100`; the matching frame is replicated to ports 2 and 3.
- `test_unmanaged_learning`: a source observed on port 0 is learned and then
    reached by a frame arriving on port 1.
- `test_ingress_port_suppression`: a table result selecting ports 0 and 1 is
    reduced to port 1 when the frame arrived on port 0.
- `test_arbiter_overwrites_source_tid`: a frame carrying an intentionally
    incorrect source `tid` enters physical port 2; the arbiter replaces it with
    2, forwarding suppresses port 2, and every output copy carries `tid = 2`.
- `test_round_robin_between_active_ingresses`: ports 0 and 1 are filled while
    forwarding is paused; after resume, frame-boundary observations verify that
    both active inputs are served alternately and that each frame retains the
    arbiter-generated ingress identity.
- `test_zero_bitmap_drops_frame`: an unknown destination with a zero default
    bitmap is consumed without appearing on any egress interface.
- `test_header_only_and_unaligned_frames`: Ethernet header-only frames and
    several non-word-aligned lengths verify final-beat `tkeep` handling.
- `test_back_to_back_frame_burst`: twelve consecutive frames of different
    lengths verify boundaries, ordering, sidebands, and sustained operation.
- `test_all_ingress_ports_simultaneously`: all four ingress FIFOs are preloaded
    with three frames; each arbitration round must serve every port once, and all
    twelve frames must reach their independently configured outputs.
- `test_unmanaged_mac_moves_to_new_port`: a learned source moves from port 0 to
    port 2, and a subsequent lookup must use the updated location.
- `test_multicast_with_output_backpressure`: eight multicast frames traverse
    two independently stalled outputs without loss, duplication, or reordering.

**TestFactory matrix:**

`run_factory_routing` follows the same factory pattern used by the other
openENOC and Taxi component tests. It generates the Cartesian product of:

- three routes: unicast, two-port multicast, and all-port multicast with
    ingress suppression,
- AXI input idle insertion disabled or enabled,
- AXI output backpressure disabled or enabled.

Every generated case sends Ethernet frames with payload lengths 0, 1, 3, 16,
47, and 128 bytes. It checks payload ordering and integrity, `tid` replacement,
`tdest` preservation, multicast copies, and absence of traffic on unselected
ports.

**Pytest parameter sweep:**

The pytest runner repeats the complete explicit-test and TestFactory suite for
the following `(DATA_W, FABRIC_DATA_W, TABLE_DEPTH, PORT_FIFO_DEPTH)` tuples:

- `(8, 32, 5, 64)`
- `(16, 64, 8, 64)`
- `(32, 32, 8, 64)`
- `(64, 16, 8, 128)`

This covers width expansion, equal-width transfer, width contraction, a
non-power-of-two forwarding-table depth, and two FIFO depths. The interface
count remains four because the directed integration scenarios intentionally
exercise all four bitmap positions.

Independent port clocks, mixed external data widths, CPU reads, and table-full
replacement behavior are not yet covered by this suite.
