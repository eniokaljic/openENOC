


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





from ._registers import csr_test_reg_neg_0x59127c6cf49571bc_cls
from ._registers import csr_regB_0x147bcdd77ddbf689_cls
from ._registers import openenoc_endpoint_interface_info_neg_0x769d3cada650b261_cls
from ._registers import openenoc_endpoint_interface_conf_mac_address_neg_0x79fb2b98c7d7201_cls
from ._registers import openenoc_endpoint_interface_conf_multicast_address_0xfe1435096c263d9_cls
from ._registers import openenoc_endpoint_interface_conf_non_oetp_control_neg_0x2996e2b07396a6a9_cls
from ._registers import openenoc_endpoint_interface_conf_rmem_timeout_neg_0x5a12504165c33716_cls
from ._registers import openenoc_endpoint_interface_conf_dma_timeout_neg_0x7ac586385b822cfd_cls
from ._registers import openenoc_endpoint_interface_conf_dma_max_fragment_size_neg_0x18d59c5f2d2d3078_cls
from ._registers import openenoc_endpoint_interface_axis_if_source_data_neg_0x21a62fa3df170803_cls
from ._registers import openenoc_endpoint_interface_axis_if_source_control_0x2ea2e4307e00845f_cls
from ._registers import openenoc_endpoint_interface_axis_if_source_status_0x5c619194de268f36_cls
from ._registers import openenoc_endpoint_interface_axis_if_sink_data_neg_0x19eaadd079c52b59_cls
from ._registers import openenoc_endpoint_interface_axis_if_sink_control_neg_0x3273764231c7691f_cls
from ._registers import openenoc_endpoint_interface_axis_if_sink_status_neg_0x170190c5e3b7dc0c_cls
from ._registers import openenoc_endpoint_interface_non_oetp_dma_tx_buffer_address_0x769c505757b68c76_cls
from ._registers import openenoc_endpoint_interface_non_oetp_dma_tx_frame_length_0x6d2b17830360c61e_cls
from ._registers import openenoc_endpoint_interface_non_oetp_dma_tx_command_status_0x7da5c32c9353e31c_cls
from ._registers import openenoc_endpoint_interface_non_oetp_dma_tx_transferred_length_neg_0x6d472440e4e4572b_cls
from ._registers import openenoc_endpoint_interface_non_oetp_dma_rx_buffer_address_neg_0x5fe36cfa037d6ea5_cls
from ._registers import openenoc_endpoint_interface_non_oetp_dma_rx_buffer_capacity_neg_0x50cf50b33c5a15fc_cls
from ._registers import openenoc_endpoint_interface_non_oetp_dma_rx_command_status_neg_0x3be8f98bc8406af1_cls
from ._registers import openenoc_endpoint_interface_non_oetp_dma_rx_received_length_0x7f947a0030fbc7b_cls
from ._registers import openenoc_endpoint_interface_irq_control_0x770fdd547c88efb3_cls
from ._registers import openenoc_endpoint_interface_irq_event_enable_0x705b22be2d4d68e6_cls
from ._registers import openenoc_endpoint_interface_irq_status_0x6debda9a601f9021_cls
from ._registers import openenoc_endpoint_interface_irq_claim_0x5e7cfa60428210a9_cls
from ._registers import openenoc_endpoint_interface_irq_complete_0x5966f8302b565a38_cls
from ._registers import openenoc_endpoint_interface_peers_entry_mac_address_0x21514b5db0ad0415_cls
from ._registers import openenoc_endpoint_interface_peers_entry_rmem_address_0x53c2ba4ffa148189_cls
from ._registers import openenoc_endpoint_interface_peers_entry_local_address_neg_0x7d40786a57efb0f3_cls
from ._registers import openenoc_endpoint_interface_peers_entry_remote_address_neg_0x1c2f4013216daeea_cls
from ._registers import openenoc_endpoint_interface_peers_entry_size_neg_0xc0a3115aa0ea53d_cls
from ._registers import openenoc_endpoint_interface_peers_entry_dma_neg_0x597d7667b00ae5fa_cls
from ._registers import openenoc_endpoint_interface_rmem_word_neg_0x7df0052261c0a6de_cls_array
from ._registers import openenoc_switch_interface_info_0x29edc06c10667378_cls
from ._registers import openenoc_switch_interface_forwarding_control_neg_0x623c0ec468557587_cls
from ._registers import openenoc_switch_interface_default_forwarding_neg_0x7d3ce32048c07ec5_cls
from ._registers import openenoc_switch_interface_forwarding_table_entry_mac_address_neg_0x4397c7d74f8fae49_cls
from ._registers import openenoc_switch_interface_forwarding_table_entry_iface_neg_0x583d5b51e8f15589_cls
from ._registers import openenoc_switch_interface_forwarding_table_entry_conf_0x1fce6111b15337_cls


