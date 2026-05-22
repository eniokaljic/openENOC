# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: AGPL-3.0-or-later

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

import cocotb
import threading
import queue
from cocotb.triggers import Timer

from build.python.csr.sim.csr import csr_simulator_cls

class RTLSimulator(csr_simulator_cls):
    def __init__(self, axi_master, address=0):
        super().__init__(address=address)
        
        self.axi = axi_master
        self.req_queue = queue.Queue()

    async def worker(self):
        while True:
            if self.req_queue.empty():
                await Timer(1, unit="ns")
                continue

            req = self.req_queue.get()

            if req["type"] == "read":
                resp = await self.axi.read(
                    req["addr"],
                    req["accesswidth"] // 8
                )

                value = int.from_bytes(resp.data, "little")

                req["result"] = value
                req["event"].set()

            else:
                payload = req["data"].to_bytes(req["accesswidth"] // 8, "little")

                await self.axi.write(req["addr"], payload)

                req["event"].set()

    # ------------------------------
    # SYNC API (called from thread)
    # ------------------------------
    def read(self, addr, width=32, accesswidth=32):
        event = threading.Event()

        req = {
            "type": "read",
            "addr": addr,
            "accesswidth": accesswidth,
            "event": event,
            "result": None
        }

        self.req_queue.put(req)

        event.wait()

        return req["result"]

    def write(self, addr, data, width=32, accesswidth=32):
        event = threading.Event()

        req = {
            "type": "write",
            "addr": addr,
            "data": data,
            "accesswidth": accesswidth,
            "event": event
        }

        self.req_queue.put(req)

        event.wait()

