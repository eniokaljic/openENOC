


"""
Python Wrapper for the csr register model

This code was generated from the PeakRDL-python package version 3.1.2

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
            2048 : 
    Register(width=64, full_inst_name='csr.endpoint_interface.info', readable=True, writable=False,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='rmem_total_depth', field_type=FieldType.READONLY),FieldDefinition(high=63, low=32, msb=63, lsb=32, inst_name='num_of_peers', field_type=FieldType.READONLY),
                                                ]),
            2056 : 
    Register(width=64, full_inst_name='csr.endpoint_interface.config.mac_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            2080 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.axis_if.source.data', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='tdata', field_type=FieldType.READWRITE),
                                                ]),
            2084 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.axis_if.source.control', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='tvalid', field_type=FieldType.READWRITE),FieldDefinition(high=8, low=8, msb=8, lsb=8, inst_name='tlast', field_type=FieldType.READWRITE),FieldDefinition(high=19, low=16, msb=19, lsb=16, inst_name='tkeep', field_type=FieldType.READWRITE),
                                                ]),
            2088 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.axis_if.source.status', readable=True, writable=False,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='tready', field_type=FieldType.READONLY),
                                                ]),
            2096 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.axis_if.sink.data', readable=True, writable=False,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='tdata', field_type=FieldType.READONLY),
                                                ]),
            2100 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.axis_if.sink.control', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='tready', field_type=FieldType.READWRITE),
                                                ]),
            2104 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.axis_if.sink.status', readable=True, writable=False,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='tvalid', field_type=FieldType.READONLY),FieldDefinition(high=8, low=8, msb=8, lsb=8, inst_name='tlast', field_type=FieldType.READONLY),FieldDefinition(high=19, low=16, msb=19, lsb=16, inst_name='tkeep', field_type=FieldType.READONLY),
                                                ]),
            2176 : 
    Register(width=64, full_inst_name='csr.endpoint_interface.peers.entry[0].mac_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            2184 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.peers.entry[0].rmem_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='offset', field_type=FieldType.READWRITE),
                                                ]),
            2188 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.peers.entry[0].local_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='base', field_type=FieldType.READWRITE),
                                                ]),
            2192 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.peers.entry[0].remote_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='base', field_type=FieldType.READWRITE),
                                                ]),
            2196 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.peers.entry[0].size', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='bytes', field_type=FieldType.READWRITE),
                                                ]),
            2200 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.peers.entry[0].dma', readable=True, writable=True,
                                         fields=[FieldDefinition(high=1, low=0, msb=1, lsb=0, inst_name='mode', field_type=FieldType.READWRITE),FieldDefinition(high=8, low=8, msb=8, lsb=8, inst_name='request', field_type=FieldType.READWRITE),FieldDefinition(high=16, low=16, msb=16, lsb=16, inst_name='idle', field_type=FieldType.READONLY),FieldDefinition(high=24, low=24, msb=24, lsb=24, inst_name='done', field_type=FieldType.READONLY),FieldDefinition(high=25, low=25, msb=25, lsb=25, inst_name='error', field_type=FieldType.READONLY),
                                                ]),
            2204 : 
    Register(width=64, full_inst_name='csr.endpoint_interface.peers.entry[1].mac_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            2212 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.peers.entry[1].rmem_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='offset', field_type=FieldType.READWRITE),
                                                ]),
            2216 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.peers.entry[1].local_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='base', field_type=FieldType.READWRITE),
                                                ]),
            2220 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.peers.entry[1].remote_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='base', field_type=FieldType.READWRITE),
                                                ]),
            2224 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.peers.entry[1].size', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='bytes', field_type=FieldType.READWRITE),
                                                ]),
            2228 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.peers.entry[1].dma', readable=True, writable=True,
                                         fields=[FieldDefinition(high=1, low=0, msb=1, lsb=0, inst_name='mode', field_type=FieldType.READWRITE),FieldDefinition(high=8, low=8, msb=8, lsb=8, inst_name='request', field_type=FieldType.READWRITE),FieldDefinition(high=16, low=16, msb=16, lsb=16, inst_name='idle', field_type=FieldType.READONLY),FieldDefinition(high=24, low=24, msb=24, lsb=24, inst_name='done', field_type=FieldType.READONLY),FieldDefinition(high=25, low=25, msb=25, lsb=25, inst_name='error', field_type=FieldType.READONLY),
                                                ]),
            2232 : 
    Register(width=64, full_inst_name='csr.endpoint_interface.peers.entry[2].mac_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            2240 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.peers.entry[2].rmem_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='offset', field_type=FieldType.READWRITE),
                                                ]),
            2244 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.peers.entry[2].local_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='base', field_type=FieldType.READWRITE),
                                                ]),
            2248 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.peers.entry[2].remote_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='base', field_type=FieldType.READWRITE),
                                                ]),
            2252 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.peers.entry[2].size', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='bytes', field_type=FieldType.READWRITE),
                                                ]),
            2256 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.peers.entry[2].dma', readable=True, writable=True,
                                         fields=[FieldDefinition(high=1, low=0, msb=1, lsb=0, inst_name='mode', field_type=FieldType.READWRITE),FieldDefinition(high=8, low=8, msb=8, lsb=8, inst_name='request', field_type=FieldType.READWRITE),FieldDefinition(high=16, low=16, msb=16, lsb=16, inst_name='idle', field_type=FieldType.READONLY),FieldDefinition(high=24, low=24, msb=24, lsb=24, inst_name='done', field_type=FieldType.READONLY),FieldDefinition(high=25, low=25, msb=25, lsb=25, inst_name='error', field_type=FieldType.READONLY),
                                                ]),
            2260 : 
    Register(width=64, full_inst_name='csr.endpoint_interface.peers.entry[3].mac_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            2268 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.peers.entry[3].rmem_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='offset', field_type=FieldType.READWRITE),
                                                ]),
            2272 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.peers.entry[3].local_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='base', field_type=FieldType.READWRITE),
                                                ]),
            2276 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.peers.entry[3].remote_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='base', field_type=FieldType.READWRITE),
                                                ]),
            2280 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.peers.entry[3].size', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='bytes', field_type=FieldType.READWRITE),
                                                ]),
            2284 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.peers.entry[3].dma', readable=True, writable=True,
                                         fields=[FieldDefinition(high=1, low=0, msb=1, lsb=0, inst_name='mode', field_type=FieldType.READWRITE),FieldDefinition(high=8, low=8, msb=8, lsb=8, inst_name='request', field_type=FieldType.READWRITE),FieldDefinition(high=16, low=16, msb=16, lsb=16, inst_name='idle', field_type=FieldType.READONLY),FieldDefinition(high=24, low=24, msb=24, lsb=24, inst_name='done', field_type=FieldType.READONLY),FieldDefinition(high=25, low=25, msb=25, lsb=25, inst_name='error', field_type=FieldType.READONLY),
                                                ]),
            3072 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[0]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3076 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[1]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3080 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[2]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3084 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[3]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3088 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[4]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3092 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[5]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3096 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[6]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3100 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[7]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3104 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[8]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3108 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[9]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3112 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[10]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3116 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[11]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3120 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[12]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3124 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[13]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3128 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[14]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3132 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[15]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3136 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[16]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3140 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[17]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3144 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[18]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3148 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[19]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3152 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[20]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3156 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[21]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3160 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[22]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3164 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[23]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3168 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[24]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3172 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[25]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3176 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[26]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3180 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[27]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3184 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[28]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3188 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[29]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3192 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[30]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3196 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[31]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3200 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[32]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3204 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[33]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3208 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[34]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3212 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[35]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3216 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[36]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3220 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[37]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3224 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[38]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3228 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[39]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3232 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[40]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3236 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[41]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3240 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[42]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3244 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[43]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3248 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[44]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3252 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[45]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3256 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[46]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3260 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[47]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3264 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[48]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3268 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[49]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3272 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[50]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3276 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[51]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3280 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[52]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3284 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[53]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3288 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[54]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3292 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[55]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3296 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[56]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3300 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[57]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3304 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[58]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3308 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[59]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3312 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[60]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3316 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[61]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3320 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[62]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3324 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[63]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3328 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[64]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3332 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[65]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3336 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[66]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3340 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[67]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3344 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[68]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3348 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[69]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3352 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[70]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3356 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[71]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3360 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[72]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3364 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[73]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3368 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[74]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3372 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[75]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3376 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[76]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3380 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[77]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3384 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[78]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3388 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[79]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3392 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[80]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3396 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[81]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3400 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[82]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3404 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[83]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3408 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[84]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3412 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[85]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3416 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[86]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3420 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[87]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3424 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[88]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3428 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[89]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3432 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[90]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3436 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[91]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3440 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[92]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3444 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[93]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3448 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[94]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3452 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[95]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3456 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[96]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3460 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[97]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3464 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[98]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3468 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[99]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3472 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[100]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3476 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[101]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3480 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[102]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3484 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[103]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3488 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[104]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3492 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[105]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3496 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[106]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3500 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[107]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3504 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[108]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3508 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[109]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3512 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[110]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3516 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[111]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3520 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[112]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3524 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[113]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3528 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[114]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3532 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[115]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3536 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[116]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3540 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[117]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3544 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[118]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3548 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[119]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3552 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[120]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3556 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[121]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3560 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[122]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3564 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[123]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3568 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[124]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3572 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[125]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3576 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[126]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3580 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[127]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3584 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[128]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3588 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[129]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3592 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[130]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3596 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[131]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3600 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[132]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3604 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[133]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3608 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[134]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3612 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[135]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3616 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[136]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3620 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[137]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3624 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[138]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3628 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[139]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3632 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[140]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3636 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[141]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3640 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[142]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3644 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[143]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3648 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[144]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3652 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[145]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3656 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[146]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3660 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[147]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3664 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[148]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3668 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[149]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3672 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[150]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3676 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[151]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3680 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[152]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3684 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[153]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3688 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[154]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3692 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[155]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3696 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[156]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3700 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[157]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3704 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[158]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3708 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[159]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3712 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[160]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3716 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[161]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3720 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[162]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3724 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[163]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3728 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[164]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3732 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[165]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3736 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[166]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3740 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[167]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3744 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[168]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3748 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[169]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3752 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[170]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3756 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[171]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3760 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[172]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3764 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[173]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3768 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[174]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3772 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[175]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3776 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[176]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3780 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[177]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3784 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[178]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3788 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[179]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3792 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[180]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3796 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[181]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3800 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[182]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3804 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[183]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3808 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[184]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3812 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[185]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3816 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[186]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3820 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[187]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3824 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[188]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3828 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[189]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3832 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[190]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3836 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[191]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3840 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[192]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3844 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[193]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3848 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[194]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3852 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[195]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3856 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[196]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3860 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[197]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3864 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[198]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3868 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[199]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3872 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[200]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3876 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[201]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3880 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[202]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3884 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[203]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3888 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[204]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3892 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[205]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3896 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[206]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3900 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[207]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3904 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[208]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3908 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[209]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3912 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[210]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3916 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[211]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3920 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[212]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3924 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[213]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3928 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[214]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3932 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[215]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3936 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[216]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3940 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[217]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3944 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[218]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3948 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[219]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3952 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[220]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3956 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[221]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3960 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[222]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3964 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[223]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3968 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[224]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3972 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[225]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3976 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[226]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3980 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[227]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3984 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[228]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3988 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[229]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3992 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[230]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            3996 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[231]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            4000 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[232]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            4004 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[233]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            4008 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[234]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            4012 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[235]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            4016 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[236]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            4020 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[237]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            4024 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[238]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            4028 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[239]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            4032 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[240]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            4036 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[241]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            4040 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[242]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            4044 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[243]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            4048 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[244]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            4052 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[245]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            4056 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[246]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            4060 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[247]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            4064 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[248]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            4068 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[249]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            4072 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[250]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            4076 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[251]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            4080 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[252]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            4084 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[253]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            4088 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[254]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            4092 : 
    Register(width=32, full_inst_name='csr.endpoint_interface.rmem.word[255]', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='data', field_type=FieldType.READWRITE),
                                                ]),
            4096 : 
    Register(width=32, full_inst_name='csr.switch_interface.info', readable=True, writable=False,
                                         fields=[FieldDefinition(high=15, low=0, msb=15, lsb=0, inst_name='table_depth', field_type=FieldType.READONLY),FieldDefinition(high=21, low=16, msb=21, lsb=16, inst_name='num_of_interfaces', field_type=FieldType.READONLY),
                                                ]),
            4100 : 
    Register(width=32, full_inst_name='csr.switch_interface.forwarding_control', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='operation_mode', field_type=FieldType.READWRITE),FieldDefinition(high=7, low=7, msb=7, lsb=7, inst_name='pause_request', field_type=FieldType.READWRITE),FieldDefinition(high=15, low=15, msb=15, lsb=15, inst_name='pause_done', field_type=FieldType.READONLY),
                                                ]),
            4104 : 
    Register(width=32, full_inst_name='csr.switch_interface.default_forwarding', readable=True, writable=True,
                                         fields=[FieldDefinition(high=3, low=0, msb=3, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            4224 : 
    Register(width=64, full_inst_name='csr.switch_interface.forwarding_table.entry[0].mac_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            4232 : 
    Register(width=32, full_inst_name='csr.switch_interface.forwarding_table.entry[0].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=3, low=0, msb=3, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            4236 : 
    Register(width=32, full_inst_name='csr.switch_interface.forwarding_table.entry[0].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            4240 : 
    Register(width=64, full_inst_name='csr.switch_interface.forwarding_table.entry[1].mac_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            4248 : 
    Register(width=32, full_inst_name='csr.switch_interface.forwarding_table.entry[1].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=3, low=0, msb=3, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            4252 : 
    Register(width=32, full_inst_name='csr.switch_interface.forwarding_table.entry[1].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            4256 : 
    Register(width=64, full_inst_name='csr.switch_interface.forwarding_table.entry[2].mac_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            4264 : 
    Register(width=32, full_inst_name='csr.switch_interface.forwarding_table.entry[2].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=3, low=0, msb=3, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            4268 : 
    Register(width=32, full_inst_name='csr.switch_interface.forwarding_table.entry[2].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            4272 : 
    Register(width=64, full_inst_name='csr.switch_interface.forwarding_table.entry[3].mac_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            4280 : 
    Register(width=32, full_inst_name='csr.switch_interface.forwarding_table.entry[3].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=3, low=0, msb=3, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            4284 : 
    Register(width=32, full_inst_name='csr.switch_interface.forwarding_table.entry[3].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            4288 : 
    Register(width=64, full_inst_name='csr.switch_interface.forwarding_table.entry[4].mac_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            4296 : 
    Register(width=32, full_inst_name='csr.switch_interface.forwarding_table.entry[4].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=3, low=0, msb=3, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            4300 : 
    Register(width=32, full_inst_name='csr.switch_interface.forwarding_table.entry[4].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            4304 : 
    Register(width=64, full_inst_name='csr.switch_interface.forwarding_table.entry[5].mac_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            4312 : 
    Register(width=32, full_inst_name='csr.switch_interface.forwarding_table.entry[5].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=3, low=0, msb=3, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            4316 : 
    Register(width=32, full_inst_name='csr.switch_interface.forwarding_table.entry[5].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            4320 : 
    Register(width=64, full_inst_name='csr.switch_interface.forwarding_table.entry[6].mac_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            4328 : 
    Register(width=32, full_inst_name='csr.switch_interface.forwarding_table.entry[6].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=3, low=0, msb=3, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            4332 : 
    Register(width=32, full_inst_name='csr.switch_interface.forwarding_table.entry[6].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            4336 : 
    Register(width=64, full_inst_name='csr.switch_interface.forwarding_table.entry[7].mac_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            4344 : 
    Register(width=32, full_inst_name='csr.switch_interface.forwarding_table.entry[7].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=3, low=0, msb=3, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            4348 : 
    Register(width=32, full_inst_name='csr.switch_interface.forwarding_table.entry[7].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
        }

    def _build_memories(self) -> list[MemoryEntry]:
        return [
        ]

if __name__ == '__main__':
    pass
