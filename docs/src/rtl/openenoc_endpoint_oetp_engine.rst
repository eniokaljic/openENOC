.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-oetp-engine:

oETP Engine -- openenoc_endpoint_oetp_engine
============================================

Parses and assembles Ethernet transport transactions, matches responses, and
supervises remote-operation completion.

**Source:** :download:`openenoc_endpoint_oetp_engine.sv <../../../hw/rtl/core/openenoc_endpoint_oetp_engine.sv>`.

Parameters
----------

.. list-table:: Parameters
   :class: rtl-reference-table
   :header-rows: 1
   :widths: 30 18 22 30

   * - Name
     - Default value
     - Allowed values
     - Description
   * - ``MAX_RAW_FRAME_SIZE``
     - ``8192``
     - 36..8192 bytes
     - Synthesized frame ceiling excluding FCS; reserves 32 bytes for the largest
       peer-frame overhead.

Signals
-------

Interface ports contain channels in both directions. The table identifies
the selected modport or stream role; member directions follow that interface.

.. list-table:: Public signals and interfaces
   :class: rtl-reference-table
   :header-rows: 1
   :widths: 26 27 17 30

   * - Name
     - Type
     - Direction / role
     - Description
   * - ``clk``
     - ``logic``
     - input
     - Clock for this component or interface domain.
   * - ``rst``
     - ``logic``
     - input
     - Active-high reset of transaction and control state.
   * - ``endpoint_if``
     - ``openenoc_endpoint_if.core``
     - bidirectional (core)
     - Endpoint configuration, commands, status, and external scalar-memory access.
   * - ``s_axis_local``
     - ``taxi_axis_if.snk``
     - sink
     - Raw/direct frames or memory payloads from the local paths.
   * - ``m_axis_local``
     - ``taxi_axis_if.src``
     - source
     - Received raw/direct frames or memory payloads to the local paths.
   * - ``s_axis_eth``
     - ``taxi_axis_if.snk``
     - sink
     - Received Ethernet frames, excluding preamble and FCS.
   * - ``m_axis_eth``
     - ``taxi_axis_if.src``
     - source
     - Transmitted Ethernet frames, excluding preamble and FCS.
   * - ``peer_lookup_if``
     - ``openenoc_peer_lookup_if.mst``
     - bidirectional (mst)
     - Peer-table query client and coherent response snapshot.
   * - ``initiator_if``
     - ``openenoc_dma_transfer_if.executor``
     - bidirectional (executor)
     - Commands and status for locally initiated remote transactions.
   * - ``responder_if``
     - ``openenoc_dma_transfer_if.requester``
     - bidirectional (requester)
     - Commands and status for servicing received remote transactions.

Architecture and operation
--------------------------

RTL boundary
~~~~~~~~~~~~

The block uses ``clk/rst`` and the generated ``endpoint_if`` configuration.
``s_axis_local/m_axis_local`` connect the shared local stream paths, while
``s_axis_eth/m_axis_eth`` connect Ethernet transport. ``peer_lookup_if`` is
the shared peer-table client. ``initiator_if`` executes locally initiated
commands and ``responder_if`` requests memory servicing for received commands;
both use :ref:`rtl-dma-transfer-if`. There is no memory-master or CPUIF port.
Memory access, scalar RMEM execution, CSR error ownership, and IRQ producers
belong to :ref:`rtl-dma-engine`.

Implementation status and scope
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``openenoc_endpoint_oetp_engine`` block owns Ethernet/oETP parsing and
assembly, Request ID allocation and response matching, multicast response
suppression, and response timeouts. It exchanges commands, data, and completions
with the DMA engine, which owns all memory access. The RTL implements all nine
commands, source/Request ID matching, both response timers, streaming bulk data,
EndOfData verification, multicast writes, and configured raw-frame routing.
Scalar RMEM initiation and execution are implemented in the DMA engine.

The protocol overview and command encodings are part of
:ref:`oetp-protocol`. The following sections retain the detailed engine design,
internal interface contract, and implementation details.
Confirmed decisions are Magic = ``0x0E``, an 8192-byte Ethernet frame limit
excluding FCS, the name Request ID, and BitEnable for RMEM writes only.
Multicast RMEM and DMA writes are also supported without request responses.
Version 1 uses sequential request-response transactions without protocol
credits or automatic retransmission. Multicast delivery is best effort.
All four-byte parameters use little-endian encoding. Request IDs reset only
with the engine/endpoint hard reset; counter-wrap collisions invalidate the
older outstanding request with a timeout outcome. A zero BitEnable is a
successful no-op. RMEM timeout completes with acknowledgement and a CSR error
record; failed reads return all ones. Multicast receivers use a common ``config.multicast_address``
alongside their individual ``config.mac_address``.
The command codes and parameter layouts below are assigned, including a
32-bit EndOfData trailer on DMA_WRITE_REQ and DMA_READ_RSP. Wire causes 1..7
and local/remote CSR encoding are assigned. Memory/protocol
ownership and the internal stream contract below are confirmed.
The implemented state machines and verification scope are described below.
VLAN tags, automatic retries, duplicate suppression, and soft reset are outside
this version.

The assigned commands cover transparent 32-bit Remote Memory (RMEM) accesses
and bulk DMA reads and writes, matching the existing endpoint interfaces.

Established encapsulation
~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: ../../images/openENOC-oETP-PDU.svg
   :align: center
   :width: 100%

   oETP PDU encapsulation from the architecture.

Offsets are measured from the first destination MAC octet. The figure
describes an untagged frame; VLAN support would change these offsets and
needs an explicit decision.

.. list-table:: Frame fields
   :header-rows: 1
   :widths: 20 30 15 35

   * - Offset
     - Field
     - Size
     - Description
   * - 0
     - Destination MAC
     - 6 bytes
     - Destination endpoint or Ethernet group.
   * - 6
     - Source MAC
     - 6 bytes
     - Sending endpoint.
   * - 12
     - EtherType
     - 2 bytes
     - ``0x88B5``; octets ``88 B5``.
   * - 14
     - Magic
     - 1 byte
     - Protocol discriminator: ``0x0E``.
   * - 15
     - Cmd
     - 1 byte
     - Command selector; assigned values are listed below.
   * - 16 + 4(i - 1)
     - Parameter i
     - 4 bytes
     - Command-specific word, for i = 1 through N.
   * - After the PDU
     - Ethernet padding, if required
     - Variable
     - Outside the logical PDU.
   * - After padding
     - FCS
     - 4 bytes
     - Added/checked by the external MAC; absent on on-chip links.

The first parameter starts at frame offset 16. Parameters have 32-bit alignment
relative to the untagged frame start, although the oETP header is only two bytes.
AXIS byte-lane placement does not change wire octet order. ``0x88B5`` is a local
experimental EtherType, rather than an exclusive oETP allocation; see
`RFC 9542, Section 3 <https://www.rfc-editor.org/rfc/rfc9542.html#section-3>`_.

Lengths, MTU, and padding
^^^^^^^^^^^^^^^^^^^^^^^^^

The Ethernet frame limit counts from Destination MAC through the last payload
or padding byte. It excludes FCS, preamble, and SFD. The external MAC can
therefore transmit up to 8196 bytes including FCS. The logical PDU has length::

   L_FRAME_MAX = 8192                  # without FCS
   M = L_FRAME_MAX - 14 = 8178         # Ethernet payload budget
   L_PDU = 2 + 4*N
   L_PDU_max(M) = 2 + 4*floor((M - 2)/4)

