<!-- SPDX-FileCopyrightText: 2026 Enio Kaljic -->
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# openENOC Full Endpoint Test Suite

## Overview

This cocotb suite verifies the `openenoc_endpoint_full` SoC wrapper by booting
`endpoint_test` PicoRV32 firmware and looping Ethernet TX back to RX. It tests
continuous transport, periodic backpressure and assertion diagnostics after
injected payload corruption.
All cases use fixed 32-bit AXI, AXI4-Lite, and Ethernet data paths.
Firmware checks are described in the
[endpoint_test README](../../../sw/apps/endpoint_test/README.md).

The DV Makefile builds `endpoint_test` for `openenoc_endpoint_full` with `DEBUG=1`
before simulation. Pytest invokes the same `firmware` target once per session.
The software build's default `DEBUG=0` therefore does not disable DV assertions;
a firmware build failure stops the tests before simulation.

The testbench loads `build/sw/openenoc_endpoint_full/imem.mem`.

The endpoint contains a 4-by-3 pipelined `openenoc_axil_crossbar`. System
initiators are ordered as PicoRV32, DMA, the reserved debug/program master,
and local RMEM access from the oETP path. Targets are ordered as DMEM, IMEM,
and CSR. DMA and RMEM access the local memories during the test; the debug
initiator is tied inactive. All initiators have read/write connectivity to
all three targets.

The generated CSR `hwif` is internal to the endpoint. An
`openenoc_endpoint_if` instance connects the generated CSR bridge to
`openenoc_endpoint_interface`, while the module exposes the bridge's
`openenoc_switch_if` side. The testbench drives `pause_done` through that
switch interface and observes its propagation into the CSR `hwif`.

The endpoint interface connects direct CSR AXI4-Stream transfers and DMA
traffic to the Ethernet-like link through buffered stream paths and the oETP
engine. Four synchronous `taxi_axis_fifo_adapter` instances buffer the direct
and DMA transmit/receive paths. The testbench loops the transmit direction
back into the receive direction, with optional backpressure or payload
corruption.

The crossbar arrays use individually named internal Taxi interfaces:
`cpu_axil_if`, `endpoint_axil_if`, `debug_axil_if`, `dmem_axil_if`,
`imem_axil_if`, and `csr_axil_if`. DMA reaches `endpoint_axil_if` through a
`taxi_axi_axil_adapter`; local RMEM reaches the fourth initiator through
`rmem_cpuif` and `openenoc_cpuif_axil_adapter`.

The CPU initiator uses the `openenoc_picorv32` drop-in wrapper around the
original PicoRV32 core and the project AXI4-Lite adapter. This suite also
serves as the integration acceptance test for the CPU wrapper and adapter
together, including firmware execution and interrupt entry/return.

Generated simulation artifacts use
`build/dv/endpoints/openenoc_endpoint_full/sim_build/` for Make and
`sim_build/pytest/<case>/` under the same component directory for pytest.
Results and FST waveforms stay with each simulation build. Python bytecode and
temporary files also stay under the component's build directory; see the
[shared output layout](../../README.md#generated-artifacts).

## Address Map

The default full-endpoint configuration uses:

| Target | Base address | Decode aperture |
| --- | ---: | ---: |
| IMEM | `0x0000_0000` | 32 KiB |
| DMEM | `0x1000_0000` | 32 KiB |
| CSR | `0x2000_0000` | 8 KiB |

IMEM and DMEM sizes and target bases are derived from
`openenoc_endpoint_full_pkg`. The CSR aperture uses
`OPENENOC_ENDPOINT_FULL_CSR_MIN_ADDR_WIDTH` from the generated CSR package.

## Test Coverage

The firmware exercises configuration and capability checks, peer mapping and
error clearing, direct RMEM self-loopback and timeout, AXIS stream APIs,
raw DMA TX/RX, peer DMA push/pull and timeout, and IRQ handling. The default full
endpoint completes all seven coverage groups.

The cocotb checks include:

- booted instruction memory, successful execution without CPU traps, and stable
  final firmware result;
- CPU instruction fetches, data-memory accesses, and CSR HAL calls reaching
  IMEM, DMEM, and CSR through the crossbar;
- all coverage bits set (`0x7f`) and no failing source file or line on success;
- three 66-byte direct AXIS frames using stream APIs: aligned buffers, unaligned
  buffers, and a 65-byte RX buffer with overflow drain, full byte count and canaries;
- a fourth 66-byte raw Ethernet frame transferred through TX/RX DMA, with exact
  payload, byte masks and final TLAST;
- 17 AXI4-Stream transfers per raw frame, with `TKEEP=0xf` on the first
  16 words, `TKEEP=0x3` on the final partial word, and `TLAST` only on that
  final word, in both Ethernet loopback and direct CSR receive traffic;
- 22 oETP frames for transparent RMEM writes/reads, missing-destination timeouts,
  and three-fragment peer push/pull transfers;
- exactly three direct frames on the CSR RX path, excluding the DMA-routed frame;
- active DMA and RMEM memory masters while the reserved debug master stays idle;
- RX notification before the frame's final Ethernet beat and CSR payload reads
  within the IRQ handler;
- 12 acknowledged claims with ordered sequences 0 through 11: three peer-DMA,
  one raw TX, one raw RX, three direct TX, three direct RX and one RMEM error;
- peer indices for timeout, push and pull events, claim-identity matching at
  completion, CPU IRQ entry/return, and no overflow or invalid completion;
- empty IRQ FIFO and reservation state with the output deasserted after success;
- generated switch dimensions on `openenoc_switch_if`, `pause_done` propagation
  into the CSR `hwif`, and endpoint MAC configuration;
- unchanged reset values of unrelated root test/switch registers, including
  `csr.test_reg` remaining zero;
- observed backpressure in the stalled case.

The assertion-failure case flips one payload bit in the first direct AXIS frame.
It checks the exact source filename and line, completed coverage `0x07`, failure
publication before the CPU trap, and stable diagnostics after the trap.

All cases use the same debug firmware. Each run allows up to 500,000 execution
cycles after reset.

## Firmware Report

The testbench exposes the four DMEM words of `_openenoc_assert_status`, defined
through the shared `assert.h`:

| Word | Signal | Firmware field |
| --- | --- | --- |
| 0 | `dmem_status` | `_openenoc_assert_status.status` |
| 1 | `dmem_checks` | `_openenoc_assert_status.completed_checks` |
| 2 | `dmem_failure_line` | `_openenoc_assert_status.failure_line` |
| 3 | `dmem_failure_file` | `_openenoc_assert_status.failure_file` |

Success requires status `0x600d600d`, coverage `0x7f`, failure line zero and a null
filename pointer. Status `0xbad0bad0` reports firmware failure before a CPU trap;
the diagnostic includes its source file, line, completed groups and observed beat
counts. The filename is decoded from the loaded firmware image. Status zero means
execution has not yet published a final result.

## Running Tests

Activate the project virtual environment, change to this directory, and run
all loopback and assertion cases. The suite builds the required debug firmware
automatically:

```bash
./run_tests.sh pytest
```

To build the firmware separately:

```bash
make -C ../../../sw APP=endpoint_test EP=openenoc_endpoint_full DEBUG=1
```

Run the default configuration and generate an FST waveform:

```bash
./run_tests.sh waves
```

Remove generated simulation artifacts:

```bash
./run_tests.sh clean
```
