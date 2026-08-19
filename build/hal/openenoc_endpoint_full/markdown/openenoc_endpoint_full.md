<!---
Markdown description for SystemRDL register map.

Don't override. Generated from: openenoc_endpoint_full
  - /home/enio/Projects/openENOC/hal/endpoints/openenoc_endpoint_full.rdl
-->

## openenoc_endpoint_full address map

- Absolute Address: 0x0
- Base Offset: 0x0
- Size: 0x20001100

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
- Size: 0x1100

<p>openENOC Full Endpoint CSR</p>

|Offset|    Identifier    |         Name         |
|------|------------------|----------------------|
|0x0000|     test_reg     |     csr.test_reg     |
|0x0004|       regB       |           —          |
|0x0800|endpoint_interface|csr.endpoint_interface|
|0x1000| switch_interface | csr.switch_interface |

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

## endpoint_interface register file

- Absolute Address: 0x20000800
- Base Offset: 0x800
- Size: 0x800

<p>Control and status register file for an openENOC Endpoint Interface instance.</p>

|Offset|Identifier|             Name             |
|------|----------|------------------------------|
| 0x000|   info   |  csr.endpoint_interface.info |
| 0x008|  config  | csr.endpoint_interface.config|
| 0x020|  axis_if |csr.endpoint_interface.axis_if|
| 0x080|   peers  | csr.endpoint_interface.peers |
| 0x400|   rmem   |  csr.endpoint_interface.rmem |

### info register

- Absolute Address: 0x20000800
- Base Offset: 0x0
- Size: 0x8

<p>Read-only information register for this openENOC Endpoint Interface instance.</p>

| Bits|   Identifier   |Access|Reset|                       Name                       |
|-----|----------------|------|-----|--------------------------------------------------|
| 31:0|rmem_total_depth|   r  |0x100|csr.endpoint_interface.info.rmem_total_depth[15:0]|
|63:32|  num_of_peers  |   r  | 0x4 |  csr.endpoint_interface.info.num_of_peers[31:16] |

#### rmem_total_depth field

<p>Total depth of the shared memory region for all remote peers. This field reflects the RMEM_TOTAL_DEPTH parameter value.</p>

#### num_of_peers field

<p>Number of remote peers supported by this openENOC Endpoint Interface instance. This field reflects the NUM_OF_PEERS parameter value.</p>

## config register file

- Absolute Address: 0x20000808
- Base Offset: 0x8
- Size: 0x8

<p>Configuration register file for this openENOC Endpoint Interface instance.</p>

|Offset| Identifier|                   Name                  |
|------|-----------|-----------------------------------------|
|  0x0 |mac_address|csr.endpoint_interface.config.mac_address|

### mac_address register

- Absolute Address: 0x20000808
- Base Offset: 0x0
- Size: 0x8

<p>Local site 48-bit destination MAC address.</p>

| Bits|Identifier|Access|Reset|                          Name                          |
|-----|----------|------|-----|--------------------------------------------------------|
| 31:0|  lo_word |  rw  | 0x0 | csr.endpoint_interface.config.mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  | 0x0 |csr.endpoint_interface.config.mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address.</p>

## axis_if register file

- Absolute Address: 0x20000820
- Base Offset: 0x20
- Size: 0x1C

<p>Register file for the AXI4-Stream source and sink interfaces.</p>

|Offset|Identifier|                 Name                |
|------|----------|-------------------------------------|
| 0x00 |  source  |csr.endpoint_interface.axis_if.source|
| 0x10 |   sink   | csr.endpoint_interface.axis_if.sink |

## source register file

- Absolute Address: 0x20000820
- Base Offset: 0x0
- Size: 0xC

<p>Register file for the AXI4-Stream source interface.</p>

|Offset|Identifier|                     Name                    |
|------|----------|---------------------------------------------|
|  0x0 |   data   |  csr.endpoint_interface.axis_if.source.data |
|  0x4 |  control |csr.endpoint_interface.axis_if.source.control|
|  0x8 |  status  | csr.endpoint_interface.axis_if.source.status|

### data register

- Absolute Address: 0x20000820
- Base Offset: 0x0
- Size: 0x4

<p>Data register for the AXI4-Stream source interface.</p>

|Bits|Identifier|Access|Reset|                         Name                         |
|----|----------|------|-----|------------------------------------------------------|
|31:0|   tdata  |  rw  | 0x0 |csr.endpoint_interface.axis_if.source.data.tdata[31:0]|

#### tdata field

<p>32-bit data value for the AXI4-Stream source interface.</p>

### control register

- Absolute Address: 0x20000824
- Base Offset: 0x4
- Size: 0x4

<p>Control register for the AXI4-Stream source interface.</p>

|Bits|Identifier|Access|Reset|                        Name                        |
|----|----------|------|-----|----------------------------------------------------|
|  0 |  tvalid  |  rw  | 0x0 |csr.endpoint_interface.axis_if.source.control.tvalid|
|  8 |   tlast  |  rw  | 0x0 | csr.endpoint_interface.axis_if.source.control.tlast|

#### tvalid field

<p>Indicates that the AXI4-Stream source interface has valid data to send. This field is a single-pulse register that is automatically cleared back to zero after being written.</p>

#### tlast field

<p>Indicates the last data word of a frame on the AXI4-Stream source interface.</p>

### status register

- Absolute Address: 0x20000828
- Base Offset: 0x8
- Size: 0x4

<p>Status register for the AXI4-Stream source interface.</p>

|Bits|Identifier|Access|Reset|                        Name                       |
|----|----------|------|-----|---------------------------------------------------|
|  0 |  tready  |   r  | 0x0 |csr.endpoint_interface.axis_if.source.status.tready|

#### tready field

<p>Indicates that the destination AXI4-Stream interface is ready to receive data.</p>

## sink register file

- Absolute Address: 0x20000830
- Base Offset: 0x10
- Size: 0xC

<p>Register file for the AXI4-Stream sink interface.</p>

|Offset|Identifier|                    Name                   |
|------|----------|-------------------------------------------|
|  0x0 |   data   |  csr.endpoint_interface.axis_if.sink.data |
|  0x4 |  control |csr.endpoint_interface.axis_if.sink.control|
|  0x8 |  status  | csr.endpoint_interface.axis_if.sink.status|

