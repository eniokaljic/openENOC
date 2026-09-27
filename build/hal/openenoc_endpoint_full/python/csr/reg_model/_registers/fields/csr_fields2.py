

"""
Python Wrapper for the csr register model

This code was generated from the PeakRDL-python package version 3.1.2

"""









from ....lib import UDPStruct
from ....lib import FieldReadOnly, FieldWriteOnly, FieldReadWrite, Field


# field definitions
    
    
class openenoc_endpoint_interface_irq_status_irq_asserted_0x70d97b6b9f860681_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.irq.status.irq_asserted"
    @property
    def rdl_desc(self) -> str:
        return "Reflects the current value of the physical endpoint IRQ output after application of irq.control.global_enable."
    
    
    

    
    
class openenoc_endpoint_interface_irq_status_fifo_level_neg_0x1de09d7e3b7d23dd_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.irq.status.fifo_level[7:0]"
    @property
    def rdl_desc(self) -> str:
        return "Number of valid claims currently queued in the IRQ event FIFO. Values greater than 255 are reported as 255."
    
    
    

    
    
class openenoc_endpoint_interface_irq_status_reserved_count_0x43bf046f0b14056b_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.irq.status.reserved_count[7:0]"
    @property
    def rdl_desc(self) -> str:
        return "Number of event FIFO credits reserved for admitted DMA operations or direct transmit frames whose events have not yet been queued. Values greater than 255 are reported as 255."
    
    
    

    
    
class openenoc_endpoint_interface_irq_claim_peer_idx_0xada149624bb2795_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.irq.claim.peer_idx[10:0]"
    @property
    def rdl_desc(self) -> str:
        return "Zero-based peer index for a PEER_DMA_COMPLETE event, in the range 0 through NUM_OF_PEERS-1. The field is not applicable to other event sources and is driven to zero for deterministic readback."
    
    
    

    
    
class openenoc_endpoint_interface_irq_claim_source_0x50c612c89deecd3c_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.irq.claim.source[3:0]"
    @property
    def rdl_desc(self) -> str:
        return "IRQ event source:\u003cul\u003e\n\u003cli\u003e0: PEER_DMA_COMPLETE. A peer DMA request completed with either success or error; peer_idx identifies the peer.\u003c/li\u003e\n\u003cli\u003e1: NON_OETP_DMA_TX_COMPLETE. A non-oETP transmit DMA request completed with either success or error.\u003c/li\u003e\n\u003cli\u003e2: NON_OETP_DMA_RX_COMPLETE. A non-oETP receive DMA request completed with either success or error.\u003c/li\u003e\n\u003cli\u003e3: NON_OETP_DIRECT_TX_COMPLETE. The final beat of a direct non-oETP transmit frame was accepted by the oETP engine.\u003c/li\u003e\n\u003cli\u003e4: NON_OETP_DIRECT_RX_AVAILABLE. The first beat of a new direct non-oETP receive frame is available on the CSR-facing AXI4-Stream interface.\u003c/li\u003e\n\u003cli\u003e5-15: Reserved.\u003c/li\u003e\n\u003c/ul\u003e\nThis field is meaningful only when valid is set."
    
    
    

    
    
class openenoc_endpoint_interface_irq_claim_sequence_neg_0x616b6149b87d6f38_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.irq.claim.sequence[15:0]"
    @property
    def rdl_desc(self) -> str:
        return "Monotonically increasing event sequence number, modulo 65536. The sequence number distinguishes otherwise identical claims and protects against stale or repeated completion requests."
    
    
    

    
    
class openenoc_endpoint_interface_irq_claim_valid_neg_0x651b8b8dba4d4a36_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.irq.claim.valid"
    @property
    def rdl_desc(self) -> str:
        return "Indicates that this register contains the valid event at the head of the IRQ event FIFO. When clear, all other claim fields shall be ignored."
    
    
    

    
    
class openenoc_endpoint_interface_irq_complete_peer_idx_0x3fcf95c696c8398c_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.irq.complete.peer_idx[10:0]"
    @property
    def rdl_desc(self) -> str:
        return "Peer-index portion of the claim token."
    
    
    

    
    
class openenoc_endpoint_interface_irq_complete_source_0x4fe551be6ddcd0cf_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.irq.complete.source[3:0]"
    @property
    def rdl_desc(self) -> str:
        return "Event-source portion of the claim token."
    
    
    

    
    
class openenoc_endpoint_interface_irq_complete_sequence_0x26e502db6753c464_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.irq.complete.sequence[15:0]"
    @property
    def rdl_desc(self) -> str:
        return "Sequence-number portion of the claim token."
    
    
    

    
    
class openenoc_endpoint_interface_irq_complete_valid_neg_0x77fa9e38dac9efdf_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.irq.complete.valid"
    @property
    def rdl_desc(self) -> str:
        return "Writing one submits the completion token. The field remains asserted until hardware validates the token and clears it. A matching token removes the current claim and releases its FIFO credit; an invalid token leaves the claim unchanged and sets irq.status.invalid_complete."
    
    
    

    
    
class openenoc_endpoint_interface_peers_entry_mac_address_lo_word_neg_0x6db9cd538a4a034a_cls(FieldReadWrite):
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
    
    
    

    
    
class openenoc_endpoint_interface_peers_entry_mac_address_hi_word_0x4e686b8fad09db0e_cls(FieldReadWrite):
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
    
    
    

    
    
class openenoc_endpoint_interface_peers_entry_rmem_address_offset_0x391ef370f903e756_cls(FieldReadWrite):
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
    
    
    

    
    
