# SPDX-FileCopyrightText: 2026 Kerim Bavcic
# SPDX-License-Identifier: AGPL-3.0-or-later

import logging
import os
import random

import cocotb
import cocotb_test.simulator
import pytest
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer
from cocotb.regression import TestFactory
TestFactory.__test__ = False

# operation_mode encoding (CSR forwarding_control.operation_mode)
MANAGED = 1
UNMANAGED = 0

# 32-bit word select within a 16-byte forwarding table entry
WORD_MAC_LO = 0
WORD_MAC_HI = 1
WORD_IFACE = 2
WORD_CONFIG = 3

ALL_BITS = 0xFFFFFFFF

# driven on the request payload once the request cycle is over, the table must
# work from its own snapshot and must never look at the interface again
STALE = 0x0BADBADBADBA


class TB:
    def __init__(self, dut):
        self.dut = dut

        self.log = logging.getLogger("cocotb.tb")
        self.log.setLevel(logging.DEBUG)

        self.num_of_interfaces = len(dut.default_forwarding)
        self.table_depth = int(os.environ.get("PARAM_TABLE_DEPTH", 32))
        self.iface_mask = (1 << self.num_of_interfaces) - 1

        cocotb.start_soon(Clock(dut.clk, 10, units="ns").start())

    async def cycle(self, count=1):
        # advance one clock cycle and settle, so outputs can be sampled and
        # inputs can be driven from the same place in the cycle
        for _ in range(count):
            await RisingEdge(self.dut.clk)
            await Timer(1, units="ns")

    async def reset(self, operation_mode=MANAGED, default_forwarding=0):
        dut = self.dut

        dut.rst.setimmediatevalue(0)
        dut.operation_mode.setimmediatevalue(operation_mode)
        dut.default_forwarding.setimmediatevalue(default_forwarding)

        dut.cpuif_req.setimmediatevalue(0)
        dut.cpuif_addr.setimmediatevalue(0)
        dut.cpuif_req_is_wr.setimmediatevalue(0)
        dut.cpuif_wr_data.setimmediatevalue(0)
        dut.cpuif_wr_biten.setimmediatevalue(0)

        dut.lookup_req.setimmediatevalue(0)
        dut.lookup_mac_addr.setimmediatevalue(0)

        dut.learning_req.setimmediatevalue(0)
        dut.learning_mac_addr.setimmediatevalue(0)
        dut.learning_port_bitmap.setimmediatevalue(0)

        await self.cycle(2)
        dut.rst.value = 1
        await self.cycle(2)
        dut.rst.value = 0
        await self.cycle(2)

    def set_mode(self, operation_mode):
        self.dut.operation_mode.value = operation_mode

    def set_default_forwarding(self, bitmap):
        self.dut.default_forwarding.value = bitmap

    # ------------------------------------------------------------------
    # CPU interface (openENOC Switch Interface CSR side)
    # ------------------------------------------------------------------

    async def cpu_write(self, index, word, data, biten=ALL_BITS):
        dut = self.dut

        dut.cpuif_addr.value = index * 16 + word * 4
        dut.cpuif_req_is_wr.value = 1
        dut.cpuif_wr_data.value = data
        dut.cpuif_wr_biten.value = biten
        dut.cpuif_req.value = 1

        await self.cycle()
        dut.cpuif_req.value = 0
        dut.cpuif_addr.value = 0
        dut.cpuif_wr_data.value = 0
        dut.cpuif_wr_biten.value = 0

        while int(dut.cpuif_wr_ack.value) != 1:
            await self.cycle()

        assert int(dut.cpuif_rd_ack.value) == 0, "rd_ack asserted during a write access"
        await self.cycle()

    async def cpu_read(self, index, word):
        dut = self.dut

        dut.cpuif_addr.value = index * 16 + word * 4
        dut.cpuif_req_is_wr.value = 0
        dut.cpuif_req.value = 1

        await self.cycle()
        dut.cpuif_req.value = 0
        dut.cpuif_addr.value = 0

        while int(dut.cpuif_rd_ack.value) != 1:
            await self.cycle()

        assert int(dut.cpuif_wr_ack.value) == 0, "wr_ack asserted during a read access"
        data = int(dut.cpuif_rd_data.value)
        await self.cycle()

        return data

    async def cpu_write_entry(self, index, mac, bitmap, enabled=1):
        await self.cpu_write(index, WORD_MAC_LO, mac & 0xFFFFFFFF)
        await self.cpu_write(index, WORD_MAC_HI, (mac >> 32) & 0xFFFF)
        await self.cpu_write(index, WORD_IFACE, bitmap)
        await self.cpu_write(index, WORD_CONFIG, enabled)

    async def cpu_read_entry(self, index):
        mac_lo = await self.cpu_read(index, WORD_MAC_LO)
        mac_hi = await self.cpu_read(index, WORD_MAC_HI)
        bitmap = await self.cpu_read(index, WORD_IFACE)
        enabled = await self.cpu_read(index, WORD_CONFIG)

        return ((mac_hi << 32) | mac_lo, bitmap, enabled)

    # ------------------------------------------------------------------
    # Lookup / learning interfaces (forwarding engine side)
    # ------------------------------------------------------------------

    async def lookup(self, mac):
        dut = self.dut

        dut.lookup_mac_addr.value = mac
        dut.lookup_req.value = 1

        await self.cycle()
        dut.lookup_req.value = 0
        dut.lookup_mac_addr.value = STALE

        while int(dut.lookup_ack.value) != 1:
            await self.cycle()

        bitmap = int(dut.lookup_port_bitmap.value)
        await self.cycle()

        return bitmap

    async def learn(self, mac, bitmap):
        dut = self.dut

        dut.learning_mac_addr.value = mac
        dut.learning_port_bitmap.value = bitmap
        dut.learning_req.value = 1

        await self.cycle()
        dut.learning_req.value = 0
        dut.learning_mac_addr.value = STALE
        dut.learning_port_bitmap.value = 0

        while int(dut.learning_ack.value) != 1:
            await self.cycle()

        await self.cycle()


