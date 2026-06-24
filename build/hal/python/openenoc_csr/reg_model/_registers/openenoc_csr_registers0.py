

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






from .fields import openenoc_csr_test_reg_test_field_0x5da54704c0098337_cls
from .fields import openenoc_endpoint_info_rmem_total_depth_0x1cc63c817352f45b_cls
from .fields import openenoc_endpoint_info_num_of_peers_0x308ccef6325eeeb2_cls
from .fields import openenoc_endpoint_config_mac_address_lo_word_neg_0x7e914f7c285fdd9f_cls
from .fields import openenoc_endpoint_config_mac_address_hi_word_neg_0x9c17c7eb3d6d599_cls
from .fields import openenoc_endpoint_axis_if_source_data_tdata_neg_0x735ff438dd219367_cls
from .fields import openenoc_endpoint_axis_if_source_control_tvalid_neg_0x38d204d6568c919a_cls
from .fields import openenoc_endpoint_axis_if_source_control_tlast_neg_0xed252c7cd08f74b_cls
from .fields import openenoc_endpoint_axis_if_source_status_tready_neg_0x565f8829c19a9abc_cls
from .fields import openenoc_endpoint_axis_if_sink_data_tdata_0x2d4029e55ca5e383_cls
from .fields import openenoc_endpoint_axis_if_sink_control_tready_0x76aadf497c2b595b_cls
from .fields import openenoc_endpoint_axis_if_sink_status_tvalid_neg_0x1e93c07b12fcc853_cls
from .fields import openenoc_endpoint_axis_if_sink_status_tlast_0x7e1169b86b56ea3d_cls
from .fields import openenoc_endpoint_peers_entry_mac_address_lo_word_0x42f2e91384b801da_cls
from .fields import openenoc_endpoint_peers_entry_mac_address_hi_word_neg_0x19e029f474334844_cls
from .fields import openenoc_endpoint_peers_entry_rmem_address_offset_neg_0x4cf06a245d51023a_cls
from .fields import openenoc_endpoint_peers_entry_local_address_base_0x76efbb6af4b42323_cls
from .fields import openenoc_endpoint_peers_entry_remote_address_base_neg_0x305270d085d4a06f_cls
from .fields import openenoc_endpoint_peers_entry_size_bytes_0x7ba0f2b5185f17d7_cls
from .fields import openenoc_endpoint_peers_entry_dma_mode_neg_0x63e0367ad46e6d32_cls
from .fields import openenoc_endpoint_peers_entry_dma_request_0x475295f51d5cf9b4_cls
from .fields import openenoc_endpoint_peers_entry_dma_idle_0x63728ad65860231b_cls
from .fields import openenoc_endpoint_peers_entry_dma_done_neg_0x679dd6917bc3fe5d_cls
from .fields import openenoc_endpoint_peers_entry_dma_error_0x518cdc9dfc4f183a_cls
from .fields import openenoc_endpoint_info_rmem_total_depth_neg_0x2d459d37235d65d5_cls
from .fields import openenoc_endpoint_info_num_of_peers_neg_0x2353d418c67aea7_cls
from .fields import openenoc_endpoint_config_mac_address_lo_word_neg_0x448f4357d313ac89_cls
from .fields import openenoc_endpoint_config_mac_address_hi_word_neg_0xb902f37a4d7a9c4_cls
from .fields import openenoc_endpoint_axis_if_source_data_tdata_neg_0x18651a6788374af0_cls
from .fields import openenoc_endpoint_axis_if_source_control_tvalid_neg_0x7693d3714677d2e2_cls
from .fields import openenoc_endpoint_axis_if_source_control_tlast_0x6f92ad91f9e86b57_cls
from .fields import openenoc_endpoint_axis_if_source_status_tready_neg_0x96c8ac4faeb1efd_cls
from .fields import openenoc_endpoint_axis_if_sink_data_tdata_neg_0x6490c579133ec028_cls
from .fields import openenoc_endpoint_axis_if_sink_control_tready_neg_0x42b52af8ff892e38_cls
from .fields import openenoc_endpoint_axis_if_sink_status_tvalid_neg_0x13672d8472c23bf5_cls
from .fields import openenoc_endpoint_axis_if_sink_status_tlast_0x1699db3a89e56b5a_cls
from .fields import openenoc_endpoint_peers_entry_mac_address_lo_word_neg_0x2d9dfd1a27a63014_cls
from .fields import openenoc_endpoint_peers_entry_mac_address_hi_word_neg_0x567d8034ecf5cbaf_cls

