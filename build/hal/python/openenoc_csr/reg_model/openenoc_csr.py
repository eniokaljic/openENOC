


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





from ._registers import openenoc_csr_test_reg_0x69f601ad22f2142_cls
from ._registers import openenoc_csr_regB_neg_0xe16f3a07eae63d6_cls
from ._registers import openenoc_endpoint_info_neg_0x735b88c1b28e8f33_cls
from ._registers import openenoc_endpoint_config_mac_address_neg_0x6ed055f4bee94bd2_cls
from ._registers import openenoc_endpoint_axis_if_source_data_0x2362d42deed0b943_cls
from ._registers import openenoc_endpoint_axis_if_source_control_neg_0x1b2b7f048b6aeae_cls
from ._registers import openenoc_endpoint_axis_if_source_status_neg_0xfee0a2f3b74c649_cls
from ._registers import openenoc_endpoint_axis_if_sink_data_0x2565dea76eeba99d_cls
from ._registers import openenoc_endpoint_axis_if_sink_control_0x2fa17f6b8f2565d1_cls
from ._registers import openenoc_endpoint_axis_if_sink_status_0x664a8cd7a8dcd9f1_cls
from ._registers import openenoc_endpoint_peers_entry_mac_address_0x78cedd86ea7d8cba_cls
from ._registers import openenoc_endpoint_peers_entry_rmem_address_neg_0x6559b47b3208e18d_cls
from ._registers import openenoc_endpoint_peers_entry_local_address_neg_0x49e3835772dee4dd_cls
from ._registers import openenoc_endpoint_peers_entry_remote_address_neg_0x5a9e65567f65065a_cls
from ._registers import openenoc_endpoint_peers_entry_size_neg_0x53f79c915dbb3e3f_cls
from ._registers import openenoc_endpoint_peers_entry_dma_0x2d21abf34620e72b_cls
from ._registers import openenoc_endpoint_info_neg_0x549c607bde34271a_cls
from ._registers import openenoc_endpoint_config_mac_address_neg_0x2d0ab396256547a3_cls
from ._registers import openenoc_endpoint_axis_if_source_data_0x42a57f4a6fdb32ef_cls
from ._registers import openenoc_endpoint_axis_if_source_control_0x6eb3ad904efccb93_cls
from ._registers import openenoc_endpoint_axis_if_source_status_neg_0x207fb7f13290ac1e_cls
from ._registers import openenoc_endpoint_axis_if_sink_data_0x6c882caebb700338_cls
from ._registers import openenoc_endpoint_axis_if_sink_control_0x557ae3e17e19b169_cls
from ._registers import openenoc_endpoint_axis_if_sink_status_0x6d742d7bb53bda94_cls
from ._registers import openenoc_endpoint_peers_entry_mac_address_0x2851813cb1c6f569_cls
from ._registers import openenoc_endpoint_peers_entry_rmem_address_neg_0x24e7ecc30ad6cee4_cls
from ._registers import openenoc_endpoint_peers_entry_local_address_neg_0x7272d9a616d480eb_cls
from ._registers import openenoc_endpoint_peers_entry_remote_address_0x2b4d9710df834c38_cls
from ._registers import openenoc_endpoint_peers_entry_size_neg_0x18ef259524231fee_cls
from ._registers import openenoc_endpoint_peers_entry_dma_neg_0x5b00f79da6c3b3d9_cls
from ._registers import openenoc_switch_info_0x38ed551aa0ce902c_cls
from ._registers import openenoc_switch_forwarding_control_neg_0x3974f1c35c15c386_cls
from ._registers import openenoc_switch_default_forwarding_neg_0x1144bb53a7ca2d14_cls
from ._registers import openenoc_switch_forwarding_table_entry_mac_address_neg_0x5bc1c3e20b454898_cls
from ._registers import openenoc_switch_forwarding_table_entry_iface_neg_0x74bbf9cefadb0da8_cls
from ._registers import openenoc_switch_forwarding_table_entry_config_0x3f0c946cc269b99e_cls
from ._registers import openenoc_switch_info_0x39a74b18ec6dcb6d_cls
from ._registers import openenoc_switch_forwarding_control_neg_0x20dc196d6725e041_cls
from ._registers import openenoc_switch_default_forwarding_0x4a14f23ca02700d9_cls
from ._registers import openenoc_switch_forwarding_table_entry_mac_address_0xa70e0bd34165450_cls
from ._registers import openenoc_switch_forwarding_table_entry_iface_neg_0x28f8afe3a0f75602_cls
from ._registers import openenoc_switch_forwarding_table_entry_config_neg_0x24732ef27b75ffa8_cls
from ._memories import openenoc_endpoint_rmem_0x497dea42f489d12d_cls
from ._memories import openenoc_endpoint_rmem_0x877eeba2c94b35f_cls


# addrmap, regfile, memor and register definitions
    
    
class openenoc_switch_forwarding_table_entry_neg_0x7c26febdf62b9e0a_cls(RegFile):
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
        
            
        self.__mac_address:openenoc_switch_forwarding_table_entry_mac_address_0xa70e0bd34165450_cls = openenoc_switch_forwarding_table_entry_mac_address_0xa70e0bd34165450_cls(
                                                                     address=self.address+0,
                                                                     logger_handle=logger_handle+'.mac_address',
                                                                     inst_name='mac_address', parent=self)
        
            
        self.__iface:openenoc_switch_forwarding_table_entry_iface_neg_0x28f8afe3a0f75602_cls = openenoc_switch_forwarding_table_entry_iface_neg_0x28f8afe3a0f75602_cls(
                                                                     address=self.address+8,
                                                                     logger_handle=logger_handle+'.iface',
                                                                     inst_name='iface', parent=self)
        
            
        self.__config:openenoc_switch_forwarding_table_entry_config_neg_0x24732ef27b75ffa8_cls = openenoc_switch_forwarding_table_entry_config_neg_0x24732ef27b75ffa8_cls(
                                                                     address=self.address+12,
                                                                     logger_handle=logger_handle+'.config',
                                                                     inst_name='config', parent=self)
        

    @property
    def size(self) -> int:
        return 16

    # properties for Register and RegisterFiles
    @property
    def mac_address(self) -> 'openenoc_switch_forwarding_table_entry_mac_address_0xa70e0bd34165450_cls':
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
    def iface(self) -> 'openenoc_switch_forwarding_table_entry_iface_neg_0x28f8afe3a0f75602_cls':
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
    def config(self) -> 'openenoc_switch_forwarding_table_entry_config_neg_0x24732ef27b75ffa8_cls':
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
    def get_child_by_system_rdl_name(self, name: Literal["mac_address"]) -> 'openenoc_switch_forwarding_table_entry_mac_address_0xa70e0bd34165450_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["iface"]) -> 'openenoc_switch_forwarding_table_entry_iface_neg_0x28f8afe3a0f75602_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["config"]) -> 'openenoc_switch_forwarding_table_entry_config_neg_0x24732ef27b75ffa8_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_switch_forwarding_table_entry_mac_address_0xa70e0bd34165450_cls', 'openenoc_switch_forwarding_table_entry_iface_neg_0x28f8afe3a0f75602_cls', 'openenoc_switch_forwarding_table_entry_config_neg_0x24732ef27b75ffa8_cls', ]: ...

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
        
        
class openenoc_switch_forwarding_table_entry_neg_0x7c26febdf62b9e0a_cls_array(RegFileArray):
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
        return openenoc_switch_forwarding_table_entry_neg_0x7c26febdf62b9e0a_cls
    

    
    
