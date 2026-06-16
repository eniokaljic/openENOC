# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: AGPL-3.0-or-later

from openenoc_csr.reg_model.openenoc_csr import openenoc_csr_cls

def test1(openenoc_csr):
    openenoc_csr.test_reg.test_field.write(123)
    assert openenoc_csr.test_reg.test_field.read() == 123

def test2(openenoc_csr):
    openenoc_csr.regB.f0.write(45)
    assert openenoc_csr.regB.f0.read() == 45

    openenoc_csr.regB.f1.write(67)
    assert openenoc_csr.regB.f1.read() == 67

    assert openenoc_csr.regB.f2.read() == 0

    assert openenoc_csr.regB.f3.read() == 0