# addrmap, regfile, memor and register definitions
    
    
class openenoc_switch_interface_forwarding_table_entry_0x54b994fc2cafb7ea_cls(RegFile):
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

    __slots__ : list[str] = ['__mac_address', '__iface', '__conf']

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
        
            
        self.__mac_address:openenoc_switch_interface_forwarding_table_entry_mac_address_neg_0x4397c7d74f8fae49_cls = openenoc_switch_interface_forwarding_table_entry_mac_address_neg_0x4397c7d74f8fae49_cls(
                                                                     address=self.address+0,
                                                                     logger_handle=logger_handle+'.mac_address',
                                                                     inst_name='mac_address', parent=self)
        
            
        self.__iface:openenoc_switch_interface_forwarding_table_entry_iface_neg_0x583d5b51e8f15589_cls = openenoc_switch_interface_forwarding_table_entry_iface_neg_0x583d5b51e8f15589_cls(
                                                                     address=self.address+8,
                                                                     logger_handle=logger_handle+'.iface',
                                                                     inst_name='iface', parent=self)
        
            
        self.__conf:openenoc_switch_interface_forwarding_table_entry_conf_0x1fce6111b15337_cls = openenoc_switch_interface_forwarding_table_entry_conf_0x1fce6111b15337_cls(
                                                                     address=self.address+12,
                                                                     logger_handle=logger_handle+'.conf',
                                                                     inst_name='conf', parent=self)
        

    @property
    def size(self) -> int:
        return 16

    # properties for Register and RegisterFiles
    @property
    def mac_address(self) -> 'openenoc_switch_interface_forwarding_table_entry_mac_address_neg_0x4397c7d74f8fae49_cls':
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
    def iface(self) -> 'openenoc_switch_interface_forwarding_table_entry_iface_neg_0x583d5b51e8f15589_cls':
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
    def conf(self) -> 'openenoc_switch_interface_forwarding_table_entry_conf_0x1fce6111b15337_cls':
        """
        Property to access conf 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].conf |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Configuration information associated with this forwarding table |
        |              |      entry.</p>                                                         |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__conf
    

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'mac_address':'mac_address','iface':'iface','conf':'conf',
            }

    
    
    
    
    
    
    # nodes:3
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["mac_address"]) -> 'openenoc_switch_interface_forwarding_table_entry_mac_address_neg_0x4397c7d74f8fae49_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["iface"]) -> 'openenoc_switch_interface_forwarding_table_entry_iface_neg_0x583d5b51e8f15589_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["conf"]) -> 'openenoc_switch_interface_forwarding_table_entry_conf_0x1fce6111b15337_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_switch_interface_forwarding_table_entry_mac_address_neg_0x4397c7d74f8fae49_cls', 'openenoc_switch_interface_forwarding_table_entry_iface_neg_0x583d5b51e8f15589_cls', 'openenoc_switch_interface_forwarding_table_entry_conf_0x1fce6111b15337_cls', ]: ...

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
        yield self.conf
        
        
class openenoc_switch_interface_forwarding_table_entry_0x54b994fc2cafb7ea_cls_array(RegFileArray):
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
        return openenoc_switch_interface_forwarding_table_entry_0x54b994fc2cafb7ea_cls
    

    
    
class openenoc_switch_interface_forwarding_table_neg_0x6a4dd06f2957a659_cls(RegFile):
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
        
        self.__entry:openenoc_switch_interface_forwarding_table_entry_0x54b994fc2cafb7ea_cls_array = openenoc_switch_interface_forwarding_table_entry_0x54b994fc2cafb7ea_cls_array(address=self.address+0,
                                                                                      stride=16,
                                                                                      dimensions=tuple([8]),
                                                                                      logger_handle=logger_handle+'.entry',
                                                                                      inst_name='entry', parent=self)
        

    @property
    def size(self) -> int:
        return 128

    # properties for Register and RegisterFiles
    @property
    def entry(self) -> 'openenoc_switch_interface_forwarding_table_entry_0x54b994fc2cafb7ea_cls_array':
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

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_switch_interface_forwarding_table_entry_0x54b994fc2cafb7ea_cls_array':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.switch_interface.forwarding_table"
    @property
    def rdl_desc(self) -> str:
        return "Forwarding table used to map MAC addresses to output interface selections for frame forwarding."
    
    

    
    def __iter__(self) -> Iterator[Union[Node, NodeArray]]:
        
        
        yield self.entry
        
        
    

    
    
class openenoc_switch_interface_neg_0x6bd0310ca632c708_cls(RegFile):
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
        
            
        self.__info:openenoc_switch_interface_info_0x29edc06c10667378_cls = openenoc_switch_interface_info_0x29edc06c10667378_cls(
                                                                     address=self.address+0,
                                                                     logger_handle=logger_handle+'.info',
                                                                     inst_name='info', parent=self)
        
            
        self.__forwarding_control:openenoc_switch_interface_forwarding_control_neg_0x623c0ec468557587_cls = openenoc_switch_interface_forwarding_control_neg_0x623c0ec468557587_cls(
                                                                     address=self.address+4,
                                                                     logger_handle=logger_handle+'.forwarding_control',
                                                                     inst_name='forwarding_control', parent=self)
        
            
        self.__default_forwarding:openenoc_switch_interface_default_forwarding_neg_0x7d3ce32048c07ec5_cls = openenoc_switch_interface_default_forwarding_neg_0x7d3ce32048c07ec5_cls(
                                                                     address=self.address+8,
                                                                     logger_handle=logger_handle+'.default_forwarding',
                                                                     inst_name='default_forwarding', parent=self)
        self.__forwarding_table:openenoc_switch_interface_forwarding_table_neg_0x6a4dd06f2957a659_cls = openenoc_switch_interface_forwarding_table_neg_0x6a4dd06f2957a659_cls(
                                                                                address=self.address+128,
                                                                                logger_handle=logger_handle+'.forwarding_table',
                                                                                inst_name='forwarding_table',
                                                                                parent=self)
        

    @property
    def size(self) -> int:
        return 256

    # properties for Register and RegisterFiles
    @property
    def info(self) -> 'openenoc_switch_interface_info_0x29edc06c10667378_cls':
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
    def forwarding_control(self) -> 'openenoc_switch_interface_forwarding_control_neg_0x623c0ec468557587_cls':
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
    def default_forwarding(self) -> 'openenoc_switch_interface_default_forwarding_neg_0x7d3ce32048c07ec5_cls':
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
    def forwarding_table(self) -> 'openenoc_switch_interface_forwarding_table_neg_0x6a4dd06f2957a659_cls':
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
    def get_child_by_system_rdl_name(self, name: Literal["info"]) -> 'openenoc_switch_interface_info_0x29edc06c10667378_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["forwarding_control"]) -> 'openenoc_switch_interface_forwarding_control_neg_0x623c0ec468557587_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["default_forwarding"]) -> 'openenoc_switch_interface_default_forwarding_neg_0x7d3ce32048c07ec5_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["forwarding_table"]) -> 'openenoc_switch_interface_forwarding_table_neg_0x6a4dd06f2957a659_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_switch_interface_info_0x29edc06c10667378_cls', 'openenoc_switch_interface_forwarding_control_neg_0x623c0ec468557587_cls', 'openenoc_switch_interface_default_forwarding_neg_0x7d3ce32048c07ec5_cls', 'openenoc_switch_interface_forwarding_table_neg_0x6a4dd06f2957a659_cls', ]: ...

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
        
        
    

    
    
class openenoc_endpoint_interface_rmem_0x45d94b2b2b16d3f_cls(RegFile):
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
        
            
        self.__word:openenoc_endpoint_interface_rmem_word_neg_0x7df0052261c0a6de_cls_array = openenoc_endpoint_interface_rmem_word_neg_0x7df0052261c0a6de_cls_array(address=self.address+0,
                                                                                      stride=4,
                                                                                      dimensions=tuple([256]),
                                                                                      logger_handle=logger_handle+'.word',
                                                                                      inst_name='word', parent=self)
        

    @property
    def size(self) -> int:
        return 1024

    # properties for Register and RegisterFiles
    @property
    def word(self) -> 'openenoc_endpoint_interface_rmem_word_neg_0x7df0052261c0a6de_cls_array':
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

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_interface_rmem_word_neg_0x7df0052261c0a6de_cls_array':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.rmem"
    @property
    def rdl_desc(self) -> str:
        return "Virtual memory region for all remote peers, with offsets and sizes defined in the\npeers regfile."
    
    

    
    def __iter__(self) -> Iterator[Union[Node, NodeArray]]:
        
        
        yield self.word
        
        
    

    
    
class openenoc_endpoint_interface_peers_entry_0x2e080e1b5b77e305_cls(RegFile):
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
        
            
        self.__mac_address:openenoc_endpoint_interface_peers_entry_mac_address_0x21514b5db0ad0415_cls = openenoc_endpoint_interface_peers_entry_mac_address_0x21514b5db0ad0415_cls(
                                                                     address=self.address+0,
                                                                     logger_handle=logger_handle+'.mac_address',
                                                                     inst_name='mac_address', parent=self)
        
            
        self.__rmem_address:openenoc_endpoint_interface_peers_entry_rmem_address_0x53c2ba4ffa148189_cls = openenoc_endpoint_interface_peers_entry_rmem_address_0x53c2ba4ffa148189_cls(
                                                                     address=self.address+8,
                                                                     logger_handle=logger_handle+'.rmem_address',
                                                                     inst_name='rmem_address', parent=self)
        
            
        self.__local_address:openenoc_endpoint_interface_peers_entry_local_address_neg_0x7d40786a57efb0f3_cls = openenoc_endpoint_interface_peers_entry_local_address_neg_0x7d40786a57efb0f3_cls(
                                                                     address=self.address+12,
                                                                     logger_handle=logger_handle+'.local_address',
                                                                     inst_name='local_address', parent=self)
        
            
        self.__remote_address:openenoc_endpoint_interface_peers_entry_remote_address_neg_0x1c2f4013216daeea_cls = openenoc_endpoint_interface_peers_entry_remote_address_neg_0x1c2f4013216daeea_cls(
                                                                     address=self.address+16,
                                                                     logger_handle=logger_handle+'.remote_address',
                                                                     inst_name='remote_address', parent=self)
        
            
        self.__size:openenoc_endpoint_interface_peers_entry_size_neg_0xc0a3115aa0ea53d_cls = openenoc_endpoint_interface_peers_entry_size_neg_0xc0a3115aa0ea53d_cls(
                                                                     address=self.address+20,
                                                                     logger_handle=logger_handle+'.size',
                                                                     inst_name='size', parent=self)
        
            
        self.__dma:openenoc_endpoint_interface_peers_entry_dma_neg_0x597d7667b00ae5fa_cls = openenoc_endpoint_interface_peers_entry_dma_neg_0x597d7667b00ae5fa_cls(
                                                                     address=self.address+24,
                                                                     logger_handle=logger_handle+'.dma',
                                                                     inst_name='dma', parent=self)
        

    @property
    def size(self) -> int:
        return 28

    # properties for Register and RegisterFiles
    @property
    def mac_address(self) -> 'openenoc_endpoint_interface_peers_entry_mac_address_0x21514b5db0ad0415_cls':
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
    def rmem_address(self) -> 'openenoc_endpoint_interface_peers_entry_rmem_address_0x53c2ba4ffa148189_cls':
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
    def local_address(self) -> 'openenoc_endpoint_interface_peers_entry_local_address_neg_0x7d40786a57efb0f3_cls':
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
    def remote_address(self) -> 'openenoc_endpoint_interface_peers_entry_remote_address_neg_0x1c2f4013216daeea_cls':
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
    def register_size(self) -> 'openenoc_endpoint_interface_peers_entry_size_neg_0xc0a3115aa0ea53d_cls':
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
    def dma(self) -> 'openenoc_endpoint_interface_peers_entry_dma_neg_0x597d7667b00ae5fa_cls':
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
        |              |      <p>DMA/RMEM configuration and control for the remote peer, with    |
        |              |      shared sticky error reporting. RMEM and bulk DMA retain separate   |
        |              |      IRQ event classes.</p>                                             |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__dma
    

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'mac_address':'mac_address','rmem_address':'rmem_address','local_address':'local_address','remote_address':'remote_address','size':'register_size','dma':'dma',
            }

    
    
    
    
    
    
    # nodes:6
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["mac_address"]) -> 'openenoc_endpoint_interface_peers_entry_mac_address_0x21514b5db0ad0415_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["rmem_address"]) -> 'openenoc_endpoint_interface_peers_entry_rmem_address_0x53c2ba4ffa148189_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["local_address"]) -> 'openenoc_endpoint_interface_peers_entry_local_address_neg_0x7d40786a57efb0f3_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["remote_address"]) -> 'openenoc_endpoint_interface_peers_entry_remote_address_neg_0x1c2f4013216daeea_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["size"]) -> 'openenoc_endpoint_interface_peers_entry_size_neg_0xc0a3115aa0ea53d_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["dma"]) -> 'openenoc_endpoint_interface_peers_entry_dma_neg_0x597d7667b00ae5fa_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_interface_peers_entry_mac_address_0x21514b5db0ad0415_cls', 'openenoc_endpoint_interface_peers_entry_rmem_address_0x53c2ba4ffa148189_cls', 'openenoc_endpoint_interface_peers_entry_local_address_neg_0x7d40786a57efb0f3_cls', 'openenoc_endpoint_interface_peers_entry_remote_address_neg_0x1c2f4013216daeea_cls', 'openenoc_endpoint_interface_peers_entry_size_neg_0xc0a3115aa0ea53d_cls', 'openenoc_endpoint_interface_peers_entry_dma_neg_0x597d7667b00ae5fa_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1]"
    @property
    def rdl_desc(self) -> str:
        return "Register file for a single remote peer configuration and memory region\ninformation."
    
    

    
    def __iter__(self) -> Iterator[Union[Node, NodeArray]]:
        
        
        yield self.mac_address
        yield self.rmem_address
        yield self.local_address
        yield self.remote_address
        yield self.register_size
        yield self.dma
        
        
class openenoc_endpoint_interface_peers_entry_0x2e080e1b5b77e305_cls_array(RegFileArray):
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
        return openenoc_endpoint_interface_peers_entry_0x2e080e1b5b77e305_cls
    

    
    
class openenoc_endpoint_interface_peers_0x2a8405b29020d2ad_cls(RegFile):
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
        
        self.__entry:openenoc_endpoint_interface_peers_entry_0x2e080e1b5b77e305_cls_array = openenoc_endpoint_interface_peers_entry_0x2e080e1b5b77e305_cls_array(address=self.address+0,
                                                                                      stride=28,
                                                                                      dimensions=tuple([4]),
                                                                                      logger_handle=logger_handle+'.entry',
                                                                                      inst_name='entry', parent=self)
        

    @property
    def size(self) -> int:
        return 112

    # properties for Register and RegisterFiles
    @property
    def entry(self) -> 'openenoc_endpoint_interface_peers_entry_0x2e080e1b5b77e305_cls_array':
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

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_interface_peers_entry_0x2e080e1b5b77e305_cls_array':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.peers"
    @property
    def rdl_desc(self) -> str:
        return "Register file for remote peer configuration and memory region information."
    
    

    
    def __iter__(self) -> Iterator[Union[Node, NodeArray]]:
        
        
        yield self.entry
        
        
    

    
    
class openenoc_endpoint_interface_irq_0x10abdd179744b18a_cls(RegFile):
    """
    Class to represent a register file in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.irq                                         |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Endpoint-level interrupt control and claim interface. Interrupt |
    |              |      events from peer DMA, non-oETP DMA, direct AXI4-Stream transfers,  |
    |              |      and RMEM failures are serialized through a shared event FIFO.</p>  |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__control', '__event_enable', '__status', '__claim', '__complete']

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
        
            
        self.__control:openenoc_endpoint_interface_irq_control_0x770fdd547c88efb3_cls = openenoc_endpoint_interface_irq_control_0x770fdd547c88efb3_cls(
                                                                     address=self.address+0,
                                                                     logger_handle=logger_handle+'.control',
                                                                     inst_name='control', parent=self)
        
            
        self.__event_enable:openenoc_endpoint_interface_irq_event_enable_0x705b22be2d4d68e6_cls = openenoc_endpoint_interface_irq_event_enable_0x705b22be2d4d68e6_cls(
                                                                     address=self.address+4,
                                                                     logger_handle=logger_handle+'.event_enable',
                                                                     inst_name='event_enable', parent=self)
        
            
        self.__status:openenoc_endpoint_interface_irq_status_0x6debda9a601f9021_cls = openenoc_endpoint_interface_irq_status_0x6debda9a601f9021_cls(
                                                                     address=self.address+8,
                                                                     logger_handle=logger_handle+'.status',
                                                                     inst_name='status', parent=self)
        
            
        self.__claim:openenoc_endpoint_interface_irq_claim_0x5e7cfa60428210a9_cls = openenoc_endpoint_interface_irq_claim_0x5e7cfa60428210a9_cls(
                                                                     address=self.address+12,
                                                                     logger_handle=logger_handle+'.claim',
                                                                     inst_name='claim', parent=self)
        
            
        self.__complete:openenoc_endpoint_interface_irq_complete_0x5966f8302b565a38_cls = openenoc_endpoint_interface_irq_complete_0x5966f8302b565a38_cls(
                                                                     address=self.address+16,
                                                                     logger_handle=logger_handle+'.complete',
                                                                     inst_name='complete', parent=self)
        

    @property
    def size(self) -> int:
        return 20

    # properties for Register and RegisterFiles
    @property
    def control(self) -> 'openenoc_endpoint_interface_irq_control_0x770fdd547c88efb3_cls':
        """
        Property to access control 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.irq.control                                 |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Global interrupt-output control and interrupt-controller        |
        |              |      maintenance requests.</p>                                          |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__control
    
    @property
    def event_enable(self) -> 'openenoc_endpoint_interface_irq_event_enable_0x705b22be2d4d68e6_cls':
        """
        Property to access event_enable 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.irq.event_enable                            |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Enables generation of individual endpoint IRQ event classes.    |
        |              |      These fields control event capture; irq.control.global_enable only |
        |              |      masks the physical IRQ output.</p>                                 |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__event_enable
    
    @property
    def status(self) -> 'openenoc_endpoint_interface_irq_status_0x6debda9a601f9021_cls':
        """
        Property to access status 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.irq.status                                  |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Status of the endpoint IRQ event FIFO and its reservation       |
        |              |      mechanism.</p>                                                     |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__status
    
    @property
    def claim(self) -> 'openenoc_endpoint_interface_irq_claim_0x5e7cfa60428210a9_cls':
        """
        Property to access claim 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.irq.claim                                   |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Read-only view of the event at the head of the IRQ event FIFO.  |
        |              |      Reading this register has no side effect, and all fields remain    |
        |              |      stable until a matching irq.complete request removes the           |
        |              |      claim.</p>                                                         |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__claim
    
    @property
    def complete(self) -> 'openenoc_endpoint_interface_irq_complete_0x5966f8302b565a38_cls':
        """
        Property to access complete 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.irq.complete                                |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Completion request for the current IRQ claim. Software          |
        |              |      acknowledges an event by copying the complete 32-bit irq.claim     |
        |              |      value into this register.</p>                                      |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__complete
    

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'control':'control','event_enable':'event_enable','status':'status','claim':'claim','complete':'complete',
            }

    
    
    
    
    
    
    # nodes:5
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["control"]) -> 'openenoc_endpoint_interface_irq_control_0x770fdd547c88efb3_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["event_enable"]) -> 'openenoc_endpoint_interface_irq_event_enable_0x705b22be2d4d68e6_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["status"]) -> 'openenoc_endpoint_interface_irq_status_0x6debda9a601f9021_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["claim"]) -> 'openenoc_endpoint_interface_irq_claim_0x5e7cfa60428210a9_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["complete"]) -> 'openenoc_endpoint_interface_irq_complete_0x5966f8302b565a38_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_interface_irq_control_0x770fdd547c88efb3_cls', 'openenoc_endpoint_interface_irq_event_enable_0x705b22be2d4d68e6_cls', 'openenoc_endpoint_interface_irq_status_0x6debda9a601f9021_cls', 'openenoc_endpoint_interface_irq_claim_0x5e7cfa60428210a9_cls', 'openenoc_endpoint_interface_irq_complete_0x5966f8302b565a38_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.irq"
    @property
    def rdl_desc(self) -> str:
        return "Endpoint-level interrupt control and claim interface. Interrupt events from peer\nDMA, non-oETP DMA, direct AXI4-Stream transfers, and RMEM failures are serialized\nthrough a shared event FIFO."
    
    

    
    def __iter__(self) -> Iterator[Union[Node, NodeArray]]:
        
        
        yield self.control
        yield self.event_enable
        yield self.status
        yield self.claim
        yield self.complete
        
        
    

    
    
class openenoc_endpoint_interface_non_oetp_dma_rx_neg_0x2a972117692b39c8_cls(RegFile):
    """
    Class to represent a register file in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.non_oetp_dma.rx                             |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Receive DMA channel for complete non-oETP Ethernet frames.</p>  |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__buffer_address', '__buffer_capacity', '__command_status', '__received_length']

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
        
            
        self.__buffer_address:openenoc_endpoint_interface_non_oetp_dma_rx_buffer_address_neg_0x5fe36cfa037d6ea5_cls = openenoc_endpoint_interface_non_oetp_dma_rx_buffer_address_neg_0x5fe36cfa037d6ea5_cls(
                                                                     address=self.address+0,
                                                                     logger_handle=logger_handle+'.buffer_address',
                                                                     inst_name='buffer_address', parent=self)
        
            
        self.__buffer_capacity:openenoc_endpoint_interface_non_oetp_dma_rx_buffer_capacity_neg_0x50cf50b33c5a15fc_cls = openenoc_endpoint_interface_non_oetp_dma_rx_buffer_capacity_neg_0x50cf50b33c5a15fc_cls(
                                                                     address=self.address+4,
                                                                     logger_handle=logger_handle+'.buffer_capacity',
                                                                     inst_name='buffer_capacity', parent=self)
        
            
        self.__command_status:openenoc_endpoint_interface_non_oetp_dma_rx_command_status_neg_0x3be8f98bc8406af1_cls = openenoc_endpoint_interface_non_oetp_dma_rx_command_status_neg_0x3be8f98bc8406af1_cls(
                                                                     address=self.address+8,
                                                                     logger_handle=logger_handle+'.command_status',
                                                                     inst_name='command_status', parent=self)
        
            
        self.__received_length:openenoc_endpoint_interface_non_oetp_dma_rx_received_length_0x7f947a0030fbc7b_cls = openenoc_endpoint_interface_non_oetp_dma_rx_received_length_0x7f947a0030fbc7b_cls(
                                                                     address=self.address+12,
                                                                     logger_handle=logger_handle+'.received_length',
                                                                     inst_name='received_length', parent=self)
        

    @property
    def size(self) -> int:
        return 16

    # properties for Register and RegisterFiles
    @property
    def buffer_address(self) -> 'openenoc_endpoint_interface_non_oetp_dma_rx_buffer_address_neg_0x5fe36cfa037d6ea5_cls':
        """
        Property to access buffer_address 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.non_oetp_dma.rx.buffer_address              |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Local memory address of the receive buffer for a non-oETP       |
        |              |      Ethernet frame.</p>                                                |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__buffer_address
    
    @property
    def buffer_capacity(self) -> 'openenoc_endpoint_interface_non_oetp_dma_rx_buffer_capacity_neg_0x50cf50b33c5a15fc_cls':
        """
        Property to access buffer_capacity 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.non_oetp_dma.rx.buffer_capacity             |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Capacity of the receive buffer for one complete non-oETP        |
        |              |      Ethernet frame.</p>                                                |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__buffer_capacity
    
    @property
    def command_status(self) -> 'openenoc_endpoint_interface_non_oetp_dma_rx_command_status_neg_0x3be8f98bc8406af1_cls':
        """
        Property to access command_status 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.non_oetp_dma.rx.command_status              |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Command and completion status for the non-oETP receive DMA      |
        |              |      channel.</p>                                                       |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__command_status
    
    @property
    def received_length(self) -> 'openenoc_endpoint_interface_non_oetp_dma_rx_received_length_0x7f947a0030fbc7b_cls':
        """
        Property to access received_length 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.non_oetp_dma.rx.received_length             |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Length of the most recently received non-oETP Ethernet          |
        |              |      frame.</p>                                                         |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__received_length
    

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'buffer_address':'buffer_address','buffer_capacity':'buffer_capacity','command_status':'command_status','received_length':'received_length',
            }

    
    
    
    
    
    
    # nodes:4
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["buffer_address"]) -> 'openenoc_endpoint_interface_non_oetp_dma_rx_buffer_address_neg_0x5fe36cfa037d6ea5_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["buffer_capacity"]) -> 'openenoc_endpoint_interface_non_oetp_dma_rx_buffer_capacity_neg_0x50cf50b33c5a15fc_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["command_status"]) -> 'openenoc_endpoint_interface_non_oetp_dma_rx_command_status_neg_0x3be8f98bc8406af1_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["received_length"]) -> 'openenoc_endpoint_interface_non_oetp_dma_rx_received_length_0x7f947a0030fbc7b_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_interface_non_oetp_dma_rx_buffer_address_neg_0x5fe36cfa037d6ea5_cls', 'openenoc_endpoint_interface_non_oetp_dma_rx_buffer_capacity_neg_0x50cf50b33c5a15fc_cls', 'openenoc_endpoint_interface_non_oetp_dma_rx_command_status_neg_0x3be8f98bc8406af1_cls', 'openenoc_endpoint_interface_non_oetp_dma_rx_received_length_0x7f947a0030fbc7b_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.non_oetp_dma.rx"
    @property
    def rdl_desc(self) -> str:
        return "Receive DMA channel for complete non-oETP Ethernet frames."
    
    

    
    def __iter__(self) -> Iterator[Union[Node, NodeArray]]:
        
        
        yield self.buffer_address
        yield self.buffer_capacity
        yield self.command_status
        yield self.received_length
        
        
    

    
    