The PDU envelope is consequently **6..8178 bytes**, or N = 1..2044. This
replaces the original diagram's 8998-byte ceiling. Each command's layout
further constrains its valid lengths. Links carrying maximum frames must
support this configured frame size; a smaller path MTU reduces the limit.
For an Ethernet payload MTU of 1500 bytes, the largest PDU is 1498 bytes.

The 8192-byte limit is an openENOC integration/design limit. The current
endpoint DMA uses that value; TAXI descriptor length widths are parameterized,
rather than universally hard-coded to 8192 bytes.

An external untagged Ethernet MAC pads short payloads to at least 46 bytes,
producing a minimum 64-byte frame including FCS. Padding is not an oETP
parameter; see the `AMD Ethernet MAC padding description
<https://docs.amd.com/r/en-US/pg135-axi-ethernetlite/Pad>`_. On-chip frames can
carry an unpadded PDU; an off-chip receiver may receive Ethernet padding.
The oETP engine emits the logical PDU without Ethernet minimum-frame padding.
The external MAC alone adds that padding when the frame leaves the chip.

Fixed commands determine their logical length from
Cmd. A DMA write request uses its Length parameter; a DMA read reply obtains
the expected data length from the outstanding context selected by Request ID.
Accept either the exact logical length or, for a PDU shorter than 46 bytes,
the frame padded to 46 payload bytes. Reject truncation and other trailing
lengths. Ignore Ethernet padding values on receive; their generation belongs
to the external MAC, not the oETP engine. Four-byte data-parameter padding
remains zero on transmit and is ignored on receive. TLAST
alone cannot identify the end of a short logical PDU received from a MAC.

DMA_WRITE_REQ and DMA_READ_RSP therefore end with the assigned 32-bit
EndOfData value ``0xE0D0E0D0``, serialized as ``D0 E0 D0 E0``. It follows the
rounded-up Data parameter array, before Ethernet padding. Relative to the
PDU start its offset is ``14 + 4*ceil(Length/4)`` for DMA_WRITE_REQ and
``6 + 4*ceil(ExpectedLength/4)`` for DMA_READ_RSP. Add 14 for frame offsets.
These are fixed expected positions, not a delimiter search: arbitrary memory
data may contain this value without ending the transfer. The trailer is never
forwarded over the memory-data AXIS path or written to memory.

Emit EndOfData only after exactly Length bytes and a successful local DMA
read completion. Omit it on failure, even if all data bytes have already been
emitted. Zero-filled Ethernet padding cannot replace any missing nonzero
trailer octet. A missing, incomplete, or incorrect EndOfData fails the
received DMA operation with remote CSR code 10. This is a completion marker,
not a checksum or a guarantee of buffer atomicity. RMEM commands,
DMA_READ_REQ, DMA_WRITE_RSP, and ERROR_RSP have no EndOfData parameter.

The external TX MAC must generate zero-filled padding. The bundled TAXI GMII
transmitter writes zero in its padding state. The external RX MAC uses
store-and-forward with ``RX_DROP_BAD_FRAME`` enabled, so invalid-FCS frames
never enter oETP. A valid Ethernet frame may still carry a deliberately
shortened oETP transfer and must pass the protocol checks above.

MAC addressing
^^^^^^^^^^^^^^

In conventional bit numbering, bit 0 of the first MAC octet selects individual
or group addressing, and bit 1 selects universal or local administration.
The example prefixes ``02:0E:0C`` and ``03:0E:0C`` are local unicast and local
group prefixes, not claims to an assigned vendor OUI. See `RFC 9542,
Section 2.1.1 <https://www.rfc-editor.org/rfc/rfc9542.html#section-2.1.1>`_.

Read requests use unicast destinations. RMEM_WRITE_REQ and DMA_WRITE_REQ
support both unicast and multicast/group destinations. Reply behavior is
selected by the destination MAC's I/G bit, rather than a new Cmd or Control
field::

   is_group = (DestinationMACOctet0 & 0x01) != 0
   expect_write_reply = not is_group

For a group-addressed write, the initiator does not wait for a reply and the
responder sends neither a success response nor ERROR_RSP. The group bit also
covers the Ethernet broadcast address: response suppression applies to it
too. For an incoming oETP frame, the destination I/G bit selects the configured
address to compare. Individual destinations must equal ``config.mac_address``;
group destinations must equal ``config.multicast_address``. There is no implicit
acceptance of other groups or broadcast traffic. A zero multicast address, its
reset value, cannot match a group destination and disables oETP group reception.
Broadcast is accepted only when ``multicast_address`` is configured to all ones.

The master uses an individual/unicast local MAC and configures the group MAC
as its outgoing peer destination. All N slave endpoints configure the same
group MAC in ``config.multicast_address``, while retaining their own unique
unicast ``config.mac_address``. Each slave configures the master's unicast
MAC in its own peer table. For bulk replication, the master entry uses mode 3
(mirror local to remote), and the corresponding slave entry uses mode 2
(permit incoming DMA writes). RMEM replication uses mode 1 at both ends.
This realizes one-master-to-N-slave best-effort memory replication.

An Ethernet source address has its group bit clear; see
`IEEE 802.3 address-field definition, Section 3.2.3
<https://www.ieee802.org/3/as/public/0503/3d0_1_CMP.pdf>`_. A configured group
MAC consequently serves as a receive destination, not an outgoing source
address. Outgoing oETP frames use the unicast ``config.mac_address`` as Source
MAC. Separating the two registers lets a slave also participate in ordinary
unicast operations without reconfiguring its group membership.

The receiver resolves the unicast source MAC to its own peer table for access
policy and address validation; the group destination is not a substitute for
the source-peer lookup. Local peer indices are not transmitted: the endpoints
can assign different indices to each other. Group-addressed read requests
are rejected locally without transmission; receivers discard any such request
without a response. The raw non-oETP receive mode does not define oETP group
membership.

Engine responsibilities and internal transport
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The DMA engine owns all memory access: the CSR-facing RMEM CPUIF slave, the
local CPUIF master used by received RMEM operations, and local AXI bulk DMA.
It owns initiating address translation, memory-window validation, fragmentation,
local completion, the shared peer error status, and the distinct DMA/RMEM IRQ
producers. A valid zero-BitEnable RMEM write is handled there as a no-op.

The oETP engine owns Ethernet/oETP parsing and assembly, header and data-word
padding handling, receive-side Ethernet padding removal, MAC/source-peer
identification, Request ID allocation and matching,
multicast response suppression, and response timeouts. It has no memory-master
or CPUIF port. Timeout is returned as an error completion; the DMA engine
terminates the local RMEM access or aborts the remainder of the DMA block.

``openenoc_dma_transfer_if`` is instantiated in both initiating and responding
directions. ``req_kind`` / ``cpl_kind`` distinguish bulk DMA (0) from RMEM (1),
independently of the existing READ/WRITE ``req_op`` / ``cpl_op``. RMEM has a
four-byte length and uses ``req_biten`` and ``req_wdata`` for writes and
``cpl_rdata`` for reads, all 32 bits wide. These scalar fields are unused for
bulk DMA. A four-byte bulk operation remains DMA; Length alone cannot select
RMEM. Local peer, sequence, and last metadata remain on the common interface.
Internal metadata does not add wire fields beyond the assigned command layouts.

The companion AXIS carries the following bytes in either direction:

.. list-table:: Internal DMA/oETP data contract
   :header-rows: 1
   :widths: 22 43 35

   * - Transfer class
     - AXIS contents
     - Address/control information
   * - Non-oETP DMA (``ROUTE_NON_OETP_DMA``)
     - Complete Ethernet frame: Destination MAC, Source MAC, EtherType, payload,
       and any Ethernet padding. No preamble, SFD, or FCS.
     - Raw DMA descriptor controls the memory buffer. Headers are preserved.
   * - oETP bulk DMA (``ROUTE_PEER``)
     - Exactly Length bytes from the memory-side range
       ``[Address, Address + Length - 1]``, in increasing address order.
       No Ethernet/oETP headers, EndOfData, or either form of padding.
     - Address, Length, and operation travel on the command interface and saved
       DMA context; they are not prefixed to the AXIS data.
   * - RMEM
     - No AXIS payload.
     - The single data word and BitEnable travel on command/completion fields.

Internal ``TDEST`` remains ``{route[1:0], peer_idx}``, and ``TID`` carries the
local fragment sequence. ``TUSER[0]`` carries LAST (the final fragment of the
block), while ``TUSER[1]`` identifies the local command context: 0 for initiator,
1 for responder. Both bits remain stable on every beat until accepted TLAST,
including during backpressure. The role resolves equal peer/sequence values
on the independent initiating and responding command paths:

.. list-table:: Bulk AXIS transfer roles
   :header-rows: 1
   :widths: 22 53 25

   * - Direction
     - Wire operation associated with the memory bytes
     - ``TUSER[1]``
   * - DMA to oETP
     - Locally initiated DMA_WRITE_REQ
     - 0 (initiator)
   * - DMA to oETP
     - DMA_READ_RSP servicing a received DMA_READ_REQ
     - 1 (responder)
   * - oETP to DMA
     - DMA_READ_RSP matching a locally initiated DMA_READ_REQ
     - 0 (initiator)
   * - oETP to DMA
     - Received DMA_WRITE_REQ
     - 1 (responder)

A peer still has one configured DMA mode. Mode 2 permits a locally initiated
read and a received write; mode 3 permits a locally initiated write and a
received read. These complementary operations can share a peer and sequence,
so the role cannot be inferred from those values or from the peer's mode.
Raw non-oETP and direct CSR streams use role 0. RMEM has no AXIS payload.
The role is internal metadata; it adds no CSR field or Ethernet/oETP wire bit.

The agreed streaming contract includes terminal fragment outcomes, separate
from data TVALID/TLAST. A producer's first TVALID does not certify that its entire
AXI read succeeded. The DMA engine must make the final source-read status
available to the oETP engine before EndOfData emission; the responder read's
completion provides that status, while the initiating write path still needs
an equivalent addition to the common transfer interface. Payload remains
streamed while that status is pending.

On RX, a peer write can finish its memory-data AXIS before the subsequent
EndOfData/complete-frame check. Carry that terminal protocol outcome back to
the DMA status owner with the accepted responder peer and local sequence
context. Join it with local memory completion before reporting final success or an error
event. A protocol failure reports CSR code 10 even when the memory write
completed with the expected byte count. The ``rx_status`` channel carries this
late outcome, while ``req_rx_status`` tells DMA to wait for it before completing
the received write. Incoming read-response failure travels on the
initiator completion channel. Do not overload the existing TUSER[0] final-block
flag with a payload error or include EndOfData in the memory stream.

Terminal status uses a ready/valid handshake independently of payload progress;
the producer holds the status and its context stable until accepted. Status
must identify the command path, peer, and sequence and remain available even
when payload TLAST was accepted earlier. A successful transfer waits for both
its required terminal protocol outcome and local memory completion. These
status paths are implemented in :ref:`rtl-dma-transfer-if`.

On failure or timeout, stop scheduling the block's remaining fragments and
finish any started wire frame without EndOfData. Drain the remainder of an
accepted receive frame through TLAST without submitting additional memory
bytes. Already accepted AXI transactions and AXIS activity must finish or be
safely drained before releasing their context. Bytes already written remain
modified; abort does not roll them back. Do not accept a replacement operation
into that context until old payload and status activity can no longer be
mistaken for the replacement. Hard reset clears the endpoint's contexts and
FIFOs as specified below.

For bulk writes, the initiating stream contains the local source bytes while
the command carries the translated remote destination address. The receiver
writes those bytes into its addressed local range. For reads, the responding
stream contains the responder's source bytes and the initiator writes them
using its saved local destination. Address translation never changes the byte
stream or adds an address word to it.

TKEEP marks actual valid bytes, including a partial final beat. TLAST ends one
complete raw frame or one memory fragment. Sequence/TID, route/peer TDEST,
LAST/TUSER[0], and role/TUSER[1] retain their internal meanings. Four-byte PDU
padding is added on transmit and removed on receive by oETP. Ethernet minimum-frame padding is
added only by an external MAC and ignored by the oETP receiver. Neither form
of padding may become bulk DMA memory writes. Non-oETP Ethernet padding remains
part of its raw frame.

Every started AXIS frame or memory fragment is assumed to end with an accepted
TLAST, including a shortened transfer caused by an operation error. A stream
that omits TLAST violates this transport contract; v1 has no separate
missing-TLAST watchdog and does not infer a new frame boundary from subsequent
Ethernet header bytes. If another frame continues the same unterminated stream,
excess length or a missing/incorrect EndOfData at its expected position can
identify the malformed DMA PDU. The receiver then drains through the eventual
TLAST; it cannot reconstruct the lost boundary.

The RTL implements this partition. The DMA engine captures initiating CPUIF
requests, translates the virtual RMEM address once, and executes received
scalar requests through its local CPUIF master. The protocol engine does not
access either memory interface.

Proposed parameter conventions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Every four-byte oETP parameter uses little-endian byte order:
``0x11223344`` is encoded as ``44 33 22 11``. This includes Request ID,
Address, Length, BitEnable, RMEM Data, and Error Code. Ethernet MAC octet order
and EtherType encoding remain unchanged; EtherType is still ``88 B5``.
Addresses and lengths are unsigned 32-bit byte quantities.

Bulk data parameters contain an ordered byte stream: the byte at the lowest
source address is transmitted first, followed by successive source bytes.
The receiver writes them at successive destination addresses without reversing
each four-byte group. B data bytes occupy ceil(B/4) parameters. Unused bytes
in the final parameter are zero on transmit, ignored on receive, and never
written to memory. This word padding differs from Ethernet minimum-frame
padding, which follows the entire PDU.

Wire parameters are:

* **Request ID:** a 32-bit identifier allocated by the initiating oETP engine.
  Each RMEM operation or DMA fragment receives an ID; any unicast reply echoes
  it. Group writes retain Request ID in the PDU without creating a remote-reply
  wait. The allocation counter and collision rule are defined below.
* **Address:** the final byte address in the responder's address space. The
  initiator translates once; the responder validates the permitted range
  without adding its local base again.
* **Length:** meaningful bulk bytes, excluding both forms of padding and EndOfData.
* **EndOfData:** the fixed 32-bit successful-completion marker after bulk Data
  in DMA_WRITE_REQ and DMA_READ_RSP only.
* **BitEnable:** a 32-bit RMEM write mask. Bit i enables Data bit i, for
  i = 0 through 31. All 32 mask bits are meaningful and map directly to local
  CPUIF wr_biten. BitEnable is not carried in RMEM reads or bulk DMA commands.
* **Error Code:** a parameter of the dedicated ERROR_RSP command only;
  successful responses have no Status field. Assigned wire causes are 1..7;
  the initiator maps them to remote CSR codes 9..15.