### data register

- Absolute Address: 0x20000830
- Base Offset: 0x0
- Size: 0x4

<p>Data register for the AXI4-Stream sink interface.</p>

|Bits|Identifier|Access|Reset|                        Name                        |
|----|----------|------|-----|----------------------------------------------------|
|31:0|   tdata  |   r  |  —  |csr.endpoint_interface.axis_if.sink.data.tdata[31:0]|

#### tdata field

<p>32-bit data value for the AXI4-Stream sink interface.</p>

### control register

- Absolute Address: 0x20000834
- Base Offset: 0x4
- Size: 0x4

<p>Control register for the AXI4-Stream sink interface.</p>

|Bits|Identifier|Access|Reset|                       Name                       |
|----|----------|------|-----|--------------------------------------------------|
|  0 |  tready  |   w  | 0x0 |csr.endpoint_interface.axis_if.sink.control.tready|

#### tready field

<p>Indicates that the AXI4-Stream sink interface is ready to receive next data transfer.</p>

### status register

- Absolute Address: 0x20000838
- Base Offset: 0x8
- Size: 0x4

<p>Status register for the AXI4-Stream sink interface.</p>

|Bits|Identifier|Access|Reset|                       Name                      |
|----|----------|------|-----|-------------------------------------------------|
|  0 |  tvalid  |   r  |  —  |csr.endpoint_interface.axis_if.sink.status.tvalid|
|  8 |   tlast  |   r  |  —  | csr.endpoint_interface.axis_if.sink.status.tlast|

#### tvalid field

<p>Indicates that the AXI4-Stream sink interface has valid data to receive.</p>

#### tlast field

<p>Indicates the last data word of a frame on the AXI4-Stream sink interface.</p>

## peers register file

- Absolute Address: 0x20000880
- Base Offset: 0x80
- Size: 0x70

<p>Register file for remote peer configuration and memory region information.</p>

|Offset|Identifier|                         Name                        |
|------|----------|-----------------------------------------------------|
| 0x00 | entry[0] |csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1]|
| 0x1C | entry[1] |csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1]|
| 0x38 | entry[2] |csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1]|
| 0x54 | entry[3] |csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1]|

## entry register file

- Absolute Address: 0x20000880
- Base Offset: 0x0
- Size: 0x1C
- Array Dimensions: [4]
- Array Stride: 0x1C
- Total Size: 0x70

<p>Register file for a single remote peer configuration and memory region information.</p>

|Offset|  Identifier  |                                Name                                |
|------|--------------|--------------------------------------------------------------------|
| 0x00 |  mac_address |  csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].mac_address |
| 0x08 | rmem_address | csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].rmem_address |
| 0x0C | local_address| csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].local_address|
| 0x10 |remote_address|csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].remote_address|
| 0x14 |     size     |     csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].size     |
| 0x18 |      dma     |      csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma     |

### mac_address register

- Absolute Address: 0x20000880
- Base Offset: 0x0
- Size: 0x8

<p>Remote peer 48-bit destination MAC address.</p>

| Bits|Identifier|Access|Reset|                                      Name                                      |
|-----|----------|------|-----|--------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address.</p>

### rmem_address register

- Absolute Address: 0x20000888
- Base Offset: 0x8
- Size: 0x4

<p>Address offset of the virtual memory region corresponding to the remote peer's memory.</p>

|Bits|Identifier|Access|Reset|                                      Name                                     |
|----|----------|------|-----|-------------------------------------------------------------------------------|
|31:0|  offset  |  rw  |  —  |csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].rmem_address.offset[31:0]|

#### offset field

<p>Word-aligned 32-bit address offset of the virtual memory region corresponding to the remote peer's memory.</p>

### local_address register

- Absolute Address: 0x2000088C
- Base Offset: 0xC
- Size: 0x4

<p>Start address of the local memory region for DMA transfers.</p>

|Bits|Identifier|Access|Reset|                                     Name                                     |
|----|----------|------|-----|------------------------------------------------------------------------------|
|31:0|   base   |  rw  |  —  |csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].local_address.base[31:0]|

#### base field

<p>Word-aligned 32-bit start address of the local memory region for DMA transfers.</p>

### remote_address register

- Absolute Address: 0x20000890
- Base Offset: 0x10
- Size: 0x4

<p>Start address of the remote peer's memory region.</p>

|Bits|Identifier|Access|Reset|                                      Name                                     |
|----|----------|------|-----|-------------------------------------------------------------------------------|
|31:0|   base   |  rw  |  —  |csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].remote_address.base[31:0]|

#### base field

<p>Word-aligned 32-bit start address of the remote peer's memory region.</p>

### size register

- Absolute Address: 0x20000894
- Base Offset: 0x14
- Size: 0x4

<p>Size of the remote peer's memory region.</p>

|Bits|Identifier|Access|Reset|                                 Name                                 |
|----|----------|------|-----|----------------------------------------------------------------------|
|31:0|   bytes  |  rw  |  —  |csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].size.bytes[31:0]|

#### bytes field

<p>32-bit size of the remote peer's memory region in bytes.</p>

### dma register

- Absolute Address: 0x20000898
- Base Offset: 0x18
- Size: 0x4

<p>DMA configuration and control for the remote peer.</p>

|Bits|Identifier|Access|Reset|                                 Name                                 |
|----|----------|------|-----|----------------------------------------------------------------------|
| 1:0|   mode   |  rw  |  —  |  csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.mode[1:0] |
|  8 |  request |  rw  | 0x0 |csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.request[8:8]|
| 16 |   idle   |   r  |  —  | csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.idle[16:16]|
| 24 |   done   |   r  |  —  | csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.done[24:24]|
| 25 |   error  |   r  |  —  |csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.error[25:25]|

#### mode field