# ----------------------------------------------------------------------
# Helper functions
# ----------------------------------------------------------------------

def make_mac(index):
    # locally administered unicast MAC addresses, one per table index
    return 0x020E0C000000 | (index & 0xFFFFFF)


def single_port(index, num_of_interfaces):
    return 1 << (index % num_of_interfaces)


# ----------------------------------------------------------------------
# Test cases
# ----------------------------------------------------------------------

async def run_reset_state(dut):
    tb = TB(dut)
    flood = tb.iface_mask
    await tb.reset(operation_mode=MANAGED, default_forwarding=flood)

    for index in range(tb.table_depth):
        mac, bitmap, enabled = await tb.cpu_read_entry(index)
        assert (mac, bitmap, enabled) == (0, 0, 0), \
            f"entry {index} is not cleared after reset: {mac:012x} {bitmap:x} {enabled}"

    # an empty table always misses, so every lookup returns default_forwarding
    assert await tb.lookup(make_mac(0)) == flood


async def run_cpu_program_and_readback(dut):
    tb = TB(dut)
    await tb.reset(operation_mode=MANAGED, default_forwarding=0)

    rnd = random.Random(1234)
    entries = []

    for index in range(tb.table_depth):
        mac = rnd.getrandbits(48)
        bitmap = rnd.getrandbits(tb.num_of_interfaces)
        enabled = rnd.getrandbits(1)
        entries.append((mac, bitmap, enabled))
        await tb.cpu_write_entry(index, mac, bitmap, enabled)

    for index, expected in enumerate(entries):
        got = await tb.cpu_read_entry(index)
        assert got == expected, f"entry {index} readback mismatch: {got} != {expected}"


async def run_cpu_write_bit_enables(dut):
    tb = TB(dut)
    await tb.reset(operation_mode=MANAGED, default_forwarding=0)

    await tb.cpu_write_entry(0, 0xFFFFFFFFFFFF, tb.iface_mask, 1)

    # only the byte enabled bits may be modified
    await tb.cpu_write(0, WORD_MAC_LO, 0x00000000, biten=0x0000FFFF)
    await tb.cpu_write(0, WORD_MAC_HI, 0x00000000, biten=0x000000FF)
    await tb.cpu_write(0, WORD_CONFIG, 0x00000000, biten=0xFFFFFFFE)

    mac, bitmap, enabled = await tb.cpu_read_entry(0)

    assert mac == 0xFF00FFFF0000, f"bit enables not honoured: {mac:012x}"
    assert bitmap == tb.iface_mask
    assert enabled == 1, "config.enabled modified without its bit enable"


