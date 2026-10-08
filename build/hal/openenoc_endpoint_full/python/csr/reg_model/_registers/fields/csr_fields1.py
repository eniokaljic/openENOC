

"""
Python Wrapper for the csr register model

This code was generated from the PeakRDL-python package version 3.1.2

"""









from ....lib import UDPStruct
from ....lib import FieldReadOnly, FieldWriteOnly, FieldReadWrite, Field


# field definitions


class openenoc_endpoint_interface_axis_if_sink_status_tlast_0x2d9cca5e6baa0192_cls(FieldReadOnly):
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
        return "Indicates the last data word of a frame on the AXI4-Stream\nsink interface."






class openenoc_endpoint_interface_axis_if_sink_status_tkeep_0x62a0176d39c90967_cls(FieldReadOnly):
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
        return "Indicates which byte lanes contain valid data on the AXI4-Stream\nsink interface."






class openenoc_endpoint_interface_non_oetp_dma_tx_buffer_address_base_neg_0x28b01b54d9107f5e_cls(FieldReadWrite):
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






class openenoc_endpoint_interface_non_oetp_dma_tx_frame_length_bytes_0x6f39179e191d9c64_cls(FieldReadWrite):
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
        return "Frame length in bytes. Valid non-zero values shall not exceed\ninfo.max_dma_frame_size_bytes."






class openenoc_endpoint_interface_non_oetp_dma_tx_command_status_request_0x572b2ec04c2729a1_cls(FieldReadWrite):
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
        return "Writing one requests transmission of the configured frame. The field\nremains asserted until the DMA engine accepts the request. Hardware clears\nit upon acceptance; while the channel is busy, a newly asserted request\nremains pending. Software or an RTL controller shall read the completion\nstatus and transferred length of the previous request before asserting this\nfield for the next request."






class openenoc_endpoint_interface_non_oetp_dma_tx_command_status_clear_errors_0x12df5b7087b874bd_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.non_oetp_dma.tx.command_status.clear_errors"
    @property
    def rdl_desc(self) -> str:
        return "Writing one clears this channel\u0027s error flag and error code.\nHardware clears the command after accepting it. The command does not\nabort an active transfer, clear done or transferred length, or complete\nan IRQ claim. A new failure takes precedence over a simultaneous clear.\nStarting or successfully completing a transfer preserves a recorded error."






class openenoc_endpoint_interface_non_oetp_dma_tx_command_status_idle_neg_0x2426ca7af38c78f9_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.non_oetp_dma.tx.command_status.idle"
    @property
    def rdl_desc(self) -> str:
        return "Indicates that the channel has no accepted transfer in progress.\nHardware deasserts this field when a request is accepted and asserts it\nwhen the transfer completes."






class openenoc_endpoint_interface_non_oetp_dma_tx_command_status_done_neg_0x38b21b6e94320d9f_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.non_oetp_dma.tx.command_status.done"
    @property
    def rdl_desc(self) -> str:
        return "Sticky successful-completion flag. Hardware sets this field after the\naccepted transfer completes successfully and clears it when the next request\nis accepted."






class openenoc_endpoint_interface_non_oetp_dma_tx_command_status_error_neg_0x36e24688106f345b_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.non_oetp_dma.tx.command_status.error"
    @property
    def rdl_desc(self) -> str:
        return "Sticky error-completion flag. Hardware sets this field when an\naccepted transfer fails. Only command_status.clear_errors or endpoint\nreset clears it; starting or successfully completing another transfer\npreserves a recorded error."