<p>DMA mode for transfers to/from the remote peer:<ul></p>
<li>0: DMA transfers to/from the remote peer are disabled.</li>
<li>1: DMA transfers to/from the remote peer are enabled in transparent mode, where accesses to the virtual memory region are directly translated to corresponding accesses to the remote peer's memory region (transactions are word-by-word, i.e., per virtual memory access).</li>
<li>2: DMA transfers to/from the remote peer are enabled in mirror-to-local mode, where the local memory region is used instead of the virtual memory region. The state of the remote peer's memory region (remote_address, size) is fetched from the remote peer on demand or periodically.</li>
<li>3: DMA transfers to/from the remote peer are enabled in mirror-to-remote mode, where the remote memory region is used instead of the virtual memory region. The state of the local peer's memory region (local_address, size) is sent to the remote peer on demand or periodically.</li>
</ul>

#### request field

<p>Writing a 1 to this field initiates a DMA transfer to/from the remote peer. This field is a single-pulse register that is automatically cleared back to zero after being written.</p>

#### idle field

<p>Indicates whether the DMA transfer to/from the remote peer is idle. A value of 1 indicates that the DMA transfer is idle, while a value of 0 indicates that the DMA transfer is in progress.</p>

#### done field

<p>Indicates whether the DMA transfer to/from the remote peer has been successful. A value of 1 indicates that the DMA transfer has completed successfully, while a value of 0 indicates that the DMA transfer is still in progress or has encountered an error.</p>

#### error field

<p>Indicates whether the DMA transfer to/from the remote peer has encountered an error. A value of 1 indicates an error, while a value of 0 indicates no error.</p>

## entry register file

- Absolute Address: 0x2000089C
- Base Offset: 0x0
- Size: 0x1C
- Array Dimensions: [4]
- Array Stride: 0x1C
- Total Size: 0x70

<p>Register file for a single remote peer configuration and memory region information.</p>

|Offset|  Identifier  |                                Name                                |
|------|--------------|--------------------------------------------------------------------|
| 0x00 |  mac_address |  csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].mac_address |
| 0x08 | rmem_address | csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].rmem_address |
| 0x0C | local_address| csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].local_address|
| 0x10 |remote_address|csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].remote_address|
| 0x14 |     size     |     csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].size     |
| 0x18 |      dma     |      csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma     |

### mac_address register

- Absolute Address: 0x2000089C
- Base Offset: 0x0
- Size: 0x8

<p>Remote peer 48-bit destination MAC address.</p>

| Bits|Identifier|Access|Reset|                                      Name                                      |
|-----|----------|------|-----|--------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address.</p>

### rmem_address register

- Absolute Address: 0x200008A4
- Base Offset: 0x8
- Size: 0x4

<p>Address offset of the virtual memory region corresponding to the remote peer's memory.</p>

|Bits|Identifier|Access|Reset|                                      Name                                     |
|----|----------|------|-----|-------------------------------------------------------------------------------|
|31:0|  offset  |  rw  |  —  |csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].rmem_address.offset[31:0]|

#### offset field

<p>Word-aligned 32-bit address offset of the virtual memory region corresponding to the remote peer's memory.</p>

### local_address register

- Absolute Address: 0x200008A8
- Base Offset: 0xC
- Size: 0x4

<p>Start address of the local memory region for DMA transfers.</p>

|Bits|Identifier|Access|Reset|                                     Name                                     |
|----|----------|------|-----|------------------------------------------------------------------------------|
|31:0|   base   |  rw  |  —  |csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].local_address.base[31:0]|

#### base field

<p>Word-aligned 32-bit start address of the local memory region for DMA transfers.</p>

### remote_address register

- Absolute Address: 0x200008AC
- Base Offset: 0x10
- Size: 0x4

<p>Start address of the remote peer's memory region.</p>

|Bits|Identifier|Access|Reset|                                      Name                                     |
|----|----------|------|-----|-------------------------------------------------------------------------------|
|31:0|   base   |  rw  |  —  |csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].remote_address.base[31:0]|

#### base field

<p>Word-aligned 32-bit start address of the remote peer's memory region.</p>

### size register

- Absolute Address: 0x200008B0
- Base Offset: 0x14
- Size: 0x4

<p>Size of the remote peer's memory region.</p>

|Bits|Identifier|Access|Reset|                                 Name                                 |
|----|----------|------|-----|----------------------------------------------------------------------|
|31:0|   bytes  |  rw  |  —  |csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].size.bytes[31:0]|

#### bytes field

<p>32-bit size of the remote peer's memory region in bytes.</p>

### dma register

- Absolute Address: 0x200008B4
- Base Offset: 0x18
- Size: 0x4

<p>DMA configuration and control for the remote peer.</p>

|Bits|Identifier|Access|Reset|                                 Name                                 |
|----|----------|------|-----|----------------------------------------------------------------------|
| 1:0|   mode   |  rw  |  —  |  csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.mode[1:0] |
|  8 |  request |  rw  | 0x0 |csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.request[8:8]|
| 16 |   idle   |   r  |  —  | csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.idle[16:16]|
| 24 |   done   |   r  |  —  | csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.done[24:24]|
| 25 |   error  |   r  |  —  |csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.error[25:25]|

#### mode field

<p>DMA mode for transfers to/from the remote peer:<ul></p>
<li>0: DMA transfers to/from the remote peer are disabled.</li>
<li>1: DMA transfers to/from the remote peer are enabled in transparent mode, where accesses to the virtual memory region are directly translated to corresponding accesses to the remote peer's memory region (transactions are word-by-word, i.e., per virtual memory access).</li>
<li>2: DMA transfers to/from the remote peer are enabled in mirror-to-local mode, where the local memory region is used instead of the virtual memory region. The state of the remote peer's memory region (remote_address, size) is fetched from the remote peer on demand or periodically.</li>
<li>3: DMA transfers to/from the remote peer are enabled in mirror-to-remote mode, where the remote memory region is used instead of the virtual memory region. The state of the local peer's memory region (local_address, size) is sent to the remote peer on demand or periodically.</li>
</ul>

#### request field

<p>Writing a 1 to this field initiates a DMA transfer to/from the remote peer. This field is a single-pulse register that is automatically cleared back to zero after being written.</p>

#### idle field

<p>Indicates whether the DMA transfer to/from the remote peer is idle. A value of 1 indicates that the DMA transfer is idle, while a value of 0 indicates that the DMA transfer is in progress.</p>

#### done field

