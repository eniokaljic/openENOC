.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-dma-engine:

DMA Engine -- openenoc_endpoint_dma_engine
==========================================

.. index::
   single: openenoc_endpoint_dma_engine

Executes local memory operations for peer transfers, raw Ethernet DMA, and
scalar remote memory accesses.

**Source:** :download:`openenoc_endpoint_dma_engine.sv <../../../hw/rtl/core/openenoc_endpoint_dma_engine.sv>`.

Parameters
----------

.. list-table:: Parameters
   :class: rtl-reference-table
   :header-rows: 1
   :widths: 26 30 20 24

   * - Name
     - Default value
     - Allowed values
     - Description
   * - ``NUM_OF_PEERS``
     - ``4``
     - Integer >= 1; match generated CSR array
     - Number of peer-table entries.
   * - ``PEER_IDX_W``
     - ``NUM_OF_PEERS > 1 ? $clog2(NUM_OF_PEERS) : 1``
     - Integer >= 1; enough bits for the peer count
     - Width of local peer indices; all connected interfaces must agree.
   * - ``MAX_RAW_FRAME_SIZE``
     - ``8192``
     - 36..8192 bytes
     - Synthesized frame ceiling excluding FCS; reserves 32 bytes for the largest
       peer-frame overhead.
   * - ``AXI_MAX_BURST_LEN``
     - ``16``
     - 1..256 beats
     - Maximum AXI burst length issued by the memory DMA controllers.
   * - ``FRAGMENT_SLOTS``
     - ``16``
     - Integer >= 1
     - Number of local fragment bookkeeping contexts; not wire credits.
   * - ``SERIAL_PEER_REQUESTS``
     - ``1'b1``
     - 0 or 1
     - One issued peer fragment at a time when set; zero permits concurrent
       scheduler contexts.
   * - ``UNALIGNED_EN``
     - ``1'b1``
     - 0 or 1
     - Enables unaligned AXI memory accesses in the underlying TAXI DMA.

Signals
-------

Interface ports contain channels in both directions. The table identifies
the selected modport or stream role; member directions follow that interface.

.. list-table:: Public signals and interfaces
   :class: rtl-reference-table
   :header-rows: 1
   :widths: 28 32 17 23

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
     - Peer/raw DMA commands and status, IRQ enables, and initiating RMEM accesses.
   * - ``peer_lookup_if``
     - ``openenoc_peer_lookup_if.mst``
     - bidirectional (mst)
     - Peer-table query client and coherent response snapshot.
   * - ``initiator_if``
     - | ``openenoc_dma_transfer_if.``
       | ``requester``
     - bidirectional (requester)
     - Commands and status for locally initiated remote transactions.
   * - ``responder_if``
     - | ``openenoc_dma_transfer_if.``
       | ``executor``
     - bidirectional (executor)
     - Commands and status for servicing received remote transactions.
   * - ``m_axis_oetp``
     - ``taxi_axis_if.src``
     - source
     - Memory-read payloads or complete raw frames toward transport.
   * - ``s_axis_oetp``
     - ``taxi_axis_if.snk``
     - sink
     - Memory-write payloads or complete raw frames from transport.
   * - ``m_axi_wr``
     - ``taxi_axi_if.wr_mst``
     - bidirectional (wr_mst)
     - Outgoing AXI4 memory write address/data/response channels.
   * - ``m_axi_rd``
     - ``taxi_axi_if.rd_mst``
     - bidirectional (rd_mst)
     - Outgoing AXI4 memory read address/response channels.
   * - ``m_local_cpuif``
     - ``openenoc_cpuif_if.mst``
     - bidirectional (mst)
     - Local scalar-memory master for received RMEM operations.
   * - ``irq_event_if[3]``
     - | ``openenoc_irq_event_if.``
       | ``producer``
     - bidirectional (producer)
     - Peer-DMA, raw-TX, and raw-RX event producers, in that order.
   * - ``rmem_irq_event_if``
     - | ``openenoc_irq_event_if.``
       | ``producer``
     - bidirectional (producer)
     - Independent initiating RMEM error-event producer.
   * - ``responder_irq_event_if``
     - | ``openenoc_irq_event_if.``
       | ``producer``
     - bidirectional (producer)
     - Received-request servicing error-event producer.

Architecture and operation
--------------------------

Responsibilities and boundary
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. index::
   single: DMA

The DMA engine owns memory access for peer bulk DMA, raw non-oETP DMA,
received oETP requests, and scalar RMEM. A single TAXI AXI read DMA and a
single AXI write DMA are shared by the implemented bulk/raw operation classes.
Peer configuration is acquired through shared lookup and retained for the
accepted block; subsequent CSR writes do not alter that block's snapshot.

``endpoint_if`` carries control/status and the external initiating RMEM
request. ``peer_lookup_if`` obtains peer entries. ``initiator_if`` requests
protocol transactions, while ``responder_if`` executes received transactions.
``m_axis_oetp/s_axis_oetp`` carry the companion streams;
``m_axi_rd/m_axi_wr`` access bulk memory. ``m_local_cpuif`` is the local RMEM
execution master. The three ``irq_event_if`` ports serve peer DMA and raw TX/RX;
``rmem_irq_event_if`` keeps initiating RMEM notification separate, and
``responder_irq_event_if`` reports received-request servicing failures.

