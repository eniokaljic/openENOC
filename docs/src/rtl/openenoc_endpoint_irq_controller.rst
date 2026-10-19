.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-endpoint-irq-controller:

IRQ controller -- openenoc_endpoint_irq_controller
==================================================

.. index::
   single: openenoc_endpoint_irq_controller

Collects admitted hardware events into ordered interrupt claims for software
completion.

**Source:** :download:`openenoc_endpoint_irq_controller.sv <../../../hw/rtl/core/openenoc_endpoint_irq_controller.sv>`.

Parameters
----------

.. list-table:: Parameters
   :class: rtl-reference-table
   :header-rows: 1
   :widths: 26 18 28 28

   * - Name
     - Default value
     - Allowed values
     - Description
   * - ``EVENT_PORTS``
     - ``6``
     - Integer >= 1
     - Number of independent interrupt-event producer ports.
   * - ``FIFO_DEPTH``
     - ``16``
     - Integer >= 1
     - Shared capacity for queued claims and producer reservations.
   * - ``PEER_IDX_W``
     - ``1``
     - 1..11
     - Event peer-index width, bounded by the generated CSR claim field.
   * - ``SEQUENCE_W``
     - ``16``
     - 1..16
     - Interrupt claim sequence width, bounded by the generated CSR token field.
   * - ``SAMPLED_ENABLE_MASK``
     - ``'0``
     - EVENT_PORTS-bit mask
     - A set bit means the producer has already sampled the source-enable decision.

Signals
-------

Interface ports contain channels in both directions. The table identifies
the selected modport or stream role; member directions follow that interface.

.. list-table:: Public signals and interfaces
   :class: rtl-reference-table
   :header-rows: 1
   :widths: 26 30 17 27

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
     - IRQ enables, claim and completion fields, status, and error-clear commands.
   * - ``irq``
     - ``logic``
     - output
     - Level interrupt notification to software.
   * - ``event_if[EVENT_PORTS]``
     - | ``openenoc_irq_event_if.``
       | ``controller``
     - bidirectional (controller)
     - Producer admission and commit channels.

Architecture and operation
--------------------------

**Boundary and parameters:** ``event_if[EVENT_PORTS]`` accepts producers of
:ref:`rtl-irq-event-if`; ``endpoint_if`` exposes enable, claim, completion,
and error controls; ``irq`` notifies software. Defaults are
``EVENT_PORTS = 6``, ``FIFO_DEPTH = 16``, ``PEER_IDX_W = 1``,
``SEQUENCE_W = 16``, and ``SAMPLED_ENABLE_MASK = 0``.
Peer and sequence widths must fit their generated CSR fields.

Endpoint integration uses seven producer ports and marks port 5 (initiating
RMEM error) as having already sampled its source enable. For that port,
``admit_enable`` includes the captured enable decision, and the controller
does not re-read the live source CSR. For unmarked ports, the controller
combines ``admit_enable`` with the source-enable CSR when preparing the
registered admission offer. Later enable changes do not revise that offer
or cancel accepted reservations.

Admission and commit use independent round-robin SELECT/OFFER machines.
Selection prepares a registered READY offer; the next edge accepts the
producer's stable VALID and metadata. Each channel accepts at most one
enabled operation every two cycles. Disabled admissions can be offered to
multiple ports in parallel. Admission reserves credit for a particular
producer port; another port cannot consume that reservation, even if both
ports report the same event source.

The FIFO capacity is shared by queued claims and reservations. An enabled
admission reserves capacity when its READY offer is prepared, before the
handshake completes. Withdrawing VALID during that offer releases the
provisional reservation. A commit converts one of its port's reservations
into a queued claim without changing the total occupied capacity. A full
credit pool blocks new enabled admissions but permits commits backed by
existing reservations. A matching completion releases a queued credit, which
can fund a new registered admission offer on the same edge.

