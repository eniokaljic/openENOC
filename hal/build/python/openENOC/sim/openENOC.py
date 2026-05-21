


"""
Python Wrapper for the openENOC register model

This code was generated from the PeakRDL-python package version 3.1.1

"""





from typing import Union

from ..sim_lib.register import Register, MemoryRegister
from ..sim_lib.memory import Memory
from ..sim_lib.simulator import MemoryEntry
from ..sim_lib.field import FieldDefinition, FieldType

from ..sim_lib.simulator import Simulator

class openENOC_simulator_cls(Simulator):

    def _build_registers(self) -> dict[int, Union[list[Union[MemoryRegister, Register]], Union[MemoryRegister, Register]]]:
        return {
            536870912 : 
    Register(width=32, full_inst_name='openENOC.csr.test_reg', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='test_field', field_type=FieldType.READWRITE),
                                                ]),
        }

    def _build_memories(self) -> list[MemoryEntry]:
        return [
            MemoryEntry(start_address=0,
                        end_address=32767,
                        memory=Memory(width=32,
                                      length=8192,
                                      full_inst_name='openENOC.imem',
                                      default_value=0)),
            MemoryEntry(start_address=268435456,
                        end_address=268468223,
                        memory=Memory(width=32,
                                      length=8192,
                                      full_inst_name='openENOC.dmem',
                                      default_value=0)),
        ]

if __name__ == '__main__':
    pass
