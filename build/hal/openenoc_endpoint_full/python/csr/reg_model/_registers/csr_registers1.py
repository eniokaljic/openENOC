

"""
Python Wrapper for the csr register model

This code was generated from the PeakRDL-python package version 3.1.2

"""










from typing import Iterator
from typing import Union
from typing import overload
from typing import Literal
from typing import Any
from typing import NoReturn
from typing import Type

from ...lib import Node, NodeArray, Base
from ...lib import UDPStruct

from ...lib import Memory
from ...lib import AddressMap
from ...lib import RegFile
from ...lib import MemoryReadOnly, MemoryWriteOnly, MemoryReadWrite
from ...lib import Reg, RegArray
from ...lib import RegReadOnly, RegWriteOnly, RegReadWrite
from ...lib import RegReadOnlyArray, RegWriteOnlyArray, RegReadWriteArray
from ...lib import ReadableMemory, WritableMemory
from ...lib import FieldReadOnly, FieldWriteOnly, FieldReadWrite, Field

from ...lib import FieldSizeProps, FieldMiscProps






from .fields import openenoc_endpoint_interface_peers_entry_rmem_address_offset_neg_0x77c601c68d28e954_cls
from .fields import openenoc_endpoint_interface_peers_entry_local_address_base_neg_0x28400c85cc112732_cls
from .fields import openenoc_endpoint_interface_peers_entry_remote_address_base_neg_0x174625b8a6d3f6de_cls
from .fields import openenoc_endpoint_interface_peers_entry_size_bytes_0x3244476a4d2fae6a_cls
from .fields import openenoc_endpoint_interface_peers_entry_dma_mode_neg_0x15fdbe027da994a2_cls
from .fields import openenoc_endpoint_interface_peers_entry_dma_irq_enable_0x63ceff98cce4c452_cls
from .fields import openenoc_endpoint_interface_peers_entry_dma_request_0x40fc698382aa1f65_cls
from .fields import openenoc_endpoint_interface_peers_entry_dma_idle_neg_0x363921ad8d982494_cls
from .fields import openenoc_endpoint_interface_peers_entry_dma_done_neg_0x14239c892a9fd992_cls
from .fields import openenoc_endpoint_interface_peers_entry_dma_error_neg_0x390ea68b0064595c_cls
from .fields import openenoc_endpoint_interface_peers_entry_dma_error_code_neg_0x3a1fc3ce313d63a5_cls
from .fields import openenoc_endpoint_interface_rmem_word_data_0x1828ae99bb1f1753_cls
from .fields import openenoc_switch_interface_info_table_depth_neg_0x73ff2c1e9894a3f5_cls
from .fields import openenoc_switch_interface_info_num_of_interfaces_neg_0x58ae57776443f7f8_cls
from .fields import openenoc_switch_interface_forwarding_control_operation_mode_neg_0x1ed9a06867712a12_cls
from .fields import openenoc_switch_interface_forwarding_control_pause_request_neg_0x1759c9134381b623_cls
from .fields import openenoc_switch_interface_forwarding_control_pause_done_neg_0xb40c02629250d28_cls
from .fields import openenoc_switch_interface_default_forwarding_bitmap_neg_0x10eb1b172c4f4a80_cls
from .fields import openenoc_switch_interface_forwarding_table_entry_mac_address_lo_word_neg_0x6268045d0c0e1fa2_cls
from .fields import openenoc_switch_interface_forwarding_table_entry_mac_address_hi_word_0x689cde9aca5897a0_cls
from .fields import openenoc_switch_interface_forwarding_table_entry_iface_bitmap_0x30c42cc116763b91_cls
from .fields import openenoc_switch_interface_forwarding_table_entry_config_enabled_neg_0x4dd8e54953c4c63c_cls

