# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: AGPL-3.0-or-later

import logging
import os
import struct

import cocotb_test.simulator
import pytest

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge
from cocotb.regression import TestFactory
from cocotb.handle import Immediate

from cocotbext.axi import AxiStreamBus, AxiStreamFrame, AxiStreamSource, AxiStreamSink

class TB(object):
    def __init__(self, dut):
        self.dut = dut

        self.log = logging.getLogger("cocotb.tb")
        self.log.setLevel(logging.DEBUG)

        cocotb.start_soon(Clock(dut.clk, 10000, unit="ps").start())

    async def reset(self):
        self.dut.rst.value = Immediate(1)
        await RisingEdge(self.dut.clk)
        await RisingEdge(self.dut.clk)
        await RisingEdge(self.dut.clk)
        await RisingEdge(self.dut.clk)
        self.dut.rst.value = 0

def read_pcap_packets(filename):
    assert os.path.isfile(filename), f"PCAP file does not exist: {filename}"

    with open(filename, "rb") as f:
        data = f.read()

    assert len(data) >= 24, f"Invalid PCAP file, too short: {filename}"

    magic = data[0:4]

    if magic in (b"\xd4\xc3\xb2\xa1", b"\x4d\x3c\xb2\xa1"):
        endian = "<"
    elif magic in (b"\xa1\xb2\xc3\xd4", b"\xa1\xb2\x3c\x4d"):
        endian = ">"
    else:
        raise AssertionError(f"Unsupported PCAP magic in {filename}: {magic.hex()}")

    global_header = data[0:24]
    packet_header_fmt = endian + "IIII"

    packets = []
    offset = 24
    packet_index = 0

    while offset < len(data):
        assert offset + 16 <= len(data), (
            f"Truncated packet header in {filename}, packet {packet_index}"
        )

        ts_sec, ts_frac, incl_len, orig_len = struct.unpack_from(
            packet_header_fmt,
            data,
            offset,
        )

        offset += 16

        assert offset + incl_len <= len(data), (
            f"Truncated packet payload in {filename}, packet {packet_index}"
        )

        payload = data[offset:offset + incl_len]
        offset += incl_len

        packets.append({
            "incl_len": incl_len,
            "orig_len": orig_len,
            "payload": payload,
        })

        packet_index += 1

    return global_header, packets


def compare_pcap_payloads(ref_path, out_path):
    ref_global_header, ref_packets = read_pcap_packets(ref_path)
    out_global_header, out_packets = read_pcap_packets(out_path)

    assert ref_global_header == out_global_header, (
        f"PCAP global header mismatch:\n"
        f"  input:  {ref_path}\n"
        f"  output: {out_path}"
    )

    assert len(ref_packets) == len(out_packets), (
        f"PCAP packet count mismatch:\n"
        f"  input:  {ref_path} ({len(ref_packets)} packets)\n"
        f"  output: {out_path} ({len(out_packets)} packets)"
    )

    for i, (ref_packet, out_packet) in enumerate(zip(ref_packets, out_packets)):
        assert ref_packet["incl_len"] == out_packet["incl_len"], (
            f"PCAP packet {i} captured length mismatch:\n"
            f"  input:  {ref_packet['incl_len']} bytes\n"
            f"  output: {out_packet['incl_len']} bytes"
        )

        assert ref_packet["orig_len"] == out_packet["orig_len"], (
            f"PCAP packet {i} original length mismatch:\n"
            f"  input:  {ref_packet['orig_len']} bytes\n"
            f"  output: {out_packet['orig_len']} bytes"
        )

        assert ref_packet["payload"] == out_packet["payload"], (
            f"PCAP packet {i} payload mismatch:\n"
            f"  input:  {ref_path}\n"
            f"  output: {out_path}"
        )

@cocotb.test()
async def test(dut):
    tb = TB(dut)

    await tb.reset()

    await RisingEdge(dut.pcapfinished)

    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)

    pcap_in_filename = os.environ["PARAM_PCAP_IN_FILENAME"].replace('\\"', '')
    pcap_out_filename = os.environ["PARAM_PCAP_OUT_FILENAME"].replace('\\"', '')

    compare_pcap_payloads(pcap_in_filename, pcap_out_filename)

# ----------------------------------------------------------------------
# PyTest framework: test parameterization and test runner
# ----------------------------------------------------------------------

tests_dir = os.path.dirname(__file__)
hw_dir = os.path.abspath(os.path.join(tests_dir, '..', '..', 'hw'))
core_dir = os.path.join(hw_dir, 'src', 'core')
taxi_axis_dir = os.path.join(hw_dir, 'libs', 'taxi', 'src', 'axis', 'rtl')

def process_f_files(files):
    lst = {}
    for f in files:
        if f[-2:].lower() == '.f':
            with open(f, 'r') as fp:
                l = fp.read().split()
            for f in process_f_files([os.path.join(os.path.dirname(f), x) for x in l]):
                lst[os.path.basename(f)] = f
        else:
            lst[os.path.basename(f)] = f
    return list(lst.values())

@pytest.mark.parametrize("data_width", [8, 16, 32, 64, 128, 256, 512])
@pytest.mark.parametrize("pcap_in_filename", ["test1.pcap", "test2.pcap"])
def test_traffic(request, data_width, pcap_in_filename):
    module = os.path.splitext(os.path.basename(__file__))[0]
    toplevel = module

    verilog_sources = [
        os.path.join(tests_dir, f"{toplevel}.sv"),
        os.path.join(tests_dir, "pcapreader.sv"),
        os.path.join(tests_dir, "pcapwriter.sv"),
        os.path.join(tests_dir, "avalon_if.sv"),
        os.path.join(taxi_axis_dir, "taxi_axis_if.sv"),
    ]

    verilog_sources = process_f_files(verilog_sources)

    sim_build = os.path.join(
        tests_dir,
        "sim_build",
        request.node.name.replace("[", "-").replace("]", "")
    )

    pcap_in_path = os.path.abspath(os.path.join(tests_dir, pcap_in_filename))
    pcap_out_path = os.path.abspath(os.path.join(sim_build, "output.pcap"))

    parameters = {
        "DATA_WIDTH": data_width,
        "CLOCK_PERIOD": 10000,
        "PCAP_IN_FILENAME": f'"{pcap_in_path}"',
        "PCAP_OUT_FILENAME": f'"{pcap_out_path}"',
    }

    extra_env = {
        f"PARAM_{k}": str(v).strip('"')
        for k, v in parameters.items()
    }

    cocotb_test.simulator.run(
        simulator="verilator",
        python_search=[tests_dir],
        verilog_sources=verilog_sources,
        toplevel=toplevel,
        module=module,
        parameters=parameters,
        sim_build=sim_build,
        extra_env=extra_env,
    )
