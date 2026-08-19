


"""
Python Wrapper for the csr register model

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





from ._registers import csr_test_reg_neg_0x1bed016ad15a95ef_cls
from ._registers import csr_regB_neg_0x6309110ed09171fa_cls
from ._registers import openenoc_endpoint_interface_info_neg_0x639a39012e010981_cls
from ._registers import openenoc_endpoint_interface_config_mac_address_0x5875bec253f92600_cls
from ._registers import openenoc_endpoint_interface_axis_if_source_data_neg_0x4ab2b2a3816c7dee_cls
from ._registers import openenoc_endpoint_interface_axis_if_source_control_0x2356e1cb785e4243_cls
from ._registers import openenoc_endpoint_interface_axis_if_source_status_0x7b4af6da31bd5135_cls
from ._registers import openenoc_endpoint_interface_axis_if_sink_data_0x713b3db23f576eaa_cls
from ._registers import openenoc_endpoint_interface_axis_if_sink_control_neg_0x2be5dabe4f99d2e7_cls
from ._registers import openenoc_endpoint_interface_axis_if_sink_status_0x4b970e22a62f9c89_cls
from ._registers import openenoc_endpoint_interface_peers_entry_mac_address_neg_0xff740dd8f2abf3a_cls
from ._registers import openenoc_endpoint_interface_peers_entry_rmem_address_neg_0x712f970ba98b47cb_cls
from ._registers import openenoc_endpoint_interface_peers_entry_local_address_neg_0x86ef9da6095870c_cls
from ._registers import openenoc_endpoint_interface_peers_entry_remote_address_0x4ef574e36bcf7fb3_cls
from ._registers import openenoc_endpoint_interface_peers_entry_size_neg_0x27d149353842ecbe_cls
from ._registers import openenoc_endpoint_interface_peers_entry_dma_neg_0x2593b064c9639942_cls
from ._registers import openenoc_endpoint_interface_rmem_word_neg_0x23a769c4b2cf9eaf_cls_array
from ._registers import openenoc_switch_interface_info_neg_0x68535d6a5887b8bd_cls
from ._registers import openenoc_switch_interface_forwarding_control_neg_0x66d5e30db0f60622_cls
from ._registers import openenoc_switch_interface_default_forwarding_neg_0x52189bae7a475b3a_cls
from ._registers import openenoc_switch_interface_forwarding_table_entry_mac_address_0x5bf162228885a291_cls
from ._registers import openenoc_switch_interface_forwarding_table_entry_iface_0x68e6aed0a1832f87_cls
from ._registers import openenoc_switch_interface_forwarding_table_entry_config_neg_0x2edf4441705a3012_cls


# addrmap, regfile, memor and register definitions
    
    
class openenoc_switch_interface_forwarding_table_entry_0x837c6e634a1e922_cls(RegFile):
    """
    Class to represent a register file in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1]      |
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
        
            
        self.__mac_address:openenoc_switch_interface_forwarding_table_entry_mac_address_0x5bf162228885a291_cls = openenoc_switch_interface_forwarding_table_entry_mac_address_0x5bf162228885a291_cls(
                                                                     address=self.address+0,
                                                                     logger_handle=logger_handle+'.mac_address',
                                                                     inst_name='mac_address', parent=self)
        
            
        self.__iface:openenoc_switch_interface_forwarding_table_entry_iface_0x68e6aed0a1832f87_cls = openenoc_switch_interface_forwarding_table_entry_iface_0x68e6aed0a1832f87_cls(
                                                                     address=self.address+8,
                                                                     logger_handle=logger_handle+'.iface',
                                                                     inst_name='iface', parent=self)
        
            
        self.__config:openenoc_switch_interface_forwarding_table_entry_config_neg_0x2edf4441705a3012_cls = openenoc_switch_interface_forwarding_table_entry_config_neg_0x2edf4441705a3012_cls(
                                                                     address=self.address+12,
                                                                     logger_handle=logger_handle+'.config',
                                                                     inst_name='config', parent=self)
        

    @property
    def size(self) -> int:
        return 16

    # properties for Register and RegisterFiles
    @property
    def mac_address(self) -> 'openenoc_switch_interface_forwarding_table_entry_mac_address_0x5bf162228885a291_cls':
        """
        Property to access mac_address 

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
        return self.__mac_address
    
    @property
    def iface(self) -> 'openenoc_switch_interface_forwarding_table_entry_iface_0x68e6aed0a1832f87_cls':
        """
        Property to access iface 

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
        return self.__iface
    
    @property
    def config(self) -> 'openenoc_switch_interface_forwarding_table_entry_config_neg_0x2edf4441705a3012_cls':
        """
        Property to access config 

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
        return self.__config
    

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'mac_address':'mac_address','iface':'iface','config':'config',
            }

    
    
    
    
    
    
    # nodes:3
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["mac_address"]) -> 'openenoc_switch_interface_forwarding_table_entry_mac_address_0x5bf162228885a291_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["iface"]) -> 'openenoc_switch_interface_forwarding_table_entry_iface_0x68e6aed0a1832f87_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["config"]) -> 'openenoc_switch_interface_forwarding_table_entry_config_neg_0x2edf4441705a3012_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_switch_interface_forwarding_table_entry_mac_address_0x5bf162228885a291_cls', 'openenoc_switch_interface_forwarding_table_entry_iface_0x68e6aed0a1832f87_cls', 'openenoc_switch_interface_forwarding_table_entry_config_neg_0x2edf4441705a3012_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1]"
    @property
    def rdl_desc(self) -> str:
        return "Forwarding table entry containing the MAC address key, output interface selection, and entry configuration."
    
    

    
    def __iter__(self) -> Iterator[Union[Node, NodeArray]]:
        
        
        yield self.mac_address
        yield self.iface
        yield self.config
        
        
class openenoc_switch_interface_forwarding_table_entry_0x837c6e634a1e922_cls_array(RegFileArray):
    """
    Class to represent a regfile array in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1]      |
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
        return openenoc_switch_interface_forwarding_table_entry_0x837c6e634a1e922_cls
    

    
    