# register definitions
    
    
class openenoc_endpoint_interface_peers_entry_rmem_address_neg_0x58b0e9acf3a8010c_cls(RegReadWrite):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].rmem_address |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Address offset of the virtual memory region corresponding to    |
    |              |      the remote peer's memory.</p>                                      |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__offset']

    def __init__(self,
                 address: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AddressMap,RegFile,MemoryReadWrite]):

        super().__init__(address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__offset:openenoc_endpoint_interface_peers_entry_rmem_address_offset_neg_0x77c601c68d28e954_cls = openenoc_endpoint_interface_peers_entry_rmem_address_offset_neg_0x77c601c68d28e954_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0, msb=31,
                low=0, high=31),
            misc_props=FieldMiscProps(
                default=None,
                is_volatile=False),
            logger_handle=logger_handle+'.offset',
            inst_name='offset',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def offset(self) -> openenoc_endpoint_interface_peers_entry_rmem_address_offset_neg_0x77c601c68d28e954_cls:
        """
        Property to access offset field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-                |
        |              |      1].rmem_address.offset[31:0]                                       |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>32-bit byte offset of the virtual memory region corresponding   |
        |              |      to the remote peer's memory. The value shall be aligned to a       |
        |              |      32-bit word boundary.</p>                                          |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__offset

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'offset':'offset',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_interface_peers_entry_rmem_address_offset_neg_0x77c601c68d28e954_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].rmem_address"
    @property
    def rdl_desc(self) -> str:
        return "Address offset of the virtual memory region corresponding to the remote\npeer\u0027s memory."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.offset
        
        
    

    
    
class openenoc_endpoint_interface_peers_entry_local_address_0xe2680fc2f82eab2_cls(RegReadWrite):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-                |
    |              |      1].local_address                                                   |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Start address of the local memory region for DMA transfers.</p> |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__base']

    def __init__(self,
                 address: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AddressMap,RegFile,MemoryReadWrite]):

        super().__init__(address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__base:openenoc_endpoint_interface_peers_entry_local_address_base_neg_0x28400c85cc112732_cls = openenoc_endpoint_interface_peers_entry_local_address_base_neg_0x28400c85cc112732_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0, msb=31,
                low=0, high=31),
            misc_props=FieldMiscProps(
                default=None,
                is_volatile=False),
            logger_handle=logger_handle+'.base',
            inst_name='base',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def base(self) -> openenoc_endpoint_interface_peers_entry_local_address_base_neg_0x28400c85cc112732_cls:
        """
        Property to access base field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-                |
        |              |      1].local_address.base[31:0]                                        |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Word-aligned 32-bit start address of the local memory region    |
        |              |      for DMA transfers.</p>                                             |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__base

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'base':'base',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_interface_peers_entry_local_address_base_neg_0x28400c85cc112732_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].local_address"
    @property
    def rdl_desc(self) -> str:
        return "Start address of the local memory region for DMA transfers."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.base
        
        
    

    
    
class openenoc_endpoint_interface_peers_entry_remote_address_neg_0x1067e35a3d279663_cls(RegReadWrite):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-                |
    |              |      1].remote_address                                                  |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Start address of the remote peer's memory region.</p>           |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__base']

    def __init__(self,
                 address: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AddressMap,RegFile,MemoryReadWrite]):

        super().__init__(address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__base:openenoc_endpoint_interface_peers_entry_remote_address_base_neg_0x174625b8a6d3f6de_cls = openenoc_endpoint_interface_peers_entry_remote_address_base_neg_0x174625b8a6d3f6de_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0, msb=31,
                low=0, high=31),
            misc_props=FieldMiscProps(
                default=None,
                is_volatile=False),
            logger_handle=logger_handle+'.base',
            inst_name='base',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def base(self) -> openenoc_endpoint_interface_peers_entry_remote_address_base_neg_0x174625b8a6d3f6de_cls:
        """
        Property to access base field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-                |
        |              |      1].remote_address.base[31:0]                                       |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Word-aligned 32-bit start address of the remote peer's memory   |
        |              |      region.</p>                                                        |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__base

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'base':'base',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_interface_peers_entry_remote_address_base_neg_0x174625b8a6d3f6de_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].remote_address"
    @property
    def rdl_desc(self) -> str:
        return "Start address of the remote peer\u0027s memory region."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.base
        
        
    

    
    
class openenoc_endpoint_interface_peers_entry_size_neg_0x5a29e04c13a68415_cls(RegReadWrite):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].size         |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Size of the remote peer's memory region.</p>                    |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__bytes']

    def __init__(self,
                 address: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AddressMap,RegFile,MemoryReadWrite]):

        super().__init__(address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__bytes:openenoc_endpoint_interface_peers_entry_size_bytes_0x3244476a4d2fae6a_cls = openenoc_endpoint_interface_peers_entry_size_bytes_0x3244476a4d2fae6a_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0, msb=31,
                low=0, high=31),
            misc_props=FieldMiscProps(
                default=None,
                is_volatile=False),
            logger_handle=logger_handle+'.bytes',
            inst_name='bytes',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def bytes(self) -> openenoc_endpoint_interface_peers_entry_size_bytes_0x3244476a4d2fae6a_cls:
        """
        Property to access bytes field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-                |
        |              |      1].size.bytes[31:0]                                                |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>32-bit size of the remote peer's memory region in bytes.</p>    |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__bytes

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'bytes':'bytes',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_interface_peers_entry_size_bytes_0x3244476a4d2fae6a_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].size"
    @property
    def rdl_desc(self) -> str:
        return "Size of the remote peer\u0027s memory region."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.bytes
        
        
    

    
    