AXI, AXI-Stream, and local CPUIF data paths are fixed at 32 bits. AXI byte
strobes and AXI-Stream KEEP masks have four bits. Elaboration checks reject
connected interfaces with other data or byte-enable widths. Receive byte
counting uses the four KEEP bits; valid contiguous masks are ``0x1``, ``0x3``,
``0x7``, and ``0xF``, with ``0xF`` required before the final beat.

AXI addresses, local CPUIF addresses, and the address fields on the transfer
and peer-lookup interfaces are fixed at 32 bits. Elaboration checks reject
connected interfaces with other address widths.

Registered control and memory boundaries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The peer scheduler, raw TX, raw RX, responder, memory read, memory write,
RMEM, and notification controllers each use a separate clocked process with
direct nonblocking register updates. The peer scheduler alone owns the shared
peer and fragment contexts; memory controllers report accepted and completed
operations through registered event pulses. Arbitration and stream assembly
are internal combinational calculations.
CSR status fields alias the owning status registers. Hardware clears, lookup
requests, transfer commands/completions, CPUIF signals, and IRQ producer
signals are registered. A held CSR clear command is applied once; a failure
arriving before that command deasserts remains sticky.

A two-entry AXI-Stream register slice (skid buffer) registers each direction
of the memory-payload AXIS link. All five AXI channels also use registered
buffers, including RREADY and BREADY. Data accepted before downstream
backpressure takes effect remains in those buffers. This adds pipeline
latency without introducing full-fragment buffering or changing the
terminal-status join.

Local read completion counts bytes accepted into the TX register slice.
The raw TX CSR completion and a peer source-read terminal status can therefore
precede the final handshake on ``m_axis_oetp`` if that slice still holds data.
Receive completion instead waits for the memory-write result as well as the
required stream/framing outcome. Neither local completion confirms Ethernet
delivery to the remote application.

Streams and fragmentation
~~~~~~~~~~~~~~~~~~~~~~~~~

The :ref:`rtl-dma-transfer-if` contract carries complete Ethernet frames without
FCS for raw DMA and exactly the descriptor's memory bytes for peer bulk DMA.
Protocol headers, EndOfData, and protocol padding belong to oETP. Scalar RMEM
data uses command/completion fields and never AXIS.

The synthesized raw-frame ceiling reserves 32 bytes for Ethernet, the largest
DMA command metadata, and EndOfData. The common physical peer fragment ceiling
is ``4 * floor((MAX_RAW_FRAME_SIZE - 32) / 4)``, or 8160 bytes at the default.
At locally initiated block acceptance, snapshot
``conf.dma_max_fragment_size.bytes`` after rounding down to a multiple of
four. Its effective value must be between 4 and the physical ceiling.
Intermediate fragments use that limit; the final fragment carries exactly
the remaining bytes and can be shorter than four bytes. Incoming requests are
bounded by the physical ceiling, independently of the receiver's local CSR
fragment-size setting.

``FRAGMENT_SLOTS`` bounds local bookkeeping contexts; it is not a wire credit
mechanism. The oETP scheduler implements the agreed sequential unicast
request-response policy. Raw frames are not divided into peer protocol
fragments. For a maximum-size unaligned raw TX read that exceeds the underlying
TAXI read counter's safe budget, the engine reads 8188 bytes followed by the
remainder in a second local descriptor. It suppresses the intermediate TLAST,
producing one Ethernet frame.

Status and notification
~~~~~~~~~~~~~~~~~~~~~~~

Peer ``dma.error/error_code`` are shared by bulk DMA and RMEM and remain sticky
across starts and successful completions. ``dma.clear_error`` clears the record;
a concurrent new failure wins. Raw TX/RX have the corresponding ``clear_errors``
controls. Error clearing does not acknowledge an IRQ or alter descriptor
ownership, abort, idle, or done state.

Initiator completions preserve final local/remote CSR encoding supplied by
oETP. A failed received request records the source peer's error before its
completion becomes visible. Its enabled local IRQ is retained independently
of reply readiness and IRQ FIFO capacity. Successful received requests do not
generate a responder event. Reporting an incoming failure does not overwrite
idle/done for an independent locally initiated block.

Reset clears contexts, pending streams, descriptor state, and event state.
No failure rolls back memory writes already performed. Software owns buffer
synchronization and any deliberate retransmission.

Scalar RMEM and terminal status
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The initiating RMEM controller captures a CPUIF pulse and resolves its virtual
address with LOOKUP_BY_RMEM. It validates the full four-byte aligned word,
translates it once to the remote base, and sends a scalar command. A pending
RMEM operation has priority over unsent bulk fragments; an already advertised
or active fragment finishes first. The controller uses IDLE, LOOKUP_REQ,
LOOKUP_RSP, READY, SEND, WAIT, and DONE states in its own clocked process.

