


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




class openenoc_csr_switch1_single_access(openenoc_csr_TestCase): # type: ignore[valid-type,misc]



    def test_user_defined_properties(self)  -> None:
        """
        Walk the address map and check user defined properties are correctly pulled up
        """
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[0]'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.entry[0].udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[1]'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.entry[1].udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[2]'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.entry[2].udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[3]'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.entry[3].udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[4]'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.entry[4].udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[5]'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.entry[5].udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[6]'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.entry[6].udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[7]'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.entry[7].udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.info'):
            
            
            self.assertDictEqual(self.dut.switch1.info.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_control'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_control.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.default_forwarding'):
            
            
            self.assertDictEqual(self.dut.switch1.default_forwarding.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[0].macaddr'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.entry[0].macaddr.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[0].iface'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.entry[0].iface.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[0].config'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.entry[0].config.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[1].macaddr'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.entry[1].macaddr.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[1].iface'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.entry[1].iface.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[1].config'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.entry[1].config.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[2].macaddr'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.entry[2].macaddr.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[2].iface'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.entry[2].iface.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[2].config'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.entry[2].config.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[3].macaddr'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.entry[3].macaddr.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[3].iface'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.entry[3].iface.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[3].config'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.entry[3].config.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[4].macaddr'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.entry[4].macaddr.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[4].iface'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.entry[4].iface.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[4].config'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.entry[4].config.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[5].macaddr'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.entry[5].macaddr.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[5].iface'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.entry[5].iface.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[5].config'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.entry[5].config.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[6].macaddr'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.entry[6].macaddr.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[6].iface'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.entry[6].iface.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[6].config'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.entry[6].config.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[7].macaddr'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.entry[7].macaddr.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[7].iface'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.entry[7].iface.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[7].config'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.entry[7].config.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.info.table_depth'):
            
            
            self.assertDictEqual(self.dut.switch1.info.table_depth.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.info.num_of_interfaces'):
            
            
            self.assertDictEqual(self.dut.switch1.info.num_of_interfaces.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_control.operation_mode'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_control.operation_mode.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_control.pause_request'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_control.pause_request.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_control.pause_done'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_control.pause_done.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.default_forwarding.bitmap'):
            
            
            self.assertDictEqual(self.dut.switch1.default_forwarding.bitmap.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[0].macaddr.lo_word'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.entry[0].macaddr.lo_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[0].macaddr.hi_word'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.entry[0].macaddr.hi_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[0].iface.bitmap'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.entry[0].iface.bitmap.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[0].config.enabled'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.entry[0].config.enabled.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[1].macaddr.lo_word'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.entry[1].macaddr.lo_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[1].macaddr.hi_word'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.entry[1].macaddr.hi_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[1].iface.bitmap'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.entry[1].iface.bitmap.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[1].config.enabled'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.entry[1].config.enabled.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[2].macaddr.lo_word'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.entry[2].macaddr.lo_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[2].macaddr.hi_word'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.entry[2].macaddr.hi_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[2].iface.bitmap'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.entry[2].iface.bitmap.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[2].config.enabled'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.entry[2].config.enabled.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[3].macaddr.lo_word'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.entry[3].macaddr.lo_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[3].macaddr.hi_word'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.entry[3].macaddr.hi_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[3].iface.bitmap'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.entry[3].iface.bitmap.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[3].config.enabled'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.entry[3].config.enabled.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[4].macaddr.lo_word'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.entry[4].macaddr.lo_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[4].macaddr.hi_word'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.entry[4].macaddr.hi_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[4].iface.bitmap'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.entry[4].iface.bitmap.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[4].config.enabled'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.entry[4].config.enabled.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[5].macaddr.lo_word'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.entry[5].macaddr.lo_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[5].macaddr.hi_word'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.entry[5].macaddr.hi_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[5].iface.bitmap'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.entry[5].iface.bitmap.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[5].config.enabled'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.entry[5].config.enabled.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[6].macaddr.lo_word'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.entry[6].macaddr.lo_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[6].macaddr.hi_word'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.entry[6].macaddr.hi_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[6].iface.bitmap'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.entry[6].iface.bitmap.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[6].config.enabled'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.entry[6].config.enabled.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[7].macaddr.lo_word'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.entry[7].macaddr.lo_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[7].macaddr.hi_word'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.entry[7].macaddr.hi_word.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[7].iface.bitmap'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.entry[7].iface.bitmap.udp,{})
            
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[7].config.enabled'):
            
            
            self.assertDictEqual(self.dut.switch1.forwarding_table.entry[7].config.enabled.udp,{})
            
        

     

    def test_register(self) -> None:
        """
        Walk the registers in the register map and check:
        - the properties
        - it can be read and written to correctly
        """
        with self.subTest(msg='register: openenoc_csr.switch1.info'):
            self._single_register_property_test(rut=self.dut.switch1.info, address=256, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch1.info",
                                                rdl_desc="Read-only information register for this openENOC Switch instance.",
                                                inst_name='info',
                                                parent_full_inst_name='openenoc_csr.switch1')
            self._single_register_read_and_write_test(rut=self.dut.switch1.info, has_sw_readable=True, has_sw_writable=False,
                                                                                          readable_fields=set(['table_depth','num_of_interfaces', ]),
                                                                                          writeable_fields=set([ ]) )
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_control'):
            self._single_register_property_test(rut=self.dut.switch1.forwarding_control, address=260, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch1.forwarding_control",
                                                rdl_desc="Forwarding control register for the openENOC Switch instance.",
                                                inst_name='forwarding_control',
                                                parent_full_inst_name='openenoc_csr.switch1')
            self._single_register_read_and_write_test(rut=self.dut.switch1.forwarding_control, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['operation_mode','pause_request','pause_done', ]),
                                                                                          writeable_fields=set(['operation_mode','pause_request', ]) )
        with self.subTest(msg='register: openenoc_csr.switch1.default_forwarding'):
            self._single_register_property_test(rut=self.dut.switch1.default_forwarding, address=264, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch1.default_forwarding",
                                                rdl_desc="Defines the destination interface or interfaces for frames that do not match any enabled forwarding table entry.",
                                                inst_name='default_forwarding',
                                                parent_full_inst_name='openenoc_csr.switch1')
            self._single_register_read_and_write_test(rut=self.dut.switch1.default_forwarding, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['bitmap', ]),
                                                                                          writeable_fields=set(['bitmap', ]) )
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[0].macaddr'):
            self._single_register_property_test(rut=self.dut.switch1.forwarding_table.entry[0].macaddr, address=384, width=64, accesswidth=32, size=8,
                                                rdl_name="csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr",
                                                rdl_desc="48-bit destination MAC address used as the key for this forwarding table entry.",
                                                inst_name='macaddr',
                                                parent_full_inst_name='openenoc_csr.switch1.forwarding_table.entry[0]')
            self._single_register_read_and_write_test(rut=self.dut.switch1.forwarding_table.entry[0].macaddr, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['lo_word','hi_word', ]),
                                                                                          writeable_fields=set(['lo_word','hi_word', ]) )
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[0].iface'):
            self._single_register_property_test(rut=self.dut.switch1.forwarding_table.entry[0].iface, address=392, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].iface",
                                                rdl_desc="Forwarding interface information associated with this forwarding table entry.",
                                                inst_name='iface',
                                                parent_full_inst_name='openenoc_csr.switch1.forwarding_table.entry[0]')
            self._single_register_read_and_write_test(rut=self.dut.switch1.forwarding_table.entry[0].iface, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['bitmap', ]),
                                                                                          writeable_fields=set(['bitmap', ]) )
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[0].config'):
            self._single_register_property_test(rut=self.dut.switch1.forwarding_table.entry[0].config, address=396, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].config",
                                                rdl_desc="Configuration information associated with this forwarding table entry.",
                                                inst_name='config',
                                                parent_full_inst_name='openenoc_csr.switch1.forwarding_table.entry[0]')
            self._single_register_read_and_write_test(rut=self.dut.switch1.forwarding_table.entry[0].config, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['enabled', ]),
                                                                                          writeable_fields=set(['enabled', ]) )
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[1].macaddr'):
            self._single_register_property_test(rut=self.dut.switch1.forwarding_table.entry[1].macaddr, address=400, width=64, accesswidth=32, size=8,
                                                rdl_name="csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr",
                                                rdl_desc="48-bit destination MAC address used as the key for this forwarding table entry.",
                                                inst_name='macaddr',
                                                parent_full_inst_name='openenoc_csr.switch1.forwarding_table.entry[1]')
            self._single_register_read_and_write_test(rut=self.dut.switch1.forwarding_table.entry[1].macaddr, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['lo_word','hi_word', ]),
                                                                                          writeable_fields=set(['lo_word','hi_word', ]) )
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[1].iface'):
            self._single_register_property_test(rut=self.dut.switch1.forwarding_table.entry[1].iface, address=408, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].iface",
                                                rdl_desc="Forwarding interface information associated with this forwarding table entry.",
                                                inst_name='iface',
                                                parent_full_inst_name='openenoc_csr.switch1.forwarding_table.entry[1]')
            self._single_register_read_and_write_test(rut=self.dut.switch1.forwarding_table.entry[1].iface, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['bitmap', ]),
                                                                                          writeable_fields=set(['bitmap', ]) )
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[1].config'):
            self._single_register_property_test(rut=self.dut.switch1.forwarding_table.entry[1].config, address=412, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].config",
                                                rdl_desc="Configuration information associated with this forwarding table entry.",
                                                inst_name='config',
                                                parent_full_inst_name='openenoc_csr.switch1.forwarding_table.entry[1]')
            self._single_register_read_and_write_test(rut=self.dut.switch1.forwarding_table.entry[1].config, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['enabled', ]),
                                                                                          writeable_fields=set(['enabled', ]) )
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[2].macaddr'):
            self._single_register_property_test(rut=self.dut.switch1.forwarding_table.entry[2].macaddr, address=416, width=64, accesswidth=32, size=8,
                                                rdl_name="csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr",
                                                rdl_desc="48-bit destination MAC address used as the key for this forwarding table entry.",
                                                inst_name='macaddr',
                                                parent_full_inst_name='openenoc_csr.switch1.forwarding_table.entry[2]')
            self._single_register_read_and_write_test(rut=self.dut.switch1.forwarding_table.entry[2].macaddr, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['lo_word','hi_word', ]),
                                                                                          writeable_fields=set(['lo_word','hi_word', ]) )
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[2].iface'):
            self._single_register_property_test(rut=self.dut.switch1.forwarding_table.entry[2].iface, address=424, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].iface",
                                                rdl_desc="Forwarding interface information associated with this forwarding table entry.",
                                                inst_name='iface',
                                                parent_full_inst_name='openenoc_csr.switch1.forwarding_table.entry[2]')
            self._single_register_read_and_write_test(rut=self.dut.switch1.forwarding_table.entry[2].iface, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['bitmap', ]),
                                                                                          writeable_fields=set(['bitmap', ]) )
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[2].config'):
            self._single_register_property_test(rut=self.dut.switch1.forwarding_table.entry[2].config, address=428, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].config",
                                                rdl_desc="Configuration information associated with this forwarding table entry.",
                                                inst_name='config',
                                                parent_full_inst_name='openenoc_csr.switch1.forwarding_table.entry[2]')
            self._single_register_read_and_write_test(rut=self.dut.switch1.forwarding_table.entry[2].config, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['enabled', ]),
                                                                                          writeable_fields=set(['enabled', ]) )
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[3].macaddr'):
            self._single_register_property_test(rut=self.dut.switch1.forwarding_table.entry[3].macaddr, address=432, width=64, accesswidth=32, size=8,
                                                rdl_name="csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr",
                                                rdl_desc="48-bit destination MAC address used as the key for this forwarding table entry.",
                                                inst_name='macaddr',
                                                parent_full_inst_name='openenoc_csr.switch1.forwarding_table.entry[3]')
            self._single_register_read_and_write_test(rut=self.dut.switch1.forwarding_table.entry[3].macaddr, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['lo_word','hi_word', ]),
                                                                                          writeable_fields=set(['lo_word','hi_word', ]) )
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[3].iface'):
            self._single_register_property_test(rut=self.dut.switch1.forwarding_table.entry[3].iface, address=440, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].iface",
                                                rdl_desc="Forwarding interface information associated with this forwarding table entry.",
                                                inst_name='iface',
                                                parent_full_inst_name='openenoc_csr.switch1.forwarding_table.entry[3]')
            self._single_register_read_and_write_test(rut=self.dut.switch1.forwarding_table.entry[3].iface, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['bitmap', ]),
                                                                                          writeable_fields=set(['bitmap', ]) )
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[3].config'):
            self._single_register_property_test(rut=self.dut.switch1.forwarding_table.entry[3].config, address=444, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].config",
                                                rdl_desc="Configuration information associated with this forwarding table entry.",
                                                inst_name='config',
                                                parent_full_inst_name='openenoc_csr.switch1.forwarding_table.entry[3]')
            self._single_register_read_and_write_test(rut=self.dut.switch1.forwarding_table.entry[3].config, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['enabled', ]),
                                                                                          writeable_fields=set(['enabled', ]) )
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[4].macaddr'):
            self._single_register_property_test(rut=self.dut.switch1.forwarding_table.entry[4].macaddr, address=448, width=64, accesswidth=32, size=8,
                                                rdl_name="csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr",
                                                rdl_desc="48-bit destination MAC address used as the key for this forwarding table entry.",
                                                inst_name='macaddr',
                                                parent_full_inst_name='openenoc_csr.switch1.forwarding_table.entry[4]')
            self._single_register_read_and_write_test(rut=self.dut.switch1.forwarding_table.entry[4].macaddr, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['lo_word','hi_word', ]),
                                                                                          writeable_fields=set(['lo_word','hi_word', ]) )
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[4].iface'):
            self._single_register_property_test(rut=self.dut.switch1.forwarding_table.entry[4].iface, address=456, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].iface",
                                                rdl_desc="Forwarding interface information associated with this forwarding table entry.",
                                                inst_name='iface',
                                                parent_full_inst_name='openenoc_csr.switch1.forwarding_table.entry[4]')
            self._single_register_read_and_write_test(rut=self.dut.switch1.forwarding_table.entry[4].iface, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['bitmap', ]),
                                                                                          writeable_fields=set(['bitmap', ]) )
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[4].config'):
            self._single_register_property_test(rut=self.dut.switch1.forwarding_table.entry[4].config, address=460, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].config",
                                                rdl_desc="Configuration information associated with this forwarding table entry.",
                                                inst_name='config',
                                                parent_full_inst_name='openenoc_csr.switch1.forwarding_table.entry[4]')
            self._single_register_read_and_write_test(rut=self.dut.switch1.forwarding_table.entry[4].config, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['enabled', ]),
                                                                                          writeable_fields=set(['enabled', ]) )
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[5].macaddr'):
            self._single_register_property_test(rut=self.dut.switch1.forwarding_table.entry[5].macaddr, address=464, width=64, accesswidth=32, size=8,
                                                rdl_name="csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr",
                                                rdl_desc="48-bit destination MAC address used as the key for this forwarding table entry.",
                                                inst_name='macaddr',
                                                parent_full_inst_name='openenoc_csr.switch1.forwarding_table.entry[5]')
            self._single_register_read_and_write_test(rut=self.dut.switch1.forwarding_table.entry[5].macaddr, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['lo_word','hi_word', ]),
                                                                                          writeable_fields=set(['lo_word','hi_word', ]) )
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[5].iface'):
            self._single_register_property_test(rut=self.dut.switch1.forwarding_table.entry[5].iface, address=472, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].iface",
                                                rdl_desc="Forwarding interface information associated with this forwarding table entry.",
                                                inst_name='iface',
                                                parent_full_inst_name='openenoc_csr.switch1.forwarding_table.entry[5]')
            self._single_register_read_and_write_test(rut=self.dut.switch1.forwarding_table.entry[5].iface, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['bitmap', ]),
                                                                                          writeable_fields=set(['bitmap', ]) )
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[5].config'):
            self._single_register_property_test(rut=self.dut.switch1.forwarding_table.entry[5].config, address=476, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].config",
                                                rdl_desc="Configuration information associated with this forwarding table entry.",
                                                inst_name='config',
                                                parent_full_inst_name='openenoc_csr.switch1.forwarding_table.entry[5]')
            self._single_register_read_and_write_test(rut=self.dut.switch1.forwarding_table.entry[5].config, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['enabled', ]),
                                                                                          writeable_fields=set(['enabled', ]) )
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[6].macaddr'):
            self._single_register_property_test(rut=self.dut.switch1.forwarding_table.entry[6].macaddr, address=480, width=64, accesswidth=32, size=8,
                                                rdl_name="csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr",
                                                rdl_desc="48-bit destination MAC address used as the key for this forwarding table entry.",
                                                inst_name='macaddr',
                                                parent_full_inst_name='openenoc_csr.switch1.forwarding_table.entry[6]')
            self._single_register_read_and_write_test(rut=self.dut.switch1.forwarding_table.entry[6].macaddr, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['lo_word','hi_word', ]),
                                                                                          writeable_fields=set(['lo_word','hi_word', ]) )
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[6].iface'):
            self._single_register_property_test(rut=self.dut.switch1.forwarding_table.entry[6].iface, address=488, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].iface",
                                                rdl_desc="Forwarding interface information associated with this forwarding table entry.",
                                                inst_name='iface',
                                                parent_full_inst_name='openenoc_csr.switch1.forwarding_table.entry[6]')
            self._single_register_read_and_write_test(rut=self.dut.switch1.forwarding_table.entry[6].iface, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['bitmap', ]),
                                                                                          writeable_fields=set(['bitmap', ]) )
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[6].config'):
            self._single_register_property_test(rut=self.dut.switch1.forwarding_table.entry[6].config, address=492, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].config",
                                                rdl_desc="Configuration information associated with this forwarding table entry.",
                                                inst_name='config',
                                                parent_full_inst_name='openenoc_csr.switch1.forwarding_table.entry[6]')
            self._single_register_read_and_write_test(rut=self.dut.switch1.forwarding_table.entry[6].config, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['enabled', ]),
                                                                                          writeable_fields=set(['enabled', ]) )
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[7].macaddr'):
            self._single_register_property_test(rut=self.dut.switch1.forwarding_table.entry[7].macaddr, address=496, width=64, accesswidth=32, size=8,
                                                rdl_name="csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr",
                                                rdl_desc="48-bit destination MAC address used as the key for this forwarding table entry.",
                                                inst_name='macaddr',
                                                parent_full_inst_name='openenoc_csr.switch1.forwarding_table.entry[7]')
            self._single_register_read_and_write_test(rut=self.dut.switch1.forwarding_table.entry[7].macaddr, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['lo_word','hi_word', ]),
                                                                                          writeable_fields=set(['lo_word','hi_word', ]) )
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[7].iface'):
            self._single_register_property_test(rut=self.dut.switch1.forwarding_table.entry[7].iface, address=504, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].iface",
                                                rdl_desc="Forwarding interface information associated with this forwarding table entry.",
                                                inst_name='iface',
                                                parent_full_inst_name='openenoc_csr.switch1.forwarding_table.entry[7]')
            self._single_register_read_and_write_test(rut=self.dut.switch1.forwarding_table.entry[7].iface, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['bitmap', ]),
                                                                                          writeable_fields=set(['bitmap', ]) )
        with self.subTest(msg='register: openenoc_csr.switch1.forwarding_table.entry[7].config'):
            self._single_register_property_test(rut=self.dut.switch1.forwarding_table.entry[7].config, address=508, width=32, accesswidth=32, size=4,
                                                rdl_name="csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].config",
                                                rdl_desc="Configuration information associated with this forwarding table entry.",
                                                inst_name='config',
                                                parent_full_inst_name='openenoc_csr.switch1.forwarding_table.entry[7]')
            self._single_register_read_and_write_test(rut=self.dut.switch1.forwarding_table.entry[7].config, has_sw_readable=True, has_sw_writable=True,
                                                                                          readable_fields=set(['enabled', ]),
                                                                                          writeable_fields=set(['enabled', ]) )
        

    def test_field(self) -> None:
        """
        Check the properties and function (read and write) on the fields both integer and enum
        """
        
        with self.subTest(msg='field: openenoc_csr.switch1.info.table_depth'):
            self._single_field_property_test(fut=self.dut.switch1.info.table_depth, lsb=0, msb=15, low=0, high=15, is_volatile=False, default=8,
                                             rdl_name="csr.switch1.info.table_depth[15:0]",
                                             rdl_desc="Depth of the forwarding table in this openENOC Switch instance. This field reflects the TABLE_DEPTH parameter value.",
                                             inst_name='table_depth',
                                             parent_full_inst_name='openenoc_csr.switch1.info')
            self._single_int_field_read_and_write_test(fut=self.dut.switch1.info.table_depth, is_sw_readable=True, is_sw_writable=False)
        with self.subTest(msg='field: openenoc_csr.switch1.info.num_of_interfaces'):
            self._single_field_property_test(fut=self.dut.switch1.info.num_of_interfaces, lsb=16, msb=21, low=16, high=21, is_volatile=False, default=4,
                                             rdl_name="csr.switch1.info.num_of_interfaces[21:16]",
                                             rdl_desc="Number of interfaces in this openENOC Switch instance. This field reflects the NUM_OF_INTERFACES parameter value.",
                                             inst_name='num_of_interfaces',
                                             parent_full_inst_name='openenoc_csr.switch1.info')
            self._single_int_field_read_and_write_test(fut=self.dut.switch1.info.num_of_interfaces, is_sw_readable=True, is_sw_writable=False)
        with self.subTest(msg='field: openenoc_csr.switch1.forwarding_control.operation_mode'):
            self._single_field_property_test(fut=self.dut.switch1.forwarding_control.operation_mode, lsb=0, msb=0, low=0, high=0, is_volatile=False, default=0,
                                             rdl_name="csr.switch1.forwarding_control.operation_mode[0:0]",
                                             rdl_desc="Mode of operation for the openENOC Switch instance. When set to 1, the switch operates in managed mode, allowing software to configure the forwarding table and control forwarding operations. When set to 0, the switch operates in unmanaged mode, where forwarding state is maintained autonomously by internal hardware logic without software intervention.",
                                             inst_name='operation_mode',
                                             parent_full_inst_name='openenoc_csr.switch1.forwarding_control')
            self._single_int_field_read_and_write_test(fut=self.dut.switch1.forwarding_control.operation_mode, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch1.forwarding_control.pause_request'):
            self._single_field_property_test(fut=self.dut.switch1.forwarding_control.pause_request, lsb=7, msb=7, low=7, high=7, is_volatile=False, default=0,
                                             rdl_name="csr.switch1.forwarding_control.pause_request[7:7]",
                                             rdl_desc="Pause request for the forwarding logic. When set, this field requests the switch to pause frame forwarding and clear its internal pipeline before forwarding table updates are performed.",
                                             inst_name='pause_request',
                                             parent_full_inst_name='openenoc_csr.switch1.forwarding_control')
            self._single_int_field_read_and_write_test(fut=self.dut.switch1.forwarding_control.pause_request, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch1.forwarding_control.pause_done'):
            self._single_field_property_test(fut=self.dut.switch1.forwarding_control.pause_done, lsb=15, msb=15, low=15, high=15, is_volatile=True, default=None,
                                             rdl_name="csr.switch1.forwarding_control.pause_done[15:15]",
                                             rdl_desc="Pause done status. When set, this field indicates that the switch has paused frame forwarding and reached a safe state for forwarding table modification.",
                                             inst_name='pause_done',
                                             parent_full_inst_name='openenoc_csr.switch1.forwarding_control')
            self._single_int_field_read_and_write_test(fut=self.dut.switch1.forwarding_control.pause_done, is_sw_readable=True, is_sw_writable=False)
        with self.subTest(msg='field: openenoc_csr.switch1.default_forwarding.bitmap'):
            self._single_field_property_test(fut=self.dut.switch1.default_forwarding.bitmap, lsb=0, msb=3, low=0, high=3, is_volatile=False, default=0,
                                             rdl_name="csr.switch1.default_forwarding.bitmap[NUM_OF_INTERFACES-1:0]",
                                             rdl_desc="Bitmap selecting the output interface or interfaces to which frames that do not match any enabled forwarding table entry are forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.",
                                             inst_name='bitmap',
                                             parent_full_inst_name='openenoc_csr.switch1.default_forwarding')
            self._single_int_field_read_and_write_test(fut=self.dut.switch1.default_forwarding.bitmap, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch1.forwarding_table.entry[0].macaddr.lo_word'):
            self._single_field_property_test(fut=self.dut.switch1.forwarding_table.entry[0].macaddr.lo_word, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]",
                                             rdl_desc="Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='lo_word',
                                             parent_full_inst_name='openenoc_csr.switch1.forwarding_table.entry[0].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch1.forwarding_table.entry[0].macaddr.lo_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch1.forwarding_table.entry[0].macaddr.hi_word'):
            self._single_field_property_test(fut=self.dut.switch1.forwarding_table.entry[0].macaddr.hi_word, lsb=32, msb=47, low=32, high=47, is_volatile=True, default=None,
                                             rdl_name="csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]",
                                             rdl_desc="Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='hi_word',
                                             parent_full_inst_name='openenoc_csr.switch1.forwarding_table.entry[0].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch1.forwarding_table.entry[0].macaddr.hi_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch1.forwarding_table.entry[0].iface.bitmap'):
            self._single_field_property_test(fut=self.dut.switch1.forwarding_table.entry[0].iface.bitmap, lsb=0, msb=3, low=0, high=3, is_volatile=True, default=None,
                                             rdl_name="csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]",
                                             rdl_desc="Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.",
                                             inst_name='bitmap',
                                             parent_full_inst_name='openenoc_csr.switch1.forwarding_table.entry[0].iface')
            self._single_int_field_read_and_write_test(fut=self.dut.switch1.forwarding_table.entry[0].iface.bitmap, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch1.forwarding_table.entry[0].config.enabled'):
            self._single_field_property_test(fut=self.dut.switch1.forwarding_table.entry[0].config.enabled, lsb=0, msb=0, low=0, high=0, is_volatile=True, default=None,
                                             rdl_name="csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled",
                                             rdl_desc="Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.",
                                             inst_name='enabled',
                                             parent_full_inst_name='openenoc_csr.switch1.forwarding_table.entry[0].config')
            self._single_int_field_read_and_write_test(fut=self.dut.switch1.forwarding_table.entry[0].config.enabled, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch1.forwarding_table.entry[1].macaddr.lo_word'):
            self._single_field_property_test(fut=self.dut.switch1.forwarding_table.entry[1].macaddr.lo_word, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]",
                                             rdl_desc="Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='lo_word',
                                             parent_full_inst_name='openenoc_csr.switch1.forwarding_table.entry[1].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch1.forwarding_table.entry[1].macaddr.lo_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch1.forwarding_table.entry[1].macaddr.hi_word'):
            self._single_field_property_test(fut=self.dut.switch1.forwarding_table.entry[1].macaddr.hi_word, lsb=32, msb=47, low=32, high=47, is_volatile=True, default=None,
                                             rdl_name="csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]",
                                             rdl_desc="Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='hi_word',
                                             parent_full_inst_name='openenoc_csr.switch1.forwarding_table.entry[1].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch1.forwarding_table.entry[1].macaddr.hi_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch1.forwarding_table.entry[1].iface.bitmap'):
            self._single_field_property_test(fut=self.dut.switch1.forwarding_table.entry[1].iface.bitmap, lsb=0, msb=3, low=0, high=3, is_volatile=True, default=None,
                                             rdl_name="csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]",
                                             rdl_desc="Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.",
                                             inst_name='bitmap',
                                             parent_full_inst_name='openenoc_csr.switch1.forwarding_table.entry[1].iface')
            self._single_int_field_read_and_write_test(fut=self.dut.switch1.forwarding_table.entry[1].iface.bitmap, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch1.forwarding_table.entry[1].config.enabled'):
            self._single_field_property_test(fut=self.dut.switch1.forwarding_table.entry[1].config.enabled, lsb=0, msb=0, low=0, high=0, is_volatile=True, default=None,
                                             rdl_name="csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled",
                                             rdl_desc="Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.",
                                             inst_name='enabled',
                                             parent_full_inst_name='openenoc_csr.switch1.forwarding_table.entry[1].config')
            self._single_int_field_read_and_write_test(fut=self.dut.switch1.forwarding_table.entry[1].config.enabled, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch1.forwarding_table.entry[2].macaddr.lo_word'):
            self._single_field_property_test(fut=self.dut.switch1.forwarding_table.entry[2].macaddr.lo_word, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]",
                                             rdl_desc="Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='lo_word',
                                             parent_full_inst_name='openenoc_csr.switch1.forwarding_table.entry[2].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch1.forwarding_table.entry[2].macaddr.lo_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch1.forwarding_table.entry[2].macaddr.hi_word'):
            self._single_field_property_test(fut=self.dut.switch1.forwarding_table.entry[2].macaddr.hi_word, lsb=32, msb=47, low=32, high=47, is_volatile=True, default=None,
                                             rdl_name="csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]",
                                             rdl_desc="Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='hi_word',
                                             parent_full_inst_name='openenoc_csr.switch1.forwarding_table.entry[2].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch1.forwarding_table.entry[2].macaddr.hi_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch1.forwarding_table.entry[2].iface.bitmap'):
            self._single_field_property_test(fut=self.dut.switch1.forwarding_table.entry[2].iface.bitmap, lsb=0, msb=3, low=0, high=3, is_volatile=True, default=None,
                                             rdl_name="csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]",
                                             rdl_desc="Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.",
                                             inst_name='bitmap',
                                             parent_full_inst_name='openenoc_csr.switch1.forwarding_table.entry[2].iface')
            self._single_int_field_read_and_write_test(fut=self.dut.switch1.forwarding_table.entry[2].iface.bitmap, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch1.forwarding_table.entry[2].config.enabled'):
            self._single_field_property_test(fut=self.dut.switch1.forwarding_table.entry[2].config.enabled, lsb=0, msb=0, low=0, high=0, is_volatile=True, default=None,
                                             rdl_name="csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled",
                                             rdl_desc="Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.",
                                             inst_name='enabled',
                                             parent_full_inst_name='openenoc_csr.switch1.forwarding_table.entry[2].config')
            self._single_int_field_read_and_write_test(fut=self.dut.switch1.forwarding_table.entry[2].config.enabled, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch1.forwarding_table.entry[3].macaddr.lo_word'):
            self._single_field_property_test(fut=self.dut.switch1.forwarding_table.entry[3].macaddr.lo_word, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]",
                                             rdl_desc="Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='lo_word',
                                             parent_full_inst_name='openenoc_csr.switch1.forwarding_table.entry[3].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch1.forwarding_table.entry[3].macaddr.lo_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch1.forwarding_table.entry[3].macaddr.hi_word'):
            self._single_field_property_test(fut=self.dut.switch1.forwarding_table.entry[3].macaddr.hi_word, lsb=32, msb=47, low=32, high=47, is_volatile=True, default=None,
                                             rdl_name="csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]",
                                             rdl_desc="Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='hi_word',
                                             parent_full_inst_name='openenoc_csr.switch1.forwarding_table.entry[3].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch1.forwarding_table.entry[3].macaddr.hi_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch1.forwarding_table.entry[3].iface.bitmap'):
            self._single_field_property_test(fut=self.dut.switch1.forwarding_table.entry[3].iface.bitmap, lsb=0, msb=3, low=0, high=3, is_volatile=True, default=None,
                                             rdl_name="csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]",
                                             rdl_desc="Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.",
                                             inst_name='bitmap',
                                             parent_full_inst_name='openenoc_csr.switch1.forwarding_table.entry[3].iface')
            self._single_int_field_read_and_write_test(fut=self.dut.switch1.forwarding_table.entry[3].iface.bitmap, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch1.forwarding_table.entry[3].config.enabled'):
            self._single_field_property_test(fut=self.dut.switch1.forwarding_table.entry[3].config.enabled, lsb=0, msb=0, low=0, high=0, is_volatile=True, default=None,
                                             rdl_name="csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled",
                                             rdl_desc="Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.",
                                             inst_name='enabled',
                                             parent_full_inst_name='openenoc_csr.switch1.forwarding_table.entry[3].config')
            self._single_int_field_read_and_write_test(fut=self.dut.switch1.forwarding_table.entry[3].config.enabled, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch1.forwarding_table.entry[4].macaddr.lo_word'):
            self._single_field_property_test(fut=self.dut.switch1.forwarding_table.entry[4].macaddr.lo_word, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]",
                                             rdl_desc="Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='lo_word',
                                             parent_full_inst_name='openenoc_csr.switch1.forwarding_table.entry[4].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch1.forwarding_table.entry[4].macaddr.lo_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch1.forwarding_table.entry[4].macaddr.hi_word'):
            self._single_field_property_test(fut=self.dut.switch1.forwarding_table.entry[4].macaddr.hi_word, lsb=32, msb=47, low=32, high=47, is_volatile=True, default=None,
                                             rdl_name="csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]",
                                             rdl_desc="Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='hi_word',
                                             parent_full_inst_name='openenoc_csr.switch1.forwarding_table.entry[4].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch1.forwarding_table.entry[4].macaddr.hi_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch1.forwarding_table.entry[4].iface.bitmap'):
            self._single_field_property_test(fut=self.dut.switch1.forwarding_table.entry[4].iface.bitmap, lsb=0, msb=3, low=0, high=3, is_volatile=True, default=None,
                                             rdl_name="csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]",
                                             rdl_desc="Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.",
                                             inst_name='bitmap',
                                             parent_full_inst_name='openenoc_csr.switch1.forwarding_table.entry[4].iface')
            self._single_int_field_read_and_write_test(fut=self.dut.switch1.forwarding_table.entry[4].iface.bitmap, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch1.forwarding_table.entry[4].config.enabled'):
            self._single_field_property_test(fut=self.dut.switch1.forwarding_table.entry[4].config.enabled, lsb=0, msb=0, low=0, high=0, is_volatile=True, default=None,
                                             rdl_name="csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled",
                                             rdl_desc="Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.",
                                             inst_name='enabled',
                                             parent_full_inst_name='openenoc_csr.switch1.forwarding_table.entry[4].config')
            self._single_int_field_read_and_write_test(fut=self.dut.switch1.forwarding_table.entry[4].config.enabled, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch1.forwarding_table.entry[5].macaddr.lo_word'):
            self._single_field_property_test(fut=self.dut.switch1.forwarding_table.entry[5].macaddr.lo_word, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]",
                                             rdl_desc="Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='lo_word',
                                             parent_full_inst_name='openenoc_csr.switch1.forwarding_table.entry[5].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch1.forwarding_table.entry[5].macaddr.lo_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch1.forwarding_table.entry[5].macaddr.hi_word'):
            self._single_field_property_test(fut=self.dut.switch1.forwarding_table.entry[5].macaddr.hi_word, lsb=32, msb=47, low=32, high=47, is_volatile=True, default=None,
                                             rdl_name="csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]",
                                             rdl_desc="Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='hi_word',
                                             parent_full_inst_name='openenoc_csr.switch1.forwarding_table.entry[5].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch1.forwarding_table.entry[5].macaddr.hi_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch1.forwarding_table.entry[5].iface.bitmap'):
            self._single_field_property_test(fut=self.dut.switch1.forwarding_table.entry[5].iface.bitmap, lsb=0, msb=3, low=0, high=3, is_volatile=True, default=None,
                                             rdl_name="csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]",
                                             rdl_desc="Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.",
                                             inst_name='bitmap',
                                             parent_full_inst_name='openenoc_csr.switch1.forwarding_table.entry[5].iface')
            self._single_int_field_read_and_write_test(fut=self.dut.switch1.forwarding_table.entry[5].iface.bitmap, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch1.forwarding_table.entry[5].config.enabled'):
            self._single_field_property_test(fut=self.dut.switch1.forwarding_table.entry[5].config.enabled, lsb=0, msb=0, low=0, high=0, is_volatile=True, default=None,
                                             rdl_name="csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled",
                                             rdl_desc="Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.",
                                             inst_name='enabled',
                                             parent_full_inst_name='openenoc_csr.switch1.forwarding_table.entry[5].config')
            self._single_int_field_read_and_write_test(fut=self.dut.switch1.forwarding_table.entry[5].config.enabled, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch1.forwarding_table.entry[6].macaddr.lo_word'):
            self._single_field_property_test(fut=self.dut.switch1.forwarding_table.entry[6].macaddr.lo_word, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]",
                                             rdl_desc="Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='lo_word',
                                             parent_full_inst_name='openenoc_csr.switch1.forwarding_table.entry[6].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch1.forwarding_table.entry[6].macaddr.lo_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch1.forwarding_table.entry[6].macaddr.hi_word'):
            self._single_field_property_test(fut=self.dut.switch1.forwarding_table.entry[6].macaddr.hi_word, lsb=32, msb=47, low=32, high=47, is_volatile=True, default=None,
                                             rdl_name="csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]",
                                             rdl_desc="Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='hi_word',
                                             parent_full_inst_name='openenoc_csr.switch1.forwarding_table.entry[6].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch1.forwarding_table.entry[6].macaddr.hi_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch1.forwarding_table.entry[6].iface.bitmap'):
            self._single_field_property_test(fut=self.dut.switch1.forwarding_table.entry[6].iface.bitmap, lsb=0, msb=3, low=0, high=3, is_volatile=True, default=None,
                                             rdl_name="csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]",
                                             rdl_desc="Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.",
                                             inst_name='bitmap',
                                             parent_full_inst_name='openenoc_csr.switch1.forwarding_table.entry[6].iface')
            self._single_int_field_read_and_write_test(fut=self.dut.switch1.forwarding_table.entry[6].iface.bitmap, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch1.forwarding_table.entry[6].config.enabled'):
            self._single_field_property_test(fut=self.dut.switch1.forwarding_table.entry[6].config.enabled, lsb=0, msb=0, low=0, high=0, is_volatile=True, default=None,
                                             rdl_name="csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled",
                                             rdl_desc="Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.",
                                             inst_name='enabled',
                                             parent_full_inst_name='openenoc_csr.switch1.forwarding_table.entry[6].config')
            self._single_int_field_read_and_write_test(fut=self.dut.switch1.forwarding_table.entry[6].config.enabled, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch1.forwarding_table.entry[7].macaddr.lo_word'):
            self._single_field_property_test(fut=self.dut.switch1.forwarding_table.entry[7].macaddr.lo_word, lsb=0, msb=31, low=0, high=31, is_volatile=True, default=None,
                                             rdl_name="csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]",
                                             rdl_desc="Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='lo_word',
                                             parent_full_inst_name='openenoc_csr.switch1.forwarding_table.entry[7].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch1.forwarding_table.entry[7].macaddr.lo_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch1.forwarding_table.entry[7].macaddr.hi_word'):
            self._single_field_property_test(fut=self.dut.switch1.forwarding_table.entry[7].macaddr.hi_word, lsb=32, msb=47, low=32, high=47, is_volatile=True, default=None,
                                             rdl_name="csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]",
                                             rdl_desc="Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.",
                                             inst_name='hi_word',
                                             parent_full_inst_name='openenoc_csr.switch1.forwarding_table.entry[7].macaddr')
            self._single_int_field_read_and_write_test(fut=self.dut.switch1.forwarding_table.entry[7].macaddr.hi_word, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch1.forwarding_table.entry[7].iface.bitmap'):
            self._single_field_property_test(fut=self.dut.switch1.forwarding_table.entry[7].iface.bitmap, lsb=0, msb=3, low=0, high=3, is_volatile=True, default=None,
                                             rdl_name="csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]",
                                             rdl_desc="Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.",
                                             inst_name='bitmap',
                                             parent_full_inst_name='openenoc_csr.switch1.forwarding_table.entry[7].iface')
            self._single_int_field_read_and_write_test(fut=self.dut.switch1.forwarding_table.entry[7].iface.bitmap, is_sw_readable=True, is_sw_writable=True)
        with self.subTest(msg='field: openenoc_csr.switch1.forwarding_table.entry[7].config.enabled'):
            self._single_field_property_test(fut=self.dut.switch1.forwarding_table.entry[7].config.enabled, lsb=0, msb=0, low=0, high=0, is_volatile=True, default=None,
                                             rdl_name="csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled",
                                             rdl_desc="Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.",
                                             inst_name='enabled',
                                             parent_full_inst_name='openenoc_csr.switch1.forwarding_table.entry[7].config')
            self._single_int_field_read_and_write_test(fut=self.dut.switch1.forwarding_table.entry[7].config.enabled, is_sw_readable=True, is_sw_writable=True)

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
        with self.subTest(msg='regfile: openenoc_csr.switch1.forwarding_table'):
            self._single_regfile_property_test(dut=self.dut.switch1.forwarding_table,
                                               size=128,
                                               rdl_name="csr.switch1.forwarding_table",
                                               rdl_desc="Forwarding table used to map MAC addresses to output interface selections for frame forwarding.",
                                               inst_name='forwarding_table',
                                               parent_full_inst_name='openenoc_csr.switch1')
            self._test_regfile_iterators(dut=self.dut.switch1.forwarding_table,
                                         writeable_registers=NodeIterators(),
                                         readable_registers=NodeIterators(),
                                         sections=NodeIterators(('entry', [8]),))
        with self.subTest(msg='regfile: openenoc_csr.switch1.forwarding_table.entry[0]'):
            self._single_regfile_property_test(dut=self.dut.switch1.forwarding_table.entry[0],
                                               size=16,
                                               rdl_name="csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1]",
                                               rdl_desc="Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.",
                                               inst_name='entry[0]',
                                               parent_full_inst_name='openenoc_csr.switch1.forwarding_table')
            self._test_regfile_iterators(dut=self.dut.switch1.forwarding_table.entry[0],
                                         writeable_registers=NodeIterators('macaddr','iface','config',),
                                         readable_registers=NodeIterators('macaddr','iface','config',),
                                         sections=NodeIterators())
        with self.subTest(msg='regfile: openenoc_csr.switch1.forwarding_table.entry[1]'):
            self._single_regfile_property_test(dut=self.dut.switch1.forwarding_table.entry[1],
                                               size=16,
                                               rdl_name="csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1]",
                                               rdl_desc="Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.",
                                               inst_name='entry[1]',
                                               parent_full_inst_name='openenoc_csr.switch1.forwarding_table')
            self._test_regfile_iterators(dut=self.dut.switch1.forwarding_table.entry[1],
                                         writeable_registers=NodeIterators('macaddr','iface','config',),
                                         readable_registers=NodeIterators('macaddr','iface','config',),
                                         sections=NodeIterators())
        with self.subTest(msg='regfile: openenoc_csr.switch1.forwarding_table.entry[2]'):
            self._single_regfile_property_test(dut=self.dut.switch1.forwarding_table.entry[2],
                                               size=16,
                                               rdl_name="csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1]",
                                               rdl_desc="Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.",
                                               inst_name='entry[2]',
                                               parent_full_inst_name='openenoc_csr.switch1.forwarding_table')
            self._test_regfile_iterators(dut=self.dut.switch1.forwarding_table.entry[2],
                                         writeable_registers=NodeIterators('macaddr','iface','config',),
                                         readable_registers=NodeIterators('macaddr','iface','config',),
                                         sections=NodeIterators())
        with self.subTest(msg='regfile: openenoc_csr.switch1.forwarding_table.entry[3]'):
            self._single_regfile_property_test(dut=self.dut.switch1.forwarding_table.entry[3],
                                               size=16,
                                               rdl_name="csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1]",
                                               rdl_desc="Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.",
                                               inst_name='entry[3]',
                                               parent_full_inst_name='openenoc_csr.switch1.forwarding_table')
            self._test_regfile_iterators(dut=self.dut.switch1.forwarding_table.entry[3],
                                         writeable_registers=NodeIterators('macaddr','iface','config',),
                                         readable_registers=NodeIterators('macaddr','iface','config',),
                                         sections=NodeIterators())
        with self.subTest(msg='regfile: openenoc_csr.switch1.forwarding_table.entry[4]'):
            self._single_regfile_property_test(dut=self.dut.switch1.forwarding_table.entry[4],
                                               size=16,
                                               rdl_name="csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1]",
                                               rdl_desc="Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.",
                                               inst_name='entry[4]',
                                               parent_full_inst_name='openenoc_csr.switch1.forwarding_table')
            self._test_regfile_iterators(dut=self.dut.switch1.forwarding_table.entry[4],
                                         writeable_registers=NodeIterators('macaddr','iface','config',),
                                         readable_registers=NodeIterators('macaddr','iface','config',),
                                         sections=NodeIterators())
        with self.subTest(msg='regfile: openenoc_csr.switch1.forwarding_table.entry[5]'):
            self._single_regfile_property_test(dut=self.dut.switch1.forwarding_table.entry[5],
                                               size=16,
                                               rdl_name="csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1]",
                                               rdl_desc="Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.",
                                               inst_name='entry[5]',
                                               parent_full_inst_name='openenoc_csr.switch1.forwarding_table')
            self._test_regfile_iterators(dut=self.dut.switch1.forwarding_table.entry[5],
                                         writeable_registers=NodeIterators('macaddr','iface','config',),
                                         readable_registers=NodeIterators('macaddr','iface','config',),
                                         sections=NodeIterators())
        with self.subTest(msg='regfile: openenoc_csr.switch1.forwarding_table.entry[6]'):
            self._single_regfile_property_test(dut=self.dut.switch1.forwarding_table.entry[6],
                                               size=16,
                                               rdl_name="csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1]",
                                               rdl_desc="Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.",
                                               inst_name='entry[6]',
                                               parent_full_inst_name='openenoc_csr.switch1.forwarding_table')
            self._test_regfile_iterators(dut=self.dut.switch1.forwarding_table.entry[6],
                                         writeable_registers=NodeIterators('macaddr','iface','config',),
                                         readable_registers=NodeIterators('macaddr','iface','config',),
                                         sections=NodeIterators())
        with self.subTest(msg='regfile: openenoc_csr.switch1.forwarding_table.entry[7]'):
            self._single_regfile_property_test(dut=self.dut.switch1.forwarding_table.entry[7],
                                               size=16,
                                               rdl_name="csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1]",
                                               rdl_desc="Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.",
                                               inst_name='entry[7]',
                                               parent_full_inst_name='openenoc_csr.switch1.forwarding_table')
            self._test_regfile_iterators(dut=self.dut.switch1.forwarding_table.entry[7],
                                         writeable_registers=NodeIterators('macaddr','iface','config',),
                                         readable_registers=NodeIterators('macaddr','iface','config',),
                                         sections=NodeIterators())
        

    

    def test_array_slicing(self) -> None:
        """
        Check slicing into array
        """
        full_slice:NodeArray
        
        with self.subTest(msg='hidden_node: openenoc_csr.switch1.forwarding_table.entry[]'):
            
            full_slice = self.dut.switch1.forwarding_table.get_child_by_system_rdl_name('entry')
            
            self.assertCountEqual(iter(full_slice[:]), iter(full_slice))
        



class openenoc_csr_switch1_block_access(openenoc_csr_TestCase_BlockAccess): # type: ignore[valid-type,misc]
    """
    tests for all the block access methods
    """

    

    def test_register_array_context_manager(self) -> None:
        """
        Walk the register map and check that register map context managers work correctly
        """
        

class openenoc_csr_switch1_alt_block_access(openenoc_csr_TestCase_AltBlockAccess): # type: ignore[valid-type,misc]
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