class openenoc_endpoint_interface_peers_entry_local_address_base_neg_0x24789a98c038dc42_cls(FieldReadWrite):
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
    
    
    

    
    
class openenoc_endpoint_interface_peers_entry_remote_address_base_neg_0x7c3facba199346c8_cls(FieldReadWrite):
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
    
    
    

    
    
class openenoc_endpoint_interface_peers_entry_size_bytes_0x73ce236a1641d389_cls(FieldReadWrite):
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
    
    
    

    
    
class openenoc_endpoint_interface_peers_entry_dma_mode_neg_0x6ed9366baf8aa643_cls(FieldReadWrite):
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
    |              |      remote peer on demand.</li> <li>3: DMA transfers to/from the       |
    |              |      remote peer are enabled in mirror-to-remote mode, where the remote |
    |              |      memory region is used instead of the virtual memory region. The    |
    |              |      state of the local peer's memory region (local_address, size) is   |
    |              |      sent to the remote peer on demand.</li> </ul>                      |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.mode[1:0]"
    @property
    def rdl_desc(self) -> str:
        return "DMA mode for transfers to/from the remote peer:\u003cul\u003e\n\u003cli\u003e0: DMA transfers to/from the remote peer are disabled.\u003c/li\u003e\n\u003cli\u003e1: DMA transfers to/from the remote peer are enabled in transparent mode, where accesses to the virtual memory region are directly translated to corresponding accesses to the remote peer\u0027s memory region (transactions are word-by-word, i.e., per virtual memory access).\u003c/li\u003e\n\u003cli\u003e2: DMA transfers to/from the remote peer are enabled in mirror-to-local mode, where the local memory region is used instead of the virtual memory region. The state of the remote peer\u0027s memory region (remote_address, size) is fetched from the remote peer on demand.\u003c/li\u003e\n\u003cli\u003e3: DMA transfers to/from the remote peer are enabled in mirror-to-remote mode, where the remote memory region is used instead of the virtual memory region. The state of the local peer\u0027s memory region (local_address, size) is sent to the remote peer on demand.\u003c/li\u003e\n\u003c/ul\u003e"
    
    
    

    
    
class openenoc_endpoint_interface_peers_entry_dma_irq_enable_neg_0x2d8b23a6503e3fc1_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

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
    |              |      execution or the done, error, and error_code status fields.</p>    |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.irq_enable"
    @property
    def rdl_desc(self) -> str:
        return "Enables generation of a PEER_DMA_COMPLETE IRQ event for this peer. Hardware samples this field together with irq.event_enable.peer_dma_complete when it accepts the peer DMA request. Changing the field while a transfer is active does not affect that transfer. Disabling the field does not affect DMA execution or the done, error, and error_code status fields."
    
    
    

    
    
class openenoc_endpoint_interface_peers_entry_dma_request_neg_0x7ed73ca7bafbf5e8_cls(FieldReadWrite):
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
    |              |      shall read the completion status of the previous request before    |
    |              |      asserting this field for the next request and shall keep the peer  |
    |              |      configuration stable while this field is asserted.</p>             |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.request[8:8]"
    @property
    def rdl_desc(self) -> str:
        return "Writing one requests a DMA transfer to or from the remote peer, according to dma.mode. The field remains asserted until the DMA engine accepts and snapshots the request. Hardware clears it upon acceptance; while a transfer for this peer is active, a newly asserted request remains pending. Software or an RTL controller shall read the completion status of the previous request before asserting this field for the next request and shall keep the peer configuration stable while this field is asserted."
    
    
    

    
    
class openenoc_endpoint_interface_peers_entry_dma_idle_0x714258df5d01e5ce_cls(FieldReadOnly):
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
    
    
    

    
    
class openenoc_endpoint_interface_peers_entry_dma_done_neg_0x53ea86779c6e3125_cls(FieldReadOnly):
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
    
    
    

    
    
class openenoc_endpoint_interface_peers_entry_dma_error_neg_0x646fd28d72afcb7c_cls(FieldReadOnly):
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
    
    
    

    
    
class openenoc_endpoint_interface_peers_entry_dma_error_code_0x56a72b174fd951ea_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.error_code[31:28]"
    @property
    def rdl_desc(self) -> str:
        return "Sticky error code for the most recently completed peer DMA transfer:\u003cul\u003e\n\u003cli\u003e0: No error.\u003c/li\u003e\n\u003cli\u003e1: Invalid DMA configuration or descriptor.\u003c/li\u003e\n\u003cli\u003e2: AXI4-Stream length or TLAST error.\u003c/li\u003e\n\u003cli\u003e3: Frame exceeds the supported size or configured buffer capacity.\u003c/li\u003e\n\u003cli\u003e4: AXI read SLVERR response.\u003c/li\u003e\n\u003cli\u003e5: AXI read DECERR response.\u003c/li\u003e\n\u003cli\u003e6: AXI write SLVERR response.\u003c/li\u003e\n\u003cli\u003e7: AXI write DECERR response.\u003c/li\u003e\n\u003cli\u003e8-15: Reserved.\u003c/li\u003e\n\u003c/ul\u003e\nHardware clears this field when the next request is accepted."
    
    
    

    
    
class openenoc_endpoint_interface_rmem_word_data_neg_0x5a7d9bc5ec0ccfb0_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]"
    @property
    def rdl_desc(self) -> str:
        return "Data stored in this virtual memory word."
    
    
    


if __name__ == '__main__':
    pass