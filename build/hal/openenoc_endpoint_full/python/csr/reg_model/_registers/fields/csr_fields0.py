

"""
Python Wrapper for the csr register model

This code was generated from the PeakRDL-python package version 3.1.2

"""









from ....lib import UDPStruct
from ....lib import FieldReadOnly, FieldWriteOnly, FieldReadWrite, Field


# field definitions
    
    
class csr_test_reg_test_field_0x6f032ba95bf69a98_cls(FieldReadWrite):
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
    
    
    

    
    
class openenoc_endpoint_interface_info_rmem_total_depth_0x4954d9c8fb4a3a6d_cls(FieldReadOnly):
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
        return "Total depth of the shared memory region for all remote peers. This field\nreflects the RMEM_TOTAL_DEPTH parameter value."
    
    
    

    
    
class openenoc_endpoint_interface_info_num_of_peers_0x65481ce675c297da_cls(FieldReadOnly):
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
        return "Number of remote peers supported by this openENOC Endpoint Interface instance,\nfrom 0 to 2047. This field reflects the NUM_OF_PEERS parameter value."
    
    
    

    
    
class openenoc_endpoint_interface_info_peer_dma_supported_0x59fbf9651c1c8d48_cls(FieldReadOnly):
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
        return "Indicates whether DMA transfers associated with configured remote peers are\nsupported."
    
    
    

    
    
class openenoc_endpoint_interface_info_non_oetp_dma_supported_neg_0x3329e39ce98aff70_cls(FieldReadOnly):
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
        return "Indicates whether endpoint-level DMA transfers of complete non-oETP Ethernet\nframes are supported."
    
    
    

    
    
class openenoc_endpoint_interface_info_direct_axis_supported_neg_0x2bb306b0b80d324d_cls(FieldReadOnly):
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
        return "Indicates whether direct CSR-driven AXI4-Stream access is supported for\nnon-oETP Ethernet frames."
    
    
    

    
    
class openenoc_endpoint_interface_info_rmem_supported_neg_0x5d68dc712329ab72_cls(FieldReadOnly):
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
    
    
    

    
    
class openenoc_endpoint_interface_info_irq_supported_0x185c69633fbe14f3_cls(FieldReadOnly):
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
        return "Indicates whether the endpoint interrupt output and interrupt-control logic\nare implemented."
    
    
    

    
    
class openenoc_endpoint_interface_info_max_dma_frame_size_bytes_0x141331f5a5579c6_cls(FieldReadOnly):
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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.info.max_dma_frame_size_bytes[63:48]"
    @property
    def rdl_desc(self) -> str:
        return "Synthesis-time maximum Ethernet frame size in bytes, excluding FCS. This\nfield reflects the MAX_RAW_FRAME_SIZE parameter value and bounds raw\nnon-oETP DMA frames. The peer DMA memory-fragment ceiling is\n4 * floor((MAX_RAW_FRAME_SIZE - 32) / 4), accounting for the Ethernet\nheader, oETP write metadata, data-word padding and EndOfData. An 8192-byte\nframe limit permits 8160-byte memory fragments. A value of zero indicates\nthat DMA is not supported."
    
    
    

    
    
class openenoc_endpoint_interface_conf_mac_address_lo_word_neg_0x39e7a03ad372ae1d_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.conf.mac_address.lo_word[31:0]              |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Lower 32 bits [31:0] of the 48-bit MAC address.</p>             |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.conf.mac_address.lo_word[31:0]"
    @property
    def rdl_desc(self) -> str:
        return "Lower 32 bits [31:0] of the 48-bit MAC address."
    
    
    

    
    
class openenoc_endpoint_interface_conf_mac_address_hi_word_0x3be0e362a3477c91_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.conf.mac_address.hi_word[47:32]             |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Upper 16 bits [47:32] of the 48-bit MAC address.</p>            |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.conf.mac_address.hi_word[47:32]"
    @property
    def rdl_desc(self) -> str:
        return "Upper 16 bits [47:32] of the 48-bit MAC address."
    
    
    

    
    