class openenoc_endpoint_interface_non_oetp_dma_tx_0x3b55de39a5c365e5_cls(RegFile):
    """
    Class to represent a register file in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.non_oetp_dma.tx                             |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Transmit DMA channel for complete non-oETP Ethernet frames.</p> |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__buffer_address', '__frame_length', '__command_status', '__transferred_length']

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
        
            
        self.__buffer_address:openenoc_endpoint_interface_non_oetp_dma_tx_buffer_address_0x769c505757b68c76_cls = openenoc_endpoint_interface_non_oetp_dma_tx_buffer_address_0x769c505757b68c76_cls(
                                                                     address=self.address+0,
                                                                     logger_handle=logger_handle+'.buffer_address',
                                                                     inst_name='buffer_address', parent=self)
        
            
        self.__frame_length:openenoc_endpoint_interface_non_oetp_dma_tx_frame_length_0x6d2b17830360c61e_cls = openenoc_endpoint_interface_non_oetp_dma_tx_frame_length_0x6d2b17830360c61e_cls(
                                                                     address=self.address+4,
                                                                     logger_handle=logger_handle+'.frame_length',
                                                                     inst_name='frame_length', parent=self)
        
            
        self.__command_status:openenoc_endpoint_interface_non_oetp_dma_tx_command_status_0x7da5c32c9353e31c_cls = openenoc_endpoint_interface_non_oetp_dma_tx_command_status_0x7da5c32c9353e31c_cls(
                                                                     address=self.address+8,
                                                                     logger_handle=logger_handle+'.command_status',
                                                                     inst_name='command_status', parent=self)
        
            
        self.__transferred_length:openenoc_endpoint_interface_non_oetp_dma_tx_transferred_length_neg_0x6d472440e4e4572b_cls = openenoc_endpoint_interface_non_oetp_dma_tx_transferred_length_neg_0x6d472440e4e4572b_cls(
                                                                     address=self.address+12,
                                                                     logger_handle=logger_handle+'.transferred_length',
                                                                     inst_name='transferred_length', parent=self)
        

    @property
    def size(self) -> int:
        return 16

    # properties for Register and RegisterFiles
    @property
    def buffer_address(self) -> 'openenoc_endpoint_interface_non_oetp_dma_tx_buffer_address_0x769c505757b68c76_cls':
        """
        Property to access buffer_address 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.non_oetp_dma.tx.buffer_address              |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Local memory address of the non-oETP Ethernet frame to          |
        |              |      transmit.</p>                                                      |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__buffer_address
    
    @property
    def frame_length(self) -> 'openenoc_endpoint_interface_non_oetp_dma_tx_frame_length_0x6d2b17830360c61e_cls':
        """
        Property to access frame_length 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.non_oetp_dma.tx.frame_length                |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Length of the complete non-oETP Ethernet frame to transmit.</p> |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__frame_length
    
    @property
    def command_status(self) -> 'openenoc_endpoint_interface_non_oetp_dma_tx_command_status_0x7da5c32c9353e31c_cls':
        """
        Property to access command_status 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.non_oetp_dma.tx.command_status              |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Command and completion status for the non-oETP transmit DMA     |
        |              |      channel.</p>                                                       |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__command_status
    
    @property
    def transferred_length(self) -> 'openenoc_endpoint_interface_non_oetp_dma_tx_transferred_length_neg_0x6d472440e4e4572b_cls':
        """
        Property to access transferred_length 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.non_oetp_dma.tx.transferred_length          |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Number of bytes transferred for the most recently accepted      |
        |              |      transmit request.</p>                                              |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__transferred_length
    

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'buffer_address':'buffer_address','frame_length':'frame_length','command_status':'command_status','transferred_length':'transferred_length',
            }

    
    
    
    
    
    
    # nodes:4
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["buffer_address"]) -> 'openenoc_endpoint_interface_non_oetp_dma_tx_buffer_address_0x769c505757b68c76_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["frame_length"]) -> 'openenoc_endpoint_interface_non_oetp_dma_tx_frame_length_0x6d2b17830360c61e_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["command_status"]) -> 'openenoc_endpoint_interface_non_oetp_dma_tx_command_status_0x7da5c32c9353e31c_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["transferred_length"]) -> 'openenoc_endpoint_interface_non_oetp_dma_tx_transferred_length_neg_0x6d472440e4e4572b_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_interface_non_oetp_dma_tx_buffer_address_0x769c505757b68c76_cls', 'openenoc_endpoint_interface_non_oetp_dma_tx_frame_length_0x6d2b17830360c61e_cls', 'openenoc_endpoint_interface_non_oetp_dma_tx_command_status_0x7da5c32c9353e31c_cls', 'openenoc_endpoint_interface_non_oetp_dma_tx_transferred_length_neg_0x6d472440e4e4572b_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.non_oetp_dma.tx"
    @property
    def rdl_desc(self) -> str:
        return "Transmit DMA channel for complete non-oETP Ethernet frames."
    
    

    
    def __iter__(self) -> Iterator[Union[Node, NodeArray]]:
        
        
        yield self.buffer_address
        yield self.frame_length
        yield self.command_status
        yield self.transferred_length
        
        
    

    
    
class openenoc_endpoint_interface_non_oetp_dma_neg_0x457dd3161aaaf0a0_cls(RegFile):
    """
    Class to represent a register file in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.non_oetp_dma                                |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Endpoint-level DMA control and status for complete non-oETP     |
    |              |      Ethernet frames. Frame data includes the Ethernet header and       |
    |              |      payload, but excludes the preamble, Start Frame Delimiter (SFD),   |
    |              |      and Frame Check Sequence (FCS).</p>                                |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__tx', '__rx']

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
        self.__tx:openenoc_endpoint_interface_non_oetp_dma_tx_0x3b55de39a5c365e5_cls = openenoc_endpoint_interface_non_oetp_dma_tx_0x3b55de39a5c365e5_cls(
                                                                                address=self.address+0,
                                                                                logger_handle=logger_handle+'.tx',
                                                                                inst_name='tx',
                                                                                parent=self)
        self.__rx:openenoc_endpoint_interface_non_oetp_dma_rx_neg_0x2a972117692b39c8_cls = openenoc_endpoint_interface_non_oetp_dma_rx_neg_0x2a972117692b39c8_cls(
                                                                                address=self.address+16,
                                                                                logger_handle=logger_handle+'.rx',
                                                                                inst_name='rx',
                                                                                parent=self)
        

    @property
    def size(self) -> int:
        return 32

    # properties for Register and RegisterFiles
    @property
    def tx(self) -> 'openenoc_endpoint_interface_non_oetp_dma_tx_0x3b55de39a5c365e5_cls':
        """
        Property to access tx 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.non_oetp_dma.tx                             |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Transmit DMA channel for complete non-oETP Ethernet frames.</p> |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__tx
    
    @property
    def rx(self) -> 'openenoc_endpoint_interface_non_oetp_dma_rx_neg_0x2a972117692b39c8_cls':
        """
        Property to access rx 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.non_oetp_dma.rx                             |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Receive DMA channel for complete non-oETP Ethernet frames.</p>  |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__rx
    

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'tx':'tx','rx':'rx',
            }

    
    
    
    
    
    
    # nodes:2
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["tx"]) -> 'openenoc_endpoint_interface_non_oetp_dma_tx_0x3b55de39a5c365e5_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["rx"]) -> 'openenoc_endpoint_interface_non_oetp_dma_rx_neg_0x2a972117692b39c8_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_interface_non_oetp_dma_tx_0x3b55de39a5c365e5_cls', 'openenoc_endpoint_interface_non_oetp_dma_rx_neg_0x2a972117692b39c8_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.non_oetp_dma"
    @property
    def rdl_desc(self) -> str:
        return "Endpoint-level DMA control and status for complete non-oETP Ethernet frames.\nFrame data includes the Ethernet header and payload, but excludes the preamble,\nStart Frame Delimiter (SFD), and Frame Check Sequence (FCS)."
    
    

    
    def __iter__(self) -> Iterator[Union[Node, NodeArray]]:
        
        
        yield self.tx
        yield self.rx
        
        
    

    
    
