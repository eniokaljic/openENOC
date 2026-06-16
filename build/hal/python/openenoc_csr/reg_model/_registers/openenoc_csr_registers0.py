

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






from .fields import openenoc_csr_test_reg_test_field_neg_0x476e25cb214ac8aa_cls
from .fields import openenoc_switch_info_table_depth_0x68bd55d73777d304_cls
from .fields import openenoc_switch_info_num_of_interfaces_neg_0x423de23bda410e60_cls
from .fields import openenoc_switch_forwarding_control_operation_mode_neg_0x7b0630db069ab533_cls
from .fields import openenoc_switch_forwarding_control_pause_request_0x65c85826c6c54bb7_cls
from .fields import openenoc_switch_forwarding_control_pause_done_neg_0x20667a094369b26f_cls
from .fields import openenoc_switch_default_forwarding_bitmap_0x257129532b64c6c1_cls
from .fields import openenoc_switch_forwarding_table_entry_macaddr_lo_word_0x401f5d102ef44fe1_cls
from .fields import openenoc_switch_forwarding_table_entry_macaddr_hi_word_neg_0x35a9d1155aa39ddc_cls
from .fields import openenoc_switch_forwarding_table_entry_iface_bitmap_0x747871441a4d77cf_cls
from .fields import openenoc_switch_forwarding_table_entry_config_enabled_0x353241b8bf045770_cls
from .fields import openenoc_switch_info_table_depth_neg_0x3f9a2cd1e9ad77cd_cls
from .fields import openenoc_switch_info_num_of_interfaces_neg_0x562ca0ace792378d_cls
from .fields import openenoc_switch_forwarding_control_operation_mode_0x5780453cd24cad77_cls
from .fields import openenoc_switch_forwarding_control_pause_request_neg_0x2b9409c28f41c75c_cls
from .fields import openenoc_switch_forwarding_control_pause_done_neg_0x4acfc220c6966198_cls
from .fields import openenoc_switch_default_forwarding_bitmap_neg_0x2c01808eb364f792_cls
from .fields import openenoc_switch_forwarding_table_entry_macaddr_lo_word_0xf991c0ffc6e7511_cls
from .fields import openenoc_switch_forwarding_table_entry_macaddr_hi_word_neg_0x6ea049d3339059a_cls
from .fields import openenoc_switch_forwarding_table_entry_iface_bitmap_0x6291453e32946f0c_cls
from .fields import openenoc_switch_forwarding_table_entry_config_enabled_neg_0x312f6d6870ebec58_cls

