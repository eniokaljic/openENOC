


"""
Unit Tests for the openenoc_csr register model Python Wrapper

This code was generated from the PeakRDL-python package version 3.1.2
"""








from typing import Union, cast

import unittest
from unittest.mock import Mock

import random


from ..sim_lib.register import Register,MemoryRegister
from ..sim_lib.field import ReadOnlyField, WriteOnlyField, ReadWriteField

from ._openenoc_csr_sim_test_base import openenoc_csr_SimTestCase_BlockAccess
from ._openenoc_csr_sim_test_base import __name__ as base_name
from ._openenoc_csr_test_base import random_enum_reg_value


from ..lib import SystemRDLEnum


from ..lib_test import reverse_bits

class openenoc_csr_endpoint2_block_access(openenoc_csr_SimTestCase_BlockAccess): # type: ignore[valid-type,misc]
    """
    tests for all the block access methods
    """

    
    def test_memory_read_and_write(self) -> None:
        """
        Walk the register map and check every register can be read and written to correctly
        """
        # test access operations (read and/or write) to register:
        # openenoc_csr.endpoint2.rmem

        # checks single unit accesses at the first entry, the last entry and a random entry in
        # in each case check a 0, max value and random value being read
        for entry in [0, random.randint(0,127), 127]:

            self.assertEqual(self.dut.endpoint2.rmem.read(start_entry=entry, number_entries=1), # type: ignore[union-attr]
                                                     [0])

        # check a multi-entry read, if the memory is small do the entire memory, however, if
        # it is large limit the number of entries to 10
        entries_to_test = 10
        
        self.assertEqual(self.dut.endpoint2.rmem.read(start_entry=0, # type: ignore[union-attr]
                                      number_entries=entries_to_test),
                                      [0 for _ in range(entries_to_test)])
        
        

        # checks single unit accesses at the first entry, the last entry and a random entry in
        # in each case check a 0, max value and random value being read
        for entry in [0, random.randint(0,127), 127]:
            for value in [0, random.randint(0,0xFFFFFFFF), 0xFFFFFFFF]:
                self.dut.endpoint2.rmem.write(start_entry=entry, data=[value]) # type: ignore[union-attr]
                self.assertEqual(self.dut.endpoint2.rmem.read(start_entry=entry, number_entries=1), # type: ignore[union-attr]
                                 [value])
                

        # check a multi-entry read, if the memory is small do the entire memory, however, if
        # it is large limit the number of entries to 10
        entries_to_test = 10
        
        random_data = [random.randint(0,0xFFFFFFFF) for x in range(entries_to_test)]
        
        self.dut.endpoint2.rmem.write(start_entry=0, data=random_data) # type: ignore[union-attr]
        self.assertEqual(self.dut.endpoint2.rmem.read(start_entry=0, number_entries=entries_to_test), # type: ignore[union-attr]
                         random_data)
        

if __name__ == '__main__':

    unittest.main()