class openenoc_endpoint_interface_axis_if_sink_neg_0x44e0e4b447b67431_cls(RegFile):
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
        
            
        self.__data:openenoc_endpoint_interface_axis_if_sink_data_neg_0x19eaadd079c52b59_cls = openenoc_endpoint_interface_axis_if_sink_data_neg_0x19eaadd079c52b59_cls(
                                                                     address=self.address+0,
                                                                     logger_handle=logger_handle+'.data',
                                                                     inst_name='data', parent=self)
        
            
        self.__control:openenoc_endpoint_interface_axis_if_sink_control_neg_0x3273764231c7691f_cls = openenoc_endpoint_interface_axis_if_sink_control_neg_0x3273764231c7691f_cls(
                                                                     address=self.address+4,
                                                                     logger_handle=logger_handle+'.control',
                                                                     inst_name='control', parent=self)
        
            
        self.__status:openenoc_endpoint_interface_axis_if_sink_status_neg_0x170190c5e3b7dc0c_cls = openenoc_endpoint_interface_axis_if_sink_status_neg_0x170190c5e3b7dc0c_cls(
                                                                     address=self.address+8,
                                                                     logger_handle=logger_handle+'.status',
                                                                     inst_name='status', parent=self)
        

    @property
    def size(self) -> int:
        return 12

    # properties for Register and RegisterFiles
    @property
    def data(self) -> 'openenoc_endpoint_interface_axis_if_sink_data_neg_0x19eaadd079c52b59_cls':
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
    def control(self) -> 'openenoc_endpoint_interface_axis_if_sink_control_neg_0x3273764231c7691f_cls':
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
    def status(self) -> 'openenoc_endpoint_interface_axis_if_sink_status_neg_0x170190c5e3b7dc0c_cls':
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
    def get_child_by_system_rdl_name(self, name: Literal["data"]) -> 'openenoc_endpoint_interface_axis_if_sink_data_neg_0x19eaadd079c52b59_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["control"]) -> 'openenoc_endpoint_interface_axis_if_sink_control_neg_0x3273764231c7691f_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["status"]) -> 'openenoc_endpoint_interface_axis_if_sink_status_neg_0x170190c5e3b7dc0c_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_interface_axis_if_sink_data_neg_0x19eaadd079c52b59_cls', 'openenoc_endpoint_interface_axis_if_sink_control_neg_0x3273764231c7691f_cls', 'openenoc_endpoint_interface_axis_if_sink_status_neg_0x170190c5e3b7dc0c_cls', ]: ...

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
        
        
    

    
    
