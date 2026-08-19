


"""
Unit Tests for the csr register model Python Wrapper

This code was generated from the PeakRDL-python package version 3.1.2
"""







import unittest


from ..lib import RegisterWriteVerifyError

from ..lib import NormalCallbackSet


from ._csr_test_base import csr_TestCase, csr_TestCase_BlockAccess

from ..reg_model import RegModel
from ..sim import Simulator


TestCaseBase = unittest.TestCase


class csr_SimTestCase_BlockAccess(TestCaseBase): # type: ignore[valid-type,misc]

    def setUp(self) -> None:
        self.sim = Simulator(address=0)
        self.dut = RegModel(callbacks=NormalCallbackSet(read_callback=self.sim.read,
                                                          write_callback=self.sim.write,
                                                          read_block_callback=self.sim.read_block,
                                                          write_block_callback=self.sim.write_block))




if __name__ == '__main__':
    pass