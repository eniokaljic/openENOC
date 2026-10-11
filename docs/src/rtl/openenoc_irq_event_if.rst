.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-irq-event-if:

IRQ event producer -- openenoc_irq_event_if
===========================================

Defines interrupt-event admission and later commitment by a hardware producer.

**Source:** :download:`openenoc_irq_event_if.sv <../../../hw/rtl/core/openenoc_irq_event_if.sv>`.

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
   * - ``PEER_IDX_W``
     - ``1``
     - Integer >= 1; enough bits for the peer count
     - Width of local peer indices; all connected interfaces must agree.

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
   * - ``admit_valid``
     - ``logic``
     - producer: output; controller: input
     - Producer requests admission before the event operation starts.
   * - ``admit_ready``
     - ``logic``
     - producer: input; controller: output
     - Controller accepts the admission.
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
     - Accepted admission holds a FIFO credit; zero means no later commit.
   * - ``commit_valid``
     - ``logic``
     - producer: output; controller: input
     - Producer offers a completed admitted event.
   * - ``commit_ready``
     - ``logic``
     - producer: input; controller: output
     - Controller accepts the completed event.
   * - ``commit_source``
     - ``logic [3:0]``
     - producer: output; controller: input
     - Committed event class code.
   * - ``commit_peer_idx``
     - ``logic [PEER_IDX_W-1:0]``
     - producer: output; controller: input
     - Committed local peer index; ignored for non-peer event classes.

Architecture and operation
--------------------------

**Parameter and roles:** ``PEER_IDX_W`` defaults to 1. Modports are
``producer``, ``controller``, and ``mon``. Clock and reset belong to the
connected modules.

The admission channel is used when an operation is accepted or a received
request/RMEM failure is recorded. The controller combines ``admit_source``
with the configured event enable and producer ``admit_enable``. A disabled
event is accepted without reserving FIFO capacity. ``admit_reserved`` reports
the reservation result during the ``admit_valid && admit_ready`` handshake.
The registered controller evaluates enable and reserves capacity when it
prepares that offer. Hold admission metadata stable while VALID is pending;
mask changes after the offer do not change its reservation result.

The producer retains that result with its operation context. Every reserved
operation eventually submits exactly one commit. ``commit_source`` and
``commit_peer_idx`` remain stable with ``commit_valid`` until ``commit_ready``.
These are local IRQ FIFO reservations, independent of the oETP wire protocol.

.. list-table:: Event source encodings
   :header-rows: 1
   :widths: 15 85

   * - Code
     - Interface constant
   * - 0
     - ``EVENT_PEER_DMA_COMPLETE``
   * - 1
     - ``EVENT_NON_OETP_DMA_TX_COMPLETE``
   * - 2
     - ``EVENT_NON_OETP_DMA_RX_COMPLETE``
   * - 3
     - ``EVENT_NON_OETP_DIRECT_TX_COMPLETE``
   * - 4
     - ``EVENT_NON_OETP_DIRECT_RX_AVAILABLE``
   * - 5
     - ``EVENT_RMEM_ERROR``

The controller behavior is described in :ref:`rtl-endpoint-irq-controller`.

Functional scenarios
--------------------

This section reserves space for scenario descriptions and WaveDrom timing
diagrams. The current outline is:

* Enabled admission and reserved capacity.
* Disabled admission without a later commit.
* Delayed commitment, backpressure, and peer metadata.
