# SPDX-FileCopyrightText: 2026 Kerim Bavcic
# SPDX-License-Identifier: AGPL-3.0-or-later

import itertools
import logging
import os

import cocotb
import cocotb_test.simulator
import pytest
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge
from cocotb.regression import TestFactory
TestFactory.__test__ = False

from cocotbext.axi import AxiStreamBus, AxiStreamFrame, AxiStreamSource, AxiStreamSink

class TB:
	def __init__(self, dut):
		self.dut = dut

		self.log = logging.getLogger("cocotb.tb")
		self.log.setLevel(logging.DEBUG)

		cocotb.start_soon(Clock(dut.clk, 10, units="ns").start())

		self.source = [AxiStreamSource(AxiStreamBus.from_entity(bus), dut.clk, dut.rst) for bus in dut.s_axis]
		self.sink = [AxiStreamSink(AxiStreamBus.from_entity(bus), dut.clk, dut.rst) for bus in dut.m_axis]

	def set_idle_generator(self, generator=None):
		if generator:
			for source in self.source:
				source.set_pause_generator(generator())

	def set_backpressure_generator(self, generator=None):
		if generator:
			for sink in self.sink:
				sink.set_pause_generator(generator())

	async def reset(self):
		self.dut.rst.setimmediatevalue(0)

		await RisingEdge(self.dut.clk)
		await RisingEdge(self.dut.clk)

		self.dut.rst.value = 1
		await RisingEdge(self.dut.clk)
		await RisingEdge(self.dut.clk)

		self.dut.rst.value = 0
		await RisingEdge(self.dut.clk)
		await RisingEdge(self.dut.clk)


# ----------------------------------------------------------------------
# Helper functions for test parameterization
# ----------------------------------------------------------------------

def make_payload(length):
	return bytearray(itertools.islice(itertools.cycle(range(1, 256)), length))

def encode_unicast_tdest(port, m_dest_w):
	return port << m_dest_w

def cycle_pause():
	return itertools.cycle([1, 1, 1, 0])

def size_list():
	data_width = len(cocotb.top.s_axis[0].tdata)
	byte_width = data_width // 8
	return list(range(1, byte_width * 4 + 1)) + [64] + [1] * 8

def multicast_mask_list():
	ports = len(cocotb.top.m_axis)
	if ports <= 0:
		return []

	all_mask = (1 << ports) - 1
	masks = [1 << 0]

	if ports >= 2:
		masks.append((1 << 0) | (1 << 1))
	if ports >= 3:
		masks.append((1 << 0) | (1 << 2))
	if ports >= 4:
		masks.append((1 << 1) | (1 << 3))

	if all_mask not in masks:
		masks.append(all_mask)

	# Include empty mask once to keep drop coverage in this factory block.
	masks.append(0)

	return list(dict.fromkeys(masks))

# ----------------------------------------------------------------------
# UNICAST test logic
# ----------------------------------------------------------------------

async def run_test_factory_unicast(dut, payload_lengths=None, payload_data=None, idle_inserter=None, backpressure_inserter=None, s=0, m=0):
	tb = TB(dut)
	await tb.reset()

	tb.set_idle_generator(idle_inserter)
	tb.set_backpressure_generator(backpressure_inserter)

	m_dest_w = len(tb.sink[0].bus.tdest)
	test_frames = []

	for idx, test_data in enumerate([payload_data(x) for x in payload_lengths()]):
		test_frame = AxiStreamFrame(test_data)
		test_frame.tid = (idx + 1) & 0xFF
		test_frame.tdest = encode_unicast_tdest(m, m_dest_w)
		test_frame.tuser = 0

		test_frames.append(test_frame)
		await tb.source[s].send(test_frame)

	for test_frame in test_frames:
		rx_frame = await tb.sink[m].recv()

		assert rx_frame.tdata == test_frame.tdata
		assert rx_frame.tid == test_frame.tid
		assert rx_frame.tdest == (test_frame.tdest & ((1 << m_dest_w) - 1))
		assert not rx_frame.tuser

	assert all(snk.empty() for snk in tb.sink)

	await RisingEdge(dut.clk)
	await RisingEdge(dut.clk)


