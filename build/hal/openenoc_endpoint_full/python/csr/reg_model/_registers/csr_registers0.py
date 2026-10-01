

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






from .fields import csr_test_reg_test_field_neg_0x2a591f0e5117bd86_cls
from .fields import openenoc_endpoint_interface_info_rmem_total_depth_0x691c38212010a163_cls
from .fields import openenoc_endpoint_interface_info_num_of_peers_neg_0x3ae7d2519a87aab5_cls
from .fields import openenoc_endpoint_interface_info_peer_dma_supported_neg_0x717ae1f7ff75b080_cls
from .fields import openenoc_endpoint_interface_info_non_oetp_dma_supported_0x2e2442a28d05c768_cls
from .fields import openenoc_endpoint_interface_info_direct_axis_supported_0x6d450aa403c40553_cls
from .fields import openenoc_endpoint_interface_info_rmem_supported_0x73c32023a23d32fb_cls
from .fields import openenoc_endpoint_interface_info_irq_supported_0x49797af9f74aa6e4_cls
from .fields import openenoc_endpoint_interface_info_max_dma_frame_size_bytes_0x5a00065fa5bd12f9_cls
from .fields import openenoc_endpoint_interface_config_mac_address_lo_word_neg_0x32c5a100e13691d5_cls
from .fields import openenoc_endpoint_interface_config_mac_address_hi_word_0x5d58fbc213117edf_cls
from .fields import openenoc_endpoint_interface_config_non_oetp_control_receive_mode_neg_0x57561c6fcabfe3f9_cls
from .fields import openenoc_endpoint_interface_axis_if_source_data_tdata_0x780b43d3631eee53_cls
from .fields import openenoc_endpoint_interface_axis_if_source_control_tvalid_0x3fc5c060358d8819_cls
from .fields import openenoc_endpoint_interface_axis_if_source_control_tlast_0x56791feb4f869721_cls
from .fields import openenoc_endpoint_interface_axis_if_source_control_tkeep_0x3a8668f529c0e3a9_cls
from .fields import openenoc_endpoint_interface_axis_if_source_status_tready_0x43396423ea79af64_cls
from .fields import openenoc_endpoint_interface_axis_if_sink_data_tdata_neg_0x3d4cdd5320bcb03d_cls
from .fields import openenoc_endpoint_interface_axis_if_sink_control_tready_neg_0x41a74e88ede986f3_cls
from .fields import openenoc_endpoint_interface_axis_if_sink_status_tvalid_0x298393fc3b549cb1_cls
from .fields import openenoc_endpoint_interface_axis_if_sink_status_tlast_neg_0x41933cb4e1d6a25d_cls
from .fields import openenoc_endpoint_interface_axis_if_sink_status_tkeep_0xc34022b77a26c1b_cls
from .fields import openenoc_endpoint_interface_non_oetp_dma_tx_buffer_address_base_neg_0x560f0cd00008fece_cls
from .fields import openenoc_endpoint_interface_non_oetp_dma_tx_frame_length_bytes_0x6e7e1f12e62dc96d_cls
from .fields import openenoc_endpoint_interface_non_oetp_dma_tx_command_status_request_neg_0x394d04bb06cb9afc_cls
from .fields import openenoc_endpoint_interface_non_oetp_dma_tx_command_status_idle_neg_0x13f5af5d0f01d1cb_cls
from .fields import openenoc_endpoint_interface_non_oetp_dma_tx_command_status_done_neg_0x3c04d9763163f90a_cls
from .fields import openenoc_endpoint_interface_non_oetp_dma_tx_command_status_error_neg_0x1c68e179e7cfe7fc_cls
from .fields import openenoc_endpoint_interface_non_oetp_dma_tx_command_status_error_code_neg_0x11295cf65b0b73f4_cls
from .fields import openenoc_endpoint_interface_non_oetp_dma_tx_transferred_length_bytes_neg_0xedbd1ffe5b40115_cls
from .fields import openenoc_endpoint_interface_non_oetp_dma_rx_buffer_address_base_0x5617bcc430358419_cls
from .fields import openenoc_endpoint_interface_non_oetp_dma_rx_buffer_capacity_bytes_neg_0x19384302be2619c8_cls
from .fields import openenoc_endpoint_interface_non_oetp_dma_rx_command_status_request_0x4522a7768784001d_cls
from .fields import openenoc_endpoint_interface_non_oetp_dma_rx_command_status_idle_0x57f04f8de916bf6f_cls
from .fields import openenoc_endpoint_interface_non_oetp_dma_rx_command_status_armed_neg_0x37392bf001485b11_cls
from .fields import openenoc_endpoint_interface_non_oetp_dma_rx_command_status_done_neg_0x507440407a7becfd_cls
from .fields import openenoc_endpoint_interface_non_oetp_dma_rx_command_status_error_0x5312aceed2c583a3_cls
from .fields import openenoc_endpoint_interface_non_oetp_dma_rx_command_status_error_code_neg_0x4b67038b6a593b5e_cls
from .fields import openenoc_endpoint_interface_non_oetp_dma_rx_received_length_bytes_0x51914132c8df5df1_cls
from .fields import openenoc_endpoint_interface_irq_control_global_enable_0x78468b6d77f5b0d6_cls
from .fields import openenoc_endpoint_interface_irq_control_clear_errors_0x34341631a90c3ac6_cls
from .fields import openenoc_endpoint_interface_irq_event_enable_peer_dma_complete_0x253a31e3e5f7cd5f_cls
from .fields import openenoc_endpoint_interface_irq_event_enable_non_oetp_dma_tx_complete_0xbfd03725ebc2482_cls
from .fields import openenoc_endpoint_interface_irq_event_enable_non_oetp_dma_rx_complete_0x3629e67722bfd09a_cls
from .fields import openenoc_endpoint_interface_irq_event_enable_non_oetp_direct_tx_complete_0xaae4fb94b3cca8d_cls
from .fields import openenoc_endpoint_interface_irq_event_enable_non_oetp_direct_rx_available_0x30d4ea837eee6b0e_cls
from .fields import openenoc_endpoint_interface_irq_status_claim_pending_neg_0x2a11b2b60d7ef56_cls
from .fields import openenoc_endpoint_interface_irq_status_credit_full_0x6cb990f26b9bde51_cls
from .fields import openenoc_endpoint_interface_irq_status_overflow_0x41b63e9cb4b127f_cls
from .fields import openenoc_endpoint_interface_irq_status_invalid_complete_0x8b83b4b300b8120_cls
from .fields import openenoc_endpoint_interface_irq_status_irq_asserted_0x56f68d1934c5ed65_cls
from .fields import openenoc_endpoint_interface_irq_status_fifo_level_0x3bf4209269d64cb7_cls
from .fields import openenoc_endpoint_interface_irq_status_reserved_count_0x3162a220699ff36f_cls
from .fields import openenoc_endpoint_interface_irq_claim_peer_idx_neg_0x69b2dc68a7396999_cls
from .fields import openenoc_endpoint_interface_irq_claim_source_neg_0x4f719fd90574e7c_cls
from .fields import openenoc_endpoint_interface_irq_claim_sequence_0x208c61200ea782a_cls
from .fields import openenoc_endpoint_interface_irq_claim_valid_neg_0x705488c4f88c1563_cls
from .fields import openenoc_endpoint_interface_irq_complete_peer_idx_0x3fada93a90ffed96_cls
from .fields import openenoc_endpoint_interface_irq_complete_source_0x1f753df5b7cec2c3_cls
from .fields import openenoc_endpoint_interface_irq_complete_sequence_0x7aeb1b299f2703b5_cls
from .fields import openenoc_endpoint_interface_irq_complete_valid_neg_0x33d28002c6c387ab_cls
from .fields import openenoc_endpoint_interface_peers_entry_mac_address_lo_word_0x51ddefabf71bf946_cls
from .fields import openenoc_endpoint_interface_peers_entry_mac_address_hi_word_0x74fd9945767a7256_cls

