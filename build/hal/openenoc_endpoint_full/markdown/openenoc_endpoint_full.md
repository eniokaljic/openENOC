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

|Offset| Identifier |                Name               |
|------|------------|-----------------------------------|
| 0x000|    info    |    csr.endpoint_interface.info    |
| 0x020|   config   |   csr.endpoint_interface.config   |
| 0x040|   axis_if  |   csr.endpoint_interface.axis_if  |
| 0x060|non_oetp_dma|csr.endpoint_interface.non_oetp_dma|
| 0x080|     irq    |     csr.endpoint_interface.irq    |
| 0x100|    peers   |    csr.endpoint_interface.peers   |
| 0x400|    rmem    |    csr.endpoint_interface.rmem    |

### info register

- Absolute Address: 0x20000800
- Base Offset: 0x0
- Size: 0x8

<p>Read-only information register for this openENOC Endpoint Interface instance.</p>

| Bits|       Identifier       |Access| Reset|                            Name                           |
|-----|------------------------|------|------|-----------------------------------------------------------|
| 31:0|    rmem_total_depth    |   r  | 0x100|     csr.endpoint_interface.info.rmem_total_depth[31:0]    |
|42:32|      num_of_peers      |   r  |  0x4 |      csr.endpoint_interface.info.num_of_peers[42:32]      |
|  43 |   peer_dma_supported   |   r  |  0x1 |       csr.endpoint_interface.info.peer_dma_supported      |
|  44 | non_oetp_dma_supported |   r  |  0x1 |     csr.endpoint_interface.info.non_oetp_dma_supported    |
|  45 |  direct_axis_supported |   r  |  0x1 |     csr.endpoint_interface.info.direct_axis_supported     |
|  46 |     rmem_supported     |   r  |  0x1 |         csr.endpoint_interface.info.rmem_supported        |
|  47 |      irq_supported     |   r  |  0x1 |         csr.endpoint_interface.info.irq_supported         |
|63:48|max_dma_frame_size_bytes|   r  |0x2000|csr.endpoint_interface.info.max_dma_frame_size_bytes[63:48]|

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

- Absolute Address: 0x20000820
- Base Offset: 0x20
- Size: 0x20

<p>Configuration register file for this openENOC Endpoint Interface instance.</p>

|Offset|      Identifier     |                        Name                       |
|------|---------------------|---------------------------------------------------|
| 0x00 |     mac_address     |     csr.endpoint_interface.config.mac_address     |
| 0x08 |  multicast_address  |  csr.endpoint_interface.config.multicast_address  |
| 0x10 |   non_oetp_control  |   csr.endpoint_interface.config.non_oetp_control  |
| 0x14 |     rmem_timeout    |     csr.endpoint_interface.config.rmem_timeout    |
| 0x18 |     dma_timeout     |     csr.endpoint_interface.config.dma_timeout     |
| 0x1C |dma_max_fragment_size|csr.endpoint_interface.config.dma_max_fragment_size|

### mac_address register

- Absolute Address: 0x20000820
- Base Offset: 0x0
- Size: 0x8

<p>Local endpoint 48-bit unicast MAC address. The oETP engine uses this address
as its source MAC and compares individual-addressed incoming oETP frames against
it. The I/G bit in the first MAC octet must be zero. Group-addressed oETP frames
are compared against config.multicast_address instead.</p>

| Bits|Identifier|Access|Reset|                          Name                          |
|-----|----------|------|-----|--------------------------------------------------------|
| 31:0|  lo_word |  rw  | 0x0 | csr.endpoint_interface.config.mac_address.lo_word[31:0]|
|47:32|  hi_word |  rw  | 0x0 |csr.endpoint_interface.config.mac_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit MAC address.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit MAC address.</p>

### multicast_address register

- Absolute Address: 0x20000828
- Base Offset: 0x8
- Size: 0x8

<p>Local endpoint 48-bit multicast destination MAC address. For an incoming
oETP frame whose destination I/G bit is one, the engine accepts the destination
only when it exactly matches this address. All slave endpoints in a replication
group use the same value. This address is not used as a source MAC. Zero is the
reset value and matches no group-addressed destination, disabling oETP group
reception. Broadcast is accepted only when this address is all ones. This field
does not change the separate non-oETP receive-mode policy.</p>

| Bits|Identifier|Access|Reset|                             Name                             |
|-----|----------|------|-----|--------------------------------------------------------------|
| 31:0|  lo_word |  rw  | 0x0 | csr.endpoint_interface.config.multicast_address.lo_word[31:0]|
|47:32|  hi_word |  rw  | 0x0 |csr.endpoint_interface.config.multicast_address.hi_word[47:32]|

#### lo_word field

<p>Lower 32 bits [31:0] of the 48-bit multicast MAC address.</p>

#### hi_word field

<p>Upper 16 bits [47:32] of the 48-bit multicast MAC address.</p>

### non_oetp_control register

- Absolute Address: 0x20000830
- Base Offset: 0x10
- Size: 0x4

<p>Receive policy for Ethernet frames that do not carry oETP traffic.</p>