class openenoc_switch_forwarding_table_0x755672201760e4b4_cls(RegFile):
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
        
        self.__entry:openenoc_switch_forwarding_table_entry_neg_0x7c26febdf62b9e0a_cls_array = openenoc_switch_forwarding_table_entry_neg_0x7c26febdf62b9e0a_cls_array(address=self.address+0,
                                                                                      stride=16,
                                                                                      dimensions=tuple([32]),
                                                                                      logger_handle=logger_handle+'.entry',
                                                                                      inst_name='entry', parent=self)
        

    @property
    def size(self) -> int:
        return 512

    # properties for Register and RegisterFiles
    @property
    def entry(self) -> 'openenoc_switch_forwarding_table_entry_neg_0x7c26febdf62b9e0a_cls_array':
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

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_switch_forwarding_table_entry_neg_0x7c26febdf62b9e0a_cls_array':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.switch2.forwarding_table"
    @property
    def rdl_desc(self) -> str:
        return "Forwarding table used to map MAC addresses to output interface selections for frame forwarding."
    
    

    
    def __iter__(self) -> Iterator[Union[Node, NodeArray]]:
        
        
        yield self.entry
        
        
    

    
    
class openenoc_switch_neg_0x62f9a5ec3f4ef54a_cls(AddressMap):
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

        
            
        self.__info:openenoc_switch_info_0x39a74b18ec6dcb6d_cls = openenoc_switch_info_0x39a74b18ec6dcb6d_cls(
                                                                     address=self.address+0,
                                                                     logger_handle=logger_handle+'.info',
                                                                     inst_name='info', parent=self)
        
            
        self.__forwarding_control:openenoc_switch_forwarding_control_neg_0x20dc196d6725e041_cls = openenoc_switch_forwarding_control_neg_0x20dc196d6725e041_cls(
                                                                     address=self.address+4,
                                                                     logger_handle=logger_handle+'.forwarding_control',
                                                                     inst_name='forwarding_control', parent=self)
        
            
        self.__default_forwarding:openenoc_switch_default_forwarding_0x4a14f23ca02700d9_cls = openenoc_switch_default_forwarding_0x4a14f23ca02700d9_cls(
                                                                     address=self.address+8,
                                                                     logger_handle=logger_handle+'.default_forwarding',
                                                                     inst_name='default_forwarding', parent=self)
        self.__forwarding_table:openenoc_switch_forwarding_table_0x755672201760e4b4_cls = openenoc_switch_forwarding_table_0x755672201760e4b4_cls(
                                                                                address=self.address+512,
                                                                                logger_handle=logger_handle+'.forwarding_table',
                                                                                inst_name='forwarding_table',
                                                                                parent=self)
        

    @property
    def size(self) -> int:
        return 1024
    @property
    def info(self) -> 'openenoc_switch_info_0x39a74b18ec6dcb6d_cls':
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
    def forwarding_control(self) -> 'openenoc_switch_forwarding_control_neg_0x20dc196d6725e041_cls':
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
    def default_forwarding(self) -> 'openenoc_switch_default_forwarding_0x4a14f23ca02700d9_cls':
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
    def forwarding_table(self) -> 'openenoc_switch_forwarding_table_0x755672201760e4b4_cls':
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
    def get_child_by_system_rdl_name(self, name: Literal["info"]) -> 'openenoc_switch_info_0x39a74b18ec6dcb6d_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["forwarding_control"]) -> 'openenoc_switch_forwarding_control_neg_0x20dc196d6725e041_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["default_forwarding"]) -> 'openenoc_switch_default_forwarding_0x4a14f23ca02700d9_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["forwarding_table"]) -> 'openenoc_switch_forwarding_table_0x755672201760e4b4_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_switch_info_0x39a74b18ec6dcb6d_cls', 'openenoc_switch_forwarding_control_neg_0x20dc196d6725e041_cls', 'openenoc_switch_default_forwarding_0x4a14f23ca02700d9_cls', 'openenoc_switch_forwarding_table_0x755672201760e4b4_cls', ]: ...

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
        
        
    

    
    
class openenoc_switch_forwarding_table_entry_neg_0x3e180bd1a5af22e5_cls(RegFile):
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
        
            
        self.__mac_address:openenoc_switch_forwarding_table_entry_mac_address_neg_0x5bc1c3e20b454898_cls = openenoc_switch_forwarding_table_entry_mac_address_neg_0x5bc1c3e20b454898_cls(
                                                                     address=self.address+0,
                                                                     logger_handle=logger_handle+'.mac_address',
                                                                     inst_name='mac_address', parent=self)
        
            
        self.__iface:openenoc_switch_forwarding_table_entry_iface_neg_0x74bbf9cefadb0da8_cls = openenoc_switch_forwarding_table_entry_iface_neg_0x74bbf9cefadb0da8_cls(
                                                                     address=self.address+8,
                                                                     logger_handle=logger_handle+'.iface',
                                                                     inst_name='iface', parent=self)
        
            
        self.__config:openenoc_switch_forwarding_table_entry_config_0x3f0c946cc269b99e_cls = openenoc_switch_forwarding_table_entry_config_0x3f0c946cc269b99e_cls(
                                                                     address=self.address+12,
                                                                     logger_handle=logger_handle+'.config',
                                                                     inst_name='config', parent=self)
        

    @property
    def size(self) -> int:
        return 16

    # properties for Register and RegisterFiles
    @property
    def mac_address(self) -> 'openenoc_switch_forwarding_table_entry_mac_address_neg_0x5bc1c3e20b454898_cls':
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
    def iface(self) -> 'openenoc_switch_forwarding_table_entry_iface_neg_0x74bbf9cefadb0da8_cls':
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
    def config(self) -> 'openenoc_switch_forwarding_table_entry_config_0x3f0c946cc269b99e_cls':
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
    def get_child_by_system_rdl_name(self, name: Literal["mac_address"]) -> 'openenoc_switch_forwarding_table_entry_mac_address_neg_0x5bc1c3e20b454898_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["iface"]) -> 'openenoc_switch_forwarding_table_entry_iface_neg_0x74bbf9cefadb0da8_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["config"]) -> 'openenoc_switch_forwarding_table_entry_config_0x3f0c946cc269b99e_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_switch_forwarding_table_entry_mac_address_neg_0x5bc1c3e20b454898_cls', 'openenoc_switch_forwarding_table_entry_iface_neg_0x74bbf9cefadb0da8_cls', 'openenoc_switch_forwarding_table_entry_config_0x3f0c946cc269b99e_cls', ]: ...

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
        
        
class openenoc_switch_forwarding_table_entry_neg_0x3e180bd1a5af22e5_cls_array(RegFileArray):
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
        return openenoc_switch_forwarding_table_entry_neg_0x3e180bd1a5af22e5_cls
    

    
    
class openenoc_switch_forwarding_table_0x39f68b51c99eed43_cls(RegFile):
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
        
        self.__entry:openenoc_switch_forwarding_table_entry_neg_0x3e180bd1a5af22e5_cls_array = openenoc_switch_forwarding_table_entry_neg_0x3e180bd1a5af22e5_cls_array(address=self.address+0,
                                                                                      stride=16,
                                                                                      dimensions=tuple([8]),
                                                                                      logger_handle=logger_handle+'.entry',
                                                                                      inst_name='entry', parent=self)
        

    @property
    def size(self) -> int:
        return 128

    # properties for Register and RegisterFiles
    @property
    def entry(self) -> 'openenoc_switch_forwarding_table_entry_neg_0x3e180bd1a5af22e5_cls_array':
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

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_switch_forwarding_table_entry_neg_0x3e180bd1a5af22e5_cls_array':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.switch1.forwarding_table"
    @property
    def rdl_desc(self) -> str:
        return "Forwarding table used to map MAC addresses to output interface selections for frame forwarding."
    
    

    
    def __iter__(self) -> Iterator[Union[Node, NodeArray]]:
        
        
        yield self.entry
        
        
    

    
    