Request ID allocation and hard reset
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The engine maintains one unsigned 32-bit allocation counter. Allocating any
locally initiated RMEM operation or DMA fragment, including a multicast write,
uses the current counter value and increments it modulo 2^32. A completion,
timeout, transfer abort, or CSR reconfiguration never resets the counter.
Only assertion of the engine/endpoint ``rst`` signal resets it to zero and
invalidates outstanding contexts. Hard reset clears every FIFO in the endpoint
reset domain and removes partial frames and pending events, restoring the
engine's power-on state. Version 1 has no software reset command.

Before reusing an ID after counter wrap, check for an older outstanding context
with that ID. If it exists, invalidate it with a TIMEOUT outcome, even if its
response-timeout CSR is zero. Apply the normal timeout completion/abort policy
and safely retire its local activity before assigning the ID to a new context.
The check is local to the initiating engine and does not emit ERROR_RSP.

With the v1 single-request scheduler, an outstanding unicast request normally
prevents allocating the 2^32 subsequent requests needed to reach this collision.
The rule still defines allocation behavior without adding a wire field.
It invalidates a live old context, but cannot identify an old reply once its
ID has actually been reassigned to an otherwise matching new request, or after
hard reset if a frame survives outside that reset domain. Hard reset drains
all FIFOs under its control; it does not identify old frames subsequently
delivered from outside that domain. Version 1 adds no session/epoch parameter
or duplicate-request suppression.

Sequence and Control stay local
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Proposal:** omit Sequence and Control from the wire PDU. Request ID selects
an outstanding context containing the peer, operation, address, length, local
DMA Sequence, and local LAST flag. The engine restores Sequence and LAST on
internal AXIS TID/TUSER and DMA completion channels. The current DMA checks
those values, so removing wire fields does not mean dropping local metadata.

For a transfer covering a complete configured peer region, the fragment at
its end can be recognized with widened address arithmetic::

   Address + Length == RegionBase + RegionSize

This requires the correct address space, stable configuration, and matching
transfer/window boundaries. It is not generally the end of a transfer of a
subrange, or when the responder permits a larger window than the initiator
transfers. The initiator already has the authoritative transfer context and
LAST flag; it need not reconstruct them from the responder's configuration.

The responder handles each received DMA request independently and sends one
reply per Request ID for unicast requests; group writes have no reply. It does
not need a wire block-end flag. Internal responder
Sequence/LAST values are assigned or derived locally and kept consistent with
that request's data and completion; they are not returned over Ethernet.
The initiator's sequential scheduler determines completion of the entire block.

Command layouts
~~~~~~~~~~~~~~~

The following command codes are assigned. Parameter lists define order; every
listed parameter occupies four bytes. No additional fixed header is introduced
by these layouts.

.. list-table:: Assigned command codes and parameter layouts
   :header-rows: 1
   :widths: 22 10 43 25

   * - Command
     - Cmd
     - Parameters, in order
     - Purpose
   * - RMEM_READ_REQ
     - ``0x10``
     - Request ID, Address
     - Read one aligned 32-bit word.
   * - RMEM_READ_RSP
     - ``0x11``
     - Request ID, Data
     - Return the full 32-bit word on success.
   * - RMEM_WRITE_REQ
     - ``0x20``
     - Request ID, Address, BitEnable, Data
     - Write selected bits of one aligned word; group destinations have no reply.
   * - RMEM_WRITE_RSP
     - ``0x21``
     - Request ID
     - Complete a unicast write after local write acknowledgement.
   * - DMA_READ_REQ
     - ``0x30``
     - Request ID, Address, Length
     - Request one remote memory fragment.
   * - DMA_READ_RSP
     - ``0x31``
     - Request ID, Data[ceil(ExpectedLength/4)], EndOfData
     - Return the requested fragment on success.
   * - DMA_WRITE_REQ
     - ``0x40``
     - Request ID, Address, Length, Data[ceil(Length/4)], EndOfData
     - Write one fragment; group destinations have no reply.
   * - DMA_WRITE_RSP
     - ``0x41``
     - Request ID
     - Acknowledge a unicast fragment after local DMA write completion.
   * - ERROR_RSP
     - ``0xFF``
     - Request ID, Error Code
     - Complete a recognized unicast request with an error instead of success.

For the four memory operation pairs, the high nibble identifies the operation
and the low nibble distinguishes request (0) from successful response (1).
The successful response code is therefore the assigned request code OR
``0x01``. ERROR_RSP = ``0xFF`` is a separate common error response; its
Request ID identifies the failed request and its Error Code identifies the
cause. Error Code values 1..7 use the causes in the local/remote error table
below; local TIMEOUT = 8 is not a wire Error Code.

All other Cmd values are reserved. Decode exact assigned codes before applying
the request/response pairing rule; an arbitrary value with bit 0 set is not
automatically a valid response. Multicast writes still use ``0x20`` or
``0x40`` and generate neither ``0x21``/``0x41`` nor ``0xFF`` responses.

RMEM READ_REQ/READ_RSP/WRITE_REQ/WRITE_RSP PDU lengths are 10, 10, 18, and
6 bytes. ERROR_RSP is 10 bytes. BitEnable = ``0xFFFFFFFF`` writes the complete
word; ``0x00000005`` enables only Data bits 0 and 2 and maps to CPUIF
wr_biten = ``0x00000005``. No expansion into byte groups is needed.
BitEnable = ``0x00000000`` is a successful no-op: after the usual frame,
peer-policy, alignment, and range validation, do not issue a target CPUIF
write. A unicast request still receives RMEM_WRITE_RSP; a group request
receives no response. Invalid requests are not made valid by a zero mask.

RMEM reads carry no BitEnable, always read a complete aligned word, and return
the complete Data word. Bulk DMA uses Address and Length to describe the exact
byte range, including an unaligned first address or a partial final word.

DMA write requests have three metadata parameters, Data, and EndOfData, with
PDU length ``18 + 4*ceil(B/4)``. Their maximum data length is **8160 bytes**
within the 8178-byte PDU budget. DMA read replies have one metadata parameter,
Data, and EndOfData, with length ``10 + 4*ceil(B/4)``; their format could fit
8168 bytes. The common DMA fragment limit is **8160 bytes** so both directions
use the same bound. On a 1500-byte payload MTU, this limit becomes 1480 bytes.

``MAX_RAW_FRAME_SIZE`` is the synthesis-time raw Ethernet frame ceiling,
excluding FCS, supplied by the endpoint RDL parameter. It defaults to 8192
bytes and remains fixed in the implemented hardware. The corresponding common
peer DMA memory-fragment ceiling is
``4 * floor((MAX_RAW_FRAME_SIZE - 32) / 4)``. The 32 bytes account for the
14-byte Ethernet header, 14 bytes of DMA_WRITE_REQ metadata, and four-byte
EndOfData; the remaining wire Data array is rounded to four-byte parameters.

``config.dma_max_fragment_size.bytes`` follows ``config.dma_timeout`` and
selects the maximum meaningful memory bytes in each locally initiated peer
DMA fragment. It is a global 32-bit read/write setting that resets to the
synthesized fragment ceiling: 8160 bytes for an 8192-byte raw frame limit.
Hardware rounds the CSR value down to a multiple of four before checking the
effective MFS range: four through the synthesized ceiling, in steps of four.
For example, 31 selects 28 bytes, 7 selects four, and 8161 through 8163 select
8160 in the default build. The CSR retains the unrounded written value. A value
of zero through three, or a rounded value above the ceiling, rejects a new
block with local invalid-parameter code 1 before memory or protocol work.
The last fragment is the smaller of the effective MFS and the exact remaining
block length; it may contain one through three meaningful bytes. Only protocol
word padding fills its wire Data parameter, never additional memory bytes.
The DMA engine snapshots the effective MFS when it accepts the whole
software-started block, so subsequent CSR writes affect only later blocks.

