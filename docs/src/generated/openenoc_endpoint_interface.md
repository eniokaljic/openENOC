<!---
Markdown description for SystemRDL register map.

Don't override. Generated from: openenoc_endpoint_interface_top
  - /home/enio/Projects/openENOC/hal/src/openenoc.rdl
-->

## openenoc_endpoint_interface_top address map

- Absolute Address: 0x0
- Base Offset: 0x0
- Size: 0x60

<p>Control and status address map for an openENOC Endpoint Interface instance.</p>

|Offset|         Identifier        |            Name           |
|------|---------------------------|---------------------------|
|  0x0 |openenoc_endpoint_interface|openenoc_endpoint_interface|

## openenoc_endpoint_interface register file

- Absolute Address: 0x0
- Base Offset: 0x0
- Size: 0x60

<p>Control and status register file for an openENOC Endpoint Interface instance.</p>

|Offset|Identifier|                Name               |
|------|----------|-----------------------------------|
| 0x00 |   info   |  openenoc_endpoint_interface.info |
| 0x08 |  config  | openenoc_endpoint_interface.config|
| 0x20 |  axis_if |openenoc_endpoint_interface.axis_if|
| 0x40 |   peers  | openenoc_endpoint_interface.peers |
| 0x5C |   rmem   |  openenoc_endpoint_interface.rmem |

### info register

- Absolute Address: 0x0
- Base Offset: 0x0
- Size: 0x8

<p>Read-only information register for this openENOC Endpoint Interface instance.</p>

| Bits|   Identifier   |Access|Reset|                          Name                         |
|-----|----------------|------|-----|-------------------------------------------------------|
| 31:0|rmem_total_depth|   r  | 0x1 |openenoc_endpoint_interface.info.rmem_total_depth[15:0]|
|63:32|  num_of_peers  |   r  | 0x1 |  openenoc_endpoint_interface.info.num_of_peers[31:16] |

#### rmem_total_depth field

<p>Total depth of the shared memory region for all remote peers. This field reflects the RMEM_TOTAL_DEPTH parameter value.</p>

#### num_of_peers field

<p>Number of remote peers supported by this openENOC Endpoint Interface instance. This field reflects the NUM_OF_PEERS parameter value.</p>

## config register file

- Absolute Address: 0x8
- Base Offset: 0x8
- Size: 0x8

<p>Configuration register file for this openENOC Endpoint Interface instance.</p>

|Offset| Identifier|                     Name                     |
|------|-----------|----------------------------------------------|
|  0x0 |mac_address|openenoc_endpoint_interface.config.mac_address|

### mac_address register

- Absolute Address: 0x8
- Base Offset: 0x0
- Size: 0x8

<p>Local site 48-bit destination MAC address.</p>

| Bits|Identifier|Access|Reset|                             Name                            |
|-----|----------|------|-----|-------------------------------------------------------------|
| 31:0|  lo_word |  rw  | 0x0 | openenoc_endpoint_interface.config.mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  | 0x0 |openenoc_endpoint_interface.config.mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address.</p>

## axis_if register file

- Absolute Address: 0x20
- Base Offset: 0x20
- Size: 0x1C

<p>Register file for the AXI4-Stream source and sink interfaces.</p>

|Offset|Identifier|                   Name                   |
|------|----------|------------------------------------------|
| 0x00 |  source  |openenoc_endpoint_interface.axis_if.source|
| 0x10 |   sink   | openenoc_endpoint_interface.axis_if.sink |

## source register file

- Absolute Address: 0x20
- Base Offset: 0x0
- Size: 0xC

<p>Register file for the AXI4-Stream source interface.</p>

|Offset|Identifier|                       Name                       |
|------|----------|--------------------------------------------------|
|  0x0 |   data   |  openenoc_endpoint_interface.axis_if.source.data |
|  0x4 |  control |openenoc_endpoint_interface.axis_if.source.control|
|  0x8 |  status  | openenoc_endpoint_interface.axis_if.source.status|

### data register

- Absolute Address: 0x20
- Base Offset: 0x0
- Size: 0x4

<p>Data register for the AXI4-Stream source interface.</p>

|Bits|Identifier|Access|Reset|                            Name                           |
|----|----------|------|-----|-----------------------------------------------------------|
|31:0|   tdata  |  rw  | 0x0 |openenoc_endpoint_interface.axis_if.source.data.tdata[31:0]|