class openenoc_switch_neg_0xf782f49dd81dd1d_cls(AddressMap):
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

        
            
        self.__info:openenoc_switch_info_0x38ed551aa0ce902c_cls = openenoc_switch_info_0x38ed551aa0ce902c_cls(
                                                                     address=self.address+0,
                                                                     logger_handle=logger_handle+'.info',
                                                                     inst_name='info', parent=self)
        
            
        self.__forwarding_control:openenoc_switch_forwarding_control_neg_0x3974f1c35c15c386_cls = openenoc_switch_forwarding_control_neg_0x3974f1c35c15c386_cls(
                                                                     address=self.address+4,
                                                                     logger_handle=logger_handle+'.forwarding_control',
                                                                     inst_name='forwarding_control', parent=self)
        
            
        self.__default_forwarding:openenoc_switch_default_forwarding_neg_0x1144bb53a7ca2d14_cls = openenoc_switch_default_forwarding_neg_0x1144bb53a7ca2d14_cls(
                                                                     address=self.address+8,
                                                                     logger_handle=logger_handle+'.default_forwarding',
                                                                     inst_name='default_forwarding', parent=self)
        self.__forwarding_table:openenoc_switch_forwarding_table_0x39f68b51c99eed43_cls = openenoc_switch_forwarding_table_0x39f68b51c99eed43_cls(
                                                                                address=self.address+128,
                                                                                logger_handle=logger_handle+'.forwarding_table',
                                                                                inst_name='forwarding_table',
                                                                                parent=self)
        

    @property
    def size(self) -> int:
        return 256
    @property
    def info(self) -> 'openenoc_switch_info_0x38ed551aa0ce902c_cls':
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
    def forwarding_control(self) -> 'openenoc_switch_forwarding_control_neg_0x3974f1c35c15c386_cls':
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
    def default_forwarding(self) -> 'openenoc_switch_default_forwarding_neg_0x1144bb53a7ca2d14_cls':
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
    def forwarding_table(self) -> 'openenoc_switch_forwarding_table_0x39f68b51c99eed43_cls':
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
    def get_child_by_system_rdl_name(self, name: Literal["info"]) -> 'openenoc_switch_info_0x38ed551aa0ce902c_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["forwarding_control"]) -> 'openenoc_switch_forwarding_control_neg_0x3974f1c35c15c386_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["default_forwarding"]) -> 'openenoc_switch_default_forwarding_neg_0x1144bb53a7ca2d14_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["forwarding_table"]) -> 'openenoc_switch_forwarding_table_0x39f68b51c99eed43_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_switch_info_0x38ed551aa0ce902c_cls', 'openenoc_switch_forwarding_control_neg_0x3974f1c35c15c386_cls', 'openenoc_switch_default_forwarding_neg_0x1144bb53a7ca2d14_cls', 'openenoc_switch_forwarding_table_0x39f68b51c99eed43_cls', ]: ...

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
        
        
    

    
    
