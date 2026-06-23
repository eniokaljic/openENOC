<!---
Markdown description for SystemRDL register map.

Don't override. Generated from: openenoc
  - /home/enio/Projects/openENOC/hal/src/openenoc.rdl
-->

## openenoc address map

- Absolute Address: 0x0
- Base Offset: 0x0
- Size: 0x20001C00

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
- Size: 0x1C00

<p>openENOC CSR</p>

|Offset|Identifier|     Name    |
|------|----------|-------------|
|0x0000| test_reg | csr.test_reg|
|0x0004|   regB   |      —      |
|0x0800| endpoint1|csr.endpoint1|
|0x1000| endpoint2|csr.endpoint2|
|0x1400|  switch1 | csr.switch1 |
|0x1800|  switch2 | csr.switch2 |

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

## endpoint1 address map

- Absolute Address: 0x20000800
- Base Offset: 0x800
- Size: 0x800

<p>Control and status register map for an openENOC Endpoint Interface instance.</p>

|Offset|Identifier|        Name        |
|------|----------|--------------------|
| 0x000|   info   | csr.endpoint1.info |
| 0x008|  config  |csr.endpoint1.config|
| 0x080|   peers  | csr.endpoint1.peers|
| 0x400|   rmem   |        rmem        |

### info register

- Absolute Address: 0x20000800
- Base Offset: 0x0
- Size: 0x4

<p>Read-only information register for this openENOC Endpoint Interface instance.</p>

| Bits|   Identifier   |Access|Reset|                   Name                  |
|-----|----------------|------|-----|-----------------------------------------|
| 15:0|rmem_total_depth|   r  |0x100|csr.endpoint1.info.rmem_total_depth[15:0]|
|31:16|  num_of_peers  |   r  | 0x4 |  csr.endpoint1.info.num_of_peers[31:16] |

#### rmem_total_depth field

<p>Total depth of the shared memory region for all remote peers. This field reflects the RMEM_TOTAL_DEPTH parameter value.</p>

#### num_of_peers field

<p>Number of remote peers supported by this openENOC Endpoint Interface instance. This field reflects the NUM_OF_PEERS parameter value.</p>

## config register file

- Absolute Address: 0x20000808
- Base Offset: 0x8
- Size: 0x8

<p>Configuration register file for this openENOC Endpoint Interface instance.</p>

|Offset| Identifier|              Name              |
|------|-----------|--------------------------------|
|  0x0 |mac_address|csr.endpoint1.config.mac_address|

### mac_address register

- Absolute Address: 0x20000808
- Base Offset: 0x0
- Size: 0x8

<p>Local site 48-bit destination MAC address.</p>

| Bits|Identifier|Access|Reset|                      Name                     |
|-----|----------|------|-----|-----------------------------------------------|
| 31:0|  lo_word |  rw  | 0x0 | csr.endpoint1.config.mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  | 0x0 |csr.endpoint1.config.mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address.</p>

## peers register file

- Absolute Address: 0x20000880
- Base Offset: 0x80
- Size: 0x70

<p>Register file for remote peer configuration and memory region information.</p>

|Offset|Identifier|                    Name                    |
|------|----------|--------------------------------------------|
| 0x00 | entry[0] |csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1]|
| 0x1C | entry[1] |csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1]|
| 0x38 | entry[2] |csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1]|
| 0x54 | entry[3] |csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1]|

## entry register file

- Absolute Address: 0x20000880
- Base Offset: 0x0
- Size: 0x1C
- Array Dimensions: [4]
- Array Stride: 0x1C
- Total Size: 0x70

<p>Register file for a single remote peer configuration and memory region information.</p>

|Offset|  Identifier  |                            Name                           |
|------|--------------|-----------------------------------------------------------|
| 0x00 |  mac_address |  csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].mac_address |
| 0x08 | rmem_address | csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].rmem_address |
| 0x0C | local_address| csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].local_address|
| 0x10 |remote_address|csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].remote_address|
| 0x14 |     size     |     csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].size     |
| 0x18 |  dma_config  |  csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].dma_config  |

### mac_address register

- Absolute Address: 0x20000880
- Base Offset: 0x0
- Size: 0x8

<p>Remote peer 48-bit destination MAC address.</p>

| Bits|Identifier|Access|Reset|                                  Name                                 |
|-----|----------|------|-----|-----------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address.</p>

### rmem_address register

- Absolute Address: 0x20000888
- Base Offset: 0x8
- Size: 0x4

<p>Address offset of the virtual memory region corresponding to the remote peer's memory.</p>

|Bits|Identifier|Access|Reset|                                 Name                                 |
|----|----------|------|-----|----------------------------------------------------------------------|
|31:0|  offset  |  rw  |  —  |csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].rmem_address.offset[31:0]|

#### offset field

<p>32-bit address offset of the virtual memory region corresponding to the remote peer's memory.</p>

### local_address register

- Absolute Address: 0x2000088C
- Base Offset: 0xC
- Size: 0x4

<p>Start address of the local memory region for DMA transfers.</p>

|Bits|Identifier|Access|Reset|                                 Name                                |
|----|----------|------|-----|---------------------------------------------------------------------|
|31:0|   base   |  rw  |  —  |csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].local_address.base[31:0]|

#### base field

<p>32-bit start address of the local memory region for DMA transfers.</p>

### remote_address register

- Absolute Address: 0x20000890
- Base Offset: 0x10
- Size: 0x4

<p>Start address of the remote peer's memory region.</p>

|Bits|Identifier|Access|Reset|                                 Name                                 |
|----|----------|------|-----|----------------------------------------------------------------------|
|31:0|   base   |  rw  |  —  |csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].remote_address.base[31:0]|

#### base field

<p>32-bit start address of the remote peer's memory region.</p>

### size register

- Absolute Address: 0x20000894
- Base Offset: 0x14
- Size: 0x4

<p>Size of the remote peer's memory region.</p>

|Bits|Identifier|Access|Reset|                             Name                            |
|----|----------|------|-----|-------------------------------------------------------------|
|31:0|   value  |  rw  |  —  |csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].size.value[31:0]|

