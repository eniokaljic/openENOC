

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






from .fields import csr_test_reg_test_field_0x2d10b449974b1aac_cls
from .fields import openenoc_endpoint_interface_info_rmem_total_depth_0x1c7e4a55a4858634_cls
from .fields import openenoc_endpoint_interface_info_num_of_peers_neg_0x5518c59f02e0f143_cls
from .fields import openenoc_endpoint_interface_info_peer_dma_supported_neg_0xd95a983276af65f_cls
from .fields import openenoc_endpoint_interface_info_non_oetp_dma_supported_neg_0x4be54bc85b3f2c81_cls
from .fields import openenoc_endpoint_interface_info_direct_axis_supported_neg_0x5868185a85cd4b2f_cls
from .fields import openenoc_endpoint_interface_info_rmem_supported_0x14f76811800d8a02_cls
from .fields import openenoc_endpoint_interface_info_irq_supported_0x6035e9c40a51546d_cls
from .fields import openenoc_endpoint_interface_info_max_dma_frame_size_bytes_0x7c2002dfead2b04b_cls
from .fields import openenoc_endpoint_interface_config_mac_address_lo_word_neg_0x48b21d5256898003_cls
from .fields import openenoc_endpoint_interface_config_mac_address_hi_word_0x5c389cda01b0a010_cls
from .fields import openenoc_endpoint_interface_config_multicast_address_lo_word_0xa51d51e8c91ffaf_cls
from .fields import openenoc_endpoint_interface_config_multicast_address_hi_word_0x2ab309c4ffe4e9d4_cls
from .fields import openenoc_endpoint_interface_config_non_oetp_control_receive_mode_neg_0xd42228a8c7c937a_cls
from .fields import openenoc_endpoint_interface_config_rmem_timeout_cycles_neg_0x21386ee83b5f90a9_cls
from .fields import openenoc_endpoint_interface_config_dma_timeout_cycles_0x1b1c348b779c5fc_cls
from .fields import openenoc_endpoint_interface_config_dma_max_fragment_size_bytes_0x56886a0b57a4a4fd_cls
from .fields import openenoc_endpoint_interface_axis_if_source_data_tdata_0x17c4542c090ffd0e_cls
from .fields import openenoc_endpoint_interface_axis_if_source_control_tvalid_neg_0x267c2272d993b105_cls
from .fields import openenoc_endpoint_interface_axis_if_source_control_tlast_neg_0x77cb31118f74f4c3_cls
from .fields import openenoc_endpoint_interface_axis_if_source_control_tkeep_0x7eae4751b962a1c_cls
from .fields import openenoc_endpoint_interface_axis_if_source_status_tready_0x67560cf213adb45d_cls
from .fields import openenoc_endpoint_interface_axis_if_sink_data_tdata_0x2bdcea2731f9535_cls
from .fields import openenoc_endpoint_interface_axis_if_sink_control_tready_0x4b7af26499667549_cls
from .fields import openenoc_endpoint_interface_axis_if_sink_status_tvalid_neg_0x236d83f545db909d_cls
from .fields import openenoc_endpoint_interface_axis_if_sink_status_tlast_0x2d9cca5e6baa0192_cls
from .fields import openenoc_endpoint_interface_axis_if_sink_status_tkeep_0x62a0176d39c90967_cls
from .fields import openenoc_endpoint_interface_non_oetp_dma_tx_buffer_address_base_neg_0x28b01b54d9107f5e_cls
from .fields import openenoc_endpoint_interface_non_oetp_dma_tx_frame_length_bytes_0x6f39179e191d9c64_cls
from .fields import openenoc_endpoint_interface_non_oetp_dma_tx_command_status_request_0x572b2ec04c2729a1_cls
from .fields import openenoc_endpoint_interface_non_oetp_dma_tx_command_status_clear_errors_0x12df5b7087b874bd_cls
from .fields import openenoc_endpoint_interface_non_oetp_dma_tx_command_status_idle_neg_0x2426ca7af38c78f9_cls
from .fields import openenoc_endpoint_interface_non_oetp_dma_tx_command_status_done_neg_0x38b21b6e94320d9f_cls
from .fields import openenoc_endpoint_interface_non_oetp_dma_tx_command_status_error_neg_0x36e24688106f345b_cls
from .fields import openenoc_endpoint_interface_non_oetp_dma_tx_command_status_error_code_0x4154b313bb26714d_cls
from .fields import openenoc_endpoint_interface_non_oetp_dma_tx_transferred_length_bytes_0x5c88bb9bca3414c_cls
from .fields import openenoc_endpoint_interface_non_oetp_dma_rx_buffer_address_base_neg_0x65ddd3cff5827fd1_cls
from .fields import openenoc_endpoint_interface_non_oetp_dma_rx_buffer_capacity_bytes_0x45d2dfc0e4c83489_cls
from .fields import openenoc_endpoint_interface_non_oetp_dma_rx_command_status_request_0xdfa81fa399196fa_cls
from .fields import openenoc_endpoint_interface_non_oetp_dma_rx_command_status_clear_errors_neg_0x1a408665671a1e4d_cls
from .fields import openenoc_endpoint_interface_non_oetp_dma_rx_command_status_idle_neg_0x6da7c7e99a698bf5_cls
from .fields import openenoc_endpoint_interface_non_oetp_dma_rx_command_status_armed_neg_0x5554fe7639dcbb69_cls
from .fields import openenoc_endpoint_interface_non_oetp_dma_rx_command_status_done_neg_0x69888afa28051618_cls
from .fields import openenoc_endpoint_interface_non_oetp_dma_rx_command_status_error_neg_0x27834466a0a1154b_cls
from .fields import openenoc_endpoint_interface_non_oetp_dma_rx_command_status_error_code_0x2f5b737b8463ea9f_cls
from .fields import openenoc_endpoint_interface_non_oetp_dma_rx_received_length_bytes_0x62104ffbe60d6f40_cls
from .fields import openenoc_endpoint_interface_irq_control_global_enable_neg_0x11fabf129a8cb0ac_cls
from .fields import openenoc_endpoint_interface_irq_control_clear_errors_neg_0x2d370550f19815f7_cls
from .fields import openenoc_endpoint_interface_irq_event_enable_peer_dma_complete_neg_0x4a570f4270edd42b_cls
from .fields import openenoc_endpoint_interface_irq_event_enable_non_oetp_dma_tx_complete_0x486df9956df8d8c8_cls
from .fields import openenoc_endpoint_interface_irq_event_enable_non_oetp_dma_rx_complete_0x6010eb6f58d7cb9d_cls
from .fields import openenoc_endpoint_interface_irq_event_enable_non_oetp_direct_tx_complete_neg_0x4932758f41036931_cls
from .fields import openenoc_endpoint_interface_irq_event_enable_non_oetp_direct_rx_available_neg_0x242e0dcdd48d0d6d_cls
from .fields import openenoc_endpoint_interface_irq_event_enable_rmem_error_neg_0xd42a525ded0713e_cls

# register definitions


