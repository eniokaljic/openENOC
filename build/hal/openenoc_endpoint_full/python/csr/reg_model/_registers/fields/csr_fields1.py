

"""
Python Wrapper for the csr register model

This code was generated from the PeakRDL-python package version 3.1.2

"""









from ....lib import UDPStruct
from ....lib import FieldReadOnly, FieldWriteOnly, FieldReadWrite, Field


# field definitions
    
    
class openenoc_endpoint_interface_non_oetp_dma_tx_command_status_idle_neg_0x13f5af5d0f01d1cb_cls(FieldReadOnly):
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
    
    
    

    
    
class openenoc_endpoint_interface_non_oetp_dma_tx_command_status_done_neg_0x3c04d9763163f90a_cls(FieldReadOnly):
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
    
    
    

    
    
class openenoc_endpoint_interface_non_oetp_dma_tx_command_status_error_neg_0x1c68e179e7cfe7fc_cls(FieldReadOnly):
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
    |              |      <p>Sticky error-completion flag. Hardware sets this field when the |
    |              |      accepted transfer terminates with an error and clears it when the  |
    |              |      next request is accepted.</p>                                      |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.non_oetp_dma.tx.command_status.error"
    @property
    def rdl_desc(self) -> str:
        return "Sticky error-completion flag. Hardware sets this field when the accepted\ntransfer terminates with an error and clears it when the next request\nis accepted."
    
    
    

    
    
class openenoc_endpoint_interface_non_oetp_dma_tx_command_status_error_code_neg_0x11295cf65b0b73f4_cls(FieldReadOnly):
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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.non_oetp_dma.tx.command_status.error_code[31:28]"
    @property
    def rdl_desc(self) -> str:
        return "Sticky error code for the most recently completed transfer:\u003cul\u003e\n\u003cli\u003e0: No error.\u003c/li\u003e\n\u003cli\u003e1: Invalid DMA configuration or descriptor.\u003c/li\u003e\n\u003cli\u003e2: AXI4-Stream length or TLAST error.\u003c/li\u003e\n\u003cli\u003e3: Frame exceeds the supported size or configured buffer capacity.\u003c/li\u003e\n\u003cli\u003e4: AXI read SLVERR response.\u003c/li\u003e\n\u003cli\u003e5: AXI read DECERR response.\u003c/li\u003e\n\u003cli\u003e6: AXI write SLVERR response.\u003c/li\u003e\n\u003cli\u003e7: AXI write DECERR response.\u003c/li\u003e\n\u003cli\u003e8-15: Reserved.\u003c/li\u003e\n\u003c/ul\u003e\nHardware clears this field when the next request is accepted."
    
    
    

    
    
class openenoc_endpoint_interface_non_oetp_dma_tx_transferred_length_bytes_neg_0xedbd1ffe5b40115_cls(FieldReadOnly):
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
    
    
    

    
    
class openenoc_endpoint_interface_non_oetp_dma_rx_buffer_address_base_0x5617bcc430358419_cls(FieldReadWrite):
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
    
    
    

    
    
class openenoc_endpoint_interface_non_oetp_dma_rx_buffer_capacity_bytes_neg_0x19384302be2619c8_cls(FieldReadWrite):
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
    
    
    

    
    
class openenoc_endpoint_interface_non_oetp_dma_rx_command_status_request_0x4522a7768784001d_cls(FieldReadWrite):
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
    
    
    

    
    
class openenoc_endpoint_interface_non_oetp_dma_rx_command_status_idle_0x57f04f8de916bf6f_cls(FieldReadOnly):
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
    
    
    

    
    
class openenoc_endpoint_interface_non_oetp_dma_rx_command_status_armed_neg_0x37392bf001485b11_cls(FieldReadOnly):
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
    
    
    

    
    
class openenoc_endpoint_interface_non_oetp_dma_rx_command_status_done_neg_0x507440407a7becfd_cls(FieldReadOnly):
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
    
    
    

    
    
class openenoc_endpoint_interface_non_oetp_dma_rx_command_status_error_0x5312aceed2c583a3_cls(FieldReadOnly):
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
    |              |      <p>Sticky error-completion flag. Hardware sets this field when the |
    |              |      accepted receive request terminates with an error and clears it    |
    |              |      when the next request is accepted.</p>                             |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.non_oetp_dma.rx.command_status.error"
    @property
    def rdl_desc(self) -> str:
        return "Sticky error-completion flag. Hardware sets this field when the accepted\nreceive request terminates with an error and clears it when the next request\nis accepted."
    
    
    

    
    
class openenoc_endpoint_interface_non_oetp_dma_rx_command_status_error_code_neg_0x4b67038b6a593b5e_cls(FieldReadOnly):
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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.non_oetp_dma.rx.command_status.error_code[31:28]"
    @property
    def rdl_desc(self) -> str:
        return "Sticky error code for the most recently completed receive transfer:\u003cul\u003e\n\u003cli\u003e0: No error.\u003c/li\u003e\n\u003cli\u003e1: Invalid DMA configuration or descriptor.\u003c/li\u003e\n\u003cli\u003e2: AXI4-Stream length or TLAST error.\u003c/li\u003e\n\u003cli\u003e3: Received frame exceeds the configured buffer capacity.\u003c/li\u003e\n\u003cli\u003e4: AXI read SLVERR response.\u003c/li\u003e\n\u003cli\u003e5: AXI read DECERR response.\u003c/li\u003e\n\u003cli\u003e6: AXI write SLVERR response.\u003c/li\u003e\n\u003cli\u003e7: AXI write DECERR response.\u003c/li\u003e\n\u003cli\u003e8-15: Reserved.\u003c/li\u003e\n\u003c/ul\u003e\nHardware clears this field when the next request is accepted."
    
    
    

    
    