<p>Indicates whether the DMA transfer to/from the remote peer has been successful. A value of 1 indicates that the DMA transfer has completed successfully, while a value of 0 indicates that the DMA transfer is still in progress or has encountered an error.</p>

#### error field

<p>Indicates whether the DMA transfer to/from the remote peer has encountered an error. A value of 1 indicates an error, while a value of 0 indicates no error.</p>

## entry register file

- Absolute Address: 0x200008B8
- Base Offset: 0x0
- Size: 0x1C
- Array Dimensions: [4]
- Array Stride: 0x1C
- Total Size: 0x70

<p>Register file for a single remote peer configuration and memory region information.</p>

|Offset|  Identifier  |                                Name                                |
|------|--------------|--------------------------------------------------------------------|
| 0x00 |  mac_address |  csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].mac_address |
| 0x08 | rmem_address | csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].rmem_address |
| 0x0C | local_address| csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].local_address|
| 0x10 |remote_address|csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].remote_address|
| 0x14 |     size     |     csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].size     |
| 0x18 |      dma     |      csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma     |

### mac_address register

- Absolute Address: 0x200008B8
- Base Offset: 0x0
- Size: 0x8

<p>Remote peer 48-bit destination MAC address.</p>

| Bits|Identifier|Access|Reset|                                      Name                                      |
|-----|----------|------|-----|--------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address.</p>

### rmem_address register

- Absolute Address: 0x200008C0
- Base Offset: 0x8
- Size: 0x4

<p>Address offset of the virtual memory region corresponding to the remote peer's memory.</p>

|Bits|Identifier|Access|Reset|                                      Name                                     |
|----|----------|------|-----|-------------------------------------------------------------------------------|
|31:0|  offset  |  rw  |  —  |csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].rmem_address.offset[31:0]|

#### offset field

<p>Word-aligned 32-bit address offset of the virtual memory region corresponding to the remote peer's memory.</p>

### local_address register

- Absolute Address: 0x200008C4
- Base Offset: 0xC
- Size: 0x4

<p>Start address of the local memory region for DMA transfers.</p>

|Bits|Identifier|Access|Reset|                                     Name                                     |
|----|----------|------|-----|------------------------------------------------------------------------------|
|31:0|   base   |  rw  |  —  |csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].local_address.base[31:0]|

#### base field

<p>Word-aligned 32-bit start address of the local memory region for DMA transfers.</p>

### remote_address register

- Absolute Address: 0x200008C8
- Base Offset: 0x10
- Size: 0x4

<p>Start address of the remote peer's memory region.</p>

|Bits|Identifier|Access|Reset|                                      Name                                     |
|----|----------|------|-----|-------------------------------------------------------------------------------|
|31:0|   base   |  rw  |  —  |csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].remote_address.base[31:0]|

#### base field

<p>Word-aligned 32-bit start address of the remote peer's memory region.</p>

### size register

- Absolute Address: 0x200008CC
- Base Offset: 0x14
- Size: 0x4

<p>Size of the remote peer's memory region.</p>

|Bits|Identifier|Access|Reset|                                 Name                                 |
|----|----------|------|-----|----------------------------------------------------------------------|
|31:0|   bytes  |  rw  |  —  |csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].size.bytes[31:0]|

#### bytes field

<p>32-bit size of the remote peer's memory region in bytes.</p>

### dma register

- Absolute Address: 0x200008D0
- Base Offset: 0x18
- Size: 0x4

<p>DMA configuration and control for the remote peer.</p>

|Bits|Identifier|Access|Reset|                                 Name                                 |
|----|----------|------|-----|----------------------------------------------------------------------|
| 1:0|   mode   |  rw  |  —  |  csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.mode[1:0] |
|  8 |  request |  rw  | 0x0 |csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.request[8:8]|
| 16 |   idle   |   r  |  —  | csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.idle[16:16]|
| 24 |   done   |   r  |  —  | csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.done[24:24]|
| 25 |   error  |   r  |  —  |csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.error[25:25]|

#### mode field

<p>DMA mode for transfers to/from the remote peer:<ul></p>
<li>0: DMA transfers to/from the remote peer are disabled.</li>
<li>1: DMA transfers to/from the remote peer are enabled in transparent mode, where accesses to the virtual memory region are directly translated to corresponding accesses to the remote peer's memory region (transactions are word-by-word, i.e., per virtual memory access).</li>
<li>2: DMA transfers to/from the remote peer are enabled in mirror-to-local mode, where the local memory region is used instead of the virtual memory region. The state of the remote peer's memory region (remote_address, size) is fetched from the remote peer on demand or periodically.</li>
<li>3: DMA transfers to/from the remote peer are enabled in mirror-to-remote mode, where the remote memory region is used instead of the virtual memory region. The state of the local peer's memory region (local_address, size) is sent to the remote peer on demand or periodically.</li>
</ul>

#### request field

<p>Writing a 1 to this field initiates a DMA transfer to/from the remote peer. This field is a single-pulse register that is automatically cleared back to zero after being written.</p>

#### idle field

<p>Indicates whether the DMA transfer to/from the remote peer is idle. A value of 1 indicates that the DMA transfer is idle, while a value of 0 indicates that the DMA transfer is in progress.</p>

#### done field

<p>Indicates whether the DMA transfer to/from the remote peer has been successful. A value of 1 indicates that the DMA transfer has completed successfully, while a value of 0 indicates that the DMA transfer is still in progress or has encountered an error.</p>

#### error field

<p>Indicates whether the DMA transfer to/from the remote peer has encountered an error. A value of 1 indicates an error, while a value of 0 indicates no error.</p>

## entry register file

- Absolute Address: 0x200008D4
- Base Offset: 0x0
- Size: 0x1C
- Array Dimensions: [4]
- Array Stride: 0x1C
- Total Size: 0x70

<p>Register file for a single remote peer configuration and memory region information.</p>

|Offset|  Identifier  |                                Name                                |
|------|--------------|--------------------------------------------------------------------|
| 0x00 |  mac_address |  csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].mac_address |
| 0x08 | rmem_address | csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].rmem_address |
| 0x0C | local_address| csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].local_address|
| 0x10 |remote_address|csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].remote_address|
| 0x14 |     size     |     csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].size     |
| 0x18 |      dma     |      csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma     |

