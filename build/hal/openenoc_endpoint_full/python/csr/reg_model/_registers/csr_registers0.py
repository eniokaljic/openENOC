

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






from .fields import csr_test_reg_test_field_0x488d59952d02ae94_cls
from .fields import openenoc_endpoint_interface_info_rmem_total_depth_neg_0x7676c999991d3d7e_cls
from .fields import openenoc_endpoint_interface_info_num_of_peers_neg_0x1bf42f4882b9ee79_cls
from .fields import openenoc_endpoint_interface_info_peer_dma_supported_neg_0x77aa97ad7e43f5e9_cls
from .fields import openenoc_endpoint_interface_info_non_oetp_dma_supported_0x11beffd49b727115_cls
from .fields import openenoc_endpoint_interface_info_direct_axis_supported_0x7a5759da51760872_cls
from .fields import openenoc_endpoint_interface_info_rmem_supported_neg_0x49880c56abc88a0c_cls
from .fields import openenoc_endpoint_interface_info_irq_supported_neg_0x2ae274724774f3fa_cls
from .fields import openenoc_endpoint_interface_info_max_dma_frame_size_bytes_0x6a108e0b8e0e4dc8_cls
from .fields import openenoc_endpoint_interface_config_mac_address_lo_word_neg_0x6dcd798f5aa80e67_cls
from .fields import openenoc_endpoint_interface_config_mac_address_hi_word_neg_0xe443bbc4bfac99c_cls
from .fields import openenoc_endpoint_interface_config_non_oetp_control_receive_mode_neg_0x6d9f6272a4841189_cls
from .fields import openenoc_endpoint_interface_axis_if_source_data_tdata_0x16ec01948abdc96e_cls
from .fields import openenoc_endpoint_interface_axis_if_source_control_tvalid_neg_0x78efe513ab1093a5_cls
from .fields import openenoc_endpoint_interface_axis_if_source_control_tlast_neg_0x6c2ca72ba88245c1_cls
from .fields import openenoc_endpoint_interface_axis_if_source_control_tkeep_neg_0x3c1c90ea49575f35_cls
from .fields import openenoc_endpoint_interface_axis_if_source_status_tready_0x6674b2b7f4dec942_cls
from .fields import openenoc_endpoint_interface_axis_if_sink_data_tdata_0x19e976a7e6284dca_cls
from .fields import openenoc_endpoint_interface_axis_if_sink_control_tready_neg_0x672a0b3e5b3f0126_cls
from .fields import openenoc_endpoint_interface_axis_if_sink_status_tvalid_neg_0x1a62ce490e24a851_cls
from .fields import openenoc_endpoint_interface_axis_if_sink_status_tlast_0x32dda572418880f2_cls
from .fields import openenoc_endpoint_interface_axis_if_sink_status_tkeep_0x2ec1c0b56219612d_cls
from .fields import openenoc_endpoint_interface_non_oetp_dma_tx_buffer_address_base_0x53de669b4d49ca8e_cls
from .fields import openenoc_endpoint_interface_non_oetp_dma_tx_frame_length_bytes_neg_0x39e646bc4b60222c_cls
from .fields import openenoc_endpoint_interface_non_oetp_dma_tx_command_status_request_neg_0x54a58129f6f13d12_cls
from .fields import openenoc_endpoint_interface_non_oetp_dma_tx_command_status_idle_0x1b640ca41a49f1cd_cls
from .fields import openenoc_endpoint_interface_non_oetp_dma_tx_command_status_done_neg_0x3d818096c770e07b_cls
from .fields import openenoc_endpoint_interface_non_oetp_dma_tx_command_status_error_neg_0x1a81c472c69ea5ba_cls
from .fields import openenoc_endpoint_interface_non_oetp_dma_tx_command_status_error_code_0x3b9ff1f5566d37f9_cls
from .fields import openenoc_endpoint_interface_non_oetp_dma_tx_transferred_length_bytes_0x392615bcffa7f2a2_cls
from .fields import openenoc_endpoint_interface_non_oetp_dma_rx_buffer_address_base_neg_0xbdf1c67849ee26b_cls
from .fields import openenoc_endpoint_interface_non_oetp_dma_rx_buffer_capacity_bytes_neg_0x3da14d50150c8859_cls
from .fields import openenoc_endpoint_interface_non_oetp_dma_rx_command_status_request_neg_0xd8d6051f536c356_cls
from .fields import openenoc_endpoint_interface_non_oetp_dma_rx_command_status_idle_neg_0x13bb001abf57c766_cls
from .fields import openenoc_endpoint_interface_non_oetp_dma_rx_command_status_armed_neg_0x676c1af1ff7d2bb4_cls
from .fields import openenoc_endpoint_interface_non_oetp_dma_rx_command_status_done_neg_0x41309f270480f35a_cls
from .fields import openenoc_endpoint_interface_non_oetp_dma_rx_command_status_error_0x16d15edb1ba03f16_cls
from .fields import openenoc_endpoint_interface_non_oetp_dma_rx_command_status_error_code_0x7b4d8ee5c1b7a654_cls
from .fields import openenoc_endpoint_interface_non_oetp_dma_rx_received_length_bytes_0x3d06bd985ea57c4_cls
from .fields import openenoc_endpoint_interface_peers_entry_mac_address_lo_word_neg_0x4a418812823ae52_cls
from .fields import openenoc_endpoint_interface_peers_entry_mac_address_hi_word_neg_0x697bdf29ce41edb5_cls
from .fields import openenoc_endpoint_interface_peers_entry_rmem_address_offset_neg_0x660419d2f3cd0bf8_cls
from .fields import openenoc_endpoint_interface_peers_entry_local_address_base_neg_0x132f4fe3d8257897_cls
from .fields import openenoc_endpoint_interface_peers_entry_remote_address_base_neg_0x3cdd60ce4b58408_cls
from .fields import openenoc_endpoint_interface_peers_entry_size_bytes_neg_0x3adc214cdc89f32e_cls
from .fields import openenoc_endpoint_interface_peers_entry_dma_mode_neg_0x391e258cd04f6f84_cls
from .fields import openenoc_endpoint_interface_peers_entry_dma_request_0x1b88f4382a6e6598_cls
from .fields import openenoc_endpoint_interface_peers_entry_dma_idle_0x36662f605b9df709_cls
from .fields import openenoc_endpoint_interface_peers_entry_dma_done_neg_0x1c2b4b158bd12e74_cls
from .fields import openenoc_endpoint_interface_peers_entry_dma_error_0x753daff6f507dbda_cls
from .fields import openenoc_endpoint_interface_peers_entry_dma_error_code_0x4e849d7e18ec5152_cls