# register definitions
    
    
class openenoc_csr_test_reg_0x5da4cb4348e794f_cls(RegReadWrite):
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
        
        self.__test_field:openenoc_csr_test_reg_test_field_neg_0x476e25cb214ac8aa_cls = openenoc_csr_test_reg_test_field_neg_0x476e25cb214ac8aa_cls(
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
    def test_field(self) -> openenoc_csr_test_reg_test_field_neg_0x476e25cb214ac8aa_cls:
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

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_csr_test_reg_test_field_neg_0x476e25cb214ac8aa_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.test_reg"
    @property
    def rdl_desc(self) -> str:
        return "Test register"
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.test_field
        
        
    

    
    
class openenoc_csr_regB_0x1a3dc8556819afec_cls(RegReadWrite):
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
        
        
    

    
    
class openenoc_switch_info_0x12b1e8c6ce706d78_cls(RegReadOnly):
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
        
        self.__table_depth:openenoc_switch_info_table_depth_0x68bd55d73777d304_cls = openenoc_switch_info_table_depth_0x68bd55d73777d304_cls(
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
        self.__num_of_interfaces:openenoc_switch_info_num_of_interfaces_neg_0x423de23bda410e60_cls = openenoc_switch_info_num_of_interfaces_neg_0x423de23bda410e60_cls(
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
    def table_depth(self) -> openenoc_switch_info_table_depth_0x68bd55d73777d304_cls:
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
    def num_of_interfaces(self) -> openenoc_switch_info_num_of_interfaces_neg_0x423de23bda410e60_cls:
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
    def get_child_by_system_rdl_name(self, name: Literal["table_depth"]) -> 'openenoc_switch_info_table_depth_0x68bd55d73777d304_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["num_of_interfaces"]) -> 'openenoc_switch_info_num_of_interfaces_neg_0x423de23bda410e60_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_switch_info_table_depth_0x68bd55d73777d304_cls', 'openenoc_switch_info_num_of_interfaces_neg_0x423de23bda410e60_cls', ]: ...

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
        
        
    

    
    
class openenoc_switch_forwarding_control_neg_0x70044bf2405d6f55_cls(RegReadWrite):
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
        
        self.__operation_mode:openenoc_switch_forwarding_control_operation_mode_neg_0x7b0630db069ab533_cls = openenoc_switch_forwarding_control_operation_mode_neg_0x7b0630db069ab533_cls(
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
        self.__pause_request:openenoc_switch_forwarding_control_pause_request_0x65c85826c6c54bb7_cls = openenoc_switch_forwarding_control_pause_request_0x65c85826c6c54bb7_cls(
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
        self.__pause_done:openenoc_switch_forwarding_control_pause_done_neg_0x20667a094369b26f_cls = openenoc_switch_forwarding_control_pause_done_neg_0x20667a094369b26f_cls(
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
    def operation_mode(self) -> openenoc_switch_forwarding_control_operation_mode_neg_0x7b0630db069ab533_cls:
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
    def pause_request(self) -> openenoc_switch_forwarding_control_pause_request_0x65c85826c6c54bb7_cls:
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
    def pause_done(self) -> openenoc_switch_forwarding_control_pause_done_neg_0x20667a094369b26f_cls:
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
    def get_child_by_system_rdl_name(self, name: Literal["operation_mode"]) -> 'openenoc_switch_forwarding_control_operation_mode_neg_0x7b0630db069ab533_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["pause_request"]) -> 'openenoc_switch_forwarding_control_pause_request_0x65c85826c6c54bb7_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["pause_done"]) -> 'openenoc_switch_forwarding_control_pause_done_neg_0x20667a094369b26f_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_switch_forwarding_control_operation_mode_neg_0x7b0630db069ab533_cls', 'openenoc_switch_forwarding_control_pause_request_0x65c85826c6c54bb7_cls', 'openenoc_switch_forwarding_control_pause_done_neg_0x20667a094369b26f_cls', ]: ...

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
        
        
    

    
    
class openenoc_switch_default_forwarding_neg_0x5cb240a578b8c880_cls(RegReadWrite):
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
        
        self.__bitmap:openenoc_switch_default_forwarding_bitmap_0x257129532b64c6c1_cls = openenoc_switch_default_forwarding_bitmap_0x257129532b64c6c1_cls(
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
    def bitmap(self) -> openenoc_switch_default_forwarding_bitmap_0x257129532b64c6c1_cls:
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

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_switch_default_forwarding_bitmap_0x257129532b64c6c1_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.switch1.default_forwarding"
    @property
    def rdl_desc(self) -> str:
        return "Defines the destination interface or interfaces for frames that do not match any enabled forwarding table entry."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.bitmap
        
        
    

    
    
class openenoc_switch_forwarding_table_entry_macaddr_neg_0x14d3d254a84b5846_cls(RegReadWrite):
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
        
        self.__lo_word:openenoc_switch_forwarding_table_entry_macaddr_lo_word_0x401f5d102ef44fe1_cls = openenoc_switch_forwarding_table_entry_macaddr_lo_word_0x401f5d102ef44fe1_cls(
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
        self.__hi_word:openenoc_switch_forwarding_table_entry_macaddr_hi_word_neg_0x35a9d1155aa39ddc_cls = openenoc_switch_forwarding_table_entry_macaddr_hi_word_neg_0x35a9d1155aa39ddc_cls(
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
    def lo_word(self) -> openenoc_switch_forwarding_table_entry_macaddr_lo_word_0x401f5d102ef44fe1_cls:
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
    def hi_word(self) -> openenoc_switch_forwarding_table_entry_macaddr_hi_word_neg_0x35a9d1155aa39ddc_cls:
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
    def get_child_by_system_rdl_name(self, name: Literal["lo_word"]) -> 'openenoc_switch_forwarding_table_entry_macaddr_lo_word_0x401f5d102ef44fe1_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["hi_word"]) -> 'openenoc_switch_forwarding_table_entry_macaddr_hi_word_neg_0x35a9d1155aa39ddc_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_switch_forwarding_table_entry_macaddr_lo_word_0x401f5d102ef44fe1_cls', 'openenoc_switch_forwarding_table_entry_macaddr_hi_word_neg_0x35a9d1155aa39ddc_cls', ]: ...

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
        
        
    

    
    
class openenoc_switch_forwarding_table_entry_iface_0xedc5c438162dca3_cls(RegReadWrite):
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
        
        self.__bitmap:openenoc_switch_forwarding_table_entry_iface_bitmap_0x747871441a4d77cf_cls = openenoc_switch_forwarding_table_entry_iface_bitmap_0x747871441a4d77cf_cls(
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
    def bitmap(self) -> openenoc_switch_forwarding_table_entry_iface_bitmap_0x747871441a4d77cf_cls:
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

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_switch_forwarding_table_entry_iface_bitmap_0x747871441a4d77cf_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].iface"
    @property
    def rdl_desc(self) -> str:
        return "Forwarding interface information associated with this forwarding table entry."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.bitmap
        
        
    

    
    
class openenoc_switch_forwarding_table_entry_config_neg_0x72ee666711cc8c54_cls(RegReadWrite):
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
        
        self.__enabled:openenoc_switch_forwarding_table_entry_config_enabled_0x353241b8bf045770_cls = openenoc_switch_forwarding_table_entry_config_enabled_0x353241b8bf045770_cls(
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
    def enabled(self) -> openenoc_switch_forwarding_table_entry_config_enabled_0x353241b8bf045770_cls:
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

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_switch_forwarding_table_entry_config_enabled_0x353241b8bf045770_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].config"
    @property
    def rdl_desc(self) -> str:
        return "Configuration information associated with this forwarding table entry."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.enabled
        
        
    

    
    
class openenoc_switch_info_neg_0x570f7c0834e2f2b4_cls(RegReadOnly):
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
        
        self.__table_depth:openenoc_switch_info_table_depth_neg_0x3f9a2cd1e9ad77cd_cls = openenoc_switch_info_table_depth_neg_0x3f9a2cd1e9ad77cd_cls(
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
        self.__num_of_interfaces:openenoc_switch_info_num_of_interfaces_neg_0x562ca0ace792378d_cls = openenoc_switch_info_num_of_interfaces_neg_0x562ca0ace792378d_cls(
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
    def table_depth(self) -> openenoc_switch_info_table_depth_neg_0x3f9a2cd1e9ad77cd_cls:
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
    def num_of_interfaces(self) -> openenoc_switch_info_num_of_interfaces_neg_0x562ca0ace792378d_cls:
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
    def get_child_by_system_rdl_name(self, name: Literal["table_depth"]) -> 'openenoc_switch_info_table_depth_neg_0x3f9a2cd1e9ad77cd_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["num_of_interfaces"]) -> 'openenoc_switch_info_num_of_interfaces_neg_0x562ca0ace792378d_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_switch_info_table_depth_neg_0x3f9a2cd1e9ad77cd_cls', 'openenoc_switch_info_num_of_interfaces_neg_0x562ca0ace792378d_cls', ]: ...

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
        
        
    

    
    
class openenoc_switch_forwarding_control_neg_0x39aac315524f6804_cls(RegReadWrite):
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
        
        self.__operation_mode:openenoc_switch_forwarding_control_operation_mode_0x5780453cd24cad77_cls = openenoc_switch_forwarding_control_operation_mode_0x5780453cd24cad77_cls(
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
        self.__pause_request:openenoc_switch_forwarding_control_pause_request_neg_0x2b9409c28f41c75c_cls = openenoc_switch_forwarding_control_pause_request_neg_0x2b9409c28f41c75c_cls(
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
        self.__pause_done:openenoc_switch_forwarding_control_pause_done_neg_0x4acfc220c6966198_cls = openenoc_switch_forwarding_control_pause_done_neg_0x4acfc220c6966198_cls(
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
    def operation_mode(self) -> openenoc_switch_forwarding_control_operation_mode_0x5780453cd24cad77_cls:
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
    def pause_request(self) -> openenoc_switch_forwarding_control_pause_request_neg_0x2b9409c28f41c75c_cls:
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
    def pause_done(self) -> openenoc_switch_forwarding_control_pause_done_neg_0x4acfc220c6966198_cls:
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
    def get_child_by_system_rdl_name(self, name: Literal["operation_mode"]) -> 'openenoc_switch_forwarding_control_operation_mode_0x5780453cd24cad77_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["pause_request"]) -> 'openenoc_switch_forwarding_control_pause_request_neg_0x2b9409c28f41c75c_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["pause_done"]) -> 'openenoc_switch_forwarding_control_pause_done_neg_0x4acfc220c6966198_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_switch_forwarding_control_operation_mode_0x5780453cd24cad77_cls', 'openenoc_switch_forwarding_control_pause_request_neg_0x2b9409c28f41c75c_cls', 'openenoc_switch_forwarding_control_pause_done_neg_0x4acfc220c6966198_cls', ]: ...

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
        
        
    

    
    
class openenoc_switch_default_forwarding_0x365a03a6c9b82407_cls(RegReadWrite):
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
        
        self.__bitmap:openenoc_switch_default_forwarding_bitmap_neg_0x2c01808eb364f792_cls = openenoc_switch_default_forwarding_bitmap_neg_0x2c01808eb364f792_cls(
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
    def bitmap(self) -> openenoc_switch_default_forwarding_bitmap_neg_0x2c01808eb364f792_cls:
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

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_switch_default_forwarding_bitmap_neg_0x2c01808eb364f792_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.switch2.default_forwarding"
    @property
    def rdl_desc(self) -> str:
        return "Defines the destination interface or interfaces for frames that do not match any enabled forwarding table entry."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.bitmap
        
        
    

    
    
class openenoc_switch_forwarding_table_entry_macaddr_0x2a46247d9e8d94e9_cls(RegReadWrite):
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
        
        self.__lo_word:openenoc_switch_forwarding_table_entry_macaddr_lo_word_0xf991c0ffc6e7511_cls = openenoc_switch_forwarding_table_entry_macaddr_lo_word_0xf991c0ffc6e7511_cls(
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
        self.__hi_word:openenoc_switch_forwarding_table_entry_macaddr_hi_word_neg_0x6ea049d3339059a_cls = openenoc_switch_forwarding_table_entry_macaddr_hi_word_neg_0x6ea049d3339059a_cls(
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
    def lo_word(self) -> openenoc_switch_forwarding_table_entry_macaddr_lo_word_0xf991c0ffc6e7511_cls:
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
    def hi_word(self) -> openenoc_switch_forwarding_table_entry_macaddr_hi_word_neg_0x6ea049d3339059a_cls:
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
    def get_child_by_system_rdl_name(self, name: Literal["lo_word"]) -> 'openenoc_switch_forwarding_table_entry_macaddr_lo_word_0xf991c0ffc6e7511_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["hi_word"]) -> 'openenoc_switch_forwarding_table_entry_macaddr_hi_word_neg_0x6ea049d3339059a_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_switch_forwarding_table_entry_macaddr_lo_word_0xf991c0ffc6e7511_cls', 'openenoc_switch_forwarding_table_entry_macaddr_hi_word_neg_0x6ea049d3339059a_cls', ]: ...

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
        
        
    

    
    
class openenoc_switch_forwarding_table_entry_iface_0x13d8400931b5c341_cls(RegReadWrite):
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
        
        self.__bitmap:openenoc_switch_forwarding_table_entry_iface_bitmap_0x6291453e32946f0c_cls = openenoc_switch_forwarding_table_entry_iface_bitmap_0x6291453e32946f0c_cls(
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
    def bitmap(self) -> openenoc_switch_forwarding_table_entry_iface_bitmap_0x6291453e32946f0c_cls:
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

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_switch_forwarding_table_entry_iface_bitmap_0x6291453e32946f0c_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface"
    @property
    def rdl_desc(self) -> str:
        return "Forwarding interface information associated with this forwarding table entry."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.bitmap
        
        
    

    
    
class openenoc_switch_forwarding_table_entry_config_neg_0x1d57bc6cb6d1c19_cls(RegReadWrite):
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
        
        self.__enabled:openenoc_switch_forwarding_table_entry_config_enabled_neg_0x312f6d6870ebec58_cls = openenoc_switch_forwarding_table_entry_config_enabled_neg_0x312f6d6870ebec58_cls(
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
    def enabled(self) -> openenoc_switch_forwarding_table_entry_config_enabled_neg_0x312f6d6870ebec58_cls:
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

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_switch_forwarding_table_entry_config_enabled_neg_0x312f6d6870ebec58_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config"
    @property
    def rdl_desc(self) -> str:
        return "Configuration information associated with this forwarding table entry."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.enabled
        
        
    


if __name__ == '__main__':
    pass