

"""
Python Wrapper for the csr register model

This code was generated from the PeakRDL-python package version 3.1.2

"""









from ....lib import UDPStruct
from ....lib import FieldReadOnly, FieldWriteOnly, FieldReadWrite, Field


# field definitions


class csr_test_reg_test_field_0x2d10b449974b1aac_cls(FieldReadWrite):
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






class openenoc_endpoint_interface_info_rmem_total_depth_0x1c7e4a55a4858634_cls(FieldReadOnly):
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






class openenoc_endpoint_interface_info_num_of_peers_neg_0x5518c59f02e0f143_cls(FieldReadOnly):
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






class openenoc_endpoint_interface_info_peer_dma_supported_neg_0xd95a983276af65f_cls(FieldReadOnly):
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






class openenoc_endpoint_interface_info_non_oetp_dma_supported_neg_0x4be54bc85b3f2c81_cls(FieldReadOnly):
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






class openenoc_endpoint_interface_info_direct_axis_supported_neg_0x5868185a85cd4b2f_cls(FieldReadOnly):
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






class openenoc_endpoint_interface_info_rmem_supported_0x14f76811800d8a02_cls(FieldReadOnly):
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






class openenoc_endpoint_interface_info_irq_supported_0x6035e9c40a51546d_cls(FieldReadOnly):
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






class openenoc_endpoint_interface_info_max_dma_frame_size_bytes_0x7c2002dfead2b04b_cls(FieldReadOnly):
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






class openenoc_endpoint_interface_config_mac_address_lo_word_neg_0x48b21d5256898003_cls(FieldReadWrite):
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






class openenoc_endpoint_interface_config_mac_address_hi_word_0x5c389cda01b0a010_cls(FieldReadWrite):
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






class openenoc_endpoint_interface_config_multicast_address_lo_word_0xa51d51e8c91ffaf_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.config.multicast_address.lo_word[31:0]"
    @property
    def rdl_desc(self) -> str:
        return "Lower 32 bits [31:0] of the 48-bit multicast MAC address."






class openenoc_endpoint_interface_config_multicast_address_hi_word_0x2ab309c4ffe4e9d4_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.config.multicast_address.hi_word[47:32]"
    @property
    def rdl_desc(self) -> str:
        return "Upper 16 bits [47:32] of the 48-bit multicast MAC address."






class openenoc_endpoint_interface_config_non_oetp_control_receive_mode_neg_0xd42228a8c7c937a_cls(FieldReadWrite):
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
        return "Receive mode for non-oETP Ethernet frames:\u003cul\u003e\n\u003cli\u003e0: Drop all non-oETP Ethernet frames.\u003c/li\u003e\n\u003cli\u003e1: Filtered mode. Accept frames addressed to the configured local MAC\naddress and Ethernet broadcast frames.\u003c/li\u003e\n\u003cli\u003e2: Multicast mode. Accept the same frames as filtered mode, plus all\nmulticast-addressed frames.\u003c/li\u003e\n\u003cli\u003e3: Promiscuous mode. Accept all non-oETP Ethernet frames.\u003c/li\u003e\n\u003c/ul\u003e\nAn accepted frame is directed to the non-oETP RX DMA channel when that channel\nis armed; otherwise it is directed to the CSR AXI4-Stream sink."






class openenoc_endpoint_interface_config_rmem_timeout_cycles_neg_0x21386ee83b5f90a9_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.config.rmem_timeout.cycles[31:0]"
    @property
    def rdl_desc(self) -> str:
        return "Maximum wait for an RMEM response in endpoint clock cycles. Zero disables\nthe timeout and permits an indefinite response wait. Hardware samples this\nvalue when it accepts an RMEM operation; subsequent writes apply to later\noperations. The response timer starts after the complete request frame has\nbeen accepted by the Ethernet-facing transmit stream and runs until the\ncomplete matching response is received and validated through Ethernet TLAST.\nRX backpressure counts toward the timeout; remaining local memory completion\ndoes not. A valid response completing on the expiry edge takes priority,\nincluding a valid ERROR_RSP with its reported cause. Hardware does not\nretry; timeout handling and retry policy belong to software. Multicast\nwrites do not wait for a response and do not use this response timeout.\nAn RMEM read timeout terminates the access with all-ones read data and read\nACK; a write timeout terminates with write ACK. The external-RMEM boundary\nuses no ERR signals. Failures set error and error_code in the associated\npeers.entry[].dma register and may generate a separate RMEM_ERROR IRQ event."