class openenoc_endpoint_peers_entry_0x1fac7bd476007739_cls(RegFile):
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

    __slots__ : list[str] = ['__mac_address', '__rmem_address', '__local_address', '__remote_address', '__size', '__dma']

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
        
            
        self.__mac_address:openenoc_endpoint_peers_entry_mac_address_0x2851813cb1c6f569_cls = openenoc_endpoint_peers_entry_mac_address_0x2851813cb1c6f569_cls(
                                                                     address=self.address+0,
                                                                     logger_handle=logger_handle+'.mac_address',
                                                                     inst_name='mac_address', parent=self)
        
            
        self.__rmem_address:openenoc_endpoint_peers_entry_rmem_address_neg_0x24e7ecc30ad6cee4_cls = openenoc_endpoint_peers_entry_rmem_address_neg_0x24e7ecc30ad6cee4_cls(
                                                                     address=self.address+8,
                                                                     logger_handle=logger_handle+'.rmem_address',
                                                                     inst_name='rmem_address', parent=self)
        
            
        self.__local_address:openenoc_endpoint_peers_entry_local_address_neg_0x7272d9a616d480eb_cls = openenoc_endpoint_peers_entry_local_address_neg_0x7272d9a616d480eb_cls(
                                                                     address=self.address+12,
                                                                     logger_handle=logger_handle+'.local_address',
                                                                     inst_name='local_address', parent=self)
        
            
        self.__remote_address:openenoc_endpoint_peers_entry_remote_address_0x2b4d9710df834c38_cls = openenoc_endpoint_peers_entry_remote_address_0x2b4d9710df834c38_cls(
                                                                     address=self.address+16,
                                                                     logger_handle=logger_handle+'.remote_address',
                                                                     inst_name='remote_address', parent=self)
        
            
        self.__size:openenoc_endpoint_peers_entry_size_neg_0x18ef259524231fee_cls = openenoc_endpoint_peers_entry_size_neg_0x18ef259524231fee_cls(
                                                                     address=self.address+20,
                                                                     logger_handle=logger_handle+'.size',
                                                                     inst_name='size', parent=self)
        
            
        self.__dma:openenoc_endpoint_peers_entry_dma_neg_0x5b00f79da6c3b3d9_cls = openenoc_endpoint_peers_entry_dma_neg_0x5b00f79da6c3b3d9_cls(
                                                                     address=self.address+24,
                                                                     logger_handle=logger_handle+'.dma',
                                                                     inst_name='dma', parent=self)
        

    @property
    def size(self) -> int:
        return 28

    # properties for Register and RegisterFiles
    @property
    def mac_address(self) -> 'openenoc_endpoint_peers_entry_mac_address_0x2851813cb1c6f569_cls':
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
    def rmem_address(self) -> 'openenoc_endpoint_peers_entry_rmem_address_neg_0x24e7ecc30ad6cee4_cls':
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
    def local_address(self) -> 'openenoc_endpoint_peers_entry_local_address_neg_0x7272d9a616d480eb_cls':
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
    def remote_address(self) -> 'openenoc_endpoint_peers_entry_remote_address_0x2b4d9710df834c38_cls':
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
    def register_size(self) -> 'openenoc_endpoint_peers_entry_size_neg_0x18ef259524231fee_cls':
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
    def dma(self) -> 'openenoc_endpoint_peers_entry_dma_neg_0x5b00f79da6c3b3d9_cls':
        """
        Property to access dma 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].dma                   |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>DMA configuration and control for the remote peer.</p>          |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__dma
    

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'mac_address':'mac_address','rmem_address':'rmem_address','local_address':'local_address','remote_address':'remote_address','size':'register_size','dma':'dma',
            }

    
    
    
    
    
    
    # nodes:6
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["mac_address"]) -> 'openenoc_endpoint_peers_entry_mac_address_0x2851813cb1c6f569_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["rmem_address"]) -> 'openenoc_endpoint_peers_entry_rmem_address_neg_0x24e7ecc30ad6cee4_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["local_address"]) -> 'openenoc_endpoint_peers_entry_local_address_neg_0x7272d9a616d480eb_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["remote_address"]) -> 'openenoc_endpoint_peers_entry_remote_address_0x2b4d9710df834c38_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["size"]) -> 'openenoc_endpoint_peers_entry_size_neg_0x18ef259524231fee_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["dma"]) -> 'openenoc_endpoint_peers_entry_dma_neg_0x5b00f79da6c3b3d9_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_peers_entry_mac_address_0x2851813cb1c6f569_cls', 'openenoc_endpoint_peers_entry_rmem_address_neg_0x24e7ecc30ad6cee4_cls', 'openenoc_endpoint_peers_entry_local_address_neg_0x7272d9a616d480eb_cls', 'openenoc_endpoint_peers_entry_remote_address_0x2b4d9710df834c38_cls', 'openenoc_endpoint_peers_entry_size_neg_0x18ef259524231fee_cls', 'openenoc_endpoint_peers_entry_dma_neg_0x5b00f79da6c3b3d9_cls', ]: ...

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
        yield self.dma
        
        
class openenoc_endpoint_peers_entry_0x1fac7bd476007739_cls_array(RegFileArray):
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
        return openenoc_endpoint_peers_entry_0x1fac7bd476007739_cls
    

    
    
class openenoc_endpoint_peers_neg_0x2e6da1c8591658c3_cls(RegFile):
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
        
        self.__entry:openenoc_endpoint_peers_entry_0x1fac7bd476007739_cls_array = openenoc_endpoint_peers_entry_0x1fac7bd476007739_cls_array(address=self.address+0,
                                                                                      stride=28,
                                                                                      dimensions=tuple([2]),
                                                                                      logger_handle=logger_handle+'.entry',
                                                                                      inst_name='entry', parent=self)
        

    @property
    def size(self) -> int:
        return 56

    # properties for Register and RegisterFiles
    @property
    def entry(self) -> 'openenoc_endpoint_peers_entry_0x1fac7bd476007739_cls_array':
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

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_peers_entry_0x1fac7bd476007739_cls_array':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint2.peers"
    @property
    def rdl_desc(self) -> str:
        return "Register file for remote peer configuration and memory region information."
    
    

    
    def __iter__(self) -> Iterator[Union[Node, NodeArray]]:
        
        
        yield self.entry
        
        
    

    
    
class openenoc_endpoint_axis_if_sink_0x13bcb1fd17dc376f_cls(RegFile):
    """
    Class to represent a register file in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint2.axis_if.sink                                         |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Register file for the AXI4-Stream sink interface.</p>           |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__data', '__control', '__status']

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
        
            
        self.__data:openenoc_endpoint_axis_if_sink_data_0x6c882caebb700338_cls = openenoc_endpoint_axis_if_sink_data_0x6c882caebb700338_cls(
                                                                     address=self.address+0,
                                                                     logger_handle=logger_handle+'.data',
                                                                     inst_name='data', parent=self)
        
            
        self.__control:openenoc_endpoint_axis_if_sink_control_0x557ae3e17e19b169_cls = openenoc_endpoint_axis_if_sink_control_0x557ae3e17e19b169_cls(
                                                                     address=self.address+4,
                                                                     logger_handle=logger_handle+'.control',
                                                                     inst_name='control', parent=self)
        
            
        self.__status:openenoc_endpoint_axis_if_sink_status_0x6d742d7bb53bda94_cls = openenoc_endpoint_axis_if_sink_status_0x6d742d7bb53bda94_cls(
                                                                     address=self.address+8,
                                                                     logger_handle=logger_handle+'.status',
                                                                     inst_name='status', parent=self)
        

    @property
    def size(self) -> int:
        return 12

    # properties for Register and RegisterFiles
    @property
    def data(self) -> 'openenoc_endpoint_axis_if_sink_data_0x6c882caebb700338_cls':
        """
        Property to access data 

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
        return self.__data
    
    @property
    def control(self) -> 'openenoc_endpoint_axis_if_sink_control_0x557ae3e17e19b169_cls':
        """
        Property to access control 

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
        return self.__control
    
    @property
    def status(self) -> 'openenoc_endpoint_axis_if_sink_status_0x6d742d7bb53bda94_cls':
        """
        Property to access status 

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
        return self.__status
    

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'data':'data','control':'control','status':'status',
            }

    
    
    
    
    
    
    # nodes:3
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["data"]) -> 'openenoc_endpoint_axis_if_sink_data_0x6c882caebb700338_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["control"]) -> 'openenoc_endpoint_axis_if_sink_control_0x557ae3e17e19b169_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["status"]) -> 'openenoc_endpoint_axis_if_sink_status_0x6d742d7bb53bda94_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_axis_if_sink_data_0x6c882caebb700338_cls', 'openenoc_endpoint_axis_if_sink_control_0x557ae3e17e19b169_cls', 'openenoc_endpoint_axis_if_sink_status_0x6d742d7bb53bda94_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint2.axis_if.sink"
    @property
    def rdl_desc(self) -> str:
        return "Register file for the AXI4-Stream sink interface."
    
    

    
    def __iter__(self) -> Iterator[Union[Node, NodeArray]]:
        
        
        yield self.data
        yield self.control
        yield self.status
        
        
    

    
    
class openenoc_endpoint_axis_if_source_neg_0x32a939981e858a5b_cls(RegFile):
    """
    Class to represent a register file in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint2.axis_if.source                                       |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Register file for the AXI4-Stream source interface.</p>         |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__data', '__control', '__status']

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
        
            
        self.__data:openenoc_endpoint_axis_if_source_data_0x42a57f4a6fdb32ef_cls = openenoc_endpoint_axis_if_source_data_0x42a57f4a6fdb32ef_cls(
                                                                     address=self.address+0,
                                                                     logger_handle=logger_handle+'.data',
                                                                     inst_name='data', parent=self)
        
            
        self.__control:openenoc_endpoint_axis_if_source_control_0x6eb3ad904efccb93_cls = openenoc_endpoint_axis_if_source_control_0x6eb3ad904efccb93_cls(
                                                                     address=self.address+4,
                                                                     logger_handle=logger_handle+'.control',
                                                                     inst_name='control', parent=self)
        
            
        self.__status:openenoc_endpoint_axis_if_source_status_neg_0x207fb7f13290ac1e_cls = openenoc_endpoint_axis_if_source_status_neg_0x207fb7f13290ac1e_cls(
                                                                     address=self.address+8,
                                                                     logger_handle=logger_handle+'.status',
                                                                     inst_name='status', parent=self)
        

    @property
    def size(self) -> int:
        return 12

    # properties for Register and RegisterFiles
    @property
    def data(self) -> 'openenoc_endpoint_axis_if_source_data_0x42a57f4a6fdb32ef_cls':
        """
        Property to access data 

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
        return self.__data
    
    @property
    def control(self) -> 'openenoc_endpoint_axis_if_source_control_0x6eb3ad904efccb93_cls':
        """
        Property to access control 

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
        return self.__control
    
    @property
    def status(self) -> 'openenoc_endpoint_axis_if_source_status_neg_0x207fb7f13290ac1e_cls':
        """
        Property to access status 

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
        return self.__status
    

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'data':'data','control':'control','status':'status',
            }

    
    
    
    
    
    
    # nodes:3
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["data"]) -> 'openenoc_endpoint_axis_if_source_data_0x42a57f4a6fdb32ef_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["control"]) -> 'openenoc_endpoint_axis_if_source_control_0x6eb3ad904efccb93_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["status"]) -> 'openenoc_endpoint_axis_if_source_status_neg_0x207fb7f13290ac1e_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_axis_if_source_data_0x42a57f4a6fdb32ef_cls', 'openenoc_endpoint_axis_if_source_control_0x6eb3ad904efccb93_cls', 'openenoc_endpoint_axis_if_source_status_neg_0x207fb7f13290ac1e_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint2.axis_if.source"
    @property
    def rdl_desc(self) -> str:
        return "Register file for the AXI4-Stream source interface."
    
    

    
    def __iter__(self) -> Iterator[Union[Node, NodeArray]]:
        
        
        yield self.data
        yield self.control
        yield self.status
        
        
    

    
    
class openenoc_endpoint_axis_if_neg_0x27d31cdbbdb0d387_cls(RegFile):
    """
    Class to represent a register file in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint2.axis_if                                              |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Register file for the AXI4-Stream source and sink               |
    |              |      interfaces.</p>                                                    |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__source', '__sink']

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
        self.__source:openenoc_endpoint_axis_if_source_neg_0x32a939981e858a5b_cls = openenoc_endpoint_axis_if_source_neg_0x32a939981e858a5b_cls(
                                                                                address=self.address+0,
                                                                                logger_handle=logger_handle+'.source',
                                                                                inst_name='source',
                                                                                parent=self)
        self.__sink:openenoc_endpoint_axis_if_sink_0x13bcb1fd17dc376f_cls = openenoc_endpoint_axis_if_sink_0x13bcb1fd17dc376f_cls(
                                                                                address=self.address+16,
                                                                                logger_handle=logger_handle+'.sink',
                                                                                inst_name='sink',
                                                                                parent=self)
        

    @property
    def size(self) -> int:
        return 28

    # properties for Register and RegisterFiles
    @property
    def source(self) -> 'openenoc_endpoint_axis_if_source_neg_0x32a939981e858a5b_cls':
        """
        Property to access source 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint2.axis_if.source                                       |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Register file for the AXI4-Stream source interface.</p>         |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__source
    
    @property
    def sink(self) -> 'openenoc_endpoint_axis_if_sink_0x13bcb1fd17dc376f_cls':
        """
        Property to access sink 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint2.axis_if.sink                                         |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Register file for the AXI4-Stream sink interface.</p>           |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__sink
    

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'source':'source','sink':'sink',
            }

    
    
    
    
    
    
    # nodes:2
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["source"]) -> 'openenoc_endpoint_axis_if_source_neg_0x32a939981e858a5b_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["sink"]) -> 'openenoc_endpoint_axis_if_sink_0x13bcb1fd17dc376f_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_axis_if_source_neg_0x32a939981e858a5b_cls', 'openenoc_endpoint_axis_if_sink_0x13bcb1fd17dc376f_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint2.axis_if"
    @property
    def rdl_desc(self) -> str:
        return "Register file for the AXI4-Stream source and sink interfaces."
    
    

    
    def __iter__(self) -> Iterator[Union[Node, NodeArray]]:
        
        
        yield self.source
        yield self.sink
        
        
    

    
    