#### tdata field

<p>32-bit data value for the AXI4-Stream source interface.</p>

### control register

- Absolute Address: 0x24
- Base Offset: 0x4
- Size: 0x4

<p>Control register for the AXI4-Stream source interface.</p>

|Bits|Identifier|Access|Reset|                           Name                          |
|----|----------|------|-----|---------------------------------------------------------|
|  0 |  tvalid  |  rw  | 0x0 |openenoc_endpoint_interface.axis_if.source.control.tvalid|
|  8 |   tlast  |  rw  | 0x0 | openenoc_endpoint_interface.axis_if.source.control.tlast|

#### tvalid field

<p>Indicates that the AXI4-Stream source interface has valid data to send. This field is a single-pulse register that is automatically cleared back to zero after being written.</p>

#### tlast field

<p>Indicates the last data word of a frame on the AXI4-Stream source interface.</p>

### status register

- Absolute Address: 0x28
- Base Offset: 0x8
- Size: 0x4

<p>Status register for the AXI4-Stream source interface.</p>

|Bits|Identifier|Access|Reset|                          Name                          |
|----|----------|------|-----|--------------------------------------------------------|
|  0 |  tready  |   r  | 0x0 |openenoc_endpoint_interface.axis_if.source.status.tready|

#### tready field

<p>Indicates that the destination AXI4-Stream interface is ready to receive data.</p>

## sink register file

- Absolute Address: 0x30
- Base Offset: 0x10
- Size: 0xC

<p>Register file for the AXI4-Stream sink interface.</p>

|Offset|Identifier|                      Name                      |
|------|----------|------------------------------------------------|
|  0x0 |   data   |  openenoc_endpoint_interface.axis_if.sink.data |
|  0x4 |  control |openenoc_endpoint_interface.axis_if.sink.control|
|  0x8 |  status  | openenoc_endpoint_interface.axis_if.sink.status|

### data register

- Absolute Address: 0x30
- Base Offset: 0x0
- Size: 0x4

<p>Data register for the AXI4-Stream sink interface.</p>

|Bits|Identifier|Access|Reset|                           Name                          |
|----|----------|------|-----|---------------------------------------------------------|
|31:0|   tdata  |   r  |  —  |openenoc_endpoint_interface.axis_if.sink.data.tdata[31:0]|

#### tdata field

<p>32-bit data value for the AXI4-Stream sink interface.</p>

### control register

- Absolute Address: 0x34
- Base Offset: 0x4
- Size: 0x4

<p>Control register for the AXI4-Stream sink interface.</p>

|Bits|Identifier|Access|Reset|                          Name                         |
|----|----------|------|-----|-------------------------------------------------------|
|  0 |  tready  |   w  | 0x0 |openenoc_endpoint_interface.axis_if.sink.control.tready|

#### tready field

<p>Indicates that the AXI4-Stream sink interface is ready to receive next data transfer.</p>

### status register

- Absolute Address: 0x38
- Base Offset: 0x8
- Size: 0x4

<p>Status register for the AXI4-Stream sink interface.</p>

|Bits|Identifier|Access|Reset|                         Name                         |
|----|----------|------|-----|------------------------------------------------------|
|  0 |  tvalid  |   r  |  —  |openenoc_endpoint_interface.axis_if.sink.status.tvalid|
|  8 |   tlast  |   r  |  —  | openenoc_endpoint_interface.axis_if.sink.status.tlast|

#### tvalid field

<p>Indicates that the AXI4-Stream sink interface has valid data to receive.</p>

#### tlast field

<p>Indicates the last data word of a frame on the AXI4-Stream sink interface.</p>

## peers register file

- Absolute Address: 0x40
- Base Offset: 0x40
- Size: 0x1C

<p>Register file for remote peer configuration and memory region information.</p>

|Offset|Identifier|                           Name                           |
|------|----------|----------------------------------------------------------|
|  0x0 | entry[0] |openenoc_endpoint_interface.peers.entry[0..NUM_OF_PEERS-1]|

## entry register file

- Absolute Address: 0x40
- Base Offset: 0x0
- Size: 0x1C
- Array Dimensions: [1]
- Array Stride: 0x1C
- Total Size: 0x1C

<p>Register file for a single remote peer configuration and memory region information.</p>

