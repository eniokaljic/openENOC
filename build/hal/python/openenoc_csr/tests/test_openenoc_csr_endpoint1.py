


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
        with self.subTest(msg='register: openenoc_csr.endpoint1.config'):
            
            
            self.assertDictEqual(self.dut.endpoint1.config.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.axis_if'):
            
            
            self.assertDictEqual(self.dut.endpoint1.axis_if.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.axis_if.source'):
            
            
            self.assertDictEqual(self.dut.endpoint1.axis_if.source.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.axis_if.sink'):
            
            
            self.assertDictEqual(self.dut.endpoint1.axis_if.sink.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[0]'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[0].udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[1]'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[1].udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[2]'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[2].udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[3]'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[3].udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.rmem'):
            
            
            self.assertDictEqual(self.dut.endpoint1.rmem.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.info'):
            
            
            self.assertDictEqual(self.dut.endpoint1.info.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.config.mac_address'):
            
            
            self.assertDictEqual(self.dut.endpoint1.config.mac_address.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.axis_if.source.data'):
            
            
            self.assertDictEqual(self.dut.endpoint1.axis_if.source.data.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.axis_if.source.control'):
            
            
            self.assertDictEqual(self.dut.endpoint1.axis_if.source.control.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.axis_if.source.status'):
            
            
            self.assertDictEqual(self.dut.endpoint1.axis_if.source.status.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.axis_if.sink.data'):
            
            
            self.assertDictEqual(self.dut.endpoint1.axis_if.sink.data.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.axis_if.sink.control'):
            
            
            self.assertDictEqual(self.dut.endpoint1.axis_if.sink.control.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.axis_if.sink.status'):
            
            
            self.assertDictEqual(self.dut.endpoint1.axis_if.sink.status.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[0].mac_address'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[0].mac_address.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[0].rmem_address'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[0].rmem_address.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[0].local_address'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[0].local_address.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[0].remote_address'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[0].remote_address.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[0].size'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[0].register_size.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[0].dma'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[0].dma.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[1].mac_address'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[1].mac_address.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[1].rmem_address'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[1].rmem_address.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[1].local_address'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[1].local_address.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[1].remote_address'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[1].remote_address.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[1].size'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[1].register_size.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[1].dma'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[1].dma.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[2].mac_address'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[2].mac_address.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[2].rmem_address'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[2].rmem_address.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[2].local_address'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[2].local_address.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[2].remote_address'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[2].remote_address.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[2].size'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[2].register_size.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[2].dma'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[2].dma.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[3].mac_address'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[3].mac_address.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[3].rmem_address'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[3].rmem_address.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[3].local_address'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[3].local_address.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[3].remote_address'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[3].remote_address.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[3].size'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[3].register_size.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[3].dma'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[3].dma.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.info.rmem_total_depth'):
            
            
            self.assertDictEqual(self.dut.endpoint1.info.rmem_total_depth.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.info.num_of_peers'):
            
            
            self.assertDictEqual(self.dut.endpoint1.info.num_of_peers.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.config.mac_address.lo_word'):
            
            
            self.assertDictEqual(self.dut.endpoint1.config.mac_address.lo_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.config.mac_address.hi_word'):
            
            
            self.assertDictEqual(self.dut.endpoint1.config.mac_address.hi_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.axis_if.source.data.tdata'):
            
            
            self.assertDictEqual(self.dut.endpoint1.axis_if.source.data.tdata.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.axis_if.source.control.tvalid'):
            
            
            self.assertDictEqual(self.dut.endpoint1.axis_if.source.control.tvalid.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.axis_if.source.control.tlast'):
            
            
            self.assertDictEqual(self.dut.endpoint1.axis_if.source.control.tlast.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.axis_if.source.status.tready'):
            
            
            self.assertDictEqual(self.dut.endpoint1.axis_if.source.status.tready.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.axis_if.sink.data.tdata'):
            
            
            self.assertDictEqual(self.dut.endpoint1.axis_if.sink.data.tdata.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.axis_if.sink.control.tready'):
            
            
            self.assertDictEqual(self.dut.endpoint1.axis_if.sink.control.tready.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.axis_if.sink.status.tvalid'):
            
            
            self.assertDictEqual(self.dut.endpoint1.axis_if.sink.status.tvalid.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.axis_if.sink.status.tlast'):
            
            
            self.assertDictEqual(self.dut.endpoint1.axis_if.sink.status.tlast.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[0].mac_address.lo_word'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[0].mac_address.lo_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[0].mac_address.hi_word'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[0].mac_address.hi_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[0].rmem_address.offset'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[0].rmem_address.offset.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[0].local_address.base'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[0].local_address.base.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[0].remote_address.base'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[0].remote_address.base.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[0].size.bytes'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[0].register_size.bytes.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[0].dma.mode'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[0].dma.mode.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[0].dma.request'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[0].dma.request.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[0].dma.idle'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[0].dma.idle.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[0].dma.done'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[0].dma.done.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[0].dma.error'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[0].dma.error.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[1].mac_address.lo_word'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[1].mac_address.lo_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[1].mac_address.hi_word'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[1].mac_address.hi_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[1].rmem_address.offset'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[1].rmem_address.offset.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[1].local_address.base'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[1].local_address.base.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[1].remote_address.base'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[1].remote_address.base.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[1].size.bytes'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[1].register_size.bytes.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[1].dma.mode'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[1].dma.mode.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[1].dma.request'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[1].dma.request.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[1].dma.idle'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[1].dma.idle.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[1].dma.done'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[1].dma.done.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[1].dma.error'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[1].dma.error.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[2].mac_address.lo_word'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[2].mac_address.lo_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[2].mac_address.hi_word'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[2].mac_address.hi_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[2].rmem_address.offset'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[2].rmem_address.offset.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[2].local_address.base'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[2].local_address.base.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[2].remote_address.base'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[2].remote_address.base.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[2].size.bytes'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[2].register_size.bytes.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[2].dma.mode'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[2].dma.mode.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[2].dma.request'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[2].dma.request.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[2].dma.idle'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[2].dma.idle.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[2].dma.done'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[2].dma.done.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[2].dma.error'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[2].dma.error.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[3].mac_address.lo_word'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[3].mac_address.lo_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[3].mac_address.hi_word'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[3].mac_address.hi_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[3].rmem_address.offset'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[3].rmem_address.offset.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[3].local_address.base'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[3].local_address.base.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[3].remote_address.base'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[3].remote_address.base.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[3].size.bytes'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[3].register_size.bytes.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[3].dma.mode'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[3].dma.mode.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[3].dma.request'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[3].dma.request.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[3].dma.idle'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[3].dma.idle.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[3].dma.done'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[3].dma.done.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[3].dma.error'):
            
            
            self.assertDictEqual(self.dut.endpoint1.peers.entry[3].dma.error.udp,{})
            
        

    
    def test_memory(self) -> None:
        """
        Walk the memory instances in the register map and check:
        - the properties
        - it can be read and written to correctly
        """
        with self.subTest(msg='memory: openenoc_csr.endpoint1.rmem'):
            self._single_memory_property_test(mut=self.dut.endpoint1.rmem, address=3072, width=32, entries=256, accesswidth=None, array_typecode=None, size=1024,
                                              rdl_name="rmem",
                                              rdl_desc="Virtual memory region for all remote peers, with offsets and sizes defined in the peers regfile.",
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
            self._single_register_property_test(rut=self.dut.endpoint1.info, address=2048, width=64, accesswidth=32, size=8,
                                                rdl_name="csr.endpoint1.info",
                                                rdl_desc="Read-only information register for this openENOC Endpoint Interface instance.",
                                                inst_name='info',
                                                parent_full_inst_name='openenoc_csr.endpoint1')
            self._single_register_read_and_write_test(rut=self.dut.endpoint1.info, has_sw_readable=True, has_sw_writable=False,
                                                                                          readable_fields=set(['rmem_total_depth','num_of_peers', ]),
                                                                                          writeable_fields=set([ ]) )
        with self.subTest(msg='register: openenoc_csr.endpoint1.config.mac_address'):
            self._single_register_property_test(rut=self.dut.endpoint1.config.mac_address, address=2056, width=64, accesswidth=32, size=8,
                                                rdl_name="csr.endpoint1.config.mac_address",
                                                rdl_desc="Local site 48-bit destination MAC address.",
                                                inst_name='mac_address',
                                                parent_full_inst_name='openenoc_csr.endpoint1.config')
            self._single_register_read_and_write_test(rut=self.dut.endpoint1.config.mac_address, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['lo_word','hi_word', ]),
                                                                                          writeable_fields=set(['lo_word','hi_word', ]) )
        with self.subTest(msg='register: openenoc_csr.endpoint1.axis_if.source.data'):
            self._single_register_property_test(rut=self.dut.endpoint1.axis_if.source.data, address=2080, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint1.axis_if.source.data",
                                                rdl_desc="Data register for the AXI4-Stream source interface.",
                                                inst_name='data',
                                                parent_full_inst_name='openenoc_csr.endpoint1.axis_if.source')
            self._single_register_read_and_write_test(rut=self.dut.endpoint1.axis_if.source.data, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['tdata', ]),
                                                                                          writeable_fields=set(['tdata', ]) )
        with self.subTest(msg='register: openenoc_csr.endpoint1.axis_if.source.control'):
            self._single_register_property_test(rut=self.dut.endpoint1.axis_if.source.control, address=2084, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint1.axis_if.source.control",
                                                rdl_desc="Control register for the AXI4-Stream source interface.",
                                                inst_name='control',
                                                parent_full_inst_name='openenoc_csr.endpoint1.axis_if.source')
            self._single_register_read_and_write_test(rut=self.dut.endpoint1.axis_if.source.control, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['tvalid','tlast', ]),
                                                                                          writeable_fields=set(['tvalid','tlast', ]) )
        with self.subTest(msg='register: openenoc_csr.endpoint1.axis_if.source.status'):
            self._single_register_property_test(rut=self.dut.endpoint1.axis_if.source.status, address=2088, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint1.axis_if.source.status",
                                                rdl_desc="Status register for the AXI4-Stream source interface.",
                                                inst_name='status',
                                                parent_full_inst_name='openenoc_csr.endpoint1.axis_if.source')
            self._single_register_read_and_write_test(rut=self.dut.endpoint1.axis_if.source.status, has_sw_readable=True, has_sw_writable=False,
                                                                                          readable_fields=set(['tready', ]),
                                                                                          writeable_fields=set([ ]) )
        with self.subTest(msg='register: openenoc_csr.endpoint1.axis_if.sink.data'):
            self._single_register_property_test(rut=self.dut.endpoint1.axis_if.sink.data, address=2096, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint1.axis_if.sink.data",
                                                rdl_desc="Data register for the AXI4-Stream sink interface.",
                                                inst_name='data',
                                                parent_full_inst_name='openenoc_csr.endpoint1.axis_if.sink')
            self._single_register_read_and_write_test(rut=self.dut.endpoint1.axis_if.sink.data, has_sw_readable=True, has_sw_writable=False,
                                                                                          readable_fields=set(['tdata', ]),
                                                                                          writeable_fields=set([ ]) )
        with self.subTest(msg='register: openenoc_csr.endpoint1.axis_if.sink.control'):
            self._single_register_property_test(rut=self.dut.endpoint1.axis_if.sink.control, address=2100, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint1.axis_if.sink.control",
                                                rdl_desc="Control register for the AXI4-Stream sink interface.",
                                                inst_name='control',
                                                parent_full_inst_name='openenoc_csr.endpoint1.axis_if.sink')
            self._single_register_read_and_write_test(rut=self.dut.endpoint1.axis_if.sink.control, has_sw_readable=False, has_sw_writable=True,
                                                                                          readable_fields=set([ ]),
                                                                                          writeable_fields=set(['tready', ]) )
        with self.subTest(msg='register: openenoc_csr.endpoint1.axis_if.sink.status'):
            self._single_register_property_test(rut=self.dut.endpoint1.axis_if.sink.status, address=2104, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint1.axis_if.sink.status",
                                                rdl_desc="Status register for the AXI4-Stream sink interface.",
                                                inst_name='status',
                                                parent_full_inst_name='openenoc_csr.endpoint1.axis_if.sink')
            self._single_register_read_and_write_test(rut=self.dut.endpoint1.axis_if.sink.status, has_sw_readable=True, has_sw_writable=False,
                                                                                          readable_fields=set(['tvalid','tlast', ]),
                                                                                          writeable_fields=set([ ]) )
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[0].mac_address'):
            self._single_register_property_test(rut=self.dut.endpoint1.peers.entry[0].mac_address, address=2176, width=64, accesswidth=32, size=8,
                                                rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].mac_address",
                                                rdl_desc="Remote peer 48-bit destination MAC address.",
                                                inst_name='mac_address',
                                                parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[0]')
            self._single_register_read_and_write_test(rut=self.dut.endpoint1.peers.entry[0].mac_address, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['lo_word','hi_word', ]),
                                                                                          writeable_fields=set(['lo_word','hi_word', ]) )
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[0].rmem_address'):
            self._single_register_property_test(rut=self.dut.endpoint1.peers.entry[0].rmem_address, address=2184, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].rmem_address",
                                                rdl_desc="Address offset of the virtual memory region corresponding to the remote peer\u0027s memory.",
                                                inst_name='rmem_address',
                                                parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[0]')
            self._single_register_read_and_write_test(rut=self.dut.endpoint1.peers.entry[0].rmem_address, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['offset', ]),
                                                                                          writeable_fields=set(['offset', ]) )
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[0].local_address'):
            self._single_register_property_test(rut=self.dut.endpoint1.peers.entry[0].local_address, address=2188, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].local_address",
                                                rdl_desc="Start address of the local memory region for DMA transfers.",
                                                inst_name='local_address',
                                                parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[0]')
            self._single_register_read_and_write_test(rut=self.dut.endpoint1.peers.entry[0].local_address, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['base', ]),
                                                                                          writeable_fields=set(['base', ]) )
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[0].remote_address'):
            self._single_register_property_test(rut=self.dut.endpoint1.peers.entry[0].remote_address, address=2192, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].remote_address",
                                                rdl_desc="Start address of the remote peer\u0027s memory region.",
                                                inst_name='remote_address',
                                                parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[0]')
            self._single_register_read_and_write_test(rut=self.dut.endpoint1.peers.entry[0].remote_address, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['base', ]),
                                                                                          writeable_fields=set(['base', ]) )
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[0].size'):
            self._single_register_property_test(rut=self.dut.endpoint1.peers.entry[0].register_size, address=2196, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].size",
                                                rdl_desc="Size of the remote peer\u0027s memory region.",
                                                inst_name='size',
                                                parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[0]')
            self._single_register_read_and_write_test(rut=self.dut.endpoint1.peers.entry[0].register_size, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['bytes', ]),
                                                                                          writeable_fields=set(['bytes', ]) )
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[0].dma'):
            self._single_register_property_test(rut=self.dut.endpoint1.peers.entry[0].dma, address=2200, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].dma",
                                                rdl_desc="DMA configuration and control for the remote peer.",
                                                inst_name='dma',
                                                parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[0]')
            self._single_register_read_and_write_test(rut=self.dut.endpoint1.peers.entry[0].dma, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['mode','request','idle','done','error', ]),
                                                                                          writeable_fields=set(['mode','request', ]) )
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[1].mac_address'):
            self._single_register_property_test(rut=self.dut.endpoint1.peers.entry[1].mac_address, address=2204, width=64, accesswidth=32, size=8,
                                                rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].mac_address",
                                                rdl_desc="Remote peer 48-bit destination MAC address.",
                                                inst_name='mac_address',
                                                parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[1]')
            self._single_register_read_and_write_test(rut=self.dut.endpoint1.peers.entry[1].mac_address, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['lo_word','hi_word', ]),
                                                                                          writeable_fields=set(['lo_word','hi_word', ]) )
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[1].rmem_address'):
            self._single_register_property_test(rut=self.dut.endpoint1.peers.entry[1].rmem_address, address=2212, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].rmem_address",
                                                rdl_desc="Address offset of the virtual memory region corresponding to the remote peer\u0027s memory.",
                                                inst_name='rmem_address',
                                                parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[1]')
            self._single_register_read_and_write_test(rut=self.dut.endpoint1.peers.entry[1].rmem_address, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['offset', ]),
                                                                                          writeable_fields=set(['offset', ]) )
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[1].local_address'):
            self._single_register_property_test(rut=self.dut.endpoint1.peers.entry[1].local_address, address=2216, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].local_address",
                                                rdl_desc="Start address of the local memory region for DMA transfers.",
                                                inst_name='local_address',
                                                parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[1]')
            self._single_register_read_and_write_test(rut=self.dut.endpoint1.peers.entry[1].local_address, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['base', ]),
                                                                                          writeable_fields=set(['base', ]) )
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[1].remote_address'):
            self._single_register_property_test(rut=self.dut.endpoint1.peers.entry[1].remote_address, address=2220, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].remote_address",
                                                rdl_desc="Start address of the remote peer\u0027s memory region.",
                                                inst_name='remote_address',
                                                parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[1]')
            self._single_register_read_and_write_test(rut=self.dut.endpoint1.peers.entry[1].remote_address, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['base', ]),
                                                                                          writeable_fields=set(['base', ]) )
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[1].size'):
            self._single_register_property_test(rut=self.dut.endpoint1.peers.entry[1].register_size, address=2224, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].size",
                                                rdl_desc="Size of the remote peer\u0027s memory region.",
                                                inst_name='size',
                                                parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[1]')
            self._single_register_read_and_write_test(rut=self.dut.endpoint1.peers.entry[1].register_size, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['bytes', ]),
                                                                                          writeable_fields=set(['bytes', ]) )
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[1].dma'):
            self._single_register_property_test(rut=self.dut.endpoint1.peers.entry[1].dma, address=2228, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].dma",
                                                rdl_desc="DMA configuration and control for the remote peer.",
                                                inst_name='dma',
                                                parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[1]')
            self._single_register_read_and_write_test(rut=self.dut.endpoint1.peers.entry[1].dma, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['mode','request','idle','done','error', ]),
                                                                                          writeable_fields=set(['mode','request', ]) )
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[2].mac_address'):
            self._single_register_property_test(rut=self.dut.endpoint1.peers.entry[2].mac_address, address=2232, width=64, accesswidth=32, size=8,
                                                rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].mac_address",
                                                rdl_desc="Remote peer 48-bit destination MAC address.",
                                                inst_name='mac_address',
                                                parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[2]')
            self._single_register_read_and_write_test(rut=self.dut.endpoint1.peers.entry[2].mac_address, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['lo_word','hi_word', ]),
                                                                                          writeable_fields=set(['lo_word','hi_word', ]) )
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[2].rmem_address'):
            self._single_register_property_test(rut=self.dut.endpoint1.peers.entry[2].rmem_address, address=2240, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].rmem_address",
                                                rdl_desc="Address offset of the virtual memory region corresponding to the remote peer\u0027s memory.",
                                                inst_name='rmem_address',
                                                parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[2]')
            self._single_register_read_and_write_test(rut=self.dut.endpoint1.peers.entry[2].rmem_address, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['offset', ]),
                                                                                          writeable_fields=set(['offset', ]) )
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[2].local_address'):
            self._single_register_property_test(rut=self.dut.endpoint1.peers.entry[2].local_address, address=2244, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].local_address",
                                                rdl_desc="Start address of the local memory region for DMA transfers.",
                                                inst_name='local_address',
                                                parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[2]')
            self._single_register_read_and_write_test(rut=self.dut.endpoint1.peers.entry[2].local_address, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['base', ]),
                                                                                          writeable_fields=set(['base', ]) )
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[2].remote_address'):
            self._single_register_property_test(rut=self.dut.endpoint1.peers.entry[2].remote_address, address=2248, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].remote_address",
                                                rdl_desc="Start address of the remote peer\u0027s memory region.",
                                                inst_name='remote_address',
                                                parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[2]')
            self._single_register_read_and_write_test(rut=self.dut.endpoint1.peers.entry[2].remote_address, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['base', ]),
                                                                                          writeable_fields=set(['base', ]) )
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[2].size'):
            self._single_register_property_test(rut=self.dut.endpoint1.peers.entry[2].register_size, address=2252, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].size",
                                                rdl_desc="Size of the remote peer\u0027s memory region.",
                                                inst_name='size',
                                                parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[2]')
            self._single_register_read_and_write_test(rut=self.dut.endpoint1.peers.entry[2].register_size, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['bytes', ]),
                                                                                          writeable_fields=set(['bytes', ]) )
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[2].dma'):
            self._single_register_property_test(rut=self.dut.endpoint1.peers.entry[2].dma, address=2256, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].dma",
                                                rdl_desc="DMA configuration and control for the remote peer.",
                                                inst_name='dma',
                                                parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[2]')
            self._single_register_read_and_write_test(rut=self.dut.endpoint1.peers.entry[2].dma, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['mode','request','idle','done','error', ]),
                                                                                          writeable_fields=set(['mode','request', ]) )
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[3].mac_address'):
            self._single_register_property_test(rut=self.dut.endpoint1.peers.entry[3].mac_address, address=2260, width=64, accesswidth=32, size=8,
                                                rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].mac_address",
                                                rdl_desc="Remote peer 48-bit destination MAC address.",
                                                inst_name='mac_address',
                                                parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[3]')
            self._single_register_read_and_write_test(rut=self.dut.endpoint1.peers.entry[3].mac_address, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['lo_word','hi_word', ]),
                                                                                          writeable_fields=set(['lo_word','hi_word', ]) )
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[3].rmem_address'):
            self._single_register_property_test(rut=self.dut.endpoint1.peers.entry[3].rmem_address, address=2268, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].rmem_address",
                                                rdl_desc="Address offset of the virtual memory region corresponding to the remote peer\u0027s memory.",
                                                inst_name='rmem_address',
                                                parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[3]')
            self._single_register_read_and_write_test(rut=self.dut.endpoint1.peers.entry[3].rmem_address, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['offset', ]),
                                                                                          writeable_fields=set(['offset', ]) )
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[3].local_address'):
            self._single_register_property_test(rut=self.dut.endpoint1.peers.entry[3].local_address, address=2272, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].local_address",
                                                rdl_desc="Start address of the local memory region for DMA transfers.",
                                                inst_name='local_address',
                                                parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[3]')
            self._single_register_read_and_write_test(rut=self.dut.endpoint1.peers.entry[3].local_address, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['base', ]),
                                                                                          writeable_fields=set(['base', ]) )
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[3].remote_address'):
            self._single_register_property_test(rut=self.dut.endpoint1.peers.entry[3].remote_address, address=2276, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].remote_address",
                                                rdl_desc="Start address of the remote peer\u0027s memory region.",
                                                inst_name='remote_address',
                                                parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[3]')
            self._single_register_read_and_write_test(rut=self.dut.endpoint1.peers.entry[3].remote_address, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['base', ]),
                                                                                          writeable_fields=set(['base', ]) )
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[3].size'):
            self._single_register_property_test(rut=self.dut.endpoint1.peers.entry[3].register_size, address=2280, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].size",
                                                rdl_desc="Size of the remote peer\u0027s memory region.",
                                                inst_name='size',
                                                parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[3]')
            self._single_register_read_and_write_test(rut=self.dut.endpoint1.peers.entry[3].register_size, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['bytes', ]),
                                                                                          writeable_fields=set(['bytes', ]) )
        with self.subTest(msg='register: openenoc_csr.endpoint1.peers.entry[3].dma'):
            self._single_register_property_test(rut=self.dut.endpoint1.peers.entry[3].dma, address=2284, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].dma",
                                                rdl_desc="DMA configuration and control for the remote peer.",
                                                inst_name='dma',
                                                parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[3]')
            self._single_register_read_and_write_test(rut=self.dut.endpoint1.peers.entry[3].dma, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['mode','request','idle','done','error', ]),
                                                                                          writeable_fields=set(['mode','request', ]) )
        

    def test_field(self) -> None:
        """
        Check the properties and function (read and write) on the fields both integer and enum
        """
        
        with self.subTest(msg='field: openenoc_csr.endpoint1.info.rmem_total_depth'):
            self._single_field_property_test(fut=self.dut.endpoint1.info.rmem_total_depth, lsb=0, msb=31, low=0, high=31, is_volatile=False, default=256,
                                             rdl_name="csr.endpoint1.info.rmem_total_depth[15:0]",
                                             rdl_desc="Total depth of the shared memory region for all remote peers. This field reflects the RMEM_TOTAL_DEPTH parameter value.",
                                             inst_name='rmem_total_depth',
                                             parent_full_inst_name='openenoc_csr.endpoint1.info')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint1.info.rmem_total_depth, is_sw_readable=True, is_sw_writable=False)
        with self.subTest(msg='field: openenoc_csr.endpoint1.info.num_of_peers'):
            self._single_field_property_test(fut=self.dut.endpoint1.info.num_of_peers, lsb=32, msb=63, low=32, high=63, is_volatile=False, default=4,
                                             rdl_name="csr.endpoint1.info.num_of_peers[31:16]",
                                             rdl_desc="Number of remote peers supported by this openENOC Endpoint Interface instance. This field reflects the NUM_OF_PEERS parameter value.",
                                             inst_name='num_of_peers',
                                             parent_full_inst_name='openenoc_csr.endpoint1.info')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint1.info.num_of_peers, is_sw_readable=True, is_sw_writable=False)
        with self.subTest(msg='field: openenoc_csr.endpoint1.config.mac_address.lo_word'):
            self._single_field_property_test(fut=self.dut.endpoint1.config.mac_address.lo_word, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=0,
                                             rdl_name="csr.endpoint1.config.mac_address.lo_word[31:0]",
                                             rdl_desc="Lower 32 bits [31:0] of the 48-bit MAC address.",
                                             inst_name='lo_word',
                                             parent_full_inst_name='openenoc_csr.endpoint1.config.mac_address')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint1.config.mac_address.lo_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.endpoint1.config.mac_address.hi_word'):
            self._single_field_property_test(fut=self.dut.endpoint1.config.mac_address.hi_word, lsb=32, msb=47, low=32, high=47, is_volatile=True, default=0,
                                             rdl_name="csr.endpoint1.config.mac_address.hi_word[47:32]",
                                             rdl_desc="Upper 16 bits [47:32] of the 48-bit MAC address.",
                                             inst_name='hi_word',
                                             parent_full_inst_name='openenoc_csr.endpoint1.config.mac_address')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint1.config.mac_address.hi_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.endpoint1.axis_if.source.data.tdata'):
            self._single_field_property_test(fut=self.dut.endpoint1.axis_if.source.data.tdata, lsb=0, msb=31, low=0, high=31, is_volatile=False, default=0,
                                             rdl_name="csr.endpoint1.axis_if.source.data.tdata[31:0]",
                                             rdl_desc="32-bit data value for the AXI4-Stream source interface.",
                                             inst_name='tdata',
                                             parent_full_inst_name='openenoc_csr.endpoint1.axis_if.source.data')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint1.axis_if.source.data.tdata, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.endpoint1.axis_if.source.control.tvalid'):
            self._single_field_property_test(fut=self.dut.endpoint1.axis_if.source.control.tvalid, lsb=0, msb=0, low=0, high=0, is_volatile=False, default=0,
                                             rdl_name="csr.endpoint1.axis_if.source.control.tvalid",
                                             rdl_desc="Indicates that the AXI4-Stream source interface has valid data to send. This field is a single-pulse register that is automatically cleared back to zero after being written.",
                                             inst_name='tvalid',
                                             parent_full_inst_name='openenoc_csr.endpoint1.axis_if.source.control')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint1.axis_if.source.control.tvalid, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.endpoint1.axis_if.source.control.tlast'):
            self._single_field_property_test(fut=self.dut.endpoint1.axis_if.source.control.tlast, lsb=8, msb=8, low=8, high=8, is_volatile=False, default=0,
                                             rdl_name="csr.endpoint1.axis_if.source.control.tlast",
                                             rdl_desc="Indicates the last data word of a frame on the AXI4-Stream source interface.",
                                             inst_name='tlast',
                                             parent_full_inst_name='openenoc_csr.endpoint1.axis_if.source.control')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint1.axis_if.source.control.tlast, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.endpoint1.axis_if.source.status.tready'):
            self._single_field_property_test(fut=self.dut.endpoint1.axis_if.source.status.tready, lsb=0, msb=0, low=0, high=0, is_volatile=True, default=0,
                                             rdl_name="csr.endpoint1.axis_if.source.status.tready",
                                             rdl_desc="Indicates that the destination AXI4-Stream interface is ready to receive data.",
                                             inst_name='tready',
                                             parent_full_inst_name='openenoc_csr.endpoint1.axis_if.source.status')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint1.axis_if.source.status.tready, is_sw_readable=True, is_sw_writable=False)
        with self.subTest(msg='field: openenoc_csr.endpoint1.axis_if.sink.data.tdata'):
            self._single_field_property_test(fut=self.dut.endpoint1.axis_if.sink.data.tdata, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint1.axis_if.sink.data.tdata[31:0]",
                                             rdl_desc="32-bit data value for the AXI4-Stream sink interface.",
                                             inst_name='tdata',
                                             parent_full_inst_name='openenoc_csr.endpoint1.axis_if.sink.data')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint1.axis_if.sink.data.tdata, is_sw_readable=True, is_sw_writable=False)
        with self.subTest(msg='field: openenoc_csr.endpoint1.axis_if.sink.control.tready'):
            self._single_field_property_test(fut=self.dut.endpoint1.axis_if.sink.control.tready, lsb=0, msb=0, low=0, high=0, is_volatile=False, default=0,
                                             rdl_name="csr.endpoint1.axis_if.sink.control.tready",
                                             rdl_desc="Indicates that the AXI4-Stream sink interface is ready to receive next data transfer.",
                                             inst_name='tready',
                                             parent_full_inst_name='openenoc_csr.endpoint1.axis_if.sink.control')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint1.axis_if.sink.control.tready, is_sw_readable=False, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.endpoint1.axis_if.sink.status.tvalid'):
            self._single_field_property_test(fut=self.dut.endpoint1.axis_if.sink.status.tvalid, lsb=0, msb=0, low=0, high=0, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint1.axis_if.sink.status.tvalid",
                                             rdl_desc="Indicates that the AXI4-Stream sink interface has valid data to receive.",
                                             inst_name='tvalid',
                                             parent_full_inst_name='openenoc_csr.endpoint1.axis_if.sink.status')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint1.axis_if.sink.status.tvalid, is_sw_readable=True, is_sw_writable=False)
        with self.subTest(msg='field: openenoc_csr.endpoint1.axis_if.sink.status.tlast'):
            self._single_field_property_test(fut=self.dut.endpoint1.axis_if.sink.status.tlast, lsb=8, msb=8, low=8, high=8, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint1.axis_if.sink.status.tlast",
                                             rdl_desc="Indicates the last data word of a frame on the AXI4-Stream sink interface.",
                                             inst_name='tlast',
                                             parent_full_inst_name='openenoc_csr.endpoint1.axis_if.sink.status')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint1.axis_if.sink.status.tlast, is_sw_readable=True, is_sw_writable=False)
        with self.subTest(msg='field: openenoc_csr.endpoint1.peers.entry[0].mac_address.lo_word'):
            self._single_field_property_test(fut=self.dut.endpoint1.peers.entry[0].mac_address.lo_word, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].mac_address.lo_word[31:0]",
                                             rdl_desc="Lower 32 bits [31:0] of the 48-bit MAC address.",
                                             inst_name='lo_word',
                                             parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[0].mac_address')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint1.peers.entry[0].mac_address.lo_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.endpoint1.peers.entry[0].mac_address.hi_word'):
            self._single_field_property_test(fut=self.dut.endpoint1.peers.entry[0].mac_address.hi_word, lsb=32, msb=47, low=32, high=47, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].mac_address.hi_word[47:32]",
                                             rdl_desc="Upper 16 bits [47:32] of the 48-bit MAC address.",
                                             inst_name='hi_word',
                                             parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[0].mac_address')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint1.peers.entry[0].mac_address.hi_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.endpoint1.peers.entry[0].rmem_address.offset'):
            self._single_field_property_test(fut=self.dut.endpoint1.peers.entry[0].rmem_address.offset, lsb=0, msb=31, low=0, high=31, is_volatile=False, default=None,
                                             rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].rmem_address.offset[31:0]",
                                             rdl_desc="Word-aligned 32-bit address offset of the virtual memory region corresponding to the remote peer\u0027s memory.",
                                             inst_name='offset',
                                             parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[0].rmem_address')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint1.peers.entry[0].rmem_address.offset, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.endpoint1.peers.entry[0].local_address.base'):
            self._single_field_property_test(fut=self.dut.endpoint1.peers.entry[0].local_address.base, lsb=0, msb=31, low=0, high=31, is_volatile=False, default=None,
                                             rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].local_address.base[31:0]",
                                             rdl_desc="Word-aligned 32-bit start address of the local memory region for DMA transfers.",
                                             inst_name='base',
                                             parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[0].local_address')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint1.peers.entry[0].local_address.base, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.endpoint1.peers.entry[0].remote_address.base'):
            self._single_field_property_test(fut=self.dut.endpoint1.peers.entry[0].remote_address.base, lsb=0, msb=31, low=0, high=31, is_volatile=False, default=None,
                                             rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].remote_address.base[31:0]",
                                             rdl_desc="Word-aligned 32-bit start address of the remote peer\u0027s memory region.",
                                             inst_name='base',
                                             parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[0].remote_address')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint1.peers.entry[0].remote_address.base, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.endpoint1.peers.entry[0].size.bytes'):
            self._single_field_property_test(fut=self.dut.endpoint1.peers.entry[0].register_size.bytes, lsb=0, msb=31, low=0, high=31, is_volatile=False, default=None,
                                             rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].size.bytes[31:0]",
                                             rdl_desc="32-bit size of the remote peer\u0027s memory region in bytes.",
                                             inst_name='bytes',
                                             parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[0].size')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint1.peers.entry[0].register_size.bytes, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.endpoint1.peers.entry[0].dma.mode'):
            self._single_field_property_test(fut=self.dut.endpoint1.peers.entry[0].dma.mode, lsb=0, msb=1, low=0, high=1, is_volatile=False, default=None,
                                             rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].dma.mode[1:0]",
                                             rdl_desc="DMA mode for transfers to/from the remote peer:\u003cul\u003e\n\u003cli\u003e0: DMA transfers to/from the remote peer are disabled.\u003c/li\u003e\n\u003cli\u003e1: DMA transfers to/from the remote peer are enabled in transparent mode, where accesses to the virtual memory region are directly translated to corresponding accesses to the remote peer\u0027s memory region (transactions are word-by-word, i.e., per virtual memory access).\u003c/li\u003e\n\u003cli\u003e2: DMA transfers to/from the remote peer are enabled in mirror-to-local mode, where the local memory region is used instead of the virtual memory region. The state of the remote peer\u0027s memory region (remote_address, size) is fetched from the remote peer on demand or periodically.\u003c/li\u003e\n\u003cli\u003e3: DMA transfers to/from the remote peer are enabled in mirror-to-remote mode, where the remote memory region is used instead of the virtual memory region. The state of the local peer\u0027s memory region (local_address, size) is sent to the remote peer on demand or periodically.\u003c/li\u003e\n\u003c/ul\u003e",
                                             inst_name='mode',
                                             parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[0].dma')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint1.peers.entry[0].dma.mode, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.endpoint1.peers.entry[0].dma.request'):
            self._single_field_property_test(fut=self.dut.endpoint1.peers.entry[0].dma.request, lsb=8, msb=8, low=8, high=8, is_volatile=False, default=0,
                                             rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].dma.request[8:8]",
                                             rdl_desc="Writing a 1 to this field initiates a DMA transfer to/from the remote peer. This field is a single-pulse register that is automatically cleared back to zero after being written.",
                                             inst_name='request',
                                             parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[0].dma')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint1.peers.entry[0].dma.request, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.endpoint1.peers.entry[0].dma.idle'):
            self._single_field_property_test(fut=self.dut.endpoint1.peers.entry[0].dma.idle, lsb=16, msb=16, low=16, high=16, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].dma.idle[16:16]",
                                             rdl_desc="Indicates whether the DMA transfer to/from the remote peer is idle. A value of 1 indicates that the DMA transfer is idle, while a value of 0 indicates that the DMA transfer is in progress.",
                                             inst_name='idle',
                                             parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[0].dma')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint1.peers.entry[0].dma.idle, is_sw_readable=True, is_sw_writable=False)
        with self.subTest(msg='field: openenoc_csr.endpoint1.peers.entry[0].dma.done'):
            self._single_field_property_test(fut=self.dut.endpoint1.peers.entry[0].dma.done, lsb=24, msb=24, low=24, high=24, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].dma.done[24:24]",
                                             rdl_desc="Indicates whether the DMA transfer to/from the remote peer has been successful. A value of 1 indicates that the DMA transfer has completed successfully, while a value of 0 indicates that the DMA transfer is still in progress or has encountered an error.",
                                             inst_name='done',
                                             parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[0].dma')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint1.peers.entry[0].dma.done, is_sw_readable=True, is_sw_writable=False)
        with self.subTest(msg='field: openenoc_csr.endpoint1.peers.entry[0].dma.error'):
            self._single_field_property_test(fut=self.dut.endpoint1.peers.entry[0].dma.error, lsb=25, msb=25, low=25, high=25, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].dma.error[25:25]",
                                             rdl_desc="Indicates whether the DMA transfer to/from the remote peer has encountered an error. A value of 1 indicates an error, while a value of 0 indicates no error.",
                                             inst_name='error',
                                             parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[0].dma')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint1.peers.entry[0].dma.error, is_sw_readable=True, is_sw_writable=False)
        with self.subTest(msg='field: openenoc_csr.endpoint1.peers.entry[1].mac_address.lo_word'):
            self._single_field_property_test(fut=self.dut.endpoint1.peers.entry[1].mac_address.lo_word, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].mac_address.lo_word[31:0]",
                                             rdl_desc="Lower 32 bits [31:0] of the 48-bit MAC address.",
                                             inst_name='lo_word',
                                             parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[1].mac_address')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint1.peers.entry[1].mac_address.lo_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.endpoint1.peers.entry[1].mac_address.hi_word'):
            self._single_field_property_test(fut=self.dut.endpoint1.peers.entry[1].mac_address.hi_word, lsb=32, msb=47, low=32, high=47, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].mac_address.hi_word[47:32]",
                                             rdl_desc="Upper 16 bits [47:32] of the 48-bit MAC address.",
                                             inst_name='hi_word',
                                             parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[1].mac_address')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint1.peers.entry[1].mac_address.hi_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.endpoint1.peers.entry[1].rmem_address.offset'):
            self._single_field_property_test(fut=self.dut.endpoint1.peers.entry[1].rmem_address.offset, lsb=0, msb=31, low=0, high=31, is_volatile=False, default=None,
                                             rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].rmem_address.offset[31:0]",
                                             rdl_desc="Word-aligned 32-bit address offset of the virtual memory region corresponding to the remote peer\u0027s memory.",
                                             inst_name='offset',
                                             parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[1].rmem_address')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint1.peers.entry[1].rmem_address.offset, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.endpoint1.peers.entry[1].local_address.base'):
            self._single_field_property_test(fut=self.dut.endpoint1.peers.entry[1].local_address.base, lsb=0, msb=31, low=0, high=31, is_volatile=False, default=None,
                                             rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].local_address.base[31:0]",
                                             rdl_desc="Word-aligned 32-bit start address of the local memory region for DMA transfers.",
                                             inst_name='base',
                                             parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[1].local_address')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint1.peers.entry[1].local_address.base, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.endpoint1.peers.entry[1].remote_address.base'):
            self._single_field_property_test(fut=self.dut.endpoint1.peers.entry[1].remote_address.base, lsb=0, msb=31, low=0, high=31, is_volatile=False, default=None,
                                             rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].remote_address.base[31:0]",
                                             rdl_desc="Word-aligned 32-bit start address of the remote peer\u0027s memory region.",
                                             inst_name='base',
                                             parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[1].remote_address')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint1.peers.entry[1].remote_address.base, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.endpoint1.peers.entry[1].size.bytes'):
            self._single_field_property_test(fut=self.dut.endpoint1.peers.entry[1].register_size.bytes, lsb=0, msb=31, low=0, high=31, is_volatile=False, default=None,
                                             rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].size.bytes[31:0]",
                                             rdl_desc="32-bit size of the remote peer\u0027s memory region in bytes.",
                                             inst_name='bytes',
                                             parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[1].size')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint1.peers.entry[1].register_size.bytes, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.endpoint1.peers.entry[1].dma.mode'):
            self._single_field_property_test(fut=self.dut.endpoint1.peers.entry[1].dma.mode, lsb=0, msb=1, low=0, high=1, is_volatile=False, default=None,
                                             rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].dma.mode[1:0]",
                                             rdl_desc="DMA mode for transfers to/from the remote peer:\u003cul\u003e\n\u003cli\u003e0: DMA transfers to/from the remote peer are disabled.\u003c/li\u003e\n\u003cli\u003e1: DMA transfers to/from the remote peer are enabled in transparent mode, where accesses to the virtual memory region are directly translated to corresponding accesses to the remote peer\u0027s memory region (transactions are word-by-word, i.e., per virtual memory access).\u003c/li\u003e\n\u003cli\u003e2: DMA transfers to/from the remote peer are enabled in mirror-to-local mode, where the local memory region is used instead of the virtual memory region. The state of the remote peer\u0027s memory region (remote_address, size) is fetched from the remote peer on demand or periodically.\u003c/li\u003e\n\u003cli\u003e3: DMA transfers to/from the remote peer are enabled in mirror-to-remote mode, where the remote memory region is used instead of the virtual memory region. The state of the local peer\u0027s memory region (local_address, size) is sent to the remote peer on demand or periodically.\u003c/li\u003e\n\u003c/ul\u003e",
                                             inst_name='mode',
                                             parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[1].dma')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint1.peers.entry[1].dma.mode, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.endpoint1.peers.entry[1].dma.request'):
            self._single_field_property_test(fut=self.dut.endpoint1.peers.entry[1].dma.request, lsb=8, msb=8, low=8, high=8, is_volatile=False, default=0,
                                             rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].dma.request[8:8]",
                                             rdl_desc="Writing a 1 to this field initiates a DMA transfer to/from the remote peer. This field is a single-pulse register that is automatically cleared back to zero after being written.",
                                             inst_name='request',
                                             parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[1].dma')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint1.peers.entry[1].dma.request, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.endpoint1.peers.entry[1].dma.idle'):
            self._single_field_property_test(fut=self.dut.endpoint1.peers.entry[1].dma.idle, lsb=16, msb=16, low=16, high=16, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].dma.idle[16:16]",
                                             rdl_desc="Indicates whether the DMA transfer to/from the remote peer is idle. A value of 1 indicates that the DMA transfer is idle, while a value of 0 indicates that the DMA transfer is in progress.",
                                             inst_name='idle',
                                             parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[1].dma')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint1.peers.entry[1].dma.idle, is_sw_readable=True, is_sw_writable=False)
        with self.subTest(msg='field: openenoc_csr.endpoint1.peers.entry[1].dma.done'):
            self._single_field_property_test(fut=self.dut.endpoint1.peers.entry[1].dma.done, lsb=24, msb=24, low=24, high=24, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].dma.done[24:24]",
                                             rdl_desc="Indicates whether the DMA transfer to/from the remote peer has been successful. A value of 1 indicates that the DMA transfer has completed successfully, while a value of 0 indicates that the DMA transfer is still in progress or has encountered an error.",
                                             inst_name='done',
                                             parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[1].dma')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint1.peers.entry[1].dma.done, is_sw_readable=True, is_sw_writable=False)
        with self.subTest(msg='field: openenoc_csr.endpoint1.peers.entry[1].dma.error'):
            self._single_field_property_test(fut=self.dut.endpoint1.peers.entry[1].dma.error, lsb=25, msb=25, low=25, high=25, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].dma.error[25:25]",
                                             rdl_desc="Indicates whether the DMA transfer to/from the remote peer has encountered an error. A value of 1 indicates an error, while a value of 0 indicates no error.",
                                             inst_name='error',
                                             parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[1].dma')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint1.peers.entry[1].dma.error, is_sw_readable=True, is_sw_writable=False)
        with self.subTest(msg='field: openenoc_csr.endpoint1.peers.entry[2].mac_address.lo_word'):
            self._single_field_property_test(fut=self.dut.endpoint1.peers.entry[2].mac_address.lo_word, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].mac_address.lo_word[31:0]",
                                             rdl_desc="Lower 32 bits [31:0] of the 48-bit MAC address.",
                                             inst_name='lo_word',
                                             parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[2].mac_address')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint1.peers.entry[2].mac_address.lo_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.endpoint1.peers.entry[2].mac_address.hi_word'):
            self._single_field_property_test(fut=self.dut.endpoint1.peers.entry[2].mac_address.hi_word, lsb=32, msb=47, low=32, high=47, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].mac_address.hi_word[47:32]",
                                             rdl_desc="Upper 16 bits [47:32] of the 48-bit MAC address.",
                                             inst_name='hi_word',
                                             parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[2].mac_address')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint1.peers.entry[2].mac_address.hi_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.endpoint1.peers.entry[2].rmem_address.offset'):
            self._single_field_property_test(fut=self.dut.endpoint1.peers.entry[2].rmem_address.offset, lsb=0, msb=31, low=0, high=31, is_volatile=False, default=None,
                                             rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].rmem_address.offset[31:0]",
                                             rdl_desc="Word-aligned 32-bit address offset of the virtual memory region corresponding to the remote peer\u0027s memory.",
                                             inst_name='offset',
                                             parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[2].rmem_address')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint1.peers.entry[2].rmem_address.offset, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.endpoint1.peers.entry[2].local_address.base'):
            self._single_field_property_test(fut=self.dut.endpoint1.peers.entry[2].local_address.base, lsb=0, msb=31, low=0, high=31, is_volatile=False, default=None,
                                             rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].local_address.base[31:0]",
                                             rdl_desc="Word-aligned 32-bit start address of the local memory region for DMA transfers.",
                                             inst_name='base',
                                             parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[2].local_address')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint1.peers.entry[2].local_address.base, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.endpoint1.peers.entry[2].remote_address.base'):
            self._single_field_property_test(fut=self.dut.endpoint1.peers.entry[2].remote_address.base, lsb=0, msb=31, low=0, high=31, is_volatile=False, default=None,
                                             rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].remote_address.base[31:0]",
                                             rdl_desc="Word-aligned 32-bit start address of the remote peer\u0027s memory region.",
                                             inst_name='base',
                                             parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[2].remote_address')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint1.peers.entry[2].remote_address.base, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.endpoint1.peers.entry[2].size.bytes'):
            self._single_field_property_test(fut=self.dut.endpoint1.peers.entry[2].register_size.bytes, lsb=0, msb=31, low=0, high=31, is_volatile=False, default=None,
                                             rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].size.bytes[31:0]",
                                             rdl_desc="32-bit size of the remote peer\u0027s memory region in bytes.",
                                             inst_name='bytes',
                                             parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[2].size')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint1.peers.entry[2].register_size.bytes, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.endpoint1.peers.entry[2].dma.mode'):
            self._single_field_property_test(fut=self.dut.endpoint1.peers.entry[2].dma.mode, lsb=0, msb=1, low=0, high=1, is_volatile=False, default=None,
                                             rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].dma.mode[1:0]",
                                             rdl_desc="DMA mode for transfers to/from the remote peer:\u003cul\u003e\n\u003cli\u003e0: DMA transfers to/from the remote peer are disabled.\u003c/li\u003e\n\u003cli\u003e1: DMA transfers to/from the remote peer are enabled in transparent mode, where accesses to the virtual memory region are directly translated to corresponding accesses to the remote peer\u0027s memory region (transactions are word-by-word, i.e., per virtual memory access).\u003c/li\u003e\n\u003cli\u003e2: DMA transfers to/from the remote peer are enabled in mirror-to-local mode, where the local memory region is used instead of the virtual memory region. The state of the remote peer\u0027s memory region (remote_address, size) is fetched from the remote peer on demand or periodically.\u003c/li\u003e\n\u003cli\u003e3: DMA transfers to/from the remote peer are enabled in mirror-to-remote mode, where the remote memory region is used instead of the virtual memory region. The state of the local peer\u0027s memory region (local_address, size) is sent to the remote peer on demand or periodically.\u003c/li\u003e\n\u003c/ul\u003e",
                                             inst_name='mode',
                                             parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[2].dma')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint1.peers.entry[2].dma.mode, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.endpoint1.peers.entry[2].dma.request'):
            self._single_field_property_test(fut=self.dut.endpoint1.peers.entry[2].dma.request, lsb=8, msb=8, low=8, high=8, is_volatile=False, default=0,
                                             rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].dma.request[8:8]",
                                             rdl_desc="Writing a 1 to this field initiates a DMA transfer to/from the remote peer. This field is a single-pulse register that is automatically cleared back to zero after being written.",
                                             inst_name='request',
                                             parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[2].dma')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint1.peers.entry[2].dma.request, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.endpoint1.peers.entry[2].dma.idle'):
            self._single_field_property_test(fut=self.dut.endpoint1.peers.entry[2].dma.idle, lsb=16, msb=16, low=16, high=16, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].dma.idle[16:16]",
                                             rdl_desc="Indicates whether the DMA transfer to/from the remote peer is idle. A value of 1 indicates that the DMA transfer is idle, while a value of 0 indicates that the DMA transfer is in progress.",
                                             inst_name='idle',
                                             parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[2].dma')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint1.peers.entry[2].dma.idle, is_sw_readable=True, is_sw_writable=False)
        with self.subTest(msg='field: openenoc_csr.endpoint1.peers.entry[2].dma.done'):
            self._single_field_property_test(fut=self.dut.endpoint1.peers.entry[2].dma.done, lsb=24, msb=24, low=24, high=24, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].dma.done[24:24]",
                                             rdl_desc="Indicates whether the DMA transfer to/from the remote peer has been successful. A value of 1 indicates that the DMA transfer has completed successfully, while a value of 0 indicates that the DMA transfer is still in progress or has encountered an error.",
                                             inst_name='done',
                                             parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[2].dma')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint1.peers.entry[2].dma.done, is_sw_readable=True, is_sw_writable=False)
        with self.subTest(msg='field: openenoc_csr.endpoint1.peers.entry[2].dma.error'):
            self._single_field_property_test(fut=self.dut.endpoint1.peers.entry[2].dma.error, lsb=25, msb=25, low=25, high=25, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].dma.error[25:25]",
                                             rdl_desc="Indicates whether the DMA transfer to/from the remote peer has encountered an error. A value of 1 indicates an error, while a value of 0 indicates no error.",
                                             inst_name='error',
                                             parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[2].dma')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint1.peers.entry[2].dma.error, is_sw_readable=True, is_sw_writable=False)
        with self.subTest(msg='field: openenoc_csr.endpoint1.peers.entry[3].mac_address.lo_word'):
            self._single_field_property_test(fut=self.dut.endpoint1.peers.entry[3].mac_address.lo_word, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].mac_address.lo_word[31:0]",
                                             rdl_desc="Lower 32 bits [31:0] of the 48-bit MAC address.",
                                             inst_name='lo_word',
                                             parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[3].mac_address')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint1.peers.entry[3].mac_address.lo_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.endpoint1.peers.entry[3].mac_address.hi_word'):
            self._single_field_property_test(fut=self.dut.endpoint1.peers.entry[3].mac_address.hi_word, lsb=32, msb=47, low=32, high=47, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].mac_address.hi_word[47:32]",
                                             rdl_desc="Upper 16 bits [47:32] of the 48-bit MAC address.",
                                             inst_name='hi_word',
                                             parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[3].mac_address')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint1.peers.entry[3].mac_address.hi_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.endpoint1.peers.entry[3].rmem_address.offset'):
            self._single_field_property_test(fut=self.dut.endpoint1.peers.entry[3].rmem_address.offset, lsb=0, msb=31, low=0, high=31, is_volatile=False, default=None,
                                             rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].rmem_address.offset[31:0]",
                                             rdl_desc="Word-aligned 32-bit address offset of the virtual memory region corresponding to the remote peer\u0027s memory.",
                                             inst_name='offset',
                                             parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[3].rmem_address')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint1.peers.entry[3].rmem_address.offset, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.endpoint1.peers.entry[3].local_address.base'):
            self._single_field_property_test(fut=self.dut.endpoint1.peers.entry[3].local_address.base, lsb=0, msb=31, low=0, high=31, is_volatile=False, default=None,
                                             rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].local_address.base[31:0]",
                                             rdl_desc="Word-aligned 32-bit start address of the local memory region for DMA transfers.",
                                             inst_name='base',
                                             parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[3].local_address')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint1.peers.entry[3].local_address.base, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.endpoint1.peers.entry[3].remote_address.base'):
            self._single_field_property_test(fut=self.dut.endpoint1.peers.entry[3].remote_address.base, lsb=0, msb=31, low=0, high=31, is_volatile=False, default=None,
                                             rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].remote_address.base[31:0]",
                                             rdl_desc="Word-aligned 32-bit start address of the remote peer\u0027s memory region.",
                                             inst_name='base',
                                             parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[3].remote_address')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint1.peers.entry[3].remote_address.base, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.endpoint1.peers.entry[3].size.bytes'):
            self._single_field_property_test(fut=self.dut.endpoint1.peers.entry[3].register_size.bytes, lsb=0, msb=31, low=0, high=31, is_volatile=False, default=None,
                                             rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].size.bytes[31:0]",
                                             rdl_desc="32-bit size of the remote peer\u0027s memory region in bytes.",
                                             inst_name='bytes',
                                             parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[3].size')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint1.peers.entry[3].register_size.bytes, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.endpoint1.peers.entry[3].dma.mode'):
            self._single_field_property_test(fut=self.dut.endpoint1.peers.entry[3].dma.mode, lsb=0, msb=1, low=0, high=1, is_volatile=False, default=None,
                                             rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].dma.mode[1:0]",
                                             rdl_desc="DMA mode for transfers to/from the remote peer:\u003cul\u003e\n\u003cli\u003e0: DMA transfers to/from the remote peer are disabled.\u003c/li\u003e\n\u003cli\u003e1: DMA transfers to/from the remote peer are enabled in transparent mode, where accesses to the virtual memory region are directly translated to corresponding accesses to the remote peer\u0027s memory region (transactions are word-by-word, i.e., per virtual memory access).\u003c/li\u003e\n\u003cli\u003e2: DMA transfers to/from the remote peer are enabled in mirror-to-local mode, where the local memory region is used instead of the virtual memory region. The state of the remote peer\u0027s memory region (remote_address, size) is fetched from the remote peer on demand or periodically.\u003c/li\u003e\n\u003cli\u003e3: DMA transfers to/from the remote peer are enabled in mirror-to-remote mode, where the remote memory region is used instead of the virtual memory region. The state of the local peer\u0027s memory region (local_address, size) is sent to the remote peer on demand or periodically.\u003c/li\u003e\n\u003c/ul\u003e",
                                             inst_name='mode',
                                             parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[3].dma')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint1.peers.entry[3].dma.mode, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.endpoint1.peers.entry[3].dma.request'):
            self._single_field_property_test(fut=self.dut.endpoint1.peers.entry[3].dma.request, lsb=8, msb=8, low=8, high=8, is_volatile=False, default=0,
                                             rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].dma.request[8:8]",
                                             rdl_desc="Writing a 1 to this field initiates a DMA transfer to/from the remote peer. This field is a single-pulse register that is automatically cleared back to zero after being written.",
                                             inst_name='request',
                                             parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[3].dma')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint1.peers.entry[3].dma.request, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.endpoint1.peers.entry[3].dma.idle'):
            self._single_field_property_test(fut=self.dut.endpoint1.peers.entry[3].dma.idle, lsb=16, msb=16, low=16, high=16, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].dma.idle[16:16]",
                                             rdl_desc="Indicates whether the DMA transfer to/from the remote peer is idle. A value of 1 indicates that the DMA transfer is idle, while a value of 0 indicates that the DMA transfer is in progress.",
                                             inst_name='idle',
                                             parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[3].dma')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint1.peers.entry[3].dma.idle, is_sw_readable=True, is_sw_writable=False)
        with self.subTest(msg='field: openenoc_csr.endpoint1.peers.entry[3].dma.done'):
            self._single_field_property_test(fut=self.dut.endpoint1.peers.entry[3].dma.done, lsb=24, msb=24, low=24, high=24, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].dma.done[24:24]",
                                             rdl_desc="Indicates whether the DMA transfer to/from the remote peer has been successful. A value of 1 indicates that the DMA transfer has completed successfully, while a value of 0 indicates that the DMA transfer is still in progress or has encountered an error.",
                                             inst_name='done',
                                             parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[3].dma')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint1.peers.entry[3].dma.done, is_sw_readable=True, is_sw_writable=False)
        with self.subTest(msg='field: openenoc_csr.endpoint1.peers.entry[3].dma.error'):
            self._single_field_property_test(fut=self.dut.endpoint1.peers.entry[3].dma.error, lsb=25, msb=25, low=25, high=25, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].dma.error[25:25]",
                                             rdl_desc="Indicates whether the DMA transfer to/from the remote peer has encountered an error. A value of 1 indicates an error, while a value of 0 indicates no error.",
                                             inst_name='error',
                                             parent_full_inst_name='openenoc_csr.endpoint1.peers.entry[3].dma')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint1.peers.entry[3].dma.error, is_sw_readable=True, is_sw_writable=False)

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
        with self.subTest(msg='regfile: openenoc_csr.endpoint1.config'):
            self._single_regfile_property_test(dut=self.dut.endpoint1.config,
                                               size=8,
                                               rdl_name="csr.endpoint1.config",
                                               rdl_desc="Configuration register file for this openENOC Endpoint Interface instance.",
                                               inst_name='config',
                                               parent_full_inst_name='openenoc_csr.endpoint1')
            self._test_regfile_iterators(dut=self.dut.endpoint1.config,
                                         writeable_registers=NodeIterators('mac_address',),
                                         readable_registers=NodeIterators('mac_address',),
                                         sections=NodeIterators())
        with self.subTest(msg='regfile: openenoc_csr.endpoint1.axis_if'):
            self._single_regfile_property_test(dut=self.dut.endpoint1.axis_if,
                                               size=28,
                                               rdl_name="csr.endpoint1.axis_if",
                                               rdl_desc="Register file for the AXI4-Stream source and sink interfaces.",
                                               inst_name='axis_if',
                                               parent_full_inst_name='openenoc_csr.endpoint1')
            self._test_regfile_iterators(dut=self.dut.endpoint1.axis_if,
                                         writeable_registers=NodeIterators(),
                                         readable_registers=NodeIterators(),
                                         sections=NodeIterators('source','sink',))
        with self.subTest(msg='regfile: openenoc_csr.endpoint1.axis_if.source'):
            self._single_regfile_property_test(dut=self.dut.endpoint1.axis_if.source,
                                               size=12,
                                               rdl_name="csr.endpoint1.axis_if.source",
                                               rdl_desc="Register file for the AXI4-Stream source interface.",
                                               inst_name='source',
                                               parent_full_inst_name='openenoc_csr.endpoint1.axis_if')
            self._test_regfile_iterators(dut=self.dut.endpoint1.axis_if.source,
                                         writeable_registers=NodeIterators('data','control',),
                                         readable_registers=NodeIterators('data','control','status',),
                                         sections=NodeIterators())
        with self.subTest(msg='regfile: openenoc_csr.endpoint1.axis_if.sink'):
            self._single_regfile_property_test(dut=self.dut.endpoint1.axis_if.sink,
                                               size=12,
                                               rdl_name="csr.endpoint1.axis_if.sink",
                                               rdl_desc="Register file for the AXI4-Stream sink interface.",
                                               inst_name='sink',
                                               parent_full_inst_name='openenoc_csr.endpoint1.axis_if')
            self._test_regfile_iterators(dut=self.dut.endpoint1.axis_if.sink,
                                         writeable_registers=NodeIterators('control',),
                                         readable_registers=NodeIterators('data','status',),
                                         sections=NodeIterators())
        with self.subTest(msg='regfile: openenoc_csr.endpoint1.peers'):
            self._single_regfile_property_test(dut=self.dut.endpoint1.peers,
                                               size=112,
                                               rdl_name="csr.endpoint1.peers",
                                               rdl_desc="Register file for remote peer configuration and memory region information.",
                                               inst_name='peers',
                                               parent_full_inst_name='openenoc_csr.endpoint1')
            self._test_regfile_iterators(dut=self.dut.endpoint1.peers,
                                         writeable_registers=NodeIterators(),
                                         readable_registers=NodeIterators(),
                                         sections=NodeIterators(('entry', [4]),))
        with self.subTest(msg='regfile: openenoc_csr.endpoint1.peers.entry[0]'):
            self._single_regfile_property_test(dut=self.dut.endpoint1.peers.entry[0],
                                               size=28,
                                               rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1]",
                                               rdl_desc="Register file for a single remote peer configuration and memory region information.",
                                               inst_name='entry[0]',
                                               parent_full_inst_name='openenoc_csr.endpoint1.peers')
            self._test_regfile_iterators(dut=self.dut.endpoint1.peers.entry[0],
                                         writeable_registers=NodeIterators('mac_address','rmem_address','local_address','remote_address','size','dma',),
                                         readable_registers=NodeIterators('mac_address','rmem_address','local_address','remote_address','size','dma',),
                                         sections=NodeIterators())
        with self.subTest(msg='regfile: openenoc_csr.endpoint1.peers.entry[1]'):
            self._single_regfile_property_test(dut=self.dut.endpoint1.peers.entry[1],
                                               size=28,
                                               rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1]",
                                               rdl_desc="Register file for a single remote peer configuration and memory region information.",
                                               inst_name='entry[1]',
                                               parent_full_inst_name='openenoc_csr.endpoint1.peers')
            self._test_regfile_iterators(dut=self.dut.endpoint1.peers.entry[1],
                                         writeable_registers=NodeIterators('mac_address','rmem_address','local_address','remote_address','size','dma',),
                                         readable_registers=NodeIterators('mac_address','rmem_address','local_address','remote_address','size','dma',),
                                         sections=NodeIterators())
        with self.subTest(msg='regfile: openenoc_csr.endpoint1.peers.entry[2]'):
            self._single_regfile_property_test(dut=self.dut.endpoint1.peers.entry[2],
                                               size=28,
                                               rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1]",
                                               rdl_desc="Register file for a single remote peer configuration and memory region information.",
                                               inst_name='entry[2]',
                                               parent_full_inst_name='openenoc_csr.endpoint1.peers')
            self._test_regfile_iterators(dut=self.dut.endpoint1.peers.entry[2],
                                         writeable_registers=NodeIterators('mac_address','rmem_address','local_address','remote_address','size','dma',),
                                         readable_registers=NodeIterators('mac_address','rmem_address','local_address','remote_address','size','dma',),
                                         sections=NodeIterators())
        with self.subTest(msg='regfile: openenoc_csr.endpoint1.peers.entry[3]'):
            self._single_regfile_property_test(dut=self.dut.endpoint1.peers.entry[3],
                                               size=28,
                                               rdl_name="csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1]",
                                               rdl_desc="Register file for a single remote peer configuration and memory region information.",
                                               inst_name='entry[3]',
                                               parent_full_inst_name='openenoc_csr.endpoint1.peers')
            self._test_regfile_iterators(dut=self.dut.endpoint1.peers.entry[3],
                                         writeable_registers=NodeIterators('mac_address','rmem_address','local_address','remote_address','size','dma',),
                                         readable_registers=NodeIterators('mac_address','rmem_address','local_address','remote_address','size','dma',),
                                         sections=NodeIterators())
        

    

    def test_array_slicing(self) -> None:
        """
        Check slicing into array
        """
        full_slice:NodeArray
        
        with self.subTest(msg='hidden_node: openenoc_csr.endpoint1.peers.entry[]'):
            
            full_slice = self.dut.endpoint1.peers.get_child_by_system_rdl_name('entry')
            
            self.assertCountEqual(iter(full_slice[:]), iter(full_slice))
        



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