class openenoc_endpoint_interface_non_oetp_dma_tx_command_status_error_code_0x4154b313bb26714d_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.non_oetp_dma.tx.command_status.error_code[31:28]"
    @property
    def rdl_desc(self) -> str:
        return "Sticky error code for the most recent transmit failure:\u003cul\u003e\n\u003cli\u003e0: No error.\u003c/li\u003e\n\u003cli\u003e1: Invalid DMA configuration or descriptor.\u003c/li\u003e\n\u003cli\u003e2: AXI4-Stream length or TLAST error.\u003c/li\u003e\n\u003cli\u003e3: Frame exceeds the supported size or configured buffer capacity.\u003c/li\u003e\n\u003cli\u003e4: AXI read SLVERR response.\u003c/li\u003e\n\u003cli\u003e5: AXI read DECERR response.\u003c/li\u003e\n\u003cli\u003e6: AXI write SLVERR response.\u003c/li\u003e\n\u003cli\u003e7: AXI write DECERR response.\u003c/li\u003e\n\u003cli\u003e8-15: Reserved.\u003c/li\u003e\n\u003c/ul\u003e\nThese errors describe local non-oETP DMA work. Only\ncommand_status.clear_errors or endpoint reset clears this field.\nA new failure replaces the code and takes precedence over a simultaneous\nclear; successful transfers preserve the previous failure."






class openenoc_endpoint_interface_non_oetp_dma_tx_transferred_length_bytes_0x5c88bb9bca3414c_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.non_oetp_dma.tx.transferred_length.bytes[31:0]"
    @property
    def rdl_desc(self) -> str:
        return "Actual number of bytes transferred. Hardware clears this field when\nthe next request is accepted."






class openenoc_endpoint_interface_non_oetp_dma_rx_buffer_address_base_neg_0x65ddd3cff5827fd1_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.non_oetp_dma.rx.buffer_address.base[31:0]"
    @property
    def rdl_desc(self) -> str:
        return "32-bit byte address of the first byte of the receive buffer."






class openenoc_endpoint_interface_non_oetp_dma_rx_buffer_capacity_bytes_0x45d2dfc0e4c83489_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.non_oetp_dma.rx.buffer_capacity.bytes[31:0]"
    @property
    def rdl_desc(self) -> str:
        return "Receive-buffer capacity in bytes. Valid non-zero values shall not exceed\ninfo.max_dma_frame_size_bytes."






class openenoc_endpoint_interface_non_oetp_dma_rx_command_status_request_0xdfa81fa399196fa_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.non_oetp_dma.rx.command_status.request"
    @property
    def rdl_desc(self) -> str:
        return "Writing one arms reception into the configured buffer. The field remains\nasserted until the DMA engine accepts the request. Hardware clears it upon\nacceptance; while the channel is busy, a newly asserted request remains\npending. Software or an RTL controller shall read the completion status and\nreceived length of the previous request before asserting this field for the\nnext request."






class openenoc_endpoint_interface_non_oetp_dma_rx_command_status_clear_errors_neg_0x1a408665671a1e4d_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.non_oetp_dma.rx.command_status.clear_errors"
    @property
    def rdl_desc(self) -> str:
        return "Writing one clears this channel\u0027s error flag and error code.\nHardware clears the command after accepting it. The command does not\nabort an active or armed receive, clear done or received length, or\ncomplete an IRQ claim. A new failure takes precedence over a simultaneous\nclear. Starting or successfully completing a transfer preserves a\nrecorded error."






class openenoc_endpoint_interface_non_oetp_dma_rx_command_status_idle_neg_0x6da7c7e99a698bf5_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.non_oetp_dma.rx.command_status.idle"
    @property
    def rdl_desc(self) -> str:
        return "Indicates that the channel has no accepted receive request in progress.\nAfter acceptance, the channel may be armed and waiting for an eligible\nnon-oETP frame or may be writing a received frame to memory."






class openenoc_endpoint_interface_non_oetp_dma_rx_command_status_armed_neg_0x5554fe7639dcbb69_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.non_oetp_dma.rx.command_status.armed"
    @property
    def rdl_desc(self) -> str:
        return "Indicates that the accepted receive request is waiting for an eligible\nnon-oETP Ethernet frame. Hardware sets this field when it accepts a request\nand clears it when the first beat of the selected frame is accepted by the\nRX DMA datapath. The frame-routing logic uses this field to select the\nRX DMA path; otherwise an accepted non-oETP frame is directed to the\nCSR AXI4-Stream sink."






class openenoc_endpoint_interface_non_oetp_dma_rx_command_status_done_neg_0x69888afa28051618_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.non_oetp_dma.rx.command_status.done"
    @property
    def rdl_desc(self) -> str:
        return "Sticky successful-completion flag. Hardware sets this field after a\nreceived frame has been written successfully and clears it when the next\nrequest is accepted."