|Offset|  Identifier  |                                   Name                                  |
|------|--------------|-------------------------------------------------------------------------|
| 0x00 |  mac_address |  openenoc_endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].mac_address |
| 0x08 | rmem_address | openenoc_endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].rmem_address |
| 0x0C | local_address| openenoc_endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].local_address|
| 0x10 |remote_address|openenoc_endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].remote_address|
| 0x14 |     size     |     openenoc_endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].size     |
| 0x18 |      dma     |      openenoc_endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma     |

### mac_address register

- Absolute Address: 0x40
- Base Offset: 0x0
- Size: 0x8

<p>Remote peer 48-bit destination MAC address.</p>

| Bits|Identifier|Access|Reset|                                         Name                                        |
|-----|----------|------|-----|-------------------------------------------------------------------------------------|
| 31:0|  lo_word |  rw  |  —  | openenoc_endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  |  —  |openenoc_endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address.</p>

### rmem_address register

- Absolute Address: 0x48
- Base Offset: 0x8
- Size: 0x4

<p>Address offset of the virtual memory region corresponding to the remote peer's memory.</p>

|Bits|Identifier|Access|Reset|                                        Name                                        |
|----|----------|------|-----|------------------------------------------------------------------------------------|
|31:0|  offset  |  rw  |  —  |openenoc_endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].rmem_address.offset[31:0]|

#### offset field

<p>Word-aligned 32-bit address offset of the virtual memory region corresponding to the remote peer's memory.</p>

### local_address register

- Absolute Address: 0x4C
- Base Offset: 0xC
- Size: 0x4

<p>Start address of the local memory region for DMA transfers.</p>

|Bits|Identifier|Access|Reset|                                        Name                                       |
|----|----------|------|-----|-----------------------------------------------------------------------------------|
|31:0|   base   |  rw  |  —  |openenoc_endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].local_address.base[31:0]|

#### base field

<p>Word-aligned 32-bit start address of the local memory region for DMA transfers.</p>

### remote_address register

- Absolute Address: 0x50
- Base Offset: 0x10
- Size: 0x4

<p>Start address of the remote peer's memory region.</p>

|Bits|Identifier|Access|Reset|                                        Name                                        |
|----|----------|------|-----|------------------------------------------------------------------------------------|
|31:0|   base   |  rw  |  —  |openenoc_endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].remote_address.base[31:0]|

#### base field

<p>Word-aligned 32-bit start address of the remote peer's memory region.</p>

### size register

- Absolute Address: 0x54
- Base Offset: 0x14
- Size: 0x4

<p>Size of the remote peer's memory region.</p>

|Bits|Identifier|Access|Reset|                                    Name                                   |
|----|----------|------|-----|---------------------------------------------------------------------------|
|31:0|   bytes  |  rw  |  —  |openenoc_endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].size.bytes[31:0]|

#### bytes field

<p>32-bit size of the remote peer's memory region in bytes.</p>

### dma register

- Absolute Address: 0x58
- Base Offset: 0x18
- Size: 0x4

<p>DMA configuration and control for the remote peer.</p>

|Bits|Identifier|Access|Reset|                                    Name                                   |
|----|----------|------|-----|---------------------------------------------------------------------------|
| 1:0|   mode   |  rw  |  —  |  openenoc_endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.mode[1:0] |
|  8 |  request |  rw  | 0x0 |openenoc_endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.request[8:8]|
| 16 |   idle   |   r  |  —  | openenoc_endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.idle[16:16]|
| 24 |   done   |   r  |  —  | openenoc_endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.done[24:24]|
| 25 |   error  |   r  |  —  |openenoc_endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.error[25:25]|

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

- Absolute Address: 0x5C
- Base Offset: 0x5C
- Size: 0x4

<p>Virtual memory region for all remote peers, with offsets and sizes defined in the peers regfile.</p>

|Offset|Identifier|                            Name                            |
|------|----------|------------------------------------------------------------|
|  0x0 |  word[0] |openenoc_endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|

### word register

- Absolute Address: 0x5C
- Base Offset: 0x0
- Size: 0x4
- Array Dimensions: [1]
- Array Stride: 0x4
- Total Size: 0x4

<p>32-bit word in the virtual memory region.</p>

|Bits|Identifier|Access|Reset|                                  Name                                 |
|----|----------|------|-----|-----------------------------------------------------------------------|
|31:0|   data   |  rw  |  —  |openenoc_endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]|

#### data field

<p>Data stored in this virtual memory word.</p>
