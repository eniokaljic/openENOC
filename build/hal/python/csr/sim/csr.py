


"""
Python Wrapper for the csr register model

This code was generated from the PeakRDL-python package version 3.1.1

"""





from typing import Union

from ..sim_lib.register import Register, MemoryRegister
from ..sim_lib.memory import Memory
from ..sim_lib.simulator import MemoryEntry
from ..sim_lib.field import FieldDefinition, FieldType

from ..sim_lib.simulator import Simulator

class csr_simulator_cls(Simulator):

    def _build_registers(self) -> dict[int, Union[list[Union[MemoryRegister, Register]], Union[MemoryRegister, Register]]]:
        return {
            0 : 
    Register(width=32, full_inst_name='csr.test_reg', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='test_field', field_type=FieldType.READWRITE),
                                                ]),
            4 : 
    Register(width=32, full_inst_name='csr.regB', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='f0', field_type=FieldType.READWRITE),FieldDefinition(high=15, low=8, msb=15, lsb=8, inst_name='f1', field_type=FieldType.READWRITE),FieldDefinition(high=23, low=16, msb=23, lsb=16, inst_name='f2', field_type=FieldType.READWRITE),FieldDefinition(high=31, low=24, msb=31, lsb=24, inst_name='f3', field_type=FieldType.READWRITE),
                                                ]),
            256 : 
    Register(width=32, full_inst_name='csr.switch1.info', readable=True, writable=False,
                                         fields=[FieldDefinition(high=15, low=0, msb=15, lsb=0, inst_name='table_depth', field_type=FieldType.READONLY),FieldDefinition(high=21, low=16, msb=21, lsb=16, inst_name='num_of_interfaces', field_type=FieldType.READONLY),
                                                ]),
            260 : 
    Register(width=32, full_inst_name='csr.switch1.forwarding_control', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='operation_mode', field_type=FieldType.READWRITE),FieldDefinition(high=7, low=7, msb=7, lsb=7, inst_name='pause_request', field_type=FieldType.READWRITE),FieldDefinition(high=15, low=15, msb=15, lsb=15, inst_name='pause_done', field_type=FieldType.READONLY),
                                                ]),
            264 : 
    Register(width=32, full_inst_name='csr.switch1.default_forwarding', readable=True, writable=True,
                                         fields=[FieldDefinition(high=3, low=0, msb=3, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            384 : 
    Register(width=64, full_inst_name='csr.switch1.forwarding_table.entry[0].macaddr', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            392 : 
    Register(width=32, full_inst_name='csr.switch1.forwarding_table.entry[0].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=3, low=0, msb=3, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            396 : 
    Register(width=32, full_inst_name='csr.switch1.forwarding_table.entry[0].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            400 : 
    Register(width=64, full_inst_name='csr.switch1.forwarding_table.entry[1].macaddr', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            408 : 
    Register(width=32, full_inst_name='csr.switch1.forwarding_table.entry[1].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=3, low=0, msb=3, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            412 : 
    Register(width=32, full_inst_name='csr.switch1.forwarding_table.entry[1].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            416 : 
    Register(width=64, full_inst_name='csr.switch1.forwarding_table.entry[2].macaddr', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            424 : 
    Register(width=32, full_inst_name='csr.switch1.forwarding_table.entry[2].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=3, low=0, msb=3, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            428 : 
    Register(width=32, full_inst_name='csr.switch1.forwarding_table.entry[2].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            432 : 
    Register(width=64, full_inst_name='csr.switch1.forwarding_table.entry[3].macaddr', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            440 : 
    Register(width=32, full_inst_name='csr.switch1.forwarding_table.entry[3].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=3, low=0, msb=3, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            444 : 
    Register(width=32, full_inst_name='csr.switch1.forwarding_table.entry[3].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            448 : 
    Register(width=64, full_inst_name='csr.switch1.forwarding_table.entry[4].macaddr', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            456 : 
    Register(width=32, full_inst_name='csr.switch1.forwarding_table.entry[4].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=3, low=0, msb=3, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            460 : 
    Register(width=32, full_inst_name='csr.switch1.forwarding_table.entry[4].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            464 : 
    Register(width=64, full_inst_name='csr.switch1.forwarding_table.entry[5].macaddr', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            472 : 
    Register(width=32, full_inst_name='csr.switch1.forwarding_table.entry[5].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=3, low=0, msb=3, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            476 : 
    Register(width=32, full_inst_name='csr.switch1.forwarding_table.entry[5].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            480 : 
    Register(width=64, full_inst_name='csr.switch1.forwarding_table.entry[6].macaddr', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            488 : 
    Register(width=32, full_inst_name='csr.switch1.forwarding_table.entry[6].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=3, low=0, msb=3, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            492 : 
    Register(width=32, full_inst_name='csr.switch1.forwarding_table.entry[6].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            496 : 
    Register(width=64, full_inst_name='csr.switch1.forwarding_table.entry[7].macaddr', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            504 : 
    Register(width=32, full_inst_name='csr.switch1.forwarding_table.entry[7].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=3, low=0, msb=3, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            508 : 
    Register(width=32, full_inst_name='csr.switch1.forwarding_table.entry[7].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            1024 : 
    Register(width=32, full_inst_name='csr.switch2.info', readable=True, writable=False,
                                         fields=[FieldDefinition(high=15, low=0, msb=15, lsb=0, inst_name='table_depth', field_type=FieldType.READONLY),FieldDefinition(high=21, low=16, msb=21, lsb=16, inst_name='num_of_interfaces', field_type=FieldType.READONLY),
                                                ]),
            1028 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_control', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='operation_mode', field_type=FieldType.READWRITE),FieldDefinition(high=7, low=7, msb=7, lsb=7, inst_name='pause_request', field_type=FieldType.READWRITE),FieldDefinition(high=15, low=15, msb=15, lsb=15, inst_name='pause_done', field_type=FieldType.READONLY),
                                                ]),
            1032 : 
    Register(width=32, full_inst_name='csr.switch2.default_forwarding', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            1536 : 
    Register(width=64, full_inst_name='csr.switch2.forwarding_table.entry[0].macaddr', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            1544 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_table.entry[0].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            1548 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_table.entry[0].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            1552 : 
    Register(width=64, full_inst_name='csr.switch2.forwarding_table.entry[1].macaddr', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            1560 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_table.entry[1].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            1564 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_table.entry[1].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            1568 : 
    Register(width=64, full_inst_name='csr.switch2.forwarding_table.entry[2].macaddr', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            1576 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_table.entry[2].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            1580 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_table.entry[2].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            1584 : 
    Register(width=64, full_inst_name='csr.switch2.forwarding_table.entry[3].macaddr', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            1592 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_table.entry[3].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            1596 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_table.entry[3].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            1600 : 
    Register(width=64, full_inst_name='csr.switch2.forwarding_table.entry[4].macaddr', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            1608 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_table.entry[4].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            1612 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_table.entry[4].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            1616 : 
    Register(width=64, full_inst_name='csr.switch2.forwarding_table.entry[5].macaddr', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            1624 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_table.entry[5].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            1628 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_table.entry[5].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            1632 : 
    Register(width=64, full_inst_name='csr.switch2.forwarding_table.entry[6].macaddr', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            1640 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_table.entry[6].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            1644 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_table.entry[6].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            1648 : 
    Register(width=64, full_inst_name='csr.switch2.forwarding_table.entry[7].macaddr', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            1656 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_table.entry[7].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            1660 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_table.entry[7].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            1664 : 
    Register(width=64, full_inst_name='csr.switch2.forwarding_table.entry[8].macaddr', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            1672 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_table.entry[8].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            1676 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_table.entry[8].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            1680 : 
    Register(width=64, full_inst_name='csr.switch2.forwarding_table.entry[9].macaddr', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            1688 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_table.entry[9].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            1692 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_table.entry[9].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            1696 : 
    Register(width=64, full_inst_name='csr.switch2.forwarding_table.entry[10].macaddr', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            1704 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_table.entry[10].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            1708 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_table.entry[10].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            1712 : 
    Register(width=64, full_inst_name='csr.switch2.forwarding_table.entry[11].macaddr', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            1720 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_table.entry[11].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            1724 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_table.entry[11].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            1728 : 
    Register(width=64, full_inst_name='csr.switch2.forwarding_table.entry[12].macaddr', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            1736 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_table.entry[12].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            1740 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_table.entry[12].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            1744 : 
    Register(width=64, full_inst_name='csr.switch2.forwarding_table.entry[13].macaddr', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            1752 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_table.entry[13].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            1756 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_table.entry[13].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            1760 : 
    Register(width=64, full_inst_name='csr.switch2.forwarding_table.entry[14].macaddr', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            1768 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_table.entry[14].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            1772 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_table.entry[14].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            1776 : 
    Register(width=64, full_inst_name='csr.switch2.forwarding_table.entry[15].macaddr', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            1784 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_table.entry[15].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            1788 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_table.entry[15].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            1792 : 
    Register(width=64, full_inst_name='csr.switch2.forwarding_table.entry[16].macaddr', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            1800 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_table.entry[16].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            1804 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_table.entry[16].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            1808 : 
    Register(width=64, full_inst_name='csr.switch2.forwarding_table.entry[17].macaddr', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            1816 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_table.entry[17].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            1820 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_table.entry[17].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            1824 : 
    Register(width=64, full_inst_name='csr.switch2.forwarding_table.entry[18].macaddr', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            1832 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_table.entry[18].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            1836 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_table.entry[18].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            1840 : 
    Register(width=64, full_inst_name='csr.switch2.forwarding_table.entry[19].macaddr', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            1848 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_table.entry[19].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            1852 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_table.entry[19].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            1856 : 
    Register(width=64, full_inst_name='csr.switch2.forwarding_table.entry[20].macaddr', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            1864 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_table.entry[20].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            1868 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_table.entry[20].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            1872 : 
    Register(width=64, full_inst_name='csr.switch2.forwarding_table.entry[21].macaddr', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            1880 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_table.entry[21].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            1884 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_table.entry[21].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            1888 : 
    Register(width=64, full_inst_name='csr.switch2.forwarding_table.entry[22].macaddr', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            1896 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_table.entry[22].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            1900 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_table.entry[22].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            1904 : 
    Register(width=64, full_inst_name='csr.switch2.forwarding_table.entry[23].macaddr', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            1912 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_table.entry[23].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            1916 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_table.entry[23].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            1920 : 
    Register(width=64, full_inst_name='csr.switch2.forwarding_table.entry[24].macaddr', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            1928 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_table.entry[24].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            1932 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_table.entry[24].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            1936 : 
    Register(width=64, full_inst_name='csr.switch2.forwarding_table.entry[25].macaddr', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            1944 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_table.entry[25].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            1948 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_table.entry[25].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            1952 : 
    Register(width=64, full_inst_name='csr.switch2.forwarding_table.entry[26].macaddr', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            1960 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_table.entry[26].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            1964 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_table.entry[26].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            1968 : 
    Register(width=64, full_inst_name='csr.switch2.forwarding_table.entry[27].macaddr', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            1976 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_table.entry[27].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            1980 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_table.entry[27].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            1984 : 
    Register(width=64, full_inst_name='csr.switch2.forwarding_table.entry[28].macaddr', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            1992 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_table.entry[28].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            1996 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_table.entry[28].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            2000 : 
    Register(width=64, full_inst_name='csr.switch2.forwarding_table.entry[29].macaddr', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            2008 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_table.entry[29].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            2012 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_table.entry[29].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            2016 : 
    Register(width=64, full_inst_name='csr.switch2.forwarding_table.entry[30].macaddr', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            2024 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_table.entry[30].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            2028 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_table.entry[30].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            2032 : 
    Register(width=64, full_inst_name='csr.switch2.forwarding_table.entry[31].macaddr', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            2040 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_table.entry[31].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            2044 : 
    Register(width=32, full_inst_name='csr.switch2.forwarding_table.entry[31].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
        }

    def _build_memories(self) -> list[MemoryEntry]:
        return [
        ]

if __name__ == '__main__':
    pass
