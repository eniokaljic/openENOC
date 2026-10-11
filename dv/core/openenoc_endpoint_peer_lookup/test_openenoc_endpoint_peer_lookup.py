# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: AGPL-3.0-or-later

import logging
import os

import cocotb
import cocotb_test.simulator
from cocotb.clock import Clock
from cocotb.triggers import FallingEdge, RisingEdge, Timer
from cocotbext.axi import AxiLiteBus, AxiLiteMaster

LOOKUP_BY_INDEX = 0
LOOKUP_BY_RMEM = 1
LOOKUP_BY_MAC = 2


def packed_slice(signal, index, width):
    return (int(signal.value) >> (index * width)) & ((1 << width) - 1)


def pack(values, width):
    result = 0
    mask = (1 << width) - 1
    for index, value in enumerate(values):
        result |= (value & mask) << (index * width)
    return result


class TB:
    def __init__(self, dut):
        from csr.lib import NormalCallbackSet
        from csr.reg_model.csr import csr_cls

        self.dut = dut
        self.log = logging.getLogger("cocotb.tb")
        self.log.setLevel(logging.DEBUG)
        # Use generated register locations even when the surrounding map changes.
        self.csr = csr_cls(callbacks=NormalCallbackSet())

        self.ports = int(os.environ.get("PARAM_LOOKUP_PORTS", 2))
        self.peer_w = len(dut.req_peer_idx) // self.ports
        self.addr_w = len(dut.req_rmem_addr) // self.ports

        self.req_valid = [0] * self.ports
        self.req_type = [0] * self.ports
        self.req_mode_mask = [0] * self.ports
        self.req_peer_idx = [0] * self.ports
        self.req_rmem_addr = [0] * self.ports
        self.req_mac_addr = [0] * self.ports
        self.rsp_ready = [0] * self.ports

        cocotb.start_soon(Clock(dut.clk, 10, unit="ns").start())
        self.axil_master = AxiLiteMaster(AxiLiteBus.from_prefix(dut, "s_axil"), dut.clk, dut.rst)

    def drive_lookup(self):
        self.dut.req_valid.value = pack(self.req_valid, 1)
        self.dut.req_type.value = pack(self.req_type, 2)
        self.dut.req_mode_mask.value = pack(self.req_mode_mask, 4)
        self.dut.req_peer_idx.value = pack(self.req_peer_idx, self.peer_w)
        self.dut.req_rmem_addr.value = pack(self.req_rmem_addr, self.addr_w)
        self.dut.req_mac_addr.value = pack(self.req_mac_addr, 48)
        self.dut.rsp_ready.value = pack(self.rsp_ready, 1)

    async def reset(self):
        self.dut.rst.setimmediatevalue(1)
        self.drive_lookup()

        for _ in range(4):
            await RisingEdge(self.dut.clk)

        self.dut.rst.value = 0
        for _ in range(2):
            await RisingEdge(self.dut.clk)

        await Timer(1, unit="ns")
        assert int(self.dut.req_ready.value) == 0
        assert int(self.dut.rsp_valid.value) == 0

    async def write_word(self, address, value):
        response = await self.axil_master.write(
            address, int(value & 0xFFFFFFFF).to_bytes(4, "little")
        )
        assert int(response.resp) == 0

    async def read_word(self, address):
        response = await self.axil_master.read(address, 4)
        assert int(response.resp) == 0
        return int.from_bytes(response.data, "little")

    async def write_peer(
        self,
        index,
        *,
        mac,
        rmem_offset,
        local_addr,
        remote_addr,
        size,
        mode,
        irq_enable,
    ):
        peer = self.csr.endpoint_interface.peers.entry[index]
        await self.write_word(peer.mac_address.address, mac)
        await self.write_word(peer.mac_address.address + 4, mac >> 32)
        await self.write_word(peer.rmem_address.address, rmem_offset)
        await self.write_word(peer.local_address.address, local_addr)
        await self.write_word(peer.remote_address.address, remote_addr)
        await self.write_word(peer.register_size.address, size)
        await self.write_word(peer.dma.address, mode | (irq_enable << 2))

    async def read_peer(self, index):
        peer = self.csr.endpoint_interface.peers.entry[index]
        mac_lo = await self.read_word(peer.mac_address.address)
        mac_hi = await self.read_word(peer.mac_address.address + 4)
        return {
            "mac_addr": mac_lo | ((mac_hi & 0xFFFF) << 32),
            "rmem_offset": await self.read_word(peer.rmem_address.address),
            "local_addr": await self.read_word(peer.local_address.address),
            "remote_addr": await self.read_word(peer.remote_address.address),
            "size": await self.read_word(peer.register_size.address),
            "dma": await self.read_word(peer.dma.address),
        }

    def set_request(
        self,
        port,
        lookup_type,
        mode_mask,
        *,
        peer_idx=0,
        rmem_addr=0,
        mac_addr=0,
    ):
        self.req_type[port] = lookup_type
        self.req_mode_mask[port] = mode_mask
        self.req_peer_idx[port] = peer_idx
        self.req_rmem_addr[port] = rmem_addr
        self.req_mac_addr[port] = mac_addr
        self.req_valid[port] = 1
        self.drive_lookup()

    def response(self, port):
        return {
            "hit": packed_slice(self.dut.rsp_hit, port, 1),
            "peer_idx": packed_slice(self.dut.rsp_peer_idx, port, self.peer_w),
            "mac_addr": packed_slice(self.dut.rsp_mac_addr, port, 48),
            "rmem_offset": packed_slice(self.dut.rsp_rmem_offset, port, self.addr_w),
            "local_addr": packed_slice(self.dut.rsp_local_addr, port, self.addr_w),
            "remote_addr": packed_slice(self.dut.rsp_remote_addr, port, self.addr_w),
            "size": packed_slice(self.dut.rsp_size, port, self.addr_w),
            "dma_mode": packed_slice(self.dut.rsp_dma_mode, port, 2),
            "irq_enable": packed_slice(self.dut.rsp_irq_enable, port, 1),
        }

    async def accept_request(
        self,
        port,
        lookup_type,
        mode_mask,
        *,
        peer_idx=0,
        rmem_addr=0,
        mac_addr=0,
    ):
        self.set_request(
            port,
            lookup_type,
            mode_mask,
            peer_idx=peer_idx,
            rmem_addr=rmem_addr,
            mac_addr=mac_addr,
        )

        for _ in range(20):
            await FallingEdge(self.dut.clk)
            await Timer(1, unit="ns")
            if packed_slice(self.dut.req_ready, port, 1):
                break
        else:
            raise AssertionError(f"lookup request on port {port} was not accepted")

        assert (
            int(self.dut.rsp_valid.value) == 0
        ), "response was asserted combinationally in the request cycle"

        await RisingEdge(self.dut.clk)
        await Timer(1, unit="ns")
        self.req_valid[port] = 0
        self.drive_lookup()

        assert int(self.dut.rsp_valid.value) == 1 << port
        return self.response(port)

    async def consume_response(self, port, stall_cycles=0):
        expected = self.response(port)

        for _ in range(stall_cycles):
            assert int(self.dut.rsp_valid.value) == 1 << port
            assert self.response(port) == expected
            await RisingEdge(self.dut.clk)
            await Timer(1, unit="ns")

        self.rsp_ready[port] = 1
        self.drive_lookup()
        await RisingEdge(self.dut.clk)
        await Timer(1, unit="ns")
        self.rsp_ready[port] = 0
        self.drive_lookup()

        assert int(self.dut.rsp_valid.value) == 0

    async def lookup(self, port, lookup_type, mode_mask, **keys):
        response = await self.accept_request(port, lookup_type, mode_mask, **keys)
        await self.consume_response(port)
        return response


