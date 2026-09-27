

"""
Python Wrapper for the csr register model

This code was generated from the PeakRDL-python package version 3.1.2

"""









from ....lib import UDPStruct
from ....lib import FieldReadOnly, FieldWriteOnly, FieldReadWrite, Field


# field definitions
    
    
class csr_test_reg_test_field_0x187c510d54a7e9e8_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.test_reg.test_field[31:0]"
    @property
    def rdl_desc(self) -> str:
        return "4-byte test field"
    
    
    

    
    
class openenoc_endpoint_interface_info_rmem_total_depth_neg_0x15d7b4483436acca_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.info.rmem_total_depth[31:0]"
    @property
    def rdl_desc(self) -> str:
        return "Total depth of the shared memory region for all remote peers. This field reflects the RMEM_TOTAL_DEPTH parameter value."
    
    
    

    
    
class openenoc_endpoint_interface_info_num_of_peers_0x2ea7b797103e1d11_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.info.num_of_peers[42:32]"
    @property
    def rdl_desc(self) -> str:
        return "Number of remote peers supported by this openENOC Endpoint Interface instance, from 0 to 2047. This field reflects the NUM_OF_PEERS parameter value."
    
    
    

    
    
class openenoc_endpoint_interface_info_peer_dma_supported_0x846ea5402ad50b6_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.info.peer_dma_supported"
    @property
    def rdl_desc(self) -> str:
        return "Indicates whether DMA transfers associated with configured remote peers are supported."
    
    
    

    
    
class openenoc_endpoint_interface_info_non_oetp_dma_supported_neg_0x63c55e45d7e815ed_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.info.non_oetp_dma_supported"
    @property
    def rdl_desc(self) -> str:
        return "Indicates whether endpoint-level DMA transfers of complete non-oETP Ethernet frames are supported."
    
    
    

    
    
class openenoc_endpoint_interface_info_direct_axis_supported_0x5a7494ada836628a_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.info.direct_axis_supported"
    @property
    def rdl_desc(self) -> str:
        return "Indicates whether direct CSR-driven AXI4-Stream access is supported for non-oETP Ethernet frames."
    
    
    

    
    
class openenoc_endpoint_interface_info_rmem_supported_0x31a010a3b4ffb16f_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.info.rmem_supported"
    @property
    def rdl_desc(self) -> str:
        return "Indicates whether the transparent Remote Memory (RMEM) interface is supported."
    
    
    

    
    
class openenoc_endpoint_interface_info_irq_supported_neg_0x37781e4574954246_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.info.irq_supported"
    @property
    def rdl_desc(self) -> str:
        return "Indicates whether the endpoint interrupt output and interrupt-control logic are implemented."
    
    
    

    
    
class openenoc_endpoint_interface_info_max_dma_frame_size_bytes_neg_0x646cb336a0300ff9_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.info.max_dma_frame_size_bytes[63:48]"
    @property
    def rdl_desc(self) -> str:
        return "Maximum size in bytes of one AXI4-Stream frame generated or consumed by the DMA engine. This field reflects the MAX_DMA_FRAME_SIZE_BYTES parameter value. A value of zero indicates that DMA is not supported."
    
    
    

    
    
class openenoc_endpoint_interface_config_mac_address_lo_word_neg_0x634bc8fba7b18561_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.config.mac_address.lo_word[31:0]"
    @property
    def rdl_desc(self) -> str:
        return "Lower 32 bits [31:0] of the 48-bit MAC address."
    
    
    

    
    
class openenoc_endpoint_interface_config_mac_address_hi_word_neg_0x4269c2855dbfba4a_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.config.mac_address.hi_word[47:32]"
    @property
    def rdl_desc(self) -> str:
        return "Upper 16 bits [47:32] of the 48-bit MAC address."
    
    
    

    
    
class openenoc_endpoint_interface_config_non_oetp_control_receive_mode_neg_0x3477766b39e0aad3_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.config.non_oetp_control.receive_mode[1:0]"
    @property
    def rdl_desc(self) -> str:
        return "Receive mode for non-oETP Ethernet frames:\u003cul\u003e\n\u003cli\u003e0: Drop all non-oETP Ethernet frames.\u003c/li\u003e\n\u003cli\u003e1: Filtered mode. Accept frames addressed to the configured local MAC address and Ethernet broadcast frames.\u003c/li\u003e\n\u003cli\u003e2: Multicast mode. Accept the same frames as filtered mode, plus all multicast-addressed frames.\u003c/li\u003e\n\u003cli\u003e3: Promiscuous mode. Accept all non-oETP Ethernet frames.\u003c/li\u003e\n\u003c/ul\u003e\nAn accepted frame is directed to the non-oETP RX DMA channel when that channel is armed; otherwise it is directed to the CSR AXI4-Stream sink."
    
    
    

    
    
