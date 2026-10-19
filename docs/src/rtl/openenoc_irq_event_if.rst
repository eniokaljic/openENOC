.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-irq-event-if:

IRQ event producer -- openenoc_irq_event_if
===========================================

.. index::
   single: openenoc_irq_event_if

Defines interrupt-event admission and later commitment by a hardware producer.

**Source:** :download:`openenoc_irq_event_if.sv <../../../hw/rtl/core/openenoc_irq_event_if.sv>`.

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
   * - ``PEER_IDX_W``
     - ``1``
     - Integer >= 1; enough bits for the peer count
     - Width of local peer indices; all connected interfaces must agree.

The current :ref:`rtl-endpoint-irq-controller` implementation accepts
``PEER_IDX_W`` from 1 to 11 so indices fit the generated CSR claim field.

Signals
-------

Directions are relative to the ``producer`` and ``controller`` modports.
The ``mon`` modport observes all signals as inputs.

.. list-table:: Public signals and interfaces
   :class: rtl-reference-table
   :header-rows: 1
   :widths: 22 28 16 34

   * - Name
     - Type
     - Direction / role
     - Description
   * - ``admit_valid``
     - ``logic``
     - producer: output; controller: input
     - Producer requests admission before the event operation starts.
   * - ``admit_ready``
     - ``logic``
     - producer: input; controller: output
     - Accepts the admission when admit_valid is also asserted.
   * - ``admit_source``
     - ``logic [3:0]``
     - producer: output; controller: input
     - Event class code to evaluate against source enables.
   * - ``admit_enable``
     - ``logic``
     - producer: output; controller: input
     - Producer enable decision, including any previously sampled source enable.
   * - ``admit_reserved``
     - ``logic``
     - producer: input; controller: output
     - Reservation result sampled with admit_valid and admit_ready; one reserves a FIFO credit.
   * - ``commit_valid``
     - ``logic``
     - producer: output; controller: input
     - Producer offers a completed admitted event.
   * - ``commit_ready``
     - ``logic``
     - producer: input; controller: output
     - Accepts the completed event when commit_valid is also asserted.
   * - ``commit_source``
     - ``logic [3:0]``
     - producer: output; controller: input
     - Committed event class code.
   * - ``commit_peer_idx``
     - ``logic [PEER_IDX_W-1:0]``
     - producer: output; controller: input
     - Peer index for peer-DMA and RMEM-error events; ignored for other sources.

Architecture and operation
--------------------------

**Parameter and roles:** ``PEER_IDX_W`` defaults to 1. Modports are
``producer``, ``controller``, and ``mon``. Clock and reset belong to the
connected modules.

Admission and commit use independent ready/valid handshakes. Admission
transfers on a rising edge with ``admit_valid && admit_ready``; commit
transfers on a rising edge with ``commit_valid && commit_ready``. The
producer asserts each VALID when the corresponding transfer is available,
without waiting for READY, and retains it until acceptance. It keeps
``admit_source`` and ``admit_enable`` stable while admission is pending,
and ``commit_source`` and ``commit_peer_idx`` stable while commit is pending.

The admission channel is used before an operation starts, or when a received
request/RMEM failure is recorded. The controller evaluates ``admit_source``
against the configured source enable and the producer's ``admit_enable``.
For producers that have already sampled the source enable, that captured
decision is included in ``admit_enable``. The controller samples the enable
decision and reserves capacity when it prepares its registered admission
offer. Later enable changes do not revise that offer.

The producer samples ``admit_reserved`` with the admission handshake and
retains the result with its operation context. A value of 1 reserves FIFO
capacity for exactly one later commit on the same producer port. A value of
0 accepts the admission without an IRQ reservation, so that operation must
not submit a commit. The operation itself may still proceed. The reservation
result is meaningful with the admission handshake; it need not remain
asserted while the operation runs.

When a reserved operation completes, the producer submits its event class
and peer index. The accepted commit converts the saved reservation into a
queued event. Changes to event enables after admission do not cancel that
commit. The current controller retains ``commit_peer_idx`` for
``EVENT_PEER_DMA_COMPLETE`` and ``EVENT_RMEM_ERROR``; it records zero for
the remaining source classes.

