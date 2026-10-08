<!---
Markdown description for SystemRDL register map.

Don't override. Generated from: openenoc_endpoint_interface_top
  - /home/enio/Projects/openENOC/hal/interfaces/openenoc_endpoint_interface.rdl
-->

## openenoc_endpoint_interface_top address map

- Absolute Address: 0x0
- Base Offset: 0x0
- Size: 0xC0

<p>Control and status address map for an openENOC Endpoint Interface instance.</p>

|Offset|         Identifier        |            Name           |
|------|---------------------------|---------------------------|
|  0x0 |openenoc_endpoint_interface|openenoc_endpoint_interface|

## openenoc_endpoint_interface register file

- Absolute Address: 0x0
- Base Offset: 0x0
- Size: 0xC0

<p>Control and status register file for an openENOC Endpoint Interface instance.</p>

|Offset| Identifier |                  Name                  |
|------|------------|----------------------------------------|
| 0x00 |    info    |    openenoc_endpoint_interface.info    |
| 0x20 |   config   |   openenoc_endpoint_interface.config   |
| 0x40 |   axis_if  |   openenoc_endpoint_interface.axis_if  |
| 0x60 |non_oetp_dma|openenoc_endpoint_interface.non_oetp_dma|
| 0x80 |     irq    |     openenoc_endpoint_interface.irq    |
| 0xA0 |    peers   |    openenoc_endpoint_interface.peers   |
| 0xBC |    rmem    |    openenoc_endpoint_interface.rmem    |

### info register

- Absolute Address: 0x0
- Base Offset: 0x0
- Size: 0x8

<p>Read-only information register for this openENOC Endpoint Interface instance.</p>

| Bits|       Identifier       |Access| Reset|                              Name                              |
|-----|------------------------|------|------|----------------------------------------------------------------|
| 31:0|    rmem_total_depth    |   r  |  0x1 |     openenoc_endpoint_interface.info.rmem_total_depth[31:0]    |
|42:32|      num_of_peers      |   r  |  0x1 |      openenoc_endpoint_interface.info.num_of_peers[42:32]      |
|  43 |   peer_dma_supported   |   r  |  0x1 |       openenoc_endpoint_interface.info.peer_dma_supported      |
|  44 | non_oetp_dma_supported |   r  |  0x1 |     openenoc_endpoint_interface.info.non_oetp_dma_supported    |
|  45 |  direct_axis_supported |   r  |  0x1 |     openenoc_endpoint_interface.info.direct_axis_supported     |
|  46 |     rmem_supported     |   r  |  0x1 |         openenoc_endpoint_interface.info.rmem_supported        |
|  47 |      irq_supported     |   r  |  0x1 |         openenoc_endpoint_interface.info.irq_supported         |
|63:48|max_dma_frame_size_bytes|   r  |0x2000|openenoc_endpoint_interface.info.max_dma_frame_size_bytes[63:48]|

#### rmem_total_depth field

<p>Total depth of the shared memory region for all remote peers. This field
reflects the RMEM_TOTAL_DEPTH parameter value.</p>

#### num_of_peers field

<p>Number of remote peers supported by this openENOC Endpoint Interface instance,
from 0 to 2047. This field reflects the NUM_OF_PEERS parameter value.</p>

#### peer_dma_supported field

<p>Indicates whether DMA transfers associated with configured remote peers are
supported.</p>

#### non_oetp_dma_supported field

<p>Indicates whether endpoint-level DMA transfers of complete non-oETP Ethernet
frames are supported.</p>

#### direct_axis_supported field

<p>Indicates whether direct CSR-driven AXI4-Stream access is supported for
non-oETP Ethernet frames.</p>

#### rmem_supported field

<p>Indicates whether the transparent Remote Memory (RMEM) interface is supported.</p>

#### irq_supported field

<p>Indicates whether the endpoint interrupt output and interrupt-control logic
are implemented.</p>

#### max_dma_frame_size_bytes field

<p>Synthesis-time maximum Ethernet frame size in bytes, excluding FCS. This
field reflects the MAX_RAW_FRAME_SIZE parameter value and bounds raw
non-oETP DMA frames. The peer DMA memory-fragment ceiling is
4 * floor((MAX_RAW_FRAME_SIZE - 32) / 4), accounting for the Ethernet
header, oETP write metadata, data-word padding and EndOfData. An 8192-byte
frame limit permits 8160-byte memory fragments. A value of zero indicates
that DMA is not supported.</p>

## config register file

- Absolute Address: 0x20
- Base Offset: 0x20
- Size: 0x20

<p>Configuration register file for this openENOC Endpoint Interface instance.</p>

|Offset|      Identifier     |                          Name                          |
|------|---------------------|--------------------------------------------------------|
| 0x00 |     mac_address     |     openenoc_endpoint_interface.config.mac_address     |
| 0x08 |  multicast_address  |  openenoc_endpoint_interface.config.multicast_address  |
| 0x10 |   non_oetp_control  |   openenoc_endpoint_interface.config.non_oetp_control  |
| 0x14 |     rmem_timeout    |     openenoc_endpoint_interface.config.rmem_timeout    |
| 0x18 |     dma_timeout     |     openenoc_endpoint_interface.config.dma_timeout     |
| 0x1C |dma_max_fragment_size|openenoc_endpoint_interface.config.dma_max_fragment_size|

### mac_address register

- Absolute Address: 0x20
- Base Offset: 0x0
- Size: 0x8

<p>Local endpoint 48-bit unicast MAC address. The oETP engine uses this address
as its source MAC and compares individual-addressed incoming oETP frames against
it. The I/G bit in the first MAC octet must be zero. Group-addressed oETP frames
are compared against config.multicast_address instead.</p>

| Bits|Identifier|Access|Reset|                             Name                            |
|-----|----------|------|-----|-------------------------------------------------------------|
| 31:0|  lo_word |  rw  | 0x0 | openenoc_endpoint_interface.config.mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  | 0x0 |openenoc_endpoint_interface.config.mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address.</p>

### multicast_address register

- Absolute Address: 0x28
- Base Offset: 0x8
- Size: 0x8

<p>Local endpoint 48-bit multicast destination MAC address. For an incoming
oETP frame whose destination I/G bit is one, the engine accepts the destination
only when it exactly matches this address. All slave endpoints in a replication
group use the same value. This address is not used as a source MAC. Zero is the
reset value and matches no group-addressed destination, disabling oETP group
reception. Broadcast is accepted only when this address is all ones. This field
does not change the separate non-oETP receive-mode policy.</p>

