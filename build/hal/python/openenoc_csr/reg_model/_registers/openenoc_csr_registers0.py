

"""
Python Wrapper for the openenoc_csr register model

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






from .fields import openenoc_csr_test_reg_test_field_neg_0x3e40c86c449c459_cls
from .fields import openenoc_endpoint_info_rmem_total_depth_neg_0x48394dfae72caedc_cls
from .fields import openenoc_endpoint_info_num_of_peers_neg_0x72a743a2ee31bcb1_cls
from .fields import openenoc_endpoint_config_mac_address_lo_word_neg_0x4c4cc56940c7b20a_cls
from .fields import openenoc_endpoint_config_mac_address_hi_word_0x3da0938188475d96_cls
from .fields import openenoc_endpoint_peers_entry_mac_address_lo_word_0x62051156f51d0c25_cls
from .fields import openenoc_endpoint_peers_entry_mac_address_hi_word_0x5ad3a0cf7a9bb51a_cls
from .fields import openenoc_endpoint_peers_entry_rmem_address_offset_0xd6c90bcd521e9a7_cls
from .fields import openenoc_endpoint_peers_entry_local_address_base_0x646a7692e00c9edb_cls
from .fields import openenoc_endpoint_peers_entry_remote_address_base_neg_0x7ab289b4ae316a1d_cls
from .fields import openenoc_endpoint_peers_entry_size_value_neg_0x4e9e0c98c704f31e_cls
from .fields import openenoc_endpoint_peers_entry_dma_config_mode_0x5fd986b44e4735b1_cls
from .fields import openenoc_endpoint_info_rmem_total_depth_neg_0x4876a1e84ba7ada7_cls
from .fields import openenoc_endpoint_info_num_of_peers_0x24f0b4c224afddb6_cls
from .fields import openenoc_endpoint_config_mac_address_lo_word_neg_0x627fd53fbffa4147_cls
from .fields import openenoc_endpoint_config_mac_address_hi_word_neg_0x6fe723c1622c5f8e_cls
from .fields import openenoc_endpoint_peers_entry_mac_address_lo_word_neg_0x3f203d0bb09e8cac_cls
from .fields import openenoc_endpoint_peers_entry_mac_address_hi_word_neg_0x5d4950358d3f9612_cls
from .fields import openenoc_endpoint_peers_entry_rmem_address_offset_neg_0x58778d0fb7848bc3_cls
from .fields import openenoc_endpoint_peers_entry_local_address_base_0xffb3c6e49bfcbde_cls
from .fields import openenoc_endpoint_peers_entry_remote_address_base_neg_0x1fb1ec1313d0d7a6_cls
from .fields import openenoc_endpoint_peers_entry_size_value_neg_0x18d87c0234b85b3d_cls
from .fields import openenoc_endpoint_peers_entry_dma_config_mode_neg_0x3a4a53270195223f_cls
from .fields import openenoc_switch_info_table_depth_0x5e4ef67b873ebaa7_cls
from .fields import openenoc_switch_info_num_of_interfaces_0x4de2c66b36843eb3_cls
from .fields import openenoc_switch_forwarding_control_operation_mode_0x79a73572aa97c5d9_cls
from .fields import openenoc_switch_forwarding_control_pause_request_neg_0x744b08c36d37b451_cls
from .fields import openenoc_switch_forwarding_control_pause_done_0x74a9d63a4df4691c_cls
from .fields import openenoc_switch_default_forwarding_bitmap_neg_0x6727db7163315abd_cls
from .fields import openenoc_switch_forwarding_table_entry_mac_address_lo_word_0x9564a1a009b9122_cls
from .fields import openenoc_switch_forwarding_table_entry_mac_address_hi_word_0x8d0840040004d52_cls
from .fields import openenoc_switch_forwarding_table_entry_iface_bitmap_0x247fa91e0c44bc44_cls
from .fields import openenoc_switch_forwarding_table_entry_config_enabled_neg_0x6a6e8c755744d830_cls
from .fields import openenoc_switch_info_table_depth_neg_0x7c3efff0035202ba_cls
from .fields import openenoc_switch_info_num_of_interfaces_0x3f5005238df5ff7c_cls

# register definitions
    
    
class openenoc_csr_test_reg_neg_0x63e55094833a6beb_cls(RegReadWrite):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.test_reg                                                       |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Test register</p>                                               |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__test_field']

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
        
        self.__test_field:openenoc_csr_test_reg_test_field_neg_0x3e40c86c449c459_cls = openenoc_csr_test_reg_test_field_neg_0x3e40c86c449c459_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0, msb=31,
                low=0, high=31),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.test_field',
            inst_name='test_field',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def test_field(self) -> openenoc_csr_test_reg_test_field_neg_0x3e40c86c449c459_cls:
        """
        Property to access test_field field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.test_reg.test_field[31:0]                                      |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>4-byte test field</p>                                           |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__test_field

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'test_field':'test_field',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_csr_test_reg_test_field_neg_0x3e40c86c449c459_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.test_reg"
    @property
    def rdl_desc(self) -> str:
        return "Test register"
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.test_field
        
        
    

    
    