# register definitions
    
    
class csr_test_reg_neg_0x7a6411631989c1c_cls(RegReadWrite):
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
        
        self.__test_field:csr_test_reg_test_field_neg_0x2a591f0e5117bd86_cls = csr_test_reg_test_field_neg_0x2a591f0e5117bd86_cls(
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
    def test_field(self) -> csr_test_reg_test_field_neg_0x2a591f0e5117bd86_cls:
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

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'csr_test_reg_test_field_neg_0x2a591f0e5117bd86_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.test_reg"
    @property
    def rdl_desc(self) -> str:
        return "Test register"
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.test_field
        
        
    

    
    
class csr_regB_0x48cf0751ca438878_cls(RegReadWrite):
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
        
        
    

    
    
class openenoc_endpoint_interface_info_0x45d0a9e0e5f2aac5_cls(RegReadOnly):
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
        
        self.__rmem_total_depth:openenoc_endpoint_interface_info_rmem_total_depth_0x691c38212010a163_cls = openenoc_endpoint_interface_info_rmem_total_depth_0x691c38212010a163_cls(
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
        self.__num_of_peers:openenoc_endpoint_interface_info_num_of_peers_neg_0x3ae7d2519a87aab5_cls = openenoc_endpoint_interface_info_num_of_peers_neg_0x3ae7d2519a87aab5_cls(
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
        self.__peer_dma_supported:openenoc_endpoint_interface_info_peer_dma_supported_neg_0x717ae1f7ff75b080_cls = openenoc_endpoint_interface_info_peer_dma_supported_neg_0x717ae1f7ff75b080_cls(
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
        self.__non_oetp_dma_supported:openenoc_endpoint_interface_info_non_oetp_dma_supported_0x2e2442a28d05c768_cls = openenoc_endpoint_interface_info_non_oetp_dma_supported_0x2e2442a28d05c768_cls(
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
        self.__direct_axis_supported:openenoc_endpoint_interface_info_direct_axis_supported_0x6d450aa403c40553_cls = openenoc_endpoint_interface_info_direct_axis_supported_0x6d450aa403c40553_cls(
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
        self.__rmem_supported:openenoc_endpoint_interface_info_rmem_supported_0x73c32023a23d32fb_cls = openenoc_endpoint_interface_info_rmem_supported_0x73c32023a23d32fb_cls(
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
        self.__irq_supported:openenoc_endpoint_interface_info_irq_supported_0x49797af9f74aa6e4_cls = openenoc_endpoint_interface_info_irq_supported_0x49797af9f74aa6e4_cls(
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
        self.__max_dma_frame_size_bytes:openenoc_endpoint_interface_info_max_dma_frame_size_bytes_0x5a00065fa5bd12f9_cls = openenoc_endpoint_interface_info_max_dma_frame_size_bytes_0x5a00065fa5bd12f9_cls(
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
    def rmem_total_depth(self) -> openenoc_endpoint_interface_info_rmem_total_depth_0x691c38212010a163_cls:
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
    def num_of_peers(self) -> openenoc_endpoint_interface_info_num_of_peers_neg_0x3ae7d2519a87aab5_cls:
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
    def peer_dma_supported(self) -> openenoc_endpoint_interface_info_peer_dma_supported_neg_0x717ae1f7ff75b080_cls:
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
    def non_oetp_dma_supported(self) -> openenoc_endpoint_interface_info_non_oetp_dma_supported_0x2e2442a28d05c768_cls:
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
    def direct_axis_supported(self) -> openenoc_endpoint_interface_info_direct_axis_supported_0x6d450aa403c40553_cls:
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
    def rmem_supported(self) -> openenoc_endpoint_interface_info_rmem_supported_0x73c32023a23d32fb_cls:
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
    def irq_supported(self) -> openenoc_endpoint_interface_info_irq_supported_0x49797af9f74aa6e4_cls:
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
    def max_dma_frame_size_bytes(self) -> openenoc_endpoint_interface_info_max_dma_frame_size_bytes_0x5a00065fa5bd12f9_cls:
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
    def get_child_by_system_rdl_name(self, name: Literal["rmem_total_depth"]) -> 'openenoc_endpoint_interface_info_rmem_total_depth_0x691c38212010a163_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["num_of_peers"]) -> 'openenoc_endpoint_interface_info_num_of_peers_neg_0x3ae7d2519a87aab5_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["peer_dma_supported"]) -> 'openenoc_endpoint_interface_info_peer_dma_supported_neg_0x717ae1f7ff75b080_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["non_oetp_dma_supported"]) -> 'openenoc_endpoint_interface_info_non_oetp_dma_supported_0x2e2442a28d05c768_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["direct_axis_supported"]) -> 'openenoc_endpoint_interface_info_direct_axis_supported_0x6d450aa403c40553_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["rmem_supported"]) -> 'openenoc_endpoint_interface_info_rmem_supported_0x73c32023a23d32fb_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["irq_supported"]) -> 'openenoc_endpoint_interface_info_irq_supported_0x49797af9f74aa6e4_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["max_dma_frame_size_bytes"]) -> 'openenoc_endpoint_interface_info_max_dma_frame_size_bytes_0x5a00065fa5bd12f9_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_interface_info_rmem_total_depth_0x691c38212010a163_cls', 'openenoc_endpoint_interface_info_num_of_peers_neg_0x3ae7d2519a87aab5_cls', 'openenoc_endpoint_interface_info_peer_dma_supported_neg_0x717ae1f7ff75b080_cls', 'openenoc_endpoint_interface_info_non_oetp_dma_supported_0x2e2442a28d05c768_cls', 'openenoc_endpoint_interface_info_direct_axis_supported_0x6d450aa403c40553_cls', 'openenoc_endpoint_interface_info_rmem_supported_0x73c32023a23d32fb_cls', 'openenoc_endpoint_interface_info_irq_supported_0x49797af9f74aa6e4_cls', 'openenoc_endpoint_interface_info_max_dma_frame_size_bytes_0x5a00065fa5bd12f9_cls', ]: ...

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
        
        
    

    
    
class openenoc_endpoint_interface_config_mac_address_0x1b631cb1d0cb7e0c_cls(RegReadWrite):
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
        
        self.__lo_word:openenoc_endpoint_interface_config_mac_address_lo_word_neg_0x32c5a100e13691d5_cls = openenoc_endpoint_interface_config_mac_address_lo_word_neg_0x32c5a100e13691d5_cls(
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
        self.__hi_word:openenoc_endpoint_interface_config_mac_address_hi_word_0x5d58fbc213117edf_cls = openenoc_endpoint_interface_config_mac_address_hi_word_0x5d58fbc213117edf_cls(
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
    def lo_word(self) -> openenoc_endpoint_interface_config_mac_address_lo_word_neg_0x32c5a100e13691d5_cls:
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
    def hi_word(self) -> openenoc_endpoint_interface_config_mac_address_hi_word_0x5d58fbc213117edf_cls:
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
    def get_child_by_system_rdl_name(self, name: Literal["lo_word"]) -> 'openenoc_endpoint_interface_config_mac_address_lo_word_neg_0x32c5a100e13691d5_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["hi_word"]) -> 'openenoc_endpoint_interface_config_mac_address_hi_word_0x5d58fbc213117edf_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_interface_config_mac_address_lo_word_neg_0x32c5a100e13691d5_cls', 'openenoc_endpoint_interface_config_mac_address_hi_word_0x5d58fbc213117edf_cls', ]: ...

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
        
        
    

    
    
class openenoc_endpoint_interface_config_non_oetp_control_neg_0x7a0eb09718dec19d_cls(RegReadWrite):
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
        
        self.__receive_mode:openenoc_endpoint_interface_config_non_oetp_control_receive_mode_neg_0x57561c6fcabfe3f9_cls = openenoc_endpoint_interface_config_non_oetp_control_receive_mode_neg_0x57561c6fcabfe3f9_cls(
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
    def receive_mode(self) -> openenoc_endpoint_interface_config_non_oetp_control_receive_mode_neg_0x57561c6fcabfe3f9_cls:
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
        |              |      broadcast frames.</li> <li>2: Multicast mode. Accept the same      |
        |              |      frames as filtered mode, plus all multicast-addressed frames.</li> |
        |              |      <li>3: Promiscuous mode. Accept all non-oETP Ethernet frames.</li> |
        |              |      <p></ul> An accepted frame is directed to the non-oETP RX DMA      |
        |              |      channel when that channel is armed; otherwise it is directed to    |
        |              |      the CSR AXI4-Stream sink.</p>                                      |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__receive_mode

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'receive_mode':'receive_mode',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_interface_config_non_oetp_control_receive_mode_neg_0x57561c6fcabfe3f9_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.config.non_oetp_control"
    @property
    def rdl_desc(self) -> str:
        return "Receive policy for Ethernet frames that do not carry oETP traffic."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.receive_mode
        
        
    

    
    
class openenoc_endpoint_interface_axis_if_source_data_0x76101c812ad76c33_cls(RegReadWrite):
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
        
        self.__tdata:openenoc_endpoint_interface_axis_if_source_data_tdata_0x780b43d3631eee53_cls = openenoc_endpoint_interface_axis_if_source_data_tdata_0x780b43d3631eee53_cls(
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
    def tdata(self) -> openenoc_endpoint_interface_axis_if_source_data_tdata_0x780b43d3631eee53_cls:
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

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_interface_axis_if_source_data_tdata_0x780b43d3631eee53_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.axis_if.source.data"
    @property
    def rdl_desc(self) -> str:
        return "Data register for the AXI4-Stream source interface."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.tdata
        
        
    

    
    
class openenoc_endpoint_interface_axis_if_source_control_0x333790cff961b9b7_cls(RegReadWrite):
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
        
        self.__tvalid:openenoc_endpoint_interface_axis_if_source_control_tvalid_0x3fc5c060358d8819_cls = openenoc_endpoint_interface_axis_if_source_control_tvalid_0x3fc5c060358d8819_cls(
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
        self.__tlast:openenoc_endpoint_interface_axis_if_source_control_tlast_0x56791feb4f869721_cls = openenoc_endpoint_interface_axis_if_source_control_tlast_0x56791feb4f869721_cls(
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
        self.__tkeep:openenoc_endpoint_interface_axis_if_source_control_tkeep_0x3a8668f529c0e3a9_cls = openenoc_endpoint_interface_axis_if_source_control_tkeep_0x3a8668f529c0e3a9_cls(
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
    def tvalid(self) -> openenoc_endpoint_interface_axis_if_source_control_tvalid_0x3fc5c060358d8819_cls:
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
    def tlast(self) -> openenoc_endpoint_interface_axis_if_source_control_tlast_0x56791feb4f869721_cls:
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
    def tkeep(self) -> openenoc_endpoint_interface_axis_if_source_control_tkeep_0x3a8668f529c0e3a9_cls:
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
    def get_child_by_system_rdl_name(self, name: Literal["tvalid"]) -> 'openenoc_endpoint_interface_axis_if_source_control_tvalid_0x3fc5c060358d8819_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["tlast"]) -> 'openenoc_endpoint_interface_axis_if_source_control_tlast_0x56791feb4f869721_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["tkeep"]) -> 'openenoc_endpoint_interface_axis_if_source_control_tkeep_0x3a8668f529c0e3a9_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_interface_axis_if_source_control_tvalid_0x3fc5c060358d8819_cls', 'openenoc_endpoint_interface_axis_if_source_control_tlast_0x56791feb4f869721_cls', 'openenoc_endpoint_interface_axis_if_source_control_tkeep_0x3a8668f529c0e3a9_cls', ]: ...

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
        
        
    

    
    
class openenoc_endpoint_interface_axis_if_source_status_neg_0x67291cf66495a15a_cls(RegReadOnly):
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
        
        self.__tready:openenoc_endpoint_interface_axis_if_source_status_tready_0x43396423ea79af64_cls = openenoc_endpoint_interface_axis_if_source_status_tready_0x43396423ea79af64_cls(
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
    def tready(self) -> openenoc_endpoint_interface_axis_if_source_status_tready_0x43396423ea79af64_cls:
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

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_interface_axis_if_source_status_tready_0x43396423ea79af64_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.axis_if.source.status"
    @property
    def rdl_desc(self) -> str:
        return "Status register for the AXI4-Stream source interface."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.tready
        
        
    

    
    
class openenoc_endpoint_interface_axis_if_sink_data_0x4e017d9cf1834733_cls(RegReadOnly):
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
        
        self.__tdata:openenoc_endpoint_interface_axis_if_sink_data_tdata_neg_0x3d4cdd5320bcb03d_cls = openenoc_endpoint_interface_axis_if_sink_data_tdata_neg_0x3d4cdd5320bcb03d_cls(
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
    def tdata(self) -> openenoc_endpoint_interface_axis_if_sink_data_tdata_neg_0x3d4cdd5320bcb03d_cls:
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

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_interface_axis_if_sink_data_tdata_neg_0x3d4cdd5320bcb03d_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.axis_if.sink.data"
    @property
    def rdl_desc(self) -> str:
        return "Data register for the AXI4-Stream sink interface."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.tdata
        
        
    

    
    
class openenoc_endpoint_interface_axis_if_sink_control_neg_0x50c06f58eadcb1f4_cls(RegReadWrite):
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
        
        self.__tready:openenoc_endpoint_interface_axis_if_sink_control_tready_neg_0x41a74e88ede986f3_cls = openenoc_endpoint_interface_axis_if_sink_control_tready_neg_0x41a74e88ede986f3_cls(
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
    def tready(self) -> openenoc_endpoint_interface_axis_if_sink_control_tready_neg_0x41a74e88ede986f3_cls:
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

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_interface_axis_if_sink_control_tready_neg_0x41a74e88ede986f3_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.axis_if.sink.control"
    @property
    def rdl_desc(self) -> str:
        return "Control register for the AXI4-Stream sink interface."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.tready
        
        
    

    
    
class openenoc_endpoint_interface_axis_if_sink_status_0x247e609445ed2fe6_cls(RegReadOnly):
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
        
        self.__tvalid:openenoc_endpoint_interface_axis_if_sink_status_tvalid_0x298393fc3b549cb1_cls = openenoc_endpoint_interface_axis_if_sink_status_tvalid_0x298393fc3b549cb1_cls(
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
        self.__tlast:openenoc_endpoint_interface_axis_if_sink_status_tlast_neg_0x41933cb4e1d6a25d_cls = openenoc_endpoint_interface_axis_if_sink_status_tlast_neg_0x41933cb4e1d6a25d_cls(
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
        self.__tkeep:openenoc_endpoint_interface_axis_if_sink_status_tkeep_0xc34022b77a26c1b_cls = openenoc_endpoint_interface_axis_if_sink_status_tkeep_0xc34022b77a26c1b_cls(
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
    def tvalid(self) -> openenoc_endpoint_interface_axis_if_sink_status_tvalid_0x298393fc3b549cb1_cls:
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
    def tlast(self) -> openenoc_endpoint_interface_axis_if_sink_status_tlast_neg_0x41933cb4e1d6a25d_cls:
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
    def tkeep(self) -> openenoc_endpoint_interface_axis_if_sink_status_tkeep_0xc34022b77a26c1b_cls:
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
    def get_child_by_system_rdl_name(self, name: Literal["tvalid"]) -> 'openenoc_endpoint_interface_axis_if_sink_status_tvalid_0x298393fc3b549cb1_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["tlast"]) -> 'openenoc_endpoint_interface_axis_if_sink_status_tlast_neg_0x41933cb4e1d6a25d_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["tkeep"]) -> 'openenoc_endpoint_interface_axis_if_sink_status_tkeep_0xc34022b77a26c1b_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_interface_axis_if_sink_status_tvalid_0x298393fc3b549cb1_cls', 'openenoc_endpoint_interface_axis_if_sink_status_tlast_neg_0x41933cb4e1d6a25d_cls', 'openenoc_endpoint_interface_axis_if_sink_status_tkeep_0xc34022b77a26c1b_cls', ]: ...

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
        
        
    

    
    
class openenoc_endpoint_interface_non_oetp_dma_tx_buffer_address_0x3fd54d286520186e_cls(RegReadWrite):
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
        
        self.__base:openenoc_endpoint_interface_non_oetp_dma_tx_buffer_address_base_neg_0x560f0cd00008fece_cls = openenoc_endpoint_interface_non_oetp_dma_tx_buffer_address_base_neg_0x560f0cd00008fece_cls(
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
    def base(self) -> openenoc_endpoint_interface_non_oetp_dma_tx_buffer_address_base_neg_0x560f0cd00008fece_cls:
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

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_interface_non_oetp_dma_tx_buffer_address_base_neg_0x560f0cd00008fece_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.non_oetp_dma.tx.buffer_address"
    @property
    def rdl_desc(self) -> str:
        return "Local memory address of the non-oETP Ethernet frame to transmit."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.base
        
        
    

    
    
class openenoc_endpoint_interface_non_oetp_dma_tx_frame_length_neg_0x662c564b9c440614_cls(RegReadWrite):
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
        
        self.__bytes:openenoc_endpoint_interface_non_oetp_dma_tx_frame_length_bytes_0x6e7e1f12e62dc96d_cls = openenoc_endpoint_interface_non_oetp_dma_tx_frame_length_bytes_0x6e7e1f12e62dc96d_cls(
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
    def bytes(self) -> openenoc_endpoint_interface_non_oetp_dma_tx_frame_length_bytes_0x6e7e1f12e62dc96d_cls:
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

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_interface_non_oetp_dma_tx_frame_length_bytes_0x6e7e1f12e62dc96d_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.non_oetp_dma.tx.frame_length"
    @property
    def rdl_desc(self) -> str:
        return "Length of the complete non-oETP Ethernet frame to transmit."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.bytes
        
        
    

    
    
class openenoc_endpoint_interface_non_oetp_dma_tx_command_status_0x235a9c77226fd79f_cls(RegReadWrite):
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
        
        self.__request:openenoc_endpoint_interface_non_oetp_dma_tx_command_status_request_neg_0x394d04bb06cb9afc_cls = openenoc_endpoint_interface_non_oetp_dma_tx_command_status_request_neg_0x394d04bb06cb9afc_cls(
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
        self.__idle:openenoc_endpoint_interface_non_oetp_dma_tx_command_status_idle_neg_0x13f5af5d0f01d1cb_cls = openenoc_endpoint_interface_non_oetp_dma_tx_command_status_idle_neg_0x13f5af5d0f01d1cb_cls(
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
        self.__done:openenoc_endpoint_interface_non_oetp_dma_tx_command_status_done_neg_0x3c04d9763163f90a_cls = openenoc_endpoint_interface_non_oetp_dma_tx_command_status_done_neg_0x3c04d9763163f90a_cls(
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
        self.__error:openenoc_endpoint_interface_non_oetp_dma_tx_command_status_error_neg_0x1c68e179e7cfe7fc_cls = openenoc_endpoint_interface_non_oetp_dma_tx_command_status_error_neg_0x1c68e179e7cfe7fc_cls(
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
        self.__error_code:openenoc_endpoint_interface_non_oetp_dma_tx_command_status_error_code_neg_0x11295cf65b0b73f4_cls = openenoc_endpoint_interface_non_oetp_dma_tx_command_status_error_code_neg_0x11295cf65b0b73f4_cls(
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
    def request(self) -> openenoc_endpoint_interface_non_oetp_dma_tx_command_status_request_neg_0x394d04bb06cb9afc_cls:
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
        |              |      newly asserted request remains pending. Software or an RTL         |
        |              |      controller shall read the completion status and transferred length |
        |              |      of the previous request before asserting this field for the next   |
        |              |      request.</p>                                                       |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__request
    @property
    def idle(self) -> openenoc_endpoint_interface_non_oetp_dma_tx_command_status_idle_neg_0x13f5af5d0f01d1cb_cls:
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
    def done(self) -> openenoc_endpoint_interface_non_oetp_dma_tx_command_status_done_neg_0x3c04d9763163f90a_cls:
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
    def error(self) -> openenoc_endpoint_interface_non_oetp_dma_tx_command_status_error_neg_0x1c68e179e7cfe7fc_cls:
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
    def error_code(self) -> openenoc_endpoint_interface_non_oetp_dma_tx_command_status_error_code_neg_0x11295cf65b0b73f4_cls:
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
    def get_child_by_system_rdl_name(self, name: Literal["request"]) -> 'openenoc_endpoint_interface_non_oetp_dma_tx_command_status_request_neg_0x394d04bb06cb9afc_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["idle"]) -> 'openenoc_endpoint_interface_non_oetp_dma_tx_command_status_idle_neg_0x13f5af5d0f01d1cb_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["done"]) -> 'openenoc_endpoint_interface_non_oetp_dma_tx_command_status_done_neg_0x3c04d9763163f90a_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["error"]) -> 'openenoc_endpoint_interface_non_oetp_dma_tx_command_status_error_neg_0x1c68e179e7cfe7fc_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["error_code"]) -> 'openenoc_endpoint_interface_non_oetp_dma_tx_command_status_error_code_neg_0x11295cf65b0b73f4_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_interface_non_oetp_dma_tx_command_status_request_neg_0x394d04bb06cb9afc_cls', 'openenoc_endpoint_interface_non_oetp_dma_tx_command_status_idle_neg_0x13f5af5d0f01d1cb_cls', 'openenoc_endpoint_interface_non_oetp_dma_tx_command_status_done_neg_0x3c04d9763163f90a_cls', 'openenoc_endpoint_interface_non_oetp_dma_tx_command_status_error_neg_0x1c68e179e7cfe7fc_cls', 'openenoc_endpoint_interface_non_oetp_dma_tx_command_status_error_code_neg_0x11295cf65b0b73f4_cls', ]: ...

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
        
        
    

    
    
class openenoc_endpoint_interface_non_oetp_dma_tx_transferred_length_0x6d9a9983e701ee64_cls(RegReadOnly):
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
        
        self.__bytes:openenoc_endpoint_interface_non_oetp_dma_tx_transferred_length_bytes_neg_0xedbd1ffe5b40115_cls = openenoc_endpoint_interface_non_oetp_dma_tx_transferred_length_bytes_neg_0xedbd1ffe5b40115_cls(
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
    def bytes(self) -> openenoc_endpoint_interface_non_oetp_dma_tx_transferred_length_bytes_neg_0xedbd1ffe5b40115_cls:
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

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_interface_non_oetp_dma_tx_transferred_length_bytes_neg_0xedbd1ffe5b40115_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.non_oetp_dma.tx.transferred_length"
    @property
    def rdl_desc(self) -> str:
        return "Number of bytes transferred for the most recently accepted transmit\nrequest."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.bytes
        
        
    

    
    
class openenoc_endpoint_interface_non_oetp_dma_rx_buffer_address_0x140af2827a957c08_cls(RegReadWrite):
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
        
        self.__base:openenoc_endpoint_interface_non_oetp_dma_rx_buffer_address_base_0x5617bcc430358419_cls = openenoc_endpoint_interface_non_oetp_dma_rx_buffer_address_base_0x5617bcc430358419_cls(
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
    def base(self) -> openenoc_endpoint_interface_non_oetp_dma_rx_buffer_address_base_0x5617bcc430358419_cls:
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

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_interface_non_oetp_dma_rx_buffer_address_base_0x5617bcc430358419_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.non_oetp_dma.rx.buffer_address"
    @property
    def rdl_desc(self) -> str:
        return "Local memory address of the receive buffer for a non-oETP Ethernet frame."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.base
        
        
    

    
    
class openenoc_endpoint_interface_non_oetp_dma_rx_buffer_capacity_neg_0x33a2912ec54e4d6f_cls(RegReadWrite):
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
        
        self.__bytes:openenoc_endpoint_interface_non_oetp_dma_rx_buffer_capacity_bytes_neg_0x19384302be2619c8_cls = openenoc_endpoint_interface_non_oetp_dma_rx_buffer_capacity_bytes_neg_0x19384302be2619c8_cls(
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
    def bytes(self) -> openenoc_endpoint_interface_non_oetp_dma_rx_buffer_capacity_bytes_neg_0x19384302be2619c8_cls:
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

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_interface_non_oetp_dma_rx_buffer_capacity_bytes_neg_0x19384302be2619c8_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.non_oetp_dma.rx.buffer_capacity"
    @property
    def rdl_desc(self) -> str:
        return "Capacity of the receive buffer for one complete non-oETP Ethernet frame."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.bytes
        
        
    

    
    
class openenoc_endpoint_interface_non_oetp_dma_rx_command_status_0x1462bf4b75842713_cls(RegReadWrite):
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
        
        self.__request:openenoc_endpoint_interface_non_oetp_dma_rx_command_status_request_0x4522a7768784001d_cls = openenoc_endpoint_interface_non_oetp_dma_rx_command_status_request_0x4522a7768784001d_cls(
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
        self.__idle:openenoc_endpoint_interface_non_oetp_dma_rx_command_status_idle_0x57f04f8de916bf6f_cls = openenoc_endpoint_interface_non_oetp_dma_rx_command_status_idle_0x57f04f8de916bf6f_cls(
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
        self.__armed:openenoc_endpoint_interface_non_oetp_dma_rx_command_status_armed_neg_0x37392bf001485b11_cls = openenoc_endpoint_interface_non_oetp_dma_rx_command_status_armed_neg_0x37392bf001485b11_cls(
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
        self.__done:openenoc_endpoint_interface_non_oetp_dma_rx_command_status_done_neg_0x507440407a7becfd_cls = openenoc_endpoint_interface_non_oetp_dma_rx_command_status_done_neg_0x507440407a7becfd_cls(
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
        self.__error:openenoc_endpoint_interface_non_oetp_dma_rx_command_status_error_0x5312aceed2c583a3_cls = openenoc_endpoint_interface_non_oetp_dma_rx_command_status_error_0x5312aceed2c583a3_cls(
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
        self.__error_code:openenoc_endpoint_interface_non_oetp_dma_rx_command_status_error_code_neg_0x4b67038b6a593b5e_cls = openenoc_endpoint_interface_non_oetp_dma_rx_command_status_error_code_neg_0x4b67038b6a593b5e_cls(
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
    def request(self) -> openenoc_endpoint_interface_non_oetp_dma_rx_command_status_request_0x4522a7768784001d_cls:
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
        |              |      newly asserted request remains pending. Software or an RTL         |
        |              |      controller shall read the completion status and received length of |
        |              |      the previous request before asserting this field for the next      |
        |              |      request.</p>                                                       |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__request
    @property
    def idle(self) -> openenoc_endpoint_interface_non_oetp_dma_rx_command_status_idle_0x57f04f8de916bf6f_cls:
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
    def armed(self) -> openenoc_endpoint_interface_non_oetp_dma_rx_command_status_armed_neg_0x37392bf001485b11_cls:
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
    def done(self) -> openenoc_endpoint_interface_non_oetp_dma_rx_command_status_done_neg_0x507440407a7becfd_cls:
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
    def error(self) -> openenoc_endpoint_interface_non_oetp_dma_rx_command_status_error_0x5312aceed2c583a3_cls:
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
    def error_code(self) -> openenoc_endpoint_interface_non_oetp_dma_rx_command_status_error_code_neg_0x4b67038b6a593b5e_cls:
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
    def get_child_by_system_rdl_name(self, name: Literal["request"]) -> 'openenoc_endpoint_interface_non_oetp_dma_rx_command_status_request_0x4522a7768784001d_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["idle"]) -> 'openenoc_endpoint_interface_non_oetp_dma_rx_command_status_idle_0x57f04f8de916bf6f_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["armed"]) -> 'openenoc_endpoint_interface_non_oetp_dma_rx_command_status_armed_neg_0x37392bf001485b11_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["done"]) -> 'openenoc_endpoint_interface_non_oetp_dma_rx_command_status_done_neg_0x507440407a7becfd_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["error"]) -> 'openenoc_endpoint_interface_non_oetp_dma_rx_command_status_error_0x5312aceed2c583a3_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["error_code"]) -> 'openenoc_endpoint_interface_non_oetp_dma_rx_command_status_error_code_neg_0x4b67038b6a593b5e_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_interface_non_oetp_dma_rx_command_status_request_0x4522a7768784001d_cls', 'openenoc_endpoint_interface_non_oetp_dma_rx_command_status_idle_0x57f04f8de916bf6f_cls', 'openenoc_endpoint_interface_non_oetp_dma_rx_command_status_armed_neg_0x37392bf001485b11_cls', 'openenoc_endpoint_interface_non_oetp_dma_rx_command_status_done_neg_0x507440407a7becfd_cls', 'openenoc_endpoint_interface_non_oetp_dma_rx_command_status_error_0x5312aceed2c583a3_cls', 'openenoc_endpoint_interface_non_oetp_dma_rx_command_status_error_code_neg_0x4b67038b6a593b5e_cls', ]: ...

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
        
        
    

    
    
class openenoc_endpoint_interface_non_oetp_dma_rx_received_length_neg_0x71fb3eaa3c74d770_cls(RegReadOnly):
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
        
        self.__bytes:openenoc_endpoint_interface_non_oetp_dma_rx_received_length_bytes_0x51914132c8df5df1_cls = openenoc_endpoint_interface_non_oetp_dma_rx_received_length_bytes_0x51914132c8df5df1_cls(
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
    def bytes(self) -> openenoc_endpoint_interface_non_oetp_dma_rx_received_length_bytes_0x51914132c8df5df1_cls:
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

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_interface_non_oetp_dma_rx_received_length_bytes_0x51914132c8df5df1_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.non_oetp_dma.rx.received_length"
    @property
    def rdl_desc(self) -> str:
        return "Length of the most recently received non-oETP Ethernet frame."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.bytes
        
        
    

    
    
class openenoc_endpoint_interface_irq_control_0x1d53c9b2400e1501_cls(RegReadWrite):
    """
    Class to represent a register in the register model

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

    __slots__ : list[str] = ['__global_enable', '__clear_errors']

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
        
        self.__global_enable:openenoc_endpoint_interface_irq_control_global_enable_0x78468b6d77f5b0d6_cls = openenoc_endpoint_interface_irq_control_global_enable_0x78468b6d77f5b0d6_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=0, msb=0,
                low=0, high=0),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.global_enable',
            inst_name='global_enable',
            field_type=int)
        self.__clear_errors:openenoc_endpoint_interface_irq_control_clear_errors_0x34341631a90c3ac6_cls = openenoc_endpoint_interface_irq_control_clear_errors_0x34341631a90c3ac6_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=8, msb=8,
                low=8, high=8),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.clear_errors',
            inst_name='clear_errors',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def global_enable(self) -> openenoc_endpoint_interface_irq_control_global_enable_0x78468b6d77f5b0d6_cls:
        """
        Property to access global_enable field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.irq.control.global_enable                   |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Enables the physical endpoint IRQ output. Clearing this field   |
        |              |      masks the output but does not prevent enabled events from being    |
        |              |      queued. Event capture is controlled by irq.event_enable and, for   |
        |              |      peer DMA, by the selected peer's dma.irq_enable field.</p>         |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__global_enable
    @property
    def clear_errors(self) -> openenoc_endpoint_interface_irq_control_clear_errors_0x34341631a90c3ac6_cls:
        """
        Property to access clear_errors field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.irq.control.clear_errors                    |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Writing one requests clearing of the sticky irq.status.overflow |
        |              |      and irq.status.invalid_complete flags. The field remains asserted  |
        |              |      until hardware accepts the request and clears it.</p>              |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__clear_errors

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'global_enable':'global_enable','clear_errors':'clear_errors',
            }

    
    
    
    
    
    
    # nodes:2
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["global_enable"]) -> 'openenoc_endpoint_interface_irq_control_global_enable_0x78468b6d77f5b0d6_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["clear_errors"]) -> 'openenoc_endpoint_interface_irq_control_clear_errors_0x34341631a90c3ac6_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_interface_irq_control_global_enable_0x78468b6d77f5b0d6_cls', 'openenoc_endpoint_interface_irq_control_clear_errors_0x34341631a90c3ac6_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.irq.control"
    @property
    def rdl_desc(self) -> str:
        return "Global interrupt-output control and interrupt-controller maintenance requests."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.global_enable
        yield self.clear_errors
        
        
    

    
    
class openenoc_endpoint_interface_irq_event_enable_neg_0x1d4a5fd091d48df_cls(RegReadWrite):
    """
    Class to represent a register in the register model

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

    __slots__ : list[str] = ['__peer_dma_complete', '__non_oetp_dma_tx_complete', '__non_oetp_dma_rx_complete', '__non_oetp_direct_tx_complete', '__non_oetp_direct_rx_available']

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
        
        self.__peer_dma_complete:openenoc_endpoint_interface_irq_event_enable_peer_dma_complete_0x253a31e3e5f7cd5f_cls = openenoc_endpoint_interface_irq_event_enable_peer_dma_complete_0x253a31e3e5f7cd5f_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=0, msb=0,
                low=0, high=0),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.peer_dma_complete',
            inst_name='peer_dma_complete',
            field_type=int)
        self.__non_oetp_dma_tx_complete:openenoc_endpoint_interface_irq_event_enable_non_oetp_dma_tx_complete_0xbfd03725ebc2482_cls = openenoc_endpoint_interface_irq_event_enable_non_oetp_dma_tx_complete_0xbfd03725ebc2482_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=1, msb=1,
                low=1, high=1),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.non_oetp_dma_tx_complete',
            inst_name='non_oetp_dma_tx_complete',
            field_type=int)
        self.__non_oetp_dma_rx_complete:openenoc_endpoint_interface_irq_event_enable_non_oetp_dma_rx_complete_0x3629e67722bfd09a_cls = openenoc_endpoint_interface_irq_event_enable_non_oetp_dma_rx_complete_0x3629e67722bfd09a_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=2, msb=2,
                low=2, high=2),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.non_oetp_dma_rx_complete',
            inst_name='non_oetp_dma_rx_complete',
            field_type=int)
        self.__non_oetp_direct_tx_complete:openenoc_endpoint_interface_irq_event_enable_non_oetp_direct_tx_complete_0xaae4fb94b3cca8d_cls = openenoc_endpoint_interface_irq_event_enable_non_oetp_direct_tx_complete_0xaae4fb94b3cca8d_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=3, msb=3,
                low=3, high=3),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.non_oetp_direct_tx_complete',
            inst_name='non_oetp_direct_tx_complete',
            field_type=int)
        self.__non_oetp_direct_rx_available:openenoc_endpoint_interface_irq_event_enable_non_oetp_direct_rx_available_0x30d4ea837eee6b0e_cls = openenoc_endpoint_interface_irq_event_enable_non_oetp_direct_rx_available_0x30d4ea837eee6b0e_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=4, msb=4,
                low=4, high=4),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.non_oetp_direct_rx_available',
            inst_name='non_oetp_direct_rx_available',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def peer_dma_complete(self) -> openenoc_endpoint_interface_irq_event_enable_peer_dma_complete_0x253a31e3e5f7cd5f_cls:
        """
        Property to access peer_dma_complete field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.irq.event_enable.peer_dma_complete          |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Enables PEER_DMA_COMPLETE events. A peer event is queued only   |
        |              |      when this field and the selected peer's dma.irq_enable field were  |
        |              |      both set when the DMA request was accepted.</p>                    |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__peer_dma_complete
    @property
    def non_oetp_dma_tx_complete(self) -> openenoc_endpoint_interface_irq_event_enable_non_oetp_dma_tx_complete_0xbfd03725ebc2482_cls:
        """
        Property to access non_oetp_dma_tx_complete field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.irq.event_enable.non_oetp_dma_tx_complete   |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Enables NON_OETP_DMA_TX_COMPLETE events. Hardware samples this  |
        |              |      field when it accepts a non-oETP transmit DMA request.</p>         |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__non_oetp_dma_tx_complete
    @property
    def non_oetp_dma_rx_complete(self) -> openenoc_endpoint_interface_irq_event_enable_non_oetp_dma_rx_complete_0x3629e67722bfd09a_cls:
        """
        Property to access non_oetp_dma_rx_complete field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.irq.event_enable.non_oetp_dma_rx_complete   |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Enables NON_OETP_DMA_RX_COMPLETE events. Hardware samples this  |
        |              |      field when it accepts a non-oETP receive DMA request.</p>          |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__non_oetp_dma_rx_complete
    @property
    def non_oetp_direct_tx_complete(self) -> openenoc_endpoint_interface_irq_event_enable_non_oetp_direct_tx_complete_0xaae4fb94b3cca8d_cls:
        """
        Property to access non_oetp_direct_tx_complete field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.irq.event_enable.non_oetp_direct_tx_complet |
        |              |      e                                                                  |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Enables NON_OETP_DIRECT_TX_COMPLETE events. Hardware samples    |
        |              |      this field when the first beat of a direct transmit frame is       |
        |              |      accepted from the CSR-facing AXI4-Stream interface. When enabled,  |
        |              |      the frame start is accepted only after an IRQ FIFO credit has been |
        |              |      reserved. The event is generated when the final beat is accepted   |
        |              |      by the oETP engine.</p>                                            |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__non_oetp_direct_tx_complete
    @property
    def non_oetp_direct_rx_available(self) -> openenoc_endpoint_interface_irq_event_enable_non_oetp_direct_rx_available_0x30d4ea837eee6b0e_cls:
        """
        Property to access non_oetp_direct_rx_available field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.irq.event_enable.non_oetp_direct_rx_availab |
        |              |      le                                                                 |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Enables NON_OETP_DIRECT_RX_AVAILABLE events. One event is       |
        |              |      generated when the first beat of a new direct receive frame        |
        |              |      becomes valid on the CSR-facing AXI4-Stream interface. When        |
        |              |      enabled, routing logic does not expose that first TVALID until an  |
        |              |      IRQ FIFO credit is available, so the event cannot be lost. The     |
        |              |      event does not depend on TLAST and therefore supports both cut-    |
        |              |      through and frame-FIFO operation.</p>                              |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__non_oetp_direct_rx_available

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'peer_dma_complete':'peer_dma_complete','non_oetp_dma_tx_complete':'non_oetp_dma_tx_complete','non_oetp_dma_rx_complete':'non_oetp_dma_rx_complete','non_oetp_direct_tx_complete':'non_oetp_direct_tx_complete','non_oetp_direct_rx_available':'non_oetp_direct_rx_available',
            }

    
    
    
    
    
    
    # nodes:5
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["peer_dma_complete"]) -> 'openenoc_endpoint_interface_irq_event_enable_peer_dma_complete_0x253a31e3e5f7cd5f_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["non_oetp_dma_tx_complete"]) -> 'openenoc_endpoint_interface_irq_event_enable_non_oetp_dma_tx_complete_0xbfd03725ebc2482_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["non_oetp_dma_rx_complete"]) -> 'openenoc_endpoint_interface_irq_event_enable_non_oetp_dma_rx_complete_0x3629e67722bfd09a_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["non_oetp_direct_tx_complete"]) -> 'openenoc_endpoint_interface_irq_event_enable_non_oetp_direct_tx_complete_0xaae4fb94b3cca8d_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["non_oetp_direct_rx_available"]) -> 'openenoc_endpoint_interface_irq_event_enable_non_oetp_direct_rx_available_0x30d4ea837eee6b0e_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_interface_irq_event_enable_peer_dma_complete_0x253a31e3e5f7cd5f_cls', 'openenoc_endpoint_interface_irq_event_enable_non_oetp_dma_tx_complete_0xbfd03725ebc2482_cls', 'openenoc_endpoint_interface_irq_event_enable_non_oetp_dma_rx_complete_0x3629e67722bfd09a_cls', 'openenoc_endpoint_interface_irq_event_enable_non_oetp_direct_tx_complete_0xaae4fb94b3cca8d_cls', 'openenoc_endpoint_interface_irq_event_enable_non_oetp_direct_rx_available_0x30d4ea837eee6b0e_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.irq.event_enable"
    @property
    def rdl_desc(self) -> str:
        return "Enables generation of individual endpoint IRQ event classes. These fields\ncontrol event capture; irq.control.global_enable only masks the physical\nIRQ output."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.peer_dma_complete
        yield self.non_oetp_dma_tx_complete
        yield self.non_oetp_dma_rx_complete
        yield self.non_oetp_direct_tx_complete
        yield self.non_oetp_direct_rx_available
        
        
    

    
    
class openenoc_endpoint_interface_irq_status_neg_0x78fdfe17ac03000_cls(RegReadOnly):
    """
    Class to represent a register in the register model

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

    __slots__ : list[str] = ['__claim_pending', '__credit_full', '__overflow', '__invalid_complete', '__irq_asserted', '__fifo_level', '__reserved_count']

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
        
        self.__claim_pending:openenoc_endpoint_interface_irq_status_claim_pending_neg_0x2a11b2b60d7ef56_cls = openenoc_endpoint_interface_irq_status_claim_pending_neg_0x2a11b2b60d7ef56_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=0, msb=0,
                low=0, high=0),
            misc_props=FieldMiscProps(
                default=None,
                is_volatile=True),
            logger_handle=logger_handle+'.claim_pending',
            inst_name='claim_pending',
            field_type=int)
        self.__credit_full:openenoc_endpoint_interface_irq_status_credit_full_0x6cb990f26b9bde51_cls = openenoc_endpoint_interface_irq_status_credit_full_0x6cb990f26b9bde51_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=1, msb=1,
                low=1, high=1),
            misc_props=FieldMiscProps(
                default=None,
                is_volatile=True),
            logger_handle=logger_handle+'.credit_full',
            inst_name='credit_full',
            field_type=int)
        self.__overflow:openenoc_endpoint_interface_irq_status_overflow_0x41b63e9cb4b127f_cls = openenoc_endpoint_interface_irq_status_overflow_0x41b63e9cb4b127f_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=2, msb=2,
                low=2, high=2),
            misc_props=FieldMiscProps(
                default=None,
                is_volatile=True),
            logger_handle=logger_handle+'.overflow',
            inst_name='overflow',
            field_type=int)
        self.__invalid_complete:openenoc_endpoint_interface_irq_status_invalid_complete_0x8b83b4b300b8120_cls = openenoc_endpoint_interface_irq_status_invalid_complete_0x8b83b4b300b8120_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=3, msb=3,
                low=3, high=3),
            misc_props=FieldMiscProps(
                default=None,
                is_volatile=True),
            logger_handle=logger_handle+'.invalid_complete',
            inst_name='invalid_complete',
            field_type=int)
        self.__irq_asserted:openenoc_endpoint_interface_irq_status_irq_asserted_0x56f68d1934c5ed65_cls = openenoc_endpoint_interface_irq_status_irq_asserted_0x56f68d1934c5ed65_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=4, msb=4,
                low=4, high=4),
            misc_props=FieldMiscProps(
                default=None,
                is_volatile=True),
            logger_handle=logger_handle+'.irq_asserted',
            inst_name='irq_asserted',
            field_type=int)
        self.__fifo_level:openenoc_endpoint_interface_irq_status_fifo_level_0x3bf4209269d64cb7_cls = openenoc_endpoint_interface_irq_status_fifo_level_0x3bf4209269d64cb7_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=8,
                lsb=8, msb=15,
                low=8, high=15),
            misc_props=FieldMiscProps(
                default=None,
                is_volatile=True),
            logger_handle=logger_handle+'.fifo_level',
            inst_name='fifo_level',
            field_type=int)
        self.__reserved_count:openenoc_endpoint_interface_irq_status_reserved_count_0x3162a220699ff36f_cls = openenoc_endpoint_interface_irq_status_reserved_count_0x3162a220699ff36f_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=8,
                lsb=16, msb=23,
                low=16, high=23),
            misc_props=FieldMiscProps(
                default=None,
                is_volatile=True),
            logger_handle=logger_handle+'.reserved_count',
            inst_name='reserved_count',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def claim_pending(self) -> openenoc_endpoint_interface_irq_status_claim_pending_neg_0x2a11b2b60d7ef56_cls:
        """
        Property to access claim_pending field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.irq.status.claim_pending                    |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Indicates that at least one valid event is available in         |
        |              |      irq.claim.</p>                                                     |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__claim_pending
    @property
    def credit_full(self) -> openenoc_endpoint_interface_irq_status_credit_full_0x6cb990f26b9bde51_cls:
        """
        Property to access credit_full field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.irq.status.credit_full                      |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Indicates that all event FIFO credits are occupied by queued    |
        |              |      claims or reserved for admitted operations. While no credit is     |
        |              |      available, new interrupt-enabled DMA requests are not accepted and |
        |              |      the start of an interrupt-enabled direct AXI4-Stream frame is      |
        |              |      backpressured.</p>                                                 |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__credit_full
    @property
    def overflow(self) -> openenoc_endpoint_interface_irq_status_overflow_0x41b63e9cb4b127f_cls:
        """
        Property to access overflow field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.irq.status.overflow                         |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Sticky internal-error flag indicating that an enabled event     |
        |              |      could not be retained. Correct credit reservation, admission       |
        |              |      control, and AXI4-Stream backpressure make this condition          |
        |              |      unreachable during normal operation. Clear with                    |
        |              |      irq.control.clear_errors.</p>                                      |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__overflow
    @property
    def invalid_complete(self) -> openenoc_endpoint_interface_irq_status_invalid_complete_0x8b83b4b300b8120_cls:
        """
        Property to access invalid_complete field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.irq.status.invalid_complete                 |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Sticky protocol-error flag indicating that irq.complete.valid   |
        |              |      was accepted while no claim was pending or that the completion     |
        |              |      token did not match the current claim. No claim is removed on a    |
        |              |      mismatch. Clear with irq.control.clear_errors.</p>                 |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__invalid_complete
    @property
    def irq_asserted(self) -> openenoc_endpoint_interface_irq_status_irq_asserted_0x56f68d1934c5ed65_cls:
        """
        Property to access irq_asserted field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.irq.status.irq_asserted                     |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Reflects the current value of the physical endpoint IRQ output  |
        |              |      after application of irq.control.global_enable.</p>                |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__irq_asserted
    @property
    def fifo_level(self) -> openenoc_endpoint_interface_irq_status_fifo_level_0x3bf4209269d64cb7_cls:
        """
        Property to access fifo_level field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.irq.status.fifo_level[7:0]                  |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Number of valid claims currently queued in the IRQ event FIFO.  |
        |              |      Values greater than 255 are reported as 255.</p>                   |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__fifo_level
    @property
    def reserved_count(self) -> openenoc_endpoint_interface_irq_status_reserved_count_0x3162a220699ff36f_cls:
        """
        Property to access reserved_count field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.irq.status.reserved_count[7:0]              |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Number of event FIFO credits reserved for admitted DMA          |
        |              |      operations or direct transmit frames whose events have not yet     |
        |              |      been queued. Values greater than 255 are reported as 255.</p>      |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__reserved_count

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'claim_pending':'claim_pending','credit_full':'credit_full','overflow':'overflow','invalid_complete':'invalid_complete','irq_asserted':'irq_asserted','fifo_level':'fifo_level','reserved_count':'reserved_count',
            }

    
    
    
    
    
    
    # nodes:7
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["claim_pending"]) -> 'openenoc_endpoint_interface_irq_status_claim_pending_neg_0x2a11b2b60d7ef56_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["credit_full"]) -> 'openenoc_endpoint_interface_irq_status_credit_full_0x6cb990f26b9bde51_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["overflow"]) -> 'openenoc_endpoint_interface_irq_status_overflow_0x41b63e9cb4b127f_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["invalid_complete"]) -> 'openenoc_endpoint_interface_irq_status_invalid_complete_0x8b83b4b300b8120_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["irq_asserted"]) -> 'openenoc_endpoint_interface_irq_status_irq_asserted_0x56f68d1934c5ed65_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["fifo_level"]) -> 'openenoc_endpoint_interface_irq_status_fifo_level_0x3bf4209269d64cb7_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["reserved_count"]) -> 'openenoc_endpoint_interface_irq_status_reserved_count_0x3162a220699ff36f_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_interface_irq_status_claim_pending_neg_0x2a11b2b60d7ef56_cls', 'openenoc_endpoint_interface_irq_status_credit_full_0x6cb990f26b9bde51_cls', 'openenoc_endpoint_interface_irq_status_overflow_0x41b63e9cb4b127f_cls', 'openenoc_endpoint_interface_irq_status_invalid_complete_0x8b83b4b300b8120_cls', 'openenoc_endpoint_interface_irq_status_irq_asserted_0x56f68d1934c5ed65_cls', 'openenoc_endpoint_interface_irq_status_fifo_level_0x3bf4209269d64cb7_cls', 'openenoc_endpoint_interface_irq_status_reserved_count_0x3162a220699ff36f_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.irq.status"
    @property
    def rdl_desc(self) -> str:
        return "Status of the endpoint IRQ event FIFO and its reservation mechanism."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.claim_pending
        yield self.credit_full
        yield self.overflow
        yield self.invalid_complete
        yield self.irq_asserted
        yield self.fifo_level
        yield self.reserved_count
        
        
    

    
    
class openenoc_endpoint_interface_irq_claim_0x4bae8d86bcd488ab_cls(RegReadOnly):
    """
    Class to represent a register in the register model

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

    __slots__ : list[str] = ['__peer_idx', '__source', '__sequence', '__valid']

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
        
        self.__peer_idx:openenoc_endpoint_interface_irq_claim_peer_idx_neg_0x69b2dc68a7396999_cls = openenoc_endpoint_interface_irq_claim_peer_idx_neg_0x69b2dc68a7396999_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=11,
                lsb=0, msb=10,
                low=0, high=10),
            misc_props=FieldMiscProps(
                default=None,
                is_volatile=True),
            logger_handle=logger_handle+'.peer_idx',
            inst_name='peer_idx',
            field_type=int)
        self.__source:openenoc_endpoint_interface_irq_claim_source_neg_0x4f719fd90574e7c_cls = openenoc_endpoint_interface_irq_claim_source_neg_0x4f719fd90574e7c_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=4,
                lsb=11, msb=14,
                low=11, high=14),
            misc_props=FieldMiscProps(
                default=None,
                is_volatile=True),
            logger_handle=logger_handle+'.source',
            inst_name='source',
            field_type=int)
        self.__sequence:openenoc_endpoint_interface_irq_claim_sequence_0x208c61200ea782a_cls = openenoc_endpoint_interface_irq_claim_sequence_0x208c61200ea782a_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=16,
                lsb=15, msb=30,
                low=15, high=30),
            misc_props=FieldMiscProps(
                default=None,
                is_volatile=True),
            logger_handle=logger_handle+'.sequence',
            inst_name='sequence',
            field_type=int)
        self.__valid:openenoc_endpoint_interface_irq_claim_valid_neg_0x705488c4f88c1563_cls = openenoc_endpoint_interface_irq_claim_valid_neg_0x705488c4f88c1563_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=31, msb=31,
                low=31, high=31),
            misc_props=FieldMiscProps(
                default=None,
                is_volatile=True),
            logger_handle=logger_handle+'.valid',
            inst_name='valid',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def peer_idx(self) -> openenoc_endpoint_interface_irq_claim_peer_idx_neg_0x69b2dc68a7396999_cls:
        """
        Property to access peer_idx field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.irq.claim.peer_idx[10:0]                    |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Zero-based peer index for a PEER_DMA_COMPLETE event, in the     |
        |              |      range 0 through NUM_OF_PEERS-1. The field is not applicable to     |
        |              |      other event sources and is driven to zero for deterministic        |
        |              |      readback.</p>                                                      |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__peer_idx
    @property
    def source(self) -> openenoc_endpoint_interface_irq_claim_source_neg_0x4f719fd90574e7c_cls:
        """
        Property to access source field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.irq.claim.source[3:0]                       |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>IRQ event source:<ul></p> <li>0: PEER_DMA_COMPLETE. A peer DMA  |
        |              |      request completed with either success or error; peer_idx           |
        |              |      identifies the peer.</li> <li>1: NON_OETP_DMA_TX_COMPLETE. A non-  |
        |              |      oETP transmit DMA request completed with either success or         |
        |              |      error.</li> <li>2: NON_OETP_DMA_RX_COMPLETE. A non-oETP receive    |
        |              |      DMA request completed with either success or error.</li> <li>3:    |
        |              |      NON_OETP_DIRECT_TX_COMPLETE. The final beat of a direct non-oETP   |
        |              |      transmit frame was accepted by the oETP engine.</li> <li>4:        |
        |              |      NON_OETP_DIRECT_RX_AVAILABLE. The first beat of a new direct non-  |
        |              |      oETP receive frame is available on the CSR-facing AXI4-Stream      |
        |              |      interface.</li> <li>5-15: Reserved.</li> <p></ul> This field is    |
        |              |      meaningful only when valid is set.</p>                             |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__source
    @property
    def sequence(self) -> openenoc_endpoint_interface_irq_claim_sequence_0x208c61200ea782a_cls:
        """
        Property to access sequence field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.irq.claim.sequence[15:0]                    |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Monotonically increasing event sequence number, modulo 65536.   |
        |              |      The sequence number distinguishes otherwise identical claims and   |
        |              |      protects against stale or repeated completion requests.</p>        |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__sequence
    @property
    def valid(self) -> openenoc_endpoint_interface_irq_claim_valid_neg_0x705488c4f88c1563_cls:
        """
        Property to access valid field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.irq.claim.valid                             |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Indicates that this register contains the valid event at the    |
        |              |      head of the IRQ event FIFO. When clear, all other claim fields     |
        |              |      shall be ignored.</p>                                              |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__valid

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'peer_idx':'peer_idx','source':'source','sequence':'sequence','valid':'valid',
            }

    
    
    
    
    
    
    # nodes:4
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["peer_idx"]) -> 'openenoc_endpoint_interface_irq_claim_peer_idx_neg_0x69b2dc68a7396999_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["source"]) -> 'openenoc_endpoint_interface_irq_claim_source_neg_0x4f719fd90574e7c_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["sequence"]) -> 'openenoc_endpoint_interface_irq_claim_sequence_0x208c61200ea782a_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["valid"]) -> 'openenoc_endpoint_interface_irq_claim_valid_neg_0x705488c4f88c1563_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_interface_irq_claim_peer_idx_neg_0x69b2dc68a7396999_cls', 'openenoc_endpoint_interface_irq_claim_source_neg_0x4f719fd90574e7c_cls', 'openenoc_endpoint_interface_irq_claim_sequence_0x208c61200ea782a_cls', 'openenoc_endpoint_interface_irq_claim_valid_neg_0x705488c4f88c1563_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.irq.claim"
    @property
    def rdl_desc(self) -> str:
        return "Read-only view of the event at the head of the IRQ event FIFO. Reading this\nregister has no side effect, and all fields remain stable until a matching\nirq.complete request removes the claim."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.peer_idx
        yield self.source
        yield self.sequence
        yield self.valid
        
        
    

    
    