# ----------------------------------------------------------------------
# MULTICAST (without scheduler) test logic
# ----------------------------------------------------------------------

async def run_test_factory_multicast_no_scheduler(dut, payload_lengths=None, payload_data=None, idle_inserter=None, backpressure_inserter=None, s=0, mask=1):
	tb = TB(dut)
	await tb.reset()

	tb.set_idle_generator(idle_inserter)
	tb.set_backpressure_generator(backpressure_inserter)

	target_ports = [p for p in range(len(tb.sink)) if mask & (1 << p)]
	test_frames = []

	for idx, test_data in enumerate([payload_data(x) for x in payload_lengths()]):
		test_frame = AxiStreamFrame(test_data)
		test_frame.tid = ((s & 0x3) << 6) | ((idx + 1) & 0x3F)
		test_frame.tdest = 0
		test_frame.tuser = mask

		test_frames.append(test_frame)
		await tb.source[s].send(test_frame)

	if target_ports:
		for test_frame in test_frames:
			for port in target_ports:
				rx_frame = await tb.sink[port].recv()
				assert rx_frame.tdata == test_frame.tdata
				assert rx_frame.tid == test_frame.tid
				assert rx_frame.tuser == mask
	else:
		for _ in range(12):
			await RisingEdge(dut.clk)

	assert all(snk.empty() for snk in tb.sink)

	await RisingEdge(dut.clk)
	await RisingEdge(dut.clk)


# ----------------------------------------------------------------------
# MULTICAST (with scheduler) test logic
# ----------------------------------------------------------------------

async def run_test_factory_multicast_scheduler(dut, payload_lengths=None, payload_data=None, idle_inserter=None, backpressure_inserter=None):
	tb = TB(dut)
	await tb.reset()

	tb.set_idle_generator(idle_inserter)
	tb.set_backpressure_generator(backpressure_inserter)

	# Hardcoded contention scenario (same intent as manual test):
	# source 0 -> outputs {0,1}, source 1 -> {1,2}, source 2 -> {2,3}
	if len(tb.source) < 3 or len(tb.sink) < 4:
		return

	plan = {
		0: (1 << 0) | (1 << 1),
		1: (1 << 1) | (1 << 2),
		2: (1 << 2) | (1 << 3),
	}

	expected_tids = {p: [] for p in range(len(tb.sink))}
	tid_to_data = {}

	for src, mask in plan.items():
		for idx, test_data in enumerate([payload_data(x) for x in payload_lengths()]):
			test_frame = AxiStreamFrame(test_data)
			test_frame.tid = ((src & 0xF) << 4) | ((idx + 1) & 0xF)
			test_frame.tdest = 0
			test_frame.tuser = mask

			tid_to_data[test_frame.tid] = bytes(test_frame.tdata)
			for port in range(len(tb.sink)):
				if mask & (1 << port):
					expected_tids[port].append(test_frame.tid)

			await tb.source[src].send(test_frame)

	for port in range(len(tb.sink)):
		remaining = list(expected_tids[port])
		for _ in range(len(remaining)):
			rx_frame = await tb.sink[port].recv()
			assert rx_frame.tid in remaining
			assert bytes(rx_frame.tdata) == tid_to_data[rx_frame.tid]
			remaining.remove(rx_frame.tid)
		assert not remaining

	assert all(snk.empty() for snk in tb.sink)

	await RisingEdge(dut.clk)
	await RisingEdge(dut.clk)


# ----------------------------------------------------------------------
# Dispatch: select and generate TestFactory cases
# ----------------------------------------------------------------------