# register definitions
    
    
class openenoc_csr_test_reg_0x69f601ad22f2142_cls(RegReadWrite):
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
        
        self.__test_field:openenoc_csr_test_reg_test_field_0x5da54704c0098337_cls = openenoc_csr_test_reg_test_field_0x5da54704c0098337_cls(
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
    def test_field(self) -> openenoc_csr_test_reg_test_field_0x5da54704c0098337_cls:
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

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_csr_test_reg_test_field_0x5da54704c0098337_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.test_reg"
    @property
    def rdl_desc(self) -> str:
        return "Test register"
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.test_field
        
        
    

    
    
class openenoc_csr_regB_neg_0xe16f3a07eae63d6_cls(RegReadWrite):
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
        
        
    

    
    
class openenoc_endpoint_info_neg_0x735b88c1b28e8f33_cls(RegReadOnly):
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
        
        self.__rmem_total_depth:openenoc_endpoint_info_rmem_total_depth_0x1cc63c817352f45b_cls = openenoc_endpoint_info_rmem_total_depth_0x1cc63c817352f45b_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0, msb=31,
                low=0, high=31),
            misc_props=FieldMiscProps(
                default=256,
                is_volatile=False),
            logger_handle=logger_handle+'.rmem_total_depth',
            inst_name='rmem_total_depth',
            field_type=int)
        self.__num_of_peers:openenoc_endpoint_info_num_of_peers_0x308ccef6325eeeb2_cls = openenoc_endpoint_info_num_of_peers_0x308ccef6325eeeb2_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=32, msb=63,
                low=32, high=63),
            misc_props=FieldMiscProps(
                default=4,
                is_volatile=False),
            logger_handle=logger_handle+'.num_of_peers',
            inst_name='num_of_peers',
            field_type=int)

    @property
    def width(self) -> int:
        return 64

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def rmem_total_depth(self) -> openenoc_endpoint_info_rmem_total_depth_0x1cc63c817352f45b_cls:
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
    def num_of_peers(self) -> openenoc_endpoint_info_num_of_peers_0x308ccef6325eeeb2_cls:
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
    def get_child_by_system_rdl_name(self, name: Literal["rmem_total_depth"]) -> 'openenoc_endpoint_info_rmem_total_depth_0x1cc63c817352f45b_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["num_of_peers"]) -> 'openenoc_endpoint_info_num_of_peers_0x308ccef6325eeeb2_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_info_rmem_total_depth_0x1cc63c817352f45b_cls', 'openenoc_endpoint_info_num_of_peers_0x308ccef6325eeeb2_cls', ]: ...

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
        
        
    

    
    
