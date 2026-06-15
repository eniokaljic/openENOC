<!---
Markdown description for SystemRDL register map.

Don't override. Generated from: openENOC
  - src/openENOC.rdl
-->

## openENOC address map

- Absolute Address: 0x0
- Base Offset: 0x0
- Size: 0x20000800

|  Offset  |Identifier|Name|
|----------|----------|----|
|0x00000000|   imem   |imem|
|0x10000000|   dmem   |dmem|
|0x20000000|    csr   | csr|

## imem memory

- Absolute Address: 0x0
- Base Offset: 0x0
- Size: 0x8000

<p>CPU Program Memory</p>

No supported members.


## dmem memory

- Absolute Address: 0x10000000
- Base Offset: 0x10000000
- Size: 0x8000

<p>CPU Data Memory</p>

No supported members.


## csr address map

- Absolute Address: 0x20000000
- Base Offset: 0x20000000
- Size: 0x800

<p>openENOC CSR</p>

|Offset|Identifier|    Name    |
|------|----------|------------|
| 0x000| test_reg |csr.test_reg|
| 0x004|   regB   |      —     |
| 0x100|  switch1 | csr.switch1|
| 0x400|  switch2 | csr.switch2|

### test_reg register

- Absolute Address: 0x20000000
- Base Offset: 0x0
- Size: 0x4

<p>Test register</p>

|Bits|Identifier|Access|Reset|             Name            |
|----|----------|------|-----|-----------------------------|
|31:0|test_field|  rw  | 0x0 |csr.test_reg.test_field[31:0]|

#### test_field field

<p>4-byte test field</p>

### regB register

- Absolute Address: 0x20000004
- Base Offset: 0x4
- Size: 0x4

| Bits|Identifier|Access|Reset|Name|
|-----|----------|------|-----|----|
| 7:0 |    f0    |  rw  | 0x0 |  — |
| 15:8|    f1    |  rw  | 0x0 |  — |
|23:16|    f2    |  rw  | 0x0 |  — |
|31:24|    f3    |  rw  | 0x0 |  — |

## switch1 address map

- Absolute Address: 0x20000100
- Base Offset: 0x100
- Size: 0x100

<p>Control and status register map for an openENOC Switch instance. It includes configuration registers and a forwarding table used to map destination MAC address keys to output interface selections for frame forwarding.</p>

|Offset|    Identifier    |             Name             |
|------|------------------|------------------------------|
| 0x00 |       info       |       csr.switch1.info       |
| 0x04 |forwarding_control|csr.switch1.forwarding_control|
| 0x08 |default_forwarding|csr.switch1.default_forwarding|
| 0x80 | forwarding_table | csr.switch1.forwarding_table |

### info register

- Absolute Address: 0x20000100
- Base Offset: 0x0
- Size: 0x4

<p>Read-only information register for this openENOC Switch instance.</p>

| Bits|    Identifier   |Access|Reset|                   Name                  |
|-----|-----------------|------|-----|-----------------------------------------|
| 15:0|   table_depth   |   r  | 0x8 |    csr.switch1.info.table_depth[15:0]   |
|21:16|num_of_interfaces|   r  | 0x4 |csr.switch1.info.num_of_interfaces[21:16]|

#### table_depth field

<p>Depth of the forwarding table in this openENOC Switch instance. This field reflects the TABLE_DEPTH parameter value.</p>

#### num_of_interfaces field

<p>Number of interfaces in this openENOC Switch instance. This field reflects the NUM_OF_INTERFACES parameter value.</p>

### forwarding_control register

- Absolute Address: 0x20000104
- Base Offset: 0x4
- Size: 0x4

<p>Forwarding control register for the openENOC Switch instance.</p>

|Bits|  Identifier  |Access|Reset|                       Name                       |
|----|--------------|------|-----|--------------------------------------------------|
|  0 |operation_mode|  rw  | 0x0 |csr.switch1.forwarding_control.operation_mode[0:0]|
|  7 | pause_request|  rw  | 0x0 | csr.switch1.forwarding_control.pause_request[7:7]|
| 15 |  pause_done  |   r  |  —  | csr.switch1.forwarding_control.pause_done[15:15] |