class openenoc_endpoint_config_neg_0x22cf35b6d9596b5f_cls(RegFile):
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
        
            
        self.__mac_address:openenoc_endpoint_config_mac_address_neg_0x2d0ab396256547a3_cls = openenoc_endpoint_config_mac_address_neg_0x2d0ab396256547a3_cls(
                                                                     address=self.address+0,
                                                                     logger_handle=logger_handle+'.mac_address',
                                                                     inst_name='mac_address', parent=self)
        

    @property
    def size(self) -> int:
        return 8

    # properties for Register and RegisterFiles
    @property
    def mac_address(self) -> 'openenoc_endpoint_config_mac_address_neg_0x2d0ab396256547a3_cls':
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

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_config_mac_address_neg_0x2d0ab396256547a3_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint2.config"
    @property
    def rdl_desc(self) -> str:
        return "Configuration register file for this openENOC Endpoint Interface instance."
    
    

    
    def __iter__(self) -> Iterator[Union[Node, NodeArray]]:
        
        
        yield self.mac_address
        
        
    

    
    
class openenoc_endpoint_0x14b5eec0360ba6db_cls(AddressMap):
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

    __slots__ : list[str] = ['__info', '__config', '__axis_if', '__peers', '__rmem']

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

        
            
        self.__info:openenoc_endpoint_info_neg_0x549c607bde34271a_cls = openenoc_endpoint_info_neg_0x549c607bde34271a_cls(
                                                                     address=self.address+0,
                                                                     logger_handle=logger_handle+'.info',
                                                                     inst_name='info', parent=self)
        self.__config:openenoc_endpoint_config_neg_0x22cf35b6d9596b5f_cls = openenoc_endpoint_config_neg_0x22cf35b6d9596b5f_cls(
                                                                                address=self.address+8,
                                                                                logger_handle=logger_handle+'.config',
                                                                                inst_name='config',
                                                                                parent=self)
        self.__axis_if:openenoc_endpoint_axis_if_neg_0x27d31cdbbdb0d387_cls = openenoc_endpoint_axis_if_neg_0x27d31cdbbdb0d387_cls(
                                                                                address=self.address+32,
                                                                                logger_handle=logger_handle+'.axis_if',
                                                                                inst_name='axis_if',
                                                                                parent=self)
        self.__peers:openenoc_endpoint_peers_neg_0x2e6da1c8591658c3_cls = openenoc_endpoint_peers_neg_0x2e6da1c8591658c3_cls(
                                                                                address=self.address+64,
                                                                                logger_handle=logger_handle+'.peers',
                                                                                inst_name='peers',
                                                                                parent=self)
        
        self.__rmem:openenoc_endpoint_rmem_0x877eeba2c94b35f_cls = openenoc_endpoint_rmem_0x877eeba2c94b35f_cls(
                                                                     address=self.address+512,
                                                                     logger_handle=logger_handle+'.rmem',
                                                                                       inst_name='rmem', parent=self)
        

    @property
    def size(self) -> int:
        return 1024
    @property
    def info(self) -> 'openenoc_endpoint_info_neg_0x549c607bde34271a_cls':
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
    def config(self) -> 'openenoc_endpoint_config_neg_0x22cf35b6d9596b5f_cls':
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
    def axis_if(self) -> 'openenoc_endpoint_axis_if_neg_0x27d31cdbbdb0d387_cls':
        """
        Property to access axis_if 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint2.axis_if                                              |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Register file for the AXI4-Stream source and sink               |
        |              |      interfaces.</p>                                                    |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__axis_if
        
    @property
    def peers(self) -> 'openenoc_endpoint_peers_neg_0x2e6da1c8591658c3_cls':
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
    def rmem(self) -> 'openenoc_endpoint_rmem_0x877eeba2c94b35f_cls':
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
        return {'info':'info','config':'config','axis_if':'axis_if','peers':'peers','rmem':'rmem',
            }

    
    
    
    
    
    
    # nodes:5
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["info"]) -> 'openenoc_endpoint_info_neg_0x549c607bde34271a_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["config"]) -> 'openenoc_endpoint_config_neg_0x22cf35b6d9596b5f_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["axis_if"]) -> 'openenoc_endpoint_axis_if_neg_0x27d31cdbbdb0d387_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["peers"]) -> 'openenoc_endpoint_peers_neg_0x2e6da1c8591658c3_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["rmem"]) -> 'openenoc_endpoint_rmem_0x877eeba2c94b35f_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_info_neg_0x549c607bde34271a_cls', 'openenoc_endpoint_config_neg_0x22cf35b6d9596b5f_cls', 'openenoc_endpoint_axis_if_neg_0x27d31cdbbdb0d387_cls', 'openenoc_endpoint_peers_neg_0x2e6da1c8591658c3_cls', 'openenoc_endpoint_rmem_0x877eeba2c94b35f_cls', ]: ...

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
        yield self.axis_if
        yield self.peers
        yield self.rmem
        
        
    

    
    
class openenoc_endpoint_peers_entry_neg_0x6adf294af53c4a69_cls(RegFile):
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

    __slots__ : list[str] = ['__mac_address', '__rmem_address', '__local_address', '__remote_address', '__size', '__dma']

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
        
            
        self.__mac_address:openenoc_endpoint_peers_entry_mac_address_0x78cedd86ea7d8cba_cls = openenoc_endpoint_peers_entry_mac_address_0x78cedd86ea7d8cba_cls(
                                                                     address=self.address+0,
                                                                     logger_handle=logger_handle+'.mac_address',
                                                                     inst_name='mac_address', parent=self)
        
            
        self.__rmem_address:openenoc_endpoint_peers_entry_rmem_address_neg_0x6559b47b3208e18d_cls = openenoc_endpoint_peers_entry_rmem_address_neg_0x6559b47b3208e18d_cls(
                                                                     address=self.address+8,
                                                                     logger_handle=logger_handle+'.rmem_address',
                                                                     inst_name='rmem_address', parent=self)
        
            
        self.__local_address:openenoc_endpoint_peers_entry_local_address_neg_0x49e3835772dee4dd_cls = openenoc_endpoint_peers_entry_local_address_neg_0x49e3835772dee4dd_cls(
                                                                     address=self.address+12,
                                                                     logger_handle=logger_handle+'.local_address',
                                                                     inst_name='local_address', parent=self)
        
            
        self.__remote_address:openenoc_endpoint_peers_entry_remote_address_neg_0x5a9e65567f65065a_cls = openenoc_endpoint_peers_entry_remote_address_neg_0x5a9e65567f65065a_cls(
                                                                     address=self.address+16,
                                                                     logger_handle=logger_handle+'.remote_address',
                                                                     inst_name='remote_address', parent=self)
        
            
        self.__size:openenoc_endpoint_peers_entry_size_neg_0x53f79c915dbb3e3f_cls = openenoc_endpoint_peers_entry_size_neg_0x53f79c915dbb3e3f_cls(
                                                                     address=self.address+20,
                                                                     logger_handle=logger_handle+'.size',
                                                                     inst_name='size', parent=self)
        
            
        self.__dma:openenoc_endpoint_peers_entry_dma_0x2d21abf34620e72b_cls = openenoc_endpoint_peers_entry_dma_0x2d21abf34620e72b_cls(
                                                                     address=self.address+24,
                                                                     logger_handle=logger_handle+'.dma',
                                                                     inst_name='dma', parent=self)
        

    @property
    def size(self) -> int:
        return 28

    # properties for Register and RegisterFiles
    @property
    def mac_address(self) -> 'openenoc_endpoint_peers_entry_mac_address_0x78cedd86ea7d8cba_cls':
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
    def rmem_address(self) -> 'openenoc_endpoint_peers_entry_rmem_address_neg_0x6559b47b3208e18d_cls':
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
    def local_address(self) -> 'openenoc_endpoint_peers_entry_local_address_neg_0x49e3835772dee4dd_cls':
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
    def remote_address(self) -> 'openenoc_endpoint_peers_entry_remote_address_neg_0x5a9e65567f65065a_cls':
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
    def register_size(self) -> 'openenoc_endpoint_peers_entry_size_neg_0x53f79c915dbb3e3f_cls':
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
    def dma(self) -> 'openenoc_endpoint_peers_entry_dma_0x2d21abf34620e72b_cls':
        """
        Property to access dma 

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
        return self.__dma
    

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'mac_address':'mac_address','rmem_address':'rmem_address','local_address':'local_address','remote_address':'remote_address','size':'register_size','dma':'dma',
            }

    
    
    
    
    
    
    # nodes:6
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["mac_address"]) -> 'openenoc_endpoint_peers_entry_mac_address_0x78cedd86ea7d8cba_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["rmem_address"]) -> 'openenoc_endpoint_peers_entry_rmem_address_neg_0x6559b47b3208e18d_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["local_address"]) -> 'openenoc_endpoint_peers_entry_local_address_neg_0x49e3835772dee4dd_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["remote_address"]) -> 'openenoc_endpoint_peers_entry_remote_address_neg_0x5a9e65567f65065a_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["size"]) -> 'openenoc_endpoint_peers_entry_size_neg_0x53f79c915dbb3e3f_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["dma"]) -> 'openenoc_endpoint_peers_entry_dma_0x2d21abf34620e72b_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_peers_entry_mac_address_0x78cedd86ea7d8cba_cls', 'openenoc_endpoint_peers_entry_rmem_address_neg_0x6559b47b3208e18d_cls', 'openenoc_endpoint_peers_entry_local_address_neg_0x49e3835772dee4dd_cls', 'openenoc_endpoint_peers_entry_remote_address_neg_0x5a9e65567f65065a_cls', 'openenoc_endpoint_peers_entry_size_neg_0x53f79c915dbb3e3f_cls', 'openenoc_endpoint_peers_entry_dma_0x2d21abf34620e72b_cls', ]: ...

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
        yield self.dma
        
        