PEERS = [
    {
        "mac": 0x001122334455,
        "rmem_offset": 0x00000000,
        "local_addr": 0x10000000,
        "remote_addr": 0x20000000,
        "size": 0xFFFFFFFF,
        "mode": 0,
        "irq_enable": 1,
    },
    {
        "mac": 0x102030405060,
        "rmem_offset": 0x00001000,
        "local_addr": 0x11000000,
        "remote_addr": 0x21000000,
        "size": 0x00000100,
        "mode": 1,
        "irq_enable": 1,
    },
    {
        "mac": 0x102030405060,
        "rmem_offset": 0x00001080,
        "local_addr": 0x12000000,
        "remote_addr": 0x22000000,
        "size": 0x00000100,
        "mode": 1,
        "irq_enable": 0,
    },
    {
        "mac": 0xAABBCCDDEEFF,
        "rmem_offset": 0x00003000,
        "local_addr": 0x13000000,
        "remote_addr": 0x23000000,
        "size": 0x00000080,
        "mode": 3,
        "irq_enable": 1,
    },
]


async def configure_peers(tb):
    for index, peer in enumerate(PEERS):
        await tb.write_peer(index, **peer)


def expected_response(index, peer):
    return {
        "hit": 1,
        "peer_idx": index,
        "mac_addr": peer["mac"],
        "rmem_offset": peer["rmem_offset"],
        "local_addr": peer["local_addr"],
        "remote_addr": peer["remote_addr"],
        "size": peer["size"],
        "dma_mode": peer["mode"],
        "irq_enable": peer["irq_enable"],
    }