#### operation_mode field

<p>Mode of operation for the openENOC Switch instance. When set to 1, the switch operates in managed mode, allowing software to configure the forwarding table and control forwarding operations. When set to 0, the switch operates in unmanaged mode, where forwarding state is maintained autonomously by internal hardware logic without software intervention.</p>

#### pause_request field

<p>Pause request for the forwarding logic. When set, this field requests the switch to pause frame forwarding and clear its internal pipeline before forwarding table updates are performed.</p>

#### pause_done field

<p>Pause done status. When set, this field indicates that the switch has paused frame forwarding and reached a safe state for forwarding table modification.</p>

### default_forwarding register

- Absolute Address: 0x20000108
- Base Offset: 0x8
- Size: 0x4

<p>Defines the destination interface or interfaces for frames that do not match any enabled forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                            Name                            |
|----|----------|------|-----|------------------------------------------------------------|
| 3:0|  bitmap  |  rw  | 0x0 |csr.switch1.default_forwarding.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which frames that do not match any enabled forwarding table entry are forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

## forwarding_table register file

- Absolute Address: 0x20000180
- Base Offset: 0x80
- Size: 0x80

<p>Forwarding table used to map MAC addresses to output interface selections for frame forwarding.</p>

|Offset|Identifier|                        Name                        |
|------|----------|----------------------------------------------------|
| 0x00 | entry[0] |csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x10 | entry[1] |csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x20 | entry[2] |csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x30 | entry[3] |csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x40 | entry[4] |csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x50 | entry[5] |csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x60 | entry[6] |csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x70 | entry[7] |csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1]|

## entry register file

- Absolute Address: 0x20000180
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [8]
- Array Stride: 0x10
- Total Size: 0x80

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                            Name                            |
|------|----------|------------------------------------------------------------|
|  0x0 |  macaddr |csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x20000180
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                    Name                                   |
|-----|----------|------|-----|---------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x20000188
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 3:0|  bitmap  |  rw  |  —  |csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x2000018C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x20000190
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [8]
- Array Stride: 0x10
- Total Size: 0x80

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                            Name                            |
|------|----------|------------------------------------------------------------|
|  0x0 |  macaddr |csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x20000190
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                    Name                                   |
|-----|----------|------|-----|---------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x20000198
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 3:0|  bitmap  |  rw  |  —  |csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x2000019C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x200001A0
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [8]
- Array Stride: 0x10
- Total Size: 0x80

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                            Name                            |
|------|----------|------------------------------------------------------------|
|  0x0 |  macaddr |csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x200001A0
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                    Name                                   |
|-----|----------|------|-----|---------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x200001A8
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 3:0|  bitmap  |  rw  |  —  |csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x200001AC
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x200001B0
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [8]
- Array Stride: 0x10
- Total Size: 0x80

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                            Name                            |
|------|----------|------------------------------------------------------------|
|  0x0 |  macaddr |csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x200001B0
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                    Name                                   |
|-----|----------|------|-----|---------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x200001B8
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 3:0|  bitmap  |  rw  |  —  |csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x200001BC
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x200001C0
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [8]
- Array Stride: 0x10
- Total Size: 0x80

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                            Name                            |
|------|----------|------------------------------------------------------------|
|  0x0 |  macaddr |csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x200001C0
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                    Name                                   |
|-----|----------|------|-----|---------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x200001C8
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 3:0|  bitmap  |  rw  |  —  |csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x200001CC
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x200001D0
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [8]
- Array Stride: 0x10
- Total Size: 0x80

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                            Name                            |
|------|----------|------------------------------------------------------------|
|  0x0 |  macaddr |csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x200001D0
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                    Name                                   |
|-----|----------|------|-----|---------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x200001D8
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 3:0|  bitmap  |  rw  |  —  |csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x200001DC
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x200001E0
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [8]
- Array Stride: 0x10
- Total Size: 0x80

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                            Name                            |
|------|----------|------------------------------------------------------------|
|  0x0 |  macaddr |csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x200001E0
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                    Name                                   |
|-----|----------|------|-----|---------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x200001E8
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 3:0|  bitmap  |  rw  |  —  |csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x200001EC
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x200001F0
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [8]
- Array Stride: 0x10
- Total Size: 0x80

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                            Name                            |
|------|----------|------------------------------------------------------------|
|  0x0 |  macaddr |csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x200001F0
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                    Name                                   |
|-----|----------|------|-----|---------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x200001F8
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 3:0|  bitmap  |  rw  |  —  |csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x200001FC
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## switch2 address map