### mac_address register

- Absolute Address: 0x200008D4
- Base Offset: 0x0
- Size: 0x8

<p>Remote peer 48-bit destination MAC address.</p>

| Bits|Identifier|Access|Reset|                                      Name                                      |
|-----|----------|------|-----|--------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address.</p>

### rmem_address register

- Absolute Address: 0x200008DC
- Base Offset: 0x8
- Size: 0x4

<p>Address offset of the virtual memory region corresponding to the remote peer's memory.</p>

|Bits|Identifier|Access|Reset|                                      Name                                     |
|----|----------|------|-----|-------------------------------------------------------------------------------|
|31:0|  offset  |  rw  |  —  |csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].rmem_address.offset[31:0]|

#### offset field

<p>Word-aligned 32-bit address offset of the virtual memory region corresponding to the remote peer's memory.</p>

### local_address register

- Absolute Address: 0x200008E0
- Base Offset: 0xC
- Size: 0x4

<p>Start address of the local memory region for DMA transfers.</p>

|Bits|Identifier|Access|Reset|                                     Name                                     |
|----|----------|------|-----|------------------------------------------------------------------------------|
|31:0|   base   |  rw  |  —  |csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].local_address.base[31:0]|

#### base field

<p>Word-aligned 32-bit start address of the local memory region for DMA transfers.</p>

### remote_address register

- Absolute Address: 0x200008E4
- Base Offset: 0x10
- Size: 0x4

<p>Start address of the remote peer's memory region.</p>

|Bits|Identifier|Access|Reset|                                      Name                                     |
|----|----------|------|-----|-------------------------------------------------------------------------------|
|31:0|   base   |  rw  |  —  |csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].remote_address.base[31:0]|

#### base field

<p>Word-aligned 32-bit start address of the remote peer's memory region.</p>

### size register

- Absolute Address: 0x200008E8
- Base Offset: 0x14
- Size: 0x4

<p>Size of the remote peer's memory region.</p>

|Bits|Identifier|Access|Reset|                                 Name                                 |
|----|----------|------|-----|----------------------------------------------------------------------|
|31:0|   bytes  |  rw  |  —  |csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].size.bytes[31:0]|

#### bytes field

<p>32-bit size of the remote peer's memory region in bytes.</p>

### dma register

- Absolute Address: 0x200008EC
- Base Offset: 0x18
- Size: 0x4

<p>DMA configuration and control for the remote peer.</p>

|Bits|Identifier|Access|Reset|                                 Name                                 |
|----|----------|------|-----|----------------------------------------------------------------------|
| 1:0|   mode   |  rw  |  —  |  csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.mode[1:0] |
|  8 |  request |  rw  | 0x0 |csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.request[8:8]|
| 16 |   idle   |   r  |  —  | csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.idle[16:16]|
| 24 |   done   |   r  |  —  | csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.done[24:24]|
| 25 |   error  |   r  |  —  |csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.error[25:25]|

#### mode field

<p>DMA mode for transfers to/from the remote peer:<ul></p>
<li>0: DMA transfers to/from the remote peer are disabled.</li>
<li>1: DMA transfers to/from the remote peer are enabled in transparent mode, where accesses to the virtual memory region are directly translated to corresponding accesses to the remote peer's memory region (transactions are word-by-word, i.e., per virtual memory access).</li>
<li>2: DMA transfers to/from the remote peer are enabled in mirror-to-local mode, where the local memory region is used instead of the virtual memory region. The state of the remote peer's memory region (remote_address, size) is fetched from the remote peer on demand or periodically.</li>
<li>3: DMA transfers to/from the remote peer are enabled in mirror-to-remote mode, where the remote memory region is used instead of the virtual memory region. The state of the local peer's memory region (local_address, size) is sent to the remote peer on demand or periodically.</li>
</ul>

#### request field

<p>Writing a 1 to this field initiates a DMA transfer to/from the remote peer. This field is a single-pulse register that is automatically cleared back to zero after being written.</p>

#### idle field

<p>Indicates whether the DMA transfer to/from the remote peer is idle. A value of 1 indicates that the DMA transfer is idle, while a value of 0 indicates that the DMA transfer is in progress.</p>

#### done field

<p>Indicates whether the DMA transfer to/from the remote peer has been successful. A value of 1 indicates that the DMA transfer has completed successfully, while a value of 0 indicates that the DMA transfer is still in progress or has encountered an error.</p>

#### error field

<p>Indicates whether the DMA transfer to/from the remote peer has encountered an error. A value of 1 indicates an error, while a value of 0 indicates no error.</p>

## rmem register file

- Absolute Address: 0x20000C00
- Base Offset: 0x400
- Size: 0x400

<p>Virtual memory region for all remote peers, with offsets and sizes defined in the peers regfile.</p>