#### value field

<p>32-bit size of the remote peer's memory region.</p>

### dma_config register

- Absolute Address: 0x20000898
- Base Offset: 0x18
- Size: 0x4

<p>DMA configuration for the remote peer.</p>

|Bits|Identifier|Access|Reset|                               Name                              |
|----|----------|------|-----|-----------------------------------------------------------------|
| 1:0|   mode   |  rw  |  —  |csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].dma_config.mode[1:0]|

#### mode field

<p>DMA mode for transfers to/from the remote peer:<ul></p>
<li>0: DMA transfers to/from the remote peer are disabled.</li>
<li>1: DMA transfers to/from the remote peer are enabled in transparent mode, where accesses to the virtual memory region are directly translated to corresponding accesses to the remote peer's memory region (transactions are word-by-word, i.e., per virtual memory access).</li>
<li>2: DMA transfers to/from the remote peer are enabled in mirror-to-local mode, where the local memory region is used instead of the virtual memory region. The state of the remote peer's memory region (remote_address, size) is fetched from the remote peer on demand or periodically.</li>
<li>3: DMA transfers to/from the remote peer are enabled in mirror-to-remote mode, where the remote memory region is used instead of the virtual memory region. The state of the local peer's memory region (local_address, size) is sent to the remote peer on demand or periodically.</li>
</ul>

## entry register file

- Absolute Address: 0x2000089C
- Base Offset: 0x0
- Size: 0x1C
- Array Dimensions: [4]
- Array Stride: 0x1C
- Total Size: 0x70

<p>Register file for a single remote peer configuration and memory region information.</p>

|Offset|  Identifier  |                            Name                           |
|------|--------------|-----------------------------------------------------------|
| 0x00 |  mac_address |  csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].mac_address |
| 0x08 | rmem_address | csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].rmem_address |
| 0x0C | local_address| csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].local_address|
| 0x10 |remote_address|csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].remote_address|
| 0x14 |     size     |     csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].size     |
| 0x18 |  dma_config  |  csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].dma_config  |

### mac_address register

- Absolute Address: 0x2000089C
- Base Offset: 0x0
- Size: 0x8

<p>Remote peer 48-bit destination MAC address.</p>

| Bits|Identifier|Access|Reset|                                  Name                                 |
|-----|----------|------|-----|-----------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address.</p>

### rmem_address register

- Absolute Address: 0x200008A4
- Base Offset: 0x8
- Size: 0x4

<p>Address offset of the virtual memory region corresponding to the remote peer's memory.</p>

|Bits|Identifier|Access|Reset|                                 Name                                 |
|----|----------|------|-----|----------------------------------------------------------------------|
|31:0|  offset  |  rw  |  —  |csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].rmem_address.offset[31:0]|

#### offset field

<p>32-bit address offset of the virtual memory region corresponding to the remote peer's memory.</p>

### local_address register

- Absolute Address: 0x200008A8
- Base Offset: 0xC
- Size: 0x4

<p>Start address of the local memory region for DMA transfers.</p>

|Bits|Identifier|Access|Reset|                                 Name                                |
|----|----------|------|-----|---------------------------------------------------------------------|
|31:0|   base   |  rw  |  —  |csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].local_address.base[31:0]|

#### base field

<p>32-bit start address of the local memory region for DMA transfers.</p>

### remote_address register

- Absolute Address: 0x200008AC
- Base Offset: 0x10
- Size: 0x4

<p>Start address of the remote peer's memory region.</p>

|Bits|Identifier|Access|Reset|                                 Name                                 |
|----|----------|------|-----|----------------------------------------------------------------------|
|31:0|   base   |  rw  |  —  |csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].remote_address.base[31:0]|

#### base field

<p>32-bit start address of the remote peer's memory region.</p>

### size register

- Absolute Address: 0x200008B0
- Base Offset: 0x14
- Size: 0x4

<p>Size of the remote peer's memory region.</p>

|Bits|Identifier|Access|Reset|                             Name                            |
|----|----------|------|-----|-------------------------------------------------------------|
|31:0|   value  |  rw  |  —  |csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].size.value[31:0]|

#### value field

<p>32-bit size of the remote peer's memory region.</p>

### dma_config register

- Absolute Address: 0x200008B4
- Base Offset: 0x18
- Size: 0x4

<p>DMA configuration for the remote peer.</p>

|Bits|Identifier|Access|Reset|                               Name                              |
|----|----------|------|-----|-----------------------------------------------------------------|
| 1:0|   mode   |  rw  |  —  |csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].dma_config.mode[1:0]|

#### mode field

<p>DMA mode for transfers to/from the remote peer:<ul></p>
<li>0: DMA transfers to/from the remote peer are disabled.</li>
<li>1: DMA transfers to/from the remote peer are enabled in transparent mode, where accesses to the virtual memory region are directly translated to corresponding accesses to the remote peer's memory region (transactions are word-by-word, i.e., per virtual memory access).</li>
<li>2: DMA transfers to/from the remote peer are enabled in mirror-to-local mode, where the local memory region is used instead of the virtual memory region. The state of the remote peer's memory region (remote_address, size) is fetched from the remote peer on demand or periodically.</li>
<li>3: DMA transfers to/from the remote peer are enabled in mirror-to-remote mode, where the remote memory region is used instead of the virtual memory region. The state of the local peer's memory region (local_address, size) is sent to the remote peer on demand or periodically.</li>
</ul>

## entry register file

- Absolute Address: 0x200008B8
- Base Offset: 0x0
- Size: 0x1C
- Array Dimensions: [4]
- Array Stride: 0x1C
- Total Size: 0x70

<p>Register file for a single remote peer configuration and memory region information.</p>

|Offset|  Identifier  |                            Name                           |
|------|--------------|-----------------------------------------------------------|
| 0x00 |  mac_address |  csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].mac_address |
| 0x08 | rmem_address | csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].rmem_address |
| 0x0C | local_address| csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].local_address|
| 0x10 |remote_address|csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].remote_address|
| 0x14 |     size     |     csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].size     |
| 0x18 |  dma_config  |  csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].dma_config  |