class openenoc_csr_regB_0x5a8939990e0f6f33_cls(RegReadWrite):
    """
    Class to represent a register in the register model

    
    """

    __slots__ : list[str] = ['__f0', '__f1', '__f2', '__f3']

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
        
        self.__f0:FieldReadWrite = FieldReadWrite(
            parent_register=self,
            size_props=FieldSizeProps(
                width=8,
                lsb=0, msb=7,
                low=0, high=7),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.f0',
            inst_name='f0',
            field_type=int)
        self.__f1:FieldReadWrite = FieldReadWrite(
            parent_register=self,
            size_props=FieldSizeProps(
                width=8,
                lsb=8, msb=15,
                low=8, high=15),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.f1',
            inst_name='f1',
            field_type=int)
        self.__f2:FieldReadWrite = FieldReadWrite(
            parent_register=self,
            size_props=FieldSizeProps(
                width=8,
                lsb=16, msb=23,
                low=16, high=23),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.f2',
            inst_name='f2',
            field_type=int)
        self.__f3:FieldReadWrite = FieldReadWrite(
            parent_register=self,
            size_props=FieldSizeProps(
                width=8,
                lsb=24, msb=31,
                low=24, high=31),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.f3',
            inst_name='f3',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def f0(self) -> FieldReadWrite:
        """
        Property to access f0 field of the register

        
        """
        return self.__f0
    @property
    def f1(self) -> FieldReadWrite:
        """
        Property to access f1 field of the register

        
        """
        return self.__f1
    @property
    def f2(self) -> FieldReadWrite:
        """
        Property to access f2 field of the register

        
        """
        return self.__f2
    @property
    def f3(self) -> FieldReadWrite:
        """
        Property to access f3 field of the register

        
        """
        return self.__f3

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'f0':'f0','f1':'f1','f2':'f2','f3':'f3',
            }

    
    
    
    
    
    
    # nodes:4
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["f0"]) -> 'FieldReadWrite': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["f1"]) -> 'FieldReadWrite': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["f2"]) -> 'FieldReadWrite': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["f3"]) -> 'FieldReadWrite': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['FieldReadWrite', 'FieldReadWrite', 'FieldReadWrite', 'FieldReadWrite', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.f0
        yield self.f1
        yield self.f2
        yield self.f3
        
        
    

    
    
class openenoc_endpoint_info_neg_0x144752e7bb25972e_cls(RegReadOnly):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint1.info                                                 |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Read-only information register for this openENOC Endpoint       |
    |              |      Interface instance.</p>                                            |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__rmem_total_depth', '__num_of_peers']

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
        
        self.__rmem_total_depth:openenoc_endpoint_info_rmem_total_depth_neg_0x48394dfae72caedc_cls = openenoc_endpoint_info_rmem_total_depth_neg_0x48394dfae72caedc_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=16,
                lsb=0, msb=15,
                low=0, high=15),
            misc_props=FieldMiscProps(
                default=256,
                is_volatile=False),
            logger_handle=logger_handle+'.rmem_total_depth',
            inst_name='rmem_total_depth',
            field_type=int)
        self.__num_of_peers:openenoc_endpoint_info_num_of_peers_neg_0x72a743a2ee31bcb1_cls = openenoc_endpoint_info_num_of_peers_neg_0x72a743a2ee31bcb1_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=16,
                lsb=16, msb=31,
                low=16, high=31),
            misc_props=FieldMiscProps(
                default=4,
                is_volatile=False),
            logger_handle=logger_handle+'.num_of_peers',
            inst_name='num_of_peers',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def rmem_total_depth(self) -> openenoc_endpoint_info_rmem_total_depth_neg_0x48394dfae72caedc_cls:
        """
        Property to access rmem_total_depth field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint1.info.rmem_total_depth[15:0]                          |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Total depth of the shared memory region for all remote peers.   |
        |              |      This field reflects the RMEM_TOTAL_DEPTH parameter value.</p>      |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__rmem_total_depth
    @property
    def num_of_peers(self) -> openenoc_endpoint_info_num_of_peers_neg_0x72a743a2ee31bcb1_cls:
        """
        Property to access num_of_peers field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint1.info.num_of_peers[31:16]                             |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Number of remote peers supported by this openENOC Endpoint      |
        |              |      Interface instance. This field reflects the NUM_OF_PEERS parameter |
        |              |      value.</p>                                                         |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__num_of_peers

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'rmem_total_depth':'rmem_total_depth','num_of_peers':'num_of_peers',
            }

    
    
    
    
    
    
    # nodes:2
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["rmem_total_depth"]) -> 'openenoc_endpoint_info_rmem_total_depth_neg_0x48394dfae72caedc_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["num_of_peers"]) -> 'openenoc_endpoint_info_num_of_peers_neg_0x72a743a2ee31bcb1_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_info_rmem_total_depth_neg_0x48394dfae72caedc_cls', 'openenoc_endpoint_info_num_of_peers_neg_0x72a743a2ee31bcb1_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint1.info"
    @property
    def rdl_desc(self) -> str:
        return "Read-only information register for this openENOC Endpoint Interface instance."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.rmem_total_depth
        yield self.num_of_peers
        
        
    

    
    
class openenoc_endpoint_config_mac_address_0x61d2410acce79936_cls(RegReadWrite):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint1.config.mac_address                                   |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Local site 48-bit destination MAC address.</p>                  |
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
        
        self.__lo_word:openenoc_endpoint_config_mac_address_lo_word_neg_0x4c4cc56940c7b20a_cls = openenoc_endpoint_config_mac_address_lo_word_neg_0x4c4cc56940c7b20a_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0, msb=31,
                low=0, high=31),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=True),
            logger_handle=logger_handle+'.lo_word',
            inst_name='lo_word',
            field_type=int)
        self.__hi_word:openenoc_endpoint_config_mac_address_hi_word_0x3da0938188475d96_cls = openenoc_endpoint_config_mac_address_hi_word_0x3da0938188475d96_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=16,
                lsb=32, msb=47,
                low=32, high=47),
            misc_props=FieldMiscProps(
                default=0,
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
    def lo_word(self) -> openenoc_endpoint_config_mac_address_lo_word_neg_0x4c4cc56940c7b20a_cls:
        """
        Property to access lo_word field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint1.config.mac_address.lo_word[31:0]                     |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Lower 32 bits [31:0] of the 48-bit MAC address.</p>             |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__lo_word
    @property
    def hi_word(self) -> openenoc_endpoint_config_mac_address_hi_word_0x3da0938188475d96_cls:
        """
        Property to access hi_word field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint1.config.mac_address.hi_word[47:32]                    |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Upper 16 bits [47:32] of the 48-bit MAC address.</p>            |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__hi_word

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'lo_word':'lo_word','hi_word':'hi_word',
            }

    
    
    
    
    
    
    # nodes:2
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["lo_word"]) -> 'openenoc_endpoint_config_mac_address_lo_word_neg_0x4c4cc56940c7b20a_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["hi_word"]) -> 'openenoc_endpoint_config_mac_address_hi_word_0x3da0938188475d96_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_config_mac_address_lo_word_neg_0x4c4cc56940c7b20a_cls', 'openenoc_endpoint_config_mac_address_hi_word_0x3da0938188475d96_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint1.config.mac_address"
    @property
    def rdl_desc(self) -> str:
        return "Local site 48-bit destination MAC address."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.lo_word
        yield self.hi_word
        
        
    

    
    
