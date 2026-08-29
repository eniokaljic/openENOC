

"""
Python Wrapper for the csr register model

This code was generated from the PeakRDL-python package version 3.1.2

"""









from ....lib import UDPStruct
from ....lib import FieldReadOnly, FieldWriteOnly, FieldReadWrite, Field


# field definitions
    
    
class openenoc_endpoint_interface_peers_entry_dma_error_neg_0x3bc21446ddde2a6c_cls(FieldReadOnly):
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






class openenoc_endpoint_interface_rmem_word_data_0x5406d30947de088f_cls(FieldReadWrite):
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






class openenoc_switch_interface_info_table_depth_0x6ac92ba3afd39d3f_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.switch_interface.info.table_depth[15:0]"
    @property
    def rdl_desc(self) -> str:
        return "Depth of the forwarding table in this openENOC Switch instance. This field reflects the TABLE_DEPTH parameter value."
    
    
    

    
    
class openenoc_switch_interface_info_num_of_interfaces_0x2e18ede9bb02fce4_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.switch_interface.info.num_of_interfaces[21:16]"
    @property
    def rdl_desc(self) -> str:
        return "Number of interfaces in this openENOC Switch instance. This field reflects the NUM_OF_INTERFACES parameter value."
    
    
    

    
    
class openenoc_switch_interface_forwarding_control_operation_mode_neg_0x1bed4712acd488c5_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.switch_interface.forwarding_control.operation_mode[0:0]"
    @property
    def rdl_desc(self) -> str:
        return "Mode of operation for the openENOC Switch instance. When set to 1, the switch operates in managed mode, allowing software to configure the forwarding table and control forwarding operations. When set to 0, the switch operates in unmanaged mode, where forwarding state is maintained autonomously by internal hardware logic without software intervention."
    
    
    

    
    
class openenoc_switch_interface_forwarding_control_pause_request_neg_0x65b63504e60e16be_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.switch_interface.forwarding_control.pause_request[7:7]"
    @property
    def rdl_desc(self) -> str:
        return "Pause request for the forwarding logic. When set, this field requests the switch to pause frame forwarding and clear its internal pipeline before forwarding table updates are performed."
    
    
    

    
    
class openenoc_switch_interface_forwarding_control_pause_done_neg_0x5ee8ccac09e5f27d_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.switch_interface.forwarding_control.pause_done[15:15]"
    @property
    def rdl_desc(self) -> str:
        return "Pause done status. When set, this field indicates that the switch has paused frame forwarding and reached a safe state for forwarding table modification."
    
    
    

    
    
class openenoc_switch_interface_default_forwarding_bitmap_0x79aa258c5bb4962d_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.switch_interface.default_forwarding.bitmap[NUM_OF_INTERFACES-1:0]"
    @property
    def rdl_desc(self) -> str:
        return "Bitmap selecting the output interface or interfaces to which frames that do not match any enabled forwarding table entry are forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface."
    
    
    

    
    
class openenoc_switch_interface_forwarding_table_entry_mac_address_lo_word_0x4ac61d356e44e548_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.lo_word[31:0]"
    @property
    def rdl_desc(self) -> str:
        return "Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry."
    
    
    

    
    
class openenoc_switch_interface_forwarding_table_entry_mac_address_hi_word_neg_0x61d6e4d75dd2df73_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.hi_word[47:32]"
    @property
    def rdl_desc(self) -> str:
        return "Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry."
    
    
    

    
    
class openenoc_switch_interface_forwarding_table_entry_iface_bitmap_neg_0x28d5385d57cc0fa4_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]"
    @property
    def rdl_desc(self) -> str:
        return "Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface."
    
    
    

    
    
class openenoc_switch_interface_forwarding_table_entry_config_enabled_0x507eeb43cb8225a4_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

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
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled"
    @property
    def rdl_desc(self) -> str:
        return "Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup."
    
    
    


if __name__ == '__main__':
    pass