class openenoc_endpoint_interface_config_dma_timeout_cycles_0x1b1c348b779c5fc_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.config.dma_timeout.cycles[31:0]"
    @property
    def rdl_desc(self) -> str:
        return "Maximum wait for a response to one peer DMA fragment, in endpoint clock\ncycles. This value is shared by all peers. Zero disables the timeout and\npermits an indefinite response wait. Hardware samples this value when the\noETP engine accepts the fragment request; later writes apply to later\nfragments. The response timer starts after the complete request frame has\nbeen accepted by the Ethernet-facing transmit stream and runs until the\ncomplete matching response is received and validated through Ethernet TLAST,\nincluding EndOfData where present. RX backpressure counts toward the timeout;\nremaining local memory completion does not. A valid response completing on\nthe expiry edge takes priority, including a valid ERROR_RSP with its reported\ncause. On expiry, hardware\naborts the remaining fragments of that DMA transfer and reports error code\n8 (timeout) in the peer DMA status. Hardware does not retry; software decides\nwhether to start another transfer. This timeout does not apply to multicast\nwrites, non-oETP DMA, or transparent RMEM operations."






class openenoc_endpoint_interface_config_dma_max_fragment_size_bytes_0x56886a0b57a4a4fd_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.config.dma_max_fragment_size.bytes[31:0]"
    @property
    def rdl_desc(self) -> str:
        return "Maximum meaningful memory bytes in one locally initiated DMA fragment,\nexcluding Ethernet/oETP headers, word padding, EndOfData and FCS. The\nhardware rounds the written value down to a multiple of four before\nvalidating it. The effective MFS must be at least four bytes and at most\n4 * floor((MAX_RAW_FRAME_SIZE - 32) / 4). With an 8192-byte frame ceiling,\nthe effective range is 4 through 8160 bytes in steps of four, with reset\nvalue 8160. For example, 31 selects 28, 7 selects 4, and 8161 through 8163\nselect 8160. Hardware snapshots the effective value when it accepts the\nwhole peer DMA transfer; later writes apply only to subsequent transfers.\nThe final fragment uses the exact remaining byte length and may be shorter\nthan four bytes. A written value of 0 through 3, or a rounded value above\nthe synthesized ceiling, rejects a new transfer with local error code 1\nbefore issuing any memory or protocol operation. The CSR retains the\nunrounded written value. This setting does not\nrestrict received peer requests, which use the synthesized fragment\nceiling, and does not affect RMEM, direct CSR streams or non-oETP DMA."






class openenoc_endpoint_interface_axis_if_source_data_tdata_0x17c4542c090ffd0e_cls(FieldReadWrite):
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






class openenoc_endpoint_interface_axis_if_source_control_tvalid_neg_0x267c2272d993b105_cls(FieldReadWrite):
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






class openenoc_endpoint_interface_axis_if_source_control_tlast_neg_0x77cb31118f74f4c3_cls(FieldReadWrite):
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






class openenoc_endpoint_interface_axis_if_source_control_tkeep_0x7eae4751b962a1c_cls(FieldReadWrite):
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






class openenoc_endpoint_interface_axis_if_source_status_tready_0x67560cf213adb45d_cls(FieldReadOnly):
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






class openenoc_endpoint_interface_axis_if_sink_data_tdata_0x2bdcea2731f9535_cls(FieldReadOnly):
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






class openenoc_endpoint_interface_axis_if_sink_control_tready_0x4b7af26499667549_cls(FieldReadWrite):
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






class openenoc_endpoint_interface_axis_if_sink_status_tvalid_neg_0x236d83f545db909d_cls(FieldReadOnly):
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