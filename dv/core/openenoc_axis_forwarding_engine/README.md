<!--
SPDX-FileCopyrightText: 2026 Kerim Bavcic
SPDX-License-Identifier: CC-BY-SA-4.0
-->

# openenoc_axis_forwarding_engine testbench

Standalone verification of the openENOC forwarding engine. The forwarding
table is not instantiated, its lookup and learning interfaces are driven by a
behavioural model inside the Python testbench, so that the engine can be
checked on its own.

## Device under test

The engine parses the MAC header of every incoming frame, starts a lookup as
soon as the destination address is complete, stops the frame with backpressure
until the table answers, and attaches the resulting egress interface bitmap to
`m_axis.tuser`. The source address is used for learning, which never stops the
frame. The ingress interface index is carried on `s_axis.tid` and is always
removed from the egress bitmap.

## Table model

The testbench implements the openENOC request/acknowledge handshake:

* the request payload is taken on the rising edge of `*_req`
* the answer is a single cycle `*_ack` after a configurable latency
* the next request may only start after `*_req` has been low again

`TB.mac_table` holds the known addresses, everything else answers with
`TB.default_forwarding`. Every accepted lookup and learning request is recorded
in `TB.lookups` and `TB.learns` for checking.

## Tests

| test | checks |
| --- | --- |
| `run_test` | frame integrity, `tid`/`tdest` pass through, `tuser` bitmap aligned with the first output beat, lookup and learning order, with and without idle and backpressure |
| `run_test_short_frames` | frames ending inside the MAC header, no lookup below 6 bytes (empty bitmap), no learning below 12 bytes |
| `run_test_no_learning` | group and all zero source addresses and managed mode do not trigger learning |
| `run_test_pause` | `pause_request` stops the engine on a frame boundary and `pause_done` reports a drained engine |

## Running

```bash
# single configuration, parameters taken from the Makefile
make

# full parameter sweep, all supported TDATA widths and interface counts
./run_tests.sh pytest

# waveforms
./run_tests.sh waves

# clean up
./run_tests.sh clean
```