|Offset|Identifier|                          Name                         |
|------|----------|-------------------------------------------------------|
| 0x000|  word[0] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x004|  word[1] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x008|  word[2] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x00C|  word[3] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x010|  word[4] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x014|  word[5] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x018|  word[6] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x01C|  word[7] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x020|  word[8] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x024|  word[9] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x028| word[10] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x02C| word[11] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x030| word[12] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x034| word[13] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x038| word[14] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x03C| word[15] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x040| word[16] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x044| word[17] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x048| word[18] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x04C| word[19] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x050| word[20] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x054| word[21] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x058| word[22] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x05C| word[23] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x060| word[24] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x064| word[25] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x068| word[26] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x06C| word[27] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x070| word[28] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x074| word[29] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x078| word[30] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x07C| word[31] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x080| word[32] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x084| word[33] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x088| word[34] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x08C| word[35] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x090| word[36] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x094| word[37] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x098| word[38] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x09C| word[39] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x0A0| word[40] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x0A4| word[41] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x0A8| word[42] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x0AC| word[43] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x0B0| word[44] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x0B4| word[45] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x0B8| word[46] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x0BC| word[47] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x0C0| word[48] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x0C4| word[49] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x0C8| word[50] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x0CC| word[51] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x0D0| word[52] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x0D4| word[53] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x0D8| word[54] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x0DC| word[55] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x0E0| word[56] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x0E4| word[57] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x0E8| word[58] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x0EC| word[59] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x0F0| word[60] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x0F4| word[61] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x0F8| word[62] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x0FC| word[63] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x100| word[64] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x104| word[65] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x108| word[66] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x10C| word[67] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x110| word[68] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x114| word[69] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x118| word[70] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x11C| word[71] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x120| word[72] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x124| word[73] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x128| word[74] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x12C| word[75] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x130| word[76] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x134| word[77] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x138| word[78] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x13C| word[79] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x140| word[80] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x144| word[81] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x148| word[82] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x14C| word[83] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x150| word[84] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x154| word[85] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x158| word[86] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x15C| word[87] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x160| word[88] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x164| word[89] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x168| word[90] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x16C| word[91] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x170| word[92] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x174| word[93] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x178| word[94] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x17C| word[95] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x180| word[96] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x184| word[97] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x188| word[98] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x18C| word[99] |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x190| word[100]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x194| word[101]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x198| word[102]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x19C| word[103]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x1A0| word[104]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x1A4| word[105]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x1A8| word[106]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x1AC| word[107]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x1B0| word[108]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x1B4| word[109]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x1B8| word[110]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x1BC| word[111]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x1C0| word[112]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x1C4| word[113]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x1C8| word[114]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x1CC| word[115]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x1D0| word[116]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x1D4| word[117]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x1D8| word[118]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x1DC| word[119]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x1E0| word[120]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x1E4| word[121]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x1E8| word[122]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x1EC| word[123]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x1F0| word[124]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x1F4| word[125]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x1F8| word[126]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x1FC| word[127]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x200| word[128]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x204| word[129]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x208| word[130]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x20C| word[131]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x210| word[132]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x214| word[133]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x218| word[134]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x21C| word[135]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x220| word[136]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x224| word[137]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x228| word[138]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x22C| word[139]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x230| word[140]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x234| word[141]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x238| word[142]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x23C| word[143]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x240| word[144]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x244| word[145]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x248| word[146]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x24C| word[147]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x250| word[148]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x254| word[149]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x258| word[150]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x25C| word[151]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x260| word[152]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x264| word[153]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x268| word[154]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x26C| word[155]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x270| word[156]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x274| word[157]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x278| word[158]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x27C| word[159]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x280| word[160]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x284| word[161]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x288| word[162]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x28C| word[163]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x290| word[164]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x294| word[165]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x298| word[166]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x29C| word[167]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x2A0| word[168]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x2A4| word[169]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x2A8| word[170]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x2AC| word[171]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x2B0| word[172]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x2B4| word[173]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x2B8| word[174]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x2BC| word[175]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x2C0| word[176]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x2C4| word[177]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x2C8| word[178]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x2CC| word[179]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x2D0| word[180]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x2D4| word[181]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x2D8| word[182]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x2DC| word[183]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x2E0| word[184]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x2E4| word[185]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x2E8| word[186]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x2EC| word[187]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x2F0| word[188]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x2F4| word[189]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x2F8| word[190]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x2FC| word[191]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x300| word[192]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x304| word[193]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x308| word[194]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x30C| word[195]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x310| word[196]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x314| word[197]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x318| word[198]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x31C| word[199]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x320| word[200]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x324| word[201]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x328| word[202]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x32C| word[203]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x330| word[204]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x334| word[205]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x338| word[206]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x33C| word[207]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x340| word[208]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x344| word[209]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x348| word[210]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x34C| word[211]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x350| word[212]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x354| word[213]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x358| word[214]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x35C| word[215]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x360| word[216]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x364| word[217]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x368| word[218]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x36C| word[219]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x370| word[220]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x374| word[221]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x378| word[222]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x37C| word[223]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x380| word[224]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x384| word[225]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x388| word[226]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x38C| word[227]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x390| word[228]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x394| word[229]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x398| word[230]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x39C| word[231]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x3A0| word[232]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x3A4| word[233]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x3A8| word[234]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x3AC| word[235]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x3B0| word[236]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x3B4| word[237]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x3B8| word[238]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x3BC| word[239]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x3C0| word[240]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x3C4| word[241]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x3C8| word[242]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x3CC| word[243]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x3D0| word[244]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x3D4| word[245]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x3D8| word[246]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x3DC| word[247]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x3E0| word[248]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x3E4| word[249]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x3E8| word[250]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x3EC| word[251]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x3F0| word[252]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x3F4| word[253]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x3F8| word[254]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|
| 0x3FC| word[255]|csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|

### word register

