<!---
Markdown description for SystemRDL register map.

Don't override. Generated from: openenoc_switch
  - /home/enio/Projects/openENOC/hal/src/openenoc.rdl
-->

## openenoc_switch address map

- Absolute Address: 0x0
- Base Offset: 0x0
- Size: 0x400

<p>Control and status register map for an openENOC Switch instance. It includes configuration registers and a forwarding table used to map destination MAC address keys to output interface selections for frame forwarding.</p>

|Offset|    Identifier    |               Name               |
|------|------------------|----------------------------------|
| 0x000|       info       |       openenoc_switch.info       |
| 0x004|forwarding_control|openenoc_switch.forwarding_control|
| 0x008|default_forwarding|openenoc_switch.default_forwarding|
| 0x200| forwarding_table | openenoc_switch.forwarding_table |

### info register

- Absolute Address: 0x0
- Base Offset: 0x0
- Size: 0x4

<p>Read-only information register for this openENOC Switch instance.</p>

| Bits|    Identifier   |Access|Reset|                     Name                    |
|-----|-----------------|------|-----|---------------------------------------------|
| 15:0|   table_depth   |   r  | 0x20|    openenoc_switch.info.table_depth[15:0]   |
|21:16|num_of_interfaces|   r  | 0x8 |openenoc_switch.info.num_of_interfaces[21:16]|

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
| 7:0|  bitmap  |  rw  | 0x0 |openenoc_switch.default_forwarding.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which frames that do not match any enabled forwarding table entry are forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

## forwarding_table register file

- Absolute Address: 0x200
- Base Offset: 0x200
- Size: 0x200

<p>Forwarding table used to map MAC addresses to output interface selections for frame forwarding.</p>

|Offset|Identifier|                          Name                          |
|------|----------|--------------------------------------------------------|
| 0x000| entry[0] |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x010| entry[1] |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x020| entry[2] |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x030| entry[3] |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x040| entry[4] |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x050| entry[5] |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x060| entry[6] |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x070| entry[7] |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x080| entry[8] |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x090| entry[9] |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x0A0| entry[10]|openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x0B0| entry[11]|openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x0C0| entry[12]|openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x0D0| entry[13]|openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x0E0| entry[14]|openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x0F0| entry[15]|openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x100| entry[16]|openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x110| entry[17]|openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x120| entry[18]|openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x130| entry[19]|openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x140| entry[20]|openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x150| entry[21]|openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x160| entry[22]|openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x170| entry[23]|openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x180| entry[24]|openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x190| entry[25]|openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x1A0| entry[26]|openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x1B0| entry[27]|openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x1C0| entry[28]|openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x1D0| entry[29]|openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x1E0| entry[30]|openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x1F0| entry[31]|openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1]|

## entry register file

