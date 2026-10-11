.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-dma-transfer-if:

DMA and RMEM Transfer Interface -- openenoc_dma_transfer_if
===========================================================

Defines commands, completions, and terminal status for bulk memory transfers
and scalar remote accesses.

**Source:** :download:`openenoc_dma_transfer_if.sv <../../../hw/rtl/core/openenoc_dma_transfer_if.sv>`.

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
   * - ``ADDR_W``
     - ``32``
     - Integer >= 1
     - Byte-address width in bits; connected interfaces must agree.
   * - ``LEN_W``
     - ``32``
     - Integer >= 1; endpoint protocol uses 32
     - Byte-count width for memory commands and terminal status.
   * - ``PEER_IDX_W``
     - ``1``
     - Integer >= 1; enough bits for the peer count
     - Width of local peer indices; all connected interfaces must agree.
   * - ``SEQUENCE_W``
     - ``32``
     - Integer >= 1; endpoint transfer metadata uses 32
     - Width of local fragment sequence metadata; separate from wire Request ID.
   * - ``ERROR_W``
     - ``4``
     - Integer >= 4
     - Width of completion/status error codes, including local and remote causes.

Signals
-------

Directions are relative to the named modport. The monitor modport, where
present, observes signals as inputs and does not drive them.

.. list-table:: Public signals and interfaces
   :class: rtl-reference-table
   :header-rows: 1
   :widths: 26 27 17 30

   * - Name
     - Type
     - Direction / role
     - Description
   * - ``non_oetp_rx_available``
     - ``logic``
     - requester: input; executor: output
     - An armed, unclaimed raw-DMA receive descriptor is available.
   * - ``non_oetp_rx_claim_valid``
     - ``logic``
     - requester: output; executor: input
     - Requests exclusive ownership of one armed raw receive descriptor.
   * - ``non_oetp_rx_claim_ready``
     - ``logic``
     - requester: input; executor: output
     - Accepts and reserves the raw receive descriptor claim.
   * - ``req_valid``
     - ``logic``
     - requester: output; executor: input
     - Request fields are valid and retained until accepted.
   * - ``req_ready``
     - ``logic``
     - requester: input; executor: output
     - Executor accepts the request on this handshake.
   * - ``req_kind``
     - ``logic``
     - requester: output; executor: input
     - Transfer kind: zero bulk DMA, one scalar RMEM.
   * - ``req_op``
     - ``logic``
     - requester: output; executor: input
     - Operation in executor address space: zero read, one write.
   * - ``req_addr``
     - ``logic [ADDR_W-1:0]``
     - requester: output; executor: input
     - Final byte address in the executor target address space.
   * - ``req_len``
     - ``logic [LEN_W-1:0]``
     - requester: output; executor: input
     - Requested memory bytes; scalar RMEM uses four.
   * - ``req_peer_idx``
     - ``logic [PEER_IDX_W-1:0]``
     - requester: output; executor: input
     - Local peer entry associated with the transaction.
   * - ``req_sequence``
     - ``logic [SEQUENCE_W-1:0]``
     - requester: output; executor: input
     - Local fragment sequence used to join payload and completion.
   * - ``req_last``
     - ``logic``
     - requester: output; executor: input
     - Marks the final fragment of a locally initiated block.
   * - ``req_biten``
     - ``logic [31:0]``
     - requester: output; executor: input
     - 32-bit write mask for scalar RMEM; unused for bulk DMA.
   * - ``req_wdata``
     - ``logic [31:0]``
     - requester: output; executor: input
     - Scalar RMEM write word; unused for bulk DMA.
   * - ``req_error_code``
     - ``logic [ERROR_W-1:0]``
     - requester: output; executor: input
     - Early protocol rejection without authorizing memory access.
   * - ``req_rx_status``
     - ``logic``
     - requester: output; executor: input
     - Incoming write also requires final framing/EndOfData status.
   * - ``tx_status_valid``
     - ``logic``
     - requester: output; executor: input
     - Source-read terminal status is valid.
   * - ``tx_status_ready``
     - ``logic``
     - requester: input; executor: output
     - Source-read terminal status is accepted.
   * - ``tx_status_peer_idx``
     - ``logic [PEER_IDX_W-1:0]``
     - requester: output; executor: input
     - Source-read local peer entry.
   * - ``tx_status_sequence``
     - ``logic [SEQUENCE_W-1:0]``
     - requester: output; executor: input
     - Source-read local fragment sequence.
   * - ``tx_status_len``
     - ``logic [LEN_W-1:0]``
     - requester: output; executor: input
     - Source-read actual delivered memory byte count.
   * - ``tx_status_error_code``
     - ``logic [ERROR_W-1:0]``
     - requester: output; executor: input
     - Source-read terminal cause; zero means success.
   * - ``rx_status_valid``
     - ``logic``
     - requester: output; executor: input
     - Receive-framing terminal status is valid.
   * - ``rx_status_ready``
     - ``logic``
     - requester: input; executor: output
     - Receive-framing terminal status is accepted.
   * - ``rx_status_peer_idx``
     - ``logic [PEER_IDX_W-1:0]``
     - requester: output; executor: input
     - Receive-framing local peer entry.
   * - ``rx_status_sequence``
     - ``logic [SEQUENCE_W-1:0]``
     - requester: output; executor: input
     - Receive-framing local fragment sequence.
   * - ``rx_status_len``
     - ``logic [LEN_W-1:0]``
     - requester: output; executor: input
     - Receive-framing actual delivered memory byte count.
   * - ``rx_status_error_code``
     - ``logic [ERROR_W-1:0]``
     - requester: output; executor: input
     - Receive-framing terminal cause; zero means success.
   * - ``cpl_valid``
     - ``logic``
     - requester: input; executor: output
     - Completion fields are valid and retained until accepted.
   * - ``cpl_ready``
     - ``logic``
     - requester: output; executor: input
     - Requester accepts the completion.
   * - ``cpl_kind``
     - ``logic``
     - requester: input; executor: output
     - Transfer kind echoed from the request.
   * - ``cpl_op``
     - ``logic``
     - requester: input; executor: output
     - Operation echoed from the request.
   * - ``cpl_transferred_len``
     - ``logic [LEN_W-1:0]``
     - requester: input; executor: output
     - Memory bytes actually transferred.
   * - ``cpl_peer_idx``
     - ``logic [PEER_IDX_W-1:0]``
     - requester: input; executor: output
     - Matching local peer entry.
   * - ``cpl_sequence``
     - ``logic [SEQUENCE_W-1:0]``
     - requester: input; executor: output
     - Matching local fragment sequence.
   * - ``cpl_last``
     - ``logic``
     - requester: input; executor: output
     - Final-block context echoed from the request.
   * - ``cpl_error``
     - ``logic``
     - requester: input; executor: output
     - Completion reports a failure.
   * - ``cpl_error_code``
     - ``logic [ERROR_W-1:0]``
     - requester: input; executor: output
     - Final CSR cause on the initiator path; wire cause on the responder path.
   * - ``cpl_rdata``
     - ``logic [31:0]``
     - requester: input; executor: output
     - Scalar RMEM read result; unused for bulk DMA.