Successful reads return the completion's scalar data. Failed reads return
``cpuif_rd_data = 0xFFFFFFFF`` with ``cpuif_rd_ack``; failed writes assert
``cpuif_wr_ack``. The native CPUIF members are ``rd_data``, ``rd_ack``, and
``wr_ack`` respectively. The generated external CPUIF boundary remains ACK-only.
The shared peer error is recorded and an enabled RMEM_ERROR notification is
retained separately from bus completion.
The enable is captured when the failure is detected, so delayed IRQ admission
cannot reinterpret it. One pending notification bit per peer retains failed
accesses independently of the next CPUIF request. Repeated errors of that peer
before admission coalesce into that notification while each failure updates
the sticky CSR code. Pending peers are selected round-robin; a new failure wins
a simultaneous clear of its pending bit. Once an event has been admitted,
a later failure creates another pending notification. Reset clears these bits.
A lookup miss acknowledges the access as failed but
cannot identify a peer entry for per-peer CSR/IRQ reporting.

Received RMEM requests execute through ``m_local_cpuif`` using the request's
final byte address, 32-bit BitEnable, and scalar data. A validated zero-BitEnable
write succeeds without issuing a local CPUIF request. The local request is a
single-cycle pulse followed by ACK wait, allowing a same-cycle or delayed ACK.
A local CPUIF read/write error uses cause 4/6 respectively.

Every received request is checked against its peer's local base, size, and
permitted mode before memory access. Range arithmetic is 33-bit and rejects
wraparound. Accepted addresses and lengths are retained in the responder
context; subsequent configuration changes do not revalidate active servicing.

For incoming bulk writes, ``req_rx_status`` requires a join of final memory
completion and final framing/EndOfData status. Early data TLAST or a late bad
marker cannot report success. Rejected memory requests drain an accepted
payload without writing it. Local AXI causes 4..7 take precedence over a
consequent framing error. For initiating writes, ``tx_status`` holds the final
source-read result until the protocol engine accepts it.

``SERIAL_PEER_REQUESTS = 1`` permits one issued peer fragment until its local
and protocol completions retire. Unsent fragments of a failed block are
invalidated. Setting the parameter to zero permits multiple outstanding
commands for independent scheduler verification; endpoint integration retains
the sequential default and the protocol engine still has one initiating slot.
``FRAGMENT_SLOTS`` permits preparation and fair selection among peer contexts.

The isolated scheduler fixture selects ``SERIAL_PEER_REQUESTS = 0`` to check
reordered commands/completions independently of the protocol engine's single
initiating slot. Endpoint integration uses the sequential default. A completion
with no forwarded payload reports zero transferred bytes; a partial failure
reports the actual forwarded count. Internal routing and role metadata follow
:ref:`rtl-dma-transfer-if` and are never added to the wire protocol.

RMEM response timers and per-fragment DMA response timers belong to oETP.
Zero disables either timer. DMA timeout stops remaining fragments and records
TIMEOUT = 8; no whole-block timer or automatic retry is required.
The complete timer interval, response-matching rules, and wire-to-CSR error
mapping are specified in :ref:`rtl-oetp-engine`; the corresponding software
controls are summarized in :ref:`rtl-endpoint-full-csr`.

Functional scenarios
--------------------

These examples connect the command/status channels of
:ref:`rtl-dma-transfer-if` to the DMA engine's public memory and payload
ports. Interface-only handshakes and firmware IRQ service are covered by
:ref:`rtl-dma-transfer-if`, :ref:`rtl-irq-event-if`, and
:ref:`rtl-endpoint-full`.

All data paths are 32 bits wide. ``A0``, ``A1``, and subsequent
``A`` labels denote addresses; ``I0`` denotes a peer index, and
``S0/S1`` denote transfer sequences. ``DA0``, ``DA1``, ...
are data words leaving the local endpoint; ``DB0``, ``DB1``, ...
arrive from the peer. Scalar request data uses ``D0/D1``.
Labels are local to each example.

Raw Ethernet examples use 66-byte frames, counted from the destination MAC
through the final frame byte, excluding preamble, SFD, and FCS. Their first
16 beats have ``tkeep = 0xF``; beat 16 has ``tkeep = 0x3`` and
``tlast = 1``. Peer bulk streams carry the exact memory payload,
with oETP framing added or removed by the protocol engine.

A transfer occurs at the ending rising edge of a shown interval when VALID
and READY are both high. Gaps omit intermediate beats, arbitration, or
memory/transport waiting; timing across a gap is not a fixed latency.
``x`` marks irrelevant values. CSR field paths are relative to
``endpoint_if.csr_to_core`` for inputs and
``endpoint_if.core_to_csr`` for Core outputs, with generated
``.value/.next`` wrappers omitted.
AXI response codes are ``BRESP = 0`` for ``OKAY`` and ``BRESP = 2``
for ``SLVERR``.

Raw TX completion with a stalled final output beat
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Software has submitted an aligned source buffer ``A0`` and
``frame_length.bytes = 66``; IRQ admission and descriptor acceptance
have already completed. The read DMA supplies one complete raw frame on
``m_axis_oetp``. The gap omits ``DA2`` through ``DA14``.

