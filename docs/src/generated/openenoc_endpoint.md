<!---
Markdown description for SystemRDL register map.

Don't override. Generated from: openenoc_endpoint
  - /home/enio/Projects/openENOC/hal/src/openenoc.rdl
-->

## openenoc_endpoint address map

- Absolute Address: 0x0
- Base Offset: 0x0
- Size: 0x800

<p>Control and status register map for an openENOC Endpoint Interface instance.</p>

|Offset|Identifier|          Name          |
|------|----------|------------------------|
| 0x000|   info   | openenoc_endpoint.info |
| 0x008|  config  |openenoc_endpoint.config|
| 0x080|   peers  | openenoc_endpoint.peers|
| 0x400|   rmem   |          rmem          |

### info register

- Absolute Address: 0x0
- Base Offset: 0x0
- Size: 0x4

<p>Read-only information register for this openENOC Endpoint Interface instance.</p>

| Bits|   Identifier   |Access|Reset|                     Name                    |
|-----|----------------|------|-----|---------------------------------------------|
| 15:0|rmem_total_depth|   r  |0x100|openenoc_endpoint.info.rmem_total_depth[15:0]|
|31:16|  num_of_peers  |   r  | 0x4 |  openenoc_endpoint.info.num_of_peers[31:16] |

#### rmem_total_depth field

<p>Total depth of the shared memory region for all remote peers. This field reflects the RMEM_TOTAL_DEPTH parameter value.</p>

#### num_of_peers field

<p>Number of remote peers supported by this openENOC Endpoint Interface instance. This field reflects the NUM_OF_PEERS parameter value.</p>

## config register file

- Absolute Address: 0x8
- Base Offset: 0x8
- Size: 0x8

<p>Configuration register file for this openENOC Endpoint Interface instance.</p>

|Offset| Identifier|                Name                |
|------|-----------|------------------------------------|
|  0x0 |mac_address|openenoc_endpoint.config.mac_address|

### mac_address register

- Absolute Address: 0x8
- Base Offset: 0x0
- Size: 0x8

<p>Local site 48-bit destination MAC address.</p>

| Bits|Identifier|Access|Reset|                        Name                       |
|-----|----------|------|-----|---------------------------------------------------|
| 31:0|  lo_word |  rw  | 0x0 | openenoc_endpoint.config.mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  | 0x0 |openenoc_endpoint.config.mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address.</p>

## peers register file

- Absolute Address: 0x80
- Base Offset: 0x80
- Size: 0x70

<p>Register file for remote peer configuration and memory region information.</p>

|Offset|Identifier|                      Name                      |
|------|----------|------------------------------------------------|
| 0x00 | entry[0] |openenoc_endpoint.peers.entry[0..NUM_OF_PEERS-1]|
| 0x1C | entry[1] |openenoc_endpoint.peers.entry[0..NUM_OF_PEERS-1]|
| 0x38 | entry[2] |openenoc_endpoint.peers.entry[0..NUM_OF_PEERS-1]|
| 0x54 | entry[3] |openenoc_endpoint.peers.entry[0..NUM_OF_PEERS-1]|

## entry register file

- Absolute Address: 0x80
- Base Offset: 0x0
- Size: 0x1C
- Array Dimensions: [4]
- Array Stride: 0x1C
- Total Size: 0x70

<p>Register file for a single remote peer configuration and memory region information.</p>

|Offset|  Identifier  |                              Name                             |
|------|--------------|---------------------------------------------------------------|
| 0x00 |  mac_address |  openenoc_endpoint.peers.entry[0..NUM_OF_PEERS-1].mac_address |
| 0x08 | rmem_address | openenoc_endpoint.peers.entry[0..NUM_OF_PEERS-1].rmem_address |
| 0x0C | local_address| openenoc_endpoint.peers.entry[0..NUM_OF_PEERS-1].local_address|
| 0x10 |remote_address|openenoc_endpoint.peers.entry[0..NUM_OF_PEERS-1].remote_address|
| 0x14 |     size     |     openenoc_endpoint.peers.entry[0..NUM_OF_PEERS-1].size     |
| 0x18 |  dma_config  |  openenoc_endpoint.peers.entry[0..NUM_OF_PEERS-1].dma_config  |