### mac_address register

- Absolute Address: 0x200008B8
- Base Offset: 0x0
- Size: 0x8

<p>Remote peer 48-bit destination MAC address.</p>

| Bits|Identifier|Access|Reset|                                  Name                                 |
|-----|----------|------|-----|-----------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address.</p>

### rmem_address register

- Absolute Address: 0x200008C0
- Base Offset: 0x8
- Size: 0x4

<p>Address offset of the virtual memory region corresponding to the remote peer's memory.</p>

|Bits|Identifier|Access|Reset|                                 Name                                 |
|----|----------|------|-----|----------------------------------------------------------------------|
|31:0|  offset  |  rw  |  —  |csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].rmem_address.offset[31:0]|

#### offset field

<p>32-bit address offset of the virtual memory region corresponding to the remote peer's memory.</p>

### local_address register

- Absolute Address: 0x200008C4
- Base Offset: 0xC
- Size: 0x4

<p>Start address of the local memory region for DMA transfers.</p>

|Bits|Identifier|Access|Reset|                                 Name                                |
|----|----------|------|-----|---------------------------------------------------------------------|
|31:0|   base   |  rw  |  —  |csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].local_address.base[31:0]|

#### base field

<p>32-bit start address of the local memory region for DMA transfers.</p>

### remote_address register

- Absolute Address: 0x200008C8
- Base Offset: 0x10
- Size: 0x4

<p>Start address of the remote peer's memory region.</p>

|Bits|Identifier|Access|Reset|                                 Name                                 |
|----|----------|------|-----|----------------------------------------------------------------------|
|31:0|   base   |  rw  |  —  |csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].remote_address.base[31:0]|

#### base field

<p>32-bit start address of the remote peer's memory region.</p>

### size register

- Absolute Address: 0x200008CC
- Base Offset: 0x14
- Size: 0x4

<p>Size of the remote peer's memory region.</p>

|Bits|Identifier|Access|Reset|                             Name                            |
|----|----------|------|-----|-------------------------------------------------------------|
|31:0|   value  |  rw  |  —  |csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].size.value[31:0]|

#### value field

<p>32-bit size of the remote peer's memory region.</p>

### dma_config register

- Absolute Address: 0x200008D0
- Base Offset: 0x18
- Size: 0x4

<p>DMA configuration for the remote peer.</p>

|Bits|Identifier|Access|Reset|                               Name                              |
|----|----------|------|-----|-----------------------------------------------------------------|
| 1:0|   mode   |  rw  |  —  |csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].dma_config.mode[1:0]|

#### mode field

<p>DMA mode for transfers to/from the remote peer:<ul></p>
<li>0: DMA transfers to/from the remote peer are disabled.</li>
<li>1: DMA transfers to/from the remote peer are enabled in transparent mode, where accesses to the virtual memory region are directly translated to corresponding accesses to the remote peer's memory region (transactions are word-by-word, i.e., per virtual memory access).</li>
<li>2: DMA transfers to/from the remote peer are enabled in mirror-to-local mode, where the local memory region is used instead of the virtual memory region. The state of the remote peer's memory region (remote_address, size) is fetched from the remote peer on demand or periodically.</li>
<li>3: DMA transfers to/from the remote peer are enabled in mirror-to-remote mode, where the remote memory region is used instead of the virtual memory region. The state of the local peer's memory region (local_address, size) is sent to the remote peer on demand or periodically.</li>
</ul>

## entry register file

- Absolute Address: 0x200008D4
- Base Offset: 0x0
- Size: 0x1C
- Array Dimensions: [4]
- Array Stride: 0x1C
- Total Size: 0x70

<p>Register file for a single remote peer configuration and memory region information.</p>

|Offset|  Identifier  |                            Name                           |
|------|--------------|-----------------------------------------------------------|
| 0x00 |  mac_address |  csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].mac_address |
| 0x08 | rmem_address | csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].rmem_address |
| 0x0C | local_address| csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].local_address|
| 0x10 |remote_address|csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].remote_address|
| 0x14 |     size     |     csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].size     |
| 0x18 |  dma_config  |  csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].dma_config  |

### mac_address register

- Absolute Address: 0x200008D4
- Base Offset: 0x0
- Size: 0x8

<p>Remote peer 48-bit destination MAC address.</p>

| Bits|Identifier|Access|Reset|                                  Name                                 |
|-----|----------|------|-----|-----------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address.</p>

### rmem_address register

- Absolute Address: 0x200008DC
- Base Offset: 0x8
- Size: 0x4

<p>Address offset of the virtual memory region corresponding to the remote peer's memory.</p>

|Bits|Identifier|Access|Reset|                                 Name                                 |
|----|----------|------|-----|----------------------------------------------------------------------|
|31:0|  offset  |  rw  |  —  |csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].rmem_address.offset[31:0]|

#### offset field

<p>32-bit address offset of the virtual memory region corresponding to the remote peer's memory.</p>

### local_address register

- Absolute Address: 0x200008E0
- Base Offset: 0xC
- Size: 0x4

<p>Start address of the local memory region for DMA transfers.</p>

|Bits|Identifier|Access|Reset|                                 Name                                |
|----|----------|------|-----|---------------------------------------------------------------------|
|31:0|   base   |  rw  |  —  |csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].local_address.base[31:0]|

#### base field

<p>32-bit start address of the local memory region for DMA transfers.</p>

### remote_address register

- Absolute Address: 0x200008E4
- Base Offset: 0x10
- Size: 0x4

<p>Start address of the remote peer's memory region.</p>

|Bits|Identifier|Access|Reset|                                 Name                                 |
|----|----------|------|-----|----------------------------------------------------------------------|
|31:0|   base   |  rw  |  —  |csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].remote_address.base[31:0]|

#### base field

<p>32-bit start address of the remote peer's memory region.</p>

### size register

- Absolute Address: 0x200008E8
- Base Offset: 0x14
- Size: 0x4

