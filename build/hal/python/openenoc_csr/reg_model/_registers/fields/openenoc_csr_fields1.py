

"""
Python Wrapper for the openenoc_csr register model

This code was generated from the PeakRDL-python package version 3.1.2

"""









from ....lib import UDPStruct
from ....lib import FieldReadOnly, FieldWriteOnly, FieldReadWrite, Field


# field definitions
    
    
class openenoc_endpoint_info_num_of_peers_neg_0x2353d418c67aea7_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint2.info.num_of_peers[31:16]                             |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Number of remote peers supported by this openENOC Endpoint      |
    |              |      Interface instance. This field reflects the NUM_OF_PEERS parameter |
    |              |      value.</p>                                                         |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint2.info.num_of_peers[31:16]"
    @property
    def rdl_desc(self) -> str:
        return "Number of remote peers supported by this openENOC Endpoint Interface instance. This field reflects the NUM_OF_PEERS parameter value."
    
    
    

    
    
class openenoc_endpoint_config_mac_address_lo_word_neg_0x448f4357d313ac89_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint2.config.mac_address.lo_word[31:0]                     |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Lower 32 bits [31:0] of the 48-bit MAC address.</p>             |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint2.config.mac_address.lo_word[31:0]"
    @property
    def rdl_desc(self) -> str:
        return "Lower 32 bits [31:0] of the 48-bit MAC address."
    
    
    

    
    
class openenoc_endpoint_config_mac_address_hi_word_neg_0xb902f37a4d7a9c4_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint2.config.mac_address.hi_word[47:32]                    |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Upper 16 bits [47:32] of the 48-bit MAC address.</p>            |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint2.config.mac_address.hi_word[47:32]"
    @property
    def rdl_desc(self) -> str:
        return "Upper 16 bits [47:32] of the 48-bit MAC address."
    
    
    

    
    
class openenoc_endpoint_axis_if_source_data_tdata_neg_0x18651a6788374af0_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint2.axis_if.source.data.tdata[31:0]                      |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>32-bit data value for the AXI4-Stream source interface.</p>     |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint2.axis_if.source.data.tdata[31:0]"
    @property
    def rdl_desc(self) -> str:
        return "32-bit data value for the AXI4-Stream source interface."
    
    
    

    
    
class openenoc_endpoint_axis_if_source_control_tvalid_neg_0x7693d3714677d2e2_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint2.axis_if.source.control.tvalid                        |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Indicates that the AXI4-Stream source interface has valid data  |
    |              |      to send. This field is a single-pulse register that is             |
    |              |      automatically cleared back to zero after being written.</p>        |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint2.axis_if.source.control.tvalid"
    @property
    def rdl_desc(self) -> str:
        return "Indicates that the AXI4-Stream source interface has valid data to send. This field is a single-pulse register that is automatically cleared back to zero after being written."
    
    
    

    
    
class openenoc_endpoint_axis_if_source_control_tlast_0x6f92ad91f9e86b57_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint2.axis_if.source.control.tlast                         |
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
        return "csr.endpoint2.axis_if.source.control.tlast"
    @property
    def rdl_desc(self) -> str:
        return "Indicates the last data word of a frame on the AXI4-Stream source interface."
    
    
    

    
    
class openenoc_endpoint_axis_if_source_status_tready_neg_0x96c8ac4faeb1efd_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint2.axis_if.source.status.tready                         |
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
        return "csr.endpoint2.axis_if.source.status.tready"
    @property
    def rdl_desc(self) -> str:
        return "Indicates that the destination AXI4-Stream interface is ready to receive data."
    
    
    

    
    
class openenoc_endpoint_axis_if_sink_data_tdata_neg_0x6490c579133ec028_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint2.axis_if.sink.data.tdata[31:0]                        |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>32-bit data value for the AXI4-Stream sink interface.</p>       |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint2.axis_if.sink.data.tdata[31:0]"
    @property
    def rdl_desc(self) -> str:
        return "32-bit data value for the AXI4-Stream sink interface."
    
    
    

    
    
class openenoc_endpoint_axis_if_sink_control_tready_neg_0x42b52af8ff892e38_cls(FieldWriteOnly):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint2.axis_if.sink.control.tready                          |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Indicates that the AXI4-Stream sink interface is ready to       |
    |              |      receive next data transfer.</p>                                    |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint2.axis_if.sink.control.tready"
    @property
    def rdl_desc(self) -> str:
        return "Indicates that the AXI4-Stream sink interface is ready to receive next data transfer."
    
    
    

    
    