- Absolute Address: 0x20000C00
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000C04
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000C08
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000C0C
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000C10
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000C14
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000C18
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000C1C
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000C20
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000C24
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000C28
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000C2C
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000C30
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000C34
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000C38
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000C3C
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000C40
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000C44
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000C48
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000C4C
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000C50
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000C54
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000C58
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000C5C
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000C60
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000C64
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000C68
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000C6C
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000C70
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000C74
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000C78
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000C7C
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000C80
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000C84
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000C88
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000C8C
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000C90
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000C94
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000C98
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000C9C
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000CA0
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000CA4
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000CA8
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000CAC
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000CB0
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000CB4
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000CB8
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000CBC
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000CC0
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000CC4
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000CC8
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000CCC
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000CD0
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000CD4
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000CD8
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000CDC
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000CE0
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000CE4
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000CE8
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000CEC
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000CF0
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000CF4
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000CF8
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000CFC
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000D00
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000D04
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000D08
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000D0C
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000D10
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000D14
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000D18
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000D1C
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000D20
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000D24
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000D28
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000D2C
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000D30
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000D34
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000D38
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000D3C
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000D40
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000D44
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000D48
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000D4C
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000D50
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000D54
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000D58
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000D5C
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000D60
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000D64
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000D68
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000D6C
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000D70
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000D74
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000D78
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000D7C
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000D80
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000D84
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000D88
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000D8C
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000D90
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000D94
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000D98
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000D9C
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000DA0
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000DA4
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000DA8
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000DAC
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000DB0
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000DB4
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000DB8
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000DBC
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000DC0
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000DC4
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000DC8
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000DCC
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000DD0
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000DD4
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000DD8
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000DDC
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000DE0
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000DE4
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000DE8
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000DEC
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000DF0
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000DF4
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000DF8
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000DFC
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000E00
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000E04
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000E08
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000E0C
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000E10
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000E14
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000E18
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000E1C
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000E20
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000E24
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000E28
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000E2C
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000E30
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000E34
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000E38
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000E3C
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000E40
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000E44
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000E48
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000E4C
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000E50
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000E54
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000E58
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000E5C
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000E60
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000E64
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000E68
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000E6C
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000E70
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000E74
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000E78
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000E7C
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000E80
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000E84
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000E88
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000E8C
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000E90
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000E94
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000E98
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000E9C
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000EA0
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000EA4
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000EA8
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000EAC
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000EB0
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000EB4
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000EB8
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000EBC
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000EC0
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000EC4
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000EC8
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000ECC
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000ED0
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000ED4
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000ED8
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000EDC
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000EE0
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000EE4
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000EE8
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000EEC
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000EF0
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000EF4
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000EF8
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000EFC
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000F00
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000F04
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000F08
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000F0C
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000F10
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000F14
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000F18
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000F1C
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000F20
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000F24
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000F28
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000F2C
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000F30
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000F34
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000F38
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000F3C
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000F40
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000F44
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000F48
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000F4C
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000F50
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000F54
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000F58
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000F5C
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000F60
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000F64
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000F68
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000F6C
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000F70
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000F74
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000F78
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000F7C
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000F80
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000F84
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000F88
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000F8C
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000F90
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000F94
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000F98
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000F9C
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000FA0
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000FA4
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000FA8
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000FAC
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000FB0
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000FB4
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000FB8
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000FBC
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000FC0
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000FC4
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000FC8
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000FCC
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000FD0
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000FD4
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000FD8
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000FDC
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000FE0
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000FE4
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000FE8
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000FEC
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000FF0
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000FF4
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000FF8
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

### word register

- Absolute Address: 0x20000FFC
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [256]
- Array Stride: 0x4
- Total Size: 0x400

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>

## switch_interface register file

- Absolute Address: 0x20001000
- Base Offset: 0x1000
- Size: 0x100

<p>Control and status register file for an openENOC Switch instance. It includes configuration registers and a forwarding table used to map destination MAC address keys to output interface selections for frame forwarding.</p>

|Offset|    Identifier    |                  Name                 |
|------|------------------|---------------------------------------|
| 0x00 |       info       |       csr.switch_interface.info       |
| 0x04 |forwarding_control|csr.switch_interface.forwarding_control|
| 0x08 |default_forwarding|csr.switch_interface.default_forwarding|
| 0x80 | forwarding_table | csr.switch_interface.forwarding_table |

### info register

- Absolute Address: 0x20001000
- Base Offset: 0x0
- Size: 0x4

<p>Read-only information register for this openENOC Switch instance.</p>

| Bits|    Identifier   |Access|Reset|                       Name                       |
|-----|-----------------|------|-----|--------------------------------------------------|
| 15:0|   table_depth   |   r  | 0x8 |    csr.switch_interface.info.table_depth[15:0]   |
|21:16|num_of_interfaces|   r  | 0x4 |csr.switch_interface.info.num_of_interfaces[21:16]|

#### table_depth field

<p>Depth of the forwarding table in this openENOC Switch instance. This field reflects the TABLE_DEPTH parameter value.</p>

#### num_of_interfaces field

<p>Number of interfaces in this openENOC Switch instance. This field reflects the NUM_OF_INTERFACES parameter value.</p>

### forwarding_control register

- Absolute Address: 0x20001004
- Base Offset: 0x4
- Size: 0x4

<p>Forwarding control register for the openENOC Switch instance.</p>

|Bits|  Identifier  |Access|Reset|                            Name                           |
|----|--------------|------|-----|-----------------------------------------------------------|
|  0 |operation_mode|  rw  | 0x0 |csr.switch_interface.forwarding_control.operation_mode[0:0]|
|  7 | pause_request|  rw  | 0x0 | csr.switch_interface.forwarding_control.pause_request[7:7]|
| 15 |  pause_done  |   r  |  —  | csr.switch_interface.forwarding_control.pause_done[15:15] |

#### operation_mode field

<p>Mode of operation for the openENOC Switch instance. When set to 1, the switch operates in managed mode, allowing software to configure the forwarding table and control forwarding operations. When set to 0, the switch operates in unmanaged mode, where forwarding state is maintained autonomously by internal hardware logic without software intervention.</p>

#### pause_request field

<p>Pause request for the forwarding logic. When set, this field requests the switch to pause frame forwarding and clear its internal pipeline before forwarding table updates are performed.</p>

#### pause_done field

<p>Pause done status. When set, this field indicates that the switch has paused frame forwarding and reached a safe state for forwarding table modification.</p>

### default_forwarding register

- Absolute Address: 0x20001008
- Base Offset: 0x8
- Size: 0x4

<p>Defines the destination interface or interfaces for frames that do not match any enabled forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                 Name                                |
|----|----------|------|-----|---------------------------------------------------------------------|
| 3:0|  bitmap  |  rw  | 0x0 |csr.switch_interface.default_forwarding.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which frames that do not match any enabled forwarding table entry are forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

## forwarding_table register file

- Absolute Address: 0x20001080
- Base Offset: 0x80
- Size: 0x80

<p>Forwarding table used to map MAC addresses to output interface selections for frame forwarding.</p>

|Offset|Identifier|                             Name                            |
|------|----------|-------------------------------------------------------------|
| 0x00 | entry[0] |csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x10 | entry[1] |csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x20 | entry[2] |csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x30 | entry[3] |csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x40 | entry[4] |csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x50 | entry[5] |csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x60 | entry[6] |csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1]|
| 0x70 | entry[7] |csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1]|

## entry register file

- Absolute Address: 0x20001080
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [8]
- Array Stride: 0x10
- Total Size: 0x80

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset| Identifier|                                   Name                                  |
|------|-----------|-------------------------------------------------------------------------|
|  0x0 |mac_address|csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address|
|  0x8 |   iface   |   csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].iface   |
|  0xC |   config  |   csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].config  |

### mac_address register