After ``DA15`` transfers, the sink lowers READY and holds the final
``DA16`` beat. DATA, KEEP, LAST, and VALID remain stable throughout
that stall. The final memory-read result has already arrived and all 66
bytes have entered the TX register slice, so ``command_status.done``
and ``command_status.idle`` rise while the final output beat is still
waiting. ``transferred_length.bytes = 66`` reports this local handoff.

The later READY edge transfers ``DA16`` to oETP. Raw TX completion does
not wait for Ethernet serialization or a remote acknowledgement. If IRQ
admission reserved an event, source 1 is committed from the completed local
operation. A pending event commit can still delay acceptance of the next
CSR request even after the raw TX idle flag rises.

.. wavedrom::
    :name: endpoint-dma-raw-tx-buffered-tail-timing
    :caption: Raw TX completion while the final AXIS beat is stalled
    :alt: The TX register slice retains the final two frame bytes after local DMA completion.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p..|........"},
            ["FSM",
                {
                    "name": "raw_tx_state_reg",
                    "wave": "=..|=.==....",
                    "data": ["NON_TX_WAIT", "NON_TX_WAIT", "NON_\nTX_\nCOMMIT", "NON_TX_IDLE"],
                    "style": "font-size: 10px;"
                },
                {
                    "name": "memory_read_state_reg",
                    "wave": "=..|==......",
                    "data": ["RD_STREAM", "RD_\nSTREAM", "RD_IDLE"],
                    "style": "font-size: 8px;"
                }
            ],
            ["m_axis_oetp",
                ["Source",
                    {"name": "tvalid", "wave": "01.|......0."},
                    {
                        "name": "tdata",
                        "wave": "x==x==....x.",
                        "data": ["DA0", "DA1", "DA15", "DA16"]
                    },
                    {"name": "tkeep", "wave": "x=.x==....x.", "data": ["0xF", "0xF", "0x3"]},
                    {"name": "tlast", "wave": "x0.|.1....x."}
                ],
                ["Sink", {"name": "tready", "wave": "1..|.0...1.."}]
            ],
            {},
            ["endpoint_if",
                ["Core",
                    {"name": "non_oetp_dma.tx.command_status.idle", "wave": "0..|..1....."},
                    {"name": "non_oetp_dma.tx.command_status.done", "wave": "0..|..1....."},
                    {"name": "non_oetp_dma.tx.command_status.error", "wave": "0..|........"},
                    {
                        "name": "non_oetp_dma.tx.transferred_length.bytes",
                        "wave": "=..|..=.....",
                        "data": ["0", "66"]
                    }
                ]
            ]
        ],
        "config": {"hscale": 1}
    }

Raw RX overflow drains the frame and waits for AXI completion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An aligned receive buffer ``A0`` has capacity 65 bytes. Its descriptor
is armed, exclusively claimed, and assigned to this 66-byte raw frame
before the shown interval. Payload metadata selects
``ROUTE_NON_OETP_DMA``. The first gap omits ``DB2`` through
``DB15`` and the corresponding earlier AXI traffic.

The final input beat ``DB16`` carries two valid bytes
(``tkeep = 0x3``). Only its first byte fits in the descriptor.
The memory DMA writes that byte with ``wstrb = 0x1``, at
``A1 = A0 + 64``, and consumes the excess frame byte without writing
past the buffer. The final AXI beat holds its data, strobe, and WLAST
while WREADY is low. With the default 16-beat burst limit, this is the
one-beat second burst; the first burst writes the preceding 64 bytes.

Even after input TLAST, the descriptor remains busy until the final AXI
write response and memory-DMA terminal status have arrived. The illustrated
response is ``OKAY``, so the final result is the stream-capacity error:
``error_code = LOCAL_OVERFLOW``,
``received_length.bytes = 65``, ``idle = 1``, and ``done = 0``.
The stored length counts bytes written within capacity, not all incoming
frame bytes. Draining through TLAST preserves the next frame boundary.

