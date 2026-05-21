


"""
Unit Tests for the openENOC register model Python Wrapper

This code was generated from the PeakRDL-python package version 3.1.1
"""








from typing import Union, cast

import unittest
from unittest.mock import Mock

import random


from ..sim_lib.register import Register,MemoryRegister
from ..sim_lib.field import ReadOnlyField, WriteOnlyField, ReadWriteField

from ._openENOC_sim_test_base import openENOC_SimTestCase_BlockAccess
from ._openENOC_sim_test_base import __name__ as base_name
from ._openENOC_test_base import random_enum_reg_value


from ..lib import SystemRDLEnum


from ..lib_test import reverse_bits

class openENOC_csr_block_access(openENOC_SimTestCase_BlockAccess): # type: ignore[valid-type,misc]
    """
    tests for all the block access methods
    """

    

if __name__ == '__main__':

    unittest.main()