class csr_test_reg_neg_0x677cda965c5b4f3a_cls(RegReadWrite):
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

        self.__test_field:csr_test_reg_test_field_0x2d10b449974b1aac_cls = csr_test_reg_test_field_0x2d10b449974b1aac_cls(
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
    def test_field(self) -> csr_test_reg_test_field_0x2d10b449974b1aac_cls:
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








    def get_child_by_system_rdl_name(self, name: Any) -> 'csr_test_reg_test_field_0x2d10b449974b1aac_cls':
        return super().get_child_by_system_rdl_name(name)









    @property
    def rdl_name(self) -> str:
        return "csr.test_reg"
    @property
    def rdl_desc(self) -> str:
        return "Test register"




    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:


        yield self.test_field






class csr_regB_neg_0x1c6020bc076fddb_cls(RegReadWrite):
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






class openenoc_endpoint_interface_info_0x3817de09ce506118_cls(RegReadOnly):
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

        self.__rmem_total_depth:openenoc_endpoint_interface_info_rmem_total_depth_0x1c7e4a55a4858634_cls = openenoc_endpoint_interface_info_rmem_total_depth_0x1c7e4a55a4858634_cls(
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
        self.__num_of_peers:openenoc_endpoint_interface_info_num_of_peers_neg_0x5518c59f02e0f143_cls = openenoc_endpoint_interface_info_num_of_peers_neg_0x5518c59f02e0f143_cls(
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
        self.__peer_dma_supported:openenoc_endpoint_interface_info_peer_dma_supported_neg_0xd95a983276af65f_cls = openenoc_endpoint_interface_info_peer_dma_supported_neg_0xd95a983276af65f_cls(
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
        self.__non_oetp_dma_supported:openenoc_endpoint_interface_info_non_oetp_dma_supported_neg_0x4be54bc85b3f2c81_cls = openenoc_endpoint_interface_info_non_oetp_dma_supported_neg_0x4be54bc85b3f2c81_cls(
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
        self.__direct_axis_supported:openenoc_endpoint_interface_info_direct_axis_supported_neg_0x5868185a85cd4b2f_cls = openenoc_endpoint_interface_info_direct_axis_supported_neg_0x5868185a85cd4b2f_cls(
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
        self.__rmem_supported:openenoc_endpoint_interface_info_rmem_supported_0x14f76811800d8a02_cls = openenoc_endpoint_interface_info_rmem_supported_0x14f76811800d8a02_cls(
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
        self.__irq_supported:openenoc_endpoint_interface_info_irq_supported_0x6035e9c40a51546d_cls = openenoc_endpoint_interface_info_irq_supported_0x6035e9c40a51546d_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=47, msb=47,
                low=47, high=47),
            misc_props=FieldMiscProps(
                default=1,
                is_volatile=False),
            logger_handle=logger_handle+'.irq_supported',
            inst_name='irq_supported',
            field_type=int)
        self.__max_dma_frame_size_bytes:openenoc_endpoint_interface_info_max_dma_frame_size_bytes_0x7c2002dfead2b04b_cls = openenoc_endpoint_interface_info_max_dma_frame_size_bytes_0x7c2002dfead2b04b_cls(
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
    def rmem_total_depth(self) -> openenoc_endpoint_interface_info_rmem_total_depth_0x1c7e4a55a4858634_cls:
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
    def num_of_peers(self) -> openenoc_endpoint_interface_info_num_of_peers_neg_0x5518c59f02e0f143_cls:
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
    def peer_dma_supported(self) -> openenoc_endpoint_interface_info_peer_dma_supported_neg_0xd95a983276af65f_cls:
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
    def non_oetp_dma_supported(self) -> openenoc_endpoint_interface_info_non_oetp_dma_supported_neg_0x4be54bc85b3f2c81_cls:
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
    def direct_axis_supported(self) -> openenoc_endpoint_interface_info_direct_axis_supported_neg_0x5868185a85cd4b2f_cls:
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
    def rmem_supported(self) -> openenoc_endpoint_interface_info_rmem_supported_0x14f76811800d8a02_cls:
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
    def irq_supported(self) -> openenoc_endpoint_interface_info_irq_supported_0x6035e9c40a51546d_cls:
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
    def max_dma_frame_size_bytes(self) -> openenoc_endpoint_interface_info_max_dma_frame_size_bytes_0x7c2002dfead2b04b_cls:
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
        |              |      <p>Synthesis-time maximum Ethernet frame size in bytes, excluding  |
        |              |      FCS. This field reflects the MAX_RAW_FRAME_SIZE parameter value    |
        |              |      and bounds raw non-oETP DMA frames. The peer DMA memory-fragment   |
        |              |      ceiling is 4 * floor((MAX_RAW_FRAME_SIZE - 32) / 4), accounting    |
        |              |      for the Ethernet header, oETP write metadata, data-word padding    |
        |              |      and EndOfData. An 8192-byte frame limit permits 8160-byte memory   |
        |              |      fragments. A value of zero indicates that DMA is not               |
        |              |      supported.</p>                                                     |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__max_dma_frame_size_bytes


    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'rmem_total_depth':'rmem_total_depth','num_of_peers':'num_of_peers','peer_dma_supported':'peer_dma_supported','non_oetp_dma_supported':'non_oetp_dma_supported','direct_axis_supported':'direct_axis_supported','rmem_supported':'rmem_supported','irq_supported':'irq_supported','max_dma_frame_size_bytes':'max_dma_frame_size_bytes',
            }







    # nodes:8

    @overload
    def get_child_by_system_rdl_name(self, name: Literal["rmem_total_depth"]) -> 'openenoc_endpoint_interface_info_rmem_total_depth_0x1c7e4a55a4858634_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: Literal["num_of_peers"]) -> 'openenoc_endpoint_interface_info_num_of_peers_neg_0x5518c59f02e0f143_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: Literal["peer_dma_supported"]) -> 'openenoc_endpoint_interface_info_peer_dma_supported_neg_0xd95a983276af65f_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: Literal["non_oetp_dma_supported"]) -> 'openenoc_endpoint_interface_info_non_oetp_dma_supported_neg_0x4be54bc85b3f2c81_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: Literal["direct_axis_supported"]) -> 'openenoc_endpoint_interface_info_direct_axis_supported_neg_0x5868185a85cd4b2f_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: Literal["rmem_supported"]) -> 'openenoc_endpoint_interface_info_rmem_supported_0x14f76811800d8a02_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: Literal["irq_supported"]) -> 'openenoc_endpoint_interface_info_irq_supported_0x6035e9c40a51546d_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: Literal["max_dma_frame_size_bytes"]) -> 'openenoc_endpoint_interface_info_max_dma_frame_size_bytes_0x7c2002dfead2b04b_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_interface_info_rmem_total_depth_0x1c7e4a55a4858634_cls', 'openenoc_endpoint_interface_info_num_of_peers_neg_0x5518c59f02e0f143_cls', 'openenoc_endpoint_interface_info_peer_dma_supported_neg_0xd95a983276af65f_cls', 'openenoc_endpoint_interface_info_non_oetp_dma_supported_neg_0x4be54bc85b3f2c81_cls', 'openenoc_endpoint_interface_info_direct_axis_supported_neg_0x5868185a85cd4b2f_cls', 'openenoc_endpoint_interface_info_rmem_supported_0x14f76811800d8a02_cls', 'openenoc_endpoint_interface_info_irq_supported_0x6035e9c40a51546d_cls', 'openenoc_endpoint_interface_info_max_dma_frame_size_bytes_0x7c2002dfead2b04b_cls', ]: ...

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






class openenoc_endpoint_interface_config_mac_address_neg_0x3801b58d64d1a9d_cls(RegReadWrite):
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
    |              |      <p>Local endpoint 48-bit unicast MAC address. The oETP engine uses |
    |              |      this address as its source MAC and compares individual-addressed   |
    |              |      incoming oETP frames against it. The I/G bit in the first MAC      |
    |              |      octet must be zero. Group-addressed oETP frames are compared       |
    |              |      against config.multicast_address instead.</p>                      |
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

        self.__lo_word:openenoc_endpoint_interface_config_mac_address_lo_word_neg_0x48b21d5256898003_cls = openenoc_endpoint_interface_config_mac_address_lo_word_neg_0x48b21d5256898003_cls(
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
        self.__hi_word:openenoc_endpoint_interface_config_mac_address_hi_word_0x5c389cda01b0a010_cls = openenoc_endpoint_interface_config_mac_address_hi_word_0x5c389cda01b0a010_cls(
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
    def lo_word(self) -> openenoc_endpoint_interface_config_mac_address_lo_word_neg_0x48b21d5256898003_cls:
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
    def hi_word(self) -> openenoc_endpoint_interface_config_mac_address_hi_word_0x5c389cda01b0a010_cls:
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
    def get_child_by_system_rdl_name(self, name: Literal["lo_word"]) -> 'openenoc_endpoint_interface_config_mac_address_lo_word_neg_0x48b21d5256898003_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: Literal["hi_word"]) -> 'openenoc_endpoint_interface_config_mac_address_hi_word_0x5c389cda01b0a010_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_interface_config_mac_address_lo_word_neg_0x48b21d5256898003_cls', 'openenoc_endpoint_interface_config_mac_address_hi_word_0x5c389cda01b0a010_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)








    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.config.mac_address"
    @property
    def rdl_desc(self) -> str:
        return "Local endpoint 48-bit unicast MAC address. The oETP engine uses this address\nas its source MAC and compares individual-addressed incoming oETP frames against\nit. The I/G bit in the first MAC octet must be zero. Group-addressed oETP frames\nare compared against config.multicast_address instead."




    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:


        yield self.lo_word
        yield self.hi_word






class openenoc_endpoint_interface_config_multicast_address_0x7ddf0f74585cdef8_cls(RegReadWrite):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.config.multicast_address                    |
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

        self.__lo_word:openenoc_endpoint_interface_config_multicast_address_lo_word_0xa51d51e8c91ffaf_cls = openenoc_endpoint_interface_config_multicast_address_lo_word_0xa51d51e8c91ffaf_cls(
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
        self.__hi_word:openenoc_endpoint_interface_config_multicast_address_hi_word_0x2ab309c4ffe4e9d4_cls = openenoc_endpoint_interface_config_multicast_address_hi_word_0x2ab309c4ffe4e9d4_cls(
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
    def lo_word(self) -> openenoc_endpoint_interface_config_multicast_address_lo_word_0xa51d51e8c91ffaf_cls:
        """
        Property to access lo_word field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.config.multicast_address.lo_word[31:0]      |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Lower 32 bits [31:0] of the 48-bit multicast MAC address.</p>   |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__lo_word
    @property
    def hi_word(self) -> openenoc_endpoint_interface_config_multicast_address_hi_word_0x2ab309c4ffe4e9d4_cls:
        """
        Property to access hi_word field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.config.multicast_address.hi_word[47:32]     |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Upper 16 bits [47:32] of the 48-bit multicast MAC address.</p>  |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__hi_word


    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'lo_word':'lo_word','hi_word':'hi_word',
            }







    # nodes:2

    @overload
    def get_child_by_system_rdl_name(self, name: Literal["lo_word"]) -> 'openenoc_endpoint_interface_config_multicast_address_lo_word_0xa51d51e8c91ffaf_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: Literal["hi_word"]) -> 'openenoc_endpoint_interface_config_multicast_address_hi_word_0x2ab309c4ffe4e9d4_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_interface_config_multicast_address_lo_word_0xa51d51e8c91ffaf_cls', 'openenoc_endpoint_interface_config_multicast_address_hi_word_0x2ab309c4ffe4e9d4_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)








    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.config.multicast_address"
    @property
    def rdl_desc(self) -> str:
        return "Local endpoint 48-bit multicast destination MAC address. For an incoming\noETP frame whose destination I/G bit is one, the engine accepts the destination\nonly when it exactly matches this address. All slave endpoints in a replication\ngroup use the same value. This address is not used as a source MAC. Zero is the\nreset value and matches no group-addressed destination, disabling oETP group\nreception. Broadcast is accepted only when this address is all ones. This field\ndoes not change the separate non-oETP receive-mode policy."




    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:


        yield self.lo_word
        yield self.hi_word






class openenoc_endpoint_interface_config_non_oetp_control_neg_0xa4dc5f32d81fa0c_cls(RegReadWrite):
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

        self.__receive_mode:openenoc_endpoint_interface_config_non_oetp_control_receive_mode_neg_0xd42228a8c7c937a_cls = openenoc_endpoint_interface_config_non_oetp_control_receive_mode_neg_0xd42228a8c7c937a_cls(
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
    def receive_mode(self) -> openenoc_endpoint_interface_config_non_oetp_control_receive_mode_neg_0xd42228a8c7c937a_cls:
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








    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_interface_config_non_oetp_control_receive_mode_neg_0xd42228a8c7c937a_cls':
        return super().get_child_by_system_rdl_name(name)









    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.config.non_oetp_control"
    @property
    def rdl_desc(self) -> str:
        return "Receive policy for Ethernet frames that do not carry oETP traffic."




    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:


        yield self.receive_mode






class openenoc_endpoint_interface_config_rmem_timeout_neg_0x766b0dfacf10491f_cls(RegReadWrite):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.config.rmem_timeout                         |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Timeout configuration for transparent RMEM operations.</p>      |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__cycles']

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

        self.__cycles:openenoc_endpoint_interface_config_rmem_timeout_cycles_neg_0x21386ee83b5f90a9_cls = openenoc_endpoint_interface_config_rmem_timeout_cycles_neg_0x21386ee83b5f90a9_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0, msb=31,
                low=0, high=31),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.cycles',
            inst_name='cycles',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32



    # build the properties for the fields

    @property
    def cycles(self) -> openenoc_endpoint_interface_config_rmem_timeout_cycles_neg_0x21386ee83b5f90a9_cls:
        """
        Property to access cycles field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.config.rmem_timeout.cycles[31:0]            |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Maximum wait for an RMEM response in endpoint clock cycles.     |
        |              |      Zero disables the timeout and permits an indefinite response wait. |
        |              |      Hardware samples this value when it accepts an RMEM operation;     |
        |              |      subsequent writes apply to later operations. The response timer    |
        |              |      starts after the complete request frame has been accepted by the   |
        |              |      Ethernet-facing transmit stream and runs until the complete        |
        |              |      matching response is received and validated through Ethernet       |
        |              |      TLAST. RX backpressure counts toward the timeout; remaining local  |
        |              |      memory completion does not. A valid response completing on the     |
        |              |      expiry edge takes priority, including a valid ERROR_RSP with its   |
        |              |      reported cause. Hardware does not retry; timeout handling and      |
        |              |      retry policy belong to software. Multicast writes do not wait for  |
        |              |      a response and do not use this response timeout. An RMEM read      |
        |              |      timeout terminates the access with all-ones read data and read     |
        |              |      ACK; a write timeout terminates with write ACK. The external-RMEM  |
        |              |      boundary uses no ERR signals. Failures set error and error_code in |
        |              |      the associated peers.entry[].dma register and may generate a       |
        |              |      separate RMEM_ERROR IRQ event.</p>                                 |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__cycles


    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'cycles':'cycles',
            }








    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_interface_config_rmem_timeout_cycles_neg_0x21386ee83b5f90a9_cls':
        return super().get_child_by_system_rdl_name(name)









    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.config.rmem_timeout"
    @property
    def rdl_desc(self) -> str:
        return "Timeout configuration for transparent RMEM operations."




    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:


        yield self.cycles






class openenoc_endpoint_interface_config_dma_timeout_0x92a634521450797_cls(RegReadWrite):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.config.dma_timeout                          |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Common response timeout for locally initiated unicast peer DMA  |
    |              |      fragments.</p>                                                     |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__cycles']

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

        self.__cycles:openenoc_endpoint_interface_config_dma_timeout_cycles_0x1b1c348b779c5fc_cls = openenoc_endpoint_interface_config_dma_timeout_cycles_0x1b1c348b779c5fc_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0, msb=31,
                low=0, high=31),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.cycles',
            inst_name='cycles',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32



    # build the properties for the fields

    @property
    def cycles(self) -> openenoc_endpoint_interface_config_dma_timeout_cycles_0x1b1c348b779c5fc_cls:
        """
        Property to access cycles field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.config.dma_timeout.cycles[31:0]             |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Maximum wait for a response to one peer DMA fragment, in        |
        |              |      endpoint clock cycles. This value is shared by all peers. Zero     |
        |              |      disables the timeout and permits an indefinite response wait.      |
        |              |      Hardware samples this value when the oETP engine accepts the       |
        |              |      fragment request; later writes apply to later fragments. The       |
        |              |      response timer starts after the complete request frame has been    |
        |              |      accepted by the Ethernet-facing transmit stream and runs until the |
        |              |      complete matching response is received and validated through       |
        |              |      Ethernet TLAST, including EndOfData where present. RX backpressure |
        |              |      counts toward the timeout; remaining local memory completion does  |
        |              |      not. A valid response completing on the expiry edge takes          |
        |              |      priority, including a valid ERROR_RSP with its reported cause. On  |
        |              |      expiry, hardware aborts the remaining fragments of that DMA        |
        |              |      transfer and reports error code 8 (timeout) in the peer DMA        |
        |              |      status. Hardware does not retry; software decides whether to start |
        |              |      another transfer. This timeout does not apply to multicast writes, |
        |              |      non-oETP DMA, or transparent RMEM operations.</p>                  |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__cycles


    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'cycles':'cycles',
            }








    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_interface_config_dma_timeout_cycles_0x1b1c348b779c5fc_cls':
        return super().get_child_by_system_rdl_name(name)









    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.config.dma_timeout"
    @property
    def rdl_desc(self) -> str:
        return "Common response timeout for locally initiated unicast peer DMA fragments."




    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:


        yield self.cycles






class openenoc_endpoint_interface_config_dma_max_fragment_size_0x50c768680d18b7f_cls(RegReadWrite):
    """
    Class to represent a register in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.config.dma_max_fragment_size                |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Common software-selected maximum memory fragment size for       |
    |              |      locally initiated peer DMA transfers. The synthesis-time frame     |
    |              |      limit remains fixed.</p>                                           |
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

        self.__bytes:openenoc_endpoint_interface_config_dma_max_fragment_size_bytes_0x56886a0b57a4a4fd_cls = openenoc_endpoint_interface_config_dma_max_fragment_size_bytes_0x56886a0b57a4a4fd_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=32,
                lsb=0, msb=31,
                low=0, high=31),
            misc_props=FieldMiscProps(
                default=8160,
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
    def bytes(self) -> openenoc_endpoint_interface_config_dma_max_fragment_size_bytes_0x56886a0b57a4a4fd_cls:
        """
        Property to access bytes field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.config.dma_max_fragment_size.bytes[31:0]    |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Maximum meaningful memory bytes in one locally initiated DMA    |
        |              |      fragment, excluding Ethernet/oETP headers, word padding, EndOfData |
        |              |      and FCS. The hardware rounds the written value down to a multiple  |
        |              |      of four before validating it. The effective MFS must be at least   |
        |              |      four bytes and at most 4 * floor((MAX_RAW_FRAME_SIZE - 32) / 4).   |
        |              |      With an 8192-byte frame ceiling, the effective range is 4 through  |
        |              |      8160 bytes in steps of four, with reset value 8160. For example,   |
        |              |      31 selects 28, 7 selects 4, and 8161 through 8163 select 8160.     |
        |              |      Hardware snapshots the effective value when it accepts the whole   |
        |              |      peer DMA transfer; later writes apply only to subsequent           |
        |              |      transfers. The final fragment uses the exact remaining byte length |
        |              |      and may be shorter than four bytes. A written value of 0 through   |
        |              |      3, or a rounded value above the synthesized ceiling, rejects a new |
        |              |      transfer with local error code 1 before issuing any memory or      |
        |              |      protocol operation. The CSR retains the unrounded written value.   |
        |              |      This setting does not restrict received peer requests, which use   |
        |              |      the synthesized fragment ceiling, and does not affect RMEM, direct |
        |              |      CSR streams or non-oETP DMA.</p>                                   |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__bytes


    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'bytes':'bytes',
            }








    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_interface_config_dma_max_fragment_size_bytes_0x56886a0b57a4a4fd_cls':
        return super().get_child_by_system_rdl_name(name)









    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.config.dma_max_fragment_size"
    @property
    def rdl_desc(self) -> str:
        return "Common software-selected maximum memory fragment size for locally\ninitiated peer DMA transfers. The synthesis-time frame limit remains fixed."




    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:


        yield self.bytes






class openenoc_endpoint_interface_axis_if_source_data_0x6f3814e57b96a795_cls(RegReadWrite):
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

        self.__tdata:openenoc_endpoint_interface_axis_if_source_data_tdata_0x17c4542c090ffd0e_cls = openenoc_endpoint_interface_axis_if_source_data_tdata_0x17c4542c090ffd0e_cls(
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
    def tdata(self) -> openenoc_endpoint_interface_axis_if_source_data_tdata_0x17c4542c090ffd0e_cls:
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








    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_interface_axis_if_source_data_tdata_0x17c4542c090ffd0e_cls':
        return super().get_child_by_system_rdl_name(name)









    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.axis_if.source.data"
    @property
    def rdl_desc(self) -> str:
        return "Data register for the AXI4-Stream source interface."




    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:


        yield self.tdata






class openenoc_endpoint_interface_axis_if_source_control_0x1457d36a2a537ffd_cls(RegReadWrite):
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

        self.__tvalid:openenoc_endpoint_interface_axis_if_source_control_tvalid_neg_0x267c2272d993b105_cls = openenoc_endpoint_interface_axis_if_source_control_tvalid_neg_0x267c2272d993b105_cls(
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
        self.__tlast:openenoc_endpoint_interface_axis_if_source_control_tlast_neg_0x77cb31118f74f4c3_cls = openenoc_endpoint_interface_axis_if_source_control_tlast_neg_0x77cb31118f74f4c3_cls(
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
        self.__tkeep:openenoc_endpoint_interface_axis_if_source_control_tkeep_0x7eae4751b962a1c_cls = openenoc_endpoint_interface_axis_if_source_control_tkeep_0x7eae4751b962a1c_cls(
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
    def tvalid(self) -> openenoc_endpoint_interface_axis_if_source_control_tvalid_neg_0x267c2272d993b105_cls:
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
    def tlast(self) -> openenoc_endpoint_interface_axis_if_source_control_tlast_neg_0x77cb31118f74f4c3_cls:
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
    def tkeep(self) -> openenoc_endpoint_interface_axis_if_source_control_tkeep_0x7eae4751b962a1c_cls:
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
    def get_child_by_system_rdl_name(self, name: Literal["tvalid"]) -> 'openenoc_endpoint_interface_axis_if_source_control_tvalid_neg_0x267c2272d993b105_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: Literal["tlast"]) -> 'openenoc_endpoint_interface_axis_if_source_control_tlast_neg_0x77cb31118f74f4c3_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: Literal["tkeep"]) -> 'openenoc_endpoint_interface_axis_if_source_control_tkeep_0x7eae4751b962a1c_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_interface_axis_if_source_control_tvalid_neg_0x267c2272d993b105_cls', 'openenoc_endpoint_interface_axis_if_source_control_tlast_neg_0x77cb31118f74f4c3_cls', 'openenoc_endpoint_interface_axis_if_source_control_tkeep_0x7eae4751b962a1c_cls', ]: ...

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






class openenoc_endpoint_interface_axis_if_source_status_0x68db7e29de1dafb9_cls(RegReadOnly):
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

        self.__tready:openenoc_endpoint_interface_axis_if_source_status_tready_0x67560cf213adb45d_cls = openenoc_endpoint_interface_axis_if_source_status_tready_0x67560cf213adb45d_cls(
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
    def tready(self) -> openenoc_endpoint_interface_axis_if_source_status_tready_0x67560cf213adb45d_cls:
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








    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_interface_axis_if_source_status_tready_0x67560cf213adb45d_cls':
        return super().get_child_by_system_rdl_name(name)









    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.axis_if.source.status"
    @property
    def rdl_desc(self) -> str:
        return "Status register for the AXI4-Stream source interface."




    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:


        yield self.tready






class openenoc_endpoint_interface_axis_if_sink_data_neg_0x3d1755264fd08754_cls(RegReadOnly):
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

        self.__tdata:openenoc_endpoint_interface_axis_if_sink_data_tdata_0x2bdcea2731f9535_cls = openenoc_endpoint_interface_axis_if_sink_data_tdata_0x2bdcea2731f9535_cls(
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
    def tdata(self) -> openenoc_endpoint_interface_axis_if_sink_data_tdata_0x2bdcea2731f9535_cls:
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








    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_interface_axis_if_sink_data_tdata_0x2bdcea2731f9535_cls':
        return super().get_child_by_system_rdl_name(name)









    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.axis_if.sink.data"
    @property
    def rdl_desc(self) -> str:
        return "Data register for the AXI4-Stream sink interface."




    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:


        yield self.tdata






class openenoc_endpoint_interface_axis_if_sink_control_neg_0x81b537506a011cb_cls(RegReadWrite):
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

        self.__tready:openenoc_endpoint_interface_axis_if_sink_control_tready_0x4b7af26499667549_cls = openenoc_endpoint_interface_axis_if_sink_control_tready_0x4b7af26499667549_cls(
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
    def tready(self) -> openenoc_endpoint_interface_axis_if_sink_control_tready_0x4b7af26499667549_cls:
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








    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_interface_axis_if_sink_control_tready_0x4b7af26499667549_cls':
        return super().get_child_by_system_rdl_name(name)









    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.axis_if.sink.control"
    @property
    def rdl_desc(self) -> str:
        return "Control register for the AXI4-Stream sink interface."




    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:


        yield self.tready






class openenoc_endpoint_interface_axis_if_sink_status_0x7a844e119be9fac_cls(RegReadOnly):
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

        self.__tvalid:openenoc_endpoint_interface_axis_if_sink_status_tvalid_neg_0x236d83f545db909d_cls = openenoc_endpoint_interface_axis_if_sink_status_tvalid_neg_0x236d83f545db909d_cls(
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
        self.__tlast:openenoc_endpoint_interface_axis_if_sink_status_tlast_0x2d9cca5e6baa0192_cls = openenoc_endpoint_interface_axis_if_sink_status_tlast_0x2d9cca5e6baa0192_cls(
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
        self.__tkeep:openenoc_endpoint_interface_axis_if_sink_status_tkeep_0x62a0176d39c90967_cls = openenoc_endpoint_interface_axis_if_sink_status_tkeep_0x62a0176d39c90967_cls(
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
    def tvalid(self) -> openenoc_endpoint_interface_axis_if_sink_status_tvalid_neg_0x236d83f545db909d_cls:
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
    def tlast(self) -> openenoc_endpoint_interface_axis_if_sink_status_tlast_0x2d9cca5e6baa0192_cls:
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
    def tkeep(self) -> openenoc_endpoint_interface_axis_if_sink_status_tkeep_0x62a0176d39c90967_cls:
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
    def get_child_by_system_rdl_name(self, name: Literal["tvalid"]) -> 'openenoc_endpoint_interface_axis_if_sink_status_tvalid_neg_0x236d83f545db909d_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: Literal["tlast"]) -> 'openenoc_endpoint_interface_axis_if_sink_status_tlast_0x2d9cca5e6baa0192_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: Literal["tkeep"]) -> 'openenoc_endpoint_interface_axis_if_sink_status_tkeep_0x62a0176d39c90967_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_interface_axis_if_sink_status_tvalid_neg_0x236d83f545db909d_cls', 'openenoc_endpoint_interface_axis_if_sink_status_tlast_0x2d9cca5e6baa0192_cls', 'openenoc_endpoint_interface_axis_if_sink_status_tkeep_0x62a0176d39c90967_cls', ]: ...

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






class openenoc_endpoint_interface_non_oetp_dma_tx_buffer_address_0x3ba96c880fb6c736_cls(RegReadWrite):
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

        self.__base:openenoc_endpoint_interface_non_oetp_dma_tx_buffer_address_base_neg_0x28b01b54d9107f5e_cls = openenoc_endpoint_interface_non_oetp_dma_tx_buffer_address_base_neg_0x28b01b54d9107f5e_cls(
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
    def base(self) -> openenoc_endpoint_interface_non_oetp_dma_tx_buffer_address_base_neg_0x28b01b54d9107f5e_cls:
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








    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_interface_non_oetp_dma_tx_buffer_address_base_neg_0x28b01b54d9107f5e_cls':
        return super().get_child_by_system_rdl_name(name)









    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.non_oetp_dma.tx.buffer_address"
    @property
    def rdl_desc(self) -> str:
        return "Local memory address of the non-oETP Ethernet frame to transmit."




    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:


        yield self.base






class openenoc_endpoint_interface_non_oetp_dma_tx_frame_length_0x54623fb834a02104_cls(RegReadWrite):
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

        self.__bytes:openenoc_endpoint_interface_non_oetp_dma_tx_frame_length_bytes_0x6f39179e191d9c64_cls = openenoc_endpoint_interface_non_oetp_dma_tx_frame_length_bytes_0x6f39179e191d9c64_cls(
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
    def bytes(self) -> openenoc_endpoint_interface_non_oetp_dma_tx_frame_length_bytes_0x6f39179e191d9c64_cls:
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








    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_interface_non_oetp_dma_tx_frame_length_bytes_0x6f39179e191d9c64_cls':
        return super().get_child_by_system_rdl_name(name)









    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.non_oetp_dma.tx.frame_length"
    @property
    def rdl_desc(self) -> str:
        return "Length of the complete non-oETP Ethernet frame to transmit."




    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:


        yield self.bytes






class openenoc_endpoint_interface_non_oetp_dma_tx_command_status_neg_0x6f7f3587b3e0b110_cls(RegReadWrite):
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

    __slots__ : list[str] = ['__request', '__clear_errors', '__idle', '__done', '__error', '__error_code']

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

        self.__request:openenoc_endpoint_interface_non_oetp_dma_tx_command_status_request_0x572b2ec04c2729a1_cls = openenoc_endpoint_interface_non_oetp_dma_tx_command_status_request_0x572b2ec04c2729a1_cls(
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
        self.__clear_errors:openenoc_endpoint_interface_non_oetp_dma_tx_command_status_clear_errors_0x12df5b7087b874bd_cls = openenoc_endpoint_interface_non_oetp_dma_tx_command_status_clear_errors_0x12df5b7087b874bd_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=9, msb=9,
                low=9, high=9),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.clear_errors',
            inst_name='clear_errors',
            field_type=int)
        self.__idle:openenoc_endpoint_interface_non_oetp_dma_tx_command_status_idle_neg_0x2426ca7af38c78f9_cls = openenoc_endpoint_interface_non_oetp_dma_tx_command_status_idle_neg_0x2426ca7af38c78f9_cls(
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
        self.__done:openenoc_endpoint_interface_non_oetp_dma_tx_command_status_done_neg_0x38b21b6e94320d9f_cls = openenoc_endpoint_interface_non_oetp_dma_tx_command_status_done_neg_0x38b21b6e94320d9f_cls(
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
        self.__error:openenoc_endpoint_interface_non_oetp_dma_tx_command_status_error_neg_0x36e24688106f345b_cls = openenoc_endpoint_interface_non_oetp_dma_tx_command_status_error_neg_0x36e24688106f345b_cls(
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
        self.__error_code:openenoc_endpoint_interface_non_oetp_dma_tx_command_status_error_code_0x4154b313bb26714d_cls = openenoc_endpoint_interface_non_oetp_dma_tx_command_status_error_code_0x4154b313bb26714d_cls(
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
    def request(self) -> openenoc_endpoint_interface_non_oetp_dma_tx_command_status_request_0x572b2ec04c2729a1_cls:
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
    def clear_errors(self) -> openenoc_endpoint_interface_non_oetp_dma_tx_command_status_clear_errors_0x12df5b7087b874bd_cls:
        """
        Property to access clear_errors field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.non_oetp_dma.tx.command_status.clear_errors |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Writing one clears this channel's error flag and error code.    |
        |              |      Hardware clears the command after accepting it. The command does   |
        |              |      not abort an active transfer, clear done or transferred length, or |
        |              |      complete an IRQ claim. A new failure takes precedence over a       |
        |              |      simultaneous clear. Starting or successfully completing a transfer |
        |              |      preserves a recorded error.</p>                                    |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__clear_errors
    @property
    def idle(self) -> openenoc_endpoint_interface_non_oetp_dma_tx_command_status_idle_neg_0x2426ca7af38c78f9_cls:
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
    def done(self) -> openenoc_endpoint_interface_non_oetp_dma_tx_command_status_done_neg_0x38b21b6e94320d9f_cls:
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
    def error(self) -> openenoc_endpoint_interface_non_oetp_dma_tx_command_status_error_neg_0x36e24688106f345b_cls:
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
        |              |      <p>Sticky error-completion flag. Hardware sets this field when an  |
        |              |      accepted transfer fails. Only command_status.clear_errors or       |
        |              |      endpoint reset clears it; starting or successfully completing      |
        |              |      another transfer preserves a recorded error.</p>                   |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__error
    @property
    def error_code(self) -> openenoc_endpoint_interface_non_oetp_dma_tx_command_status_error_code_0x4154b313bb26714d_cls:
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
        |              |      <p>Sticky error code for the most recent transmit failure:<ul></p> |
        |              |      <li>0: No error.</li> <li>1: Invalid DMA configuration or          |
        |              |      descriptor.</li> <li>2: AXI4-Stream length or TLAST error.</li>    |
        |              |      <li>3: Frame exceeds the supported size or configured buffer       |
        |              |      capacity.</li> <li>4: AXI read SLVERR response.</li> <li>5: AXI    |
        |              |      read DECERR response.</li> <li>6: AXI write SLVERR response.</li>  |
        |              |      <li>7: AXI write DECERR response.</li> <li>8-15: Reserved.</li>    |
        |              |      <p></ul> These errors describe local non-oETP DMA work. Only       |
        |              |      command_status.clear_errors or endpoint reset clears this field. A |
        |              |      new failure replaces the code and takes precedence over a          |
        |              |      simultaneous clear; successful transfers preserve the previous     |
        |              |      failure.</p>                                                       |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__error_code


    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'request':'request','clear_errors':'clear_errors','idle':'idle','done':'done','error':'error','error_code':'error_code',
            }







    # nodes:6

    @overload
    def get_child_by_system_rdl_name(self, name: Literal["request"]) -> 'openenoc_endpoint_interface_non_oetp_dma_tx_command_status_request_0x572b2ec04c2729a1_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: Literal["clear_errors"]) -> 'openenoc_endpoint_interface_non_oetp_dma_tx_command_status_clear_errors_0x12df5b7087b874bd_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: Literal["idle"]) -> 'openenoc_endpoint_interface_non_oetp_dma_tx_command_status_idle_neg_0x2426ca7af38c78f9_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: Literal["done"]) -> 'openenoc_endpoint_interface_non_oetp_dma_tx_command_status_done_neg_0x38b21b6e94320d9f_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: Literal["error"]) -> 'openenoc_endpoint_interface_non_oetp_dma_tx_command_status_error_neg_0x36e24688106f345b_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: Literal["error_code"]) -> 'openenoc_endpoint_interface_non_oetp_dma_tx_command_status_error_code_0x4154b313bb26714d_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_interface_non_oetp_dma_tx_command_status_request_0x572b2ec04c2729a1_cls', 'openenoc_endpoint_interface_non_oetp_dma_tx_command_status_clear_errors_0x12df5b7087b874bd_cls', 'openenoc_endpoint_interface_non_oetp_dma_tx_command_status_idle_neg_0x2426ca7af38c78f9_cls', 'openenoc_endpoint_interface_non_oetp_dma_tx_command_status_done_neg_0x38b21b6e94320d9f_cls', 'openenoc_endpoint_interface_non_oetp_dma_tx_command_status_error_neg_0x36e24688106f345b_cls', 'openenoc_endpoint_interface_non_oetp_dma_tx_command_status_error_code_0x4154b313bb26714d_cls', ]: ...

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
        yield self.clear_errors
        yield self.idle
        yield self.done
        yield self.error
        yield self.error_code






class openenoc_endpoint_interface_non_oetp_dma_tx_transferred_length_0x7625b94e878299c7_cls(RegReadOnly):
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

        self.__bytes:openenoc_endpoint_interface_non_oetp_dma_tx_transferred_length_bytes_0x5c88bb9bca3414c_cls = openenoc_endpoint_interface_non_oetp_dma_tx_transferred_length_bytes_0x5c88bb9bca3414c_cls(
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
    def bytes(self) -> openenoc_endpoint_interface_non_oetp_dma_tx_transferred_length_bytes_0x5c88bb9bca3414c_cls:
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








    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_interface_non_oetp_dma_tx_transferred_length_bytes_0x5c88bb9bca3414c_cls':
        return super().get_child_by_system_rdl_name(name)









    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.non_oetp_dma.tx.transferred_length"
    @property
    def rdl_desc(self) -> str:
        return "Number of bytes transferred for the most recently accepted transmit\nrequest."




    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:


        yield self.bytes






class openenoc_endpoint_interface_non_oetp_dma_rx_buffer_address_neg_0x3f8cc87b2d6147cc_cls(RegReadWrite):
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

        self.__base:openenoc_endpoint_interface_non_oetp_dma_rx_buffer_address_base_neg_0x65ddd3cff5827fd1_cls = openenoc_endpoint_interface_non_oetp_dma_rx_buffer_address_base_neg_0x65ddd3cff5827fd1_cls(
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
    def base(self) -> openenoc_endpoint_interface_non_oetp_dma_rx_buffer_address_base_neg_0x65ddd3cff5827fd1_cls:
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








    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_interface_non_oetp_dma_rx_buffer_address_base_neg_0x65ddd3cff5827fd1_cls':
        return super().get_child_by_system_rdl_name(name)









    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.non_oetp_dma.rx.buffer_address"
    @property
    def rdl_desc(self) -> str:
        return "Local memory address of the receive buffer for a non-oETP Ethernet frame."




    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:


        yield self.base






class openenoc_endpoint_interface_non_oetp_dma_rx_buffer_capacity_neg_0x60c0e4f2a27338ae_cls(RegReadWrite):
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

        self.__bytes:openenoc_endpoint_interface_non_oetp_dma_rx_buffer_capacity_bytes_0x45d2dfc0e4c83489_cls = openenoc_endpoint_interface_non_oetp_dma_rx_buffer_capacity_bytes_0x45d2dfc0e4c83489_cls(
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
    def bytes(self) -> openenoc_endpoint_interface_non_oetp_dma_rx_buffer_capacity_bytes_0x45d2dfc0e4c83489_cls:
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








    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_interface_non_oetp_dma_rx_buffer_capacity_bytes_0x45d2dfc0e4c83489_cls':
        return super().get_child_by_system_rdl_name(name)









    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.non_oetp_dma.rx.buffer_capacity"
    @property
    def rdl_desc(self) -> str:
        return "Capacity of the receive buffer for one complete non-oETP Ethernet frame."




    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:


        yield self.bytes






class openenoc_endpoint_interface_non_oetp_dma_rx_command_status_0x4656e808a3040765_cls(RegReadWrite):
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

    __slots__ : list[str] = ['__request', '__clear_errors', '__idle', '__armed', '__done', '__error', '__error_code']

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

        self.__request:openenoc_endpoint_interface_non_oetp_dma_rx_command_status_request_0xdfa81fa399196fa_cls = openenoc_endpoint_interface_non_oetp_dma_rx_command_status_request_0xdfa81fa399196fa_cls(
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
        self.__clear_errors:openenoc_endpoint_interface_non_oetp_dma_rx_command_status_clear_errors_neg_0x1a408665671a1e4d_cls = openenoc_endpoint_interface_non_oetp_dma_rx_command_status_clear_errors_neg_0x1a408665671a1e4d_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=9, msb=9,
                low=9, high=9),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.clear_errors',
            inst_name='clear_errors',
            field_type=int)
        self.__idle:openenoc_endpoint_interface_non_oetp_dma_rx_command_status_idle_neg_0x6da7c7e99a698bf5_cls = openenoc_endpoint_interface_non_oetp_dma_rx_command_status_idle_neg_0x6da7c7e99a698bf5_cls(
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
        self.__armed:openenoc_endpoint_interface_non_oetp_dma_rx_command_status_armed_neg_0x5554fe7639dcbb69_cls = openenoc_endpoint_interface_non_oetp_dma_rx_command_status_armed_neg_0x5554fe7639dcbb69_cls(
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
        self.__done:openenoc_endpoint_interface_non_oetp_dma_rx_command_status_done_neg_0x69888afa28051618_cls = openenoc_endpoint_interface_non_oetp_dma_rx_command_status_done_neg_0x69888afa28051618_cls(
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
        self.__error:openenoc_endpoint_interface_non_oetp_dma_rx_command_status_error_neg_0x27834466a0a1154b_cls = openenoc_endpoint_interface_non_oetp_dma_rx_command_status_error_neg_0x27834466a0a1154b_cls(
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
        self.__error_code:openenoc_endpoint_interface_non_oetp_dma_rx_command_status_error_code_0x2f5b737b8463ea9f_cls = openenoc_endpoint_interface_non_oetp_dma_rx_command_status_error_code_0x2f5b737b8463ea9f_cls(
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
    def request(self) -> openenoc_endpoint_interface_non_oetp_dma_rx_command_status_request_0xdfa81fa399196fa_cls:
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
    def clear_errors(self) -> openenoc_endpoint_interface_non_oetp_dma_rx_command_status_clear_errors_neg_0x1a408665671a1e4d_cls:
        """
        Property to access clear_errors field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.non_oetp_dma.rx.command_status.clear_errors |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Writing one clears this channel's error flag and error code.    |
        |              |      Hardware clears the command after accepting it. The command does   |
        |              |      not abort an active or armed receive, clear done or received       |
        |              |      length, or complete an IRQ claim. A new failure takes precedence   |
        |              |      over a simultaneous clear. Starting or successfully completing a   |
        |              |      transfer preserves a recorded error.</p>                           |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__clear_errors
    @property
    def idle(self) -> openenoc_endpoint_interface_non_oetp_dma_rx_command_status_idle_neg_0x6da7c7e99a698bf5_cls:
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
    def armed(self) -> openenoc_endpoint_interface_non_oetp_dma_rx_command_status_armed_neg_0x5554fe7639dcbb69_cls:
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
    def done(self) -> openenoc_endpoint_interface_non_oetp_dma_rx_command_status_done_neg_0x69888afa28051618_cls:
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
    def error(self) -> openenoc_endpoint_interface_non_oetp_dma_rx_command_status_error_neg_0x27834466a0a1154b_cls:
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
        |              |      <p>Sticky error-completion flag. Hardware sets this field when an  |
        |              |      accepted receive fails. Only command_status.clear_errors or        |
        |              |      endpoint reset clears it; starting or successfully completing      |
        |              |      another receive preserves a recorded error.</p>                    |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__error
    @property
    def error_code(self) -> openenoc_endpoint_interface_non_oetp_dma_rx_command_status_error_code_0x2f5b737b8463ea9f_cls:
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
        |              |      <p>Sticky error code for the most recent receive failure:<ul></p>  |
        |              |      <li>0: No error.</li> <li>1: Invalid DMA configuration or          |
        |              |      descriptor.</li> <li>2: AXI4-Stream length or TLAST error.</li>    |
        |              |      <li>3: Received frame exceeds the configured buffer capacity.</li> |
        |              |      <li>4: AXI read SLVERR response.</li> <li>5: AXI read DECERR       |
        |              |      response.</li> <li>6: AXI write SLVERR response.</li> <li>7: AXI   |
        |              |      write DECERR response.</li> <li>8-15: Reserved.</li> <p></ul> Only |
        |              |      command_status.clear_errors or endpoint reset clears this field. A |
        |              |      new failure replaces the code and takes precedence over a          |
        |              |      simultaneous clear; successful transfers preserve the previous     |
        |              |      failure.</p>                                                       |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__error_code


    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'request':'request','clear_errors':'clear_errors','idle':'idle','armed':'armed','done':'done','error':'error','error_code':'error_code',
            }







    # nodes:7

    @overload
    def get_child_by_system_rdl_name(self, name: Literal["request"]) -> 'openenoc_endpoint_interface_non_oetp_dma_rx_command_status_request_0xdfa81fa399196fa_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: Literal["clear_errors"]) -> 'openenoc_endpoint_interface_non_oetp_dma_rx_command_status_clear_errors_neg_0x1a408665671a1e4d_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: Literal["idle"]) -> 'openenoc_endpoint_interface_non_oetp_dma_rx_command_status_idle_neg_0x6da7c7e99a698bf5_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: Literal["armed"]) -> 'openenoc_endpoint_interface_non_oetp_dma_rx_command_status_armed_neg_0x5554fe7639dcbb69_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: Literal["done"]) -> 'openenoc_endpoint_interface_non_oetp_dma_rx_command_status_done_neg_0x69888afa28051618_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: Literal["error"]) -> 'openenoc_endpoint_interface_non_oetp_dma_rx_command_status_error_neg_0x27834466a0a1154b_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: Literal["error_code"]) -> 'openenoc_endpoint_interface_non_oetp_dma_rx_command_status_error_code_0x2f5b737b8463ea9f_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_interface_non_oetp_dma_rx_command_status_request_0xdfa81fa399196fa_cls', 'openenoc_endpoint_interface_non_oetp_dma_rx_command_status_clear_errors_neg_0x1a408665671a1e4d_cls', 'openenoc_endpoint_interface_non_oetp_dma_rx_command_status_idle_neg_0x6da7c7e99a698bf5_cls', 'openenoc_endpoint_interface_non_oetp_dma_rx_command_status_armed_neg_0x5554fe7639dcbb69_cls', 'openenoc_endpoint_interface_non_oetp_dma_rx_command_status_done_neg_0x69888afa28051618_cls', 'openenoc_endpoint_interface_non_oetp_dma_rx_command_status_error_neg_0x27834466a0a1154b_cls', 'openenoc_endpoint_interface_non_oetp_dma_rx_command_status_error_code_0x2f5b737b8463ea9f_cls', ]: ...

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
        yield self.clear_errors
        yield self.idle
        yield self.armed
        yield self.done
        yield self.error
        yield self.error_code






class openenoc_endpoint_interface_non_oetp_dma_rx_received_length_neg_0x1263f1c7107a03ec_cls(RegReadOnly):
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

        self.__bytes:openenoc_endpoint_interface_non_oetp_dma_rx_received_length_bytes_0x62104ffbe60d6f40_cls = openenoc_endpoint_interface_non_oetp_dma_rx_received_length_bytes_0x62104ffbe60d6f40_cls(
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
    def bytes(self) -> openenoc_endpoint_interface_non_oetp_dma_rx_received_length_bytes_0x62104ffbe60d6f40_cls:
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








    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_interface_non_oetp_dma_rx_received_length_bytes_0x62104ffbe60d6f40_cls':
        return super().get_child_by_system_rdl_name(name)









    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.non_oetp_dma.rx.received_length"
    @property
    def rdl_desc(self) -> str:
        return "Length of the most recently received non-oETP Ethernet frame."




    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:


        yield self.bytes






class openenoc_endpoint_interface_irq_control_neg_0x3bc98f7c2b3747ac_cls(RegReadWrite):
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

        self.__global_enable:openenoc_endpoint_interface_irq_control_global_enable_neg_0x11fabf129a8cb0ac_cls = openenoc_endpoint_interface_irq_control_global_enable_neg_0x11fabf129a8cb0ac_cls(
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
        self.__clear_errors:openenoc_endpoint_interface_irq_control_clear_errors_neg_0x2d370550f19815f7_cls = openenoc_endpoint_interface_irq_control_clear_errors_neg_0x2d370550f19815f7_cls(
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
    def global_enable(self) -> openenoc_endpoint_interface_irq_control_global_enable_neg_0x11fabf129a8cb0ac_cls:
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
    def clear_errors(self) -> openenoc_endpoint_interface_irq_control_clear_errors_neg_0x2d370550f19815f7_cls:
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
    def get_child_by_system_rdl_name(self, name: Literal["global_enable"]) -> 'openenoc_endpoint_interface_irq_control_global_enable_neg_0x11fabf129a8cb0ac_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: Literal["clear_errors"]) -> 'openenoc_endpoint_interface_irq_control_clear_errors_neg_0x2d370550f19815f7_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_interface_irq_control_global_enable_neg_0x11fabf129a8cb0ac_cls', 'openenoc_endpoint_interface_irq_control_clear_errors_neg_0x2d370550f19815f7_cls', ]: ...

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






class openenoc_endpoint_interface_irq_event_enable_neg_0x22d2c02df8f5fa44_cls(RegReadWrite):
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

    __slots__ : list[str] = ['__peer_dma_complete', '__non_oetp_dma_tx_complete', '__non_oetp_dma_rx_complete', '__non_oetp_direct_tx_complete', '__non_oetp_direct_rx_available', '__rmem_error']

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

        self.__peer_dma_complete:openenoc_endpoint_interface_irq_event_enable_peer_dma_complete_neg_0x4a570f4270edd42b_cls = openenoc_endpoint_interface_irq_event_enable_peer_dma_complete_neg_0x4a570f4270edd42b_cls(
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
        self.__non_oetp_dma_tx_complete:openenoc_endpoint_interface_irq_event_enable_non_oetp_dma_tx_complete_0x486df9956df8d8c8_cls = openenoc_endpoint_interface_irq_event_enable_non_oetp_dma_tx_complete_0x486df9956df8d8c8_cls(
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
        self.__non_oetp_dma_rx_complete:openenoc_endpoint_interface_irq_event_enable_non_oetp_dma_rx_complete_0x6010eb6f58d7cb9d_cls = openenoc_endpoint_interface_irq_event_enable_non_oetp_dma_rx_complete_0x6010eb6f58d7cb9d_cls(
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
        self.__non_oetp_direct_tx_complete:openenoc_endpoint_interface_irq_event_enable_non_oetp_direct_tx_complete_neg_0x4932758f41036931_cls = openenoc_endpoint_interface_irq_event_enable_non_oetp_direct_tx_complete_neg_0x4932758f41036931_cls(
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
        self.__non_oetp_direct_rx_available:openenoc_endpoint_interface_irq_event_enable_non_oetp_direct_rx_available_neg_0x242e0dcdd48d0d6d_cls = openenoc_endpoint_interface_irq_event_enable_non_oetp_direct_rx_available_neg_0x242e0dcdd48d0d6d_cls(
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
        self.__rmem_error:openenoc_endpoint_interface_irq_event_enable_rmem_error_neg_0xd42a525ded0713e_cls = openenoc_endpoint_interface_irq_event_enable_rmem_error_neg_0xd42a525ded0713e_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=5, msb=5,
                low=5, high=5),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.rmem_error',
            inst_name='rmem_error',
            field_type=int)

    @property
    def width(self) -> int:
        return 32

    @property
    def accesswidth(self) -> int:
        return 32



    # build the properties for the fields

    @property
    def peer_dma_complete(self) -> openenoc_endpoint_interface_irq_event_enable_peer_dma_complete_neg_0x4a570f4270edd42b_cls:
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
        |              |      both set when the DMA request was accepted. A failed incoming bulk |
        |              |      DMA request also generates this event for the peer resolved from   |
        |              |      the source MAC. For incoming failures, hardware captures the per-  |
        |              |      peer enable when recording the failure and samples this field at   |
        |              |      IRQ admission. Successful incoming requests generate no event. CSR |
        |              |      error recording and the error response do not wait for IRQ FIFO    |
        |              |      capacity.</p>                                                      |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__peer_dma_complete
    @property
    def non_oetp_dma_tx_complete(self) -> openenoc_endpoint_interface_irq_event_enable_non_oetp_dma_tx_complete_0x486df9956df8d8c8_cls:
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
    def non_oetp_dma_rx_complete(self) -> openenoc_endpoint_interface_irq_event_enable_non_oetp_dma_rx_complete_0x6010eb6f58d7cb9d_cls:
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
    def non_oetp_direct_tx_complete(self) -> openenoc_endpoint_interface_irq_event_enable_non_oetp_direct_tx_complete_neg_0x4932758f41036931_cls:
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
    def non_oetp_direct_rx_available(self) -> openenoc_endpoint_interface_irq_event_enable_non_oetp_direct_rx_available_neg_0x242e0dcdd48d0d6d_cls:
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
    def rmem_error(self) -> openenoc_endpoint_interface_irq_event_enable_rmem_error_neg_0xd42a525ded0713e_cls:
        """
        Property to access rmem_error field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.irq.event_enable.rmem_error                 |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Enables RMEM_ERROR events for locally initiated RMEM failures,  |
        |              |      including timeout and an accepted ERROR_RSP, and failed incoming   |
        |              |      RMEM requests from a resolved peer. Hardware records the           |
        |              |      associated peer's dma.error and dma.error_code before exposing the |
        |              |      event and terminates the failed RMEM access without waiting for    |
        |              |      IRQ FIFO capacity. For locally initiated failures the enable is    |
        |              |      sampled when the failure is recorded; incoming failures sample it  |
        |              |      at IRQ admission. The bulk DMA per-peer irq_enable does not gate   |
        |              |      RMEM_ERROR. Successful RMEM accesses generate no event.</p>        |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__rmem_error


    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'peer_dma_complete':'peer_dma_complete','non_oetp_dma_tx_complete':'non_oetp_dma_tx_complete','non_oetp_dma_rx_complete':'non_oetp_dma_rx_complete','non_oetp_direct_tx_complete':'non_oetp_direct_tx_complete','non_oetp_direct_rx_available':'non_oetp_direct_rx_available','rmem_error':'rmem_error',
            }







    # nodes:6

    @overload
    def get_child_by_system_rdl_name(self, name: Literal["peer_dma_complete"]) -> 'openenoc_endpoint_interface_irq_event_enable_peer_dma_complete_neg_0x4a570f4270edd42b_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: Literal["non_oetp_dma_tx_complete"]) -> 'openenoc_endpoint_interface_irq_event_enable_non_oetp_dma_tx_complete_0x486df9956df8d8c8_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: Literal["non_oetp_dma_rx_complete"]) -> 'openenoc_endpoint_interface_irq_event_enable_non_oetp_dma_rx_complete_0x6010eb6f58d7cb9d_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: Literal["non_oetp_direct_tx_complete"]) -> 'openenoc_endpoint_interface_irq_event_enable_non_oetp_direct_tx_complete_neg_0x4932758f41036931_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: Literal["non_oetp_direct_rx_available"]) -> 'openenoc_endpoint_interface_irq_event_enable_non_oetp_direct_rx_available_neg_0x242e0dcdd48d0d6d_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: Literal["rmem_error"]) -> 'openenoc_endpoint_interface_irq_event_enable_rmem_error_neg_0xd42a525ded0713e_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_interface_irq_event_enable_peer_dma_complete_neg_0x4a570f4270edd42b_cls', 'openenoc_endpoint_interface_irq_event_enable_non_oetp_dma_tx_complete_0x486df9956df8d8c8_cls', 'openenoc_endpoint_interface_irq_event_enable_non_oetp_dma_rx_complete_0x6010eb6f58d7cb9d_cls', 'openenoc_endpoint_interface_irq_event_enable_non_oetp_direct_tx_complete_neg_0x4932758f41036931_cls', 'openenoc_endpoint_interface_irq_event_enable_non_oetp_direct_rx_available_neg_0x242e0dcdd48d0d6d_cls', 'openenoc_endpoint_interface_irq_event_enable_rmem_error_neg_0xd42a525ded0713e_cls', ]: ...

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
        yield self.rmem_error





if __name__ == '__main__':
    pass