class openenoc_endpoint_interface_irq_complete_neg_0x7b5c4c16ce1f5929_cls(RegReadWrite):
    """
    Class to represent a register in the register model

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

    __slots__ : list[str] = ['__peer_idx', '__source', '__sequence', '__valid']

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
        
        self.__peer_idx:openenoc_endpoint_interface_irq_complete_peer_idx_0x3fada93a90ffed96_cls = openenoc_endpoint_interface_irq_complete_peer_idx_0x3fada93a90ffed96_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=11,
                lsb=0, msb=10,
                low=0, high=10),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.peer_idx',
            inst_name='peer_idx',
            field_type=int)
        self.__source:openenoc_endpoint_interface_irq_complete_source_0x1f753df5b7cec2c3_cls = openenoc_endpoint_interface_irq_complete_source_0x1f753df5b7cec2c3_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=4,
                lsb=11, msb=14,
                low=11, high=14),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.source',
            inst_name='source',
            field_type=int)
        self.__sequence:openenoc_endpoint_interface_irq_complete_sequence_0x7aeb1b299f2703b5_cls = openenoc_endpoint_interface_irq_complete_sequence_0x7aeb1b299f2703b5_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=16,
                lsb=15, msb=30,
                low=15, high=30),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.sequence',
            inst_name='sequence',
            field_type=int)
        self.__valid:openenoc_endpoint_interface_irq_complete_valid_neg_0x33d28002c6c387ab_cls = openenoc_endpoint_interface_irq_complete_valid_neg_0x33d28002c6c387ab_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=31, msb=31,
                low=31, high=31),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.valid',
            inst_name='valid',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32

    

    # build the properties for the fields
    
    @property
    def peer_idx(self) -> openenoc_endpoint_interface_irq_complete_peer_idx_0x3fada93a90ffed96_cls:
        """
        Property to access peer_idx field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.irq.complete.peer_idx[10:0]                 |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Peer-index portion of the claim token.</p>                      |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__peer_idx
    @property
    def source(self) -> openenoc_endpoint_interface_irq_complete_source_0x1f753df5b7cec2c3_cls:
        """
        Property to access source field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.irq.complete.source[3:0]                    |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Event-source portion of the claim token.</p>                    |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__source
    @property
    def sequence(self) -> openenoc_endpoint_interface_irq_complete_sequence_0x7aeb1b299f2703b5_cls:
        """
        Property to access sequence field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.irq.complete.sequence[15:0]                 |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Sequence-number portion of the claim token.</p>                 |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__sequence
    @property
    def valid(self) -> openenoc_endpoint_interface_irq_complete_valid_neg_0x33d28002c6c387ab_cls:
        """
        Property to access valid field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.irq.complete.valid                          |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Writing one submits the completion token. The field remains     |
        |              |      asserted until hardware validates the token and clears it. A       |
        |              |      matching token removes the current claim and releases its FIFO     |
        |              |      credit; an invalid token leaves the claim unchanged and sets       |
        |              |      irq.status.invalid_complete.</p>                                   |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__valid

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'peer_idx':'peer_idx','source':'source','sequence':'sequence','valid':'valid',
            }

    
    
    
    
    
    
    # nodes:4
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["peer_idx"]) -> 'openenoc_endpoint_interface_irq_complete_peer_idx_0x3fada93a90ffed96_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["source"]) -> 'openenoc_endpoint_interface_irq_complete_source_0x1f753df5b7cec2c3_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["sequence"]) -> 'openenoc_endpoint_interface_irq_complete_sequence_0x7aeb1b299f2703b5_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["valid"]) -> 'openenoc_endpoint_interface_irq_complete_valid_neg_0x33d28002c6c387ab_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_interface_irq_complete_peer_idx_0x3fada93a90ffed96_cls', 'openenoc_endpoint_interface_irq_complete_source_0x1f753df5b7cec2c3_cls', 'openenoc_endpoint_interface_irq_complete_sequence_0x7aeb1b299f2703b5_cls', 'openenoc_endpoint_interface_irq_complete_valid_neg_0x33d28002c6c387ab_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.irq.complete"
    @property
    def rdl_desc(self) -> str:
        return "Completion request for the current IRQ claim. Software acknowledges an event by\ncopying the complete 32-bit irq.claim value into this register."
    
    

    
    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:
        
        
        yield self.peer_idx
        yield self.source
        yield self.sequence
        yield self.valid
        
        
    

    
    
class openenoc_endpoint_interface_peers_entry_mac_address_0x2f0b3f22ead21068_cls(RegReadWrite):
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
        
        self.__lo_word:openenoc_endpoint_interface_peers_entry_mac_address_lo_word_0x51ddefabf71bf946_cls = openenoc_endpoint_interface_peers_entry_mac_address_lo_word_0x51ddefabf71bf946_cls(
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
        self.__hi_word:openenoc_endpoint_interface_peers_entry_mac_address_hi_word_0x74fd9945767a7256_cls = openenoc_endpoint_interface_peers_entry_mac_address_hi_word_0x74fd9945767a7256_cls(
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
    def lo_word(self) -> openenoc_endpoint_interface_peers_entry_mac_address_lo_word_0x51ddefabf71bf946_cls:
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
    def hi_word(self) -> openenoc_endpoint_interface_peers_entry_mac_address_hi_word_0x74fd9945767a7256_cls:
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
    def get_child_by_system_rdl_name(self, name: Literal["lo_word"]) -> 'openenoc_endpoint_interface_peers_entry_mac_address_lo_word_0x51ddefabf71bf946_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["hi_word"]) -> 'openenoc_endpoint_interface_peers_entry_mac_address_hi_word_0x74fd9945767a7256_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_interface_peers_entry_mac_address_lo_word_0x51ddefabf71bf946_cls', 'openenoc_endpoint_interface_peers_entry_mac_address_hi_word_0x74fd9945767a7256_cls', ]: ...

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
        
        
    


if __name__ == '__main__':
    pass