.. wavedrom::
    :name: endpoint-dma-raw-rx-overflow-timing
    :caption: A 66-byte raw frame exceeds a 65-byte receive buffer
    :alt: The final two-byte input beat writes only one byte; overflow is reported after AXI completion.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p..|..|......|.."},
            ["FSM",
                {
                    "name": "raw_rx_state_reg",
                    "wave": "==.|=.|=.....|==",
                    "data": ["NON_\nRX_\nARMED",
                        "NON_RX_\nQUEUE",
                        "NON_RX_WAIT",
                        "NON_RX_WAIT",
                        "NON_RX_\nCOMMIT",
                        "NON_\nRX_IDLE"
                    ],
                    "style": "font-size: 8px;"
                },
                {
                    "name": "memory_write_state_reg",
                    "wave": "=..|=.|=.....|=.",
                    "data": ["WR_IDLE", "WR_\nSTREAM", "WR_STREAM", "WR_IDLE"]
                }
            ],
            ["s_axis_oetp",
                ["Source",
                    {"name": "tvalid", "wave": "01.|.0|......|.."},
                    {"name": "tdata", "wave": "x==x=x|......|..", "data": ["DB0", "DB1", "DB16"]},
                    {"name": "tkeep", "wave": "x=.x=x|......|..", "data": ["0xF", "0x3"]},
                    {"name": "tlast", "wave": "x0.|1x|......|.."}
                ],
                ["Sink", {"name": "tready", "wave": "1..|..|......|.."}]
            ],
            {},
            ["m_axi_wr",
                ["Master",
                    {"name": "wvalid", "wave": "0..|..|1..0..|.."},
                    {"name": "wdata", "wave": "x..|..|=..x..|..", "data": ["DB16"]},
                    {"name": "wstrb", "wave": "x..|..|=..x..|..", "data": ["0x1"]},
                    {"name": "wlast", "wave": "x..|..|1..x..|.."},
                    {"name": "bready", "wave": "1..|..|......|.."}
                ],
                ["Slave",
                    {"name": "wready", "wave": "1..|..|0.1...|.."},
                    {"name": "bvalid", "wave": "0..|..|....10|.."},
                    {"name": "bresp", "wave": "x..|..|....=x|..", "data": ["OKAY"]}
                ]
            ],
            {},
            ["endpoint_if",
                ["Core",
                    {"name": "non_oetp_dma.rx.command_status.idle", "wave": "0..|..|......|1."},
                    {"name": "non_oetp_dma.rx.command_status.done", "wave": "0..|..|......|.."},
                    {"name": "non_oetp_dma.rx.command_status.error", "wave": "0..|..|......|1."},
                    {
                        "name": "non_oetp_dma.rx.command_status.error_code",
                        "wave": "=..|..|......|=.",
                        "style": "font-size: 12px;",
                        "data": ["NONE", "LOCAL_\nOVERFLOW"]
                    },
                    {
                        "name": "non_oetp_dma.rx.received_length.bytes",
                        "wave": "=..|..|......|=.",
                        "data": ["0", "65"]
                    }
                ]
            ]
        ],
        "config": {"hscale": 1}
    }

Peer read retirement joins protocol and memory completion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use the sequential default ``SERIAL_PEER_REQUESTS = 1``. Peer
``I0`` mirrors a 66-byte remote block into local memory, with an accepted
64-byte fragment limit. Let ``A0`` be the local base and ``A1``
the remote base. The block retains these addresses and its fragment-size
snapshot even if software changes the corresponding CSRs while it runs.

.. list-table:: Fragment commands for the accepted block
   :class: documentation-table
   :header-rows: 1
   :widths: 15 22 22 15 26

   * - Sequence
     - Remote address
     - Local write address
     - Length
     - Block-final flag
   * - ``S0``
     - ``A1``
     - ``A0``
     - 64
     - 0
   * - ``S1``
     - ``A3 = A1 + 64``
     - ``A2 = A0 + 64``
     - 2
     - 1

The first fragment has already retired. The diagram begins with the final
``TRANSFER_KIND_DMA/DMA_OP_READ`` command, using ``req_addr = A3``,
``req_len = 2``, ``req_peer_idx = I0``, and ``req_last = 1``.
Its returned payload is ``DB16``, written at local address ``A2``.

The companion stream carries ``tid = S1``,
``tdest = {ROUTE_PEER, I0}``, the initiator role bit clear, and the
block-final user bit set. TLAST ends this fragment's payload; the user
bit distinguishes the final fragment of the block. These fields select
the matching local memory context and are not Ethernet-link metadata.

A successful protocol completion for ``I0/S1`` arrives before the
local AXI write response. The DMA engine retains that completion, keeps
the peer busy, and waits for memory completion. Only after the final
``OKAY`` response, terminal memory status, and fragment retirement do
``dma.idle`` and ``dma.done`` rise. An enabled peer event is emitted
once for the completed block, rather than once per fragment.

.. wavedrom::
    :name: endpoint-dma-peer-read-memory-join-timing
    :caption: Peer read completion waits for the final local AXI write
    :alt: The final two-byte fragment completes remotely before its local write response arrives.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p...|....|...|.."},
            ["FSM",
                {
                    "name": "memory_write_state_reg",
                    "wave": "=...|=.=.|=..|=.",
                    "data": ["WR_IDLE", "WR_IDLE", "WR_DESC", "WR_STREAM", "WR_IDLE"],
                    "style": "font-size: 12px;"
                }
            ],
            ["initiator_if",
                ["Requester",
                    {"name": "req_valid", "wave": "01.0|....|...|.."},
                    {"name": "req_sequence", "wave": "x=.x|....|...|..", "data": ["S1"]},
                    {"name": "cpl_ready", "wave": "1...|....|...|.."}
                ],
                ["Executor",
                    {"name": "req_ready", "wave": "0.10|....|...|.."},
                    {"name": "cpl_valid", "wave": "0...|..10|...|.."},
                    {"name": "cpl_sequence", "wave": "x...|..=x|...|..", "data": ["S1"]},
                    {"name": "cpl_transferred_len", "wave": "x...|..=x|...|..", "data": ["2"]},
                    {"name": "cpl_error", "wave": "x...|..0x|...|.."}
                ]
            ],
            {},
            ["s_axis_oetp",
                ["Source",
                    {"name": "tvalid", "wave": "0...|10..|...|.."},
                    {"name": "tdata", "wave": "x...|=x..|...|..", "data": ["DB16"]},
                    {"name": "tkeep", "wave": "x...|=x..|...|..", "data": ["0x3"]},
                    {"name": "tlast", "wave": "x...|1x..|...|.."}
                ],
                ["Sink", {"name": "tready", "wave": "1...|....|...|.."}]
            ],
            {},
            ["m_axi_wr",
                ["Master", {"name": "bready", "wave": "1...|....|...|.."}, {}],
                ["Slave",
                    {"name": "bvalid", "wave": "0...|....|.10|.."},
                    {"name": "bresp", "wave": "x...|....|.=x|..", "data": ["OKAY"]}
                ]
            ],
            {},
            ["endpoint_if",
                ["Core",
                    {"name": "peers.entry[I0].dma.idle", "wave": "0...|....|...|1."},
                    {"name": "peers.entry[I0].dma.done", "wave": "0...|....|...|1."},
                    {"name": "peers.entry[I0].dma.error", "wave": "0...|....|...|.."}
                ]
            ]
        ],
        "config": {"hscale": 1}
    }

