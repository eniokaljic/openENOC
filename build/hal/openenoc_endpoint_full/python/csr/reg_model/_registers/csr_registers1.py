

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






from .fields import openenoc_endpoint_interface_irq_status_claim_pending_neg_0x1a89fec29eb2077a_cls
from .fields import openenoc_endpoint_interface_irq_status_credit_full_neg_0x64dc71f18f165161_cls
from .fields import openenoc_endpoint_interface_irq_status_overflow_neg_0x1cf2e3e20d3f23cc_cls
from .fields import openenoc_endpoint_interface_irq_status_invalid_complete_neg_0x29ba81e00710d8b1_cls
from .fields import openenoc_endpoint_interface_irq_status_irq_asserted_neg_0x51b7d031f64acc37_cls
from .fields import openenoc_endpoint_interface_irq_status_fifo_level_0x226d3ad9bb8e03e4_cls
from .fields import openenoc_endpoint_interface_irq_status_reserved_count_0x460123819538551a_cls
from .fields import openenoc_endpoint_interface_irq_claim_peer_idx_neg_0x4f359d25dd9f3a5f_cls
from .fields import openenoc_endpoint_interface_irq_claim_source_0x3d5467fc226424d6_cls
from .fields import openenoc_endpoint_interface_irq_claim_sequence_0x32fe5d47acab25d7_cls
from .fields import openenoc_endpoint_interface_irq_claim_valid_neg_0x6afdb5fd6cd7619b_cls
from .fields import openenoc_endpoint_interface_irq_complete_peer_idx_0x13061dca12f481cb_cls
from .fields import openenoc_endpoint_interface_irq_complete_source_0x42454737ca14846c_cls
from .fields import openenoc_endpoint_interface_irq_complete_sequence_0xbd1a53b104c3175_cls
from .fields import openenoc_endpoint_interface_irq_complete_valid_neg_0x3bff197b75bcc364_cls
from .fields import openenoc_endpoint_interface_peers_entry_mac_address_lo_word_0xe1c975d97202fd0_cls
from .fields import openenoc_endpoint_interface_peers_entry_mac_address_hi_word_neg_0x4cc5274056686759_cls
from .fields import openenoc_endpoint_interface_peers_entry_rmem_address_offset_neg_0x6b30420f4eda4c9c_cls
from .fields import openenoc_endpoint_interface_peers_entry_local_address_base_neg_0x56ed9909ffe1ca58_cls
from .fields import openenoc_endpoint_interface_peers_entry_remote_address_base_neg_0x23982d390e4b01f9_cls
from .fields import openenoc_endpoint_interface_peers_entry_size_bytes_0x1f61e557cbf457c3_cls
from .fields import openenoc_endpoint_interface_peers_entry_dma_mode_neg_0x7b78380871f25d0e_cls
from .fields import openenoc_endpoint_interface_peers_entry_dma_irq_enable_0x13adf522afa89a04_cls
from .fields import openenoc_endpoint_interface_peers_entry_dma_request_0x62a887a898cd772c_cls
from .fields import openenoc_endpoint_interface_peers_entry_dma_clear_error_0x346423c994b788f1_cls
from .fields import openenoc_endpoint_interface_peers_entry_dma_idle_0x9e29a917cec77bb_cls
from .fields import openenoc_endpoint_interface_peers_entry_dma_done_neg_0x14e1cabbad6c980c_cls
from .fields import openenoc_endpoint_interface_peers_entry_dma_error_0x7b5e53815b0db6f_cls
from .fields import openenoc_endpoint_interface_peers_entry_dma_error_code_neg_0x184bb6e8f052f02c_cls
from .fields import openenoc_endpoint_interface_rmem_word_data_0x6c032404cbab12f7_cls
from .fields import openenoc_switch_interface_info_table_depth_0x6a23b2f2a4e4cad_cls
from .fields import openenoc_switch_interface_info_num_of_interfaces_0x5b8af1cceefaacbb_cls
from .fields import openenoc_switch_interface_forwarding_control_operation_mode_neg_0x2b68b50bbfa32a1c_cls
from .fields import openenoc_switch_interface_forwarding_control_pause_request_0x3fca318d6d37e18_cls
from .fields import openenoc_switch_interface_forwarding_control_pause_done_neg_0x696e866563f40182_cls
from .fields import openenoc_switch_interface_default_forwarding_bitmap_neg_0x7ddef3e68c368f37_cls
from .fields import openenoc_switch_interface_forwarding_table_entry_mac_address_lo_word_neg_0x1a55655eb47a453c_cls
from .fields import openenoc_switch_interface_forwarding_table_entry_mac_address_hi_word_0x71157053d1016d34_cls
from .fields import openenoc_switch_interface_forwarding_table_entry_iface_bitmap_0x627b1bb55fa275b2_cls
from .fields import openenoc_switch_interface_forwarding_table_entry_config_enabled_0xd904eaff2d4a80d_cls

# register definitions


