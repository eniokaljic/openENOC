


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




class openenoc_csr_endpoint2_single_access(openenoc_csr_TestCase): # type: ignore[valid-type,misc]



    def test_user_defined_properties(self)  -> None:
        """
        Walk the address map and check user defined properties are correctly pulled up
        """
        with self.subTest(msg='register: openenoc_csr.endpoint2.config'):
            
            
            self.assertDictEqual(self.dut.endpoint2.config.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint2.peers'):
            
            
            self.assertDictEqual(self.dut.endpoint2.peers.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint2.peers.entry[0]'):
            
            
            self.assertDictEqual(self.dut.endpoint2.peers.entry[0].udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint2.peers.entry[1]'):
            
            
            self.assertDictEqual(self.dut.endpoint2.peers.entry[1].udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint2.rmem'):
            
            
            self.assertDictEqual(self.dut.endpoint2.rmem.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint2.info'):
            
            
            self.assertDictEqual(self.dut.endpoint2.info.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint2.config.mac_address'):
            
            
            self.assertDictEqual(self.dut.endpoint2.config.mac_address.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint2.peers.entry[0].mac_address'):
            
            
            self.assertDictEqual(self.dut.endpoint2.peers.entry[0].mac_address.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint2.peers.entry[0].rmem_address'):
            
            
            self.assertDictEqual(self.dut.endpoint2.peers.entry[0].rmem_address.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint2.peers.entry[0].local_address'):
            
            
            self.assertDictEqual(self.dut.endpoint2.peers.entry[0].local_address.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint2.peers.entry[0].remote_address'):
            
            
            self.assertDictEqual(self.dut.endpoint2.peers.entry[0].remote_address.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint2.peers.entry[0].size'):
            
            
            self.assertDictEqual(self.dut.endpoint2.peers.entry[0].register_size.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint2.peers.entry[0].dma_config'):
            
            
            self.assertDictEqual(self.dut.endpoint2.peers.entry[0].dma_config.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint2.peers.entry[1].mac_address'):
            
            
            self.assertDictEqual(self.dut.endpoint2.peers.entry[1].mac_address.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint2.peers.entry[1].rmem_address'):
            
            
            self.assertDictEqual(self.dut.endpoint2.peers.entry[1].rmem_address.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint2.peers.entry[1].local_address'):
            
            
            self.assertDictEqual(self.dut.endpoint2.peers.entry[1].local_address.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint2.peers.entry[1].remote_address'):
            
            
            self.assertDictEqual(self.dut.endpoint2.peers.entry[1].remote_address.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint2.peers.entry[1].size'):
            
            
            self.assertDictEqual(self.dut.endpoint2.peers.entry[1].register_size.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint2.peers.entry[1].dma_config'):
            
            
            self.assertDictEqual(self.dut.endpoint2.peers.entry[1].dma_config.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint2.info.rmem_total_depth'):
            
            
            self.assertDictEqual(self.dut.endpoint2.info.rmem_total_depth.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint2.info.num_of_peers'):
            
            
            self.assertDictEqual(self.dut.endpoint2.info.num_of_peers.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint2.config.mac_address.lo_word'):
            
            
            self.assertDictEqual(self.dut.endpoint2.config.mac_address.lo_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint2.config.mac_address.hi_word'):
            
            
            self.assertDictEqual(self.dut.endpoint2.config.mac_address.hi_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint2.peers.entry[0].mac_address.lo_word'):
            
            
            self.assertDictEqual(self.dut.endpoint2.peers.entry[0].mac_address.lo_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint2.peers.entry[0].mac_address.hi_word'):
            
            
            self.assertDictEqual(self.dut.endpoint2.peers.entry[0].mac_address.hi_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint2.peers.entry[0].rmem_address.offset'):
            
            
            self.assertDictEqual(self.dut.endpoint2.peers.entry[0].rmem_address.offset.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint2.peers.entry[0].local_address.base'):
            
            
            self.assertDictEqual(self.dut.endpoint2.peers.entry[0].local_address.base.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint2.peers.entry[0].remote_address.base'):
            
            
            self.assertDictEqual(self.dut.endpoint2.peers.entry[0].remote_address.base.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint2.peers.entry[0].size.value'):
            
            
            self.assertDictEqual(self.dut.endpoint2.peers.entry[0].register_size.value.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint2.peers.entry[0].dma_config.mode'):
            
            
            self.assertDictEqual(self.dut.endpoint2.peers.entry[0].dma_config.mode.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint2.peers.entry[1].mac_address.lo_word'):
            
            
            self.assertDictEqual(self.dut.endpoint2.peers.entry[1].mac_address.lo_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint2.peers.entry[1].mac_address.hi_word'):
            
            
            self.assertDictEqual(self.dut.endpoint2.peers.entry[1].mac_address.hi_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint2.peers.entry[1].rmem_address.offset'):
            
            
            self.assertDictEqual(self.dut.endpoint2.peers.entry[1].rmem_address.offset.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint2.peers.entry[1].local_address.base'):
            
            
            self.assertDictEqual(self.dut.endpoint2.peers.entry[1].local_address.base.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint2.peers.entry[1].remote_address.base'):
            
            
            self.assertDictEqual(self.dut.endpoint2.peers.entry[1].remote_address.base.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint2.peers.entry[1].size.value'):
            
            
            self.assertDictEqual(self.dut.endpoint2.peers.entry[1].register_size.value.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint2.peers.entry[1].dma_config.mode'):
            
            
            self.assertDictEqual(self.dut.endpoint2.peers.entry[1].dma_config.mode.udp,{})
            
        

    
    def test_memory(self) -> None:
        """
        Walk the memory instances in the register map and check:
        - the properties
        - it can be read and written to correctly
        """
        with self.subTest(msg='memory: openenoc_csr.endpoint2.rmem'):
            self._single_memory_property_test(mut=self.dut.endpoint2.rmem, address=4608, width=32, entries=128, accesswidth=None, array_typecode=None, size=512,
                                              rdl_name="rmem",
                                              rdl_desc="Virtual memory region for all remote peers, with offsets and sizes defined in the peers regfile.",
                                              inst_name='rmem',
                                              parent_full_inst_name='openenoc_csr.endpoint2')
            self._single_memory_read_and_write_test(mut=self.dut.endpoint2.rmem, is_sw_readable=True, is_sw_writable=True,
                                                                                        writeable_registers=NodeIterators(),
                                                                                        readable_registers=NodeIterators())
        
     

    def test_register(self) -> None:
        """
        Walk the registers in the register map and check:
        - the properties
        - it can be read and written to correctly
        """
        with self.subTest(msg='register: openenoc_csr.endpoint2.info'):
            self._single_register_property_test(rut=self.dut.endpoint2.info, address=4096, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint2.info",
                                                rdl_desc="Read-only information register for this openENOC Endpoint Interface instance.",
                                                inst_name='info',
                                                parent_full_inst_name='openenoc_csr.endpoint2')
            self._single_register_read_and_write_test(rut=self.dut.endpoint2.info, has_sw_readable=True, has_sw_writable=False,
                                                                                          readable_fields=set(['rmem_total_depth','num_of_peers', ]),
                                                                                          writeable_fields=set([ ]) )
        with self.subTest(msg='register: openenoc_csr.endpoint2.config.mac_address'):
            self._single_register_property_test(rut=self.dut.endpoint2.config.mac_address, address=4104, width=64, accesswidth=32, size=8,
                                                rdl_name="csr.endpoint2.config.mac_address",
                                                rdl_desc="Local site 48-bit destination MAC address.",
                                                inst_name='mac_address',
                                                parent_full_inst_name='openenoc_csr.endpoint2.config')
            self._single_register_read_and_write_test(rut=self.dut.endpoint2.config.mac_address, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['lo_word','hi_word', ]),
                                                                                          writeable_fields=set(['lo_word','hi_word', ]) )
        with self.subTest(msg='register: openenoc_csr.endpoint2.peers.entry[0].mac_address'):
            self._single_register_property_test(rut=self.dut.endpoint2.peers.entry[0].mac_address, address=4160, width=64, accesswidth=32, size=8,
                                                rdl_name="csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].mac_address",
                                                rdl_desc="Remote peer 48-bit destination MAC address.",
                                                inst_name='mac_address',
                                                parent_full_inst_name='openenoc_csr.endpoint2.peers.entry[0]')
            self._single_register_read_and_write_test(rut=self.dut.endpoint2.peers.entry[0].mac_address, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['lo_word','hi_word', ]),
                                                                                          writeable_fields=set(['lo_word','hi_word', ]) )
        with self.subTest(msg='register: openenoc_csr.endpoint2.peers.entry[0].rmem_address'):
            self._single_register_property_test(rut=self.dut.endpoint2.peers.entry[0].rmem_address, address=4168, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].rmem_address",
                                                rdl_desc="Address offset of the virtual memory region corresponding to the remote peer\u0027s memory.",
                                                inst_name='rmem_address',
                                                parent_full_inst_name='openenoc_csr.endpoint2.peers.entry[0]')
            self._single_register_read_and_write_test(rut=self.dut.endpoint2.peers.entry[0].rmem_address, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['offset', ]),
                                                                                          writeable_fields=set(['offset', ]) )
        with self.subTest(msg='register: openenoc_csr.endpoint2.peers.entry[0].local_address'):
            self._single_register_property_test(rut=self.dut.endpoint2.peers.entry[0].local_address, address=4172, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].local_address",
                                                rdl_desc="Start address of the local memory region for DMA transfers.",
                                                inst_name='local_address',
                                                parent_full_inst_name='openenoc_csr.endpoint2.peers.entry[0]')
            self._single_register_read_and_write_test(rut=self.dut.endpoint2.peers.entry[0].local_address, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['base', ]),
                                                                                          writeable_fields=set(['base', ]) )
        with self.subTest(msg='register: openenoc_csr.endpoint2.peers.entry[0].remote_address'):
            self._single_register_property_test(rut=self.dut.endpoint2.peers.entry[0].remote_address, address=4176, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].remote_address",
                                                rdl_desc="Start address of the remote peer\u0027s memory region.",
                                                inst_name='remote_address',
                                                parent_full_inst_name='openenoc_csr.endpoint2.peers.entry[0]')
            self._single_register_read_and_write_test(rut=self.dut.endpoint2.peers.entry[0].remote_address, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['base', ]),
                                                                                          writeable_fields=set(['base', ]) )
        with self.subTest(msg='register: openenoc_csr.endpoint2.peers.entry[0].size'):
            self._single_register_property_test(rut=self.dut.endpoint2.peers.entry[0].register_size, address=4180, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].size",
                                                rdl_desc="Size of the remote peer\u0027s memory region.",
                                                inst_name='size',
                                                parent_full_inst_name='openenoc_csr.endpoint2.peers.entry[0]')
            self._single_register_read_and_write_test(rut=self.dut.endpoint2.peers.entry[0].register_size, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['value', ]),
                                                                                          writeable_fields=set(['value', ]) )
        with self.subTest(msg='register: openenoc_csr.endpoint2.peers.entry[0].dma_config'):
            self._single_register_property_test(rut=self.dut.endpoint2.peers.entry[0].dma_config, address=4184, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].dma_config",
                                                rdl_desc="DMA configuration for the remote peer.",
                                                inst_name='dma_config',
                                                parent_full_inst_name='openenoc_csr.endpoint2.peers.entry[0]')
            self._single_register_read_and_write_test(rut=self.dut.endpoint2.peers.entry[0].dma_config, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['mode', ]),
                                                                                          writeable_fields=set(['mode', ]) )
        with self.subTest(msg='register: openenoc_csr.endpoint2.peers.entry[1].mac_address'):
            self._single_register_property_test(rut=self.dut.endpoint2.peers.entry[1].mac_address, address=4188, width=64, accesswidth=32, size=8,
                                                rdl_name="csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].mac_address",
                                                rdl_desc="Remote peer 48-bit destination MAC address.",
                                                inst_name='mac_address',
                                                parent_full_inst_name='openenoc_csr.endpoint2.peers.entry[1]')
            self._single_register_read_and_write_test(rut=self.dut.endpoint2.peers.entry[1].mac_address, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['lo_word','hi_word', ]),
                                                                                          writeable_fields=set(['lo_word','hi_word', ]) )
        with self.subTest(msg='register: openenoc_csr.endpoint2.peers.entry[1].rmem_address'):
            self._single_register_property_test(rut=self.dut.endpoint2.peers.entry[1].rmem_address, address=4196, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].rmem_address",
                                                rdl_desc="Address offset of the virtual memory region corresponding to the remote peer\u0027s memory.",
                                                inst_name='rmem_address',
                                                parent_full_inst_name='openenoc_csr.endpoint2.peers.entry[1]')
            self._single_register_read_and_write_test(rut=self.dut.endpoint2.peers.entry[1].rmem_address, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['offset', ]),
                                                                                          writeable_fields=set(['offset', ]) )
        with self.subTest(msg='register: openenoc_csr.endpoint2.peers.entry[1].local_address'):
            self._single_register_property_test(rut=self.dut.endpoint2.peers.entry[1].local_address, address=4200, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].local_address",
                                                rdl_desc="Start address of the local memory region for DMA transfers.",
                                                inst_name='local_address',
                                                parent_full_inst_name='openenoc_csr.endpoint2.peers.entry[1]')
            self._single_register_read_and_write_test(rut=self.dut.endpoint2.peers.entry[1].local_address, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['base', ]),
                                                                                          writeable_fields=set(['base', ]) )
        with self.subTest(msg='register: openenoc_csr.endpoint2.peers.entry[1].remote_address'):
            self._single_register_property_test(rut=self.dut.endpoint2.peers.entry[1].remote_address, address=4204, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].remote_address",
                                                rdl_desc="Start address of the remote peer\u0027s memory region.",
                                                inst_name='remote_address',
                                                parent_full_inst_name='openenoc_csr.endpoint2.peers.entry[1]')
            self._single_register_read_and_write_test(rut=self.dut.endpoint2.peers.entry[1].remote_address, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['base', ]),
                                                                                          writeable_fields=set(['base', ]) )
        with self.subTest(msg='register: openenoc_csr.endpoint2.peers.entry[1].size'):
            self._single_register_property_test(rut=self.dut.endpoint2.peers.entry[1].register_size, address=4208, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].size",
                                                rdl_desc="Size of the remote peer\u0027s memory region.",
                                                inst_name='size',
                                                parent_full_inst_name='openenoc_csr.endpoint2.peers.entry[1]')
            self._single_register_read_and_write_test(rut=self.dut.endpoint2.peers.entry[1].register_size, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['value', ]),
                                                                                          writeable_fields=set(['value', ]) )
        with self.subTest(msg='register: openenoc_csr.endpoint2.peers.entry[1].dma_config'):
            self._single_register_property_test(rut=self.dut.endpoint2.peers.entry[1].dma_config, address=4212, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].dma_config",
                                                rdl_desc="DMA configuration for the remote peer.",
                                                inst_name='dma_config',
                                                parent_full_inst_name='openenoc_csr.endpoint2.peers.entry[1]')
            self._single_register_read_and_write_test(rut=self.dut.endpoint2.peers.entry[1].dma_config, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['mode', ]),
                                                                                          writeable_fields=set(['mode', ]) )
        

    def test_field(self) -> None:
        """
        Check the properties and function (read and write) on the fields both integer and enum
        """
        
        with self.subTest(msg='field: openenoc_csr.endpoint2.info.rmem_total_depth'):
            self._single_field_property_test(fut=self.dut.endpoint2.info.rmem_total_depth, lsb=0, msb=15, low=0, high=15, is_volatile=False, default=128,
                                             rdl_name="csr.endpoint2.info.rmem_total_depth[15:0]",
                                             rdl_desc="Total depth of the shared memory region for all remote peers. This field reflects the RMEM_TOTAL_DEPTH parameter value.",
                                             inst_name='rmem_total_depth',
                                             parent_full_inst_name='openenoc_csr.endpoint2.info')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint2.info.rmem_total_depth, is_sw_readable=True, is_sw_writable=False)
        with self.subTest(msg='field: openenoc_csr.endpoint2.info.num_of_peers'):
            self._single_field_property_test(fut=self.dut.endpoint2.info.num_of_peers, lsb=16, msb=31, low=16, high=31, is_volatile=False, default=2,
                                             rdl_name="csr.endpoint2.info.num_of_peers[31:16]",
                                             rdl_desc="Number of remote peers supported by this openENOC Endpoint Interface instance. This field reflects the NUM_OF_PEERS parameter value.",
                                             inst_name='num_of_peers',
                                             parent_full_inst_name='openenoc_csr.endpoint2.info')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint2.info.num_of_peers, is_sw_readable=True, is_sw_writable=False)
        with self.subTest(msg='field: openenoc_csr.endpoint2.config.mac_address.lo_word'):
            self._single_field_property_test(fut=self.dut.endpoint2.config.mac_address.lo_word, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=0,
                                             rdl_name="csr.endpoint2.config.mac_address.lo_word[31:0]",
                                             rdl_desc="Lower 32 bits [31:0] of the 48-bit MAC address.",
                                             inst_name='lo_word',
                                             parent_full_inst_name='openenoc_csr.endpoint2.config.mac_address')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint2.config.mac_address.lo_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.endpoint2.config.mac_address.hi_word'):
            self._single_field_property_test(fut=self.dut.endpoint2.config.mac_address.hi_word, lsb=32, msb=47, low=32, high=47, is_volatile=True, default=0,
                                             rdl_name="csr.endpoint2.config.mac_address.hi_word[47:32]",
                                             rdl_desc="Upper 16 bits [47:32] of the 48-bit MAC address.",
                                             inst_name='hi_word',
                                             parent_full_inst_name='openenoc_csr.endpoint2.config.mac_address')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint2.config.mac_address.hi_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.endpoint2.peers.entry[0].mac_address.lo_word'):
            self._single_field_property_test(fut=self.dut.endpoint2.peers.entry[0].mac_address.lo_word, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].mac_address.lo_word[31:0]",
                                             rdl_desc="Lower 32 bits [31:0] of the 48-bit MAC address.",
                                             inst_name='lo_word',
                                             parent_full_inst_name='openenoc_csr.endpoint2.peers.entry[0].mac_address')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint2.peers.entry[0].mac_address.lo_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.endpoint2.peers.entry[0].mac_address.hi_word'):
            self._single_field_property_test(fut=self.dut.endpoint2.peers.entry[0].mac_address.hi_word, lsb=32, msb=47, low=32, high=47, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].mac_address.hi_word[47:32]",
                                             rdl_desc="Upper 16 bits [47:32] of the 48-bit MAC address.",
                                             inst_name='hi_word',
                                             parent_full_inst_name='openenoc_csr.endpoint2.peers.entry[0].mac_address')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint2.peers.entry[0].mac_address.hi_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.endpoint2.peers.entry[0].rmem_address.offset'):
            self._single_field_property_test(fut=self.dut.endpoint2.peers.entry[0].rmem_address.offset, lsb=0, msb=31, low=0, high=31, is_volatile=False, default=None,
                                             rdl_name="csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].rmem_address.offset[31:0]",
                                             rdl_desc="32-bit address offset of the virtual memory region corresponding to the remote peer\u0027s memory.",
                                             inst_name='offset',
                                             parent_full_inst_name='openenoc_csr.endpoint2.peers.entry[0].rmem_address')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint2.peers.entry[0].rmem_address.offset, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.endpoint2.peers.entry[0].local_address.base'):
            self._single_field_property_test(fut=self.dut.endpoint2.peers.entry[0].local_address.base, lsb=0, msb=31, low=0, high=31, is_volatile=False, default=None,
                                             rdl_name="csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].local_address.base[31:0]",
                                             rdl_desc="32-bit start address of the local memory region for DMA transfers.",
                                             inst_name='base',
                                             parent_full_inst_name='openenoc_csr.endpoint2.peers.entry[0].local_address')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint2.peers.entry[0].local_address.base, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.endpoint2.peers.entry[0].remote_address.base'):
            self._single_field_property_test(fut=self.dut.endpoint2.peers.entry[0].remote_address.base, lsb=0, msb=31, low=0, high=31, is_volatile=False, default=None,
                                             rdl_name="csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].remote_address.base[31:0]",
                                             rdl_desc="32-bit start address of the remote peer\u0027s memory region.",
                                             inst_name='base',
                                             parent_full_inst_name='openenoc_csr.endpoint2.peers.entry[0].remote_address')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint2.peers.entry[0].remote_address.base, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.endpoint2.peers.entry[0].size.value'):
            self._single_field_property_test(fut=self.dut.endpoint2.peers.entry[0].register_size.value, lsb=0, msb=31, low=0, high=31, is_volatile=False, default=None,
                                             rdl_name="csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].size.value[31:0]",
                                             rdl_desc="32-bit size of the remote peer\u0027s memory region.",
                                             inst_name='value',
                                             parent_full_inst_name='openenoc_csr.endpoint2.peers.entry[0].size')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint2.peers.entry[0].register_size.value, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.endpoint2.peers.entry[0].dma_config.mode'):
            self._single_field_property_test(fut=self.dut.endpoint2.peers.entry[0].dma_config.mode, lsb=0, msb=1, low=0, high=1, is_volatile=False, default=None,
                                             rdl_name="csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].dma_config.mode[1:0]",
                                             rdl_desc="DMA mode for transfers to/from the remote peer:\u003cul\u003e\n\u003cli\u003e0: DMA transfers to/from the remote peer are disabled.\u003c/li\u003e\n\u003cli\u003e1: DMA transfers to/from the remote peer are enabled in transparent mode, where accesses to the virtual memory region are directly translated to corresponding accesses to the remote peer\u0027s memory region (transactions are word-by-word, i.e., per virtual memory access).\u003c/li\u003e\n\u003cli\u003e2: DMA transfers to/from the remote peer are enabled in mirror-to-local mode, where the local memory region is used instead of the virtual memory region. The state of the remote peer\u0027s memory region (remote_address, size) is fetched from the remote peer on demand or periodically.\u003c/li\u003e\n\u003cli\u003e3: DMA transfers to/from the remote peer are enabled in mirror-to-remote mode, where the remote memory region is used instead of the virtual memory region. The state of the local peer\u0027s memory region (local_address, size) is sent to the remote peer on demand or periodically.\u003c/li\u003e\n\u003c/ul\u003e",
                                             inst_name='mode',
                                             parent_full_inst_name='openenoc_csr.endpoint2.peers.entry[0].dma_config')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint2.peers.entry[0].dma_config.mode, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.endpoint2.peers.entry[1].mac_address.lo_word'):
            self._single_field_property_test(fut=self.dut.endpoint2.peers.entry[1].mac_address.lo_word, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].mac_address.lo_word[31:0]",
                                             rdl_desc="Lower 32 bits [31:0] of the 48-bit MAC address.",
                                             inst_name='lo_word',
                                             parent_full_inst_name='openenoc_csr.endpoint2.peers.entry[1].mac_address')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint2.peers.entry[1].mac_address.lo_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.endpoint2.peers.entry[1].mac_address.hi_word'):
            self._single_field_property_test(fut=self.dut.endpoint2.peers.entry[1].mac_address.hi_word, lsb=32, msb=47, low=32, high=47, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].mac_address.hi_word[47:32]",
                                             rdl_desc="Upper 16 bits [47:32] of the 48-bit MAC address.",
                                             inst_name='hi_word',
                                             parent_full_inst_name='openenoc_csr.endpoint2.peers.entry[1].mac_address')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint2.peers.entry[1].mac_address.hi_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.endpoint2.peers.entry[1].rmem_address.offset'):
            self._single_field_property_test(fut=self.dut.endpoint2.peers.entry[1].rmem_address.offset, lsb=0, msb=31, low=0, high=31, is_volatile=False, default=None,
                                             rdl_name="csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].rmem_address.offset[31:0]",
                                             rdl_desc="32-bit address offset of the virtual memory region corresponding to the remote peer\u0027s memory.",
                                             inst_name='offset',
                                             parent_full_inst_name='openenoc_csr.endpoint2.peers.entry[1].rmem_address')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint2.peers.entry[1].rmem_address.offset, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.endpoint2.peers.entry[1].local_address.base'):
            self._single_field_property_test(fut=self.dut.endpoint2.peers.entry[1].local_address.base, lsb=0, msb=31, low=0, high=31, is_volatile=False, default=None,
                                             rdl_name="csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].local_address.base[31:0]",
                                             rdl_desc="32-bit start address of the local memory region for DMA transfers.",
                                             inst_name='base',
                                             parent_full_inst_name='openenoc_csr.endpoint2.peers.entry[1].local_address')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint2.peers.entry[1].local_address.base, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.endpoint2.peers.entry[1].remote_address.base'):
            self._single_field_property_test(fut=self.dut.endpoint2.peers.entry[1].remote_address.base, lsb=0, msb=31, low=0, high=31, is_volatile=False, default=None,
                                             rdl_name="csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].remote_address.base[31:0]",
                                             rdl_desc="32-bit start address of the remote peer\u0027s memory region.",
                                             inst_name='base',
                                             parent_full_inst_name='openenoc_csr.endpoint2.peers.entry[1].remote_address')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint2.peers.entry[1].remote_address.base, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.endpoint2.peers.entry[1].size.value'):
            self._single_field_property_test(fut=self.dut.endpoint2.peers.entry[1].register_size.value, lsb=0, msb=31, low=0, high=31, is_volatile=False, default=None,
                                             rdl_name="csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].size.value[31:0]",
                                             rdl_desc="32-bit size of the remote peer\u0027s memory region.",
                                             inst_name='value',
                                             parent_full_inst_name='openenoc_csr.endpoint2.peers.entry[1].size')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint2.peers.entry[1].register_size.value, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.endpoint2.peers.entry[1].dma_config.mode'):
            self._single_field_property_test(fut=self.dut.endpoint2.peers.entry[1].dma_config.mode, lsb=0, msb=1, low=0, high=1, is_volatile=False, default=None,
                                             rdl_name="csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].dma_config.mode[1:0]",
                                             rdl_desc="DMA mode for transfers to/from the remote peer:\u003cul\u003e\n\u003cli\u003e0: DMA transfers to/from the remote peer are disabled.\u003c/li\u003e\n\u003cli\u003e1: DMA transfers to/from the remote peer are enabled in transparent mode, where accesses to the virtual memory region are directly translated to corresponding accesses to the remote peer\u0027s memory region (transactions are word-by-word, i.e., per virtual memory access).\u003c/li\u003e\n\u003cli\u003e2: DMA transfers to/from the remote peer are enabled in mirror-to-local mode, where the local memory region is used instead of the virtual memory region. The state of the remote peer\u0027s memory region (remote_address, size) is fetched from the remote peer on demand or periodically.\u003c/li\u003e\n\u003cli\u003e3: DMA transfers to/from the remote peer are enabled in mirror-to-remote mode, where the remote memory region is used instead of the virtual memory region. The state of the local peer\u0027s memory region (local_address, size) is sent to the remote peer on demand or periodically.\u003c/li\u003e\n\u003c/ul\u003e",
                                             inst_name='mode',
                                             parent_full_inst_name='openenoc_csr.endpoint2.peers.entry[1].dma_config')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint2.peers.entry[1].dma_config.mode, is_sw_readable=True, is_sw_writable=True)

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
        with self.subTest(msg='regfile: openenoc_csr.endpoint2.config'):
            self._single_regfile_property_test(dut=self.dut.endpoint2.config,
                                               size=8,
                                               rdl_name="csr.endpoint2.config",
                                               rdl_desc="Configuration register file for this openENOC Endpoint Interface instance.",
                                               inst_name='config',
                                               parent_full_inst_name='openenoc_csr.endpoint2')
            self._test_regfile_iterators(dut=self.dut.endpoint2.config,
                                         writeable_registers=NodeIterators('mac_address',),
                                         readable_registers=NodeIterators('mac_address',),
                                         sections=NodeIterators())
        with self.subTest(msg='regfile: openenoc_csr.endpoint2.peers'):
            self._single_regfile_property_test(dut=self.dut.endpoint2.peers,
                                               size=56,
                                               rdl_name="csr.endpoint2.peers",
                                               rdl_desc="Register file for remote peer configuration and memory region information.",
                                               inst_name='peers',
                                               parent_full_inst_name='openenoc_csr.endpoint2')
            self._test_regfile_iterators(dut=self.dut.endpoint2.peers,
                                         writeable_registers=NodeIterators(),
                                         readable_registers=NodeIterators(),
                                         sections=NodeIterators(('entry', [2]),))
        with self.subTest(msg='regfile: openenoc_csr.endpoint2.peers.entry[0]'):
            self._single_regfile_property_test(dut=self.dut.endpoint2.peers.entry[0],
                                               size=28,
                                               rdl_name="csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1]",
                                               rdl_desc="Register file for a single remote peer configuration and memory region information.",
                                               inst_name='entry[0]',
                                               parent_full_inst_name='openenoc_csr.endpoint2.peers')
            self._test_regfile_iterators(dut=self.dut.endpoint2.peers.entry[0],
                                         writeable_registers=NodeIterators('mac_address','rmem_address','local_address','remote_address','size','dma_config',),
                                         readable_registers=NodeIterators('mac_address','rmem_address','local_address','remote_address','size','dma_config',),
                                         sections=NodeIterators())
        with self.subTest(msg='regfile: openenoc_csr.endpoint2.peers.entry[1]'):
            self._single_regfile_property_test(dut=self.dut.endpoint2.peers.entry[1],
                                               size=28,
                                               rdl_name="csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1]",
                                               rdl_desc="Register file for a single remote peer configuration and memory region information.",
                                               inst_name='entry[1]',
                                               parent_full_inst_name='openenoc_csr.endpoint2.peers')
            self._test_regfile_iterators(dut=self.dut.endpoint2.peers.entry[1],
                                         writeable_registers=NodeIterators('mac_address','rmem_address','local_address','remote_address','size','dma_config',),
                                         readable_registers=NodeIterators('mac_address','rmem_address','local_address','remote_address','size','dma_config',),
                                         sections=NodeIterators())
        

    

    def test_array_slicing(self) -> None:
        """
        Check slicing into array
        """
        full_slice:NodeArray
        
        with self.subTest(msg='hidden_node: openenoc_csr.endpoint2.peers.entry[]'):
            
            full_slice = self.dut.endpoint2.peers.get_child_by_system_rdl_name('entry')
            
            self.assertCountEqual(iter(full_slice[:]), iter(full_slice))
        



class openenoc_csr_endpoint2_block_access(openenoc_csr_TestCase_BlockAccess): # type: ignore[valid-type,misc]
    """
    tests for all the block access methods
    """

    
    def test_memory_read_and_write(self) -> None:
        """
        Walk the register map and check every register can be read and written to correctly
        """
        # test access operations (read and/or write) to register:
        # openenoc_csr.endpoint2.rmem
        with patch(base_name + '.write_addr_space') as write_callback_mock,\
                            patch(base_name + '.read_addr_space', return_value=1) as read_callback_mock, \
                            patch(base_name + '.read_block_addr_space',
                                  return_value=[0]) as read_block_callback_mock , \
                            patch(base_name + '.write_block_addr_space') as write_block_callback_mock:

            # checks single unit accesses at the first entry, the last entry and a random entry in
            # in each case check a 0, max value and random value being read
            for entry in [0, random.randint(0,127), 127]:
                for value in [0, random.randint(0,0xFFFFFFFF), 0xFFFFFFFF]:
                    read_block_callback_mock.reset_mock()
                    
                    read_block_callback_mock.return_value = [value]
                    

                    
                    self.assertEqual(self.dut.endpoint2.rmem.read(start_entry=entry, number_entries=1), # type: ignore[union-attr]
                                                             [value])
                    
                    read_block_callback_mock.assert_called_once_with(
                                        addr=4608+(entry * 4),
                                        width=32,
                                        accesswidth=32,
                                        length=1)

            # check a multi-entry read, if the memory is small do the entire memory, however, if
            # it is large limit the number of entries to 10
            entries_to_test = 10
            
            random_data = [random.randint(0,0xFFFFFFFF) for x in range(entries_to_test)]
            


            read_block_callback_mock.reset_mock()
            read_block_callback_mock.return_value = random_data

            self.assertEqual(self.dut.endpoint2.rmem.read(start_entry=0, # type: ignore[union-attr]
                                          number_entries=entries_to_test),
                                          random_data)

            write_callback_mock.assert_not_called()
            read_callback_mock.assert_not_called()
            write_block_callback_mock.assert_not_called()
            read_block_callback_mock.reset_mock()
            

            # checks single unit accesses at the first entry, the last entry and a random entry in
            # in each case check a 0, max value and random value being read
            for entry in [0, random.randint(0,127), 127]:
                for value in [0, random.randint(0,0xFFFFFFFF), 0xFFFFFFFF]:
                    write_block_callback_mock.reset_mock()
                    
                    self.dut.endpoint2.rmem.write(start_entry=entry, data=[value]) # type: ignore[union-attr]
                    write_block_callback_mock.assert_called_once_with(
                                        addr=4608+(entry * 4),
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
            
            self.dut.endpoint2.rmem.write(start_entry=0, data=random_data) # type: ignore[union-attr]

            write_block_callback_mock.assert_called_once_with(
                                        addr=4608,
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
        

class openenoc_csr_endpoint2_alt_block_access(openenoc_csr_TestCase_AltBlockAccess): # type: ignore[valid-type,misc]
    """
    tests for all the block access methods with the alternative callbacks, this is a simpler
    version of the tests above
    """
    
    def test_memory_read_and_write(self) -> None:
        """
        Walk the register map and check every register can be read and written to correctly
        """
        # test access operations (read and/or write) to register:
        # openenoc_csr.endpoint2.rmem
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
            self.assertEqual(self.dut.endpoint2.rmem.read(start_entry=0, # type: ignore[union-attr]
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
            self.dut.endpoint2.rmem.write(start_entry=0, data=random_data_list) # type: ignore[union-attr]

            write_block_callback_mock.assert_called_once_with(
                                        addr=4608,
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