- Absolute Address: 0x20000400
- Base Offset: 0x400
- Size: 0x400

<p>Control and status register map for an openENOC Switch instance. It includes configuration registers and a forwarding table used to map destination MAC address keys to output interface selections for frame forwarding.</p>

|Offset|    Identifier    |             Name             |
|------|------------------|------------------------------|
| 0x000|       info       |       csr.switch2.info       |
| 0x004|forwarding_control|csr.switch2.forwarding_control|
| 0x008|default_forwarding|csr.switch2.default_forwarding|
| 0x200| forwarding_table | csr.switch2.forwarding_table |

### info register

- Absolute Address: 0x20000400
- Base Offset: 0x0
- Size: 0x4

<p>Read-only information register for this openENOC Switch instance.</p>

| Bits|    Identifier   |Access|Reset|                   Name                  |
|-----|-----------------|------|-----|-----------------------------------------|
| 15:0|   table_depth   |   r  | 0x20|    csr.switch2.info.table_depth[15:0]   |
|21:16|num_of_interfaces|   r  | 0x8 |csr.switch2.info.num_of_interfaces[21:16]|

#### table_depth field

<p>Depth of the forwarding table in this openENOC Switch instance. This field reflects the TABLE_DEPTH parameter value.</p>

#### num_of_interfaces field

<p>Number of interfaces in this openENOC Switch instance. This field reflects the NUM_OF_INTERFACES parameter value.</p>

### forwarding_control register

- Absolute Address: 0x20000404
- Base Offset: 0x4
- Size: 0x4

<p>Forwarding control register for the openENOC Switch instance.</p>

|Bits|  Identifier  |Access|Reset|                       Name                       |
|----|--------------|------|-----|--------------------------------------------------|
|  0 |operation_mode|  rw  | 0x0 |csr.switch2.forwarding_control.operation_mode[0:0]|
|  7 | pause_request|  rw  | 0x0 | csr.switch2.forwarding_control.pause_request[7:7]|
| 15 |  pause_done  |   r  |  —  | csr.switch2.forwarding_control.pause_done[15:15] |

#### operation_mode field

<p>Mode of operation for the openENOC Switch instance. When set to 1, the switch operates in managed mode, allowing software to configure the forwarding table and control forwarding operations. When set to 0, the switch operates in unmanaged mode, where forwarding state is maintained autonomously by internal hardware logic without software intervention.</p>

#### pause_request field

<p>Pause request for the forwarding logic. When set, this field requests the switch to pause frame forwarding and clear its internal pipeline before forwarding table updates are performed.</p>

#### pause_done field

<p>Pause done status. When set, this field indicates that the switch has paused frame forwarding and reached a safe state for forwarding table modification.</p>

### default_forwarding register

- Absolute Address: 0x20000408
- Base Offset: 0x8
- Size: 0x4

<p>Defines the destination interface or interfaces for frames that do not match any enabled forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                            Name                            |
|----|----------|------|-----|------------------------------------------------------------|
| 7:0|  bitmap  |  rw  | 0x0 |csr.switch2.default_forwarding.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which frames that do not match any enabled forwarding table entry are forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

## forwarding_table register file

- Absolute Address: 0x20000600
- Base Offset: 0x200
- Size: 0x200

<p>Forwarding table used to map MAC addresses to output interface selections for frame forwarding.</p>

