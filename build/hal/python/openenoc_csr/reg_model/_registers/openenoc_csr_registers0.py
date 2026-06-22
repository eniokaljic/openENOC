

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






from .fields import openenoc_csr_test_reg_test_field_0x673609eff3bac637_cls
from .fields import openenoc_switch_info_table_depth_0x68d6d3f4fa877b7a_cls
from .fields import openenoc_switch_info_num_of_interfaces_neg_0x61e9762b08ab994f_cls
from .fields import openenoc_switch_forwarding_control_operation_mode_0x43af1c7fa8d7907e_cls
from .fields import openenoc_switch_forwarding_control_pause_request_neg_0x21cd5f1c37735e8_cls
from .fields import openenoc_switch_forwarding_control_pause_done_neg_0x1e2d7ca1eb846a55_cls
from .fields import openenoc_switch_default_forwarding_bitmap_0x60c0738a4811b16a_cls
from .fields import openenoc_switch_forwarding_table_entry_macaddr_lo_word_0x575c22e34384f678_cls
from .fields import openenoc_switch_forwarding_table_entry_macaddr_hi_word_0x7f673539b0cd808d_cls
from .fields import openenoc_switch_forwarding_table_entry_iface_bitmap_0x15f4b72475b882d3_cls
from .fields import openenoc_switch_forwarding_table_entry_config_enabled_0x7a79d2f0b143e4f4_cls
from .fields import openenoc_switch_info_table_depth_neg_0x704b5f0c648c4fbb_cls
from .fields import openenoc_switch_info_num_of_interfaces_neg_0x5355cde1cf8eba63_cls
from .fields import openenoc_switch_forwarding_control_operation_mode_0x3cc7b7577b22380c_cls
from .fields import openenoc_switch_forwarding_control_pause_request_0x6dc0c8931cf0be76_cls
from .fields import openenoc_switch_forwarding_control_pause_done_0x6056551b63557329_cls
from .fields import openenoc_switch_default_forwarding_bitmap_neg_0x579f05bf35b603a8_cls
from .fields import openenoc_switch_forwarding_table_entry_macaddr_lo_word_0x4489424609a90dd1_cls
from .fields import openenoc_switch_forwarding_table_entry_macaddr_hi_word_neg_0xaf14854b24af335_cls
from .fields import openenoc_switch_forwarding_table_entry_iface_bitmap_neg_0x2179538f9fe81a80_cls
from .fields import openenoc_switch_forwarding_table_entry_config_enabled_neg_0x6bb3ed71e2fab4a6_cls
from .fields import openenoc_endpoint_info_placeholder_0x60ef31f71f9e7ed1_cls