Received DMA requests use the synthesized fragment ceiling independently of
the receiver's local fragmentation setting. A received read is answered with
the exact requested Length and is not split into additional replies. RMEM,
direct CSR streams, and non-oETP DMA are unaffected by this setting. Raw DMA
continues to carry one complete frame up to ``MAX_RAW_FRAME_SIZE``. The full
endpoint passes the RDL-generated parameter to its RTL interface, keeping the
CSR reset, advertised raw ceiling, and implemented capacity consistent.

An unaligned raw TX read near the 8192-byte ceiling requires an additional
AXI input word beyond TAXI's cycle-counter capacity. The DMA engine uses two
local read descriptors for that case, suppressing the intermediate TLAST and
retaining any read error. It still emits one continuous raw AXIS frame and
reports one whole-frame completion. Peer fragments remain below this boundary.

Bulk lengths must be positive. Validate Address + Length with a widened
calculation, checking overflow and the entire permitted window. This proposal
preserves unaligned bulk DMA support; RMEM remains word aligned.

Transactions and access policy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the sequential request-response model, a read consists of a
request and a data reply; a unicast write consists of a data-bearing request
and a result reply. A multicast write consists only of the data-bearing
request. The DMA engine executes RMEM through local CPUIF and bulk operations
through its AXI DMA paths; oETP transports their commands, data, and completions.

A reply must match an outstanding context's source MAC, Request ID, and
expected response command. It cannot create a memory operation itself.
Discard unmatched/late replies. ExpectedLength for a DMA_READ_RSP comes from
the saved request, not a reply parameter. Its data must contain exactly that
many bytes plus the defined word/Ethernet padding. An unmatched read reply
is drained and discarded without interpreting or writing its data.
A recognized response from the expected peer, with the active Request ID and
expected response command but an invalid length, terminates the request with
an error when the mismatch is detected, without waiting for the configured
response timeout. A streamed DMA_READ_RSP may already have modified part of
local memory; failure does not restore those bytes. An incomplete DMA_READ_RSP
or a missing/incorrect EndOfData records remote code 10 directly. The same error-completion
rule applies to a malformed ERROR_RSP that can
reliably be associated with that request. An ERROR_RSP is never answered with
another ERROR_RSP.

A success response implies that the entire requested operation succeeded;
there is no success Status or transferred-length parameter. A write reply
containing only Request ID means the target interface
acknowledged the write, not merely that the Ethernet frame arrived.

A unicast block completes only after every issued fragment's local work and
remote reply succeed, one fragment at a time. For reads, supply data and
completion to the local DMA path while
respecting its handshakes. Restore local Sequence, LAST, and completion length
from the Request ID context; do not substitute Request ID for initiator TID.

TX streams without a store-and-forward barrier between DMA and oETP. The first
AXIS TVALID belonging to a fragment starts Ethernet/oETP frame preparation;
the engine does not wait for the whole fragment or its read completion.
Only the EndOfData trailer waits for successful local read completion.

A read failure before frame transmission starts produces local error status;
for a received unicast DMA_READ_REQ it produces ERROR_RSP with the local cause.
Once DMA_WRITE_REQ or DMA_READ_RSP transmission has begun, a local read error
stops payload emission and ends that frame early without EndOfData. Do not append
an early marker or substitute a second ERROR_RSP for an already started response.
Already accepted local AXI/AXIS activity must still be drained or cancelled
safely before resources are reused. The source records its local AXI cause;
the receiver records remote incomplete-transfer code 10 and may have already
modified memory. A failed initiating write does not wait indefinitely for a
reply to its shortened frame; late replies are discarded with the failed ID.

An incomplete unicast DMA_WRITE_REQ receives ERROR_RSP wire cause 2 while its
receiver records CSR code 10. Group writes retain local diagnostics and no
reply. An incomplete DMA_READ_RSP fails its outstanding request with code 10
and never elicits ERROR_RSP. A received operation failing on its local target
interface retains the existing local error record and ERROR_RSP rules.

Multicast write completion
^^^^^^^^^^^^^^^^^^^^^^^^^^

The sender snapshots the destination MAC and group-write flag for each accepted
operation. Reconfiguration cannot change whether that operation expects a
reply. Request IDs and the existing command parameter layouts are retained;
no explicit no-response flag or multicast command is added.

For multicast RMEM writes, acknowledge the local initiating CPUIF request
after the entire outgoing frame has been accepted by the Ethernet-facing
stream. Do not start an RMEM remote-response timeout for this operation.
For multicast DMA writes, each fragment completes after its local memory read
succeeds and its complete Ethernet frame has been accepted by that stream,
including the accepted TLAST beat. Keep its context until both conditions
hold, then return a locally generated initiator_if completion with the saved
peer, Sequence, LAST, and Length. Local failures still report local errors.
Block completion waits for all issued fragments to finish locally; it is not
triggered solely by the final-address fragment.

The existing DMA engine waits for both local work and initiator_if completion.
The locally generated completion satisfies the latter for a group write; it
must not depend on a nonexistent remote acknowledgement. Completion describes
local emission into the fabric. Reception and memory updates at group members
remain unconfirmed, including whether the group had any accepting members.

The receiver snapshots the group classification from the received destination
MAC. It performs the same framing, source-peer permission, mask, and complete
address-range checks as for a unicast write, then executes any accepted write
through CPUIF or responder DMA. Even after that local operation completes, it
sends no RMEM_WRITE_RSP, DMA_WRITE_RSP, or ERROR_RSP for the group request.
Rejected group writes and local memory failures remain local outcomes. Incoming
responses cannot complete a multicast write context awaiting only local work.

Every receiver sees the same final Address and Length (or aligned RMEM Address
and BitEnable); there is no per-member wire address translation. Each receiver
validates that address against its own configured window. Group membership is
configured by the shared ``config.multicast_address``; source access policy is
configured separately in each receiver's peer table.

Peer access checks
^^^^^^^^^^^^^^^^^^

The existing CSR peer policy constrains responder requests:

.. list-table:: Peer access policy
   :header-rows: 1
   :widths: 15 40 45

   * - Mode
     - Permitted incoming requests
     - Locally initiated behavior
   * - 0
     - None
     - Disabled.
   * - 1
     - RMEM read and write
     - Transparent RMEM access.
   * - 2
     - Bulk DMA write
     - Mirror remote to local using DMA reads.
   * - 3
     - Bulk DMA read
     - Mirror local to remote using DMA writes.

DMA mirrors require complementary peer modes. Validate responder addresses
against the local window associated with the source peer. Snapshot configuration
needed for an accepted operation until that operation completes.

Before local memory access, check the decoded command layout, destination,
source peer policy, alignment, and the entire address range. Bulk payload
transfer starts without waiting for the complete Ethernet frame. Count and
check framing and payload length while receiving data. A late length/framing
error or a bus failure can leave a partial DMA write; failure does not imply
rollback or block atomicity.

Other EtherTypes, or ``0x88B5`` with different
Magic, follow the raw non-oETP receive policy. A matching oETP Magic with
malformed content is rejected as oETP, never passed to a raw DMA descriptor.
Unknown sources never cause memory access and are discarded without a reply.
Recognized unicast requests from known peers with a trustworthy Request ID
receive ERROR_RSP when command, length, or access validation fails, including
an operation prohibited by that peer's mode. A group write never receives an
error reply.
Unparseable frames are discarded. ERROR_RSP is a response, never a new request,
and must not provoke another error response. Error Code distinguishes causes
such as access/range rejection, malformed length, and local bus failure; its
numeric assignments are listed below. Without a
transferred-length parameter, an error makes no claim about how many bytes
were modified before failure.