| Bits|Identifier|Access|Reset|                                Name                               |
|-----|----------|------|-----|-------------------------------------------------------------------|
| 31:0|  lo_word |  rw  | 0x0 | openenoc_endpoint_interface.config.multicast_address.lo_word[31:0]|
|47:32|  hi_word |  rw  | 0x0 |openenoc_endpoint_interface.config.multicast_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit multicast MAC address.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit multicast MAC address.</p>

### non_oetp_control register

- Absolute Address: 0x30
- Base Offset: 0x10
- Size: 0x4

<p>Receive policy for Ethernet frames that do not carry oETP traffic.</p>

|Bits| Identifier |Access|Reset|                                 Name                                |
|----|------------|------|-----|---------------------------------------------------------------------|
| 1:0|receive_mode|  rw  | 0x1 |openenoc_endpoint_interface.config.non_oetp_control.receive_mode[1:0]|

#### receive_mode field

<p>Receive mode for non-oETP Ethernet frames:<ul></p>
<li>0: Drop all non-oETP Ethernet frames.</li>
<li>1: Filtered mode. Accept frames addressed to the configured local MAC
address and Ethernet broadcast frames.</li>
<li>2: Multicast mode. Accept the same frames as filtered mode, plus all
multicast-addressed frames.</li>
<li>3: Promiscuous mode. Accept all non-oETP Ethernet frames.</li>
<p></ul>
An accepted frame is directed to the non-oETP RX DMA channel when that channel
is armed; otherwise it is directed to the CSR AXI4-Stream sink.</p>

### rmem_timeout register

- Absolute Address: 0x34
- Base Offset: 0x14
- Size: 0x4

<p>Timeout configuration for transparent RMEM operations.</p>

|Bits|Identifier|Access|Reset|                            Name                            |
|----|----------|------|-----|------------------------------------------------------------|
|31:0|  cycles  |  rw  | 0x0 |openenoc_endpoint_interface.config.rmem_timeout.cycles[31:0]|

#### cycles field

<p>Maximum wait for an RMEM response in endpoint clock cycles. Zero disables
the timeout and permits an indefinite response wait. Hardware samples this
value when it accepts an RMEM operation; subsequent writes apply to later
operations. The response timer starts after the complete request frame has
been accepted by the Ethernet-facing transmit stream and runs until the
complete matching response is received and validated through Ethernet TLAST.
RX backpressure counts toward the timeout; remaining local memory completion
does not. A valid response completing on the expiry edge takes priority,
including a valid ERROR_RSP with its reported cause. Hardware does not
retry; timeout handling and retry policy belong to software. Multicast
writes do not wait for a response and do not use this response timeout.
An RMEM read timeout terminates the access with all-ones read data and read
ACK; a write timeout terminates with write ACK. The external-RMEM boundary
uses no ERR signals. Failures set error and error_code in the associated
peers.entry[].dma register and may generate a separate RMEM_ERROR IRQ event.</p>

### dma_timeout register

- Absolute Address: 0x38
- Base Offset: 0x18
- Size: 0x4

<p>Common response timeout for locally initiated unicast peer DMA fragments.</p>

|Bits|Identifier|Access|Reset|                            Name                           |
|----|----------|------|-----|-----------------------------------------------------------|
|31:0|  cycles  |  rw  | 0x0 |openenoc_endpoint_interface.config.dma_timeout.cycles[31:0]|

#### cycles field

<p>Maximum wait for a response to one peer DMA fragment, in endpoint clock
cycles. This value is shared by all peers. Zero disables the timeout and
permits an indefinite response wait. Hardware samples this value when the
oETP engine accepts the fragment request; later writes apply to later
fragments. The response timer starts after the complete request frame has
been accepted by the Ethernet-facing transmit stream and runs until the
complete matching response is received and validated through Ethernet TLAST,
including EndOfData where present. RX backpressure counts toward the timeout;
remaining local memory completion does not. A valid response completing on
the expiry edge takes priority, including a valid ERROR_RSP with its reported
cause. On expiry, hardware
aborts the remaining fragments of that DMA transfer and reports error code
8 (timeout) in the peer DMA status. Hardware does not retry; software decides
whether to start another transfer. This timeout does not apply to multicast
writes, non-oETP DMA, or transparent RMEM operations.</p>

### dma_max_fragment_size register

- Absolute Address: 0x3C
- Base Offset: 0x1C
- Size: 0x4

<p>Common software-selected maximum memory fragment size for locally
initiated peer DMA transfers. The synthesis-time frame limit remains fixed.</p>

|Bits|Identifier|Access| Reset|                                Name                                |
|----|----------|------|------|--------------------------------------------------------------------|
|31:0|   bytes  |  rw  |0x1FE0|openenoc_endpoint_interface.config.dma_max_fragment_size.bytes[31:0]|

#### bytes field

<p>Maximum meaningful memory bytes in one locally initiated DMA fragment,
excluding Ethernet/oETP headers, word padding, EndOfData and FCS. The
hardware rounds the written value down to a multiple of four before
validating it. The effective MFS must be at least four bytes and at most
4 * floor((MAX_RAW_FRAME_SIZE - 32) / 4). With an 8192-byte frame ceiling,
the effective range is 4 through 8160 bytes in steps of four, with reset
value 8160. For example, 31 selects 28, 7 selects 4, and 8161 through 8163
select 8160. Hardware snapshots the effective value when it accepts the
whole peer DMA transfer; later writes apply only to subsequent transfers.
The final fragment uses the exact remaining byte length and may be shorter
than four bytes. A written value of 0 through 3, or a rounded value above
the synthesized ceiling, rejects a new transfer with local error code 1
before issuing any memory or protocol operation. The CSR retains the
unrounded written value. This setting does not
restrict received peer requests, which use the synthesized fragment
ceiling, and does not affect RMEM, direct CSR streams or non-oETP DMA.</p>

## axis_if register file

- Absolute Address: 0x40
- Base Offset: 0x40
- Size: 0x1C

<p>Register file for the AXI4-Stream source and sink interfaces.</p>

|Offset|Identifier|                   Name                   |
|------|----------|------------------------------------------|
| 0x00 |  source  |openenoc_endpoint_interface.axis_if.source|
| 0x10 |   sink   | openenoc_endpoint_interface.axis_if.sink |

## source register file

- Absolute Address: 0x40
- Base Offset: 0x0
- Size: 0xC

<p>Register file for the AXI4-Stream source interface.</p>

|Offset|Identifier|                       Name                       |
|------|----------|--------------------------------------------------|
|  0x0 |   data   |  openenoc_endpoint_interface.axis_if.source.data |
|  0x4 |  control |openenoc_endpoint_interface.axis_if.source.control|
|  0x8 |  status  | openenoc_endpoint_interface.axis_if.source.status|

