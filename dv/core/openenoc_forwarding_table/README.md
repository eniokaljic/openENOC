<!-- SPDX-FileCopyrightText: 2026 Kerim Bavcic -->
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# openENOC Forwarding Table Test Suite

## Overview

This test suite validates the `openenoc_forwarding_table` module, the CAM + RAM
forwarding table of the openENOC Switch. The destination MAC address is stored
in the CAM, the destination interface bitmap and the entry enable bit in the
companion RAM.

The module is verified stand-alone, i.e. without the openENOC Switch Interface
CSR and without any AXI4-Stream traffic. All interfaces are driven and sampled
directly.

### Entry layout

Each entry occupies 16 bytes, all words are 32-bit aligned and match the
`forwarding_table.entry[]` register file of the openENOC Switch Interface CSR:

| Offset | Register             | Contents               |
| ------ | -------------------- | ---------------------- |
| `+0x0` | `mac_address.lo_word`| MAC address `[31:0]`   |
| `+0x4` | `mac_address.hi_word`| MAC address `[47:32]`  |
| `+0x8` | `iface.bitmap`       | destination interfaces |
| `+0xC` | `config.enabled`     | entry valid            |

### Modes of operation

| `operation_mode` | Mode      | Behaviour                                                             |
| ---------------- | --------- | --------------------------------------------------------------------- |
| `1`              | managed   | software owns the table, learning requests are acknowledged and ignored |
| `0`              | unmanaged | the table learns autonomously, software writes are acknowledged and ignored (reads are allowed) |

### Interfaces

All three interfaces share the same req/ack handshake, modelled after the
[PeakRDL internal cpuif protocol](https://peakrdl-regblock.readthedocs.io/en/latest/cpuif/internal_protocol.html):
the master asserts `*_req` for a single clock cycle, the request payload only
has to be valid during that cycle, the table takes a snapshot of the request
and answers with a single cycle `*_ack` once it has been processed. The master
issues the next request only after it received the acknowledge.

The snapshot is taken on the rising edge of `*_req`, so a master that keeps its
request asserted until the acknowledge is served as well, and served exactly
once.

- **CPU interface** (`cpuif_*`): 32-bit interface of the external `forwarding_table`
  regfile of the openENOC Switch Interface CSR
  (`hwif_out.forwarding_table.*` / `hwif_in.forwarding_table.*`).
- **Lookup interface**: the result is presented on `lookup_if.port_bitmap`
  together with `lookup_if.ack`. A miss returns `default_forwarding`
  (`hwif_out.default_forwarding.bitmap.value`).
- **Learning interface**: a known MAC address only refreshes its port bitmap,
  a new MAC address is written at the circular write pointer, replacing the
  oldest entry.

The table is a single shared resource, only one master is served at a time.
The CPU interface has the highest priority, followed by lookup and learning.
Because every request is captured, a request issued while the table is busy is
served later instead of being lost.

## Configuration

Edit `Makefile` to configure parameters.

```Makefile
export PARAM_NUM_OF_INTERFACES := 8
export PARAM_TABLE_DEPTH := 32
```

`ADDR_WIDTH` is derived from `TABLE_DEPTH` (`$clog2(TABLE_DEPTH * 16)`) and is
not configurable.

## Running Tests

### Option 1: Pytest

Uses `pytest` + `cocotb_test` to sweep multiple configurations (`NUM_OF_INTERFACES`, `TABLE_DEPTH`).

```bash
./run_tests.sh pytest
```

### Option 2: Waveforms
Builds and runs simulation with waveform dumping enabled.

```bash
./run_tests.sh waves
```

## Test Cases

| Test                                     | Description                                                                 |
| ---------------------------------------- | --------------------------------------------------------------------------- |
| `run_reset_state`                        | table cleared after reset, lookup returns `default_forwarding`               |
| `run_cpu_program_and_readback`           | software programs every entry and reads it back                              |
| `run_cpu_write_bit_enables`              | `cpuif_wr_biten` masking of partial writes                                   |
| `run_iface_bit_enables`                  | `cpuif_wr_biten` masking of the interface bitmap word                        |
| `run_lookup_managed`                     | lookup hit, miss, disabled entry and `default_forwarding` handling           |
| `run_duplicate_mac_lowest_index_wins`    | the same MAC address in two entries, the lowest index wins                   |
| `run_blackhole_entry`                    | a hit with an empty bitmap drops instead of falling back to flooding         |
| `run_learning_ignored_in_managed_mode`   | learning is acknowledged but leaves the table untouched                      |
| `run_learn_pointer_unaffected_by_managed_mode` | the circular write pointer does not move while in managed mode         |
| `run_learning_unmanaged`                 | learning, bitmap refresh of a known MAC address and circular replacement     |
| `run_cpu_write_ignored_in_unmanaged_mode`| software writes are acknowledged but ignored, reads still work               |
| `run_cpu_address_out_of_range`           | an address without an entry behind it is acknowledged, reads as zero and writes nowhere |
| `run_exclusive_access`                   | overlapping CPU and lookup accesses are serialized                           |
| `run_concurrent_requests`                | requests issued on all interfaces in the same cycle are captured, all served and prioritized |
| `run_held_request`                       | a request held past the acknowledge results in exactly one transaction       |
| `run_back_to_back_requests`              | a new request in the cycle right after the acknowledge, without idle cycles  |
