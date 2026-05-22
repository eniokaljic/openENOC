# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: AGPL-3.0-or-later

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from build.python.csr.reg_model.csr import csr_cls

def Application(csr):
    csr.test_reg.test_field.write(123)
    assert csr.test_reg.test_field.read() == 123

    csr.regB.f0.write(45)
    assert csr.regB.f0.read() == 45

    csr.regB.f1.write(67)
    assert csr.regB.f1.read() == 67
        
    assert csr.regB.f2.read() == 0
        
    assert csr.regB.f3.read() == 0

