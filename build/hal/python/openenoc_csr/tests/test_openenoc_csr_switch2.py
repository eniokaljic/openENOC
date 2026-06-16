


"""
Unit Tests for the openenoc_csr register model Python Wrapper

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




class openenoc_csr_switch2_single_access(openenoc_csr_TestCase): # type: ignore[valid-type,misc]



    def test_user_defined_properties(self)  -> None:
        """
        Walk the address map and check user defined properties are correctly pulled up
        """
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[0]'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[0].udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[1]'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[1].udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[2]'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[2].udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[3]'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[3].udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[4]'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[4].udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[5]'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[5].udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[6]'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[6].udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[7]'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[7].udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[8]'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[8].udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[9]'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[9].udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[10]'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[10].udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[11]'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[11].udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[12]'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[12].udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[13]'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[13].udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[14]'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[14].udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[15]'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[15].udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[16]'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[16].udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[17]'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[17].udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[18]'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[18].udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[19]'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[19].udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[20]'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[20].udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[21]'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[21].udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[22]'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[22].udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[23]'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[23].udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[24]'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[24].udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[25]'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[25].udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[26]'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[26].udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[27]'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[27].udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[28]'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[28].udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[29]'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[29].udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[30]'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[30].udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[31]'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[31].udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.info'):
            
            
            self.assertDictEqual(self.dut.switch2.info.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_control'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_control.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.default_forwarding'):
            
            
            self.assertDictEqual(self.dut.switch2.default_forwarding.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[0].macaddr'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[0].macaddr.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[0].iface'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[0].iface.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[0].config'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[0].config.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[1].macaddr'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[1].macaddr.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[1].iface'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[1].iface.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[1].config'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[1].config.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[2].macaddr'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[2].macaddr.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[2].iface'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[2].iface.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[2].config'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[2].config.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[3].macaddr'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[3].macaddr.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[3].iface'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[3].iface.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[3].config'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[3].config.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[4].macaddr'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[4].macaddr.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[4].iface'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[4].iface.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[4].config'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[4].config.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[5].macaddr'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[5].macaddr.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[5].iface'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[5].iface.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[5].config'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[5].config.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[6].macaddr'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[6].macaddr.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[6].iface'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[6].iface.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[6].config'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[6].config.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[7].macaddr'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[7].macaddr.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[7].iface'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[7].iface.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[7].config'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[7].config.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[8].macaddr'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[8].macaddr.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[8].iface'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[8].iface.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[8].config'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[8].config.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[9].macaddr'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[9].macaddr.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[9].iface'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[9].iface.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[9].config'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[9].config.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[10].macaddr'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[10].macaddr.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[10].iface'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[10].iface.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[10].config'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[10].config.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[11].macaddr'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[11].macaddr.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[11].iface'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[11].iface.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[11].config'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[11].config.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[12].macaddr'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[12].macaddr.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[12].iface'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[12].iface.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[12].config'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[12].config.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[13].macaddr'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[13].macaddr.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[13].iface'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[13].iface.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[13].config'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[13].config.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[14].macaddr'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[14].macaddr.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[14].iface'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[14].iface.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[14].config'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[14].config.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[15].macaddr'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[15].macaddr.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[15].iface'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[15].iface.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[15].config'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[15].config.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[16].macaddr'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[16].macaddr.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[16].iface'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[16].iface.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[16].config'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[16].config.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[17].macaddr'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[17].macaddr.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[17].iface'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[17].iface.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[17].config'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[17].config.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[18].macaddr'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[18].macaddr.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[18].iface'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[18].iface.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[18].config'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[18].config.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[19].macaddr'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[19].macaddr.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[19].iface'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[19].iface.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[19].config'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[19].config.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[20].macaddr'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[20].macaddr.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[20].iface'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[20].iface.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[20].config'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[20].config.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[21].macaddr'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[21].macaddr.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[21].iface'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[21].iface.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[21].config'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[21].config.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[22].macaddr'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[22].macaddr.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[22].iface'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[22].iface.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[22].config'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[22].config.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[23].macaddr'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[23].macaddr.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[23].iface'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[23].iface.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[23].config'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[23].config.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[24].macaddr'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[24].macaddr.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[24].iface'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[24].iface.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[24].config'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[24].config.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[25].macaddr'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[25].macaddr.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[25].iface'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[25].iface.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[25].config'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[25].config.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[26].macaddr'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[26].macaddr.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[26].iface'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[26].iface.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[26].config'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[26].config.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[27].macaddr'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[27].macaddr.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[27].iface'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[27].iface.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[27].config'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[27].config.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[28].macaddr'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[28].macaddr.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[28].iface'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[28].iface.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[28].config'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[28].config.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[29].macaddr'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[29].macaddr.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[29].iface'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[29].iface.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[29].config'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[29].config.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[30].macaddr'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[30].macaddr.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[30].iface'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[30].iface.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[30].config'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[30].config.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[31].macaddr'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[31].macaddr.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[31].iface'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[31].iface.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[31].config'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[31].config.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.info.table_depth'):
            
            
            self.assertDictEqual(self.dut.switch2.info.table_depth.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.info.num_of_interfaces'):
            
            
            self.assertDictEqual(self.dut.switch2.info.num_of_interfaces.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_control.operation_mode'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_control.operation_mode.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_control.pause_request'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_control.pause_request.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_control.pause_done'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_control.pause_done.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.default_forwarding.bitmap'):
            
            
            self.assertDictEqual(self.dut.switch2.default_forwarding.bitmap.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[0].macaddr.lo_word'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[0].macaddr.lo_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[0].macaddr.hi_word'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[0].macaddr.hi_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[0].iface.bitmap'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[0].iface.bitmap.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[0].config.enabled'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[0].config.enabled.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[1].macaddr.lo_word'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[1].macaddr.lo_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[1].macaddr.hi_word'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[1].macaddr.hi_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[1].iface.bitmap'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[1].iface.bitmap.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[1].config.enabled'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[1].config.enabled.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[2].macaddr.lo_word'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[2].macaddr.lo_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[2].macaddr.hi_word'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[2].macaddr.hi_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[2].iface.bitmap'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[2].iface.bitmap.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[2].config.enabled'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[2].config.enabled.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[3].macaddr.lo_word'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[3].macaddr.lo_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[3].macaddr.hi_word'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[3].macaddr.hi_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[3].iface.bitmap'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[3].iface.bitmap.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[3].config.enabled'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[3].config.enabled.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[4].macaddr.lo_word'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[4].macaddr.lo_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[4].macaddr.hi_word'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[4].macaddr.hi_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[4].iface.bitmap'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[4].iface.bitmap.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[4].config.enabled'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[4].config.enabled.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[5].macaddr.lo_word'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[5].macaddr.lo_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[5].macaddr.hi_word'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[5].macaddr.hi_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[5].iface.bitmap'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[5].iface.bitmap.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[5].config.enabled'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[5].config.enabled.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[6].macaddr.lo_word'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[6].macaddr.lo_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[6].macaddr.hi_word'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[6].macaddr.hi_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[6].iface.bitmap'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[6].iface.bitmap.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[6].config.enabled'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[6].config.enabled.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[7].macaddr.lo_word'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[7].macaddr.lo_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[7].macaddr.hi_word'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[7].macaddr.hi_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[7].iface.bitmap'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[7].iface.bitmap.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[7].config.enabled'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[7].config.enabled.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[8].macaddr.lo_word'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[8].macaddr.lo_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[8].macaddr.hi_word'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[8].macaddr.hi_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[8].iface.bitmap'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[8].iface.bitmap.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[8].config.enabled'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[8].config.enabled.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[9].macaddr.lo_word'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[9].macaddr.lo_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[9].macaddr.hi_word'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[9].macaddr.hi_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[9].iface.bitmap'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[9].iface.bitmap.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[9].config.enabled'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[9].config.enabled.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[10].macaddr.lo_word'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[10].macaddr.lo_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[10].macaddr.hi_word'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[10].macaddr.hi_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[10].iface.bitmap'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[10].iface.bitmap.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[10].config.enabled'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[10].config.enabled.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[11].macaddr.lo_word'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[11].macaddr.lo_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[11].macaddr.hi_word'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[11].macaddr.hi_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[11].iface.bitmap'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[11].iface.bitmap.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[11].config.enabled'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[11].config.enabled.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[12].macaddr.lo_word'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[12].macaddr.lo_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[12].macaddr.hi_word'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[12].macaddr.hi_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[12].iface.bitmap'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[12].iface.bitmap.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[12].config.enabled'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[12].config.enabled.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[13].macaddr.lo_word'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[13].macaddr.lo_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[13].macaddr.hi_word'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[13].macaddr.hi_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[13].iface.bitmap'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[13].iface.bitmap.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[13].config.enabled'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[13].config.enabled.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[14].macaddr.lo_word'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[14].macaddr.lo_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[14].macaddr.hi_word'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[14].macaddr.hi_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[14].iface.bitmap'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[14].iface.bitmap.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[14].config.enabled'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[14].config.enabled.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[15].macaddr.lo_word'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[15].macaddr.lo_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[15].macaddr.hi_word'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[15].macaddr.hi_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[15].iface.bitmap'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[15].iface.bitmap.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[15].config.enabled'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[15].config.enabled.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[16].macaddr.lo_word'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[16].macaddr.lo_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[16].macaddr.hi_word'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[16].macaddr.hi_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[16].iface.bitmap'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[16].iface.bitmap.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[16].config.enabled'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[16].config.enabled.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[17].macaddr.lo_word'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[17].macaddr.lo_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[17].macaddr.hi_word'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[17].macaddr.hi_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[17].iface.bitmap'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[17].iface.bitmap.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[17].config.enabled'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[17].config.enabled.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[18].macaddr.lo_word'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[18].macaddr.lo_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[18].macaddr.hi_word'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[18].macaddr.hi_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[18].iface.bitmap'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[18].iface.bitmap.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[18].config.enabled'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[18].config.enabled.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[19].macaddr.lo_word'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[19].macaddr.lo_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[19].macaddr.hi_word'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[19].macaddr.hi_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[19].iface.bitmap'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[19].iface.bitmap.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[19].config.enabled'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[19].config.enabled.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[20].macaddr.lo_word'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[20].macaddr.lo_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[20].macaddr.hi_word'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[20].macaddr.hi_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[20].iface.bitmap'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[20].iface.bitmap.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[20].config.enabled'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[20].config.enabled.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[21].macaddr.lo_word'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[21].macaddr.lo_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[21].macaddr.hi_word'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[21].macaddr.hi_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[21].iface.bitmap'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[21].iface.bitmap.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[21].config.enabled'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[21].config.enabled.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[22].macaddr.lo_word'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[22].macaddr.lo_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[22].macaddr.hi_word'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[22].macaddr.hi_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[22].iface.bitmap'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[22].iface.bitmap.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[22].config.enabled'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[22].config.enabled.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[23].macaddr.lo_word'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[23].macaddr.lo_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[23].macaddr.hi_word'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[23].macaddr.hi_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[23].iface.bitmap'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[23].iface.bitmap.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[23].config.enabled'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[23].config.enabled.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[24].macaddr.lo_word'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[24].macaddr.lo_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[24].macaddr.hi_word'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[24].macaddr.hi_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[24].iface.bitmap'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[24].iface.bitmap.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[24].config.enabled'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[24].config.enabled.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[25].macaddr.lo_word'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[25].macaddr.lo_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[25].macaddr.hi_word'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[25].macaddr.hi_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[25].iface.bitmap'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[25].iface.bitmap.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[25].config.enabled'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[25].config.enabled.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[26].macaddr.lo_word'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[26].macaddr.lo_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[26].macaddr.hi_word'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[26].macaddr.hi_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[26].iface.bitmap'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[26].iface.bitmap.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[26].config.enabled'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[26].config.enabled.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[27].macaddr.lo_word'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[27].macaddr.lo_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[27].macaddr.hi_word'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[27].macaddr.hi_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[27].iface.bitmap'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[27].iface.bitmap.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[27].config.enabled'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[27].config.enabled.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[28].macaddr.lo_word'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[28].macaddr.lo_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[28].macaddr.hi_word'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[28].macaddr.hi_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[28].iface.bitmap'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[28].iface.bitmap.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[28].config.enabled'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[28].config.enabled.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[29].macaddr.lo_word'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[29].macaddr.lo_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[29].macaddr.hi_word'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[29].macaddr.hi_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[29].iface.bitmap'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[29].iface.bitmap.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[29].config.enabled'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[29].config.enabled.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[30].macaddr.lo_word'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[30].macaddr.lo_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[30].macaddr.hi_word'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[30].macaddr.hi_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[30].iface.bitmap'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[30].iface.bitmap.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[30].config.enabled'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[30].config.enabled.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[31].macaddr.lo_word'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[31].macaddr.lo_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[31].macaddr.hi_word'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[31].macaddr.hi_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[31].iface.bitmap'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[31].iface.bitmap.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[31].config.enabled'):
            
            
            self.assertDictEqual(self.dut.switch2.forwarding_table.entry[31].config.enabled.udp,{})
            
        

     

    def test_register(self) -> None:
        """
        Walk the registers in the register map and check:
        - the properties
        - it can be read and written to correctly
        """
        with self.subTest(msg='register: openenoc_csr.switch2.info'):
            self._single_register_property_test(rut=self.dut.switch2.info, address=1024, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.info",
                                                rdl_desc="Read-only information register for this openENOC Switch instance.",
                                                inst_name='info',
                                                parent_full_inst_name='openenoc_csr.switch2')
            self._single_register_read_and_write_test(rut=self.dut.switch2.info, has_sw_readable=True, has_sw_writable=False,
                                                                                          readable_fields=set(['table_depth','num_of_interfaces', ]),
                                                                                          writeable_fields=set([ ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_control'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_control, address=1028, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_control",
                                                rdl_desc="Forwarding control register for the openENOC Switch instance.",
                                                inst_name='forwarding_control',
                                                parent_full_inst_name='openenoc_csr.switch2')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_control, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['operation_mode','pause_request','pause_done', ]),
                                                                                          writeable_fields=set(['operation_mode','pause_request', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.default_forwarding'):
            self._single_register_property_test(rut=self.dut.switch2.default_forwarding, address=1032, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.default_forwarding",
                                                rdl_desc="Defines the destination interface or interfaces for frames that do not match any enabled forwarding table entry.",
                                                inst_name='default_forwarding',
                                                parent_full_inst_name='openenoc_csr.switch2')
            self._single_register_read_and_write_test(rut=self.dut.switch2.default_forwarding, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['bitmap', ]),
                                                                                          writeable_fields=set(['bitmap', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[0].macaddr'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[0].macaddr, address=1536, width=64, accesswidth=32, size=8,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr",
                                                rdl_desc="48-bit destination MAC address used as the key for this forwarding table entry.",
                                                inst_name='macaddr',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[0]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[0].macaddr, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['lo_word','hi_word', ]),
                                                                                          writeable_fields=set(['lo_word','hi_word', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[0].iface'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[0].iface, address=1544, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface",
                                                rdl_desc="Forwarding interface information associated with this forwarding table entry.",
                                                inst_name='iface',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[0]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[0].iface, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['bitmap', ]),
                                                                                          writeable_fields=set(['bitmap', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[0].config'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[0].config, address=1548, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config",
                                                rdl_desc="Configuration information associated with this forwarding table entry.",
                                                inst_name='config',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[0]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[0].config, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['enabled', ]),
                                                                                          writeable_fields=set(['enabled', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[1].macaddr'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[1].macaddr, address=1552, width=64, accesswidth=32, size=8,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr",
                                                rdl_desc="48-bit destination MAC address used as the key for this forwarding table entry.",
                                                inst_name='macaddr',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[1]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[1].macaddr, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['lo_word','hi_word', ]),
                                                                                          writeable_fields=set(['lo_word','hi_word', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[1].iface'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[1].iface, address=1560, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface",
                                                rdl_desc="Forwarding interface information associated with this forwarding table entry.",
                                                inst_name='iface',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[1]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[1].iface, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['bitmap', ]),
                                                                                          writeable_fields=set(['bitmap', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[1].config'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[1].config, address=1564, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config",
                                                rdl_desc="Configuration information associated with this forwarding table entry.",
                                                inst_name='config',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[1]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[1].config, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['enabled', ]),
                                                                                          writeable_fields=set(['enabled', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[2].macaddr'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[2].macaddr, address=1568, width=64, accesswidth=32, size=8,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr",
                                                rdl_desc="48-bit destination MAC address used as the key for this forwarding table entry.",
                                                inst_name='macaddr',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[2]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[2].macaddr, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['lo_word','hi_word', ]),
                                                                                          writeable_fields=set(['lo_word','hi_word', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[2].iface'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[2].iface, address=1576, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface",
                                                rdl_desc="Forwarding interface information associated with this forwarding table entry.",
                                                inst_name='iface',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[2]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[2].iface, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['bitmap', ]),
                                                                                          writeable_fields=set(['bitmap', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[2].config'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[2].config, address=1580, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config",
                                                rdl_desc="Configuration information associated with this forwarding table entry.",
                                                inst_name='config',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[2]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[2].config, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['enabled', ]),
                                                                                          writeable_fields=set(['enabled', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[3].macaddr'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[3].macaddr, address=1584, width=64, accesswidth=32, size=8,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr",
                                                rdl_desc="48-bit destination MAC address used as the key for this forwarding table entry.",
                                                inst_name='macaddr',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[3]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[3].macaddr, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['lo_word','hi_word', ]),
                                                                                          writeable_fields=set(['lo_word','hi_word', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[3].iface'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[3].iface, address=1592, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface",
                                                rdl_desc="Forwarding interface information associated with this forwarding table entry.",
                                                inst_name='iface',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[3]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[3].iface, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['bitmap', ]),
                                                                                          writeable_fields=set(['bitmap', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[3].config'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[3].config, address=1596, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config",
                                                rdl_desc="Configuration information associated with this forwarding table entry.",
                                                inst_name='config',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[3]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[3].config, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['enabled', ]),
                                                                                          writeable_fields=set(['enabled', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[4].macaddr'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[4].macaddr, address=1600, width=64, accesswidth=32, size=8,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr",
                                                rdl_desc="48-bit destination MAC address used as the key for this forwarding table entry.",
                                                inst_name='macaddr',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[4]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[4].macaddr, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['lo_word','hi_word', ]),
                                                                                          writeable_fields=set(['lo_word','hi_word', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[4].iface'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[4].iface, address=1608, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface",
                                                rdl_desc="Forwarding interface information associated with this forwarding table entry.",
                                                inst_name='iface',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[4]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[4].iface, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['bitmap', ]),
                                                                                          writeable_fields=set(['bitmap', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[4].config'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[4].config, address=1612, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config",
                                                rdl_desc="Configuration information associated with this forwarding table entry.",
                                                inst_name='config',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[4]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[4].config, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['enabled', ]),
                                                                                          writeable_fields=set(['enabled', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[5].macaddr'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[5].macaddr, address=1616, width=64, accesswidth=32, size=8,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr",
                                                rdl_desc="48-bit destination MAC address used as the key for this forwarding table entry.",
                                                inst_name='macaddr',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[5]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[5].macaddr, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['lo_word','hi_word', ]),
                                                                                          writeable_fields=set(['lo_word','hi_word', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[5].iface'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[5].iface, address=1624, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface",
                                                rdl_desc="Forwarding interface information associated with this forwarding table entry.",
                                                inst_name='iface',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[5]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[5].iface, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['bitmap', ]),
                                                                                          writeable_fields=set(['bitmap', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[5].config'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[5].config, address=1628, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config",
                                                rdl_desc="Configuration information associated with this forwarding table entry.",
                                                inst_name='config',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[5]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[5].config, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['enabled', ]),
                                                                                          writeable_fields=set(['enabled', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[6].macaddr'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[6].macaddr, address=1632, width=64, accesswidth=32, size=8,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr",
                                                rdl_desc="48-bit destination MAC address used as the key for this forwarding table entry.",
                                                inst_name='macaddr',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[6]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[6].macaddr, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['lo_word','hi_word', ]),
                                                                                          writeable_fields=set(['lo_word','hi_word', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[6].iface'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[6].iface, address=1640, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface",
                                                rdl_desc="Forwarding interface information associated with this forwarding table entry.",
                                                inst_name='iface',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[6]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[6].iface, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['bitmap', ]),
                                                                                          writeable_fields=set(['bitmap', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[6].config'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[6].config, address=1644, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config",
                                                rdl_desc="Configuration information associated with this forwarding table entry.",
                                                inst_name='config',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[6]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[6].config, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['enabled', ]),
                                                                                          writeable_fields=set(['enabled', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[7].macaddr'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[7].macaddr, address=1648, width=64, accesswidth=32, size=8,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr",
                                                rdl_desc="48-bit destination MAC address used as the key for this forwarding table entry.",
                                                inst_name='macaddr',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[7]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[7].macaddr, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['lo_word','hi_word', ]),
                                                                                          writeable_fields=set(['lo_word','hi_word', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[7].iface'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[7].iface, address=1656, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface",
                                                rdl_desc="Forwarding interface information associated with this forwarding table entry.",
                                                inst_name='iface',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[7]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[7].iface, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['bitmap', ]),
                                                                                          writeable_fields=set(['bitmap', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[7].config'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[7].config, address=1660, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config",
                                                rdl_desc="Configuration information associated with this forwarding table entry.",
                                                inst_name='config',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[7]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[7].config, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['enabled', ]),
                                                                                          writeable_fields=set(['enabled', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[8].macaddr'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[8].macaddr, address=1664, width=64, accesswidth=32, size=8,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr",
                                                rdl_desc="48-bit destination MAC address used as the key for this forwarding table entry.",
                                                inst_name='macaddr',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[8]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[8].macaddr, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['lo_word','hi_word', ]),
                                                                                          writeable_fields=set(['lo_word','hi_word', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[8].iface'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[8].iface, address=1672, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface",
                                                rdl_desc="Forwarding interface information associated with this forwarding table entry.",
                                                inst_name='iface',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[8]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[8].iface, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['bitmap', ]),
                                                                                          writeable_fields=set(['bitmap', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[8].config'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[8].config, address=1676, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config",
                                                rdl_desc="Configuration information associated with this forwarding table entry.",
                                                inst_name='config',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[8]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[8].config, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['enabled', ]),
                                                                                          writeable_fields=set(['enabled', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[9].macaddr'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[9].macaddr, address=1680, width=64, accesswidth=32, size=8,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr",
                                                rdl_desc="48-bit destination MAC address used as the key for this forwarding table entry.",
                                                inst_name='macaddr',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[9]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[9].macaddr, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['lo_word','hi_word', ]),
                                                                                          writeable_fields=set(['lo_word','hi_word', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[9].iface'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[9].iface, address=1688, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface",
                                                rdl_desc="Forwarding interface information associated with this forwarding table entry.",
                                                inst_name='iface',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[9]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[9].iface, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['bitmap', ]),
                                                                                          writeable_fields=set(['bitmap', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[9].config'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[9].config, address=1692, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config",
                                                rdl_desc="Configuration information associated with this forwarding table entry.",
                                                inst_name='config',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[9]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[9].config, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['enabled', ]),
                                                                                          writeable_fields=set(['enabled', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[10].macaddr'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[10].macaddr, address=1696, width=64, accesswidth=32, size=8,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr",
                                                rdl_desc="48-bit destination MAC address used as the key for this forwarding table entry.",
                                                inst_name='macaddr',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[10]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[10].macaddr, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['lo_word','hi_word', ]),
                                                                                          writeable_fields=set(['lo_word','hi_word', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[10].iface'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[10].iface, address=1704, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface",
                                                rdl_desc="Forwarding interface information associated with this forwarding table entry.",
                                                inst_name='iface',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[10]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[10].iface, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['bitmap', ]),
                                                                                          writeable_fields=set(['bitmap', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[10].config'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[10].config, address=1708, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config",
                                                rdl_desc="Configuration information associated with this forwarding table entry.",
                                                inst_name='config',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[10]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[10].config, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['enabled', ]),
                                                                                          writeable_fields=set(['enabled', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[11].macaddr'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[11].macaddr, address=1712, width=64, accesswidth=32, size=8,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr",
                                                rdl_desc="48-bit destination MAC address used as the key for this forwarding table entry.",
                                                inst_name='macaddr',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[11]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[11].macaddr, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['lo_word','hi_word', ]),
                                                                                          writeable_fields=set(['lo_word','hi_word', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[11].iface'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[11].iface, address=1720, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface",
                                                rdl_desc="Forwarding interface information associated with this forwarding table entry.",
                                                inst_name='iface',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[11]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[11].iface, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['bitmap', ]),
                                                                                          writeable_fields=set(['bitmap', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[11].config'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[11].config, address=1724, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config",
                                                rdl_desc="Configuration information associated with this forwarding table entry.",
                                                inst_name='config',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[11]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[11].config, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['enabled', ]),
                                                                                          writeable_fields=set(['enabled', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[12].macaddr'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[12].macaddr, address=1728, width=64, accesswidth=32, size=8,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr",
                                                rdl_desc="48-bit destination MAC address used as the key for this forwarding table entry.",
                                                inst_name='macaddr',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[12]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[12].macaddr, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['lo_word','hi_word', ]),
                                                                                          writeable_fields=set(['lo_word','hi_word', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[12].iface'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[12].iface, address=1736, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface",
                                                rdl_desc="Forwarding interface information associated with this forwarding table entry.",
                                                inst_name='iface',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[12]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[12].iface, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['bitmap', ]),
                                                                                          writeable_fields=set(['bitmap', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[12].config'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[12].config, address=1740, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config",
                                                rdl_desc="Configuration information associated with this forwarding table entry.",
                                                inst_name='config',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[12]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[12].config, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['enabled', ]),
                                                                                          writeable_fields=set(['enabled', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[13].macaddr'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[13].macaddr, address=1744, width=64, accesswidth=32, size=8,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr",
                                                rdl_desc="48-bit destination MAC address used as the key for this forwarding table entry.",
                                                inst_name='macaddr',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[13]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[13].macaddr, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['lo_word','hi_word', ]),
                                                                                          writeable_fields=set(['lo_word','hi_word', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[13].iface'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[13].iface, address=1752, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface",
                                                rdl_desc="Forwarding interface information associated with this forwarding table entry.",
                                                inst_name='iface',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[13]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[13].iface, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['bitmap', ]),
                                                                                          writeable_fields=set(['bitmap', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[13].config'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[13].config, address=1756, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config",
                                                rdl_desc="Configuration information associated with this forwarding table entry.",
                                                inst_name='config',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[13]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[13].config, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['enabled', ]),
                                                                                          writeable_fields=set(['enabled', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[14].macaddr'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[14].macaddr, address=1760, width=64, accesswidth=32, size=8,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr",
                                                rdl_desc="48-bit destination MAC address used as the key for this forwarding table entry.",
                                                inst_name='macaddr',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[14]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[14].macaddr, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['lo_word','hi_word', ]),
                                                                                          writeable_fields=set(['lo_word','hi_word', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[14].iface'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[14].iface, address=1768, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface",
                                                rdl_desc="Forwarding interface information associated with this forwarding table entry.",
                                                inst_name='iface',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[14]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[14].iface, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['bitmap', ]),
                                                                                          writeable_fields=set(['bitmap', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[14].config'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[14].config, address=1772, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config",
                                                rdl_desc="Configuration information associated with this forwarding table entry.",
                                                inst_name='config',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[14]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[14].config, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['enabled', ]),
                                                                                          writeable_fields=set(['enabled', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[15].macaddr'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[15].macaddr, address=1776, width=64, accesswidth=32, size=8,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr",
                                                rdl_desc="48-bit destination MAC address used as the key for this forwarding table entry.",
                                                inst_name='macaddr',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[15]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[15].macaddr, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['lo_word','hi_word', ]),
                                                                                          writeable_fields=set(['lo_word','hi_word', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[15].iface'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[15].iface, address=1784, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface",
                                                rdl_desc="Forwarding interface information associated with this forwarding table entry.",
                                                inst_name='iface',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[15]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[15].iface, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['bitmap', ]),
                                                                                          writeable_fields=set(['bitmap', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[15].config'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[15].config, address=1788, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config",
                                                rdl_desc="Configuration information associated with this forwarding table entry.",
                                                inst_name='config',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[15]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[15].config, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['enabled', ]),
                                                                                          writeable_fields=set(['enabled', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[16].macaddr'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[16].macaddr, address=1792, width=64, accesswidth=32, size=8,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr",
                                                rdl_desc="48-bit destination MAC address used as the key for this forwarding table entry.",
                                                inst_name='macaddr',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[16]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[16].macaddr, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['lo_word','hi_word', ]),
                                                                                          writeable_fields=set(['lo_word','hi_word', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[16].iface'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[16].iface, address=1800, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface",
                                                rdl_desc="Forwarding interface information associated with this forwarding table entry.",
                                                inst_name='iface',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[16]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[16].iface, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['bitmap', ]),
                                                                                          writeable_fields=set(['bitmap', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[16].config'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[16].config, address=1804, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config",
                                                rdl_desc="Configuration information associated with this forwarding table entry.",
                                                inst_name='config',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[16]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[16].config, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['enabled', ]),
                                                                                          writeable_fields=set(['enabled', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[17].macaddr'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[17].macaddr, address=1808, width=64, accesswidth=32, size=8,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr",
                                                rdl_desc="48-bit destination MAC address used as the key for this forwarding table entry.",
                                                inst_name='macaddr',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[17]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[17].macaddr, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['lo_word','hi_word', ]),
                                                                                          writeable_fields=set(['lo_word','hi_word', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[17].iface'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[17].iface, address=1816, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface",
                                                rdl_desc="Forwarding interface information associated with this forwarding table entry.",
                                                inst_name='iface',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[17]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[17].iface, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['bitmap', ]),
                                                                                          writeable_fields=set(['bitmap', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[17].config'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[17].config, address=1820, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config",
                                                rdl_desc="Configuration information associated with this forwarding table entry.",
                                                inst_name='config',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[17]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[17].config, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['enabled', ]),
                                                                                          writeable_fields=set(['enabled', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[18].macaddr'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[18].macaddr, address=1824, width=64, accesswidth=32, size=8,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr",
                                                rdl_desc="48-bit destination MAC address used as the key for this forwarding table entry.",
                                                inst_name='macaddr',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[18]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[18].macaddr, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['lo_word','hi_word', ]),
                                                                                          writeable_fields=set(['lo_word','hi_word', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[18].iface'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[18].iface, address=1832, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface",
                                                rdl_desc="Forwarding interface information associated with this forwarding table entry.",
                                                inst_name='iface',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[18]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[18].iface, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['bitmap', ]),
                                                                                          writeable_fields=set(['bitmap', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[18].config'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[18].config, address=1836, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config",
                                                rdl_desc="Configuration information associated with this forwarding table entry.",
                                                inst_name='config',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[18]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[18].config, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['enabled', ]),
                                                                                          writeable_fields=set(['enabled', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[19].macaddr'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[19].macaddr, address=1840, width=64, accesswidth=32, size=8,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr",
                                                rdl_desc="48-bit destination MAC address used as the key for this forwarding table entry.",
                                                inst_name='macaddr',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[19]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[19].macaddr, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['lo_word','hi_word', ]),
                                                                                          writeable_fields=set(['lo_word','hi_word', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[19].iface'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[19].iface, address=1848, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface",
                                                rdl_desc="Forwarding interface information associated with this forwarding table entry.",
                                                inst_name='iface',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[19]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[19].iface, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['bitmap', ]),
                                                                                          writeable_fields=set(['bitmap', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[19].config'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[19].config, address=1852, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config",
                                                rdl_desc="Configuration information associated with this forwarding table entry.",
                                                inst_name='config',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[19]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[19].config, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['enabled', ]),
                                                                                          writeable_fields=set(['enabled', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[20].macaddr'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[20].macaddr, address=1856, width=64, accesswidth=32, size=8,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr",
                                                rdl_desc="48-bit destination MAC address used as the key for this forwarding table entry.",
                                                inst_name='macaddr',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[20]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[20].macaddr, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['lo_word','hi_word', ]),
                                                                                          writeable_fields=set(['lo_word','hi_word', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[20].iface'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[20].iface, address=1864, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface",
                                                rdl_desc="Forwarding interface information associated with this forwarding table entry.",
                                                inst_name='iface',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[20]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[20].iface, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['bitmap', ]),
                                                                                          writeable_fields=set(['bitmap', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[20].config'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[20].config, address=1868, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config",
                                                rdl_desc="Configuration information associated with this forwarding table entry.",
                                                inst_name='config',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[20]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[20].config, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['enabled', ]),
                                                                                          writeable_fields=set(['enabled', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[21].macaddr'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[21].macaddr, address=1872, width=64, accesswidth=32, size=8,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr",
                                                rdl_desc="48-bit destination MAC address used as the key for this forwarding table entry.",
                                                inst_name='macaddr',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[21]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[21].macaddr, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['lo_word','hi_word', ]),
                                                                                          writeable_fields=set(['lo_word','hi_word', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[21].iface'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[21].iface, address=1880, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface",
                                                rdl_desc="Forwarding interface information associated with this forwarding table entry.",
                                                inst_name='iface',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[21]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[21].iface, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['bitmap', ]),
                                                                                          writeable_fields=set(['bitmap', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[21].config'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[21].config, address=1884, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config",
                                                rdl_desc="Configuration information associated with this forwarding table entry.",
                                                inst_name='config',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[21]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[21].config, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['enabled', ]),
                                                                                          writeable_fields=set(['enabled', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[22].macaddr'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[22].macaddr, address=1888, width=64, accesswidth=32, size=8,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr",
                                                rdl_desc="48-bit destination MAC address used as the key for this forwarding table entry.",
                                                inst_name='macaddr',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[22]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[22].macaddr, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['lo_word','hi_word', ]),
                                                                                          writeable_fields=set(['lo_word','hi_word', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[22].iface'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[22].iface, address=1896, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface",
                                                rdl_desc="Forwarding interface information associated with this forwarding table entry.",
                                                inst_name='iface',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[22]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[22].iface, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['bitmap', ]),
                                                                                          writeable_fields=set(['bitmap', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[22].config'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[22].config, address=1900, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config",
                                                rdl_desc="Configuration information associated with this forwarding table entry.",
                                                inst_name='config',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[22]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[22].config, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['enabled', ]),
                                                                                          writeable_fields=set(['enabled', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[23].macaddr'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[23].macaddr, address=1904, width=64, accesswidth=32, size=8,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr",
                                                rdl_desc="48-bit destination MAC address used as the key for this forwarding table entry.",
                                                inst_name='macaddr',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[23]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[23].macaddr, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['lo_word','hi_word', ]),
                                                                                          writeable_fields=set(['lo_word','hi_word', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[23].iface'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[23].iface, address=1912, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface",
                                                rdl_desc="Forwarding interface information associated with this forwarding table entry.",
                                                inst_name='iface',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[23]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[23].iface, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['bitmap', ]),
                                                                                          writeable_fields=set(['bitmap', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[23].config'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[23].config, address=1916, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config",
                                                rdl_desc="Configuration information associated with this forwarding table entry.",
                                                inst_name='config',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[23]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[23].config, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['enabled', ]),
                                                                                          writeable_fields=set(['enabled', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[24].macaddr'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[24].macaddr, address=1920, width=64, accesswidth=32, size=8,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr",
                                                rdl_desc="48-bit destination MAC address used as the key for this forwarding table entry.",
                                                inst_name='macaddr',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[24]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[24].macaddr, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['lo_word','hi_word', ]),
                                                                                          writeable_fields=set(['lo_word','hi_word', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[24].iface'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[24].iface, address=1928, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface",
                                                rdl_desc="Forwarding interface information associated with this forwarding table entry.",
                                                inst_name='iface',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[24]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[24].iface, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['bitmap', ]),
                                                                                          writeable_fields=set(['bitmap', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[24].config'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[24].config, address=1932, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config",
                                                rdl_desc="Configuration information associated with this forwarding table entry.",
                                                inst_name='config',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[24]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[24].config, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['enabled', ]),
                                                                                          writeable_fields=set(['enabled', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[25].macaddr'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[25].macaddr, address=1936, width=64, accesswidth=32, size=8,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr",
                                                rdl_desc="48-bit destination MAC address used as the key for this forwarding table entry.",
                                                inst_name='macaddr',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[25]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[25].macaddr, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['lo_word','hi_word', ]),
                                                                                          writeable_fields=set(['lo_word','hi_word', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[25].iface'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[25].iface, address=1944, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface",
                                                rdl_desc="Forwarding interface information associated with this forwarding table entry.",
                                                inst_name='iface',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[25]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[25].iface, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['bitmap', ]),
                                                                                          writeable_fields=set(['bitmap', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[25].config'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[25].config, address=1948, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config",
                                                rdl_desc="Configuration information associated with this forwarding table entry.",
                                                inst_name='config',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[25]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[25].config, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['enabled', ]),
                                                                                          writeable_fields=set(['enabled', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[26].macaddr'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[26].macaddr, address=1952, width=64, accesswidth=32, size=8,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr",
                                                rdl_desc="48-bit destination MAC address used as the key for this forwarding table entry.",
                                                inst_name='macaddr',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[26]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[26].macaddr, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['lo_word','hi_word', ]),
                                                                                          writeable_fields=set(['lo_word','hi_word', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[26].iface'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[26].iface, address=1960, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface",
                                                rdl_desc="Forwarding interface information associated with this forwarding table entry.",
                                                inst_name='iface',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[26]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[26].iface, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['bitmap', ]),
                                                                                          writeable_fields=set(['bitmap', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[26].config'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[26].config, address=1964, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config",
                                                rdl_desc="Configuration information associated with this forwarding table entry.",
                                                inst_name='config',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[26]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[26].config, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['enabled', ]),
                                                                                          writeable_fields=set(['enabled', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[27].macaddr'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[27].macaddr, address=1968, width=64, accesswidth=32, size=8,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr",
                                                rdl_desc="48-bit destination MAC address used as the key for this forwarding table entry.",
                                                inst_name='macaddr',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[27]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[27].macaddr, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['lo_word','hi_word', ]),
                                                                                          writeable_fields=set(['lo_word','hi_word', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[27].iface'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[27].iface, address=1976, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface",
                                                rdl_desc="Forwarding interface information associated with this forwarding table entry.",
                                                inst_name='iface',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[27]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[27].iface, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['bitmap', ]),
                                                                                          writeable_fields=set(['bitmap', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[27].config'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[27].config, address=1980, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config",
                                                rdl_desc="Configuration information associated with this forwarding table entry.",
                                                inst_name='config',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[27]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[27].config, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['enabled', ]),
                                                                                          writeable_fields=set(['enabled', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[28].macaddr'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[28].macaddr, address=1984, width=64, accesswidth=32, size=8,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr",
                                                rdl_desc="48-bit destination MAC address used as the key for this forwarding table entry.",
                                                inst_name='macaddr',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[28]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[28].macaddr, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['lo_word','hi_word', ]),
                                                                                          writeable_fields=set(['lo_word','hi_word', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[28].iface'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[28].iface, address=1992, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface",
                                                rdl_desc="Forwarding interface information associated with this forwarding table entry.",
                                                inst_name='iface',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[28]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[28].iface, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['bitmap', ]),
                                                                                          writeable_fields=set(['bitmap', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[28].config'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[28].config, address=1996, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config",
                                                rdl_desc="Configuration information associated with this forwarding table entry.",
                                                inst_name='config',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[28]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[28].config, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['enabled', ]),
                                                                                          writeable_fields=set(['enabled', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[29].macaddr'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[29].macaddr, address=2000, width=64, accesswidth=32, size=8,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr",
                                                rdl_desc="48-bit destination MAC address used as the key for this forwarding table entry.",
                                                inst_name='macaddr',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[29]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[29].macaddr, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['lo_word','hi_word', ]),
                                                                                          writeable_fields=set(['lo_word','hi_word', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[29].iface'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[29].iface, address=2008, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface",
                                                rdl_desc="Forwarding interface information associated with this forwarding table entry.",
                                                inst_name='iface',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[29]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[29].iface, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['bitmap', ]),
                                                                                          writeable_fields=set(['bitmap', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[29].config'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[29].config, address=2012, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config",
                                                rdl_desc="Configuration information associated with this forwarding table entry.",
                                                inst_name='config',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[29]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[29].config, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['enabled', ]),
                                                                                          writeable_fields=set(['enabled', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[30].macaddr'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[30].macaddr, address=2016, width=64, accesswidth=32, size=8,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr",
                                                rdl_desc="48-bit destination MAC address used as the key for this forwarding table entry.",
                                                inst_name='macaddr',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[30]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[30].macaddr, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['lo_word','hi_word', ]),
                                                                                          writeable_fields=set(['lo_word','hi_word', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[30].iface'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[30].iface, address=2024, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface",
                                                rdl_desc="Forwarding interface information associated with this forwarding table entry.",
                                                inst_name='iface',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[30]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[30].iface, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['bitmap', ]),
                                                                                          writeable_fields=set(['bitmap', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[30].config'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[30].config, address=2028, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config",
                                                rdl_desc="Configuration information associated with this forwarding table entry.",
                                                inst_name='config',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[30]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[30].config, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['enabled', ]),
                                                                                          writeable_fields=set(['enabled', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[31].macaddr'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[31].macaddr, address=2032, width=64, accesswidth=32, size=8,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr",
                                                rdl_desc="48-bit destination MAC address used as the key for this forwarding table entry.",
                                                inst_name='macaddr',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[31]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[31].macaddr, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['lo_word','hi_word', ]),
                                                                                          writeable_fields=set(['lo_word','hi_word', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[31].iface'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[31].iface, address=2040, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface",
                                                rdl_desc="Forwarding interface information associated with this forwarding table entry.",
                                                inst_name='iface',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[31]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[31].iface, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['bitmap', ]),
                                                                                          writeable_fields=set(['bitmap', ]) )
        with self.subTest(msg='register: openenoc_csr.switch2.forwarding_table.entry[31].config'):
            self._single_register_property_test(rut=self.dut.switch2.forwarding_table.entry[31].config, address=2044, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config",
                                                rdl_desc="Configuration information associated with this forwarding table entry.",
                                                inst_name='config',
                                                parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[31]')
            self._single_register_read_and_write_test(rut=self.dut.switch2.forwarding_table.entry[31].config, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['enabled', ]),
                                                                                          writeable_fields=set(['enabled', ]) )
        

    def test_field(self) -> None:
        """
        Check the properties and function (read and write) on the fields both integer and enum
        """
        
        with self.subTest(msg='field: openenoc_csr.switch2.info.table_depth'):
            self._single_field_property_test(fut=self.dut.switch2.info.table_depth, lsb=0, msb=15, low=0, high=15, is_volatile=False, default=32,
                                             rdl_name="csr.switch2.info.table_depth[15:0]",
                                             rdl_desc="Depth of the forwarding table in this openENOC Switch instance. This field reflects the TABLE_DEPTH parameter value.",
                                             inst_name='table_depth',
                                             parent_full_inst_name='openenoc_csr.switch2.info')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.info.table_depth, is_sw_readable=True, is_sw_writable=False)
        with self.subTest(msg='field: openenoc_csr.switch2.info.num_of_interfaces'):
            self._single_field_property_test(fut=self.dut.switch2.info.num_of_interfaces, lsb=16, msb=21, low=16, high=21, is_volatile=False, default=8,
                                             rdl_name="csr.switch2.info.num_of_interfaces[21:16]",
                                             rdl_desc="Number of interfaces in this openENOC Switch instance. This field reflects the NUM_OF_INTERFACES parameter value.",
                                             inst_name='num_of_interfaces',
                                             parent_full_inst_name='openenoc_csr.switch2.info')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.info.num_of_interfaces, is_sw_readable=True, is_sw_writable=False)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_control.operation_mode'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_control.operation_mode, lsb=0, msb=0, low=0, high=0, is_volatile=False, default=0,
                                             rdl_name="csr.switch2.forwarding_control.operation_mode[0:0]",
                                             rdl_desc="Mode of operation for the openENOC Switch instance. When set to 1, the switch operates in managed mode, allowing software to configure the forwarding table and control forwarding operations. When set to 0, the switch operates in unmanaged mode, where forwarding state is maintained autonomously by internal hardware logic without software intervention.",
                                             inst_name='operation_mode',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_control')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_control.operation_mode, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_control.pause_request'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_control.pause_request, lsb=7, msb=7, low=7, high=7, is_volatile=False, default=0,
                                             rdl_name="csr.switch2.forwarding_control.pause_request[7:7]",
                                             rdl_desc="Pause request for the forwarding logic. When set, this field requests the switch to pause frame forwarding and clear its internal pipeline before forwarding table updates are performed.",
                                             inst_name='pause_request',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_control')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_control.pause_request, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_control.pause_done'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_control.pause_done, lsb=15, msb=15, low=15, high=15, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_control.pause_done[15:15]",
                                             rdl_desc="Pause done status. When set, this field indicates that the switch has paused frame forwarding and reached a safe state for forwarding table modification.",
                                             inst_name='pause_done',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_control')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_control.pause_done, is_sw_readable=True, is_sw_writable=False)
        with self.subTest(msg='field: openenoc_csr.switch2.default_forwarding.bitmap'):
            self._single_field_property_test(fut=self.dut.switch2.default_forwarding.bitmap, lsb=0, msb=7, low=0, high=7, is_volatile=False, default=0,
                                             rdl_name="csr.switch2.default_forwarding.bitmap[NUM_OF_INTERFACES-1:0]",
                                             rdl_desc="Bitmap selecting the output interface or interfaces to which frames that do not match any enabled forwarding table entry are forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.",
                                             inst_name='bitmap',
                                             parent_full_inst_name='openenoc_csr.switch2.default_forwarding')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.default_forwarding.bitmap, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[0].macaddr.lo_word'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[0].macaddr.lo_word, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]",
                                             rdl_desc="Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='lo_word',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[0].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[0].macaddr.lo_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[0].macaddr.hi_word'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[0].macaddr.hi_word, lsb=32, msb=47, low=32, high=47, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]",
                                             rdl_desc="Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='hi_word',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[0].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[0].macaddr.hi_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[0].iface.bitmap'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[0].iface.bitmap, lsb=0, msb=7, low=0, high=7, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]",
                                             rdl_desc="Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.",
                                             inst_name='bitmap',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[0].iface')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[0].iface.bitmap, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[0].config.enabled'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[0].config.enabled, lsb=0, msb=0, low=0, high=0, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled",
                                             rdl_desc="Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.",
                                             inst_name='enabled',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[0].config')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[0].config.enabled, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[1].macaddr.lo_word'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[1].macaddr.lo_word, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]",
                                             rdl_desc="Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='lo_word',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[1].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[1].macaddr.lo_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[1].macaddr.hi_word'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[1].macaddr.hi_word, lsb=32, msb=47, low=32, high=47, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]",
                                             rdl_desc="Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='hi_word',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[1].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[1].macaddr.hi_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[1].iface.bitmap'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[1].iface.bitmap, lsb=0, msb=7, low=0, high=7, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]",
                                             rdl_desc="Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.",
                                             inst_name='bitmap',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[1].iface')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[1].iface.bitmap, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[1].config.enabled'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[1].config.enabled, lsb=0, msb=0, low=0, high=0, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled",
                                             rdl_desc="Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.",
                                             inst_name='enabled',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[1].config')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[1].config.enabled, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[2].macaddr.lo_word'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[2].macaddr.lo_word, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]",
                                             rdl_desc="Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='lo_word',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[2].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[2].macaddr.lo_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[2].macaddr.hi_word'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[2].macaddr.hi_word, lsb=32, msb=47, low=32, high=47, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]",
                                             rdl_desc="Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='hi_word',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[2].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[2].macaddr.hi_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[2].iface.bitmap'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[2].iface.bitmap, lsb=0, msb=7, low=0, high=7, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]",
                                             rdl_desc="Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.",
                                             inst_name='bitmap',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[2].iface')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[2].iface.bitmap, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[2].config.enabled'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[2].config.enabled, lsb=0, msb=0, low=0, high=0, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled",
                                             rdl_desc="Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.",
                                             inst_name='enabled',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[2].config')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[2].config.enabled, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[3].macaddr.lo_word'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[3].macaddr.lo_word, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]",
                                             rdl_desc="Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='lo_word',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[3].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[3].macaddr.lo_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[3].macaddr.hi_word'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[3].macaddr.hi_word, lsb=32, msb=47, low=32, high=47, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]",
                                             rdl_desc="Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='hi_word',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[3].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[3].macaddr.hi_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[3].iface.bitmap'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[3].iface.bitmap, lsb=0, msb=7, low=0, high=7, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]",
                                             rdl_desc="Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.",
                                             inst_name='bitmap',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[3].iface')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[3].iface.bitmap, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[3].config.enabled'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[3].config.enabled, lsb=0, msb=0, low=0, high=0, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled",
                                             rdl_desc="Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.",
                                             inst_name='enabled',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[3].config')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[3].config.enabled, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[4].macaddr.lo_word'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[4].macaddr.lo_word, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]",
                                             rdl_desc="Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='lo_word',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[4].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[4].macaddr.lo_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[4].macaddr.hi_word'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[4].macaddr.hi_word, lsb=32, msb=47, low=32, high=47, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]",
                                             rdl_desc="Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='hi_word',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[4].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[4].macaddr.hi_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[4].iface.bitmap'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[4].iface.bitmap, lsb=0, msb=7, low=0, high=7, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]",
                                             rdl_desc="Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.",
                                             inst_name='bitmap',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[4].iface')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[4].iface.bitmap, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[4].config.enabled'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[4].config.enabled, lsb=0, msb=0, low=0, high=0, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled",
                                             rdl_desc="Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.",
                                             inst_name='enabled',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[4].config')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[4].config.enabled, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[5].macaddr.lo_word'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[5].macaddr.lo_word, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]",
                                             rdl_desc="Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='lo_word',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[5].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[5].macaddr.lo_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[5].macaddr.hi_word'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[5].macaddr.hi_word, lsb=32, msb=47, low=32, high=47, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]",
                                             rdl_desc="Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='hi_word',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[5].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[5].macaddr.hi_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[5].iface.bitmap'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[5].iface.bitmap, lsb=0, msb=7, low=0, high=7, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]",
                                             rdl_desc="Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.",
                                             inst_name='bitmap',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[5].iface')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[5].iface.bitmap, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[5].config.enabled'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[5].config.enabled, lsb=0, msb=0, low=0, high=0, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled",
                                             rdl_desc="Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.",
                                             inst_name='enabled',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[5].config')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[5].config.enabled, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[6].macaddr.lo_word'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[6].macaddr.lo_word, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]",
                                             rdl_desc="Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='lo_word',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[6].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[6].macaddr.lo_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[6].macaddr.hi_word'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[6].macaddr.hi_word, lsb=32, msb=47, low=32, high=47, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]",
                                             rdl_desc="Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='hi_word',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[6].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[6].macaddr.hi_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[6].iface.bitmap'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[6].iface.bitmap, lsb=0, msb=7, low=0, high=7, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]",
                                             rdl_desc="Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.",
                                             inst_name='bitmap',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[6].iface')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[6].iface.bitmap, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[6].config.enabled'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[6].config.enabled, lsb=0, msb=0, low=0, high=0, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled",
                                             rdl_desc="Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.",
                                             inst_name='enabled',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[6].config')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[6].config.enabled, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[7].macaddr.lo_word'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[7].macaddr.lo_word, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]",
                                             rdl_desc="Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='lo_word',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[7].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[7].macaddr.lo_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[7].macaddr.hi_word'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[7].macaddr.hi_word, lsb=32, msb=47, low=32, high=47, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]",
                                             rdl_desc="Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='hi_word',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[7].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[7].macaddr.hi_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[7].iface.bitmap'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[7].iface.bitmap, lsb=0, msb=7, low=0, high=7, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]",
                                             rdl_desc="Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.",
                                             inst_name='bitmap',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[7].iface')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[7].iface.bitmap, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[7].config.enabled'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[7].config.enabled, lsb=0, msb=0, low=0, high=0, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled",
                                             rdl_desc="Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.",
                                             inst_name='enabled',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[7].config')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[7].config.enabled, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[8].macaddr.lo_word'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[8].macaddr.lo_word, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]",
                                             rdl_desc="Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='lo_word',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[8].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[8].macaddr.lo_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[8].macaddr.hi_word'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[8].macaddr.hi_word, lsb=32, msb=47, low=32, high=47, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]",
                                             rdl_desc="Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='hi_word',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[8].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[8].macaddr.hi_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[8].iface.bitmap'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[8].iface.bitmap, lsb=0, msb=7, low=0, high=7, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]",
                                             rdl_desc="Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.",
                                             inst_name='bitmap',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[8].iface')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[8].iface.bitmap, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[8].config.enabled'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[8].config.enabled, lsb=0, msb=0, low=0, high=0, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled",
                                             rdl_desc="Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.",
                                             inst_name='enabled',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[8].config')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[8].config.enabled, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[9].macaddr.lo_word'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[9].macaddr.lo_word, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]",
                                             rdl_desc="Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='lo_word',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[9].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[9].macaddr.lo_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[9].macaddr.hi_word'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[9].macaddr.hi_word, lsb=32, msb=47, low=32, high=47, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]",
                                             rdl_desc="Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='hi_word',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[9].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[9].macaddr.hi_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[9].iface.bitmap'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[9].iface.bitmap, lsb=0, msb=7, low=0, high=7, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]",
                                             rdl_desc="Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.",
                                             inst_name='bitmap',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[9].iface')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[9].iface.bitmap, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[9].config.enabled'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[9].config.enabled, lsb=0, msb=0, low=0, high=0, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled",
                                             rdl_desc="Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.",
                                             inst_name='enabled',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[9].config')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[9].config.enabled, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[10].macaddr.lo_word'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[10].macaddr.lo_word, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]",
                                             rdl_desc="Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='lo_word',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[10].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[10].macaddr.lo_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[10].macaddr.hi_word'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[10].macaddr.hi_word, lsb=32, msb=47, low=32, high=47, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]",
                                             rdl_desc="Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='hi_word',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[10].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[10].macaddr.hi_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[10].iface.bitmap'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[10].iface.bitmap, lsb=0, msb=7, low=0, high=7, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]",
                                             rdl_desc="Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.",
                                             inst_name='bitmap',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[10].iface')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[10].iface.bitmap, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[10].config.enabled'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[10].config.enabled, lsb=0, msb=0, low=0, high=0, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled",
                                             rdl_desc="Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.",
                                             inst_name='enabled',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[10].config')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[10].config.enabled, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[11].macaddr.lo_word'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[11].macaddr.lo_word, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]",
                                             rdl_desc="Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='lo_word',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[11].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[11].macaddr.lo_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[11].macaddr.hi_word'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[11].macaddr.hi_word, lsb=32, msb=47, low=32, high=47, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]",
                                             rdl_desc="Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='hi_word',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[11].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[11].macaddr.hi_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[11].iface.bitmap'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[11].iface.bitmap, lsb=0, msb=7, low=0, high=7, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]",
                                             rdl_desc="Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.",
                                             inst_name='bitmap',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[11].iface')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[11].iface.bitmap, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[11].config.enabled'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[11].config.enabled, lsb=0, msb=0, low=0, high=0, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled",
                                             rdl_desc="Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.",
                                             inst_name='enabled',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[11].config')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[11].config.enabled, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[12].macaddr.lo_word'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[12].macaddr.lo_word, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]",
                                             rdl_desc="Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='lo_word',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[12].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[12].macaddr.lo_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[12].macaddr.hi_word'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[12].macaddr.hi_word, lsb=32, msb=47, low=32, high=47, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]",
                                             rdl_desc="Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='hi_word',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[12].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[12].macaddr.hi_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[12].iface.bitmap'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[12].iface.bitmap, lsb=0, msb=7, low=0, high=7, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]",
                                             rdl_desc="Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.",
                                             inst_name='bitmap',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[12].iface')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[12].iface.bitmap, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[12].config.enabled'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[12].config.enabled, lsb=0, msb=0, low=0, high=0, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled",
                                             rdl_desc="Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.",
                                             inst_name='enabled',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[12].config')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[12].config.enabled, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[13].macaddr.lo_word'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[13].macaddr.lo_word, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]",
                                             rdl_desc="Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='lo_word',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[13].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[13].macaddr.lo_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[13].macaddr.hi_word'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[13].macaddr.hi_word, lsb=32, msb=47, low=32, high=47, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]",
                                             rdl_desc="Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='hi_word',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[13].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[13].macaddr.hi_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[13].iface.bitmap'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[13].iface.bitmap, lsb=0, msb=7, low=0, high=7, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]",
                                             rdl_desc="Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.",
                                             inst_name='bitmap',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[13].iface')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[13].iface.bitmap, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[13].config.enabled'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[13].config.enabled, lsb=0, msb=0, low=0, high=0, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled",
                                             rdl_desc="Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.",
                                             inst_name='enabled',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[13].config')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[13].config.enabled, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[14].macaddr.lo_word'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[14].macaddr.lo_word, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]",
                                             rdl_desc="Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='lo_word',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[14].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[14].macaddr.lo_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[14].macaddr.hi_word'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[14].macaddr.hi_word, lsb=32, msb=47, low=32, high=47, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]",
                                             rdl_desc="Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='hi_word',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[14].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[14].macaddr.hi_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[14].iface.bitmap'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[14].iface.bitmap, lsb=0, msb=7, low=0, high=7, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]",
                                             rdl_desc="Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.",
                                             inst_name='bitmap',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[14].iface')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[14].iface.bitmap, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[14].config.enabled'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[14].config.enabled, lsb=0, msb=0, low=0, high=0, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled",
                                             rdl_desc="Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.",
                                             inst_name='enabled',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[14].config')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[14].config.enabled, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[15].macaddr.lo_word'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[15].macaddr.lo_word, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]",
                                             rdl_desc="Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='lo_word',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[15].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[15].macaddr.lo_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[15].macaddr.hi_word'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[15].macaddr.hi_word, lsb=32, msb=47, low=32, high=47, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]",
                                             rdl_desc="Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='hi_word',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[15].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[15].macaddr.hi_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[15].iface.bitmap'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[15].iface.bitmap, lsb=0, msb=7, low=0, high=7, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]",
                                             rdl_desc="Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.",
                                             inst_name='bitmap',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[15].iface')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[15].iface.bitmap, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[15].config.enabled'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[15].config.enabled, lsb=0, msb=0, low=0, high=0, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled",
                                             rdl_desc="Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.",
                                             inst_name='enabled',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[15].config')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[15].config.enabled, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[16].macaddr.lo_word'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[16].macaddr.lo_word, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]",
                                             rdl_desc="Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='lo_word',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[16].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[16].macaddr.lo_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[16].macaddr.hi_word'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[16].macaddr.hi_word, lsb=32, msb=47, low=32, high=47, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]",
                                             rdl_desc="Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='hi_word',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[16].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[16].macaddr.hi_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[16].iface.bitmap'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[16].iface.bitmap, lsb=0, msb=7, low=0, high=7, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]",
                                             rdl_desc="Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.",
                                             inst_name='bitmap',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[16].iface')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[16].iface.bitmap, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[16].config.enabled'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[16].config.enabled, lsb=0, msb=0, low=0, high=0, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled",
                                             rdl_desc="Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.",
                                             inst_name='enabled',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[16].config')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[16].config.enabled, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[17].macaddr.lo_word'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[17].macaddr.lo_word, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]",
                                             rdl_desc="Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='lo_word',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[17].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[17].macaddr.lo_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[17].macaddr.hi_word'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[17].macaddr.hi_word, lsb=32, msb=47, low=32, high=47, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]",
                                             rdl_desc="Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='hi_word',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[17].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[17].macaddr.hi_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[17].iface.bitmap'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[17].iface.bitmap, lsb=0, msb=7, low=0, high=7, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]",
                                             rdl_desc="Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.",
                                             inst_name='bitmap',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[17].iface')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[17].iface.bitmap, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[17].config.enabled'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[17].config.enabled, lsb=0, msb=0, low=0, high=0, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled",
                                             rdl_desc="Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.",
                                             inst_name='enabled',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[17].config')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[17].config.enabled, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[18].macaddr.lo_word'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[18].macaddr.lo_word, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]",
                                             rdl_desc="Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='lo_word',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[18].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[18].macaddr.lo_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[18].macaddr.hi_word'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[18].macaddr.hi_word, lsb=32, msb=47, low=32, high=47, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]",
                                             rdl_desc="Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='hi_word',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[18].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[18].macaddr.hi_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[18].iface.bitmap'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[18].iface.bitmap, lsb=0, msb=7, low=0, high=7, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]",
                                             rdl_desc="Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.",
                                             inst_name='bitmap',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[18].iface')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[18].iface.bitmap, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[18].config.enabled'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[18].config.enabled, lsb=0, msb=0, low=0, high=0, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled",
                                             rdl_desc="Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.",
                                             inst_name='enabled',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[18].config')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[18].config.enabled, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[19].macaddr.lo_word'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[19].macaddr.lo_word, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]",
                                             rdl_desc="Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='lo_word',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[19].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[19].macaddr.lo_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[19].macaddr.hi_word'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[19].macaddr.hi_word, lsb=32, msb=47, low=32, high=47, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]",
                                             rdl_desc="Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='hi_word',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[19].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[19].macaddr.hi_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[19].iface.bitmap'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[19].iface.bitmap, lsb=0, msb=7, low=0, high=7, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]",
                                             rdl_desc="Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.",
                                             inst_name='bitmap',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[19].iface')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[19].iface.bitmap, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[19].config.enabled'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[19].config.enabled, lsb=0, msb=0, low=0, high=0, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled",
                                             rdl_desc="Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.",
                                             inst_name='enabled',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[19].config')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[19].config.enabled, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[20].macaddr.lo_word'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[20].macaddr.lo_word, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]",
                                             rdl_desc="Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='lo_word',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[20].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[20].macaddr.lo_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[20].macaddr.hi_word'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[20].macaddr.hi_word, lsb=32, msb=47, low=32, high=47, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]",
                                             rdl_desc="Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='hi_word',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[20].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[20].macaddr.hi_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[20].iface.bitmap'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[20].iface.bitmap, lsb=0, msb=7, low=0, high=7, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]",
                                             rdl_desc="Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.",
                                             inst_name='bitmap',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[20].iface')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[20].iface.bitmap, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[20].config.enabled'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[20].config.enabled, lsb=0, msb=0, low=0, high=0, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled",
                                             rdl_desc="Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.",
                                             inst_name='enabled',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[20].config')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[20].config.enabled, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[21].macaddr.lo_word'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[21].macaddr.lo_word, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]",
                                             rdl_desc="Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='lo_word',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[21].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[21].macaddr.lo_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[21].macaddr.hi_word'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[21].macaddr.hi_word, lsb=32, msb=47, low=32, high=47, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]",
                                             rdl_desc="Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='hi_word',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[21].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[21].macaddr.hi_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[21].iface.bitmap'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[21].iface.bitmap, lsb=0, msb=7, low=0, high=7, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]",
                                             rdl_desc="Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.",
                                             inst_name='bitmap',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[21].iface')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[21].iface.bitmap, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[21].config.enabled'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[21].config.enabled, lsb=0, msb=0, low=0, high=0, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled",
                                             rdl_desc="Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.",
                                             inst_name='enabled',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[21].config')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[21].config.enabled, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[22].macaddr.lo_word'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[22].macaddr.lo_word, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]",
                                             rdl_desc="Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='lo_word',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[22].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[22].macaddr.lo_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[22].macaddr.hi_word'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[22].macaddr.hi_word, lsb=32, msb=47, low=32, high=47, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]",
                                             rdl_desc="Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='hi_word',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[22].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[22].macaddr.hi_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[22].iface.bitmap'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[22].iface.bitmap, lsb=0, msb=7, low=0, high=7, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]",
                                             rdl_desc="Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.",
                                             inst_name='bitmap',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[22].iface')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[22].iface.bitmap, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[22].config.enabled'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[22].config.enabled, lsb=0, msb=0, low=0, high=0, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled",
                                             rdl_desc="Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.",
                                             inst_name='enabled',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[22].config')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[22].config.enabled, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[23].macaddr.lo_word'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[23].macaddr.lo_word, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]",
                                             rdl_desc="Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='lo_word',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[23].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[23].macaddr.lo_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[23].macaddr.hi_word'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[23].macaddr.hi_word, lsb=32, msb=47, low=32, high=47, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]",
                                             rdl_desc="Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='hi_word',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[23].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[23].macaddr.hi_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[23].iface.bitmap'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[23].iface.bitmap, lsb=0, msb=7, low=0, high=7, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]",
                                             rdl_desc="Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.",
                                             inst_name='bitmap',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[23].iface')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[23].iface.bitmap, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[23].config.enabled'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[23].config.enabled, lsb=0, msb=0, low=0, high=0, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled",
                                             rdl_desc="Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.",
                                             inst_name='enabled',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[23].config')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[23].config.enabled, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[24].macaddr.lo_word'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[24].macaddr.lo_word, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]",
                                             rdl_desc="Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='lo_word',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[24].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[24].macaddr.lo_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[24].macaddr.hi_word'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[24].macaddr.hi_word, lsb=32, msb=47, low=32, high=47, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]",
                                             rdl_desc="Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='hi_word',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[24].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[24].macaddr.hi_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[24].iface.bitmap'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[24].iface.bitmap, lsb=0, msb=7, low=0, high=7, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]",
                                             rdl_desc="Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.",
                                             inst_name='bitmap',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[24].iface')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[24].iface.bitmap, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[24].config.enabled'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[24].config.enabled, lsb=0, msb=0, low=0, high=0, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled",
                                             rdl_desc="Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.",
                                             inst_name='enabled',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[24].config')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[24].config.enabled, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[25].macaddr.lo_word'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[25].macaddr.lo_word, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]",
                                             rdl_desc="Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='lo_word',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[25].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[25].macaddr.lo_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[25].macaddr.hi_word'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[25].macaddr.hi_word, lsb=32, msb=47, low=32, high=47, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]",
                                             rdl_desc="Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='hi_word',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[25].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[25].macaddr.hi_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[25].iface.bitmap'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[25].iface.bitmap, lsb=0, msb=7, low=0, high=7, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]",
                                             rdl_desc="Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.",
                                             inst_name='bitmap',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[25].iface')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[25].iface.bitmap, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[25].config.enabled'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[25].config.enabled, lsb=0, msb=0, low=0, high=0, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled",
                                             rdl_desc="Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.",
                                             inst_name='enabled',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[25].config')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[25].config.enabled, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[26].macaddr.lo_word'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[26].macaddr.lo_word, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]",
                                             rdl_desc="Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='lo_word',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[26].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[26].macaddr.lo_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[26].macaddr.hi_word'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[26].macaddr.hi_word, lsb=32, msb=47, low=32, high=47, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]",
                                             rdl_desc="Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='hi_word',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[26].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[26].macaddr.hi_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[26].iface.bitmap'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[26].iface.bitmap, lsb=0, msb=7, low=0, high=7, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]",
                                             rdl_desc="Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.",
                                             inst_name='bitmap',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[26].iface')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[26].iface.bitmap, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[26].config.enabled'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[26].config.enabled, lsb=0, msb=0, low=0, high=0, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled",
                                             rdl_desc="Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.",
                                             inst_name='enabled',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[26].config')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[26].config.enabled, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[27].macaddr.lo_word'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[27].macaddr.lo_word, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]",
                                             rdl_desc="Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='lo_word',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[27].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[27].macaddr.lo_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[27].macaddr.hi_word'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[27].macaddr.hi_word, lsb=32, msb=47, low=32, high=47, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]",
                                             rdl_desc="Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='hi_word',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[27].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[27].macaddr.hi_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[27].iface.bitmap'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[27].iface.bitmap, lsb=0, msb=7, low=0, high=7, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]",
                                             rdl_desc="Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.",
                                             inst_name='bitmap',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[27].iface')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[27].iface.bitmap, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[27].config.enabled'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[27].config.enabled, lsb=0, msb=0, low=0, high=0, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled",
                                             rdl_desc="Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.",
                                             inst_name='enabled',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[27].config')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[27].config.enabled, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[28].macaddr.lo_word'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[28].macaddr.lo_word, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]",
                                             rdl_desc="Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='lo_word',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[28].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[28].macaddr.lo_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[28].macaddr.hi_word'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[28].macaddr.hi_word, lsb=32, msb=47, low=32, high=47, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]",
                                             rdl_desc="Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='hi_word',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[28].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[28].macaddr.hi_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[28].iface.bitmap'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[28].iface.bitmap, lsb=0, msb=7, low=0, high=7, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]",
                                             rdl_desc="Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.",
                                             inst_name='bitmap',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[28].iface')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[28].iface.bitmap, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[28].config.enabled'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[28].config.enabled, lsb=0, msb=0, low=0, high=0, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled",
                                             rdl_desc="Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.",
                                             inst_name='enabled',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[28].config')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[28].config.enabled, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[29].macaddr.lo_word'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[29].macaddr.lo_word, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]",
                                             rdl_desc="Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='lo_word',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[29].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[29].macaddr.lo_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[29].macaddr.hi_word'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[29].macaddr.hi_word, lsb=32, msb=47, low=32, high=47, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]",
                                             rdl_desc="Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='hi_word',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[29].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[29].macaddr.hi_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[29].iface.bitmap'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[29].iface.bitmap, lsb=0, msb=7, low=0, high=7, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]",
                                             rdl_desc="Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.",
                                             inst_name='bitmap',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[29].iface')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[29].iface.bitmap, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[29].config.enabled'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[29].config.enabled, lsb=0, msb=0, low=0, high=0, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled",
                                             rdl_desc="Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.",
                                             inst_name='enabled',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[29].config')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[29].config.enabled, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[30].macaddr.lo_word'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[30].macaddr.lo_word, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]",
                                             rdl_desc="Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='lo_word',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[30].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[30].macaddr.lo_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[30].macaddr.hi_word'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[30].macaddr.hi_word, lsb=32, msb=47, low=32, high=47, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]",
                                             rdl_desc="Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='hi_word',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[30].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[30].macaddr.hi_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[30].iface.bitmap'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[30].iface.bitmap, lsb=0, msb=7, low=0, high=7, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]",
                                             rdl_desc="Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.",
                                             inst_name='bitmap',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[30].iface')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[30].iface.bitmap, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[30].config.enabled'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[30].config.enabled, lsb=0, msb=0, low=0, high=0, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled",
                                             rdl_desc="Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.",
                                             inst_name='enabled',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[30].config')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[30].config.enabled, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[31].macaddr.lo_word'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[31].macaddr.lo_word, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]",
                                             rdl_desc="Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='lo_word',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[31].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[31].macaddr.lo_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[31].macaddr.hi_word'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[31].macaddr.hi_word, lsb=32, msb=47, low=32, high=47, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]",
                                             rdl_desc="Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='hi_word',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[31].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[31].macaddr.hi_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[31].iface.bitmap'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[31].iface.bitmap, lsb=0, msb=7, low=0, high=7, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]",
                                             rdl_desc="Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.",
                                             inst_name='bitmap',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[31].iface')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[31].iface.bitmap, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch2.forwarding_table.entry[31].config.enabled'):
            self._single_field_property_test(fut=self.dut.switch2.forwarding_table.entry[31].config.enabled, lsb=0, msb=0, low=0, high=0, is_volatile=True, default=None,
                                             rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled",
                                             rdl_desc="Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.",
                                             inst_name='enabled',
                                             parent_full_inst_name='openenoc_csr.switch2.forwarding_table.entry[31].config')
            self._single_int_field_read_and_write_test(fut=self.dut.switch2.forwarding_table.entry[31].config.enabled, is_sw_readable=True, is_sw_writable=True)

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
        with self.subTest(msg='regfile: openenoc_csr.switch2.forwarding_table'):
            self._single_regfile_property_test(dut=self.dut.switch2.forwarding_table,
                                               size=512,
                                               rdl_name="csr.switch2.forwarding_table",
                                               rdl_desc="Forwarding table used to map MAC addresses to output interface selections for frame forwarding.",
                                               inst_name='forwarding_table',
                                               parent_full_inst_name='openenoc_csr.switch2')
            self._test_regfile_iterators(dut=self.dut.switch2.forwarding_table,
                                         writeable_registers=NodeIterators(),
                                         readable_registers=NodeIterators(),
                                         sections=NodeIterators(('entry', [32]),))
        with self.subTest(msg='regfile: openenoc_csr.switch2.forwarding_table.entry[0]'):
            self._single_regfile_property_test(dut=self.dut.switch2.forwarding_table.entry[0],
                                               size=16,
                                               rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]",
                                               rdl_desc="Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.",
                                               inst_name='entry[0]',
                                               parent_full_inst_name='openenoc_csr.switch2.forwarding_table')
            self._test_regfile_iterators(dut=self.dut.switch2.forwarding_table.entry[0],
                                         writeable_registers=NodeIterators('macaddr','iface','config',),
                                         readable_registers=NodeIterators('macaddr','iface','config',),
                                         sections=NodeIterators())
        with self.subTest(msg='regfile: openenoc_csr.switch2.forwarding_table.entry[1]'):
            self._single_regfile_property_test(dut=self.dut.switch2.forwarding_table.entry[1],
                                               size=16,
                                               rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]",
                                               rdl_desc="Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.",
                                               inst_name='entry[1]',
                                               parent_full_inst_name='openenoc_csr.switch2.forwarding_table')
            self._test_regfile_iterators(dut=self.dut.switch2.forwarding_table.entry[1],
                                         writeable_registers=NodeIterators('macaddr','iface','config',),
                                         readable_registers=NodeIterators('macaddr','iface','config',),
                                         sections=NodeIterators())
        with self.subTest(msg='regfile: openenoc_csr.switch2.forwarding_table.entry[2]'):
            self._single_regfile_property_test(dut=self.dut.switch2.forwarding_table.entry[2],
                                               size=16,
                                               rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]",
                                               rdl_desc="Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.",
                                               inst_name='entry[2]',
                                               parent_full_inst_name='openenoc_csr.switch2.forwarding_table')
            self._test_regfile_iterators(dut=self.dut.switch2.forwarding_table.entry[2],
                                         writeable_registers=NodeIterators('macaddr','iface','config',),
                                         readable_registers=NodeIterators('macaddr','iface','config',),
                                         sections=NodeIterators())
        with self.subTest(msg='regfile: openenoc_csr.switch2.forwarding_table.entry[3]'):
            self._single_regfile_property_test(dut=self.dut.switch2.forwarding_table.entry[3],
                                               size=16,
                                               rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]",
                                               rdl_desc="Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.",
                                               inst_name='entry[3]',
                                               parent_full_inst_name='openenoc_csr.switch2.forwarding_table')
            self._test_regfile_iterators(dut=self.dut.switch2.forwarding_table.entry[3],
                                         writeable_registers=NodeIterators('macaddr','iface','config',),
                                         readable_registers=NodeIterators('macaddr','iface','config',),
                                         sections=NodeIterators())
        with self.subTest(msg='regfile: openenoc_csr.switch2.forwarding_table.entry[4]'):
            self._single_regfile_property_test(dut=self.dut.switch2.forwarding_table.entry[4],
                                               size=16,
                                               rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]",
                                               rdl_desc="Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.",
                                               inst_name='entry[4]',
                                               parent_full_inst_name='openenoc_csr.switch2.forwarding_table')
            self._test_regfile_iterators(dut=self.dut.switch2.forwarding_table.entry[4],
                                         writeable_registers=NodeIterators('macaddr','iface','config',),
                                         readable_registers=NodeIterators('macaddr','iface','config',),
                                         sections=NodeIterators())
        with self.subTest(msg='regfile: openenoc_csr.switch2.forwarding_table.entry[5]'):
            self._single_regfile_property_test(dut=self.dut.switch2.forwarding_table.entry[5],
                                               size=16,
                                               rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]",
                                               rdl_desc="Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.",
                                               inst_name='entry[5]',
                                               parent_full_inst_name='openenoc_csr.switch2.forwarding_table')
            self._test_regfile_iterators(dut=self.dut.switch2.forwarding_table.entry[5],
                                         writeable_registers=NodeIterators('macaddr','iface','config',),
                                         readable_registers=NodeIterators('macaddr','iface','config',),
                                         sections=NodeIterators())
        with self.subTest(msg='regfile: openenoc_csr.switch2.forwarding_table.entry[6]'):
            self._single_regfile_property_test(dut=self.dut.switch2.forwarding_table.entry[6],
                                               size=16,
                                               rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]",
                                               rdl_desc="Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.",
                                               inst_name='entry[6]',
                                               parent_full_inst_name='openenoc_csr.switch2.forwarding_table')
            self._test_regfile_iterators(dut=self.dut.switch2.forwarding_table.entry[6],
                                         writeable_registers=NodeIterators('macaddr','iface','config',),
                                         readable_registers=NodeIterators('macaddr','iface','config',),
                                         sections=NodeIterators())
        with self.subTest(msg='regfile: openenoc_csr.switch2.forwarding_table.entry[7]'):
            self._single_regfile_property_test(dut=self.dut.switch2.forwarding_table.entry[7],
                                               size=16,
                                               rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]",
                                               rdl_desc="Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.",
                                               inst_name='entry[7]',
                                               parent_full_inst_name='openenoc_csr.switch2.forwarding_table')
            self._test_regfile_iterators(dut=self.dut.switch2.forwarding_table.entry[7],
                                         writeable_registers=NodeIterators('macaddr','iface','config',),
                                         readable_registers=NodeIterators('macaddr','iface','config',),
                                         sections=NodeIterators())
        with self.subTest(msg='regfile: openenoc_csr.switch2.forwarding_table.entry[8]'):
            self._single_regfile_property_test(dut=self.dut.switch2.forwarding_table.entry[8],
                                               size=16,
                                               rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]",
                                               rdl_desc="Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.",
                                               inst_name='entry[8]',
                                               parent_full_inst_name='openenoc_csr.switch2.forwarding_table')
            self._test_regfile_iterators(dut=self.dut.switch2.forwarding_table.entry[8],
                                         writeable_registers=NodeIterators('macaddr','iface','config',),
                                         readable_registers=NodeIterators('macaddr','iface','config',),
                                         sections=NodeIterators())
        with self.subTest(msg='regfile: openenoc_csr.switch2.forwarding_table.entry[9]'):
            self._single_regfile_property_test(dut=self.dut.switch2.forwarding_table.entry[9],
                                               size=16,
                                               rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]",
                                               rdl_desc="Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.",
                                               inst_name='entry[9]',
                                               parent_full_inst_name='openenoc_csr.switch2.forwarding_table')
            self._test_regfile_iterators(dut=self.dut.switch2.forwarding_table.entry[9],
                                         writeable_registers=NodeIterators('macaddr','iface','config',),
                                         readable_registers=NodeIterators('macaddr','iface','config',),
                                         sections=NodeIterators())
        with self.subTest(msg='regfile: openenoc_csr.switch2.forwarding_table.entry[10]'):
            self._single_regfile_property_test(dut=self.dut.switch2.forwarding_table.entry[10],
                                               size=16,
                                               rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]",
                                               rdl_desc="Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.",
                                               inst_name='entry[10]',
                                               parent_full_inst_name='openenoc_csr.switch2.forwarding_table')
            self._test_regfile_iterators(dut=self.dut.switch2.forwarding_table.entry[10],
                                         writeable_registers=NodeIterators('macaddr','iface','config',),
                                         readable_registers=NodeIterators('macaddr','iface','config',),
                                         sections=NodeIterators())
        with self.subTest(msg='regfile: openenoc_csr.switch2.forwarding_table.entry[11]'):
            self._single_regfile_property_test(dut=self.dut.switch2.forwarding_table.entry[11],
                                               size=16,
                                               rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]",
                                               rdl_desc="Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.",
                                               inst_name='entry[11]',
                                               parent_full_inst_name='openenoc_csr.switch2.forwarding_table')
            self._test_regfile_iterators(dut=self.dut.switch2.forwarding_table.entry[11],
                                         writeable_registers=NodeIterators('macaddr','iface','config',),
                                         readable_registers=NodeIterators('macaddr','iface','config',),
                                         sections=NodeIterators())
        with self.subTest(msg='regfile: openenoc_csr.switch2.forwarding_table.entry[12]'):
            self._single_regfile_property_test(dut=self.dut.switch2.forwarding_table.entry[12],
                                               size=16,
                                               rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]",
                                               rdl_desc="Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.",
                                               inst_name='entry[12]',
                                               parent_full_inst_name='openenoc_csr.switch2.forwarding_table')
            self._test_regfile_iterators(dut=self.dut.switch2.forwarding_table.entry[12],
                                         writeable_registers=NodeIterators('macaddr','iface','config',),
                                         readable_registers=NodeIterators('macaddr','iface','config',),
                                         sections=NodeIterators())
        with self.subTest(msg='regfile: openenoc_csr.switch2.forwarding_table.entry[13]'):
            self._single_regfile_property_test(dut=self.dut.switch2.forwarding_table.entry[13],
                                               size=16,
                                               rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]",
                                               rdl_desc="Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.",
                                               inst_name='entry[13]',
                                               parent_full_inst_name='openenoc_csr.switch2.forwarding_table')
            self._test_regfile_iterators(dut=self.dut.switch2.forwarding_table.entry[13],
                                         writeable_registers=NodeIterators('macaddr','iface','config',),
                                         readable_registers=NodeIterators('macaddr','iface','config',),
                                         sections=NodeIterators())
        with self.subTest(msg='regfile: openenoc_csr.switch2.forwarding_table.entry[14]'):
            self._single_regfile_property_test(dut=self.dut.switch2.forwarding_table.entry[14],
                                               size=16,
                                               rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]",
                                               rdl_desc="Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.",
                                               inst_name='entry[14]',
                                               parent_full_inst_name='openenoc_csr.switch2.forwarding_table')
            self._test_regfile_iterators(dut=self.dut.switch2.forwarding_table.entry[14],
                                         writeable_registers=NodeIterators('macaddr','iface','config',),
                                         readable_registers=NodeIterators('macaddr','iface','config',),
                                         sections=NodeIterators())
        with self.subTest(msg='regfile: openenoc_csr.switch2.forwarding_table.entry[15]'):
            self._single_regfile_property_test(dut=self.dut.switch2.forwarding_table.entry[15],
                                               size=16,
                                               rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]",
                                               rdl_desc="Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.",
                                               inst_name='entry[15]',
                                               parent_full_inst_name='openenoc_csr.switch2.forwarding_table')
            self._test_regfile_iterators(dut=self.dut.switch2.forwarding_table.entry[15],
                                         writeable_registers=NodeIterators('macaddr','iface','config',),
                                         readable_registers=NodeIterators('macaddr','iface','config',),
                                         sections=NodeIterators())
        with self.subTest(msg='regfile: openenoc_csr.switch2.forwarding_table.entry[16]'):
            self._single_regfile_property_test(dut=self.dut.switch2.forwarding_table.entry[16],
                                               size=16,
                                               rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]",
                                               rdl_desc="Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.",
                                               inst_name='entry[16]',
                                               parent_full_inst_name='openenoc_csr.switch2.forwarding_table')
            self._test_regfile_iterators(dut=self.dut.switch2.forwarding_table.entry[16],
                                         writeable_registers=NodeIterators('macaddr','iface','config',),
                                         readable_registers=NodeIterators('macaddr','iface','config',),
                                         sections=NodeIterators())
        with self.subTest(msg='regfile: openenoc_csr.switch2.forwarding_table.entry[17]'):
            self._single_regfile_property_test(dut=self.dut.switch2.forwarding_table.entry[17],
                                               size=16,
                                               rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]",
                                               rdl_desc="Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.",
                                               inst_name='entry[17]',
                                               parent_full_inst_name='openenoc_csr.switch2.forwarding_table')
            self._test_regfile_iterators(dut=self.dut.switch2.forwarding_table.entry[17],
                                         writeable_registers=NodeIterators('macaddr','iface','config',),
                                         readable_registers=NodeIterators('macaddr','iface','config',),
                                         sections=NodeIterators())
        with self.subTest(msg='regfile: openenoc_csr.switch2.forwarding_table.entry[18]'):
            self._single_regfile_property_test(dut=self.dut.switch2.forwarding_table.entry[18],
                                               size=16,
                                               rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]",
                                               rdl_desc="Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.",
                                               inst_name='entry[18]',
                                               parent_full_inst_name='openenoc_csr.switch2.forwarding_table')
            self._test_regfile_iterators(dut=self.dut.switch2.forwarding_table.entry[18],
                                         writeable_registers=NodeIterators('macaddr','iface','config',),
                                         readable_registers=NodeIterators('macaddr','iface','config',),
                                         sections=NodeIterators())
        with self.subTest(msg='regfile: openenoc_csr.switch2.forwarding_table.entry[19]'):
            self._single_regfile_property_test(dut=self.dut.switch2.forwarding_table.entry[19],
                                               size=16,
                                               rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]",
                                               rdl_desc="Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.",
                                               inst_name='entry[19]',
                                               parent_full_inst_name='openenoc_csr.switch2.forwarding_table')
            self._test_regfile_iterators(dut=self.dut.switch2.forwarding_table.entry[19],
                                         writeable_registers=NodeIterators('macaddr','iface','config',),
                                         readable_registers=NodeIterators('macaddr','iface','config',),
                                         sections=NodeIterators())
        with self.subTest(msg='regfile: openenoc_csr.switch2.forwarding_table.entry[20]'):
            self._single_regfile_property_test(dut=self.dut.switch2.forwarding_table.entry[20],
                                               size=16,
                                               rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]",
                                               rdl_desc="Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.",
                                               inst_name='entry[20]',
                                               parent_full_inst_name='openenoc_csr.switch2.forwarding_table')
            self._test_regfile_iterators(dut=self.dut.switch2.forwarding_table.entry[20],
                                         writeable_registers=NodeIterators('macaddr','iface','config',),
                                         readable_registers=NodeIterators('macaddr','iface','config',),
                                         sections=NodeIterators())
        with self.subTest(msg='regfile: openenoc_csr.switch2.forwarding_table.entry[21]'):
            self._single_regfile_property_test(dut=self.dut.switch2.forwarding_table.entry[21],
                                               size=16,
                                               rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]",
                                               rdl_desc="Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.",
                                               inst_name='entry[21]',
                                               parent_full_inst_name='openenoc_csr.switch2.forwarding_table')
            self._test_regfile_iterators(dut=self.dut.switch2.forwarding_table.entry[21],
                                         writeable_registers=NodeIterators('macaddr','iface','config',),
                                         readable_registers=NodeIterators('macaddr','iface','config',),
                                         sections=NodeIterators())
        with self.subTest(msg='regfile: openenoc_csr.switch2.forwarding_table.entry[22]'):
            self._single_regfile_property_test(dut=self.dut.switch2.forwarding_table.entry[22],
                                               size=16,
                                               rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]",
                                               rdl_desc="Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.",
                                               inst_name='entry[22]',
                                               parent_full_inst_name='openenoc_csr.switch2.forwarding_table')
            self._test_regfile_iterators(dut=self.dut.switch2.forwarding_table.entry[22],
                                         writeable_registers=NodeIterators('macaddr','iface','config',),
                                         readable_registers=NodeIterators('macaddr','iface','config',),
                                         sections=NodeIterators())
        with self.subTest(msg='regfile: openenoc_csr.switch2.forwarding_table.entry[23]'):
            self._single_regfile_property_test(dut=self.dut.switch2.forwarding_table.entry[23],
                                               size=16,
                                               rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]",
                                               rdl_desc="Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.",
                                               inst_name='entry[23]',
                                               parent_full_inst_name='openenoc_csr.switch2.forwarding_table')
            self._test_regfile_iterators(dut=self.dut.switch2.forwarding_table.entry[23],
                                         writeable_registers=NodeIterators('macaddr','iface','config',),
                                         readable_registers=NodeIterators('macaddr','iface','config',),
                                         sections=NodeIterators())
        with self.subTest(msg='regfile: openenoc_csr.switch2.forwarding_table.entry[24]'):
            self._single_regfile_property_test(dut=self.dut.switch2.forwarding_table.entry[24],
                                               size=16,
                                               rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]",
                                               rdl_desc="Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.",
                                               inst_name='entry[24]',
                                               parent_full_inst_name='openenoc_csr.switch2.forwarding_table')
            self._test_regfile_iterators(dut=self.dut.switch2.forwarding_table.entry[24],
                                         writeable_registers=NodeIterators('macaddr','iface','config',),
                                         readable_registers=NodeIterators('macaddr','iface','config',),
                                         sections=NodeIterators())
        with self.subTest(msg='regfile: openenoc_csr.switch2.forwarding_table.entry[25]'):
            self._single_regfile_property_test(dut=self.dut.switch2.forwarding_table.entry[25],
                                               size=16,
                                               rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]",
                                               rdl_desc="Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.",
                                               inst_name='entry[25]',
                                               parent_full_inst_name='openenoc_csr.switch2.forwarding_table')
            self._test_regfile_iterators(dut=self.dut.switch2.forwarding_table.entry[25],
                                         writeable_registers=NodeIterators('macaddr','iface','config',),
                                         readable_registers=NodeIterators('macaddr','iface','config',),
                                         sections=NodeIterators())
        with self.subTest(msg='regfile: openenoc_csr.switch2.forwarding_table.entry[26]'):
            self._single_regfile_property_test(dut=self.dut.switch2.forwarding_table.entry[26],
                                               size=16,
                                               rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]",
                                               rdl_desc="Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.",
                                               inst_name='entry[26]',
                                               parent_full_inst_name='openenoc_csr.switch2.forwarding_table')
            self._test_regfile_iterators(dut=self.dut.switch2.forwarding_table.entry[26],
                                         writeable_registers=NodeIterators('macaddr','iface','config',),
                                         readable_registers=NodeIterators('macaddr','iface','config',),
                                         sections=NodeIterators())
        with self.subTest(msg='regfile: openenoc_csr.switch2.forwarding_table.entry[27]'):
            self._single_regfile_property_test(dut=self.dut.switch2.forwarding_table.entry[27],
                                               size=16,
                                               rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]",
                                               rdl_desc="Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.",
                                               inst_name='entry[27]',
                                               parent_full_inst_name='openenoc_csr.switch2.forwarding_table')
            self._test_regfile_iterators(dut=self.dut.switch2.forwarding_table.entry[27],
                                         writeable_registers=NodeIterators('macaddr','iface','config',),
                                         readable_registers=NodeIterators('macaddr','iface','config',),
                                         sections=NodeIterators())
        with self.subTest(msg='regfile: openenoc_csr.switch2.forwarding_table.entry[28]'):
            self._single_regfile_property_test(dut=self.dut.switch2.forwarding_table.entry[28],
                                               size=16,
                                               rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]",
                                               rdl_desc="Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.",
                                               inst_name='entry[28]',
                                               parent_full_inst_name='openenoc_csr.switch2.forwarding_table')
            self._test_regfile_iterators(dut=self.dut.switch2.forwarding_table.entry[28],
                                         writeable_registers=NodeIterators('macaddr','iface','config',),
                                         readable_registers=NodeIterators('macaddr','iface','config',),
                                         sections=NodeIterators())
        with self.subTest(msg='regfile: openenoc_csr.switch2.forwarding_table.entry[29]'):
            self._single_regfile_property_test(dut=self.dut.switch2.forwarding_table.entry[29],
                                               size=16,
                                               rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]",
                                               rdl_desc="Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.",
                                               inst_name='entry[29]',
                                               parent_full_inst_name='openenoc_csr.switch2.forwarding_table')
            self._test_regfile_iterators(dut=self.dut.switch2.forwarding_table.entry[29],
                                         writeable_registers=NodeIterators('macaddr','iface','config',),
                                         readable_registers=NodeIterators('macaddr','iface','config',),
                                         sections=NodeIterators())
        with self.subTest(msg='regfile: openenoc_csr.switch2.forwarding_table.entry[30]'):
            self._single_regfile_property_test(dut=self.dut.switch2.forwarding_table.entry[30],
                                               size=16,
                                               rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]",
                                               rdl_desc="Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.",
                                               inst_name='entry[30]',
                                               parent_full_inst_name='openenoc_csr.switch2.forwarding_table')
            self._test_regfile_iterators(dut=self.dut.switch2.forwarding_table.entry[30],
                                         writeable_registers=NodeIterators('macaddr','iface','config',),
                                         readable_registers=NodeIterators('macaddr','iface','config',),
                                         sections=NodeIterators())
        with self.subTest(msg='regfile: openenoc_csr.switch2.forwarding_table.entry[31]'):
            self._single_regfile_property_test(dut=self.dut.switch2.forwarding_table.entry[31],
                                               size=16,
                                               rdl_name="csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]",
                                               rdl_desc="Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.",
                                               inst_name='entry[31]',
                                               parent_full_inst_name='openenoc_csr.switch2.forwarding_table')
            self._test_regfile_iterators(dut=self.dut.switch2.forwarding_table.entry[31],
                                         writeable_registers=NodeIterators('macaddr','iface','config',),
                                         readable_registers=NodeIterators('macaddr','iface','config',),
                                         sections=NodeIterators())
        

    

    def test_array_slicing(self) -> None:
        """
        Check slicing into array
        """
        full_slice:NodeArray
        
        with self.subTest(msg='hidden_node: openenoc_csr.switch2.forwarding_table.entry[]'):
            
            full_slice = self.dut.switch2.forwarding_table.get_child_by_system_rdl_name('entry')
            
            self.assertCountEqual(iter(full_slice[:]), iter(full_slice))
        



class openenoc_csr_switch2_block_access(openenoc_csr_TestCase_BlockAccess): # type: ignore[valid-type,misc]
    """
    tests for all the block access methods
    """

    

    def test_register_array_context_manager(self) -> None:
        """
        Walk the register map and check that register map context managers work correctly
        """
        

class openenoc_csr_switch2_alt_block_access(openenoc_csr_TestCase_AltBlockAccess): # type: ignore[valid-type,misc]
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