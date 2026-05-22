# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: AGPL-3.0-or-later

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from build.python.csr.lib import NormalCallbackSet
from build.python.csr.reg_model.csr import csr_cls
from HardwareInterface import HardwareInterface
from Application import Application

if __name__ == '__main__':
    hw = HardwareInterface(address=0)
    csr = csr_cls(callbacks=NormalCallbackSet(read_callback=hw.read, write_callback=hw.write))
    Application(csr)

