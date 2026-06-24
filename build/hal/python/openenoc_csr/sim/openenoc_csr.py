


"""
Python Wrapper for the openenoc_csr register model

This code was generated from the PeakRDL-python package version 3.1.2

"""





from typing import Union

from ..sim_lib.register import Register, MemoryRegister
from ..sim_lib.memory import Memory
from ..sim_lib.simulator import MemoryEntry
from ..sim_lib.field import FieldDefinition, FieldType

from ..sim_lib.simulator import Simulator

class openenoc_csr_simulator_cls(Simulator):

    def _build_registers(self) -> dict[int, Union[list[Union[MemoryRegister, Register]], Union[MemoryRegister, Register]]]:
        return {
            0 : 
    Register(width=32, full_inst_name='openenoc_csr.test_reg', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='test_field', field_type=FieldType.READWRITE),
                                                ]),
            4 : 
    Register(width=32, full_inst_name='openenoc_csr.regB', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='f0', field_type=FieldType.READWRITE),FieldDefinition(high=15, low=8, msb=15, lsb=8, inst_name='f1', field_type=FieldType.READWRITE),FieldDefinition(high=23, low=16, msb=23, lsb=16, inst_name='f2', field_type=FieldType.READWRITE),FieldDefinition(high=31, low=24, msb=31, lsb=24, inst_name='f3', field_type=FieldType.READWRITE),
                                                ]),
            2048 : 
    Register(width=64, full_inst_name='openenoc_csr.endpoint1.info', readable=True, writable=False,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='rmem_total_depth', field_type=FieldType.READONLY),FieldDefinition(high=63, low=32, msb=63, lsb=32, inst_name='num_of_peers', field_type=FieldType.READONLY),
                                                ]),
            2056 : 
    Register(width=64, full_inst_name='openenoc_csr.endpoint1.config.mac_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            2080 : 
    Register(width=32, full_inst_name='openenoc_csr.endpoint1.axis_if.source.data', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='tdata', field_type=FieldType.READWRITE),
                                                ]),
            2084 : 
    Register(width=32, full_inst_name='openenoc_csr.endpoint1.axis_if.source.control', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='tvalid', field_type=FieldType.READWRITE),FieldDefinition(high=8, low=8, msb=8, lsb=8, inst_name='tlast', field_type=FieldType.READWRITE),
                                                ]),
            2088 : 
    Register(width=32, full_inst_name='openenoc_csr.endpoint1.axis_if.source.status', readable=True, writable=False,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='tready', field_type=FieldType.READONLY),
                                                ]),
            2096 : 
    Register(width=32, full_inst_name='openenoc_csr.endpoint1.axis_if.sink.data', readable=True, writable=False,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='tdata', field_type=FieldType.READONLY),
                                                ]),
            2100 : 
    Register(width=32, full_inst_name='openenoc_csr.endpoint1.axis_if.sink.control', readable=False, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='tready', field_type=FieldType.WRITEONLY),
                                                ]),
            2104 : 
    Register(width=32, full_inst_name='openenoc_csr.endpoint1.axis_if.sink.status', readable=True, writable=False,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='tvalid', field_type=FieldType.READONLY),FieldDefinition(high=8, low=8, msb=8, lsb=8, inst_name='tlast', field_type=FieldType.READONLY),
                                                ]),
            2176 : 
    Register(width=64, full_inst_name='openenoc_csr.endpoint1.peers.entry[0].mac_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            2184 : 
    Register(width=32, full_inst_name='openenoc_csr.endpoint1.peers.entry[0].rmem_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='offset', field_type=FieldType.READWRITE),
                                                ]),
            2188 : 
    Register(width=32, full_inst_name='openenoc_csr.endpoint1.peers.entry[0].local_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='base', field_type=FieldType.READWRITE),
                                                ]),
            2192 : 
    Register(width=32, full_inst_name='openenoc_csr.endpoint1.peers.entry[0].remote_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='base', field_type=FieldType.READWRITE),
                                                ]),
            2196 : 
    Register(width=32, full_inst_name='openenoc_csr.endpoint1.peers.entry[0].size', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='bytes', field_type=FieldType.READWRITE),
                                                ]),
            2200 : 
    Register(width=32, full_inst_name='openenoc_csr.endpoint1.peers.entry[0].dma', readable=True, writable=True,
                                         fields=[FieldDefinition(high=1, low=0, msb=1, lsb=0, inst_name='mode', field_type=FieldType.READWRITE),FieldDefinition(high=8, low=8, msb=8, lsb=8, inst_name='request', field_type=FieldType.READWRITE),FieldDefinition(high=16, low=16, msb=16, lsb=16, inst_name='idle', field_type=FieldType.READONLY),FieldDefinition(high=24, low=24, msb=24, lsb=24, inst_name='done', field_type=FieldType.READONLY),FieldDefinition(high=25, low=25, msb=25, lsb=25, inst_name='error', field_type=FieldType.READONLY),
                                                ]),
            2204 : 
    Register(width=64, full_inst_name='openenoc_csr.endpoint1.peers.entry[1].mac_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            2212 : 
    Register(width=32, full_inst_name='openenoc_csr.endpoint1.peers.entry[1].rmem_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='offset', field_type=FieldType.READWRITE),
                                                ]),
            2216 : 
    Register(width=32, full_inst_name='openenoc_csr.endpoint1.peers.entry[1].local_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='base', field_type=FieldType.READWRITE),
                                                ]),
            2220 : 
    Register(width=32, full_inst_name='openenoc_csr.endpoint1.peers.entry[1].remote_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='base', field_type=FieldType.READWRITE),
                                                ]),
            2224 : 
    Register(width=32, full_inst_name='openenoc_csr.endpoint1.peers.entry[1].size', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='bytes', field_type=FieldType.READWRITE),
                                                ]),
            2228 : 
    Register(width=32, full_inst_name='openenoc_csr.endpoint1.peers.entry[1].dma', readable=True, writable=True,
                                         fields=[FieldDefinition(high=1, low=0, msb=1, lsb=0, inst_name='mode', field_type=FieldType.READWRITE),FieldDefinition(high=8, low=8, msb=8, lsb=8, inst_name='request', field_type=FieldType.READWRITE),FieldDefinition(high=16, low=16, msb=16, lsb=16, inst_name='idle', field_type=FieldType.READONLY),FieldDefinition(high=24, low=24, msb=24, lsb=24, inst_name='done', field_type=FieldType.READONLY),FieldDefinition(high=25, low=25, msb=25, lsb=25, inst_name='error', field_type=FieldType.READONLY),
                                                ]),
            2232 : 
    Register(width=64, full_inst_name='openenoc_csr.endpoint1.peers.entry[2].mac_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            2240 : 
    Register(width=32, full_inst_name='openenoc_csr.endpoint1.peers.entry[2].rmem_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='offset', field_type=FieldType.READWRITE),
                                                ]),
            2244 : 
    Register(width=32, full_inst_name='openenoc_csr.endpoint1.peers.entry[2].local_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='base', field_type=FieldType.READWRITE),
                                                ]),
            2248 : 
    Register(width=32, full_inst_name='openenoc_csr.endpoint1.peers.entry[2].remote_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='base', field_type=FieldType.READWRITE),
                                                ]),
            2252 : 
    Register(width=32, full_inst_name='openenoc_csr.endpoint1.peers.entry[2].size', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='bytes', field_type=FieldType.READWRITE),
                                                ]),
            2256 : 
    Register(width=32, full_inst_name='openenoc_csr.endpoint1.peers.entry[2].dma', readable=True, writable=True,
                                         fields=[FieldDefinition(high=1, low=0, msb=1, lsb=0, inst_name='mode', field_type=FieldType.READWRITE),FieldDefinition(high=8, low=8, msb=8, lsb=8, inst_name='request', field_type=FieldType.READWRITE),FieldDefinition(high=16, low=16, msb=16, lsb=16, inst_name='idle', field_type=FieldType.READONLY),FieldDefinition(high=24, low=24, msb=24, lsb=24, inst_name='done', field_type=FieldType.READONLY),FieldDefinition(high=25, low=25, msb=25, lsb=25, inst_name='error', field_type=FieldType.READONLY),
                                                ]),
            2260 : 
    Register(width=64, full_inst_name='openenoc_csr.endpoint1.peers.entry[3].mac_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            2268 : 
    Register(width=32, full_inst_name='openenoc_csr.endpoint1.peers.entry[3].rmem_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='offset', field_type=FieldType.READWRITE),
                                                ]),
            2272 : 
    Register(width=32, full_inst_name='openenoc_csr.endpoint1.peers.entry[3].local_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='base', field_type=FieldType.READWRITE),
                                                ]),
            2276 : 
    Register(width=32, full_inst_name='openenoc_csr.endpoint1.peers.entry[3].remote_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='base', field_type=FieldType.READWRITE),
                                                ]),
            2280 : 
    Register(width=32, full_inst_name='openenoc_csr.endpoint1.peers.entry[3].size', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='bytes', field_type=FieldType.READWRITE),
                                                ]),
            2284 : 
    Register(width=32, full_inst_name='openenoc_csr.endpoint1.peers.entry[3].dma', readable=True, writable=True,
                                         fields=[FieldDefinition(high=1, low=0, msb=1, lsb=0, inst_name='mode', field_type=FieldType.READWRITE),FieldDefinition(high=8, low=8, msb=8, lsb=8, inst_name='request', field_type=FieldType.READWRITE),FieldDefinition(high=16, low=16, msb=16, lsb=16, inst_name='idle', field_type=FieldType.READONLY),FieldDefinition(high=24, low=24, msb=24, lsb=24, inst_name='done', field_type=FieldType.READONLY),FieldDefinition(high=25, low=25, msb=25, lsb=25, inst_name='error', field_type=FieldType.READONLY),
                                                ]),
            4096 : 
    Register(width=64, full_inst_name='openenoc_csr.endpoint2.info', readable=True, writable=False,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='rmem_total_depth', field_type=FieldType.READONLY),FieldDefinition(high=63, low=32, msb=63, lsb=32, inst_name='num_of_peers', field_type=FieldType.READONLY),
                                                ]),
            4104 : 
    Register(width=64, full_inst_name='openenoc_csr.endpoint2.config.mac_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            4128 : 
    Register(width=32, full_inst_name='openenoc_csr.endpoint2.axis_if.source.data', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='tdata', field_type=FieldType.READWRITE),
                                                ]),
            4132 : 
    Register(width=32, full_inst_name='openenoc_csr.endpoint2.axis_if.source.control', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='tvalid', field_type=FieldType.READWRITE),FieldDefinition(high=8, low=8, msb=8, lsb=8, inst_name='tlast', field_type=FieldType.READWRITE),
                                                ]),
            4136 : 
    Register(width=32, full_inst_name='openenoc_csr.endpoint2.axis_if.source.status', readable=True, writable=False,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='tready', field_type=FieldType.READONLY),
                                                ]),
            4144 : 
    Register(width=32, full_inst_name='openenoc_csr.endpoint2.axis_if.sink.data', readable=True, writable=False,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='tdata', field_type=FieldType.READONLY),
                                                ]),
            4148 : 
    Register(width=32, full_inst_name='openenoc_csr.endpoint2.axis_if.sink.control', readable=False, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='tready', field_type=FieldType.WRITEONLY),
                                                ]),
            4152 : 
    Register(width=32, full_inst_name='openenoc_csr.endpoint2.axis_if.sink.status', readable=True, writable=False,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='tvalid', field_type=FieldType.READONLY),FieldDefinition(high=8, low=8, msb=8, lsb=8, inst_name='tlast', field_type=FieldType.READONLY),
                                                ]),
            4160 : 
    Register(width=64, full_inst_name='openenoc_csr.endpoint2.peers.entry[0].mac_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            4168 : 
    Register(width=32, full_inst_name='openenoc_csr.endpoint2.peers.entry[0].rmem_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='offset', field_type=FieldType.READWRITE),
                                                ]),
            4172 : 
    Register(width=32, full_inst_name='openenoc_csr.endpoint2.peers.entry[0].local_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='base', field_type=FieldType.READWRITE),
                                                ]),
            4176 : 
    Register(width=32, full_inst_name='openenoc_csr.endpoint2.peers.entry[0].remote_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='base', field_type=FieldType.READWRITE),
                                                ]),
            4180 : 
    Register(width=32, full_inst_name='openenoc_csr.endpoint2.peers.entry[0].size', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='bytes', field_type=FieldType.READWRITE),
                                                ]),
            4184 : 
    Register(width=32, full_inst_name='openenoc_csr.endpoint2.peers.entry[0].dma', readable=True, writable=True,
                                         fields=[FieldDefinition(high=1, low=0, msb=1, lsb=0, inst_name='mode', field_type=FieldType.READWRITE),FieldDefinition(high=8, low=8, msb=8, lsb=8, inst_name='request', field_type=FieldType.READWRITE),FieldDefinition(high=16, low=16, msb=16, lsb=16, inst_name='idle', field_type=FieldType.READONLY),FieldDefinition(high=24, low=24, msb=24, lsb=24, inst_name='done', field_type=FieldType.READONLY),FieldDefinition(high=25, low=25, msb=25, lsb=25, inst_name='error', field_type=FieldType.READONLY),
                                                ]),
            4188 : 
    Register(width=64, full_inst_name='openenoc_csr.endpoint2.peers.entry[1].mac_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            4196 : 
    Register(width=32, full_inst_name='openenoc_csr.endpoint2.peers.entry[1].rmem_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='offset', field_type=FieldType.READWRITE),
                                                ]),
            4200 : 
    Register(width=32, full_inst_name='openenoc_csr.endpoint2.peers.entry[1].local_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='base', field_type=FieldType.READWRITE),
                                                ]),
            4204 : 
    Register(width=32, full_inst_name='openenoc_csr.endpoint2.peers.entry[1].remote_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='base', field_type=FieldType.READWRITE),
                                                ]),
            4208 : 
    Register(width=32, full_inst_name='openenoc_csr.endpoint2.peers.entry[1].size', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='bytes', field_type=FieldType.READWRITE),
                                                ]),
            4212 : 
    Register(width=32, full_inst_name='openenoc_csr.endpoint2.peers.entry[1].dma', readable=True, writable=True,
                                         fields=[FieldDefinition(high=1, low=0, msb=1, lsb=0, inst_name='mode', field_type=FieldType.READWRITE),FieldDefinition(high=8, low=8, msb=8, lsb=8, inst_name='request', field_type=FieldType.READWRITE),FieldDefinition(high=16, low=16, msb=16, lsb=16, inst_name='idle', field_type=FieldType.READONLY),FieldDefinition(high=24, low=24, msb=24, lsb=24, inst_name='done', field_type=FieldType.READONLY),FieldDefinition(high=25, low=25, msb=25, lsb=25, inst_name='error', field_type=FieldType.READONLY),
                                                ]),
            5120 : 
    Register(width=32, full_inst_name='openenoc_csr.switch1.info', readable=True, writable=False,
                                         fields=[FieldDefinition(high=15, low=0, msb=15, lsb=0, inst_name='table_depth', field_type=FieldType.READONLY),FieldDefinition(high=21, low=16, msb=21, lsb=16, inst_name='num_of_interfaces', field_type=FieldType.READONLY),
                                                ]),
            5124 : 
    Register(width=32, full_inst_name='openenoc_csr.switch1.forwarding_control', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='operation_mode', field_type=FieldType.READWRITE),FieldDefinition(high=7, low=7, msb=7, lsb=7, inst_name='pause_request', field_type=FieldType.READWRITE),FieldDefinition(high=15, low=15, msb=15, lsb=15, inst_name='pause_done', field_type=FieldType.READONLY),
                                                ]),
            5128 : 
    Register(width=32, full_inst_name='openenoc_csr.switch1.default_forwarding', readable=True, writable=True,
                                         fields=[FieldDefinition(high=3, low=0, msb=3, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            5248 : 
    Register(width=64, full_inst_name='openenoc_csr.switch1.forwarding_table.entry[0].mac_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            5256 : 
    Register(width=32, full_inst_name='openenoc_csr.switch1.forwarding_table.entry[0].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=3, low=0, msb=3, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            5260 : 
    Register(width=32, full_inst_name='openenoc_csr.switch1.forwarding_table.entry[0].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            5264 : 
    Register(width=64, full_inst_name='openenoc_csr.switch1.forwarding_table.entry[1].mac_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            5272 : 
    Register(width=32, full_inst_name='openenoc_csr.switch1.forwarding_table.entry[1].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=3, low=0, msb=3, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            5276 : 
    Register(width=32, full_inst_name='openenoc_csr.switch1.forwarding_table.entry[1].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            5280 : 
    Register(width=64, full_inst_name='openenoc_csr.switch1.forwarding_table.entry[2].mac_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            5288 : 
    Register(width=32, full_inst_name='openenoc_csr.switch1.forwarding_table.entry[2].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=3, low=0, msb=3, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            5292 : 
    Register(width=32, full_inst_name='openenoc_csr.switch1.forwarding_table.entry[2].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            5296 : 
    Register(width=64, full_inst_name='openenoc_csr.switch1.forwarding_table.entry[3].mac_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            5304 : 
    Register(width=32, full_inst_name='openenoc_csr.switch1.forwarding_table.entry[3].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=3, low=0, msb=3, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            5308 : 
    Register(width=32, full_inst_name='openenoc_csr.switch1.forwarding_table.entry[3].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            5312 : 
    Register(width=64, full_inst_name='openenoc_csr.switch1.forwarding_table.entry[4].mac_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            5320 : 
    Register(width=32, full_inst_name='openenoc_csr.switch1.forwarding_table.entry[4].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=3, low=0, msb=3, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            5324 : 
    Register(width=32, full_inst_name='openenoc_csr.switch1.forwarding_table.entry[4].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            5328 : 
    Register(width=64, full_inst_name='openenoc_csr.switch1.forwarding_table.entry[5].mac_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            5336 : 
    Register(width=32, full_inst_name='openenoc_csr.switch1.forwarding_table.entry[5].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=3, low=0, msb=3, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            5340 : 
    Register(width=32, full_inst_name='openenoc_csr.switch1.forwarding_table.entry[5].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            5344 : 
    Register(width=64, full_inst_name='openenoc_csr.switch1.forwarding_table.entry[6].mac_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            5352 : 
    Register(width=32, full_inst_name='openenoc_csr.switch1.forwarding_table.entry[6].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=3, low=0, msb=3, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            5356 : 
    Register(width=32, full_inst_name='openenoc_csr.switch1.forwarding_table.entry[6].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            5360 : 
    Register(width=64, full_inst_name='openenoc_csr.switch1.forwarding_table.entry[7].mac_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            5368 : 
    Register(width=32, full_inst_name='openenoc_csr.switch1.forwarding_table.entry[7].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=3, low=0, msb=3, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            5372 : 
    Register(width=32, full_inst_name='openenoc_csr.switch1.forwarding_table.entry[7].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            6144 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.info', readable=True, writable=False,
                                         fields=[FieldDefinition(high=15, low=0, msb=15, lsb=0, inst_name='table_depth', field_type=FieldType.READONLY),FieldDefinition(high=21, low=16, msb=21, lsb=16, inst_name='num_of_interfaces', field_type=FieldType.READONLY),
                                                ]),
            6148 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_control', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='operation_mode', field_type=FieldType.READWRITE),FieldDefinition(high=7, low=7, msb=7, lsb=7, inst_name='pause_request', field_type=FieldType.READWRITE),FieldDefinition(high=15, low=15, msb=15, lsb=15, inst_name='pause_done', field_type=FieldType.READONLY),
                                                ]),
            6152 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.default_forwarding', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            6656 : 
    Register(width=64, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[0].mac_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            6664 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[0].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            6668 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[0].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            6672 : 
    Register(width=64, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[1].mac_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            6680 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[1].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            6684 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[1].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            6688 : 
    Register(width=64, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[2].mac_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            6696 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[2].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            6700 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[2].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            6704 : 
    Register(width=64, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[3].mac_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            6712 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[3].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            6716 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[3].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            6720 : 
    Register(width=64, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[4].mac_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            6728 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[4].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            6732 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[4].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            6736 : 
    Register(width=64, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[5].mac_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            6744 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[5].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            6748 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[5].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            6752 : 
    Register(width=64, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[6].mac_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            6760 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[6].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            6764 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[6].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            6768 : 
    Register(width=64, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[7].mac_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            6776 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[7].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            6780 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[7].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            6784 : 
    Register(width=64, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[8].mac_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            6792 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[8].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            6796 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[8].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            6800 : 
    Register(width=64, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[9].mac_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            6808 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[9].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            6812 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[9].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            6816 : 
    Register(width=64, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[10].mac_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            6824 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[10].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            6828 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[10].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            6832 : 
    Register(width=64, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[11].mac_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            6840 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[11].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            6844 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[11].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            6848 : 
    Register(width=64, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[12].mac_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            6856 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[12].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            6860 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[12].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            6864 : 
    Register(width=64, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[13].mac_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            6872 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[13].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            6876 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[13].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            6880 : 
    Register(width=64, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[14].mac_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            6888 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[14].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            6892 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[14].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            6896 : 
    Register(width=64, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[15].mac_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            6904 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[15].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            6908 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[15].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            6912 : 
    Register(width=64, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[16].mac_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            6920 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[16].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            6924 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[16].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            6928 : 
    Register(width=64, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[17].mac_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            6936 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[17].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            6940 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[17].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            6944 : 
    Register(width=64, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[18].mac_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            6952 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[18].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            6956 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[18].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            6960 : 
    Register(width=64, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[19].mac_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            6968 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[19].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            6972 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[19].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            6976 : 
    Register(width=64, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[20].mac_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            6984 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[20].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            6988 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[20].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            6992 : 
    Register(width=64, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[21].mac_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            7000 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[21].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            7004 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[21].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            7008 : 
    Register(width=64, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[22].mac_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            7016 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[22].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            7020 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[22].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            7024 : 
    Register(width=64, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[23].mac_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            7032 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[23].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            7036 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[23].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            7040 : 
    Register(width=64, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[24].mac_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            7048 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[24].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            7052 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[24].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            7056 : 
    Register(width=64, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[25].mac_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            7064 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[25].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            7068 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[25].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            7072 : 
    Register(width=64, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[26].mac_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            7080 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[26].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            7084 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[26].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            7088 : 
    Register(width=64, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[27].mac_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            7096 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[27].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            7100 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[27].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            7104 : 
    Register(width=64, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[28].mac_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            7112 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[28].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            7116 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[28].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            7120 : 
    Register(width=64, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[29].mac_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            7128 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[29].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            7132 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[29].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            7136 : 
    Register(width=64, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[30].mac_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            7144 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[30].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            7148 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[30].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
            7152 : 
    Register(width=64, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[31].mac_address', readable=True, writable=True,
                                         fields=[FieldDefinition(high=31, low=0, msb=31, lsb=0, inst_name='lo_word', field_type=FieldType.READWRITE),FieldDefinition(high=47, low=32, msb=47, lsb=32, inst_name='hi_word', field_type=FieldType.READWRITE),
                                                ]),
            7160 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[31].iface', readable=True, writable=True,
                                         fields=[FieldDefinition(high=7, low=0, msb=7, lsb=0, inst_name='bitmap', field_type=FieldType.READWRITE),
                                                ]),
            7164 : 
    Register(width=32, full_inst_name='openenoc_csr.switch2.forwarding_table.entry[31].config', readable=True, writable=True,
                                         fields=[FieldDefinition(high=0, low=0, msb=0, lsb=0, inst_name='enabled', field_type=FieldType.READWRITE),
                                                ]),
        }

    def _build_memories(self) -> list[MemoryEntry]:
        return [
            MemoryEntry(start_address=3072,
                        end_address=4095,
                        memory=Memory(width=32,
                                      length=256,
                                      full_inst_name='openenoc_csr.endpoint1.rmem',
                                      default_value=0)),
            MemoryEntry(start_address=4608,
                        end_address=5119,
                        memory=Memory(width=32,
                                      length=128,
                                      full_inst_name='openenoc_csr.endpoint2.rmem',
                                      default_value=0)),
        ]

if __name__ == '__main__':
    pass
