# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: AGPL-3.0-or-later

# Dummy hardware interface - to be replaced with JTAG or similar interface

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from build.python.csr.sim.csr import csr_simulator_cls

class HardwareInterface(csr_simulator_cls):
    def read(self, addr: int, width: int = 32, accesswidth: int = 32) -> int:
        data = self._read(addr, width, accesswidth)
        print(f"Read value 0x{data:08X} from address 0x{addr:08X}")
        return data

    def write(self, addr: int, data: int, width: int=32, accesswidth: int=32) -> None:
        print(f"Write value 0x{data:08X} to address 0x{addr:08X}")
        self._write(addr, width, accesswidth, data)