Streaming receive and partial transfers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The endpoint's DMA receive FIFO, ``u_dma_rx_fifo``, already uses
``FRAME_FIFO = 0``. Its default capacity is 16384 bytes, but that buffering
absorbs bus timing and backpressure; it does not require a complete fragment
before exposing payload to the DMA engine. The protocol design retains this
streaming model and introduces no full-frame validation barrier.

Small internal data buffers may register pipeline boundaries, align byte lanes,
and synchronize payload with control and terminal status. They preserve AXIS
fields while stalled and do not require a whole frame or fragment before
forwarding data.

* Capture and check command metadata before starting the memory operation.
  For a DMA_READ_RSP, first match the source peer, Request ID, and expected
  response command, and use the saved request's expected length.
* Forward only meaningful memory bytes as they arrive. Strip protocol headers,
  data-word padding, and received Ethernet padding. TKEEP marks actual bytes;
  TLAST ends the internal memory fragment. Preserve local sequence, route,
  peer, and last metadata.
* Track the input frame and payload byte counts through Ethernet TLAST. Never
  forward bytes beyond Length to memory. A short payload or invalid trailing
  length fails the operation and the receiver drains any remaining frame data.
  At the expected end of the rounded Data array, check the complete EndOfData
  word. Never scan memory data for this pattern. Zero Ethernet padding can be
  consumed as apparent missing data before this check, but cannot pass it;
  such a failure records remote code 10 and may leave partial or zero-filled writes.
* Emit a successful unicast write response only after the receive-frame length
  and EndOfData checks and local memory operation have both completed successfully. An
  eligible failed unicast write produces ERROR_RSP; a group write produces
  neither a success nor an error response.

The same streaming policy applies to DMA_WRITE_REQ and DMA_READ_RSP. A failure
can therefore leave part of the responder's destination or the initiator's
local destination modified. ERROR_RSP reports failure without an exact count
of modified bytes. Hardware provides no rollback, cross-fragment atomicity,
or buffer synchronization. Software manages buffer ownership, consistency,
and recovery above oETP. RX processing and TX responses remain serviceable
while an outgoing request awaits its reply.

A frame that reaches TLAST with insufficient payload or without a valid
EndOfData produces remote stream error 10. This also applies when padding
makes the received payload appear sufficiently long.
If the frame or reply never arrives, failure detection instead depends on an
enabled initiator response timeout; a zero timeout still permits indefinite
waiting. Timeout does not imply that the destination buffer is unchanged.

Error origin and CSR status
~~~~~~~~~~~~~~~~~~~~~~~~~~~

``peers.entry[n].dma.error`` and ``error_code`` are shared by transparent RMEM
(peer mode 1) and bulk DMA (peer modes 2/3). They report the most recent failure,
including failures while servicing received requests, initiator-local DMA
failures, and errors returned through the oETP completion interface.
The current DMA engine records local and completion-path errors separately
and gives a fragment's local memory error precedence when both are present.
A receive-short indication on the internal AXIS path is a consequence of a
remote truncated transfer when the protocol completion identifies code 10;
it must not replace that canonical code with local stream error 2.

Local CSR codes 4/5 denote AXI read SLVERR/DECERR; codes 6/7 denote AXI write
SLVERR/DECERR. Local and remote are relative to the endpoint recording the
failure. From the initiator's perspective, DMA_WRITE reads local source memory
and writes remote target memory; DMA_READ reads remote source memory and
writes local destination memory. The responder's source read or target write
is its own local memory operation. Raw non-oETP DMA has only local AXI
memory accesses. CSR values 4/5 and 6/7 report local AXI failures; the remote
equivalents are 12/13 and 14/15.

CSR values 1..7 report locally detected failures. Code 8 reports local response
timeout, and values 9..15 report the remote equivalents of causes 1..7 received
in a valid ERROR_RSP. Remote stream code 10 also identifies directly detected
incomplete incoming DMA_WRITE_REQ/DMA_READ_RSP or missing/incorrect EndOfData;
it does not require an ERROR_RSP to arrive first. This encoding fits the existing four-bit
field and is defined by the RDL and internal transfer interface.

.. list-table:: Local and remote CSR error codes
   :header-rows: 1
   :widths: 60 20 20

   * - Cause
     - Local CSR code
     - Remote CSR code
   * - Invalid request, configuration, or parameters
     - 1
     - 9
   * - Stream/PDU length or TLAST error
     - 2
     - 10
   * - Supported size or buffer capacity exceeded
     - 3
     - 11
   * - AXI read SLVERR
     - 4
     - 12
   * - AXI read DECERR
     - 5
     - 13
   * - AXI write SLVERR
     - 6
     - 14
   * - AXI write DECERR
     - 7
     - 15
   * - Response timeout or Request ID wrap collision
     - 8
     - Not reported by ERROR_RSP.

The corresponding wire Error Code values are 1..7, describing the
responder's failure while servicing the request. The initiator validates the
full 32-bit value and maps it to ``CSR code = 8 + wire code``. Wire values
outside 1..7 are invalid response parameters and terminate the matching
request with local invalid-parameter error code 1. They are never truncated
or interpreted as a locally detected timeout. Internal stream faults and
other local framing checks use code 2; an incomplete received DMA data frame
uses code 10 directly, as does a valid ERROR_RSP reporting cause 2.
Non-oETP DMA has only local causes. Zero continues to mean no recorded error.

The oETP engine returns the final CSR code on initiator completions, including
locally detected errors and timeout. ``csr_error_from_wire`` in
``openenoc_dma_transfer_if`` validates and maps a full 32-bit wire cause.
The DMA engine preserves that code for RMEM and bulk errors. Responder
completions report the local servicing cause 1..7 for ERROR_RSP serialization.
For a resolved source peer, the DMA responder also records that cause in its
own peer CSR before exposing the failed completion to the oETP engine. The
exception is an incomplete received bulk write: its peer CSR records remote
code 10 while its responder completion carries wire cause 2. Late protocol
outcomes such as missing EndOfData must reach the DMA status owner through
the internal transfer contract, even if the streamed memory write has completed.
The protocol engine serializes ERROR_RSP for unicast and suppresses it for multicast;
the local record and enabled notification apply in both cases. A received
failure never changes ``dma.request``, ``idle``, or ``done`` for an independently
initiated transfer. Successful received requests preserve sticky errors.
The wire decoder calls the helper only after response-context validation.

Bulk responder failures use PEER_DMA_COMPLETE, source 0, with the source peer's
``dma.irq_enable`` captured when the failure is recorded. The IRQ controller
samples ``irq.event_enable.peer_dma_complete`` when preparing the registered
admission offer.
Received RMEM failures use RMEM_ERROR, source 5, with
``irq.event_enable.rmem_error`` sampled when preparing the admission offer, independently of the
per-peer bulk enable. Successful incoming requests generate neither event.
Once admitted, the event retains its source and peer index until committed.
An unavailable IRQ FIFO delays the notification, not CSR recording or the
current error completion. The DMA responder retains one pending notification
and defers accepting another incoming request until it is admitted and committed.
IRQ claim handling remains independent of ``dma.clear_error``.

