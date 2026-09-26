

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






from .fields import openenoc_endpoint_interface_rmem_word_data_neg_0x32b33d7999aa7f89_cls
from .fields import openenoc_switch_interface_info_table_depth_neg_0x68d62822e06703a8_cls
from .fields import openenoc_switch_interface_info_num_of_interfaces_0x212c7530acb23a8d_cls
from .fields import openenoc_switch_interface_forwarding_control_operation_mode_0x3365db6880074dee_cls
from .fields import openenoc_switch_interface_forwarding_control_pause_request_neg_0x31ca77f18e28cd5_cls
from .fields import openenoc_switch_interface_forwarding_control_pause_done_neg_0x683c4a31fa31b32a_cls
from .fields import openenoc_switch_interface_default_forwarding_bitmap_0x78752798531a4b66_cls
from .fields import openenoc_switch_interface_forwarding_table_entry_mac_address_lo_word_neg_0x4a71d41daefb8214_cls
from .fields import openenoc_switch_interface_forwarding_table_entry_mac_address_hi_word_neg_0x7cf420dc561fa72d_cls
from .fields import openenoc_switch_interface_forwarding_table_entry_iface_bitmap_0x44fcd4411f1c797f_cls
from .fields import openenoc_switch_interface_forwarding_table_entry_config_enabled_0x4966be7ddd1dd292_cls

# register definitions
    
    
class openenoc_endpoint_interface_rmem_word_0x1ea8ac8fae67aec5_cls(RegReadWrite):
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
        
        self.__data:openenoc_endpoint_interface_rmem_word_data_neg_0x32b33d7999aa7f89_cls = openenoc_endpoint_interface_rmem_word_data_neg_0x32b33d7999aa7f89_cls(
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
    def data(self) -> openenoc_endpoint_interface_rmem_word_data_neg_0x32b33d7999aa7f89_cls:
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

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_interface_rmem_word_data_neg_0x32b33d7999aa7f89_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]"
    @property
    def rdl_desc(self) -> str:
        return "32-bit word in the virtual memory region."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.data
        
        
class openenoc_endpoint_interface_rmem_word_0x1ea8ac8fae67aec5_cls_array(RegReadWriteArray):
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
        return openenoc_endpoint_interface_rmem_word_0x1ea8ac8fae67aec5_cls

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]"
    @property
    def rdl_desc(self) -> str:
        return "32-bit word in the virtual memory region."
    
    
    

    
    
