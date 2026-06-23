


"""
Python Wrapper for the openenoc_csr register model

This code was generated from the PeakRDL-python package version 3.1.2

"""












from typing import Iterator
from typing import Optional
from typing import Union
from typing import Type
from typing import overload
from typing import Literal
from typing import Any
from typing import NoReturn
import warnings



from ..lib import Node, NodeArray, Base
from ..lib import UDPStruct

from ..lib  import AddressMapArray, RegFileArray
from ..lib import Memory, MemoryArray
from ..lib import AddressMap
from ..lib import RegFile
from ..lib  import AddressMapArray
from ..lib  import RegFileArray
from ..lib import MemoryReadOnly, MemoryWriteOnly, MemoryReadWrite
from ..lib import MemoryReadOnlyArray, MemoryWriteOnlyArray, MemoryReadWriteArray
from ..lib import Reg, RegArray
from ..lib import RegReadOnly, RegWriteOnly, RegReadWrite
from ..lib import RegReadOnlyArray, RegWriteOnlyArray, RegReadWriteArray
from ..lib import FieldReadOnly, FieldWriteOnly, FieldReadWrite, Field

from ..lib import ReadableRegister, WritableRegister
from ..lib import ReadableMemory, WritableMemory
from ..lib import ReadableRegisterArray, WriteableRegisterArray



from ..lib import NormalCallbackSet, NormalCallbackSetLegacy





from ._registers import openenoc_csr_test_reg_neg_0x63e55094833a6beb_cls
from ._registers import openenoc_csr_regB_0x5a8939990e0f6f33_cls
from ._registers import openenoc_endpoint_info_neg_0x144752e7bb25972e_cls
from ._registers import openenoc_endpoint_config_mac_address_0x61d2410acce79936_cls
from ._registers import openenoc_endpoint_peers_entry_mac_address_neg_0x8f48d8633492ed4_cls
from ._registers import openenoc_endpoint_peers_entry_rmem_address_neg_0x62c0b86882179d7e_cls
from ._registers import openenoc_endpoint_peers_entry_local_address_0x5e831e10b41c6fb_cls
from ._registers import openenoc_endpoint_peers_entry_remote_address_neg_0x223e1b6047fd79a0_cls
from ._registers import openenoc_endpoint_peers_entry_size_0x2d529c5bcdde579c_cls
from ._registers import openenoc_endpoint_peers_entry_dma_config_0x43b8a83f649220e2_cls
from ._registers import openenoc_endpoint_info_neg_0x7b286401d99eb76f_cls
from ._registers import openenoc_endpoint_config_mac_address_neg_0x569317322d004cae_cls
from ._registers import openenoc_endpoint_peers_entry_mac_address_0x4c3b9bf94c15fd1e_cls
from ._registers import openenoc_endpoint_peers_entry_rmem_address_neg_0x6dc3b4f7bdc64903_cls
from ._registers import openenoc_endpoint_peers_entry_local_address_neg_0x1d5d26465448b9a9_cls
from ._registers import openenoc_endpoint_peers_entry_remote_address_0x6cf8d7f42e54136a_cls
from ._registers import openenoc_endpoint_peers_entry_size_0x27118595bf8e91c1_cls
from ._registers import openenoc_endpoint_peers_entry_dma_config_0x673d7a78ab6c7374_cls
from ._registers import openenoc_switch_info_0x339671246e70a307_cls
from ._registers import openenoc_switch_forwarding_control_neg_0x2f951cf3e4a74839_cls
from ._registers import openenoc_switch_default_forwarding_0x37fa1bd5f8436f51_cls
from ._registers import openenoc_switch_forwarding_table_entry_mac_address_neg_0x7fbcf3beb5f1a482_cls
from ._registers import openenoc_switch_forwarding_table_entry_iface_0x4831070b1dc215ed_cls
from ._registers import openenoc_switch_forwarding_table_entry_config_0x66f5d3fa40fe4407_cls
from ._registers import openenoc_switch_info_0x376ad29c9d8132a8_cls
from ._registers import openenoc_switch_forwarding_control_0x6f00ec9e7f97b1d2_cls
from ._registers import openenoc_switch_default_forwarding_0x4a2999255f84625b_cls
from ._registers import openenoc_switch_forwarding_table_entry_mac_address_neg_0x11105a7f760259e_cls
from ._registers import openenoc_switch_forwarding_table_entry_iface_0x567f1dd21d796db2_cls
from ._registers import openenoc_switch_forwarding_table_entry_config_0x2d231e11bf983d80_cls
from ._memories import openenoc_endpoint_rmem_0x2226a565f586b7dd_cls
from ._memories import openenoc_endpoint_rmem_0x67b8bcd87c7d73cc_cls


# addrmap, regfile, memor and register definitions
    
    
class openenoc_switch_forwarding_table_entry_neg_0x45726c49c86faa23_cls(RegFile):
    """
    Class to represent a register file in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]               |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Forwarding table entry containing the MAC address key, output   |
    |              |      interface selection, and entry configuration.</p>                  |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__mac_address', '__iface', '__config']

    def __init__(self,
                 address: int,
                 logger_handle:str,
                 inst_name:str,
                 parent:Union[AddressMap,RegFile]):

        super().__init__(address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # instance of objects within the class
        
            
        self.__mac_address:openenoc_switch_forwarding_table_entry_mac_address_neg_0x11105a7f760259e_cls = openenoc_switch_forwarding_table_entry_mac_address_neg_0x11105a7f760259e_cls(
                                                                     address=self.address+0,
                                                                     logger_handle=logger_handle+'.mac_address',
                                                                     inst_name='mac_address', parent=self)
        
            
        self.__iface:openenoc_switch_forwarding_table_entry_iface_0x567f1dd21d796db2_cls = openenoc_switch_forwarding_table_entry_iface_0x567f1dd21d796db2_cls(
                                                                     address=self.address+8,
                                                                     logger_handle=logger_handle+'.iface',
                                                                     inst_name='iface', parent=self)
        
            
        self.__config:openenoc_switch_forwarding_table_entry_config_0x2d231e11bf983d80_cls = openenoc_switch_forwarding_table_entry_config_0x2d231e11bf983d80_cls(
                                                                     address=self.address+12,
                                                                     logger_handle=logger_handle+'.config',
                                                                     inst_name='config', parent=self)
        

    @property
    def size(self) -> int:
        return 16

    # properties for Register and RegisterFiles
    @property
    def mac_address(self) -> 'openenoc_switch_forwarding_table_entry_mac_address_neg_0x11105a7f760259e_cls':
        """
        Property to access mac_address 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address   |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>48-bit destination MAC address used as the key for this         |
        |              |      forwarding table entry.</p>                                        |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__mac_address
    
    @property
    def iface(self) -> 'openenoc_switch_forwarding_table_entry_iface_0x567f1dd21d796db2_cls':
        """
        Property to access iface 

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
        return self.__iface
    
    @property
    def config(self) -> 'openenoc_switch_forwarding_table_entry_config_0x2d231e11bf983d80_cls':
        """
        Property to access config 

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
        return self.__config
    

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'mac_address':'mac_address','iface':'iface','config':'config',
            }

    
    
    
    
    
    
    # nodes:3
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["mac_address"]) -> 'openenoc_switch_forwarding_table_entry_mac_address_neg_0x11105a7f760259e_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["iface"]) -> 'openenoc_switch_forwarding_table_entry_iface_0x567f1dd21d796db2_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["config"]) -> 'openenoc_switch_forwarding_table_entry_config_0x2d231e11bf983d80_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_switch_forwarding_table_entry_mac_address_neg_0x11105a7f760259e_cls', 'openenoc_switch_forwarding_table_entry_iface_0x567f1dd21d796db2_cls', 'openenoc_switch_forwarding_table_entry_config_0x2d231e11bf983d80_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]"
    @property
    def rdl_desc(self) -> str:
        return "Forwarding table entry containing the MAC address key, output interface selection, and entry configuration."
    
    

    
    def __iter__(self) -> Iterator[Union[Node, NodeArray]]:
        
        
        yield self.mac_address
        yield self.iface
        yield self.config
        
        