### data register

- Absolute Address: 0x40
- Base Offset: 0x0
- Size: 0x4

<p>Data register for the AXI4-Stream source interface.</p>

|Bits|Identifier|Access|Reset|                            Name                           |
|----|----------|------|-----|-----------------------------------------------------------|
|31:0|   tdata  |  rw  | 0x0 |openenoc_endpoint_interface.axis_if.source.data.tdata[31:0]|

#### tdata field

<p>32-bit data value for the AXI4-Stream source interface.</p>

### control register

- Absolute Address: 0x44
- Base Offset: 0x4
- Size: 0x4

<p>Control register for the AXI4-Stream source interface.</p>

| Bits|Identifier|Access|Reset|                             Name                            |
|-----|----------|------|-----|-------------------------------------------------------------|
|  0  |  tvalid  |  rw  | 0x0 |  openenoc_endpoint_interface.axis_if.source.control.tvalid  |
|  8  |   tlast  |  rw  | 0x0 |   openenoc_endpoint_interface.axis_if.source.control.tlast  |
|19:16|   tkeep  |  rw  | 0x0 |openenoc_endpoint_interface.axis_if.source.control.tkeep[3:0]|

#### tvalid field

<p>Indicates that the AXI4-Stream source interface has valid data to send.
Once asserted by software, the field remains asserted until the transfer is
accepted by the destination.</p>

#### tlast field

<p>Indicates the last data word of a frame on the AXI4-Stream source
interface.</p>

#### tkeep field

<p>Indicates which byte lanes contain valid data on the AXI4-Stream source
interface.</p>

### status register

- Absolute Address: 0x48
- Base Offset: 0x8
- Size: 0x4

<p>Status register for the AXI4-Stream source interface.</p>

|Bits|Identifier|Access|Reset|                          Name                          |
|----|----------|------|-----|--------------------------------------------------------|
|  0 |  tready  |   r  | 0x0 |openenoc_endpoint_interface.axis_if.source.status.tready|

#### tready field

<p>Indicates that the destination AXI4-Stream interface is ready to
receive data.</p>

## sink register file

- Absolute Address: 0x50
- Base Offset: 0x10
- Size: 0xC

<p>Register file for the AXI4-Stream sink interface.</p>

|Offset|Identifier|                      Name                      |
|------|----------|------------------------------------------------|
|  0x0 |   data   |  openenoc_endpoint_interface.axis_if.sink.data |
|  0x4 |  control |openenoc_endpoint_interface.axis_if.sink.control|
|  0x8 |  status  | openenoc_endpoint_interface.axis_if.sink.status|

### data register

- Absolute Address: 0x50
- Base Offset: 0x0
- Size: 0x4

<p>Data register for the AXI4-Stream sink interface.</p>

|Bits|Identifier|Access|Reset|                           Name                          |
|----|----------|------|-----|---------------------------------------------------------|
|31:0|   tdata  |   r  |  —  |openenoc_endpoint_interface.axis_if.sink.data.tdata[31:0]|

#### tdata field

<p>32-bit data value for the AXI4-Stream sink interface.</p>

### control register

- Absolute Address: 0x54
- Base Offset: 0x4
- Size: 0x4

<p>Control register for the AXI4-Stream sink interface.</p>

|Bits|Identifier|Access|Reset|                          Name                         |
|----|----------|------|-----|-------------------------------------------------------|
|  0 |  tready  |  rw  | 0x0 |openenoc_endpoint_interface.axis_if.sink.control.tready|

#### tready field

<p>Indicates that the AXI4-Stream sink interface is ready to accept a
data transfer. Once asserted by software, the field remains asserted until
a transfer occurs.</p>

### status register

- Absolute Address: 0x58
- Base Offset: 0x8
- Size: 0x4

<p>Status register for the AXI4-Stream sink interface.</p>

| Bits|Identifier|Access|Reset|                           Name                           |
|-----|----------|------|-----|----------------------------------------------------------|
|  0  |  tvalid  |   r  |  —  |  openenoc_endpoint_interface.axis_if.sink.status.tvalid  |
|  8  |   tlast  |   r  |  —  |   openenoc_endpoint_interface.axis_if.sink.status.tlast  |
|19:16|   tkeep  |   r  |  —  |openenoc_endpoint_interface.axis_if.sink.status.tkeep[3:0]|

#### tvalid field

<p>Indicates that the AXI4-Stream sink interface has valid data
to receive.</p>

#### tlast field

<p>Indicates the last data word of a frame on the AXI4-Stream
sink interface.</p>

#### tkeep field

<p>Indicates which byte lanes contain valid data on the AXI4-Stream
sink interface.</p>

## non_oetp_dma register file

- Absolute Address: 0x60
- Base Offset: 0x60
- Size: 0x20

<p>Endpoint-level DMA control and status for complete non-oETP Ethernet frames.
Frame data includes the Ethernet header and payload, but excludes the preamble,
Start Frame Delimiter (SFD), and Frame Check Sequence (FCS).</p>

|Offset|Identifier|                    Name                   |
|------|----------|-------------------------------------------|
| 0x00 |    tx    |openenoc_endpoint_interface.non_oetp_dma.tx|
| 0x10 |    rx    |openenoc_endpoint_interface.non_oetp_dma.rx|

## tx register file

- Absolute Address: 0x60
- Base Offset: 0x0
- Size: 0x10

<p>Transmit DMA channel for complete non-oETP Ethernet frames.</p>

|Offset|    Identifier    |                             Name                             |
|------|------------------|--------------------------------------------------------------|
|  0x0 |  buffer_address  |  openenoc_endpoint_interface.non_oetp_dma.tx.buffer_address  |
|  0x4 |   frame_length   |   openenoc_endpoint_interface.non_oetp_dma.tx.frame_length   |
|  0x8 |  command_status  |  openenoc_endpoint_interface.non_oetp_dma.tx.command_status  |
|  0xC |transferred_length|openenoc_endpoint_interface.non_oetp_dma.tx.transferred_length|

### buffer_address register

- Absolute Address: 0x60
- Base Offset: 0x0
- Size: 0x4

<p>Local memory address of the non-oETP Ethernet frame to transmit.</p>

|Bits|Identifier|Access|Reset|                                 Name                                |
|----|----------|------|-----|---------------------------------------------------------------------|
|31:0|   base   |  rw  | 0x0 |openenoc_endpoint_interface.non_oetp_dma.tx.buffer_address.base[31:0]|

#### base field

<p>32-bit byte address of the first byte of the transmit buffer.</p>

### frame_length register