Architecture and operation
--------------------------

This symmetric command/completion interface connects the memory owner,
:ref:`rtl-dma-engine`, to :ref:`rtl-oetp-engine`. It is instantiated twice:

* Initiator path: DMA is the requester; oETP is the executor.
* Responder path: oETP is the requester; DMA is the executor.

Command and completion
~~~~~~~~~~~~~~~~~~~~~~

``req_valid/req_ready`` and ``cpl_valid/cpl_ready`` are independent handshakes.
Keep each channel's fields stable while valid is asserted and ready is clear.
The request carries kind, operation, final byte address, length, peer index,
fragment sequence, final-block flag, and the scalar RMEM fields. Completion
returns kind, operation, transferred length, matching peer/sequence/final-block
context, error flag/code, and scalar read data.

``DMA_OP_READ = 0`` and ``DMA_OP_WRITE = 1`` are defined from the executor's
point of view. ``req_addr`` is already in the executor's target address space.
The requester performs address translation once. The executor may validate
the permitted memory region but must not translate the address again.

``req_kind`` distinguishes ``TRANSFER_KIND_DMA = 0`` from
``TRANSFER_KIND_RMEM = 1``, including when a bulk fragment is four bytes long.
RMEM uses ``req_len = 4``, ``req_biten`` and ``req_wdata`` for writes, and
``cpl_rdata`` for reads. RMEM has no AXIS payload; the scalar fields are unused
for bulk DMA. RMEM reads do not transfer BitEnable.

Error reporting
~~~~~~~~~~~~~~~

Initiator completions carry final CSR error codes: local causes 1..7, local
TIMEOUT 8, and remote causes 9..15. The oETP engine validates the full 32-bit
ERROR_RSP cause with ``csr_error_from_wire``: wire causes 1..7 map to CSR
codes 9..15; every other wire value maps to local invalid-operation code 1.
The DMA engine preserves the encoding rather than inferring error origin from
the completion channel.

An incomplete received DMA data frame, including missing or incorrect
EndOfData, directly records remote stream code 10 without requiring an
ERROR_RSP first. Responder completions instead supply wire causes 1..7. An
incomplete incoming write returns cause 2 while its receiving peer CSR records
code 10. The complete mapping is specified in :ref:`rtl-oetp-engine` and the
RDL-derived HAL.

