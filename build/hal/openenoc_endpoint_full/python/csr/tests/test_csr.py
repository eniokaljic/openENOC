


"""
Unit Tests for the csr register model Python Wrapper

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
        with self.subTest(msg='register: csr.endpoint_interface'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.config'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.config.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.axis_if'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.axis_if.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.axis_if.source'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.axis_if.source.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.axis_if.sink'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.axis_if.sink.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[0]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[0].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[1]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[1].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[2]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[2].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[3]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[3].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface'):
            
            
            self.assertDictEqual(self.dut.switch_interface.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[0]'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.entry[0].udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[1]'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.entry[1].udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[2]'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.entry[2].udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[3]'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.entry[3].udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[4]'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.entry[4].udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[5]'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.entry[5].udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[6]'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.entry[6].udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[7]'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.entry[7].udp,{})
            
        with self.subTest(msg='register: csr.test_reg'):
            
            
            self.assertDictEqual(self.dut.test_reg.udp,{})
            
        with self.subTest(msg='register: csr.regB'):
            
            
            self.assertDictEqual(self.dut.regB.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.info'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.info.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.config.mac_address'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.config.mac_address.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.axis_if.source.data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.axis_if.source.data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.axis_if.source.control'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.axis_if.source.control.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.axis_if.source.status'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.axis_if.source.status.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.axis_if.sink.data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.axis_if.sink.data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.axis_if.sink.control'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.axis_if.sink.control.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.axis_if.sink.status'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.axis_if.sink.status.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[0].mac_address'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[0].mac_address.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[0].rmem_address'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[0].rmem_address.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[0].local_address'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[0].local_address.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[0].remote_address'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[0].remote_address.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[0].size'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[0].register_size.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[0].dma'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[0].dma.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[1].mac_address'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[1].mac_address.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[1].rmem_address'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[1].rmem_address.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[1].local_address'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[1].local_address.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[1].remote_address'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[1].remote_address.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[1].size'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[1].register_size.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[1].dma'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[1].dma.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[2].mac_address'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[2].mac_address.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[2].rmem_address'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[2].rmem_address.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[2].local_address'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[2].local_address.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[2].remote_address'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[2].remote_address.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[2].size'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[2].register_size.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[2].dma'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[2].dma.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[3].mac_address'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[3].mac_address.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[3].rmem_address'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[3].rmem_address.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[3].local_address'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[3].local_address.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[3].remote_address'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[3].remote_address.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[3].size'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[3].register_size.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[3].dma'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[3].dma.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[0]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[0].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[1]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[1].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[2]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[2].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[3]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[3].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[4]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[4].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[5]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[5].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[6]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[6].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[7]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[7].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[8]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[8].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[9]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[9].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[10]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[10].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[11]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[11].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[12]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[12].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[13]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[13].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[14]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[14].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[15]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[15].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[16]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[16].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[17]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[17].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[18]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[18].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[19]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[19].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[20]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[20].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[21]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[21].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[22]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[22].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[23]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[23].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[24]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[24].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[25]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[25].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[26]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[26].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[27]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[27].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[28]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[28].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[29]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[29].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[30]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[30].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[31]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[31].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[32]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[32].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[33]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[33].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[34]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[34].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[35]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[35].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[36]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[36].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[37]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[37].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[38]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[38].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[39]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[39].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[40]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[40].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[41]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[41].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[42]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[42].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[43]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[43].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[44]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[44].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[45]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[45].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[46]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[46].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[47]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[47].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[48]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[48].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[49]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[49].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[50]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[50].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[51]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[51].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[52]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[52].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[53]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[53].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[54]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[54].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[55]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[55].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[56]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[56].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[57]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[57].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[58]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[58].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[59]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[59].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[60]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[60].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[61]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[61].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[62]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[62].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[63]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[63].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[64]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[64].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[65]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[65].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[66]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[66].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[67]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[67].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[68]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[68].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[69]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[69].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[70]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[70].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[71]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[71].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[72]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[72].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[73]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[73].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[74]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[74].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[75]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[75].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[76]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[76].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[77]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[77].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[78]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[78].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[79]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[79].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[80]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[80].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[81]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[81].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[82]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[82].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[83]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[83].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[84]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[84].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[85]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[85].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[86]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[86].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[87]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[87].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[88]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[88].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[89]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[89].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[90]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[90].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[91]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[91].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[92]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[92].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[93]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[93].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[94]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[94].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[95]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[95].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[96]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[96].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[97]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[97].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[98]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[98].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[99]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[99].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[100]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[100].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[101]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[101].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[102]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[102].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[103]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[103].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[104]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[104].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[105]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[105].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[106]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[106].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[107]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[107].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[108]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[108].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[109]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[109].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[110]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[110].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[111]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[111].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[112]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[112].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[113]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[113].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[114]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[114].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[115]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[115].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[116]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[116].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[117]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[117].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[118]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[118].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[119]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[119].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[120]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[120].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[121]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[121].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[122]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[122].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[123]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[123].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[124]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[124].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[125]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[125].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[126]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[126].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[127]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[127].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[128]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[128].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[129]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[129].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[130]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[130].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[131]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[131].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[132]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[132].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[133]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[133].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[134]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[134].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[135]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[135].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[136]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[136].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[137]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[137].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[138]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[138].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[139]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[139].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[140]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[140].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[141]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[141].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[142]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[142].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[143]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[143].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[144]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[144].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[145]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[145].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[146]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[146].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[147]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[147].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[148]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[148].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[149]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[149].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[150]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[150].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[151]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[151].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[152]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[152].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[153]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[153].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[154]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[154].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[155]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[155].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[156]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[156].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[157]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[157].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[158]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[158].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[159]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[159].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[160]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[160].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[161]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[161].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[162]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[162].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[163]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[163].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[164]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[164].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[165]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[165].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[166]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[166].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[167]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[167].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[168]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[168].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[169]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[169].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[170]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[170].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[171]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[171].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[172]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[172].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[173]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[173].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[174]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[174].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[175]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[175].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[176]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[176].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[177]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[177].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[178]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[178].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[179]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[179].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[180]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[180].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[181]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[181].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[182]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[182].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[183]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[183].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[184]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[184].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[185]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[185].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[186]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[186].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[187]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[187].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[188]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[188].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[189]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[189].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[190]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[190].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[191]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[191].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[192]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[192].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[193]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[193].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[194]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[194].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[195]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[195].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[196]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[196].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[197]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[197].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[198]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[198].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[199]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[199].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[200]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[200].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[201]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[201].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[202]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[202].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[203]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[203].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[204]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[204].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[205]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[205].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[206]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[206].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[207]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[207].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[208]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[208].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[209]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[209].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[210]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[210].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[211]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[211].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[212]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[212].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[213]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[213].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[214]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[214].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[215]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[215].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[216]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[216].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[217]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[217].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[218]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[218].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[219]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[219].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[220]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[220].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[221]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[221].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[222]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[222].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[223]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[223].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[224]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[224].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[225]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[225].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[226]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[226].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[227]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[227].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[228]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[228].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[229]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[229].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[230]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[230].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[231]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[231].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[232]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[232].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[233]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[233].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[234]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[234].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[235]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[235].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[236]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[236].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[237]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[237].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[238]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[238].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[239]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[239].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[240]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[240].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[241]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[241].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[242]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[242].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[243]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[243].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[244]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[244].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[245]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[245].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[246]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[246].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[247]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[247].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[248]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[248].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[249]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[249].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[250]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[250].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[251]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[251].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[252]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[252].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[253]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[253].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[254]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[254].udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[255]'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[255].udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.info'):
            
            
            self.assertDictEqual(self.dut.switch_interface.info.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_control'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_control.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.default_forwarding'):
            
            
            self.assertDictEqual(self.dut.switch_interface.default_forwarding.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[0].mac_address'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.entry[0].mac_address.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[0].iface'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.entry[0].iface.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[0].config'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.entry[0].config.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[1].mac_address'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.entry[1].mac_address.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[1].iface'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.entry[1].iface.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[1].config'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.entry[1].config.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[2].mac_address'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.entry[2].mac_address.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[2].iface'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.entry[2].iface.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[2].config'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.entry[2].config.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[3].mac_address'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.entry[3].mac_address.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[3].iface'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.entry[3].iface.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[3].config'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.entry[3].config.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[4].mac_address'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.entry[4].mac_address.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[4].iface'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.entry[4].iface.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[4].config'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.entry[4].config.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[5].mac_address'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.entry[5].mac_address.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[5].iface'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.entry[5].iface.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[5].config'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.entry[5].config.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[6].mac_address'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.entry[6].mac_address.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[6].iface'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.entry[6].iface.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[6].config'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.entry[6].config.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[7].mac_address'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.entry[7].mac_address.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[7].iface'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.entry[7].iface.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[7].config'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.entry[7].config.udp,{})
            
        with self.subTest(msg='register: csr.test_reg.test_field'):
            
            
            self.assertDictEqual(self.dut.test_reg.test_field.udp,{})
            
        with self.subTest(msg='register: csr.regB.f0'):
            
            
            self.assertDictEqual(self.dut.regB.f0.udp,{})
            
        with self.subTest(msg='register: csr.regB.f1'):
            
            
            self.assertDictEqual(self.dut.regB.f1.udp,{})
            
        with self.subTest(msg='register: csr.regB.f2'):
            
            
            self.assertDictEqual(self.dut.regB.f2.udp,{})
            
        with self.subTest(msg='register: csr.regB.f3'):
            
            
            self.assertDictEqual(self.dut.regB.f3.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.info.rmem_total_depth'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.info.rmem_total_depth.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.info.num_of_peers'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.info.num_of_peers.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.config.mac_address.lo_word'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.config.mac_address.lo_word.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.config.mac_address.hi_word'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.config.mac_address.hi_word.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.axis_if.source.data.tdata'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.axis_if.source.data.tdata.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.axis_if.source.control.tvalid'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.axis_if.source.control.tvalid.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.axis_if.source.control.tlast'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.axis_if.source.control.tlast.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.axis_if.source.control.tkeep'):


            self.assertDictEqual(self.dut.endpoint_interface.axis_if.source.control.tkeep.udp,{})

        with self.subTest(msg='register: csr.endpoint_interface.axis_if.source.status.tready'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.axis_if.source.status.tready.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.axis_if.sink.data.tdata'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.axis_if.sink.data.tdata.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.axis_if.sink.control.tready'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.axis_if.sink.control.tready.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.axis_if.sink.status.tvalid'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.axis_if.sink.status.tvalid.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.axis_if.sink.status.tlast'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.axis_if.sink.status.tlast.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.axis_if.sink.status.tkeep'):


            self.assertDictEqual(self.dut.endpoint_interface.axis_if.sink.status.tkeep.udp,{})

        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[0].mac_address.lo_word'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[0].mac_address.lo_word.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[0].mac_address.hi_word'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[0].mac_address.hi_word.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[0].rmem_address.offset'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[0].rmem_address.offset.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[0].local_address.base'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[0].local_address.base.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[0].remote_address.base'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[0].remote_address.base.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[0].size.bytes'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[0].register_size.bytes.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[0].dma.mode'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[0].dma.mode.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[0].dma.request'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[0].dma.request.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[0].dma.idle'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[0].dma.idle.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[0].dma.done'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[0].dma.done.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[0].dma.error'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[0].dma.error.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[1].mac_address.lo_word'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[1].mac_address.lo_word.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[1].mac_address.hi_word'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[1].mac_address.hi_word.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[1].rmem_address.offset'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[1].rmem_address.offset.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[1].local_address.base'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[1].local_address.base.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[1].remote_address.base'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[1].remote_address.base.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[1].size.bytes'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[1].register_size.bytes.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[1].dma.mode'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[1].dma.mode.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[1].dma.request'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[1].dma.request.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[1].dma.idle'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[1].dma.idle.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[1].dma.done'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[1].dma.done.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[1].dma.error'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[1].dma.error.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[2].mac_address.lo_word'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[2].mac_address.lo_word.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[2].mac_address.hi_word'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[2].mac_address.hi_word.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[2].rmem_address.offset'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[2].rmem_address.offset.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[2].local_address.base'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[2].local_address.base.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[2].remote_address.base'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[2].remote_address.base.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[2].size.bytes'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[2].register_size.bytes.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[2].dma.mode'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[2].dma.mode.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[2].dma.request'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[2].dma.request.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[2].dma.idle'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[2].dma.idle.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[2].dma.done'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[2].dma.done.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[2].dma.error'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[2].dma.error.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[3].mac_address.lo_word'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[3].mac_address.lo_word.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[3].mac_address.hi_word'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[3].mac_address.hi_word.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[3].rmem_address.offset'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[3].rmem_address.offset.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[3].local_address.base'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[3].local_address.base.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[3].remote_address.base'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[3].remote_address.base.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[3].size.bytes'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[3].register_size.bytes.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[3].dma.mode'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[3].dma.mode.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[3].dma.request'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[3].dma.request.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[3].dma.idle'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[3].dma.idle.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[3].dma.done'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[3].dma.done.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[3].dma.error'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.peers.entry[3].dma.error.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[0].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[0].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[1].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[1].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[2].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[2].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[3].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[3].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[4].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[4].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[5].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[5].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[6].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[6].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[7].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[7].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[8].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[8].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[9].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[9].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[10].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[10].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[11].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[11].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[12].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[12].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[13].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[13].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[14].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[14].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[15].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[15].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[16].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[16].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[17].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[17].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[18].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[18].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[19].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[19].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[20].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[20].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[21].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[21].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[22].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[22].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[23].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[23].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[24].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[24].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[25].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[25].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[26].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[26].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[27].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[27].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[28].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[28].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[29].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[29].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[30].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[30].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[31].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[31].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[32].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[32].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[33].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[33].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[34].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[34].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[35].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[35].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[36].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[36].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[37].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[37].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[38].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[38].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[39].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[39].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[40].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[40].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[41].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[41].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[42].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[42].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[43].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[43].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[44].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[44].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[45].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[45].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[46].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[46].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[47].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[47].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[48].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[48].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[49].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[49].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[50].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[50].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[51].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[51].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[52].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[52].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[53].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[53].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[54].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[54].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[55].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[55].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[56].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[56].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[57].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[57].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[58].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[58].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[59].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[59].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[60].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[60].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[61].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[61].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[62].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[62].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[63].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[63].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[64].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[64].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[65].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[65].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[66].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[66].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[67].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[67].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[68].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[68].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[69].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[69].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[70].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[70].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[71].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[71].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[72].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[72].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[73].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[73].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[74].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[74].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[75].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[75].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[76].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[76].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[77].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[77].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[78].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[78].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[79].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[79].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[80].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[80].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[81].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[81].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[82].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[82].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[83].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[83].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[84].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[84].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[85].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[85].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[86].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[86].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[87].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[87].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[88].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[88].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[89].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[89].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[90].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[90].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[91].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[91].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[92].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[92].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[93].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[93].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[94].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[94].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[95].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[95].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[96].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[96].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[97].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[97].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[98].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[98].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[99].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[99].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[100].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[100].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[101].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[101].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[102].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[102].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[103].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[103].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[104].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[104].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[105].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[105].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[106].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[106].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[107].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[107].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[108].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[108].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[109].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[109].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[110].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[110].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[111].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[111].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[112].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[112].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[113].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[113].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[114].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[114].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[115].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[115].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[116].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[116].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[117].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[117].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[118].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[118].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[119].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[119].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[120].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[120].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[121].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[121].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[122].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[122].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[123].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[123].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[124].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[124].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[125].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[125].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[126].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[126].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[127].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[127].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[128].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[128].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[129].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[129].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[130].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[130].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[131].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[131].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[132].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[132].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[133].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[133].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[134].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[134].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[135].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[135].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[136].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[136].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[137].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[137].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[138].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[138].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[139].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[139].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[140].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[140].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[141].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[141].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[142].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[142].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[143].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[143].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[144].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[144].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[145].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[145].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[146].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[146].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[147].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[147].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[148].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[148].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[149].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[149].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[150].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[150].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[151].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[151].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[152].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[152].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[153].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[153].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[154].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[154].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[155].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[155].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[156].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[156].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[157].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[157].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[158].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[158].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[159].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[159].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[160].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[160].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[161].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[161].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[162].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[162].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[163].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[163].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[164].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[164].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[165].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[165].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[166].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[166].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[167].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[167].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[168].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[168].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[169].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[169].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[170].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[170].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[171].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[171].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[172].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[172].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[173].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[173].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[174].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[174].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[175].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[175].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[176].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[176].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[177].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[177].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[178].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[178].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[179].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[179].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[180].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[180].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[181].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[181].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[182].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[182].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[183].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[183].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[184].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[184].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[185].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[185].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[186].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[186].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[187].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[187].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[188].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[188].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[189].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[189].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[190].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[190].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[191].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[191].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[192].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[192].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[193].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[193].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[194].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[194].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[195].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[195].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[196].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[196].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[197].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[197].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[198].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[198].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[199].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[199].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[200].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[200].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[201].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[201].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[202].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[202].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[203].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[203].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[204].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[204].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[205].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[205].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[206].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[206].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[207].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[207].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[208].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[208].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[209].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[209].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[210].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[210].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[211].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[211].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[212].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[212].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[213].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[213].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[214].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[214].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[215].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[215].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[216].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[216].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[217].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[217].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[218].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[218].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[219].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[219].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[220].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[220].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[221].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[221].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[222].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[222].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[223].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[223].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[224].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[224].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[225].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[225].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[226].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[226].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[227].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[227].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[228].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[228].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[229].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[229].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[230].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[230].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[231].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[231].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[232].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[232].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[233].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[233].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[234].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[234].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[235].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[235].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[236].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[236].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[237].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[237].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[238].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[238].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[239].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[239].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[240].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[240].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[241].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[241].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[242].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[242].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[243].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[243].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[244].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[244].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[245].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[245].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[246].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[246].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[247].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[247].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[248].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[248].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[249].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[249].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[250].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[250].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[251].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[251].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[252].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[252].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[253].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[253].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[254].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[254].data.udp,{})
            
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[255].data'):
            
            
            self.assertDictEqual(self.dut.endpoint_interface.rmem.word[255].data.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.info.table_depth'):
            
            
            self.assertDictEqual(self.dut.switch_interface.info.table_depth.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.info.num_of_interfaces'):
            
            
            self.assertDictEqual(self.dut.switch_interface.info.num_of_interfaces.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_control.operation_mode'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_control.operation_mode.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_control.pause_request'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_control.pause_request.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_control.pause_done'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_control.pause_done.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.default_forwarding.bitmap'):
            
            
            self.assertDictEqual(self.dut.switch_interface.default_forwarding.bitmap.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[0].mac_address.lo_word'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.entry[0].mac_address.lo_word.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[0].mac_address.hi_word'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.entry[0].mac_address.hi_word.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[0].iface.bitmap'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.entry[0].iface.bitmap.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[0].config.enabled'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.entry[0].config.enabled.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[1].mac_address.lo_word'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.entry[1].mac_address.lo_word.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[1].mac_address.hi_word'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.entry[1].mac_address.hi_word.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[1].iface.bitmap'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.entry[1].iface.bitmap.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[1].config.enabled'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.entry[1].config.enabled.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[2].mac_address.lo_word'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.entry[2].mac_address.lo_word.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[2].mac_address.hi_word'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.entry[2].mac_address.hi_word.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[2].iface.bitmap'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.entry[2].iface.bitmap.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[2].config.enabled'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.entry[2].config.enabled.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[3].mac_address.lo_word'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.entry[3].mac_address.lo_word.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[3].mac_address.hi_word'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.entry[3].mac_address.hi_word.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[3].iface.bitmap'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.entry[3].iface.bitmap.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[3].config.enabled'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.entry[3].config.enabled.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[4].mac_address.lo_word'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.entry[4].mac_address.lo_word.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[4].mac_address.hi_word'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.entry[4].mac_address.hi_word.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[4].iface.bitmap'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.entry[4].iface.bitmap.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[4].config.enabled'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.entry[4].config.enabled.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[5].mac_address.lo_word'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.entry[5].mac_address.lo_word.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[5].mac_address.hi_word'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.entry[5].mac_address.hi_word.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[5].iface.bitmap'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.entry[5].iface.bitmap.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[5].config.enabled'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.entry[5].config.enabled.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[6].mac_address.lo_word'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.entry[6].mac_address.lo_word.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[6].mac_address.hi_word'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.entry[6].mac_address.hi_word.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[6].iface.bitmap'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.entry[6].iface.bitmap.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[6].config.enabled'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.entry[6].config.enabled.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[7].mac_address.lo_word'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.entry[7].mac_address.lo_word.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[7].mac_address.hi_word'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.entry[7].mac_address.hi_word.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[7].iface.bitmap'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.entry[7].iface.bitmap.udp,{})
            
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[7].config.enabled'):
            
            
            self.assertDictEqual(self.dut.switch_interface.forwarding_table.entry[7].config.enabled.udp,{})
            
        

     

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
        with self.subTest(msg='register: csr.regB'):
            self._single_register_property_test(rut=self.dut.regB, address=4, width=32, accesswidth=32, size=4,
                                                rdl_name=None,
                                                rdl_desc=None,
                                                inst_name='regB',
                                                parent_full_inst_name='csr')
            self._single_register_read_and_write_test(rut=self.dut.regB, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['f0','f1','f2','f3', ]),
                                                                                          writeable_fields=set(['f0','f1','f2','f3', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.info'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.info, address=2048, width=64, accesswidth=32, size=8,
                                                rdl_name="csr.endpoint_interface.info",
                                                rdl_desc="Read-only information register for this openENOC Endpoint Interface instance.",
                                                inst_name='info',
                                                parent_full_inst_name='csr.endpoint_interface')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.info, has_sw_readable=True, has_sw_writable=False,
                                                                                          readable_fields=set(['rmem_total_depth','num_of_peers', ]),
                                                                                          writeable_fields=set([ ]) )
        with self.subTest(msg='register: csr.endpoint_interface.config.mac_address'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.config.mac_address, address=2056, width=64, accesswidth=32, size=8,
                                                rdl_name="csr.endpoint_interface.config.mac_address",
                                                rdl_desc="Local site 48-bit destination MAC address.",
                                                inst_name='mac_address',
                                                parent_full_inst_name='csr.endpoint_interface.config')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.config.mac_address, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['lo_word','hi_word', ]),
                                                                                          writeable_fields=set(['lo_word','hi_word', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.axis_if.source.data'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.axis_if.source.data, address=2080, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.axis_if.source.data",
                                                rdl_desc="Data register for the AXI4-Stream source interface.",
                                                inst_name='data',
                                                parent_full_inst_name='csr.endpoint_interface.axis_if.source')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.axis_if.source.data, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['tdata', ]),
                                                                                          writeable_fields=set(['tdata', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.axis_if.source.control'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.axis_if.source.control, address=2084, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.axis_if.source.control",
                                                rdl_desc="Control register for the AXI4-Stream source interface.",
                                                inst_name='control',
                                                parent_full_inst_name='csr.endpoint_interface.axis_if.source')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.axis_if.source.control, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['tvalid','tlast','tkeep', ]),
                                                                                          writeable_fields=set(['tvalid','tlast','tkeep', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.axis_if.source.status'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.axis_if.source.status, address=2088, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.axis_if.source.status",
                                                rdl_desc="Status register for the AXI4-Stream source interface.",
                                                inst_name='status',
                                                parent_full_inst_name='csr.endpoint_interface.axis_if.source')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.axis_if.source.status, has_sw_readable=True, has_sw_writable=False,
                                                                                          readable_fields=set(['tready', ]),
                                                                                          writeable_fields=set([ ]) )
        with self.subTest(msg='register: csr.endpoint_interface.axis_if.sink.data'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.axis_if.sink.data, address=2096, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.axis_if.sink.data",
                                                rdl_desc="Data register for the AXI4-Stream sink interface.",
                                                inst_name='data',
                                                parent_full_inst_name='csr.endpoint_interface.axis_if.sink')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.axis_if.sink.data, has_sw_readable=True, has_sw_writable=False,
                                                                                          readable_fields=set(['tdata', ]),
                                                                                          writeable_fields=set([ ]) )
        with self.subTest(msg='register: csr.endpoint_interface.axis_if.sink.control'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.axis_if.sink.control, address=2100, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.axis_if.sink.control",
                                                rdl_desc="Control register for the AXI4-Stream sink interface.",
                                                inst_name='control',
                                                parent_full_inst_name='csr.endpoint_interface.axis_if.sink')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.axis_if.sink.control, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['tready', ]),
                                                                                          writeable_fields=set(['tready', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.axis_if.sink.status'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.axis_if.sink.status, address=2104, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.axis_if.sink.status",
                                                rdl_desc="Status register for the AXI4-Stream sink interface.",
                                                inst_name='status',
                                                parent_full_inst_name='csr.endpoint_interface.axis_if.sink')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.axis_if.sink.status, has_sw_readable=True, has_sw_writable=False,
                                                                                          readable_fields=set(['tvalid','tlast','tkeep', ]),
                                                                                          writeable_fields=set([ ]) )
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[0].mac_address'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.peers.entry[0].mac_address, address=2176, width=64, accesswidth=32, size=8,
                                                rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].mac_address",
                                                rdl_desc="Remote peer 48-bit destination MAC address.",
                                                inst_name='mac_address',
                                                parent_full_inst_name='csr.endpoint_interface.peers.entry[0]')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.peers.entry[0].mac_address, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['lo_word','hi_word', ]),
                                                                                          writeable_fields=set(['lo_word','hi_word', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[0].rmem_address'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.peers.entry[0].rmem_address, address=2184, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].rmem_address",
                                                rdl_desc="Address offset of the virtual memory region corresponding to the remote peer\u0027s memory.",
                                                inst_name='rmem_address',
                                                parent_full_inst_name='csr.endpoint_interface.peers.entry[0]')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.peers.entry[0].rmem_address, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['offset', ]),
                                                                                          writeable_fields=set(['offset', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[0].local_address'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.peers.entry[0].local_address, address=2188, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].local_address",
                                                rdl_desc="Start address of the local memory region for DMA transfers.",
                                                inst_name='local_address',
                                                parent_full_inst_name='csr.endpoint_interface.peers.entry[0]')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.peers.entry[0].local_address, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['base', ]),
                                                                                          writeable_fields=set(['base', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[0].remote_address'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.peers.entry[0].remote_address, address=2192, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].remote_address",
                                                rdl_desc="Start address of the remote peer\u0027s memory region.",
                                                inst_name='remote_address',
                                                parent_full_inst_name='csr.endpoint_interface.peers.entry[0]')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.peers.entry[0].remote_address, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['base', ]),
                                                                                          writeable_fields=set(['base', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[0].size'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.peers.entry[0].register_size, address=2196, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].size",
                                                rdl_desc="Size of the remote peer\u0027s memory region.",
                                                inst_name='size',
                                                parent_full_inst_name='csr.endpoint_interface.peers.entry[0]')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.peers.entry[0].register_size, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['bytes', ]),
                                                                                          writeable_fields=set(['bytes', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[0].dma'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.peers.entry[0].dma, address=2200, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma",
                                                rdl_desc="DMA configuration and control for the remote peer.",
                                                inst_name='dma',
                                                parent_full_inst_name='csr.endpoint_interface.peers.entry[0]')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.peers.entry[0].dma, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['mode','request','idle','done','error', ]),
                                                                                          writeable_fields=set(['mode','request', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[1].mac_address'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.peers.entry[1].mac_address, address=2204, width=64, accesswidth=32, size=8,
                                                rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].mac_address",
                                                rdl_desc="Remote peer 48-bit destination MAC address.",
                                                inst_name='mac_address',
                                                parent_full_inst_name='csr.endpoint_interface.peers.entry[1]')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.peers.entry[1].mac_address, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['lo_word','hi_word', ]),
                                                                                          writeable_fields=set(['lo_word','hi_word', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[1].rmem_address'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.peers.entry[1].rmem_address, address=2212, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].rmem_address",
                                                rdl_desc="Address offset of the virtual memory region corresponding to the remote peer\u0027s memory.",
                                                inst_name='rmem_address',
                                                parent_full_inst_name='csr.endpoint_interface.peers.entry[1]')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.peers.entry[1].rmem_address, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['offset', ]),
                                                                                          writeable_fields=set(['offset', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[1].local_address'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.peers.entry[1].local_address, address=2216, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].local_address",
                                                rdl_desc="Start address of the local memory region for DMA transfers.",
                                                inst_name='local_address',
                                                parent_full_inst_name='csr.endpoint_interface.peers.entry[1]')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.peers.entry[1].local_address, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['base', ]),
                                                                                          writeable_fields=set(['base', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[1].remote_address'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.peers.entry[1].remote_address, address=2220, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].remote_address",
                                                rdl_desc="Start address of the remote peer\u0027s memory region.",
                                                inst_name='remote_address',
                                                parent_full_inst_name='csr.endpoint_interface.peers.entry[1]')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.peers.entry[1].remote_address, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['base', ]),
                                                                                          writeable_fields=set(['base', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[1].size'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.peers.entry[1].register_size, address=2224, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].size",
                                                rdl_desc="Size of the remote peer\u0027s memory region.",
                                                inst_name='size',
                                                parent_full_inst_name='csr.endpoint_interface.peers.entry[1]')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.peers.entry[1].register_size, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['bytes', ]),
                                                                                          writeable_fields=set(['bytes', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[1].dma'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.peers.entry[1].dma, address=2228, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma",
                                                rdl_desc="DMA configuration and control for the remote peer.",
                                                inst_name='dma',
                                                parent_full_inst_name='csr.endpoint_interface.peers.entry[1]')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.peers.entry[1].dma, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['mode','request','idle','done','error', ]),
                                                                                          writeable_fields=set(['mode','request', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[2].mac_address'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.peers.entry[2].mac_address, address=2232, width=64, accesswidth=32, size=8,
                                                rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].mac_address",
                                                rdl_desc="Remote peer 48-bit destination MAC address.",
                                                inst_name='mac_address',
                                                parent_full_inst_name='csr.endpoint_interface.peers.entry[2]')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.peers.entry[2].mac_address, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['lo_word','hi_word', ]),
                                                                                          writeable_fields=set(['lo_word','hi_word', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[2].rmem_address'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.peers.entry[2].rmem_address, address=2240, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].rmem_address",
                                                rdl_desc="Address offset of the virtual memory region corresponding to the remote peer\u0027s memory.",
                                                inst_name='rmem_address',
                                                parent_full_inst_name='csr.endpoint_interface.peers.entry[2]')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.peers.entry[2].rmem_address, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['offset', ]),
                                                                                          writeable_fields=set(['offset', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[2].local_address'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.peers.entry[2].local_address, address=2244, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].local_address",
                                                rdl_desc="Start address of the local memory region for DMA transfers.",
                                                inst_name='local_address',
                                                parent_full_inst_name='csr.endpoint_interface.peers.entry[2]')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.peers.entry[2].local_address, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['base', ]),
                                                                                          writeable_fields=set(['base', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[2].remote_address'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.peers.entry[2].remote_address, address=2248, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].remote_address",
                                                rdl_desc="Start address of the remote peer\u0027s memory region.",
                                                inst_name='remote_address',
                                                parent_full_inst_name='csr.endpoint_interface.peers.entry[2]')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.peers.entry[2].remote_address, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['base', ]),
                                                                                          writeable_fields=set(['base', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[2].size'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.peers.entry[2].register_size, address=2252, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].size",
                                                rdl_desc="Size of the remote peer\u0027s memory region.",
                                                inst_name='size',
                                                parent_full_inst_name='csr.endpoint_interface.peers.entry[2]')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.peers.entry[2].register_size, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['bytes', ]),
                                                                                          writeable_fields=set(['bytes', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[2].dma'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.peers.entry[2].dma, address=2256, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma",
                                                rdl_desc="DMA configuration and control for the remote peer.",
                                                inst_name='dma',
                                                parent_full_inst_name='csr.endpoint_interface.peers.entry[2]')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.peers.entry[2].dma, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['mode','request','idle','done','error', ]),
                                                                                          writeable_fields=set(['mode','request', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[3].mac_address'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.peers.entry[3].mac_address, address=2260, width=64, accesswidth=32, size=8,
                                                rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].mac_address",
                                                rdl_desc="Remote peer 48-bit destination MAC address.",
                                                inst_name='mac_address',
                                                parent_full_inst_name='csr.endpoint_interface.peers.entry[3]')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.peers.entry[3].mac_address, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['lo_word','hi_word', ]),
                                                                                          writeable_fields=set(['lo_word','hi_word', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[3].rmem_address'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.peers.entry[3].rmem_address, address=2268, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].rmem_address",
                                                rdl_desc="Address offset of the virtual memory region corresponding to the remote peer\u0027s memory.",
                                                inst_name='rmem_address',
                                                parent_full_inst_name='csr.endpoint_interface.peers.entry[3]')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.peers.entry[3].rmem_address, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['offset', ]),
                                                                                          writeable_fields=set(['offset', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[3].local_address'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.peers.entry[3].local_address, address=2272, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].local_address",
                                                rdl_desc="Start address of the local memory region for DMA transfers.",
                                                inst_name='local_address',
                                                parent_full_inst_name='csr.endpoint_interface.peers.entry[3]')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.peers.entry[3].local_address, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['base', ]),
                                                                                          writeable_fields=set(['base', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[3].remote_address'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.peers.entry[3].remote_address, address=2276, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].remote_address",
                                                rdl_desc="Start address of the remote peer\u0027s memory region.",
                                                inst_name='remote_address',
                                                parent_full_inst_name='csr.endpoint_interface.peers.entry[3]')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.peers.entry[3].remote_address, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['base', ]),
                                                                                          writeable_fields=set(['base', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[3].size'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.peers.entry[3].register_size, address=2280, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].size",
                                                rdl_desc="Size of the remote peer\u0027s memory region.",
                                                inst_name='size',
                                                parent_full_inst_name='csr.endpoint_interface.peers.entry[3]')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.peers.entry[3].register_size, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['bytes', ]),
                                                                                          writeable_fields=set(['bytes', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.peers.entry[3].dma'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.peers.entry[3].dma, address=2284, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma",
                                                rdl_desc="DMA configuration and control for the remote peer.",
                                                inst_name='dma',
                                                parent_full_inst_name='csr.endpoint_interface.peers.entry[3]')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.peers.entry[3].dma, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['mode','request','idle','done','error', ]),
                                                                                          writeable_fields=set(['mode','request', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[0]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[0], address=3072, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[0]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[0], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[1]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[1], address=3076, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[1]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[1], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[2]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[2], address=3080, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[2]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[2], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[3]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[3], address=3084, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[3]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[3], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[4]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[4], address=3088, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[4]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[4], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[5]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[5], address=3092, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[5]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[5], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[6]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[6], address=3096, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[6]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[6], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[7]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[7], address=3100, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[7]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[7], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[8]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[8], address=3104, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[8]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[8], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[9]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[9], address=3108, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[9]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[9], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[10]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[10], address=3112, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[10]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[10], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[11]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[11], address=3116, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[11]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[11], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[12]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[12], address=3120, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[12]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[12], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[13]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[13], address=3124, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[13]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[13], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[14]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[14], address=3128, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[14]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[14], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[15]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[15], address=3132, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[15]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[15], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[16]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[16], address=3136, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[16]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[16], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[17]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[17], address=3140, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[17]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[17], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[18]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[18], address=3144, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[18]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[18], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[19]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[19], address=3148, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[19]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[19], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[20]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[20], address=3152, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[20]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[20], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[21]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[21], address=3156, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[21]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[21], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[22]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[22], address=3160, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[22]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[22], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[23]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[23], address=3164, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[23]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[23], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[24]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[24], address=3168, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[24]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[24], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[25]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[25], address=3172, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[25]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[25], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[26]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[26], address=3176, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[26]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[26], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[27]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[27], address=3180, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[27]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[27], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[28]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[28], address=3184, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[28]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[28], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[29]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[29], address=3188, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[29]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[29], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[30]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[30], address=3192, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[30]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[30], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[31]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[31], address=3196, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[31]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[31], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[32]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[32], address=3200, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[32]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[32], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[33]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[33], address=3204, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[33]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[33], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[34]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[34], address=3208, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[34]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[34], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[35]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[35], address=3212, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[35]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[35], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[36]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[36], address=3216, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[36]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[36], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[37]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[37], address=3220, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[37]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[37], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[38]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[38], address=3224, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[38]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[38], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[39]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[39], address=3228, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[39]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[39], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[40]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[40], address=3232, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[40]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[40], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[41]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[41], address=3236, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[41]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[41], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[42]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[42], address=3240, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[42]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[42], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[43]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[43], address=3244, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[43]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[43], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[44]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[44], address=3248, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[44]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[44], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[45]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[45], address=3252, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[45]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[45], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[46]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[46], address=3256, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[46]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[46], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[47]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[47], address=3260, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[47]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[47], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[48]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[48], address=3264, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[48]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[48], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[49]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[49], address=3268, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[49]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[49], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[50]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[50], address=3272, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[50]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[50], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[51]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[51], address=3276, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[51]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[51], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[52]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[52], address=3280, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[52]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[52], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[53]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[53], address=3284, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[53]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[53], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[54]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[54], address=3288, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[54]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[54], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[55]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[55], address=3292, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[55]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[55], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[56]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[56], address=3296, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[56]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[56], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[57]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[57], address=3300, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[57]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[57], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[58]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[58], address=3304, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[58]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[58], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[59]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[59], address=3308, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[59]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[59], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[60]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[60], address=3312, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[60]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[60], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[61]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[61], address=3316, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[61]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[61], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[62]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[62], address=3320, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[62]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[62], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[63]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[63], address=3324, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[63]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[63], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[64]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[64], address=3328, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[64]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[64], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[65]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[65], address=3332, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[65]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[65], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[66]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[66], address=3336, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[66]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[66], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[67]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[67], address=3340, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[67]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[67], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[68]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[68], address=3344, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[68]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[68], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[69]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[69], address=3348, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[69]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[69], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[70]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[70], address=3352, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[70]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[70], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[71]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[71], address=3356, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[71]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[71], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[72]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[72], address=3360, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[72]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[72], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[73]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[73], address=3364, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[73]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[73], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[74]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[74], address=3368, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[74]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[74], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[75]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[75], address=3372, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[75]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[75], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[76]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[76], address=3376, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[76]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[76], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[77]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[77], address=3380, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[77]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[77], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[78]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[78], address=3384, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[78]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[78], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[79]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[79], address=3388, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[79]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[79], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[80]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[80], address=3392, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[80]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[80], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[81]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[81], address=3396, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[81]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[81], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[82]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[82], address=3400, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[82]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[82], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[83]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[83], address=3404, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[83]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[83], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[84]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[84], address=3408, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[84]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[84], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[85]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[85], address=3412, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[85]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[85], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[86]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[86], address=3416, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[86]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[86], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[87]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[87], address=3420, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[87]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[87], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[88]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[88], address=3424, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[88]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[88], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[89]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[89], address=3428, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[89]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[89], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[90]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[90], address=3432, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[90]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[90], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[91]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[91], address=3436, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[91]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[91], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[92]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[92], address=3440, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[92]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[92], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[93]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[93], address=3444, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[93]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[93], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[94]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[94], address=3448, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[94]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[94], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[95]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[95], address=3452, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[95]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[95], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[96]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[96], address=3456, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[96]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[96], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[97]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[97], address=3460, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[97]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[97], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[98]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[98], address=3464, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[98]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[98], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[99]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[99], address=3468, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[99]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[99], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[100]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[100], address=3472, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[100]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[100], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[101]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[101], address=3476, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[101]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[101], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[102]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[102], address=3480, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[102]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[102], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[103]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[103], address=3484, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[103]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[103], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[104]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[104], address=3488, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[104]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[104], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[105]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[105], address=3492, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[105]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[105], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[106]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[106], address=3496, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[106]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[106], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[107]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[107], address=3500, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[107]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[107], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[108]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[108], address=3504, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[108]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[108], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[109]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[109], address=3508, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[109]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[109], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[110]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[110], address=3512, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[110]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[110], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[111]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[111], address=3516, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[111]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[111], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[112]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[112], address=3520, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[112]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[112], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[113]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[113], address=3524, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[113]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[113], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[114]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[114], address=3528, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[114]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[114], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[115]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[115], address=3532, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[115]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[115], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[116]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[116], address=3536, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[116]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[116], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[117]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[117], address=3540, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[117]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[117], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[118]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[118], address=3544, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[118]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[118], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[119]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[119], address=3548, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[119]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[119], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[120]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[120], address=3552, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[120]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[120], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[121]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[121], address=3556, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[121]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[121], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[122]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[122], address=3560, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[122]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[122], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[123]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[123], address=3564, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[123]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[123], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[124]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[124], address=3568, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[124]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[124], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[125]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[125], address=3572, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[125]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[125], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[126]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[126], address=3576, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[126]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[126], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[127]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[127], address=3580, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[127]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[127], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[128]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[128], address=3584, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[128]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[128], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[129]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[129], address=3588, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[129]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[129], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[130]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[130], address=3592, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[130]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[130], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[131]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[131], address=3596, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[131]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[131], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[132]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[132], address=3600, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[132]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[132], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[133]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[133], address=3604, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[133]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[133], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[134]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[134], address=3608, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[134]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[134], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[135]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[135], address=3612, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[135]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[135], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[136]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[136], address=3616, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[136]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[136], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[137]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[137], address=3620, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[137]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[137], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[138]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[138], address=3624, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[138]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[138], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[139]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[139], address=3628, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[139]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[139], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[140]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[140], address=3632, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[140]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[140], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[141]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[141], address=3636, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[141]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[141], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[142]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[142], address=3640, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[142]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[142], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[143]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[143], address=3644, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[143]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[143], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[144]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[144], address=3648, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[144]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[144], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[145]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[145], address=3652, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[145]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[145], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[146]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[146], address=3656, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[146]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[146], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[147]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[147], address=3660, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[147]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[147], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[148]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[148], address=3664, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[148]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[148], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[149]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[149], address=3668, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[149]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[149], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[150]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[150], address=3672, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[150]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[150], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[151]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[151], address=3676, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[151]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[151], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[152]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[152], address=3680, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[152]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[152], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[153]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[153], address=3684, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[153]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[153], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[154]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[154], address=3688, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[154]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[154], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[155]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[155], address=3692, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[155]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[155], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[156]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[156], address=3696, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[156]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[156], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[157]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[157], address=3700, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[157]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[157], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[158]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[158], address=3704, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[158]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[158], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[159]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[159], address=3708, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[159]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[159], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[160]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[160], address=3712, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[160]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[160], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[161]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[161], address=3716, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[161]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[161], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[162]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[162], address=3720, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[162]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[162], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[163]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[163], address=3724, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[163]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[163], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[164]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[164], address=3728, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[164]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[164], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[165]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[165], address=3732, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[165]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[165], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[166]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[166], address=3736, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[166]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[166], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[167]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[167], address=3740, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[167]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[167], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[168]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[168], address=3744, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[168]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[168], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[169]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[169], address=3748, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[169]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[169], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[170]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[170], address=3752, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[170]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[170], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[171]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[171], address=3756, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[171]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[171], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[172]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[172], address=3760, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[172]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[172], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[173]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[173], address=3764, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[173]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[173], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[174]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[174], address=3768, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[174]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[174], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[175]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[175], address=3772, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[175]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[175], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[176]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[176], address=3776, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[176]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[176], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[177]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[177], address=3780, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[177]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[177], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[178]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[178], address=3784, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[178]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[178], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[179]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[179], address=3788, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[179]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[179], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[180]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[180], address=3792, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[180]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[180], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[181]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[181], address=3796, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[181]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[181], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[182]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[182], address=3800, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[182]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[182], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[183]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[183], address=3804, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[183]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[183], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[184]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[184], address=3808, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[184]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[184], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[185]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[185], address=3812, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[185]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[185], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[186]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[186], address=3816, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[186]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[186], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[187]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[187], address=3820, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[187]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[187], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[188]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[188], address=3824, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[188]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[188], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[189]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[189], address=3828, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[189]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[189], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[190]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[190], address=3832, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[190]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[190], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[191]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[191], address=3836, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[191]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[191], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[192]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[192], address=3840, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[192]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[192], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[193]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[193], address=3844, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[193]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[193], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[194]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[194], address=3848, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[194]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[194], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[195]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[195], address=3852, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[195]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[195], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[196]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[196], address=3856, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[196]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[196], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[197]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[197], address=3860, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[197]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[197], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[198]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[198], address=3864, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[198]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[198], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[199]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[199], address=3868, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[199]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[199], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[200]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[200], address=3872, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[200]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[200], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[201]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[201], address=3876, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[201]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[201], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[202]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[202], address=3880, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[202]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[202], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[203]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[203], address=3884, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[203]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[203], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[204]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[204], address=3888, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[204]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[204], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[205]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[205], address=3892, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[205]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[205], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[206]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[206], address=3896, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[206]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[206], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[207]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[207], address=3900, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[207]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[207], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[208]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[208], address=3904, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[208]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[208], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[209]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[209], address=3908, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[209]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[209], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[210]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[210], address=3912, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[210]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[210], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[211]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[211], address=3916, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[211]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[211], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[212]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[212], address=3920, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[212]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[212], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[213]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[213], address=3924, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[213]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[213], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[214]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[214], address=3928, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[214]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[214], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[215]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[215], address=3932, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[215]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[215], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[216]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[216], address=3936, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[216]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[216], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[217]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[217], address=3940, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[217]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[217], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[218]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[218], address=3944, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[218]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[218], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[219]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[219], address=3948, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[219]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[219], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[220]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[220], address=3952, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[220]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[220], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[221]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[221], address=3956, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[221]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[221], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[222]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[222], address=3960, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[222]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[222], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[223]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[223], address=3964, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[223]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[223], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[224]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[224], address=3968, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[224]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[224], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[225]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[225], address=3972, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[225]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[225], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[226]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[226], address=3976, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[226]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[226], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[227]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[227], address=3980, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[227]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[227], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[228]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[228], address=3984, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[228]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[228], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[229]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[229], address=3988, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[229]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[229], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[230]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[230], address=3992, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[230]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[230], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[231]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[231], address=3996, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[231]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[231], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[232]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[232], address=4000, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[232]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[232], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[233]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[233], address=4004, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[233]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[233], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[234]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[234], address=4008, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[234]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[234], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[235]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[235], address=4012, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[235]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[235], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[236]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[236], address=4016, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[236]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[236], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[237]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[237], address=4020, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[237]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[237], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[238]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[238], address=4024, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[238]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[238], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[239]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[239], address=4028, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[239]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[239], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[240]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[240], address=4032, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[240]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[240], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[241]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[241], address=4036, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[241]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[241], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[242]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[242], address=4040, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[242]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[242], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[243]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[243], address=4044, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[243]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[243], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[244]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[244], address=4048, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[244]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[244], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[245]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[245], address=4052, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[245]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[245], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[246]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[246], address=4056, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[246]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[246], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[247]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[247], address=4060, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[247]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[247], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[248]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[248], address=4064, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[248]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[248], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[249]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[249], address=4068, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[249]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[249], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[250]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[250], address=4072, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[250]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[250], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[251]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[251], address=4076, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[251]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[251], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[252]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[252], address=4080, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[252]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[252], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[253]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[253], address=4084, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[253]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[253], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[254]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[254], address=4088, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[254]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[254], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[255]'):
            self._single_register_property_test(rut=self.dut.endpoint_interface.rmem.word[255], address=4092, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]",
                                                rdl_desc="32-bit word in the virtual memory region.",
                                                inst_name='word[255]',
                                                parent_full_inst_name='csr.endpoint_interface.rmem')
            self._single_register_read_and_write_test(rut=self.dut.endpoint_interface.rmem.word[255], has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['data', ]),
                                                                                          writeable_fields=set(['data', ]) )
        with self.subTest(msg='register: csr.switch_interface.info'):
            self._single_register_property_test(rut=self.dut.switch_interface.info, address=4096, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch_interface.info",
                                                rdl_desc="Read-only information register for this openENOC Switch instance.",
                                                inst_name='info',
                                                parent_full_inst_name='csr.switch_interface')
            self._single_register_read_and_write_test(rut=self.dut.switch_interface.info, has_sw_readable=True, has_sw_writable=False,
                                                                                          readable_fields=set(['table_depth','num_of_interfaces', ]),
                                                                                          writeable_fields=set([ ]) )
        with self.subTest(msg='register: csr.switch_interface.forwarding_control'):
            self._single_register_property_test(rut=self.dut.switch_interface.forwarding_control, address=4100, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch_interface.forwarding_control",
                                                rdl_desc="Forwarding control register for the openENOC Switch instance.",
                                                inst_name='forwarding_control',
                                                parent_full_inst_name='csr.switch_interface')
            self._single_register_read_and_write_test(rut=self.dut.switch_interface.forwarding_control, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['operation_mode','pause_request','pause_done', ]),
                                                                                          writeable_fields=set(['operation_mode','pause_request', ]) )
        with self.subTest(msg='register: csr.switch_interface.default_forwarding'):
            self._single_register_property_test(rut=self.dut.switch_interface.default_forwarding, address=4104, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch_interface.default_forwarding",
                                                rdl_desc="Defines the destination interface or interfaces for frames that do not match any enabled forwarding table entry.",
                                                inst_name='default_forwarding',
                                                parent_full_inst_name='csr.switch_interface')
            self._single_register_read_and_write_test(rut=self.dut.switch_interface.default_forwarding, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['bitmap', ]),
                                                                                          writeable_fields=set(['bitmap', ]) )
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[0].mac_address'):
            self._single_register_property_test(rut=self.dut.switch_interface.forwarding_table.entry[0].mac_address, address=4224, width=64, accesswidth=32, size=8,
                                                rdl_name="csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address",
                                                rdl_desc="48-bit destination MAC address used as the key for this forwarding table entry.",
                                                inst_name='mac_address',
                                                parent_full_inst_name='csr.switch_interface.forwarding_table.entry[0]')
            self._single_register_read_and_write_test(rut=self.dut.switch_interface.forwarding_table.entry[0].mac_address, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['lo_word','hi_word', ]),
                                                                                          writeable_fields=set(['lo_word','hi_word', ]) )
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[0].iface'):
            self._single_register_property_test(rut=self.dut.switch_interface.forwarding_table.entry[0].iface, address=4232, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].iface",
                                                rdl_desc="Forwarding interface information associated with this forwarding table entry.",
                                                inst_name='iface',
                                                parent_full_inst_name='csr.switch_interface.forwarding_table.entry[0]')
            self._single_register_read_and_write_test(rut=self.dut.switch_interface.forwarding_table.entry[0].iface, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['bitmap', ]),
                                                                                          writeable_fields=set(['bitmap', ]) )
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[0].config'):
            self._single_register_property_test(rut=self.dut.switch_interface.forwarding_table.entry[0].config, address=4236, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].config",
                                                rdl_desc="Configuration information associated with this forwarding table entry.",
                                                inst_name='config',
                                                parent_full_inst_name='csr.switch_interface.forwarding_table.entry[0]')
            self._single_register_read_and_write_test(rut=self.dut.switch_interface.forwarding_table.entry[0].config, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['enabled', ]),
                                                                                          writeable_fields=set(['enabled', ]) )
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[1].mac_address'):
            self._single_register_property_test(rut=self.dut.switch_interface.forwarding_table.entry[1].mac_address, address=4240, width=64, accesswidth=32, size=8,
                                                rdl_name="csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address",
                                                rdl_desc="48-bit destination MAC address used as the key for this forwarding table entry.",
                                                inst_name='mac_address',
                                                parent_full_inst_name='csr.switch_interface.forwarding_table.entry[1]')
            self._single_register_read_and_write_test(rut=self.dut.switch_interface.forwarding_table.entry[1].mac_address, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['lo_word','hi_word', ]),
                                                                                          writeable_fields=set(['lo_word','hi_word', ]) )
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[1].iface'):
            self._single_register_property_test(rut=self.dut.switch_interface.forwarding_table.entry[1].iface, address=4248, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].iface",
                                                rdl_desc="Forwarding interface information associated with this forwarding table entry.",
                                                inst_name='iface',
                                                parent_full_inst_name='csr.switch_interface.forwarding_table.entry[1]')
            self._single_register_read_and_write_test(rut=self.dut.switch_interface.forwarding_table.entry[1].iface, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['bitmap', ]),
                                                                                          writeable_fields=set(['bitmap', ]) )
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[1].config'):
            self._single_register_property_test(rut=self.dut.switch_interface.forwarding_table.entry[1].config, address=4252, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].config",
                                                rdl_desc="Configuration information associated with this forwarding table entry.",
                                                inst_name='config',
                                                parent_full_inst_name='csr.switch_interface.forwarding_table.entry[1]')
            self._single_register_read_and_write_test(rut=self.dut.switch_interface.forwarding_table.entry[1].config, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['enabled', ]),
                                                                                          writeable_fields=set(['enabled', ]) )
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[2].mac_address'):
            self._single_register_property_test(rut=self.dut.switch_interface.forwarding_table.entry[2].mac_address, address=4256, width=64, accesswidth=32, size=8,
                                                rdl_name="csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address",
                                                rdl_desc="48-bit destination MAC address used as the key for this forwarding table entry.",
                                                inst_name='mac_address',
                                                parent_full_inst_name='csr.switch_interface.forwarding_table.entry[2]')
            self._single_register_read_and_write_test(rut=self.dut.switch_interface.forwarding_table.entry[2].mac_address, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['lo_word','hi_word', ]),
                                                                                          writeable_fields=set(['lo_word','hi_word', ]) )
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[2].iface'):
            self._single_register_property_test(rut=self.dut.switch_interface.forwarding_table.entry[2].iface, address=4264, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].iface",
                                                rdl_desc="Forwarding interface information associated with this forwarding table entry.",
                                                inst_name='iface',
                                                parent_full_inst_name='csr.switch_interface.forwarding_table.entry[2]')
            self._single_register_read_and_write_test(rut=self.dut.switch_interface.forwarding_table.entry[2].iface, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['bitmap', ]),
                                                                                          writeable_fields=set(['bitmap', ]) )
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[2].config'):
            self._single_register_property_test(rut=self.dut.switch_interface.forwarding_table.entry[2].config, address=4268, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].config",
                                                rdl_desc="Configuration information associated with this forwarding table entry.",
                                                inst_name='config',
                                                parent_full_inst_name='csr.switch_interface.forwarding_table.entry[2]')
            self._single_register_read_and_write_test(rut=self.dut.switch_interface.forwarding_table.entry[2].config, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['enabled', ]),
                                                                                          writeable_fields=set(['enabled', ]) )
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[3].mac_address'):
            self._single_register_property_test(rut=self.dut.switch_interface.forwarding_table.entry[3].mac_address, address=4272, width=64, accesswidth=32, size=8,
                                                rdl_name="csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address",
                                                rdl_desc="48-bit destination MAC address used as the key for this forwarding table entry.",
                                                inst_name='mac_address',
                                                parent_full_inst_name='csr.switch_interface.forwarding_table.entry[3]')
            self._single_register_read_and_write_test(rut=self.dut.switch_interface.forwarding_table.entry[3].mac_address, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['lo_word','hi_word', ]),
                                                                                          writeable_fields=set(['lo_word','hi_word', ]) )
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[3].iface'):
            self._single_register_property_test(rut=self.dut.switch_interface.forwarding_table.entry[3].iface, address=4280, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].iface",
                                                rdl_desc="Forwarding interface information associated with this forwarding table entry.",
                                                inst_name='iface',
                                                parent_full_inst_name='csr.switch_interface.forwarding_table.entry[3]')
            self._single_register_read_and_write_test(rut=self.dut.switch_interface.forwarding_table.entry[3].iface, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['bitmap', ]),
                                                                                          writeable_fields=set(['bitmap', ]) )
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[3].config'):
            self._single_register_property_test(rut=self.dut.switch_interface.forwarding_table.entry[3].config, address=4284, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].config",
                                                rdl_desc="Configuration information associated with this forwarding table entry.",
                                                inst_name='config',
                                                parent_full_inst_name='csr.switch_interface.forwarding_table.entry[3]')
            self._single_register_read_and_write_test(rut=self.dut.switch_interface.forwarding_table.entry[3].config, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['enabled', ]),
                                                                                          writeable_fields=set(['enabled', ]) )
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[4].mac_address'):
            self._single_register_property_test(rut=self.dut.switch_interface.forwarding_table.entry[4].mac_address, address=4288, width=64, accesswidth=32, size=8,
                                                rdl_name="csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address",
                                                rdl_desc="48-bit destination MAC address used as the key for this forwarding table entry.",
                                                inst_name='mac_address',
                                                parent_full_inst_name='csr.switch_interface.forwarding_table.entry[4]')
            self._single_register_read_and_write_test(rut=self.dut.switch_interface.forwarding_table.entry[4].mac_address, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['lo_word','hi_word', ]),
                                                                                          writeable_fields=set(['lo_word','hi_word', ]) )
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[4].iface'):
            self._single_register_property_test(rut=self.dut.switch_interface.forwarding_table.entry[4].iface, address=4296, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].iface",
                                                rdl_desc="Forwarding interface information associated with this forwarding table entry.",
                                                inst_name='iface',
                                                parent_full_inst_name='csr.switch_interface.forwarding_table.entry[4]')
            self._single_register_read_and_write_test(rut=self.dut.switch_interface.forwarding_table.entry[4].iface, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['bitmap', ]),
                                                                                          writeable_fields=set(['bitmap', ]) )
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[4].config'):
            self._single_register_property_test(rut=self.dut.switch_interface.forwarding_table.entry[4].config, address=4300, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].config",
                                                rdl_desc="Configuration information associated with this forwarding table entry.",
                                                inst_name='config',
                                                parent_full_inst_name='csr.switch_interface.forwarding_table.entry[4]')
            self._single_register_read_and_write_test(rut=self.dut.switch_interface.forwarding_table.entry[4].config, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['enabled', ]),
                                                                                          writeable_fields=set(['enabled', ]) )
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[5].mac_address'):
            self._single_register_property_test(rut=self.dut.switch_interface.forwarding_table.entry[5].mac_address, address=4304, width=64, accesswidth=32, size=8,
                                                rdl_name="csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address",
                                                rdl_desc="48-bit destination MAC address used as the key for this forwarding table entry.",
                                                inst_name='mac_address',
                                                parent_full_inst_name='csr.switch_interface.forwarding_table.entry[5]')
            self._single_register_read_and_write_test(rut=self.dut.switch_interface.forwarding_table.entry[5].mac_address, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['lo_word','hi_word', ]),
                                                                                          writeable_fields=set(['lo_word','hi_word', ]) )
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[5].iface'):
            self._single_register_property_test(rut=self.dut.switch_interface.forwarding_table.entry[5].iface, address=4312, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].iface",
                                                rdl_desc="Forwarding interface information associated with this forwarding table entry.",
                                                inst_name='iface',
                                                parent_full_inst_name='csr.switch_interface.forwarding_table.entry[5]')
            self._single_register_read_and_write_test(rut=self.dut.switch_interface.forwarding_table.entry[5].iface, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['bitmap', ]),
                                                                                          writeable_fields=set(['bitmap', ]) )
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[5].config'):
            self._single_register_property_test(rut=self.dut.switch_interface.forwarding_table.entry[5].config, address=4316, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].config",
                                                rdl_desc="Configuration information associated with this forwarding table entry.",
                                                inst_name='config',
                                                parent_full_inst_name='csr.switch_interface.forwarding_table.entry[5]')
            self._single_register_read_and_write_test(rut=self.dut.switch_interface.forwarding_table.entry[5].config, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['enabled', ]),
                                                                                          writeable_fields=set(['enabled', ]) )
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[6].mac_address'):
            self._single_register_property_test(rut=self.dut.switch_interface.forwarding_table.entry[6].mac_address, address=4320, width=64, accesswidth=32, size=8,
                                                rdl_name="csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address",
                                                rdl_desc="48-bit destination MAC address used as the key for this forwarding table entry.",
                                                inst_name='mac_address',
                                                parent_full_inst_name='csr.switch_interface.forwarding_table.entry[6]')
            self._single_register_read_and_write_test(rut=self.dut.switch_interface.forwarding_table.entry[6].mac_address, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['lo_word','hi_word', ]),
                                                                                          writeable_fields=set(['lo_word','hi_word', ]) )
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[6].iface'):
            self._single_register_property_test(rut=self.dut.switch_interface.forwarding_table.entry[6].iface, address=4328, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].iface",
                                                rdl_desc="Forwarding interface information associated with this forwarding table entry.",
                                                inst_name='iface',
                                                parent_full_inst_name='csr.switch_interface.forwarding_table.entry[6]')
            self._single_register_read_and_write_test(rut=self.dut.switch_interface.forwarding_table.entry[6].iface, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['bitmap', ]),
                                                                                          writeable_fields=set(['bitmap', ]) )
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[6].config'):
            self._single_register_property_test(rut=self.dut.switch_interface.forwarding_table.entry[6].config, address=4332, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].config",
                                                rdl_desc="Configuration information associated with this forwarding table entry.",
                                                inst_name='config',
                                                parent_full_inst_name='csr.switch_interface.forwarding_table.entry[6]')
            self._single_register_read_and_write_test(rut=self.dut.switch_interface.forwarding_table.entry[6].config, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['enabled', ]),
                                                                                          writeable_fields=set(['enabled', ]) )
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[7].mac_address'):
            self._single_register_property_test(rut=self.dut.switch_interface.forwarding_table.entry[7].mac_address, address=4336, width=64, accesswidth=32, size=8,
                                                rdl_name="csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address",
                                                rdl_desc="48-bit destination MAC address used as the key for this forwarding table entry.",
                                                inst_name='mac_address',
                                                parent_full_inst_name='csr.switch_interface.forwarding_table.entry[7]')
            self._single_register_read_and_write_test(rut=self.dut.switch_interface.forwarding_table.entry[7].mac_address, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['lo_word','hi_word', ]),
                                                                                          writeable_fields=set(['lo_word','hi_word', ]) )
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[7].iface'):
            self._single_register_property_test(rut=self.dut.switch_interface.forwarding_table.entry[7].iface, address=4344, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].iface",
                                                rdl_desc="Forwarding interface information associated with this forwarding table entry.",
                                                inst_name='iface',
                                                parent_full_inst_name='csr.switch_interface.forwarding_table.entry[7]')
            self._single_register_read_and_write_test(rut=self.dut.switch_interface.forwarding_table.entry[7].iface, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['bitmap', ]),
                                                                                          writeable_fields=set(['bitmap', ]) )
        with self.subTest(msg='register: csr.switch_interface.forwarding_table.entry[7].config'):
            self._single_register_property_test(rut=self.dut.switch_interface.forwarding_table.entry[7].config, address=4348, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].config",
                                                rdl_desc="Configuration information associated with this forwarding table entry.",
                                                inst_name='config',
                                                parent_full_inst_name='csr.switch_interface.forwarding_table.entry[7]')
            self._single_register_read_and_write_test(rut=self.dut.switch_interface.forwarding_table.entry[7].config, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['enabled', ]),
                                                                                          writeable_fields=set(['enabled', ]) )
        

    def test_field(self) -> None:
        """
        Check the properties and function (read and write) on the fields both integer and enum
        """
        
        with self.subTest(msg='field: csr.test_reg.test_field'):
            self._single_field_property_test(fut=self.dut.test_reg.test_field, lsb=0, msb=31, low=0, high=31, is_volatile=False, default=0,
                                             rdl_name="csr.test_reg.test_field[31:0]",
                                             rdl_desc="4-byte test field",
                                             inst_name='test_field',
                                             parent_full_inst_name='csr.test_reg')
            self._single_int_field_read_and_write_test(fut=self.dut.test_reg.test_field, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.regB.f0'):
            self._single_field_property_test(fut=self.dut.regB.f0, lsb=0, msb=7, low=0, high=7, is_volatile=False, default=0,
                                             rdl_name=None,
                                             rdl_desc=None,
                                             inst_name='f0',
                                             parent_full_inst_name='csr.regB')
            self._single_int_field_read_and_write_test(fut=self.dut.regB.f0, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.regB.f1'):
            self._single_field_property_test(fut=self.dut.regB.f1, lsb=8, msb=15, low=8, high=15, is_volatile=False, default=0,
                                             rdl_name=None,
                                             rdl_desc=None,
                                             inst_name='f1',
                                             parent_full_inst_name='csr.regB')
            self._single_int_field_read_and_write_test(fut=self.dut.regB.f1, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.regB.f2'):
            self._single_field_property_test(fut=self.dut.regB.f2, lsb=16, msb=23, low=16, high=23, is_volatile=False, default=0,
                                             rdl_name=None,
                                             rdl_desc=None,
                                             inst_name='f2',
                                             parent_full_inst_name='csr.regB')
            self._single_int_field_read_and_write_test(fut=self.dut.regB.f2, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.regB.f3'):
            self._single_field_property_test(fut=self.dut.regB.f3, lsb=24, msb=31, low=24, high=31, is_volatile=False, default=0,
                                             rdl_name=None,
                                             rdl_desc=None,
                                             inst_name='f3',
                                             parent_full_inst_name='csr.regB')
            self._single_int_field_read_and_write_test(fut=self.dut.regB.f3, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.info.rmem_total_depth'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.info.rmem_total_depth, lsb=0, msb=31, low=0, high=31, is_volatile=False, default=256,
                                             rdl_name="csr.endpoint_interface.info.rmem_total_depth[15:0]",
                                             rdl_desc="Total depth of the shared memory region for all remote peers. This field reflects the RMEM_TOTAL_DEPTH parameter value.",
                                             inst_name='rmem_total_depth',
                                             parent_full_inst_name='csr.endpoint_interface.info')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.info.rmem_total_depth, is_sw_readable=True, is_sw_writable=False)
        with self.subTest(msg='field: csr.endpoint_interface.info.num_of_peers'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.info.num_of_peers, lsb=32, msb=63, low=32, high=63, is_volatile=False, default=4,
                                             rdl_name="csr.endpoint_interface.info.num_of_peers[31:16]",
                                             rdl_desc="Number of remote peers supported by this openENOC Endpoint Interface instance. This field reflects the NUM_OF_PEERS parameter value.",
                                             inst_name='num_of_peers',
                                             parent_full_inst_name='csr.endpoint_interface.info')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.info.num_of_peers, is_sw_readable=True, is_sw_writable=False)
        with self.subTest(msg='field: csr.endpoint_interface.config.mac_address.lo_word'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.config.mac_address.lo_word, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=0,
                                             rdl_name="csr.endpoint_interface.config.mac_address.lo_word[31:0]",
                                             rdl_desc="Lower 32 bits [31:0] of the 48-bit MAC address.",
                                             inst_name='lo_word',
                                             parent_full_inst_name='csr.endpoint_interface.config.mac_address')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.config.mac_address.lo_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.config.mac_address.hi_word'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.config.mac_address.hi_word, lsb=32, msb=47, low=32, high=47, is_volatile=True, default=0,
                                             rdl_name="csr.endpoint_interface.config.mac_address.hi_word[47:32]",
                                             rdl_desc="Upper 16 bits [47:32] of the 48-bit MAC address.",
                                             inst_name='hi_word',
                                             parent_full_inst_name='csr.endpoint_interface.config.mac_address')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.config.mac_address.hi_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.axis_if.source.data.tdata'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.axis_if.source.data.tdata, lsb=0, msb=31, low=0, high=31, is_volatile=False, default=0,
                                             rdl_name="csr.endpoint_interface.axis_if.source.data.tdata[31:0]",
                                             rdl_desc="32-bit data value for the AXI4-Stream source interface.",
                                             inst_name='tdata',
                                             parent_full_inst_name='csr.endpoint_interface.axis_if.source.data')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.axis_if.source.data.tdata, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.axis_if.source.control.tvalid'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.axis_if.source.control.tvalid, lsb=0, msb=0, low=0, high=0, is_volatile=False, default=0,
                                             rdl_name="csr.endpoint_interface.axis_if.source.control.tvalid",
                                             rdl_desc="Indicates that the AXI4-Stream source interface has valid data to send. Once asserted by software, the field remains asserted until the transfer is accepted by the destination.",
                                             inst_name='tvalid',
                                             parent_full_inst_name='csr.endpoint_interface.axis_if.source.control')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.axis_if.source.control.tvalid, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.axis_if.source.control.tlast'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.axis_if.source.control.tlast, lsb=8, msb=8, low=8, high=8, is_volatile=False, default=0,
                                             rdl_name="csr.endpoint_interface.axis_if.source.control.tlast",
                                             rdl_desc="Indicates the last data word of a frame on the AXI4-Stream source interface.",
                                             inst_name='tlast',
                                             parent_full_inst_name='csr.endpoint_interface.axis_if.source.control')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.axis_if.source.control.tlast, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.axis_if.source.control.tkeep'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.axis_if.source.control.tkeep, lsb=16, msb=19, low=16, high=19, is_volatile=False, default=0,
                                             rdl_name="csr.endpoint_interface.axis_if.source.control.tkeep[3:0]",
                                             rdl_desc="Indicates which byte lanes contain valid data on the AXI4-Stream source interface.",
                                             inst_name='tkeep',
                                             parent_full_inst_name='csr.endpoint_interface.axis_if.source.control')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.axis_if.source.control.tkeep, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.axis_if.source.status.tready'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.axis_if.source.status.tready, lsb=0, msb=0, low=0, high=0, is_volatile=True, default=0,
                                             rdl_name="csr.endpoint_interface.axis_if.source.status.tready",
                                             rdl_desc="Indicates that the destination AXI4-Stream interface is ready to receive data.",
                                             inst_name='tready',
                                             parent_full_inst_name='csr.endpoint_interface.axis_if.source.status')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.axis_if.source.status.tready, is_sw_readable=True, is_sw_writable=False)
        with self.subTest(msg='field: csr.endpoint_interface.axis_if.sink.data.tdata'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.axis_if.sink.data.tdata, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.axis_if.sink.data.tdata[31:0]",
                                             rdl_desc="32-bit data value for the AXI4-Stream sink interface.",
                                             inst_name='tdata',
                                             parent_full_inst_name='csr.endpoint_interface.axis_if.sink.data')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.axis_if.sink.data.tdata, is_sw_readable=True, is_sw_writable=False)
        with self.subTest(msg='field: csr.endpoint_interface.axis_if.sink.control.tready'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.axis_if.sink.control.tready, lsb=0, msb=0, low=0, high=0, is_volatile=False, default=0,
                                             rdl_name="csr.endpoint_interface.axis_if.sink.control.tready",
                                             rdl_desc="Indicates that the AXI4-Stream sink interface is ready to accept a data transfer. Once asserted by software, the field remains asserted until a transfer occurs.",
                                             inst_name='tready',
                                             parent_full_inst_name='csr.endpoint_interface.axis_if.sink.control')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.axis_if.sink.control.tready, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.axis_if.sink.status.tvalid'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.axis_if.sink.status.tvalid, lsb=0, msb=0, low=0, high=0, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.axis_if.sink.status.tvalid",
                                             rdl_desc="Indicates that the AXI4-Stream sink interface has valid data to receive.",
                                             inst_name='tvalid',
                                             parent_full_inst_name='csr.endpoint_interface.axis_if.sink.status')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.axis_if.sink.status.tvalid, is_sw_readable=True, is_sw_writable=False)
        with self.subTest(msg='field: csr.endpoint_interface.axis_if.sink.status.tlast'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.axis_if.sink.status.tlast, lsb=8, msb=8, low=8, high=8, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.axis_if.sink.status.tlast",
                                             rdl_desc="Indicates the last data word of a frame on the AXI4-Stream sink interface.",
                                             inst_name='tlast',
                                             parent_full_inst_name='csr.endpoint_interface.axis_if.sink.status')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.axis_if.sink.status.tlast, is_sw_readable=True, is_sw_writable=False)
        with self.subTest(msg='field: csr.endpoint_interface.axis_if.sink.status.tkeep'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.axis_if.sink.status.tkeep, lsb=16, msb=19, low=16, high=19, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.axis_if.sink.status.tkeep[3:0]",
                                             rdl_desc="Indicates which byte lanes contain valid data on the AXI4-Stream sink interface.",
                                             inst_name='tkeep',
                                             parent_full_inst_name='csr.endpoint_interface.axis_if.sink.status')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.axis_if.sink.status.tkeep, is_sw_readable=True, is_sw_writable=False)
        with self.subTest(msg='field: csr.endpoint_interface.peers.entry[0].mac_address.lo_word'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.peers.entry[0].mac_address.lo_word, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].mac_address.lo_word[31:0]",
                                             rdl_desc="Lower 32 bits [31:0] of the 48-bit MAC address.",
                                             inst_name='lo_word',
                                             parent_full_inst_name='csr.endpoint_interface.peers.entry[0].mac_address')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.peers.entry[0].mac_address.lo_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.peers.entry[0].mac_address.hi_word'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.peers.entry[0].mac_address.hi_word, lsb=32, msb=47, low=32, high=47, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].mac_address.hi_word[47:32]",
                                             rdl_desc="Upper 16 bits [47:32] of the 48-bit MAC address.",
                                             inst_name='hi_word',
                                             parent_full_inst_name='csr.endpoint_interface.peers.entry[0].mac_address')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.peers.entry[0].mac_address.hi_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.peers.entry[0].rmem_address.offset'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.peers.entry[0].rmem_address.offset, lsb=0, msb=31, low=0, high=31, is_volatile=False, default=None,
                                             rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].rmem_address.offset[31:0]",
                                             rdl_desc="Word-aligned 32-bit address offset of the virtual memory region corresponding to the remote peer\u0027s memory.",
                                             inst_name='offset',
                                             parent_full_inst_name='csr.endpoint_interface.peers.entry[0].rmem_address')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.peers.entry[0].rmem_address.offset, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.peers.entry[0].local_address.base'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.peers.entry[0].local_address.base, lsb=0, msb=31, low=0, high=31, is_volatile=False, default=None,
                                             rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].local_address.base[31:0]",
                                             rdl_desc="Word-aligned 32-bit start address of the local memory region for DMA transfers.",
                                             inst_name='base',
                                             parent_full_inst_name='csr.endpoint_interface.peers.entry[0].local_address')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.peers.entry[0].local_address.base, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.peers.entry[0].remote_address.base'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.peers.entry[0].remote_address.base, lsb=0, msb=31, low=0, high=31, is_volatile=False, default=None,
                                             rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].remote_address.base[31:0]",
                                             rdl_desc="Word-aligned 32-bit start address of the remote peer\u0027s memory region.",
                                             inst_name='base',
                                             parent_full_inst_name='csr.endpoint_interface.peers.entry[0].remote_address')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.peers.entry[0].remote_address.base, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.peers.entry[0].size.bytes'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.peers.entry[0].register_size.bytes, lsb=0, msb=31, low=0, high=31, is_volatile=False, default=None,
                                             rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].size.bytes[31:0]",
                                             rdl_desc="32-bit size of the remote peer\u0027s memory region in bytes.",
                                             inst_name='bytes',
                                             parent_full_inst_name='csr.endpoint_interface.peers.entry[0].size')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.peers.entry[0].register_size.bytes, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.peers.entry[0].dma.mode'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.peers.entry[0].dma.mode, lsb=0, msb=1, low=0, high=1, is_volatile=False, default=None,
                                             rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.mode[1:0]",
                                             rdl_desc="DMA mode for transfers to/from the remote peer:\u003cul\u003e\n\u003cli\u003e0: DMA transfers to/from the remote peer are disabled.\u003c/li\u003e\n\u003cli\u003e1: DMA transfers to/from the remote peer are enabled in transparent mode, where accesses to the virtual memory region are directly translated to corresponding accesses to the remote peer\u0027s memory region (transactions are word-by-word, i.e., per virtual memory access).\u003c/li\u003e\n\u003cli\u003e2: DMA transfers to/from the remote peer are enabled in mirror-to-local mode, where the local memory region is used instead of the virtual memory region. The state of the remote peer\u0027s memory region (remote_address, size) is fetched from the remote peer on demand or periodically.\u003c/li\u003e\n\u003cli\u003e3: DMA transfers to/from the remote peer are enabled in mirror-to-remote mode, where the remote memory region is used instead of the virtual memory region. The state of the local peer\u0027s memory region (local_address, size) is sent to the remote peer on demand or periodically.\u003c/li\u003e\n\u003c/ul\u003e",
                                             inst_name='mode',
                                             parent_full_inst_name='csr.endpoint_interface.peers.entry[0].dma')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.peers.entry[0].dma.mode, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.peers.entry[0].dma.request'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.peers.entry[0].dma.request, lsb=8, msb=8, low=8, high=8, is_volatile=False, default=0,
                                             rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.request[8:8]",
                                             rdl_desc="Writing a 1 to this field initiates a DMA transfer to/from the remote peer. This field is a single-pulse register that is automatically cleared back to zero after being written.",
                                             inst_name='request',
                                             parent_full_inst_name='csr.endpoint_interface.peers.entry[0].dma')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.peers.entry[0].dma.request, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.peers.entry[0].dma.idle'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.peers.entry[0].dma.idle, lsb=16, msb=16, low=16, high=16, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.idle[16:16]",
                                             rdl_desc="Indicates whether the DMA transfer to/from the remote peer is idle. A value of 1 indicates that the DMA transfer is idle, while a value of 0 indicates that the DMA transfer is in progress.",
                                             inst_name='idle',
                                             parent_full_inst_name='csr.endpoint_interface.peers.entry[0].dma')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.peers.entry[0].dma.idle, is_sw_readable=True, is_sw_writable=False)
        with self.subTest(msg='field: csr.endpoint_interface.peers.entry[0].dma.done'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.peers.entry[0].dma.done, lsb=24, msb=24, low=24, high=24, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.done[24:24]",
                                             rdl_desc="Indicates whether the DMA transfer to/from the remote peer has been successful. A value of 1 indicates that the DMA transfer has completed successfully, while a value of 0 indicates that the DMA transfer is still in progress or has encountered an error.",
                                             inst_name='done',
                                             parent_full_inst_name='csr.endpoint_interface.peers.entry[0].dma')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.peers.entry[0].dma.done, is_sw_readable=True, is_sw_writable=False)
        with self.subTest(msg='field: csr.endpoint_interface.peers.entry[0].dma.error'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.peers.entry[0].dma.error, lsb=25, msb=25, low=25, high=25, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.error[25:25]",
                                             rdl_desc="Indicates whether the DMA transfer to/from the remote peer has encountered an error. A value of 1 indicates an error, while a value of 0 indicates no error.",
                                             inst_name='error',
                                             parent_full_inst_name='csr.endpoint_interface.peers.entry[0].dma')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.peers.entry[0].dma.error, is_sw_readable=True, is_sw_writable=False)
        with self.subTest(msg='field: csr.endpoint_interface.peers.entry[1].mac_address.lo_word'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.peers.entry[1].mac_address.lo_word, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].mac_address.lo_word[31:0]",
                                             rdl_desc="Lower 32 bits [31:0] of the 48-bit MAC address.",
                                             inst_name='lo_word',
                                             parent_full_inst_name='csr.endpoint_interface.peers.entry[1].mac_address')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.peers.entry[1].mac_address.lo_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.peers.entry[1].mac_address.hi_word'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.peers.entry[1].mac_address.hi_word, lsb=32, msb=47, low=32, high=47, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].mac_address.hi_word[47:32]",
                                             rdl_desc="Upper 16 bits [47:32] of the 48-bit MAC address.",
                                             inst_name='hi_word',
                                             parent_full_inst_name='csr.endpoint_interface.peers.entry[1].mac_address')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.peers.entry[1].mac_address.hi_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.peers.entry[1].rmem_address.offset'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.peers.entry[1].rmem_address.offset, lsb=0, msb=31, low=0, high=31, is_volatile=False, default=None,
                                             rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].rmem_address.offset[31:0]",
                                             rdl_desc="Word-aligned 32-bit address offset of the virtual memory region corresponding to the remote peer\u0027s memory.",
                                             inst_name='offset',
                                             parent_full_inst_name='csr.endpoint_interface.peers.entry[1].rmem_address')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.peers.entry[1].rmem_address.offset, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.peers.entry[1].local_address.base'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.peers.entry[1].local_address.base, lsb=0, msb=31, low=0, high=31, is_volatile=False, default=None,
                                             rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].local_address.base[31:0]",
                                             rdl_desc="Word-aligned 32-bit start address of the local memory region for DMA transfers.",
                                             inst_name='base',
                                             parent_full_inst_name='csr.endpoint_interface.peers.entry[1].local_address')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.peers.entry[1].local_address.base, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.peers.entry[1].remote_address.base'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.peers.entry[1].remote_address.base, lsb=0, msb=31, low=0, high=31, is_volatile=False, default=None,
                                             rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].remote_address.base[31:0]",
                                             rdl_desc="Word-aligned 32-bit start address of the remote peer\u0027s memory region.",
                                             inst_name='base',
                                             parent_full_inst_name='csr.endpoint_interface.peers.entry[1].remote_address')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.peers.entry[1].remote_address.base, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.peers.entry[1].size.bytes'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.peers.entry[1].register_size.bytes, lsb=0, msb=31, low=0, high=31, is_volatile=False, default=None,
                                             rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].size.bytes[31:0]",
                                             rdl_desc="32-bit size of the remote peer\u0027s memory region in bytes.",
                                             inst_name='bytes',
                                             parent_full_inst_name='csr.endpoint_interface.peers.entry[1].size')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.peers.entry[1].register_size.bytes, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.peers.entry[1].dma.mode'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.peers.entry[1].dma.mode, lsb=0, msb=1, low=0, high=1, is_volatile=False, default=None,
                                             rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.mode[1:0]",
                                             rdl_desc="DMA mode for transfers to/from the remote peer:\u003cul\u003e\n\u003cli\u003e0: DMA transfers to/from the remote peer are disabled.\u003c/li\u003e\n\u003cli\u003e1: DMA transfers to/from the remote peer are enabled in transparent mode, where accesses to the virtual memory region are directly translated to corresponding accesses to the remote peer\u0027s memory region (transactions are word-by-word, i.e., per virtual memory access).\u003c/li\u003e\n\u003cli\u003e2: DMA transfers to/from the remote peer are enabled in mirror-to-local mode, where the local memory region is used instead of the virtual memory region. The state of the remote peer\u0027s memory region (remote_address, size) is fetched from the remote peer on demand or periodically.\u003c/li\u003e\n\u003cli\u003e3: DMA transfers to/from the remote peer are enabled in mirror-to-remote mode, where the remote memory region is used instead of the virtual memory region. The state of the local peer\u0027s memory region (local_address, size) is sent to the remote peer on demand or periodically.\u003c/li\u003e\n\u003c/ul\u003e",
                                             inst_name='mode',
                                             parent_full_inst_name='csr.endpoint_interface.peers.entry[1].dma')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.peers.entry[1].dma.mode, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.peers.entry[1].dma.request'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.peers.entry[1].dma.request, lsb=8, msb=8, low=8, high=8, is_volatile=False, default=0,
                                             rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.request[8:8]",
                                             rdl_desc="Writing a 1 to this field initiates a DMA transfer to/from the remote peer. This field is a single-pulse register that is automatically cleared back to zero after being written.",
                                             inst_name='request',
                                             parent_full_inst_name='csr.endpoint_interface.peers.entry[1].dma')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.peers.entry[1].dma.request, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.peers.entry[1].dma.idle'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.peers.entry[1].dma.idle, lsb=16, msb=16, low=16, high=16, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.idle[16:16]",
                                             rdl_desc="Indicates whether the DMA transfer to/from the remote peer is idle. A value of 1 indicates that the DMA transfer is idle, while a value of 0 indicates that the DMA transfer is in progress.",
                                             inst_name='idle',
                                             parent_full_inst_name='csr.endpoint_interface.peers.entry[1].dma')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.peers.entry[1].dma.idle, is_sw_readable=True, is_sw_writable=False)
        with self.subTest(msg='field: csr.endpoint_interface.peers.entry[1].dma.done'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.peers.entry[1].dma.done, lsb=24, msb=24, low=24, high=24, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.done[24:24]",
                                             rdl_desc="Indicates whether the DMA transfer to/from the remote peer has been successful. A value of 1 indicates that the DMA transfer has completed successfully, while a value of 0 indicates that the DMA transfer is still in progress or has encountered an error.",
                                             inst_name='done',
                                             parent_full_inst_name='csr.endpoint_interface.peers.entry[1].dma')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.peers.entry[1].dma.done, is_sw_readable=True, is_sw_writable=False)
        with self.subTest(msg='field: csr.endpoint_interface.peers.entry[1].dma.error'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.peers.entry[1].dma.error, lsb=25, msb=25, low=25, high=25, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.error[25:25]",
                                             rdl_desc="Indicates whether the DMA transfer to/from the remote peer has encountered an error. A value of 1 indicates an error, while a value of 0 indicates no error.",
                                             inst_name='error',
                                             parent_full_inst_name='csr.endpoint_interface.peers.entry[1].dma')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.peers.entry[1].dma.error, is_sw_readable=True, is_sw_writable=False)
        with self.subTest(msg='field: csr.endpoint_interface.peers.entry[2].mac_address.lo_word'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.peers.entry[2].mac_address.lo_word, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].mac_address.lo_word[31:0]",
                                             rdl_desc="Lower 32 bits [31:0] of the 48-bit MAC address.",
                                             inst_name='lo_word',
                                             parent_full_inst_name='csr.endpoint_interface.peers.entry[2].mac_address')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.peers.entry[2].mac_address.lo_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.peers.entry[2].mac_address.hi_word'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.peers.entry[2].mac_address.hi_word, lsb=32, msb=47, low=32, high=47, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].mac_address.hi_word[47:32]",
                                             rdl_desc="Upper 16 bits [47:32] of the 48-bit MAC address.",
                                             inst_name='hi_word',
                                             parent_full_inst_name='csr.endpoint_interface.peers.entry[2].mac_address')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.peers.entry[2].mac_address.hi_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.peers.entry[2].rmem_address.offset'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.peers.entry[2].rmem_address.offset, lsb=0, msb=31, low=0, high=31, is_volatile=False, default=None,
                                             rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].rmem_address.offset[31:0]",
                                             rdl_desc="Word-aligned 32-bit address offset of the virtual memory region corresponding to the remote peer\u0027s memory.",
                                             inst_name='offset',
                                             parent_full_inst_name='csr.endpoint_interface.peers.entry[2].rmem_address')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.peers.entry[2].rmem_address.offset, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.peers.entry[2].local_address.base'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.peers.entry[2].local_address.base, lsb=0, msb=31, low=0, high=31, is_volatile=False, default=None,
                                             rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].local_address.base[31:0]",
                                             rdl_desc="Word-aligned 32-bit start address of the local memory region for DMA transfers.",
                                             inst_name='base',
                                             parent_full_inst_name='csr.endpoint_interface.peers.entry[2].local_address')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.peers.entry[2].local_address.base, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.peers.entry[2].remote_address.base'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.peers.entry[2].remote_address.base, lsb=0, msb=31, low=0, high=31, is_volatile=False, default=None,
                                             rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].remote_address.base[31:0]",
                                             rdl_desc="Word-aligned 32-bit start address of the remote peer\u0027s memory region.",
                                             inst_name='base',
                                             parent_full_inst_name='csr.endpoint_interface.peers.entry[2].remote_address')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.peers.entry[2].remote_address.base, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.peers.entry[2].size.bytes'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.peers.entry[2].register_size.bytes, lsb=0, msb=31, low=0, high=31, is_volatile=False, default=None,
                                             rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].size.bytes[31:0]",
                                             rdl_desc="32-bit size of the remote peer\u0027s memory region in bytes.",
                                             inst_name='bytes',
                                             parent_full_inst_name='csr.endpoint_interface.peers.entry[2].size')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.peers.entry[2].register_size.bytes, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.peers.entry[2].dma.mode'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.peers.entry[2].dma.mode, lsb=0, msb=1, low=0, high=1, is_volatile=False, default=None,
                                             rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.mode[1:0]",
                                             rdl_desc="DMA mode for transfers to/from the remote peer:\u003cul\u003e\n\u003cli\u003e0: DMA transfers to/from the remote peer are disabled.\u003c/li\u003e\n\u003cli\u003e1: DMA transfers to/from the remote peer are enabled in transparent mode, where accesses to the virtual memory region are directly translated to corresponding accesses to the remote peer\u0027s memory region (transactions are word-by-word, i.e., per virtual memory access).\u003c/li\u003e\n\u003cli\u003e2: DMA transfers to/from the remote peer are enabled in mirror-to-local mode, where the local memory region is used instead of the virtual memory region. The state of the remote peer\u0027s memory region (remote_address, size) is fetched from the remote peer on demand or periodically.\u003c/li\u003e\n\u003cli\u003e3: DMA transfers to/from the remote peer are enabled in mirror-to-remote mode, where the remote memory region is used instead of the virtual memory region. The state of the local peer\u0027s memory region (local_address, size) is sent to the remote peer on demand or periodically.\u003c/li\u003e\n\u003c/ul\u003e",
                                             inst_name='mode',
                                             parent_full_inst_name='csr.endpoint_interface.peers.entry[2].dma')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.peers.entry[2].dma.mode, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.peers.entry[2].dma.request'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.peers.entry[2].dma.request, lsb=8, msb=8, low=8, high=8, is_volatile=False, default=0,
                                             rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.request[8:8]",
                                             rdl_desc="Writing a 1 to this field initiates a DMA transfer to/from the remote peer. This field is a single-pulse register that is automatically cleared back to zero after being written.",
                                             inst_name='request',
                                             parent_full_inst_name='csr.endpoint_interface.peers.entry[2].dma')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.peers.entry[2].dma.request, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.peers.entry[2].dma.idle'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.peers.entry[2].dma.idle, lsb=16, msb=16, low=16, high=16, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.idle[16:16]",
                                             rdl_desc="Indicates whether the DMA transfer to/from the remote peer is idle. A value of 1 indicates that the DMA transfer is idle, while a value of 0 indicates that the DMA transfer is in progress.",
                                             inst_name='idle',
                                             parent_full_inst_name='csr.endpoint_interface.peers.entry[2].dma')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.peers.entry[2].dma.idle, is_sw_readable=True, is_sw_writable=False)
        with self.subTest(msg='field: csr.endpoint_interface.peers.entry[2].dma.done'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.peers.entry[2].dma.done, lsb=24, msb=24, low=24, high=24, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.done[24:24]",
                                             rdl_desc="Indicates whether the DMA transfer to/from the remote peer has been successful. A value of 1 indicates that the DMA transfer has completed successfully, while a value of 0 indicates that the DMA transfer is still in progress or has encountered an error.",
                                             inst_name='done',
                                             parent_full_inst_name='csr.endpoint_interface.peers.entry[2].dma')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.peers.entry[2].dma.done, is_sw_readable=True, is_sw_writable=False)
        with self.subTest(msg='field: csr.endpoint_interface.peers.entry[2].dma.error'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.peers.entry[2].dma.error, lsb=25, msb=25, low=25, high=25, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.error[25:25]",
                                             rdl_desc="Indicates whether the DMA transfer to/from the remote peer has encountered an error. A value of 1 indicates an error, while a value of 0 indicates no error.",
                                             inst_name='error',
                                             parent_full_inst_name='csr.endpoint_interface.peers.entry[2].dma')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.peers.entry[2].dma.error, is_sw_readable=True, is_sw_writable=False)
        with self.subTest(msg='field: csr.endpoint_interface.peers.entry[3].mac_address.lo_word'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.peers.entry[3].mac_address.lo_word, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].mac_address.lo_word[31:0]",
                                             rdl_desc="Lower 32 bits [31:0] of the 48-bit MAC address.",
                                             inst_name='lo_word',
                                             parent_full_inst_name='csr.endpoint_interface.peers.entry[3].mac_address')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.peers.entry[3].mac_address.lo_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.peers.entry[3].mac_address.hi_word'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.peers.entry[3].mac_address.hi_word, lsb=32, msb=47, low=32, high=47, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].mac_address.hi_word[47:32]",
                                             rdl_desc="Upper 16 bits [47:32] of the 48-bit MAC address.",
                                             inst_name='hi_word',
                                             parent_full_inst_name='csr.endpoint_interface.peers.entry[3].mac_address')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.peers.entry[3].mac_address.hi_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.peers.entry[3].rmem_address.offset'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.peers.entry[3].rmem_address.offset, lsb=0, msb=31, low=0, high=31, is_volatile=False, default=None,
                                             rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].rmem_address.offset[31:0]",
                                             rdl_desc="Word-aligned 32-bit address offset of the virtual memory region corresponding to the remote peer\u0027s memory.",
                                             inst_name='offset',
                                             parent_full_inst_name='csr.endpoint_interface.peers.entry[3].rmem_address')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.peers.entry[3].rmem_address.offset, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.peers.entry[3].local_address.base'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.peers.entry[3].local_address.base, lsb=0, msb=31, low=0, high=31, is_volatile=False, default=None,
                                             rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].local_address.base[31:0]",
                                             rdl_desc="Word-aligned 32-bit start address of the local memory region for DMA transfers.",
                                             inst_name='base',
                                             parent_full_inst_name='csr.endpoint_interface.peers.entry[3].local_address')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.peers.entry[3].local_address.base, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.peers.entry[3].remote_address.base'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.peers.entry[3].remote_address.base, lsb=0, msb=31, low=0, high=31, is_volatile=False, default=None,
                                             rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].remote_address.base[31:0]",
                                             rdl_desc="Word-aligned 32-bit start address of the remote peer\u0027s memory region.",
                                             inst_name='base',
                                             parent_full_inst_name='csr.endpoint_interface.peers.entry[3].remote_address')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.peers.entry[3].remote_address.base, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.peers.entry[3].size.bytes'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.peers.entry[3].register_size.bytes, lsb=0, msb=31, low=0, high=31, is_volatile=False, default=None,
                                             rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].size.bytes[31:0]",
                                             rdl_desc="32-bit size of the remote peer\u0027s memory region in bytes.",
                                             inst_name='bytes',
                                             parent_full_inst_name='csr.endpoint_interface.peers.entry[3].size')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.peers.entry[3].register_size.bytes, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.peers.entry[3].dma.mode'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.peers.entry[3].dma.mode, lsb=0, msb=1, low=0, high=1, is_volatile=False, default=None,
                                             rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.mode[1:0]",
                                             rdl_desc="DMA mode for transfers to/from the remote peer:\u003cul\u003e\n\u003cli\u003e0: DMA transfers to/from the remote peer are disabled.\u003c/li\u003e\n\u003cli\u003e1: DMA transfers to/from the remote peer are enabled in transparent mode, where accesses to the virtual memory region are directly translated to corresponding accesses to the remote peer\u0027s memory region (transactions are word-by-word, i.e., per virtual memory access).\u003c/li\u003e\n\u003cli\u003e2: DMA transfers to/from the remote peer are enabled in mirror-to-local mode, where the local memory region is used instead of the virtual memory region. The state of the remote peer\u0027s memory region (remote_address, size) is fetched from the remote peer on demand or periodically.\u003c/li\u003e\n\u003cli\u003e3: DMA transfers to/from the remote peer are enabled in mirror-to-remote mode, where the remote memory region is used instead of the virtual memory region. The state of the local peer\u0027s memory region (local_address, size) is sent to the remote peer on demand or periodically.\u003c/li\u003e\n\u003c/ul\u003e",
                                             inst_name='mode',
                                             parent_full_inst_name='csr.endpoint_interface.peers.entry[3].dma')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.peers.entry[3].dma.mode, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.peers.entry[3].dma.request'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.peers.entry[3].dma.request, lsb=8, msb=8, low=8, high=8, is_volatile=False, default=0,
                                             rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.request[8:8]",
                                             rdl_desc="Writing a 1 to this field initiates a DMA transfer to/from the remote peer. This field is a single-pulse register that is automatically cleared back to zero after being written.",
                                             inst_name='request',
                                             parent_full_inst_name='csr.endpoint_interface.peers.entry[3].dma')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.peers.entry[3].dma.request, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.peers.entry[3].dma.idle'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.peers.entry[3].dma.idle, lsb=16, msb=16, low=16, high=16, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.idle[16:16]",
                                             rdl_desc="Indicates whether the DMA transfer to/from the remote peer is idle. A value of 1 indicates that the DMA transfer is idle, while a value of 0 indicates that the DMA transfer is in progress.",
                                             inst_name='idle',
                                             parent_full_inst_name='csr.endpoint_interface.peers.entry[3].dma')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.peers.entry[3].dma.idle, is_sw_readable=True, is_sw_writable=False)
        with self.subTest(msg='field: csr.endpoint_interface.peers.entry[3].dma.done'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.peers.entry[3].dma.done, lsb=24, msb=24, low=24, high=24, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.done[24:24]",
                                             rdl_desc="Indicates whether the DMA transfer to/from the remote peer has been successful. A value of 1 indicates that the DMA transfer has completed successfully, while a value of 0 indicates that the DMA transfer is still in progress or has encountered an error.",
                                             inst_name='done',
                                             parent_full_inst_name='csr.endpoint_interface.peers.entry[3].dma')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.peers.entry[3].dma.done, is_sw_readable=True, is_sw_writable=False)
        with self.subTest(msg='field: csr.endpoint_interface.peers.entry[3].dma.error'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.peers.entry[3].dma.error, lsb=25, msb=25, low=25, high=25, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.error[25:25]",
                                             rdl_desc="Indicates whether the DMA transfer to/from the remote peer has encountered an error. A value of 1 indicates an error, while a value of 0 indicates no error.",
                                             inst_name='error',
                                             parent_full_inst_name='csr.endpoint_interface.peers.entry[3].dma')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.peers.entry[3].dma.error, is_sw_readable=True, is_sw_writable=False)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[0].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[0].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[0]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[0].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[1].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[1].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[1]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[1].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[2].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[2].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[2]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[2].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[3].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[3].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[3]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[3].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[4].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[4].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[4]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[4].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[5].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[5].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[5]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[5].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[6].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[6].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[6]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[6].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[7].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[7].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[7]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[7].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[8].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[8].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[8]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[8].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[9].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[9].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[9]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[9].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[10].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[10].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[10]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[10].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[11].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[11].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[11]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[11].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[12].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[12].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[12]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[12].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[13].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[13].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[13]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[13].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[14].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[14].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[14]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[14].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[15].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[15].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[15]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[15].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[16].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[16].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[16]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[16].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[17].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[17].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[17]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[17].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[18].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[18].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[18]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[18].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[19].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[19].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[19]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[19].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[20].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[20].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[20]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[20].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[21].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[21].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[21]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[21].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[22].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[22].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[22]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[22].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[23].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[23].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[23]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[23].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[24].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[24].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[24]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[24].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[25].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[25].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[25]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[25].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[26].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[26].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[26]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[26].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[27].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[27].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[27]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[27].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[28].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[28].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[28]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[28].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[29].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[29].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[29]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[29].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[30].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[30].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[30]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[30].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[31].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[31].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[31]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[31].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[32].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[32].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[32]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[32].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[33].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[33].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[33]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[33].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[34].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[34].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[34]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[34].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[35].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[35].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[35]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[35].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[36].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[36].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[36]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[36].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[37].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[37].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[37]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[37].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[38].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[38].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[38]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[38].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[39].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[39].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[39]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[39].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[40].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[40].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[40]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[40].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[41].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[41].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[41]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[41].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[42].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[42].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[42]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[42].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[43].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[43].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[43]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[43].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[44].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[44].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[44]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[44].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[45].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[45].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[45]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[45].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[46].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[46].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[46]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[46].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[47].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[47].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[47]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[47].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[48].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[48].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[48]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[48].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[49].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[49].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[49]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[49].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[50].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[50].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[50]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[50].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[51].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[51].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[51]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[51].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[52].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[52].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[52]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[52].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[53].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[53].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[53]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[53].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[54].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[54].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[54]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[54].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[55].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[55].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[55]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[55].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[56].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[56].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[56]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[56].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[57].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[57].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[57]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[57].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[58].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[58].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[58]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[58].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[59].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[59].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[59]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[59].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[60].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[60].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[60]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[60].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[61].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[61].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[61]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[61].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[62].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[62].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[62]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[62].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[63].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[63].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[63]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[63].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[64].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[64].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[64]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[64].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[65].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[65].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[65]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[65].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[66].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[66].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[66]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[66].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[67].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[67].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[67]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[67].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[68].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[68].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[68]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[68].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[69].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[69].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[69]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[69].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[70].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[70].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[70]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[70].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[71].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[71].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[71]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[71].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[72].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[72].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[72]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[72].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[73].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[73].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[73]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[73].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[74].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[74].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[74]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[74].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[75].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[75].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[75]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[75].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[76].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[76].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[76]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[76].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[77].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[77].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[77]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[77].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[78].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[78].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[78]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[78].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[79].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[79].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[79]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[79].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[80].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[80].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[80]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[80].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[81].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[81].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[81]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[81].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[82].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[82].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[82]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[82].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[83].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[83].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[83]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[83].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[84].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[84].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[84]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[84].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[85].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[85].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[85]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[85].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[86].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[86].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[86]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[86].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[87].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[87].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[87]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[87].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[88].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[88].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[88]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[88].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[89].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[89].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[89]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[89].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[90].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[90].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[90]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[90].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[91].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[91].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[91]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[91].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[92].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[92].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[92]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[92].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[93].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[93].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[93]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[93].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[94].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[94].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[94]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[94].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[95].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[95].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[95]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[95].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[96].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[96].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[96]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[96].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[97].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[97].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[97]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[97].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[98].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[98].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[98]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[98].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[99].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[99].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[99]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[99].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[100].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[100].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[100]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[100].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[101].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[101].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[101]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[101].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[102].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[102].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[102]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[102].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[103].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[103].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[103]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[103].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[104].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[104].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[104]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[104].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[105].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[105].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[105]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[105].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[106].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[106].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[106]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[106].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[107].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[107].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[107]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[107].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[108].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[108].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[108]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[108].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[109].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[109].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[109]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[109].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[110].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[110].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[110]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[110].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[111].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[111].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[111]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[111].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[112].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[112].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[112]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[112].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[113].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[113].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[113]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[113].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[114].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[114].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[114]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[114].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[115].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[115].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[115]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[115].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[116].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[116].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[116]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[116].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[117].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[117].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[117]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[117].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[118].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[118].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[118]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[118].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[119].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[119].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[119]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[119].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[120].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[120].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[120]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[120].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[121].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[121].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[121]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[121].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[122].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[122].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[122]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[122].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[123].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[123].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[123]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[123].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[124].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[124].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[124]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[124].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[125].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[125].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[125]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[125].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[126].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[126].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[126]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[126].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[127].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[127].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[127]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[127].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[128].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[128].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[128]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[128].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[129].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[129].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[129]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[129].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[130].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[130].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[130]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[130].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[131].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[131].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[131]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[131].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[132].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[132].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[132]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[132].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[133].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[133].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[133]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[133].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[134].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[134].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[134]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[134].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[135].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[135].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[135]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[135].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[136].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[136].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[136]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[136].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[137].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[137].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[137]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[137].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[138].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[138].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[138]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[138].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[139].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[139].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[139]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[139].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[140].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[140].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[140]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[140].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[141].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[141].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[141]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[141].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[142].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[142].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[142]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[142].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[143].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[143].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[143]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[143].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[144].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[144].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[144]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[144].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[145].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[145].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[145]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[145].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[146].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[146].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[146]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[146].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[147].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[147].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[147]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[147].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[148].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[148].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[148]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[148].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[149].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[149].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[149]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[149].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[150].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[150].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[150]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[150].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[151].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[151].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[151]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[151].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[152].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[152].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[152]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[152].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[153].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[153].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[153]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[153].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[154].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[154].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[154]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[154].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[155].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[155].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[155]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[155].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[156].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[156].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[156]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[156].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[157].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[157].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[157]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[157].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[158].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[158].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[158]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[158].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[159].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[159].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[159]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[159].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[160].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[160].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[160]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[160].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[161].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[161].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[161]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[161].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[162].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[162].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[162]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[162].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[163].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[163].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[163]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[163].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[164].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[164].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[164]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[164].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[165].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[165].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[165]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[165].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[166].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[166].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[166]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[166].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[167].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[167].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[167]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[167].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[168].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[168].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[168]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[168].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[169].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[169].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[169]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[169].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[170].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[170].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[170]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[170].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[171].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[171].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[171]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[171].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[172].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[172].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[172]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[172].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[173].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[173].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[173]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[173].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[174].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[174].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[174]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[174].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[175].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[175].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[175]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[175].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[176].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[176].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[176]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[176].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[177].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[177].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[177]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[177].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[178].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[178].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[178]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[178].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[179].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[179].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[179]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[179].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[180].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[180].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[180]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[180].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[181].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[181].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[181]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[181].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[182].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[182].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[182]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[182].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[183].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[183].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[183]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[183].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[184].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[184].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[184]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[184].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[185].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[185].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[185]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[185].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[186].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[186].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[186]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[186].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[187].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[187].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[187]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[187].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[188].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[188].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[188]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[188].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[189].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[189].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[189]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[189].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[190].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[190].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[190]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[190].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[191].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[191].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[191]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[191].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[192].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[192].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[192]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[192].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[193].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[193].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[193]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[193].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[194].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[194].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[194]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[194].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[195].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[195].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[195]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[195].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[196].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[196].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[196]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[196].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[197].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[197].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[197]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[197].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[198].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[198].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[198]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[198].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[199].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[199].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[199]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[199].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[200].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[200].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[200]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[200].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[201].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[201].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[201]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[201].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[202].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[202].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[202]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[202].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[203].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[203].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[203]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[203].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[204].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[204].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[204]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[204].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[205].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[205].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[205]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[205].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[206].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[206].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[206]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[206].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[207].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[207].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[207]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[207].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[208].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[208].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[208]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[208].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[209].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[209].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[209]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[209].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[210].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[210].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[210]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[210].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[211].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[211].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[211]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[211].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[212].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[212].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[212]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[212].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[213].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[213].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[213]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[213].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[214].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[214].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[214]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[214].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[215].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[215].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[215]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[215].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[216].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[216].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[216]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[216].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[217].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[217].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[217]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[217].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[218].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[218].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[218]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[218].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[219].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[219].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[219]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[219].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[220].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[220].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[220]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[220].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[221].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[221].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[221]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[221].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[222].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[222].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[222]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[222].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[223].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[223].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[223]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[223].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[224].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[224].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[224]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[224].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[225].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[225].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[225]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[225].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[226].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[226].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[226]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[226].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[227].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[227].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[227]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[227].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[228].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[228].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[228]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[228].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[229].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[229].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[229]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[229].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[230].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[230].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[230]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[230].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[231].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[231].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[231]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[231].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[232].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[232].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[232]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[232].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[233].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[233].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[233]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[233].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[234].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[234].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[234]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[234].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[235].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[235].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[235]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[235].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[236].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[236].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[236]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[236].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[237].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[237].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[237]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[237].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[238].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[238].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[238]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[238].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[239].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[239].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[239]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[239].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[240].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[240].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[240]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[240].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[241].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[241].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[241]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[241].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[242].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[242].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[242]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[242].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[243].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[243].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[243]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[243].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[244].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[244].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[244]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[244].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[245].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[245].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[245]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[245].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[246].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[246].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[246]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[246].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[247].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[247].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[247]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[247].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[248].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[248].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[248]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[248].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[249].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[249].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[249]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[249].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[250].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[250].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[250]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[250].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[251].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[251].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[251]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[251].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[252].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[252].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[252]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[252].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[253].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[253].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[253]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[253].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[254].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[254].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[254]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[254].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.endpoint_interface.rmem.word[255].data'):
            self._single_field_property_test(fut=self.dut.endpoint_interface.rmem.word[255].data, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]",
                                             rdl_desc="Data stored in this virtual memory word.",
                                             inst_name='data',
                                             parent_full_inst_name='csr.endpoint_interface.rmem.word[255]')
            self._single_int_field_read_and_write_test(fut=self.dut.endpoint_interface.rmem.word[255].data, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.switch_interface.info.table_depth'):
            self._single_field_property_test(fut=self.dut.switch_interface.info.table_depth, lsb=0, msb=15, low=0, high=15, is_volatile=False, default=8,
                                             rdl_name="csr.switch_interface.info.table_depth[15:0]",
                                             rdl_desc="Depth of the forwarding table in this openENOC Switch instance. This field reflects the TABLE_DEPTH parameter value.",
                                             inst_name='table_depth',
                                             parent_full_inst_name='csr.switch_interface.info')
            self._single_int_field_read_and_write_test(fut=self.dut.switch_interface.info.table_depth, is_sw_readable=True, is_sw_writable=False)
        with self.subTest(msg='field: csr.switch_interface.info.num_of_interfaces'):
            self._single_field_property_test(fut=self.dut.switch_interface.info.num_of_interfaces, lsb=16, msb=21, low=16, high=21, is_volatile=False, default=4,
                                             rdl_name="csr.switch_interface.info.num_of_interfaces[21:16]",
                                             rdl_desc="Number of interfaces in this openENOC Switch instance. This field reflects the NUM_OF_INTERFACES parameter value.",
                                             inst_name='num_of_interfaces',
                                             parent_full_inst_name='csr.switch_interface.info')
            self._single_int_field_read_and_write_test(fut=self.dut.switch_interface.info.num_of_interfaces, is_sw_readable=True, is_sw_writable=False)
        with self.subTest(msg='field: csr.switch_interface.forwarding_control.operation_mode'):
            self._single_field_property_test(fut=self.dut.switch_interface.forwarding_control.operation_mode, lsb=0, msb=0, low=0, high=0, is_volatile=False, default=0,
                                             rdl_name="csr.switch_interface.forwarding_control.operation_mode[0:0]",
                                             rdl_desc="Mode of operation for the openENOC Switch instance. When set to 1, the switch operates in managed mode, allowing software to configure the forwarding table and control forwarding operations. When set to 0, the switch operates in unmanaged mode, where forwarding state is maintained autonomously by internal hardware logic without software intervention.",
                                             inst_name='operation_mode',
                                             parent_full_inst_name='csr.switch_interface.forwarding_control')
            self._single_int_field_read_and_write_test(fut=self.dut.switch_interface.forwarding_control.operation_mode, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.switch_interface.forwarding_control.pause_request'):
            self._single_field_property_test(fut=self.dut.switch_interface.forwarding_control.pause_request, lsb=7, msb=7, low=7, high=7, is_volatile=False, default=0,
                                             rdl_name="csr.switch_interface.forwarding_control.pause_request[7:7]",
                                             rdl_desc="Pause request for the forwarding logic. When set, this field requests the switch to pause frame forwarding and clear its internal pipeline before forwarding table updates are performed.",
                                             inst_name='pause_request',
                                             parent_full_inst_name='csr.switch_interface.forwarding_control')
            self._single_int_field_read_and_write_test(fut=self.dut.switch_interface.forwarding_control.pause_request, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.switch_interface.forwarding_control.pause_done'):
            self._single_field_property_test(fut=self.dut.switch_interface.forwarding_control.pause_done, lsb=15, msb=15, low=15, high=15, is_volatile=True, default=None,
                                             rdl_name="csr.switch_interface.forwarding_control.pause_done[15:15]",
                                             rdl_desc="Pause done status. When set, this field indicates that the switch has paused frame forwarding and reached a safe state for forwarding table modification.",
                                             inst_name='pause_done',
                                             parent_full_inst_name='csr.switch_interface.forwarding_control')
            self._single_int_field_read_and_write_test(fut=self.dut.switch_interface.forwarding_control.pause_done, is_sw_readable=True, is_sw_writable=False)
        with self.subTest(msg='field: csr.switch_interface.default_forwarding.bitmap'):
            self._single_field_property_test(fut=self.dut.switch_interface.default_forwarding.bitmap, lsb=0, msb=3, low=0, high=3, is_volatile=False, default=0,
                                             rdl_name="csr.switch_interface.default_forwarding.bitmap[NUM_OF_INTERFACES-1:0]",
                                             rdl_desc="Bitmap selecting the output interface or interfaces to which frames that do not match any enabled forwarding table entry are forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.",
                                             inst_name='bitmap',
                                             parent_full_inst_name='csr.switch_interface.default_forwarding')
            self._single_int_field_read_and_write_test(fut=self.dut.switch_interface.default_forwarding.bitmap, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.switch_interface.forwarding_table.entry[0].mac_address.lo_word'):
            self._single_field_property_test(fut=self.dut.switch_interface.forwarding_table.entry[0].mac_address.lo_word, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.lo_word[31:0]",
                                             rdl_desc="Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='lo_word',
                                             parent_full_inst_name='csr.switch_interface.forwarding_table.entry[0].mac_address')
            self._single_int_field_read_and_write_test(fut=self.dut.switch_interface.forwarding_table.entry[0].mac_address.lo_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.switch_interface.forwarding_table.entry[0].mac_address.hi_word'):
            self._single_field_property_test(fut=self.dut.switch_interface.forwarding_table.entry[0].mac_address.hi_word, lsb=32, msb=47, low=32, high=47, is_volatile=True, default=None,
                                             rdl_name="csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.hi_word[47:32]",
                                             rdl_desc="Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='hi_word',
                                             parent_full_inst_name='csr.switch_interface.forwarding_table.entry[0].mac_address')
            self._single_int_field_read_and_write_test(fut=self.dut.switch_interface.forwarding_table.entry[0].mac_address.hi_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.switch_interface.forwarding_table.entry[0].iface.bitmap'):
            self._single_field_property_test(fut=self.dut.switch_interface.forwarding_table.entry[0].iface.bitmap, lsb=0, msb=3, low=0, high=3, is_volatile=True, default=None,
                                             rdl_name="csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]",
                                             rdl_desc="Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.",
                                             inst_name='bitmap',
                                             parent_full_inst_name='csr.switch_interface.forwarding_table.entry[0].iface')
            self._single_int_field_read_and_write_test(fut=self.dut.switch_interface.forwarding_table.entry[0].iface.bitmap, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.switch_interface.forwarding_table.entry[0].config.enabled'):
            self._single_field_property_test(fut=self.dut.switch_interface.forwarding_table.entry[0].config.enabled, lsb=0, msb=0, low=0, high=0, is_volatile=True, default=None,
                                             rdl_name="csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled",
                                             rdl_desc="Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.",
                                             inst_name='enabled',
                                             parent_full_inst_name='csr.switch_interface.forwarding_table.entry[0].config')
            self._single_int_field_read_and_write_test(fut=self.dut.switch_interface.forwarding_table.entry[0].config.enabled, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.switch_interface.forwarding_table.entry[1].mac_address.lo_word'):
            self._single_field_property_test(fut=self.dut.switch_interface.forwarding_table.entry[1].mac_address.lo_word, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.lo_word[31:0]",
                                             rdl_desc="Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='lo_word',
                                             parent_full_inst_name='csr.switch_interface.forwarding_table.entry[1].mac_address')
            self._single_int_field_read_and_write_test(fut=self.dut.switch_interface.forwarding_table.entry[1].mac_address.lo_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.switch_interface.forwarding_table.entry[1].mac_address.hi_word'):
            self._single_field_property_test(fut=self.dut.switch_interface.forwarding_table.entry[1].mac_address.hi_word, lsb=32, msb=47, low=32, high=47, is_volatile=True, default=None,
                                             rdl_name="csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.hi_word[47:32]",
                                             rdl_desc="Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='hi_word',
                                             parent_full_inst_name='csr.switch_interface.forwarding_table.entry[1].mac_address')
            self._single_int_field_read_and_write_test(fut=self.dut.switch_interface.forwarding_table.entry[1].mac_address.hi_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.switch_interface.forwarding_table.entry[1].iface.bitmap'):
            self._single_field_property_test(fut=self.dut.switch_interface.forwarding_table.entry[1].iface.bitmap, lsb=0, msb=3, low=0, high=3, is_volatile=True, default=None,
                                             rdl_name="csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]",
                                             rdl_desc="Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.",
                                             inst_name='bitmap',
                                             parent_full_inst_name='csr.switch_interface.forwarding_table.entry[1].iface')
            self._single_int_field_read_and_write_test(fut=self.dut.switch_interface.forwarding_table.entry[1].iface.bitmap, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.switch_interface.forwarding_table.entry[1].config.enabled'):
            self._single_field_property_test(fut=self.dut.switch_interface.forwarding_table.entry[1].config.enabled, lsb=0, msb=0, low=0, high=0, is_volatile=True, default=None,
                                             rdl_name="csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled",
                                             rdl_desc="Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.",
                                             inst_name='enabled',
                                             parent_full_inst_name='csr.switch_interface.forwarding_table.entry[1].config')
            self._single_int_field_read_and_write_test(fut=self.dut.switch_interface.forwarding_table.entry[1].config.enabled, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.switch_interface.forwarding_table.entry[2].mac_address.lo_word'):
            self._single_field_property_test(fut=self.dut.switch_interface.forwarding_table.entry[2].mac_address.lo_word, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.lo_word[31:0]",
                                             rdl_desc="Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='lo_word',
                                             parent_full_inst_name='csr.switch_interface.forwarding_table.entry[2].mac_address')
            self._single_int_field_read_and_write_test(fut=self.dut.switch_interface.forwarding_table.entry[2].mac_address.lo_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.switch_interface.forwarding_table.entry[2].mac_address.hi_word'):
            self._single_field_property_test(fut=self.dut.switch_interface.forwarding_table.entry[2].mac_address.hi_word, lsb=32, msb=47, low=32, high=47, is_volatile=True, default=None,
                                             rdl_name="csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.hi_word[47:32]",
                                             rdl_desc="Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='hi_word',
                                             parent_full_inst_name='csr.switch_interface.forwarding_table.entry[2].mac_address')
            self._single_int_field_read_and_write_test(fut=self.dut.switch_interface.forwarding_table.entry[2].mac_address.hi_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.switch_interface.forwarding_table.entry[2].iface.bitmap'):
            self._single_field_property_test(fut=self.dut.switch_interface.forwarding_table.entry[2].iface.bitmap, lsb=0, msb=3, low=0, high=3, is_volatile=True, default=None,
                                             rdl_name="csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]",
                                             rdl_desc="Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.",
                                             inst_name='bitmap',
                                             parent_full_inst_name='csr.switch_interface.forwarding_table.entry[2].iface')
            self._single_int_field_read_and_write_test(fut=self.dut.switch_interface.forwarding_table.entry[2].iface.bitmap, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.switch_interface.forwarding_table.entry[2].config.enabled'):
            self._single_field_property_test(fut=self.dut.switch_interface.forwarding_table.entry[2].config.enabled, lsb=0, msb=0, low=0, high=0, is_volatile=True, default=None,
                                             rdl_name="csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled",
                                             rdl_desc="Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.",
                                             inst_name='enabled',
                                             parent_full_inst_name='csr.switch_interface.forwarding_table.entry[2].config')
            self._single_int_field_read_and_write_test(fut=self.dut.switch_interface.forwarding_table.entry[2].config.enabled, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.switch_interface.forwarding_table.entry[3].mac_address.lo_word'):
            self._single_field_property_test(fut=self.dut.switch_interface.forwarding_table.entry[3].mac_address.lo_word, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.lo_word[31:0]",
                                             rdl_desc="Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='lo_word',
                                             parent_full_inst_name='csr.switch_interface.forwarding_table.entry[3].mac_address')
            self._single_int_field_read_and_write_test(fut=self.dut.switch_interface.forwarding_table.entry[3].mac_address.lo_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.switch_interface.forwarding_table.entry[3].mac_address.hi_word'):
            self._single_field_property_test(fut=self.dut.switch_interface.forwarding_table.entry[3].mac_address.hi_word, lsb=32, msb=47, low=32, high=47, is_volatile=True, default=None,
                                             rdl_name="csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.hi_word[47:32]",
                                             rdl_desc="Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='hi_word',
                                             parent_full_inst_name='csr.switch_interface.forwarding_table.entry[3].mac_address')
            self._single_int_field_read_and_write_test(fut=self.dut.switch_interface.forwarding_table.entry[3].mac_address.hi_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.switch_interface.forwarding_table.entry[3].iface.bitmap'):
            self._single_field_property_test(fut=self.dut.switch_interface.forwarding_table.entry[3].iface.bitmap, lsb=0, msb=3, low=0, high=3, is_volatile=True, default=None,
                                             rdl_name="csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]",
                                             rdl_desc="Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.",
                                             inst_name='bitmap',
                                             parent_full_inst_name='csr.switch_interface.forwarding_table.entry[3].iface')
            self._single_int_field_read_and_write_test(fut=self.dut.switch_interface.forwarding_table.entry[3].iface.bitmap, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.switch_interface.forwarding_table.entry[3].config.enabled'):
            self._single_field_property_test(fut=self.dut.switch_interface.forwarding_table.entry[3].config.enabled, lsb=0, msb=0, low=0, high=0, is_volatile=True, default=None,
                                             rdl_name="csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled",
                                             rdl_desc="Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.",
                                             inst_name='enabled',
                                             parent_full_inst_name='csr.switch_interface.forwarding_table.entry[3].config')
            self._single_int_field_read_and_write_test(fut=self.dut.switch_interface.forwarding_table.entry[3].config.enabled, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.switch_interface.forwarding_table.entry[4].mac_address.lo_word'):
            self._single_field_property_test(fut=self.dut.switch_interface.forwarding_table.entry[4].mac_address.lo_word, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.lo_word[31:0]",
                                             rdl_desc="Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='lo_word',
                                             parent_full_inst_name='csr.switch_interface.forwarding_table.entry[4].mac_address')
            self._single_int_field_read_and_write_test(fut=self.dut.switch_interface.forwarding_table.entry[4].mac_address.lo_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.switch_interface.forwarding_table.entry[4].mac_address.hi_word'):
            self._single_field_property_test(fut=self.dut.switch_interface.forwarding_table.entry[4].mac_address.hi_word, lsb=32, msb=47, low=32, high=47, is_volatile=True, default=None,
                                             rdl_name="csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.hi_word[47:32]",
                                             rdl_desc="Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='hi_word',
                                             parent_full_inst_name='csr.switch_interface.forwarding_table.entry[4].mac_address')
            self._single_int_field_read_and_write_test(fut=self.dut.switch_interface.forwarding_table.entry[4].mac_address.hi_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.switch_interface.forwarding_table.entry[4].iface.bitmap'):
            self._single_field_property_test(fut=self.dut.switch_interface.forwarding_table.entry[4].iface.bitmap, lsb=0, msb=3, low=0, high=3, is_volatile=True, default=None,
                                             rdl_name="csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]",
                                             rdl_desc="Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.",
                                             inst_name='bitmap',
                                             parent_full_inst_name='csr.switch_interface.forwarding_table.entry[4].iface')
            self._single_int_field_read_and_write_test(fut=self.dut.switch_interface.forwarding_table.entry[4].iface.bitmap, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.switch_interface.forwarding_table.entry[4].config.enabled'):
            self._single_field_property_test(fut=self.dut.switch_interface.forwarding_table.entry[4].config.enabled, lsb=0, msb=0, low=0, high=0, is_volatile=True, default=None,
                                             rdl_name="csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled",
                                             rdl_desc="Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.",
                                             inst_name='enabled',
                                             parent_full_inst_name='csr.switch_interface.forwarding_table.entry[4].config')
            self._single_int_field_read_and_write_test(fut=self.dut.switch_interface.forwarding_table.entry[4].config.enabled, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.switch_interface.forwarding_table.entry[5].mac_address.lo_word'):
            self._single_field_property_test(fut=self.dut.switch_interface.forwarding_table.entry[5].mac_address.lo_word, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.lo_word[31:0]",
                                             rdl_desc="Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='lo_word',
                                             parent_full_inst_name='csr.switch_interface.forwarding_table.entry[5].mac_address')
            self._single_int_field_read_and_write_test(fut=self.dut.switch_interface.forwarding_table.entry[5].mac_address.lo_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.switch_interface.forwarding_table.entry[5].mac_address.hi_word'):
            self._single_field_property_test(fut=self.dut.switch_interface.forwarding_table.entry[5].mac_address.hi_word, lsb=32, msb=47, low=32, high=47, is_volatile=True, default=None,
                                             rdl_name="csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.hi_word[47:32]",
                                             rdl_desc="Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='hi_word',
                                             parent_full_inst_name='csr.switch_interface.forwarding_table.entry[5].mac_address')
            self._single_int_field_read_and_write_test(fut=self.dut.switch_interface.forwarding_table.entry[5].mac_address.hi_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.switch_interface.forwarding_table.entry[5].iface.bitmap'):
            self._single_field_property_test(fut=self.dut.switch_interface.forwarding_table.entry[5].iface.bitmap, lsb=0, msb=3, low=0, high=3, is_volatile=True, default=None,
                                             rdl_name="csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]",
                                             rdl_desc="Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.",
                                             inst_name='bitmap',
                                             parent_full_inst_name='csr.switch_interface.forwarding_table.entry[5].iface')
            self._single_int_field_read_and_write_test(fut=self.dut.switch_interface.forwarding_table.entry[5].iface.bitmap, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.switch_interface.forwarding_table.entry[5].config.enabled'):
            self._single_field_property_test(fut=self.dut.switch_interface.forwarding_table.entry[5].config.enabled, lsb=0, msb=0, low=0, high=0, is_volatile=True, default=None,
                                             rdl_name="csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled",
                                             rdl_desc="Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.",
                                             inst_name='enabled',
                                             parent_full_inst_name='csr.switch_interface.forwarding_table.entry[5].config')
            self._single_int_field_read_and_write_test(fut=self.dut.switch_interface.forwarding_table.entry[5].config.enabled, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.switch_interface.forwarding_table.entry[6].mac_address.lo_word'):
            self._single_field_property_test(fut=self.dut.switch_interface.forwarding_table.entry[6].mac_address.lo_word, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.lo_word[31:0]",
                                             rdl_desc="Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='lo_word',
                                             parent_full_inst_name='csr.switch_interface.forwarding_table.entry[6].mac_address')
            self._single_int_field_read_and_write_test(fut=self.dut.switch_interface.forwarding_table.entry[6].mac_address.lo_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.switch_interface.forwarding_table.entry[6].mac_address.hi_word'):
            self._single_field_property_test(fut=self.dut.switch_interface.forwarding_table.entry[6].mac_address.hi_word, lsb=32, msb=47, low=32, high=47, is_volatile=True, default=None,
                                             rdl_name="csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.hi_word[47:32]",
                                             rdl_desc="Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='hi_word',
                                             parent_full_inst_name='csr.switch_interface.forwarding_table.entry[6].mac_address')
            self._single_int_field_read_and_write_test(fut=self.dut.switch_interface.forwarding_table.entry[6].mac_address.hi_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.switch_interface.forwarding_table.entry[6].iface.bitmap'):
            self._single_field_property_test(fut=self.dut.switch_interface.forwarding_table.entry[6].iface.bitmap, lsb=0, msb=3, low=0, high=3, is_volatile=True, default=None,
                                             rdl_name="csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]",
                                             rdl_desc="Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.",
                                             inst_name='bitmap',
                                             parent_full_inst_name='csr.switch_interface.forwarding_table.entry[6].iface')
            self._single_int_field_read_and_write_test(fut=self.dut.switch_interface.forwarding_table.entry[6].iface.bitmap, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.switch_interface.forwarding_table.entry[6].config.enabled'):
            self._single_field_property_test(fut=self.dut.switch_interface.forwarding_table.entry[6].config.enabled, lsb=0, msb=0, low=0, high=0, is_volatile=True, default=None,
                                             rdl_name="csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled",
                                             rdl_desc="Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.",
                                             inst_name='enabled',
                                             parent_full_inst_name='csr.switch_interface.forwarding_table.entry[6].config')
            self._single_int_field_read_and_write_test(fut=self.dut.switch_interface.forwarding_table.entry[6].config.enabled, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.switch_interface.forwarding_table.entry[7].mac_address.lo_word'):
            self._single_field_property_test(fut=self.dut.switch_interface.forwarding_table.entry[7].mac_address.lo_word, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.lo_word[31:0]",
                                             rdl_desc="Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='lo_word',
                                             parent_full_inst_name='csr.switch_interface.forwarding_table.entry[7].mac_address')
            self._single_int_field_read_and_write_test(fut=self.dut.switch_interface.forwarding_table.entry[7].mac_address.lo_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.switch_interface.forwarding_table.entry[7].mac_address.hi_word'):
            self._single_field_property_test(fut=self.dut.switch_interface.forwarding_table.entry[7].mac_address.hi_word, lsb=32, msb=47, low=32, high=47, is_volatile=True, default=None,
                                             rdl_name="csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.hi_word[47:32]",
                                             rdl_desc="Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='hi_word',
                                             parent_full_inst_name='csr.switch_interface.forwarding_table.entry[7].mac_address')
            self._single_int_field_read_and_write_test(fut=self.dut.switch_interface.forwarding_table.entry[7].mac_address.hi_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.switch_interface.forwarding_table.entry[7].iface.bitmap'):
            self._single_field_property_test(fut=self.dut.switch_interface.forwarding_table.entry[7].iface.bitmap, lsb=0, msb=3, low=0, high=3, is_volatile=True, default=None,
                                             rdl_name="csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]",
                                             rdl_desc="Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.",
                                             inst_name='bitmap',
                                             parent_full_inst_name='csr.switch_interface.forwarding_table.entry[7].iface')
            self._single_int_field_read_and_write_test(fut=self.dut.switch_interface.forwarding_table.entry[7].iface.bitmap, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: csr.switch_interface.forwarding_table.entry[7].config.enabled'):
            self._single_field_property_test(fut=self.dut.switch_interface.forwarding_table.entry[7].config.enabled, lsb=0, msb=0, low=0, high=0, is_volatile=True, default=None,
                                             rdl_name="csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled",
                                             rdl_desc="Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.",
                                             inst_name='enabled',
                                             parent_full_inst_name='csr.switch_interface.forwarding_table.entry[7].config')
            self._single_int_field_read_and_write_test(fut=self.dut.switch_interface.forwarding_table.entry[7].config.enabled, is_sw_readable=True, is_sw_writable=True)

    def test_addrmap(self) -> None:
        """
        Check the properties on the addrmaps files
        """

        
        with self.subTest(msg='addrmap: top_node'):
            self._single_addrmap_property_test(dut=self.dut,
                                               size=4352,
                                               rdl_name="csr",
                                               rdl_desc="openENOC Full Endpoint CSR",
                                               inst_name='csr',
                                               parent_full_inst_name=None)
            self._test_addrmap_iterators(dut=self.dut,
                                         writeable_registers=NodeIterators('test_reg','regB',),
                                         readable_registers=NodeIterators('test_reg','regB',),
                                         sections=NodeIterators('endpoint_interface','switch_interface',),
                                         memories=NodeIterators())
        


        # test all the address maps
        

    def test_regfile(self) -> None:
        """
        Check the properties on the register files
        """

        # test all the register files
        with self.subTest(msg='regfile: csr.endpoint_interface'):
            self._single_regfile_property_test(dut=self.dut.endpoint_interface,
                                               size=2048,
                                               rdl_name="csr.endpoint_interface",
                                               rdl_desc="Control and status register file for an openENOC Endpoint Interface instance.",
                                               inst_name='endpoint_interface',
                                               parent_full_inst_name='csr')
            self._test_regfile_iterators(dut=self.dut.endpoint_interface,
                                         writeable_registers=NodeIterators(),
                                         readable_registers=NodeIterators('info',),
                                         sections=NodeIterators('config','axis_if','peers','rmem',))
        with self.subTest(msg='regfile: csr.endpoint_interface.config'):
            self._single_regfile_property_test(dut=self.dut.endpoint_interface.config,
                                               size=8,
                                               rdl_name="csr.endpoint_interface.config",
                                               rdl_desc="Configuration register file for this openENOC Endpoint Interface instance.",
                                               inst_name='config',
                                               parent_full_inst_name='csr.endpoint_interface')
            self._test_regfile_iterators(dut=self.dut.endpoint_interface.config,
                                         writeable_registers=NodeIterators('mac_address',),
                                         readable_registers=NodeIterators('mac_address',),
                                         sections=NodeIterators())
        with self.subTest(msg='regfile: csr.endpoint_interface.axis_if'):
            self._single_regfile_property_test(dut=self.dut.endpoint_interface.axis_if,
                                               size=28,
                                               rdl_name="csr.endpoint_interface.axis_if",
                                               rdl_desc="Register file for the AXI4-Stream source and sink interfaces.",
                                               inst_name='axis_if',
                                               parent_full_inst_name='csr.endpoint_interface')
            self._test_regfile_iterators(dut=self.dut.endpoint_interface.axis_if,
                                         writeable_registers=NodeIterators(),
                                         readable_registers=NodeIterators(),
                                         sections=NodeIterators('source','sink',))
        with self.subTest(msg='regfile: csr.endpoint_interface.axis_if.source'):
            self._single_regfile_property_test(dut=self.dut.endpoint_interface.axis_if.source,
                                               size=12,
                                               rdl_name="csr.endpoint_interface.axis_if.source",
                                               rdl_desc="Register file for the AXI4-Stream source interface.",
                                               inst_name='source',
                                               parent_full_inst_name='csr.endpoint_interface.axis_if')
            self._test_regfile_iterators(dut=self.dut.endpoint_interface.axis_if.source,
                                         writeable_registers=NodeIterators('data','control',),
                                         readable_registers=NodeIterators('data','control','status',),
                                         sections=NodeIterators())
        with self.subTest(msg='regfile: csr.endpoint_interface.axis_if.sink'):
            self._single_regfile_property_test(dut=self.dut.endpoint_interface.axis_if.sink,
                                               size=12,
                                               rdl_name="csr.endpoint_interface.axis_if.sink",
                                               rdl_desc="Register file for the AXI4-Stream sink interface.",
                                               inst_name='sink',
                                               parent_full_inst_name='csr.endpoint_interface.axis_if')
            self._test_regfile_iterators(dut=self.dut.endpoint_interface.axis_if.sink,
                                         writeable_registers=NodeIterators('control',),
                                         readable_registers=NodeIterators('data','control','status',),
                                         sections=NodeIterators())
        with self.subTest(msg='regfile: csr.endpoint_interface.peers'):
            self._single_regfile_property_test(dut=self.dut.endpoint_interface.peers,
                                               size=112,
                                               rdl_name="csr.endpoint_interface.peers",
                                               rdl_desc="Register file for remote peer configuration and memory region information.",
                                               inst_name='peers',
                                               parent_full_inst_name='csr.endpoint_interface')
            self._test_regfile_iterators(dut=self.dut.endpoint_interface.peers,
                                         writeable_registers=NodeIterators(),
                                         readable_registers=NodeIterators(),
                                         sections=NodeIterators(('entry', [4]),))
        with self.subTest(msg='regfile: csr.endpoint_interface.peers.entry[0]'):
            self._single_regfile_property_test(dut=self.dut.endpoint_interface.peers.entry[0],
                                               size=28,
                                               rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1]",
                                               rdl_desc="Register file for a single remote peer configuration and memory region information.",
                                               inst_name='entry[0]',
                                               parent_full_inst_name='csr.endpoint_interface.peers')
            self._test_regfile_iterators(dut=self.dut.endpoint_interface.peers.entry[0],
                                         writeable_registers=NodeIterators('mac_address','rmem_address','local_address','remote_address','size','dma',),
                                         readable_registers=NodeIterators('mac_address','rmem_address','local_address','remote_address','size','dma',),
                                         sections=NodeIterators())
        with self.subTest(msg='regfile: csr.endpoint_interface.peers.entry[1]'):
            self._single_regfile_property_test(dut=self.dut.endpoint_interface.peers.entry[1],
                                               size=28,
                                               rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1]",
                                               rdl_desc="Register file for a single remote peer configuration and memory region information.",
                                               inst_name='entry[1]',
                                               parent_full_inst_name='csr.endpoint_interface.peers')
            self._test_regfile_iterators(dut=self.dut.endpoint_interface.peers.entry[1],
                                         writeable_registers=NodeIterators('mac_address','rmem_address','local_address','remote_address','size','dma',),
                                         readable_registers=NodeIterators('mac_address','rmem_address','local_address','remote_address','size','dma',),
                                         sections=NodeIterators())
        with self.subTest(msg='regfile: csr.endpoint_interface.peers.entry[2]'):
            self._single_regfile_property_test(dut=self.dut.endpoint_interface.peers.entry[2],
                                               size=28,
                                               rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1]",
                                               rdl_desc="Register file for a single remote peer configuration and memory region information.",
                                               inst_name='entry[2]',
                                               parent_full_inst_name='csr.endpoint_interface.peers')
            self._test_regfile_iterators(dut=self.dut.endpoint_interface.peers.entry[2],
                                         writeable_registers=NodeIterators('mac_address','rmem_address','local_address','remote_address','size','dma',),
                                         readable_registers=NodeIterators('mac_address','rmem_address','local_address','remote_address','size','dma',),
                                         sections=NodeIterators())
        with self.subTest(msg='regfile: csr.endpoint_interface.peers.entry[3]'):
            self._single_regfile_property_test(dut=self.dut.endpoint_interface.peers.entry[3],
                                               size=28,
                                               rdl_name="csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1]",
                                               rdl_desc="Register file for a single remote peer configuration and memory region information.",
                                               inst_name='entry[3]',
                                               parent_full_inst_name='csr.endpoint_interface.peers')
            self._test_regfile_iterators(dut=self.dut.endpoint_interface.peers.entry[3],
                                         writeable_registers=NodeIterators('mac_address','rmem_address','local_address','remote_address','size','dma',),
                                         readable_registers=NodeIterators('mac_address','rmem_address','local_address','remote_address','size','dma',),
                                         sections=NodeIterators())
        with self.subTest(msg='regfile: csr.endpoint_interface.rmem'):
            self._single_regfile_property_test(dut=self.dut.endpoint_interface.rmem,
                                               size=1024,
                                               rdl_name="csr.endpoint_interface.rmem",
                                               rdl_desc="Virtual memory region for all remote peers, with offsets and sizes defined in the peers regfile.",
                                               inst_name='rmem',
                                               parent_full_inst_name='csr.endpoint_interface')
            self._test_regfile_iterators(dut=self.dut.endpoint_interface.rmem,
                                         writeable_registers=NodeIterators(('word', [256]),),
                                         readable_registers=NodeIterators(('word', [256]),),
                                         sections=NodeIterators())
        with self.subTest(msg='regfile: csr.switch_interface'):
            self._single_regfile_property_test(dut=self.dut.switch_interface,
                                               size=256,
                                               rdl_name="csr.switch_interface",
                                               rdl_desc="Control and status register file for an openENOC Switch instance. It includes configuration registers and a forwarding table used to map destination MAC address keys to output interface selections for frame forwarding.",
                                               inst_name='switch_interface',
                                               parent_full_inst_name='csr')
            self._test_regfile_iterators(dut=self.dut.switch_interface,
                                         writeable_registers=NodeIterators('forwarding_control','default_forwarding',),
                                         readable_registers=NodeIterators('info','forwarding_control','default_forwarding',),
                                         sections=NodeIterators('forwarding_table',))
        with self.subTest(msg='regfile: csr.switch_interface.forwarding_table'):
            self._single_regfile_property_test(dut=self.dut.switch_interface.forwarding_table,
                                               size=128,
                                               rdl_name="csr.switch_interface.forwarding_table",
                                               rdl_desc="Forwarding table used to map MAC addresses to output interface selections for frame forwarding.",
                                               inst_name='forwarding_table',
                                               parent_full_inst_name='csr.switch_interface')
            self._test_regfile_iterators(dut=self.dut.switch_interface.forwarding_table,
                                         writeable_registers=NodeIterators(),
                                         readable_registers=NodeIterators(),
                                         sections=NodeIterators(('entry', [8]),))
        with self.subTest(msg='regfile: csr.switch_interface.forwarding_table.entry[0]'):
            self._single_regfile_property_test(dut=self.dut.switch_interface.forwarding_table.entry[0],
                                               size=16,
                                               rdl_name="csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1]",
                                               rdl_desc="Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.",
                                               inst_name='entry[0]',
                                               parent_full_inst_name='csr.switch_interface.forwarding_table')
            self._test_regfile_iterators(dut=self.dut.switch_interface.forwarding_table.entry[0],
                                         writeable_registers=NodeIterators('mac_address','iface','config',),
                                         readable_registers=NodeIterators('mac_address','iface','config',),
                                         sections=NodeIterators())
        with self.subTest(msg='regfile: csr.switch_interface.forwarding_table.entry[1]'):
            self._single_regfile_property_test(dut=self.dut.switch_interface.forwarding_table.entry[1],
                                               size=16,
                                               rdl_name="csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1]",
                                               rdl_desc="Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.",
                                               inst_name='entry[1]',
                                               parent_full_inst_name='csr.switch_interface.forwarding_table')
            self._test_regfile_iterators(dut=self.dut.switch_interface.forwarding_table.entry[1],
                                         writeable_registers=NodeIterators('mac_address','iface','config',),
                                         readable_registers=NodeIterators('mac_address','iface','config',),
                                         sections=NodeIterators())
        with self.subTest(msg='regfile: csr.switch_interface.forwarding_table.entry[2]'):
            self._single_regfile_property_test(dut=self.dut.switch_interface.forwarding_table.entry[2],
                                               size=16,
                                               rdl_name="csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1]",
                                               rdl_desc="Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.",
                                               inst_name='entry[2]',
                                               parent_full_inst_name='csr.switch_interface.forwarding_table')
            self._test_regfile_iterators(dut=self.dut.switch_interface.forwarding_table.entry[2],
                                         writeable_registers=NodeIterators('mac_address','iface','config',),
                                         readable_registers=NodeIterators('mac_address','iface','config',),
                                         sections=NodeIterators())
        with self.subTest(msg='regfile: csr.switch_interface.forwarding_table.entry[3]'):
            self._single_regfile_property_test(dut=self.dut.switch_interface.forwarding_table.entry[3],
                                               size=16,
                                               rdl_name="csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1]",
                                               rdl_desc="Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.",
                                               inst_name='entry[3]',
                                               parent_full_inst_name='csr.switch_interface.forwarding_table')
            self._test_regfile_iterators(dut=self.dut.switch_interface.forwarding_table.entry[3],
                                         writeable_registers=NodeIterators('mac_address','iface','config',),
                                         readable_registers=NodeIterators('mac_address','iface','config',),
                                         sections=NodeIterators())
        with self.subTest(msg='regfile: csr.switch_interface.forwarding_table.entry[4]'):
            self._single_regfile_property_test(dut=self.dut.switch_interface.forwarding_table.entry[4],
                                               size=16,
                                               rdl_name="csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1]",
                                               rdl_desc="Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.",
                                               inst_name='entry[4]',
                                               parent_full_inst_name='csr.switch_interface.forwarding_table')
            self._test_regfile_iterators(dut=self.dut.switch_interface.forwarding_table.entry[4],
                                         writeable_registers=NodeIterators('mac_address','iface','config',),
                                         readable_registers=NodeIterators('mac_address','iface','config',),
                                         sections=NodeIterators())
        with self.subTest(msg='regfile: csr.switch_interface.forwarding_table.entry[5]'):
            self._single_regfile_property_test(dut=self.dut.switch_interface.forwarding_table.entry[5],
                                               size=16,
                                               rdl_name="csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1]",
                                               rdl_desc="Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.",
                                               inst_name='entry[5]',
                                               parent_full_inst_name='csr.switch_interface.forwarding_table')
            self._test_regfile_iterators(dut=self.dut.switch_interface.forwarding_table.entry[5],
                                         writeable_registers=NodeIterators('mac_address','iface','config',),
                                         readable_registers=NodeIterators('mac_address','iface','config',),
                                         sections=NodeIterators())
        with self.subTest(msg='regfile: csr.switch_interface.forwarding_table.entry[6]'):
            self._single_regfile_property_test(dut=self.dut.switch_interface.forwarding_table.entry[6],
                                               size=16,
                                               rdl_name="csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1]",
                                               rdl_desc="Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.",
                                               inst_name='entry[6]',
                                               parent_full_inst_name='csr.switch_interface.forwarding_table')
            self._test_regfile_iterators(dut=self.dut.switch_interface.forwarding_table.entry[6],
                                         writeable_registers=NodeIterators('mac_address','iface','config',),
                                         readable_registers=NodeIterators('mac_address','iface','config',),
                                         sections=NodeIterators())
        with self.subTest(msg='regfile: csr.switch_interface.forwarding_table.entry[7]'):
            self._single_regfile_property_test(dut=self.dut.switch_interface.forwarding_table.entry[7],
                                               size=16,
                                               rdl_name="csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1]",
                                               rdl_desc="Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.",
                                               inst_name='entry[7]',
                                               parent_full_inst_name='csr.switch_interface.forwarding_table')
            self._test_regfile_iterators(dut=self.dut.switch_interface.forwarding_table.entry[7],
                                         writeable_registers=NodeIterators('mac_address','iface','config',),
                                         readable_registers=NodeIterators('mac_address','iface','config',),
                                         sections=NodeIterators())
        

    

    def test_array_slicing(self) -> None:
        """
        Check slicing into array
        """
        full_slice:NodeArray
        
        with self.subTest(msg='hidden_node: csr.endpoint_interface.peers.entry[]'):
            
            full_slice = self.dut.endpoint_interface.peers.get_child_by_system_rdl_name('entry')
            
            self.assertCountEqual(iter(full_slice[:]), iter(full_slice))
        
        with self.subTest(msg='hidden_node: csr.endpoint_interface.rmem.word[]'):
            
            full_slice = self.dut.endpoint_interface.rmem.get_child_by_system_rdl_name('word')
            
            self.assertCountEqual(iter(full_slice[:]), iter(full_slice))
        
        with self.subTest(msg='hidden_node: csr.switch_interface.forwarding_table.entry[]'):
            
            full_slice = self.dut.switch_interface.forwarding_table.get_child_by_system_rdl_name('entry')
            
            self.assertCountEqual(iter(full_slice[:]), iter(full_slice))
        



class csr_block_access(csr_TestCase_BlockAccess): # type: ignore[valid-type,misc]
    """
    tests for all the block access methods
    """

    

    def test_register_array_context_manager(self) -> None:
        """
        Walk the register map and check that register map context managers work correctly
        """
        
        # test context manager to register:
        # csr.endpoint_interface.rmem.word[]
        # size 4
        # total_size 1024
        empty_read = [0 for i in range(1024 // 4)]
        follow_along = [0 for i in range(1024 // 4)]
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[]'):
            with patch(base_name + '.write_addr_space') as write_callback_mock,\
                                patch(base_name + '.read_addr_space', return_value=0) as read_callback_mock, \
                                patch(base_name + '.read_block_addr_space',
                                      return_value=empty_read) as read_block_callback_mock , \
                                patch(base_name + '.write_block_addr_space') as write_block_callback_mock:
                with self.dut.endpoint_interface.rmem.word.single_read_modify_write() as dut:
                    pass
                
                read_callback_mock.assert_not_called()
                write_callback_mock.assert_not_called()

class csr_alt_block_access(csr_TestCase_AltBlockAccess): # type: ignore[valid-type,misc]
    """
    tests for all the block access methods with the alternative callbacks, this is a simpler
    version of the tests above
    """
    

    def test_register_array_context_manager(self) -> None:
        """
        Walk the register map and check that register map context managers work correctly
        """
        
        # test context manager to register with alt block interfaces:
        # csr.endpoint_interface.rmem.word[]
        # size 4
        # total_size 1024
        
        empty_read = [0 for i in range(1024 // 4)]
        follow_along = [0 for i in range(1024 // 4)]
        with self.subTest(msg='register: csr.endpoint_interface.rmem.word[]'):
            with patch(base_name + '.write_addr_space') as write_callback_mock,\
                            patch(base_name + '.read_addr_space', return_value=1) as read_callback_mock, \
                            patch(base_name + '.read_block_addr_space_alt',
                                  return_value=Array('L', empty_read)) as read_block_callback_mock , \
                            patch(base_name + '.write_block_addr_space_alt') as write_block_callback_mock:
                with self.dut.endpoint_interface.rmem.word.single_read_modify_write() as dut:
                    pass
                
                read_callback_mock.assert_not_called()
                write_callback_mock.assert_not_called()
        


if __name__ == '__main__':

    unittest.main()