|Bits| Identifier |Access|Reset|                              Name                              |
|----|------------|------|-----|----------------------------------------------------------------|
| 1:0|receive_mode|  rw  | 0x1 |csr.endpoint_interface.config.non_oetp_control.receive_mode[1:0]|

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

- Absolute Address: 0x20000834
- Base Offset: 0x14
- Size: 0x4

<p>Timeout configuration for transparent RMEM operations.</p>

|Bits|Identifier|Access|Reset|                          Name                         |
|----|----------|------|-----|-------------------------------------------------------|
|31:0|  cycles  |  rw  | 0x0 |csr.endpoint_interface.config.rmem_timeout.cycles[31:0]|

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

- Absolute Address: 0x20000838
- Base Offset: 0x18
- Size: 0x4

<p>Common response timeout for locally initiated unicast peer DMA fragments.</p>

|Bits|Identifier|Access|Reset|                         Name                         |
|----|----------|------|-----|------------------------------------------------------|
|31:0|  cycles  |  rw  | 0x0 |csr.endpoint_interface.config.dma_timeout.cycles[31:0]|

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

- Absolute Address: 0x2000083C
- Base Offset: 0x1C
- Size: 0x4

<p>Common software-selected maximum memory fragment size for locally
initiated peer DMA transfers. The synthesis-time frame limit remains fixed.</p>

|Bits|Identifier|Access| Reset|                              Name                             |
|----|----------|------|------|---------------------------------------------------------------|
|31:0|   bytes  |  rw  |0x1FE0|csr.endpoint_interface.config.dma_max_fragment_size.bytes[31:0]|

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

- Absolute Address: 0x20000840
- Base Offset: 0x40
- Size: 0x1C

<p>Register file for the AXI4-Stream source and sink interfaces.</p>

|Offset|Identifier|                 Name                |
|------|----------|-------------------------------------|
| 0x00 |  source  |csr.endpoint_interface.axis_if.source|
| 0x10 |   sink   | csr.endpoint_interface.axis_if.sink |

## source register file

- Absolute Address: 0x20000840
- Base Offset: 0x0
- Size: 0xC

<p>Register file for the AXI4-Stream source interface.</p>

|Offset|Identifier|                     Name                    |
|------|----------|---------------------------------------------|
|  0x0 |   data   |  csr.endpoint_interface.axis_if.source.data |
|  0x4 |  control |csr.endpoint_interface.axis_if.source.control|
|  0x8 |  status  | csr.endpoint_interface.axis_if.source.status|

### data register

- Absolute Address: 0x20000840
- Base Offset: 0x0
- Size: 0x4

<p>Data register for the AXI4-Stream source interface.</p>

|Bits|Identifier|Access|Reset|                         Name                         |
|----|----------|------|-----|------------------------------------------------------|
|31:0|   tdata  |  rw  | 0x0 |csr.endpoint_interface.axis_if.source.data.tdata[31:0]|

#### tdata field

<p>32-bit data value for the AXI4-Stream source interface.</p>

### control register

- Absolute Address: 0x20000844
- Base Offset: 0x4
- Size: 0x4

<p>Control register for the AXI4-Stream source interface.</p>

| Bits|Identifier|Access|Reset|                          Name                          |
|-----|----------|------|-----|--------------------------------------------------------|
|  0  |  tvalid  |  rw  | 0x0 |  csr.endpoint_interface.axis_if.source.control.tvalid  |
|  8  |   tlast  |  rw  | 0x0 |   csr.endpoint_interface.axis_if.source.control.tlast  |
|19:16|   tkeep  |  rw  | 0x0 |csr.endpoint_interface.axis_if.source.control.tkeep[3:0]|

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

- Absolute Address: 0x20000848
- Base Offset: 0x8
- Size: 0x4

<p>Status register for the AXI4-Stream source interface.</p>

|Bits|Identifier|Access|Reset|                        Name                       |
|----|----------|------|-----|---------------------------------------------------|
|  0 |  tready  |   r  | 0x0 |csr.endpoint_interface.axis_if.source.status.tready|

#### tready field

<p>Indicates that the destination AXI4-Stream interface is ready to
receive data.</p>

## sink register file

- Absolute Address: 0x20000850
- Base Offset: 0x10
- Size: 0xC

<p>Register file for the AXI4-Stream sink interface.</p>

|Offset|Identifier|                    Name                   |
|------|----------|-------------------------------------------|
|  0x0 |   data   |  csr.endpoint_interface.axis_if.sink.data |
|  0x4 |  control |csr.endpoint_interface.axis_if.sink.control|
|  0x8 |  status  | csr.endpoint_interface.axis_if.sink.status|

### data register

- Absolute Address: 0x20000850
- Base Offset: 0x0
- Size: 0x4

<p>Data register for the AXI4-Stream sink interface.</p>

|Bits|Identifier|Access|Reset|                        Name                        |
|----|----------|------|-----|----------------------------------------------------|
|31:0|   tdata  |   r  |  —  |csr.endpoint_interface.axis_if.sink.data.tdata[31:0]|