class openenoc_endpoint_axis_if_sink_status_tvalid_neg_0x13672d8472c23bf5_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint2.axis_if.sink.status.tvalid                           |
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
        return "csr.endpoint2.axis_if.sink.status.tvalid"
    @property
    def rdl_desc(self) -> str:
        return "Indicates that the AXI4-Stream sink interface has valid data to receive."
    
    
    

    
    
class openenoc_endpoint_axis_if_sink_status_tlast_0x1699db3a89e56b5a_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint2.axis_if.sink.status.tlast                            |
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
        return "csr.endpoint2.axis_if.sink.status.tlast"
    @property
    def rdl_desc(self) -> str:
        return "Indicates the last data word of a frame on the AXI4-Stream sink interface."
    
    
    

    
    
class openenoc_endpoint_peers_entry_mac_address_lo_word_neg_0x2d9dfd1a27a63014_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint2.peers.entry[0..NUM_OF_PEERS-                         |
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
        return "csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].mac_address.lo_word[31:0]"
    @property
    def rdl_desc(self) -> str:
        return "Lower 32 bits [31:0] of the 48-bit MAC address."
    
    
    

    
    
class openenoc_endpoint_peers_entry_mac_address_hi_word_neg_0x567d8034ecf5cbaf_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint2.peers.entry[0..NUM_OF_PEERS-                         |
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
        return "csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].mac_address.hi_word[47:32]"
    @property
    def rdl_desc(self) -> str:
        return "Upper 16 bits [47:32] of the 48-bit MAC address."
    
    
    

    
    
class openenoc_endpoint_peers_entry_rmem_address_offset_0x58961113824d53bc_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint2.peers.entry[0..NUM_OF_PEERS-                         |
    |              |      1].rmem_address.offset[31:0]                                       |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Word-aligned 32-bit address offset of the virtual memory region |
    |              |      corresponding to the remote peer's memory.</p>                     |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].rmem_address.offset[31:0]"
    @property
    def rdl_desc(self) -> str:
        return "Word-aligned 32-bit address offset of the virtual memory region corresponding to the remote peer\u0027s memory."
    
    
    

    
    
class openenoc_endpoint_peers_entry_local_address_base_neg_0x5b7d70f0bbf4dde4_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint2.peers.entry[0..NUM_OF_PEERS-                         |
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
        return "csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].local_address.base[31:0]"
    @property
    def rdl_desc(self) -> str:
        return "Word-aligned 32-bit start address of the local memory region for DMA transfers."
    
    
    

    
    
class openenoc_endpoint_peers_entry_remote_address_base_0x72670eeff0341774_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint2.peers.entry[0..NUM_OF_PEERS-                         |
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
        return "csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].remote_address.base[31:0]"
    @property
    def rdl_desc(self) -> str:
        return "Word-aligned 32-bit start address of the remote peer\u0027s memory region."
    
    
    

    
    
class openenoc_endpoint_peers_entry_size_bytes_0x5d3f71ac3f63a95a_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].size.bytes[31:0]      |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>32-bit size of the remote peer's memory region in bytes.</p>    |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].size.bytes[31:0]"
    @property
    def rdl_desc(self) -> str:
        return "32-bit size of the remote peer\u0027s memory region in bytes."
    
    
    

    
    
class openenoc_endpoint_peers_entry_dma_mode_0x24ac8698fe836ba7_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].dma.mode[1:0]         |
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
        return "csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].dma.mode[1:0]"
    @property
    def rdl_desc(self) -> str:
        return "DMA mode for transfers to/from the remote peer:\u003cul\u003e\n\u003cli\u003e0: DMA transfers to/from the remote peer are disabled.\u003c/li\u003e\n\u003cli\u003e1: DMA transfers to/from the remote peer are enabled in transparent mode, where accesses to the virtual memory region are directly translated to corresponding accesses to the remote peer\u0027s memory region (transactions are word-by-word, i.e., per virtual memory access).\u003c/li\u003e\n\u003cli\u003e2: DMA transfers to/from the remote peer are enabled in mirror-to-local mode, where the local memory region is used instead of the virtual memory region. The state of the remote peer\u0027s memory region (remote_address, size) is fetched from the remote peer on demand or periodically.\u003c/li\u003e\n\u003cli\u003e3: DMA transfers to/from the remote peer are enabled in mirror-to-remote mode, where the remote memory region is used instead of the virtual memory region. The state of the local peer\u0027s memory region (local_address, size) is sent to the remote peer on demand or periodically.\u003c/li\u003e\n\u003c/ul\u003e"
    
    
    

    
    
class openenoc_endpoint_peers_entry_dma_request_0x668604d38e9d8a32_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].dma.request[8:8]      |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Writing a 1 to this field initiates a DMA transfer to/from the  |
    |              |      remote peer. This field is a single-pulse register that is         |
    |              |      automatically cleared back to zero after being written.</p>        |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].dma.request[8:8]"
    @property
    def rdl_desc(self) -> str:
        return "Writing a 1 to this field initiates a DMA transfer to/from the remote peer. This field is a single-pulse register that is automatically cleared back to zero after being written."
    
    
    

    
    