Claims are ordered by accepted commits, which may differ from admission
order. Each accepted commit receives the next sequence number, starting at
zero after reset and wrapping modulo ``2**SEQUENCE_W``. These sequence
tokens are independent of oETP Request IDs. The current head remains stable
until software completes it. A matching completion and an already offered
commit can replace the head on the same edge without dropping claim validity.

Software completes a claim by copying its valid, sequence, source, and peer
fields to ``irq.complete``. All token fields must match the head, including
zero extension into unused upper CSR bits when parameter widths are smaller.
The controller acknowledges a completion command through
``complete.valid.hwclr`` whether the token matches or not. A mismatch, or a
command with no claim pending, leaves the queue unchanged and sets sticky
``status.invalid_complete``. A commit without a reservation on its producer
port, or without queue space, sets ``status.overflow`` and creates no claim.

``control.clear_errors`` clears these two controller diagnostics; a new
error on the same edge takes precedence. Completion and clear commands are
each applied once while their command bit remains asserted. Their registered
``hwclr`` outputs stay high until the respective input bit is sampled low.
Clearing controller or DMA errors is separate from completing a claim.

The global enable masks only the physical level IRQ. Event capture, credit
accounting, and claim visibility continue while it is low. The registered
``irq`` and ``status.irq_asserted`` reflect the sampled global enable and
whether claims remain after the edge's queue updates.
``status.claim_pending`` follows claim validity independently of this mask.
``status.fifo_level`` counts queued claims; ``status.reserved_count``
counts reservations, including provisional READY offers. Both CSR counters
saturate at 255. ``status.credit_full`` uses the exact internal counts,
so saturation does not affect capacity control. Reset clears claims,
reservations, sequence state, handshakes, IRQ, and controller diagnostics.

Functional scenarios
--------------------

The admission/commit contract is illustrated in :ref:`rtl-irq-event-if`,
and firmware IRQ service is illustrated in :ref:`rtl-endpoint-full`.
The examples here focus on controller credit accounting and claim retirement.
They use ``EVENT_PORTS = 1``, ``PEER_IDX_W = 2``, and
``SEQUENCE_W = 16``; each states its FIFO depth.

``S0`` denotes ``EVENT_PEER_DMA_COMPLETE`` (source 0), enabled throughout.
The producer uses ``admit_enable = 1`` and ``admit_source = S0``;
all commits use ``commit_source = S0``. ``I0`` and ``I1`` denote
distinct peer indices. ``D0`` and ``D1`` are complete claim words with
sequence numbers 0 and 1, respectively, source ``S0``, and peer indices
``I0`` and ``I1``.

Numbered cycles label intervals between rising edges. Admission and commit
transfer at an interval's ending rising edge when VALID and READY are high.
CSR command bits are sampled at the same edge. CSR field paths are
relative to ``endpoint_if.csr_to_core`` for CSR inputs and
``endpoint_if.core_to_csr`` for Core outputs;
generated ``.value`` and ``.next`` wrappers are omitted. The diagrams
show the controller boundary, so they do not include CSR bus transaction
latency. ``claim`` and ``complete`` denote packed words while valid;
``x`` marks irrelevant values.

IRQ masking, shared credit, and completion-edge reuse
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use ``FIFO_DEPTH = 1``, initially empty after reset. The physical IRQ is
masked by ``control.global_enable = 0``. Preparing the first admission
offer reserves the only credit: ``status.reserved_count = 1`` and
``status.credit_full = 1`` are already visible in cycle 2, when the
admission handshake occurs.

The first commit transfers in cycle 4. In cycle 5, the reservation has
become queued claim ``D0``: ``status.reserved_count`` falls to zero,
``status.fifo_level`` rises to one, and ``status.credit_full`` remains
asserted. The claim is visible even though ``irq = 0``. A second enabled
admission waits from cycle 5 because no credit is free.

Software raises the global enable in cycle 7, so ``irq`` rises in
cycle 8. The matching completion ``D0`` is sampled at the end of
cycle 8. That edge removes the claim and prepares the waiting admission
offer. In cycle 9, the FIFO is empty, a new reservation occupies its
capacity, and ``status.credit_full`` is still asserted. The second
admission transfers in that cycle.