class openenoc_endpoint_config_mac_address_neg_0x6ed055f4bee94bd2_cls(RegReadWrite):
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
        
        self.__lo_word:openenoc_endpoint_config_mac_address_lo_word_neg_0x7e914f7c285fdd9f_cls = openenoc_endpoint_config_mac_address_lo_word_neg_0x7e914f7c285fdd9f_cls(
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
        self.__hi_word:openenoc_endpoint_config_mac_address_hi_word_neg_0x9c17c7eb3d6d599_cls = openenoc_endpoint_config_mac_address_hi_word_neg_0x9c17c7eb3d6d599_cls(
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
    def lo_word(self) -> openenoc_endpoint_config_mac_address_lo_word_neg_0x7e914f7c285fdd9f_cls:
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
    def hi_word(self) -> openenoc_endpoint_config_mac_address_hi_word_neg_0x9c17c7eb3d6d599_cls:
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
    def get_child_by_system_rdl_name(self, name: Literal["lo_word"]) -> 'openenoc_endpoint_config_mac_address_lo_word_neg_0x7e914f7c285fdd9f_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["hi_word"]) -> 'openenoc_endpoint_config_mac_address_hi_word_neg_0x9c17c7eb3d6d599_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_config_mac_address_lo_word_neg_0x7e914f7c285fdd9f_cls', 'openenoc_endpoint_config_mac_address_hi_word_neg_0x9c17c7eb3d6d599_cls', ]: ...

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
        
        
    

    
    
class openenoc_endpoint_axis_if_source_data_0x2362d42deed0b943_cls(RegReadWrite):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint1.axis_if.source.data                                  |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Data register for the AXI4-Stream source interface.</p>         |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__tdata']

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
        
        self.__tdata:openenoc_endpoint_axis_if_source_data_tdata_neg_0x735ff438dd219367_cls = openenoc_endpoint_axis_if_source_data_tdata_neg_0x735ff438dd219367_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0, msb=31,
                low=0, high=31),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.tdata',
            inst_name='tdata',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def tdata(self) -> openenoc_endpoint_axis_if_source_data_tdata_neg_0x735ff438dd219367_cls:
        """
        Property to access tdata field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint1.axis_if.source.data.tdata[31:0]                      |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>32-bit data value for the AXI4-Stream source interface.</p>     |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__tdata

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'tdata':'tdata',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_axis_if_source_data_tdata_neg_0x735ff438dd219367_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint1.axis_if.source.data"
    @property
    def rdl_desc(self) -> str:
        return "Data register for the AXI4-Stream source interface."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.tdata
        
        
    

    
    
class openenoc_endpoint_axis_if_source_control_neg_0x1b2b7f048b6aeae_cls(RegReadWrite):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint1.axis_if.source.control                               |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Control register for the AXI4-Stream source interface.</p>      |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__tvalid', '__tlast']

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
        
        self.__tvalid:openenoc_endpoint_axis_if_source_control_tvalid_neg_0x38d204d6568c919a_cls = openenoc_endpoint_axis_if_source_control_tvalid_neg_0x38d204d6568c919a_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=0, msb=0,
                low=0, high=0),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.tvalid',
            inst_name='tvalid',
            field_type=int)
        self.__tlast:openenoc_endpoint_axis_if_source_control_tlast_neg_0xed252c7cd08f74b_cls = openenoc_endpoint_axis_if_source_control_tlast_neg_0xed252c7cd08f74b_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=8, msb=8,
                low=8, high=8),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.tlast',
            inst_name='tlast',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def tvalid(self) -> openenoc_endpoint_axis_if_source_control_tvalid_neg_0x38d204d6568c919a_cls:
        """
        Property to access tvalid field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint1.axis_if.source.control.tvalid                        |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Indicates that the AXI4-Stream source interface has valid data  |
        |              |      to send. This field is a single-pulse register that is             |
        |              |      automatically cleared back to zero after being written.</p>        |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__tvalid
    @property
    def tlast(self) -> openenoc_endpoint_axis_if_source_control_tlast_neg_0xed252c7cd08f74b_cls:
        """
        Property to access tlast field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint1.axis_if.source.control.tlast                         |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Indicates the last data word of a frame on the AXI4-Stream      |
        |              |      source interface.</p>                                              |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__tlast

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'tvalid':'tvalid','tlast':'tlast',
            }

    
    
    
    
    
    
    # nodes:2
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["tvalid"]) -> 'openenoc_endpoint_axis_if_source_control_tvalid_neg_0x38d204d6568c919a_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["tlast"]) -> 'openenoc_endpoint_axis_if_source_control_tlast_neg_0xed252c7cd08f74b_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_axis_if_source_control_tvalid_neg_0x38d204d6568c919a_cls', 'openenoc_endpoint_axis_if_source_control_tlast_neg_0xed252c7cd08f74b_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint1.axis_if.source.control"
    @property
    def rdl_desc(self) -> str:
        return "Control register for the AXI4-Stream source interface."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.tvalid
        yield self.tlast
        
        
    

    
    
class openenoc_endpoint_axis_if_source_status_neg_0xfee0a2f3b74c649_cls(RegReadOnly):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint1.axis_if.source.status                                |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Status register for the AXI4-Stream source interface.</p>       |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__tready']

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
        
        self.__tready:openenoc_endpoint_axis_if_source_status_tready_neg_0x565f8829c19a9abc_cls = openenoc_endpoint_axis_if_source_status_tready_neg_0x565f8829c19a9abc_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=0, msb=0,
                low=0, high=0),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=True),
            logger_handle=logger_handle+'.tready',
            inst_name='tready',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def tready(self) -> openenoc_endpoint_axis_if_source_status_tready_neg_0x565f8829c19a9abc_cls:
        """
        Property to access tready field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint1.axis_if.source.status.tready                         |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Indicates that the destination AXI4-Stream interface is ready   |
        |              |      to receive data.</p>                                               |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__tready

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'tready':'tready',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_axis_if_source_status_tready_neg_0x565f8829c19a9abc_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint1.axis_if.source.status"
    @property
    def rdl_desc(self) -> str:
        return "Status register for the AXI4-Stream source interface."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.tready
        
        
    

    
    
class openenoc_endpoint_axis_if_sink_data_0x2565dea76eeba99d_cls(RegReadOnly):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint1.axis_if.sink.data                                    |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Data register for the AXI4-Stream sink interface.</p>           |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__tdata']

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
        
        self.__tdata:openenoc_endpoint_axis_if_sink_data_tdata_0x2d4029e55ca5e383_cls = openenoc_endpoint_axis_if_sink_data_tdata_0x2d4029e55ca5e383_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0, msb=31,
                low=0, high=31),
            misc_props=FieldMiscProps(
                default=None,
                is_volatile=True),
            logger_handle=logger_handle+'.tdata',
            inst_name='tdata',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def tdata(self) -> openenoc_endpoint_axis_if_sink_data_tdata_0x2d4029e55ca5e383_cls:
        """
        Property to access tdata field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint1.axis_if.sink.data.tdata[31:0]                        |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>32-bit data value for the AXI4-Stream sink interface.</p>       |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__tdata

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'tdata':'tdata',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_axis_if_sink_data_tdata_0x2d4029e55ca5e383_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint1.axis_if.sink.data"
    @property
    def rdl_desc(self) -> str:
        return "Data register for the AXI4-Stream sink interface."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.tdata
        
        
    

    
    
class openenoc_endpoint_axis_if_sink_control_0x2fa17f6b8f2565d1_cls(RegWriteOnly):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint1.axis_if.sink.control                                 |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Control register for the AXI4-Stream sink interface.</p>        |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__tready']

    def __init__(self,
                 address: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AddressMap,RegFile,WritableMemory]):

        super().__init__(address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__tready:openenoc_endpoint_axis_if_sink_control_tready_0x76aadf497c2b595b_cls = openenoc_endpoint_axis_if_sink_control_tready_0x76aadf497c2b595b_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=0, msb=0,
                low=0, high=0),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.tready',
            inst_name='tready',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    
    
    def write_fields(self,tready : int) -> None: # type: ignore[override]
        """
        Do a write to the register, updating all fields
        """
        reg_value = 0
        reg_value &= self.tready.inverse_bitmask
        reg_value |= self.tready._encode_write_value(tready)
        

        self.write(reg_value)

    

    # build the properties for the fields
    
    @property
    def tready(self) -> openenoc_endpoint_axis_if_sink_control_tready_0x76aadf497c2b595b_cls:
        """
        Property to access tready field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint1.axis_if.sink.control.tready                          |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Indicates that the AXI4-Stream sink interface is ready to       |
        |              |      receive next data transfer.</p>                                    |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__tready

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'tready':'tready',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_axis_if_sink_control_tready_0x76aadf497c2b595b_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint1.axis_if.sink.control"
    @property
    def rdl_desc(self) -> str:
        return "Control register for the AXI4-Stream sink interface."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.tready
        
        
    

    
    