<p>Size of the remote peer's memory region.</p>

|Bits|Identifier|Access|Reset|                             Name                            |
|----|----------|------|-----|-------------------------------------------------------------|
|31:0|   value  |  rw  |  —  |csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].size.value[31:0]|

#### value field

<p>32-bit size of the remote peer's memory region.</p>

### dma_config register

- Absolute Address: 0x200008EC
- Base Offset: 0x18
- Size: 0x4

<p>DMA configuration for the remote peer.</p>

|Bits|Identifier|Access|Reset|                               Name                              |
|----|----------|------|-----|-----------------------------------------------------------------|
| 1:0|   mode   |  rw  |  —  |csr.endpoint1.peers.entry[0..NUM_OF_PEERS-1].dma_config.mode[1:0]|

#### mode field

<p>DMA mode for transfers to/from the remote peer:<ul></p>
<li>0: DMA transfers to/from the remote peer are disabled.</li>
<li>1: DMA transfers to/from the remote peer are enabled in transparent mode, where accesses to the virtual memory region are directly translated to corresponding accesses to the remote peer's memory region (transactions are word-by-word, i.e., per virtual memory access).</li>
<li>2: DMA transfers to/from the remote peer are enabled in mirror-to-local mode, where the local memory region is used instead of the virtual memory region. The state of the remote peer's memory region (remote_address, size) is fetched from the remote peer on demand or periodically.</li>
<li>3: DMA transfers to/from the remote peer are enabled in mirror-to-remote mode, where the remote memory region is used instead of the virtual memory region. The state of the local peer's memory region (local_address, size) is sent to the remote peer on demand or periodically.</li>
</ul>

## rmem memory

- Absolute Address: 0x20000C00
- Base Offset: 0x400
- Size: 0x400

<p>Virtual memory region for all remote peers, with offsets and sizes defined in the peers regfile.</p>

No supported members.


## endpoint2 address map

- Absolute Address: 0x20001000
- Base Offset: 0x1000
- Size: 0x400

<p>Control and status register map for an openENOC Endpoint Interface instance.</p>

|Offset|Identifier|        Name        |
|------|----------|--------------------|
| 0x000|   info   | csr.endpoint2.info |
| 0x008|  config  |csr.endpoint2.config|
| 0x040|   peers  | csr.endpoint2.peers|
| 0x200|   rmem   |        rmem        |

### info register

- Absolute Address: 0x20001000
- Base Offset: 0x0
- Size: 0x4

<p>Read-only information register for this openENOC Endpoint Interface instance.</p>

| Bits|   Identifier   |Access|Reset|                   Name                  |
|-----|----------------|------|-----|-----------------------------------------|
| 15:0|rmem_total_depth|   r  | 0x80|csr.endpoint2.info.rmem_total_depth[15:0]|
|31:16|  num_of_peers  |   r  | 0x2 |  csr.endpoint2.info.num_of_peers[31:16] |

#### rmem_total_depth field

<p>Total depth of the shared memory region for all remote peers. This field reflects the RMEM_TOTAL_DEPTH parameter value.</p>

#### num_of_peers field

<p>Number of remote peers supported by this openENOC Endpoint Interface instance. This field reflects the NUM_OF_PEERS parameter value.</p>

## config register file

- Absolute Address: 0x20001008
- Base Offset: 0x8
- Size: 0x8

<p>Configuration register file for this openENOC Endpoint Interface instance.</p>

|Offset| Identifier|              Name              |
|------|-----------|--------------------------------|
|  0x0 |mac_address|csr.endpoint2.config.mac_address|

### mac_address register

- Absolute Address: 0x20001008
- Base Offset: 0x0
- Size: 0x8

<p>Local site 48-bit destination MAC address.</p>

| Bits|Identifier|Access|Reset|                      Name                     |
|-----|----------|------|-----|-----------------------------------------------|
| 31:0|  lo_word |  rw  | 0x0 | csr.endpoint2.config.mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  | 0x0 |csr.endpoint2.config.mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address.</p>

## peers register file

- Absolute Address: 0x20001040
- Base Offset: 0x40
- Size: 0x38

<p>Register file for remote peer configuration and memory region information.</p>

|Offset|Identifier|                    Name                    |
|------|----------|--------------------------------------------|
| 0x00 | entry[0] |csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1]|
| 0x1C | entry[1] |csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1]|

## entry register file

- Absolute Address: 0x20001040
- Base Offset: 0x0
- Size: 0x1C
- Array Dimensions: [2]
- Array Stride: 0x1C
- Total Size: 0x38

<p>Register file for a single remote peer configuration and memory region information.</p>

|Offset|  Identifier  |                            Name                           |
|------|--------------|-----------------------------------------------------------|
| 0x00 |  mac_address |  csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].mac_address |
| 0x08 | rmem_address | csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].rmem_address |
| 0x0C | local_address| csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].local_address|
| 0x10 |remote_address|csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].remote_address|
| 0x14 |     size     |     csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].size     |
| 0x18 |  dma_config  |  csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].dma_config  |

### mac_address register

- Absolute Address: 0x20001040
- Base Offset: 0x0
- Size: 0x8

<p>Remote peer 48-bit destination MAC address.</p>

| Bits|Identifier|Access|Reset|                                  Name                                 |
|-----|----------|------|-----|-----------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address.</p>

### rmem_address register

- Absolute Address: 0x20001048
- Base Offset: 0x8
- Size: 0x4

<p>Address offset of the virtual memory region corresponding to the remote peer's memory.</p>

|Bits|Identifier|Access|Reset|                                 Name                                 |
|----|----------|------|-----|----------------------------------------------------------------------|
|31:0|  offset  |  rw  |  —  |csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].rmem_address.offset[31:0]|

#### offset field

<p>32-bit address offset of the virtual memory region corresponding to the remote peer's memory.</p>

### local_address register

- Absolute Address: 0x2000104C
- Base Offset: 0xC
- Size: 0x4

<p>Start address of the local memory region for DMA transfers.</p>