Its commit transfers in cycle 11 and becomes claim ``D1`` in cycle 12.
Because the global enable remains high, this new claim also raises
``irq``. Masking the IRQ never released either operation's credit.

.. wavedrom::
    :name: endpoint-irq-controller-credit-mask-timing
    :caption: IRQ masking and reuse of shared FIFO credit
    :alt: A one-entry IRQ FIFO accounts for reservations and claims while masking its physical IRQ.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p............."},
            ["FSM",
                {
                    "name": "admission_state_reg",
                    "wave": "=.==.....==...",
                    "data": ["SELECT", "OFFER", "SELECT", "OFFER", "SELECT"],
                    "style": "font-size: 12px;"
                },
                {
                    "name": "commit_state_reg",
                    "wave": "=...==.....==.",
                    "data": ["SELECT", "OFFER", "SELECT", "OFFER", "SELECT"],
                    "style": "font-size: 12px;"
                }
            ],
            {"name": "irq", "wave": "0.......10..1."},
            ["event_if[0]",
                ["Producer",
                    {"name": "admit_valid", "wave": "01.0.1....0..."},
                    {"name": "commit_valid", "wave": "0..1.0....1.0."},
                    {"name": "commit_peer_idx", "wave": "x..=.x....=.x.", "data": ["I0", "I1"]}
                ],
                ["Controller",
                    {"name": "admit_ready", "wave": "0.10.....10..."},
                    {"name": "admit_reserved", "wave": "0.10.....10..."},
                    {"name": "commit_ready", "wave": "0...10.....10."}
                ]
            ],
            {},
            ["endpoint_if",
                ["CSR",
                    {"name": "irq.control.global_enable", "wave": "0......1......"},
                    {"name": "irq.complete.valid", "wave": "0.......1.0..."},
                    {"name": "irq.complete", "wave": "x.......=.x...", "data": ["D0"]}
                ],
                ["Core",
                    {"name": "irq.claim.valid", "wave": "0....1...0..1."},
                    {"name": "irq.claim", "wave": "x....=...x..=.", "data": ["D0", "D1"]},
                    {"name": "irq.complete.valid.hwclr", "wave": "0........1.0.."},
                    {
                        "name": "irq.status.fifo_level",
                        "wave": "=....=...=..=.",
                        "data": ["0", "1", "0", "1"]
                    },
                    {
                        "name": "irq.status.reserved_count",
                        "wave": "=.=..=...=..=.",
                        "data": ["0", "1", "0", "1", "0"]
                    },
                    {"name": "irq.status.credit_full", "wave": "0.1..........."}
                ]
            ]
        ],
        "head": {
            "tick": 0
        },
        "config": {
            "hscale": 1
        }
    }

Exact completion tokens and simultaneous head replacement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use ``FIFO_DEPTH = 2`` and ``control.global_enable = 1``. Initially,
claim ``D0`` occupies one entry, and the same producer already holds
a reservation for its second operation. No new admission is needed in the
shown interval. ``D2`` copies ``D0`` except for an incorrect sequence
number.

Software asserts ``complete.valid`` with ``D2`` in cycle 1 and holds
it through cycle 3. The controller acknowledges the command in cycle 2
and sets ``status.invalid_complete``, while ``D0``, FIFO occupancy,
and ``irq`` remain unchanged. The acknowledgement therefore confirms
command processing, not successful claim retirement.

In cycle 5, software presents the correct ``D0`` token and requests
error clearing. On the same edge, the producer commits its second
operation with peer ``I1``. Claim ``D1`` replaces ``D0`` in
cycle 6: ``claim.valid`` and ``irq`` remain high, FIFO occupancy stays
at one, and the remaining reservation is consumed.

