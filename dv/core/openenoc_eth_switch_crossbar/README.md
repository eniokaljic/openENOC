<!-- SPDX-FileCopyrightText: 2026 Kerim Bavcic -->
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# openENOC Crossbar Switch Test Suite

## Overview

This integration suite validates the `openenoc_eth_switch_crossbar` module. The
switch contains one forwarding engine per ingress port, a shared forwarding
table with independent lookup and learning arbitration, and a bitmap-routed AXI
Stream output switch. Independent noncontending paths can transfer frames
concurrently, while each contested output is arbitrated independently.

The test wrapper instantiates the switch, a parameterized array of
`openenoc_eth_if` links, and one `openenoc_switch_if`. The generated CSR block is
intentionally not instantiated. Flattened testbench signals drive the control
fields of `openenoc_switch_if` directly from Cocotb and expose status,
forwarding-table, and arbitration observations.

The wrapper acts as the peer opposite each switch port. For a side-B switch
port it transmits through `a2b_axis_if` and receives through `b2a_axis_if`; those
directions are reversed for a side-A switch port. Constant-index bridges expose
both cases uniformly as `port_rx_axis_if` and `port_tx_axis_if`.

## Datapath Under Test

For every ingress port, the suite exercises the complete crossbar datapath:

1. An asynchronous FIFO adapter moves the frame into the fabric clock domain
   and adapts it to `FABRIC_DATA_W`.
2. The physical ingress index replaces the incoming `tid` value.
3. A dedicated `openenoc_axis_forwarding_engine` extracts the destination and
   source MAC addresses and issues lookup and learning requests.
4. `openenoc_forwarding_table_arb_mux` arbitrates lookup and learning requests
   independently and returns each response to the requesting engine.
5. `openenoc_forwarding_table` returns a programmed route or the default
   forwarding bitmap and learns source MAC addresses in unmanaged mode.
6. Each forwarding engine removes its ingress port from the route and writes
   the resulting egress bitmap into `tuser`.
7. `openenoc_axis_switch` replicates frames to selected outputs. Disjoint routes
   can advance concurrently, and contending routes arbitrate per output.
8. Per-port egress FIFO adapters return frames to the external port clock and
   data width.

Unlike the shared-bus architecture, the crossbar has no global ingress frame
ordering. Ordering is preserved within each ingress stream and at each egress
output.

## Control Interface Model

The wrapper exposes CSR-equivalent controls for:

- managed or unmanaged operation mode,
- pause request and pause-done status,
- default forwarding bitmap,
- forwarding-table CPU address, write data, bit enables, request, and
  acknowledge signals.

Each forwarding-table entry occupies 16 bytes:

| Word | Byte offset | Contents |
|---|---:|---|
| MAC low | 0 | MAC address bits 31:0 |
| MAC high | 4 | MAC address bits 47:32 |
| Interface bitmap | 8 | Egress-port bitmap |
| Configuration | 12 | Entry-enable bit |

Managed-mode tests pause all forwarding engines at frame boundaries before
modifying the forwarding table.

## Configuration

The direct Cocotb run uses parameters exported by `Makefile`:

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

`NUM_OF_INTERFACES` must be between 2 and 32. `TABLE_DEPTH` must be at least
one. `FABRIC_DATA_W` must be a multiple of eight from 8 through 512 bits. Each
external port must use 8-bit byte lanes, and its width must have an integer
ratio with the fabric width.

`PORT_FIFO_DEPTH` is expressed in bytes. It must be an exact multiple of the
wider stream's byte-lane count, and the resulting number of widest-side words
must be a power of two and at least two. Bit `n` of `PORT_SIDE` selects side A
(`0`) or side B (`1`) for port `n`.

## Running Tests

### Option 1: Cocotb (with waveform generation)

Runs Cocotb tests based on the module configuration specified in the Makefile.

```bash
./run_tests.sh waves
# Generates waveforms and opens gtkwave
```

### Option 2: Pytest

Uses the pytest framework to iterate through different configurations and run
the Cocotb tests for each configuration.

```bash
./run_tests.sh pytest
# Uses pytest parameterization to run all configurations
```

## Test Coverage

**Functional checks:**

- End-to-end frame transfer through ingress adaptation, per-port forwarding,
   output switching, and egress adaptation
- Lookup misses using the CSR default-forwarding bitmap
- Managed forwarding-table programming through the CPU request/acknowledge
   interface