Received write joins framing status and preserves the AXI cause
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A validated received command has already been accepted on ``responder_if``:
kind DMA, operation WRITE, peer ``I0``, sequence ``S0``, length 12,
and ``req_rx_status = 1``. Its destination lies inside the peer's local
mirror-to-local window. Payload metadata selects ``{ROUTE_PEER, I0}``,
sequence ``S0``, and the responder role.

The input ends early after two full words, ``DB0/DB1``, or eight bytes.
The gap includes their AXI write traffic. The memory slave returns
``BRESP = SLVERR``, which maps to local write cause 6. The protocol
engine later supplies matching receive terminal status with length 8
and framing cause 2. No completion is advertised while this required
status is still missing, even though memory servicing has ended.

Once both outcomes are known, the local AXI error takes precedence:
the responder completion has ``cpl_error = 1``,
``cpl_error_code = LOCAL_AXI_WR_SLVERR``, and ``cpl_transferred_len = 8``.
The peer CSR error is recorded before that completion becomes visible.
Without an AXI error, the framing failure would instead use wire cause
``LOCAL_AXIS`` in the completion and ``REMOTE_AXIS`` in the receiving peer's CSR.
No error path rolls back memory writes already performed.

Assume the error's IRQ source is enabled but
``responder_irq_event_if.admit_ready = 0`` throughout this interval.
The completion still transfers to the ready protocol engine. Its retained
notification keeps ``responder_if.req_ready = 0`` after the reply,
until IRQ admission and any reserved commit finish. Reporting this incoming
failure does not finish or replace an independently initiated peer block.

.. wavedrom::
    :name: endpoint-dma-responder-error-join-timing
    :caption: Received-write completion joins framing status with the original AXI error
    :alt: A late framing error cannot replace AXI write cause 6; IRQ admission does not block the reply.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p...|..|......."},
            ["FSM",
                {
                    "name": "responder_state_reg",
                    "wave": "=...|=.|=.=..=.",
                    "data": ["RESP_WR_QUEUE", "RESP_WAIT", "RESP_WAIT", "RESP_COMPLETE", "RESP_IDLE"],
                    "style": "font-size: 10px;"
                },
                {
                    "name": "memory_write_state_reg",
                    "wave": "=..=|=.|=......",
                    "data": ["WR_IDLE", "WR_\nDESC", "WR_STREAM", "WR_IDLE"],
                    "style": "font-size: 8px;"
                }
            ],
            ["s_axis_oetp",
                ["Source",
                    {"name": "tvalid", "wave": "01.0|..|......."},
                    {"name": "tdata", "wave": "x==x|..|.......", "data": ["DB0", "DB1"]},
                    {"name": "tkeep", "wave": "x=.x|..|.......", "data": ["0xF"]},
                    {"name": "tlast", "wave": "x01x|..|......."}
                ],
                ["Sink", {"name": "tready", "wave": "1..0|1.|......."}]
            ],
            {},
            ["m_axi_wr",
                ["Master", {"name": "bready", "wave": "1...|..|......."}, {}],
                ["Slave",
                    {"name": "bvalid", "wave": "0...|10|......."},
                    {
                        "name": "bresp",
                        "wave": "x...|=x|.......",
                        "style": "font-size: 10px;",
                        "data": ["SLVERR"]
                    }
                ]
            ],
            {},
            ["responder_if",
                ["Requester",
                    {"name": "rx_status_valid", "wave": "0...|..|10....."},
                    {"name": "rx_status_len", "wave": "x...|..|=x.....", "data": ["8"]},
                    {
                        "name": "rx_status_error_code",
                        "wave": "x...|..|=x.....",
                        "style": "font-size: 10px;",
                        "data": ["LOCAL_\nAXIS"]
                    },
                    {"name": "cpl_ready", "wave": "1...|..|......."}
                ],
                ["Executor",
                    {"name": "rx_status_ready", "wave": "1...|..|.0....."},
                    {"name": "req_ready", "wave": "0...|..|......."},
                    {"name": "cpl_valid", "wave": "0...|..|....10."},
                    {"name": "cpl_transferred_len", "wave": "x...|..|....=x.", "data": ["8"]},
                    {"name": "cpl_error", "wave": "x...|..|....1x."},
                    {
                        "name": "cpl_error_code",
                        "wave": "x...|..|....=x.",
                        "style": "font-size: 10px;",
                        "data": ["LOCAL_\nAXI_\nWR_\nSLVERR"]
                    }
                ]
            ],
            {},
            ["endpoint_if",
                ["Core",
                    {"name": "peers.entry[I0].dma.error", "wave": "0...|..|...1..."},
                    {
                        "name": "peers.entry[I0].dma.error_code",
                        "wave": "=...|..|...=...",
                        "style": "font-size: 12px;",
                        "data": ["NONE", "LOCAL_AXI_WR_SLVERR"]
                    }
                ],
                {}
            ]
        ],
        "config": {"hscale": 1}
    }