class openenoc_endpoint_interface_axis_if_source_0x781ff427f6c9c0fd_cls(RegFile):
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
        
            
        self.__data:openenoc_endpoint_interface_axis_if_source_data_neg_0x21a62fa3df170803_cls = openenoc_endpoint_interface_axis_if_source_data_neg_0x21a62fa3df170803_cls(
                                                                     address=self.address+0,
                                                                     logger_handle=logger_handle+'.data',
                                                                     inst_name='data', parent=self)
        
            
        self.__control:openenoc_endpoint_interface_axis_if_source_control_0x2ea2e4307e00845f_cls = openenoc_endpoint_interface_axis_if_source_control_0x2ea2e4307e00845f_cls(
                                                                     address=self.address+4,
                                                                     logger_handle=logger_handle+'.control',
                                                                     inst_name='control', parent=self)
        
            
        self.__status:openenoc_endpoint_interface_axis_if_source_status_0x5c619194de268f36_cls = openenoc_endpoint_interface_axis_if_source_status_0x5c619194de268f36_cls(
                                                                     address=self.address+8,
                                                                     logger_handle=logger_handle+'.status',
                                                                     inst_name='status', parent=self)
        

    @property
    def size(self) -> int:
        return 12

    # properties for Register and RegisterFiles
    @property
    def data(self) -> 'openenoc_endpoint_interface_axis_if_source_data_neg_0x21a62fa3df170803_cls':
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
    def control(self) -> 'openenoc_endpoint_interface_axis_if_source_control_0x2ea2e4307e00845f_cls':
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
    def status(self) -> 'openenoc_endpoint_interface_axis_if_source_status_0x5c619194de268f36_cls':
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
    def get_child_by_system_rdl_name(self, name: Literal["data"]) -> 'openenoc_endpoint_interface_axis_if_source_data_neg_0x21a62fa3df170803_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["control"]) -> 'openenoc_endpoint_interface_axis_if_source_control_0x2ea2e4307e00845f_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["status"]) -> 'openenoc_endpoint_interface_axis_if_source_status_0x5c619194de268f36_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_interface_axis_if_source_data_neg_0x21a62fa3df170803_cls', 'openenoc_endpoint_interface_axis_if_source_control_0x2ea2e4307e00845f_cls', 'openenoc_endpoint_interface_axis_if_source_status_0x5c619194de268f36_cls', ]: ...

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
        
        
    

    
    