class openenoc_endpoint_peers_entry_mac_address_neg_0x8f48d8633492ed4_cls(RegReadWrite):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].mac_address           |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Remote peer 48-bit destination MAC address.</p>                 |
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
        
        self.__lo_word:openenoc_endpoint_peers_entry_mac_address_lo_word_0x62051156f51d0c25_cls = openenoc_endpoint_peers_entry_mac_address_lo_word_0x62051156f51d0c25_cls(
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
        self.__hi_word:openenoc_endpoint_peers_entry_mac_address_hi_word_0x5ad3a0cf7a9bb51a_cls = openenoc_endpoint_peers_entry_mac_address_hi_word_0x5ad3a0cf7a9bb51a_cls(
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
    def lo_word(self) -> openenoc_endpoint_peers_entry_mac_address_lo_word_0x62051156f51d0c25_cls:
        """
        Property to access lo_word field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint1.peers.entry[0..NUM_OF_PEERS-                         |
        |              |      1].mac_address.lo_word[31:0]                                       |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Lower 32 bits [31:0] of the 48-bit MAC address.</p>             |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__lo_word
    @property
    def hi_word(self) -> openenoc_endpoint_peers_entry_mac_address_hi_word_0x5ad3a0cf7a9bb51a_cls:
        """
        Property to access hi_word field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint1.peers.entry[0..NUM_OF_PEERS-                         |
        |              |      1].mac_address.hi_word[47:32]                                      |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Upper 16 bits [47:32] of the 48-bit MAC address.</p>            |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__hi_word

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'lo_word':'lo_word','hi_word':'hi_word',
            }

    
    
    
    
    
    
    # nodes:2
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["lo_word"]) -> 'openenoc_endpoint_peers_entry_mac_address_lo_word_0x62051156f51d0c25_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["hi_word"]) -> 'openenoc_endpoint_peers_entry_mac_address_hi_word_0x5ad3a0cf7a9bb51a_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_peers_entry_mac_address_lo_word_0x62051156f51d0c25_cls', 'openenoc_endpoint_peers_entry_mac_address_hi_word_0x5ad3a0cf7a9bb51a_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].mac_address"
    @property
    def rdl_desc(self) -> str:
        return "Remote peer 48-bit destination MAC address."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.lo_word
        yield self.hi_word
        
        
    

    
    
class openenoc_endpoint_peers_entry_rmem_address_neg_0x62c0b86882179d7e_cls(RegReadWrite):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].rmem_address          |
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
        
        self.__offset:openenoc_endpoint_peers_entry_rmem_address_offset_0xd6c90bcd521e9a7_cls = openenoc_endpoint_peers_entry_rmem_address_offset_0xd6c90bcd521e9a7_cls(
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
    def offset(self) -> openenoc_endpoint_peers_entry_rmem_address_offset_0xd6c90bcd521e9a7_cls:
        """
        Property to access offset field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint1.peers.entry[0..NUM_OF_PEERS-                         |
        |              |      1].rmem_address.offset[31:0]                                       |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>32-bit address offset of the virtual memory region              |
        |              |      corresponding to the remote peer's memory.</p>                     |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__offset

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'offset':'offset',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_peers_entry_rmem_address_offset_0xd6c90bcd521e9a7_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].rmem_address"
    @property
    def rdl_desc(self) -> str:
        return "Address offset of the virtual memory region corresponding to the remote peer\u0027s memory."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.offset
        
        
    

    
    
class openenoc_endpoint_peers_entry_local_address_0x5e831e10b41c6fb_cls(RegReadWrite):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].local_address         |
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
        
        self.__base:openenoc_endpoint_peers_entry_local_address_base_0x646a7692e00c9edb_cls = openenoc_endpoint_peers_entry_local_address_base_0x646a7692e00c9edb_cls(
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
    def base(self) -> openenoc_endpoint_peers_entry_local_address_base_0x646a7692e00c9edb_cls:
        """
        Property to access base field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint1.peers.entry[0..NUM_OF_PEERS-                         |
        |              |      1].local_address.base[31:0]                                        |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>32-bit start address of the local memory region for DMA         |
        |              |      transfers.</p>                                                     |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__base

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'base':'base',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_peers_entry_local_address_base_0x646a7692e00c9edb_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].local_address"
    @property
    def rdl_desc(self) -> str:
        return "Start address of the local memory region for DMA transfers."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.base
        
        
    

    
    
