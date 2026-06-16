# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: AGPL-3.0-or-later

from openenoc_csr.lib import NormalCallbackSet
from openenoc_csr.reg_model.openenoc_csr import openenoc_csr_cls
from hardware_interface import HardwareInterface
from tests import *

if __name__ == '__main__':
    hw = HardwareInterface(address=0)
    openenoc_csr = openenoc_csr_cls(callbacks=NormalCallbackSet(read_callback=hw.read, write_callback=hw.write))
    test1(openenoc_csr)
    test2(openenoc_csr)