#### tdata field

<p>32-bit data value for the AXI4-Stream sink interface.</p>

### control register

- Absolute Address: 0x20000854
- Base Offset: 0x4
- Size: 0x4

<p>Control register for the AXI4-Stream sink interface.</p>

|Bits|Identifier|Access|Reset|                       Name                       |
|----|----------|------|-----|--------------------------------------------------|
|  0 |  tready  |  rw  | 0x0 |csr.endpoint_interface.axis_if.sink.control.tready|

#### tready field

<p>Indicates that the AXI4-Stream sink interface is ready to accept a
data transfer. Once asserted by software, the field remains asserted until
a transfer occurs.</p>

### status register

- Absolute Address: 0x20000858
- Base Offset: 0x8
- Size: 0x4

<p>Status register for the AXI4-Stream sink interface.</p>

| Bits|Identifier|Access|Reset|                         Name                        |
|-----|----------|------|-----|-----------------------------------------------------|
|  0  |  tvalid  |   r  |  —  |  csr.endpoint_interface.axis_if.sink.status.tvalid  |
|  8  |   tlast  |   r  |  —  |   csr.endpoint_interface.axis_if.sink.status.tlast  |
|19:16|   tkeep  |   r  |  —  |csr.endpoint_interface.axis_if.sink.status.tkeep[3:0]|

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

- Absolute Address: 0x20000860
- Base Offset: 0x60
- Size: 0x20

<p>Endpoint-level DMA control and status for complete non-oETP Ethernet frames.
Frame data includes the Ethernet header and payload, but excludes the preamble,
Start Frame Delimiter (SFD), and Frame Check Sequence (FCS).</p>

|Offset|Identifier|                 Name                 |
|------|----------|--------------------------------------|
| 0x00 |    tx    |csr.endpoint_interface.non_oetp_dma.tx|
| 0x10 |    rx    |csr.endpoint_interface.non_oetp_dma.rx|

## tx register file

- Absolute Address: 0x20000860
- Base Offset: 0x0
- Size: 0x10

<p>Transmit DMA channel for complete non-oETP Ethernet frames.</p>

|Offset|    Identifier    |                           Name                          |
|------|------------------|---------------------------------------------------------|
|  0x0 |  buffer_address  |  csr.endpoint_interface.non_oetp_dma.tx.buffer_address  |
|  0x4 |   frame_length   |   csr.endpoint_interface.non_oetp_dma.tx.frame_length   |
|  0x8 |  command_status  |  csr.endpoint_interface.non_oetp_dma.tx.command_status  |
|  0xC |transferred_length|csr.endpoint_interface.non_oetp_dma.tx.transferred_length|

### buffer_address register

- Absolute Address: 0x20000860
- Base Offset: 0x0
- Size: 0x4

<p>Local memory address of the non-oETP Ethernet frame to transmit.</p>

|Bits|Identifier|Access|Reset|                              Name                              |
|----|----------|------|-----|----------------------------------------------------------------|
|31:0|   base   |  rw  | 0x0 |csr.endpoint_interface.non_oetp_dma.tx.buffer_address.base[31:0]|

#### base field

<p>32-bit byte address of the first byte of the transmit buffer.</p>

### frame_length register

- Absolute Address: 0x20000864
- Base Offset: 0x4
- Size: 0x4

<p>Length of the complete non-oETP Ethernet frame to transmit.</p>

|Bits|Identifier|Access|Reset|                              Name                             |
|----|----------|------|-----|---------------------------------------------------------------|
|31:0|   bytes  |  rw  | 0x0 |csr.endpoint_interface.non_oetp_dma.tx.frame_length.bytes[31:0]|

#### bytes field

<p>Frame length in bytes. Valid non-zero values shall not exceed
info.max_dma_frame_size_bytes.</p>

### command_status register

- Absolute Address: 0x20000868
- Base Offset: 0x8
- Size: 0x4

<p>Command and completion status for the non-oETP transmit DMA channel.</p>

| Bits| Identifier |Access|Reset|                                  Name                                 |
|-----|------------|------|-----|-----------------------------------------------------------------------|
|  8  |   request  |  rw  | 0x0 |     csr.endpoint_interface.non_oetp_dma.tx.command_status.request     |
|  9  |clear_errors|  rw  | 0x0 |   csr.endpoint_interface.non_oetp_dma.tx.command_status.clear_errors  |
|  16 |    idle    |   r  |  —  |       csr.endpoint_interface.non_oetp_dma.tx.command_status.idle      |
|  24 |    done    |   r  |  —  |       csr.endpoint_interface.non_oetp_dma.tx.command_status.done      |
|  25 |    error   |   r  |  —  |      csr.endpoint_interface.non_oetp_dma.tx.command_status.error      |
|31:28| error_code |   r  |  —  |csr.endpoint_interface.non_oetp_dma.tx.command_status.error_code[31:28]|

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

- Absolute Address: 0x2000086C
- Base Offset: 0xC
- Size: 0x4

<p>Number of bytes transferred for the most recently accepted transmit
request.</p>