# register definitions
    
    
class csr_test_reg_0x78406839790ddb86_cls(RegReadWrite):
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
        
        self.__test_field:csr_test_reg_test_field_0x488d59952d02ae94_cls = csr_test_reg_test_field_0x488d59952d02ae94_cls(
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
    def test_field(self) -> csr_test_reg_test_field_0x488d59952d02ae94_cls:
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

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'csr_test_reg_test_field_0x488d59952d02ae94_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.test_reg"
    @property
    def rdl_desc(self) -> str:
        return "Test register"
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.test_field
        
        
    

    
    
class csr_regB_0x3ce7387ba908d624_cls(RegReadWrite):
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
        
        
    

    
    
class openenoc_endpoint_interface_info_neg_0x4848ad19296bafad_cls(RegReadOnly):
    """
    Class to represent a register in the register model

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

    __slots__ : list[str] = ['__rmem_total_depth', '__num_of_peers', '__peer_dma_supported', '__non_oetp_dma_supported', '__direct_axis_supported', '__rmem_supported', '__irq_supported', '__max_dma_frame_size_bytes']

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
        
        self.__rmem_total_depth:openenoc_endpoint_interface_info_rmem_total_depth_neg_0x7676c999991d3d7e_cls = openenoc_endpoint_interface_info_rmem_total_depth_neg_0x7676c999991d3d7e_cls(
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
        self.__num_of_peers:openenoc_endpoint_interface_info_num_of_peers_neg_0x1bf42f4882b9ee79_cls = openenoc_endpoint_interface_info_num_of_peers_neg_0x1bf42f4882b9ee79_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=11,
                lsb=32, msb=42,
                low=32, high=42),
            misc_props=FieldMiscProps(
                default=4,
                is_volatile=False),
            logger_handle=logger_handle+'.num_of_peers',
            inst_name='num_of_peers',
            field_type=int)
        self.__peer_dma_supported:openenoc_endpoint_interface_info_peer_dma_supported_neg_0x77aa97ad7e43f5e9_cls = openenoc_endpoint_interface_info_peer_dma_supported_neg_0x77aa97ad7e43f5e9_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=43, msb=43,
                low=43, high=43),
            misc_props=FieldMiscProps(
                default=1,
                is_volatile=False),
            logger_handle=logger_handle+'.peer_dma_supported',
            inst_name='peer_dma_supported',
            field_type=int)
        self.__non_oetp_dma_supported:openenoc_endpoint_interface_info_non_oetp_dma_supported_0x11beffd49b727115_cls = openenoc_endpoint_interface_info_non_oetp_dma_supported_0x11beffd49b727115_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=44, msb=44,
                low=44, high=44),
            misc_props=FieldMiscProps(
                default=1,
                is_volatile=False),
            logger_handle=logger_handle+'.non_oetp_dma_supported',
            inst_name='non_oetp_dma_supported',
            field_type=int)
        self.__direct_axis_supported:openenoc_endpoint_interface_info_direct_axis_supported_0x7a5759da51760872_cls = openenoc_endpoint_interface_info_direct_axis_supported_0x7a5759da51760872_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=45, msb=45,
                low=45, high=45),
            misc_props=FieldMiscProps(
                default=1,
                is_volatile=False),
            logger_handle=logger_handle+'.direct_axis_supported',
            inst_name='direct_axis_supported',
            field_type=int)
        self.__rmem_supported:openenoc_endpoint_interface_info_rmem_supported_neg_0x49880c56abc88a0c_cls = openenoc_endpoint_interface_info_rmem_supported_neg_0x49880c56abc88a0c_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=46, msb=46,
                low=46, high=46),
            misc_props=FieldMiscProps(
                default=1,
                is_volatile=False),
            logger_handle=logger_handle+'.rmem_supported',
            inst_name='rmem_supported',
            field_type=int)
        self.__irq_supported:openenoc_endpoint_interface_info_irq_supported_neg_0x2ae274724774f3fa_cls = openenoc_endpoint_interface_info_irq_supported_neg_0x2ae274724774f3fa_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=47, msb=47,
                low=47, high=47),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.irq_supported',
            inst_name='irq_supported',
            field_type=int)
        self.__max_dma_frame_size_bytes:openenoc_endpoint_interface_info_max_dma_frame_size_bytes_0x6a108e0b8e0e4dc8_cls = openenoc_endpoint_interface_info_max_dma_frame_size_bytes_0x6a108e0b8e0e4dc8_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=16,
                lsb=48, msb=63,
                low=48, high=63),
            misc_props=FieldMiscProps(
                default=8192,
                is_volatile=False),
            logger_handle=logger_handle+'.max_dma_frame_size_bytes',
            inst_name='max_dma_frame_size_bytes',
            field_type=int)

    @property
    def width(self) -> int:
        return 64

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def rmem_total_depth(self) -> openenoc_endpoint_interface_info_rmem_total_depth_neg_0x7676c999991d3d7e_cls:
        """
        Property to access rmem_total_depth field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.info.rmem_total_depth[31:0]                 |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Total depth of the shared memory region for all remote peers.   |
        |              |      This field reflects the RMEM_TOTAL_DEPTH parameter value.</p>      |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__rmem_total_depth
    @property
    def num_of_peers(self) -> openenoc_endpoint_interface_info_num_of_peers_neg_0x1bf42f4882b9ee79_cls:
        """
        Property to access num_of_peers field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.info.num_of_peers[42:32]                    |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Number of remote peers supported by this openENOC Endpoint      |
        |              |      Interface instance, from 0 to 2047. This field reflects the        |
        |              |      NUM_OF_PEERS parameter value.</p>                                  |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__num_of_peers
    @property
    def peer_dma_supported(self) -> openenoc_endpoint_interface_info_peer_dma_supported_neg_0x77aa97ad7e43f5e9_cls:
        """
        Property to access peer_dma_supported field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.info.peer_dma_supported                     |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Indicates whether DMA transfers associated with configured      |
        |              |      remote peers are supported.</p>                                    |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__peer_dma_supported
    @property
    def non_oetp_dma_supported(self) -> openenoc_endpoint_interface_info_non_oetp_dma_supported_0x11beffd49b727115_cls:
        """
        Property to access non_oetp_dma_supported field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.info.non_oetp_dma_supported                 |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Indicates whether endpoint-level DMA transfers of complete non- |
        |              |      oETP Ethernet frames are supported.</p>                            |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__non_oetp_dma_supported
    @property
    def direct_axis_supported(self) -> openenoc_endpoint_interface_info_direct_axis_supported_0x7a5759da51760872_cls:
        """
        Property to access direct_axis_supported field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.info.direct_axis_supported                  |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Indicates whether direct CSR-driven AXI4-Stream access is       |
        |              |      supported for non-oETP Ethernet frames.</p>                        |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__direct_axis_supported
    @property
    def rmem_supported(self) -> openenoc_endpoint_interface_info_rmem_supported_neg_0x49880c56abc88a0c_cls:
        """
        Property to access rmem_supported field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.info.rmem_supported                         |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Indicates whether the transparent Remote Memory (RMEM)          |
        |              |      interface is supported.</p>                                        |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__rmem_supported
    @property
    def irq_supported(self) -> openenoc_endpoint_interface_info_irq_supported_neg_0x2ae274724774f3fa_cls:
        """
        Property to access irq_supported field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.info.irq_supported                          |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Indicates whether the endpoint interrupt output and interrupt-  |
        |              |      control logic are implemented.</p>                                 |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__irq_supported
    @property
    def max_dma_frame_size_bytes(self) -> openenoc_endpoint_interface_info_max_dma_frame_size_bytes_0x6a108e0b8e0e4dc8_cls:
        """
        Property to access max_dma_frame_size_bytes field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.info.max_dma_frame_size_bytes[63:48]        |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Maximum size in bytes of one AXI4-Stream frame generated or     |
        |              |      consumed by the DMA engine. This field reflects the                |
        |              |      MAX_DMA_FRAME_SIZE_BYTES parameter value. A value of zero          |
        |              |      indicates that DMA is not supported.</p>                           |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__max_dma_frame_size_bytes

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'rmem_total_depth':'rmem_total_depth','num_of_peers':'num_of_peers','peer_dma_supported':'peer_dma_supported','non_oetp_dma_supported':'non_oetp_dma_supported','direct_axis_supported':'direct_axis_supported','rmem_supported':'rmem_supported','irq_supported':'irq_supported','max_dma_frame_size_bytes':'max_dma_frame_size_bytes',
            }

    
    
    
    
    
    
    # nodes:8
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["rmem_total_depth"]) -> 'openenoc_endpoint_interface_info_rmem_total_depth_neg_0x7676c999991d3d7e_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["num_of_peers"]) -> 'openenoc_endpoint_interface_info_num_of_peers_neg_0x1bf42f4882b9ee79_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["peer_dma_supported"]) -> 'openenoc_endpoint_interface_info_peer_dma_supported_neg_0x77aa97ad7e43f5e9_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["non_oetp_dma_supported"]) -> 'openenoc_endpoint_interface_info_non_oetp_dma_supported_0x11beffd49b727115_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["direct_axis_supported"]) -> 'openenoc_endpoint_interface_info_direct_axis_supported_0x7a5759da51760872_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["rmem_supported"]) -> 'openenoc_endpoint_interface_info_rmem_supported_neg_0x49880c56abc88a0c_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["irq_supported"]) -> 'openenoc_endpoint_interface_info_irq_supported_neg_0x2ae274724774f3fa_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["max_dma_frame_size_bytes"]) -> 'openenoc_endpoint_interface_info_max_dma_frame_size_bytes_0x6a108e0b8e0e4dc8_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_interface_info_rmem_total_depth_neg_0x7676c999991d3d7e_cls', 'openenoc_endpoint_interface_info_num_of_peers_neg_0x1bf42f4882b9ee79_cls', 'openenoc_endpoint_interface_info_peer_dma_supported_neg_0x77aa97ad7e43f5e9_cls', 'openenoc_endpoint_interface_info_non_oetp_dma_supported_0x11beffd49b727115_cls', 'openenoc_endpoint_interface_info_direct_axis_supported_0x7a5759da51760872_cls', 'openenoc_endpoint_interface_info_rmem_supported_neg_0x49880c56abc88a0c_cls', 'openenoc_endpoint_interface_info_irq_supported_neg_0x2ae274724774f3fa_cls', 'openenoc_endpoint_interface_info_max_dma_frame_size_bytes_0x6a108e0b8e0e4dc8_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.info"
    @property
    def rdl_desc(self) -> str:
        return "Read-only information register for this openENOC Endpoint Interface instance."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.rmem_total_depth
        yield self.num_of_peers
        yield self.peer_dma_supported
        yield self.non_oetp_dma_supported
        yield self.direct_axis_supported
        yield self.rmem_supported
        yield self.irq_supported
        yield self.max_dma_frame_size_bytes
        
        
    

    
    
class openenoc_endpoint_interface_config_mac_address_0x79092841bedb4058_cls(RegReadWrite):
    """
    Class to represent a register in the register model

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
        
        self.__lo_word:openenoc_endpoint_interface_config_mac_address_lo_word_neg_0x6dcd798f5aa80e67_cls = openenoc_endpoint_interface_config_mac_address_lo_word_neg_0x6dcd798f5aa80e67_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0, msb=31,
                low=0, high=31),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.lo_word',
            inst_name='lo_word',
            field_type=int)
        self.__hi_word:openenoc_endpoint_interface_config_mac_address_hi_word_neg_0xe443bbc4bfac99c_cls = openenoc_endpoint_interface_config_mac_address_hi_word_neg_0xe443bbc4bfac99c_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=16,
                lsb=32, msb=47,
                low=32, high=47),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
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
    def lo_word(self) -> openenoc_endpoint_interface_config_mac_address_lo_word_neg_0x6dcd798f5aa80e67_cls:
        """
        Property to access lo_word field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.config.mac_address.lo_word[31:0]            |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Lower 32 bits [31:0] of the 48-bit MAC address.</p>             |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__lo_word
    @property
    def hi_word(self) -> openenoc_endpoint_interface_config_mac_address_hi_word_neg_0xe443bbc4bfac99c_cls:
        """
        Property to access hi_word field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.config.mac_address.hi_word[47:32]           |
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
    def get_child_by_system_rdl_name(self, name: Literal["lo_word"]) -> 'openenoc_endpoint_interface_config_mac_address_lo_word_neg_0x6dcd798f5aa80e67_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["hi_word"]) -> 'openenoc_endpoint_interface_config_mac_address_hi_word_neg_0xe443bbc4bfac99c_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_interface_config_mac_address_lo_word_neg_0x6dcd798f5aa80e67_cls', 'openenoc_endpoint_interface_config_mac_address_hi_word_neg_0xe443bbc4bfac99c_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.config.mac_address"
    @property
    def rdl_desc(self) -> str:
        return "Local site 48-bit destination MAC address."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.lo_word
        yield self.hi_word
        
        
    

    
    