class openenoc_endpoint_peers_entry_neg_0x6adf294af53c4a69_cls_array(RegFileArray):
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
        return openenoc_endpoint_peers_entry_neg_0x6adf294af53c4a69_cls
    

    
    
class openenoc_endpoint_peers_0x611f7b30a870504e_cls(RegFile):
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
        
        self.__entry:openenoc_endpoint_peers_entry_neg_0x6adf294af53c4a69_cls_array = openenoc_endpoint_peers_entry_neg_0x6adf294af53c4a69_cls_array(address=self.address+0,
                                                                                      stride=28,
                                                                                      dimensions=tuple([4]),
                                                                                      logger_handle=logger_handle+'.entry',
                                                                                      inst_name='entry', parent=self)
        

    @property
    def size(self) -> int:
        return 112

    # properties for Register and RegisterFiles
    @property
    def entry(self) -> 'openenoc_endpoint_peers_entry_neg_0x6adf294af53c4a69_cls_array':
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

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_peers_entry_neg_0x6adf294af53c4a69_cls_array':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint1.peers"
    @property
    def rdl_desc(self) -> str:
        return "Register file for remote peer configuration and memory region information."
    
    

    
    def __iter__(self) -> Iterator[Union[Node, NodeArray]]:
        
        
        yield self.entry
        
        
    

    
    
class openenoc_endpoint_axis_if_sink_neg_0x546e273df416d100_cls(RegFile):
    """
    Class to represent a register file in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint1.axis_if.sink                                         |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Register file for the AXI4-Stream sink interface.</p>           |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__data', '__control', '__status']

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
        
            
        self.__data:openenoc_endpoint_axis_if_sink_data_0x2565dea76eeba99d_cls = openenoc_endpoint_axis_if_sink_data_0x2565dea76eeba99d_cls(
                                                                     address=self.address+0,
                                                                     logger_handle=logger_handle+'.data',
                                                                     inst_name='data', parent=self)
        
            
        self.__control:openenoc_endpoint_axis_if_sink_control_0x2fa17f6b8f2565d1_cls = openenoc_endpoint_axis_if_sink_control_0x2fa17f6b8f2565d1_cls(
                                                                     address=self.address+4,
                                                                     logger_handle=logger_handle+'.control',
                                                                     inst_name='control', parent=self)
        
            
        self.__status:openenoc_endpoint_axis_if_sink_status_0x664a8cd7a8dcd9f1_cls = openenoc_endpoint_axis_if_sink_status_0x664a8cd7a8dcd9f1_cls(
                                                                     address=self.address+8,
                                                                     logger_handle=logger_handle+'.status',
                                                                     inst_name='status', parent=self)
        

    @property
    def size(self) -> int:
        return 12

    # properties for Register and RegisterFiles
    @property
    def data(self) -> 'openenoc_endpoint_axis_if_sink_data_0x2565dea76eeba99d_cls':
        """
        Property to access data 

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
        return self.__data
    
    @property
    def control(self) -> 'openenoc_endpoint_axis_if_sink_control_0x2fa17f6b8f2565d1_cls':
        """
        Property to access control 

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
        return self.__control
    
    @property
    def status(self) -> 'openenoc_endpoint_axis_if_sink_status_0x664a8cd7a8dcd9f1_cls':
        """
        Property to access status 

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
        return self.__status
    

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'data':'data','control':'control','status':'status',
            }

    
    
    
    
    
    
    # nodes:3
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["data"]) -> 'openenoc_endpoint_axis_if_sink_data_0x2565dea76eeba99d_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["control"]) -> 'openenoc_endpoint_axis_if_sink_control_0x2fa17f6b8f2565d1_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["status"]) -> 'openenoc_endpoint_axis_if_sink_status_0x664a8cd7a8dcd9f1_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_axis_if_sink_data_0x2565dea76eeba99d_cls', 'openenoc_endpoint_axis_if_sink_control_0x2fa17f6b8f2565d1_cls', 'openenoc_endpoint_axis_if_sink_status_0x664a8cd7a8dcd9f1_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint1.axis_if.sink"
    @property
    def rdl_desc(self) -> str:
        return "Register file for the AXI4-Stream sink interface."
    
    

    
    def __iter__(self) -> Iterator[Union[Node, NodeArray]]:
        
        
        yield self.data
        yield self.control
        yield self.status
        
        
    

    
    