- Absolute Address: 0x64
- Base Offset: 0x4
- Size: 0x4

<p>Length of the complete non-oETP Ethernet frame to transmit.</p>

|Bits|Identifier|Access|Reset|                                Name                                |
|----|----------|------|-----|--------------------------------------------------------------------|
|31:0|   bytes  |  rw  | 0x0 |openenoc_endpoint_interface.non_oetp_dma.tx.frame_length.bytes[31:0]|

#### bytes field

<p>Frame length in bytes. Valid non-zero values shall not exceed
info.max_dma_frame_size_bytes.</p>

### command_status register

- Absolute Address: 0x68
- Base Offset: 0x8
- Size: 0x4

<p>Command and completion status for the non-oETP transmit DMA channel.</p>

| Bits| Identifier |Access|Reset|                                    Name                                    |
|-----|------------|------|-----|----------------------------------------------------------------------------|
|  8  |   request  |  rw  | 0x0 |     openenoc_endpoint_interface.non_oetp_dma.tx.command_status.request     |
|  9  |clear_errors|  rw  | 0x0 |   openenoc_endpoint_interface.non_oetp_dma.tx.command_status.clear_errors  |
|  16 |    idle    |   r  |  —  |       openenoc_endpoint_interface.non_oetp_dma.tx.command_status.idle      |
|  24 |    done    |   r  |  —  |       openenoc_endpoint_interface.non_oetp_dma.tx.command_status.done      |
|  25 |    error   |   r  |  —  |      openenoc_endpoint_interface.non_oetp_dma.tx.command_status.error      |
|31:28| error_code |   r  |  —  |openenoc_endpoint_interface.non_oetp_dma.tx.command_status.error_code[31:28]|

#### request field

<p>Writing one requests transmission of the configured frame. The field
remains asserted until the DMA engine accepts the request. Hardware clears
it upon acceptance; while the channel is busy, a newly asserted request
remains pending. Software or an RTL controller shall read the completion
status and transferred length of the previous request before asserting this
field for the next request.</p>

#### clear_errors field

<p>Writing one clears this channel's error flag and error code.
Hardware clears the command after accepting it. The command does not
abort an active transfer, clear done or transferred length, or complete
an IRQ claim. A new failure takes precedence over a simultaneous clear.
Starting or successfully completing a transfer preserves a recorded error.</p>

#### idle field

<p>Indicates that the channel has no accepted transfer in progress.
Hardware deasserts this field when a request is accepted and asserts it
when the transfer completes.</p>

#### done field

<p>Sticky successful-completion flag. Hardware sets this field after the
accepted transfer completes successfully and clears it when the next request
is accepted.</p>

#### error field

<p>Sticky error-completion flag. Hardware sets this field when an
accepted transfer fails. Only command_status.clear_errors or endpoint
reset clears it; starting or successfully completing another transfer
preserves a recorded error.</p>

#### error_code field

<p>Sticky error code for the most recent transmit failure:<ul></p>
<li>0: No error.</li>
<li>1: Invalid DMA configuration or descriptor.</li>
<li>2: AXI4-Stream length or TLAST error.</li>
<li>3: Frame exceeds the supported size or configured buffer capacity.</li>
<li>4: AXI read SLVERR response.</li>
<li>5: AXI read DECERR response.</li>
<li>6: AXI write SLVERR response.</li>
<li>7: AXI write DECERR response.</li>
<li>8-15: Reserved.</li>
<p></ul>
These errors describe local non-oETP DMA work. Only
command_status.clear_errors or endpoint reset clears this field.
A new failure replaces the code and takes precedence over a simultaneous
clear; successful transfers preserve the previous failure.</p>

### transferred_length register

- Absolute Address: 0x6C
- Base Offset: 0xC
- Size: 0x4

<p>Number of bytes transferred for the most recently accepted transmit
request.</p>

|Bits|Identifier|Access|Reset|                                   Name                                   |
|----|----------|------|-----|--------------------------------------------------------------------------|
|31:0|   bytes  |   r  |  —  |openenoc_endpoint_interface.non_oetp_dma.tx.transferred_length.bytes[31:0]|

#### bytes field

<p>Actual number of bytes transferred. Hardware clears this field when
the next request is accepted.</p>

## rx register file

- Absolute Address: 0x70
- Base Offset: 0x10
- Size: 0x10

<p>Receive DMA channel for complete non-oETP Ethernet frames.</p>

|Offset|   Identifier  |                            Name                           |
|------|---------------|-----------------------------------------------------------|
|  0x0 | buffer_address| openenoc_endpoint_interface.non_oetp_dma.rx.buffer_address|
|  0x4 |buffer_capacity|openenoc_endpoint_interface.non_oetp_dma.rx.buffer_capacity|
|  0x8 | command_status| openenoc_endpoint_interface.non_oetp_dma.rx.command_status|
|  0xC |received_length|openenoc_endpoint_interface.non_oetp_dma.rx.received_length|

### buffer_address register

- Absolute Address: 0x70
- Base Offset: 0x0
- Size: 0x4

<p>Local memory address of the receive buffer for a non-oETP Ethernet frame.</p>

|Bits|Identifier|Access|Reset|                                 Name                                |
|----|----------|------|-----|---------------------------------------------------------------------|
|31:0|   base   |  rw  | 0x0 |openenoc_endpoint_interface.non_oetp_dma.rx.buffer_address.base[31:0]|

#### base field

<p>32-bit byte address of the first byte of the receive buffer.</p>

### buffer_capacity register

- Absolute Address: 0x74
- Base Offset: 0x4
- Size: 0x4

<p>Capacity of the receive buffer for one complete non-oETP Ethernet frame.</p>

|Bits|Identifier|Access|Reset|                                  Name                                 |
|----|----------|------|-----|-----------------------------------------------------------------------|
|31:0|   bytes  |  rw  | 0x0 |openenoc_endpoint_interface.non_oetp_dma.rx.buffer_capacity.bytes[31:0]|

#### bytes field

<p>Receive-buffer capacity in bytes. Valid non-zero values shall not exceed
info.max_dma_frame_size_bytes.</p>

### command_status register

- Absolute Address: 0x78
- Base Offset: 0x8
- Size: 0x4

<p>Command and completion status for the non-oETP receive DMA channel.</p>