class openenoc_endpoint_interface_conf_multicast_address_lo_word_neg_0xcc2ea928df26efe_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.conf.multicast_address.lo_word[31:0]        |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Lower 32 bits [31:0] of the 48-bit multicast MAC address.</p>   |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.conf.multicast_address.lo_word[31:0]"
    @property
    def rdl_desc(self) -> str:
        return "Lower 32 bits [31:0] of the 48-bit multicast MAC address."
    
    
    

    
    
class openenoc_endpoint_interface_conf_multicast_address_hi_word_neg_0x41ad67e676a2b60f_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.conf.multicast_address.hi_word[47:32]       |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Upper 16 bits [47:32] of the 48-bit multicast MAC address.</p>  |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.conf.multicast_address.hi_word[47:32]"
    @property
    def rdl_desc(self) -> str:
        return "Upper 16 bits [47:32] of the 48-bit multicast MAC address."
    
    
    

    
    
class openenoc_endpoint_interface_conf_non_oetp_control_receive_mode_neg_0x25285ab0c80b71c8_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.conf.non_oetp_control.receive_mode[1:0]     |
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
        return "csr.endpoint_interface.conf.non_oetp_control.receive_mode[1:0]"
    @property
    def rdl_desc(self) -> str:
        return "Receive mode for non-oETP Ethernet frames:\u003cul\u003e\n\u003cli\u003e0: Drop all non-oETP Ethernet frames.\u003c/li\u003e\n\u003cli\u003e1: Filtered mode. Accept frames addressed to the configured local MAC\naddress and Ethernet broadcast frames.\u003c/li\u003e\n\u003cli\u003e2: Multicast mode. Accept the same frames as filtered mode, plus all\nmulticast-addressed frames.\u003c/li\u003e\n\u003cli\u003e3: Promiscuous mode. Accept all non-oETP Ethernet frames.\u003c/li\u003e\n\u003c/ul\u003e\nAn accepted frame is directed to the non-oETP RX DMA channel when that channel\nis armed; otherwise it is directed to the CSR AXI4-Stream sink."
    
    
    

    
    
class openenoc_endpoint_interface_conf_rmem_timeout_cycles_neg_0x70d0832b71f863df_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.conf.rmem_timeout.cycles[31:0]              |
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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.conf.rmem_timeout.cycles[31:0]"
    @property
    def rdl_desc(self) -> str:
        return "Maximum wait for an RMEM response in endpoint clock cycles. Zero disables\nthe timeout and permits an indefinite response wait. Hardware samples this\nvalue when it accepts an RMEM operation; subsequent writes apply to later\noperations. The response timer starts after the complete request frame has\nbeen accepted by the Ethernet-facing transmit stream and runs until the\ncomplete matching response is received and validated through Ethernet TLAST.\nRX backpressure counts toward the timeout; remaining local memory completion\ndoes not. A valid response completing on the expiry edge takes priority,\nincluding a valid ERROR_RSP with its reported cause. Hardware does not\nretry; timeout handling and retry policy belong to software. Multicast\nwrites do not wait for a response and do not use this response timeout.\nAn RMEM read timeout terminates the access with all-ones read data and read\nACK; a write timeout terminates with write ACK. The external-RMEM boundary\nuses no ERR signals. Failures set error and error_code in the associated\npeers.entry[].dma register and may generate a separate RMEM_ERROR IRQ event."
    
    
    

    
    
class openenoc_endpoint_interface_conf_dma_timeout_cycles_neg_0x8b21908088a8573_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.conf.dma_timeout.cycles[31:0]               |
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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.conf.dma_timeout.cycles[31:0]"
    @property
    def rdl_desc(self) -> str:
        return "Maximum wait for a response to one peer DMA fragment, in endpoint clock\ncycles. This value is shared by all peers. Zero disables the timeout and\npermits an indefinite response wait. Hardware samples this value when the\noETP engine accepts the fragment request; later writes apply to later\nfragments. The response timer starts after the complete request frame has\nbeen accepted by the Ethernet-facing transmit stream and runs until the\ncomplete matching response is received and validated through Ethernet TLAST,\nincluding EndOfData where present. RX backpressure counts toward the timeout;\nremaining local memory completion does not. A valid response completing on\nthe expiry edge takes priority, including a valid ERROR_RSP with its reported\ncause. On expiry, hardware\naborts the remaining fragments of that DMA transfer and reports error code\n8 (timeout) in the peer DMA status. Hardware does not retry; software decides\nwhether to start another transfer. This timeout does not apply to multicast\nwrites, non-oETP DMA, or transparent RMEM operations."
    
    
    

    
    
