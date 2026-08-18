

"""
Python Wrapper for the csr register model

This code was generated from the PeakRDL-python package version 3.1.2

"""









from ....lib import UDPStruct
from ....lib import FieldReadOnly, FieldWriteOnly, FieldReadWrite, Field


# field definitions
    
    
class csr_test_reg_test_field_0x3f45d68e065b8689_cls(FieldReadWrite):
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
    
    
    

    
    
class openenoc_endpoint_interface_info_rmem_total_depth_0x6b3fda525bba572f_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.info.rmem_total_depth[15:0]                 |
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
        return "csr.endpoint_interface.info.rmem_total_depth[15:0]"
    @property
    def rdl_desc(self) -> str:
        return "Total depth of the shared memory region for all remote peers. This field reflects the RMEM_TOTAL_DEPTH parameter value."
    
    
    

    
    
class openenoc_endpoint_interface_info_num_of_peers_0x2d935eb900ee3669_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.info.num_of_peers[31:16]                    |
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
        return "csr.endpoint_interface.info.num_of_peers[31:16]"
    @property
    def rdl_desc(self) -> str:
        return "Number of remote peers supported by this openENOC Endpoint Interface instance. This field reflects the NUM_OF_PEERS parameter value."
    
    
    

    
    
class openenoc_endpoint_interface_config_mac_address_lo_word_neg_0x18b0f47ad17b0ee9_cls(FieldReadWrite):
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
    
    
    

    
    
class openenoc_endpoint_interface_config_mac_address_hi_word_neg_0x14d8bc57a2290a2d_cls(FieldReadWrite):
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
    
    
    

    
    
class openenoc_endpoint_interface_axis_if_source_data_tdata_0x6a48e8c1f2a53b09_cls(FieldReadWrite):
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
    
    
    

    
    
class openenoc_endpoint_interface_axis_if_source_control_tvalid_0x19bc7bfcb2094e64_cls(FieldReadWrite):
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
    |              |      to send. This field is a single-pulse register that is             |
    |              |      automatically cleared back to zero after being written.</p>        |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.axis_if.source.control.tvalid"
    @property
    def rdl_desc(self) -> str:
        return "Indicates that the AXI4-Stream source interface has valid data to send. This field is a single-pulse register that is automatically cleared back to zero after being written."
    
    
    

    
    
class openenoc_endpoint_interface_axis_if_source_control_tlast_neg_0x6c3103f20ef2e5a2_cls(FieldReadWrite):
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
    
    
    

    
    
class openenoc_endpoint_interface_axis_if_source_status_tready_0x2c6d57d247eff0fe_cls(FieldReadOnly):
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
    
    
    

    
    
class openenoc_endpoint_interface_axis_if_sink_data_tdata_neg_0x7674ed91576dd1f3_cls(FieldReadOnly):
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
    
    
    

    
    
class openenoc_endpoint_interface_axis_if_sink_control_tready_0x721f23dcf90d2889_cls(FieldWriteOnly):
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
    |              |      receive next data transfer.</p>                                    |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.axis_if.sink.control.tready"
    @property
    def rdl_desc(self) -> str:
        return "Indicates that the AXI4-Stream sink interface is ready to receive next data transfer."
    
    
    

    
    
class openenoc_endpoint_interface_axis_if_sink_status_tvalid_neg_0x67bea87ef0333bba_cls(FieldReadOnly):
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
    
    
    

    
    
class openenoc_endpoint_interface_axis_if_sink_status_tlast_0x7886fced4a0c15f6_cls(FieldReadOnly):
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
    
    
    

    
    
class openenoc_endpoint_interface_peers_entry_mac_address_lo_word_0x62cb9bd007d8c4f8_cls(FieldReadWrite):
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
    
    
    

    
    
class openenoc_endpoint_interface_peers_entry_mac_address_hi_word_neg_0x68509bf0aa6b40be_cls(FieldReadWrite):
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
    
    
    

    
    