class openenoc_switch_forwarding_table_entry_neg_0x45726c49c86faa23_cls_array(RegFileArray):
    """
    Class to represent a regfile array in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]               |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Forwarding table entry containing the MAC address key, output   |
    |              |      interface selection, and entry configuration.</p>                  |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__: list[str] = []

    @property
    def _element_datatype(self) -> Type[RegFile]:
        return openenoc_switch_forwarding_table_entry_neg_0x45726c49c86faa23_cls
    

    
    
class openenoc_switch_forwarding_table_0x39c99ed7cb4325f0_cls(RegFile):
    """
    Class to represent a register file in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.switch2.forwarding_table                                       |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Forwarding table used to map MAC addresses to output interface  |
    |              |      selections for frame forwarding.</p>                               |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__entry']

    def __init__(self,
                 address: int,
                 logger_handle:str,
                 inst_name:str,
                 parent:Union[AddressMap,RegFile]):

        super().__init__(address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # instance of objects within the class
        
        self.__entry:openenoc_switch_forwarding_table_entry_neg_0x45726c49c86faa23_cls_array = openenoc_switch_forwarding_table_entry_neg_0x45726c49c86faa23_cls_array(address=self.address+0,
                                                                                      stride=16,
                                                                                      dimensions=tuple([32]),
                                                                                      logger_handle=logger_handle+'.entry',
                                                                                      inst_name='entry', parent=self)
        

    @property
    def size(self) -> int:
        return 512

    # properties for Register and RegisterFiles
    @property
    def entry(self) -> 'openenoc_switch_forwarding_table_entry_neg_0x45726c49c86faa23_cls_array':
        """
        Property to access entry array

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]               |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Forwarding table entry containing the MAC address key, output   |
        |              |      interface selection, and entry configuration.</p>                  |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__entry
    

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'entry':'entry',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_switch_forwarding_table_entry_neg_0x45726c49c86faa23_cls_array':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.switch2.forwarding_table"
    @property
    def rdl_desc(self) -> str:
        return "Forwarding table used to map MAC addresses to output interface selections for frame forwarding."
    
    

    
    def __iter__(self) -> Iterator[Union[Node, NodeArray]]:
        
        
        yield self.entry
        
        
    

    
    
class openenoc_switch_neg_0x18758b2ea4675b7a_cls(AddressMap):
    """
    Class to represent a address map in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.switch2                                                        |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Control and status register map for an openENOC Switch          |
    |              |      instance. It includes configuration registers and a forwarding     |
    |              |      table used to map destination MAC address keys to output interface |
    |              |      selections for frame forwarding.</p>                               |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__info', '__forwarding_control', '__default_forwarding', '__forwarding_table']

    def __init__(self, *,
                 address:int,
                 logger_handle:str,
                 inst_name:str,
                 callbacks: Optional[Union[NormalCallbackSet, NormalCallbackSetLegacy]]=None,
                 parent:Optional[AddressMap]=None):

        if callbacks is not None:
            if not isinstance(callbacks, (NormalCallbackSet, NormalCallbackSetLegacy)):
                raise TypeError(f'callbacks should be NormalCallbackSet, NormalCallbackSetLegacy got {type(callbacks)}')

        super().__init__(callbacks=callbacks,
                         address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        
            
        self.__info:openenoc_switch_info_0x376ad29c9d8132a8_cls = openenoc_switch_info_0x376ad29c9d8132a8_cls(
                                                                     address=self.address+0,
                                                                     logger_handle=logger_handle+'.info',
                                                                     inst_name='info', parent=self)
        
            
        self.__forwarding_control:openenoc_switch_forwarding_control_0x6f00ec9e7f97b1d2_cls = openenoc_switch_forwarding_control_0x6f00ec9e7f97b1d2_cls(
                                                                     address=self.address+4,
                                                                     logger_handle=logger_handle+'.forwarding_control',
                                                                     inst_name='forwarding_control', parent=self)
        
            
        self.__default_forwarding:openenoc_switch_default_forwarding_0x4a2999255f84625b_cls = openenoc_switch_default_forwarding_0x4a2999255f84625b_cls(
                                                                     address=self.address+8,
                                                                     logger_handle=logger_handle+'.default_forwarding',
                                                                     inst_name='default_forwarding', parent=self)
        self.__forwarding_table:openenoc_switch_forwarding_table_0x39c99ed7cb4325f0_cls = openenoc_switch_forwarding_table_0x39c99ed7cb4325f0_cls(
                                                                                address=self.address+512,
                                                                                logger_handle=logger_handle+'.forwarding_table',
                                                                                inst_name='forwarding_table',
                                                                                parent=self)
        

    @property
    def size(self) -> int:
        return 1024
    @property
    def info(self) -> 'openenoc_switch_info_0x376ad29c9d8132a8_cls':
        """
        Property to access info 

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
        return self.__info
        
    @property
    def forwarding_control(self) -> 'openenoc_switch_forwarding_control_0x6f00ec9e7f97b1d2_cls':
        """
        Property to access forwarding_control 

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
        return self.__forwarding_control
        
    @property
    def default_forwarding(self) -> 'openenoc_switch_default_forwarding_0x4a2999255f84625b_cls':
        """
        Property to access default_forwarding 

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
        return self.__default_forwarding
        
    @property
    def forwarding_table(self) -> 'openenoc_switch_forwarding_table_0x39c99ed7cb4325f0_cls':
        """
        Property to access forwarding_table 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.switch2.forwarding_table                                       |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Forwarding table used to map MAC addresses to output interface  |
        |              |      selections for frame forwarding.</p>                               |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__forwarding_table
        

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'info':'info','forwarding_control':'forwarding_control','default_forwarding':'default_forwarding','forwarding_table':'forwarding_table',
            }

    
    
    
    
    
    
    # nodes:4
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["info"]) -> 'openenoc_switch_info_0x376ad29c9d8132a8_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["forwarding_control"]) -> 'openenoc_switch_forwarding_control_0x6f00ec9e7f97b1d2_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["default_forwarding"]) -> 'openenoc_switch_default_forwarding_0x4a2999255f84625b_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["forwarding_table"]) -> 'openenoc_switch_forwarding_table_0x39c99ed7cb4325f0_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_switch_info_0x376ad29c9d8132a8_cls', 'openenoc_switch_forwarding_control_0x6f00ec9e7f97b1d2_cls', 'openenoc_switch_default_forwarding_0x4a2999255f84625b_cls', 'openenoc_switch_forwarding_table_0x39c99ed7cb4325f0_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.switch2"
    @property
    def rdl_desc(self) -> str:
        return "Control and status register map for an openENOC Switch instance. It includes configuration registers and a forwarding table used to map destination MAC address keys to output interface selections for frame forwarding."
    
    

    
    def __iter__(self) -> Iterator[Union[Node, NodeArray]]:
        
        
        yield self.info
        yield self.forwarding_control
        yield self.default_forwarding
        yield self.forwarding_table
        
        
    

    
    