class openenoc_switch_interface_forwarding_table_0x4923086c07258c8d_cls(RegFile):
    """
    Class to represent a register file in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.switch_interface.forwarding_table                              |
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
        
        self.__entry:openenoc_switch_interface_forwarding_table_entry_0x837c6e634a1e922_cls_array = openenoc_switch_interface_forwarding_table_entry_0x837c6e634a1e922_cls_array(address=self.address+0,
                                                                                      stride=16,
                                                                                      dimensions=tuple([8]),
                                                                                      logger_handle=logger_handle+'.entry',
                                                                                      inst_name='entry', parent=self)
        

    @property
    def size(self) -> int:
        return 128

    # properties for Register and RegisterFiles
    @property
    def entry(self) -> 'openenoc_switch_interface_forwarding_table_entry_0x837c6e634a1e922_cls_array':
        """
        Property to access entry array

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1]      |
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

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_switch_interface_forwarding_table_entry_0x837c6e634a1e922_cls_array':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.switch_interface.forwarding_table"
    @property
    def rdl_desc(self) -> str:
        return "Forwarding table used to map MAC addresses to output interface selections for frame forwarding."
    
    

    
    def __iter__(self) -> Iterator[Union[Node, NodeArray]]:
        
        
        yield self.entry
        
        
    

    
    