class openenoc_endpoint_interface_axis_if_0x592581d562d9b4b7_cls(RegFile):
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
        self.__source:openenoc_endpoint_interface_axis_if_source_0x781ff427f6c9c0fd_cls = openenoc_endpoint_interface_axis_if_source_0x781ff427f6c9c0fd_cls(
                                                                                address=self.address+0,
                                                                                logger_handle=logger_handle+'.source',
                                                                                inst_name='source',
                                                                                parent=self)
        self.__sink:openenoc_endpoint_interface_axis_if_sink_neg_0x44e0e4b447b67431_cls = openenoc_endpoint_interface_axis_if_sink_neg_0x44e0e4b447b67431_cls(
                                                                                address=self.address+16,
                                                                                logger_handle=logger_handle+'.sink',
                                                                                inst_name='sink',
                                                                                parent=self)
        

    @property
    def size(self) -> int:
        return 28

    # properties for Register and RegisterFiles
    @property
    def source(self) -> 'openenoc_endpoint_interface_axis_if_source_0x781ff427f6c9c0fd_cls':
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
    def sink(self) -> 'openenoc_endpoint_interface_axis_if_sink_neg_0x44e0e4b447b67431_cls':
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
    def get_child_by_system_rdl_name(self, name: Literal["source"]) -> 'openenoc_endpoint_interface_axis_if_source_0x781ff427f6c9c0fd_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["sink"]) -> 'openenoc_endpoint_interface_axis_if_sink_neg_0x44e0e4b447b67431_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_interface_axis_if_source_0x781ff427f6c9c0fd_cls', 'openenoc_endpoint_interface_axis_if_sink_neg_0x44e0e4b447b67431_cls', ]: ...

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
        
        
    

    
    