|Bits|Identifier|Access|Reset|                                 Name                                |
|----|----------|------|-----|---------------------------------------------------------------------|
|31:0|   base   |  rw  |  —  |csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].local_address.base[31:0]|

#### base field

<p>32-bit start address of the local memory region for DMA transfers.</p>

### remote_address register

- Absolute Address: 0x20001050
- Base Offset: 0x10
- Size: 0x4

<p>Start address of the remote peer's memory region.</p>

|Bits|Identifier|Access|Reset|                                 Name                                 |
|----|----------|------|-----|----------------------------------------------------------------------|
|31:0|   base   |  rw  |  —  |csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].remote_address.base[31:0]|

#### base field

<p>32-bit start address of the remote peer's memory region.</p>

### size register

- Absolute Address: 0x20001054
- Base Offset: 0x14
- Size: 0x4

<p>Size of the remote peer's memory region.</p>

|Bits|Identifier|Access|Reset|                             Name                            |
|----|----------|------|-----|-------------------------------------------------------------|
|31:0|   value  |  rw  |  —  |csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].size.value[31:0]|

#### value field

<p>32-bit size of the remote peer's memory region.</p>

### dma_config register

- Absolute Address: 0x20001058
- Base Offset: 0x18
- Size: 0x4

<p>DMA configuration for the remote peer.</p>

|Bits|Identifier|Access|Reset|                               Name                              |
|----|----------|------|-----|-----------------------------------------------------------------|
| 1:0|   mode   |  rw  |  —  |csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].dma_config.mode[1:0]|

#### mode field

<p>DMA mode for transfers to/from the remote peer:<ul></p>
<li>0: DMA transfers to/from the remote peer are disabled.</li>
<li>1: DMA transfers to/from the remote peer are enabled in transparent mode, where accesses to the virtual memory region are directly translated to corresponding accesses to the remote peer's memory region (transactions are word-by-word, i.e., per virtual memory access).</li>
<li>2: DMA transfers to/from the remote peer are enabled in mirror-to-local mode, where the local memory region is used instead of the virtual memory region. The state of the remote peer's memory region (remote_address, size) is fetched from the remote peer on demand or periodically.</li>
<li>3: DMA transfers to/from the remote peer are enabled in mirror-to-remote mode, where the remote memory region is used instead of the virtual memory region. The state of the local peer's memory region (local_address, size) is sent to the remote peer on demand or periodically.</li>
</ul>

## entry register file

- Absolute Address: 0x2000105C
- Base Offset: 0x0
- Size: 0x1C
- Array Dimensions: [2]
- Array Stride: 0x1C
- Total Size: 0x38

<p>Register file for a single remote peer configuration and memory region information.</p>

|Offset|  Identifier  |                            Name                           |
|------|--------------|-----------------------------------------------------------|
| 0x00 |  mac_address |  csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].mac_address |
| 0x08 | rmem_address | csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].rmem_address |
| 0x0C | local_address| csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].local_address|
| 0x10 |remote_address|csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].remote_address|
| 0x14 |     size     |     csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].size     |
| 0x18 |  dma_config  |  csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].dma_config  |

### mac_address register

- Absolute Address: 0x2000105C
- Base Offset: 0x0
- Size: 0x8

<p>Remote peer 48-bit destination MAC address.</p>

| Bits|Identifier|Access|Reset|                                  Name                                 |
|-----|----------|------|-----|-----------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address.</p>

### rmem_address register

- Absolute Address: 0x20001064
- Base Offset: 0x8
- Size: 0x4

<p>Address offset of the virtual memory region corresponding to the remote peer's memory.</p>

|Bits|Identifier|Access|Reset|                                 Name                                 |
|----|----------|------|-----|----------------------------------------------------------------------|
|31:0|  offset  |  rw  |  —  |csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].rmem_address.offset[31:0]|

#### offset field

<p>32-bit address offset of the virtual memory region corresponding to the remote peer's memory.</p>

### local_address register

- Absolute Address: 0x20001068
- Base Offset: 0xC
- Size: 0x4

<p>Start address of the local memory region for DMA transfers.</p>

|Bits|Identifier|Access|Reset|                                 Name                                |
|----|----------|------|-----|---------------------------------------------------------------------|
|31:0|   base   |  rw  |  —  |csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].local_address.base[31:0]|

#### base field

<p>32-bit start address of the local memory region for DMA transfers.</p>

### remote_address register

- Absolute Address: 0x2000106C
- Base Offset: 0x10
- Size: 0x4

<p>Start address of the remote peer's memory region.</p>

|Bits|Identifier|Access|Reset|                                 Name                                 |
|----|----------|------|-----|----------------------------------------------------------------------|
|31:0|   base   |  rw  |  —  |csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].remote_address.base[31:0]|

#### base field

<p>32-bit start address of the remote peer's memory region.</p>

### size register

- Absolute Address: 0x20001070
- Base Offset: 0x14
- Size: 0x4

<p>Size of the remote peer's memory region.</p>

|Bits|Identifier|Access|Reset|                             Name                            |
|----|----------|------|-----|-------------------------------------------------------------|
|31:0|   value  |  rw  |  —  |csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].size.value[31:0]|

#### value field

<p>32-bit size of the remote peer's memory region.</p>

### dma_config register

- Absolute Address: 0x20001074
- Base Offset: 0x18
- Size: 0x4

<p>DMA configuration for the remote peer.</p>

|Bits|Identifier|Access|Reset|                               Name                              |
|----|----------|------|-----|-----------------------------------------------------------------|
| 1:0|   mode   |  rw  |  —  |csr.endpoint2.peers.entry[0..NUM_OF_PEERS-1].dma_config.mode[1:0]|

#### mode field