class openenoc_endpoint_peers_entry_dma_idle_neg_0x6f4dfc3dec01ccac_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].dma.idle[16:16]       |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Indicates whether the DMA transfer to/from the remote peer is   |
    |              |      idle. A value of 1 indicates that the DMA transfer is idle, while  |
    |              |      a value of 0 indicates that the DMA transfer is in progress.</p>   |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].dma.idle[16:16]"
    @property
    def rdl_desc(self) -> str:
        return "Indicates whether the DMA transfer to/from the remote peer is idle. A value of 1 indicates that the DMA transfer is idle, while a value of 0 indicates that the DMA transfer is in progress."
    
    
    

    
    
class openenoc_endpoint_peers_entry_dma_done_0x4426ece43561514a_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].dma.done[24:24]       |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Indicates whether the DMA transfer to/from the remote peer has  |
    |              |      been successful. A value of 1 indicates that the DMA transfer has  |
    |              |      completed successfully, while a value of 0 indicates that the DMA  |
    |              |      transfer is still in progress or has encountered an error.</p>     |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].dma.done[24:24]"
    @property
    def rdl_desc(self) -> str:
        return "Indicates whether the DMA transfer to/from the remote peer has been successful. A value of 1 indicates that the DMA transfer has completed successfully, while a value of 0 indicates that the DMA transfer is still in progress or has encountered an error."
    
    
    

    
    
class openenoc_endpoint_peers_entry_dma_error_neg_0x6379ca8afedb0d51_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].dma.error[25:25]      |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Indicates whether the DMA transfer to/from the remote peer has  |
    |              |      encountered an error. A value of 1 indicates an error, while a     |
    |              |      value of 0 indicates no error.</p>                                 |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].dma.error[25:25]"
    @property
    def rdl_desc(self) -> str:
        return "Indicates whether the DMA transfer to/from the remote peer has encountered an error. A value of 1 indicates an error, while a value of 0 indicates no error."
    
    
    

    
    
class openenoc_switch_info_table_depth_0x1bf7cb8e0630e090_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.switch1.info.table_depth[15:0]                                 |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Depth of the forwarding table in this openENOC Switch instance. |
    |              |      This field reflects the TABLE_DEPTH parameter value.</p>           |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.switch1.info.table_depth[15:0]"
    @property
    def rdl_desc(self) -> str:
        return "Depth of the forwarding table in this openENOC Switch instance. This field reflects the TABLE_DEPTH parameter value."
    
    
    

    
    
class openenoc_switch_info_num_of_interfaces_0x589388453a8ea724_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.switch1.info.num_of_interfaces[21:16]                          |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Number of interfaces in this openENOC Switch instance. This     |
    |              |      field reflects the NUM_OF_INTERFACES parameter value.</p>          |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.switch1.info.num_of_interfaces[21:16]"
    @property
    def rdl_desc(self) -> str:
        return "Number of interfaces in this openENOC Switch instance. This field reflects the NUM_OF_INTERFACES parameter value."
    
    
    

    
    
class openenoc_switch_forwarding_control_operation_mode_neg_0x2a91c036544c803f_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.switch1.forwarding_control.operation_mode[0:0]                 |
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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.switch1.forwarding_control.operation_mode[0:0]"
    @property
    def rdl_desc(self) -> str:
        return "Mode of operation for the openENOC Switch instance. When set to 1, the switch operates in managed mode, allowing software to configure the forwarding table and control forwarding operations. When set to 0, the switch operates in unmanaged mode, where forwarding state is maintained autonomously by internal hardware logic without software intervention."
    
    
    


if __name__ == '__main__':
    pass