.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-dma-engine:

DMA Engine -- openenoc_endpoint_dma_engine
==========================================

Executes local memory operations for peer transfers, raw Ethernet DMA, and
scalar remote memory accesses.

**Source:** :download:`openenoc_endpoint_dma_engine.sv <../../../hw/rtl/core/openenoc_endpoint_dma_engine.sv>`.

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
   * - ``NUM_OF_PEERS``
     - ``4``
     - Integer >= 1; match generated CSR array
     - Number of peer-table entries.
   * - ``PEER_IDX_W``
     - ``NUM_OF_PEERS > 1 ? $clog2( NUM_OF_PEERS ) : 1``
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
   * - ``peer_lookup_if``
     - ``openenoc_peer_lookup_if.mst``
     - bidirectional (mst)
     - Peer-table query client and coherent response snapshot.
   * - ``initiator_if``
     - ``openenoc_dma_transfer_if.requester``
     - bidirectional (requester)
     - Commands and status for locally initiated remote transactions.
   * - ``responder_if``
     - ``openenoc_dma_transfer_if.executor``
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
     - ``openenoc_irq_event_if.producer``
     - bidirectional (producer)
     - Peer-DMA, raw-TX, and raw-RX event producers, in that order.
   * - ``rmem_irq_event_if``
     - ``openenoc_irq_event_if.producer``
     - bidirectional (producer)
     - Independent initiating RMEM error-event producer.
   * - ``responder_irq_event_if``
     - ``openenoc_irq_event_if.producer``
     - bidirectional (producer)
     - Received-request servicing error-event producer.

Architecture and operation
--------------------------

Responsibilities and boundary
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

Registered control and memory boundaries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The peer scheduler, raw TX, raw RX, responder, memory read, memory write,
RMEM, and notification controllers each use a separate clocked process with
direct nonblocking register updates. The peer scheduler alone owns the shared
peer and fragment contexts; memory controllers report accepted and completed
operations through registered event pulses. Arbitration and stream assembly
are internal combinational calculations.
CSR status fields alias the owning status registers. Hardware clears, lookup
requests, transfer commands/completions, CPUIF signals, and IRQ producer signals are registered. A held CSR clear command
is applied once; a failure arriving before that command deasserts remains sticky.

Two-entry skid buffers register both directions of the memory-payload AXIS link.
All five AXI channels use registered skid boundaries, including RREADY and
BREADY. Data accepted before downstream backpressure takes effect remains in
those buffers. This adds pipeline latency to memory access without introducing
full-fragment buffering or changing the terminal-status join.

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
``config.dma_max_fragment_size.bytes`` after rounding down to a multiple of
four. Its effective value must be between 4 and the physical ceiling.
Intermediate fragments use that limit; the final fragment carries exactly
the remaining bytes and can be shorter than four bytes. Incoming requests are
bounded by the physical ceiling, independently of the receiver's local CSR
fragment-size setting.

``FRAGMENT_SLOTS`` bounds local bookkeeping contexts; it is not a wire credit
mechanism. The oETP scheduler implements the agreed sequential unicast
request-response policy. Raw frames are not divided into peer protocol
fragments. For a maximum-size unaligned raw TX read that exceeds the underlying
TAXI read counter's safe budget, the engine uses two local read descriptors
and suppresses the intermediate TLAST, producing one Ethernet frame.

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
all ones with read ACK; failed writes receive write ACK. The generated external
CPUIF boundary remains ACK-only. The shared peer error is recorded and an
enabled RMEM_ERROR notification is retained separately from bus completion.
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

Verification and reference work
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``dv/core/openenoc_endpoint_dma_engine/`` exercises memory access,
fragmentation, peer/raw flows, errors, and backpressure. Its scheduler fixture
also exercises multiple outstanding commands and reordered completions.
A subcycle test checks control, CSR, IRQ, AXIS, and all AXI master outputs during
an active memory read, and verifies that a held clear cannot erase a later failure.
``dv/core/openenoc_endpoint_interface/`` verifies the integrated sequential
transport, RMEM CPUIF, memory-window checks, terminal-status joins, AXI failure
precedence, abort/restart, and retained IRQ notifications with a full queue.

Functional scenarios
--------------------

This section reserves space for scenario descriptions and WaveDrom timing
diagrams. The current outline is:

* Raw transmit/receive, unaligned memory access, and descriptor claims.
* Peer read/write fragmentation, fragment-size snapshots, and partial tails.
* Scalar accesses, priority over bulk traffic, and zero-enable writes.
* Local/remote failures, sticky error clearing, and retained IRQ notifications.
* Concurrent initiator/responder roles and terminal-status joins.
