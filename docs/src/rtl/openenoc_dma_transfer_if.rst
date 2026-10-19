.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-dma-transfer-if:

DMA and RMEM Transfer Interface -- openenoc_dma_transfer_if
===========================================================

.. index::
   single: openenoc_dma_transfer_if

Defines commands, completions, and terminal status for bulk memory transfers
and scalar remote accesses.

**Source:**
:download:`openenoc_dma_transfer_if.sv <../../../hw/rtl/core/openenoc_dma_transfer_if.sv>`.

Parameters
----------

.. list-table:: Parameters
   :class: rtl-reference-table
   :header-rows: 1
   :widths: 18 18 22 42

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

Directions are relative to the ``requester`` and ``executor`` modports.
The ``mon`` modport observes all signals as inputs.

.. list-table:: Public signals and interfaces
   :class: rtl-reference-table
   :header-rows: 1
   :widths: 28 28 16 28

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
     - Accepts the request when req_valid is also asserted.
   * - ``req_kind``
     - ``logic``
     - requester: output; executor: input
     - ``TRANSFER_KIND_DMA`` or ``TRANSFER_KIND_RMEM``.
   * - ``req_op``
     - ``logic``
     - requester: output; executor: input
     - ``DMA_OP_READ`` or ``DMA_OP_WRITE`` in executor address space.
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
     - Source-read terminal cause; ``NONE`` means success.
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
     - Accepts the completion when cpl_valid is also asserted.
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
Each transfer occurs on a rising edge with both VALID and READY high. Assert
VALID when a transfer is available, without waiting for READY, and retain
VALID and the channel's fields until acceptance. The same rule applies to
descriptor claims and terminal status channels. Clock and reset belong to
the connected modules; the interface contains no clock/reset ports or storage.
The request carries kind, operation, final byte address, length, peer index,
fragment sequence, final-block flag, and the scalar RMEM fields. Completion
returns kind, operation, transferred length, matching peer/sequence/final-block
context, error flag/code, and scalar read data.

An initiating write's ``tx_status_len`` reports bytes read from its local
source. Its ``cpl_transferred_len`` reports the transaction result; the
current oETP executor returns zero when a source error aborts that write.
The source-read count alone does not establish successful remote delivery.

``DMA_OP_READ = 0`` and ``DMA_OP_WRITE = 1`` are defined from the executor's
point of view. ``req_addr`` is already in the executor's target address space.
The requester performs address translation once. The executor may validate
the permitted memory region but must not translate the address again.

``req_kind`` distinguishes ``TRANSFER_KIND_DMA = 0`` from
``TRANSFER_KIND_RMEM = 1``, including when a bulk fragment is four bytes long.
The interface defines ``RMEM_WORD_BYTES = 4``. RMEM uses
``req_len = RMEM_WORD_BYTES``, ``req_biten`` and ``req_wdata`` for writes, and
``cpl_rdata`` for reads. RMEM has no AXIS payload; the scalar fields are
unused for bulk DMA. RMEM reads do not transfer BitEnable.

.. list-table:: Transfer kind and operation encodings
   :class: documentation-table
   :header-rows: 1
   :widths: 26 10 26 38

   * - Field
     - Code
     - Interface constant
     - Meaning
   * - ``req_kind``, ``cpl_kind``
     - 0
     - ``TRANSFER_KIND_DMA``
     - Bulk memory transfer.
   * - ``req_kind``, ``cpl_kind``
     - 1
     - ``TRANSFER_KIND_RMEM``
     - Scalar remote-memory access.
   * - ``req_op``, ``cpl_op``
     - 0
     - ``DMA_OP_READ``
     - Read the executor's memory.
   * - ``req_op``, ``cpl_op``
     - 1
     - ``DMA_OP_WRITE``
     - Write the executor's memory.

.. _rtl-dma-transfer-error-codes:

Error reporting
~~~~~~~~~~~~~~~

The following encodings apply to ``req_error_code``,
``tx_status_error_code``, ``rx_status_error_code``, and ``cpl_error_code``.
Interface constants have the ``ERROR_`` prefix, omitted from the mnemonics
in diagrams and the table below. ``NONE`` is the successful status.

