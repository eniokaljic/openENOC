.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-endpoint-peer-lookup:

Peer-table lookup -- openenoc_endpoint_peer_lookup
==================================================

.. index::
   single: openenoc_endpoint_peer_lookup

Resolves peer-table queries and returns a coherent configuration snapshot to
each client.

**Source:** :download:`openenoc_endpoint_peer_lookup.sv <../../../hw/rtl/core/openenoc_endpoint_peer_lookup.sv>`.

Parameters
----------

.. list-table:: Parameters
   :class: rtl-reference-table
   :header-rows: 1
   :widths: 20 30 20 30

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
   :widths: 29 32 17 22

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
     - CSR peer-table configuration sampled when accepting a lookup request.
   * - ``lookup_if[LOOKUP_PORTS]``
     - ``openenoc_peer_lookup_if.slv``
     - bidirectional (slv)
     - Per-client peer query and coherent peer-entry response snapshot.

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
edge once it reaches the response-queue head. Arbitration starts at client 0
after reset and advances to the client following each accepted request,
skipping clients without an active request.

All clients share a two-entry response queue. Responses leave in request
acceptance order, and only the owner of the head response sees ``rsp_valid``.
If that client stalls, a response for another client must wait behind it even
when the other client is ready. The second entry can hold a response for a
request already granted before the stall. A full queue stops new grants;
freeing an entry permits another registered grant, so a waiting request is
accepted on the following edge. With ready clients, the module accepts one
request and returns one response per cycle after the initial grant latency.
Configuration writes do not alter a buffered response, which remains stable
until its owner accepts it.

Disabled entries never match. Index lookups select peer DMA modes 2/3; RMEM
lookups select mode 1 and require the requested address to belong to its
half-open RMEM region. MAC lookups select any enabled matching entry.
``req_mode_mask`` further restricts permitted modes for every lookup type.
When several eligible entries match, the lowest peer-table index wins.
Zero-sized RMEM regions never match. The region end is calculated with an
extra carry bit, so a range extending beyond the 32-bit address space does
not wrap around to low addresses. A miss returns deterministic zero entry
fields. Reset clears the response queue, outward handshakes, and round-robin
state.

Functional scenarios
--------------------

Query types, mode masks, and single-client snapshot timing are covered by
:ref:`rtl-peer-lookup-if`. The example below uses the default two clients
and four peer entries to show contention for the shared response queue.
All requests use ``req_type = LOOKUP_BY_INDEX`` and
``req_mode_mask = 0xC``. ``I0``, ``I1``, and ``I2`` identify distinct enabled
entries in DMA mode 2 or 3, so every query returns the selected peer.

Numbered cycles label intervals between rising edges; a transfer occurs at
the ending rising edge when VALID and READY are both high. ``x`` marks
irrelevant values. The queue is initially empty, and arbitration starts
from its reset position.

Concurrent clients and shared response queue
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Both clients assert ``req_valid`` in cycle 1. Client 0 receives the first
registered grant and its request for ``I0`` transfers in cycle 2. The next
grant goes to client 1, whose request for ``I1`` transfers in cycle 3.
Client 0 presents its next request, for ``I2``, immediately after the first
acceptance and holds it while waiting for another grant.

Client 0 keeps ``rsp_ready = 0`` through cycle 5. Its response for ``I0``
remains at the queue head, and the response for ``I1`` occupies the second
entry. Client 1 keeps ``rsp_ready = 1``, but its ``rsp_valid`` stays low
until the preceding response is consumed. The full queue also prevents a
grant for the waiting ``I2`` request.

Client 0 accepts its first response in cycle 6. The newly available space
allows a registered grant for ``I2`` in cycle 7, while the response for
client 1 also transfers in that cycle. The response for ``I2`` then
transfers in cycle 8. Each response includes the full snapshot associated
with its accepted request.

.. wavedrom::
    :name: endpoint-peer-lookup-shared-queue-timing
    :caption: Shared peer-lookup response queue with a stalled client
    :alt: Two clients contend for the lookup queue; a stalled head response delays the other client.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p.........."},
            [
                "FSM",
                {
                    "name": "queue_state_reg",
                    "wave": "=..==..=.=.",
                    "data": ["EMPTY", "ONE", "FULL", "ONE", "EMPTY"]
                }
            ],
            ["lookup_if[0]",
                ["Master",
                    {"name": "req_valid", "wave": "01......0.."},
                    {"name": "req_peer_idx", "wave": "x=.=....x..", "data": ["I0", "I2"]},
                    {"name": "rsp_ready", "wave": "0.....1...."}
                ],
                ["Slave",
                    {"name": "req_ready", "wave": "0.10...1.0."},
                    {"name": "rsp_valid", "wave": "0..1...010."},
                    {"name": "rsp_peer_idx", "wave": "x..=...x=x.", "data": ["I0", "I2"]}
                ]
            ],
            {},
            ["lookup_if[1]",
                ["Master",
                    {"name": "req_valid", "wave": "01..0......"},
                    {"name": "req_peer_idx", "wave": "x=..x......", "data": ["I1"]},
                    {"name": "rsp_ready", "wave": "1.........."}
                ],
                ["Slave",
                    {"name": "req_ready", "wave": "0..10......"},
                    {"name": "rsp_valid", "wave": "0......10.."},
                    {"name": "rsp_peer_idx", "wave": "x......=x..", "data": ["I1"]}
                ]
            ]
        ],
        "head": {"tick": 0},
        "config": {"hscale": 1}
    }

.. _verification-openenoc-endpoint-peer-lookup:

Verification
------------

The test suite is in ``dv/core/openenoc_endpoint_peer_lookup/``.

Testbench
~~~~~~~~~

This cocotb suite verifies peer lookup with the generated CSR block and bridge. All peer
configuration uses AXI4-Lite transactions. Five cases run with two clients, four peers, two-bit
peer indices, and 32-bit addresses.

The tests check continuous traffic, buffered response ownership, backpressure, configuration
snapshots, overlapping-entry priority, RMEM range boundaries, and output stability between
clock edges.

Coverage
~~~~~~~~

The suite covers:

- generated CSR configuration, readback, and complete coherent peer snapshots;

- index, RMEM-address, and MAC-address lookup with DMA-mode filtering;

- disabled entries, mode masks, deterministic misses, and lowest-index match priority;

- half-open and zero-sized regions, overlaps, and address-wrap protection;

- registered grants, round-robin arbitration, and sustained one-response-per- cycle traffic;

- two buffered responses, stable backpressured data, and same-cycle replacement;

- configuration changes after acceptance and output stability between clock edges.