class openenoc_endpoint_interface_conf_0x39b3494183983d47_cls(RegFile):
    """
    Class to represent a register file in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.conf                                        |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Configuration register file for this openENOC Endpoint          |
    |              |      Interface instance.</p>                                            |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__mac_address', '__multicast_address', '__non_oetp_control', '__rmem_timeout', '__dma_timeout', '__dma_max_fragment_size']

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
        
            
        self.__mac_address:openenoc_endpoint_interface_conf_mac_address_neg_0x79fb2b98c7d7201_cls = openenoc_endpoint_interface_conf_mac_address_neg_0x79fb2b98c7d7201_cls(
                                                                     address=self.address+0,
                                                                     logger_handle=logger_handle+'.mac_address',
                                                                     inst_name='mac_address', parent=self)
        
            
        self.__multicast_address:openenoc_endpoint_interface_conf_multicast_address_0xfe1435096c263d9_cls = openenoc_endpoint_interface_conf_multicast_address_0xfe1435096c263d9_cls(
                                                                     address=self.address+8,
                                                                     logger_handle=logger_handle+'.multicast_address',
                                                                     inst_name='multicast_address', parent=self)
        
            
        self.__non_oetp_control:openenoc_endpoint_interface_conf_non_oetp_control_neg_0x2996e2b07396a6a9_cls = openenoc_endpoint_interface_conf_non_oetp_control_neg_0x2996e2b07396a6a9_cls(
                                                                     address=self.address+16,
                                                                     logger_handle=logger_handle+'.non_oetp_control',
                                                                     inst_name='non_oetp_control', parent=self)
        
            
        self.__rmem_timeout:openenoc_endpoint_interface_conf_rmem_timeout_neg_0x5a12504165c33716_cls = openenoc_endpoint_interface_conf_rmem_timeout_neg_0x5a12504165c33716_cls(
                                                                     address=self.address+20,
                                                                     logger_handle=logger_handle+'.rmem_timeout',
                                                                     inst_name='rmem_timeout', parent=self)
        
            
        self.__dma_timeout:openenoc_endpoint_interface_conf_dma_timeout_neg_0x7ac586385b822cfd_cls = openenoc_endpoint_interface_conf_dma_timeout_neg_0x7ac586385b822cfd_cls(
                                                                     address=self.address+24,
                                                                     logger_handle=logger_handle+'.dma_timeout',
                                                                     inst_name='dma_timeout', parent=self)
        
            
        self.__dma_max_fragment_size:openenoc_endpoint_interface_conf_dma_max_fragment_size_neg_0x18d59c5f2d2d3078_cls = openenoc_endpoint_interface_conf_dma_max_fragment_size_neg_0x18d59c5f2d2d3078_cls(
                                                                     address=self.address+28,
                                                                     logger_handle=logger_handle+'.dma_max_fragment_size',
                                                                     inst_name='dma_max_fragment_size', parent=self)
        

    @property
    def size(self) -> int:
        return 32

    # properties for Register and RegisterFiles
    @property
    def mac_address(self) -> 'openenoc_endpoint_interface_conf_mac_address_neg_0x79fb2b98c7d7201_cls':
        """
        Property to access mac_address 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.conf.mac_address                            |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Local endpoint 48-bit unicast MAC address. The oETP engine uses |
        |              |      this address as its source MAC and compares individual-addressed   |
        |              |      incoming oETP frames against it. The I/G bit in the first MAC      |
        |              |      octet must be zero. Group-addressed oETP frames are compared       |
        |              |      against conf.multicast_address instead.</p>                        |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__mac_address
    
    @property
    def multicast_address(self) -> 'openenoc_endpoint_interface_conf_multicast_address_0xfe1435096c263d9_cls':
        """
        Property to access multicast_address 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.conf.multicast_address                      |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Local endpoint 48-bit multicast destination MAC address. For an |
        |              |      incoming oETP frame whose destination I/G bit is one, the engine   |
        |              |      accepts the destination only when it exactly matches this address. |
        |              |      All slave endpoints in a replication group use the same value.     |
        |              |      This address is not used as a source MAC. Zero is the reset value  |
        |              |      and matches no group-addressed destination, disabling oETP group   |
        |              |      reception. Broadcast is accepted only when this address is all     |
        |              |      ones. This field does not change the separate non-oETP receive-    |
        |              |      mode policy.</p>                                                   |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__multicast_address
    
    @property
    def non_oetp_control(self) -> 'openenoc_endpoint_interface_conf_non_oetp_control_neg_0x2996e2b07396a6a9_cls':
        """
        Property to access non_oetp_control 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.conf.non_oetp_control                       |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Receive policy for Ethernet frames that do not carry oETP       |
        |              |      traffic.</p>                                                       |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__non_oetp_control
    
    @property
    def rmem_timeout(self) -> 'openenoc_endpoint_interface_conf_rmem_timeout_neg_0x5a12504165c33716_cls':
        """
        Property to access rmem_timeout 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.conf.rmem_timeout                           |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Timeout configuration for transparent RMEM operations.</p>      |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__rmem_timeout
    
    @property
    def dma_timeout(self) -> 'openenoc_endpoint_interface_conf_dma_timeout_neg_0x7ac586385b822cfd_cls':
        """
        Property to access dma_timeout 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.conf.dma_timeout                            |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Common response timeout for locally initiated unicast peer DMA  |
        |              |      fragments.</p>                                                     |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__dma_timeout
    
    @property
    def dma_max_fragment_size(self) -> 'openenoc_endpoint_interface_conf_dma_max_fragment_size_neg_0x18d59c5f2d2d3078_cls':
        """
        Property to access dma_max_fragment_size 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.conf.dma_max_fragment_size                  |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Common software-selected maximum memory fragment size for       |
        |              |      locally initiated peer DMA transfers. The synthesis-time frame     |
        |              |      limit remains fixed.</p>                                           |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__dma_max_fragment_size
    

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'mac_address':'mac_address','multicast_address':'multicast_address','non_oetp_control':'non_oetp_control','rmem_timeout':'rmem_timeout','dma_timeout':'dma_timeout','dma_max_fragment_size':'dma_max_fragment_size',
            }

    
    
    
    
    
    
    # nodes:6
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["mac_address"]) -> 'openenoc_endpoint_interface_conf_mac_address_neg_0x79fb2b98c7d7201_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["multicast_address"]) -> 'openenoc_endpoint_interface_conf_multicast_address_0xfe1435096c263d9_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["non_oetp_control"]) -> 'openenoc_endpoint_interface_conf_non_oetp_control_neg_0x2996e2b07396a6a9_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["rmem_timeout"]) -> 'openenoc_endpoint_interface_conf_rmem_timeout_neg_0x5a12504165c33716_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["dma_timeout"]) -> 'openenoc_endpoint_interface_conf_dma_timeout_neg_0x7ac586385b822cfd_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["dma_max_fragment_size"]) -> 'openenoc_endpoint_interface_conf_dma_max_fragment_size_neg_0x18d59c5f2d2d3078_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_interface_conf_mac_address_neg_0x79fb2b98c7d7201_cls', 'openenoc_endpoint_interface_conf_multicast_address_0xfe1435096c263d9_cls', 'openenoc_endpoint_interface_conf_non_oetp_control_neg_0x2996e2b07396a6a9_cls', 'openenoc_endpoint_interface_conf_rmem_timeout_neg_0x5a12504165c33716_cls', 'openenoc_endpoint_interface_conf_dma_timeout_neg_0x7ac586385b822cfd_cls', 'openenoc_endpoint_interface_conf_dma_max_fragment_size_neg_0x18d59c5f2d2d3078_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.conf"
    @property
    def rdl_desc(self) -> str:
        return "Configuration register file for this openENOC Endpoint Interface instance."
    
    

    
    def __iter__(self) -> Iterator[Union[Node, NodeArray]]:
        
        
        yield self.mac_address
        yield self.multicast_address
        yield self.non_oetp_control
        yield self.rmem_timeout
        yield self.dma_timeout
        yield self.dma_max_fragment_size
        
        
    

    
    
class openenoc_endpoint_interface_0x5b9893f856e7c8c7_cls(RegFile):
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

    __slots__ : list[str] = ['__info', '__conf', '__axis_if', '__non_oetp_dma', '__irq', '__peers', '__rmem']

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
        
            
        self.__info:openenoc_endpoint_interface_info_neg_0x769d3cada650b261_cls = openenoc_endpoint_interface_info_neg_0x769d3cada650b261_cls(
                                                                     address=self.address+0,
                                                                     logger_handle=logger_handle+'.info',
                                                                     inst_name='info', parent=self)
        self.__conf:openenoc_endpoint_interface_conf_0x39b3494183983d47_cls = openenoc_endpoint_interface_conf_0x39b3494183983d47_cls(
                                                                                address=self.address+32,
                                                                                logger_handle=logger_handle+'.conf',
                                                                                inst_name='conf',
                                                                                parent=self)
        self.__axis_if:openenoc_endpoint_interface_axis_if_0x592581d562d9b4b7_cls = openenoc_endpoint_interface_axis_if_0x592581d562d9b4b7_cls(
                                                                                address=self.address+64,
                                                                                logger_handle=logger_handle+'.axis_if',
                                                                                inst_name='axis_if',
                                                                                parent=self)
        self.__non_oetp_dma:openenoc_endpoint_interface_non_oetp_dma_neg_0x457dd3161aaaf0a0_cls = openenoc_endpoint_interface_non_oetp_dma_neg_0x457dd3161aaaf0a0_cls(
                                                                                address=self.address+96,
                                                                                logger_handle=logger_handle+'.non_oetp_dma',
                                                                                inst_name='non_oetp_dma',
                                                                                parent=self)
        self.__irq:openenoc_endpoint_interface_irq_0x10abdd179744b18a_cls = openenoc_endpoint_interface_irq_0x10abdd179744b18a_cls(
                                                                                address=self.address+128,
                                                                                logger_handle=logger_handle+'.irq',
                                                                                inst_name='irq',
                                                                                parent=self)
        self.__peers:openenoc_endpoint_interface_peers_0x2a8405b29020d2ad_cls = openenoc_endpoint_interface_peers_0x2a8405b29020d2ad_cls(
                                                                                address=self.address+256,
                                                                                logger_handle=logger_handle+'.peers',
                                                                                inst_name='peers',
                                                                                parent=self)
        self.__rmem:openenoc_endpoint_interface_rmem_0x45d94b2b2b16d3f_cls = openenoc_endpoint_interface_rmem_0x45d94b2b2b16d3f_cls(
                                                                                address=self.address+1024,
                                                                                logger_handle=logger_handle+'.rmem',
                                                                                inst_name='rmem',
                                                                                parent=self)
        

    @property
    def size(self) -> int:
        return 2048

    # properties for Register and RegisterFiles
    @property
    def info(self) -> 'openenoc_endpoint_interface_info_neg_0x769d3cada650b261_cls':
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
    def conf(self) -> 'openenoc_endpoint_interface_conf_0x39b3494183983d47_cls':
        """
        Property to access conf 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.conf                                        |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Configuration register file for this openENOC Endpoint          |
        |              |      Interface instance.</p>                                            |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__conf
    
    @property
    def axis_if(self) -> 'openenoc_endpoint_interface_axis_if_0x592581d562d9b4b7_cls':
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
    def non_oetp_dma(self) -> 'openenoc_endpoint_interface_non_oetp_dma_neg_0x457dd3161aaaf0a0_cls':
        """
        Property to access non_oetp_dma 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.non_oetp_dma                                |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Endpoint-level DMA control and status for complete non-oETP     |
        |              |      Ethernet frames. Frame data includes the Ethernet header and       |
        |              |      payload, but excludes the preamble, Start Frame Delimiter (SFD),   |
        |              |      and Frame Check Sequence (FCS).</p>                                |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__non_oetp_dma
    
    @property
    def irq(self) -> 'openenoc_endpoint_interface_irq_0x10abdd179744b18a_cls':
        """
        Property to access irq 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.irq                                         |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Endpoint-level interrupt control and claim interface. Interrupt |
        |              |      events from peer DMA, non-oETP DMA, direct AXI4-Stream transfers,  |
        |              |      and RMEM failures are serialized through a shared event FIFO.</p>  |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__irq
    
    @property
    def peers(self) -> 'openenoc_endpoint_interface_peers_0x2a8405b29020d2ad_cls':
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
    def rmem(self) -> 'openenoc_endpoint_interface_rmem_0x45d94b2b2b16d3f_cls':
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
        return {'info':'info','conf':'conf','axis_if':'axis_if','non_oetp_dma':'non_oetp_dma','irq':'irq','peers':'peers','rmem':'rmem',
            }

    
    
    
    
    
    
    # nodes:7
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["info"]) -> 'openenoc_endpoint_interface_info_neg_0x769d3cada650b261_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["conf"]) -> 'openenoc_endpoint_interface_conf_0x39b3494183983d47_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["axis_if"]) -> 'openenoc_endpoint_interface_axis_if_0x592581d562d9b4b7_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["non_oetp_dma"]) -> 'openenoc_endpoint_interface_non_oetp_dma_neg_0x457dd3161aaaf0a0_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["irq"]) -> 'openenoc_endpoint_interface_irq_0x10abdd179744b18a_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["peers"]) -> 'openenoc_endpoint_interface_peers_0x2a8405b29020d2ad_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["rmem"]) -> 'openenoc_endpoint_interface_rmem_0x45d94b2b2b16d3f_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_interface_info_neg_0x769d3cada650b261_cls', 'openenoc_endpoint_interface_conf_0x39b3494183983d47_cls', 'openenoc_endpoint_interface_axis_if_0x592581d562d9b4b7_cls', 'openenoc_endpoint_interface_non_oetp_dma_neg_0x457dd3161aaaf0a0_cls', 'openenoc_endpoint_interface_irq_0x10abdd179744b18a_cls', 'openenoc_endpoint_interface_peers_0x2a8405b29020d2ad_cls', 'openenoc_endpoint_interface_rmem_0x45d94b2b2b16d3f_cls', ]: ...

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
        yield self.conf
        yield self.axis_if
        yield self.non_oetp_dma
        yield self.irq
        yield self.peers
        yield self.rmem
        
        
    

    
    