|Bits|Identifier|Access|Reset|                                 Name                                |
|----|----------|------|-----|---------------------------------------------------------------------|
|31:0|   bytes  |   r  |  —  |csr.endpoint_interface.non_oetp_dma.tx.transferred_length.bytes[31:0]|

#### bytes field

<p>Actual number of bytes transferred. Hardware clears this field when
the next request is accepted.</p>

## rx register file

- Absolute Address: 0x20000870
- Base Offset: 0x10
- Size: 0x10

<p>Receive DMA channel for complete non-oETP Ethernet frames.</p>

|Offset|   Identifier  |                         Name                         |
|------|---------------|------------------------------------------------------|
|  0x0 | buffer_address| csr.endpoint_interface.non_oetp_dma.rx.buffer_address|
|  0x4 |buffer_capacity|csr.endpoint_interface.non_oetp_dma.rx.buffer_capacity|
|  0x8 | command_status| csr.endpoint_interface.non_oetp_dma.rx.command_status|
|  0xC |received_length|csr.endpoint_interface.non_oetp_dma.rx.received_length|

### buffer_address register

- Absolute Address: 0x20000870
- Base Offset: 0x0
- Size: 0x4

<p>Local memory address of the receive buffer for a non-oETP Ethernet frame.</p>

|Bits|Identifier|Access|Reset|                              Name                              |
|----|----------|------|-----|----------------------------------------------------------------|
|31:0|   base   |  rw  | 0x0 |csr.endpoint_interface.non_oetp_dma.rx.buffer_address.base[31:0]|

#### base field

<p>32-bit byte address of the first byte of the receive buffer.</p>

### buffer_capacity register

- Absolute Address: 0x20000874
- Base Offset: 0x4
- Size: 0x4

<p>Capacity of the receive buffer for one complete non-oETP Ethernet frame.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   bytes  |  rw  | 0x0 |csr.endpoint_interface.non_oetp_dma.rx.buffer_capacity.bytes[31:0]|

#### bytes field

<p>Receive-buffer capacity in bytes. Valid non-zero values shall not exceed
info.max_dma_frame_size_bytes.</p>

### command_status register

- Absolute Address: 0x20000878
- Base Offset: 0x8
- Size: 0x4

<p>Command and completion status for the non-oETP receive DMA channel.</p>

| Bits| Identifier |Access|Reset|                                  Name                                 |
|-----|------------|------|-----|-----------------------------------------------------------------------|
|  8  |   request  |  rw  | 0x0 |     csr.endpoint_interface.non_oetp_dma.rx.command_status.request     |
|  9  |clear_errors|  rw  | 0x0 |   csr.endpoint_interface.non_oetp_dma.rx.command_status.clear_errors  |
|  16 |    idle    |   r  |  —  |       csr.endpoint_interface.non_oetp_dma.rx.command_status.idle      |
|  17 |    armed   |   r  |  —  |      csr.endpoint_interface.non_oetp_dma.rx.command_status.armed      |
|  24 |    done    |   r  |  —  |       csr.endpoint_interface.non_oetp_dma.rx.command_status.done      |
|  25 |    error   |   r  |  —  |      csr.endpoint_interface.non_oetp_dma.rx.command_status.error      |
|31:28| error_code |   r  |  —  |csr.endpoint_interface.non_oetp_dma.rx.command_status.error_code[31:28]|

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

- Absolute Address: 0x2000087C
- Base Offset: 0xC
- Size: 0x4

<p>Length of the most recently received non-oETP Ethernet frame.</p>

|Bits|Identifier|Access|Reset|                               Name                               |
|----|----------|------|-----|------------------------------------------------------------------|
|31:0|   bytes  |   r  |  —  |csr.endpoint_interface.non_oetp_dma.rx.received_length.bytes[31:0]|

#### bytes field

<p>Actual number of frame bytes written to the receive buffer. Hardware
clears this field when the next request is accepted.</p>

## irq register file

- Absolute Address: 0x20000880
- Base Offset: 0x80
- Size: 0x14

<p>Endpoint-level interrupt control and claim interface. Interrupt events from peer
DMA, non-oETP DMA, direct AXI4-Stream transfers, and RMEM failures are serialized
through a shared event FIFO.</p>

|Offset| Identifier |                  Name                 |
|------|------------|---------------------------------------|
| 0x00 |   control  |   csr.endpoint_interface.irq.control  |
| 0x04 |event_enable|csr.endpoint_interface.irq.event_enable|
| 0x08 |   status   |   csr.endpoint_interface.irq.status   |
| 0x0C |    claim   |    csr.endpoint_interface.irq.claim   |
| 0x10 |  complete  |  csr.endpoint_interface.irq.complete  |

### control register

- Absolute Address: 0x20000880
- Base Offset: 0x0
- Size: 0x4

<p>Global interrupt-output control and interrupt-controller maintenance requests.</p>