async def run_lookup_managed(dut):
    tb = TB(dut)
    flood = tb.iface_mask
    await tb.reset(operation_mode=MANAGED, default_forwarding=flood)

    for index in range(tb.table_depth):
        await tb.cpu_write_entry(index, make_mac(index),
                                 single_port(index, tb.num_of_interfaces), 1)

    for index in range(tb.table_depth):
        expected = single_port(index, tb.num_of_interfaces)
        got = await tb.lookup(make_mac(index))
        assert got == expected, f"lookup {index} returned {got:x}, expected {expected:x}"

    # unknown MAC address, forwarded according to default_forwarding
    assert await tb.lookup(0x0EE0EE0EE0EE) == flood

    # a disabled entry must be ignored during lookup
    await tb.cpu_write(0, WORD_CONFIG, 0)
    assert await tb.lookup(make_mac(0)) == flood

    # default_forwarding is sampled by the table, not latched at configuration
    tb.set_default_forwarding(0)
    assert await tb.lookup(make_mac(0)) == 0


async def run_learning_ignored_in_managed_mode(dut):
    tb = TB(dut)
    flood = tb.iface_mask
    await tb.reset(operation_mode=MANAGED, default_forwarding=flood)

    for index in range(tb.table_depth + 2):
        await tb.learn(make_mac(index), single_port(index, tb.num_of_interfaces))

    # the learning process is transparent, but the table stays untouched
    for index in range(tb.table_depth):
        assert await tb.cpu_read_entry(index) == (0, 0, 0), \
            f"entry {index} modified while in managed mode"

    assert await tb.lookup(make_mac(0)) == flood


async def run_learning_unmanaged(dut):
    tb = TB(dut)
    flood = tb.iface_mask
    await tb.reset(operation_mode=UNMANAGED, default_forwarding=flood)

    # fill the whole table, the write pointer wraps back to entry 0
    for index in range(tb.table_depth):
        await tb.learn(make_mac(index), single_port(index, tb.num_of_interfaces))

    for index in range(tb.table_depth):
        expected = single_port(index, tb.num_of_interfaces)
        got = await tb.lookup(make_mac(index))
        assert got == expected, f"learned entry {index}: {got:x} != {expected:x}"

    # software may still inspect the learned entries
    mac, bitmap, enabled = await tb.cpu_read_entry(0)
    assert (mac, bitmap, enabled) == (make_mac(0),
                                      single_port(0, tb.num_of_interfaces), 1)

    # a known MAC address only refreshes the port bitmap, no entry is consumed
    last = tb.table_depth - 1
    refreshed = single_port(last + 1, tb.num_of_interfaces)
    await tb.learn(make_mac(last), refreshed)
    assert await tb.lookup(make_mac(last)) == refreshed
    assert await tb.cpu_read_entry(last) == (make_mac(last), refreshed, 1)

    # a new MAC address overwrites the oldest entry (circular allocation)
    new_mac = make_mac(0x800000)
    new_bitmap = single_port(1, tb.num_of_interfaces)
    await tb.learn(new_mac, new_bitmap)

    assert await tb.lookup(new_mac) == new_bitmap
    assert await tb.cpu_read_entry(0) == (new_mac, new_bitmap, 1)
    assert await tb.lookup(make_mac(0)) == flood, "oldest entry was not replaced"


async def run_cpu_write_ignored_in_unmanaged_mode(dut):
    tb = TB(dut)
    flood = tb.iface_mask
    await tb.reset(operation_mode=MANAGED, default_forwarding=flood)

    mac = make_mac(7)
    bitmap = single_port(0, tb.num_of_interfaces)
    await tb.cpu_write_entry(0, mac, bitmap, 1)

    tb.set_mode(UNMANAGED)
    await tb.cycle()

    # writes are acknowledged, but must not change the table
    await tb.cpu_write_entry(0, 0xFFFFFFFFFFFF, tb.iface_mask, 0)

    assert await tb.cpu_read_entry(0) == (mac, bitmap, 1), \
        "software write accepted while in unmanaged mode"
    assert await tb.lookup(mac) == bitmap