class openenoc_switch_interface_info_0x335174d291281a8d_cls(RegReadOnly):
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
        
        self.__table_depth:openenoc_switch_interface_info_table_depth_neg_0x68d62822e06703a8_cls = openenoc_switch_interface_info_table_depth_neg_0x68d62822e06703a8_cls(
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
        self.__num_of_interfaces:openenoc_switch_interface_info_num_of_interfaces_0x212c7530acb23a8d_cls = openenoc_switch_interface_info_num_of_interfaces_0x212c7530acb23a8d_cls(
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
    def table_depth(self) -> openenoc_switch_interface_info_table_depth_neg_0x68d62822e06703a8_cls:
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
    def num_of_interfaces(self) -> openenoc_switch_interface_info_num_of_interfaces_0x212c7530acb23a8d_cls:
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
    def get_child_by_system_rdl_name(self, name: Literal["table_depth"]) -> 'openenoc_switch_interface_info_table_depth_neg_0x68d62822e06703a8_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["num_of_interfaces"]) -> 'openenoc_switch_interface_info_num_of_interfaces_0x212c7530acb23a8d_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_switch_interface_info_table_depth_neg_0x68d62822e06703a8_cls', 'openenoc_switch_interface_info_num_of_interfaces_0x212c7530acb23a8d_cls', ]: ...

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
        
        
    

    
    
class openenoc_switch_interface_forwarding_control_0x77dcf2330fa4c948_cls(RegReadWrite):
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
        
        self.__operation_mode:openenoc_switch_interface_forwarding_control_operation_mode_0x3365db6880074dee_cls = openenoc_switch_interface_forwarding_control_operation_mode_0x3365db6880074dee_cls(
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
        self.__pause_request:openenoc_switch_interface_forwarding_control_pause_request_neg_0x31ca77f18e28cd5_cls = openenoc_switch_interface_forwarding_control_pause_request_neg_0x31ca77f18e28cd5_cls(
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
        self.__pause_done:openenoc_switch_interface_forwarding_control_pause_done_neg_0x683c4a31fa31b32a_cls = openenoc_switch_interface_forwarding_control_pause_done_neg_0x683c4a31fa31b32a_cls(
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
    def operation_mode(self) -> openenoc_switch_interface_forwarding_control_operation_mode_0x3365db6880074dee_cls:
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
    def pause_request(self) -> openenoc_switch_interface_forwarding_control_pause_request_neg_0x31ca77f18e28cd5_cls:
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
    def pause_done(self) -> openenoc_switch_interface_forwarding_control_pause_done_neg_0x683c4a31fa31b32a_cls:
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
    def get_child_by_system_rdl_name(self, name: Literal["operation_mode"]) -> 'openenoc_switch_interface_forwarding_control_operation_mode_0x3365db6880074dee_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["pause_request"]) -> 'openenoc_switch_interface_forwarding_control_pause_request_neg_0x31ca77f18e28cd5_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["pause_done"]) -> 'openenoc_switch_interface_forwarding_control_pause_done_neg_0x683c4a31fa31b32a_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_switch_interface_forwarding_control_operation_mode_0x3365db6880074dee_cls', 'openenoc_switch_interface_forwarding_control_pause_request_neg_0x31ca77f18e28cd5_cls', 'openenoc_switch_interface_forwarding_control_pause_done_neg_0x683c4a31fa31b32a_cls', ]: ...

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
        
        
    

    
    
class openenoc_switch_interface_default_forwarding_0x6d78030d38ddea_cls(RegReadWrite):
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
        
        self.__bitmap:openenoc_switch_interface_default_forwarding_bitmap_0x78752798531a4b66_cls = openenoc_switch_interface_default_forwarding_bitmap_0x78752798531a4b66_cls(
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
    def bitmap(self) -> openenoc_switch_interface_default_forwarding_bitmap_0x78752798531a4b66_cls:
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

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_switch_interface_default_forwarding_bitmap_0x78752798531a4b66_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.switch_interface.default_forwarding"
    @property
    def rdl_desc(self) -> str:
        return "Defines the destination interface or interfaces for frames that do not match any enabled forwarding table entry."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.bitmap
        
        
    

    
    
class openenoc_switch_interface_forwarding_table_entry_mac_address_0x6902bea3ff0ef316_cls(RegReadWrite):
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
        
        self.__lo_word:openenoc_switch_interface_forwarding_table_entry_mac_address_lo_word_neg_0x4a71d41daefb8214_cls = openenoc_switch_interface_forwarding_table_entry_mac_address_lo_word_neg_0x4a71d41daefb8214_cls(
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
        self.__hi_word:openenoc_switch_interface_forwarding_table_entry_mac_address_hi_word_neg_0x7cf420dc561fa72d_cls = openenoc_switch_interface_forwarding_table_entry_mac_address_hi_word_neg_0x7cf420dc561fa72d_cls(
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
    def lo_word(self) -> openenoc_switch_interface_forwarding_table_entry_mac_address_lo_word_neg_0x4a71d41daefb8214_cls:
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
    def hi_word(self) -> openenoc_switch_interface_forwarding_table_entry_mac_address_hi_word_neg_0x7cf420dc561fa72d_cls:
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
    def get_child_by_system_rdl_name(self, name: Literal["lo_word"]) -> 'openenoc_switch_interface_forwarding_table_entry_mac_address_lo_word_neg_0x4a71d41daefb8214_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["hi_word"]) -> 'openenoc_switch_interface_forwarding_table_entry_mac_address_hi_word_neg_0x7cf420dc561fa72d_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_switch_interface_forwarding_table_entry_mac_address_lo_word_neg_0x4a71d41daefb8214_cls', 'openenoc_switch_interface_forwarding_table_entry_mac_address_hi_word_neg_0x7cf420dc561fa72d_cls', ]: ...

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
        
        
    

    
    
class openenoc_switch_interface_forwarding_table_entry_iface_0x1e73631b31abe831_cls(RegReadWrite):
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
        
        self.__bitmap:openenoc_switch_interface_forwarding_table_entry_iface_bitmap_0x44fcd4411f1c797f_cls = openenoc_switch_interface_forwarding_table_entry_iface_bitmap_0x44fcd4411f1c797f_cls(
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
    def bitmap(self) -> openenoc_switch_interface_forwarding_table_entry_iface_bitmap_0x44fcd4411f1c797f_cls:
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

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_switch_interface_forwarding_table_entry_iface_bitmap_0x44fcd4411f1c797f_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].iface"
    @property
    def rdl_desc(self) -> str:
        return "Forwarding interface information associated with this forwarding table entry."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.bitmap
        
        
    

    
    
class openenoc_switch_interface_forwarding_table_entry_config_neg_0x5f483b321a3d26fd_cls(RegReadWrite):
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
        
        self.__enabled:openenoc_switch_interface_forwarding_table_entry_config_enabled_0x4966be7ddd1dd292_cls = openenoc_switch_interface_forwarding_table_entry_config_enabled_0x4966be7ddd1dd292_cls(
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
    def enabled(self) -> openenoc_switch_interface_forwarding_table_entry_config_enabled_0x4966be7ddd1dd292_cls:
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

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_switch_interface_forwarding_table_entry_config_enabled_0x4966be7ddd1dd292_cls':
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