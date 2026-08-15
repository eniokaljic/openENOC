

"""
Python Wrapper for the csr register model

This code was generated from the PeakRDL-python package version 3.1.2

"""









from ....lib import UDPStruct
from ....lib import FieldReadOnly, FieldWriteOnly, FieldReadWrite, Field


# field definitions
    
    
class openenoc_switch_interface_info_table_depth_0x1f523232bb6ad048_cls(FieldReadOnly):
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
    
    
    

    
    
class openenoc_switch_interface_info_num_of_interfaces_0x3783b49f00ac1afa_cls(FieldReadOnly):
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
    
    
    

    
    
class openenoc_switch_interface_forwarding_control_operation_mode_0x53980b4f97dca578_cls(FieldReadWrite):
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
    
    
    

    
    
class openenoc_switch_interface_forwarding_control_pause_request_0x28e139b166e4a560_cls(FieldReadWrite):
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
    
    
    

    
    
class openenoc_switch_interface_forwarding_control_pause_done_neg_0xea8be225bc9fdfc_cls(FieldReadOnly):
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
    
    
    

    
    
class openenoc_switch_interface_default_forwarding_bitmap_neg_0x21e17482d46c1437_cls(FieldReadWrite):
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
    
    
    

    
    
class openenoc_switch_interface_forwarding_table_entry_mac_address_lo_word_0x45996a5cc08c9c21_cls(FieldReadWrite):
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
    
    
    

    
    
class openenoc_switch_interface_forwarding_table_entry_mac_address_hi_word_neg_0xb77852204992c1_cls(FieldReadWrite):
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
    
    
    

    
    
class openenoc_switch_interface_forwarding_table_entry_iface_bitmap_neg_0x1dede35bdac060eb_cls(FieldReadWrite):
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
    
    
    

    
    
class openenoc_switch_interface_forwarding_table_entry_config_enabled_neg_0x26cb525c3da9ed7a_cls(FieldReadWrite):
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