MISS = {
    "hit": 0,
    "peer_idx": 0,
    "mac_addr": 0,
    "rmem_offset": 0,
    "local_addr": 0,
    "remote_addr": 0,
    "size": 0,
    "dma_mode": 0,
    "irq_enable": 0,
}


@cocotb.test()
async def test_lookup_modes_priority_and_boundaries(dut):
    tb = TB(dut)
    await tb.reset()
    await configure_peers(tb)

    peer1_csr = await tb.read_peer(1)
    assert peer1_csr == {
        "mac_addr": PEERS[1]["mac"],
        "rmem_offset": PEERS[1]["rmem_offset"],
        "local_addr": PEERS[1]["local_addr"],
        "remote_addr": PEERS[1]["remote_addr"],
        "size": PEERS[1]["size"],
        "dma": PEERS[1]["mode"] | (PEERS[1]["irq_enable"] << 2),
    }

    assert await tb.lookup(0, LOOKUP_BY_INDEX, 0xF, peer_idx=3) == expected_response(3, PEERS[3])
    assert await tb.lookup(0, LOOKUP_BY_INDEX, 0xF, peer_idx=1) == MISS
    assert await tb.lookup(0, LOOKUP_BY_INDEX, 1 << 2, peer_idx=3) == MISS

    assert await tb.lookup(1, LOOKUP_BY_RMEM, 1 << 1, rmem_addr=0x1000) == expected_response(
        1, PEERS[1]
    )
    assert await tb.lookup(1, LOOKUP_BY_RMEM, 1 << 1, rmem_addr=0x1090) == expected_response(
        1, PEERS[1]
    )
    assert await tb.lookup(1, LOOKUP_BY_RMEM, 1 << 1, rmem_addr=0x1100) == expected_response(
        2, PEERS[2]
    )
    assert await tb.lookup(1, LOOKUP_BY_RMEM, 1 << 1, rmem_addr=0x1180) == MISS
    assert await tb.lookup(1, LOOKUP_BY_RMEM, 1 << 2, rmem_addr=0x1000) == MISS

    assert await tb.lookup(0, LOOKUP_BY_MAC, 1 << 1, mac_addr=PEERS[1]["mac"]) == expected_response(
        1, PEERS[1]
    )
    assert await tb.lookup(0, LOOKUP_BY_MAC, 1 << 3, mac_addr=PEERS[3]["mac"]) == expected_response(
        3, PEERS[3]
    )
    assert await tb.lookup(0, LOOKUP_BY_MAC, 0xF, mac_addr=PEERS[0]["mac"]) == MISS
    assert await tb.lookup(0, LOOKUP_BY_MAC, 0, mac_addr=PEERS[3]["mac"]) == MISS
    assert await tb.lookup(0, 3, 0xF, peer_idx=3) == MISS


