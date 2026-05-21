# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: AGPL-3.0-or-later

# An example test

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from build.python.openENOC.lib import NormalCallbackSet
from build.python.openENOC.reg_model.openENOC import openENOC_cls
from HardwareSimulator import HardwareSimulator

if __name__ == '__main__':
    hw = HardwareSimulator(address=0)
    reg_model = openENOC_cls(callbacks=NormalCallbackSet(read_callback=hw.read, write_callback=hw.write))

    reg_model.csr.test_reg.test_field.write(123)
    print(reg_model.csr.test_reg.test_field.read())