class openenoc_endpoint_interface_config_non_oetp_control_0x653dbf85e93f385_cls(RegReadWrite):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.config.non_oetp_control                     |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Receive policy for Ethernet frames that do not carry oETP       |
    |              |      traffic.</p>                                                       |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__receive_mode']

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
        
        self.__receive_mode:openenoc_endpoint_interface_config_non_oetp_control_receive_mode_neg_0x6d9f6272a4841189_cls = openenoc_endpoint_interface_config_non_oetp_control_receive_mode_neg_0x6d9f6272a4841189_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=2,
                lsb=0, msb=1,
                low=0, high=1),
            misc_props=FieldMiscProps(
                default=1,
                is_volatile=False),
            logger_handle=logger_handle+'.receive_mode',
            inst_name='receive_mode',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def receive_mode(self) -> openenoc_endpoint_interface_config_non_oetp_control_receive_mode_neg_0x6d9f6272a4841189_cls:
        """
        Property to access receive_mode field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.config.non_oetp_control.receive_mode[1:0]   |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Receive mode for non-oETP Ethernet frames:<ul></p> <li>0: Drop  |
        |              |      all non-oETP Ethernet frames.</li> <li>1: Filtered mode. Accept    |
        |              |      frames addressed to the configured local MAC address and Ethernet  |
        |              |      broadcast frames.</li> <li>2: Promiscuous mode. Accept all non-    |
        |              |      oETP Ethernet frames.</li> <li>3: Reserved. Hardware shall treat   |
        |              |      this value as drop mode.</li> <p></ul> An accepted frame is        |
        |              |      directed to the non-oETP RX DMA channel when that channel is       |
        |              |      armed; otherwise it is directed to the CSR AXI4-Stream sink.</p>   |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__receive_mode

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'receive_mode':'receive_mode',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_interface_config_non_oetp_control_receive_mode_neg_0x6d9f6272a4841189_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.config.non_oetp_control"
    @property
    def rdl_desc(self) -> str:
        return "Receive policy for Ethernet frames that do not carry oETP traffic."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.receive_mode
        
        
    

    
    
class openenoc_endpoint_interface_axis_if_source_data_0xe9693343a5d094a_cls(RegReadWrite):
    """
    Class to represent a register in the register model

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
        
        self.__tdata:openenoc_endpoint_interface_axis_if_source_data_tdata_0x16ec01948abdc96e_cls = openenoc_endpoint_interface_axis_if_source_data_tdata_0x16ec01948abdc96e_cls(
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
    def tdata(self) -> openenoc_endpoint_interface_axis_if_source_data_tdata_0x16ec01948abdc96e_cls:
        """
        Property to access tdata field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.axis_if.source.data.tdata[31:0]             |
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

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_interface_axis_if_source_data_tdata_0x16ec01948abdc96e_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.axis_if.source.data"
    @property
    def rdl_desc(self) -> str:
        return "Data register for the AXI4-Stream source interface."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.tdata
        
        
    

    
    
class openenoc_endpoint_interface_axis_if_source_control_neg_0x5d68303dd4d10c2a_cls(RegReadWrite):
    """
    Class to represent a register in the register model

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

    __slots__ : list[str] = ['__tvalid', '__tlast', '__tkeep']

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
        
        self.__tvalid:openenoc_endpoint_interface_axis_if_source_control_tvalid_neg_0x78efe513ab1093a5_cls = openenoc_endpoint_interface_axis_if_source_control_tvalid_neg_0x78efe513ab1093a5_cls(
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
        self.__tlast:openenoc_endpoint_interface_axis_if_source_control_tlast_neg_0x6c2ca72ba88245c1_cls = openenoc_endpoint_interface_axis_if_source_control_tlast_neg_0x6c2ca72ba88245c1_cls(
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
        self.__tkeep:openenoc_endpoint_interface_axis_if_source_control_tkeep_neg_0x3c1c90ea49575f35_cls = openenoc_endpoint_interface_axis_if_source_control_tkeep_neg_0x3c1c90ea49575f35_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=4,
                lsb=16, msb=19,
                low=16, high=19),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.tkeep',
            inst_name='tkeep',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def tvalid(self) -> openenoc_endpoint_interface_axis_if_source_control_tvalid_neg_0x78efe513ab1093a5_cls:
        """
        Property to access tvalid field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.axis_if.source.control.tvalid               |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Indicates that the AXI4-Stream source interface has valid data  |
        |              |      to send. Once asserted by software, the field remains asserted     |
        |              |      until the transfer is accepted by the destination.</p>             |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__tvalid
    @property
    def tlast(self) -> openenoc_endpoint_interface_axis_if_source_control_tlast_neg_0x6c2ca72ba88245c1_cls:
        """
        Property to access tlast field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.axis_if.source.control.tlast                |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Indicates the last data word of a frame on the AXI4-Stream      |
        |              |      source interface.</p>                                              |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__tlast
    @property
    def tkeep(self) -> openenoc_endpoint_interface_axis_if_source_control_tkeep_neg_0x3c1c90ea49575f35_cls:
        """
        Property to access tkeep field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.axis_if.source.control.tkeep[3:0]           |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Indicates which byte lanes contain valid data on the            |
        |              |      AXI4-Stream source interface.</p>                                  |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__tkeep

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'tvalid':'tvalid','tlast':'tlast','tkeep':'tkeep',
            }

    
    
    
    
    
    
    # nodes:3
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["tvalid"]) -> 'openenoc_endpoint_interface_axis_if_source_control_tvalid_neg_0x78efe513ab1093a5_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["tlast"]) -> 'openenoc_endpoint_interface_axis_if_source_control_tlast_neg_0x6c2ca72ba88245c1_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["tkeep"]) -> 'openenoc_endpoint_interface_axis_if_source_control_tkeep_neg_0x3c1c90ea49575f35_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_interface_axis_if_source_control_tvalid_neg_0x78efe513ab1093a5_cls', 'openenoc_endpoint_interface_axis_if_source_control_tlast_neg_0x6c2ca72ba88245c1_cls', 'openenoc_endpoint_interface_axis_if_source_control_tkeep_neg_0x3c1c90ea49575f35_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.axis_if.source.control"
    @property
    def rdl_desc(self) -> str:
        return "Control register for the AXI4-Stream source interface."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.tvalid
        yield self.tlast
        yield self.tkeep
        
        
    

    
    
class openenoc_endpoint_interface_axis_if_source_status_0xb04096d4160b055_cls(RegReadOnly):
    """
    Class to represent a register in the register model

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
        
        self.__tready:openenoc_endpoint_interface_axis_if_source_status_tready_0x6674b2b7f4dec942_cls = openenoc_endpoint_interface_axis_if_source_status_tready_0x6674b2b7f4dec942_cls(
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
    def tready(self) -> openenoc_endpoint_interface_axis_if_source_status_tready_0x6674b2b7f4dec942_cls:
        """
        Property to access tready field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.axis_if.source.status.tready                |
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

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_interface_axis_if_source_status_tready_0x6674b2b7f4dec942_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.axis_if.source.status"
    @property
    def rdl_desc(self) -> str:
        return "Status register for the AXI4-Stream source interface."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.tready
        
        
    

    
    
class openenoc_endpoint_interface_axis_if_sink_data_neg_0x3b004716259ce70a_cls(RegReadOnly):
    """
    Class to represent a register in the register model

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
        
        self.__tdata:openenoc_endpoint_interface_axis_if_sink_data_tdata_0x19e976a7e6284dca_cls = openenoc_endpoint_interface_axis_if_sink_data_tdata_0x19e976a7e6284dca_cls(
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
    def tdata(self) -> openenoc_endpoint_interface_axis_if_sink_data_tdata_0x19e976a7e6284dca_cls:
        """
        Property to access tdata field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.axis_if.sink.data.tdata[31:0]               |
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

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_interface_axis_if_sink_data_tdata_0x19e976a7e6284dca_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.axis_if.sink.data"
    @property
    def rdl_desc(self) -> str:
        return "Data register for the AXI4-Stream sink interface."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.tdata
        
        
    

    
    
class openenoc_endpoint_interface_axis_if_sink_control_0x222b0c8726cf4230_cls(RegReadWrite):
    """
    Class to represent a register in the register model

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

    __slots__ : list[str] = ['__tready']

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
        
        self.__tready:openenoc_endpoint_interface_axis_if_sink_control_tready_neg_0x672a0b3e5b3f0126_cls = openenoc_endpoint_interface_axis_if_sink_control_tready_neg_0x672a0b3e5b3f0126_cls(
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

    

    # build the properties for the fields
    
    @property
    def tready(self) -> openenoc_endpoint_interface_axis_if_sink_control_tready_neg_0x672a0b3e5b3f0126_cls:
        """
        Property to access tready field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.axis_if.sink.control.tready                 |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Indicates that the AXI4-Stream sink interface is ready to       |
        |              |      accept a data transfer. Once asserted by software, the field       |
        |              |      remains asserted until a transfer occurs.</p>                      |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__tready

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'tready':'tready',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_interface_axis_if_sink_control_tready_neg_0x672a0b3e5b3f0126_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.axis_if.sink.control"
    @property
    def rdl_desc(self) -> str:
        return "Control register for the AXI4-Stream sink interface."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.tready
        
        
    

    
    
class openenoc_endpoint_interface_axis_if_sink_status_0x4515671aa4bd3d34_cls(RegReadOnly):
    """
    Class to represent a register in the register model

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

    __slots__ : list[str] = ['__tvalid', '__tlast', '__tkeep']

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
        
        self.__tvalid:openenoc_endpoint_interface_axis_if_sink_status_tvalid_neg_0x1a62ce490e24a851_cls = openenoc_endpoint_interface_axis_if_sink_status_tvalid_neg_0x1a62ce490e24a851_cls(
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
        self.__tlast:openenoc_endpoint_interface_axis_if_sink_status_tlast_0x32dda572418880f2_cls = openenoc_endpoint_interface_axis_if_sink_status_tlast_0x32dda572418880f2_cls(
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
        self.__tkeep:openenoc_endpoint_interface_axis_if_sink_status_tkeep_0x2ec1c0b56219612d_cls = openenoc_endpoint_interface_axis_if_sink_status_tkeep_0x2ec1c0b56219612d_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=4,
                lsb=16, msb=19,
                low=16, high=19),
            misc_props=FieldMiscProps(
                default=None,
                is_volatile=True),
            logger_handle=logger_handle+'.tkeep',
            inst_name='tkeep',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def tvalid(self) -> openenoc_endpoint_interface_axis_if_sink_status_tvalid_neg_0x1a62ce490e24a851_cls:
        """
        Property to access tvalid field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.axis_if.sink.status.tvalid                  |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Indicates that the AXI4-Stream sink interface has valid data to |
        |              |      receive.</p>                                                       |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__tvalid
    @property
    def tlast(self) -> openenoc_endpoint_interface_axis_if_sink_status_tlast_0x32dda572418880f2_cls:
        """
        Property to access tlast field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.axis_if.sink.status.tlast                   |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Indicates the last data word of a frame on the AXI4-Stream sink |
        |              |      interface.</p>                                                     |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__tlast
    @property
    def tkeep(self) -> openenoc_endpoint_interface_axis_if_sink_status_tkeep_0x2ec1c0b56219612d_cls:
        """
        Property to access tkeep field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.axis_if.sink.status.tkeep[3:0]              |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Indicates which byte lanes contain valid data on the            |
        |              |      AXI4-Stream sink interface.</p>                                    |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__tkeep

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'tvalid':'tvalid','tlast':'tlast','tkeep':'tkeep',
            }

    
    
    
    
    
    
    # nodes:3
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["tvalid"]) -> 'openenoc_endpoint_interface_axis_if_sink_status_tvalid_neg_0x1a62ce490e24a851_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["tlast"]) -> 'openenoc_endpoint_interface_axis_if_sink_status_tlast_0x32dda572418880f2_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["tkeep"]) -> 'openenoc_endpoint_interface_axis_if_sink_status_tkeep_0x2ec1c0b56219612d_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_interface_axis_if_sink_status_tvalid_neg_0x1a62ce490e24a851_cls', 'openenoc_endpoint_interface_axis_if_sink_status_tlast_0x32dda572418880f2_cls', 'openenoc_endpoint_interface_axis_if_sink_status_tkeep_0x2ec1c0b56219612d_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.axis_if.sink.status"
    @property
    def rdl_desc(self) -> str:
        return "Status register for the AXI4-Stream sink interface."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.tvalid
        yield self.tlast
        yield self.tkeep
        
        
    

    
    
class openenoc_endpoint_interface_non_oetp_dma_tx_buffer_address_0x4ce91f0ce21c98fd_cls(RegReadWrite):
    """
    Class to represent a register in the register model

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
        
        self.__base:openenoc_endpoint_interface_non_oetp_dma_tx_buffer_address_base_0x53de669b4d49ca8e_cls = openenoc_endpoint_interface_non_oetp_dma_tx_buffer_address_base_0x53de669b4d49ca8e_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0, msb=31,
                low=0, high=31),
            misc_props=FieldMiscProps(
                default=0,
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
    def base(self) -> openenoc_endpoint_interface_non_oetp_dma_tx_buffer_address_base_0x53de669b4d49ca8e_cls:
        """
        Property to access base field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.non_oetp_dma.tx.buffer_address.base[31:0]   |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>32-bit byte address of the first byte of the transmit           |
        |              |      buffer.</p>                                                        |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__base

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'base':'base',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_interface_non_oetp_dma_tx_buffer_address_base_0x53de669b4d49ca8e_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.non_oetp_dma.tx.buffer_address"
    @property
    def rdl_desc(self) -> str:
        return "Local memory address of the non-oETP Ethernet frame to transmit."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.base
        
        
    

    
    
class openenoc_endpoint_interface_non_oetp_dma_tx_frame_length_0x4490b34232c03d9c_cls(RegReadWrite):
    """
    Class to represent a register in the register model

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
        
        self.__bytes:openenoc_endpoint_interface_non_oetp_dma_tx_frame_length_bytes_neg_0x39e646bc4b60222c_cls = openenoc_endpoint_interface_non_oetp_dma_tx_frame_length_bytes_neg_0x39e646bc4b60222c_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0, msb=31,
                low=0, high=31),
            misc_props=FieldMiscProps(
                default=0,
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
    def bytes(self) -> openenoc_endpoint_interface_non_oetp_dma_tx_frame_length_bytes_neg_0x39e646bc4b60222c_cls:
        """
        Property to access bytes field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.non_oetp_dma.tx.frame_length.bytes[31:0]    |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Frame length in bytes. Valid non-zero values shall not exceed   |
        |              |      info.max_dma_frame_size_bytes.</p>                                 |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__bytes

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'bytes':'bytes',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_interface_non_oetp_dma_tx_frame_length_bytes_neg_0x39e646bc4b60222c_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.non_oetp_dma.tx.frame_length"
    @property
    def rdl_desc(self) -> str:
        return "Length of the complete non-oETP Ethernet frame to transmit."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.bytes
        
        
    

    
    
class openenoc_endpoint_interface_non_oetp_dma_tx_command_status_0x34b82dd39836e41_cls(RegReadWrite):
    """
    Class to represent a register in the register model

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

    __slots__ : list[str] = ['__request', '__idle', '__done', '__error', '__error_code']

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
        
        self.__request:openenoc_endpoint_interface_non_oetp_dma_tx_command_status_request_neg_0x54a58129f6f13d12_cls = openenoc_endpoint_interface_non_oetp_dma_tx_command_status_request_neg_0x54a58129f6f13d12_cls(
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
        self.__idle:openenoc_endpoint_interface_non_oetp_dma_tx_command_status_idle_0x1b640ca41a49f1cd_cls = openenoc_endpoint_interface_non_oetp_dma_tx_command_status_idle_0x1b640ca41a49f1cd_cls(
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
        self.__done:openenoc_endpoint_interface_non_oetp_dma_tx_command_status_done_neg_0x3d818096c770e07b_cls = openenoc_endpoint_interface_non_oetp_dma_tx_command_status_done_neg_0x3d818096c770e07b_cls(
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
        self.__error:openenoc_endpoint_interface_non_oetp_dma_tx_command_status_error_neg_0x1a81c472c69ea5ba_cls = openenoc_endpoint_interface_non_oetp_dma_tx_command_status_error_neg_0x1a81c472c69ea5ba_cls(
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
        self.__error_code:openenoc_endpoint_interface_non_oetp_dma_tx_command_status_error_code_0x3b9ff1f5566d37f9_cls = openenoc_endpoint_interface_non_oetp_dma_tx_command_status_error_code_0x3b9ff1f5566d37f9_cls(
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
    def request(self) -> openenoc_endpoint_interface_non_oetp_dma_tx_command_status_request_neg_0x54a58129f6f13d12_cls:
        """
        Property to access request field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.non_oetp_dma.tx.command_status.request      |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Writing one requests transmission of the configured frame. The  |
        |              |      field remains asserted until the DMA engine accepts the request.   |
        |              |      Hardware clears it upon acceptance; while the channel is busy, a   |
        |              |      newly asserted request remains pending.</p>                        |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__request
    @property
    def idle(self) -> openenoc_endpoint_interface_non_oetp_dma_tx_command_status_idle_0x1b640ca41a49f1cd_cls:
        """
        Property to access idle field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.non_oetp_dma.tx.command_status.idle         |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Indicates that the channel has no accepted transfer in          |
        |              |      progress. Hardware deasserts this field when a request is accepted |
        |              |      and asserts it when the transfer completes.</p>                    |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__idle
    @property
    def done(self) -> openenoc_endpoint_interface_non_oetp_dma_tx_command_status_done_neg_0x3d818096c770e07b_cls:
        """
        Property to access done field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.non_oetp_dma.tx.command_status.done         |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Sticky successful-completion flag. Hardware sets this field     |
        |              |      after the accepted transfer completes successfully and clears it   |
        |              |      when the next request is accepted.</p>                             |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__done
    @property
    def error(self) -> openenoc_endpoint_interface_non_oetp_dma_tx_command_status_error_neg_0x1a81c472c69ea5ba_cls:
        """
        Property to access error field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.non_oetp_dma.tx.command_status.error        |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Sticky error-completion flag. Hardware sets this field when the |
        |              |      accepted transfer terminates with an error and clears it when the  |
        |              |      next request is accepted.</p>                                      |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__error
    @property
    def error_code(self) -> openenoc_endpoint_interface_non_oetp_dma_tx_command_status_error_code_0x3b9ff1f5566d37f9_cls:
        """
        Property to access error_code field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.non_oetp_dma.tx.command_status.error_code[3 |
        |              |      1:28]                                                              |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Sticky error code for the most recently completed               |
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
        return {'request':'request','idle':'idle','done':'done','error':'error','error_code':'error_code',
            }

    
    
    
    
    
    
    # nodes:5
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["request"]) -> 'openenoc_endpoint_interface_non_oetp_dma_tx_command_status_request_neg_0x54a58129f6f13d12_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["idle"]) -> 'openenoc_endpoint_interface_non_oetp_dma_tx_command_status_idle_0x1b640ca41a49f1cd_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["done"]) -> 'openenoc_endpoint_interface_non_oetp_dma_tx_command_status_done_neg_0x3d818096c770e07b_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["error"]) -> 'openenoc_endpoint_interface_non_oetp_dma_tx_command_status_error_neg_0x1a81c472c69ea5ba_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["error_code"]) -> 'openenoc_endpoint_interface_non_oetp_dma_tx_command_status_error_code_0x3b9ff1f5566d37f9_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_interface_non_oetp_dma_tx_command_status_request_neg_0x54a58129f6f13d12_cls', 'openenoc_endpoint_interface_non_oetp_dma_tx_command_status_idle_0x1b640ca41a49f1cd_cls', 'openenoc_endpoint_interface_non_oetp_dma_tx_command_status_done_neg_0x3d818096c770e07b_cls', 'openenoc_endpoint_interface_non_oetp_dma_tx_command_status_error_neg_0x1a81c472c69ea5ba_cls', 'openenoc_endpoint_interface_non_oetp_dma_tx_command_status_error_code_0x3b9ff1f5566d37f9_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.non_oetp_dma.tx.command_status"
    @property
    def rdl_desc(self) -> str:
        return "Command and completion status for the non-oETP transmit DMA channel."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.request
        yield self.idle
        yield self.done
        yield self.error
        yield self.error_code
        
        
    

    
    
class openenoc_endpoint_interface_non_oetp_dma_tx_transferred_length_neg_0xf376b5ec411263f_cls(RegReadOnly):
    """
    Class to represent a register in the register model

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

    __slots__ : list[str] = ['__bytes']

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
        
        self.__bytes:openenoc_endpoint_interface_non_oetp_dma_tx_transferred_length_bytes_0x392615bcffa7f2a2_cls = openenoc_endpoint_interface_non_oetp_dma_tx_transferred_length_bytes_0x392615bcffa7f2a2_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0, msb=31,
                low=0, high=31),
            misc_props=FieldMiscProps(
                default=None,
                is_volatile=True),
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
    def bytes(self) -> openenoc_endpoint_interface_non_oetp_dma_tx_transferred_length_bytes_0x392615bcffa7f2a2_cls:
        """
        Property to access bytes field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.non_oetp_dma.tx.transferred_length.bytes[31 |
        |              |      :0]                                                                |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Actual number of bytes transferred. Hardware clears this field  |
        |              |      when the next request is accepted.</p>                             |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__bytes

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'bytes':'bytes',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_interface_non_oetp_dma_tx_transferred_length_bytes_0x392615bcffa7f2a2_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.non_oetp_dma.tx.transferred_length"
    @property
    def rdl_desc(self) -> str:
        return "Number of bytes transferred for the most recently accepted transmit request."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.bytes
        
        
    

    
    
class openenoc_endpoint_interface_non_oetp_dma_rx_buffer_address_0x1e1c0507927419bb_cls(RegReadWrite):
    """
    Class to represent a register in the register model

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
        
        self.__base:openenoc_endpoint_interface_non_oetp_dma_rx_buffer_address_base_neg_0xbdf1c67849ee26b_cls = openenoc_endpoint_interface_non_oetp_dma_rx_buffer_address_base_neg_0xbdf1c67849ee26b_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0, msb=31,
                low=0, high=31),
            misc_props=FieldMiscProps(
                default=0,
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
    def base(self) -> openenoc_endpoint_interface_non_oetp_dma_rx_buffer_address_base_neg_0xbdf1c67849ee26b_cls:
        """
        Property to access base field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.non_oetp_dma.rx.buffer_address.base[31:0]   |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>32-bit byte address of the first byte of the receive            |
        |              |      buffer.</p>                                                        |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__base

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'base':'base',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_interface_non_oetp_dma_rx_buffer_address_base_neg_0xbdf1c67849ee26b_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.non_oetp_dma.rx.buffer_address"
    @property
    def rdl_desc(self) -> str:
        return "Local memory address of the receive buffer for a non-oETP Ethernet frame."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.base
        
        
    

    
    
class openenoc_endpoint_interface_non_oetp_dma_rx_buffer_capacity_neg_0x6116b5ecbb32e21c_cls(RegReadWrite):
    """
    Class to represent a register in the register model

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
        
        self.__bytes:openenoc_endpoint_interface_non_oetp_dma_rx_buffer_capacity_bytes_neg_0x3da14d50150c8859_cls = openenoc_endpoint_interface_non_oetp_dma_rx_buffer_capacity_bytes_neg_0x3da14d50150c8859_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0, msb=31,
                low=0, high=31),
            misc_props=FieldMiscProps(
                default=0,
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
    def bytes(self) -> openenoc_endpoint_interface_non_oetp_dma_rx_buffer_capacity_bytes_neg_0x3da14d50150c8859_cls:
        """
        Property to access bytes field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.non_oetp_dma.rx.buffer_capacity.bytes[31:0] |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Receive-buffer capacity in bytes. Valid non-zero values shall   |
        |              |      not exceed info.max_dma_frame_size_bytes.</p>                      |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__bytes

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'bytes':'bytes',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_interface_non_oetp_dma_rx_buffer_capacity_bytes_neg_0x3da14d50150c8859_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.non_oetp_dma.rx.buffer_capacity"
    @property
    def rdl_desc(self) -> str:
        return "Capacity of the receive buffer for one complete non-oETP Ethernet frame."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.bytes
        
        
    

    
    
class openenoc_endpoint_interface_non_oetp_dma_rx_command_status_0x70be6bab06cc5089_cls(RegReadWrite):
    """
    Class to represent a register in the register model

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

    __slots__ : list[str] = ['__request', '__idle', '__armed', '__done', '__error', '__error_code']

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
        
        self.__request:openenoc_endpoint_interface_non_oetp_dma_rx_command_status_request_neg_0xd8d6051f536c356_cls = openenoc_endpoint_interface_non_oetp_dma_rx_command_status_request_neg_0xd8d6051f536c356_cls(
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
        self.__idle:openenoc_endpoint_interface_non_oetp_dma_rx_command_status_idle_neg_0x13bb001abf57c766_cls = openenoc_endpoint_interface_non_oetp_dma_rx_command_status_idle_neg_0x13bb001abf57c766_cls(
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
        self.__armed:openenoc_endpoint_interface_non_oetp_dma_rx_command_status_armed_neg_0x676c1af1ff7d2bb4_cls = openenoc_endpoint_interface_non_oetp_dma_rx_command_status_armed_neg_0x676c1af1ff7d2bb4_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=17, msb=17,
                low=17, high=17),
            misc_props=FieldMiscProps(
                default=None,
                is_volatile=True),
            logger_handle=logger_handle+'.armed',
            inst_name='armed',
            field_type=int)
        self.__done:openenoc_endpoint_interface_non_oetp_dma_rx_command_status_done_neg_0x41309f270480f35a_cls = openenoc_endpoint_interface_non_oetp_dma_rx_command_status_done_neg_0x41309f270480f35a_cls(
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
        self.__error:openenoc_endpoint_interface_non_oetp_dma_rx_command_status_error_0x16d15edb1ba03f16_cls = openenoc_endpoint_interface_non_oetp_dma_rx_command_status_error_0x16d15edb1ba03f16_cls(
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
        self.__error_code:openenoc_endpoint_interface_non_oetp_dma_rx_command_status_error_code_0x7b4d8ee5c1b7a654_cls = openenoc_endpoint_interface_non_oetp_dma_rx_command_status_error_code_0x7b4d8ee5c1b7a654_cls(
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
    def request(self) -> openenoc_endpoint_interface_non_oetp_dma_rx_command_status_request_neg_0xd8d6051f536c356_cls:
        """
        Property to access request field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.non_oetp_dma.rx.command_status.request      |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Writing one arms reception into the configured buffer. The      |
        |              |      field remains asserted until the DMA engine accepts the request.   |
        |              |      Hardware clears it upon acceptance; while the channel is busy, a   |
        |              |      newly asserted request remains pending.</p>                        |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__request
    @property
    def idle(self) -> openenoc_endpoint_interface_non_oetp_dma_rx_command_status_idle_neg_0x13bb001abf57c766_cls:
        """
        Property to access idle field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.non_oetp_dma.rx.command_status.idle         |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Indicates that the channel has no accepted receive request in   |
        |              |      progress. After acceptance, the channel may be armed and waiting   |
        |              |      for an eligible non-oETP frame or may be writing a received frame  |
        |              |      to memory.</p>                                                     |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__idle
    @property
    def armed(self) -> openenoc_endpoint_interface_non_oetp_dma_rx_command_status_armed_neg_0x676c1af1ff7d2bb4_cls:
        """
        Property to access armed field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.non_oetp_dma.rx.command_status.armed        |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Indicates that the accepted receive request is waiting for an   |
        |              |      eligible non-oETP Ethernet frame. Hardware sets this field when it |
        |              |      accepts a request and clears it when the first beat of the         |
        |              |      selected frame is accepted by the RX DMA datapath. The frame-      |
        |              |      routing logic uses this field to select the RX DMA path; otherwise |
        |              |      an accepted non-oETP frame is directed to the CSR AXI4-Stream      |
        |              |      sink.</p>                                                          |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__armed
    @property
    def done(self) -> openenoc_endpoint_interface_non_oetp_dma_rx_command_status_done_neg_0x41309f270480f35a_cls:
        """
        Property to access done field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.non_oetp_dma.rx.command_status.done         |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Sticky successful-completion flag. Hardware sets this field     |
        |              |      after a received frame has been written successfully and clears it |
        |              |      when the next request is accepted.</p>                             |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__done
    @property
    def error(self) -> openenoc_endpoint_interface_non_oetp_dma_rx_command_status_error_0x16d15edb1ba03f16_cls:
        """
        Property to access error field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.non_oetp_dma.rx.command_status.error        |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Sticky error-completion flag. Hardware sets this field when the |
        |              |      accepted receive request terminates with an error and clears it    |
        |              |      when the next request is accepted.</p>                             |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__error
    @property
    def error_code(self) -> openenoc_endpoint_interface_non_oetp_dma_rx_command_status_error_code_0x7b4d8ee5c1b7a654_cls:
        """
        Property to access error_code field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.non_oetp_dma.rx.command_status.error_code[3 |
        |              |      1:28]                                                              |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Sticky error code for the most recently completed receive       |
        |              |      transfer:<ul></p> <li>0: No error.</li> <li>1: Invalid DMA         |
        |              |      configuration or descriptor.</li> <li>2: AXI4-Stream length or     |
        |              |      TLAST error.</li> <li>3: Received frame exceeds the configured     |
        |              |      buffer capacity.</li> <li>4: AXI read SLVERR response.</li> <li>5: |
        |              |      AXI read DECERR response.</li> <li>6: AXI write SLVERR             |
        |              |      response.</li> <li>7: AXI write DECERR response.</li> <li>8-15:    |
        |              |      Reserved.</li> <p></ul> Hardware clears this field when the next   |
        |              |      request is accepted.</p>                                           |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__error_code

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'request':'request','idle':'idle','armed':'armed','done':'done','error':'error','error_code':'error_code',
            }

    
    
    
    
    
    
    # nodes:6
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["request"]) -> 'openenoc_endpoint_interface_non_oetp_dma_rx_command_status_request_neg_0xd8d6051f536c356_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["idle"]) -> 'openenoc_endpoint_interface_non_oetp_dma_rx_command_status_idle_neg_0x13bb001abf57c766_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["armed"]) -> 'openenoc_endpoint_interface_non_oetp_dma_rx_command_status_armed_neg_0x676c1af1ff7d2bb4_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["done"]) -> 'openenoc_endpoint_interface_non_oetp_dma_rx_command_status_done_neg_0x41309f270480f35a_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["error"]) -> 'openenoc_endpoint_interface_non_oetp_dma_rx_command_status_error_0x16d15edb1ba03f16_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["error_code"]) -> 'openenoc_endpoint_interface_non_oetp_dma_rx_command_status_error_code_0x7b4d8ee5c1b7a654_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_interface_non_oetp_dma_rx_command_status_request_neg_0xd8d6051f536c356_cls', 'openenoc_endpoint_interface_non_oetp_dma_rx_command_status_idle_neg_0x13bb001abf57c766_cls', 'openenoc_endpoint_interface_non_oetp_dma_rx_command_status_armed_neg_0x676c1af1ff7d2bb4_cls', 'openenoc_endpoint_interface_non_oetp_dma_rx_command_status_done_neg_0x41309f270480f35a_cls', 'openenoc_endpoint_interface_non_oetp_dma_rx_command_status_error_0x16d15edb1ba03f16_cls', 'openenoc_endpoint_interface_non_oetp_dma_rx_command_status_error_code_0x7b4d8ee5c1b7a654_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.non_oetp_dma.rx.command_status"
    @property
    def rdl_desc(self) -> str:
        return "Command and completion status for the non-oETP receive DMA channel."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.request
        yield self.idle
        yield self.armed
        yield self.done
        yield self.error
        yield self.error_code
        
        
    

    
    
class openenoc_endpoint_interface_non_oetp_dma_rx_received_length_0x68af296624048f0a_cls(RegReadOnly):
    """
    Class to represent a register in the register model

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

    __slots__ : list[str] = ['__bytes']

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
        
        self.__bytes:openenoc_endpoint_interface_non_oetp_dma_rx_received_length_bytes_0x3d06bd985ea57c4_cls = openenoc_endpoint_interface_non_oetp_dma_rx_received_length_bytes_0x3d06bd985ea57c4_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0, msb=31,
                low=0, high=31),
            misc_props=FieldMiscProps(
                default=None,
                is_volatile=True),
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
    def bytes(self) -> openenoc_endpoint_interface_non_oetp_dma_rx_received_length_bytes_0x3d06bd985ea57c4_cls:
        """
        Property to access bytes field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.non_oetp_dma.rx.received_length.bytes[31:0] |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Actual number of frame bytes written to the receive buffer.     |
        |              |      Hardware clears this field when the next request is accepted.</p>  |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__bytes

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'bytes':'bytes',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_interface_non_oetp_dma_rx_received_length_bytes_0x3d06bd985ea57c4_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.non_oetp_dma.rx.received_length"
    @property
    def rdl_desc(self) -> str:
        return "Length of the most recently received non-oETP Ethernet frame."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.bytes
        
        
    

    
    
class openenoc_endpoint_interface_peers_entry_mac_address_neg_0x4884f62c1c08602a_cls(RegReadWrite):
    """
    Class to represent a register in the register model

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
        
        self.__lo_word:openenoc_endpoint_interface_peers_entry_mac_address_lo_word_neg_0x4a418812823ae52_cls = openenoc_endpoint_interface_peers_entry_mac_address_lo_word_neg_0x4a418812823ae52_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0, msb=31,
                low=0, high=31),
            misc_props=FieldMiscProps(
                default=None,
                is_volatile=False),
            logger_handle=logger_handle+'.lo_word',
            inst_name='lo_word',
            field_type=int)
        self.__hi_word:openenoc_endpoint_interface_peers_entry_mac_address_hi_word_neg_0x697bdf29ce41edb5_cls = openenoc_endpoint_interface_peers_entry_mac_address_hi_word_neg_0x697bdf29ce41edb5_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=16,
                lsb=32, msb=47,
                low=32, high=47),
            misc_props=FieldMiscProps(
                default=None,
                is_volatile=False),
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
    def lo_word(self) -> openenoc_endpoint_interface_peers_entry_mac_address_lo_word_neg_0x4a418812823ae52_cls:
        """
        Property to access lo_word field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-                |
        |              |      1].mac_address.lo_word[31:0]                                       |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Lower 32 bits [31:0] of the 48-bit MAC address.</p>             |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__lo_word
    @property
    def hi_word(self) -> openenoc_endpoint_interface_peers_entry_mac_address_hi_word_neg_0x697bdf29ce41edb5_cls:
        """
        Property to access hi_word field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-                |
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
    def get_child_by_system_rdl_name(self, name: Literal["lo_word"]) -> 'openenoc_endpoint_interface_peers_entry_mac_address_lo_word_neg_0x4a418812823ae52_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["hi_word"]) -> 'openenoc_endpoint_interface_peers_entry_mac_address_hi_word_neg_0x697bdf29ce41edb5_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_interface_peers_entry_mac_address_lo_word_neg_0x4a418812823ae52_cls', 'openenoc_endpoint_interface_peers_entry_mac_address_hi_word_neg_0x697bdf29ce41edb5_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].mac_address"
    @property
    def rdl_desc(self) -> str:
        return "Remote peer 48-bit destination MAC address."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.lo_word
        yield self.hi_word
        
        
    

    
    
class openenoc_endpoint_interface_peers_entry_rmem_address_neg_0xe2bb09fed929943_cls(RegReadWrite):
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
        
        self.__offset:openenoc_endpoint_interface_peers_entry_rmem_address_offset_neg_0x660419d2f3cd0bf8_cls = openenoc_endpoint_interface_peers_entry_rmem_address_offset_neg_0x660419d2f3cd0bf8_cls(
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
    def offset(self) -> openenoc_endpoint_interface_peers_entry_rmem_address_offset_neg_0x660419d2f3cd0bf8_cls:
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

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_interface_peers_entry_rmem_address_offset_neg_0x660419d2f3cd0bf8_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].rmem_address"
    @property
    def rdl_desc(self) -> str:
        return "Address offset of the virtual memory region corresponding to the remote peer\u0027s memory."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.offset
        
        
    

    
    
class openenoc_endpoint_interface_peers_entry_local_address_neg_0x294cad689ba21566_cls(RegReadWrite):
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
        
        self.__base:openenoc_endpoint_interface_peers_entry_local_address_base_neg_0x132f4fe3d8257897_cls = openenoc_endpoint_interface_peers_entry_local_address_base_neg_0x132f4fe3d8257897_cls(
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
    def base(self) -> openenoc_endpoint_interface_peers_entry_local_address_base_neg_0x132f4fe3d8257897_cls:
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

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_interface_peers_entry_local_address_base_neg_0x132f4fe3d8257897_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].local_address"
    @property
    def rdl_desc(self) -> str:
        return "Start address of the local memory region for DMA transfers."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.base
        
        
    

    
    
class openenoc_endpoint_interface_peers_entry_remote_address_0x49f6b6b2b2e7c990_cls(RegReadWrite):
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
        
        self.__base:openenoc_endpoint_interface_peers_entry_remote_address_base_neg_0x3cdd60ce4b58408_cls = openenoc_endpoint_interface_peers_entry_remote_address_base_neg_0x3cdd60ce4b58408_cls(
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
    def base(self) -> openenoc_endpoint_interface_peers_entry_remote_address_base_neg_0x3cdd60ce4b58408_cls:
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

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_interface_peers_entry_remote_address_base_neg_0x3cdd60ce4b58408_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].remote_address"
    @property
    def rdl_desc(self) -> str:
        return "Start address of the remote peer\u0027s memory region."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.base
        
        
    

    
    
class openenoc_endpoint_interface_peers_entry_size_neg_0x7a929575eee9f562_cls(RegReadWrite):
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
        
        self.__bytes:openenoc_endpoint_interface_peers_entry_size_bytes_neg_0x3adc214cdc89f32e_cls = openenoc_endpoint_interface_peers_entry_size_bytes_neg_0x3adc214cdc89f32e_cls(
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
    def bytes(self) -> openenoc_endpoint_interface_peers_entry_size_bytes_neg_0x3adc214cdc89f32e_cls:
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

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_interface_peers_entry_size_bytes_neg_0x3adc214cdc89f32e_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].size"
    @property
    def rdl_desc(self) -> str:
        return "Size of the remote peer\u0027s memory region."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.bytes
        
        
    

    
    
class openenoc_endpoint_interface_peers_entry_dma_0x6db1d73803893a31_cls(RegReadWrite):
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

    __slots__ : list[str] = ['__mode', '__request', '__idle', '__done', '__error', '__error_code']

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
        
        self.__mode:openenoc_endpoint_interface_peers_entry_dma_mode_neg_0x391e258cd04f6f84_cls = openenoc_endpoint_interface_peers_entry_dma_mode_neg_0x391e258cd04f6f84_cls(
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
        self.__request:openenoc_endpoint_interface_peers_entry_dma_request_0x1b88f4382a6e6598_cls = openenoc_endpoint_interface_peers_entry_dma_request_0x1b88f4382a6e6598_cls(
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
        self.__idle:openenoc_endpoint_interface_peers_entry_dma_idle_0x36662f605b9df709_cls = openenoc_endpoint_interface_peers_entry_dma_idle_0x36662f605b9df709_cls(
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
        self.__done:openenoc_endpoint_interface_peers_entry_dma_done_neg_0x1c2b4b158bd12e74_cls = openenoc_endpoint_interface_peers_entry_dma_done_neg_0x1c2b4b158bd12e74_cls(
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
        self.__error:openenoc_endpoint_interface_peers_entry_dma_error_0x753daff6f507dbda_cls = openenoc_endpoint_interface_peers_entry_dma_error_0x753daff6f507dbda_cls(
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
        self.__error_code:openenoc_endpoint_interface_peers_entry_dma_error_code_0x4e849d7e18ec5152_cls = openenoc_endpoint_interface_peers_entry_dma_error_code_0x4e849d7e18ec5152_cls(
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
    def mode(self) -> openenoc_endpoint_interface_peers_entry_dma_mode_neg_0x391e258cd04f6f84_cls:
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
    def request(self) -> openenoc_endpoint_interface_peers_entry_dma_request_0x1b88f4382a6e6598_cls:
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
        |              |      shall keep the peer configuration stable while this field is       |
        |              |      asserted.</p>                                                      |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__request
    @property
    def idle(self) -> openenoc_endpoint_interface_peers_entry_dma_idle_0x36662f605b9df709_cls:
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
    def done(self) -> openenoc_endpoint_interface_peers_entry_dma_done_neg_0x1c2b4b158bd12e74_cls:
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
    def error(self) -> openenoc_endpoint_interface_peers_entry_dma_error_0x753daff6f507dbda_cls:
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
    def error_code(self) -> openenoc_endpoint_interface_peers_entry_dma_error_code_0x4e849d7e18ec5152_cls:
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
        return {'mode':'mode','request':'request','idle':'idle','done':'done','error':'error','error_code':'error_code',
            }

    
    
    
    
    
    
    # nodes:6
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["mode"]) -> 'openenoc_endpoint_interface_peers_entry_dma_mode_neg_0x391e258cd04f6f84_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["request"]) -> 'openenoc_endpoint_interface_peers_entry_dma_request_0x1b88f4382a6e6598_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["idle"]) -> 'openenoc_endpoint_interface_peers_entry_dma_idle_0x36662f605b9df709_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["done"]) -> 'openenoc_endpoint_interface_peers_entry_dma_done_neg_0x1c2b4b158bd12e74_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["error"]) -> 'openenoc_endpoint_interface_peers_entry_dma_error_0x753daff6f507dbda_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["error_code"]) -> 'openenoc_endpoint_interface_peers_entry_dma_error_code_0x4e849d7e18ec5152_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_interface_peers_entry_dma_mode_neg_0x391e258cd04f6f84_cls', 'openenoc_endpoint_interface_peers_entry_dma_request_0x1b88f4382a6e6598_cls', 'openenoc_endpoint_interface_peers_entry_dma_idle_0x36662f605b9df709_cls', 'openenoc_endpoint_interface_peers_entry_dma_done_neg_0x1c2b4b158bd12e74_cls', 'openenoc_endpoint_interface_peers_entry_dma_error_0x753daff6f507dbda_cls', 'openenoc_endpoint_interface_peers_entry_dma_error_code_0x4e849d7e18ec5152_cls', ]: ...

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
        yield self.request
        yield self.idle
        yield self.done
        yield self.error
        yield self.error_code
        
        
    


if __name__ == '__main__':
    pass