<p>DMA mode for transfers to/from the remote peer:<ul></p>
<li>0: DMA transfers to/from the remote peer are disabled.</li>
<li>1: DMA transfers to/from the remote peer are enabled in transparent mode, where accesses to the virtual memory region are directly translated to corresponding accesses to the remote peer's memory region (transactions are word-by-word, i.e., per virtual memory access).</li>
<li>2: DMA transfers to/from the remote peer are enabled in mirror-to-local mode, where the local memory region is used instead of the virtual memory region. The state of the remote peer's memory region (remote_address, size) is fetched from the remote peer on demand or periodically.</li>
<li>3: DMA transfers to/from the remote peer are enabled in mirror-to-remote mode, where the remote memory region is used instead of the virtual memory region. The state of the local peer's memory region (local_address, size) is sent to the remote peer on demand or periodically.</li>
</ul>

## rmem memory

- Absolute Address: 0x20001200
- Base Offset: 0x200
- Size: 0x200

<p>Virtual memory region for all remote peers, with offsets and sizes defined in the peers regfile.</p>

No supported members.


## switch1 address map

- Absolute Address: 0x20001400
- Base Offset: 0x1400
- Size: 0x100

<p>Control and status register map for an openENOC Switch instance. It includes configuration registers and a forwarding table used to map destination MAC address keys to output interface selections for frame forwarding.</p>

|Offset|    Identifier    |             Name             |
|------|------------------|------------------------------|
| 0x00 |       info       |       csr.switch1.info       |
| 0x04 |forwarding_control|csr.switch1.forwarding_control|
| 0x08 |default_forwarding|csr.switch1.default_forwarding|
| 0x80 | forwarding_table | csr.switch1.forwarding_table |

### info register

- Absolute Address: 0x20001400
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

- Absolute Address: 0x20001404
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

- Absolute Address: 0x20001408
- Base Offset: 0x8
- Size: 0x4

<p>Defines the destination interface or interfaces for frames that do not match any enabled forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                            Name                            |
|----|----------|------|-----|------------------------------------------------------------|
| 3:0|  bitmap  |  rw  | 0x0 |csr.switch1.default_forwarding.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which frames that do not match any enabled forwarding table entry are forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

## forwarding_table register file

- Absolute Address: 0x20001480
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

- Absolute Address: 0x20001480
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [8]
- Array Stride: 0x10
- Total Size: 0x80

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset| Identifier|                              Name                              |
|------|-----------|----------------------------------------------------------------|
|  0x0 |mac_address|csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address|
|  0x8 |   iface   |   csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].iface   |
|  0xC |   config  |   csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].config  |

### mac_address register

- Absolute Address: 0x20001480
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x20001488
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 3:0|  bitmap  |  rw  |  —  |csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x2000148C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x20001490
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [8]
- Array Stride: 0x10
- Total Size: 0x80

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset| Identifier|                              Name                              |
|------|-----------|----------------------------------------------------------------|
|  0x0 |mac_address|csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address|
|  0x8 |   iface   |   csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].iface   |
|  0xC |   config  |   csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].config  |

### mac_address register

- Absolute Address: 0x20001490
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x20001498
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 3:0|  bitmap  |  rw  |  —  |csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x2000149C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x200014A0
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [8]
- Array Stride: 0x10
- Total Size: 0x80

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset| Identifier|                              Name                              |
|------|-----------|----------------------------------------------------------------|
|  0x0 |mac_address|csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address|
|  0x8 |   iface   |   csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].iface   |
|  0xC |   config  |   csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].config  |

### mac_address register

- Absolute Address: 0x200014A0
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x200014A8
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 3:0|  bitmap  |  rw  |  —  |csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x200014AC
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x200014B0
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [8]
- Array Stride: 0x10
- Total Size: 0x80

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset| Identifier|                              Name                              |
|------|-----------|----------------------------------------------------------------|
|  0x0 |mac_address|csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address|
|  0x8 |   iface   |   csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].iface   |
|  0xC |   config  |   csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].config  |

### mac_address register

- Absolute Address: 0x200014B0
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x200014B8
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 3:0|  bitmap  |  rw  |  —  |csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x200014BC
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x200014C0
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [8]
- Array Stride: 0x10
- Total Size: 0x80

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset| Identifier|                              Name                              |
|------|-----------|----------------------------------------------------------------|
|  0x0 |mac_address|csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address|
|  0x8 |   iface   |   csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].iface   |
|  0xC |   config  |   csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].config  |

### mac_address register

- Absolute Address: 0x200014C0
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x200014C8
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 3:0|  bitmap  |  rw  |  —  |csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x200014CC
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x200014D0
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [8]
- Array Stride: 0x10
- Total Size: 0x80

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset| Identifier|                              Name                              |
|------|-----------|----------------------------------------------------------------|
|  0x0 |mac_address|csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address|
|  0x8 |   iface   |   csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].iface   |
|  0xC |   config  |   csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].config  |

### mac_address register

- Absolute Address: 0x200014D0
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x200014D8
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 3:0|  bitmap  |  rw  |  —  |csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x200014DC
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x200014E0
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [8]
- Array Stride: 0x10
- Total Size: 0x80

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset| Identifier|                              Name                              |
|------|-----------|----------------------------------------------------------------|
|  0x0 |mac_address|csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address|
|  0x8 |   iface   |   csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].iface   |
|  0xC |   config  |   csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].config  |

### mac_address register

- Absolute Address: 0x200014E0
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x200014E8
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 3:0|  bitmap  |  rw  |  —  |csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x200014EC
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x200014F0
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [8]
- Array Stride: 0x10
- Total Size: 0x80

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset| Identifier|                              Name                              |
|------|-----------|----------------------------------------------------------------|
|  0x0 |mac_address|csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address|
|  0x8 |   iface   |   csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].iface   |
|  0xC |   config  |   csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].config  |

### mac_address register

- Absolute Address: 0x200014F0
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x200014F8
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 3:0|  bitmap  |  rw  |  —  |csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x200014FC
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch1.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## switch2 address map

- Absolute Address: 0x20001800
- Base Offset: 0x1800
- Size: 0x400

<p>Control and status register map for an openENOC Switch instance. It includes configuration registers and a forwarding table used to map destination MAC address keys to output interface selections for frame forwarding.</p>