|Bits|  Identifier |Access|Reset|                      Name                      |
|----|-------------|------|-----|------------------------------------------------|
|  0 |global_enable|  rw  | 0x0 |csr.endpoint_interface.irq.control.global_enable|
|  8 | clear_errors|  rw  | 0x0 | csr.endpoint_interface.irq.control.clear_errors|

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

- Absolute Address: 0x20000884
- Base Offset: 0x4
- Size: 0x4

<p>Enables generation of individual endpoint IRQ event classes. These fields
control event capture; irq.control.global_enable only masks the physical
IRQ output.</p>

|Bits|         Identifier         |Access|Reset|                                Name                                |
|----|----------------------------|------|-----|--------------------------------------------------------------------|
|  0 |      peer_dma_complete     |  rw  | 0x0 |      csr.endpoint_interface.irq.event_enable.peer_dma_complete     |
|  1 |  non_oetp_dma_tx_complete  |  rw  | 0x0 |  csr.endpoint_interface.irq.event_enable.non_oetp_dma_tx_complete  |
|  2 |  non_oetp_dma_rx_complete  |  rw  | 0x0 |  csr.endpoint_interface.irq.event_enable.non_oetp_dma_rx_complete  |
|  3 | non_oetp_direct_tx_complete|  rw  | 0x0 | csr.endpoint_interface.irq.event_enable.non_oetp_direct_tx_complete|
|  4 |non_oetp_direct_rx_available|  rw  | 0x0 |csr.endpoint_interface.irq.event_enable.non_oetp_direct_rx_available|
|  5 |         rmem_error         |  rw  | 0x0 |         csr.endpoint_interface.irq.event_enable.rmem_error         |

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

- Absolute Address: 0x20000888
- Base Offset: 0x8
- Size: 0x4

<p>Status of the endpoint IRQ event FIFO and its reservation mechanism.</p>

| Bits|   Identifier   |Access|Reset|                         Name                        |
|-----|----------------|------|-----|-----------------------------------------------------|
|  0  |  claim_pending |   r  |  —  |   csr.endpoint_interface.irq.status.claim_pending   |
|  1  |   credit_full  |   r  |  —  |    csr.endpoint_interface.irq.status.credit_full    |
|  2  |    overflow    |   r  |  —  |      csr.endpoint_interface.irq.status.overflow     |
|  3  |invalid_complete|   r  |  —  |  csr.endpoint_interface.irq.status.invalid_complete |
|  4  |  irq_asserted  |   r  |  —  |    csr.endpoint_interface.irq.status.irq_asserted   |
| 15:8|   fifo_level   |   r  |  —  |  csr.endpoint_interface.irq.status.fifo_level[7:0]  |
|23:16| reserved_count |   r  |  —  |csr.endpoint_interface.irq.status.reserved_count[7:0]|

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

- Absolute Address: 0x2000088C
- Base Offset: 0xC
- Size: 0x4

<p>Read-only view of the event at the head of the IRQ event FIFO. Reading this
register has no side effect, and all fields remain stable until a matching
irq.complete request removes the claim.</p>

| Bits|Identifier|Access|Reset|                      Name                     |
|-----|----------|------|-----|-----------------------------------------------|
| 10:0| peer_idx |   r  |  —  |csr.endpoint_interface.irq.claim.peer_idx[10:0]|
|14:11|  source  |   r  |  —  |  csr.endpoint_interface.irq.claim.source[3:0] |
|30:15| sequence |   r  |  —  |csr.endpoint_interface.irq.claim.sequence[15:0]|
|  31 |   valid  |   r  |  —  |     csr.endpoint_interface.irq.claim.valid    |

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

- Absolute Address: 0x20000890
- Base Offset: 0x10
- Size: 0x4

<p>Completion request for the current IRQ claim. Software acknowledges an event by
copying the complete 32-bit irq.claim value into this register.</p>

| Bits|Identifier|Access|Reset|                       Name                       |
|-----|----------|------|-----|--------------------------------------------------|
| 10:0| peer_idx |  rw  | 0x0 |csr.endpoint_interface.irq.complete.peer_idx[10:0]|
|14:11|  source  |  rw  | 0x0 |  csr.endpoint_interface.irq.complete.source[3:0] |
|30:15| sequence |  rw  | 0x0 |csr.endpoint_interface.irq.complete.sequence[15:0]|
|  31 |   valid  |  rw  | 0x0 |     csr.endpoint_interface.irq.complete.valid    |

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

- Absolute Address: 0x20000900
- Base Offset: 0x100
- Size: 0x70

<p>Register file for remote peer configuration and memory region information.</p>

|Offset|Identifier|                         Name                        |
|------|----------|-----------------------------------------------------|
| 0x00 | entry[0] |csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1]|
| 0x1C | entry[1] |csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1]|
| 0x38 | entry[2] |csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1]|
| 0x54 | entry[3] |csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1]|

## entry register file

- Absolute Address: 0x20000900
- Base Offset: 0x0
- Size: 0x1C
- Array Dimensions: [4]
- Array Stride: 0x1C
- Total Size: 0x70

<p>Register file for a single remote peer configuration and memory region
information.</p>

