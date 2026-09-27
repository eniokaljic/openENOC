

"""
Python Wrapper for the csr register model

This code was generated from the PeakRDL-python package version 3.1.2

"""









from ....lib import UDPStruct
from ....lib import FieldReadOnly, FieldWriteOnly, FieldReadWrite, Field


# field definitions
    
    
class openenoc_endpoint_interface_non_oetp_dma_tx_command_status_idle_0x72b4856ac66af50_cls(FieldReadOnly):
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
        return "Indicates that the channel has no accepted transfer in progress. Hardware deasserts this field when a request is accepted and asserts it when the transfer completes."
    
    
    

    
    
class openenoc_endpoint_interface_non_oetp_dma_tx_command_status_done_0x519f56e8a0233ea6_cls(FieldReadOnly):
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
        return "Sticky successful-completion flag. Hardware sets this field after the accepted transfer completes successfully and clears it when the next request is accepted."
    
    
    

    
    
class openenoc_endpoint_interface_non_oetp_dma_tx_command_status_error_0xe63eb479a27f4f6_cls(FieldReadOnly):
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
        return "Sticky error-completion flag. Hardware sets this field when the accepted transfer terminates with an error and clears it when the next request is accepted."
    
    
    

    
    
class openenoc_endpoint_interface_non_oetp_dma_tx_command_status_error_code_neg_0x489d93e4d02761a5_cls(FieldReadOnly):
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
    
    
    

    
    
class openenoc_endpoint_interface_non_oetp_dma_tx_transferred_length_bytes_neg_0x62ee4e3be8653128_cls(FieldReadOnly):
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
        return "Actual number of bytes transferred. Hardware clears this field when the next request is accepted."
    
    
    

    
    
class openenoc_endpoint_interface_non_oetp_dma_rx_buffer_address_base_0x2283e3fb6196a0f8_cls(FieldReadWrite):
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
    
    
    

    
    
class openenoc_endpoint_interface_non_oetp_dma_rx_buffer_capacity_bytes_0x36693b0f4a2d659d_cls(FieldReadWrite):
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
        return "Receive-buffer capacity in bytes. Valid non-zero values shall not exceed info.max_dma_frame_size_bytes."
    
    
    

    
    
class openenoc_endpoint_interface_non_oetp_dma_rx_command_status_request_neg_0x1251ddd46cc1dfc2_cls(FieldReadWrite):
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
    |              |      newly asserted request remains pending.</p>                        |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.non_oetp_dma.rx.command_status.request"
    @property
    def rdl_desc(self) -> str:
        return "Writing one arms reception into the configured buffer. The field remains asserted until the DMA engine accepts the request. Hardware clears it upon acceptance; while the channel is busy, a newly asserted request remains pending."
    
    
    

    
    
class openenoc_endpoint_interface_non_oetp_dma_rx_command_status_idle_0x657ae60eb40c0f1b_cls(FieldReadOnly):
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
        return "Indicates that the channel has no accepted receive request in progress. After acceptance, the channel may be armed and waiting for an eligible non-oETP frame or may be writing a received frame to memory."
    
    
    

    
    
class openenoc_endpoint_interface_non_oetp_dma_rx_command_status_armed_0x7e58c34b2118db23_cls(FieldReadOnly):
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
        return "Indicates that the accepted receive request is waiting for an eligible non-oETP Ethernet frame. Hardware sets this field when it accepts a request and clears it when the first beat of the selected frame is accepted by the RX DMA datapath. The frame-routing logic uses this field to select the RX DMA path; otherwise an accepted non-oETP frame is directed to the CSR AXI4-Stream sink."
    
    
    

    
    
class openenoc_endpoint_interface_non_oetp_dma_rx_command_status_done_neg_0x596c1aea30c2f259_cls(FieldReadOnly):
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
        return "Sticky successful-completion flag. Hardware sets this field after a received frame has been written successfully and clears it when the next request is accepted."
    
    
    

    
    
class openenoc_endpoint_interface_non_oetp_dma_rx_command_status_error_neg_0x2f7a59597cc5abfa_cls(FieldReadOnly):
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
        return "Sticky error-completion flag. Hardware sets this field when the accepted receive request terminates with an error and clears it when the next request is accepted."
    
    
    

    
    
class openenoc_endpoint_interface_non_oetp_dma_rx_command_status_error_code_0x258a5b25a5e6c22f_cls(FieldReadOnly):
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
    
    
    

    
    
class openenoc_endpoint_interface_non_oetp_dma_rx_received_length_bytes_neg_0xe17e8b2164761aa_cls(FieldReadOnly):
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
        return "Actual number of frame bytes written to the receive buffer. Hardware clears this field when the next request is accepted."
    
    
    

    
    