.. list-table:: Error and terminal-status codes
   :class: documentation-table
   :header-rows: 1
   :widths: 10 26 64

   * - Code
     - Mnemonic
     - Meaning
   * - 0
     - ``NONE``
     - No error.
   * - 1
     - ``LOCAL_INVALID``
     - Invalid local request, configuration, address, or parameters.
   * - 2
     - ``LOCAL_AXIS``
     - Local stream length, KEEP, TLAST, or framing error.
   * - 3
     - ``LOCAL_OVERFLOW``
     - Local supported size or buffer capacity exceeded.
   * - 4
     - ``LOCAL_AXI_RD_SLVERR``
     - Local AXI read SLVERR or local CPUIF read error.
   * - 5
     - ``LOCAL_AXI_RD_DECERR``
     - Local AXI read returned DECERR.
   * - 6
     - ``LOCAL_AXI_WR_SLVERR``
     - Local AXI write SLVERR or local CPUIF write error.
   * - 7
     - ``LOCAL_AXI_WR_DECERR``
     - Local AXI write returned DECERR.
   * - 8
     - ``TIMEOUT``
     - Local response timeout.
   * - 9
     - ``REMOTE_INVALID``
     - Remote request, configuration, address, or parameter rejection.
   * - 10
     - ``REMOTE_AXIS``
     - Remote stream/framing error or incomplete received frame.
   * - 11
     - ``REMOTE_OVERFLOW``
     - Remote supported size or buffer capacity exceeded.
   * - 12
     - ``REMOTE_AXI_RD_SLVERR``
     - Remote AXI read returned SLVERR.
   * - 13
     - ``REMOTE_AXI_RD_DECERR``
     - Remote AXI read returned DECERR.
   * - 14
     - ``REMOTE_AXI_WR_SLVERR``
     - Remote AXI write returned SLVERR.
   * - 15
     - ``REMOTE_AXI_WR_DECERR``
     - Remote AXI write returned DECERR.

Initiator completions carry final CSR error codes: local causes 1..7, local
TIMEOUT 8, and remote causes 9..15. The oETP engine validates the full 32-bit
ERROR_RSP cause with ``csr_error_from_wire``: wire causes 1..7 map to CSR
codes 9..15; every other wire value maps to ``LOCAL_INVALID``.
The DMA engine preserves the encoding rather than inferring error origin from
the completion channel.

An incomplete received DMA data frame, including missing or incorrect
EndOfData, directly records ``REMOTE_AXIS`` without requiring an
ERROR_RSP first. Responder completions instead supply wire causes 1..7. An
incomplete incoming write returns ``LOCAL_AXIS`` while its receiving peer CSR
records ``REMOTE_AXIS``. Here ``LOCAL_AXIS`` names the responder's wire cause;
it does not change the origin recorded in the receiving peer's CSR.
The wire mapping is specified in :ref:`rtl-oetp-engine` and the
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
   :class: documentation-table
   :header-rows: 1
   :widths: 10 26 64

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
   :class: documentation-table
   :header-rows: 1
   :widths: 28 28 44

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
framing failure uses ``LOCAL_AXIS`` on this interface; DMA records
``REMOTE_AXIS`` while returning wire cause ``LOCAL_AXIS`` in its completion.
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

The examples use ``ADDR_W = LEN_W = SEQUENCE_W = 32``,
``PEER_IDX_W = 2``, and ``ERROR_W = 4``. ``A0`` and ``A1``
denote final executor addresses; ``D0`` and ``D1`` denote scalar
data; ``M0`` denotes a per-bit write mask; ``I0/I1`` and
``S0/S1`` denote local peer indices and fragment sequences. Labels are
local to each diagram. All commands below have ``req_error_code = NONE``
and ``req_last = 1``; completions retain the command's kind, operation,
peer, sequence, and final-block context.

``clk`` is the common clock of the connected logic, shown as a sampling
reference. Numbered cycles label intervals between rising edges; transfers
occur at each interval's ending rising edge when VALID and READY are both
high. Shaded ``x`` regions mark irrelevant values, not a requirement to
drive unknowns. The shown waiting times are illustrative.