class openenoc_endpoint_interface_irq_status_0x1fceb31297181213_cls(RegReadOnly):
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

        self.__claim_pending:openenoc_endpoint_interface_irq_status_claim_pending_neg_0x1a89fec29eb2077a_cls = openenoc_endpoint_interface_irq_status_claim_pending_neg_0x1a89fec29eb2077a_cls(
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
        self.__credit_full:openenoc_endpoint_interface_irq_status_credit_full_neg_0x64dc71f18f165161_cls = openenoc_endpoint_interface_irq_status_credit_full_neg_0x64dc71f18f165161_cls(
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
        self.__overflow:openenoc_endpoint_interface_irq_status_overflow_neg_0x1cf2e3e20d3f23cc_cls = openenoc_endpoint_interface_irq_status_overflow_neg_0x1cf2e3e20d3f23cc_cls(
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
        self.__invalid_complete:openenoc_endpoint_interface_irq_status_invalid_complete_neg_0x29ba81e00710d8b1_cls = openenoc_endpoint_interface_irq_status_invalid_complete_neg_0x29ba81e00710d8b1_cls(
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
        self.__irq_asserted:openenoc_endpoint_interface_irq_status_irq_asserted_neg_0x51b7d031f64acc37_cls = openenoc_endpoint_interface_irq_status_irq_asserted_neg_0x51b7d031f64acc37_cls(
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
        self.__fifo_level:openenoc_endpoint_interface_irq_status_fifo_level_0x226d3ad9bb8e03e4_cls = openenoc_endpoint_interface_irq_status_fifo_level_0x226d3ad9bb8e03e4_cls(
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
        self.__reserved_count:openenoc_endpoint_interface_irq_status_reserved_count_0x460123819538551a_cls = openenoc_endpoint_interface_irq_status_reserved_count_0x460123819538551a_cls(
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
    def claim_pending(self) -> openenoc_endpoint_interface_irq_status_claim_pending_neg_0x1a89fec29eb2077a_cls:
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
    def credit_full(self) -> openenoc_endpoint_interface_irq_status_credit_full_neg_0x64dc71f18f165161_cls:
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
    def overflow(self) -> openenoc_endpoint_interface_irq_status_overflow_neg_0x1cf2e3e20d3f23cc_cls:
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
    def invalid_complete(self) -> openenoc_endpoint_interface_irq_status_invalid_complete_neg_0x29ba81e00710d8b1_cls:
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
    def irq_asserted(self) -> openenoc_endpoint_interface_irq_status_irq_asserted_neg_0x51b7d031f64acc37_cls:
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
    def fifo_level(self) -> openenoc_endpoint_interface_irq_status_fifo_level_0x226d3ad9bb8e03e4_cls:
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
    def reserved_count(self) -> openenoc_endpoint_interface_irq_status_reserved_count_0x460123819538551a_cls:
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
    def get_child_by_system_rdl_name(self, name: Literal["claim_pending"]) -> 'openenoc_endpoint_interface_irq_status_claim_pending_neg_0x1a89fec29eb2077a_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: Literal["credit_full"]) -> 'openenoc_endpoint_interface_irq_status_credit_full_neg_0x64dc71f18f165161_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: Literal["overflow"]) -> 'openenoc_endpoint_interface_irq_status_overflow_neg_0x1cf2e3e20d3f23cc_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: Literal["invalid_complete"]) -> 'openenoc_endpoint_interface_irq_status_invalid_complete_neg_0x29ba81e00710d8b1_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: Literal["irq_asserted"]) -> 'openenoc_endpoint_interface_irq_status_irq_asserted_neg_0x51b7d031f64acc37_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: Literal["fifo_level"]) -> 'openenoc_endpoint_interface_irq_status_fifo_level_0x226d3ad9bb8e03e4_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: Literal["reserved_count"]) -> 'openenoc_endpoint_interface_irq_status_reserved_count_0x460123819538551a_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_interface_irq_status_claim_pending_neg_0x1a89fec29eb2077a_cls', 'openenoc_endpoint_interface_irq_status_credit_full_neg_0x64dc71f18f165161_cls', 'openenoc_endpoint_interface_irq_status_overflow_neg_0x1cf2e3e20d3f23cc_cls', 'openenoc_endpoint_interface_irq_status_invalid_complete_neg_0x29ba81e00710d8b1_cls', 'openenoc_endpoint_interface_irq_status_irq_asserted_neg_0x51b7d031f64acc37_cls', 'openenoc_endpoint_interface_irq_status_fifo_level_0x226d3ad9bb8e03e4_cls', 'openenoc_endpoint_interface_irq_status_reserved_count_0x460123819538551a_cls', ]: ...

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






class openenoc_endpoint_interface_irq_claim_0x4e78513b68c694ac_cls(RegReadOnly):
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

        self.__peer_idx:openenoc_endpoint_interface_irq_claim_peer_idx_neg_0x4f359d25dd9f3a5f_cls = openenoc_endpoint_interface_irq_claim_peer_idx_neg_0x4f359d25dd9f3a5f_cls(
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
        self.__source:openenoc_endpoint_interface_irq_claim_source_0x3d5467fc226424d6_cls = openenoc_endpoint_interface_irq_claim_source_0x3d5467fc226424d6_cls(
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
        self.__sequence:openenoc_endpoint_interface_irq_claim_sequence_0x32fe5d47acab25d7_cls = openenoc_endpoint_interface_irq_claim_sequence_0x32fe5d47acab25d7_cls(
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
        self.__valid:openenoc_endpoint_interface_irq_claim_valid_neg_0x6afdb5fd6cd7619b_cls = openenoc_endpoint_interface_irq_claim_valid_neg_0x6afdb5fd6cd7619b_cls(
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
    def peer_idx(self) -> openenoc_endpoint_interface_irq_claim_peer_idx_neg_0x4f359d25dd9f3a5f_cls:
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
        |              |      <p>Zero-based peer index for a PEER_DMA_COMPLETE or RMEM_ERROR     |
        |              |      event, in the range 0 through NUM_OF_PEERS-1. The field is not     |
        |              |      applicable to other event sources and is driven to zero for        |
        |              |      deterministic readback.</p>                                        |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__peer_idx
    @property
    def source(self) -> openenoc_endpoint_interface_irq_claim_source_0x3d5467fc226424d6_cls:
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
        |              |      interface.</li> <li>5: RMEM_ERROR. A locally initiated RMEM        |
        |              |      operation failed. The cause is recorded in                         |
        |              |      peers.entry[peer_idx].dma; peer_idx identifies the associated      |
        |              |      peer.</li> <li>6-15: Reserved.</li> <p></ul> This field is         |
        |              |      meaningful only when valid is set.</p>                             |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__source
    @property
    def sequence(self) -> openenoc_endpoint_interface_irq_claim_sequence_0x32fe5d47acab25d7_cls:
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
    def valid(self) -> openenoc_endpoint_interface_irq_claim_valid_neg_0x6afdb5fd6cd7619b_cls:
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
    def get_child_by_system_rdl_name(self, name: Literal["peer_idx"]) -> 'openenoc_endpoint_interface_irq_claim_peer_idx_neg_0x4f359d25dd9f3a5f_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: Literal["source"]) -> 'openenoc_endpoint_interface_irq_claim_source_0x3d5467fc226424d6_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: Literal["sequence"]) -> 'openenoc_endpoint_interface_irq_claim_sequence_0x32fe5d47acab25d7_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: Literal["valid"]) -> 'openenoc_endpoint_interface_irq_claim_valid_neg_0x6afdb5fd6cd7619b_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_interface_irq_claim_peer_idx_neg_0x4f359d25dd9f3a5f_cls', 'openenoc_endpoint_interface_irq_claim_source_0x3d5467fc226424d6_cls', 'openenoc_endpoint_interface_irq_claim_sequence_0x32fe5d47acab25d7_cls', 'openenoc_endpoint_interface_irq_claim_valid_neg_0x6afdb5fd6cd7619b_cls', ]: ...

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






class openenoc_endpoint_interface_irq_complete_0x56fc9100a31fa49c_cls(RegReadWrite):
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

        self.__peer_idx:openenoc_endpoint_interface_irq_complete_peer_idx_0x13061dca12f481cb_cls = openenoc_endpoint_interface_irq_complete_peer_idx_0x13061dca12f481cb_cls(
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
        self.__source:openenoc_endpoint_interface_irq_complete_source_0x42454737ca14846c_cls = openenoc_endpoint_interface_irq_complete_source_0x42454737ca14846c_cls(
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
        self.__sequence:openenoc_endpoint_interface_irq_complete_sequence_0xbd1a53b104c3175_cls = openenoc_endpoint_interface_irq_complete_sequence_0xbd1a53b104c3175_cls(
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
        self.__valid:openenoc_endpoint_interface_irq_complete_valid_neg_0x3bff197b75bcc364_cls = openenoc_endpoint_interface_irq_complete_valid_neg_0x3bff197b75bcc364_cls(
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
    def peer_idx(self) -> openenoc_endpoint_interface_irq_complete_peer_idx_0x13061dca12f481cb_cls:
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
    def source(self) -> openenoc_endpoint_interface_irq_complete_source_0x42454737ca14846c_cls:
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
    def sequence(self) -> openenoc_endpoint_interface_irq_complete_sequence_0xbd1a53b104c3175_cls:
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
    def valid(self) -> openenoc_endpoint_interface_irq_complete_valid_neg_0x3bff197b75bcc364_cls:
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
    def get_child_by_system_rdl_name(self, name: Literal["peer_idx"]) -> 'openenoc_endpoint_interface_irq_complete_peer_idx_0x13061dca12f481cb_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: Literal["source"]) -> 'openenoc_endpoint_interface_irq_complete_source_0x42454737ca14846c_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: Literal["sequence"]) -> 'openenoc_endpoint_interface_irq_complete_sequence_0xbd1a53b104c3175_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: Literal["valid"]) -> 'openenoc_endpoint_interface_irq_complete_valid_neg_0x3bff197b75bcc364_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_interface_irq_complete_peer_idx_0x13061dca12f481cb_cls', 'openenoc_endpoint_interface_irq_complete_source_0x42454737ca14846c_cls', 'openenoc_endpoint_interface_irq_complete_sequence_0xbd1a53b104c3175_cls', 'openenoc_endpoint_interface_irq_complete_valid_neg_0x3bff197b75bcc364_cls', ]: ...

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






class openenoc_endpoint_interface_peers_entry_mac_address_0x53a93b7228fa3d4a_cls(RegReadWrite):
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

        self.__lo_word:openenoc_endpoint_interface_peers_entry_mac_address_lo_word_0xe1c975d97202fd0_cls = openenoc_endpoint_interface_peers_entry_mac_address_lo_word_0xe1c975d97202fd0_cls(
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
        self.__hi_word:openenoc_endpoint_interface_peers_entry_mac_address_hi_word_neg_0x4cc5274056686759_cls = openenoc_endpoint_interface_peers_entry_mac_address_hi_word_neg_0x4cc5274056686759_cls(
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
    def lo_word(self) -> openenoc_endpoint_interface_peers_entry_mac_address_lo_word_0xe1c975d97202fd0_cls:
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
    def hi_word(self) -> openenoc_endpoint_interface_peers_entry_mac_address_hi_word_neg_0x4cc5274056686759_cls:
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
    def get_child_by_system_rdl_name(self, name: Literal["lo_word"]) -> 'openenoc_endpoint_interface_peers_entry_mac_address_lo_word_0xe1c975d97202fd0_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: Literal["hi_word"]) -> 'openenoc_endpoint_interface_peers_entry_mac_address_hi_word_neg_0x4cc5274056686759_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_interface_peers_entry_mac_address_lo_word_0xe1c975d97202fd0_cls', 'openenoc_endpoint_interface_peers_entry_mac_address_hi_word_neg_0x4cc5274056686759_cls', ]: ...

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






class openenoc_endpoint_interface_peers_entry_rmem_address_0x78be046f42821d8b_cls(RegReadWrite):
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

        self.__offset:openenoc_endpoint_interface_peers_entry_rmem_address_offset_neg_0x6b30420f4eda4c9c_cls = openenoc_endpoint_interface_peers_entry_rmem_address_offset_neg_0x6b30420f4eda4c9c_cls(
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
    def offset(self) -> openenoc_endpoint_interface_peers_entry_rmem_address_offset_neg_0x6b30420f4eda4c9c_cls:
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








    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_interface_peers_entry_rmem_address_offset_neg_0x6b30420f4eda4c9c_cls':
        return super().get_child_by_system_rdl_name(name)









    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].rmem_address"
    @property
    def rdl_desc(self) -> str:
        return "Address offset of the virtual memory region corresponding to the remote\npeer\u0027s memory."




    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:


        yield self.offset






class openenoc_endpoint_interface_peers_entry_local_address_neg_0x37447cba3af05281_cls(RegReadWrite):
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

        self.__base:openenoc_endpoint_interface_peers_entry_local_address_base_neg_0x56ed9909ffe1ca58_cls = openenoc_endpoint_interface_peers_entry_local_address_base_neg_0x56ed9909ffe1ca58_cls(
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
    def base(self) -> openenoc_endpoint_interface_peers_entry_local_address_base_neg_0x56ed9909ffe1ca58_cls:
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








    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_interface_peers_entry_local_address_base_neg_0x56ed9909ffe1ca58_cls':
        return super().get_child_by_system_rdl_name(name)









    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].local_address"
    @property
    def rdl_desc(self) -> str:
        return "Start address of the local memory region for DMA transfers."




    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:


        yield self.base






class openenoc_endpoint_interface_peers_entry_remote_address_neg_0x5704b642b4374288_cls(RegReadWrite):
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

        self.__base:openenoc_endpoint_interface_peers_entry_remote_address_base_neg_0x23982d390e4b01f9_cls = openenoc_endpoint_interface_peers_entry_remote_address_base_neg_0x23982d390e4b01f9_cls(
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
    def base(self) -> openenoc_endpoint_interface_peers_entry_remote_address_base_neg_0x23982d390e4b01f9_cls:
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








    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_interface_peers_entry_remote_address_base_neg_0x23982d390e4b01f9_cls':
        return super().get_child_by_system_rdl_name(name)









    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].remote_address"
    @property
    def rdl_desc(self) -> str:
        return "Start address of the remote peer\u0027s memory region."




    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:


        yield self.base






class openenoc_endpoint_interface_peers_entry_size_0x1bf7d36766fec747_cls(RegReadWrite):
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

        self.__bytes:openenoc_endpoint_interface_peers_entry_size_bytes_0x1f61e557cbf457c3_cls = openenoc_endpoint_interface_peers_entry_size_bytes_0x1f61e557cbf457c3_cls(
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
    def bytes(self) -> openenoc_endpoint_interface_peers_entry_size_bytes_0x1f61e557cbf457c3_cls:
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








    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_interface_peers_entry_size_bytes_0x1f61e557cbf457c3_cls':
        return super().get_child_by_system_rdl_name(name)









    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].size"
    @property
    def rdl_desc(self) -> str:
        return "Size of the remote peer\u0027s memory region."




    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:


        yield self.bytes






class openenoc_endpoint_interface_peers_entry_dma_0x23366d4e2436f2c6_cls(RegReadWrite):
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
    |              |      <p>DMA/RMEM configuration and control for the remote peer, with    |
    |              |      shared sticky error reporting. RMEM and bulk DMA retain separate   |
    |              |      IRQ event classes.</p>                                             |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__mode', '__irq_enable', '__request', '__clear_error', '__idle', '__done', '__error', '__error_code']

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

        self.__mode:openenoc_endpoint_interface_peers_entry_dma_mode_neg_0x7b78380871f25d0e_cls = openenoc_endpoint_interface_peers_entry_dma_mode_neg_0x7b78380871f25d0e_cls(
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
        self.__irq_enable:openenoc_endpoint_interface_peers_entry_dma_irq_enable_0x13adf522afa89a04_cls = openenoc_endpoint_interface_peers_entry_dma_irq_enable_0x13adf522afa89a04_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=2, msb=2,
                low=2, high=2),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.irq_enable',
            inst_name='irq_enable',
            field_type=int)
        self.__request:openenoc_endpoint_interface_peers_entry_dma_request_0x62a887a898cd772c_cls = openenoc_endpoint_interface_peers_entry_dma_request_0x62a887a898cd772c_cls(
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
        self.__clear_error:openenoc_endpoint_interface_peers_entry_dma_clear_error_0x346423c994b788f1_cls = openenoc_endpoint_interface_peers_entry_dma_clear_error_0x346423c994b788f1_cls(
            parent_register=self,
            size_props=FieldSizeProps(
                width=1,
                lsb=9, msb=9,
                low=9, high=9),
            misc_props=FieldMiscProps(
                default=0,
                is_volatile=False),
            logger_handle=logger_handle+'.clear_error',
            inst_name='clear_error',
            field_type=int)
        self.__idle:openenoc_endpoint_interface_peers_entry_dma_idle_0x9e29a917cec77bb_cls = openenoc_endpoint_interface_peers_entry_dma_idle_0x9e29a917cec77bb_cls(
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
        self.__done:openenoc_endpoint_interface_peers_entry_dma_done_neg_0x14e1cabbad6c980c_cls = openenoc_endpoint_interface_peers_entry_dma_done_neg_0x14e1cabbad6c980c_cls(
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
        self.__error:openenoc_endpoint_interface_peers_entry_dma_error_0x7b5e53815b0db6f_cls = openenoc_endpoint_interface_peers_entry_dma_error_0x7b5e53815b0db6f_cls(
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
        self.__error_code:openenoc_endpoint_interface_peers_entry_dma_error_code_neg_0x184bb6e8f052f02c_cls = openenoc_endpoint_interface_peers_entry_dma_error_code_neg_0x184bb6e8f052f02c_cls(
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
    def mode(self) -> openenoc_endpoint_interface_peers_entry_dma_mode_neg_0x7b78380871f25d0e_cls:
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
        |              |      <p>DMA mode and responder access policy for the remote             |
        |              |      peer:<ul></p> <li>0: Disabled. Locally initiated DMA and           |
        |              |      transparent RMEM operations are disabled, and incoming oETP memory |
        |              |      requests from this peer are rejected.</li>  <li>1: Transparent     |
        |              |      RMEM mode. Accesses to the virtual RMEM region are translated into |
        |              |      individual remote memory accesses. Incoming transparent RMEM read  |
        |              |      and write requests from this peer are permitted. Bulk DMA read and |
        |              |      write requests are rejected.</li>  <li>2: Mirror-to-local mode. A  |
        |              |      locally initiated DMA request fetches the remote memory region     |
        |              |      into the configured local memory region using remote DMA reads. On |
        |              |      the responder side, incoming bulk DMA write requests from this     |
        |              |      peer are permitted and target the configured local memory region.  |
        |              |      Incoming bulk DMA read requests are rejected.</li>  <li>3: Mirror- |
        |              |      to-remote mode. A locally initiated DMA request sends the          |
        |              |      configured local memory region to the remote memory region using   |
        |              |      remote DMA writes. On the responder side, incoming bulk DMA read   |
        |              |      requests from this peer are permitted and source data from the     |
        |              |      configured local memory region. Incoming bulk DMA write requests   |
        |              |      are rejected.</li>  </ul> <p>Consequently, a mirror relationship   |
        |              |      uses complementary modes: an initiator operating in mirror-to-     |
        |              |      local mode communicates with a responder entry configured as       |
        |              |      mirror-to-remote, while an initiator operating in mirror-to-remote |
        |              |      mode communicates with a responder entry configured as mirror-to-  |
        |              |      local.</p>                                                         |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__mode
    @property
    def irq_enable(self) -> openenoc_endpoint_interface_peers_entry_dma_irq_enable_0x13adf522afa89a04_cls:
        """
        Property to access irq_enable field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-                |
        |              |      1].dma.irq_enable                                                  |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Enables generation of a PEER_DMA_COMPLETE IRQ event for this    |
        |              |      peer. Hardware samples this field together with                    |
        |              |      irq.event_enable.peer_dma_complete when it accepts the peer DMA    |
        |              |      request. Changing the field while a transfer is active does not    |
        |              |      affect that transfer. Disabling the field does not affect DMA      |
        |              |      execution or the done, error, and error_code status fields. For a  |
        |              |      failed incoming bulk DMA request, this field is captured when      |
        |              |      recording the failure and irq.event_enable.peer_dma_complete is    |
        |              |      sampled at IRQ admission. The event identifies this peer by the    |
        |              |      received source MAC. Successful incoming requests generate no      |
        |              |      event. RMEM errors use their separate irq.event_enable.rmem_error  |
        |              |      path.</p>                                                          |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__irq_enable
    @property
    def request(self) -> openenoc_endpoint_interface_peers_entry_dma_request_0x62a887a898cd772c_cls:
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
        |              |      shall read the completion status of the previous request before    |
        |              |      asserting this field for the next request and shall keep the peer  |
        |              |      configuration stable while this field is asserted.</p>             |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__request
    @property
    def clear_error(self) -> openenoc_endpoint_interface_peers_entry_dma_clear_error_0x346423c994b788f1_cls:
        """
        Property to access clear_error field of the register

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-                |
        |              |      1].dma.clear_error                                                 |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Writing one clears this peer's shared RMEM/DMA error flag and   |
        |              |      error code. The field remains asserted until hardware accepts and  |
        |              |      clears the command. It does not abort an active operation, clear   |
        |              |      done, or complete an IRQ claim. A new failure takes precedence     |
        |              |      over a simultaneous clear. Starting or successfully completing an  |
        |              |      operation does not clear a previously recorded error.</p>          |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__clear_error
    @property
    def idle(self) -> openenoc_endpoint_interface_peers_entry_dma_idle_0x9e29a917cec77bb_cls:
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
    def done(self) -> openenoc_endpoint_interface_peers_entry_dma_done_neg_0x14e1cabbad6c980c_cls:
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
    def error(self) -> openenoc_endpoint_interface_peers_entry_dma_error_0x7b5e53815b0db6f_cls:
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
        |              |      <p>Shared sticky RMEM/DMA error flag for this peer. Hardware sets  |
        |              |      this field when a locally initiated RMEM access or bulk DMA        |
        |              |      transfer fails, or when servicing an incoming RMEM or bulk DMA     |
        |              |      request from this peer fails. Received requests are associated by  |
        |              |      source MAC. An incoming failure records its code before exposing   |
        |              |      its error response, independently of IRQ enable; it does not       |
        |              |      change the locally initiated dma.request, idle, or done state. An  |
        |              |      incomplete incoming DMA data frame records remote stream code 10.  |
        |              |      Multicast response suppression does not suppress this local error  |
        |              |      record or an enabled event. Only dma.clear_error or endpoint reset |
        |              |      clears a latched error; starting or successfully completing        |
        |              |      another operation does not clear it. The flag is independent of    |
        |              |      the IRQ event-enable fields.</p>                                   |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__error
    @property
    def error_code(self) -> openenoc_endpoint_interface_peers_entry_dma_error_code_neg_0x184bb6e8f052f02c_cls:
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
        |              |      <p>Shared sticky code for the most recent RMEM or bulk DMA failure |
        |              |      for this peer:<ul></p> <li>0: No error.</li> <li>1: Local invalid  |
        |              |      request, configuration, descriptor, or parameters.</li> <li>2:     |
        |              |      Local stream/PDU length or TLAST error.</li> <li>3: Local          |
        |              |      supported-size or buffer-capacity overflow.</li> <li>4: Local AXI  |
        |              |      read SLVERR response.</li> <li>5: Local AXI read DECERR            |
        |              |      response.</li> <li>6: Local AXI write SLVERR response.</li> <li>7: |
        |              |      Local AXI write DECERR response.</li> <li>8: Local peer response   |
        |              |      timeout or Request ID wrap collision. An RMEM access               |
        |              |      terminates through its ACK-only boundary; a bulk DMA timeout       |
        |              |      aborts     the remaining fragments. Hardware does not retry.</li>  |
        |              |      <li>9: Remote invalid request, configuration, descriptor, or       |
        |              |      parameters.</li> <li>10: Remote stream/PDU length or TLAST error.  |
        |              |      Also used directly by     the receiver of an incomplete            |
        |              |      DMA_WRITE_REQ or DMA_READ_RSP,     including missing or incorrect  |
        |              |      EndOfData.</li> <li>11: Remote supported-size or buffer-capacity   |
        |              |      overflow.</li> <li>12: Remote AXI read SLVERR response.</li>       |
        |              |      <li>13: Remote AXI read DECERR response.</li> <li>14: Remote AXI   |
        |              |      write SLVERR response.</li> <li>15: Remote AXI write DECERR        |
        |              |      response.</li> <p></ul> Codes 1-8 describe errors detected by this |
        |              |      endpoint, including malformed responses, local memory failures,    |
        |              |      and failures while servicing received requests. Codes 9-15         |
        |              |      describe failures reported by the responding peer through a valid  |
        |              |      ERROR_RSP. Code 10 additionally reports an incomplete incoming DMA |
        |              |      data frame detected at this endpoint, without requiring an         |
        |              |      ERROR_RSP first. A missing or incorrect EndOfData uses this same   |
        |              |      code even when Ethernet padding masks the short data length. A     |
        |              |      receiver of an incomplete unicast DMA_WRITE_REQ records CSR code   |
        |              |      10 but sends ERROR_RSP wire cause 2; multicast writes generate no  |
        |              |      response. ERROR_RSP carries a 32-bit cause in the range 1-7, which |
        |              |      the initiating oETP engine validates and maps to CSR code = 8 +    |
        |              |      wire code. Values outside 1-7 are invalid response parameters and  |
        |              |      record local code 1; they must not be truncated or mistaken for    |
        |              |      local TIMEOUT = 8. The oETP initiator completion channel carries   |
        |              |      this final CSR encoding for both RMEM and bulk DMA. The responder  |
        |              |      completion channel reports its cause 1-7 for serialization as      |
        |              |      ERROR_RSP; cause 2 on an incomplete received bulk write            |
        |              |      corresponds to receiver CSR code 10. Hardware clears this field    |
        |              |      only on dma.clear_error or endpoint reset. Successful operations   |
        |              |      preserve a recorded failure. A new failure replaces the code and   |
        |              |      takes precedence over a simultaneous clear. A failed streaming     |
        |              |      transfer may have partially modified memory; error reporting does  |
        |              |      not provide rollback or an exact count of modified bytes. Software |
        |              |      manages buffer synchronization and recovery.</p>                   |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__error_code


    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'mode':'mode','irq_enable':'irq_enable','request':'request','clear_error':'clear_error','idle':'idle','done':'done','error':'error','error_code':'error_code',
            }







    # nodes:8

    @overload
    def get_child_by_system_rdl_name(self, name: Literal["mode"]) -> 'openenoc_endpoint_interface_peers_entry_dma_mode_neg_0x7b78380871f25d0e_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: Literal["irq_enable"]) -> 'openenoc_endpoint_interface_peers_entry_dma_irq_enable_0x13adf522afa89a04_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: Literal["request"]) -> 'openenoc_endpoint_interface_peers_entry_dma_request_0x62a887a898cd772c_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: Literal["clear_error"]) -> 'openenoc_endpoint_interface_peers_entry_dma_clear_error_0x346423c994b788f1_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: Literal["idle"]) -> 'openenoc_endpoint_interface_peers_entry_dma_idle_0x9e29a917cec77bb_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: Literal["done"]) -> 'openenoc_endpoint_interface_peers_entry_dma_done_neg_0x14e1cabbad6c980c_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: Literal["error"]) -> 'openenoc_endpoint_interface_peers_entry_dma_error_0x7b5e53815b0db6f_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: Literal["error_code"]) -> 'openenoc_endpoint_interface_peers_entry_dma_error_code_neg_0x184bb6e8f052f02c_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_endpoint_interface_peers_entry_dma_mode_neg_0x7b78380871f25d0e_cls', 'openenoc_endpoint_interface_peers_entry_dma_irq_enable_0x13adf522afa89a04_cls', 'openenoc_endpoint_interface_peers_entry_dma_request_0x62a887a898cd772c_cls', 'openenoc_endpoint_interface_peers_entry_dma_clear_error_0x346423c994b788f1_cls', 'openenoc_endpoint_interface_peers_entry_dma_idle_0x9e29a917cec77bb_cls', 'openenoc_endpoint_interface_peers_entry_dma_done_neg_0x14e1cabbad6c980c_cls', 'openenoc_endpoint_interface_peers_entry_dma_error_0x7b5e53815b0db6f_cls', 'openenoc_endpoint_interface_peers_entry_dma_error_code_neg_0x184bb6e8f052f02c_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)








    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma"
    @property
    def rdl_desc(self) -> str:
        return "DMA/RMEM configuration and control for the remote peer, with shared\nsticky error reporting. RMEM and bulk DMA retain separate IRQ event classes."




    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:


        yield self.mode
        yield self.irq_enable
        yield self.request
        yield self.clear_error
        yield self.idle
        yield self.done
        yield self.error
        yield self.error_code






class openenoc_endpoint_interface_rmem_word_neg_0x3107ed52a4b4c065_cls(RegReadWrite):
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

        self.__data:openenoc_endpoint_interface_rmem_word_data_0x6c032404cbab12f7_cls = openenoc_endpoint_interface_rmem_word_data_0x6c032404cbab12f7_cls(
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
    def data(self) -> openenoc_endpoint_interface_rmem_word_data_0x6c032404cbab12f7_cls:
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








    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_endpoint_interface_rmem_word_data_0x6c032404cbab12f7_cls':
        return super().get_child_by_system_rdl_name(name)









    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]"
    @property
    def rdl_desc(self) -> str:
        return "32-bit word in the virtual memory region."




    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:


        yield self.data


class openenoc_endpoint_interface_rmem_word_neg_0x3107ed52a4b4c065_cls_array(RegReadWriteArray):
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
        return openenoc_endpoint_interface_rmem_word_neg_0x3107ed52a4b4c065_cls

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]"
    @property
    def rdl_desc(self) -> str:
        return "32-bit word in the virtual memory region."






class openenoc_switch_interface_info_0x1e02a0c79a5f5b28_cls(RegReadOnly):
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

        self.__table_depth:openenoc_switch_interface_info_table_depth_0x6a23b2f2a4e4cad_cls = openenoc_switch_interface_info_table_depth_0x6a23b2f2a4e4cad_cls(
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
        self.__num_of_interfaces:openenoc_switch_interface_info_num_of_interfaces_0x5b8af1cceefaacbb_cls = openenoc_switch_interface_info_num_of_interfaces_0x5b8af1cceefaacbb_cls(
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
    def table_depth(self) -> openenoc_switch_interface_info_table_depth_0x6a23b2f2a4e4cad_cls:
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
    def num_of_interfaces(self) -> openenoc_switch_interface_info_num_of_interfaces_0x5b8af1cceefaacbb_cls:
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
    def get_child_by_system_rdl_name(self, name: Literal["table_depth"]) -> 'openenoc_switch_interface_info_table_depth_0x6a23b2f2a4e4cad_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: Literal["num_of_interfaces"]) -> 'openenoc_switch_interface_info_num_of_interfaces_0x5b8af1cceefaacbb_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_switch_interface_info_table_depth_0x6a23b2f2a4e4cad_cls', 'openenoc_switch_interface_info_num_of_interfaces_0x5b8af1cceefaacbb_cls', ]: ...

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






class openenoc_switch_interface_forwarding_control_0x72905725afdb3c37_cls(RegReadWrite):
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

        self.__operation_mode:openenoc_switch_interface_forwarding_control_operation_mode_neg_0x2b68b50bbfa32a1c_cls = openenoc_switch_interface_forwarding_control_operation_mode_neg_0x2b68b50bbfa32a1c_cls(
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
        self.__pause_request:openenoc_switch_interface_forwarding_control_pause_request_0x3fca318d6d37e18_cls = openenoc_switch_interface_forwarding_control_pause_request_0x3fca318d6d37e18_cls(
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
        self.__pause_done:openenoc_switch_interface_forwarding_control_pause_done_neg_0x696e866563f40182_cls = openenoc_switch_interface_forwarding_control_pause_done_neg_0x696e866563f40182_cls(
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
    def operation_mode(self) -> openenoc_switch_interface_forwarding_control_operation_mode_neg_0x2b68b50bbfa32a1c_cls:
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
    def pause_request(self) -> openenoc_switch_interface_forwarding_control_pause_request_0x3fca318d6d37e18_cls:
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
    def pause_done(self) -> openenoc_switch_interface_forwarding_control_pause_done_neg_0x696e866563f40182_cls:
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
    def get_child_by_system_rdl_name(self, name: Literal["operation_mode"]) -> 'openenoc_switch_interface_forwarding_control_operation_mode_neg_0x2b68b50bbfa32a1c_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: Literal["pause_request"]) -> 'openenoc_switch_interface_forwarding_control_pause_request_0x3fca318d6d37e18_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: Literal["pause_done"]) -> 'openenoc_switch_interface_forwarding_control_pause_done_neg_0x696e866563f40182_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_switch_interface_forwarding_control_operation_mode_neg_0x2b68b50bbfa32a1c_cls', 'openenoc_switch_interface_forwarding_control_pause_request_0x3fca318d6d37e18_cls', 'openenoc_switch_interface_forwarding_control_pause_done_neg_0x696e866563f40182_cls', ]: ...

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






class openenoc_switch_interface_default_forwarding_0x60c2651012bf5117_cls(RegReadWrite):
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

        self.__bitmap:openenoc_switch_interface_default_forwarding_bitmap_neg_0x7ddef3e68c368f37_cls = openenoc_switch_interface_default_forwarding_bitmap_neg_0x7ddef3e68c368f37_cls(
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
    def bitmap(self) -> openenoc_switch_interface_default_forwarding_bitmap_neg_0x7ddef3e68c368f37_cls:
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








    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_switch_interface_default_forwarding_bitmap_neg_0x7ddef3e68c368f37_cls':
        return super().get_child_by_system_rdl_name(name)









    @property
    def rdl_name(self) -> str:
        return "csr.switch_interface.default_forwarding"
    @property
    def rdl_desc(self) -> str:
        return "Defines the destination interface or interfaces for frames that do not match any enabled forwarding table entry."




    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:


        yield self.bitmap






class openenoc_switch_interface_forwarding_table_entry_mac_address_neg_0x28320c38b39a8f77_cls(RegReadWrite):
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

        self.__lo_word:openenoc_switch_interface_forwarding_table_entry_mac_address_lo_word_neg_0x1a55655eb47a453c_cls = openenoc_switch_interface_forwarding_table_entry_mac_address_lo_word_neg_0x1a55655eb47a453c_cls(
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
        self.__hi_word:openenoc_switch_interface_forwarding_table_entry_mac_address_hi_word_0x71157053d1016d34_cls = openenoc_switch_interface_forwarding_table_entry_mac_address_hi_word_0x71157053d1016d34_cls(
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
    def lo_word(self) -> openenoc_switch_interface_forwarding_table_entry_mac_address_lo_word_neg_0x1a55655eb47a453c_cls:
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
    def hi_word(self) -> openenoc_switch_interface_forwarding_table_entry_mac_address_hi_word_0x71157053d1016d34_cls:
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
    def get_child_by_system_rdl_name(self, name: Literal["lo_word"]) -> 'openenoc_switch_interface_forwarding_table_entry_mac_address_lo_word_neg_0x1a55655eb47a453c_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: Literal["hi_word"]) -> 'openenoc_switch_interface_forwarding_table_entry_mac_address_hi_word_0x71157053d1016d34_cls': ...


    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openenoc_switch_interface_forwarding_table_entry_mac_address_lo_word_neg_0x1a55655eb47a453c_cls', 'openenoc_switch_interface_forwarding_table_entry_mac_address_hi_word_0x71157053d1016d34_cls', ]: ...

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






class openenoc_switch_interface_forwarding_table_entry_iface_0x5f2bbbc9eb9056b5_cls(RegReadWrite):
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

        self.__bitmap:openenoc_switch_interface_forwarding_table_entry_iface_bitmap_0x627b1bb55fa275b2_cls = openenoc_switch_interface_forwarding_table_entry_iface_bitmap_0x627b1bb55fa275b2_cls(
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
    def bitmap(self) -> openenoc_switch_interface_forwarding_table_entry_iface_bitmap_0x627b1bb55fa275b2_cls:
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








    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_switch_interface_forwarding_table_entry_iface_bitmap_0x627b1bb55fa275b2_cls':
        return super().get_child_by_system_rdl_name(name)









    @property
    def rdl_name(self) -> str:
        return "csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].iface"
    @property
    def rdl_desc(self) -> str:
        return "Forwarding interface information associated with this forwarding table entry."




    def __iter__(self) -> Iterator[Union[FieldReadOnly,FieldWriteOnly,FieldReadWrite]]:


        yield self.bitmap






class openenoc_switch_interface_forwarding_table_entry_config_0x10dc5c75c262d64e_cls(RegReadWrite):
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

        self.__enabled:openenoc_switch_interface_forwarding_table_entry_config_enabled_0xd904eaff2d4a80d_cls = openenoc_switch_interface_forwarding_table_entry_config_enabled_0xd904eaff2d4a80d_cls(
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
    def enabled(self) -> openenoc_switch_interface_forwarding_table_entry_config_enabled_0xd904eaff2d4a80d_cls:
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








    def get_child_by_system_rdl_name(self, name: Any) -> 'openenoc_switch_interface_forwarding_table_entry_config_enabled_0xd904eaff2d4a80d_cls':
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