| Bits| Identifier |Access|Reset|                                    Name                                    |
|-----|------------|------|-----|----------------------------------------------------------------------------|
|  8  |   request  |  rw  | 0x0 |     openenoc_endpoint_interface.non_oetp_dma.rx.command_status.request     |
|  9  |clear_errors|  rw  | 0x0 |   openenoc_endpoint_interface.non_oetp_dma.rx.command_status.clear_errors  |
|  16 |    idle    |   r  |  —  |       openenoc_endpoint_interface.non_oetp_dma.rx.command_status.idle      |
|  17 |    armed   |   r  |  —  |      openenoc_endpoint_interface.non_oetp_dma.rx.command_status.armed      |
|  24 |    done    |   r  |  —  |       openenoc_endpoint_interface.non_oetp_dma.rx.command_status.done      |
|  25 |    error   |   r  |  —  |      openenoc_endpoint_interface.non_oetp_dma.rx.command_status.error      |
|31:28| error_code |   r  |  —  |openenoc_endpoint_interface.non_oetp_dma.rx.command_status.error_code[31:28]|

#### request field

<p>Writing one arms reception into the configured buffer. The field remains
asserted until the DMA engine accepts the request. Hardware clears it upon
acceptance; while the channel is busy, a newly asserted request remains
pending. Software or an RTL controller shall read the completion status and
received length of the previous request before asserting this field for the
next request.</p>

#### clear_errors field

<p>Writing one clears this channel's error flag and error code.
Hardware clears the command after accepting it. The command does not
abort an active or armed receive, clear done or received length, or
complete an IRQ claim. A new failure takes precedence over a simultaneous
clear. Starting or successfully completing a transfer preserves a
recorded error.</p>

#### idle field

<p>Indicates that the channel has no accepted receive request in progress.
After acceptance, the channel may be armed and waiting for an eligible
non-oETP frame or may be writing a received frame to memory.</p>

#### armed field

<p>Indicates that the accepted receive request is waiting for an eligible
non-oETP Ethernet frame. Hardware sets this field when it accepts a request
and clears it when the first beat of the selected frame is accepted by the
RX DMA datapath. The frame-routing logic uses this field to select the
RX DMA path; otherwise an accepted non-oETP frame is directed to the
CSR AXI4-Stream sink.</p>

#### done field

<p>Sticky successful-completion flag. Hardware sets this field after a
received frame has been written successfully and clears it when the next
request is accepted.</p>

#### error field

<p>Sticky error-completion flag. Hardware sets this field when an
accepted receive fails. Only command_status.clear_errors or endpoint
reset clears it; starting or successfully completing another receive
preserves a recorded error.</p>

#### error_code field

<p>Sticky error code for the most recent receive failure:<ul></p>
<li>0: No error.</li>
<li>1: Invalid DMA configuration or descriptor.</li>
<li>2: AXI4-Stream length or TLAST error.</li>
<li>3: Received frame exceeds the configured buffer capacity.</li>
<li>4: AXI read SLVERR response.</li>
<li>5: AXI read DECERR response.</li>
<li>6: AXI write SLVERR response.</li>
<li>7: AXI write DECERR response.</li>
<li>8-15: Reserved.</li>
<p></ul>
Only command_status.clear_errors or endpoint reset clears this field.
A new failure replaces the code and takes precedence over a simultaneous
clear; successful transfers preserve the previous failure.</p>

### received_length register

- Absolute Address: 0x7C
- Base Offset: 0xC
- Size: 0x4

<p>Length of the most recently received non-oETP Ethernet frame.</p>

|Bits|Identifier|Access|Reset|                                  Name                                 |
|----|----------|------|-----|-----------------------------------------------------------------------|
|31:0|   bytes  |   r  |  —  |openenoc_endpoint_interface.non_oetp_dma.rx.received_length.bytes[31:0]|

#### bytes field

<p>Actual number of frame bytes written to the receive buffer. Hardware
clears this field when the next request is accepted.</p>

## irq register file

- Absolute Address: 0x80
- Base Offset: 0x80
- Size: 0x14

<p>Endpoint-level interrupt control and claim interface. Interrupt events from peer
DMA, non-oETP DMA, direct AXI4-Stream transfers, and RMEM failures are serialized
through a shared event FIFO.</p>

|Offset| Identifier |                    Name                    |
|------|------------|--------------------------------------------|
| 0x00 |   control  |   openenoc_endpoint_interface.irq.control  |
| 0x04 |event_enable|openenoc_endpoint_interface.irq.event_enable|
| 0x08 |   status   |   openenoc_endpoint_interface.irq.status   |
| 0x0C |    claim   |    openenoc_endpoint_interface.irq.claim   |
| 0x10 |  complete  |  openenoc_endpoint_interface.irq.complete  |

### control register

- Absolute Address: 0x80
- Base Offset: 0x0
- Size: 0x4

<p>Global interrupt-output control and interrupt-controller maintenance requests.</p>

|Bits|  Identifier |Access|Reset|                         Name                        |
|----|-------------|------|-----|-----------------------------------------------------|
|  0 |global_enable|  rw  | 0x0 |openenoc_endpoint_interface.irq.control.global_enable|
|  8 | clear_errors|  rw  | 0x0 | openenoc_endpoint_interface.irq.control.clear_errors|

#### global_enable field

<p>Enables the physical endpoint IRQ output. Clearing this field masks the
output but does not prevent enabled events from being queued. Event capture is
controlled by irq.event_enable and, for peer DMA, by the selected peer's
dma.irq_enable field.</p>

#### clear_errors field

<p>Writing one requests clearing of the sticky irq.status.overflow and
irq.status.invalid_complete flags. The field remains asserted until hardware
accepts the request and clears it.</p>

### event_enable register

- Absolute Address: 0x84
- Base Offset: 0x4
- Size: 0x4

<p>Enables generation of individual endpoint IRQ event classes. These fields
control event capture; irq.control.global_enable only masks the physical
IRQ output.</p>

|Bits|         Identifier         |Access|Reset|                                   Name                                  |
|----|----------------------------|------|-----|-------------------------------------------------------------------------|
|  0 |      peer_dma_complete     |  rw  | 0x0 |      openenoc_endpoint_interface.irq.event_enable.peer_dma_complete     |
|  1 |  non_oetp_dma_tx_complete  |  rw  | 0x0 |  openenoc_endpoint_interface.irq.event_enable.non_oetp_dma_tx_complete  |
|  2 |  non_oetp_dma_rx_complete  |  rw  | 0x0 |  openenoc_endpoint_interface.irq.event_enable.non_oetp_dma_rx_complete  |
|  3 | non_oetp_direct_tx_complete|  rw  | 0x0 | openenoc_endpoint_interface.irq.event_enable.non_oetp_direct_tx_complete|
|  4 |non_oetp_direct_rx_available|  rw  | 0x0 |openenoc_endpoint_interface.irq.event_enable.non_oetp_direct_rx_available|
|  5 |         rmem_error         |  rw  | 0x0 |         openenoc_endpoint_interface.irq.event_enable.rmem_error         |