- Lookup hits and multicast replication
- Autonomous source-MAC learning in unmanaged mode
- Removal of the ingress interface from the egress bitmap
- Replacement of incoming `tid` with the physical ingress port index
- Preservation of frame data and `tdest`
- Continuous `tvalid` across back-to-back frame boundaries
- Standard 1500-byte and jumbo 9000-byte Ethernet payloads
- Dropping frames with incomplete 1-5 byte destination addresses
- Dropping frames with incomplete 6-11 byte Ethernet headers
- Detection of frames delivered to unexpected egress ports
- Pause request and pause-done sequencing before managed table updates
- Pause requests asserted while one or more frames are active
- CPU readback through the switch CSR bridge
- Independent lookup and learning arbitration
- Concurrent transfers through noncontending crossbar paths
- Per-output arbitration between contending ingress streams
- Multicast over overlapping routes with asymmetric output backpressure
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
- `test_ingress_overwrites_source_tid`: a frame carrying an intentionally
   incorrect source `tid` enters physical port 2; the ingress bridge replaces
   it with 2, forwarding suppresses port 2, and every output copy carries
   `tid = 2`.
- `test_round_robin_between_active_ingresses`: ports 0 and 1 queue two frames
   each while forwarding is paused. After resume, the monitor checks every
   lookup and learning grant against the pending request set and round-robin
   pointer. Independent frame streams are not required to alternate globally.
- `test_zero_bitmap_drops_frame`: an unknown destination with a zero default
   bitmap is consumed without appearing on any egress interface.
- `test_incomplete_destination_address_drops_frame`: frames ending before the
   complete six-byte destination address are dropped even when the default
   forwarding bitmap selects a valid egress.
- `test_incomplete_ethernet_header_drops_frame`: frames with a complete
   destination address but an incomplete source address are dropped even when
   the destination has a valid programmed unicast route.
- `test_header_only_and_unaligned_frames`: Ethernet header-only frames and
   several non-word-aligned lengths verify final-beat `tkeep` handling.
- `test_back_to_back_frame_burst`: twelve consecutive frames of different
   lengths verify boundaries, ordering, sidebands, and sustained operation.
- `test_no_idle_cycle_between_back_to_back_frames`: four queued frames verify
   that the source presents the next frame in the cycle immediately following
   each accepted `tlast`, without a source-created idle cycle.
- `test_standard_and_jumbo_payloads`: frames carrying 1500-byte and 9000-byte
   payloads with EtherType `0x88B5` traverse the switch intact. Their internal
   AXI Stream lengths are 1514 and 9014 bytes because FCS is not present.
- `test_all_ingress_ports_simultaneously`: every ingress FIFO is preloaded with
   three frames. The test verifies all lookup and learning requests, correct
   response routing, concurrent arbitration channels, and delivery to each
   independently configured output.
- `test_unmanaged_mac_moves_to_new_port`: a learned source moves from port 0 to
   port 2, and a subsequent lookup must use the updated location.
- `test_multicast_with_output_backpressure`: eight multicast frames traverse
   two independently stalled outputs without loss, duplication, or reordering.
- `test_managed_table_cpu_readback`: the highest valid table entry is written
   and all four CSR words are read back through the switch interface.
- `test_pause_completes_current_frame_and_blocks_next`: pause is asserted after
   a long frame starts. That frame drains, the next frame remains blocked, and
   forwarding resumes only after pause is released.
- `test_parallel_disjoint_paths`: two long frames use disjoint routes and the
   monitor confirms that more than one fabric transfer occurs in the same
   cycle.
- `test_contending_ingresses`: three ingress streams target one egress under
   backpressure. Per-source frame order and complete delivery are checked while
   the output switch arbitrates the contention.
- `test_concurrent_learning_and_cpu_reads`: three ingress engines learn source
   addresses while software repeatedly reads the forwarding table. All learned
   entries must remain present and usable afterward.
- `test_pause_multiple_active_engines`: two forwarding engines start long
   frames concurrently. Global `pause_done` may assert only after every engine
   reaches a frame boundary, and queued frames remain blocked until resume.
- `test_reset_pending_transactions`: reset is asserted while forwarding-table
   requests are queued. Pending ownership and responses must clear, and a fresh
   post-reset frame must complete normally.
- `test_overlapping_multicast_routes`: two ingress streams use multicast routes
   with one independent output each and one shared output. Independent copies
   proceed concurrently while the common output arbitrates without loss,
   duplication, or per-source reordering.

The passive scoreboard checks request strobes, pending requests, round-robin
selection, active transaction ownership, response routing, learning bitmaps,
physical ingress identity, and concurrent fabric transfers.

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

The pytest runner repeats all 24 directed tests and 12 TestFactory cases for
the following `(NUM_OF_INTERFACES, DATA_W, FABRIC_DATA_W, TABLE_DEPTH,
PORT_FIFO_DEPTH, PORT_SIDE)` tuples:

- `(4, 8, 32, 5, 64, 0b1111)`
- `(5, 24, 48, 8, 48, 0b10101)`
- `(4, 32, 32, 8, 64, 0b0000)`
- `(8, 64, 16, 8, 16, 0b10101010)`

This covers width expansion, equal-width transfer, width contraction,
non-power-of-two external stream widths and table depth, minimum two-word
FIFOs, and all-A, all-B, and mixed port orientations.

Independent port clocks, heterogeneous widths between ports, `TABLE_DEPTH=1`,
and table-full replacement behavior are not yet covered by this suite.
