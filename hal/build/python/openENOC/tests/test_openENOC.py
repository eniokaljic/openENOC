


"""
Unit Tests for the openENOC register model Python Wrapper

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
from ..reg_model.openENOC_property_enums import *


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

from ._openENOC_test_base import openENOC_TestCase, openENOC_TestCase_BlockAccess, openENOC_TestCase_AltBlockAccess
from ._openENOC_test_base import __name__ as base_name
from ._openENOC_test_base import random_enum_reg_value




class openENOC_single_access(openENOC_TestCase): # type: ignore[valid-type,misc]



    def test_user_defined_properties(self)  -> None:
        """
        Walk the address map and check user defined properties are correctly pulled up
        """
        with self.subTest(msg='register: openENOC.csr'):
            
            
            self.assertDictEqual(self.dut.csr.udp,{})
            
        with self.subTest(msg='register: openENOC.imem'):
            
            
            self.assertDictEqual(self.dut.imem.udp,{})
            
        with self.subTest(msg='register: openENOC.dmem'):
            
            
            self.assertDictEqual(self.dut.dmem.udp,{})
            
        

    
    def test_memory(self) -> None:
        """
        Walk the memory instances in the register map and check:
        - the properties
        - it can be read and written to correctly
        """
        with self.subTest(msg='memory: openENOC.imem'):
            self._single_memory_property_test(mut=self.dut.imem, address=0, width=32, entries=8192, accesswidth=None, array_typecode=None, size=32768,
                                              rdl_name="imem",
                                              rdl_desc="CPU Program Memory",
                                              inst_name='imem',
                                              parent_full_inst_name='openENOC')
            self._single_memory_read_and_write_test(mut=self.dut.imem, is_sw_readable=True, is_sw_writable=True,
                                                                                        writeable_registers=NodeIterators(),
                                                                                        readable_registers=NodeIterators())
        with self.subTest(msg='memory: openENOC.dmem'):
            self._single_memory_property_test(mut=self.dut.dmem, address=268435456, width=32, entries=8192, accesswidth=None, array_typecode=None, size=32768,
                                              rdl_name="dmem",
                                              rdl_desc="CPU Data Memory",
                                              inst_name='dmem',
                                              parent_full_inst_name='openENOC')
            self._single_memory_read_and_write_test(mut=self.dut.dmem, is_sw_readable=True, is_sw_writable=True,
                                                                                        writeable_registers=NodeIterators(),
                                                                                        readable_registers=NodeIterators())
        
     

    def test_register(self) -> None:
        """
        Walk the registers in the register map and check:
        - the properties
        - it can be read and written to correctly
        """
        

    def test_field(self) -> None:
        """
        Check the properties and function (read and write) on the fields both integer and enum
        """
        

    def test_addrmap(self) -> None:
        """
        Check the properties on the addrmaps files
        """

        
        with self.subTest(msg='addrmap: top_node'):
            self._single_addrmap_property_test(dut=self.dut,
                                               size=536870916,
                                               rdl_name=None,
                                               rdl_desc=None,
                                               inst_name='openENOC',
                                               parent_full_inst_name=None)
            self._test_addrmap_iterators(dut=self.dut,
                                         writeable_registers=NodeIterators(),
                                         readable_registers=NodeIterators(),
                                         sections=NodeIterators('csr',),
                                         memories=NodeIterators('imem','dmem',))
        


        # test all the address maps
        with self.subTest(msg='addrmap: openENOC.csr'):
            self._single_addrmap_property_test(dut=self.dut.csr,
                                               size=4,
                                               rdl_name="csr",
                                               rdl_desc="openENOC CSR",
                                               inst_name='csr',
                                               parent_full_inst_name='openENOC')
            self._test_addrmap_iterators(dut=self.dut.csr,
                                         writeable_registers=NodeIterators('test_reg',),
                                         readable_registers=NodeIterators('test_reg',),
                                         sections=NodeIterators(),
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
        



class openENOC_block_access(openENOC_TestCase_BlockAccess): # type: ignore[valid-type,misc]
    """
    tests for all the block access methods
    """

    
    def test_memory_read_and_write(self) -> None:
        """
        Walk the register map and check every register can be read and written to correctly
        """
        # test access operations (read and/or write) to register:
        # openENOC.imem
        with patch(base_name + '.write_addr_space') as write_callback_mock,\
                            patch(base_name + '.read_addr_space', return_value=1) as read_callback_mock, \
                            patch(base_name + '.read_block_addr_space',
                                  return_value=[0]) as read_block_callback_mock , \
                            patch(base_name + '.write_block_addr_space') as write_block_callback_mock:

            # checks single unit accesses at the first entry, the last entry and a random entry in
            # in each case check a 0, max value and random value being read
            for entry in [0, random.randint(0,8191), 8191]:
                for value in [0, random.randint(0,0xFFFFFFFF), 0xFFFFFFFF]:
                    read_block_callback_mock.reset_mock()
                    
                    read_block_callback_mock.return_value = [value]
                    

                    
                    self.assertEqual(self.dut.imem.read(start_entry=entry, number_entries=1), # type: ignore[union-attr]
                                                             [value])
                    
                    read_block_callback_mock.assert_called_once_with(
                                        addr=0+(entry * 4),
                                        width=32,
                                        accesswidth=32,
                                        length=1)

            # check a multi-entry read, if the memory is small do the entire memory, however, if
            # it is large limit the number of entries to 10
            entries_to_test = 10
            
            random_data = [random.randint(0,0xFFFFFFFF) for x in range(entries_to_test)]
            


            read_block_callback_mock.reset_mock()
            read_block_callback_mock.return_value = random_data

            self.assertEqual(self.dut.imem.read(start_entry=0, # type: ignore[union-attr]
                                          number_entries=entries_to_test),
                                          random_data)

            write_callback_mock.assert_not_called()
            read_callback_mock.assert_not_called()
            write_block_callback_mock.assert_not_called()
            read_block_callback_mock.reset_mock()
            

            # checks single unit accesses at the first entry, the last entry and a random entry in
            # in each case check a 0, max value and random value being read
            for entry in [0, random.randint(0,8191), 8191]:
                for value in [0, random.randint(0,0xFFFFFFFF), 0xFFFFFFFF]:
                    write_block_callback_mock.reset_mock()
                    
                    self.dut.imem.write(start_entry=entry, data=[value]) # type: ignore[union-attr]
                    write_block_callback_mock.assert_called_once_with(
                                        addr=0+(entry * 4),
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
            
            self.dut.imem.write(start_entry=0, data=random_data) # type: ignore[union-attr]

            write_block_callback_mock.assert_called_once_with(
                                        addr=0,
                                        width=32,
                                        accesswidth=32,
                                        data=random_data)

            read_callback_mock.assert_not_called()
            write_callback_mock.assert_not_called()
            read_block_callback_mock.assert_not_called()
            write_block_callback_mock.reset_mock()# test access operations (read and/or write) to register:
        # openENOC.dmem
        with patch(base_name + '.write_addr_space') as write_callback_mock,\
                            patch(base_name + '.read_addr_space', return_value=1) as read_callback_mock, \
                            patch(base_name + '.read_block_addr_space',
                                  return_value=[0]) as read_block_callback_mock , \
                            patch(base_name + '.write_block_addr_space') as write_block_callback_mock:

            # checks single unit accesses at the first entry, the last entry and a random entry in
            # in each case check a 0, max value and random value being read
            for entry in [0, random.randint(0,8191), 8191]:
                for value in [0, random.randint(0,0xFFFFFFFF), 0xFFFFFFFF]:
                    read_block_callback_mock.reset_mock()
                    
                    read_block_callback_mock.return_value = [value]
                    

                    
                    self.assertEqual(self.dut.dmem.read(start_entry=entry, number_entries=1), # type: ignore[union-attr]
                                                             [value])
                    
                    read_block_callback_mock.assert_called_once_with(
                                        addr=268435456+(entry * 4),
                                        width=32,
                                        accesswidth=32,
                                        length=1)

            # check a multi-entry read, if the memory is small do the entire memory, however, if
            # it is large limit the number of entries to 10
            entries_to_test = 10
            
            random_data = [random.randint(0,0xFFFFFFFF) for x in range(entries_to_test)]
            


            read_block_callback_mock.reset_mock()
            read_block_callback_mock.return_value = random_data

            self.assertEqual(self.dut.dmem.read(start_entry=0, # type: ignore[union-attr]
                                          number_entries=entries_to_test),
                                          random_data)

            write_callback_mock.assert_not_called()
            read_callback_mock.assert_not_called()
            write_block_callback_mock.assert_not_called()
            read_block_callback_mock.reset_mock()
            

            # checks single unit accesses at the first entry, the last entry and a random entry in
            # in each case check a 0, max value and random value being read
            for entry in [0, random.randint(0,8191), 8191]:
                for value in [0, random.randint(0,0xFFFFFFFF), 0xFFFFFFFF]:
                    write_block_callback_mock.reset_mock()
                    
                    self.dut.dmem.write(start_entry=entry, data=[value]) # type: ignore[union-attr]
                    write_block_callback_mock.assert_called_once_with(
                                        addr=268435456+(entry * 4),
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
            
            self.dut.dmem.write(start_entry=0, data=random_data) # type: ignore[union-attr]

            write_block_callback_mock.assert_called_once_with(
                                        addr=268435456,
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
        

class openENOC_alt_block_access(openENOC_TestCase_AltBlockAccess): # type: ignore[valid-type,misc]
    """
    tests for all the block access methods with the alternative callbacks, this is a simpler
    version of the tests above
    """
    
    def test_memory_read_and_write(self) -> None:
        """
        Walk the register map and check every register can be read and written to correctly
        """
        # test access operations (read and/or write) to register:
        # openENOC.imem
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
            self.assertEqual(self.dut.imem.read(start_entry=0, # type: ignore[union-attr]
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
            self.dut.imem.write(start_entry=0, data=random_data_list) # type: ignore[union-attr]

            write_block_callback_mock.assert_called_once_with(
                                        addr=0,
                                        width=32,
                                        accesswidth=32,
                                        data=random_data_array)

            read_callback_mock.assert_not_called()
            write_callback_mock.assert_not_called()
            read_block_callback_mock.assert_not_called()
            write_block_callback_mock.reset_mock()
        # test access operations (read and/or write) to register:
        # openENOC.dmem
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
            self.assertEqual(self.dut.dmem.read(start_entry=0, # type: ignore[union-attr]
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
            self.dut.dmem.write(start_entry=0, data=random_data_list) # type: ignore[union-attr]

            write_block_callback_mock.assert_called_once_with(
                                        addr=268435456,
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