Scalar writes with zero and nonzero BitEnable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Both received requests are validated ``TRANSFER_KIND_RMEM/DMA_OP_WRITE``
commands for peer ``I0``, with length four, aligned addresses
``A0/A1`` inside an RMEM-mode window, and ``req_rx_status = 0``.
They require no AXIS payload or AXI memory descriptor.

The first request, sequence ``S0``, uses ``M0 = 0x00000000``.
It succeeds with four transferred bytes without issuing a local CPUIF
request. Window validation still applies before this zero-enable shortcut.

The second request, sequence ``S1``, uses
``M1 = 0x0000000F``, enabling bits 3:0 of scalar data ``D1``.
The DMA engine issues one local CPUIF write pulse and retains the address,
data, and per-bit enable while waiting for the delayed write ACK.
A successful ACK permits the four-byte completion, which remains stable
until the requester accepts it.

In the numbered example, requests transfer in cycles 1 and 5.
The second request produces the local CPUIF pulse in cycle 7, receives
ACK in cycle 9, and presents its completion from cycle 11 through
acceptance in cycle 13. The first completion transfers in cycle 3
without any local request pulse.

.. wavedrom::
    :name: endpoint-dma-rmem-zero-enable-timing
    :caption: Zero-enable RMEM write and a scalar write with delayed local acknowledgement
    :alt: Only the nonzero BitEnable request issues a local CPUIF pulse; both report four transferred bytes.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p.............."},
            [
                "FSM",
                {
                    "name": "responder_state_reg",
                    "wave": "=.=.=.==..=...=",
                    "data": [
                        "RESP_IDLE",
                        "RESP_\nCOMPLETE",
                        "RESP_IDLE",
                        "RESP_\nRMEM_\nREQ",
                        "RESP_RMEM_WAIT",
                        "RESP_COMPLETE",
                        "RESP_\nIDLE"
                    ],
                    "style": "font-size: 10px;"
                }
            ],
            ["responder_if",
                ["Requester",
                    {"name": "req_valid", "wave": "010..10........"},
                    {"name": "req_addr", "wave": "x=x..=x........", "data": ["A0", "A1"]},
                    {"name": "req_biten", "wave": "x=x..=x........", "data": ["M0", "M1"]},
                    {"name": "req_wdata", "wave": "x=x..=x........", "data": ["D0", "D1"]},
                    {"name": "req_sequence", "wave": "x=x..=x........", "data": ["S0", "S1"]},
                    {"name": "cpl_ready", "wave": "1....0.......1."}
                ],
                ["Executor",
                    {"name": "req_ready", "wave": "1.0..10........"},
                    {"name": "cpl_valid", "wave": "0..10......1..0"},
                    {"name": "cpl_sequence", "wave": "x..=x......=..x", "data": ["S0", "S1"]},
                    {"name": "cpl_transferred_len", "wave": "x..=x......=..x", "data": ["4", "4"]},
                    {"name": "cpl_error", "wave": "x..0x......0..x"}
                ]
            ],
            {},
            ["m_local_cpuif",
                ["Master",
                    {"name": "req", "wave": "0......10......"},
                    {"name": "req_is_wr", "wave": "x......1..x...."},
                    {"name": "addr", "wave": "x......=..x....", "data": ["A1"]},
                    {"name": "wr_data", "wave": "x......=..x....", "data": ["D1"]},
                    {"name": "wr_biten", "wave": "x......=..x....", "data": ["M1"]}
                ],
                ["Slave",
                    {"name": "wr_ack", "wave": "0........10...."},
                    {"name": "wr_err", "wave": "0.............."}
                ]
            ]
        ],
        "head": {"tick": 0},
        "config": {"hscale": 1}
    }

Scalar read with delayed local acknowledgement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A received ``TRANSFER_KIND_RMEM/DMA_OP_READ`` command selects peer ``I0``
and sequence ``S0``, with ``req_len = 4`` and ``req_rx_status = 0``.
Its aligned ``req_addr = A0`` is the final local byte address inside the
peer's RMEM-mode window. Scalar read data returns in ``cpl_rdata``.

