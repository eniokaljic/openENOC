


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
        }

    def _build_memories(self) -> list[MemoryEntry]:
        return [
        ]

if __name__ == '__main__':
    pass