### mac_address register

- Absolute Address: 0x80
- Base Offset: 0x0
- Size: 0x8

<p>Remote peer 48-bit destination MAC address.</p>

| Bits|Identifier|Access|Reset|                                    Name                                   |
|-----|----------|------|-----|---------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | openenoc_endpoint.peers.entry[0..NUM_OF_PEERS-1].mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |openenoc_endpoint.peers.entry[0..NUM_OF_PEERS-1].mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address.</p>

### rmem_address register

- Absolute Address: 0x88
- Base Offset: 0x8
- Size: 0x4

<p>Address offset of the virtual memory region corresponding to the remote peer's memory.</p>

|Bits|Identifier|Access|Reset|                                   Name                                   |
|----|----------|------|-----|--------------------------------------------------------------------------|
|31:0|  offset  |  rw  |  —  |openenoc_endpoint.peers.entry[0..NUM_OF_PEERS-1].rmem_address.offset[31:0]|

#### offset field

<p>32-bit address offset of the virtual memory region corresponding to the remote peer's memory.</p>

### local_address register

- Absolute Address: 0x8C
- Base Offset: 0xC
- Size: 0x4

<p>Start address of the local memory region for DMA transfers.</p>

|Bits|Identifier|Access|Reset|                                   Name                                  |
|----|----------|------|-----|-------------------------------------------------------------------------|
|31:0|   base   |  rw  |  —  |openenoc_endpoint.peers.entry[0..NUM_OF_PEERS-1].local_address.base[31:0]|

#### base field

<p>32-bit start address of the local memory region for DMA transfers.</p>

### remote_address register

- Absolute Address: 0x90
- Base Offset: 0x10
- Size: 0x4

<p>Start address of the remote peer's memory region.</p>

|Bits|Identifier|Access|Reset|                                   Name                                   |
|----|----------|------|-----|--------------------------------------------------------------------------|
|31:0|   base   |  rw  |  —  |openenoc_endpoint.peers.entry[0..NUM_OF_PEERS-1].remote_address.base[31:0]|

#### base field

<p>32-bit start address of the remote peer's memory region.</p>

### size register

- Absolute Address: 0x94
- Base Offset: 0x14
- Size: 0x4

<p>Size of the remote peer's memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                              |
|----|----------|------|-----|-----------------------------------------------------------------|
|31:0|   value  |  rw  |  —  |openenoc_endpoint.peers.entry[0..NUM_OF_PEERS-1].size.value[31:0]|

#### value field

<p>32-bit size of the remote peer's memory region.</p>

### dma_config register

- Absolute Address: 0x98
- Base Offset: 0x18
- Size: 0x4

<p>DMA configuration for the remote peer.</p>

|Bits|Identifier|Access|Reset|                                 Name                                |
|----|----------|------|-----|---------------------------------------------------------------------|
| 1:0|   mode   |  rw  |  —  |openenoc_endpoint.peers.entry[0..NUM_OF_PEERS-1].dma_config.mode[1:0]|

#### mode field

<p>DMA mode for transfers to/from the remote peer:<ul></p>
<li>0: DMA transfers to/from the remote peer are disabled.</li>
<li>1: DMA transfers to/from the remote peer are enabled in transparent mode, where accesses to the virtual memory region are directly translated to corresponding accesses to the remote peer's memory region (transactions are word-by-word, i.e., per virtual memory access).</li>
<li>2: DMA transfers to/from the remote peer are enabled in mirror-to-local mode, where the local memory region is used instead of the virtual memory region. The state of the remote peer's memory region (remote_address, size) is fetched from the remote peer on demand or periodically.</li>
<li>3: DMA transfers to/from the remote peer are enabled in mirror-to-remote mode, where the remote memory region is used instead of the virtual memory region. The state of the local peer's memory region (local_address, size) is sent to the remote peer on demand or periodically.</li>
</ul>

