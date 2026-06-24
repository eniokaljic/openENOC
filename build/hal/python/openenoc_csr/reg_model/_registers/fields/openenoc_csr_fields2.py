

"""
Python Wrapper for the openenoc_csr register model

This code was generated from the PeakRDL-python package version 3.1.2

"""









from ....lib import UDPStruct
from ....lib import FieldReadOnly, FieldWriteOnly, FieldReadWrite, Field


# field definitions
    
    
class openenoc_switch_forwarding_control_pause_request_neg_0x720c32db768c9dff_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.switch1.forwarding_control.pause_request[7:7]                  |
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
        return "csr.switch1.forwarding_control.pause_request[7:7]"
    @property
    def rdl_desc(self) -> str:
        return "Pause request for the forwarding logic. When set, this field requests the switch to pause frame forwarding and clear its internal pipeline before forwarding table updates are performed."
    
    
    

    
    
class openenoc_switch_forwarding_control_pause_done_0x30a9e4ccb1f06e4a_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.switch1.forwarding_control.pause_done[15:15]                   |
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
        return "csr.switch1.forwarding_control.pause_done[15:15]"
    @property
    def rdl_desc(self) -> str:
        return "Pause done status. When set, this field indicates that the switch has paused frame forwarding and reached a safe state for forwarding table modification."
    
    
    

    
    
class openenoc_switch_default_forwarding_bitmap_0x67b1f974a797558d_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.switch1.default_forwarding.bitmap[NUM_OF_INTERFACES-1:0]       |
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
        return "csr.switch1.default_forwarding.bitmap[NUM_OF_INTERFACES-1:0]"
    @property
    def rdl_desc(self) -> str:
        return "Bitmap selecting the output interface or interfaces to which frames that do not match any enabled forwarding table entry are forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface."
    
    
    

    
    
class openenoc_switch_forwarding_table_entry_mac_address_lo_word_0x738bc4a3191fe4cf_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-                 |
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
        return "csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.lo_word[31:0]"
    @property
    def rdl_desc(self) -> str:
        return "Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry."
    
    
    

    
    
class openenoc_switch_forwarding_table_entry_mac_address_hi_word_0x68c9ecaac982d4a5_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-                 |
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
        return "csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.hi_word[47:32]"
    @property
    def rdl_desc(self) -> str:
        return "Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry."
    
    
    

    
    
class openenoc_switch_forwarding_table_entry_iface_bitmap_neg_0x5baaf220aa9f97a1_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-                 |
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
        return "csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]"
    @property
    def rdl_desc(self) -> str:
        return "Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface."
    
    
    

    
    
class openenoc_switch_forwarding_table_entry_config_enabled_0x471cba01095740d0_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-                 |
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
        return "csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled"
    @property
    def rdl_desc(self) -> str:
        return "Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup."
    
    
    

    
    
class openenoc_switch_info_table_depth_0x7f12fc9d365c3bc5_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.switch2.info.table_depth[15:0]                                 |
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
        return "csr.switch2.info.table_depth[15:0]"
    @property
    def rdl_desc(self) -> str:
        return "Depth of the forwarding table in this openENOC Switch instance. This field reflects the TABLE_DEPTH parameter value."
    
    
    

    
    
class openenoc_switch_info_num_of_interfaces_0x83fb07408080162_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.switch2.info.num_of_interfaces[21:16]                          |
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
        return "csr.switch2.info.num_of_interfaces[21:16]"
    @property
    def rdl_desc(self) -> str:
        return "Number of interfaces in this openENOC Switch instance. This field reflects the NUM_OF_INTERFACES parameter value."
    
    
    

    
    
class openenoc_switch_forwarding_control_operation_mode_0x6404e58015e440a4_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.switch2.forwarding_control.operation_mode[0:0]                 |
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
        return "csr.switch2.forwarding_control.operation_mode[0:0]"
    @property
    def rdl_desc(self) -> str:
        return "Mode of operation for the openENOC Switch instance. When set to 1, the switch operates in managed mode, allowing software to configure the forwarding table and control forwarding operations. When set to 0, the switch operates in unmanaged mode, where forwarding state is maintained autonomously by internal hardware logic without software intervention."
    
    
    

    
    
class openenoc_switch_forwarding_control_pause_request_neg_0x456f4eb51ea8ab05_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.switch2.forwarding_control.pause_request[7:7]                  |
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
        return "csr.switch2.forwarding_control.pause_request[7:7]"
    @property
    def rdl_desc(self) -> str:
        return "Pause request for the forwarding logic. When set, this field requests the switch to pause frame forwarding and clear its internal pipeline before forwarding table updates are performed."
    
    
    

    
    
class openenoc_switch_forwarding_control_pause_done_0x7e59160d993020a7_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.switch2.forwarding_control.pause_done[15:15]                   |
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
        return "csr.switch2.forwarding_control.pause_done[15:15]"
    @property
    def rdl_desc(self) -> str:
        return "Pause done status. When set, this field indicates that the switch has paused frame forwarding and reached a safe state for forwarding table modification."
    
    
    

    
    
class openenoc_switch_default_forwarding_bitmap_neg_0x5e27b7219eaedcbb_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.switch2.default_forwarding.bitmap[NUM_OF_INTERFACES-1:0]       |
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
        return "csr.switch2.default_forwarding.bitmap[NUM_OF_INTERFACES-1:0]"
    @property
    def rdl_desc(self) -> str:
        return "Bitmap selecting the output interface or interfaces to which frames that do not match any enabled forwarding table entry are forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface."
    
    
    

    
    
class openenoc_switch_forwarding_table_entry_mac_address_lo_word_0x49eb0013a7b460dc_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-                 |
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
        return "csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.lo_word[31:0]"
    @property
    def rdl_desc(self) -> str:
        return "Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry."
    
    
    

    
    
class openenoc_switch_forwarding_table_entry_mac_address_hi_word_0xae75c3718a090cf_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-                 |
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
        return "csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.hi_word[47:32]"
    @property
    def rdl_desc(self) -> str:
        return "Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry."
    
    
    

    
    
class openenoc_switch_forwarding_table_entry_iface_bitmap_0x3598fcfdda6317d6_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-                 |
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
        return "csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]"
    @property
    def rdl_desc(self) -> str:
        return "Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface."
    
    
    

    
    
class openenoc_switch_forwarding_table_entry_config_enabled_neg_0x2cfdca4a3b9765cc_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-                 |
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
        return "csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled"
    @property
    def rdl_desc(self) -> str:
        return "Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup."
    
    
    


if __name__ == '__main__':
    pass