- Absolute Address: 0x20001080
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                          Name                                          |
|-----|----------|------|-----|----------------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x20001088
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                               Name                                              |
|----|----------|------|-----|-------------------------------------------------------------------------------------------------|
| 3:0|  bitmap  |  rw  |  —  |csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x2000108C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                    Name                                    |
|----|----------|------|-----|----------------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x20001090
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [8]
- Array Stride: 0x10
- Total Size: 0x80

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset| Identifier|                                   Name                                  |
|------|-----------|-------------------------------------------------------------------------|
|  0x0 |mac_address|csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address|
|  0x8 |   iface   |   csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].iface   |
|  0xC |   config  |   csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].config  |

### mac_address register

- Absolute Address: 0x20001090
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                          Name                                          |
|-----|----------|------|-----|----------------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x20001098
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                               Name                                              |
|----|----------|------|-----|-------------------------------------------------------------------------------------------------|
| 3:0|  bitmap  |  rw  |  —  |csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x2000109C
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                    Name                                    |
|----|----------|------|-----|----------------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x200010A0
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [8]
- Array Stride: 0x10
- Total Size: 0x80

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset| Identifier|                                   Name                                  |
|------|-----------|-------------------------------------------------------------------------|
|  0x0 |mac_address|csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address|
|  0x8 |   iface   |   csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].iface   |
|  0xC |   config  |   csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].config  |

### mac_address register

- Absolute Address: 0x200010A0
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                          Name                                          |
|-----|----------|------|-----|----------------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x200010A8
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                               Name                                              |
|----|----------|------|-----|-------------------------------------------------------------------------------------------------|
| 3:0|  bitmap  |  rw  |  —  |csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x200010AC
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                    Name                                    |
|----|----------|------|-----|----------------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x200010B0
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [8]
- Array Stride: 0x10
- Total Size: 0x80

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset| Identifier|                                   Name                                  |
|------|-----------|-------------------------------------------------------------------------|
|  0x0 |mac_address|csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address|
|  0x8 |   iface   |   csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].iface   |
|  0xC |   config  |   csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].config  |

### mac_address register

- Absolute Address: 0x200010B0
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                          Name                                          |
|-----|----------|------|-----|----------------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x200010B8
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                               Name                                              |
|----|----------|------|-----|-------------------------------------------------------------------------------------------------|
| 3:0|  bitmap  |  rw  |  —  |csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x200010BC
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                    Name                                    |
|----|----------|------|-----|----------------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x200010C0
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [8]
- Array Stride: 0x10
- Total Size: 0x80

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset| Identifier|                                   Name                                  |
|------|-----------|-------------------------------------------------------------------------|
|  0x0 |mac_address|csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address|
|  0x8 |   iface   |   csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].iface   |
|  0xC |   config  |   csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].config  |

### mac_address register

- Absolute Address: 0x200010C0
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                          Name                                          |
|-----|----------|------|-----|----------------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x200010C8
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                               Name                                              |
|----|----------|------|-----|-------------------------------------------------------------------------------------------------|
| 3:0|  bitmap  |  rw  |  —  |csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x200010CC
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                    Name                                    |
|----|----------|------|-----|----------------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x200010D0
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [8]
- Array Stride: 0x10
- Total Size: 0x80

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset| Identifier|                                   Name                                  |
|------|-----------|-------------------------------------------------------------------------|
|  0x0 |mac_address|csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address|
|  0x8 |   iface   |   csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].iface   |
|  0xC |   config  |   csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].config  |

### mac_address register

- Absolute Address: 0x200010D0
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                          Name                                          |
|-----|----------|------|-----|----------------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x200010D8
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                               Name                                              |
|----|----------|------|-----|-------------------------------------------------------------------------------------------------|
| 3:0|  bitmap  |  rw  |  —  |csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x200010DC
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                    Name                                    |
|----|----------|------|-----|----------------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x200010E0
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [8]
- Array Stride: 0x10
- Total Size: 0x80

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset| Identifier|                                   Name                                  |
|------|-----------|-------------------------------------------------------------------------|
|  0x0 |mac_address|csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address|
|  0x8 |   iface   |   csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].iface   |
|  0xC |   config  |   csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].config  |

### mac_address register

- Absolute Address: 0x200010E0
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                          Name                                          |
|-----|----------|------|-----|----------------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x200010E8
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                               Name                                              |
|----|----------|------|-----|-------------------------------------------------------------------------------------------------|
| 3:0|  bitmap  |  rw  |  —  |csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x200010EC
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                    Name                                    |
|----|----------|------|-----|----------------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>

## entry register file

- Absolute Address: 0x200010F0
- Base Offset: 0x0
- Size: 0x10
- Array Dimensions: [8]
- Array Stride: 0x10
- Total Size: 0x80

<p>Forwarding table entry containing the MAC address key, output interface selection, and entry configuration.</p>

|Offset| Identifier|                                   Name                                  |
|------|-----------|-------------------------------------------------------------------------|
|  0x0 |mac_address|csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address|
|  0x8 |   iface   |   csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].iface   |
|  0xC |   config  |   csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].config  |

### mac_address register

- Absolute Address: 0x200010F0
- Base Offset: 0x0
- Size: 0x8

<p>48-bit destination MAC address used as the key for this forwarding table entry.</p>

| Bits|Identifier|Access|Reset|                                          Name                                          |
|-----|----------|------|-----|----------------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry.</p>

### iface register

- Absolute Address: 0x200010F8
- Base Offset: 0x8
- Size: 0x4

<p>Forwarding interface information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                               Name                                              |
|----|----------|------|-----|-------------------------------------------------------------------------------------------------|
| 3:0|  bitmap  |  rw  |  —  |csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]|

#### bitmap field

<p>Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface.</p>

### config register

- Absolute Address: 0x200010FC
- Base Offset: 0xC
- Size: 0x4

<p>Configuration information associated with this forwarding table entry.</p>

|Bits|Identifier|Access|Reset|                                    Name                                    |
|----|----------|------|-----|----------------------------------------------------------------------------|
|  0 |  enabled |  rw  |  —  |csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled|

#### enabled field

<p>Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup.</p>
