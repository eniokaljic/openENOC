<!---
Markdown description for SystemRDL register map.

Don't override. Generated from: openenoc_switch
  - /home/enio/Projects/openENOC/hal/src/openenoc.rdl
-->

## openenoc_switch address map

- Absolute Address: 0x0
- Base Offset: 0x0
- Size: 0x20

<p>Control and status register map for an openENOC Switch instance. It includes configuration registers and a forwarding table used to map destination MAC address keys to output interface selections for frame forwarding.</p>

|Offset|    Identifier    |               Name               |
|------|------------------|----------------------------------|
| 0x00 |       info       |       openenoc_switch.info       |
| 0x04 |forwarding_control|openenoc_switch.forwarding_control|
| 0x08 |default_forwarding|openenoc_switch.default_forwarding|
| 0x10 | forwarding_table | openenoc_switch.forwarding_table |

### info register

- Absolute Address: 0x0
- Base Offset: 0x0
- Size: 0x4

<p>Read-only information register for this openENOC Switch instance.</p>

| Bits|    Identifier   |Access|Reset|                     Name                    |
|-----|-----------------|------|-----|---------------------------------------------|
| 15:0|   table_depth   |   r  | 0x1 |    openenoc_switch.info.table_depth[15:0]   |
|21:16|num_of_interfaces|   r  | 0x1 |openenoc_switch.info.num_of_interfaces[21:16]|

#### table_depth field

<p>Depth of the forwarding table in this openENOC Switch instance. This field reflects the TABLE_DEPTH parameter value.</p>

#### num_of_interfaces field

<p>Number of interfaces in this openENOC Switch instance. This field reflects the NUM_OF_INTERFACES parameter value.</p>

### forwarding_control register

- Absolute Address: 0x4
- Base Offset: 0x4
- Size: 0x4

<p>Forwarding control register for the openENOC Switch instance.</p>

|Bits|  Identifier  |Access|Reset|                         Name                         |
|----|--------------|------|-----|------------------------------------------------------|
|  0 |operation_mode|  rw  | 0x0 |openenoc_switch.forwarding_control.operation_mode[0:0]|
|  7 | pause_request|  rw  | 0x0 | openenoc_switch.forwarding_control.pause_request[7:7]|
| 15 |  pause_done  |   r  |  —  | openenoc_switch.forwarding_control.pause_done[15:15] |

#### operation_mode field

<p>Mode of operation for the openENOC Switch instance. When set to 1, the switch operates in managed mode, allowing software to configure the forwarding table and control forwarding operations. When set to 0, the switch operates in unmanaged mode, where forwarding state is maintained autonomously by internal hardware logic without software intervention.</p>

#### pause_request field

<p>Pause request for the forwarding logic. When set, this field requests the switch to pause frame forwarding and clear its internal pipeline before forwarding table updates are performed.</p>

#### pause_done field

<p>Pause done status. When set, this field indicates that the switch has paused frame forwarding and reached a safe state for forwarding table modification.</p>

### default_forwarding register

- Absolute Address: 0x8
- Base Offset: 0x8
- Size: 0x4

<p>Defines the destination interface or interfaces for frames that do not match any enabled forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                              Name                              |
|----|----------|------|-----|----------------------------------------------------------------|
|  0 |  bitmap  |  rw  | 0x0 |openenoc_switch.default_forwarding.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which frames that do not match any enabled forwarding table entry are forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

## forwarding_table register file

- Absolute Address: 0x10
- Base Offset: 0x10
- Size: 0x10

<p>Forwarding table used to map MAC addresses to output interface selections for frame forwarding.</p>

|Offset|Identifier|                          Name                          |
|------|----------|--------------------------------------------------------|
|  0x0 | entry[0] |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1]|

## entry register file

- Absolute Address: 0x10
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [1]
- Array Stride: 0x10
- Total Size: 0x10

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset| Identifier|                                Name                                |
|------|-----------|--------------------------------------------------------------------|
|  0x0 |mac_address|openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address|
|  0x8 |   iface   |   openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface   |
|  0xC |   config  |   openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config  |

### mac_address register

- Absolute Address: 0x10
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                        Name                                       |
|-----|----------|------|-----|-----------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x18
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                            Name                                            |
|----|----------|------|-----|--------------------------------------------------------------------------------------------|
|  0 |  bitmap  |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x1C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                  Name                                 |
|----|----------|------|-----|-----------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>