|Offset|    Identifier    |             Name             |
|------|------------------|------------------------------|
| 0x000|       info       |       csr.switch2.info       |
| 0x004|forwarding_control|csr.switch2.forwarding_control|
| 0x008|default_forwarding|csr.switch2.default_forwarding|
| 0x200| forwarding_table | csr.switch2.forwarding_table |

### info register

- Absolute Address: 0x20001800
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

- Absolute Address: 0x20001804
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

- Absolute Address: 0x20001808
- Base Offset: 0x8
- Size: 0x4

<p>Defines the destination interface or interfaces for frames that do not match any enabled forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                            Name                            |
|----|----------|------|-----|------------------------------------------------------------|
| 7:0|  bitmap  |  rw  | 0x0 |csr.switch2.default_forwarding.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which frames that do not match any enabled forwarding table entry are forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

## forwarding_table register file

- Absolute Address: 0x20001A00
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

- Absolute Address: 0x20001A00
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset| Identifier|                              Name                              |
|------|-----------|----------------------------------------------------------------|
|  0x0 |mac_address|csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address|
|  0x8 |   iface   |   csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface   |
|  0xC |   config  |   csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config  |

### mac_address register

- Absolute Address: 0x20001A00
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x20001A08
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x20001A0C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x20001A10
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset| Identifier|                              Name                              |
|------|-----------|----------------------------------------------------------------|
|  0x0 |mac_address|csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address|
|  0x8 |   iface   |   csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface   |
|  0xC |   config  |   csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config  |

### mac_address register

- Absolute Address: 0x20001A10
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x20001A18
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x20001A1C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x20001A20
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset| Identifier|                              Name                              |
|------|-----------|----------------------------------------------------------------|
|  0x0 |mac_address|csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address|
|  0x8 |   iface   |   csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface   |
|  0xC |   config  |   csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config  |

### mac_address register

- Absolute Address: 0x20001A20
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x20001A28
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x20001A2C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x20001A30
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset| Identifier|                              Name                              |
|------|-----------|----------------------------------------------------------------|
|  0x0 |mac_address|csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address|
|  0x8 |   iface   |   csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface   |
|  0xC |   config  |   csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config  |

### mac_address register

- Absolute Address: 0x20001A30
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x20001A38
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x20001A3C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x20001A40
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset| Identifier|                              Name                              |
|------|-----------|----------------------------------------------------------------|
|  0x0 |mac_address|csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address|
|  0x8 |   iface   |   csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface   |
|  0xC |   config  |   csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config  |

### mac_address register

- Absolute Address: 0x20001A40
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x20001A48
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x20001A4C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x20001A50
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset| Identifier|                              Name                              |
|------|-----------|----------------------------------------------------------------|
|  0x0 |mac_address|csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address|
|  0x8 |   iface   |   csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface   |
|  0xC |   config  |   csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config  |

### mac_address register

- Absolute Address: 0x20001A50
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x20001A58
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x20001A5C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x20001A60
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset| Identifier|                              Name                              |
|------|-----------|----------------------------------------------------------------|
|  0x0 |mac_address|csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address|
|  0x8 |   iface   |   csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface   |
|  0xC |   config  |   csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config  |

### mac_address register

- Absolute Address: 0x20001A60
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x20001A68
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x20001A6C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x20001A70
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset| Identifier|                              Name                              |
|------|-----------|----------------------------------------------------------------|
|  0x0 |mac_address|csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address|
|  0x8 |   iface   |   csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface   |
|  0xC |   config  |   csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config  |

### mac_address register

- Absolute Address: 0x20001A70
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x20001A78
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x20001A7C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x20001A80
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset| Identifier|                              Name                              |
|------|-----------|----------------------------------------------------------------|
|  0x0 |mac_address|csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address|
|  0x8 |   iface   |   csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface   |
|  0xC |   config  |   csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config  |

### mac_address register

- Absolute Address: 0x20001A80
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x20001A88
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x20001A8C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x20001A90
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset| Identifier|                              Name                              |
|------|-----------|----------------------------------------------------------------|
|  0x0 |mac_address|csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address|
|  0x8 |   iface   |   csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface   |
|  0xC |   config  |   csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config  |

### mac_address register

- Absolute Address: 0x20001A90
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x20001A98
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x20001A9C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x20001AA0
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset| Identifier|                              Name                              |
|------|-----------|----------------------------------------------------------------|
|  0x0 |mac_address|csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address|
|  0x8 |   iface   |   csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface   |
|  0xC |   config  |   csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config  |

### mac_address register

- Absolute Address: 0x20001AA0
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x20001AA8
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x20001AAC
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x20001AB0
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset| Identifier|                              Name                              |
|------|-----------|----------------------------------------------------------------|
|  0x0 |mac_address|csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address|
|  0x8 |   iface   |   csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface   |
|  0xC |   config  |   csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config  |

### mac_address register

- Absolute Address: 0x20001AB0
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x20001AB8
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x20001ABC
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x20001AC0
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset| Identifier|                              Name                              |
|------|-----------|----------------------------------------------------------------|
|  0x0 |mac_address|csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address|
|  0x8 |   iface   |   csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface   |
|  0xC |   config  |   csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config  |

### mac_address register

- Absolute Address: 0x20001AC0
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x20001AC8
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x20001ACC
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x20001AD0
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset| Identifier|                              Name                              |
|------|-----------|----------------------------------------------------------------|
|  0x0 |mac_address|csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address|
|  0x8 |   iface   |   csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface   |
|  0xC |   config  |   csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config  |

### mac_address register

- Absolute Address: 0x20001AD0
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x20001AD8
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x20001ADC
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x20001AE0
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset| Identifier|                              Name                              |
|------|-----------|----------------------------------------------------------------|
|  0x0 |mac_address|csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address|
|  0x8 |   iface   |   csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface   |
|  0xC |   config  |   csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config  |

### mac_address register

- Absolute Address: 0x20001AE0
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x20001AE8
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x20001AEC
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x20001AF0
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset| Identifier|                              Name                              |
|------|-----------|----------------------------------------------------------------|
|  0x0 |mac_address|csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address|
|  0x8 |   iface   |   csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface   |
|  0xC |   config  |   csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config  |