class openenoc_endpoint_interface_peers_entry_dma_0x7cd581c641d8b54a_cls(RegReadWrite):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma          |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>DMA configuration and control for the remote peer.</p>          |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__mode', '__irq_enable', '__request', '__idle', '__done', '__error', '__error_code']

    def __init__(self,
                 address: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AddressMap,RegFile,MemoryReadWrite]):

        super().__init__(address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__mode:openenoc_endpoint_interface_peers_entry_dma_mode_neg_0x15fdbe027da994a2_cls = openenoc_endpoint_interface_peers_entry_dma_mode_neg_0x15fdbe027da994a2_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=2,
                lsb=0, msb=1,
                low=0, high=1),
            misc_props=FieldMiscProps(
                default=None,
                is_volatile=False),
            logger_handle=logger_handle+'.mode',
            inst_name='mode',
            field_type=int)
        self.__irq_enable:openenoc_endpoint_interface_peers_entry_dma_irq_enable_0x63ceff98cce4c452_cls = openenoc_endpoint_interface_peers_entry_dma_irq_enable_0x63ceff98cce4c452_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=2, msb=2,
                low=2, high=2),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.irq_enable',
            inst_name='irq_enable',
            field_type=int)
        self.__request:openenoc_endpoint_interface_peers_entry_dma_request_0x40fc698382aa1f65_cls = openenoc_endpoint_interface_peers_entry_dma_request_0x40fc698382aa1f65_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=8, msb=8,
                low=8, high=8),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.request',
            inst_name='request',
            field_type=int)
        self.__idle:openenoc_endpoint_interface_peers_entry_dma_idle_neg_0x363921ad8d982494_cls = openenoc_endpoint_interface_peers_entry_dma_idle_neg_0x363921ad8d982494_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=16, msb=16,
                low=16, high=16),
            misc_props=FieldMiscProps(
                default=None,
                is_volatile=True),
            logger_handle=logger_handle+'.idle',
            inst_name='idle',
            field_type=int)
        self.__done:openenoc_endpoint_interface_peers_entry_dma_done_neg_0x14239c892a9fd992_cls = openenoc_endpoint_interface_peers_entry_dma_done_neg_0x14239c892a9fd992_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=24, msb=24,
                low=24, high=24),
            misc_props=FieldMiscProps(
                default=None,
                is_volatile=True),
            logger_handle=logger_handle+'.done',
            inst_name='done',
            field_type=int)
        self.__error:openenoc_endpoint_interface_peers_entry_dma_error_neg_0x390ea68b0064595c_cls = openenoc_endpoint_interface_peers_entry_dma_error_neg_0x390ea68b0064595c_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=25, msb=25,
                low=25, high=25),
            misc_props=FieldMiscProps(
                default=None,
                is_volatile=True),
            logger_handle=logger_handle+'.error',
            inst_name='error',
            field_type=int)
        self.__error_code:openenoc_endpoint_interface_peers_entry_dma_error_code_neg_0x3a1fc3ce313d63a5_cls = openenoc_endpoint_interface_peers_entry_dma_error_code_neg_0x3a1fc3ce313d63a5_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=4,
                lsb=28, msb=31,
                low=28, high=31),
            misc_props=FieldMiscProps(
                default=None,
                is_volatile=True),
            logger_handle=logger_handle+'.error_code',
            inst_name='error_code',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def mode(self) -> openenoc_endpoint_interface_peers_entry_dma_mode_neg_0x15fdbe027da994a2_cls:
        """
        Property to access mode field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-                |
        |              |      1].dma.mode[1:0]                                                   |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>DMA mode and responder access policy for the remote             |
        |              |      peer:<ul></p> <li>0: Disabled. Locally initiated DMA and           |
        |              |      transparent RMEM operations are disabled, and incoming oETP memory |
        |              |      requests from this peer are rejected.</li>  <li>1: Transparent     |
        |              |      RMEM mode. Accesses to the virtual RMEM region are translated into |
        |              |      individual remote memory accesses. Incoming transparent RMEM read  |
        |              |      and write requests from this peer are permitted. Bulk DMA read and |
        |              |      write requests are rejected.</li>  <li>2: Mirror-to-local mode. A  |
        |              |      locally initiated DMA request fetches the remote memory region     |
        |              |      into the configured local memory region using remote DMA reads. On |
        |              |      the responder side, incoming bulk DMA write requests from this     |
        |              |      peer are permitted and target the configured local memory region.  |
        |              |      Incoming bulk DMA read requests are rejected.</li>  <li>3: Mirror- |
        |              |      to-remote mode. A locally initiated DMA request sends the          |
        |              |      configured local memory region to the remote memory region using   |
        |              |      remote DMA writes. On the responder side, incoming bulk DMA read   |
        |              |      requests from this peer are permitted and source data from the     |
        |              |      configured local memory region. Incoming bulk DMA write requests   |
        |              |      are rejected.</li>  </ul> <p>Consequently, a mirror relationship   |
        |              |      uses complementary modes: an initiator operating in mirror-to-     |
        |              |      local mode communicates with a responder entry configured as       |
        |              |      mirror-to-remote, while an initiator operating in mirror-to-remote |
        |              |      mode communicates with a responder entry configured as mirror-to-  |
        |              |      local.</p>                                                         |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__mode
    @property
    def irq_enable(self) -> openenoc_endpoint_interface_peers_entry_dma_irq_enable_0x63ceff98cce4c452_cls:
        """
        Property to access irq_enable field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-                |
        |              |      1].dma.irq_enable                                                  |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Enables generation of a PEER_DMA_COMPLETE IRQ event for this    |
        |              |      peer. Hardware samples this field together with                    |
        |              |      irq.event_enable.peer_dma_complete when it accepts the peer DMA    |
        |              |      request. Changing the field while a transfer is active does not    |
        |              |      affect that transfer. Disabling the field does not affect DMA      |
        |              |      execution or the done, error, and error_code status fields.</p>    |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__irq_enable
    @property
    def request(self) -> openenoc_endpoint_interface_peers_entry_dma_request_0x40fc698382aa1f65_cls:
        """
        Property to access request field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-                |
        |              |      1].dma.request[8:8]                                                |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Writing one requests a DMA transfer to or from the remote peer, |
        |              |      according to dma.mode. The field remains asserted until the DMA    |
        |              |      engine accepts and snapshots the request. Hardware clears it upon  |
        |              |      acceptance; while a transfer for this peer is active, a newly      |
        |              |      asserted request remains pending. Software or an RTL controller    |
        |              |      shall read the completion status of the previous request before    |
        |              |      asserting this field for the next request and shall keep the peer  |
        |              |      configuration stable while this field is asserted.</p>             |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__request
    @property
    def idle(self) -> openenoc_endpoint_interface_peers_entry_dma_idle_neg_0x363921ad8d982494_cls:
        """
        Property to access idle field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-                |
        |              |      1].dma.idle[16:16]                                                 |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Indicates whether this peer has no accepted DMA request in      |
        |              |      progress. Hardware deasserts this field when a request is accepted |
        |              |      and asserts it after all fragments of the requested block have     |
        |              |      completed.</p>                                                     |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__idle
    @property
    def done(self) -> openenoc_endpoint_interface_peers_entry_dma_done_neg_0x14239c892a9fd992_cls:
        """
        Property to access done field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-                |
        |              |      1].dma.done[24:24]                                                 |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Sticky successful-completion flag for this peer. Hardware sets  |
        |              |      this field after all fragments of the accepted block transfer      |
        |              |      complete successfully and clears it when the next request is       |
        |              |      accepted.</p>                                                      |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__done
    @property
    def error(self) -> openenoc_endpoint_interface_peers_entry_dma_error_neg_0x390ea68b0064595c_cls:
        """
        Property to access error field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-                |
        |              |      1].dma.error[25:25]                                                |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Sticky error-completion flag for this peer. Hardware sets this  |
        |              |      field if the accepted block transfer terminates with an error and  |
        |              |      clears it when the next request is accepted.</p>                   |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__error
    @property
    def error_code(self) -> openenoc_endpoint_interface_peers_entry_dma_error_code_neg_0x3a1fc3ce313d63a5_cls:
        """
        Property to access error_code field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-                |
        |              |      1].dma.error_code[31:28]                                           |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Sticky error code for the most recently completed peer DMA      |
        |              |      transfer:<ul></p> <li>0: No error.</li> <li>1: Invalid DMA         |
        |              |      configuration or descriptor.</li> <li>2: AXI4-Stream length or     |
        |              |      TLAST error.</li> <li>3: Frame exceeds the supported size or       |
        |              |      configured buffer capacity.</li> <li>4: AXI read SLVERR            |
        |              |      response.</li> <li>5: AXI read DECERR response.</li> <li>6: AXI    |
        |              |      write SLVERR response.</li> <li>7: AXI write DECERR response.</li> |
        |              |      <li>8-15: Reserved.</li> <p></ul> Hardware clears this field when  |
        |              |      the next request is accepted.</p>                                  |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__error_code

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'mode':'mode','irq_enable':'irq_enable','request':'request','idle':'idle','done':'done','error':'error','error_code':'error_code',
            }

    
    
    
    
    
    
    # nodes:7
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["mode"]) -> 'openenoc_endpoint_interface_peers_entry_dma_mode_neg_0x15fdbe027da994a2_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["irq_enable"]) -> 'openenoc_endpoint_interface_peers_entry_dma_irq_enable_0x63ceff98cce4c452_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["request"]) -> 'openenoc_endpoint_interface_peers_entry_dma_request_0x40fc698382aa1f65_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["idle"]) -> 'openenoc_endpoint_interface_peers_entry_dma_idle_neg_0x363921ad8d982494_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["done"]) -> 'openenoc_endpoint_interface_peers_entry_dma_done_neg_0x14239c892a9fd992_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["error"]) -> 'openenoc_endpoint_interface_peers_entry_dma_error_neg_0x390ea68b0064595c_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["error_code"]) -> 'openenoc_endpoint_interface_peers_entry_dma_error_code_neg_0x3a1fc3ce313d63a5_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_interface_peers_entry_dma_mode_neg_0x15fdbe027da994a2_cls', 'openenoc_endpoint_interface_peers_entry_dma_irq_enable_0x63ceff98cce4c452_cls', 'openenoc_endpoint_interface_peers_entry_dma_request_0x40fc698382aa1f65_cls', 'openenoc_endpoint_interface_peers_entry_dma_idle_neg_0x363921ad8d982494_cls', 'openenoc_endpoint_interface_peers_entry_dma_done_neg_0x14239c892a9fd992_cls', 'openenoc_endpoint_interface_peers_entry_dma_error_neg_0x390ea68b0064595c_cls', 'openenoc_endpoint_interface_peers_entry_dma_error_code_neg_0x3a1fc3ce313d63a5_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma"
    @property
    def rdl_desc(self) -> str:
        return "DMA configuration and control for the remote peer."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.mode
        yield self.irq_enable
        yield self.request
        yield self.idle
        yield self.done
        yield self.error
        yield self.error_code
        
        
    

    
    
class openenoc_endpoint_interface_rmem_word_0x480ef9667036699d_cls(RegReadWrite):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]            |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>32-bit word in the virtual memory region.</p>                   |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__data']

    def __init__(self,
                 address: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AddressMap,RegFile,MemoryReadWrite]):

        super().__init__(address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__data:openenoc_endpoint_interface_rmem_word_data_0x1828ae99bb1f1753_cls = openenoc_endpoint_interface_rmem_word_data_0x1828ae99bb1f1753_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0, msb=31,
                low=0, high=31),
            misc_props=FieldMiscProps(
                default=None,
                is_volatile=True),
            logger_handle=logger_handle+'.data',
            inst_name='data',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def data(self) -> openenoc_endpoint_interface_rmem_word_data_0x1828ae99bb1f1753_cls:
        """
        Property to access data field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0] |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Data stored in this virtual memory word.</p>                    |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__data

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'data':'data',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_interface_rmem_word_data_0x1828ae99bb1f1753_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]"
    @property
    def rdl_desc(self) -> str:
        return "32-bit word in the virtual memory region."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.data
        
        
