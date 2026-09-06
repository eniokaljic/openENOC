# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: AGPL-3.0-or-later

from cocotb.task import resume

from csr.sim.csr import csr_simulator_cls


class RTLSimulator(csr_simulator_cls):
    def __init__(self, axi_master, address=0):
        super().__init__(address=address)
        self.axi = axi_master

    @resume
    async def read(self, addr, width=32, accesswidth=32):
        del width
        response = await self.axi.read(addr, accesswidth // 8)
        return int.from_bytes(response.data, "little")

    @resume
    async def write(self, addr, data, width=32, accesswidth=32):
        del width
        payload = data.to_bytes(accesswidth // 8, "little")
        await self.axi.write(addr, payload)