class openenoc_switch_forwarding_table_entry_neg_0x596c6cc2ae0297e0_cls(RegFile):
    """
    Class to represent a register file in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1]               |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Forwarding table entry containing the MAC address key, output   |
    |              |      interface selection, and entry configuration.</p>                  |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__mac_address', '__iface', '__config']

    def __init__(self,
                 address: int,
                 logger_handle:str,
                 inst_name:str,
                 parent:Union[AddressMap,RegFile]):

        super().__init__(address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # instance of objects within the class
        
            
        self.__mac_address:openenoc_switch_forwarding_table_entry_mac_address_neg_0x7fbcf3beb5f1a482_cls = openenoc_switch_forwarding_table_entry_mac_address_neg_0x7fbcf3beb5f1a482_cls(
                                                                     address=self.address+0,
                                                                     logger_handle=logger_handle+'.mac_address',
                                                                     inst_name='mac_address', parent=self)
        
            
        self.__iface:openenoc_switch_forwarding_table_entry_iface_0x4831070b1dc215ed_cls = openenoc_switch_forwarding_table_entry_iface_0x4831070b1dc215ed_cls(
                                                                     address=self.address+8,
                                                                     logger_handle=logger_handle+'.iface',
                                                                     inst_name='iface', parent=self)
        
            
        self.__config:openenoc_switch_forwarding_table_entry_config_0x66f5d3fa40fe4407_cls = openenoc_switch_forwarding_table_entry_config_0x66f5d3fa40fe4407_cls(
                                                                     address=self.address+12,
                                                                     logger_handle=logger_handle+'.config',
                                                                     inst_name='config', parent=self)
        

    @property
    def size(self) -> int:
        return 16

    # properties for Register and RegisterFiles
    @property
    def mac_address(self) -> 'openenoc_switch_forwarding_table_entry_mac_address_neg_0x7fbcf3beb5f1a482_cls':
        """
        Property to access mac_address 

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
        return self.__mac_address
    
    @property
    def iface(self) -> 'openenoc_switch_forwarding_table_entry_iface_0x4831070b1dc215ed_cls':
        """
        Property to access iface 

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
        return self.__iface
    
    @property
    def config(self) -> 'openenoc_switch_forwarding_table_entry_config_0x66f5d3fa40fe4407_cls':
        """
        Property to access config 

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
        return self.__config
    

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'mac_address':'mac_address','iface':'iface','config':'config',
            }

    
    
    
    
    
    
    # nodes:3
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["mac_address"]) -> 'openenoc_switch_forwarding_table_entry_mac_address_neg_0x7fbcf3beb5f1a482_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["iface"]) -> 'openenoc_switch_forwarding_table_entry_iface_0x4831070b1dc215ed_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["config"]) -> 'openenoc_switch_forwarding_table_entry_config_0x66f5d3fa40fe4407_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_switch_forwarding_table_entry_mac_address_neg_0x7fbcf3beb5f1a482_cls', 'openenoc_switch_forwarding_table_entry_iface_0x4831070b1dc215ed_cls', 'openenoc_switch_forwarding_table_entry_config_0x66f5d3fa40fe4407_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1]"
    @property
    def rdl_desc(self) -> str:
        return "Forwarding table entry containing the MAC address key, output interface selection, and entry configuration."
    
    

    
    def __iter__(self) -> Iterator[Union[Node, NodeArray]]:
        
        
        yield self.mac_address
        yield self.iface
        yield self.config
        
        
class openenoc_switch_forwarding_table_entry_neg_0x596c6cc2ae0297e0_cls_array(RegFileArray):
    """
    Class to represent a regfile array in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1]               |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Forwarding table entry containing the MAC address key, output   |
    |              |      interface selection, and entry configuration.</p>                  |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__: list[str] = []

    @property
    def _element_datatype(self) -> Type[RegFile]:
        return openenoc_switch_forwarding_table_entry_neg_0x596c6cc2ae0297e0_cls
    

    
    
class openenoc_switch_forwarding_table_neg_0x259c6b1fd07f64bb_cls(RegFile):
    """
    Class to represent a register file in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.switch1.forwarding_table                                       |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Forwarding table used to map MAC addresses to output interface  |
    |              |      selections for frame forwarding.</p>                               |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__entry']

    def __init__(self,
                 address: int,
                 logger_handle:str,
                 inst_name:str,
                 parent:Union[AddressMap,RegFile]):

        super().__init__(address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # instance of objects within the class
        
        self.__entry:openenoc_switch_forwarding_table_entry_neg_0x596c6cc2ae0297e0_cls_array = openenoc_switch_forwarding_table_entry_neg_0x596c6cc2ae0297e0_cls_array(address=self.address+0,
                                                                                      stride=16,
                                                                                      dimensions=tuple([8]),
                                                                                      logger_handle=logger_handle+'.entry',
                                                                                      inst_name='entry', parent=self)
        

    @property
    def size(self) -> int:
        return 128

    # properties for Register and RegisterFiles
    @property
    def entry(self) -> 'openenoc_switch_forwarding_table_entry_neg_0x596c6cc2ae0297e0_cls_array':
        """
        Property to access entry array

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1]               |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Forwarding table entry containing the MAC address key, output   |
        |              |      interface selection, and entry configuration.</p>                  |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__entry
    

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'entry':'entry',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_switch_forwarding_table_entry_neg_0x596c6cc2ae0297e0_cls_array':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.switch1.forwarding_table"
    @property
    def rdl_desc(self) -> str:
        return "Forwarding table used to map MAC addresses to output interface selections for frame forwarding."
    
    

    
    def __iter__(self) -> Iterator[Union[Node, NodeArray]]:
        
        
        yield self.entry
        
        
    

    
    
class openenoc_switch_neg_0x4d08d0cd09c95c34_cls(AddressMap):
    """
    Class to represent a address map in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.switch1                                                        |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Control and status register map for an openENOC Switch          |
    |              |      instance. It includes configuration registers and a forwarding     |
    |              |      table used to map destination MAC address keys to output interface |
    |              |      selections for frame forwarding.</p>                               |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__info', '__forwarding_control', '__default_forwarding', '__forwarding_table']

    def __init__(self, *,
                 address:int,
                 logger_handle:str,
                 inst_name:str,
                 callbacks: Optional[Union[NormalCallbackSet, NormalCallbackSetLegacy]]=None,
                 parent:Optional[AddressMap]=None):

        if callbacks is not None:
            if not isinstance(callbacks, (NormalCallbackSet, NormalCallbackSetLegacy)):
                raise TypeError(f'callbacks should be NormalCallbackSet, NormalCallbackSetLegacy got {type(callbacks)}')

        super().__init__(callbacks=callbacks,
                         address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        
            
        self.__info:openenoc_switch_info_0x339671246e70a307_cls = openenoc_switch_info_0x339671246e70a307_cls(
                                                                     address=self.address+0,
                                                                     logger_handle=logger_handle+'.info',
                                                                     inst_name='info', parent=self)
        
            
        self.__forwarding_control:openenoc_switch_forwarding_control_neg_0x2f951cf3e4a74839_cls = openenoc_switch_forwarding_control_neg_0x2f951cf3e4a74839_cls(
                                                                     address=self.address+4,
                                                                     logger_handle=logger_handle+'.forwarding_control',
                                                                     inst_name='forwarding_control', parent=self)
        
            
        self.__default_forwarding:openenoc_switch_default_forwarding_0x37fa1bd5f8436f51_cls = openenoc_switch_default_forwarding_0x37fa1bd5f8436f51_cls(
                                                                     address=self.address+8,
                                                                     logger_handle=logger_handle+'.default_forwarding',
                                                                     inst_name='default_forwarding', parent=self)
        self.__forwarding_table:openenoc_switch_forwarding_table_neg_0x259c6b1fd07f64bb_cls = openenoc_switch_forwarding_table_neg_0x259c6b1fd07f64bb_cls(
                                                                                address=self.address+128,
                                                                                logger_handle=logger_handle+'.forwarding_table',
                                                                                inst_name='forwarding_table',
                                                                                parent=self)
        

    @property
    def size(self) -> int:
        return 256
    @property
    def info(self) -> 'openenoc_switch_info_0x339671246e70a307_cls':
        """
        Property to access info 

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
        return self.__info
        
    @property
    def forwarding_control(self) -> 'openenoc_switch_forwarding_control_neg_0x2f951cf3e4a74839_cls':
        """
        Property to access forwarding_control 

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
        return self.__forwarding_control
        
    @property
    def default_forwarding(self) -> 'openenoc_switch_default_forwarding_0x37fa1bd5f8436f51_cls':
        """
        Property to access default_forwarding 

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
        return self.__default_forwarding
        
    @property
    def forwarding_table(self) -> 'openenoc_switch_forwarding_table_neg_0x259c6b1fd07f64bb_cls':
        """
        Property to access forwarding_table 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.switch1.forwarding_table                                       |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Forwarding table used to map MAC addresses to output interface  |
        |              |      selections for frame forwarding.</p>                               |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__forwarding_table
        

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'info':'info','forwarding_control':'forwarding_control','default_forwarding':'default_forwarding','forwarding_table':'forwarding_table',
            }

    
    
    
    
    
    
    # nodes:4
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["info"]) -> 'openenoc_switch_info_0x339671246e70a307_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["forwarding_control"]) -> 'openenoc_switch_forwarding_control_neg_0x2f951cf3e4a74839_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["default_forwarding"]) -> 'openenoc_switch_default_forwarding_0x37fa1bd5f8436f51_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["forwarding_table"]) -> 'openenoc_switch_forwarding_table_neg_0x259c6b1fd07f64bb_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_switch_info_0x339671246e70a307_cls', 'openenoc_switch_forwarding_control_neg_0x2f951cf3e4a74839_cls', 'openenoc_switch_default_forwarding_0x37fa1bd5f8436f51_cls', 'openenoc_switch_forwarding_table_neg_0x259c6b1fd07f64bb_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.switch1"
    @property
    def rdl_desc(self) -> str:
        return "Control and status register map for an openENOC Switch instance. It includes configuration registers and a forwarding table used to map destination MAC address keys to output interface selections for frame forwarding."
    
    

    
    def __iter__(self) -> Iterator[Union[Node, NodeArray]]:
        
        
        yield self.info
        yield self.forwarding_control
        yield self.default_forwarding
        yield self.forwarding_table
        
        
    

    
    