Initiator and responder command/completion handshakes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On ``initiator_if``, DMA requests a scalar RMEM write from oETP.
It asserts ``req_valid`` in cycle 1 with ``TRANSFER_KIND_RMEM``,
``DMA_OP_WRITE``, address ``A0``, length 4, mask ``M0``, and write data ``D0``.
The request remains stable until acceptance in cycle 3.
For example, ``M0 = 0x0000000F`` enables only bits 3:0 of the
32-bit word.

The completion becomes valid in cycle 7 and retains ``I0/S0``,
a transferred length of 4, and zero error while ``cpl_ready = 0``.
DMA accepts it in cycle 8. ``req_rx_status = 0``; this scalar
operation completes through the request and completion channels.

.. wavedrom::
    :name: dma-transfer-if-initiator-rmem-timing
    :caption: Initiator RMEM write with request and completion backpressure
    :alt: An RMEM write is accepted in cycle 3 and its retained completion transfers in cycle 8.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p........."},
            ["Requester",
                {"name": "req_valid", "wave": "01..0....."},
                {
                    "name": "req_kind",
                    "wave": "x=..x.....",
                    "style": "font-size: 10px;",
                    "data": ["TRANSFER_KIND_RMEM"]
                },
                {"name": "req_op", "wave": "x=..x.....", "data": ["DMA_OP_WRITE"]},
                {"name": "req_addr", "wave": "x=..x.....", "data": ["A0"]},
                {"name": "req_len", "wave": "x=..x.....", "data": ["4"]},
                {"name": "req_biten", "wave": "x=..x.....", "data": ["M0"]},
                {"name": "req_wdata", "wave": "x=..x.....", "data": ["D0"]},
                {"name": "req_peer_idx", "wave": "x=..x.....", "data": ["I0"]},
                {"name": "req_sequence", "wave": "x=..x.....", "data": ["S0"]},
                {"name": "cpl_ready", "wave": "0.......1."}
            ],
            ["Executor",
                {"name": "req_ready", "wave": "0..10....."},
                {"name": "cpl_valid", "wave": "0......1.0"},
                {"name": "cpl_transferred_len", "wave": "x......=.x", "data": ["4"]},
                {"name": "cpl_peer_idx", "wave": "x......=.x", "data": ["I0"]},
                {"name": "cpl_sequence", "wave": "x......=.x", "data": ["S0"]},
                {"name": "cpl_error", "wave": "x......0.x"},
                {"name": "cpl_error_code", "wave": "x......=.x", "data": ["NONE"]}
            ]
        ],
        "head": {"tick": 0},
        "config": {"hscale": 1}
    }

On ``responder_if``, oETP requests a scalar RMEM read from DMA.
The request presents ``TRANSFER_KIND_RMEM``, ``DMA_OP_READ``, address ``A1``, length 4,
and context ``I1/S1`` in cycle 1; DMA accepts it in cycle 2.
DMA returns ``cpl_rdata = D1`` with a transferred length of 4 and
zero error in cycle 5. The entire completion remains stable until oETP
accepts it in cycle 6. ``req_biten`` and ``req_wdata`` are unused
for this read, and ``req_rx_status = 0``.