class openenoc_endpoint_peers_entry_remote_address_neg_0x223e1b6047fd79a0_cls(RegReadWrite):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].remote_address        |
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
        
        self.__base:openenoc_endpoint_peers_entry_remote_address_base_neg_0x7ab289b4ae316a1d_cls = openenoc_endpoint_peers_entry_remote_address_base_neg_0x7ab289b4ae316a1d_cls(
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
    def base(self) -> openenoc_endpoint_peers_entry_remote_address_base_neg_0x7ab289b4ae316a1d_cls:
        """
        Property to access base field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint1.peers.entry[0..NUM_OF_PEERS-                         |
        |              |      1].remote_address.base[31:0]                                       |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>32-bit start address of the remote peer's memory region.</p>    |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__base

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'base':'base',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_peers_entry_remote_address_base_neg_0x7ab289b4ae316a1d_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].remote_address"
    @property
    def rdl_desc(self) -> str:
        return "Start address of the remote peer\u0027s memory region."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.base
        
        
    

    
    
class openenoc_endpoint_peers_entry_size_0x2d529c5bcdde579c_cls(RegReadWrite):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].size                  |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Size of the remote peer's memory region.</p>                    |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__value']

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
        
        self.__value:openenoc_endpoint_peers_entry_size_value_neg_0x4e9e0c98c704f31e_cls = openenoc_endpoint_peers_entry_size_value_neg_0x4e9e0c98c704f31e_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0, msb=31,
                low=0, high=31),
            misc_props=FieldMiscProps(
                default=None,
                is_volatile=False),
            logger_handle=logger_handle+'.value',
            inst_name='value',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def value(self) -> openenoc_endpoint_peers_entry_size_value_neg_0x4e9e0c98c704f31e_cls:
        """
        Property to access value field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].size.value[31:0]      |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>32-bit size of the remote peer's memory region.</p>             |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__value

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'value':'value',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_peers_entry_size_value_neg_0x4e9e0c98c704f31e_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].size"
    @property
    def rdl_desc(self) -> str:
        return "Size of the remote peer\u0027s memory region."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.value
        
        
    

    
    