async def run_exclusive_access(dut):
    tb = TB(dut)
    flood = tb.iface_mask
    await tb.reset(operation_mode=MANAGED, default_forwarding=flood)

    mac = make_mac(3)
    bitmap = single_port(2, tb.num_of_interfaces)
    await tb.cpu_write_entry(0, mac, bitmap, 1)

    # a lookup request and a CPU access overlap in time, the table serves only
    # one of them at a time, but both must complete
    dut.lookup_mac_addr.value = mac
    dut.lookup_req.value = 1
    read_task = cocotb.start_soon(tb.cpu_read(0, WORD_IFACE))

    await tb.cycle()
    dut.lookup_req.value = 0
    dut.lookup_mac_addr.value = STALE

    while int(dut.lookup_ack.value) != 1:
        assert int(dut.lookup_ack.value) + int(dut.cpuif_rd_ack.value) \
            + int(dut.cpuif_wr_ack.value) <= 1, "table served two masters at once"
        await tb.cycle()

    assert int(dut.cpuif_rd_ack.value) == 0, "table served two masters at once"
    lookup_bitmap = int(dut.lookup_port_bitmap.value)
    await tb.cycle()

    assert lookup_bitmap == bitmap
    assert await read_task == bitmap


async def run_concurrent_requests(dut):
    tb = TB(dut)
    flood = tb.iface_mask
    await tb.reset(operation_mode=UNMANAGED, default_forwarding=flood)

    mac = make_mac(5)
    bitmap = single_port(1, tb.num_of_interfaces)

    # all three interfaces issue a single cycle request in the very same clock
    # cycle, no request may be lost while the table is busy with another one
    dut.cpuif_addr.value = WORD_IFACE * 4
    dut.cpuif_req_is_wr.value = 0
    dut.cpuif_req.value = 1

    dut.lookup_mac_addr.value = mac
    dut.lookup_req.value = 1

    dut.learning_mac_addr.value = mac
    dut.learning_port_bitmap.value = bitmap
    dut.learning_req.value = 1

    await tb.cycle()

    # the request payload is only required to be valid in the request cycle
    dut.cpuif_req.value = 0
    dut.cpuif_addr.value = 0
    dut.lookup_req.value = 0
    dut.lookup_mac_addr.value = STALE
    dut.learning_req.value = 0
    dut.learning_mac_addr.value = STALE
    dut.learning_port_bitmap.value = 0

    acks = {"cpu": 0, "lookup": 0, "learning": 0}
    order = []
    rd_data = None
    lookup_bitmap = None

    for _ in range(16):
        active = int(dut.cpuif_rd_ack.value) + int(dut.cpuif_wr_ack.value) \
            + int(dut.lookup_ack.value) + int(dut.learning_ack.value)
        assert active <= 1, "more than one interface acknowledged in one cycle"

        if int(dut.cpuif_rd_ack.value):
            order.append("cpu")
            rd_data = int(dut.cpuif_rd_data.value)
        if int(dut.lookup_ack.value):
            order.append("lookup")
            lookup_bitmap = int(dut.lookup_port_bitmap.value)
        if int(dut.learning_ack.value):
            order.append("learning")

        acks["cpu"] += int(dut.cpuif_rd_ack.value)
        acks["lookup"] += int(dut.lookup_ack.value)
        acks["learning"] += int(dut.learning_ack.value)
        await tb.cycle()

    assert acks == {"cpu": 1, "lookup": 1, "learning": 1}, \
        f"lost or duplicated requests: {acks}"

    # software has the highest priority, learning the lowest
    assert order == ["cpu", "lookup", "learning"], f"unexpected service order: {order}"

    # both were served before the learning write happened, so they still see an
    # empty table
    assert rd_data == 0, f"stale read data on a cleared entry: {rd_data:x}"
    assert lookup_bitmap == flood, "the lookup was served after the learning write"

    # the learning request was captured with its payload and did update the
    # table, the very same lookup that flooded before now hits
    assert await tb.lookup(mac) == bitmap

    # and software sees the learned entry through the CPU interface as well
    assert await tb.cpu_read_entry(0) == (mac, bitmap, 1), \
        "the learned entry is not visible to software"


async def run_iface_bit_enables(dut):
    tb = TB(dut)
    await tb.reset(operation_mode=MANAGED, default_forwarding=0)

    await tb.cpu_write_entry(0, make_mac(0), tb.iface_mask, 1)

    # clearing a single interface bit must leave the remaining ones untouched
    await tb.cpu_write(0, WORD_IFACE, 0x00000000, biten=0x00000001)
    mac, bitmap, enabled = await tb.cpu_read_entry(0)

    assert bitmap == tb.iface_mask & ~0x1, f"iface bit enables not honoured: {bitmap:x}"
    assert mac == make_mac(0), "the MAC address was modified by an iface write"
    assert enabled == 1
    assert await tb.lookup(make_mac(0)) == tb.iface_mask & ~0x1

    # setting it back through the same bit enable
    await tb.cpu_write(0, WORD_IFACE, ALL_BITS, biten=0x00000001)
    _, bitmap, _ = await tb.cpu_read_entry(0)
    assert bitmap == tb.iface_mask

    # a write without any bit enable set changes nothing
    await tb.cpu_write(0, WORD_IFACE, 0x00000000, biten=0x00000000)
    _, bitmap, _ = await tb.cpu_read_entry(0)
    assert bitmap == tb.iface_mask, "a write with no bit enables changed the bitmap"