class openenoc_switch_interface_0x11366b9728f55963_cls(RegFile):
    """
    Class to represent a register file in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.switch_interface                                               |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Control and status register file for an openENOC Switch         |
    |              |      instance. It includes configuration registers and a forwarding     |
    |              |      table used to map destination MAC address keys to output interface |
    |              |      selections for frame forwarding.</p>                               |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__info', '__forwarding_control', '__default_forwarding', '__forwarding_table']

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
        
            
        self.__info:openenoc_switch_interface_info_neg_0x68535d6a5887b8bd_cls = openenoc_switch_interface_info_neg_0x68535d6a5887b8bd_cls(
                                                                     address=self.address+0,
                                                                     logger_handle=logger_handle+'.info',
                                                                     inst_name='info', parent=self)
        
            
        self.__forwarding_control:openenoc_switch_interface_forwarding_control_neg_0x66d5e30db0f60622_cls = openenoc_switch_interface_forwarding_control_neg_0x66d5e30db0f60622_cls(
                                                                     address=self.address+4,
                                                                     logger_handle=logger_handle+'.forwarding_control',
                                                                     inst_name='forwarding_control', parent=self)
        
            
        self.__default_forwarding:openenoc_switch_interface_default_forwarding_neg_0x52189bae7a475b3a_cls = openenoc_switch_interface_default_forwarding_neg_0x52189bae7a475b3a_cls(
                                                                     address=self.address+8,
                                                                     logger_handle=logger_handle+'.default_forwarding',
                                                                     inst_name='default_forwarding', parent=self)
        self.__forwarding_table:openenoc_switch_interface_forwarding_table_0x4923086c07258c8d_cls = openenoc_switch_interface_forwarding_table_0x4923086c07258c8d_cls(
                                                                                address=self.address+128,
                                                                                logger_handle=logger_handle+'.forwarding_table',
                                                                                inst_name='forwarding_table',
                                                                                parent=self)
        

    @property
    def size(self) -> int:
        return 256

    # properties for Register and RegisterFiles
    @property
    def info(self) -> 'openenoc_switch_interface_info_neg_0x68535d6a5887b8bd_cls':
        """
        Property to access info 

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
        return self.__info
    
    @property
    def forwarding_control(self) -> 'openenoc_switch_interface_forwarding_control_neg_0x66d5e30db0f60622_cls':
        """
        Property to access forwarding_control 

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
        return self.__forwarding_control
    
    @property
    def default_forwarding(self) -> 'openenoc_switch_interface_default_forwarding_neg_0x52189bae7a475b3a_cls':
        """
        Property to access default_forwarding 

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
        return self.__default_forwarding
    
    @property
    def forwarding_table(self) -> 'openenoc_switch_interface_forwarding_table_0x4923086c07258c8d_cls':
        """
        Property to access forwarding_table 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.switch_interface.forwarding_table                              |
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
    def get_child_by_system_rdl_name(self, name: Literal["info"]) -> 'openenoc_switch_interface_info_neg_0x68535d6a5887b8bd_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["forwarding_control"]) -> 'openenoc_switch_interface_forwarding_control_neg_0x66d5e30db0f60622_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["default_forwarding"]) -> 'openenoc_switch_interface_default_forwarding_neg_0x52189bae7a475b3a_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["forwarding_table"]) -> 'openenoc_switch_interface_forwarding_table_0x4923086c07258c8d_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_switch_interface_info_neg_0x68535d6a5887b8bd_cls', 'openenoc_switch_interface_forwarding_control_neg_0x66d5e30db0f60622_cls', 'openenoc_switch_interface_default_forwarding_neg_0x52189bae7a475b3a_cls', 'openenoc_switch_interface_forwarding_table_0x4923086c07258c8d_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.switch_interface"
    @property
    def rdl_desc(self) -> str:
        return "Control and status register file for an openENOC Switch instance. It includes configuration registers and a forwarding table used to map destination MAC address keys to output interface selections for frame forwarding."
    
    

    
    def __iter__(self) -> Iterator[Union[Node, NodeArray]]:
        
        
        yield self.info
        yield self.forwarding_control
        yield self.default_forwarding
        yield self.forwarding_table
        
        
    

    
    
class openenoc_endpoint_interface_rmem_0x78bf74252298273c_cls(RegFile):
    """
    Class to represent a register file in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.rmem                                        |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Virtual memory region for all remote peers, with offsets and    |
    |              |      sizes defined in the peers regfile.</p>                            |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__word']

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
        
            
        self.__word:openenoc_endpoint_interface_rmem_word_neg_0x23a769c4b2cf9eaf_cls_array = openenoc_endpoint_interface_rmem_word_neg_0x23a769c4b2cf9eaf_cls_array(address=self.address+0,
                                                                                      stride=4,
                                                                                      dimensions=tuple([256]),
                                                                                      logger_handle=logger_handle+'.word',
                                                                                      inst_name='word', parent=self)
        

    @property
    def size(self) -> int:
        return 1024

    # properties for Register and RegisterFiles
    @property
    def word(self) -> 'openenoc_endpoint_interface_rmem_word_neg_0x23a769c4b2cf9eaf_cls_array':
        """
        Property to access word array

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
        return self.__word
    

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'word':'word',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_interface_rmem_word_neg_0x23a769c4b2cf9eaf_cls_array':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.rmem"
    @property
    def rdl_desc(self) -> str:
        return "Virtual memory region for all remote peers, with offsets and sizes defined in the peers regfile."
    
    

    
    def __iter__(self) -> Iterator[Union[Node, NodeArray]]:
        
        
        yield self.word
        
        
    

    
    
class openenoc_endpoint_interface_peers_entry_0x26fba004d62a73f3_cls(RegFile):
    """
    Class to represent a register file in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1]              |
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
        
            
        self.__mac_address:openenoc_endpoint_interface_peers_entry_mac_address_neg_0xff740dd8f2abf3a_cls = openenoc_endpoint_interface_peers_entry_mac_address_neg_0xff740dd8f2abf3a_cls(
                                                                     address=self.address+0,
                                                                     logger_handle=logger_handle+'.mac_address',
                                                                     inst_name='mac_address', parent=self)
        
            
        self.__rmem_address:openenoc_endpoint_interface_peers_entry_rmem_address_neg_0x712f970ba98b47cb_cls = openenoc_endpoint_interface_peers_entry_rmem_address_neg_0x712f970ba98b47cb_cls(
                                                                     address=self.address+8,
                                                                     logger_handle=logger_handle+'.rmem_address',
                                                                     inst_name='rmem_address', parent=self)
        
            
        self.__local_address:openenoc_endpoint_interface_peers_entry_local_address_neg_0x86ef9da6095870c_cls = openenoc_endpoint_interface_peers_entry_local_address_neg_0x86ef9da6095870c_cls(
                                                                     address=self.address+12,
                                                                     logger_handle=logger_handle+'.local_address',
                                                                     inst_name='local_address', parent=self)
        
            
        self.__remote_address:openenoc_endpoint_interface_peers_entry_remote_address_0x4ef574e36bcf7fb3_cls = openenoc_endpoint_interface_peers_entry_remote_address_0x4ef574e36bcf7fb3_cls(
                                                                     address=self.address+16,
                                                                     logger_handle=logger_handle+'.remote_address',
                                                                     inst_name='remote_address', parent=self)
        
            
        self.__size:openenoc_endpoint_interface_peers_entry_size_neg_0x27d149353842ecbe_cls = openenoc_endpoint_interface_peers_entry_size_neg_0x27d149353842ecbe_cls(
                                                                     address=self.address+20,
                                                                     logger_handle=logger_handle+'.size',
                                                                     inst_name='size', parent=self)
        
            
        self.__dma:openenoc_endpoint_interface_peers_entry_dma_neg_0x2593b064c9639942_cls = openenoc_endpoint_interface_peers_entry_dma_neg_0x2593b064c9639942_cls(
                                                                     address=self.address+24,
                                                                     logger_handle=logger_handle+'.dma',
                                                                     inst_name='dma', parent=self)
        

    @property
    def size(self) -> int:
        return 28

    # properties for Register and RegisterFiles
    @property
    def mac_address(self) -> 'openenoc_endpoint_interface_peers_entry_mac_address_neg_0xff740dd8f2abf3a_cls':
        """
        Property to access mac_address 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].mac_address  |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Remote peer 48-bit destination MAC address.</p>                 |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__mac_address
    
    @property
    def rmem_address(self) -> 'openenoc_endpoint_interface_peers_entry_rmem_address_neg_0x712f970ba98b47cb_cls':
        """
        Property to access rmem_address 

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
        return self.__rmem_address
    
    @property
    def local_address(self) -> 'openenoc_endpoint_interface_peers_entry_local_address_neg_0x86ef9da6095870c_cls':
        """
        Property to access local_address 

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
        return self.__local_address
    
    @property
    def remote_address(self) -> 'openenoc_endpoint_interface_peers_entry_remote_address_0x4ef574e36bcf7fb3_cls':
        """
        Property to access remote_address 

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
        return self.__remote_address
    
    @property
    def register_size(self) -> 'openenoc_endpoint_interface_peers_entry_size_neg_0x27d149353842ecbe_cls':
        """
        Property to access size 

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
        return self.__size
    
    @property
    def dma(self) -> 'openenoc_endpoint_interface_peers_entry_dma_neg_0x2593b064c9639942_cls':
        """
        Property to access dma 

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
        return self.__dma
    

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'mac_address':'mac_address','rmem_address':'rmem_address','local_address':'local_address','remote_address':'remote_address','size':'register_size','dma':'dma',
            }

    
    
    
    
    
    
    # nodes:6
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["mac_address"]) -> 'openenoc_endpoint_interface_peers_entry_mac_address_neg_0xff740dd8f2abf3a_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["rmem_address"]) -> 'openenoc_endpoint_interface_peers_entry_rmem_address_neg_0x712f970ba98b47cb_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["local_address"]) -> 'openenoc_endpoint_interface_peers_entry_local_address_neg_0x86ef9da6095870c_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["remote_address"]) -> 'openenoc_endpoint_interface_peers_entry_remote_address_0x4ef574e36bcf7fb3_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["size"]) -> 'openenoc_endpoint_interface_peers_entry_size_neg_0x27d149353842ecbe_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["dma"]) -> 'openenoc_endpoint_interface_peers_entry_dma_neg_0x2593b064c9639942_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_interface_peers_entry_mac_address_neg_0xff740dd8f2abf3a_cls', 'openenoc_endpoint_interface_peers_entry_rmem_address_neg_0x712f970ba98b47cb_cls', 'openenoc_endpoint_interface_peers_entry_local_address_neg_0x86ef9da6095870c_cls', 'openenoc_endpoint_interface_peers_entry_remote_address_0x4ef574e36bcf7fb3_cls', 'openenoc_endpoint_interface_peers_entry_size_neg_0x27d149353842ecbe_cls', 'openenoc_endpoint_interface_peers_entry_dma_neg_0x2593b064c9639942_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1]"
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
        
        
class openenoc_endpoint_interface_peers_entry_0x26fba004d62a73f3_cls_array(RegFileArray):
    """
    Class to represent a regfile array in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1]              |
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
        return openenoc_endpoint_interface_peers_entry_0x26fba004d62a73f3_cls
    

    
    
class openenoc_endpoint_interface_peers_0x39d7a117c0591cca_cls(RegFile):
    """
    Class to represent a register file in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.peers                                       |
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
        
        self.__entry:openenoc_endpoint_interface_peers_entry_0x26fba004d62a73f3_cls_array = openenoc_endpoint_interface_peers_entry_0x26fba004d62a73f3_cls_array(address=self.address+0,
                                                                                      stride=28,
                                                                                      dimensions=tuple([4]),
                                                                                      logger_handle=logger_handle+'.entry',
                                                                                      inst_name='entry', parent=self)
        

    @property
    def size(self) -> int:
        return 112

    # properties for Register and RegisterFiles
    @property
    def entry(self) -> 'openenoc_endpoint_interface_peers_entry_0x26fba004d62a73f3_cls_array':
        """
        Property to access entry array

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1]              |
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

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_interface_peers_entry_0x26fba004d62a73f3_cls_array':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.peers"
    @property
    def rdl_desc(self) -> str:
        return "Register file for remote peer configuration and memory region information."
    
    

    
    def __iter__(self) -> Iterator[Union[Node, NodeArray]]:
        
        
        yield self.entry
        
        
    

    
    
class openenoc_endpoint_interface_axis_if_sink_0x5bd94f247a6c8358_cls(RegFile):
    """
    Class to represent a register file in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.axis_if.sink                                |
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
        
            
        self.__data:openenoc_endpoint_interface_axis_if_sink_data_0x713b3db23f576eaa_cls = openenoc_endpoint_interface_axis_if_sink_data_0x713b3db23f576eaa_cls(
                                                                     address=self.address+0,
                                                                     logger_handle=logger_handle+'.data',
                                                                     inst_name='data', parent=self)
        
            
        self.__control:openenoc_endpoint_interface_axis_if_sink_control_neg_0x2be5dabe4f99d2e7_cls = openenoc_endpoint_interface_axis_if_sink_control_neg_0x2be5dabe4f99d2e7_cls(
                                                                     address=self.address+4,
                                                                     logger_handle=logger_handle+'.control',
                                                                     inst_name='control', parent=self)
        
            
        self.__status:openenoc_endpoint_interface_axis_if_sink_status_0x4b970e22a62f9c89_cls = openenoc_endpoint_interface_axis_if_sink_status_0x4b970e22a62f9c89_cls(
                                                                     address=self.address+8,
                                                                     logger_handle=logger_handle+'.status',
                                                                     inst_name='status', parent=self)
        

    @property
    def size(self) -> int:
        return 12

    # properties for Register and RegisterFiles
    @property
    def data(self) -> 'openenoc_endpoint_interface_axis_if_sink_data_0x713b3db23f576eaa_cls':
        """
        Property to access data 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.axis_if.sink.data                           |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Data register for the AXI4-Stream sink interface.</p>           |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__data
    
    @property
    def control(self) -> 'openenoc_endpoint_interface_axis_if_sink_control_neg_0x2be5dabe4f99d2e7_cls':
        """
        Property to access control 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.axis_if.sink.control                        |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Control register for the AXI4-Stream sink interface.</p>        |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__control
    
    @property
    def status(self) -> 'openenoc_endpoint_interface_axis_if_sink_status_0x4b970e22a62f9c89_cls':
        """
        Property to access status 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.axis_if.sink.status                         |
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
    def get_child_by_system_rdl_name(self, name: Literal["data"]) -> 'openenoc_endpoint_interface_axis_if_sink_data_0x713b3db23f576eaa_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["control"]) -> 'openenoc_endpoint_interface_axis_if_sink_control_neg_0x2be5dabe4f99d2e7_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["status"]) -> 'openenoc_endpoint_interface_axis_if_sink_status_0x4b970e22a62f9c89_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_interface_axis_if_sink_data_0x713b3db23f576eaa_cls', 'openenoc_endpoint_interface_axis_if_sink_control_neg_0x2be5dabe4f99d2e7_cls', 'openenoc_endpoint_interface_axis_if_sink_status_0x4b970e22a62f9c89_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.axis_if.sink"
    @property
    def rdl_desc(self) -> str:
        return "Register file for the AXI4-Stream sink interface."
    
    

    
    def __iter__(self) -> Iterator[Union[Node, NodeArray]]:
        
        
        yield self.data
        yield self.control
        yield self.status
        
        
    

    
    
class openenoc_endpoint_interface_axis_if_source_neg_0x1c7b98ce836f36a3_cls(RegFile):
    """
    Class to represent a register file in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.axis_if.source                              |
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
        
            
        self.__data:openenoc_endpoint_interface_axis_if_source_data_neg_0x4ab2b2a3816c7dee_cls = openenoc_endpoint_interface_axis_if_source_data_neg_0x4ab2b2a3816c7dee_cls(
                                                                     address=self.address+0,
                                                                     logger_handle=logger_handle+'.data',
                                                                     inst_name='data', parent=self)
        
            
        self.__control:openenoc_endpoint_interface_axis_if_source_control_0x2356e1cb785e4243_cls = openenoc_endpoint_interface_axis_if_source_control_0x2356e1cb785e4243_cls(
                                                                     address=self.address+4,
                                                                     logger_handle=logger_handle+'.control',
                                                                     inst_name='control', parent=self)
        
            
        self.__status:openenoc_endpoint_interface_axis_if_source_status_0x7b4af6da31bd5135_cls = openenoc_endpoint_interface_axis_if_source_status_0x7b4af6da31bd5135_cls(
                                                                     address=self.address+8,
                                                                     logger_handle=logger_handle+'.status',
                                                                     inst_name='status', parent=self)
        

    @property
    def size(self) -> int:
        return 12

    # properties for Register and RegisterFiles
    @property
    def data(self) -> 'openenoc_endpoint_interface_axis_if_source_data_neg_0x4ab2b2a3816c7dee_cls':
        """
        Property to access data 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.axis_if.source.data                         |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Data register for the AXI4-Stream source interface.</p>         |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__data
    
    @property
    def control(self) -> 'openenoc_endpoint_interface_axis_if_source_control_0x2356e1cb785e4243_cls':
        """
        Property to access control 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.axis_if.source.control                      |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Control register for the AXI4-Stream source interface.</p>      |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__control
    
    @property
    def status(self) -> 'openenoc_endpoint_interface_axis_if_source_status_0x7b4af6da31bd5135_cls':
        """
        Property to access status 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.axis_if.source.status                       |
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
    def get_child_by_system_rdl_name(self, name: Literal["data"]) -> 'openenoc_endpoint_interface_axis_if_source_data_neg_0x4ab2b2a3816c7dee_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["control"]) -> 'openenoc_endpoint_interface_axis_if_source_control_0x2356e1cb785e4243_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["status"]) -> 'openenoc_endpoint_interface_axis_if_source_status_0x7b4af6da31bd5135_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_interface_axis_if_source_data_neg_0x4ab2b2a3816c7dee_cls', 'openenoc_endpoint_interface_axis_if_source_control_0x2356e1cb785e4243_cls', 'openenoc_endpoint_interface_axis_if_source_status_0x7b4af6da31bd5135_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.axis_if.source"
    @property
    def rdl_desc(self) -> str:
        return "Register file for the AXI4-Stream source interface."
    
    

    
    def __iter__(self) -> Iterator[Union[Node, NodeArray]]:
        
        
        yield self.data
        yield self.control
        yield self.status
        
        
    

    
    
class openenoc_endpoint_interface_axis_if_0x3feb390ce0f22f04_cls(RegFile):
    """
    Class to represent a register file in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.axis_if                                     |
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
        self.__source:openenoc_endpoint_interface_axis_if_source_neg_0x1c7b98ce836f36a3_cls = openenoc_endpoint_interface_axis_if_source_neg_0x1c7b98ce836f36a3_cls(
                                                                                address=self.address+0,
                                                                                logger_handle=logger_handle+'.source',
                                                                                inst_name='source',
                                                                                parent=self)
        self.__sink:openenoc_endpoint_interface_axis_if_sink_0x5bd94f247a6c8358_cls = openenoc_endpoint_interface_axis_if_sink_0x5bd94f247a6c8358_cls(
                                                                                address=self.address+16,
                                                                                logger_handle=logger_handle+'.sink',
                                                                                inst_name='sink',
                                                                                parent=self)
        

    @property
    def size(self) -> int:
        return 28

    # properties for Register and RegisterFiles
    @property
    def source(self) -> 'openenoc_endpoint_interface_axis_if_source_neg_0x1c7b98ce836f36a3_cls':
        """
        Property to access source 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.axis_if.source                              |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Register file for the AXI4-Stream source interface.</p>         |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__source
    
    @property
    def sink(self) -> 'openenoc_endpoint_interface_axis_if_sink_0x5bd94f247a6c8358_cls':
        """
        Property to access sink 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.axis_if.sink                                |
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
    def get_child_by_system_rdl_name(self, name: Literal["source"]) -> 'openenoc_endpoint_interface_axis_if_source_neg_0x1c7b98ce836f36a3_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["sink"]) -> 'openenoc_endpoint_interface_axis_if_sink_0x5bd94f247a6c8358_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_interface_axis_if_source_neg_0x1c7b98ce836f36a3_cls', 'openenoc_endpoint_interface_axis_if_sink_0x5bd94f247a6c8358_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.axis_if"
    @property
    def rdl_desc(self) -> str:
        return "Register file for the AXI4-Stream source and sink interfaces."
    
    

    
    def __iter__(self) -> Iterator[Union[Node, NodeArray]]:
        
        
        yield self.source
        yield self.sink
        
        
    

    
    