class openenoc_endpoint_interface_conf_dma_max_fragment_size_bytes_0x10d2931b375c3289_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.conf.dma_max_fragment_size.bytes[31:0]      |
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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.conf.dma_max_fragment_size.bytes[31:0]"
    @property
    def rdl_desc(self) -> str:
        return "Maximum meaningful memory bytes in one locally initiated DMA fragment,\nexcluding Ethernet/oETP headers, word padding, EndOfData and FCS. The\nhardware rounds the written value down to a multiple of four before\nvalidating it. The effective MFS must be at least four bytes and at most\n4 * floor((MAX_RAW_FRAME_SIZE - 32) / 4). With an 8192-byte frame ceiling,\nthe effective range is 4 through 8160 bytes in steps of four, with reset\nvalue 8160. For example, 31 selects 28, 7 selects 4, and 8161 through 8163\nselect 8160. Hardware snapshots the effective value when it accepts the\nwhole peer DMA transfer; later writes apply only to subsequent transfers.\nThe final fragment uses the exact remaining byte length and may be shorter\nthan four bytes. A written value of 0 through 3, or a rounded value above\nthe synthesized ceiling, rejects a new transfer with local error code 1\nbefore issuing any memory or protocol operation. The CSR retains the\nunrounded written value. This setting does not\nrestrict received peer requests, which use the synthesized fragment\nceiling, and does not affect RMEM, direct CSR streams or non-oETP DMA."
    
    
    

    
    
class openenoc_endpoint_interface_axis_if_source_data_tdata_neg_0x4200337404afbbdb_cls(FieldReadWrite):
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
    
    
    

    
    
class openenoc_endpoint_interface_axis_if_source_control_tvalid_0x660d49a7122f428b_cls(FieldReadWrite):
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
        return "Indicates that the AXI4-Stream source interface has valid data to send.\nOnce asserted by software, the field remains asserted until the transfer is\naccepted by the destination."
    
    
    

    
    
class openenoc_endpoint_interface_axis_if_source_control_tlast_0x1c04b5dfa51b2aae_cls(FieldReadWrite):
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
        return "Indicates the last data word of a frame on the AXI4-Stream source\ninterface."
    
    
    

    
    
class openenoc_endpoint_interface_axis_if_source_control_tkeep_neg_0x1a03c947030aa83f_cls(FieldReadWrite):
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
        return "Indicates which byte lanes contain valid data on the AXI4-Stream source\ninterface."
    
    
    

    
    
class openenoc_endpoint_interface_axis_if_source_status_tready_neg_0x581f7e9d5f5e2f1b_cls(FieldReadOnly):
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
        return "Indicates that the destination AXI4-Stream interface is ready to\nreceive data."
    
    
    

    
    
class openenoc_endpoint_interface_axis_if_sink_data_tdata_neg_0x19ea2d447c51524_cls(FieldReadOnly):
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
    
    
    

    
    
class openenoc_endpoint_interface_axis_if_sink_control_tready_neg_0x125bfc15ab3a7ea1_cls(FieldReadWrite):
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
        return "Indicates that the AXI4-Stream sink interface is ready to accept a\ndata transfer. Once asserted by software, the field remains asserted until\na transfer occurs."
    
    
    

    
    
class openenoc_endpoint_interface_axis_if_sink_status_tvalid_neg_0x273beaeaaceee30e_cls(FieldReadOnly):
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
        return "Indicates that the AXI4-Stream sink interface has valid data\nto receive."
    
    
    


if __name__ == '__main__':
    pass