class openenoc_endpoint_interface_non_oetp_dma_rx_received_length_bytes_0x51914132c8df5df1_cls(FieldReadOnly):
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
    
    
    

    
    
class openenoc_endpoint_interface_irq_control_global_enable_0x78468b6d77f5b0d6_cls(FieldReadWrite):
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
    
    
    

    
    
class openenoc_endpoint_interface_irq_control_clear_errors_0x34341631a90c3ac6_cls(FieldReadWrite):
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
    
    
    

    
    
class openenoc_endpoint_interface_irq_event_enable_peer_dma_complete_0x253a31e3e5f7cd5f_cls(FieldReadWrite):
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
    |              |      both set when the DMA request was accepted.</p>                    |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.irq.event_enable.peer_dma_complete"
    @property
    def rdl_desc(self) -> str:
        return "Enables PEER_DMA_COMPLETE events. A peer event is queued only when this\nfield and the selected peer\u0027s dma.irq_enable field were both set when the DMA\nrequest was accepted."
    
    
    

    
    
class openenoc_endpoint_interface_irq_event_enable_non_oetp_dma_tx_complete_0xbfd03725ebc2482_cls(FieldReadWrite):
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
    
    
    

    
    
class openenoc_endpoint_interface_irq_event_enable_non_oetp_dma_rx_complete_0x3629e67722bfd09a_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.irq.event_enable.non_oetp_dma_rx_complete"
    @property
    def rdl_desc(self) -> str:
        return "Enables NON_OETP_DMA_RX_COMPLETE events. Hardware samples this field when\nit accepts a non-oETP receive DMA request."
    
    
    

    
    
class openenoc_endpoint_interface_irq_event_enable_non_oetp_direct_tx_complete_0xaae4fb94b3cca8d_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.irq.event_enable.non_oetp_direct_tx_complete"
    @property
    def rdl_desc(self) -> str:
        return "Enables NON_OETP_DIRECT_TX_COMPLETE events. Hardware samples this field when\nthe first beat of a direct transmit frame is accepted from the CSR-facing\nAXI4-Stream interface. When enabled, the frame start is accepted only after an\nIRQ FIFO credit has been reserved. The event is generated when the final beat\nis accepted by the oETP engine."
    
    
    

    
    
class openenoc_endpoint_interface_irq_event_enable_non_oetp_direct_rx_available_0x30d4ea837eee6b0e_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.irq.event_enable.non_oetp_direct_rx_available"
    @property
    def rdl_desc(self) -> str:
        return "Enables NON_OETP_DIRECT_RX_AVAILABLE events. One event is generated when\nthe first beat of a new direct receive frame becomes valid on the CSR-facing\nAXI4-Stream interface. When enabled, routing logic does not expose that first\nTVALID until an IRQ FIFO credit is available, so the event cannot be lost.\nThe event does not depend on TLAST and therefore supports both cut-through and\nframe-FIFO operation."
    
    
    

    
    
class openenoc_endpoint_interface_irq_status_claim_pending_neg_0x2a11b2b60d7ef56_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.irq.status.claim_pending"
    @property
    def rdl_desc(self) -> str:
        return "Indicates that at least one valid event is available in irq.claim."
    
    
    

    
    
class openenoc_endpoint_interface_irq_status_credit_full_0x6cb990f26b9bde51_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.irq.status.credit_full"
    @property
    def rdl_desc(self) -> str:
        return "Indicates that all event FIFO credits are occupied by queued claims or\nreserved for admitted operations. While no credit is available, new\ninterrupt-enabled DMA requests are not accepted and the start of an\ninterrupt-enabled direct AXI4-Stream frame is backpressured."
    
    
    

    
    
class openenoc_endpoint_interface_irq_status_overflow_0x41b63e9cb4b127f_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.irq.status.overflow"
    @property
    def rdl_desc(self) -> str:
        return "Sticky internal-error flag indicating that an enabled event could not be\nretained. Correct credit reservation, admission control, and AXI4-Stream\nbackpressure make this condition unreachable during normal operation. Clear with\nirq.control.clear_errors."
    
    
    

    
    
class openenoc_endpoint_interface_irq_status_invalid_complete_0x8b83b4b300b8120_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.irq.status.invalid_complete"
    @property
    def rdl_desc(self) -> str:
        return "Sticky protocol-error flag indicating that irq.complete.valid was accepted\nwhile no claim was pending or that the completion token did not match the\ncurrent claim. No claim is removed on a mismatch. Clear with\nirq.control.clear_errors."
    
    
    


if __name__ == '__main__':
    pass