class openenoc_endpoint_peers_entry_neg_0x36121e79d8a9883f_cls(RegFile):
    """
    Class to represent a register file in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1]                       |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Register file for a single remote peer configuration and memory |
    |              |      region information.</p>                                            |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__mac_address', '__rmem_address', '__local_address', '__remote_address', '__size', '__dma_config']

    def __init__(self,
                 address: int,
                 logger_handle:str,
                 inst_name:str,
                 parent:Union[AddressMap,RegFile]):

        super().__init__(address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # instance of objects within the class
        
            
        self.__mac_address:openenoc_endpoint_peers_entry_mac_address_0x4c3b9bf94c15fd1e_cls = openenoc_endpoint_peers_entry_mac_address_0x4c3b9bf94c15fd1e_cls(
                                                                     address=self.address+0,
                                                                     logger_handle=logger_handle+'.mac_address',
                                                                     inst_name='mac_address', parent=self)
        
            
        self.__rmem_address:openenoc_endpoint_peers_entry_rmem_address_neg_0x6dc3b4f7bdc64903_cls = openenoc_endpoint_peers_entry_rmem_address_neg_0x6dc3b4f7bdc64903_cls(
                                                                     address=self.address+8,
                                                                     logger_handle=logger_handle+'.rmem_address',
                                                                     inst_name='rmem_address', parent=self)
        
            
        self.__local_address:openenoc_endpoint_peers_entry_local_address_neg_0x1d5d26465448b9a9_cls = openenoc_endpoint_peers_entry_local_address_neg_0x1d5d26465448b9a9_cls(
                                                                     address=self.address+12,
                                                                     logger_handle=logger_handle+'.local_address',
                                                                     inst_name='local_address', parent=self)
        
            
        self.__remote_address:openenoc_endpoint_peers_entry_remote_address_0x6cf8d7f42e54136a_cls = openenoc_endpoint_peers_entry_remote_address_0x6cf8d7f42e54136a_cls(
                                                                     address=self.address+16,
                                                                     logger_handle=logger_handle+'.remote_address',
                                                                     inst_name='remote_address', parent=self)
        
            
        self.__size:openenoc_endpoint_peers_entry_size_0x27118595bf8e91c1_cls = openenoc_endpoint_peers_entry_size_0x27118595bf8e91c1_cls(
                                                                     address=self.address+20,
                                                                     logger_handle=logger_handle+'.size',
                                                                     inst_name='size', parent=self)
        
            
        self.__dma_config:openenoc_endpoint_peers_entry_dma_config_0x673d7a78ab6c7374_cls = openenoc_endpoint_peers_entry_dma_config_0x673d7a78ab6c7374_cls(
                                                                     address=self.address+24,
                                                                     logger_handle=logger_handle+'.dma_config',
                                                                     inst_name='dma_config', parent=self)
        

    @property
    def size(self) -> int:
        return 28

    # properties for Register and RegisterFiles
    @property
    def mac_address(self) -> 'openenoc_endpoint_peers_entry_mac_address_0x4c3b9bf94c15fd1e_cls':
        """
        Property to access mac_address 

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
        return self.__mac_address
    
    @property
    def rmem_address(self) -> 'openenoc_endpoint_peers_entry_rmem_address_neg_0x6dc3b4f7bdc64903_cls':
        """
        Property to access rmem_address 

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
        return self.__rmem_address
    
    @property
    def local_address(self) -> 'openenoc_endpoint_peers_entry_local_address_neg_0x1d5d26465448b9a9_cls':
        """
        Property to access local_address 

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
        return self.__local_address
    
    @property
    def remote_address(self) -> 'openenoc_endpoint_peers_entry_remote_address_0x6cf8d7f42e54136a_cls':
        """
        Property to access remote_address 

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
        return self.__remote_address
    
    @property
    def register_size(self) -> 'openenoc_endpoint_peers_entry_size_0x27118595bf8e91c1_cls':
        """
        Property to access size 

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
        return self.__size
    
    @property
    def dma_config(self) -> 'openenoc_endpoint_peers_entry_dma_config_0x673d7a78ab6c7374_cls':
        """
        Property to access dma_config 

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
        return self.__dma_config
    

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'mac_address':'mac_address','rmem_address':'rmem_address','local_address':'local_address','remote_address':'remote_address','size':'register_size','dma_config':'dma_config',
            }

    
    
    
    
    
    
    # nodes:6
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["mac_address"]) -> 'openenoc_endpoint_peers_entry_mac_address_0x4c3b9bf94c15fd1e_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["rmem_address"]) -> 'openenoc_endpoint_peers_entry_rmem_address_neg_0x6dc3b4f7bdc64903_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["local_address"]) -> 'openenoc_endpoint_peers_entry_local_address_neg_0x1d5d26465448b9a9_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["remote_address"]) -> 'openenoc_endpoint_peers_entry_remote_address_0x6cf8d7f42e54136a_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["size"]) -> 'openenoc_endpoint_peers_entry_size_0x27118595bf8e91c1_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["dma_config"]) -> 'openenoc_endpoint_peers_entry_dma_config_0x673d7a78ab6c7374_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_peers_entry_mac_address_0x4c3b9bf94c15fd1e_cls', 'openenoc_endpoint_peers_entry_rmem_address_neg_0x6dc3b4f7bdc64903_cls', 'openenoc_endpoint_peers_entry_local_address_neg_0x1d5d26465448b9a9_cls', 'openenoc_endpoint_peers_entry_remote_address_0x6cf8d7f42e54136a_cls', 'openenoc_endpoint_peers_entry_size_0x27118595bf8e91c1_cls', 'openenoc_endpoint_peers_entry_dma_config_0x673d7a78ab6c7374_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1]"
    @property
    def rdl_desc(self) -> str:
        return "Register file for a single remote peer configuration and memory region information."
    
    

    
    def __iter__(self) -> Iterator[Union[Node, NodeArray]]:
        
        
        yield self.mac_address
        yield self.rmem_address
        yield self.local_address
        yield self.remote_address
        yield self.register_size
        yield self.dma_config
        
        
class openenoc_endpoint_peers_entry_neg_0x36121e79d8a9883f_cls_array(RegFileArray):
    """
    Class to represent a regfile array in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1]                       |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Register file for a single remote peer configuration and memory |
    |              |      region information.</p>                                            |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__: list[str] = []

    @property
    def _element_datatype(self) -> Type[RegFile]:
        return openenoc_endpoint_peers_entry_neg_0x36121e79d8a9883f_cls
    

    
    