class openenoc_endpoint_interface_rmem_word_0x480ef9667036699d_cls_array(RegReadWriteArray):
    """
    Class to represent a register array in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]            |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>32-bit word in the virtual memory region.</p>                   |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__: list[str] = []

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    @property
    def _element_datatype(self) -> Type[RegReadWrite]:
        return openenoc_endpoint_interface_rmem_word_0x480ef9667036699d_cls

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]"
    @property
    def rdl_desc(self) -> str:
        return "32-bit word in the virtual memory region."
    
    
    

    
    
class openenoc_switch_interface_info_0x2c1825e94fa9ff06_cls(RegReadOnly):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.switch_interface.info                                          |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Read-only information register for this openENOC Switch         |
    |              |      instance.</p>                                                      |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__table_depth', '__num_of_interfaces']

    def __init__(self,
                 address: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AddressMap,RegFile,ReadableMemory]):

        super().__init__(address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__table_depth:openenoc_switch_interface_info_table_depth_neg_0x73ff2c1e9894a3f5_cls = openenoc_switch_interface_info_table_depth_neg_0x73ff2c1e9894a3f5_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=16,
                lsb=0, msb=15,
                low=0, high=15),
            misc_props=FieldMiscProps(
                default=8,
                is_volatile=False),
            logger_handle=logger_handle+'.table_depth',
            inst_name='table_depth',
            field_type=int)
        self.__num_of_interfaces:openenoc_switch_interface_info_num_of_interfaces_neg_0x58ae57776443f7f8_cls = openenoc_switch_interface_info_num_of_interfaces_neg_0x58ae57776443f7f8_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=6,
                lsb=16, msb=21,
                low=16, high=21),
            misc_props=FieldMiscProps(
                default=4,
                is_volatile=False),
            logger_handle=logger_handle+'.num_of_interfaces',
            inst_name='num_of_interfaces',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def table_depth(self) -> openenoc_switch_interface_info_table_depth_neg_0x73ff2c1e9894a3f5_cls:
        """
        Property to access table_depth field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.switch_interface.info.table_depth[15:0]                        |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Depth of the forwarding table in this openENOC Switch instance. |
        |              |      This field reflects the TABLE_DEPTH parameter value.</p>           |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__table_depth
    @property
    def num_of_interfaces(self) -> openenoc_switch_interface_info_num_of_interfaces_neg_0x58ae57776443f7f8_cls:
        """
        Property to access num_of_interfaces field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.switch_interface.info.num_of_interfaces[21:16]                 |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Number of interfaces in this openENOC Switch instance. This     |
        |              |      field reflects the NUM_OF_INTERFACES parameter value.</p>          |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__num_of_interfaces

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'table_depth':'table_depth','num_of_interfaces':'num_of_interfaces',
            }

    
    
    
    
    
    
    # nodes:2
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["table_depth"]) -> 'openenoc_switch_interface_info_table_depth_neg_0x73ff2c1e9894a3f5_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["num_of_interfaces"]) -> 'openenoc_switch_interface_info_num_of_interfaces_neg_0x58ae57776443f7f8_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_switch_interface_info_table_depth_neg_0x73ff2c1e9894a3f5_cls', 'openenoc_switch_interface_info_num_of_interfaces_neg_0x58ae57776443f7f8_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.switch_interface.info"
    @property
    def rdl_desc(self) -> str:
        return "Read-only information register for this openENOC Switch instance."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.table_depth
        yield self.num_of_interfaces
        
        
    

    
    
class openenoc_switch_interface_forwarding_control_0x47e96ad2ded239c7_cls(RegReadWrite):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.switch_interface.forwarding_control                            |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Forwarding control register for the openENOC Switch             |
    |              |      instance.</p>                                                      |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__operation_mode', '__pause_request', '__pause_done']

    def __init__(self,
                 address: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AddressMap,RegFile,MemoryReadWrite]):

        super().__init__(address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__operation_mode:openenoc_switch_interface_forwarding_control_operation_mode_neg_0x1ed9a06867712a12_cls = openenoc_switch_interface_forwarding_control_operation_mode_neg_0x1ed9a06867712a12_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=0, msb=0,
                low=0, high=0),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.operation_mode',
            inst_name='operation_mode',
            field_type=int)
        self.__pause_request:openenoc_switch_interface_forwarding_control_pause_request_neg_0x1759c9134381b623_cls = openenoc_switch_interface_forwarding_control_pause_request_neg_0x1759c9134381b623_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=7, msb=7,
                low=7, high=7),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.pause_request',
            inst_name='pause_request',
            field_type=int)
        self.__pause_done:openenoc_switch_interface_forwarding_control_pause_done_neg_0xb40c02629250d28_cls = openenoc_switch_interface_forwarding_control_pause_done_neg_0xb40c02629250d28_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=15, msb=15,
                low=15, high=15),
            misc_props=FieldMiscProps(
                default=None,
                is_volatile=True),
            logger_handle=logger_handle+'.pause_done',
            inst_name='pause_done',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def operation_mode(self) -> openenoc_switch_interface_forwarding_control_operation_mode_neg_0x1ed9a06867712a12_cls:
        """
        Property to access operation_mode field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.switch_interface.forwarding_control.operation_mode[0:0]        |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Mode of operation for the openENOC Switch instance. When set to |
        |              |      1, the switch operates in managed mode, allowing software to       |
        |              |      configure the forwarding table and control forwarding operations.  |
        |              |      When set to 0, the switch operates in unmanaged mode, where        |
        |              |      forwarding state is maintained autonomously by internal hardware   |
        |              |      logic without software intervention.</p>                           |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__operation_mode
    @property
    def pause_request(self) -> openenoc_switch_interface_forwarding_control_pause_request_neg_0x1759c9134381b623_cls:
        """
        Property to access pause_request field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.switch_interface.forwarding_control.pause_request[7:7]         |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Pause request for the forwarding logic. When set, this field    |
        |              |      requests the switch to pause frame forwarding and clear its        |
        |              |      internal pipeline before forwarding table updates are              |
        |              |      performed.</p>                                                     |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__pause_request
    @property
    def pause_done(self) -> openenoc_switch_interface_forwarding_control_pause_done_neg_0xb40c02629250d28_cls:
        """
        Property to access pause_done field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.switch_interface.forwarding_control.pause_done[15:15]          |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Pause done status. When set, this field indicates that the      |
        |              |      switch has paused frame forwarding and reached a safe state for    |
        |              |      forwarding table modification.</p>                                 |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__pause_done

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'operation_mode':'operation_mode','pause_request':'pause_request','pause_done':'pause_done',
            }

    
    
    
    
    
    
    # nodes:3
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["operation_mode"]) -> 'openenoc_switch_interface_forwarding_control_operation_mode_neg_0x1ed9a06867712a12_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["pause_request"]) -> 'openenoc_switch_interface_forwarding_control_pause_request_neg_0x1759c9134381b623_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["pause_done"]) -> 'openenoc_switch_interface_forwarding_control_pause_done_neg_0xb40c02629250d28_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_switch_interface_forwarding_control_operation_mode_neg_0x1ed9a06867712a12_cls', 'openenoc_switch_interface_forwarding_control_pause_request_neg_0x1759c9134381b623_cls', 'openenoc_switch_interface_forwarding_control_pause_done_neg_0xb40c02629250d28_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.switch_interface.forwarding_control"
    @property
    def rdl_desc(self) -> str:
        return "Forwarding control register for the openENOC Switch instance."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.operation_mode
        yield self.pause_request
        yield self.pause_done
        
        
    

    
    