async def run_duplicate_mac_lowest_index_wins(dut):
    tb = TB(dut)
    flood = tb.iface_mask
    await tb.reset(operation_mode=MANAGED, default_forwarding=flood)

    mac = make_mac(9)
    low = single_port(0, tb.num_of_interfaces)
    high = single_port(1, tb.num_of_interfaces)

    # the very same MAC address is programmed into two entries
    await tb.cpu_write_entry(1, mac, low, 1)
    await tb.cpu_write_entry(tb.table_depth - 1, mac, high, 1)

    assert await tb.lookup(mac) == low, "the lowest matching index must win"

    # with the lowest match disabled the next one takes over
    await tb.cpu_write(1, WORD_CONFIG, 0)
    assert await tb.lookup(mac) == high

    # with both disabled the lookup misses again
    await tb.cpu_write(tb.table_depth - 1, WORD_CONFIG, 0)
    assert await tb.lookup(mac) == flood


async def run_blackhole_entry(dut):
    tb = TB(dut)
    flood = tb.iface_mask
    await tb.reset(operation_mode=MANAGED, default_forwarding=flood)

    dropped = make_mac(11)
    await tb.cpu_write_entry(0, dropped, 0, 1)

    # a hit with an empty bitmap means "drop", it must not fall back to
    # default_forwarding the way a miss does
    assert await tb.lookup(dropped) == 0, \
        "a hit with an empty bitmap fell back to default_forwarding"

    # an actual miss still floods
    assert await tb.lookup(make_mac(12)) == flood


async def run_learn_pointer_unaffected_by_managed_mode(dut):
    tb = TB(dut)
    flood = tb.iface_mask
    await tb.reset(operation_mode=MANAGED, default_forwarding=flood)

    # learning requests are acknowledged, but they may not move the write
    # pointer while software owns the table
    for index in range(tb.table_depth + 3):
        await tb.learn(make_mac(index), single_port(index, tb.num_of_interfaces))

    tb.set_mode(UNMANAGED)
    await tb.cycle()

    mac = make_mac(0xA00000)
    bitmap = single_port(0, tb.num_of_interfaces)
    await tb.learn(mac, bitmap)

    assert await tb.cpu_read_entry(0) == (mac, bitmap, 1), \
        "the circular write pointer moved while in managed mode"


async def run_cpu_address_out_of_range(dut):
    tb = TB(dut)
    await tb.reset(operation_mode=MANAGED, default_forwarding=0)

    # the address bus covers a power of two number of entries, only a table
    # depth that is not a power of two leaves addresses without an entry
    addressable = 1 << (len(dut.cpuif_addr) - 4)

    if addressable <= tb.table_depth:
        tb.log.info("address space matches the table depth, nothing to check")
        return

    mac = make_mac(1)
    bitmap = single_port(0, tb.num_of_interfaces)
    await tb.cpu_write_entry(0, mac, bitmap, 1)

    bad = tb.table_depth

    # the access is acknowledged, otherwise the CPU would stall forever, but it
    # must neither write anything nor return anything
    await tb.cpu_write_entry(bad, 0xFFFFFFFFFFFF, tb.iface_mask, 1)

    assert await tb.cpu_read_entry(bad) == (0, 0, 0), \
        "a read outside the table returned data"
    assert await tb.cpu_read_entry(0) == (mac, bitmap, 1), \
        "a write outside the table corrupted an existing entry"
    assert await tb.lookup(0xFFFFFFFFFFFF) == 0, \
        "a write outside the table created a searchable entry"