|Offset|  Identifier  |                                Name                                |
|------|--------------|--------------------------------------------------------------------|
| 0x00 |  mac_address |  csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].mac_address |
| 0x08 | rmem_address | csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].rmem_address |
| 0x0C | local_address| csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].local_address|
| 0x10 |remote_address|csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].remote_address|
| 0x14 |     size     |     csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].size     |
| 0x18 |      dma     |      csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma     |

### mac_address register

- Absolute Address: 0x20000900
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

- Absolute Address: 0x20000908
- Base Offset: 0x8
- Size: 0x4

<p>Address offset of the virtual memory region corresponding to the remote
peer's memory.</p>

|Bits|Identifier|Access|Reset|                                      Name                                     |
|----|----------|------|-----|-------------------------------------------------------------------------------|
|31:0|  offset  |  rw  |  —  |csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].rmem_address.offset[31:0]|

#### offset field

<p>32-bit byte offset of the virtual memory region corresponding to the
remote peer's memory. The value shall be aligned to a 32-bit word boundary.</p>

### local_address register

- Absolute Address: 0x2000090C
- Base Offset: 0xC
- Size: 0x4

<p>Start address of the local memory region for DMA transfers.</p>

|Bits|Identifier|Access|Reset|                                     Name                                     |
|----|----------|------|-----|------------------------------------------------------------------------------|
|31:0|   base   |  rw  |  —  |csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].local_address.base[31:0]|

#### base field

<p>Word-aligned 32-bit start address of the local memory region for
DMA transfers.</p>

### remote_address register

- Absolute Address: 0x20000910
- Base Offset: 0x10
- Size: 0x4

<p>Start address of the remote peer's memory region.</p>

|Bits|Identifier|Access|Reset|                                      Name                                     |
|----|----------|------|-----|-------------------------------------------------------------------------------|
|31:0|   base   |  rw  |  —  |csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].remote_address.base[31:0]|

#### base field

<p>Word-aligned 32-bit start address of the remote peer's memory region.</p>

### size register

- Absolute Address: 0x20000914
- Base Offset: 0x14
- Size: 0x4

<p>Size of the remote peer's memory region.</p>

|Bits|Identifier|Access|Reset|                                 Name                                 |
|----|----------|------|-----|----------------------------------------------------------------------|
|31:0|   bytes  |  rw  |  —  |csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].size.bytes[31:0]|

#### bytes field

<p>32-bit size of the remote peer's memory region in bytes.</p>

### dma register

- Absolute Address: 0x20000918
- Base Offset: 0x18
- Size: 0x4

<p>DMA/RMEM configuration and control for the remote peer, with shared
sticky error reporting. RMEM and bulk DMA retain separate IRQ event classes.</p>

| Bits| Identifier|Access|Reset|                                    Name                                   |
|-----|-----------|------|-----|---------------------------------------------------------------------------|
| 1:0 |    mode   |  rw  |  —  |    csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.mode[1:0]    |
|  2  | irq_enable|  rw  | 0x0 |    csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.irq_enable   |
|  8  |  request  |  rw  | 0x0 |   csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.request[8:8]  |
|  9  |clear_error|  rw  | 0x0 |   csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.clear_error   |
|  16 |    idle   |   r  |  —  |   csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.idle[16:16]   |
|  24 |    done   |   r  |  —  |   csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.done[24:24]   |
|  25 |   error   |   r  |  —  |   csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.error[25:25]  |
|31:28| error_code|   r  |  —  |csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.error_code[31:28]|

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

## entry register file

- Absolute Address: 0x2000091C
- Base Offset: 0x0
- Size: 0x1C
- Array Dimensions: [4]
- Array Stride: 0x1C
- Total Size: 0x70

<p>Register file for a single remote peer configuration and memory region
information.</p>

|Offset|  Identifier  |                                Name                                |
|------|--------------|--------------------------------------------------------------------|
| 0x00 |  mac_address |  csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].mac_address |
| 0x08 | rmem_address | csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].rmem_address |
| 0x0C | local_address| csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].local_address|
| 0x10 |remote_address|csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].remote_address|
| 0x14 |     size     |     csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].size     |
| 0x18 |      dma     |      csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma     |

### mac_address register

- Absolute Address: 0x2000091C
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

- Absolute Address: 0x20000924
- Base Offset: 0x8
- Size: 0x4

<p>Address offset of the virtual memory region corresponding to the remote
peer's memory.</p>

|Bits|Identifier|Access|Reset|                                      Name                                     |
|----|----------|------|-----|-------------------------------------------------------------------------------|
|31:0|  offset  |  rw  |  —  |csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].rmem_address.offset[31:0]|

#### offset field

<p>32-bit byte offset of the virtual memory region corresponding to the
remote peer's memory. The value shall be aligned to a 32-bit word boundary.</p>

### local_address register

- Absolute Address: 0x20000928
- Base Offset: 0xC
- Size: 0x4

<p>Start address of the local memory region for DMA transfers.</p>