@cocotb.test()
async def test_rmem_wrap_and_zero_size(dut):
    tb = TB(dut)
    await tb.reset()

    wrapping = dict(PEERS[1])
    wrapping["rmem_offset"] = 0xFFFFFFF0
    wrapping["size"] = 0x20
    await tb.write_peer(1, **wrapping)

    assert await tb.lookup(0, LOOKUP_BY_RMEM, 1 << 1, rmem_addr=0xFFFFFFF8) == expected_response(
        1, wrapping
    )
    assert await tb.lookup(0, LOOKUP_BY_RMEM, 1 << 1, rmem_addr=0x00000008) == MISS

    wrapping["size"] = 0
    await tb.write_peer(1, **wrapping)
    assert await tb.lookup(0, LOOKUP_BY_RMEM, 1 << 1, rmem_addr=0xFFFFFFF0) == MISS


@cocotb.test()
async def test_snapshot_backpressure_and_pipeline_replacement(dut):
    tb = TB(dut)
    await tb.reset()
    await configure_peers(tb)

    old_response = await tb.accept_request(0, LOOKUP_BY_INDEX, 1 << 3, peer_idx=3)
    assert old_response == expected_response(3, PEERS[3])

    updated = dict(PEERS[3])
    updated.update(
        mac=0x0A0B0C0D0E0F,
        rmem_offset=0x4000,
        local_addr=0x14000000,
        remote_addr=0x24000000,
        size=0x180,
        irq_enable=0,
    )
    await tb.write_peer(3, **updated)

    assert int(dut.rsp_valid.value) == 1
    assert tb.response(0) == old_response, "stalled response changed with its CSR source"

    tb.set_request(1, LOOKUP_BY_INDEX, 1 << 3, peer_idx=3)
    for _ in range(10):
        await FallingEdge(dut.clk)
        await Timer(1, unit="ns")
        if packed_slice(dut.req_ready, 1, 1):
            break
    else:
        raise AssertionError("registered request grant did not arrive")
    await RisingEdge(dut.clk)
    await Timer(1, unit="ns")
    tb.req_valid[1] = 0
    tb.drive_lookup()
    assert int(dut.req_ready.value) == 0, "full response buffers did not backpressure requests"
    assert tb.response(0) == old_response
    tb.rsp_ready[0] = 1
    tb.drive_lookup()
    await RisingEdge(dut.clk)
    await Timer(1, unit="ns")
    tb.rsp_ready[0] = 0
    tb.drive_lookup()

    assert int(dut.rsp_valid.value) == 1 << 1
    assert tb.response(1) == expected_response(3, updated)
    await tb.consume_response(1, stall_cycles=2)


@cocotb.test()
async def test_round_robin_and_full_throughput(dut):
    tb = TB(dut)
    await tb.reset()
    await configure_peers(tb)

    tb.set_request(0, LOOKUP_BY_INDEX, 1 << 3, peer_idx=3)
    tb.set_request(1, LOOKUP_BY_MAC, 1 << 1, mac_addr=PEERS[1]["mac"])
    tb.rsp_ready = [1, 1]
    tb.drive_lookup()

    await RisingEdge(dut.clk)
    await Timer(1, unit="ns")
    assert int(dut.rsp_valid.value) == 0
    owners = []
    for _ in range(8):
        await RisingEdge(dut.clk)
        await Timer(1, unit="ns")
        valid = int(dut.rsp_valid.value)
        assert valid in (1, 2), "lookup pipeline inserted a response bubble"
        owner = 0 if valid == 1 else 1
        owners.append(owner)

        if owner == 0:
            assert tb.response(0) == expected_response(3, PEERS[3])
        else:
            assert tb.response(1) == expected_response(1, PEERS[1])

    assert all(a != b for a, b in zip(owners, owners[1:])), owners
    assert set(owners) == {0, 1}

    tb.req_valid = [0, 0]
    tb.drive_lookup()
    await RisingEdge(dut.clk)
    await Timer(1, unit="ns")
    assert int(dut.rsp_valid.value) == 0