class openenoc_switch_interface_default_forwarding_0x176bb20641e3036c_cls(RegReadWrite):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.switch_interface.default_forwarding                            |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Defines the destination interface or interfaces for frames that |
    |              |      do not match any enabled forwarding table entry.</p>               |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__bitmap']

    def __init__(self,
                 address: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AddressMap,RegFile,MemoryReadWrite]):

        super().__init__(address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__bitmap:openenoc_switch_interface_default_forwarding_bitmap_neg_0x10eb1b172c4f4a80_cls = openenoc_switch_interface_default_forwarding_bitmap_neg_0x10eb1b172c4f4a80_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=4,
                lsb=0, msb=3,
                low=0, high=3),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.bitmap',
            inst_name='bitmap',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def bitmap(self) -> openenoc_switch_interface_default_forwarding_bitmap_neg_0x10eb1b172c4f4a80_cls:
        """
        Property to access bitmap field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.switch_interface.default_forwarding.bitmap[NUM_OF_INTERFACES-  |
        |              |      1:0]                                                               |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Bitmap selecting the output interface or interfaces to which    |
        |              |      frames that do not match any enabled forwarding table entry are    |
        |              |      forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the    |
        |              |      first interface; bit 0 corresponds to the last interface.</p>      |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__bitmap

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'bitmap':'bitmap',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_switch_interface_default_forwarding_bitmap_neg_0x10eb1b172c4f4a80_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.switch_interface.default_forwarding"
    @property
    def rdl_desc(self) -> str:
        return "Defines the destination interface or interfaces for frames that do not match any enabled forwarding table entry."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.bitmap
        
        
    

    
    
class openenoc_switch_interface_forwarding_table_entry_mac_address_neg_0x74c2a512ae98d7a4_cls(RegReadWrite):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-        |
    |              |      1].mac_address                                                     |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>48-bit destination MAC address used as the key for this         |
    |              |      forwarding table entry.</p>                                        |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__lo_word', '__hi_word']

    def __init__(self,
                 address: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AddressMap,RegFile,MemoryReadWrite]):

        super().__init__(address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__lo_word:openenoc_switch_interface_forwarding_table_entry_mac_address_lo_word_neg_0x6268045d0c0e1fa2_cls = openenoc_switch_interface_forwarding_table_entry_mac_address_lo_word_neg_0x6268045d0c0e1fa2_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0, msb=31,
                low=0, high=31),
            misc_props=FieldMiscProps(
                default=None,
                is_volatile=True),
            logger_handle=logger_handle+'.lo_word',
            inst_name='lo_word',
            field_type=int)
        self.__hi_word:openenoc_switch_interface_forwarding_table_entry_mac_address_hi_word_0x689cde9aca5897a0_cls = openenoc_switch_interface_forwarding_table_entry_mac_address_hi_word_0x689cde9aca5897a0_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=16,
                lsb=32, msb=47,
                low=32, high=47),
            misc_props=FieldMiscProps(
                default=None,
                is_volatile=True),
            logger_handle=logger_handle+'.hi_word',
            inst_name='hi_word',
            field_type=int)

    @property
    def width(self) -> int:
        return 64

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def lo_word(self) -> openenoc_switch_interface_forwarding_table_entry_mac_address_lo_word_neg_0x6268045d0c0e1fa2_cls:
        """
        Property to access lo_word field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-        |
        |              |      1].mac_address.lo_word[31:0]                                       |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this   |
        |              |      forwarding table entry.</p>                                        |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__lo_word
    @property
    def hi_word(self) -> openenoc_switch_interface_forwarding_table_entry_mac_address_hi_word_0x689cde9aca5897a0_cls:
        """
        Property to access hi_word field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-        |
        |              |      1].mac_address.hi_word[47:32]                                      |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this  |
        |              |      forwarding table entry.</p>                                        |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__hi_word

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'lo_word':'lo_word','hi_word':'hi_word',
            }

    
    
    
    
    
    
    # nodes:2
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["lo_word"]) -> 'openenoc_switch_interface_forwarding_table_entry_mac_address_lo_word_neg_0x6268045d0c0e1fa2_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["hi_word"]) -> 'openenoc_switch_interface_forwarding_table_entry_mac_address_hi_word_0x689cde9aca5897a0_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_switch_interface_forwarding_table_entry_mac_address_lo_word_neg_0x6268045d0c0e1fa2_cls', 'openenoc_switch_interface_forwarding_table_entry_mac_address_hi_word_0x689cde9aca5897a0_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address"
    @property
    def rdl_desc(self) -> str:
        return "48-bit destination MAC address used as the key for this forwarding table entry."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.lo_word
        yield self.hi_word
        
        
    

    
    
class openenoc_switch_interface_forwarding_table_entry_iface_0x2495eb9bccfeb31f_cls(RegReadWrite):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-        |
    |              |      1].iface                                                           |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Forwarding interface information associated with this           |
    |              |      forwarding table entry.</p>                                        |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__bitmap']

    def __init__(self,
                 address: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AddressMap,RegFile,MemoryReadWrite]):

        super().__init__(address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__bitmap:openenoc_switch_interface_forwarding_table_entry_iface_bitmap_0x30c42cc116763b91_cls = openenoc_switch_interface_forwarding_table_entry_iface_bitmap_0x30c42cc116763b91_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=4,
                lsb=0, msb=3,
                low=0, high=3),
            misc_props=FieldMiscProps(
                default=None,
                is_volatile=True),
            logger_handle=logger_handle+'.bitmap',
            inst_name='bitmap',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def bitmap(self) -> openenoc_switch_interface_forwarding_table_entry_iface_bitmap_0x30c42cc116763b91_cls:
        """
        Property to access bitmap field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-        |
        |              |      1].iface.bitmap[NUM_OF_INTERFACES-1:0]                             |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Bitmap selecting the output interface or interfaces to which a  |
        |              |      matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB,     |
        |              |      corresponds to the first interface; bit 0 corresponds to the last  |
        |              |      interface.</p>                                                     |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__bitmap

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'bitmap':'bitmap',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_switch_interface_forwarding_table_entry_iface_bitmap_0x30c42cc116763b91_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].iface"
    @property
    def rdl_desc(self) -> str:
        return "Forwarding interface information associated with this forwarding table entry."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.bitmap
        
        
    

    
    