These are local IRQ FIFO reservations, independent of the oETP wire protocol.
The interface contains no clock/reset ports or internal storage.

.. list-table:: Event source encodings
   :class: documentation-table
   :header-rows: 1
   :widths: 10 40 50

   * - Code
     - Interface constant
     - Meaning
   * - 0
     - ``EVENT_PEER_DMA_COMPLETE``
     - Peer bulk-DMA completion or servicing failure.
   * - 1
     - ``EVENT_NON_OETP_DMA_TX_COMPLETE``
     - Raw DMA transmit completion.
   * - 2
     - ``EVENT_NON_OETP_DMA_RX_COMPLETE``
     - Raw DMA receive completion.
   * - 3
     - ``EVENT_NON_OETP_DIRECT_TX_COMPLETE``
     - Direct CSR frame transmit completion.
   * - 4
     - ``EVENT_NON_OETP_DIRECT_RX_AVAILABLE``
     - Direct CSR frame available for reception.
   * - 5
     - ``EVENT_RMEM_ERROR``
     - Scalar RMEM failure.

The controller behavior is described in :ref:`rtl-endpoint-irq-controller`.

Functional scenarios
--------------------

The examples use ``PEER_IDX_W = 2`` and event source
``EVENT_PEER_DMA_COMPLETE``; ``I0`` and ``I1`` denote
peer indices. Labels are local to each diagram.

``clk`` is the common clock of the connected logic, shown as a sampling
reference. Numbered cycles label intervals between rising edges; transfers
occur at each interval's ending rising edge when VALID and READY are both
high. Shaded ``x`` regions mark irrelevant values, not a requirement to
drive unknowns. Waiting times depend on the connected logic and are not
interface latency guarantees.

Enabled admission and reserved capacity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The producer presents ``admit_source = EVENT_PEER_DMA_COMPLETE`` and ``admit_enable = 1``
with ``admit_valid = 1`` in cycle 1. The source is enabled in the
controller configuration, and capacity is available. In cycle 2, the
controller asserts ``admit_ready`` with ``admit_reserved = 1``.
The producer samples the reservation at the ending rising edge and
deasserts ``admit_valid`` in cycle 3.

The producer retains the reservation while the operation runs. In cycle 5,
it presents the completed event with ``commit_source = EVENT_PEER_DMA_COMPLETE``,
``commit_peer_idx = I0``, and ``commit_valid = 1``. These fields
remain stable until the commit transfers in cycle 6 with
``commit_ready = 1``. The producer deasserts ``commit_valid`` in
cycle 7. This consumes the earlier reservation exactly once.

.. wavedrom::
    :name: irq-event-if-enabled-timing
    :caption: Enabled event admission followed by a reserved commit
    :alt: Admission reserves capacity in cycle 2 and the completed event commits in cycle 6.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p......."},
            ["Producer",
                {"name": "admit_valid", "wave": "01.0...."},
                {
                    "name": "admit_source",
                    "wave": "x=.x....",
                    "style": "font-size: 12px;",
                    "data": ["EVENT_\nPEER_DMA_\nCOMPLETE"]
                },
                {"name": "admit_enable", "wave": "x1.x...."},
                {"name": "commit_valid", "wave": "0....1.0"},
                {
                    "name": "commit_source",
                    "wave": "x....=.x",
                    "style": "font-size: 12px;",
                    "data": ["EVENT_\nPEER_DMA_\nCOMPLETE"]
                },
                {"name": "commit_peer_idx", "wave": "x....=.x", "data": ["I0"]}
            ],
            ["Controller",
                {"name": "admit_ready", "wave": "0.10...."},
                {"name": "admit_reserved", "wave": "0.10...."},
                {"name": "commit_ready", "wave": "0.....10"}
            ]
        ],
        "head": {"tick": 0},
        "config": {"hscale": 1}
    }