class openenoc_endpoint_axis_if_source_neg_0x66ff47bc485a31e6_cls(RegFile):
    """
    Class to represent a register file in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint1.axis_if.source                                       |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Register file for the AXI4-Stream source interface.</p>         |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__data', '__control', '__status']

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
        
            
        self.__data:openenoc_endpoint_axis_if_source_data_0x2362d42deed0b943_cls = openenoc_endpoint_axis_if_source_data_0x2362d42deed0b943_cls(
                                                                     address=self.address+0,
                                                                     logger_handle=logger_handle+'.data',
                                                                     inst_name='data', parent=self)
        
            
        self.__control:openenoc_endpoint_axis_if_source_control_neg_0x1b2b7f048b6aeae_cls = openenoc_endpoint_axis_if_source_control_neg_0x1b2b7f048b6aeae_cls(
                                                                     address=self.address+4,
                                                                     logger_handle=logger_handle+'.control',
                                                                     inst_name='control', parent=self)
        
            
        self.__status:openenoc_endpoint_axis_if_source_status_neg_0xfee0a2f3b74c649_cls = openenoc_endpoint_axis_if_source_status_neg_0xfee0a2f3b74c649_cls(
                                                                     address=self.address+8,
                                                                     logger_handle=logger_handle+'.status',
                                                                     inst_name='status', parent=self)
        

    @property
    def size(self) -> int:
        return 12

    # properties for Register and RegisterFiles
    @property
    def data(self) -> 'openenoc_endpoint_axis_if_source_data_0x2362d42deed0b943_cls':
        """
        Property to access data 

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
        return self.__data
    
    @property
    def control(self) -> 'openenoc_endpoint_axis_if_source_control_neg_0x1b2b7f048b6aeae_cls':
        """
        Property to access control 

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
        return self.__control
    
    @property
    def status(self) -> 'openenoc_endpoint_axis_if_source_status_neg_0xfee0a2f3b74c649_cls':
        """
        Property to access status 

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
        return self.__status
    

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'data':'data','control':'control','status':'status',
            }

    
    
    
    
    
    
    # nodes:3
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["data"]) -> 'openenoc_endpoint_axis_if_source_data_0x2362d42deed0b943_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["control"]) -> 'openenoc_endpoint_axis_if_source_control_neg_0x1b2b7f048b6aeae_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["status"]) -> 'openenoc_endpoint_axis_if_source_status_neg_0xfee0a2f3b74c649_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_axis_if_source_data_0x2362d42deed0b943_cls', 'openenoc_endpoint_axis_if_source_control_neg_0x1b2b7f048b6aeae_cls', 'openenoc_endpoint_axis_if_source_status_neg_0xfee0a2f3b74c649_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint1.axis_if.source"
    @property
    def rdl_desc(self) -> str:
        return "Register file for the AXI4-Stream source interface."
    
    

    
    def __iter__(self) -> Iterator[Union[Node, NodeArray]]:
        
        
        yield self.data
        yield self.control
        yield self.status
        
        
    

    
    