class openenoc_endpoint_peers_neg_0x70c83387264542f3_cls(RegFile):
    """
    Class to represent a register file in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint2.peers                                                |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Register file for remote peer configuration and memory region   |
    |              |      information.</p>                                                   |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__entry']

    def __init__(self,
                 address: int,
                 logger_handle:str,
                 inst_name:str,
                 parent:Union[AddressMap,RegFile]):

        super().__init__(address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # instance of objects within the class
        
        self.__entry:openenoc_endpoint_peers_entry_neg_0x36121e79d8a9883f_cls_array = openenoc_endpoint_peers_entry_neg_0x36121e79d8a9883f_cls_array(address=self.address+0,
                                                                                      stride=28,
                                                                                      dimensions=tuple([2]),
                                                                                      logger_handle=logger_handle+'.entry',
                                                                                      inst_name='entry', parent=self)
        

    @property
    def size(self) -> int:
        return 56

    # properties for Register and RegisterFiles
    @property
    def entry(self) -> 'openenoc_endpoint_peers_entry_neg_0x36121e79d8a9883f_cls_array':
        """
        Property to access entry array

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1]                       |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Register file for a single remote peer configuration and memory |
        |              |      region information.</p>                                            |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__entry
    

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'entry':'entry',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_peers_entry_neg_0x36121e79d8a9883f_cls_array':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint2.peers"
    @property
    def rdl_desc(self) -> str:
        return "Register file for remote peer configuration and memory region information."
    
    

    
    def __iter__(self) -> Iterator[Union[Node, NodeArray]]:
        
        
        yield self.entry
        
        
    

    
    
class openenoc_endpoint_config_neg_0x38a152f39880389e_cls(RegFile):
    """
    Class to represent a register file in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint2.config                                               |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Configuration register file for this openENOC Endpoint          |
    |              |      Interface instance.</p>                                            |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__mac_address']

    def __init__(self,
                 address: int,
                 logger_handle:str,
                 inst_name:str,
                 parent:Union[AddressMap,RegFile]):

        super().__init__(address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # instance of objects within the class
        
            
        self.__mac_address:openenoc_endpoint_config_mac_address_neg_0x569317322d004cae_cls = openenoc_endpoint_config_mac_address_neg_0x569317322d004cae_cls(
                                                                     address=self.address+0,
                                                                     logger_handle=logger_handle+'.mac_address',
                                                                     inst_name='mac_address', parent=self)
        

    @property
    def size(self) -> int:
        return 8

    # properties for Register and RegisterFiles
    @property
    def mac_address(self) -> 'openenoc_endpoint_config_mac_address_neg_0x569317322d004cae_cls':
        """
        Property to access mac_address 

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
        return self.__mac_address
    

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'mac_address':'mac_address',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_config_mac_address_neg_0x569317322d004cae_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint2.config"
    @property
    def rdl_desc(self) -> str:
        return "Configuration register file for this openENOC Endpoint Interface instance."
    
    

    
    def __iter__(self) -> Iterator[Union[Node, NodeArray]]:
        
        
        yield self.mac_address
        
        
    

    
    
