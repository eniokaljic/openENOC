.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-FileCopyrightText: 2026 Kerim Bavcic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-forwarding-table-arb-mux:

Forwarding-table request arbiter -- openenoc_forwarding_table_arb_mux
=====================================================================

Arbitrates multiple lookup and learning clients onto a shared forwarding table.

**Source:** :download:`openenoc_forwarding_table_arb_mux.sv <../../../hw/rtl/core/openenoc_forwarding_table_arb_mux.sv>`.

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
   * - ``NUM_OF_INTERFACES``
     - ``4``
     - 2..32
     - Number of upstream lookup/learning clients and bitmap width.

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
   * - ``s_lookup_if[NUM_OF_INTERFACES]``
     - ``openenoc_lookup_if.slv``
     - bidirectional (slv)
     - Per-port destination lookup clients.
   * - ``s_learning_if[NUM_OF_INTERFACES]``
     - ``openenoc_learning_if.slv``
     - bidirectional (slv)
     - Per-port source-learning clients.
   * - ``m_lookup_if``
     - ``openenoc_lookup_if.mst``
     - bidirectional (mst)
     - Shared forwarding-table lookup channel.
   * - ``m_learning_if``
     - ``openenoc_learning_if.mst``
     - bidirectional (mst)
     - Shared forwarding-table learning channel.

Architecture and operation
--------------------------

``NUM_OF_INTERFACES`` sets the number of ``s_lookup_if`` and ``s_learning_if``
clients. ``m_lookup_if`` and ``m_learning_if`` connect the shared table.
Lookup and learning have independent round-robin arbiters.

Each source may have one outstanding request per channel. A request can be
a one-cycle strobe; its payload is captured even while another source owns
the downstream channel. A requester that holds ``req`` until ``ack`` is also
accepted through edge detection. Each downstream channel has one outstanding
transaction, with registered ownership until acknowledgement. The table keeps
its separate CPU/lookup/learning priority policy. ``rst`` clears pending requests
and ownership.

**Verification:** ``dv/core/openenoc_forwarding_table_arb_mux/``. Further
documentation should illustrate simultaneous requests and independent-channel
progress.

Functional scenarios
--------------------

This section reserves space for scenario descriptions and WaveDrom timing
diagrams. The current outline is:

* Simultaneous client requests and round-robin service.
* One-cycle requests and requests held until acknowledgement.
* Independent lookup/learning progress and reset.
