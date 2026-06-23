


"""
Unit Tests for the openenoc_csr register model Python Wrapper

This code was generated from the PeakRDL-python package version 3.1.2
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
from ..reg_model.openenoc_csr_property_enums import *


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

from ._openenoc_csr_test_base import openenoc_csr_TestCase, openenoc_csr_TestCase_BlockAccess, openenoc_csr_TestCase_AltBlockAccess
from ._openenoc_csr_test_base import __name__ as base_name
from ._openenoc_csr_test_base import random_enum_reg_value




class openenoc_csr_single_access(openenoc_csr_TestCase): # type: ignore[valid-type,misc]



    def test_user_defined_properties(self)  -> None:
        """
        Walk the address map and check user defined properties are correctly pulled up
        """
        with self.subTest(msg='register: openenoc_csr.endpoint1'):
            
            
            self.assertDictEqual(self.dut.endpoint1.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint2'):
            
            
            self.assertDictEqual(self.dut.endpoint2.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1'):
            
            
            self.assertDictEqual(self.dut.switch1.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2'):
            
            
            self.assertDictEqual(self.dut.switch2.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.test_reg'):
            
            
            self.assertDictEqual(self.dut.test_reg.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.regB'):
            
            
            self.assertDictEqual(self.dut.regB.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.test_reg.test_field'):
            
            
            self.assertDictEqual(self.dut.test_reg.test_field.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.regB.f0'):
            
            
            self.assertDictEqual(self.dut.regB.f0.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.regB.f1'):
            
            
            self.assertDictEqual(self.dut.regB.f1.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.regB.f2'):
            
            
            self.assertDictEqual(self.dut.regB.f2.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.regB.f3'):
            
            
            self.assertDictEqual(self.dut.regB.f3.udp,{})
            
        

     

    def test_register(self) -> None:
        """
        Walk the registers in the register map and check:
        - the properties
        - it can be read and written to correctly
        """
        with self.subTest(msg='register: openenoc_csr.test_reg'):
            self._single_register_property_test(rut=self.dut.test_reg, address=0, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.test_reg",
                                                rdl_desc="Test register",
                                                inst_name='test_reg',
                                                parent_full_inst_name='openenoc_csr')
            self._single_register_read_and_write_test(rut=self.dut.test_reg, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['test_field', ]),
                                                                                          writeable_fields=set(['test_field', ]) )
        with self.subTest(msg='register: openenoc_csr.regB'):
            self._single_register_property_test(rut=self.dut.regB, address=4, width=32, accesswidth=32, size=4,
                                                rdl_name=None,
                                                rdl_desc=None,
                                                inst_name='regB',
                                                parent_full_inst_name='openenoc_csr')
            self._single_register_read_and_write_test(rut=self.dut.regB, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['f0','f1','f2','f3', ]),
                                                                                          writeable_fields=set(['f0','f1','f2','f3', ]) )
        

    def test_field(self) -> None:
        """
        Check the properties and function (read and write) on the fields both integer and enum
        """
        
        with self.subTest(msg='field: openenoc_csr.test_reg.test_field'):
            self._single_field_property_test(fut=self.dut.test_reg.test_field, lsb=0, msb=31, low=0, high=31, is_volatile=False, default=0,
                                             rdl_name="csr.test_reg.test_field[31:0]",
                                             rdl_desc="4-byte test field",
                                             inst_name='test_field',
                                             parent_full_inst_name='openenoc_csr.test_reg')
            self._single_int_field_read_and_write_test(fut=self.dut.test_reg.test_field, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.regB.f0'):
            self._single_field_property_test(fut=self.dut.regB.f0, lsb=0, msb=7, low=0, high=7, is_volatile=False, default=0,
                                             rdl_name=None,
                                             rdl_desc=None,
                                             inst_name='f0',
                                             parent_full_inst_name='openenoc_csr.regB')
            self._single_int_field_read_and_write_test(fut=self.dut.regB.f0, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.regB.f1'):
            self._single_field_property_test(fut=self.dut.regB.f1, lsb=8, msb=15, low=8, high=15, is_volatile=False, default=0,
                                             rdl_name=None,
                                             rdl_desc=None,
                                             inst_name='f1',
                                             parent_full_inst_name='openenoc_csr.regB')
            self._single_int_field_read_and_write_test(fut=self.dut.regB.f1, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.regB.f2'):
            self._single_field_property_test(fut=self.dut.regB.f2, lsb=16, msb=23, low=16, high=23, is_volatile=False, default=0,
                                             rdl_name=None,
                                             rdl_desc=None,
                                             inst_name='f2',
                                             parent_full_inst_name='openenoc_csr.regB')
            self._single_int_field_read_and_write_test(fut=self.dut.regB.f2, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.regB.f3'):
            self._single_field_property_test(fut=self.dut.regB.f3, lsb=24, msb=31, low=24, high=31, is_volatile=False, default=0,
                                             rdl_name=None,
                                             rdl_desc=None,
                                             inst_name='f3',
                                             parent_full_inst_name='openenoc_csr.regB')
            self._single_int_field_read_and_write_test(fut=self.dut.regB.f3, is_sw_readable=True, is_sw_writable=True)

    def test_addrmap(self) -> None:
        """
        Check the properties on the addrmaps files
        """

        
        with self.subTest(msg='addrmap: top_node'):
            self._single_addrmap_property_test(dut=self.dut,
                                               size=7168,
                                               rdl_name="csr",
                                               rdl_desc="openENOC CSR",
                                               inst_name='openenoc_csr',
                                               parent_full_inst_name=None)
            self._test_addrmap_iterators(dut=self.dut,
                                         writeable_registers=NodeIterators('test_reg','regB',),
                                         readable_registers=NodeIterators('test_reg','regB',),
                                         sections=NodeIterators('endpoint1','endpoint2','switch1','switch2',),
                                         memories=NodeIterators())
        


        # test all the address maps
        with self.subTest(msg='addrmap: openenoc_csr.endpoint1'):
            self._single_addrmap_property_test(dut=self.dut.endpoint1,
                                               size=2048,
                                               rdl_name="csr.endpoint1",
                                               rdl_desc="Control and status register map for an openENOC Endpoint Interface instance.",
                                               inst_name='endpoint1',
                                               parent_full_inst_name='openenoc_csr')
            self._test_addrmap_iterators(dut=self.dut.endpoint1,
                                         writeable_registers=NodeIterators(),
                                         readable_registers=NodeIterators('info',),
                                         sections=NodeIterators('config','peers',),
                                         memories=NodeIterators('rmem',))
        with self.subTest(msg='addrmap: openenoc_csr.endpoint2'):
            self._single_addrmap_property_test(dut=self.dut.endpoint2,
                                               size=1024,
                                               rdl_name="csr.endpoint2",
                                               rdl_desc="Control and status register map for an openENOC Endpoint Interface instance.",
                                               inst_name='endpoint2',
                                               parent_full_inst_name='openenoc_csr')
            self._test_addrmap_iterators(dut=self.dut.endpoint2,
                                         writeable_registers=NodeIterators(),
                                         readable_registers=NodeIterators('info',),
                                         sections=NodeIterators('config','peers',),
                                         memories=NodeIterators('rmem',))
        with self.subTest(msg='addrmap: openenoc_csr.switch1'):
            self._single_addrmap_property_test(dut=self.dut.switch1,
                                               size=256,
                                               rdl_name="csr.switch1",
                                               rdl_desc="Control and status register map for an openENOC Switch instance. It includes configuration registers and a forwarding table used to map destination MAC address keys to output interface selections for frame forwarding.",
                                               inst_name='switch1',
                                               parent_full_inst_name='openenoc_csr')
            self._test_addrmap_iterators(dut=self.dut.switch1,
                                         writeable_registers=NodeIterators('forwarding_control','default_forwarding',),
                                         readable_registers=NodeIterators('info','forwarding_control','default_forwarding',),
                                         sections=NodeIterators('forwarding_table',),
                                         memories=NodeIterators())
        with self.subTest(msg='addrmap: openenoc_csr.switch2'):
            self._single_addrmap_property_test(dut=self.dut.switch2,
                                               size=1024,
                                               rdl_name="csr.switch2",
                                               rdl_desc="Control and status register map for an openENOC Switch instance. It includes configuration registers and a forwarding table used to map destination MAC address keys to output interface selections for frame forwarding.",
                                               inst_name='switch2',
                                               parent_full_inst_name='openenoc_csr')
            self._test_addrmap_iterators(dut=self.dut.switch2,
                                         writeable_registers=NodeIterators('forwarding_control','default_forwarding',),
                                         readable_registers=NodeIterators('info','forwarding_control','default_forwarding',),
                                         sections=NodeIterators('forwarding_table',),
                                         memories=NodeIterators())
        

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
        



class openenoc_csr_block_access(openenoc_csr_TestCase_BlockAccess): # type: ignore[valid-type,misc]
    """
    tests for all the block access methods
    """

    

    def test_register_array_context_manager(self) -> None:
        """
        Walk the register map and check that register map context managers work correctly
        """
        

class openenoc_csr_alt_block_access(openenoc_csr_TestCase_AltBlockAccess): # type: ignore[valid-type,misc]
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