## entry register file

- Absolute Address: 0x9C
- Base Offset: 0x0
- Size: 0x1C
- Array Dimensions: [4]
- Array Stride: 0x1C
- Total Size: 0x70

<p>Register file for a single remote peer configuration and memory region information.</p>

|Offset|  Identifier  |                              Name                             |
|------|--------------|---------------------------------------------------------------|
| 0x00 |  mac_address |  openenoc_endpoint.peers.entry[0..NUM_OF_PEERS-1].mac_address |
| 0x08 | rmem_address | openenoc_endpoint.peers.entry[0..NUM_OF_PEERS-1].rmem_address |
| 0x0C | local_address| openenoc_endpoint.peers.entry[0..NUM_OF_PEERS-1].local_address|
| 0x10 |remote_address|openenoc_endpoint.peers.entry[0..NUM_OF_PEERS-1].remote_address|
| 0x14 |     size     |     openenoc_endpoint.peers.entry[0..NUM_OF_PEERS-1].size     |
| 0x18 |  dma_config  |  openenoc_endpoint.peers.entry[0..NUM_OF_PEERS-1].dma_config  |

### mac_address register

- Absolute Address: 0x9C
- Base Offset: 0x0
- Size: 0x8

<p>Remote peer 48-bit destination MAC address.</p>

| Bits|Identifier|Access|Reset|                                    Name                                   |
|-----|----------|------|-----|---------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | openenoc_endpoint.peers.entry[0..NUM_OF_PEERS-1].mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |openenoc_endpoint.peers.entry[0..NUM_OF_PEERS-1].mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address.</p>

### rmem_address register

- Absolute Address: 0xA4
- Base Offset: 0x8
- Size: 0x4

<p>Address offset of the virtual memory region corresponding to the remote peer's memory.</p>

|Bits|Identifier|Access|Reset|                                   Name                                   |
|----|----------|------|-----|--------------------------------------------------------------------------|
|31:0|  offset  |  rw  |  —  |openenoc_endpoint.peers.entry[0..NUM_OF_PEERS-1].rmem_address.offset[31:0]|

#### offset field

<p>32-bit address offset of the virtual memory region corresponding to the remote peer's memory.</p>

### local_address register

- Absolute Address: 0xA8
- Base Offset: 0xC
- Size: 0x4

<p>Start address of the local memory region for DMA transfers.</p>

|Bits|Identifier|Access|Reset|                                   Name                                  |
|----|----------|------|-----|-------------------------------------------------------------------------|
|31:0|   base   |  rw  |  —  |openenoc_endpoint.peers.entry[0..NUM_OF_PEERS-1].local_address.base[31:0]|

#### base field

<p>32-bit start address of the local memory region for DMA transfers.</p>

### remote_address register

- Absolute Address: 0xAC
- Base Offset: 0x10
- Size: 0x4

<p>Start address of the remote peer's memory region.</p>

|Bits|Identifier|Access|Reset|                                   Name                                   |
|----|----------|------|-----|--------------------------------------------------------------------------|
|31:0|   base   |  rw  |  —  |openenoc_endpoint.peers.entry[0..NUM_OF_PEERS-1].remote_address.base[31:0]|

#### base field

<p>32-bit start address of the remote peer's memory region.</p>

### size register

- Absolute Address: 0xB0
- Base Offset: 0x14
- Size: 0x4

<p>Size of the remote peer's memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                              |
|----|----------|------|-----|-----------------------------------------------------------------|
|31:0|   value  |  rw  |  —  |openenoc_endpoint.peers.entry[0..NUM_OF_PEERS-1].size.value[31:0]|

