<!-- SPDX-FileCopyrightText: 2026 Kerim Bavcic -->
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# openENOC Forwarding Table Arbiter Multiplexer Test Suite

## Overview

This suite validates `openenoc_forwarding_table_arb_mux` as a stand-alone
module. The real forwarding table, forwarding engines and Ethernet datapath are
not instantiated. Cocotb drives all lookup and learning masters directly and
models the two forwarding-table slave interfaces with independently variable
response delays.

The module contains two independent round-robin arbiters:

- all per-port lookup interfaces share one downstream lookup interface;
- all per-port learning interfaces share one downstream learning interface.

Every source can have one outstanding request per channel. The arbiter captures
the one-cycle request and its payload, queues simultaneous requests, keeps the
selected owner until the slave acknowledges the transaction, and returns the
response only to that owner. Lookup and learning may be active concurrently.

## Configuration

Edit `Makefile` to configure a direct cocotb run:

```Makefile
export PARAM_NUM_OF_INTERFACES := 4
```

The pytest runner sweeps `NUM_OF_INTERFACES` over 2, 4, 5, 8 and 32 ports. The
five-port configuration checks round-robin pointer wrap for a port count that
is not a power of two.

## Running Tests

### Option 1: Cocotb with waveform generation

```bash
./run_tests.sh waves
```

### Option 2: Pytest parameter sweep

```bash
./run_tests.sh pytest
```

## Test Coverage

The TestFactory matrix combines three arrival patterns, four slave timing
profiles and three channel selections:

| Dimension | Values |
|---|---|
| Request arrival | consecutive source requests, request during an active transaction, all ports simultaneously |
| Slave response delay | minimum, alternating short/long, deterministic random, long |
| Active channels | lookup only, learning only, lookup and learning concurrently |

Additional directed tests cover:

- independent completion timing between lookup and learning;
- new requests arriving on the same edge as a slave acknowledge;
- requests held until acknowledge producing exactly one transaction;
- repeatable randomized arrivals and variable response delays;
- reset while transactions are active and queued.

The scoreboard checks every captured request, payload snapshot, downstream
request strobe, round-robin selection, registered owner, acknowledge target and
lookup bitmap. Inactive payloads are deliberately overwritten after request
capture so that using live source data instead of the saved request is detected.