|Bits|Identifier|Access|Reset|                                     Name                                     |
|----|----------|------|-----|------------------------------------------------------------------------------|
|31:0|   base   |  rw  |  —  |csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].local_address.base[31:0]|

#### base field

<p>Word-aligned 32-bit start address of the local memory region for
DMA transfers.</p>

### remote_address register

- Absolute Address: 0x2000092C
- Base Offset: 0x10
- Size: 0x4

<p>Start address of the remote peer's memory region.</p>

|Bits|Identifier|Access|Reset|                                      Name                                     |
|----|----------|------|-----|-------------------------------------------------------------------------------|
|31:0|   base   |  rw  |  —  |csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].remote_address.base[31:0]|

#### base field

<p>Word-aligned 32-bit start address of the remote peer's memory region.</p>

### size register

- Absolute Address: 0x20000930
- Base Offset: 0x14
- Size: 0x4

<p>Size of the remote peer's memory region.</p>

|Bits|Identifier|Access|Reset|                                 Name                                 |
|----|----------|------|-----|----------------------------------------------------------------------|
|31:0|   bytes  |  rw  |  —  |csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].size.bytes[31:0]|

#### bytes field

<p>32-bit size of the remote peer's memory region in bytes.</p>

### dma register

- Absolute Address: 0x20000934
- Base Offset: 0x18
- Size: 0x4

<p>DMA/RMEM configuration and control for the remote peer, with shared
sticky error reporting. RMEM and bulk DMA retain separate IRQ event classes.</p>

| Bits| Identifier|Access|Reset|                                    Name                                   |
|-----|-----------|------|-----|---------------------------------------------------------------------------|
| 1:0 |    mode   |  rw  |  —  |    csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.mode[1:0]    |
|  2  | irq_enable|  rw  | 0x0 |    csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.irq_enable   |
|  8  |  request  |  rw  | 0x0 |   csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.request[8:8]  |
|  9  |clear_error|  rw  | 0x0 |   csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.clear_error   |
|  16 |    idle   |   r  |  —  |   csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.idle[16:16]   |
|  24 |    done   |   r  |  —  |   csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.done[24:24]   |
|  25 |   error   |   r  |  —  |   csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.error[25:25]  |
|31:28| error_code|   r  |  —  |csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.error_code[31:28]|

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

## entry register file

- Absolute Address: 0x20000938
- Base Offset: 0x0
- Size: 0x1C
- Array Dimensions: [4]
- Array Stride: 0x1C
- Total Size: 0x70

<p>Register file for a single remote peer configuration and memory region
information.</p>

|Offset|  Identifier  |                                Name                                |
|------|--------------|--------------------------------------------------------------------|
| 0x00 |  mac_address |  csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].mac_address |
| 0x08 | rmem_address | csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].rmem_address |
| 0x0C | local_address| csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].local_address|
| 0x10 |remote_address|csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].remote_address|
| 0x14 |     size     |     csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].size     |
| 0x18 |      dma     |      csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma     |

### mac_address register

- Absolute Address: 0x20000938
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

- Absolute Address: 0x20000940
- Base Offset: 0x8
- Size: 0x4

<p>Address offset of the virtual memory region corresponding to the remote
peer's memory.</p>

|Bits|Identifier|Access|Reset|                                      Name                                     |
|----|----------|------|-----|-------------------------------------------------------------------------------|
|31:0|  offset  |  rw  |  —  |csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].rmem_address.offset[31:0]|

#### offset field

<p>32-bit byte offset of the virtual memory region corresponding to the
remote peer's memory. The value shall be aligned to a 32-bit word boundary.</p>

### local_address register

- Absolute Address: 0x20000944
- Base Offset: 0xC
- Size: 0x4

<p>Start address of the local memory region for DMA transfers.</p>

|Bits|Identifier|Access|Reset|                                     Name                                     |
|----|----------|------|-----|------------------------------------------------------------------------------|
|31:0|   base   |  rw  |  —  |csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].local_address.base[31:0]|

#### base field

<p>Word-aligned 32-bit start address of the local memory region for
DMA transfers.</p>

### remote_address register

- Absolute Address: 0x20000948
- Base Offset: 0x10
- Size: 0x4

<p>Start address of the remote peer's memory region.</p>

|Bits|Identifier|Access|Reset|                                      Name                                     |
|----|----------|------|-----|-------------------------------------------------------------------------------|
|31:0|   base   |  rw  |  —  |csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].remote_address.base[31:0]|

#### base field

<p>Word-aligned 32-bit start address of the remote peer's memory region.</p>

### size register

- Absolute Address: 0x2000094C
- Base Offset: 0x14
- Size: 0x4

<p>Size of the remote peer's memory region.</p>

|Bits|Identifier|Access|Reset|                                 Name                                 |
|----|----------|------|-----|----------------------------------------------------------------------|
|31:0|   bytes  |  rw  |  —  |csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].size.bytes[31:0]|

#### bytes field

<p>32-bit size of the remote peer's memory region in bytes.</p>

### dma register

