<!-- SPDX-FileCopyrightText: 2026 Kerim Bavcic -->
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# openENOC Shared-Fabric Switch Test Suite

## Overview

This integration suite validates the `openenoc_eth_shared_fabric_switch`
module. The switch combines per-port clock-domain and data-width adapters, a
frame-aware round-robin AXI Stream arbiter/multiplexer, the openENOC forwarding
engine and forwarding table, and a bitmap-routed AXI Stream demultiplexer.

The test wrapper instantiates the switch, a parameterized array of
`openenoc_eth_if` links, and one `openenoc_switch_if`. The default Makefile
configuration uses four links. The generated CSR register block is
intentionally not instantiated. Flattened testbench signals drive the control
fields of `openenoc_switch_if` directly from cocotb and expose the corresponding
status and acknowledge signals.

The wrapper acts as the peer opposite each switch port. For a side-B switch
port it transmits through `a2b` and receives through `b2a`; those directions are
reversed for a side-A switch port. Constant-index AXI Stream bridges expose both
cases uniformly as `port_rx_axis` and `port_tx_axis`. This also avoids
unreliable VPI access to nested interface arrays with Verilator.

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
- Pause requests asserted while a frame is active
- CPU readback through the switch CSR bridge
- Side-A, side-B, and mixed port orientations

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
- `test_managed_table_cpu_readback`: the highest valid table entry is written
    and all four CSR words are read back through the switch interface.
- `test_pause_completes_current_frame_and_blocks_next`: pause is asserted after
    arbitration starts a long frame; that frame drains, the next frame remains
    blocked, and forwarding resumes only after pause is released.

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

The pytest runner repeats all 14 directed tests and 12 TestFactory cases for
the following `(NUM_OF_INTERFACES, DATA_W, FABRIC_DATA_W, TABLE_DEPTH,
PORT_FIFO_DEPTH, PORT_SIDE)` tuples:

- `(4, 8, 32, 5, 64, 0b1111)`
- `(5, 24, 48, 8, 48, 0b10101)`
- `(4, 32, 32, 8, 64, 0b0000)`
- `(8, 64, 16, 8, 16, 0b10101010)`

This covers four, five, and eight interfaces; width expansion, equal-width
transfer, and width contraction; power-of-two and non-power-of-two stream
widths; a non-power-of-two forwarding-table depth; a minimum-size two-word
FIFO; and all-A, all-B, and mixed port orientations.

Independent port clocks, heterogeneous widths between ports, `TABLE_DEPTH=1`,
and table-full replacement behavior are not yet covered by this suite.
