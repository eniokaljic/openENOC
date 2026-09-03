<!-- SPDX-FileCopyrightText: 2026 Enio Kaljic -->
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# openENOC Traffic-Based Test Suite

## Overview

This test suite validates the PCAP-based traffic replay and capture infrastructure used in openENOC verification.

The test connects a `pcapreader` instance directly to a `pcapwriter` instance through an AXI4-Stream interface. Packets are read from an input PCAP file, transferred through the streaming interface, written to an output PCAP file, and then compared against the original input. This verifies that the traffic source, traffic sink, packet formatting, frame boundaries, and AXI4-Stream data-width handling preserve packet contents correctly.

Although both Avalon-ST and AXI4-Stream interfaces are available in the PCAP reader and writer modules, this test configuration uses the AXI4-Stream path.

## Test Structure

The verification environment consists of:

* `test_traffic.sv` - SystemVerilog wrapper that connects the PCAP reader and writer through AXI4-Stream
* `test_traffic.py` - cocotb testbench, PCAP comparison logic, and pytest runner
* `run_tests.sh` - common test runner used to launch the pytest regression or waveform simulation
* `Makefile` - low-level cocotb simulation entry point used by the script
* `pcapreader.sv` - PCAP replay module that converts packets into Avalon-ST or AXI4-Stream traffic
* `pcapwriter.sv` - PCAP capture module that writes Avalon-ST or AXI4-Stream traffic into a PCAP file
* `avalon_if.sv` - Avalon-ST interface definition used by the generic PCAP reader/writer infrastructure
* `taxi_axis_if.sv` - AXI4-Stream interface definition used by this test configuration
* `test1.pcap` - input PCAP file used by the regression
* `test2.pcap` - input PCAP file used by the regression
* `output.pcap` - generated output file when running a single simulation configuration

## Testbench Architecture

The SystemVerilog wrapper instantiates one `pcapreader` and one `pcapwriter`. Both modules are configured with the same `DATA_WIDTH` and `CLOCK_PERIOD` parameters.

```systemverilog
pcapreader #(
    .PCAP_FILENAME(PCAP_IN_FILENAME),
    .SIGNAL_TYPE("axisif"),
    .DATA_WIDTH(DATA_WIDTH),
    .CLOCK_PERIOD(CLOCK_PERIOD)
) u_pcapreader (...);

pcapwriter #(
    .PCAP_FILENAME(PCAP_OUT_FILENAME),
    .SIGNAL_TYPE("axisif"),
    .DATA_WIDTH(DATA_WIDTH),
    .CLOCK_PERIOD(CLOCK_PERIOD)
) u_pcapwriter (...);
```

The reader drives the shared AXI4-Stream interface, while the writer consumes the same stream and reconstructs the packets into a PCAP file. The `pcapfinished` signal is asserted once the reader reaches the end of the input file.

## Test Configuration

The main configuration parameters are:

```Makefile
export PARAM_DATA_WIDTH := 8
export PARAM_CLOCK_PERIOD := 10000
export PARAM_PCAP_IN_FILENAME := \"test1.pcap\"
export PARAM_PCAP_OUT_FILENAME := \"output.pcap\"
```

`DATA_WIDTH` selects the AXI4-Stream data width in bits. The regression covers the following widths:

```python
[8, 16, 32, 64, 128, 256, 512]
```

`CLOCK_PERIOD` is specified in picoseconds and is used by both the PCAP reader and writer to model packet timing.

`PCAP_IN_FILENAME` selects the input traffic capture, while `PCAP_OUT_FILENAME` selects the generated output capture.

## Running Tests

The test is normally executed through the common `run_tests.sh` wrapper used by the openENOC verification tests. The script selects the intended flow and keeps the command line consistent with the rest of the repository.

### Option 1: Pytest

Uses `pytest` + `cocotb_test` to sweep the configured AXI4-Stream data widths and input PCAP files.

```bash
./run_tests.sh pytest
```

### Option 2: Waves

Builds and runs a single simulation configuration with waveform dumping enabled.

```bash
./run_tests.sh waves
```

The waveform flow is intended for debugging one selected configuration, while the pytest flow is intended for the full parameterized regression.

## Pytest Configuration

The pytest configuration runs the test for two input PCAP files and seven AXI4-Stream data widths:

```python
@pytest.mark.parametrize("data_width", [8, 16, 32, 64, 128, 256, 512])
@pytest.mark.parametrize("pcap_in_filename", ["test1.pcap", "test2.pcap"])
```

This produces 14 regression configurations in total.

Each pytest case writes its output PCAP file into a separate `sim_build` subdirectory derived from the pytest case name. This avoids collisions between parallel or repeated test runs.

## Test Flow

Each test performs the following sequence:

1. Start the simulation clock.
2. Apply reset for four clock cycles.
3. Wait until the PCAP reader asserts `pcapfinished`.
4. Wait two additional clock cycles to allow the writer to flush the final packet.
5. Compare the generated output PCAP file against the input PCAP file.

The comparison checks:

* PCAP global header
* Packet count
* Captured packet length
* Original packet length
* Packet payload bytes

A mismatch in any of these fields fails the test and reports the input and output files involved.

## Test Coverage

The test suite covers the following scenarios:

### PCAP Replay

Verifies that packets can be read from a PCAP file and converted into AXI4-Stream transfers.

Coverage includes:

* PCAP global header parsing
* Packet header parsing
* Timestamp-based packet scheduling
* AXI4-Stream `tdata`, `tkeep`, `tvalid`, `tready`, and `tlast` generation
* Multiple AXI4-Stream data widths

### PCAP Capture

Verifies that AXI4-Stream transfers can be reconstructed into a valid PCAP output file.

Coverage includes:

* Packet boundary detection using `tlast`
* Packet size calculation using `tkeep`
* PCAP packet header generation
* Payload reconstruction
* Output file flushing after each packet

### End-to-End Payload Preservation

Verifies that packets replayed by `pcapreader` and captured by `pcapwriter` remain unchanged at the PCAP payload level.

Coverage includes:

* Single-packet input captures
* Multi-packet input captures
* Short Ethernet frames
* Frames that span multiple AXI4-Stream beats on narrow data widths
* Frames that fit into fewer AXI4-Stream beats on wide data widths

### Data-Width Sweep

Verifies that the same PCAP traffic is preserved across AXI4-Stream data widths from 8 bits to 512 bits.

This checks that byte ordering, `tkeep` generation, and packet termination remain correct across narrow and wide streaming datapaths.

## Input PCAP Files

The regression uses two input PCAP files:

* `test1.pcap` - simple single-packet capture
* `test2.pcap` - multi-packet capture with different packet lengths

These files are used as reference captures. The generated output PCAP is compared against the selected reference file after each simulation run.

## Notes

The test is primarily intended to validate the reusable PCAP traffic infrastructure used by other openENOC verification environments. It does not insert a packet-processing DUT between the reader and writer.

The PCAP reader and writer modules support both Avalon-ST and AXI4-Stream signaling, but the current test wrapper selects `SIGNAL_TYPE("axisif")`.

For very narrow data widths, larger packets require more simulation cycles because fewer bytes are transferred per AXI4-Stream beat. For very wide data widths, the test mainly stresses byte ordering, `tkeep` handling, and correct packet termination.
