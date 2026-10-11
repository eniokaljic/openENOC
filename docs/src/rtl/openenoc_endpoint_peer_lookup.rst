.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-endpoint-peer-lookup:

Peer-table lookup -- openenoc_endpoint_peer_lookup
==================================================

Resolves peer-table queries and returns a coherent configuration snapshot to
each client.

**Source:** :download:`openenoc_endpoint_peer_lookup.sv <../../../hw/rtl/core/openenoc_endpoint_peer_lookup.sv>`.

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
   * - ``LOOKUP_PORTS``
     - ``2``
     - Integer >= 1
     - Number of peer-lookup clients sharing the response queue.
   * - ``NUM_OF_PEERS``
     - ``4``
     - Integer >= 1; match generated CSR array
     - Number of peer-table entries.
   * - ``PEER_IDX_W``
     - ``NUM_OF_PEERS > 1 ? $clog2(NUM_OF_PEERS) : 1``
     - Integer >= 1; enough bits for the peer count
     - Width of local peer indices; all connected interfaces must agree.
   * - ``ADDR_W``
     - ``32``
     - 32
     - Peer address width required by the current CSR entry format.

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
   * - ``lookup_if[LOOKUP_PORTS]``
     - ``openenoc_peer_lookup_if.slv``
     - bidirectional (slv)
     - Destination lookup request and returned forwarding bitmap.

Architecture and operation
--------------------------

**Boundary and parameters:** ``endpoint_if`` supplies the CSR peer table;
``lookup_if[LOOKUP_PORTS]`` serves clients of :ref:`rtl-peer-lookup-if`.
Defaults are ``LOOKUP_PORTS = 2``, ``NUM_OF_PEERS = 4``, and ``ADDR_W = 32``;
``PEER_IDX_W`` is derived with a minimum of one bit.

A single clocked process arbitrates requests round-robin, samples peer entries,
and updates registered READY and response outputs. A request first receives a
registered grant and is accepted on the following rising edge if VALID remains
asserted. The coherent entry snapshot becomes visible after that acceptance
edge and remains stable until the owning client accepts it.

The queue writes only the accepted response entry. A same-edge write to its
head is forwarded into the registered response output without copying the
entire queue. Two response entries absorb a request already granted before backpressure is
observed. Queue occupancy uses EMPTY, ONE, and FULL states. With ready clients,
the lookup accepts and returns one request per cycle after the initial grant
latency. A full queue stops new grants, and reopening it requires a registered
grant cycle. Configuration writes do not alter a buffered response.

Disabled entries never match. Index lookups select peer DMA modes 2/3; RMEM
lookups select mode 1 and require the requested address to belong to its
half-open RMEM region. MAC lookups select any enabled matching entry.
``req_mode_mask`` further restricts permitted modes for every lookup type.
A miss returns deterministic zero entry fields. Reset clears the response
queue, outward handshakes, and round-robin state.

**Verification:** ``dv/core/openenoc_endpoint_peer_lookup/`` covers continuous
traffic, buffered response ownership, backpressure, configuration snapshots,
and subcycle output stability. Future reference
detail should illustrate simultaneous-client timing and overlapping-entry
selection using the existing tests and table scan order.

Functional scenarios
--------------------

This section reserves space for scenario descriptions and WaveDrom timing
diagrams. The current outline is:

* Index, scalar-address, and MAC-address lookups.
* Disabled entries, mode masks, overlapping matches, and range boundaries.
* Concurrent clients, buffered responses, configuration changes, and stalls.