class openenoc_endpoint_axis_if_sink_status_0x664a8cd7a8dcd9f1_cls(RegReadOnly):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint1.axis_if.sink.status                                  |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Status register for the AXI4-Stream sink interface.</p>         |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__tvalid', '__tlast']

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
        
        self.__tvalid:openenoc_endpoint_axis_if_sink_status_tvalid_neg_0x1e93c07b12fcc853_cls = openenoc_endpoint_axis_if_sink_status_tvalid_neg_0x1e93c07b12fcc853_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=0, msb=0,
                low=0, high=0),
            misc_props=FieldMiscProps(
                default=None,
                is_volatile=True),
            logger_handle=logger_handle+'.tvalid',
            inst_name='tvalid',
            field_type=int)
        self.__tlast:openenoc_endpoint_axis_if_sink_status_tlast_0x7e1169b86b56ea3d_cls = openenoc_endpoint_axis_if_sink_status_tlast_0x7e1169b86b56ea3d_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=8, msb=8,
                low=8, high=8),
            misc_props=FieldMiscProps(
                default=None,
                is_volatile=True),
            logger_handle=logger_handle+'.tlast',
            inst_name='tlast',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def tvalid(self) -> openenoc_endpoint_axis_if_sink_status_tvalid_neg_0x1e93c07b12fcc853_cls:
        """
        Property to access tvalid field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint1.axis_if.sink.status.tvalid                           |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Indicates that the AXI4-Stream sink interface has valid data to |
        |              |      receive.</p>                                                       |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__tvalid
    @property
    def tlast(self) -> openenoc_endpoint_axis_if_sink_status_tlast_0x7e1169b86b56ea3d_cls:
        """
        Property to access tlast field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint1.axis_if.sink.status.tlast                            |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Indicates the last data word of a frame on the AXI4-Stream sink |
        |              |      interface.</p>                                                     |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__tlast

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'tvalid':'tvalid','tlast':'tlast',
            }

    
    
    
    
    
    
    # nodes:2
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["tvalid"]) -> 'openenoc_endpoint_axis_if_sink_status_tvalid_neg_0x1e93c07b12fcc853_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["tlast"]) -> 'openenoc_endpoint_axis_if_sink_status_tlast_0x7e1169b86b56ea3d_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_axis_if_sink_status_tvalid_neg_0x1e93c07b12fcc853_cls', 'openenoc_endpoint_axis_if_sink_status_tlast_0x7e1169b86b56ea3d_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint1.axis_if.sink.status"
    @property
    def rdl_desc(self) -> str:
        return "Status register for the AXI4-Stream sink interface."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.tvalid
        yield self.tlast
        
        
    

    
    