#### peer_dma_complete field

<p>Enables PEER_DMA_COMPLETE events. A peer event is queued only when this
field and the selected peer's dma.irq_enable field were both set when the DMA
request was accepted. A failed incoming bulk DMA request also generates this
event for the peer resolved from the source MAC. For incoming failures,
hardware captures the per-peer enable when recording the failure and samples
this field at IRQ admission. Successful incoming requests generate no event.
CSR error recording and the error response do not wait for IRQ FIFO capacity.</p>

#### non_oetp_dma_tx_complete field

<p>Enables NON_OETP_DMA_TX_COMPLETE events. Hardware samples this field when
it accepts a non-oETP transmit DMA request.</p>

#### non_oetp_dma_rx_complete field

<p>Enables NON_OETP_DMA_RX_COMPLETE events. Hardware samples this field when
it accepts a non-oETP receive DMA request.</p>

#### non_oetp_direct_tx_complete field

<p>Enables NON_OETP_DIRECT_TX_COMPLETE events. Hardware samples this field when
the first beat of a direct transmit frame is accepted from the CSR-facing
AXI4-Stream interface. When enabled, the frame start is accepted only after an
IRQ FIFO credit has been reserved. The event is generated when the final beat
is accepted by the oETP engine.</p>

#### non_oetp_direct_rx_available field

<p>Enables NON_OETP_DIRECT_RX_AVAILABLE events. One event is generated when
the first beat of a new direct receive frame becomes valid on the CSR-facing
AXI4-Stream interface. When enabled, routing logic does not expose that first
TVALID until an IRQ FIFO credit is available, so the event cannot be lost.
The event does not depend on TLAST and therefore supports both cut-through and
frame-FIFO operation.</p>

#### rmem_error field

<p>Enables RMEM_ERROR events for locally initiated RMEM failures, including
timeout and an accepted ERROR_RSP, and failed incoming RMEM requests from a
resolved peer. Hardware records the associated peer's
dma.error and dma.error_code before
exposing the event and terminates the failed RMEM access without waiting
for IRQ FIFO capacity. For locally initiated failures the enable is sampled
when the failure is recorded; incoming failures sample it at IRQ admission.
The bulk DMA per-peer irq_enable does not gate RMEM_ERROR.
Successful RMEM accesses generate no event.</p>

### status register

- Absolute Address: 0x88
- Base Offset: 0x8
- Size: 0x4

<p>Status of the endpoint IRQ event FIFO and its reservation mechanism.</p>

| Bits|   Identifier   |Access|Reset|                           Name                           |
|-----|----------------|------|-----|----------------------------------------------------------|
|  0  |  claim_pending |   r  |  —  |   openenoc_endpoint_interface.irq.status.claim_pending   |
|  1  |   credit_full  |   r  |  —  |    openenoc_endpoint_interface.irq.status.credit_full    |
|  2  |    overflow    |   r  |  —  |      openenoc_endpoint_interface.irq.status.overflow     |
|  3  |invalid_complete|   r  |  —  |  openenoc_endpoint_interface.irq.status.invalid_complete |
|  4  |  irq_asserted  |   r  |  —  |    openenoc_endpoint_interface.irq.status.irq_asserted   |
| 15:8|   fifo_level   |   r  |  —  |  openenoc_endpoint_interface.irq.status.fifo_level[7:0]  |
|23:16| reserved_count |   r  |  —  |openenoc_endpoint_interface.irq.status.reserved_count[7:0]|

#### claim_pending field

<p>Indicates that at least one valid event is available in irq.claim.</p>

#### credit_full field

<p>Indicates that all event FIFO credits are occupied by queued claims or
reserved for admitted operations. While no credit is available, new
interrupt-enabled DMA requests are not accepted and the start of an
interrupt-enabled direct AXI4-Stream frame is backpressured.</p>

#### overflow field

<p>Sticky internal-error flag indicating that an enabled event could not be
retained. Correct credit reservation, admission control, and AXI4-Stream
backpressure make this condition unreachable during normal operation. Clear with
irq.control.clear_errors.</p>

#### invalid_complete field

<p>Sticky protocol-error flag indicating that irq.complete.valid was accepted
while no claim was pending or that the completion token did not match the
current claim. No claim is removed on a mismatch. Clear with
irq.control.clear_errors.</p>

#### irq_asserted field

<p>Reflects the current value of the physical endpoint IRQ output after
application of irq.control.global_enable.</p>

#### fifo_level field

<p>Number of valid claims currently queued in the IRQ event FIFO. Values
greater than 255 are reported as 255.</p>

#### reserved_count field

<p>Number of event FIFO credits reserved for admitted DMA operations or direct
transmit frames whose events have not yet been queued. Values greater than 255
are reported as 255.</p>

### claim register

- Absolute Address: 0x8C
- Base Offset: 0xC
- Size: 0x4

<p>Read-only view of the event at the head of the IRQ event FIFO. Reading this
register has no side effect, and all fields remain stable until a matching
irq.complete request removes the claim.</p>

| Bits|Identifier|Access|Reset|                        Name                        |
|-----|----------|------|-----|----------------------------------------------------|
| 10:0| peer_idx |   r  |  —  |openenoc_endpoint_interface.irq.claim.peer_idx[10:0]|
|14:11|  source  |   r  |  —  |  openenoc_endpoint_interface.irq.claim.source[3:0] |
|30:15| sequence |   r  |  —  |openenoc_endpoint_interface.irq.claim.sequence[15:0]|
|  31 |   valid  |   r  |  —  |     openenoc_endpoint_interface.irq.claim.valid    |

#### peer_idx field

<p>Zero-based peer index for a PEER_DMA_COMPLETE or RMEM_ERROR event, in the range 0 through
NUM_OF_PEERS-1. The field is not applicable to other event sources and is driven
to zero for deterministic readback.</p>

#### source field

<p>IRQ event source:<ul></p>
<li>0: PEER_DMA_COMPLETE. A peer DMA request completed with either success or
error; peer_idx identifies the peer.</li>
<li>1: NON_OETP_DMA_TX_COMPLETE. A non-oETP transmit DMA request completed with
either success or error.</li>
<li>2: NON_OETP_DMA_RX_COMPLETE. A non-oETP receive DMA request completed with
either success or error.</li>
<li>3: NON_OETP_DIRECT_TX_COMPLETE. The final beat of a direct non-oETP transmit
frame was accepted by the oETP engine.</li>
<li>4: NON_OETP_DIRECT_RX_AVAILABLE. The first beat of a new direct non-oETP
receive frame is available on the CSR-facing AXI4-Stream interface.</li>
<li>5: RMEM_ERROR. A locally initiated RMEM operation failed. The cause is
recorded in peers.entry[peer_idx].dma; peer_idx identifies the associated peer.</li>
<li>6-15: Reserved.</li>
<p></ul>
This field is meaningful only when valid is set.</p>

