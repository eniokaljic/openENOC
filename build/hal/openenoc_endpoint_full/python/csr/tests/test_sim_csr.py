


"""
Unit Tests for the csr register model Python Wrapper

This code was generated from the PeakRDL-python package version 3.1.2
"""








from typing import Union, cast

import unittest
from unittest.mock import Mock

import random


from ..sim_lib.register import Register,MemoryRegister
from ..sim_lib.field import ReadOnlyField, WriteOnlyField, ReadWriteField

from ._csr_sim_test_base import csr_SimTestCase_BlockAccess
from ._csr_sim_test_base import __name__ as base_name
from ._csr_test_base import random_enum_reg_value


from ..lib import SystemRDLEnum


from ..lib_test import reverse_bits

class csr_block_access(csr_SimTestCase_BlockAccess): # type: ignore[valid-type,misc]
    """
    tests for all the block access methods
    """

    

if __name__ == '__main__':

    unittest.main()