class openenoc_endpoint_peers_entry_mac_address_0x78cedd86ea7d8cba_cls(RegReadWrite):
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
        
        self.__lo_word:openenoc_endpoint_peers_entry_mac_address_lo_word_0x42f2e91384b801da_cls = openenoc_endpoint_peers_entry_mac_address_lo_word_0x42f2e91384b801da_cls(
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
        self.__hi_word:openenoc_endpoint_peers_entry_mac_address_hi_word_neg_0x19e029f474334844_cls = openenoc_endpoint_peers_entry_mac_address_hi_word_neg_0x19e029f474334844_cls(
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
    def lo_word(self) -> openenoc_endpoint_peers_entry_mac_address_lo_word_0x42f2e91384b801da_cls:
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
    def hi_word(self) -> openenoc_endpoint_peers_entry_mac_address_hi_word_neg_0x19e029f474334844_cls:
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
    def get_child_by_system_rdl_name(self, name: Literal["lo_word"]) -> 'openenoc_endpoint_peers_entry_mac_address_lo_word_0x42f2e91384b801da_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["hi_word"]) -> 'openenoc_endpoint_peers_entry_mac_address_hi_word_neg_0x19e029f474334844_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_peers_entry_mac_address_lo_word_0x42f2e91384b801da_cls', 'openenoc_endpoint_peers_entry_mac_address_hi_word_neg_0x19e029f474334844_cls', ]: ...

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
        
        
    

    
    
class openenoc_endpoint_peers_entry_rmem_address_neg_0x6559b47b3208e18d_cls(RegReadWrite):
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
        
        self.__offset:openenoc_endpoint_peers_entry_rmem_address_offset_neg_0x4cf06a245d51023a_cls = openenoc_endpoint_peers_entry_rmem_address_offset_neg_0x4cf06a245d51023a_cls(
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
    def offset(self) -> openenoc_endpoint_peers_entry_rmem_address_offset_neg_0x4cf06a245d51023a_cls:
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
        |              |      <p>Word-aligned 32-bit address offset of the virtual memory region |
        |              |      corresponding to the remote peer's memory.</p>                     |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__offset

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'offset':'offset',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_peers_entry_rmem_address_offset_neg_0x4cf06a245d51023a_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].rmem_address"
    @property
    def rdl_desc(self) -> str:
        return "Address offset of the virtual memory region corresponding to the remote peer\u0027s memory."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.offset
        
        
    

    
    
class openenoc_endpoint_peers_entry_local_address_neg_0x49e3835772dee4dd_cls(RegReadWrite):
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
        
        self.__base:openenoc_endpoint_peers_entry_local_address_base_0x76efbb6af4b42323_cls = openenoc_endpoint_peers_entry_local_address_base_0x76efbb6af4b42323_cls(
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
    def base(self) -> openenoc_endpoint_peers_entry_local_address_base_0x76efbb6af4b42323_cls:
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
        |              |      <p>Word-aligned 32-bit start address of the local memory region    |
        |              |      for DMA transfers.</p>                                             |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__base

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'base':'base',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_peers_entry_local_address_base_0x76efbb6af4b42323_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].local_address"
    @property
    def rdl_desc(self) -> str:
        return "Start address of the local memory region for DMA transfers."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.base
        
        
    

    
    
class openenoc_endpoint_peers_entry_remote_address_neg_0x5a9e65567f65065a_cls(RegReadWrite):
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
        
        self.__base:openenoc_endpoint_peers_entry_remote_address_base_neg_0x305270d085d4a06f_cls = openenoc_endpoint_peers_entry_remote_address_base_neg_0x305270d085d4a06f_cls(
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
    def base(self) -> openenoc_endpoint_peers_entry_remote_address_base_neg_0x305270d085d4a06f_cls:
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
        |              |      <p>Word-aligned 32-bit start address of the remote peer's memory   |
        |              |      region.</p>                                                        |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__base

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'base':'base',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_peers_entry_remote_address_base_neg_0x305270d085d4a06f_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].remote_address"
    @property
    def rdl_desc(self) -> str:
        return "Start address of the remote peer\u0027s memory region."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.base
        
        
    

    
    
class openenoc_endpoint_peers_entry_size_neg_0x53f79c915dbb3e3f_cls(RegReadWrite):
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
        
        self.__bytes:openenoc_endpoint_peers_entry_size_bytes_0x7ba0f2b5185f17d7_cls = openenoc_endpoint_peers_entry_size_bytes_0x7ba0f2b5185f17d7_cls(
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
    def bytes(self) -> openenoc_endpoint_peers_entry_size_bytes_0x7ba0f2b5185f17d7_cls:
        """
        Property to access bytes field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].size.bytes[31:0]      |
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

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_peers_entry_size_bytes_0x7ba0f2b5185f17d7_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].size"
    @property
    def rdl_desc(self) -> str:
        return "Size of the remote peer\u0027s memory region."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.bytes
        
        
    

    
    
class openenoc_endpoint_peers_entry_dma_0x2d21abf34620e72b_cls(RegReadWrite):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].dma                   |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>DMA configuration and control for the remote peer.</p>          |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__mode', '__request', '__idle', '__done', '__error']

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
        
        self.__mode:openenoc_endpoint_peers_entry_dma_mode_neg_0x63e0367ad46e6d32_cls = openenoc_endpoint_peers_entry_dma_mode_neg_0x63e0367ad46e6d32_cls(
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
        self.__request:openenoc_endpoint_peers_entry_dma_request_0x475295f51d5cf9b4_cls = openenoc_endpoint_peers_entry_dma_request_0x475295f51d5cf9b4_cls(
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
        self.__idle:openenoc_endpoint_peers_entry_dma_idle_0x63728ad65860231b_cls = openenoc_endpoint_peers_entry_dma_idle_0x63728ad65860231b_cls(
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
        self.__done:openenoc_endpoint_peers_entry_dma_done_neg_0x679dd6917bc3fe5d_cls = openenoc_endpoint_peers_entry_dma_done_neg_0x679dd6917bc3fe5d_cls(
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
        self.__error:openenoc_endpoint_peers_entry_dma_error_0x518cdc9dfc4f183a_cls = openenoc_endpoint_peers_entry_dma_error_0x518cdc9dfc4f183a_cls(
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

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def mode(self) -> openenoc_endpoint_peers_entry_dma_mode_neg_0x63e0367ad46e6d32_cls:
        """
        Property to access mode field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].dma.mode[1:0]         |
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
    def request(self) -> openenoc_endpoint_peers_entry_dma_request_0x475295f51d5cf9b4_cls:
        """
        Property to access request field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].dma.request[8:8]      |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Writing a 1 to this field initiates a DMA transfer to/from the  |
        |              |      remote peer. This field is a single-pulse register that is         |
        |              |      automatically cleared back to zero after being written.</p>        |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__request
    @property
    def idle(self) -> openenoc_endpoint_peers_entry_dma_idle_0x63728ad65860231b_cls:
        """
        Property to access idle field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].dma.idle[16:16]       |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Indicates whether the DMA transfer to/from the remote peer is   |
        |              |      idle. A value of 1 indicates that the DMA transfer is idle, while  |
        |              |      a value of 0 indicates that the DMA transfer is in progress.</p>   |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__idle
    @property
    def done(self) -> openenoc_endpoint_peers_entry_dma_done_neg_0x679dd6917bc3fe5d_cls:
        """
        Property to access done field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].dma.done[24:24]       |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Indicates whether the DMA transfer to/from the remote peer has  |
        |              |      been successful. A value of 1 indicates that the DMA transfer has  |
        |              |      completed successfully, while a value of 0 indicates that the DMA  |
        |              |      transfer is still in progress or has encountered an error.</p>     |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__done
    @property
    def error(self) -> openenoc_endpoint_peers_entry_dma_error_0x518cdc9dfc4f183a_cls:
        """
        Property to access error field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].dma.error[25:25]      |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Indicates whether the DMA transfer to/from the remote peer has  |
        |              |      encountered an error. A value of 1 indicates an error, while a     |
        |              |      value of 0 indicates no error.</p>                                 |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__error

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'mode':'mode','request':'request','idle':'idle','done':'done','error':'error',
            }

    
    
    
    
    
    
    # nodes:5
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["mode"]) -> 'openenoc_endpoint_peers_entry_dma_mode_neg_0x63e0367ad46e6d32_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["request"]) -> 'openenoc_endpoint_peers_entry_dma_request_0x475295f51d5cf9b4_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["idle"]) -> 'openenoc_endpoint_peers_entry_dma_idle_0x63728ad65860231b_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["done"]) -> 'openenoc_endpoint_peers_entry_dma_done_neg_0x679dd6917bc3fe5d_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["error"]) -> 'openenoc_endpoint_peers_entry_dma_error_0x518cdc9dfc4f183a_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_peers_entry_dma_mode_neg_0x63e0367ad46e6d32_cls', 'openenoc_endpoint_peers_entry_dma_request_0x475295f51d5cf9b4_cls', 'openenoc_endpoint_peers_entry_dma_idle_0x63728ad65860231b_cls', 'openenoc_endpoint_peers_entry_dma_done_neg_0x679dd6917bc3fe5d_cls', 'openenoc_endpoint_peers_entry_dma_error_0x518cdc9dfc4f183a_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].dma"
    @property
    def rdl_desc(self) -> str:
        return "DMA configuration and control for the remote peer."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.mode
        yield self.request
        yield self.idle
        yield self.done
        yield self.error
        
        
    

    
    