class csr_neg_0x6da9b8a7f75c2cc_cls(AddressMap):
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

        
            
        self.__test_reg:csr_test_reg_neg_0x59127c6cf49571bc_cls = csr_test_reg_neg_0x59127c6cf49571bc_cls(
                                                                     address=self.address+0,
                                                                     logger_handle=logger_handle+'.test_reg',
                                                                     inst_name='test_reg', parent=self)
        
            
        self.__regB:csr_regB_0x147bcdd77ddbf689_cls = csr_regB_0x147bcdd77ddbf689_cls(
                                                                     address=self.address+4,
                                                                     logger_handle=logger_handle+'.regB',
                                                                     inst_name='regB', parent=self)
        self.__endpoint_interface:openenoc_endpoint_interface_0x5b9893f856e7c8c7_cls = openenoc_endpoint_interface_0x5b9893f856e7c8c7_cls(
                                                                                address=self.address+2048,
                                                                                logger_handle=logger_handle+'.endpoint_interface',
                                                                                inst_name='endpoint_interface',
                                                                                parent=self)
        self.__switch_interface:openenoc_switch_interface_neg_0x6bd0310ca632c708_cls = openenoc_switch_interface_neg_0x6bd0310ca632c708_cls(
                                                                                address=self.address+4096,
                                                                                logger_handle=logger_handle+'.switch_interface',
                                                                                inst_name='switch_interface',
                                                                                parent=self)
        

    @property
    def size(self) -> int:
        return 4352
    @property
    def test_reg(self) -> 'csr_test_reg_neg_0x59127c6cf49571bc_cls':
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
    def regB(self) -> 'csr_regB_0x147bcdd77ddbf689_cls':
        """
        Property to access regB 

        
        """
        return self.__regB
        
    @property
    def endpoint_interface(self) -> 'openenoc_endpoint_interface_0x5b9893f856e7c8c7_cls':
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
    def switch_interface(self) -> 'openenoc_switch_interface_neg_0x6bd0310ca632c708_cls':
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
    def get_child_by_system_rdl_name(self, name: Literal["test_reg"]) -> 'csr_test_reg_neg_0x59127c6cf49571bc_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["regB"]) -> 'csr_regB_0x147bcdd77ddbf689_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["endpoint_interface"]) -> 'openenoc_endpoint_interface_0x5b9893f856e7c8c7_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["switch_interface"]) -> 'openenoc_switch_interface_neg_0x6bd0310ca632c708_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['csr_test_reg_neg_0x59127c6cf49571bc_cls', 'csr_regB_0x147bcdd77ddbf689_cls', 'openenoc_endpoint_interface_0x5b9893f856e7c8c7_cls', 'openenoc_switch_interface_neg_0x6bd0310ca632c708_cls', ]: ...

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
        
        
    


csr_cls = csr_neg_0x6da9b8a7f75c2cc_cls

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