.. wavedrom::
    :name: dma-transfer-if-responder-rmem-timing
    :caption: Responder RMEM read returning scalar data in the completion
    :alt: An RMEM read is accepted in cycle 2 and returns D1 until completion acceptance in cycle 6.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p......."},
            ["Requester",
                {"name": "req_valid", "wave": "01.0...."},
                {
                    "name": "req_kind",
                    "wave": "x=.x....",
                    "style": "font-size: 12px;",
                    "data": ["TRANSFER_\nKIND_RMEM"]
                },
                {
                    "name": "req_op",
                    "wave": "x=.x....",
                    "style": "font-size: 10px;",
                    "data": ["DMA_OP_READ"]
                },
                {"name": "req_addr", "wave": "x=.x....", "data": ["A1"]},
                {"name": "req_len", "wave": "x=.x....", "data": ["4"]},
                {"name": "req_peer_idx", "wave": "x=.x....", "data": ["I1"]},
                {"name": "req_sequence", "wave": "x=.x....", "data": ["S1"]},
                {"name": "cpl_ready", "wave": "0.....1."}
            ],
            ["Executor",
                {"name": "req_ready", "wave": "0.10...."},
                {"name": "cpl_valid", "wave": "0....1.0"},
                {"name": "cpl_transferred_len", "wave": "x....=.x", "data": ["4"]},
                {"name": "cpl_peer_idx", "wave": "x....=.x", "data": ["I1"]},
                {"name": "cpl_sequence", "wave": "x....=.x", "data": ["S1"]},
                {"name": "cpl_error", "wave": "x....0.x"},
                {"name": "cpl_error_code", "wave": "x....=.x", "data": ["NONE"]},
                {"name": "cpl_rdata", "wave": "x....=.x", "data": ["D1"]}
            ]
        ],
        "head": {"tick": 0},
        "config": {"hscale": 1}
    }

Exclusive receive descriptor claims
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An armed, unclaimed raw receive descriptor is available at the beginning
of the diagram. On ``responder_if``, the requester asserts
``non_oetp_rx_claim_valid`` in cycle 2. With claim READY also high,
that cycle's ending rising edge transfers exclusive ownership.

Both ``non_oetp_rx_available`` and claim READY return low in cycle 3.
No new descriptor can be claimed while that ownership is outstanding.
After the first receive completes and software arms the next descriptor,
availability and claim READY rise in cycle 8. A second claim transfers in
cycle 9, and both controller outputs return low in cycle 10.
Availability reports one armed, unclaimed descriptor.

.. wavedrom::
    :name: dma-transfer-if-rx-claim-timing
    :caption: Exclusive ownership claimed once for each armed receive descriptor
    :alt: Descriptor claims transfer in cycles 2 and 9, with rearming before the second claim.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p..........."},
            ["Requester", {"name": "non_oetp_rx_claim_valid", "wave": "0.10.....10."}, {}, {}],
            ["Executor",
                {"name": "non_oetp_rx_available", "wave": "1..0....1.0."},
                {"name": "non_oetp_rx_claim_ready", "wave": "1..0....1.0."},
                {}
            ]
        ],
        "head": {"tick": 0},
        "config": {"hscale": 1}
    }

Terminal status and failed completions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An initiating bulk write uses ``TRANSFER_KIND_DMA``, ``DMA_OP_WRITE``, a requested length
of 12, context ``I0/S0``, and ``req_rx_status = 0``.
The command is accepted in cycle 2.

A local source-read failure is reported with ``tx_status_len = 8``
and ``tx_status_error_code = LOCAL_AXI_RD_SLVERR``. DMA presents this status with
matching ``I0/S0`` in cycle 6 and retains all fields until oETP
accepts it in cycle 7.

The subsequent initiator completion preserves ``LOCAL_AXI_RD_SLVERR``, asserts
``cpl_error``, and reports ``cpl_transferred_len = 0`` because the
write failed. Its local source-read count of 8 does not establish successful
remote delivery. The completion remains valid and stable from cycle 10
through acceptance in cycle 12.