class openenoc_endpoint_interface_peers_entry_mac_address_lo_word_neg_0xbb558e0a6b80bb7_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].mac_address.lo_word[31:0]"
    @property
    def rdl_desc(self) -> str:
        return "Lower 32 bits [31:0] of the 48-bit MAC address."
    
    
    

    
    
class openenoc_endpoint_interface_peers_entry_mac_address_hi_word_neg_0x458571c5dca6dd0d_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].mac_address.hi_word[47:32]"
    @property
    def rdl_desc(self) -> str:
        return "Upper 16 bits [47:32] of the 48-bit MAC address."
    
    
    

    
    
class openenoc_endpoint_interface_peers_entry_rmem_address_offset_neg_0x49d468b3f3666cb2_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].rmem_address.offset[31:0]"
    @property
    def rdl_desc(self) -> str:
        return "32-bit byte offset of the virtual memory region corresponding to the remote peer\u0027s memory. The value shall be aligned to a 32-bit word boundary."
    
    
    

    
    
class openenoc_endpoint_interface_peers_entry_local_address_base_0x5c03c1c6be9def0f_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].local_address.base[31:0]"
    @property
    def rdl_desc(self) -> str:
        return "Word-aligned 32-bit start address of the local memory region for DMA transfers."
    
    
    

    
    
class openenoc_endpoint_interface_peers_entry_remote_address_base_neg_0x5120d823fa2a9f79_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].remote_address.base[31:0]"
    @property
    def rdl_desc(self) -> str:
        return "Word-aligned 32-bit start address of the remote peer\u0027s memory region."
    
    
    

    
    
class openenoc_endpoint_interface_peers_entry_size_bytes_0x4d6cce94763ebe25_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].size.bytes[31:0]"
    @property
    def rdl_desc(self) -> str:
        return "32-bit size of the remote peer\u0027s memory region in bytes."
    
    
    

    
    
class openenoc_endpoint_interface_peers_entry_dma_mode_neg_0x327014553474984e_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.mode[1:0]"
    @property
    def rdl_desc(self) -> str:
        return "DMA mode for transfers to/from the remote peer:\u003cul\u003e\n\u003cli\u003e0: DMA transfers to/from the remote peer are disabled.\u003c/li\u003e\n\u003cli\u003e1: DMA transfers to/from the remote peer are enabled in transparent mode, where accesses to the virtual memory region are directly translated to corresponding accesses to the remote peer\u0027s memory region (transactions are word-by-word, i.e., per virtual memory access).\u003c/li\u003e\n\u003cli\u003e2: DMA transfers to/from the remote peer are enabled in mirror-to-local mode, where the local memory region is used instead of the virtual memory region. The state of the remote peer\u0027s memory region (remote_address, size) is fetched from the remote peer on demand or periodically.\u003c/li\u003e\n\u003cli\u003e3: DMA transfers to/from the remote peer are enabled in mirror-to-remote mode, where the remote memory region is used instead of the virtual memory region. The state of the local peer\u0027s memory region (local_address, size) is sent to the remote peer on demand or periodically.\u003c/li\u003e\n\u003c/ul\u003e"
    
    
    

    
    
class openenoc_endpoint_interface_peers_entry_dma_request_0x66f0e24c90dc1bec_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.request[8:8]"
    @property
    def rdl_desc(self) -> str:
        return "Writing one requests a DMA transfer to or from the remote peer, according to dma.mode. The field remains asserted until the DMA engine accepts and snapshots the request. Hardware clears it upon acceptance; while a transfer for this peer is active, a newly asserted request remains pending. Software or an RTL controller shall keep the peer configuration stable while this field is asserted."
    
    
    

    
    
class openenoc_endpoint_interface_peers_entry_dma_idle_0x5557dc44a5cba24_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.idle[16:16]"
    @property
    def rdl_desc(self) -> str:
        return "Indicates whether this peer has no accepted DMA request in progress. Hardware deasserts this field when a request is accepted and asserts it after all fragments of the requested block have completed."
    
    
    

    
    
class openenoc_endpoint_interface_peers_entry_dma_done_0x62d3d0804e3eb4fa_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.done[24:24]"
    @property
    def rdl_desc(self) -> str:
        return "Sticky successful-completion flag for this peer. Hardware sets this field after all fragments of the accepted block transfer complete successfully and clears it when the next request is accepted."
    
    
    

    
    
class openenoc_endpoint_interface_peers_entry_dma_error_0x600dcca39501014c_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.error[25:25]"
    @property
    def rdl_desc(self) -> str:
        return "Sticky error-completion flag for this peer. Hardware sets this field if the accepted block transfer terminates with an error and clears it when the next request is accepted."
    
    
    


if __name__ == '__main__':
    pass