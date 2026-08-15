# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: AGPL-3.0-or-later

from csr.lib import NormalCallbackSet
from csr.reg_model.csr import csr_cls
from hardware_interface import HardwareInterface
from tests import *

if __name__ == '__main__':
    hw = HardwareInterface(address=0)
    csr = csr_cls(callbacks=NormalCallbackSet(read_callback=hw.read, write_callback=hw.write))
    test1(csr)
    test2(csr)
