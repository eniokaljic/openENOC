


"""
Unit Tests for the csr register model Python Wrapper

This code was generated from the PeakRDL-python package version 3.1.1
"""






from typing import Union,Iterable
from array import array as Array

import unittest
from unittest.mock import patch, call

import random
from itertools import combinations, chain
import math


from ..lib import UnsupportedWidthError

from ..reg_model import RegModel
from ..reg_model.csr_property_enums import *


from ..lib import FieldReadOnly, FieldWriteOnly, FieldReadWrite
from ..lib import RegReadWrite, RegReadOnly, RegWriteOnly
from ..lib import RegReadWriteArray, RegReadOnlyArray, RegWriteOnlyArray
from ..lib import MemoryReadOnly, MemoryWriteOnly, MemoryReadWrite
from ..lib import MemoryReadOnlyArray, MemoryWriteOnlyArray, MemoryReadWriteArray
from ..lib import AddressMap, RegFile
from ..lib import AddressMapArray, RegFileArray
from ..lib import Memory


from ..lib import NodeArray
from ..lib import Field
from ..lib import Reg

from ..lib import SystemRDLEnum, SystemRDLEnumEntry

from ..lib_test import reverse_bits
from ..lib_test import NodeIterators

from ._csr_test_base import csr_TestCase, csr_TestCase_BlockAccess, csr_TestCase_AltBlockAccess
from ._csr_test_base import __name__ as base_name
from ._csr_test_base import random_enum_reg_value




class csr_single_access(csr_TestCase): # type: ignore[valid-type,misc]



    def test_user_defined_properties(self)  -> None:
        """
        Walk the address map and check user defined properties are correctly pulled up
        """
        with self.subTest(msg='register: csr.test_reg'):
            
            
            self.assertDictEqual(self.dut.test_reg.udp,{})
            
        with self.subTest(msg='register: csr.test_reg.test_field'):
            
            
            self.assertDictEqual(self.dut.test_reg.test_field.udp,{})
            
        

     

    def test_register(self) -> None:
        """
        Walk the registers in the register map and check:
        - the properties
        - it can be read and written to correctly
        """
        with self.subTest(msg='register: csr.test_reg'):
            self._single_register_property_test(rut=self.dut.test_reg, address=0, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.test_reg",
                                                rdl_desc="Test register",
                                                inst_name='test_reg',
                                                parent_full_inst_name='csr')
            self._single_register_read_and_write_test(rut=self.dut.test_reg, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['test_field', ]),
                                                                                          writeable_fields=set(['test_field', ]) )
        

    def test_field(self) -> None:
        """
        Check the properties and function (read and write) on the fields both integer and enum
        """
        
        with self.subTest(msg='field: csr.test_reg.test_field'):
            self._single_field_property_test(fut=self.dut.test_reg.test_field, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=0,
                                             rdl_name="csr.test_reg.test_field[31:0]",
                                             rdl_desc="4-byte test field",
                                             inst_name='test_field',
                                             parent_full_inst_name='csr.test_reg')
            self._single_int_field_read_and_write_test(fut=self.dut.test_reg.test_field, is_sw_readable=True, is_sw_writable=True)

    def test_addrmap(self) -> None:
        """
        Check the properties on the addrmaps files
        """

        
        with self.subTest(msg='addrmap: top_node'):
            self._single_addrmap_property_test(dut=self.dut,
                                               size=4,
                                               rdl_name="csr",
                                               rdl_desc="openENOC CSR",
                                               inst_name='csr',
                                               parent_full_inst_name=None)
            self._test_addrmap_iterators(dut=self.dut,
                                         writeable_registers=NodeIterators('test_reg',),
                                         readable_registers=NodeIterators('test_reg',),
                                         sections=NodeIterators(),
                                         memories=NodeIterators())
        


        # test all the address maps
        

    def test_regfile(self) -> None:
        """
        Check the properties on the register files
        """

        # test all the register files
        

    

    def test_array_slicing(self) -> None:
        """
        Check slicing into array
        """
        full_slice:NodeArray
        



class csr_block_access(csr_TestCase_BlockAccess): # type: ignore[valid-type,misc]
    """
    tests for all the block access methods
    """

    

    def test_register_array_context_manager(self) -> None:
        """
        Walk the register map and check that register map context managers work correctly
        """
        

class csr_alt_block_access(csr_TestCase_AltBlockAccess): # type: ignore[valid-type,misc]
    """
    tests for all the block access methods with the alternative callbacks, this is a simpler
    version of the tests above
    """
    

    def test_register_array_context_manager(self) -> None:
        """
        Walk the register map and check that register map context managers work correctly
        """
        


if __name__ == '__main__':

    unittest.main()