For example, configure A's peer entry for B and B's peer entry for A, and enable
PEER_DMA_COMPLETE globally and per peer on both endpoints. When A issues a
unicast DMA_WRITE_REQ and B's local AXI write fails with SLVERR, B records
``dma.error = 1`` and local ``error_code = 6`` in its entry for A, queues its
enabled error event, and returns ERROR_RSP with the original Request ID and
wire Error Code 6. A maps that reply to remote ``error_code = 14`` in its entry
for B and completes its failed transfer with its enabled completion event.
Both IRQ claims identify the peer local to their own endpoint. Neither claim
nor ERROR_RSP reports how many bytes were modified; software must treat the
target buffer as potentially partially updated.

The error flag and code remain latched across subsequent operations, including
successful completion. Write one to ``peers.entry[n].dma.clear_error`` to clear
both; hardware acknowledges the command by clearing that field. A new failure
takes precedence over a simultaneous clear. Clearing does not abort active
work, change the bulk DMA done/idle state, or complete an IRQ claim. Software
can clear an earlier failure before starting an operation whose result it wants
to assess independently. Error recording does not depend on IRQ enable.

An ERROR_RSP received from a peer reports failure while that peer serviced
the request. Wire AXI causes 4..7 map to CSR values 12..15 and preserve their
bus-operation meaning. Local response timeout code 8 is generated by the initiator when
no peer response arrives, rather than by a received ERROR_RSP.

Transfer sequencing and timeouts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Version 1 has at most one active locally initiated unicast request per endpoint.
The next request is transmitted only after the current request completes.
For a software-started DMA block, issue one fragment, wait for its response
and local completion, then issue the next fragment. Any fragment error aborts
the rest of the block. Internal descriptor preparation does not permit multiple
unicast requests to be in flight on the wire. Pre-prepared fragments of a
failed block must be cancelled before they can be transmitted.

Incoming requests are serviced independently while the endpoint waits for its
own response. Response transmission must be possible during that wait; otherwise
two endpoints issuing requests to one another could wait indefinitely. Locally
initiated RMEM and peer DMA operations share the single outgoing request slot.

If no responder context is available when a new incoming request is classified,
discard that request and drain its frame through TLAST without issuing memory
work or a response. Do not stall the RX parser waiting for a responder context,
since a response to this endpoint's own request may follow the discarded frame.
This also applies while the DMA responder retains a pending IRQ notification.
Replies matching the active initiating context remain serviceable independently
of responder availability. A discarded unicast request is observed by its
initiator through an enabled response timeout; with a zero timeout it can wait
indefinitely. A discarded group write retains best-effort delivery semantics.

Give pending RMEM priority over the next bulk DMA fragment at a free request
slot. Do not preempt an active Ethernet frame or unicast request. Responses
to incoming operations have transmit priority. Arbitration among peer DMA
and raw non-oETP traffic must be fair so a continuous producer cannot starve
another traffic class indefinitely.

There are no wire credit messages, credit counters, or advertised receive
reservations in v1. Local buffers and AXIS backpressure remain implementation
resources. Off-chip frame loss or receiver overload can result in a missing
unicast response; the configured timeout governs that wait. Multicast writes
are emitted one fragment at a time and are best effort, with no per-member
capacity accounting or reception/completion guarantee.

The two 32-bit response-timeout CSRs count endpoint clock cycles:

* ``config.rmem_timeout.cycles`` applies to unicast RMEM operations.
* ``config.dma_timeout.cycles`` applies separately to each unicast peer
  DMA fragment and is common to all peers. There is no whole-block DMA timer.

Both reset to zero. Zero disables that timer and permits an indefinite response
wait; a nonzero value bounds the wait for the matching response. The value is
sampled when the operation or fragment is accepted. Counting starts after the
complete request frame is accepted by the Ethernet-facing transmit stream.
CSR changes apply to later operations/fragments, not an already active timer.
Multicast writes do not wait for responses and do not run these timers.

Receiving the response header or matching its Request ID does not stop the
timer. A successful response stops it only after the complete matching frame
has been received and validated, including EndOfData where present and the
accepted Ethernet TLAST. A recognized malformed response or valid ERROR_RSP
instead terminates the wait with its corresponding error. RX backpressure is
included in the timed interval. After a valid response has completed, any
remaining local memory completion is outside this response timeout. If a valid
response finishes on the same clock edge as timer expiry, the response takes
priority; a valid ERROR_RSP retains its reported cause rather than becoming a
timeout.

On DMA fragment timeout, return the fragment's error completion with code
**8 (TIMEOUT)**, cease issuing further fragments of that block, and cancel its
unsent descriptors and pending commands. Retire the failed transfer once local
activity is quiescent, reporting ``idle = 1``, ``done = 0``, ``error = 1``, and
``error_code = 8``. An enabled peer completion IRQ follows the existing error
completion path. Do not wait for a response from a timed-out fragment, and do
not retry it or advance to the next fragment. This error is reported locally;
it does not generate a wire ERROR_RSP to a peer that has not responded.

Late responses to the timed-out Request ID are discarded and must not write
local memory or complete a subsequently started transfer. Already accepted
local stream/memory activity must be safely drained or cancelled before its
resources are reused. A timeout cannot undo an already performed remote write.
Software manages timeout handling and any deliberate restart of a transfer;
hardware never retransmits automatically. A retry can repeat a remote write
whose response was lost. This version provides no cross-fragment atomicity
or memory fence.

The CSR definitions and generated HAL expose this policy. The protocol engine
implements response timing, and DMA cancels unsent fragments after the failed
fragment's local activity is quiescent.

RMEM failure completion and notification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An RMEM timeout terminates the initiating bus access with the following signals
asserted together for its terminal response:

* Read: ``cpuif_rd_data = 0xFFFFFFFF`` and ``cpuif_rd_ack = 1``.
* Write: ``cpuif_wr_ack = 1``.

These are the CPUIF acknowledgement signals; the native interface members are
``rd_ack`` and ``wr_ack``. The external-RMEM PeakRDL boundary carries ACK and
read data, and remains unchanged without ERR signals. The all-ones read data
alone is not an error indication because it can also be valid memory data.
Invalidate the outstanding Request ID on timeout, so a late response cannot
complete that access again. Counter-wrap invalidation uses this same outcome.

Every resolved-peer locally initiated RMEM failure, including TIMEOUT and an
accepted ERROR_RSP, sets that peer's shared ``dma.error`` and ``dma.error_code``.
Local timeout and Request ID collision record code 8. The wire Error Code is
still a 32-bit parameter, but its numeric codes must have an explicit mapping
to the shared four-bit CSR field; do not silently truncate an arbitrary cause.
A later RMEM or bulk DMA failure replaces that peer's recorded code. There is
no separate RMEM status register or read/write metadata register.

``irq.event_enable.rmem_error`` at bit 5 enables the common RMEM_ERROR
notification, IRQ source 5. The claim identifies the affected peer. For a
locally initiated failure, sample this enable when the failure is recorded;
received-request failures use IRQ admission as described above. Record the
CSR status before exposing the event. RMEM keeps its existing separate IRQ path; bulk DMA still uses
PEER_DMA_COMPLETE and its own enable policy. Clear the shared CSR record with
that peer's ``dma.clear_error``; completing either IRQ claim does not clear it.
Software can poll the flag or handle the IRQ to select recovery.