- Absolute Address: 0x20000950
- Base Offset: 0x18
- Size: 0x4

<p>DMA/RMEM configuration and control for the remote peer, with shared
sticky error reporting. RMEM and bulk DMA retain separate IRQ event classes.</p>

| Bits| Identifier|Access|Reset|                                    Name                                   |
|-----|-----------|------|-----|---------------------------------------------------------------------------|
| 1:0 |    mode   |  rw  |  —  |    csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.mode[1:0]    |
|  2  | irq_enable|  rw  | 0x0 |    csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.irq_enable   |
|  8  |  request  |  rw  | 0x0 |   csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.request[8:8]  |
|  9  |clear_error|  rw  | 0x0 |   csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.clear_error   |
|  16 |    idle   |   r  |  —  |   csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.idle[16:16]   |
|  24 |    done   |   r  |  —  |   csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.done[24:24]   |
|  25 |   error   |   r  |  —  |   csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.error[25:25]  |
|31:28| error_code|   r  |  —  |csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.error_code[31:28]|

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

## entry register file

- Absolute Address: 0x20000954
- Base Offset: 0x0
- Size: 0x1C
- Array Dimensions: [4]
- Array Stride: 0x1C
- Total Size: 0x70

<p>Register file for a single remote peer configuration and memory region
information.</p>

|Offset|  Identifier  |                                Name                                |
|------|--------------|--------------------------------------------------------------------|
| 0x00 |  mac_address |  csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].mac_address |
| 0x08 | rmem_address | csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].rmem_address |
| 0x0C | local_address| csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].local_address|
| 0x10 |remote_address|csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].remote_address|
| 0x14 |     size     |     csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].size     |
| 0x18 |      dma     |      csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma     |

### mac_address register

- Absolute Address: 0x20000954
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

- Absolute Address: 0x2000095C
- Base Offset: 0x8
- Size: 0x4

<p>Address offset of the virtual memory region corresponding to the remote
peer's memory.</p>

|Bits|Identifier|Access|Reset|                                      Name                                     |
|----|----------|------|-----|-------------------------------------------------------------------------------|
|31:0|  offset  |  rw  |  —  |csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].rmem_address.offset[31:0]|

#### offset field

<p>32-bit byte offset of the virtual memory region corresponding to the
remote peer's memory. The value shall be aligned to a 32-bit word boundary.</p>

### local_address register

- Absolute Address: 0x20000960
- Base Offset: 0xC
- Size: 0x4

<p>Start address of the local memory region for DMA transfers.</p>

|Bits|Identifier|Access|Reset|                                     Name                                     |
|----|----------|------|-----|------------------------------------------------------------------------------|
|31:0|   base   |  rw  |  —  |csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].local_address.base[31:0]|

#### base field

<p>Word-aligned 32-bit start address of the local memory region for
DMA transfers.</p>

### remote_address register

- Absolute Address: 0x20000964
- Base Offset: 0x10
- Size: 0x4

<p>Start address of the remote peer's memory region.</p>

|Bits|Identifier|Access|Reset|                                      Name                                     |
|----|----------|------|-----|-------------------------------------------------------------------------------|
|31:0|   base   |  rw  |  —  |csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].remote_address.base[31:0]|

#### base field

<p>Word-aligned 32-bit start address of the remote peer's memory region.</p>

### size register

- Absolute Address: 0x20000968
- Base Offset: 0x14
- Size: 0x4

<p>Size of the remote peer's memory region.</p>

|Bits|Identifier|Access|Reset|                                 Name                                 |
|----|----------|------|-----|----------------------------------------------------------------------|
|31:0|   bytes  |  rw  |  —  |csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].size.bytes[31:0]|

#### bytes field

<p>32-bit size of the remote peer's memory region in bytes.</p>

### dma register

- Absolute Address: 0x2000096C
- Base Offset: 0x18
- Size: 0x4

<p>DMA/RMEM configuration and control for the remote peer, with shared
sticky error reporting. RMEM and bulk DMA retain separate IRQ event classes.</p>

| Bits| Identifier|Access|Reset|                                    Name                                   |
|-----|-----------|------|-----|---------------------------------------------------------------------------|
| 1:0 |    mode   |  rw  |  —  |    csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.mode[1:0]    |
|  2  | irq_enable|  rw  | 0x0 |    csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.irq_enable   |
|  8  |  request  |  rw  | 0x0 |   csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.request[8:8]  |
|  9  |clear_error|  rw  | 0x0 |   csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.clear_error   |
|  16 |    idle   |   r  |  —  |   csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.idle[16:16]   |
|  24 |    done   |   r  |  —  |   csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.done[24:24]   |
|  25 |   error   |   r  |  —  |   csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.error[25:25]  |
|31:28| error_code|   r  |  —  |csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.error_code[31:28]|

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

- Absolute Address: 0x20000C00
- Base Offset: 0x400
- Size: 0x400

<p>Virtual memory region for all remote peers, with offsets and sizes defined in the
peers regfile.</p>

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