class openenoc_endpoint_peers_entry_dma_config_0x43b8a83f649220e2_cls(RegReadWrite):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].dma_config            |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>DMA configuration for the remote peer.</p>                      |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__mode']

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
        
        self.__mode:openenoc_endpoint_peers_entry_dma_config_mode_0x5fd986b44e4735b1_cls = openenoc_endpoint_peers_entry_dma_config_mode_0x5fd986b44e4735b1_cls(
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

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def mode(self) -> openenoc_endpoint_peers_entry_dma_config_mode_0x5fd986b44e4735b1_cls:
        """
        Property to access mode field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].dma_config.mode[1:0]  |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>DMA mode for transfers to/from the remote peer:<ul></p> <li>0:  |
        |              |      DMA transfers to/from the remote peer are disabled.</li> <li>1:    |
        |              |      DMA transfers to/from the remote peer are enabled in transparent   |
        |              |      mode, where accesses to the virtual memory region are directly     |
        |              |      translated to corresponding accesses to the remote peer's memory   |
        |              |      region (transactions are word-by-word, i.e., per virtual memory    |
        |              |      access).</li> <li>2: DMA transfers to/from the remote peer are     |
        |              |      enabled in mirror-to-local mode, where the local memory region is  |
        |              |      used instead of the virtual memory region. The state of the remote |
        |              |      peer's memory region (remote_address, size) is fetched from the    |
        |              |      remote peer on demand or periodically.</li> <li>3: DMA transfers   |
        |              |      to/from the remote peer are enabled in mirror-to-remote mode,      |
        |              |      where the remote memory region is used instead of the virtual      |
        |              |      memory region. The state of the local peer's memory region         |
        |              |      (local_address, size) is sent to the remote peer on demand or      |
        |              |      periodically.</li> </ul>                                           |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__mode

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'mode':'mode',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_peers_entry_dma_config_mode_0x5fd986b44e4735b1_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].dma_config"
    @property
    def rdl_desc(self) -> str:
        return "DMA configuration for the remote peer."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.mode
        
        
    

    
    
class openenoc_endpoint_info_neg_0x7b286401d99eb76f_cls(RegReadOnly):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint2.info                                                 |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Read-only information register for this openENOC Endpoint       |
    |              |      Interface instance.</p>                                            |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__rmem_total_depth', '__num_of_peers']

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
        
        self.__rmem_total_depth:openenoc_endpoint_info_rmem_total_depth_neg_0x4876a1e84ba7ada7_cls = openenoc_endpoint_info_rmem_total_depth_neg_0x4876a1e84ba7ada7_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=16,
                lsb=0, msb=15,
                low=0, high=15),
            misc_props=FieldMiscProps(
                default=128,
                is_volatile=False),
            logger_handle=logger_handle+'.rmem_total_depth',
            inst_name='rmem_total_depth',
            field_type=int)
        self.__num_of_peers:openenoc_endpoint_info_num_of_peers_0x24f0b4c224afddb6_cls = openenoc_endpoint_info_num_of_peers_0x24f0b4c224afddb6_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=16,
                lsb=16, msb=31,
                low=16, high=31),
            misc_props=FieldMiscProps(
                default=2,
                is_volatile=False),
            logger_handle=logger_handle+'.num_of_peers',
            inst_name='num_of_peers',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def rmem_total_depth(self) -> openenoc_endpoint_info_rmem_total_depth_neg_0x4876a1e84ba7ada7_cls:
        """
        Property to access rmem_total_depth field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint2.info.rmem_total_depth[15:0]                          |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Total depth of the shared memory region for all remote peers.   |
        |              |      This field reflects the RMEM_TOTAL_DEPTH parameter value.</p>      |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__rmem_total_depth
    @property
    def num_of_peers(self) -> openenoc_endpoint_info_num_of_peers_0x24f0b4c224afddb6_cls:
        """
        Property to access num_of_peers field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint2.info.num_of_peers[31:16]                             |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Number of remote peers supported by this openENOC Endpoint      |
        |              |      Interface instance. This field reflects the NUM_OF_PEERS parameter |
        |              |      value.</p>                                                         |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__num_of_peers

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'rmem_total_depth':'rmem_total_depth','num_of_peers':'num_of_peers',
            }

    
    
    
    
    
    
    # nodes:2
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["rmem_total_depth"]) -> 'openenoc_endpoint_info_rmem_total_depth_neg_0x4876a1e84ba7ada7_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["num_of_peers"]) -> 'openenoc_endpoint_info_num_of_peers_0x24f0b4c224afddb6_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_info_rmem_total_depth_neg_0x4876a1e84ba7ada7_cls', 'openenoc_endpoint_info_num_of_peers_0x24f0b4c224afddb6_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint2.info"
    @property
    def rdl_desc(self) -> str:
        return "Read-only information register for this openENOC Endpoint Interface instance."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.rmem_total_depth
        yield self.num_of_peers
        
        
    

    
    
class openenoc_endpoint_config_mac_address_neg_0x569317322d004cae_cls(RegReadWrite):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint2.config.mac_address                                   |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Local site 48-bit destination MAC address.</p>                  |
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
        
        self.__lo_word:openenoc_endpoint_config_mac_address_lo_word_neg_0x627fd53fbffa4147_cls = openenoc_endpoint_config_mac_address_lo_word_neg_0x627fd53fbffa4147_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0, msb=31,
                low=0, high=31),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=True),
            logger_handle=logger_handle+'.lo_word',
            inst_name='lo_word',
            field_type=int)
        self.__hi_word:openenoc_endpoint_config_mac_address_hi_word_neg_0x6fe723c1622c5f8e_cls = openenoc_endpoint_config_mac_address_hi_word_neg_0x6fe723c1622c5f8e_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=16,
                lsb=32, msb=47,
                low=32, high=47),
            misc_props=FieldMiscProps(
                default=0,
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
    def lo_word(self) -> openenoc_endpoint_config_mac_address_lo_word_neg_0x627fd53fbffa4147_cls:
        """
        Property to access lo_word field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint2.config.mac_address.lo_word[31:0]                     |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Lower 32 bits [31:0] of the 48-bit MAC address.</p>             |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__lo_word
    @property
    def hi_word(self) -> openenoc_endpoint_config_mac_address_hi_word_neg_0x6fe723c1622c5f8e_cls:
        """
        Property to access hi_word field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint2.config.mac_address.hi_word[47:32]                    |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Upper 16 bits [47:32] of the 48-bit MAC address.</p>            |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__hi_word

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'lo_word':'lo_word','hi_word':'hi_word',
            }

    
    
    
    
    
    
    # nodes:2
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["lo_word"]) -> 'openenoc_endpoint_config_mac_address_lo_word_neg_0x627fd53fbffa4147_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["hi_word"]) -> 'openenoc_endpoint_config_mac_address_hi_word_neg_0x6fe723c1622c5f8e_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_config_mac_address_lo_word_neg_0x627fd53fbffa4147_cls', 'openenoc_endpoint_config_mac_address_hi_word_neg_0x6fe723c1622c5f8e_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint2.config.mac_address"
    @property
    def rdl_desc(self) -> str:
        return "Local site 48-bit destination MAC address."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.lo_word
        yield self.hi_word
        
        
    

    
    
class openenoc_endpoint_peers_entry_mac_address_0x4c3b9bf94c15fd1e_cls(RegReadWrite):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].mac_address           |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Remote peer 48-bit destination MAC address.</p>                 |
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
        
        self.__lo_word:openenoc_endpoint_peers_entry_mac_address_lo_word_neg_0x3f203d0bb09e8cac_cls = openenoc_endpoint_peers_entry_mac_address_lo_word_neg_0x3f203d0bb09e8cac_cls(
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
        self.__hi_word:openenoc_endpoint_peers_entry_mac_address_hi_word_neg_0x5d4950358d3f9612_cls = openenoc_endpoint_peers_entry_mac_address_hi_word_neg_0x5d4950358d3f9612_cls(
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
    def lo_word(self) -> openenoc_endpoint_peers_entry_mac_address_lo_word_neg_0x3f203d0bb09e8cac_cls:
        """
        Property to access lo_word field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint2.peers.entry[0..NUM_OF_PEERS-                         |
        |              |      1].mac_address.lo_word[31:0]                                       |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Lower 32 bits [31:0] of the 48-bit MAC address.</p>             |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__lo_word
    @property
    def hi_word(self) -> openenoc_endpoint_peers_entry_mac_address_hi_word_neg_0x5d4950358d3f9612_cls:
        """
        Property to access hi_word field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint2.peers.entry[0..NUM_OF_PEERS-                         |
        |              |      1].mac_address.hi_word[47:32]                                      |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Upper 16 bits [47:32] of the 48-bit MAC address.</p>            |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__hi_word

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'lo_word':'lo_word','hi_word':'hi_word',
            }

    
    
    
    
    
    
    # nodes:2
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["lo_word"]) -> 'openenoc_endpoint_peers_entry_mac_address_lo_word_neg_0x3f203d0bb09e8cac_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["hi_word"]) -> 'openenoc_endpoint_peers_entry_mac_address_hi_word_neg_0x5d4950358d3f9612_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_peers_entry_mac_address_lo_word_neg_0x3f203d0bb09e8cac_cls', 'openenoc_endpoint_peers_entry_mac_address_hi_word_neg_0x5d4950358d3f9612_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].mac_address"
    @property
    def rdl_desc(self) -> str:
        return "Remote peer 48-bit destination MAC address."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.lo_word
        yield self.hi_word
        
        
    

    
    
class openenoc_endpoint_peers_entry_rmem_address_neg_0x6dc3b4f7bdc64903_cls(RegReadWrite):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].rmem_address          |
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
        
        self.__offset:openenoc_endpoint_peers_entry_rmem_address_offset_neg_0x58778d0fb7848bc3_cls = openenoc_endpoint_peers_entry_rmem_address_offset_neg_0x58778d0fb7848bc3_cls(
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
    def offset(self) -> openenoc_endpoint_peers_entry_rmem_address_offset_neg_0x58778d0fb7848bc3_cls:
        """
        Property to access offset field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint2.peers.entry[0..NUM_OF_PEERS-                         |
        |              |      1].rmem_address.offset[31:0]                                       |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>32-bit address offset of the virtual memory region              |
        |              |      corresponding to the remote peer's memory.</p>                     |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__offset

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'offset':'offset',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_peers_entry_rmem_address_offset_neg_0x58778d0fb7848bc3_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].rmem_address"
    @property
    def rdl_desc(self) -> str:
        return "Address offset of the virtual memory region corresponding to the remote peer\u0027s memory."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.offset
        
        
    

    
    