The failure must also terminate the blocked RMEM bus access; an IRQ alone
cannot release a CPU waiting for that access and might prevent it from entering
the handler. IRQ delivery must not be a prerequisite for releasing the access.
For a received RMEM ERROR_RSP, finish the access through the same ACK-only
boundary and record its mapped Error Code in the peer CSR; a failed read returns
all ones.
Successful or successfully emitted multicast writes generate no RMEM_ERROR.
A failed local multicast emission can still produce a local error record/event;
response suppression does not suppress initiator-local diagnostics. Hardware
does not retry automatically. The existing IRQ sequence token remains separate
from Request ID.

The DMA block owns the shared error registers and receives RMEM error completions
on the transfer interface. Its separate RMEM IRQ producer retains a pending
notification for each peer while the IRQ FIFO is full; repeated pre-admission
failures of that peer coalesce while updating its CSR code. CPUIF ACK and
subsequent requests proceed independently. Local CPUIF execution errors use cause 4 for read failure and
cause 6 for write failure because CPUIF supplies one error bit rather than an
AXI response encoding.

Implemented control and datapath
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The initiator, responder, lookup, RX, and TX controllers each own a separate
clocked process. State and context registers receive direct nonblocking
assignments. Command handshakes are registered in their owning controller and
state transitions consume the actual VALID/READY handshake. Registered command
stages add latency without allowing a second acceptance of the same offer. TX and RX can progress independently; one
initiating context and one responding context can coexist.

Every outward handshake, metadata, and status signal comes from a register.
The four external AXIS boundaries use two-entry skid buffers with registered
READY and payload signals around the width adapters. They retain a beat already
in flight when backpressure changes and sustain consecutive beat transfers.
Inactive stream strobes are derived from registered keep masks. These small
buffers add pipeline latency without storing an entire frame. The response
timer still starts at the actual Ethernet-facing TLAST handshake.

.. list-table:: Control machines
   :header-rows: 1
   :widths: 15 38 47

   * - Machine
     - Normal path
     - Completion and exceptional paths
   * - Initiator
     - IDLE, LOOKUP, LOOKUP_WAIT, ACCEPT, TX, WAIT
     - COMPLETE holds command completion until accepted. ABORT flushes any
       held RX memory word with TLAST before reporting timeout.
   * - Responder
     - IDLE, EXECUTE
     - Holds source peer, command, Request ID, local sequence, multicast flag,
       and memory result until the reply ends or multicast service completes.
   * - RX
     - IDLE, HEADER, CLASSIFY, META, MATCH or LOOKUP/LOOKUP_WAIT,
       ADMIT, REQUEST, DATA, EOD, TAIL, VALIDATE, FINAL
     - DROP drains rejected traffic. ABORT closes partial memory output.
       RAW_CLAIM, RAW_REPLAY, RAW_STREAM, RAW_FINISH retain and route raw frames.
   * - TX
     - IDLE, PRIME, HEADER, DATA, STATUS, FLUSH, EOD, WAIT_END
     - ERROR_FLUSH and DRAIN close an already started failed frame without
       EndOfData. PRE_DRAIN discards buffered source data when failure is known
       before frame preparation. RAW streams a complete raw frame.
   * - Lookup
     - IDLE, INITIATOR_REQ, INITIATOR_RSP or RX_REQ, RX_RSP
     - Arbitrates the initiating and receiving protocol lookup clients;
       the external endpoint lookup also arbitrates against the DMA client.

An initiating command remains unaccepted until its peer lookup is complete.
This prevents local DMA from starting a rejected memory-source descriptor.
On acceptance the engine allocates Request ID and snapshots its MAC addresses,
multicast decision, and timer. The wire timer starts at the Ethernet-facing
TLAST handshake after all width adaptation and TX backpressure.

A known, addressed request is admitted only when the responder is available.
A busy responder drains the new request through TLAST without a reply. It does
not occupy the matcher for the independently pending initiating response.
A malformed recognized command never falls through to the raw receive path.
Source lookup precedes memory servicing; DMA validates the complete local
address range and configured peer mode before issuing a memory descriptor.

All four streams are adapted to a 32-bit internal word path. Ethernet MAC
bytes and EtherType are assembled explicitly; 32-bit protocol parameters use
little-endian words. The RX metadata buffer has eight words with keep/last
information. Each bulk direction has one held word and one output word;
there is no full-fragment validation buffer. The final source word is retained
until memory-read status is known, so a failed source cannot emit EndOfData.
The current staged bulk path transfers a 32-bit word every two cycles without
stalls. Wider external interfaces preserve ordering and metadata, but do not
increase that internal throughput.

The principal paths are::

    local AXIS -> input skid buffer -> width adapter -> held/output words
               -> Ethernet header -> rounded Data -> conditional EndOfData
               -> Ethernet adapter -> output skid buffer -> Ethernet AXIS

    Ethernet AXIS -> input skid buffer -> width adapter -> header/parser
                  -> source lookup -> exact Length bytes -> local adapter
                  -> output skid buffer -> DMA memory
                  -> fixed-position EndOfData + TLAST checks -> terminal status

Raw frames bypass oETP encapsulation while retaining the parsed prefix.
The raw receive policy selects drop, filtered, multicast, or promiscuous
admission. An armed raw DMA descriptor is claimed once before the first local
payload beat; otherwise the frame goes to the direct CSR path.

Received request replies have TX priority when their scalar response or payload
is ready. Raw traffic and eligible initiating traffic alternate at frame
boundaries. A shared FIFO head is consumed only by the matching role, peer,
and local sequence; response priority cannot reorder that FIFO.
The endpoint TX mux also uses round-robin arbitration between DMA and direct
traffic. A pending RMEM command is selected ahead of the next unsent bulk
fragment after the current fragment's memory and protocol activity retires.

The global Request ID counter advances only on command acceptance and resets
only with hard reset. It wraps naturally at 32 bits. With one initiating
context, an outstanding-ID collision cannot occur: no later request can obtain
an ID until that context is complete.

Verification
~~~~~~~~~~~~~

``dv/core/openenoc_endpoint_oetp_engine/`` verifies the module independently
with a registered peer-lookup fixture, memory-service command/completion
fixtures, and independent Ethernet/memory AXIS sources and sinks. Fifteen
cases cover all commands, scalar fields, full-width error mapping, maximum
8160-byte data, padding, EndOfData position, multicast, raw filters and claims,
timeout start and snapshots, abort draining, busy responders, simultaneous
roles, Request ID wrap, response-at-expiry precedence, reset, and backpressure.
A subcycle test pulses handshake inputs during an active write and checks all
control, data, metadata, and READY outputs for stability between rising edges.
The cases run with local/Ethernet widths 32/32, 64/8, and 32/64.

Only after those isolated tests passed was the module connected to
``openenoc_endpoint_interface``. The interface suite uses the actual DMA engine,
peer lookup, IRQ controller, stream FIFOs, AXI RAM, and local CPUIF service.
It covers sequential multi-fragment reads/writes, abort/restart, partial final
fragments, range checks, multicast writes, local/remote errors, late EndOfData
failure after memory writes, RMEM priority, and IRQ FIFO saturation. Both
engines' existing isolated regressions remain part of verification.
The firmware smoke and full-endpoint feature coverage is unchanged; new HAL
and control APIs remain a separate iteration.

Functional scenarios
--------------------

This section reserves space for scenario descriptions and WaveDrom timing
diagrams. The current outline is:

* All scalar and bulk read/write command encodings.
* Streaming data, partial tails, EndOfData, and early/late source failures.
* Matched replies, remote errors, late replies, and fragment timeouts.
* Multicast write completion and receiver response suppression.
* Raw-frame routing, descriptor claims, and invalid frame draining.
* Independent initiating/responding roles, priority, reset, and Request ID wrap.