#### value field

<p>32-bit size of the remote peer's memory region.</p>

### dma_config register

- Absolute Address: 0xB4
- Base Offset: 0x18
- Size: 0x4

<p>DMA configuration for the remote peer.</p>

|Bits|Identifier|Access|Reset|                                 Name                                |
|----|----------|------|-----|---------------------------------------------------------------------|
| 1:0|   mode   |  rw  |  —  |openenoc_endpoint.peers.entry[0..NUM_OF_PEERS-1].dma_config.mode[1:0]|

#### mode field

<p>DMA mode for transfers to/from the remote peer:<ul></p>
<li>0: DMA transfers to/from the remote peer are disabled.</li>
<li>1: DMA transfers to/from the remote peer are enabled in transparent mode, where accesses to the virtual memory region are directly translated to corresponding accesses to the remote peer's memory region (transactions are word-by-word, i.e., per virtual memory access).</li>
<li>2: DMA transfers to/from the remote peer are enabled in mirror-to-local mode, where the local memory region is used instead of the virtual memory region. The state of the remote peer's memory region (remote_address, size) is fetched from the remote peer on demand or periodically.</li>
<li>3: DMA transfers to/from the remote peer are enabled in mirror-to-remote mode, where the remote memory region is used instead of the virtual memory region. The state of the local peer's memory region (local_address, size) is sent to the remote peer on demand or periodically.</li>
</ul>

## entry register file

- Absolute Address: 0xB8
- Base Offset: 0x0
- Size: 0x1C
- Array Dimensions: [4]
- Array Stride: 0x1C
- Total Size: 0x70

<p>Register file for a single remote peer configuration and memory region information.</p>

|Offset|  Identifier  |                              Name                             |
|------|--------------|---------------------------------------------------------------|
| 0x00 |  mac_address |  openenoc_endpoint.peers.entry[0..NUM_OF_PEERS-1].mac_address |
| 0x08 | rmem_address | openenoc_endpoint.peers.entry[0..NUM_OF_PEERS-1].rmem_address |
| 0x0C | local_address| openenoc_endpoint.peers.entry[0..NUM_OF_PEERS-1].local_address|
| 0x10 |remote_address|openenoc_endpoint.peers.entry[0..NUM_OF_PEERS-1].remote_address|
| 0x14 |     size     |     openenoc_endpoint.peers.entry[0..NUM_OF_PEERS-1].size     |
| 0x18 |  dma_config  |  openenoc_endpoint.peers.entry[0..NUM_OF_PEERS-1].dma_config  |

### mac_address register

- Absolute Address: 0xB8
- Base Offset: 0x0
- Size: 0x8

<p>Remote peer 48-bit destination MAC address.</p>

| Bits|Identifier|Access|Reset|                                    Name                                   |
|-----|----------|------|-----|---------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | openenoc_endpoint.peers.entry[0..NUM_OF_PEERS-1].mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |openenoc_endpoint.peers.entry[0..NUM_OF_PEERS-1].mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address.</p>

### rmem_address register

- Absolute Address: 0xC0
- Base Offset: 0x8
- Size: 0x4

<p>Address offset of the virtual memory region corresponding to the remote peer's memory.</p>

|Bits|Identifier|Access|Reset|                                   Name                                   |
|----|----------|------|-----|--------------------------------------------------------------------------|
|31:0|  offset  |  rw  |  —  |openenoc_endpoint.peers.entry[0..NUM_OF_PEERS-1].rmem_address.offset[31:0]|

#### offset field

<p>32-bit address offset of the virtual memory region corresponding to the remote peer's memory.</p>

### local_address register

- Absolute Address: 0xC4
- Base Offset: 0xC
- Size: 0x4

<p>Start address of the local memory region for DMA transfers.</p>