- Absolute Address: 0x200
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                              Name                              |
|------|----------|----------------------------------------------------------------|
|  0x0 |  macaddr |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x200
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x208
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                            Name                                            |
|----|----------|------|-----|--------------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x20C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                  Name                                 |
|----|----------|------|-----|-----------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x210
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                              Name                              |
|------|----------|----------------------------------------------------------------|
|  0x0 |  macaddr |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x210
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x218
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                            Name                                            |
|----|----------|------|-----|--------------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x21C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                  Name                                 |
|----|----------|------|-----|-----------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x220
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                              Name                              |
|------|----------|----------------------------------------------------------------|
|  0x0 |  macaddr |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x220
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x228
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                            Name                                            |
|----|----------|------|-----|--------------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x22C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                  Name                                 |
|----|----------|------|-----|-----------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x230
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                              Name                              |
|------|----------|----------------------------------------------------------------|
|  0x0 |  macaddr |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x230
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x238
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                            Name                                            |
|----|----------|------|-----|--------------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x23C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                  Name                                 |
|----|----------|------|-----|-----------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x240
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                              Name                              |
|------|----------|----------------------------------------------------------------|
|  0x0 |  macaddr |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x240
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x248
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                            Name                                            |
|----|----------|------|-----|--------------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x24C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                  Name                                 |
|----|----------|------|-----|-----------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x250
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                              Name                              |
|------|----------|----------------------------------------------------------------|
|  0x0 |  macaddr |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x250
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x258
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                            Name                                            |
|----|----------|------|-----|--------------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x25C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                  Name                                 |
|----|----------|------|-----|-----------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x260
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                              Name                              |
|------|----------|----------------------------------------------------------------|
|  0x0 |  macaddr |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x260
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x268
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                            Name                                            |
|----|----------|------|-----|--------------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x26C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                  Name                                 |
|----|----------|------|-----|-----------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x270
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                              Name                              |
|------|----------|----------------------------------------------------------------|
|  0x0 |  macaddr |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x270
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x278
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                            Name                                            |
|----|----------|------|-----|--------------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x27C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                  Name                                 |
|----|----------|------|-----|-----------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x280
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                              Name                              |
|------|----------|----------------------------------------------------------------|
|  0x0 |  macaddr |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x280
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x288
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                            Name                                            |
|----|----------|------|-----|--------------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x28C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                  Name                                 |
|----|----------|------|-----|-----------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x290
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                              Name                              |
|------|----------|----------------------------------------------------------------|
|  0x0 |  macaddr |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x290
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x298
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                            Name                                            |
|----|----------|------|-----|--------------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x29C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                  Name                                 |
|----|----------|------|-----|-----------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x2A0
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                              Name                              |
|------|----------|----------------------------------------------------------------|
|  0x0 |  macaddr |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x2A0
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x2A8
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                            Name                                            |
|----|----------|------|-----|--------------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x2AC
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                  Name                                 |
|----|----------|------|-----|-----------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x2B0
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                              Name                              |
|------|----------|----------------------------------------------------------------|
|  0x0 |  macaddr |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x2B0
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x2B8
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                            Name                                            |
|----|----------|------|-----|--------------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x2BC
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                  Name                                 |
|----|----------|------|-----|-----------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x2C0
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                              Name                              |
|------|----------|----------------------------------------------------------------|
|  0x0 |  macaddr |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x2C0
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x2C8
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                            Name                                            |
|----|----------|------|-----|--------------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x2CC
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                  Name                                 |
|----|----------|------|-----|-----------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x2D0
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                              Name                              |
|------|----------|----------------------------------------------------------------|
|  0x0 |  macaddr |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x2D0
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x2D8
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                            Name                                            |
|----|----------|------|-----|--------------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x2DC
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                  Name                                 |
|----|----------|------|-----|-----------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x2E0
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                              Name                              |
|------|----------|----------------------------------------------------------------|
|  0x0 |  macaddr |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x2E0
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x2E8
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                            Name                                            |
|----|----------|------|-----|--------------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x2EC
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                  Name                                 |
|----|----------|------|-----|-----------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x2F0
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                              Name                              |
|------|----------|----------------------------------------------------------------|
|  0x0 |  macaddr |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x2F0
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x2F8
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                            Name                                            |
|----|----------|------|-----|--------------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x2FC
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                  Name                                 |
|----|----------|------|-----|-----------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x300
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                              Name                              |
|------|----------|----------------------------------------------------------------|
|  0x0 |  macaddr |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x300
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x308
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                            Name                                            |
|----|----------|------|-----|--------------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x30C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                  Name                                 |
|----|----------|------|-----|-----------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x310
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                              Name                              |
|------|----------|----------------------------------------------------------------|
|  0x0 |  macaddr |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x310
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x318
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                            Name                                            |
|----|----------|------|-----|--------------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x31C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                  Name                                 |
|----|----------|------|-----|-----------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x320
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                              Name                              |
|------|----------|----------------------------------------------------------------|
|  0x0 |  macaddr |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x320
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x328
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                            Name                                            |
|----|----------|------|-----|--------------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x32C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                  Name                                 |
|----|----------|------|-----|-----------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x330
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                              Name                              |
|------|----------|----------------------------------------------------------------|
|  0x0 |  macaddr |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x330
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x338
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                            Name                                            |
|----|----------|------|-----|--------------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x33C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                  Name                                 |
|----|----------|------|-----|-----------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x340
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                              Name                              |
|------|----------|----------------------------------------------------------------|
|  0x0 |  macaddr |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x340
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x348
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                            Name                                            |
|----|----------|------|-----|--------------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x34C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                  Name                                 |
|----|----------|------|-----|-----------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x350
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                              Name                              |
|------|----------|----------------------------------------------------------------|
|  0x0 |  macaddr |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x350
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x358
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                            Name                                            |
|----|----------|------|-----|--------------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x35C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                  Name                                 |
|----|----------|------|-----|-----------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x360
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                              Name                              |
|------|----------|----------------------------------------------------------------|
|  0x0 |  macaddr |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x360
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x368
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                            Name                                            |
|----|----------|------|-----|--------------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x36C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                  Name                                 |
|----|----------|------|-----|-----------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x370
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                              Name                              |
|------|----------|----------------------------------------------------------------|
|  0x0 |  macaddr |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x370
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x378
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                            Name                                            |
|----|----------|------|-----|--------------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x37C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                  Name                                 |
|----|----------|------|-----|-----------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x380
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                              Name                              |
|------|----------|----------------------------------------------------------------|
|  0x0 |  macaddr |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x380
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x388
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                            Name                                            |
|----|----------|------|-----|--------------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x38C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                  Name                                 |
|----|----------|------|-----|-----------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x390
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                              Name                              |
|------|----------|----------------------------------------------------------------|
|  0x0 |  macaddr |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x390
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x398
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                            Name                                            |
|----|----------|------|-----|--------------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x39C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                  Name                                 |
|----|----------|------|-----|-----------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x3A0
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                              Name                              |
|------|----------|----------------------------------------------------------------|
|  0x0 |  macaddr |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x3A0
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x3A8
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                            Name                                            |
|----|----------|------|-----|--------------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x3AC
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                  Name                                 |
|----|----------|------|-----|-----------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x3B0
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                              Name                              |
|------|----------|----------------------------------------------------------------|
|  0x0 |  macaddr |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x3B0
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x3B8
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                            Name                                            |
|----|----------|------|-----|--------------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x3BC
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                  Name                                 |
|----|----------|------|-----|-----------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x3C0
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                              Name                              |
|------|----------|----------------------------------------------------------------|
|  0x0 |  macaddr |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x3C0
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x3C8
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                            Name                                            |
|----|----------|------|-----|--------------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x3CC
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                  Name                                 |
|----|----------|------|-----|-----------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x3D0
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                              Name                              |
|------|----------|----------------------------------------------------------------|
|  0x0 |  macaddr |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x3D0
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x3D8
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                            Name                                            |
|----|----------|------|-----|--------------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x3DC
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                  Name                                 |
|----|----------|------|-----|-----------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x3E0
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                              Name                              |
|------|----------|----------------------------------------------------------------|
|  0x0 |  macaddr |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x3E0
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x3E8
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                            Name                                            |
|----|----------|------|-----|--------------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x3EC
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                  Name                                 |
|----|----------|------|-----|-----------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x3F0
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                              Name                              |
|------|----------|----------------------------------------------------------------|
|  0x0 |  macaddr |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x3F0
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x3F8
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                            Name                                            |
|----|----------|------|-----|--------------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x3FC
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                  Name                                 |
|----|----------|------|-----|-----------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |openenoc_switch.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>