class openenoc_endpoint_info_neg_0x549c607bde34271a_cls(RegReadOnly):
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
        
        self.__rmem_total_depth:openenoc_endpoint_info_rmem_total_depth_neg_0x2d459d37235d65d5_cls = openenoc_endpoint_info_rmem_total_depth_neg_0x2d459d37235d65d5_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0, msb=31,
                low=0, high=31),
            misc_props=FieldMiscProps(
                default=128,
                is_volatile=False),
            logger_handle=logger_handle+'.rmem_total_depth',
            inst_name='rmem_total_depth',
            field_type=int)
        self.__num_of_peers:openenoc_endpoint_info_num_of_peers_neg_0x2353d418c67aea7_cls = openenoc_endpoint_info_num_of_peers_neg_0x2353d418c67aea7_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=32, msb=63,
                low=32, high=63),
            misc_props=FieldMiscProps(
                default=2,
                is_volatile=False),
            logger_handle=logger_handle+'.num_of_peers',
            inst_name='num_of_peers',
            field_type=int)

    @property
    def width(self) -> int:
        return 64

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def rmem_total_depth(self) -> openenoc_endpoint_info_rmem_total_depth_neg_0x2d459d37235d65d5_cls:
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
    def num_of_peers(self) -> openenoc_endpoint_info_num_of_peers_neg_0x2353d418c67aea7_cls:
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
    def get_child_by_system_rdl_name(self, name: Literal["rmem_total_depth"]) -> 'openenoc_endpoint_info_rmem_total_depth_neg_0x2d459d37235d65d5_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["num_of_peers"]) -> 'openenoc_endpoint_info_num_of_peers_neg_0x2353d418c67aea7_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_info_rmem_total_depth_neg_0x2d459d37235d65d5_cls', 'openenoc_endpoint_info_num_of_peers_neg_0x2353d418c67aea7_cls', ]: ...

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
        
        
    

    
    