|Offset|Identifier|                        Name                        |
|------|----------|----------------------------------------------------|
| 0x000| entry[0] |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x010| entry[1] |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x020| entry[2] |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x030| entry[3] |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x040| entry[4] |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x050| entry[5] |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x060| entry[6] |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x070| entry[7] |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x080| entry[8] |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x090| entry[9] |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x0A0| entry[10]|csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x0B0| entry[11]|csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x0C0| entry[12]|csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x0D0| entry[13]|csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x0E0| entry[14]|csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x0F0| entry[15]|csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x100| entry[16]|csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x110| entry[17]|csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x120| entry[18]|csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x130| entry[19]|csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x140| entry[20]|csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x150| entry[21]|csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x160| entry[22]|csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x170| entry[23]|csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x180| entry[24]|csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x190| entry[25]|csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x1A0| entry[26]|csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x1B0| entry[27]|csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x1C0| entry[28]|csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x1D0| entry[29]|csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x1E0| entry[30]|csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x1F0| entry[31]|csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1]|

## entry register file

- Absolute Address: 0x20000600
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                            Name                            |
|------|----------|------------------------------------------------------------|
|  0x0 |  macaddr |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x20000600
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                    Name                                   |
|-----|----------|------|-----|---------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x20000608
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x2000060C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x20000610
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                            Name                            |
|------|----------|------------------------------------------------------------|
|  0x0 |  macaddr |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x20000610
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                    Name                                   |
|-----|----------|------|-----|---------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x20000618
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x2000061C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x20000620
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                            Name                            |
|------|----------|------------------------------------------------------------|
|  0x0 |  macaddr |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x20000620
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                    Name                                   |
|-----|----------|------|-----|---------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x20000628
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x2000062C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x20000630
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                            Name                            |
|------|----------|------------------------------------------------------------|
|  0x0 |  macaddr |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x20000630
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                    Name                                   |
|-----|----------|------|-----|---------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x20000638
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x2000063C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x20000640
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                            Name                            |
|------|----------|------------------------------------------------------------|
|  0x0 |  macaddr |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x20000640
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                    Name                                   |
|-----|----------|------|-----|---------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x20000648
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x2000064C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x20000650
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                            Name                            |
|------|----------|------------------------------------------------------------|
|  0x0 |  macaddr |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x20000650
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                    Name                                   |
|-----|----------|------|-----|---------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x20000658
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x2000065C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x20000660
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                            Name                            |
|------|----------|------------------------------------------------------------|
|  0x0 |  macaddr |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x20000660
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                    Name                                   |
|-----|----------|------|-----|---------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x20000668
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x2000066C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x20000670
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                            Name                            |
|------|----------|------------------------------------------------------------|
|  0x0 |  macaddr |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x20000670
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                    Name                                   |
|-----|----------|------|-----|---------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x20000678
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x2000067C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x20000680
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                            Name                            |
|------|----------|------------------------------------------------------------|
|  0x0 |  macaddr |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x20000680
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                    Name                                   |
|-----|----------|------|-----|---------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x20000688
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x2000068C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x20000690
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                            Name                            |
|------|----------|------------------------------------------------------------|
|  0x0 |  macaddr |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x20000690
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                    Name                                   |
|-----|----------|------|-----|---------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x20000698
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x2000069C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x200006A0
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                            Name                            |
|------|----------|------------------------------------------------------------|
|  0x0 |  macaddr |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x200006A0
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                    Name                                   |
|-----|----------|------|-----|---------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x200006A8
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x200006AC
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x200006B0
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                            Name                            |
|------|----------|------------------------------------------------------------|
|  0x0 |  macaddr |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x200006B0
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                    Name                                   |
|-----|----------|------|-----|---------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x200006B8
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x200006BC
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x200006C0
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                            Name                            |
|------|----------|------------------------------------------------------------|
|  0x0 |  macaddr |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x200006C0
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                    Name                                   |
|-----|----------|------|-----|---------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x200006C8
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x200006CC
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x200006D0
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                            Name                            |
|------|----------|------------------------------------------------------------|
|  0x0 |  macaddr |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x200006D0
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                    Name                                   |
|-----|----------|------|-----|---------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x200006D8
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x200006DC
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x200006E0
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                            Name                            |
|------|----------|------------------------------------------------------------|
|  0x0 |  macaddr |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x200006E0
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                    Name                                   |
|-----|----------|------|-----|---------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x200006E8
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x200006EC
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x200006F0
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                            Name                            |
|------|----------|------------------------------------------------------------|
|  0x0 |  macaddr |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x200006F0
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                    Name                                   |
|-----|----------|------|-----|---------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x200006F8
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x200006FC
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x20000700
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                            Name                            |
|------|----------|------------------------------------------------------------|
|  0x0 |  macaddr |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x20000700
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                    Name                                   |
|-----|----------|------|-----|---------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x20000708
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x2000070C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x20000710
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                            Name                            |
|------|----------|------------------------------------------------------------|
|  0x0 |  macaddr |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x20000710
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                    Name                                   |
|-----|----------|------|-----|---------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x20000718
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x2000071C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x20000720
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                            Name                            |
|------|----------|------------------------------------------------------------|
|  0x0 |  macaddr |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x20000720
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                    Name                                   |
|-----|----------|------|-----|---------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x20000728
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x2000072C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x20000730
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                            Name                            |
|------|----------|------------------------------------------------------------|
|  0x0 |  macaddr |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x20000730
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                    Name                                   |
|-----|----------|------|-----|---------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x20000738
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x2000073C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x20000740
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                            Name                            |
|------|----------|------------------------------------------------------------|
|  0x0 |  macaddr |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x20000740
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                    Name                                   |
|-----|----------|------|-----|---------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x20000748
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x2000074C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x20000750
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                            Name                            |
|------|----------|------------------------------------------------------------|
|  0x0 |  macaddr |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x20000750
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                    Name                                   |
|-----|----------|------|-----|---------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x20000758
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x2000075C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x20000760
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                            Name                            |
|------|----------|------------------------------------------------------------|
|  0x0 |  macaddr |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x20000760
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                    Name                                   |
|-----|----------|------|-----|---------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x20000768
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x2000076C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x20000770
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                            Name                            |
|------|----------|------------------------------------------------------------|
|  0x0 |  macaddr |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x20000770
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                    Name                                   |
|-----|----------|------|-----|---------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x20000778
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x2000077C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x20000780
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                            Name                            |
|------|----------|------------------------------------------------------------|
|  0x0 |  macaddr |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x20000780
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                    Name                                   |
|-----|----------|------|-----|---------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x20000788
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x2000078C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x20000790
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                            Name                            |
|------|----------|------------------------------------------------------------|
|  0x0 |  macaddr |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x20000790
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                    Name                                   |
|-----|----------|------|-----|---------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x20000798
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x2000079C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x200007A0
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                            Name                            |
|------|----------|------------------------------------------------------------|
|  0x0 |  macaddr |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x200007A0
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                    Name                                   |
|-----|----------|------|-----|---------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x200007A8
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x200007AC
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x200007B0
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                            Name                            |
|------|----------|------------------------------------------------------------|
|  0x0 |  macaddr |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x200007B0
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                    Name                                   |
|-----|----------|------|-----|---------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x200007B8
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x200007BC
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x200007C0
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                            Name                            |
|------|----------|------------------------------------------------------------|
|  0x0 |  macaddr |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x200007C0
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                    Name                                   |
|-----|----------|------|-----|---------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x200007C8
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x200007CC
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x200007D0
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                            Name                            |
|------|----------|------------------------------------------------------------|
|  0x0 |  macaddr |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x200007D0
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                    Name                                   |
|-----|----------|------|-----|---------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x200007D8
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x200007DC
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x200007E0
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                            Name                            |
|------|----------|------------------------------------------------------------|
|  0x0 |  macaddr |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x200007E0
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                    Name                                   |
|-----|----------|------|-----|---------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x200007E8
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x200007EC
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x200007F0
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset|Identifier|                            Name                            |
|------|----------|------------------------------------------------------------|
|  0x0 |  macaddr |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr|
|  0x8 |   iface  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface |
|  0xC |  config  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config|

### macaddr register

- Absolute Address: 0x200007F0
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                    Name                                   |
|-----|----------|------|-----|---------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].macaddr.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x200007F8
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x200007FC
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>