#### sequence field

<p>Monotonically increasing event sequence number, modulo 65536. The sequence
number distinguishes otherwise identical claims and protects against stale or
repeated completion requests.</p>

#### valid field

<p>Indicates that this register contains the valid event at the head of the
IRQ event FIFO. When clear, all other claim fields shall be ignored.</p>

### complete register

- Absolute Address: 0x90
- Base Offset: 0x10
- Size: 0x4

<p>Completion request for the current IRQ claim. Software acknowledges an event by
copying the complete 32-bit irq.claim value into this register.</p>

| Bits|Identifier|Access|Reset|                          Name                         |
|-----|----------|------|-----|-------------------------------------------------------|
| 10:0| peer_idx |  rw  | 0x0 |openenoc_endpoint_interface.irq.complete.peer_idx[10:0]|
|14:11|  source  |  rw  | 0x0 |  openenoc_endpoint_interface.irq.complete.source[3:0] |
|30:15| sequence |  rw  | 0x0 |openenoc_endpoint_interface.irq.complete.sequence[15:0]|
|  31 |   valid  |  rw  | 0x0 |     openenoc_endpoint_interface.irq.complete.valid    |

#### peer_idx field

<p>Peer-index portion of the claim token.</p>

#### source field

<p>Event-source portion of the claim token.</p>

#### sequence field

<p>Sequence-number portion of the claim token.</p>

#### valid field

<p>Writing one submits the completion token. The field remains asserted until
hardware validates the token and clears it. A matching token removes the current
claim and releases its FIFO credit; an invalid token leaves the claim unchanged
and sets irq.status.invalid_complete.</p>

## peers register file

- Absolute Address: 0xA0
- Base Offset: 0xA0
- Size: 0x1C

<p>Register file for remote peer configuration and memory region information.</p>

|Offset|Identifier|                           Name                           |
|------|----------|----------------------------------------------------------|
|  0x0 | entry[0] |openenoc_endpoint_interface.peers.entry[0..NUM_OF_PEERS-1]|

## entry register file

- Absolute Address: 0xA0
- Base Offset: 0x0
- Size: 0x1C
- Array Dimensions: [1]
- Array Stride: 0x1C
- Total Size: 0x1C

<p>Register file for a single remote peer configuration and memory region
information.</p>

|Offset|  Identifier  |                                   Name                                  |
|------|--------------|-------------------------------------------------------------------------|
| 0x00 |  mac_address |  openenoc_endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].mac_address |
| 0x08 | rmem_address | openenoc_endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].rmem_address |
| 0x0C | local_address| openenoc_endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].local_address|
| 0x10 |remote_address|openenoc_endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].remote_address|
| 0x14 |     size     |     openenoc_endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].size     |
| 0x18 |      dma     |      openenoc_endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma     |

### mac_address register

- Absolute Address: 0xA0
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

- Absolute Address: 0xA8
- Base Offset: 0x8
- Size: 0x4

<p>Address offset of the virtual memory region corresponding to the remote
peer's memory.</p>

|Bits|Identifier|Access|Reset|                                        Name                                        |
|----|----------|------|-----|------------------------------------------------------------------------------------|
|31:0|  offset  |  rw  |  —  |openenoc_endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].rmem_address.offset[31:0]|

#### offset field

<p>32-bit byte offset of the virtual memory region corresponding to the
remote peer's memory. The value shall be aligned to a 32-bit word boundary.</p>

### local_address register

- Absolute Address: 0xAC
- Base Offset: 0xC
- Size: 0x4

<p>Start address of the local memory region for DMA transfers.</p>

|Bits|Identifier|Access|Reset|                                        Name                                       |
|----|----------|------|-----|-----------------------------------------------------------------------------------|
|31:0|   base   |  rw  |  —  |openenoc_endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].local_address.base[31:0]|

#### base field

<p>Word-aligned 32-bit start address of the local memory region for
DMA transfers.</p>

### remote_address register

- Absolute Address: 0xB0
- Base Offset: 0x10
- Size: 0x4

<p>Start address of the remote peer's memory region.</p>

|Bits|Identifier|Access|Reset|                                        Name                                        |
|----|----------|------|-----|------------------------------------------------------------------------------------|
|31:0|   base   |  rw  |  —  |openenoc_endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].remote_address.base[31:0]|

#### base field

<p>Word-aligned 32-bit start address of the remote peer's memory region.</p>

### size register

- Absolute Address: 0xB4
- Base Offset: 0x14
- Size: 0x4

<p>Size of the remote peer's memory region.</p>

|Bits|Identifier|Access|Reset|                                    Name                                   |
|----|----------|------|-----|---------------------------------------------------------------------------|
|31:0|   bytes  |  rw  |  —  |openenoc_endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].size.bytes[31:0]|

#### bytes field

<p>32-bit size of the remote peer's memory region in bytes.</p>

### dma register

- Absolute Address: 0xB8
- Base Offset: 0x18
- Size: 0x4

<p>DMA/RMEM configuration and control for the remote peer, with shared
sticky error reporting. RMEM and bulk DMA retain separate IRQ event classes.</p>

| Bits| Identifier|Access|Reset|                                      Name                                      |
|-----|-----------|------|-----|--------------------------------------------------------------------------------|
| 1:0 |    mode   |  rw  |  —  |    openenoc_endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.mode[1:0]    |
|  2  | irq_enable|  rw  | 0x0 |    openenoc_endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.irq_enable   |
|  8  |  request  |  rw  | 0x0 |   openenoc_endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.request[8:8]  |
|  9  |clear_error|  rw  | 0x0 |   openenoc_endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.clear_error   |
|  16 |    idle   |   r  |  —  |   openenoc_endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.idle[16:16]   |
|  24 |    done   |   r  |  —  |   openenoc_endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.done[24:24]   |
|  25 |   error   |   r  |  —  |   openenoc_endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.error[25:25]  |
|31:28| error_code|   r  |  —  |openenoc_endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.error_code[31:28]|

#### mode field

<p>DMA mode and responder access policy for the remote peer:<ul></p>
<li>0: Disabled. Locally initiated DMA and transparent RMEM
operations are disabled, and incoming oETP memory requests from
this peer are rejected.</li>