class openenoc_endpoint_peers_entry_local_address_neg_0x1d5d26465448b9a9_cls(RegReadWrite):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].local_address         |
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
        
        self.__base:openenoc_endpoint_peers_entry_local_address_base_0xffb3c6e49bfcbde_cls = openenoc_endpoint_peers_entry_local_address_base_0xffb3c6e49bfcbde_cls(
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
    def base(self) -> openenoc_endpoint_peers_entry_local_address_base_0xffb3c6e49bfcbde_cls:
        """
        Property to access base field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint2.peers.entry[0..NUM_OF_PEERS-                         |
        |              |      1].local_address.base[31:0]                                        |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>32-bit start address of the local memory region for DMA         |
        |              |      transfers.</p>                                                     |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__base

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'base':'base',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_peers_entry_local_address_base_0xffb3c6e49bfcbde_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].local_address"
    @property
    def rdl_desc(self) -> str:
        return "Start address of the local memory region for DMA transfers."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.base
        
        
    

    
    
class openenoc_endpoint_peers_entry_remote_address_0x6cf8d7f42e54136a_cls(RegReadWrite):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].remote_address        |
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
        
        self.__base:openenoc_endpoint_peers_entry_remote_address_base_neg_0x1fb1ec1313d0d7a6_cls = openenoc_endpoint_peers_entry_remote_address_base_neg_0x1fb1ec1313d0d7a6_cls(
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
    def base(self) -> openenoc_endpoint_peers_entry_remote_address_base_neg_0x1fb1ec1313d0d7a6_cls:
        """
        Property to access base field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint2.peers.entry[0..NUM_OF_PEERS-                         |
        |              |      1].remote_address.base[31:0]                                       |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>32-bit start address of the remote peer's memory region.</p>    |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__base

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'base':'base',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_peers_entry_remote_address_base_neg_0x1fb1ec1313d0d7a6_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].remote_address"
    @property
    def rdl_desc(self) -> str:
        return "Start address of the remote peer\u0027s memory region."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.base
        
        
    

    
    
class openenoc_endpoint_peers_entry_size_0x27118595bf8e91c1_cls(RegReadWrite):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].size                  |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Size of the remote peer's memory region.</p>                    |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__value']

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
        
        self.__value:openenoc_endpoint_peers_entry_size_value_neg_0x18d87c0234b85b3d_cls = openenoc_endpoint_peers_entry_size_value_neg_0x18d87c0234b85b3d_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0, msb=31,
                low=0, high=31),
            misc_props=FieldMiscProps(
                default=None,
                is_volatile=False),
            logger_handle=logger_handle+'.value',
            inst_name='value',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def value(self) -> openenoc_endpoint_peers_entry_size_value_neg_0x18d87c0234b85b3d_cls:
        """
        Property to access value field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].size.value[31:0]      |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>32-bit size of the remote peer's memory region.</p>             |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__value

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'value':'value',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_peers_entry_size_value_neg_0x18d87c0234b85b3d_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].size"
    @property
    def rdl_desc(self) -> str:
        return "Size of the remote peer\u0027s memory region."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.value
        
        
    

    
    
class openenoc_endpoint_peers_entry_dma_config_0x673d7a78ab6c7374_cls(RegReadWrite):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].dma_config            |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>DMA configuration for the remote peer.</p>                      |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__mode']

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
        
        self.__mode:openenoc_endpoint_peers_entry_dma_config_mode_neg_0x3a4a53270195223f_cls = openenoc_endpoint_peers_entry_dma_config_mode_neg_0x3a4a53270195223f_cls(
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

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def mode(self) -> openenoc_endpoint_peers_entry_dma_config_mode_neg_0x3a4a53270195223f_cls:
        """
        Property to access mode field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].dma_config.mode[1:0]  |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>DMA mode for transfers to/from the remote peer:<ul></p> <li>0:  |
        |              |      DMA transfers to/from the remote peer are disabled.</li> <li>1:    |
        |              |      DMA transfers to/from the remote peer are enabled in transparent   |
        |              |      mode, where accesses to the virtual memory region are directly     |
        |              |      translated to corresponding accesses to the remote peer's memory   |
        |              |      region (transactions are word-by-word, i.e., per virtual memory    |
        |              |      access).</li> <li>2: DMA transfers to/from the remote peer are     |
        |              |      enabled in mirror-to-local mode, where the local memory region is  |
        |              |      used instead of the virtual memory region. The state of the remote |
        |              |      peer's memory region (remote_address, size) is fetched from the    |
        |              |      remote peer on demand or periodically.</li> <li>3: DMA transfers   |
        |              |      to/from the remote peer are enabled in mirror-to-remote mode,      |
        |              |      where the remote memory region is used instead of the virtual      |
        |              |      memory region. The state of the local peer's memory region         |
        |              |      (local_address, size) is sent to the remote peer on demand or      |
        |              |      periodically.</li> </ul>                                           |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__mode

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'mode':'mode',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_peers_entry_dma_config_mode_neg_0x3a4a53270195223f_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].dma_config"
    @property
    def rdl_desc(self) -> str:
        return "DMA configuration for the remote peer."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.mode
        
        
    

    
    