### mac_address register

- Absolute Address: 0x20001AF0
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x20001AF8
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x20001AFC
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x20001B00
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset| Identifier|                              Name                              |
|------|-----------|----------------------------------------------------------------|
|  0x0 |mac_address|csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address|
|  0x8 |   iface   |   csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface   |
|  0xC |   config  |   csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config  |

### mac_address register

- Absolute Address: 0x20001B00
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x20001B08
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x20001B0C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x20001B10
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset| Identifier|                              Name                              |
|------|-----------|----------------------------------------------------------------|
|  0x0 |mac_address|csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address|
|  0x8 |   iface   |   csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface   |
|  0xC |   config  |   csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config  |

### mac_address register

- Absolute Address: 0x20001B10
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x20001B18
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x20001B1C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x20001B20
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset| Identifier|                              Name                              |
|------|-----------|----------------------------------------------------------------|
|  0x0 |mac_address|csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address|
|  0x8 |   iface   |   csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface   |
|  0xC |   config  |   csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config  |

### mac_address register

- Absolute Address: 0x20001B20
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x20001B28
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x20001B2C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x20001B30
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset| Identifier|                              Name                              |
|------|-----------|----------------------------------------------------------------|
|  0x0 |mac_address|csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address|
|  0x8 |   iface   |   csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface   |
|  0xC |   config  |   csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config  |

### mac_address register

- Absolute Address: 0x20001B30
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x20001B38
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x20001B3C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x20001B40
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset| Identifier|                              Name                              |
|------|-----------|----------------------------------------------------------------|
|  0x0 |mac_address|csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address|
|  0x8 |   iface   |   csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface   |
|  0xC |   config  |   csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config  |

### mac_address register

- Absolute Address: 0x20001B40
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x20001B48
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x20001B4C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x20001B50
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset| Identifier|                              Name                              |
|------|-----------|----------------------------------------------------------------|
|  0x0 |mac_address|csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address|
|  0x8 |   iface   |   csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface   |
|  0xC |   config  |   csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config  |

### mac_address register

- Absolute Address: 0x20001B50
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x20001B58
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x20001B5C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x20001B60
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset| Identifier|                              Name                              |
|------|-----------|----------------------------------------------------------------|
|  0x0 |mac_address|csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address|
|  0x8 |   iface   |   csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface   |
|  0xC |   config  |   csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config  |

### mac_address register

- Absolute Address: 0x20001B60
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x20001B68
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x20001B6C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x20001B70
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset| Identifier|                              Name                              |
|------|-----------|----------------------------------------------------------------|
|  0x0 |mac_address|csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address|
|  0x8 |   iface   |   csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface   |
|  0xC |   config  |   csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config  |

### mac_address register

- Absolute Address: 0x20001B70
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x20001B78
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x20001B7C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x20001B80
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset| Identifier|                              Name                              |
|------|-----------|----------------------------------------------------------------|
|  0x0 |mac_address|csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address|
|  0x8 |   iface   |   csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface   |
|  0xC |   config  |   csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config  |

### mac_address register

- Absolute Address: 0x20001B80
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x20001B88
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x20001B8C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x20001B90
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset| Identifier|                              Name                              |
|------|-----------|----------------------------------------------------------------|
|  0x0 |mac_address|csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address|
|  0x8 |   iface   |   csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface   |
|  0xC |   config  |   csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config  |

### mac_address register

- Absolute Address: 0x20001B90
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x20001B98
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x20001B9C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x20001BA0
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset| Identifier|                              Name                              |
|------|-----------|----------------------------------------------------------------|
|  0x0 |mac_address|csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address|
|  0x8 |   iface   |   csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface   |
|  0xC |   config  |   csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config  |

### mac_address register

- Absolute Address: 0x20001BA0
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x20001BA8
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x20001BAC
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x20001BB0
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset| Identifier|                              Name                              |
|------|-----------|----------------------------------------------------------------|
|  0x0 |mac_address|csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address|
|  0x8 |   iface   |   csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface   |
|  0xC |   config  |   csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config  |

### mac_address register

- Absolute Address: 0x20001BB0
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x20001BB8
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x20001BBC
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x20001BC0
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset| Identifier|                              Name                              |
|------|-----------|----------------------------------------------------------------|
|  0x0 |mac_address|csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address|
|  0x8 |   iface   |   csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface   |
|  0xC |   config  |   csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config  |

### mac_address register

- Absolute Address: 0x20001BC0
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x20001BC8
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x20001BCC
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x20001BD0
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset| Identifier|                              Name                              |
|------|-----------|----------------------------------------------------------------|
|  0x0 |mac_address|csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address|
|  0x8 |   iface   |   csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface   |
|  0xC |   config  |   csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config  |

### mac_address register

- Absolute Address: 0x20001BD0
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x20001BD8
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x20001BDC
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x20001BE0
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset| Identifier|                              Name                              |
|------|-----------|----------------------------------------------------------------|
|  0x0 |mac_address|csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address|
|  0x8 |   iface   |   csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface   |
|  0xC |   config  |   csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config  |

### mac_address register

- Absolute Address: 0x20001BE0
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x20001BE8
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x20001BEC
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x20001BF0
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [32]
- Array Stride: 0x10
- Total Size: 0x200

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset| Identifier|                              Name                              |
|------|-----------|----------------------------------------------------------------|
|  0x0 |mac_address|csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address|
|  0x8 |   iface   |   csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface   |
|  0xC |   config  |   csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config  |

### mac_address register

- Absolute Address: 0x20001BF0
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                      Name                                     |
|-----|----------|------|-----|-------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x20001BF8
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                          Name                                          |
|----|----------|------|-----|----------------------------------------------------------------------------------------|
| 7:0|  bitmap  |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x20001BFC
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                Name                               |
|----|----------|------|-----|-------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch2.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>
