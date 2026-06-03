# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: AGPL-3.0-or-later

from csr.lib import NormalCallbackSet
from csr.reg_model.csr import csr_cls
from HardwareInterface import HardwareInterface
from Tests import *

if __name__ == '__main__':
    hw = HardwareInterface(address=0)
    csr = csr_cls(callbacks=NormalCallbackSet(read_callback=hw.read, write_callback=hw.write))
    Test1(csr)
    Test2(csr)