if getattr(cocotb, 'top', None) is not None:
	s_count = len(cocotb.top.s_axis)
	m_count = len(cocotb.top.m_axis)

	if os.environ.get('PARAM_TUSER_BITMAP_ROUTE', '0') == '1':
		factory = TestFactory(run_test_factory_multicast_no_scheduler)
		factory.add_option("payload_lengths", [size_list])
		factory.add_option("payload_data", [make_payload])
		factory.add_option("idle_inserter", [None])
		factory.add_option("backpressure_inserter", [None])
		factory.add_option("s", range(min(s_count, 2)))
		factory.add_option("mask", multicast_mask_list())
		factory.generate_tests()

		factory = TestFactory(run_test_factory_multicast_scheduler)
		factory.add_option("payload_lengths", [size_list])
		factory.add_option("payload_data", [make_payload])
		factory.add_option("idle_inserter", [None, cycle_pause])
		factory.add_option("backpressure_inserter", [None, cycle_pause])
		factory.generate_tests()
	else:
		factory = TestFactory(run_test_factory_unicast)
		factory.add_option("payload_lengths", [size_list])
		factory.add_option("payload_data", [make_payload])
		factory.add_option("idle_inserter", [None, cycle_pause])
		factory.add_option("backpressure_inserter", [None, cycle_pause])
		factory.add_option("s", range(min(s_count, 2)))
		factory.add_option("m", range(min(m_count, 2)))
		factory.generate_tests()

# ----------------------------------------------------------------------
# PyTest framework: test parameterization and test runner
# ----------------------------------------------------------------------

tests_dir = os.path.dirname(__file__)
repo_dir = os.path.abspath(os.path.join(tests_dir, '..', '..', '..'))
hw_dir = os.path.join(repo_dir, 'hw')
libs_dir = os.path.join(repo_dir, 'libs')
core_dir = os.path.join(hw_dir, 'rtl', 'core')
taxi_axis_dir = os.path.join(libs_dir, 'taxi', 'src', 'axis', 'rtl')
common_dir = os.path.abspath(os.path.join(tests_dir, '..', '..', 'common'))

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


@pytest.mark.parametrize("data_w", [8, 16])
@pytest.mark.parametrize("m_count", [2, 4])
@pytest.mark.parametrize("s_count", [2, 4])
@pytest.mark.parametrize("tuser_bitmap_route", [0, 1])
def test_openenoc_axis_switch(request, s_count, m_count, data_w, tuser_bitmap_route):
	dut = "openenoc_axis_switch"
	module = os.path.splitext(os.path.basename(__file__))[0]
	toplevel = module

	verilog_sources = [
		os.path.join(tests_dir, f"{toplevel}.sv"),
		os.path.join(core_dir, f"{dut}.sv"),
		os.path.join(taxi_axis_dir, "taxi_axis_if.sv"),
		os.path.join(taxi_axis_dir, "taxi_axis_register.sv"),
	]

	verilog_sources = process_f_files(verilog_sources)

	parameters = {}
	parameters['S_COUNT'] = s_count
	parameters['M_COUNT'] = m_count
	parameters['DATA_W'] = data_w
	parameters['KEEP_EN'] = int(parameters['DATA_W'] > 8)
	parameters['KEEP_W'] = (parameters['DATA_W'] + 7) // 8
	parameters['STRB_EN'] = 0
	parameters['LAST_EN'] = 1
	parameters['ID_EN'] = 1
	parameters['M_ID_W'] = 8
	parameters['S_ID_W'] = parameters['M_ID_W'] + (s_count-1).bit_length()
	parameters['DEST_EN'] = 1
	parameters['M_DEST_W'] = 8
	parameters['S_DEST_W'] = parameters['M_DEST_W'] + (m_count-1).bit_length()
	parameters['USER_EN'] = 1
	parameters['USER_W'] = m_count
	parameters['TUSER_BITMAP_ROUTE'] = tuser_bitmap_route
	parameters['S_REG_TYPE'] = 2
	parameters['M_REG_TYPE'] = 0

	extra_env = {f'PARAM_{k}': str(v) for k, v in parameters.items()}

	sim_build = os.path.join(tests_dir, "sim_build",
		request.node.name.replace('[', '-').replace(']', ''))

	cocotb_test.simulator.run(
		simulator="verilator",
		python_search=[tests_dir],
		verilog_sources=verilog_sources,
		toplevel=toplevel,
		module=module,
		parameters=parameters,
		extra_args=[
			os.path.join(common_dir, "config.vlt"),
		],
		sim_build=sim_build,
		extra_env=extra_env,
	)