class openenoc_endpoint_neg_0x2f5175b626adbc0f_cls(AddressMap):
    """
    Class to represent a address map in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint2                                                      |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Control and status register map for an openENOC Endpoint        |
    |              |      Interface instance.</p>                                            |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__info', '__config', '__peers', '__rmem']

    def __init__(self, *,
                 address:int,
                 logger_handle:str,
                 inst_name:str,
                 callbacks: Optional[Union[NormalCallbackSet, NormalCallbackSetLegacy]]=None,
                 parent:Optional[AddressMap]=None):

        if callbacks is not None:
            if not isinstance(callbacks, (NormalCallbackSet, NormalCallbackSetLegacy)):
                raise TypeError(f'callbacks should be NormalCallbackSet, NormalCallbackSetLegacy got {type(callbacks)}')

        super().__init__(callbacks=callbacks,
                         address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        
            
        self.__info:openenoc_endpoint_info_neg_0x7b286401d99eb76f_cls = openenoc_endpoint_info_neg_0x7b286401d99eb76f_cls(
                                                                     address=self.address+0,
                                                                     logger_handle=logger_handle+'.info',
                                                                     inst_name='info', parent=self)
        self.__config:openenoc_endpoint_config_neg_0x38a152f39880389e_cls = openenoc_endpoint_config_neg_0x38a152f39880389e_cls(
                                                                                address=self.address+8,
                                                                                logger_handle=logger_handle+'.config',
                                                                                inst_name='config',
                                                                                parent=self)
        self.__peers:openenoc_endpoint_peers_neg_0x70c83387264542f3_cls = openenoc_endpoint_peers_neg_0x70c83387264542f3_cls(
                                                                                address=self.address+64,
                                                                                logger_handle=logger_handle+'.peers',
                                                                                inst_name='peers',
                                                                                parent=self)
        
        self.__rmem:openenoc_endpoint_rmem_0x67b8bcd87c7d73cc_cls = openenoc_endpoint_rmem_0x67b8bcd87c7d73cc_cls(
                                                                     address=self.address+512,
                                                                     logger_handle=logger_handle+'.rmem',
                                                                                       inst_name='rmem', parent=self)
        

    @property
    def size(self) -> int:
        return 1024
    @property
    def info(self) -> 'openenoc_endpoint_info_neg_0x7b286401d99eb76f_cls':
        """
        Property to access info 

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
        return self.__info
        
    @property
    def config(self) -> 'openenoc_endpoint_config_neg_0x38a152f39880389e_cls':
        """
        Property to access config 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint2.config                                               |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Configuration register file for this openENOC Endpoint          |
        |              |      Interface instance.</p>                                            |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__config
        
    @property
    def peers(self) -> 'openenoc_endpoint_peers_neg_0x70c83387264542f3_cls':
        """
        Property to access peers 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint2.peers                                                |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Register file for remote peer configuration and memory region   |
        |              |      information.</p>                                                   |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__peers
        
    @property
    def rmem(self) -> 'openenoc_endpoint_rmem_0x67b8bcd87c7d73cc_cls':
        """
        Property to access rmem 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      rmem                                                               |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Virtual memory region for all remote peers, with offsets and    |
        |              |      sizes defined in the peers regfile.</p>                            |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__rmem
        

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'info':'info','config':'config','peers':'peers','rmem':'rmem',
            }

    
    
    
    
    
    
    # nodes:4
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["info"]) -> 'openenoc_endpoint_info_neg_0x7b286401d99eb76f_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["config"]) -> 'openenoc_endpoint_config_neg_0x38a152f39880389e_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["peers"]) -> 'openenoc_endpoint_peers_neg_0x70c83387264542f3_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["rmem"]) -> 'openenoc_endpoint_rmem_0x67b8bcd87c7d73cc_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_info_neg_0x7b286401d99eb76f_cls', 'openenoc_endpoint_config_neg_0x38a152f39880389e_cls', 'openenoc_endpoint_peers_neg_0x70c83387264542f3_cls', 'openenoc_endpoint_rmem_0x67b8bcd87c7d73cc_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint2"
    @property
    def rdl_desc(self) -> str:
        return "Control and status register map for an openENOC Endpoint Interface instance."
    
    

    
    def __iter__(self) -> Iterator[Union[Node, NodeArray]]:
        
        
        yield self.info
        yield self.config
        yield self.peers
        yield self.rmem
        
        
    

    
    
class openenoc_endpoint_peers_entry_0x44741467ecde707e_cls(RegFile):
    """
    Class to represent a register file in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1]                       |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Register file for a single remote peer configuration and memory |
    |              |      region information.</p>                                            |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__mac_address', '__rmem_address', '__local_address', '__remote_address', '__size', '__dma_config']

    def __init__(self,
                 address: int,
                 logger_handle:str,
                 inst_name:str,
                 parent:Union[AddressMap,RegFile]):

        super().__init__(address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # instance of objects within the class
        
            
        self.__mac_address:openenoc_endpoint_peers_entry_mac_address_neg_0x8f48d8633492ed4_cls = openenoc_endpoint_peers_entry_mac_address_neg_0x8f48d8633492ed4_cls(
                                                                     address=self.address+0,
                                                                     logger_handle=logger_handle+'.mac_address',
                                                                     inst_name='mac_address', parent=self)
        
            
        self.__rmem_address:openenoc_endpoint_peers_entry_rmem_address_neg_0x62c0b86882179d7e_cls = openenoc_endpoint_peers_entry_rmem_address_neg_0x62c0b86882179d7e_cls(
                                                                     address=self.address+8,
                                                                     logger_handle=logger_handle+'.rmem_address',
                                                                     inst_name='rmem_address', parent=self)
        
            
        self.__local_address:openenoc_endpoint_peers_entry_local_address_0x5e831e10b41c6fb_cls = openenoc_endpoint_peers_entry_local_address_0x5e831e10b41c6fb_cls(
                                                                     address=self.address+12,
                                                                     logger_handle=logger_handle+'.local_address',
                                                                     inst_name='local_address', parent=self)
        
            
        self.__remote_address:openenoc_endpoint_peers_entry_remote_address_neg_0x223e1b6047fd79a0_cls = openenoc_endpoint_peers_entry_remote_address_neg_0x223e1b6047fd79a0_cls(
                                                                     address=self.address+16,
                                                                     logger_handle=logger_handle+'.remote_address',
                                                                     inst_name='remote_address', parent=self)
        
            
        self.__size:openenoc_endpoint_peers_entry_size_0x2d529c5bcdde579c_cls = openenoc_endpoint_peers_entry_size_0x2d529c5bcdde579c_cls(
                                                                     address=self.address+20,
                                                                     logger_handle=logger_handle+'.size',
                                                                     inst_name='size', parent=self)
        
            
        self.__dma_config:openenoc_endpoint_peers_entry_dma_config_0x43b8a83f649220e2_cls = openenoc_endpoint_peers_entry_dma_config_0x43b8a83f649220e2_cls(
                                                                     address=self.address+24,
                                                                     logger_handle=logger_handle+'.dma_config',
                                                                     inst_name='dma_config', parent=self)
        

    @property
    def size(self) -> int:
        return 28

    # properties for Register and RegisterFiles
    @property
    def mac_address(self) -> 'openenoc_endpoint_peers_entry_mac_address_neg_0x8f48d8633492ed4_cls':
        """
        Property to access mac_address 

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
        return self.__mac_address
    
    @property
    def rmem_address(self) -> 'openenoc_endpoint_peers_entry_rmem_address_neg_0x62c0b86882179d7e_cls':
        """
        Property to access rmem_address 

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
        return self.__rmem_address
    
    @property
    def local_address(self) -> 'openenoc_endpoint_peers_entry_local_address_0x5e831e10b41c6fb_cls':
        """
        Property to access local_address 

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
        return self.__local_address
    
    @property
    def remote_address(self) -> 'openenoc_endpoint_peers_entry_remote_address_neg_0x223e1b6047fd79a0_cls':
        """
        Property to access remote_address 

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
        return self.__remote_address
    
    @property
    def register_size(self) -> 'openenoc_endpoint_peers_entry_size_0x2d529c5bcdde579c_cls':
        """
        Property to access size 

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
        return self.__size
    
    @property
    def dma_config(self) -> 'openenoc_endpoint_peers_entry_dma_config_0x43b8a83f649220e2_cls':
        """
        Property to access dma_config 

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
        return self.__dma_config
    

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'mac_address':'mac_address','rmem_address':'rmem_address','local_address':'local_address','remote_address':'remote_address','size':'register_size','dma_config':'dma_config',
            }

    
    
    
    
    
    
    # nodes:6
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["mac_address"]) -> 'openenoc_endpoint_peers_entry_mac_address_neg_0x8f48d8633492ed4_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["rmem_address"]) -> 'openenoc_endpoint_peers_entry_rmem_address_neg_0x62c0b86882179d7e_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["local_address"]) -> 'openenoc_endpoint_peers_entry_local_address_0x5e831e10b41c6fb_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["remote_address"]) -> 'openenoc_endpoint_peers_entry_remote_address_neg_0x223e1b6047fd79a0_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["size"]) -> 'openenoc_endpoint_peers_entry_size_0x2d529c5bcdde579c_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["dma_config"]) -> 'openenoc_endpoint_peers_entry_dma_config_0x43b8a83f649220e2_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_peers_entry_mac_address_neg_0x8f48d8633492ed4_cls', 'openenoc_endpoint_peers_entry_rmem_address_neg_0x62c0b86882179d7e_cls', 'openenoc_endpoint_peers_entry_local_address_0x5e831e10b41c6fb_cls', 'openenoc_endpoint_peers_entry_remote_address_neg_0x223e1b6047fd79a0_cls', 'openenoc_endpoint_peers_entry_size_0x2d529c5bcdde579c_cls', 'openenoc_endpoint_peers_entry_dma_config_0x43b8a83f649220e2_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1]"
    @property
    def rdl_desc(self) -> str:
        return "Register file for a single remote peer configuration and memory region information."
    
    

    
    def __iter__(self) -> Iterator[Union[Node, NodeArray]]:
        
        
        yield self.mac_address
        yield self.rmem_address
        yield self.local_address
        yield self.remote_address
        yield self.register_size
        yield self.dma_config
        
        