@cocotb.test()
async def test_registered_outputs_between_clock_edges(dut):
    tb = TB(dut)
    await tb.reset()
    await configure_peers(tb)
    response = await tb.accept_request(0, LOOKUP_BY_MAC, 0xF, mac_addr=PEERS[1]["mac"])
    names = [
        "req_ready",
        "rsp_valid",
        "rsp_hit",
        "rsp_peer_idx",
        "rsp_mac_addr",
        "rsp_rmem_offset",
        "rsp_local_addr",
        "rsp_remote_addr",
        "rsp_size",
        "rsp_dma_mode",
        "rsp_irq_enable",
    ]
    outputs = [getattr(dut, name) for name in names]
    for _ in range(8):
        await FallingEdge(dut.clk)
        await Timer(1, unit="ns")
        before = [int(signal.value) for signal in outputs]
        tb.rsp_ready = [1] * tb.ports
        tb.req_valid = [1] * tb.ports
        tb.req_mac_addr = [0] * tb.ports
        tb.drive_lookup()
        await Timer(1, unit="ns")
        assert [int(signal.value) for signal in outputs] == before
        tb.req_valid = [0] * tb.ports
        tb.rsp_ready = [0] * tb.ports
        tb.drive_lookup()
        await Timer(1, unit="ns")
        assert [int(signal.value) for signal in outputs] == before
    assert tb.response(0) == response
    await tb.consume_response(0)


tests_dir = os.path.abspath(os.path.dirname(__file__))
repo_dir = os.path.abspath(os.path.join(tests_dir, "..", "..", ".."))
core_dir = os.path.join(repo_dir, "hw", "rtl", "core")
hal_if_dir = os.path.join(repo_dir, "build", "hal", "rtl")
hal_rtl_dir = os.path.join(repo_dir, "build", "hal", "openenoc_endpoint_full", "rtl")
hal_python_dir = os.path.join(repo_dir, "build", "hal", "openenoc_endpoint_full", "python")
common_dir = os.path.join(repo_dir, "dv", "common")


def test_openenoc_endpoint_peer_lookup(request):
    dut = "openenoc_endpoint_peer_lookup"
    module = os.path.splitext(os.path.basename(__file__))[0]
    toplevel = module

    verilog_sources = [
        os.path.join(hal_rtl_dir, "openenoc_endpoint_full_csr_pkg.sv"),
        os.path.join(hal_if_dir, "openenoc_endpoint_if.sv"),
        os.path.join(hal_if_dir, "openenoc_switch_if.sv"),
        os.path.join(core_dir, "openenoc_peer_lookup_if.sv"),
        os.path.join(core_dir, "openenoc_rr_arbiter.sv"),
        os.path.join(core_dir, f"{dut}.sv"),
        os.path.join(hal_rtl_dir, "openenoc_endpoint_full_csr.sv"),
        os.path.join(hal_rtl_dir, "openenoc_endpoint_full_csr_bridge.sv"),
        os.path.join(tests_dir, f"{toplevel}.sv"),
    ]

    parameters = {"LOOKUP_PORTS": 2}
    extra_env = {"PARAM_LOOKUP_PORTS": "2"}
    sim_build = os.path.join(tests_dir, "sim_build", request.node.name)

    cocotb_test.simulator.run(
        simulator="verilator",
        python_search=[tests_dir, hal_python_dir],
        verilog_sources=verilog_sources,
        toplevel=toplevel,
        module=module,
        parameters=parameters,
        timescale="1ns/1ps",
        extra_args=["-Wall", os.path.join(common_dir, "config.vlt")],
        sim_build=sim_build,
        extra_env=extra_env,
    )