.. wavedrom::
    :name: dma-transfer-if-tx-status-timing
    :caption: Source-read terminal error followed by a failed initiator completion
    :alt: TX status reports eight source bytes and LOCAL_AXI_RD_SLVERR before a failed completion.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p............."},
            ["Requester",
                {"name": "req_valid", "wave": "01.0.........."},
                {"name": "req_len", "wave": "x=.x..........", "data": ["12"]},
                {"name": "req_peer_idx", "wave": "x=.x..........", "data": ["I0"]},
                {"name": "req_sequence", "wave": "x=.x..........", "data": ["S0"]},
                {"name": "req_rx_status", "wave": "x0.x.........."},
                {"name": "tx_status_valid", "wave": "0.....1.0....."},
                {"name": "tx_status_peer_idx", "wave": "x.....=.x.....", "data": ["I0"]},
                {"name": "tx_status_sequence", "wave": "x.....=.x.....", "data": ["S0"]},
                {"name": "tx_status_len", "wave": "x.....=.x.....", "data": ["8"]},
                {
                    "name": "tx_status_error_code",
                    "wave": "x.....=.x.....",
                    "data": ["LOCAL_\nAXI_RD_\nSLVERR"]
                },
                {"name": "cpl_ready", "wave": "0...........1."}
            ],
            ["Executor",
                {"name": "req_ready", "wave": "0.10.........."},
                {"name": "tx_status_ready", "wave": "0......10....."},
                {"name": "cpl_valid", "wave": "0.........1..0"},
                {"name": "cpl_transferred_len", "wave": "x.........=..x", "data": ["0"]},
                {"name": "cpl_peer_idx", "wave": "x.........=..x", "data": ["I0"]},
                {"name": "cpl_sequence", "wave": "x.........=..x", "data": ["S0"]},
                {"name": "cpl_error", "wave": "x.........1..x"},
                {
                    "name": "cpl_error_code",
                    "wave": "x.........=..x",
                    "data": ["LOCAL_AXI_\nRD_SLVERR"]
                }
            ]
        ],
        "head": {"tick": 0},
        "config": {"hscale": 1}
    }

For an incoming bulk write, ``responder_if`` instead carries
``req_rx_status = 1``, with ``TRANSFER_KIND_DMA``, ``DMA_OP_WRITE``, a requested length
of 12, and context ``I0/S0``. The command is accepted in cycle 2.

The requester presents ``rx_status_len = 8`` and ``LOCAL_AXIS`` for an
incomplete received transfer in cycle 6. The status retains matching peer
and sequence fields until acceptance in cycle 7. Assume memory servicing
has also finished and reports eight transferred bytes with no AXI error.
The executor waits for both the memory outcome and the required receive
status before completing the operation.

The completion becomes valid in cycle 10 with
``cpl_transferred_len = 8``, ``cpl_error = 1``, and ``LOCAL_AXIS``,
and is accepted in cycle 12. This responder-path code is the wire stream
cause; DMA records ``REMOTE_AXIS`` in the receiving peer's CSR.
A local AXI error, if present, would take priority over the derived
framing error.

.. wavedrom::
    :name: dma-transfer-if-rx-status-timing
    :caption: Receive terminal status joined with the failed responder completion
    :alt: RX status reports eight bytes and LOCAL_AXIS before the retained responder completion.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p............."},
            ["Requester",
                {"name": "req_valid", "wave": "01.0.........."},
                {"name": "req_len", "wave": "x=.x..........", "data": ["12"]},
                {"name": "req_peer_idx", "wave": "x=.x..........", "data": ["I0"]},
                {"name": "req_sequence", "wave": "x=.x..........", "data": ["S0"]},
                {"name": "req_rx_status", "wave": "x1.x.........."},
                {"name": "rx_status_valid", "wave": "0.....1.0....."},
                {"name": "rx_status_peer_idx", "wave": "x.....=.x.....", "data": ["I0"]},
                {"name": "rx_status_sequence", "wave": "x.....=.x.....", "data": ["S0"]},
                {"name": "rx_status_len", "wave": "x.....=.x.....", "data": ["8"]},
                {
                    "name": "rx_status_error_code",
                    "wave": "x.....=.x.....",
                    "style": "font-size: 12px;",
                    "data": ["LOCAL_AXIS"]
                },
                {"name": "cpl_ready", "wave": "0...........1."}
            ],
            ["Executor",
                {"name": "req_ready", "wave": "0.10.........."},
                {"name": "rx_status_ready", "wave": "0......10....."},
                {"name": "cpl_valid", "wave": "0.........1..0"},
                {"name": "cpl_transferred_len", "wave": "x.........=..x", "data": ["8"]},
                {"name": "cpl_peer_idx", "wave": "x.........=..x", "data": ["I0"]},
                {"name": "cpl_sequence", "wave": "x.........=..x", "data": ["S0"]},
                {"name": "cpl_error", "wave": "x.........1..x"},
                {"name": "cpl_error_code", "wave": "x.........=..x", "data": ["LOCAL_AXIS"]}
            ]
        ],
        "head": {"tick": 0},
        "config": {"hscale": 1}
    }