class openenoc_endpoint_peers_entry_0x44741467ecde707e_cls_array(RegFileArray):
    """
    Class to represent a regfile array in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1]                       |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Register file for a single remote peer configuration and memory |
    |              |      region information.</p>                                            |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__: list[str] = []

    @property
    def _element_datatype(self) -> Type[RegFile]:
        return openenoc_endpoint_peers_entry_0x44741467ecde707e_cls
    

    
    
class openenoc_endpoint_peers_0x296c871c67e3abab_cls(RegFile):
    """
    Class to represent a register file in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint1.peers                                                |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Register file for remote peer configuration and memory region   |
    |              |      information.</p>                                                   |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__entry']

    def __init__(self,
                 address: int,
                 logger_handle:str,
                 inst_name:str,
                 parent:Union[AddressMap,RegFile]):

        super().__init__(address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # instance of objects within the class
        
        self.__entry:openenoc_endpoint_peers_entry_0x44741467ecde707e_cls_array = openenoc_endpoint_peers_entry_0x44741467ecde707e_cls_array(address=self.address+0,
                                                                                      stride=28,
                                                                                      dimensions=tuple([4]),
                                                                                      logger_handle=logger_handle+'.entry',
                                                                                      inst_name='entry', parent=self)
        

    @property
    def size(self) -> int:
        return 112

    # properties for Register and RegisterFiles
    @property
    def entry(self) -> 'openenoc_endpoint_peers_entry_0x44741467ecde707e_cls_array':
        """
        Property to access entry array

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1]                       |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Register file for a single remote peer configuration and memory |
        |              |      region information.</p>                                            |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__entry
    

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'entry':'entry',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_peers_entry_0x44741467ecde707e_cls_array':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint1.peers"
    @property
    def rdl_desc(self) -> str:
        return "Register file for remote peer configuration and memory region information."
    
    

    
    def __iter__(self) -> Iterator[Union[Node, NodeArray]]:
        
        
        yield self.entry
        
        
    

    
    
class openenoc_endpoint_config_neg_0x65761fef90733e54_cls(RegFile):
    """
    Class to represent a register file in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint1.config                                               |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Configuration register file for this openENOC Endpoint          |
    |              |      Interface instance.</p>                                            |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__mac_address']

    def __init__(self,
                 address: int,
                 logger_handle:str,
                 inst_name:str,
                 parent:Union[AddressMap,RegFile]):

        super().__init__(address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        # instance of objects within the class
        
            
        self.__mac_address:openenoc_endpoint_config_mac_address_0x61d2410acce79936_cls = openenoc_endpoint_config_mac_address_0x61d2410acce79936_cls(
                                                                     address=self.address+0,
                                                                     logger_handle=logger_handle+'.mac_address',
                                                                     inst_name='mac_address', parent=self)
        

    @property
    def size(self) -> int:
        return 8

    # properties for Register and RegisterFiles
    @property
    def mac_address(self) -> 'openenoc_endpoint_config_mac_address_0x61d2410acce79936_cls':
        """
        Property to access mac_address 

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
        return self.__mac_address
    

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'mac_address':'mac_address',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_config_mac_address_0x61d2410acce79936_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint1.config"
    @property
    def rdl_desc(self) -> str:
        return "Configuration register file for this openENOC Endpoint Interface instance."
    
    

    
    def __iter__(self) -> Iterator[Union[Node, NodeArray]]:
        
        
        yield self.mac_address
        
        
    

    
    
class openenoc_endpoint_0x4ad6110f15032c47_cls(AddressMap):
    """
    Class to represent a address map in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint1                                                      |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Control and status register map for an openENOC Endpoint        |
    |              |      Interface instance.</p>                                            |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__info', '__config', '__peers', '__rmem']

    def __init__(self, *,
                 address:int,
                 logger_handle:str,
                 inst_name:str,
                 callbacks: Optional[Union[NormalCallbackSet, NormalCallbackSetLegacy]]=None,
                 parent:Optional[AddressMap]=None):

        if callbacks is not None:
            if not isinstance(callbacks, (NormalCallbackSet, NormalCallbackSetLegacy)):
                raise TypeError(f'callbacks should be NormalCallbackSet, NormalCallbackSetLegacy got {type(callbacks)}')

        super().__init__(callbacks=callbacks,
                         address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        
            
        self.__info:openenoc_endpoint_info_neg_0x144752e7bb25972e_cls = openenoc_endpoint_info_neg_0x144752e7bb25972e_cls(
                                                                     address=self.address+0,
                                                                     logger_handle=logger_handle+'.info',
                                                                     inst_name='info', parent=self)
        self.__config:openenoc_endpoint_config_neg_0x65761fef90733e54_cls = openenoc_endpoint_config_neg_0x65761fef90733e54_cls(
                                                                                address=self.address+8,
                                                                                logger_handle=logger_handle+'.config',
                                                                                inst_name='config',
                                                                                parent=self)
        self.__peers:openenoc_endpoint_peers_0x296c871c67e3abab_cls = openenoc_endpoint_peers_0x296c871c67e3abab_cls(
                                                                                address=self.address+128,
                                                                                logger_handle=logger_handle+'.peers',
                                                                                inst_name='peers',
                                                                                parent=self)
        
        self.__rmem:openenoc_endpoint_rmem_0x2226a565f586b7dd_cls = openenoc_endpoint_rmem_0x2226a565f586b7dd_cls(
                                                                     address=self.address+1024,
                                                                     logger_handle=logger_handle+'.rmem',
                                                                                       inst_name='rmem', parent=self)
        

    @property
    def size(self) -> int:
        return 2048
    @property
    def info(self) -> 'openenoc_endpoint_info_neg_0x144752e7bb25972e_cls':
        """
        Property to access info 

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
        return self.__info
        
    @property
    def config(self) -> 'openenoc_endpoint_config_neg_0x65761fef90733e54_cls':
        """
        Property to access config 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint1.config                                               |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Configuration register file for this openENOC Endpoint          |
        |              |      Interface instance.</p>                                            |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__config
        
    @property
    def peers(self) -> 'openenoc_endpoint_peers_0x296c871c67e3abab_cls':
        """
        Property to access peers 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint1.peers                                                |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Register file for remote peer configuration and memory region   |
        |              |      information.</p>                                                   |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__peers
        
    @property
    def rmem(self) -> 'openenoc_endpoint_rmem_0x2226a565f586b7dd_cls':
        """
        Property to access rmem 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      rmem                                                               |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Virtual memory region for all remote peers, with offsets and    |
        |              |      sizes defined in the peers regfile.</p>                            |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__rmem
        

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'info':'info','config':'config','peers':'peers','rmem':'rmem',
            }

    
    
    
    
    
    
    # nodes:4
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["info"]) -> 'openenoc_endpoint_info_neg_0x144752e7bb25972e_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["config"]) -> 'openenoc_endpoint_config_neg_0x65761fef90733e54_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["peers"]) -> 'openenoc_endpoint_peers_0x296c871c67e3abab_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["rmem"]) -> 'openenoc_endpoint_rmem_0x2226a565f586b7dd_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_info_neg_0x144752e7bb25972e_cls', 'openenoc_endpoint_config_neg_0x65761fef90733e54_cls', 'openenoc_endpoint_peers_0x296c871c67e3abab_cls', 'openenoc_endpoint_rmem_0x2226a565f586b7dd_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint1"
    @property
    def rdl_desc(self) -> str:
        return "Control and status register map for an openENOC Endpoint Interface instance."
    
    

    
    def __iter__(self) -> Iterator[Union[Node, NodeArray]]:
        
        
        yield self.info
        yield self.config
        yield self.peers
        yield self.rmem
        
        
    

    
    
