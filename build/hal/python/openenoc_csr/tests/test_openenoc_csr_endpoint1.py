


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




class openenoc_csr_endpoint1_single_access(openenoc_csr_TestCase): # type: ignore[valid-type,misc]



    def test_user_defined_properties(self)  -> None:
        """
        Walk the address map and check user defined properties are correctly pulled up
        """
        with self.subTest(msg='register: openenoc_csr.endpoint1.rmem'):
            
            
            self.assertDictEqual(self.dut.endpoint1.rmem.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.info'):
            
            
            self.assertDictEqual(self.dut.endpoint1.info.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.info.placeholder'):
            
            
            self.assertDictEqual(self.dut.endpoint1.info.placeholder.udp,{})
            
        

    
    def test_memory(self) -> None:
        """
        Walk the memory instances in the register map and check:
        - the properties
        - it can be read and written to correctly
        """
        with self.subTest(msg='memory: openenoc_csr.endpoint1.rmem'):
            self._single_memory_property_test(mut=self.dut.endpoint1.rmem, address=3072, width=32, entries=256, accesswidth=None, array_typecode=None, size=1024,
                                              rdl_name="rmem",
                                              rdl_desc="Remote Memory",
                                              inst_name='rmem',
                                              parent_full_inst_name='openenoc_csr.endpoint1')
            self._single_memory_read_and_write_test(mut=self.dut.endpoint1.rmem, is_sw_readable=True, is_sw_writable=True,
                                                                                        writeable_registers=NodeIterators(),
                                                                                        readable_registers=NodeIterators())
        
     

    def test_register(self) -> None:
        """
        Walk the registers in the register map and check:
        - the properties
        - it can be read and written to correctly
        """
        with self.subTest(msg='register: openenoc_csr.endpoint1.info'):
            self._single_register_property_test(rut=self.dut.endpoint1.info, address=2048, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint1.info",
                                                rdl_desc="Read-only information register for this openENOC Endpoint Interface instance.",
                                                inst_name='info',
                                                parent_full_inst_name='openenoc_csr.endpoint1')
            self._single_register_read_and_write_test(rut=self.dut.endpoint1.info, has_sw_readable=True, has_sw_writable=False,
                                                                                          readable_fields=set(['placeholder', ]),
                                                                                          writeable_fields=set([ ]) )
        

    def test_field(self) -> None:
        """
        Check the properties and function (read and write) on the fields both integer and enum
        """
        
        with self.subTest(msg='field: openenoc_csr.endpoint1.info.placeholder'):
            self._single_field_property_test(fut=self.dut.endpoint1.info.placeholder, lsb=0, msb=31, low=0, high=31, is_volatile=False, default=None,
                                             rdl_name="csr.endpoint1.info.placeholder[31:0]",
                                             rdl_desc="Placeholder field for this openENOC Endpoint Interface instance.",
                                             inst_name='placeholder',
                                             parent_full_inst_name='openenoc_csr.endpoint1.info')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint1.info.placeholder, is_sw_readable=True, is_sw_writable=False)

    def test_addrmap(self) -> None:
        """
        Check the properties on the addrmaps files
        """

        


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
        



class openenoc_csr_endpoint1_block_access(openenoc_csr_TestCase_BlockAccess): # type: ignore[valid-type,misc]
    """
    tests for all the block access methods
    """

    
    def test_memory_read_and_write(self) -> None:
        """
        Walk the register map and check every register can be read and written to correctly
        """
        # test access operations (read and/or write) to register:
        # openenoc_csr.endpoint1.rmem
        with patch(base_name + '.write_addr_space') as write_callback_mock,\
                            patch(base_name + '.read_addr_space', return_value=1) as read_callback_mock, \
                            patch(base_name + '.read_block_addr_space',
                                  return_value=[0]) as read_block_callback_mock , \
                            patch(base_name + '.write_block_addr_space') as write_block_callback_mock:

            # checks single unit accesses at the first entry, the last entry and a random entry in
            # in each case check a 0, max value and random value being read
            for entry in [0, random.randint(0,255), 255]:
                for value in [0, random.randint(0,0xFFFFFFFF), 0xFFFFFFFF]:
                    read_block_callback_mock.reset_mock()
                    
                    read_block_callback_mock.return_value = [value]
                    

                    
                    self.assertEqual(self.dut.endpoint1.rmem.read(start_entry=entry, number_entries=1), # type: ignore[union-attr]
                                                             [value])
                    
                    read_block_callback_mock.assert_called_once_with(
                                        addr=3072+(entry * 4),
                                        width=32,
                                        accesswidth=32,
                                        length=1)

            # check a multi-entry read, if the memory is small do the entire memory, however, if
            # it is large limit the number of entries to 10
            entries_to_test = 10
            
            random_data = [random.randint(0,0xFFFFFFFF) for x in range(entries_to_test)]
            


            read_block_callback_mock.reset_mock()
            read_block_callback_mock.return_value = random_data

            self.assertEqual(self.dut.endpoint1.rmem.read(start_entry=0, # type: ignore[union-attr]
                                          number_entries=entries_to_test),
                                          random_data)

            write_callback_mock.assert_not_called()
            read_callback_mock.assert_not_called()
            write_block_callback_mock.assert_not_called()
            read_block_callback_mock.reset_mock()
            

            # checks single unit accesses at the first entry, the last entry and a random entry in
            # in each case check a 0, max value and random value being read
            for entry in [0, random.randint(0,255), 255]:
                for value in [0, random.randint(0,0xFFFFFFFF), 0xFFFFFFFF]:
                    write_block_callback_mock.reset_mock()
                    
                    self.dut.endpoint1.rmem.write(start_entry=entry, data=[value]) # type: ignore[union-attr]
                    write_block_callback_mock.assert_called_once_with(
                                        addr=3072+(entry * 4),
                                        width=32,
                                        accesswidth=32,
                                        data=[value])
                    


            read_callback_mock.assert_not_called()
            write_callback_mock.assert_not_called()
            read_block_callback_mock.assert_not_called()
            write_block_callback_mock.reset_mock()

            # check a multi-entry read, if the memory is small do the entire memory, however, if
            # it is large limit the number of entries to 10
            entries_to_test = 10
            
            random_data = [random.randint(0,0xFFFFFFFF) for x in range(entries_to_test)]
            
            self.dut.endpoint1.rmem.write(start_entry=0, data=random_data) # type: ignore[union-attr]

            write_block_callback_mock.assert_called_once_with(
                                        addr=3072,
                                        width=32,
                                        accesswidth=32,
                                        data=random_data)

            read_callback_mock.assert_not_called()
            write_callback_mock.assert_not_called()
            read_block_callback_mock.assert_not_called()
            write_block_callback_mock.reset_mock()

    def test_register_array_context_manager(self) -> None:
        """
        Walk the register map and check that register map context managers work correctly
        """
        

class openenoc_csr_endpoint1_alt_block_access(openenoc_csr_TestCase_AltBlockAccess): # type: ignore[valid-type,misc]
    """
    tests for all the block access methods with the alternative callbacks, this is a simpler
    version of the tests above
    """
    
    def test_memory_read_and_write(self) -> None:
        """
        Walk the register map and check every register can be read and written to correctly
        """
        # test access operations (read and/or write) to register:
        # openenoc_csr.endpoint1.rmem
        entries_to_test = 10
        
        with patch(base_name + '.write_addr_space') as write_callback_mock,\
                            patch(base_name + '.read_addr_space', return_value=1) as read_callback_mock, \
                            patch(base_name + '.read_block_addr_space_alt',
                                  return_value=Array('L', [0])) as read_block_callback_mock , \
                            patch(base_name + '.write_block_addr_space_alt') as write_block_callback_mock:

            random_data_list = [random.randint(0,0xFFFFFFFF) for x in range(entries_to_test)]
            random_data_array = Array('L', random_data_list)

            read_block_callback_mock.reset_mock()
            
            read_block_callback_mock.return_value = random_data_array
            self.assertEqual(self.dut.endpoint1.rmem.read(start_entry=0, # type: ignore[union-attr]
                                          number_entries=entries_to_test),
                                          random_data_list)
            

            write_callback_mock.assert_not_called()
            read_callback_mock.assert_not_called()
            write_block_callback_mock.assert_not_called()
            read_block_callback_mock.reset_mock()
            

            # check a multi-entry read, if the memory is small do the entire memory, however, if
            # it is large limit the number of entries to 10
            entries_to_test = 10
            random_data_list = [random.randint(0,0xFFFFFFFF) for x in range(entries_to_test)]
            random_data_array = Array('L', random_data_list)
            self.dut.endpoint1.rmem.write(start_entry=0, data=random_data_list) # type: ignore[union-attr]

            write_block_callback_mock.assert_called_once_with(
                                        addr=3072,
                                        width=32,
                                        accesswidth=32,
                                        data=random_data_array)

            read_callback_mock.assert_not_called()
            write_callback_mock.assert_not_called()
            read_block_callback_mock.assert_not_called()
            write_block_callback_mock.reset_mock()
        

    def test_register_array_context_manager(self) -> None:
        """
        Walk the register map and check that register map context managers work correctly
        """
        


if __name__ == '__main__':

    unittest.main()