class openenoc_endpoint_interface_axis_if_source_data_tdata_0x108e87bb9b0c173b_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.axis_if.source.data.tdata[31:0]"
    @property
    def rdl_desc(self) -> str:
        return "32-bit data value for the AXI4-Stream source interface."
    
    
    

    
    
class openenoc_endpoint_interface_axis_if_source_control_tvalid_0x6337b1faeb7cf9f2_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.axis_if.source.control.tvalid"
    @property
    def rdl_desc(self) -> str:
        return "Indicates that the AXI4-Stream source interface has valid data to send. Once asserted by software, the field remains asserted until the transfer is accepted by the destination."
    
    
    

    
    
class openenoc_endpoint_interface_axis_if_source_control_tlast_0x6923bb12cf6fdc8c_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.axis_if.source.control.tlast"
    @property
    def rdl_desc(self) -> str:
        return "Indicates the last data word of a frame on the AXI4-Stream source interface."
    
    
    

    
    
class openenoc_endpoint_interface_axis_if_source_control_tkeep_0x29105e430faaac6f_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.axis_if.source.control.tkeep[3:0]"
    @property
    def rdl_desc(self) -> str:
        return "Indicates which byte lanes contain valid data on the AXI4-Stream source interface."
    
    
    

    
    
class openenoc_endpoint_interface_axis_if_source_status_tready_neg_0x6676033b4b3640e3_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.axis_if.source.status.tready"
    @property
    def rdl_desc(self) -> str:
        return "Indicates that the destination AXI4-Stream interface is ready to receive data."
    
    
    

    
    
class openenoc_endpoint_interface_axis_if_sink_data_tdata_0x6491154aba812f3a_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.axis_if.sink.data.tdata[31:0]"
    @property
    def rdl_desc(self) -> str:
        return "32-bit data value for the AXI4-Stream sink interface."
    
    
    

    
    
class openenoc_endpoint_interface_axis_if_sink_control_tready_neg_0x294a0b157efe8c14_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.axis_if.sink.control.tready"
    @property
    def rdl_desc(self) -> str:
        return "Indicates that the AXI4-Stream sink interface is ready to accept a data transfer. Once asserted by software, the field remains asserted until a transfer occurs."
    
    
    

    
    
class openenoc_endpoint_interface_axis_if_sink_status_tvalid_neg_0x38111b5f44b8ef97_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.axis_if.sink.status.tvalid"
    @property
    def rdl_desc(self) -> str:
        return "Indicates that the AXI4-Stream sink interface has valid data to receive."
    
    
    

    
    
class openenoc_endpoint_interface_axis_if_sink_status_tlast_0x47bf5e268a8ae1f3_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.axis_if.sink.status.tlast"
    @property
    def rdl_desc(self) -> str:
        return "Indicates the last data word of a frame on the AXI4-Stream sink interface."
    
    
    

    
    
class openenoc_endpoint_interface_axis_if_sink_status_tkeep_0x61ea3f94bb511b89_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.axis_if.sink.status.tkeep[3:0]"
    @property
    def rdl_desc(self) -> str:
        return "Indicates which byte lanes contain valid data on the AXI4-Stream sink interface."
    
    
    

    
    
class openenoc_endpoint_interface_non_oetp_dma_tx_buffer_address_base_neg_0xbc6b584b3d0921c_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.non_oetp_dma.tx.buffer_address.base[31:0]"
    @property
    def rdl_desc(self) -> str:
        return "32-bit byte address of the first byte of the transmit buffer."
    
    
    

    
    
class openenoc_endpoint_interface_non_oetp_dma_tx_frame_length_bytes_0x6de5a63c03c64bac_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.non_oetp_dma.tx.frame_length.bytes[31:0]"
    @property
    def rdl_desc(self) -> str:
        return "Frame length in bytes. Valid non-zero values shall not exceed info.max_dma_frame_size_bytes."
    
    
    

    
    
class openenoc_endpoint_interface_non_oetp_dma_tx_command_status_request_0x7c1de03386c77085_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.non_oetp_dma.tx.command_status.request"
    @property
    def rdl_desc(self) -> str:
        return "Writing one requests transmission of the configured frame. The field remains asserted until the DMA engine accepts the request. Hardware clears it upon acceptance; while the channel is busy, a newly asserted request remains pending. Software or an RTL controller shall read the completion status and transferred length of the previous request before asserting this field for the next request."
    
    
    


if __name__ == '__main__':
    pass