class openenoc_csr_0x7c1295420f17b538_cls(AddressMap):
    """
    Class to represent a address map in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr                                                                |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>openENOC CSR</p>                                                |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__test_reg', '__regB', '__endpoint1', '__endpoint2', '__switch1', '__switch2']

    def __init__(self, *,
                 address:int=0,
                 logger_handle:str='reg_model.openenoc_csr',
                 inst_name:str='openenoc_csr',
                 callbacks: Optional[Union[NormalCallbackSet, NormalCallbackSetLegacy]]=None,
                 parent:Optional[AddressMap]=None):

        if callbacks is not None:
            if not isinstance(callbacks, (NormalCallbackSet, NormalCallbackSetLegacy)):
                raise TypeError(f'callbacks should be NormalCallbackSet, NormalCallbackSetLegacy got {type(callbacks)}')

        super().__init__(callbacks=callbacks,
                         address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        
            
        self.__test_reg:openenoc_csr_test_reg_neg_0x63e55094833a6beb_cls = openenoc_csr_test_reg_neg_0x63e55094833a6beb_cls(
                                                                     address=self.address+0,
                                                                     logger_handle=logger_handle+'.test_reg',
                                                                     inst_name='test_reg', parent=self)
        
            
        self.__regB:openenoc_csr_regB_0x5a8939990e0f6f33_cls = openenoc_csr_regB_0x5a8939990e0f6f33_cls(
                                                                     address=self.address+4,
                                                                     logger_handle=logger_handle+'.regB',
                                                                     inst_name='regB', parent=self)
        self.__endpoint1:openenoc_endpoint_0x4ad6110f15032c47_cls = openenoc_endpoint_0x4ad6110f15032c47_cls(
                                                                                address=self.address+2048,
                                                                                logger_handle=logger_handle+'.endpoint1',
                                                                                inst_name='endpoint1',
                                                                                parent=self)
        self.__endpoint2:openenoc_endpoint_neg_0x2f5175b626adbc0f_cls = openenoc_endpoint_neg_0x2f5175b626adbc0f_cls(
                                                                                address=self.address+4096,
                                                                                logger_handle=logger_handle+'.endpoint2',
                                                                                inst_name='endpoint2',
                                                                                parent=self)
        self.__switch1:openenoc_switch_neg_0x4d08d0cd09c95c34_cls = openenoc_switch_neg_0x4d08d0cd09c95c34_cls(
                                                                                address=self.address+5120,
                                                                                logger_handle=logger_handle+'.switch1',
                                                                                inst_name='switch1',
                                                                                parent=self)
        self.__switch2:openenoc_switch_neg_0x18758b2ea4675b7a_cls = openenoc_switch_neg_0x18758b2ea4675b7a_cls(
                                                                                address=self.address+6144,
                                                                                logger_handle=logger_handle+'.switch2',
                                                                                inst_name='switch2',
                                                                                parent=self)
        

    @property
    def size(self) -> int:
        return 7168
    @property
    def test_reg(self) -> 'openenoc_csr_test_reg_neg_0x63e55094833a6beb_cls':
        """
        Property to access test_reg 

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
        return self.__test_reg
        
    @property
    def regB(self) -> 'openenoc_csr_regB_0x5a8939990e0f6f33_cls':
        """
        Property to access regB 

        
        """
        return self.__regB
        
    @property
    def endpoint1(self) -> 'openenoc_endpoint_0x4ad6110f15032c47_cls':
        """
        Property to access endpoint1 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint1                                                      |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Control and status register map for an openENOC Endpoint        |
        |              |      Interface instance.</p>                                            |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__endpoint1
        
    @property
    def endpoint2(self) -> 'openenoc_endpoint_neg_0x2f5175b626adbc0f_cls':
        """
        Property to access endpoint2 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint2                                                      |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Control and status register map for an openENOC Endpoint        |
        |              |      Interface instance.</p>                                            |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__endpoint2
        
    @property
    def switch1(self) -> 'openenoc_switch_neg_0x4d08d0cd09c95c34_cls':
        """
        Property to access switch1 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.switch1                                                        |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Control and status register map for an openENOC Switch          |
        |              |      instance. It includes configuration registers and a forwarding     |
        |              |      table used to map destination MAC address keys to output interface |
        |              |      selections for frame forwarding.</p>                               |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__switch1
        
    @property
    def switch2(self) -> 'openenoc_switch_neg_0x18758b2ea4675b7a_cls':
        """
        Property to access switch2 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.switch2                                                        |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Control and status register map for an openENOC Switch          |
        |              |      instance. It includes configuration registers and a forwarding     |
        |              |      table used to map destination MAC address keys to output interface |
        |              |      selections for frame forwarding.</p>                               |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__switch2
        

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'test_reg':'test_reg','regB':'regB','endpoint1':'endpoint1','endpoint2':'endpoint2','switch1':'switch1','switch2':'switch2',
            }

    
    
    
    
    
    
    # nodes:6
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["test_reg"]) -> 'openenoc_csr_test_reg_neg_0x63e55094833a6beb_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["regB"]) -> 'openenoc_csr_regB_0x5a8939990e0f6f33_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["endpoint1"]) -> 'openenoc_endpoint_0x4ad6110f15032c47_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["endpoint2"]) -> 'openenoc_endpoint_neg_0x2f5175b626adbc0f_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["switch1"]) -> 'openenoc_switch_neg_0x4d08d0cd09c95c34_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["switch2"]) -> 'openenoc_switch_neg_0x18758b2ea4675b7a_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_csr_test_reg_neg_0x63e55094833a6beb_cls', 'openenoc_csr_regB_0x5a8939990e0f6f33_cls', 'openenoc_endpoint_0x4ad6110f15032c47_cls', 'openenoc_endpoint_neg_0x2f5175b626adbc0f_cls', 'openenoc_switch_neg_0x4d08d0cd09c95c34_cls', 'openenoc_switch_neg_0x18758b2ea4675b7a_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr"
    @property
    def rdl_desc(self) -> str:
        return "openENOC CSR"
    
    

    
    def __iter__(self) -> Iterator[Union[Node, NodeArray]]:
        
        
        yield self.test_reg
        yield self.regB
        yield self.endpoint1
        yield self.endpoint2
        yield self.switch1
        yield self.switch2
        
        
    


openenoc_csr_cls = openenoc_csr_0x7c1295420f17b538_cls

if __name__ == '__main__':
    # dummy functions to demonstrate the class
    def read_addr_space(addr: int, width: int, accesswidth: int) -> int:
        """
        Callback to simulate the operation of the package, everytime the read is called, it will
        request the user input the value to be read back.

        Args:
            addr: Address to write to
            width: Width of the register in bits
            accesswidth: Minimum access width of the register in bits

        Returns:
            value inputted by the used
        """
        assert isinstance(addr, int)
        assert isinstance(width, int)
        assert isinstance(accesswidth, int)
        return int(input('value to read from address:0x%X'%addr))

    def write_addr_space(addr: int, width: int, accesswidth: int, data: int) -> None:
        """
        Callback to simulate the operation of the package, everytime the read is called, it will
        request the user input the value to be read back.

        Args:
            addr: Address to write to
            width: Width of the register in bits
            accesswidth: Minimum access width of the register in bits
            data: value to be written to the register

        Returns:
            None
        """
        assert isinstance(addr, int)
        assert isinstance(width, int)
        assert isinstance(accesswidth, int)
        assert isinstance(data, int)
        print('write data:0x%X to address:0x%X'%(data, addr))

    # create an instance of the class
    openenoc_csr = openenoc_csr_cls(callbacks = NormalCallbackSet(read_callback=read_addr_space,
                                                                                                     write_callback=write_addr_space))