The old completion ``D0`` stays asserted through cycle 7, but it is
applied only once. It does not remove ``D1`` or reassert
``status.invalid_complete`` after the clear. Software releases the
command, then submits ``D1`` in cycle 9. The queue becomes empty and
``irq`` falls in cycle 10.

.. wavedrom::
    :name: endpoint-irq-controller-completion-replacement-timing
    :caption: Exact completion matching and claim replacement without an IRQ gap
    :alt: An invalid token preserves the head; a valid completion and commit replace it together.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p............"},
            ["FSM",
                {"name": "admission_state_reg", "wave": "=............", "data": ["SELECT"]},
                {
                    "name": "commit_state_reg",
                    "wave": "=....==......",
                    "data": ["SELECT", "OFFER", "SELECT"],
                    "style": "font-size: 12px;"
                }
            ],
            {"name": "irq", "wave": "1.........0.."},
            ["event_if[0]",
                ["Producer",
                    {"name": "admit_valid", "wave": "0............"},
                    {"name": "commit_valid", "wave": "0...1.0......"},
                    {"name": "commit_peer_idx", "wave": "x...=.x......", "data": ["I1"]}
                ],
                ["Controller",
                    {"name": "admit_ready", "wave": "0............"},
                    {"name": "admit_reserved", "wave": "0............"},
                    {"name": "commit_ready", "wave": "0....10......"}
                ]
            ],
            {},
            ["endpoint_if",
                ["CSR",
                    {"name": "irq.complete.valid", "wave": "01..01..01.0."},
                    {"name": "irq.complete", "wave": "x=..x=..x=.x.", "data": ["D2", "D0", "D1"]},
                    {"name": "irq.control.clear_errors", "wave": "0....1..0...."}
                ],
                ["Core",
                    {"name": "irq.claim.valid", "wave": "1.........0.."},
                    {"name": "irq.claim", "wave": "=.....=...x..", "data": ["D0", "D1"]},
                    {"name": "irq.complete.valid.hwclr", "wave": "0.1..01..01.0"},
                    {"name": "irq.control.clear_errors.hwclr", "wave": "0.....1..0..."},
                    {"name": "irq.status.fifo_level", "wave": "=.........=..", "data": ["1", "0"]},
                    {
                        "name": "irq.status.reserved_count",
                        "wave": "=.....=......",
                        "data": ["1", "0"]
                    },
                    {"name": "irq.status.invalid_complete", "wave": "0.1...0......"}
                ]
            ]
        ],
        "head": {
            "tick": 0
        },
        "config": {
            "hscale": 1
        }
    }

.. _verification-openenoc-endpoint-irq-controller:

Verification
------------

The test suite is in ``dv/core/openenoc_endpoint_irq_controller/``.

Testbench
~~~~~~~~~

This cocotb suite verifies the IRQ controller in isolation from the processor, CSR register
block, and event producers. The wrapper flattens CSR fields and event interfaces for cocotb.
Eight cases run in eight configurations covering 1–7 producer ports, FIFO depths 1, 3, 4, 7, 8,
16, and 260, peer widths up to 11 bits, and sequence widths up to 16 bits.

The tests check independent producer arbitration and credits, FIFO pressure, exact completion
tokens, simultaneous completion and commit, held CSR commands, IRQ masking, sequence wrap,
status saturation, and output stability between clock edges.

Coverage
~~~~~~~~

The suite covers:

- reset of claims, reservations, sequence state, and sticky diagnostics;

- locally disabled admissions and all six source enables, including RMEM_ERROR;

- per-producer reservations, including independent initiator/responder ports sharing source 0;

- independent round-robin admission and commit arbitration;

- FIFO-full backpressure, capacity reuse, and simultaneous claim enqueue/dequeue;

- ordered, stable claims with preserved peer indices and exact completion-token matching;

- invalid tokens, nonzero unused token bits, and commits without reservations;

- global IRQ masking, sequence wraparound, arbitrary FIFO depths, and 8-bit status saturation;

- registered output stability and one application of held CSR completion/clear commands.