class openenoc_endpoint_interface_non_oetp_dma_rx_command_status_error_neg_0x27834466a0a1154b_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.non_oetp_dma.rx.command_status.error"
    @property
    def rdl_desc(self) -> str:
        return "Sticky error-completion flag. Hardware sets this field when an\naccepted receive fails. Only command_status.clear_errors or endpoint\nreset clears it; starting or successfully completing another receive\npreserves a recorded error."






class openenoc_endpoint_interface_non_oetp_dma_rx_command_status_error_code_0x2f5b737b8463ea9f_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.non_oetp_dma.rx.command_status.error_code[31:28]"
    @property
    def rdl_desc(self) -> str:
        return "Sticky error code for the most recent receive failure:\u003cul\u003e\n\u003cli\u003e0: No error.\u003c/li\u003e\n\u003cli\u003e1: Invalid DMA configuration or descriptor.\u003c/li\u003e\n\u003cli\u003e2: AXI4-Stream length or TLAST error.\u003c/li\u003e\n\u003cli\u003e3: Received frame exceeds the configured buffer capacity.\u003c/li\u003e\n\u003cli\u003e4: AXI read SLVERR response.\u003c/li\u003e\n\u003cli\u003e5: AXI read DECERR response.\u003c/li\u003e\n\u003cli\u003e6: AXI write SLVERR response.\u003c/li\u003e\n\u003cli\u003e7: AXI write DECERR response.\u003c/li\u003e\n\u003cli\u003e8-15: Reserved.\u003c/li\u003e\n\u003c/ul\u003e\nOnly command_status.clear_errors or endpoint reset clears this field.\nA new failure replaces the code and takes precedence over a simultaneous\nclear; successful transfers preserve the previous failure."






class openenoc_endpoint_interface_non_oetp_dma_rx_received_length_bytes_0x62104ffbe60d6f40_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.non_oetp_dma.rx.received_length.bytes[31:0]"
    @property
    def rdl_desc(self) -> str:
        return "Actual number of frame bytes written to the receive buffer. Hardware\nclears this field when the next request is accepted."






class openenoc_endpoint_interface_irq_control_global_enable_neg_0x11fabf129a8cb0ac_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.irq.control.global_enable"
    @property
    def rdl_desc(self) -> str:
        return "Enables the physical endpoint IRQ output. Clearing this field masks the\noutput but does not prevent enabled events from being queued. Event capture is\ncontrolled by irq.event_enable and, for peer DMA, by the selected peer\u0027s\ndma.irq_enable field."






class openenoc_endpoint_interface_irq_control_clear_errors_neg_0x2d370550f19815f7_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.irq.control.clear_errors"
    @property
    def rdl_desc(self) -> str:
        return "Writing one requests clearing of the sticky irq.status.overflow and\nirq.status.invalid_complete flags. The field remains asserted until hardware\naccepts the request and clears it."






class openenoc_endpoint_interface_irq_event_enable_peer_dma_complete_neg_0x4a570f4270edd42b_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.irq.event_enable.peer_dma_complete"
    @property
    def rdl_desc(self) -> str:
        return "Enables PEER_DMA_COMPLETE events. A peer event is queued only when this\nfield and the selected peer\u0027s dma.irq_enable field were both set when the DMA\nrequest was accepted. A failed incoming bulk DMA request also generates this\nevent for the peer resolved from the source MAC. For incoming failures,\nhardware captures the per-peer enable when recording the failure and samples\nthis field at IRQ admission. Successful incoming requests generate no event.\nCSR error recording and the error response do not wait for IRQ FIFO capacity."






class openenoc_endpoint_interface_irq_event_enable_non_oetp_dma_tx_complete_0x486df9956df8d8c8_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.irq.event_enable.non_oetp_dma_tx_complete"
    @property
    def rdl_desc(self) -> str:
        return "Enables NON_OETP_DMA_TX_COMPLETE events. Hardware samples this field when\nit accepts a non-oETP transmit DMA request."





if __name__ == '__main__':
    pass