class openenoc_endpoint_interface_peers_entry_rmem_address_offset_0x58f2abf17da3316d_cls(FieldReadWrite):
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
    |              |      <p>Word-aligned 32-bit address offset of the virtual memory region |
    |              |      corresponding to the remote peer's memory.</p>                     |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].rmem_address.offset[31:0]"
    @property
    def rdl_desc(self) -> str:
        return "Word-aligned 32-bit address offset of the virtual memory region corresponding to the remote peer\u0027s memory."
    
    
    

    
    
class openenoc_endpoint_interface_peers_entry_local_address_base_neg_0x3d16471265716c7f_cls(FieldReadWrite):
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
    
    
    

    
    
class openenoc_endpoint_interface_peers_entry_remote_address_base_neg_0x6303ce9f936a1ee7_cls(FieldReadWrite):
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
    
    
    

    
    
class openenoc_endpoint_interface_peers_entry_size_bytes_neg_0x3c897074d335a951_cls(FieldReadWrite):
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
    
    
    

    
    
class openenoc_endpoint_interface_peers_entry_dma_mode_0x70a7cff283ea55dc_cls(FieldReadWrite):
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
    
    
    

    
    
class openenoc_endpoint_interface_peers_entry_dma_request_neg_0x64ab09a994890e0_cls(FieldReadWrite):
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
    |              |      <p>Writing a 1 to this field initiates a DMA transfer to/from the  |
    |              |      remote peer. This field is a single-pulse register that is         |
    |              |      automatically cleared back to zero after being written.</p>        |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.request[8:8]"
    @property
    def rdl_desc(self) -> str:
        return "Writing a 1 to this field initiates a DMA transfer to/from the remote peer. This field is a single-pulse register that is automatically cleared back to zero after being written."
    
    
    

    
    
class openenoc_endpoint_interface_peers_entry_dma_idle_0x49dd266b30acfbd_cls(FieldReadOnly):
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
    |              |      <p>Indicates whether the DMA transfer to/from the remote peer is   |
    |              |      idle. A value of 1 indicates that the DMA transfer is idle, while  |
    |              |      a value of 0 indicates that the DMA transfer is in progress.</p>   |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.idle[16:16]"
    @property
    def rdl_desc(self) -> str:
        return "Indicates whether the DMA transfer to/from the remote peer is idle. A value of 1 indicates that the DMA transfer is idle, while a value of 0 indicates that the DMA transfer is in progress."
    
    
    

    
    
class openenoc_endpoint_interface_peers_entry_dma_done_neg_0x3dd243800525799f_cls(FieldReadOnly):
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
    |              |      <p>Indicates whether the DMA transfer to/from the remote peer has  |
    |              |      been successful. A value of 1 indicates that the DMA transfer has  |
    |              |      completed successfully, while a value of 0 indicates that the DMA  |
    |              |      transfer is still in progress or has encountered an error.</p>     |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.done[24:24]"
    @property
    def rdl_desc(self) -> str:
        return "Indicates whether the DMA transfer to/from the remote peer has been successful. A value of 1 indicates that the DMA transfer has completed successfully, while a value of 0 indicates that the DMA transfer is still in progress or has encountered an error."
    
    
    

    
    
class openenoc_endpoint_interface_peers_entry_dma_error_0x3687e3fb91b0a6d6_cls(FieldReadOnly):
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
    |              |      <p>Indicates whether the DMA transfer to/from the remote peer has  |
    |              |      encountered an error. A value of 1 indicates an error, while a     |
    |              |      value of 0 indicates no error.</p>                                 |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.error[25:25]"
    @property
    def rdl_desc(self) -> str:
        return "Indicates whether the DMA transfer to/from the remote peer has encountered an error. A value of 1 indicates an error, while a value of 0 indicates no error."
    
    
    

    
    
class openenoc_endpoint_interface_rmem_word_data_neg_0x4e28bf16cde65f0f_cls(FieldReadWrite):
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