<li>1: Transparent RMEM mode. Accesses to the virtual RMEM region
are translated into individual remote memory accesses. Incoming
transparent RMEM read and write requests from this peer are
permitted. Bulk DMA read and write requests are rejected.</li>

<li>2: Mirror-to-local mode. A locally initiated DMA request fetches
the remote memory region into the configured local memory region
using remote DMA reads. On the responder side, incoming bulk DMA
write requests from this peer are permitted and target the
configured local memory region. Incoming bulk DMA read requests
are rejected.</li>

<li>3: Mirror-to-remote mode. A locally initiated DMA request sends
the configured local memory region to the remote memory region
using remote DMA writes. On the responder side, incoming bulk DMA
read requests from this peer are permitted and source data from
the configured local memory region. Incoming bulk DMA write
requests are rejected.</li>

</ul>
<p>Consequently, a mirror relationship uses complementary modes:
an initiator operating in mirror-to-local mode communicates with
a responder entry configured as mirror-to-remote, while an
initiator operating in mirror-to-remote mode communicates with a
responder entry configured as mirror-to-local.</p>

#### irq_enable field

<p>Enables generation of a PEER_DMA_COMPLETE IRQ event for this peer.
Hardware samples this field together with irq.event_enable.peer_dma_complete
when it accepts the peer DMA request. Changing the field while a transfer is
active does not affect that transfer. Disabling the field does not affect
DMA execution or the done, error, and error_code status fields. For a
failed incoming bulk DMA request, this field is captured when recording
the failure and irq.event_enable.peer_dma_complete is sampled at IRQ
admission. The event identifies this peer by the received source MAC.
Successful incoming requests generate no event. RMEM errors use their
separate irq.event_enable.rmem_error path.</p>

#### request field

<p>Writing one requests a DMA transfer to or from the remote peer,
according to dma.mode. The field remains asserted until the DMA engine
accepts and snapshots the request. Hardware clears it upon acceptance;
while a transfer for this peer is active, a newly asserted request remains
pending. Software or an RTL controller shall read the completion status of
the previous request before asserting this field for the next request and
shall keep the peer configuration stable while this field is asserted.</p>

#### clear_error field

<p>Writing one clears this peer's shared RMEM/DMA error flag and error
code. The field remains asserted until hardware accepts and clears the
command. It does not abort an active operation, clear done, or complete
an IRQ claim. A new failure takes precedence over a simultaneous clear.
Starting or successfully completing an operation does not clear a
previously recorded error.</p>

#### idle field

<p>Indicates whether this peer has no accepted DMA request in progress.
Hardware deasserts this field when a request is accepted and asserts it
after all fragments of the requested block have completed.</p>

#### done field

<p>Sticky successful-completion flag for this peer. Hardware sets this
field after all fragments of the accepted block transfer complete
successfully and clears it when the next request is accepted.</p>

#### error field

<p>Shared sticky RMEM/DMA error flag for this peer. Hardware sets this
field when a locally initiated RMEM access or bulk DMA transfer fails,
or when servicing an incoming RMEM or bulk DMA request from this peer
fails. Received requests are associated by source MAC. An incoming failure
records its code before exposing its error response, independently of
IRQ enable; it does not change the locally initiated dma.request, idle,
or done state. An incomplete incoming DMA data frame records remote
stream code 10. Multicast response suppression does not suppress this
local error record or an enabled event.
Only dma.clear_error or endpoint reset clears a latched error; starting
or successfully completing another operation does not clear it. The
flag is independent of the IRQ event-enable fields.</p>

#### error_code field

<p>Shared sticky code for the most recent RMEM or bulk DMA failure for this peer:<ul></p>
<li>0: No error.</li>
<li>1: Local invalid request, configuration, descriptor, or parameters.</li>
<li>2: Local stream/PDU length or TLAST error.</li>
<li>3: Local supported-size or buffer-capacity overflow.</li>
<li>4: Local AXI read SLVERR response.</li>
<li>5: Local AXI read DECERR response.</li>
<li>6: Local AXI write SLVERR response.</li>
<li>7: Local AXI write DECERR response.</li>
<li>8: Local peer response timeout or Request ID wrap collision. An RMEM access
    terminates through its ACK-only boundary; a bulk DMA timeout aborts
    the remaining fragments. Hardware does not retry.</li>
<li>9: Remote invalid request, configuration, descriptor, or parameters.</li>
<li>10: Remote stream/PDU length or TLAST error. Also used directly by
    the receiver of an incomplete DMA_WRITE_REQ or DMA_READ_RSP,
    including missing or incorrect EndOfData.</li>
<li>11: Remote supported-size or buffer-capacity overflow.</li>
<li>12: Remote AXI read SLVERR response.</li>
<li>13: Remote AXI read DECERR response.</li>
<li>14: Remote AXI write SLVERR response.</li>
<li>15: Remote AXI write DECERR response.</li>
<p></ul>
Codes 1-8 describe errors detected by this endpoint, including
malformed responses, local memory failures, and failures while servicing
received requests. Codes 9-15 describe
failures reported by the responding peer through a valid ERROR_RSP.
Code 10 additionally reports an incomplete incoming DMA data frame
detected at this endpoint, without requiring an ERROR_RSP first.
A missing or incorrect EndOfData uses this same code even when
Ethernet padding masks the short data length. A receiver of an
incomplete unicast DMA_WRITE_REQ records CSR code 10 but sends
ERROR_RSP wire cause 2; multicast writes generate no response.
ERROR_RSP carries a 32-bit cause in the range 1-7, which the initiating
oETP engine validates and maps to CSR code = 8 + wire code. Values
outside 1-7 are invalid response parameters and record local code 1;
they must not be truncated or mistaken for local TIMEOUT = 8.
The oETP initiator completion channel carries this final CSR encoding
for both RMEM and bulk DMA. The responder completion channel reports
its cause 1-7 for serialization as ERROR_RSP; cause 2 on an incomplete
received bulk write corresponds to receiver CSR code 10. Hardware
clears this field only on dma.clear_error or endpoint reset. Successful
operations preserve a recorded failure. A new failure replaces the code
and takes precedence over a simultaneous clear. A failed streaming
transfer may have partially modified memory; error reporting does not
provide rollback or an exact count of modified bytes. Software manages
buffer synchronization and recovery.</p>

## rmem register file

- Absolute Address: 0xBC
- Base Offset: 0xBC
- Size: 0x4

<p>Virtual memory region for all remote peers, with offsets and sizes defined in the
peers regfile.</p>

|Offset|Identifier|                            Name                            |
|------|----------|------------------------------------------------------------|
|  0x0 |  word[0] |openenoc_endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1]|

### word register

- Absolute Address: 0xBC
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