|Bits|Identifier|Access|Reset|                                   Name                                  |
|----|----------|------|-----|-------------------------------------------------------------------------|
|31:0|   base   |  rw  |  —  |openenoc_endpoint.peers.entry[0..NUM_OF_PEERS-1].local_address.base[31:0]|

#### base field

<p>32-bit start address of the local memory region for DMA transfers.</p>

### remote_address register

- Absolute Address: 0xC8
- Base Offset: 0x10
- Size: 0x4

<p>Start address of the remote peer's memory region.</p>

|Bits|Identifier|Access|Reset|                                   Name                                   |
|----|----------|------|-----|--------------------------------------------------------------------------|
|31:0|   base   |  rw  |  —  |openenoc_endpoint.peers.entry[0..NUM_OF_PEERS-1].remote_address.base[31:0]|

#### base field

<p>32-bit start address of the remote peer's memory region.</p>

### size register

- Absolute Address: 0xCC
- Base Offset: 0x14
- Size: 0x4

<p>Size of the remote peer's memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                              |
|----|----------|------|-----|-----------------------------------------------------------------|
|31:0|   value  |  rw  |  —  |openenoc_endpoint.peers.entry[0..NUM_OF_PEERS-1].size.value[31:0]|

#### value field

<p>32-bit size of the remote peer's memory region.</p>

### dma_config register

- Absolute Address: 0xD0
- Base Offset: 0x18
- Size: 0x4

<p>DMA configuration for the remote peer.</p>

|Bits|Identifier|Access|Reset|                                 Name                                |
|----|----------|------|-----|---------------------------------------------------------------------|
| 1:0|   mode   |  rw  |  —  |openenoc_endpoint.peers.entry[0..NUM_OF_PEERS-1].dma_config.mode[1:0]|

#### mode field

<p>DMA mode for transfers to/from the remote peer:<ul></p>
<li>0: DMA transfers to/from the remote peer are disabled.</li>
<li>1: DMA transfers to/from the remote peer are enabled in transparent mode, where accesses to the virtual memory region are directly translated to corresponding accesses to the remote peer's memory region (transactions are word-by-word, i.e., per virtual memory access).</li>
<li>2: DMA transfers to/from the remote peer are enabled in mirror-to-local mode, where the local memory region is used instead of the virtual memory region. The state of the remote peer's memory region (remote_address, size) is fetched from the remote peer on demand or periodically.</li>
<li>3: DMA transfers to/from the remote peer are enabled in mirror-to-remote mode, where the remote memory region is used instead of the virtual memory region. The state of the local peer's memory region (local_address, size) is sent to the remote peer on demand or periodically.</li>
</ul>

## entry register file

- Absolute Address: 0xD4
- Base Offset: 0x0
- Size: 0x1C
- Array Dimensions: [4]
- Array Stride: 0x1C
- Total Size: 0x70

<p>Register file for a single remote peer configuration and memory region information.</p>

|Offset|  Identifier  |                              Name                             |
|------|--------------|---------------------------------------------------------------|
| 0x00 |  mac_address |  openenoc_endpoint.peers.entry[0..NUM_OF_PEERS-1].mac_address |
| 0x08 | rmem_address | openenoc_endpoint.peers.entry[0..NUM_OF_PEERS-1].rmem_address |
| 0x0C | local_address| openenoc_endpoint.peers.entry[0..NUM_OF_PEERS-1].local_address|
| 0x10 |remote_address|openenoc_endpoint.peers.entry[0..NUM_OF_PEERS-1].remote_address|
| 0x14 |     size     |     openenoc_endpoint.peers.entry[0..NUM_OF_PEERS-1].size     |
| 0x18 |  dma_config  |  openenoc_endpoint.peers.entry[0..NUM_OF_PEERS-1].dma_config  |

### mac_address register

- Absolute Address: 0xD4
- Base Offset: 0x0
- Size: 0x8

<p>Remote peer 48-bit destination MAC address.</p>