# register definitions
    
    
class openenoc_csr_test_reg_0x3f30da3aa8dc9c75_cls(RegReadWrite):
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
        
        self.__test_field:openenoc_csr_test_reg_test_field_0x673609eff3bac637_cls = openenoc_csr_test_reg_test_field_0x673609eff3bac637_cls(
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
    def test_field(self) -> openenoc_csr_test_reg_test_field_0x673609eff3bac637_cls:
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

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_csr_test_reg_test_field_0x673609eff3bac637_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.test_reg"
    @property
    def rdl_desc(self) -> str:
        return "Test register"
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.test_field
        
        
    

    
    
class openenoc_csr_regB_0x3c083fe13ca16b03_cls(RegReadWrite):
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
        
        
    

    
    
class openenoc_switch_info_neg_0x7ae6f7afe2223cb6_cls(RegReadOnly):
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
        
        self.__table_depth:openenoc_switch_info_table_depth_0x68d6d3f4fa877b7a_cls = openenoc_switch_info_table_depth_0x68d6d3f4fa877b7a_cls(
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
        self.__num_of_interfaces:openenoc_switch_info_num_of_interfaces_neg_0x61e9762b08ab994f_cls = openenoc_switch_info_num_of_interfaces_neg_0x61e9762b08ab994f_cls(
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
    def table_depth(self) -> openenoc_switch_info_table_depth_0x68d6d3f4fa877b7a_cls:
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
    def num_of_interfaces(self) -> openenoc_switch_info_num_of_interfaces_neg_0x61e9762b08ab994f_cls:
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
    def get_child_by_system_rdl_name(self, name: Literal["table_depth"]) -> 'openenoc_switch_info_table_depth_0x68d6d3f4fa877b7a_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["num_of_interfaces"]) -> 'openenoc_switch_info_num_of_interfaces_neg_0x61e9762b08ab994f_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_switch_info_table_depth_0x68d6d3f4fa877b7a_cls', 'openenoc_switch_info_num_of_interfaces_neg_0x61e9762b08ab994f_cls', ]: ...

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
        
        
    

    
    
class openenoc_switch_forwarding_control_neg_0x2706647eeaac8595_cls(RegReadWrite):
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
        
        self.__operation_mode:openenoc_switch_forwarding_control_operation_mode_0x43af1c7fa8d7907e_cls = openenoc_switch_forwarding_control_operation_mode_0x43af1c7fa8d7907e_cls(
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
        self.__pause_request:openenoc_switch_forwarding_control_pause_request_neg_0x21cd5f1c37735e8_cls = openenoc_switch_forwarding_control_pause_request_neg_0x21cd5f1c37735e8_cls(
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
        self.__pause_done:openenoc_switch_forwarding_control_pause_done_neg_0x1e2d7ca1eb846a55_cls = openenoc_switch_forwarding_control_pause_done_neg_0x1e2d7ca1eb846a55_cls(
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
    def operation_mode(self) -> openenoc_switch_forwarding_control_operation_mode_0x43af1c7fa8d7907e_cls:
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
    def pause_request(self) -> openenoc_switch_forwarding_control_pause_request_neg_0x21cd5f1c37735e8_cls:
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
    def pause_done(self) -> openenoc_switch_forwarding_control_pause_done_neg_0x1e2d7ca1eb846a55_cls:
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
    def get_child_by_system_rdl_name(self, name: Literal["operation_mode"]) -> 'openenoc_switch_forwarding_control_operation_mode_0x43af1c7fa8d7907e_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["pause_request"]) -> 'openenoc_switch_forwarding_control_pause_request_neg_0x21cd5f1c37735e8_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["pause_done"]) -> 'openenoc_switch_forwarding_control_pause_done_neg_0x1e2d7ca1eb846a55_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_switch_forwarding_control_operation_mode_0x43af1c7fa8d7907e_cls', 'openenoc_switch_forwarding_control_pause_request_neg_0x21cd5f1c37735e8_cls', 'openenoc_switch_forwarding_control_pause_done_neg_0x1e2d7ca1eb846a55_cls', ]: ...

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
        
        
    

    
    
class openenoc_switch_default_forwarding_neg_0x67ec41965df8b626_cls(RegReadWrite):
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
        
        self.__bitmap:openenoc_switch_default_forwarding_bitmap_0x60c0738a4811b16a_cls = openenoc_switch_default_forwarding_bitmap_0x60c0738a4811b16a_cls(
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
    def bitmap(self) -> openenoc_switch_default_forwarding_bitmap_0x60c0738a4811b16a_cls:
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

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_switch_default_forwarding_bitmap_0x60c0738a4811b16a_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.switch1.default_forwarding"
    @property
    def rdl_desc(self) -> str:
        return "Defines the destination interface or interfaces for frames that do not match any enabled forwarding table entry."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.bitmap
        
        
    

    
    
class openenoc_switch_forwarding_table_entry_macaddr_neg_0x50b30858704ffc6b_cls(RegReadWrite):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr       |
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
        
        self.__lo_word:openenoc_switch_forwarding_table_entry_macaddr_lo_word_0x575c22e34384f678_cls = openenoc_switch_forwarding_table_entry_macaddr_lo_word_0x575c22e34384f678_cls(
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
        self.__hi_word:openenoc_switch_forwarding_table_entry_macaddr_hi_word_0x7f673539b0cd808d_cls = openenoc_switch_forwarding_table_entry_macaddr_hi_word_0x7f673539b0cd808d_cls(
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
    def lo_word(self) -> openenoc_switch_forwarding_table_entry_macaddr_lo_word_0x575c22e34384f678_cls:
        """
        Property to access lo_word field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-                 |
        |              |      1].macaddr.lo_word[31:0]                                           |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this   |
        |              |      forwarding table entry.</p>                                        |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__lo_word
    @property
    def hi_word(self) -> openenoc_switch_forwarding_table_entry_macaddr_hi_word_0x7f673539b0cd808d_cls:
        """
        Property to access hi_word field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-                 |
        |              |      1].macaddr.hi_word[47:32]                                          |
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
    def get_child_by_system_rdl_name(self, name: Literal["lo_word"]) -> 'openenoc_switch_forwarding_table_entry_macaddr_lo_word_0x575c22e34384f678_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["hi_word"]) -> 'openenoc_switch_forwarding_table_entry_macaddr_hi_word_0x7f673539b0cd808d_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_switch_forwarding_table_entry_macaddr_lo_word_0x575c22e34384f678_cls', 'openenoc_switch_forwarding_table_entry_macaddr_hi_word_0x7f673539b0cd808d_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr"
    @property
    def rdl_desc(self) -> str:
        return "48-bit destination MAC address used as the key for this forwarding table entry."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.lo_word
        yield self.hi_word
        
        
    

    
    
class openenoc_switch_forwarding_table_entry_iface_0x6e7f55c0f04a23f_cls(RegReadWrite):
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
        
        self.__bitmap:openenoc_switch_forwarding_table_entry_iface_bitmap_0x15f4b72475b882d3_cls = openenoc_switch_forwarding_table_entry_iface_bitmap_0x15f4b72475b882d3_cls(
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
    def bitmap(self) -> openenoc_switch_forwarding_table_entry_iface_bitmap_0x15f4b72475b882d3_cls:
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

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_switch_forwarding_table_entry_iface_bitmap_0x15f4b72475b882d3_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].iface"
    @property
    def rdl_desc(self) -> str:
        return "Forwarding interface information associated with this forwarding table entry."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.bitmap
        
        
    

    
    
class openenoc_switch_forwarding_table_entry_config_0x151239c9dd2f2e19_cls(RegReadWrite):
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
        
        self.__enabled:openenoc_switch_forwarding_table_entry_config_enabled_0x7a79d2f0b143e4f4_cls = openenoc_switch_forwarding_table_entry_config_enabled_0x7a79d2f0b143e4f4_cls(
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
    def enabled(self) -> openenoc_switch_forwarding_table_entry_config_enabled_0x7a79d2f0b143e4f4_cls:
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

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_switch_forwarding_table_entry_config_enabled_0x7a79d2f0b143e4f4_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].config"
    @property
    def rdl_desc(self) -> str:
        return "Configuration information associated with this forwarding table entry."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.enabled
        
        
    

    
    
class openenoc_switch_info_0x5fe2743488d051e8_cls(RegReadOnly):
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
        
        self.__table_depth:openenoc_switch_info_table_depth_neg_0x704b5f0c648c4fbb_cls = openenoc_switch_info_table_depth_neg_0x704b5f0c648c4fbb_cls(
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
        self.__num_of_interfaces:openenoc_switch_info_num_of_interfaces_neg_0x5355cde1cf8eba63_cls = openenoc_switch_info_num_of_interfaces_neg_0x5355cde1cf8eba63_cls(
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
    def table_depth(self) -> openenoc_switch_info_table_depth_neg_0x704b5f0c648c4fbb_cls:
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
    def num_of_interfaces(self) -> openenoc_switch_info_num_of_interfaces_neg_0x5355cde1cf8eba63_cls:
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
    def get_child_by_system_rdl_name(self, name: Literal["table_depth"]) -> 'openenoc_switch_info_table_depth_neg_0x704b5f0c648c4fbb_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["num_of_interfaces"]) -> 'openenoc_switch_info_num_of_interfaces_neg_0x5355cde1cf8eba63_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_switch_info_table_depth_neg_0x704b5f0c648c4fbb_cls', 'openenoc_switch_info_num_of_interfaces_neg_0x5355cde1cf8eba63_cls', ]: ...

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
        
        
    

    
    
class openenoc_switch_forwarding_control_neg_0x3cbe7d1b6d7881c9_cls(RegReadWrite):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.switch2.forwarding_control                                     |
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
        
        self.__operation_mode:openenoc_switch_forwarding_control_operation_mode_0x3cc7b7577b22380c_cls = openenoc_switch_forwarding_control_operation_mode_0x3cc7b7577b22380c_cls(
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
        self.__pause_request:openenoc_switch_forwarding_control_pause_request_0x6dc0c8931cf0be76_cls = openenoc_switch_forwarding_control_pause_request_0x6dc0c8931cf0be76_cls(
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
        self.__pause_done:openenoc_switch_forwarding_control_pause_done_0x6056551b63557329_cls = openenoc_switch_forwarding_control_pause_done_0x6056551b63557329_cls(
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
    def operation_mode(self) -> openenoc_switch_forwarding_control_operation_mode_0x3cc7b7577b22380c_cls:
        """
        Property to access operation_mode field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.switch2.forwarding_control.operation_mode[0:0]                 |
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
    def pause_request(self) -> openenoc_switch_forwarding_control_pause_request_0x6dc0c8931cf0be76_cls:
        """
        Property to access pause_request field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.switch2.forwarding_control.pause_request[7:7]                  |
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
    def pause_done(self) -> openenoc_switch_forwarding_control_pause_done_0x6056551b63557329_cls:
        """
        Property to access pause_done field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.switch2.forwarding_control.pause_done[15:15]                   |
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
    def get_child_by_system_rdl_name(self, name: Literal["operation_mode"]) -> 'openenoc_switch_forwarding_control_operation_mode_0x3cc7b7577b22380c_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["pause_request"]) -> 'openenoc_switch_forwarding_control_pause_request_0x6dc0c8931cf0be76_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["pause_done"]) -> 'openenoc_switch_forwarding_control_pause_done_0x6056551b63557329_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_switch_forwarding_control_operation_mode_0x3cc7b7577b22380c_cls', 'openenoc_switch_forwarding_control_pause_request_0x6dc0c8931cf0be76_cls', 'openenoc_switch_forwarding_control_pause_done_0x6056551b63557329_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.switch2.forwarding_control"
    @property
    def rdl_desc(self) -> str:
        return "Forwarding control register for the openENOC Switch instance."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.operation_mode
        yield self.pause_request
        yield self.pause_done
        
        
    

    
    
class openenoc_switch_default_forwarding_0x72e0f488544122f6_cls(RegReadWrite):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.switch2.default_forwarding                                     |
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
        
        self.__bitmap:openenoc_switch_default_forwarding_bitmap_neg_0x579f05bf35b603a8_cls = openenoc_switch_default_forwarding_bitmap_neg_0x579f05bf35b603a8_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=8,
                lsb=0, msb=7,
                low=0, high=7),
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
    def bitmap(self) -> openenoc_switch_default_forwarding_bitmap_neg_0x579f05bf35b603a8_cls:
        """
        Property to access bitmap field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.switch2.default_forwarding.bitmap[NUM_OF_INTERFACES-1:0]       |
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

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_switch_default_forwarding_bitmap_neg_0x579f05bf35b603a8_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.switch2.default_forwarding"
    @property
    def rdl_desc(self) -> str:
        return "Defines the destination interface or interfaces for frames that do not match any enabled forwarding table entry."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.bitmap
        
        
    

    
    
class openenoc_switch_forwarding_table_entry_macaddr_neg_0x5d62fd6566329f98_cls(RegReadWrite):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr       |
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
        
        self.__lo_word:openenoc_switch_forwarding_table_entry_macaddr_lo_word_0x4489424609a90dd1_cls = openenoc_switch_forwarding_table_entry_macaddr_lo_word_0x4489424609a90dd1_cls(
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
        self.__hi_word:openenoc_switch_forwarding_table_entry_macaddr_hi_word_neg_0xaf14854b24af335_cls = openenoc_switch_forwarding_table_entry_macaddr_hi_word_neg_0xaf14854b24af335_cls(
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
    def lo_word(self) -> openenoc_switch_forwarding_table_entry_macaddr_lo_word_0x4489424609a90dd1_cls:
        """
        Property to access lo_word field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-                 |
        |              |      1].macaddr.lo_word[31:0]                                           |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this   |
        |              |      forwarding table entry.</p>                                        |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__lo_word
    @property
    def hi_word(self) -> openenoc_switch_forwarding_table_entry_macaddr_hi_word_neg_0xaf14854b24af335_cls:
        """
        Property to access hi_word field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-                 |
        |              |      1].macaddr.hi_word[47:32]                                          |
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
    def get_child_by_system_rdl_name(self, name: Literal["lo_word"]) -> 'openenoc_switch_forwarding_table_entry_macaddr_lo_word_0x4489424609a90dd1_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["hi_word"]) -> 'openenoc_switch_forwarding_table_entry_macaddr_hi_word_neg_0xaf14854b24af335_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_switch_forwarding_table_entry_macaddr_lo_word_0x4489424609a90dd1_cls', 'openenoc_switch_forwarding_table_entry_macaddr_hi_word_neg_0xaf14854b24af335_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr"
    @property
    def rdl_desc(self) -> str:
        return "48-bit destination MAC address used as the key for this forwarding table entry."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.lo_word
        yield self.hi_word
        
        
    

    
    
class openenoc_switch_forwarding_table_entry_iface_neg_0x2dd01d9e9041477_cls(RegReadWrite):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface         |
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
        
        self.__bitmap:openenoc_switch_forwarding_table_entry_iface_bitmap_neg_0x2179538f9fe81a80_cls = openenoc_switch_forwarding_table_entry_iface_bitmap_neg_0x2179538f9fe81a80_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=8,
                lsb=0, msb=7,
                low=0, high=7),
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
    def bitmap(self) -> openenoc_switch_forwarding_table_entry_iface_bitmap_neg_0x2179538f9fe81a80_cls:
        """
        Property to access bitmap field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-                 |
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

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_switch_forwarding_table_entry_iface_bitmap_neg_0x2179538f9fe81a80_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface"
    @property
    def rdl_desc(self) -> str:
        return "Forwarding interface information associated with this forwarding table entry."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.bitmap
        
        
    

    
    
class openenoc_switch_forwarding_table_entry_config_neg_0x4ec294a067c7cd5d_cls(RegReadWrite):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config        |
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
        
        self.__enabled:openenoc_switch_forwarding_table_entry_config_enabled_neg_0x6bb3ed71e2fab4a6_cls = openenoc_switch_forwarding_table_entry_config_enabled_neg_0x6bb3ed71e2fab4a6_cls(
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
    def enabled(self) -> openenoc_switch_forwarding_table_entry_config_enabled_neg_0x6bb3ed71e2fab4a6_cls:
        """
        Property to access enabled field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-                 |
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

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_switch_forwarding_table_entry_config_enabled_neg_0x6bb3ed71e2fab4a6_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config"
    @property
    def rdl_desc(self) -> str:
        return "Configuration information associated with this forwarding table entry."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.enabled
        
        
    

    
    
class openenoc_endpoint_info_0x10849a1f39de2855_cls(RegReadOnly):
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

    __slots__ : list[str] = ['__placeholder']

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
        
        self.__placeholder:openenoc_endpoint_info_placeholder_0x60ef31f71f9e7ed1_cls = openenoc_endpoint_info_placeholder_0x60ef31f71f9e7ed1_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0, msb=31,
                low=0, high=31),
            misc_props=FieldMiscProps(
                default=None,
                is_volatile=False),
            logger_handle=logger_handle+'.placeholder',
            inst_name='placeholder',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def placeholder(self) -> openenoc_endpoint_info_placeholder_0x60ef31f71f9e7ed1_cls:
        """
        Property to access placeholder field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint1.info.placeholder[31:0]                               |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Placeholder field for this openENOC Endpoint Interface          |
        |              |      instance.</p>                                                      |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__placeholder

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'placeholder':'placeholder',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_info_placeholder_0x60ef31f71f9e7ed1_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint1.info"
    @property
    def rdl_desc(self) -> str:
        return "Read-only information register for this openENOC Endpoint Interface instance."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.placeholder
        
        
    


if __name__ == '__main__':
    pass