class openenoc_switch_interface_forwarding_table_entry_config_neg_0x2e7c20c52a8cffaa_cls(RegReadWrite):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-        |
    |              |      1].config                                                          |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Configuration information associated with this forwarding table |
    |              |      entry.</p>                                                         |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__enabled']

    def __init__(self,
                 address: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AddressMap,RegFile,MemoryReadWrite]):

        super().__init__(address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__enabled:openenoc_switch_interface_forwarding_table_entry_config_enabled_neg_0x4dd8e54953c4c63c_cls = openenoc_switch_interface_forwarding_table_entry_config_enabled_neg_0x4dd8e54953c4c63c_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=0, msb=0,
                low=0, high=0),
            misc_props=FieldMiscProps(
                default=None,
                is_volatile=True),
            logger_handle=logger_handle+'.enabled',
            inst_name='enabled',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def enabled(self) -> openenoc_switch_interface_forwarding_table_entry_config_enabled_neg_0x4dd8e54953c4c63c_cls:
        """
        Property to access enabled field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-        |
        |              |      1].config.enabled                                                  |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Enables this forwarding table entry. When cleared, the entry is |
        |              |      ignored during forwarding table lookup.</p>                        |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__enabled

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'enabled':'enabled',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_switch_interface_forwarding_table_entry_config_enabled_neg_0x4dd8e54953c4c63c_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].config"
    @property
    def rdl_desc(self) -> str:
        return "Configuration information associated with this forwarding table entry."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.enabled
        
        
    


if __name__ == '__main__':
    pass