async def run_held_request(dut):
    tb = TB(dut)
    flood = tb.iface_mask
    await tb.reset(operation_mode=UNMANAGED, default_forwarding=flood)

    mac = make_mac(2)
    bitmap = single_port(0, tb.num_of_interfaces)

    # the request is kept asserted past the acknowledge instead of being a
    # single cycle strobe, the table must still perform exactly one transaction
    dut.learning_mac_addr.value = mac
    dut.learning_port_bitmap.value = bitmap
    dut.learning_req.value = 1

    acks = 0
    for i in range(16):
        acks += int(dut.learning_ack.value)
        if i == 5:
            dut.learning_req.value = 0
            dut.learning_mac_addr.value = STALE
            dut.learning_port_bitmap.value = 0
        await tb.cycle()

    assert acks == 1, f"a held learning request produced {acks} acknowledges"
    assert await tb.lookup(mac) == bitmap

    # exactly one entry was consumed, so the next new address lands right after
    next_mac = make_mac(3)
    next_bitmap = single_port(1, tb.num_of_interfaces)
    await tb.learn(next_mac, next_bitmap)
    assert await tb.cpu_read_entry(1) == (next_mac, next_bitmap, 1), \
        "a held learning request consumed more than one entry"

    # the same for the lookup interface
    dut.lookup_mac_addr.value = mac
    dut.lookup_req.value = 1

    acks = 0
    for i in range(16):
        acks += int(dut.lookup_ack.value)
        if int(dut.lookup_ack.value) == 1:
            assert int(dut.lookup_port_bitmap.value) == bitmap
        if i == 5:
            dut.lookup_req.value = 0
            dut.lookup_mac_addr.value = STALE
        await tb.cycle()

    assert acks == 1, f"a held lookup request produced {acks} acknowledges"


async def run_back_to_back_requests(dut):
    tb = TB(dut)
    flood = tb.iface_mask
    await tb.reset(operation_mode=MANAGED, default_forwarding=flood)

    count = min(tb.table_depth, 8)

    for index in range(count):
        await tb.cpu_write_entry(index, make_mac(index),
                                 single_port(index, tb.num_of_interfaces), 1)

    # every request is issued in the cycle right after the previous acknowledge,
    # without the settling cycle the TB helpers normally insert
    for index in range(count):
        dut.lookup_mac_addr.value = make_mac(index)
        dut.lookup_req.value = 1

        await tb.cycle()
        dut.lookup_req.value = 0
        dut.lookup_mac_addr.value = STALE

        while int(dut.lookup_ack.value) != 1:
            await tb.cycle()

        expected = single_port(index, tb.num_of_interfaces)
        got = int(dut.lookup_port_bitmap.value)
        assert got == expected, \
            f"back to back lookup {index} returned {got:x}, expected {expected:x}"

    dut.lookup_mac_addr.value = 0


# ----------------------------------------------------------------------
# Dispatch: select test cases to run based on Makefile configuration
# ----------------------------------------------------------------------

if getattr(cocotb, 'top', None) is not None:
    for test in [run_reset_state,
                 run_cpu_program_and_readback,
                 run_cpu_write_bit_enables,
                 run_iface_bit_enables,
                 run_lookup_managed,
                 run_duplicate_mac_lowest_index_wins,
                 run_blackhole_entry,
                 run_learning_ignored_in_managed_mode,
                 run_learn_pointer_unaffected_by_managed_mode,
                 run_learning_unmanaged,
                 run_cpu_write_ignored_in_unmanaged_mode,
                 run_cpu_address_out_of_range,
                 run_exclusive_access,
                 run_concurrent_requests,
                 run_held_request,
                 run_back_to_back_requests]:
        TestFactory(test).generate_tests()

# ----------------------------------------------------------------------
# PyTest framework: test parameterization and test runner
# ----------------------------------------------------------------------

tests_dir = os.path.dirname(__file__)
hw_dir = os.path.abspath(os.path.join(tests_dir, '..', '..', '..', 'hw'))
core_dir = os.path.join(hw_dir, 'rtl', 'core')
common_dir = os.path.abspath(os.path.join(tests_dir, '..', '..', 'common'))


# a table depth that is not a power of two leaves addresses inside the address
# space that have no entry behind them, which exercises the range check
@pytest.mark.parametrize("num_of_interfaces, table_depth",
                         [(2, 4), (4, 8), (5, 20), (8, 32)])
def test_openenoc_forwarding_table(request, num_of_interfaces, table_depth):
    dut = "openenoc_forwarding_table"
    module = os.path.splitext(os.path.basename(__file__))[0]
    toplevel = module

    verilog_sources = [
        os.path.join(tests_dir, f"{toplevel}.sv"),
        os.path.join(core_dir, f"{dut}.sv"),
    ]

    parameters = {}
    parameters['NUM_OF_INTERFACES'] = num_of_interfaces
    parameters['TABLE_DEPTH'] = table_depth

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