class openenoc_endpoint_config_mac_address_neg_0x2d0ab396256547a3_cls(RegReadWrite):
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
        
        self.__lo_word:openenoc_endpoint_config_mac_address_lo_word_neg_0x448f4357d313ac89_cls = openenoc_endpoint_config_mac_address_lo_word_neg_0x448f4357d313ac89_cls(
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
        self.__hi_word:openenoc_endpoint_config_mac_address_hi_word_neg_0xb902f37a4d7a9c4_cls = openenoc_endpoint_config_mac_address_hi_word_neg_0xb902f37a4d7a9c4_cls(
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
    def lo_word(self) -> openenoc_endpoint_config_mac_address_lo_word_neg_0x448f4357d313ac89_cls:
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
    def hi_word(self) -> openenoc_endpoint_config_mac_address_hi_word_neg_0xb902f37a4d7a9c4_cls:
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
    def get_child_by_system_rdl_name(self, name: Literal["lo_word"]) -> 'openenoc_endpoint_config_mac_address_lo_word_neg_0x448f4357d313ac89_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["hi_word"]) -> 'openenoc_endpoint_config_mac_address_hi_word_neg_0xb902f37a4d7a9c4_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_config_mac_address_lo_word_neg_0x448f4357d313ac89_cls', 'openenoc_endpoint_config_mac_address_hi_word_neg_0xb902f37a4d7a9c4_cls', ]: ...

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
        
        
    

    
    
class openenoc_endpoint_axis_if_source_data_0x42a57f4a6fdb32ef_cls(RegReadWrite):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint2.axis_if.source.data                                  |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Data register for the AXI4-Stream source interface.</p>         |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__tdata']

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
        
        self.__tdata:openenoc_endpoint_axis_if_source_data_tdata_neg_0x18651a6788374af0_cls = openenoc_endpoint_axis_if_source_data_tdata_neg_0x18651a6788374af0_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0, msb=31,
                low=0, high=31),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.tdata',
            inst_name='tdata',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def tdata(self) -> openenoc_endpoint_axis_if_source_data_tdata_neg_0x18651a6788374af0_cls:
        """
        Property to access tdata field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint2.axis_if.source.data.tdata[31:0]                      |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>32-bit data value for the AXI4-Stream source interface.</p>     |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__tdata

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'tdata':'tdata',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_axis_if_source_data_tdata_neg_0x18651a6788374af0_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint2.axis_if.source.data"
    @property
    def rdl_desc(self) -> str:
        return "Data register for the AXI4-Stream source interface."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.tdata
        
        
    

    
    
class openenoc_endpoint_axis_if_source_control_0x6eb3ad904efccb93_cls(RegReadWrite):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint2.axis_if.source.control                               |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Control register for the AXI4-Stream source interface.</p>      |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__tvalid', '__tlast']

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
        
        self.__tvalid:openenoc_endpoint_axis_if_source_control_tvalid_neg_0x7693d3714677d2e2_cls = openenoc_endpoint_axis_if_source_control_tvalid_neg_0x7693d3714677d2e2_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=0, msb=0,
                low=0, high=0),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.tvalid',
            inst_name='tvalid',
            field_type=int)
        self.__tlast:openenoc_endpoint_axis_if_source_control_tlast_0x6f92ad91f9e86b57_cls = openenoc_endpoint_axis_if_source_control_tlast_0x6f92ad91f9e86b57_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=8, msb=8,
                low=8, high=8),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.tlast',
            inst_name='tlast',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def tvalid(self) -> openenoc_endpoint_axis_if_source_control_tvalid_neg_0x7693d3714677d2e2_cls:
        """
        Property to access tvalid field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint2.axis_if.source.control.tvalid                        |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Indicates that the AXI4-Stream source interface has valid data  |
        |              |      to send. This field is a single-pulse register that is             |
        |              |      automatically cleared back to zero after being written.</p>        |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__tvalid
    @property
    def tlast(self) -> openenoc_endpoint_axis_if_source_control_tlast_0x6f92ad91f9e86b57_cls:
        """
        Property to access tlast field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint2.axis_if.source.control.tlast                         |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Indicates the last data word of a frame on the AXI4-Stream      |
        |              |      source interface.</p>                                              |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__tlast

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'tvalid':'tvalid','tlast':'tlast',
            }

    
    
    
    
    
    
    # nodes:2
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["tvalid"]) -> 'openenoc_endpoint_axis_if_source_control_tvalid_neg_0x7693d3714677d2e2_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["tlast"]) -> 'openenoc_endpoint_axis_if_source_control_tlast_0x6f92ad91f9e86b57_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_axis_if_source_control_tvalid_neg_0x7693d3714677d2e2_cls', 'openenoc_endpoint_axis_if_source_control_tlast_0x6f92ad91f9e86b57_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint2.axis_if.source.control"
    @property
    def rdl_desc(self) -> str:
        return "Control register for the AXI4-Stream source interface."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.tvalid
        yield self.tlast
        
        
    

    
    
class openenoc_endpoint_axis_if_source_status_neg_0x207fb7f13290ac1e_cls(RegReadOnly):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint2.axis_if.source.status                                |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Status register for the AXI4-Stream source interface.</p>       |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__tready']

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
        
        self.__tready:openenoc_endpoint_axis_if_source_status_tready_neg_0x96c8ac4faeb1efd_cls = openenoc_endpoint_axis_if_source_status_tready_neg_0x96c8ac4faeb1efd_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=0, msb=0,
                low=0, high=0),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=True),
            logger_handle=logger_handle+'.tready',
            inst_name='tready',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def tready(self) -> openenoc_endpoint_axis_if_source_status_tready_neg_0x96c8ac4faeb1efd_cls:
        """
        Property to access tready field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint2.axis_if.source.status.tready                         |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Indicates that the destination AXI4-Stream interface is ready   |
        |              |      to receive data.</p>                                               |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__tready

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'tready':'tready',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_axis_if_source_status_tready_neg_0x96c8ac4faeb1efd_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint2.axis_if.source.status"
    @property
    def rdl_desc(self) -> str:
        return "Status register for the AXI4-Stream source interface."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.tready
        
        
    

    
    
class openenoc_endpoint_axis_if_sink_data_0x6c882caebb700338_cls(RegReadOnly):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint2.axis_if.sink.data                                    |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Data register for the AXI4-Stream sink interface.</p>           |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__tdata']

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
        
        self.__tdata:openenoc_endpoint_axis_if_sink_data_tdata_neg_0x6490c579133ec028_cls = openenoc_endpoint_axis_if_sink_data_tdata_neg_0x6490c579133ec028_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0, msb=31,
                low=0, high=31),
            misc_props=FieldMiscProps(
                default=None,
                is_volatile=True),
            logger_handle=logger_handle+'.tdata',
            inst_name='tdata',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def tdata(self) -> openenoc_endpoint_axis_if_sink_data_tdata_neg_0x6490c579133ec028_cls:
        """
        Property to access tdata field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint2.axis_if.sink.data.tdata[31:0]                        |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>32-bit data value for the AXI4-Stream sink interface.</p>       |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__tdata

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'tdata':'tdata',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_axis_if_sink_data_tdata_neg_0x6490c579133ec028_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint2.axis_if.sink.data"
    @property
    def rdl_desc(self) -> str:
        return "Data register for the AXI4-Stream sink interface."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.tdata
        
        
    

    
    
class openenoc_endpoint_axis_if_sink_control_0x557ae3e17e19b169_cls(RegWriteOnly):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint2.axis_if.sink.control                                 |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Control register for the AXI4-Stream sink interface.</p>        |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__tready']

    def __init__(self,
                 address: int,
                 logger_handle: str,
                 inst_name: str,
                 parent: Union[AddressMap,RegFile,WritableMemory]):

        super().__init__(address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # build the field attributes
        
        self.__tready:openenoc_endpoint_axis_if_sink_control_tready_neg_0x42b52af8ff892e38_cls = openenoc_endpoint_axis_if_sink_control_tready_neg_0x42b52af8ff892e38_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=0, msb=0,
                low=0, high=0),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.tready',
            inst_name='tready',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    
    
    def write_fields(self,tready : int) -> None: # type: ignore[override]
        """
        Do a write to the register, updating all fields
        """
        reg_value = 0
        reg_value &= self.tready.inverse_bitmask
        reg_value |= self.tready._encode_write_value(tready)
        

        self.write(reg_value)

    

    # build the properties for the fields
    
    @property
    def tready(self) -> openenoc_endpoint_axis_if_sink_control_tready_neg_0x42b52af8ff892e38_cls:
        """
        Property to access tready field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint2.axis_if.sink.control.tready                          |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Indicates that the AXI4-Stream sink interface is ready to       |
        |              |      receive next data transfer.</p>                                    |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__tready

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'tready':'tready',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_axis_if_sink_control_tready_neg_0x42b52af8ff892e38_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint2.axis_if.sink.control"
    @property
    def rdl_desc(self) -> str:
        return "Control register for the AXI4-Stream sink interface."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.tready
        
        
    

    
    