class openenoc_switch_info_0x339671246e70a307_cls(RegReadOnly):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.switch1.info                                                   |
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
        
        self.__table_depth:openenoc_switch_info_table_depth_0x5e4ef67b873ebaa7_cls = openenoc_switch_info_table_depth_0x5e4ef67b873ebaa7_cls(
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
        self.__num_of_interfaces:openenoc_switch_info_num_of_interfaces_0x4de2c66b36843eb3_cls = openenoc_switch_info_num_of_interfaces_0x4de2c66b36843eb3_cls(
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
    def table_depth(self) -> openenoc_switch_info_table_depth_0x5e4ef67b873ebaa7_cls:
        """
        Property to access table_depth field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.switch1.info.table_depth[15:0]                                 |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Depth of the forwarding table in this openENOC Switch instance. |
        |              |      This field reflects the TABLE_DEPTH parameter value.</p>           |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__table_depth
    @property
    def num_of_interfaces(self) -> openenoc_switch_info_num_of_interfaces_0x4de2c66b36843eb3_cls:
        """
        Property to access num_of_interfaces field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.switch1.info.num_of_interfaces[21:16]                          |
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
    def get_child_by_system_rdl_name(self, name: Literal["table_depth"]) -> 'openenoc_switch_info_table_depth_0x5e4ef67b873ebaa7_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["num_of_interfaces"]) -> 'openenoc_switch_info_num_of_interfaces_0x4de2c66b36843eb3_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_switch_info_table_depth_0x5e4ef67b873ebaa7_cls', 'openenoc_switch_info_num_of_interfaces_0x4de2c66b36843eb3_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.switch1.info"
    @property
    def rdl_desc(self) -> str:
        return "Read-only information register for this openENOC Switch instance."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.table_depth
        yield self.num_of_interfaces
        
        
    

    
    
class openenoc_switch_forwarding_control_neg_0x2f951cf3e4a74839_cls(RegReadWrite):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.switch1.forwarding_control                                     |
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
        
        self.__operation_mode:openenoc_switch_forwarding_control_operation_mode_0x79a73572aa97c5d9_cls = openenoc_switch_forwarding_control_operation_mode_0x79a73572aa97c5d9_cls(
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
        self.__pause_request:openenoc_switch_forwarding_control_pause_request_neg_0x744b08c36d37b451_cls = openenoc_switch_forwarding_control_pause_request_neg_0x744b08c36d37b451_cls(
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
        self.__pause_done:openenoc_switch_forwarding_control_pause_done_0x74a9d63a4df4691c_cls = openenoc_switch_forwarding_control_pause_done_0x74a9d63a4df4691c_cls(
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
    def operation_mode(self) -> openenoc_switch_forwarding_control_operation_mode_0x79a73572aa97c5d9_cls:
        """
        Property to access operation_mode field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.switch1.forwarding_control.operation_mode[0:0]                 |
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
    def pause_request(self) -> openenoc_switch_forwarding_control_pause_request_neg_0x744b08c36d37b451_cls:
        """
        Property to access pause_request field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.switch1.forwarding_control.pause_request[7:7]                  |
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
    def pause_done(self) -> openenoc_switch_forwarding_control_pause_done_0x74a9d63a4df4691c_cls:
        """
        Property to access pause_done field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.switch1.forwarding_control.pause_done[15:15]                   |
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
    def get_child_by_system_rdl_name(self, name: Literal["operation_mode"]) -> 'openenoc_switch_forwarding_control_operation_mode_0x79a73572aa97c5d9_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["pause_request"]) -> 'openenoc_switch_forwarding_control_pause_request_neg_0x744b08c36d37b451_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["pause_done"]) -> 'openenoc_switch_forwarding_control_pause_done_0x74a9d63a4df4691c_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_switch_forwarding_control_operation_mode_0x79a73572aa97c5d9_cls', 'openenoc_switch_forwarding_control_pause_request_neg_0x744b08c36d37b451_cls', 'openenoc_switch_forwarding_control_pause_done_0x74a9d63a4df4691c_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.switch1.forwarding_control"
    @property
    def rdl_desc(self) -> str:
        return "Forwarding control register for the openENOC Switch instance."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.operation_mode
        yield self.pause_request
        yield self.pause_done
        
        
    

    
    
class openenoc_switch_default_forwarding_0x37fa1bd5f8436f51_cls(RegReadWrite):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.switch1.default_forwarding                                     |
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
        
        self.__bitmap:openenoc_switch_default_forwarding_bitmap_neg_0x6727db7163315abd_cls = openenoc_switch_default_forwarding_bitmap_neg_0x6727db7163315abd_cls(
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
    def bitmap(self) -> openenoc_switch_default_forwarding_bitmap_neg_0x6727db7163315abd_cls:
        """
        Property to access bitmap field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.switch1.default_forwarding.bitmap[NUM_OF_INTERFACES-1:0]       |
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

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_switch_default_forwarding_bitmap_neg_0x6727db7163315abd_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.switch1.default_forwarding"
    @property
    def rdl_desc(self) -> str:
        return "Defines the destination interface or interfaces for frames that do not match any enabled forwarding table entry."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.bitmap
        
        
    

    
    
class openenoc_switch_forwarding_table_entry_mac_address_neg_0x7fbcf3beb5f1a482_cls(RegReadWrite):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address   |
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
        
        self.__lo_word:openenoc_switch_forwarding_table_entry_mac_address_lo_word_0x9564a1a009b9122_cls = openenoc_switch_forwarding_table_entry_mac_address_lo_word_0x9564a1a009b9122_cls(
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
        self.__hi_word:openenoc_switch_forwarding_table_entry_mac_address_hi_word_0x8d0840040004d52_cls = openenoc_switch_forwarding_table_entry_mac_address_hi_word_0x8d0840040004d52_cls(
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
    def lo_word(self) -> openenoc_switch_forwarding_table_entry_mac_address_lo_word_0x9564a1a009b9122_cls:
        """
        Property to access lo_word field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-                 |
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
    def hi_word(self) -> openenoc_switch_forwarding_table_entry_mac_address_hi_word_0x8d0840040004d52_cls:
        """
        Property to access hi_word field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-                 |
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
    def get_child_by_system_rdl_name(self, name: Literal["lo_word"]) -> 'openenoc_switch_forwarding_table_entry_mac_address_lo_word_0x9564a1a009b9122_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["hi_word"]) -> 'openenoc_switch_forwarding_table_entry_mac_address_hi_word_0x8d0840040004d52_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_switch_forwarding_table_entry_mac_address_lo_word_0x9564a1a009b9122_cls', 'openenoc_switch_forwarding_table_entry_mac_address_hi_word_0x8d0840040004d52_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address"
    @property
    def rdl_desc(self) -> str:
        return "48-bit destination MAC address used as the key for this forwarding table entry."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.lo_word
        yield self.hi_word
        
        
    

    
    
class openenoc_switch_forwarding_table_entry_iface_0x4831070b1dc215ed_cls(RegReadWrite):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].iface         |
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
        
        self.__bitmap:openenoc_switch_forwarding_table_entry_iface_bitmap_0x247fa91e0c44bc44_cls = openenoc_switch_forwarding_table_entry_iface_bitmap_0x247fa91e0c44bc44_cls(
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
    def bitmap(self) -> openenoc_switch_forwarding_table_entry_iface_bitmap_0x247fa91e0c44bc44_cls:
        """
        Property to access bitmap field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-                 |
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

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_switch_forwarding_table_entry_iface_bitmap_0x247fa91e0c44bc44_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].iface"
    @property
    def rdl_desc(self) -> str:
        return "Forwarding interface information associated with this forwarding table entry."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.bitmap
        
        
    

    
    
class openenoc_switch_forwarding_table_entry_config_0x66f5d3fa40fe4407_cls(RegReadWrite):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].config        |
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
        
        self.__enabled:openenoc_switch_forwarding_table_entry_config_enabled_neg_0x6a6e8c755744d830_cls = openenoc_switch_forwarding_table_entry_config_enabled_neg_0x6a6e8c755744d830_cls(
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
    def enabled(self) -> openenoc_switch_forwarding_table_entry_config_enabled_neg_0x6a6e8c755744d830_cls:
        """
        Property to access enabled field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-                 |
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

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_switch_forwarding_table_entry_config_enabled_neg_0x6a6e8c755744d830_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].config"
    @property
    def rdl_desc(self) -> str:
        return "Configuration information associated with this forwarding table entry."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.enabled
        
        
    

    
    
class openenoc_switch_info_0x376ad29c9d8132a8_cls(RegReadOnly):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.switch2.info                                                   |
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
        
        self.__table_depth:openenoc_switch_info_table_depth_neg_0x7c3efff0035202ba_cls = openenoc_switch_info_table_depth_neg_0x7c3efff0035202ba_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=16,
                lsb=0, msb=15,
                low=0, high=15),
            misc_props=FieldMiscProps(
                default=32,
                is_volatile=False),
            logger_handle=logger_handle+'.table_depth',
            inst_name='table_depth',
            field_type=int)
        self.__num_of_interfaces:openenoc_switch_info_num_of_interfaces_0x3f5005238df5ff7c_cls = openenoc_switch_info_num_of_interfaces_0x3f5005238df5ff7c_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=6,
                lsb=16, msb=21,
                low=16, high=21),
            misc_props=FieldMiscProps(
                default=8,
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
    def table_depth(self) -> openenoc_switch_info_table_depth_neg_0x7c3efff0035202ba_cls:
        """
        Property to access table_depth field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.switch2.info.table_depth[15:0]                                 |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Depth of the forwarding table in this openENOC Switch instance. |
        |              |      This field reflects the TABLE_DEPTH parameter value.</p>           |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__table_depth
    @property
    def num_of_interfaces(self) -> openenoc_switch_info_num_of_interfaces_0x3f5005238df5ff7c_cls:
        """
        Property to access num_of_interfaces field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.switch2.info.num_of_interfaces[21:16]                          |
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
    def get_child_by_system_rdl_name(self, name: Literal["table_depth"]) -> 'openenoc_switch_info_table_depth_neg_0x7c3efff0035202ba_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["num_of_interfaces"]) -> 'openenoc_switch_info_num_of_interfaces_0x3f5005238df5ff7c_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_switch_info_table_depth_neg_0x7c3efff0035202ba_cls', 'openenoc_switch_info_num_of_interfaces_0x3f5005238df5ff7c_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.switch2.info"
    @property
    def rdl_desc(self) -> str:
        return "Read-only information register for this openENOC Switch instance."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.table_depth
        yield self.num_of_interfaces
        
        
    


if __name__ == '__main__':
    pass