class openenoc_endpoint_interface_config_0x5830be79b2944b61_cls(RegFile):
    """
    Class to represent a register file in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.config                                      |
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
        
            
        self.__mac_address:openenoc_endpoint_interface_config_mac_address_0x5875bec253f92600_cls = openenoc_endpoint_interface_config_mac_address_0x5875bec253f92600_cls(
                                                                     address=self.address+0,
                                                                     logger_handle=logger_handle+'.mac_address',
                                                                     inst_name='mac_address', parent=self)
        

    @property
    def size(self) -> int:
        return 8

    # properties for Register and RegisterFiles
    @property
    def mac_address(self) -> 'openenoc_endpoint_interface_config_mac_address_0x5875bec253f92600_cls':
        """
        Property to access mac_address 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.config.mac_address                          |
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

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_interface_config_mac_address_0x5875bec253f92600_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.config"
    @property
    def rdl_desc(self) -> str:
        return "Configuration register file for this openENOC Endpoint Interface instance."
    
    

    
    def __iter__(self) -> Iterator[Union[Node, NodeArray]]:
        
        
        yield self.mac_address
        
        
    

    
    
class openenoc_endpoint_interface_neg_0x6aed29be915be9f_cls(RegFile):
    """
    Class to represent a register file in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface                                             |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Control and status register file for an openENOC Endpoint       |
    |              |      Interface instance.</p>                                            |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__info', '__config', '__axis_if', '__peers', '__rmem']

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
        
            
        self.__info:openenoc_endpoint_interface_info_neg_0x639a39012e010981_cls = openenoc_endpoint_interface_info_neg_0x639a39012e010981_cls(
                                                                     address=self.address+0,
                                                                     logger_handle=logger_handle+'.info',
                                                                     inst_name='info', parent=self)
        self.__config:openenoc_endpoint_interface_config_0x5830be79b2944b61_cls = openenoc_endpoint_interface_config_0x5830be79b2944b61_cls(
                                                                                address=self.address+8,
                                                                                logger_handle=logger_handle+'.config',
                                                                                inst_name='config',
                                                                                parent=self)
        self.__axis_if:openenoc_endpoint_interface_axis_if_0x3feb390ce0f22f04_cls = openenoc_endpoint_interface_axis_if_0x3feb390ce0f22f04_cls(
                                                                                address=self.address+32,
                                                                                logger_handle=logger_handle+'.axis_if',
                                                                                inst_name='axis_if',
                                                                                parent=self)
        self.__peers:openenoc_endpoint_interface_peers_0x39d7a117c0591cca_cls = openenoc_endpoint_interface_peers_0x39d7a117c0591cca_cls(
                                                                                address=self.address+128,
                                                                                logger_handle=logger_handle+'.peers',
                                                                                inst_name='peers',
                                                                                parent=self)
        self.__rmem:openenoc_endpoint_interface_rmem_0x78bf74252298273c_cls = openenoc_endpoint_interface_rmem_0x78bf74252298273c_cls(
                                                                                address=self.address+1024,
                                                                                logger_handle=logger_handle+'.rmem',
                                                                                inst_name='rmem',
                                                                                parent=self)
        

    @property
    def size(self) -> int:
        return 2048

    # properties for Register and RegisterFiles
    @property
    def info(self) -> 'openenoc_endpoint_interface_info_neg_0x639a39012e010981_cls':
        """
        Property to access info 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.info                                        |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Read-only information register for this openENOC Endpoint       |
        |              |      Interface instance.</p>                                            |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__info
    
    @property
    def config(self) -> 'openenoc_endpoint_interface_config_0x5830be79b2944b61_cls':
        """
        Property to access config 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.config                                      |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Configuration register file for this openENOC Endpoint          |
        |              |      Interface instance.</p>                                            |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__config
    
    @property
    def axis_if(self) -> 'openenoc_endpoint_interface_axis_if_0x3feb390ce0f22f04_cls':
        """
        Property to access axis_if 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.axis_if                                     |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Register file for the AXI4-Stream source and sink               |
        |              |      interfaces.</p>                                                    |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__axis_if
    
    @property
    def peers(self) -> 'openenoc_endpoint_interface_peers_0x39d7a117c0591cca_cls':
        """
        Property to access peers 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.peers                                       |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Register file for remote peer configuration and memory region   |
        |              |      information.</p>                                                   |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__peers
    
    @property
    def rmem(self) -> 'openenoc_endpoint_interface_rmem_0x78bf74252298273c_cls':
        """
        Property to access rmem 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.rmem                                        |
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
    def get_child_by_system_rdl_name(self, name: Literal["info"]) -> 'openenoc_endpoint_interface_info_neg_0x639a39012e010981_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["config"]) -> 'openenoc_endpoint_interface_config_0x5830be79b2944b61_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["axis_if"]) -> 'openenoc_endpoint_interface_axis_if_0x3feb390ce0f22f04_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["peers"]) -> 'openenoc_endpoint_interface_peers_0x39d7a117c0591cca_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["rmem"]) -> 'openenoc_endpoint_interface_rmem_0x78bf74252298273c_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_interface_info_neg_0x639a39012e010981_cls', 'openenoc_endpoint_interface_config_0x5830be79b2944b61_cls', 'openenoc_endpoint_interface_axis_if_0x3feb390ce0f22f04_cls', 'openenoc_endpoint_interface_peers_0x39d7a117c0591cca_cls', 'openenoc_endpoint_interface_rmem_0x78bf74252298273c_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface"
    @property
    def rdl_desc(self) -> str:
        return "Control and status register file for an openENOC Endpoint Interface instance."
    
    

    
    def __iter__(self) -> Iterator[Union[Node, NodeArray]]:
        
        
        yield self.info
        yield self.config
        yield self.axis_if
        yield self.peers
        yield self.rmem
        
        
    

    
    