class openenoc_endpoint_axis_if_sink_status_0x6d742d7bb53bda94_cls(RegReadOnly):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint2.axis_if.sink.status                                  |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Status register for the AXI4-Stream sink interface.</p>         |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__tvalid', '__tlast']

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
        
        self.__tvalid:openenoc_endpoint_axis_if_sink_status_tvalid_neg_0x13672d8472c23bf5_cls = openenoc_endpoint_axis_if_sink_status_tvalid_neg_0x13672d8472c23bf5_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=0, msb=0,
                low=0, high=0),
            misc_props=FieldMiscProps(
                default=None,
                is_volatile=True),
            logger_handle=logger_handle+'.tvalid',
            inst_name='tvalid',
            field_type=int)
        self.__tlast:openenoc_endpoint_axis_if_sink_status_tlast_0x1699db3a89e56b5a_cls = openenoc_endpoint_axis_if_sink_status_tlast_0x1699db3a89e56b5a_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=8, msb=8,
                low=8, high=8),
            misc_props=FieldMiscProps(
                default=None,
                is_volatile=True),
            logger_handle=logger_handle+'.tlast',
            inst_name='tlast',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def tvalid(self) -> openenoc_endpoint_axis_if_sink_status_tvalid_neg_0x13672d8472c23bf5_cls:
        """
        Property to access tvalid field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint2.axis_if.sink.status.tvalid                           |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Indicates that the AXI4-Stream sink interface has valid data to |
        |              |      receive.</p>                                                       |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__tvalid
    @property
    def tlast(self) -> openenoc_endpoint_axis_if_sink_status_tlast_0x1699db3a89e56b5a_cls:
        """
        Property to access tlast field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint2.axis_if.sink.status.tlast                            |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Indicates the last data word of a frame on the AXI4-Stream sink |
        |              |      interface.</p>                                                     |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__tlast

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'tvalid':'tvalid','tlast':'tlast',
            }

    
    
    
    
    
    
    # nodes:2
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["tvalid"]) -> 'openenoc_endpoint_axis_if_sink_status_tvalid_neg_0x13672d8472c23bf5_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["tlast"]) -> 'openenoc_endpoint_axis_if_sink_status_tlast_0x1699db3a89e56b5a_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_axis_if_sink_status_tvalid_neg_0x13672d8472c23bf5_cls', 'openenoc_endpoint_axis_if_sink_status_tlast_0x1699db3a89e56b5a_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint2.axis_if.sink.status"
    @property
    def rdl_desc(self) -> str:
        return "Status register for the AXI4-Stream sink interface."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.tvalid
        yield self.tlast
        
        
    

    
    
class openenoc_endpoint_peers_entry_mac_address_0x2851813cb1c6f569_cls(RegReadWrite):
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
        
        self.__lo_word:openenoc_endpoint_peers_entry_mac_address_lo_word_neg_0x2d9dfd1a27a63014_cls = openenoc_endpoint_peers_entry_mac_address_lo_word_neg_0x2d9dfd1a27a63014_cls(
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
        self.__hi_word:openenoc_endpoint_peers_entry_mac_address_hi_word_neg_0x567d8034ecf5cbaf_cls = openenoc_endpoint_peers_entry_mac_address_hi_word_neg_0x567d8034ecf5cbaf_cls(
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
    def lo_word(self) -> openenoc_endpoint_peers_entry_mac_address_lo_word_neg_0x2d9dfd1a27a63014_cls:
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
    def hi_word(self) -> openenoc_endpoint_peers_entry_mac_address_hi_word_neg_0x567d8034ecf5cbaf_cls:
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
    def get_child_by_system_rdl_name(self, name: Literal["lo_word"]) -> 'openenoc_endpoint_peers_entry_mac_address_lo_word_neg_0x2d9dfd1a27a63014_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["hi_word"]) -> 'openenoc_endpoint_peers_entry_mac_address_hi_word_neg_0x567d8034ecf5cbaf_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_peers_entry_mac_address_lo_word_neg_0x2d9dfd1a27a63014_cls', 'openenoc_endpoint_peers_entry_mac_address_hi_word_neg_0x567d8034ecf5cbaf_cls', ]: ...

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
        
        
    


if __name__ == '__main__':
    pass