class openenoc_endpoint_axis_if_neg_0x5ef9eefe8a6ac923_cls(RegFile):
    """
    Class to represent a register file in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint1.axis_if                                              |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Register file for the AXI4-Stream source and sink               |
    |              |      interfaces.</p>                                                    |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__source', '__sink']

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
        self.__source:openenoc_endpoint_axis_if_source_neg_0x66ff47bc485a31e6_cls = openenoc_endpoint_axis_if_source_neg_0x66ff47bc485a31e6_cls(
                                                                                address=self.address+0,
                                                                                logger_handle=logger_handle+'.source',
                                                                                inst_name='source',
                                                                                parent=self)
        self.__sink:openenoc_endpoint_axis_if_sink_neg_0x546e273df416d100_cls = openenoc_endpoint_axis_if_sink_neg_0x546e273df416d100_cls(
                                                                                address=self.address+16,
                                                                                logger_handle=logger_handle+'.sink',
                                                                                inst_name='sink',
                                                                                parent=self)
        

    @property
    def size(self) -> int:
        return 28

    # properties for Register and RegisterFiles
    @property
    def source(self) -> 'openenoc_endpoint_axis_if_source_neg_0x66ff47bc485a31e6_cls':
        """
        Property to access source 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint1.axis_if.source                                       |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Register file for the AXI4-Stream source interface.</p>         |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__source
    
    @property
    def sink(self) -> 'openenoc_endpoint_axis_if_sink_neg_0x546e273df416d100_cls':
        """
        Property to access sink 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint1.axis_if.sink                                         |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Register file for the AXI4-Stream sink interface.</p>           |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__sink
    

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'source':'source','sink':'sink',
            }

    
    
    
    
    
    
    # nodes:2
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["source"]) -> 'openenoc_endpoint_axis_if_source_neg_0x66ff47bc485a31e6_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["sink"]) -> 'openenoc_endpoint_axis_if_sink_neg_0x546e273df416d100_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_axis_if_source_neg_0x66ff47bc485a31e6_cls', 'openenoc_endpoint_axis_if_sink_neg_0x546e273df416d100_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint1.axis_if"
    @property
    def rdl_desc(self) -> str:
        return "Register file for the AXI4-Stream source and sink interfaces."
    
    

    
    def __iter__(self) -> Iterator[Union[Node, NodeArray]]:
        
        
        yield self.source
        yield self.sink
        
        
    

    
    
class openenoc_endpoint_config_neg_0x6344a13cf1241008_cls(RegFile):
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
        
            
        self.__mac_address:openenoc_endpoint_config_mac_address_neg_0x6ed055f4bee94bd2_cls = openenoc_endpoint_config_mac_address_neg_0x6ed055f4bee94bd2_cls(
                                                                     address=self.address+0,
                                                                     logger_handle=logger_handle+'.mac_address',
                                                                     inst_name='mac_address', parent=self)
        

    @property
    def size(self) -> int:
        return 8

    # properties for Register and RegisterFiles
    @property
    def mac_address(self) -> 'openenoc_endpoint_config_mac_address_neg_0x6ed055f4bee94bd2_cls':
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

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_config_mac_address_neg_0x6ed055f4bee94bd2_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint1.config"
    @property
    def rdl_desc(self) -> str:
        return "Configuration register file for this openENOC Endpoint Interface instance."
    
    

    
    def __iter__(self) -> Iterator[Union[Node, NodeArray]]:
        
        
        yield self.mac_address
        
        
    

    
    
class openenoc_endpoint_0x72cc9b177b7571db_cls(AddressMap):
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

    __slots__ : list[str] = ['__info', '__config', '__axis_if', '__peers', '__rmem']

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

        
            
        self.__info:openenoc_endpoint_info_neg_0x735b88c1b28e8f33_cls = openenoc_endpoint_info_neg_0x735b88c1b28e8f33_cls(
                                                                     address=self.address+0,
                                                                     logger_handle=logger_handle+'.info',
                                                                     inst_name='info', parent=self)
        self.__config:openenoc_endpoint_config_neg_0x6344a13cf1241008_cls = openenoc_endpoint_config_neg_0x6344a13cf1241008_cls(
                                                                                address=self.address+8,
                                                                                logger_handle=logger_handle+'.config',
                                                                                inst_name='config',
                                                                                parent=self)
        self.__axis_if:openenoc_endpoint_axis_if_neg_0x5ef9eefe8a6ac923_cls = openenoc_endpoint_axis_if_neg_0x5ef9eefe8a6ac923_cls(
                                                                                address=self.address+32,
                                                                                logger_handle=logger_handle+'.axis_if',
                                                                                inst_name='axis_if',
                                                                                parent=self)
        self.__peers:openenoc_endpoint_peers_0x611f7b30a870504e_cls = openenoc_endpoint_peers_0x611f7b30a870504e_cls(
                                                                                address=self.address+128,
                                                                                logger_handle=logger_handle+'.peers',
                                                                                inst_name='peers',
                                                                                parent=self)
        
        self.__rmem:openenoc_endpoint_rmem_0x497dea42f489d12d_cls = openenoc_endpoint_rmem_0x497dea42f489d12d_cls(
                                                                     address=self.address+1024,
                                                                     logger_handle=logger_handle+'.rmem',
                                                                                       inst_name='rmem', parent=self)
        

    @property
    def size(self) -> int:
        return 2048
    @property
    def info(self) -> 'openenoc_endpoint_info_neg_0x735b88c1b28e8f33_cls':
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
    def config(self) -> 'openenoc_endpoint_config_neg_0x6344a13cf1241008_cls':
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
    def axis_if(self) -> 'openenoc_endpoint_axis_if_neg_0x5ef9eefe8a6ac923_cls':
        """
        Property to access axis_if 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint1.axis_if                                              |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Register file for the AXI4-Stream source and sink               |
        |              |      interfaces.</p>                                                    |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__axis_if
        
    @property
    def peers(self) -> 'openenoc_endpoint_peers_0x611f7b30a870504e_cls':
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
    def rmem(self) -> 'openenoc_endpoint_rmem_0x497dea42f489d12d_cls':
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
        return {'info':'info','config':'config','axis_if':'axis_if','peers':'peers','rmem':'rmem',
            }

    
    
    
    
    
    
    # nodes:5
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["info"]) -> 'openenoc_endpoint_info_neg_0x735b88c1b28e8f33_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["config"]) -> 'openenoc_endpoint_config_neg_0x6344a13cf1241008_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["axis_if"]) -> 'openenoc_endpoint_axis_if_neg_0x5ef9eefe8a6ac923_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["peers"]) -> 'openenoc_endpoint_peers_0x611f7b30a870504e_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["rmem"]) -> 'openenoc_endpoint_rmem_0x497dea42f489d12d_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_info_neg_0x735b88c1b28e8f33_cls', 'openenoc_endpoint_config_neg_0x6344a13cf1241008_cls', 'openenoc_endpoint_axis_if_neg_0x5ef9eefe8a6ac923_cls', 'openenoc_endpoint_peers_0x611f7b30a870504e_cls', 'openenoc_endpoint_rmem_0x497dea42f489d12d_cls', ]: ...

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
        yield self.axis_if
        yield self.peers
        yield self.rmem
        
        
    

    
    
class openenoc_csr_neg_0x74459a8ac5f10756_cls(AddressMap):
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

        
            
        self.__test_reg:openenoc_csr_test_reg_0x69f601ad22f2142_cls = openenoc_csr_test_reg_0x69f601ad22f2142_cls(
                                                                     address=self.address+0,
                                                                     logger_handle=logger_handle+'.test_reg',
                                                                     inst_name='test_reg', parent=self)
        
            
        self.__regB:openenoc_csr_regB_neg_0xe16f3a07eae63d6_cls = openenoc_csr_regB_neg_0xe16f3a07eae63d6_cls(
                                                                     address=self.address+4,
                                                                     logger_handle=logger_handle+'.regB',
                                                                     inst_name='regB', parent=self)
        self.__endpoint1:openenoc_endpoint_0x72cc9b177b7571db_cls = openenoc_endpoint_0x72cc9b177b7571db_cls(
                                                                                address=self.address+2048,
                                                                                logger_handle=logger_handle+'.endpoint1',
                                                                                inst_name='endpoint1',
                                                                                parent=self)
        self.__endpoint2:openenoc_endpoint_0x14b5eec0360ba6db_cls = openenoc_endpoint_0x14b5eec0360ba6db_cls(
                                                                                address=self.address+4096,
                                                                                logger_handle=logger_handle+'.endpoint2',
                                                                                inst_name='endpoint2',
                                                                                parent=self)
        self.__switch1:openenoc_switch_neg_0xf782f49dd81dd1d_cls = openenoc_switch_neg_0xf782f49dd81dd1d_cls(
                                                                                address=self.address+5120,
                                                                                logger_handle=logger_handle+'.switch1',
                                                                                inst_name='switch1',
                                                                                parent=self)
        self.__switch2:openenoc_switch_neg_0x62f9a5ec3f4ef54a_cls = openenoc_switch_neg_0x62f9a5ec3f4ef54a_cls(
                                                                                address=self.address+6144,
                                                                                logger_handle=logger_handle+'.switch2',
                                                                                inst_name='switch2',
                                                                                parent=self)
        

    @property
    def size(self) -> int:
        return 7168
    @property
    def test_reg(self) -> 'openenoc_csr_test_reg_0x69f601ad22f2142_cls':
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
    def regB(self) -> 'openenoc_csr_regB_neg_0xe16f3a07eae63d6_cls':
        """
        Property to access regB 

        
        """
        return self.__regB
        
    @property
    def endpoint1(self) -> 'openenoc_endpoint_0x72cc9b177b7571db_cls':
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
    def endpoint2(self) -> 'openenoc_endpoint_0x14b5eec0360ba6db_cls':
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
    def switch1(self) -> 'openenoc_switch_neg_0xf782f49dd81dd1d_cls':
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
    def switch2(self) -> 'openenoc_switch_neg_0x62f9a5ec3f4ef54a_cls':
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
    def get_child_by_system_rdl_name(self, name: Literal["test_reg"]) -> 'openenoc_csr_test_reg_0x69f601ad22f2142_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["regB"]) -> 'openenoc_csr_regB_neg_0xe16f3a07eae63d6_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["endpoint1"]) -> 'openenoc_endpoint_0x72cc9b177b7571db_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["endpoint2"]) -> 'openenoc_endpoint_0x14b5eec0360ba6db_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["switch1"]) -> 'openenoc_switch_neg_0xf782f49dd81dd1d_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["switch2"]) -> 'openenoc_switch_neg_0x62f9a5ec3f4ef54a_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_csr_test_reg_0x69f601ad22f2142_cls', 'openenoc_csr_regB_neg_0xe16f3a07eae63d6_cls', 'openenoc_endpoint_0x72cc9b177b7571db_cls', 'openenoc_endpoint_0x14b5eec0360ba6db_cls', 'openenoc_switch_neg_0xf782f49dd81dd1d_cls', 'openenoc_switch_neg_0x62f9a5ec3f4ef54a_cls', ]: ...

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
        
        
    


openenoc_csr_cls = openenoc_csr_neg_0x74459a8ac5f10756_cls

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