On the responder path, ``req_peer_idx`` identifies the receiving endpoint's
peer entry resolved from the request's source MAC. DMA records a servicing
failure there before exposing completion and retains an enabled local IRQ
independently of the reply. Success generates no responder IRQ. Diagnostics
do not change the idle/done state of a separately initiated transfer.

Companion AXIS contract
~~~~~~~~~~~~~~~~~~~~~~~

Each direction carries one shared stream. The route field in
``TDEST = {route[1:0], peer_idx}`` selects:

.. list-table:: Internal routes
   :header-rows: 1
   :widths: 15 30 55

   * - Code
     - Constant
     - Payload
   * - 0
     - ``ROUTE_PEER``
     - Exactly ``req_len`` memory bytes, ordered by increasing address.
   * - 1
     - ``ROUTE_NON_OETP_DMA``
     - Complete Ethernet frame, from Destination MAC through payload/padding.
   * - 2
     - ``ROUTE_DIRECT``
     - Ethernet frame from or to the direct CSR stream.
   * - 3
     - ``ROUTE_DROP``
     - Discard route.

Peer payload contains no address/length fields, Ethernet/oETP headers,
EndOfData, protocol word padding, Ethernet padding, or FCS. Address and length
travel on the command channel. Raw frames retain their Ethernet headers and
any existing Ethernet padding, but exclude preamble, SFD, and FCS.

``TKEEP`` selects actual bytes and ``TLAST`` ends one memory fragment or raw
frame. ``TID`` carries the local fragment sequence. ``TUSER[0]`` marks the final
fragment of a block; ``TUSER[1]`` selects local role, initiator 0 or responder 1.
Keep metadata stable throughout a peer fragment, through accepted ``TLAST``.
The role disambiguates equal peer/sequence values on independent command paths.
Raw/direct streams use role zero. These fields are internal metadata rather
than oETP wire parameters.

Every started stream frame or fragment ends with TLAST, even when it is shorter
than the requested length because of an operation error. Missing TLAST is a
transport-contract violation; no separate missing-TLAST watchdog is specified.
Small pipeline buffers may synchronize data and control while retaining the
streaming contract.

Raw receive descriptor claim
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The responder path also exposes ``non_oetp_rx_available`` and
``non_oetp_rx_claim_valid/ready``. Claim one armed descriptor before submitting
its frame. The handshake reserves it once, independently of AXIS/FIFO readiness;
no further claim is accepted until software arms the next descriptor.
Hold claim valid until accepted, then supply exactly one
``ROUTE_NON_OETP_DMA`` frame. ``available`` describes an unclaimed descriptor,
not available FIFO space. Filtered frames must not consume a descriptor.

Terminal status channels
~~~~~~~~~~~~~~~~~~~~~~~~~

``req_error_code`` carries an early protocol rejection to the memory/status
owner without permitting a memory descriptor. ``req_rx_status`` marks an
incoming bulk write that also requires final RX framing/EndOfData validation.
A rejected write can still require that status while its wire frame is drained.

.. list-table:: Final status ownership
   :header-rows: 1
   :widths: 22 28 50

   * - Operation
     - Channel
     - Producer and meaning
   * - Initiating DMA write
     - ``initiator_if.tx_status``
     - DMA reports final source-read byte count and local error to oETP.
   * - Responding DMA read
     - ``responder_if.cpl``
     - DMA reports final source-read completion to oETP.
   * - Incoming DMA write
     - ``responder_if.rx_status``
     - oETP reports final delivered byte count and framing outcome to DMA.
   * - Matched DMA read reply
     - ``initiator_if.cpl``
     - oETP reports final response validity and delivered byte count to DMA.

The explicit status channels have valid/ready, peer index, local sequence,
length, and error code. TX status contains local CSR causes. Incoming RX
framing failure uses cause 2 on this interface; DMA records the resulting
remote stream code 10 while returning wire cause 2 in its completion.
An AXI source/target error keeps its original local cause over a derived stream
failure. The interface instance identifies the command path.

Status is independent of payload progress and remains stable until accepted.
Data TLAST does not authorize a successful wire trailer or completion: success
requires the associated final status. Zero delivered bytes with a receive error
permit cancellation of an unstarted memory descriptor. Partial data ends with
TLAST and is drained before the context is recycled. ``TUSER[0]`` remains a
final-block flag and ``TUSER[1]`` remains a role; neither conveys an error.

The detailed streaming and failure rules are specified in :ref:`rtl-oetp-engine`.

Functional scenarios
--------------------

This section reserves space for scenario descriptions and WaveDrom timing
diagrams. The current outline is:

* Initiator and responder command/completion handshakes.
* Exact memory payloads, raw frames, and role metadata.
* Descriptor claims, partial transfers, and terminal error status.
