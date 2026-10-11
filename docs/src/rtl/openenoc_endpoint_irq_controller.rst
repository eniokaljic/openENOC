.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-endpoint-irq-controller:

IRQ controller -- openenoc_endpoint_irq_controller
==================================================

Collects admitted hardware events into ordered interrupt claims for software
completion.

**Source:** :download:`openenoc_endpoint_irq_controller.sv <../../../hw/rtl/core/openenoc_endpoint_irq_controller.sv>`.

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
   * - ``EVENT_PORTS``
     - ``6``
     - Integer >= 1
     - Number of independent interrupt-event producer ports.
   * - ``FIFO_DEPTH``
     - ``16``
     - Integer >= 1; arbitrary depth
     - Number of queued interrupt claims, with exact internal occupancy.
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
   * - ``irq``
     - ``logic``
     - output
     - Level interrupt notification to software.
   * - ``event_if[EVENT_PORTS]``
     - ``openenoc_irq_event_if.controller``
     - bidirectional (controller)
     - Producer admission and commit channels.

Architecture and operation
--------------------------

**Boundary and parameters:** ``event_if[EVENT_PORTS]`` accepts producers of
:ref:`rtl-irq-event-if`; ``endpoint_if`` exposes enable, claim, completion,
and error controls; ``irq`` notifies software. Defaults are ``EVENT_PORTS = 6``,
``FIFO_DEPTH = 16``, ``PEER_IDX_W = 1``, and ``SEQUENCE_W = 16``, and ``SAMPLED_ENABLE_MASK = 0``. Endpoint
integration overrides the producer count to seven and marks port 5 (initiating
RMEM error) as having already sampled its source enable. Other producers sample
the source enable when preparing their registered admission offer. ``admit_enable`` from a marked producer includes
that captured enable; the controller does not re-read the live source CSR.
The global physical IRQ mask remains independent of event collection.
Peer and sequence widths
must fit their generated CSR fields.

Admission and commit each own a clocked process. A third process owns the
circular claim queue, credit counters, CSR status, and physical IRQ output.
Local arithmetic values combine simultaneous reservation, withdrawal, commit,
and completion events. All outward signals are registered.
Admission and commit use independent round-robin SELECT/OFFER machines:
selection prepares a registered READY offer, and the next edge consumes the
producer's stable VALID and metadata. Each channel can accept one enabled
operation every two cycles. Disabled admissions may be offered in parallel.

An enabled admission reserves FIFO capacity while preparing its offer, so
registered READY cannot overbook the queue. The producer observes
``admit_reserved`` with its handshake. A withdrawn offer releases its provisional
reservation. Disabled operations receive ``admit_reserved = 0``. A later commit
converts one reservation into a queued claim without changing total occupied
capacity. The offer captures the enable decision; subsequent CSR mask changes
cannot revise it.

The queue uses an indexed write and a registered head with forwarding for a
simultaneous write to that head. A matching completion and an already offered
commit can pop and push on the same edge without losing claim validity. Claim
fields remain stable until software completes that head.

A matching software completion removes the claim at the FIFO head. An invalid
completion leaves the FIFO unchanged and records the controller diagnostic.
Completion and error-clear hardware acknowledgements are registered; each held
CSR command is applied once. Global IRQ mask changes take effect on the next
rising edge, independently of admission and queued claims.
IRQ sequence tokens are independent of oETP Request IDs. Reset clears FIFO,
reservations, sequence state, and controller errors. Clearing controller or DMA
errors is separate from completing a claim.

**Verification:** ``dv/core/openenoc_endpoint_irq_controller/`` includes
subcycle output checks, held completion commands, and simultaneous pop/push. Detailed
cycle examples for simultaneous admission, commit, and completion remain to
be added to this reference.

Functional scenarios
--------------------

This section reserves space for scenario descriptions and WaveDrom timing
diagrams. The current outline is:

* Enabled/disabled admission and independent producer reservations.
* Admission and commit arbitration under FIFO pressure.
* Simultaneous enqueue/dequeue and exact completion-token matching.
* Mask changes, held CSR commands, sequence wrap, and status saturation.