class csr_neg_0x658d35c98f120733_cls(AddressMap):
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
    |              |      <p>openENOC Full Endpoint CSR</p>                                  |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__test_reg', '__regB', '__endpoint_interface', '__switch_interface']

    def __init__(self, *,
                 address:int=0,
                 logger_handle:str='reg_model.csr',
                 inst_name:str='csr',
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

        
            
        self.__test_reg:csr_test_reg_neg_0x1bed016ad15a95ef_cls = csr_test_reg_neg_0x1bed016ad15a95ef_cls(
                                                                     address=self.address+0,
                                                                     logger_handle=logger_handle+'.test_reg',
                                                                     inst_name='test_reg', parent=self)
        
            
        self.__regB:csr_regB_neg_0x6309110ed09171fa_cls = csr_regB_neg_0x6309110ed09171fa_cls(
                                                                     address=self.address+4,
                                                                     logger_handle=logger_handle+'.regB',
                                                                     inst_name='regB', parent=self)
        self.__endpoint_interface:openenoc_endpoint_interface_neg_0x6aed29be915be9f_cls = openenoc_endpoint_interface_neg_0x6aed29be915be9f_cls(
                                                                                address=self.address+2048,
                                                                                logger_handle=logger_handle+'.endpoint_interface',
                                                                                inst_name='endpoint_interface',
                                                                                parent=self)
        self.__switch_interface:openenoc_switch_interface_0x11366b9728f55963_cls = openenoc_switch_interface_0x11366b9728f55963_cls(
                                                                                address=self.address+4096,
                                                                                logger_handle=logger_handle+'.switch_interface',
                                                                                inst_name='switch_interface',
                                                                                parent=self)
        

    @property
    def size(self) -> int:
        return 4352
    @property
    def test_reg(self) -> 'csr_test_reg_neg_0x1bed016ad15a95ef_cls':
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
    def regB(self) -> 'csr_regB_neg_0x6309110ed09171fa_cls':
        """
        Property to access regB 

        
        """
        return self.__regB
        
    @property
    def endpoint_interface(self) -> 'openenoc_endpoint_interface_neg_0x6aed29be915be9f_cls':
        """
        Property to access endpoint_interface 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface                                             |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Control and status register file for an openENOC Endpoint       |
        |              |      Interface instance.</p>                                            |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__endpoint_interface
        
    @property
    def switch_interface(self) -> 'openenoc_switch_interface_0x11366b9728f55963_cls':
        """
        Property to access switch_interface 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.switch_interface                                               |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Control and status register file for an openENOC Switch         |
        |              |      instance. It includes configuration registers and a forwarding     |
        |              |      table used to map destination MAC address keys to output interface |
        |              |      selections for frame forwarding.</p>                               |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__switch_interface
        

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'test_reg':'test_reg','regB':'regB','endpoint_interface':'endpoint_interface','switch_interface':'switch_interface',
            }

    
    
    
    
    
    
    # nodes:4
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["test_reg"]) -> 'csr_test_reg_neg_0x1bed016ad15a95ef_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["regB"]) -> 'csr_regB_neg_0x6309110ed09171fa_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["endpoint_interface"]) -> 'openenoc_endpoint_interface_neg_0x6aed29be915be9f_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["switch_interface"]) -> 'openenoc_switch_interface_0x11366b9728f55963_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['csr_test_reg_neg_0x1bed016ad15a95ef_cls', 'csr_regB_neg_0x6309110ed09171fa_cls', 'openenoc_endpoint_interface_neg_0x6aed29be915be9f_cls', 'openenoc_switch_interface_0x11366b9728f55963_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr"
    @property
    def rdl_desc(self) -> str:
        return "openENOC Full Endpoint CSR"
    
    

    
    def __iter__(self) -> Iterator[Union[Node, NodeArray]]:
        
        
        yield self.test_reg
        yield self.regB
        yield self.endpoint_interface
        yield self.switch_interface
        
        
    


csr_cls = csr_neg_0x658d35c98f120733_cls

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
    csr = csr_cls(callbacks = NormalCallbackSet(read_callback=read_addr_space,
                                                                                                     write_callback=write_addr_space))