Disabled admission without a later commit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Two admissions illustrate disabled event production. For the first, the
source is enabled in the controller, but the producer supplies
``admit_enable = 0`` with ``EVENT_PEER_DMA_COMPLETE`` in cycle 1. The admission
transfers in cycle 2 with ``admit_reserved = 0``.

Before the second admission, the controller's source-enable setting for
``EVENT_PEER_DMA_COMPLETE`` is cleared. The producer supplies ``admit_enable = 1`` in
cycle 5, but the admission still transfers without a reservation in cycle 6.

Both operations may proceed after admission. Neither has reserved an IRQ
event, so neither sends a later commit. ``commit_valid`` remains low
when the operations finish, even if the source is subsequently enabled.
Disabled admissions do not require free IRQ FIFO capacity.

.. wavedrom::
    :name: irq-event-if-disabled-timing
    :caption: Disabled admissions accepted without a commit reservation
    :alt: Both disabled admissions complete without a reservation or later commit.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p........"},
            ["Producer",
                {"name": "admit_valid", "wave": "01.0.1.0."},
                {
                    "name": "admit_source",
                    "wave": "x=.x.=.x.",
                    "style": "font-size: 12px;",
                    "data": ["EVENT_\nPEER_DMA_\nCOMPLETE", "EVENT_\nPEER_DMA_\nCOMPLETE"]
                },
                {"name": "admit_enable", "wave": "x0.x.1.x."},
                {"name": "commit_valid", "wave": "0........"},
                {"name": "commit_source", "wave": "x........"},
                {"name": "commit_peer_idx", "wave": "x........"}
            ],
            ["Controller",
                {"name": "admit_ready", "wave": "0.10..10."},
                {"name": "admit_reserved", "wave": "0........"},
                {"name": "commit_ready", "wave": "0........"}
            ]
        ],
        "head": {"tick": 0},
        "config": {"hscale": 1}
    }

Delayed commitment, backpressure, and peer metadata
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The producer requests admission for ``EVENT_PEER_DMA_COMPLETE`` in cycle 1, while capacity
is unavailable. It keeps ``admit_valid``, ``admit_source``, and
``admit_enable`` unchanged through cycle 4. The controller then offers
capacity with ``admit_ready = 1`` and ``admit_reserved = 1``;
the admission transfers at that cycle's ending rising edge.

The reservation remains associated with the operation after
``admit_reserved`` returns low in cycle 5. A source-enable change in
cycle 6 does not alter the accepted reservation. The operation completes
later, and the producer asserts ``commit_valid`` in cycle 8 with
``commit_source = EVENT_PEER_DMA_COMPLETE`` and ``commit_peer_idx = I1``.

With ``commit_ready = 0`` in cycles 8 and 9, the producer retains
VALID and both metadata fields. The commit transfers in cycle 10 when
``commit_ready = 1``, and the producer deasserts VALID in cycle 11.
The committed peer index identifies the completed operation, even though
no peer index was transferred on the earlier admission channel.

.. wavedrom::
    :name: irq-event-if-backpressure-timing
    :caption: Delayed reserved commit with stable peer metadata under backpressure
    :alt: Admission waits until cycle 4; commit metadata stays stable until cycle 10.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p..........."},
            ["Producer",
                {"name": "admit_valid", "wave": "01...0......"},
                {
                    "name": "admit_source",
                    "wave": "x=...x......",
                    "style": "font-size: 10px;",
                    "data": ["EVENT_PEER_DMA_COMPLETE"]
                },
                {"name": "admit_enable", "wave": "x1...x......"},
                {"name": "commit_valid", "wave": "0.......1..0"},
                {
                    "name": "commit_source",
                    "wave": "x.......=..x",
                    "style": "font-size: 12px;",
                    "data": ["EVENT_PEER_\nDMA_COMPLETE"]
                },
                {"name": "commit_peer_idx", "wave": "x.......=..x", "data": ["I1"]}
            ],
            ["Controller",
                {"name": "admit_ready", "wave": "0...10......"},
                {"name": "admit_reserved", "wave": "0...10......"},
                {"name": "commit_ready", "wave": "0.........10"}
            ]
        ],
        "head": {"tick": 0},
        "config": {"hscale": 1}
    }