The command transfers in cycle 1. The DMA engine issues one local CPUIF
read pulse in cycle 3 with ``req_is_wr = 0``, then waits without repeating
the request. The memory returns ``rd_ack = 1`` and ``rd_data = D0`` in
cycle 6. The engine captures the data at that acknowledgement edge.

The successful completion becomes valid in cycle 8, with
``cpl_rdata = D0``, ``cpl_transferred_len = 4``, and the original
``I0/S0`` context. The requester delays acceptance until cycle 10;
VALID, data, and completion metadata remain stable throughout the stall,
even after local ``rd_ack`` has returned low. The responder is ready for
another command in cycle 12.

If ``rd_err`` accompanies the local ACK, the engine instead reports
``LOCAL_AXI_RD_SLVERR`` in a failed completion and records
the peer diagnostic before advertising that completion.

.. wavedrom::
    :name: endpoint-dma-rmem-read-timing
    :caption: RMEM read data retained after a delayed local acknowledgement
    :alt: A single local read pulse receives data D0 before the held scalar completion is accepted.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p............"},
            [
                "FSM",
                {
                    "name": "responder_state_reg",
                    "wave": "=.==...=...=.",
                    "data": [
                        "RESP_IDLE",
                        "RESP_\nRMEM_\nREQ",
                        "RESP_RMEM_WAIT",
                        "RESP_COMPLETE",
                        "RESP_IDLE"
                    ],
                    "style": "font-size: 10px;"
                }
            ],
            ["responder_if",
                ["Requester",
                    {"name": "req_valid", "wave": "010.........."},
                    {"name": "req_addr", "wave": "x=x..........", "data": ["A0"]},
                    {"name": "req_sequence", "wave": "x=x..........", "data": ["S0"]},
                    {"name": "cpl_ready", "wave": "0.........1.."}
                ],
                ["Executor",
                    {"name": "req_ready", "wave": "1.0.........1"},
                    {"name": "cpl_valid", "wave": "0.......1..0."},
                    {"name": "cpl_sequence", "wave": "x.......=..x.", "data": ["S0"]},
                    {"name": "cpl_transferred_len", "wave": "x.......=..x.", "data": ["4"]},
                    {"name": "cpl_rdata", "wave": "x.......=..x.", "data": ["D0"]},
                    {"name": "cpl_error", "wave": "x.......0..x."}
                ]
            ],
            {},
            ["m_local_cpuif",
                ["Master",
                    {"name": "req", "wave": "0..10........"},
                    {"name": "req_is_wr", "wave": "0............"},
                    {"name": "addr", "wave": "x..=...x.....", "data": ["A0"]}
                ],
                ["Slave",
                    {"name": "rd_ack", "wave": "0.....10....."},
                    {"name": "rd_data", "wave": "x.....=x.....", "data": ["D0"]},
                    {"name": "rd_err", "wave": "0............"}
                ]
            ]
        ],
        "head": {"tick": 0},
        "config": {"hscale": 1}
    }

.. _verification-openenoc-endpoint-dma-engine:

Verification
------------

The test suite is in ``dv/core/openenoc_endpoint_dma_engine/``.

Testbench
~~~~~~~~~

This cocotb suite verifies DMA memory access, fragmentation, peer/raw flows, errors, and
backpressure in isolation. It uses AXI memory and AXI4-Stream models, a behavioral peer-lookup
responder, and driven IRQ and transaction handshakes. The fixture uses four peers, eight
fragment slots, and 32-bit data. Pytest runs 18 cases at raw-frame ceilings of 96 and 8192
bytes; compact transfer cases use a 64-byte local fragment size. The scheduler fixture enables
multiple outstanding commands to exercise reordered completions.

A subcycle test checks control, CSR, IRQ, AXIS, and all AXI master outputs during an active
memory read, and verifies that a held clear cannot erase a later failure.

Coverage
~~~~~~~~

The suite covers:

- raw TX/RX with unaligned addresses, full Ethernet frames, descriptor claims, and length/status
  reporting;

- peer mirror-to-remote writes and mirror-to-local reads with exact payload and guard-byte checks;

- fragmentation, slot reuse, concurrent peers, reordered completions, and final-fragment metadata;

- fragment-size rounding, configuration snapshots, valid boundaries, and invalid-setting
  rejection;

- 8192-byte unaligned raw TX across two local reads, including source errors in either part;

- scalar RMEM validation, command kinds, BitEnable, error recording, and separate IRQ
  notification;

- received READ/WRITE servicing, local windows, role disambiguation, and simultaneous
  initiator/responder traffic;

- local/remote error encoding, full-width wire causes, and original AXI-cause precedence;

- partial writes, late framing errors, terminal-status joins, and bilateral failure reporting;

- sticky peer/raw errors, independent clear commands, simultaneous new failure, and clearing
  during active transfers;

- IRQ gating, retained event metadata, admission/commit stalls, and one commit per admitted event;

- command, CSR, IRQ, AXIS, and AXI output stability under backpressure and between clock edges.