| Bits|Identifier|Access|Reset|                                    Name                                   |
|-----|----------|------|-----|---------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | openenoc_endpoint.peers.entry[0..NUM_OF_PEERS-1].mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |openenoc_endpoint.peers.entry[0..NUM_OF_PEERS-1].mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address.</p>

### rmem_address register

- Absolute Address: 0xDC
- Base Offset: 0x8
- Size: 0x4

<p>Address offset of the virtual memory region corresponding to the remote peer's memory.</p>

|Bits|Identifier|Access|Reset|                                   Name                                   |
|----|----------|------|-----|--------------------------------------------------------------------------|
|31:0|  offset  |  rw  |  —  |openenoc_endpoint.peers.entry[0..NUM_OF_PEERS-1].rmem_address.offset[31:0]|

#### offset field

<p>32-bit address offset of the virtual memory region corresponding to the remote peer's memory.</p>

### local_address register

- Absolute Address: 0xE0
- Base Offset: 0xC
- Size: 0x4

<p>Start address of the local memory region for DMA transfers.</p>

|Bits|Identifier|Access|Reset|                                   Name                                  |
|----|----------|------|-----|-------------------------------------------------------------------------|
|31:0|   base   |  rw  |  —  |openenoc_endpoint.peers.entry[0..NUM_OF_PEERS-1].local_address.base[31:0]|

#### base field

<p>32-bit start address of the local memory region for DMA transfers.</p>

### remote_address register

- Absolute Address: 0xE4
- Base Offset: 0x10
- Size: 0x4

<p>Start address of the remote peer's memory region.</p>

|Bits|Identifier|Access|Reset|                                   Name                                   |
|----|----------|------|-----|--------------------------------------------------------------------------|
|31:0|   base   |  rw  |  —  |openenoc_endpoint.peers.entry[0..NUM_OF_PEERS-1].remote_address.base[31:0]|

#### base field

<p>32-bit start address of the remote peer's memory region.</p>

### size register

- Absolute Address: 0xE8
- Base Offset: 0x14
- Size: 0x4

<p>Size of the remote peer's memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                              |
|----|----------|------|-----|-----------------------------------------------------------------|
|31:0|   value  |  rw  |  —  |openenoc_endpoint.peers.entry[0..NUM_OF_PEERS-1].size.value[31:0]|

#### value field

<p>32-bit size of the remote peer's memory region.</p>

### dma_config register

- Absolute Address: 0xEC
- Base Offset: 0x18
- Size: 0x4

<p>DMA configuration for the remote peer.</p>

|Bits|Identifier|Access|Reset|                                 Name                                |
|----|----------|------|-----|---------------------------------------------------------------------|
| 1:0|   mode   |  rw  |  —  |openenoc_endpoint.peers.entry[0..NUM_OF_PEERS-1].dma_config.mode[1:0]|

#### mode field

<p>DMA mode for transfers to/from the remote peer:<ul></p>
<li>0: DMA transfers to/from the remote peer are disabled.</li>
<li>1: DMA transfers to/from the remote peer are enabled in transparent mode, where accesses to the virtual memory region are directly translated to corresponding accesses to the remote peer's memory region (transactions are word-by-word, i.e., per virtual memory access).</li>
<li>2: DMA transfers to/from the remote peer are enabled in mirror-to-local mode, where the local memory region is used instead of the virtual memory region. The state of the remote peer's memory region (remote_address, size) is fetched from the remote peer on demand or periodically.</li>
<li>3: DMA transfers to/from the remote peer are enabled in mirror-to-remote mode, where the remote memory region is used instead of the virtual memory region. The state of the local peer's memory region (local_address, size) is sent to the remote peer on demand or periodically.</li>
</ul>

## rmem memory

- Absolute Address: 0x400
- Base Offset: 0x400
- Size: 0x400

<p>Virtual memory region for all remote peers, with offsets and sizes defined in the peers regfile.</p>

No supported members.

