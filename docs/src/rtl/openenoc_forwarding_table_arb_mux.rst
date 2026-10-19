.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-FileCopyrightText: 2026 Kerim Bavcic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-forwarding-table-arb-mux:

Forwarding-table request arbiter -- openenoc_forwarding_table_arb_mux
=====================================================================

.. index::
   single: openenoc_forwarding_table_arb_mux

Arbitrates multiple lookup and learning clients onto a shared forwarding table.

**Source:** :download:`openenoc_forwarding_table_arb_mux.sv <../../../hw/rtl/core/openenoc_forwarding_table_arb_mux.sv>`.

Parameters
----------

.. list-table:: Parameters
   :class: rtl-reference-table
   :header-rows: 1
   :widths: 24 18 20 38

   * - Name
     - Default value
     - Allowed values
     - Description
   * - ``NUM_OF_INTERFACES``
     - ``4``
     - 2..32
     - Number of upstream clients on each channel and width of every port bitmap;
       all connected interfaces must use this value.

Signals
-------

Interface ports contain channels in both directions. The table identifies
the selected modport or stream role; member directions follow that interface.

.. list-table:: Public signals and interfaces
   :class: rtl-reference-table
   :header-rows: 1
   :widths: 24 30 17 29

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
     - Active-high reset; suppresses requests and acknowledgements and clears
       pending work, ownership, captured payloads, and arbitration priority.
   * - ``s_lookup_if [NUM_OF_INTERFACES]``
     - ``openenoc_lookup_if.slv``
     - bidirectional (slv)
     - Per-port destination lookup clients.
   * - ``s_learning_if [NUM_OF_INTERFACES]``
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

Each client may have one outstanding request on each channel. A low-to-high
transition of ``req`` captures its MAC address and, for learning, its port
bitmap. Capture works while another client owns the downstream channel.
Pending requests from different clients are retained separately. A client
cannot queue a second request on the same channel before its first completes.

Each idle channel searches its pending clients in circular order, starting
at its current priority position. Reset initializes that position to client
zero. Launching a request advances it to the client after the winner, wrapping
after ``NUM_OF_INTERFACES - 1``. Empty positions are skipped. A request
captured during an interval becomes eligible after that interval's ending
edge; selection does not bypass the captured pending state.

A downstream request is a registered one-cycle pulse. Its selected MAC and
learning bitmap come from the captured payload, and its client identity is
retained until acknowledgement. Only one transaction may be outstanding on
each downstream channel. Even with queued work, the next request is launched
after the current response has released ownership; it is not issued in the
response interval.

An upstream request held through acknowledgement is one transaction. Changing
its payload after the first active interval does not replace the snapshot.
Another request requires a sampled low interval followed by a new assertion.
A new request may coincide with the previous acknowledgement after such a low
interval; the new payload is queued separately from the completing operation.

The downstream acknowledgement is routed to the recorded owner in the same
interval, without an additional response register. A lookup bitmap is passed
to that owner with its acknowledgement; all other lookup clients receive
``ack = 0`` and bitmap zero. Learning returns only the acknowledgement.
The module does not interpret MAC matches or bitmap contents.

Lookup and learning keep independent priority positions, pending requests,
and active owners. Both downstream request pulses may therefore occur
together, and waiting on one response does not hold the other arbiter.
The shared :ref:`rtl-forwarding-table` still applies its own fixed
CPU/lookup/learning service priority; independent arbitration does not make
table accesses simultaneous.

Asserting ``rst`` suppresses both downstream request pulses and upstream
acknowledgements. The clocked reset clears queued work, active ownership,
payload snapshots, and both priority positions. Cancelled requests receive no
completion. Reset is coordinated with the clients and downstream table so
that abandoned responses are discarded before new work starts.

Functional scenarios
--------------------

The examples use ``NUM_OF_INTERFACES = 4`` and a 10 ns clock period.
``A0`` through ``A5`` are distinct MAC addresses. Port bitmaps show all four
bits in port order ``[3:0]``. ``0b0001``, ``0b0010``, ``0b0100``, and ``0b1000``
select ports 0 through 3; ``0b1111`` is the default bitmap.

The downstream forwarding table has four entries. Initially it contains
enabled mappings ``A0/0b0001``, ``A1/0b0010``, ``A2/0b0100``, and ``A3/0b1000``
at indices 0 through 3. Learning allocation starts at entry zero.
The first two scenarios use managed mode; the final two use unmanaged mode.
All examples start after reset and initial table setup, except for the reset
explicitly shown in the final scenario.

A numbered tick marks a clock interval. Inputs are sampled at its ending
rising edge. ``x`` marks payload values that are irrelevant outside their
request or response interval. Upstream lookup bitmaps are shown as zero
outside their owning acknowledgement, matching the module's output gating.

Round-robin order wraps across the client array
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Client 2 first issues a lookup for ``A2`` in tick 1. Its response in
tick 5 completes that request. The next priority position is now client 3.
In tick 6, all four clients submit new lookup requests:

.. list-table:: Lookup requests presented together in tick 6
   :class: documentation-table
   :header-rows: 1
   :widths: 25 25 25 25

   * - Client
     - MAC key
     - Response bitmap
     - Service order
   * - 0
     - ``A0``
     - ``0b0001``
     - 2
   * - 1
     - ``A1``
     - ``0b0010``
     - 3
   * - 2
     - ``A2``
     - ``0b0100``
     - 4
   * - 3
     - ``A3``
     - ``0b1000``
     - 1

The burst is served in order 3, 0, 1, 2. Each response reaches only
the client whose request was forwarded. The one-cycle source pulses
remain pending while earlier transactions use the table channel.

.. wavedrom::
    :name: forwarding-arb-round-robin-timing
    :caption: Round-robin lookup service wraps from client 3 to client 0
    :alt: Round-robin lookup service wraps from client 3 to client 0.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p........................"},
            ["s_lookup_if[0]",
                ["Master",
                    {"name": "req", "wave": "0.....10................."},
                    {"name": "mac_addr", "wave": "x.....=x.................", "data": ["A0"]}
                ],
                ["Slave",
                    {"name": "ack", "wave": "0.............10........."},
                    {
                        "name": "port_bitmap",
                        "wave": "=.............==.........",
                        "style": "font-size: 12px;",
                        "data": ["0b0000", "0b0001", "0b0000"]
                    }
                ]
            ],
            {},
            ["s_lookup_if[1]",
                ["Master",
                    {"name": "req", "wave": "0.....10................."},
                    {"name": "mac_addr", "wave": "x.....=x.................", "data": ["A1"]}
                ],
                ["Slave",
                    {"name": "ack", "wave": "0.................10....."},
                    {
                        "name": "port_bitmap",
                        "wave": "=.................==.....",
                        "style": "font-size: 10px;",
                        "data": ["0b0000", "0b0010", "0b0000"]
                    }
                ]
            ],
            {},
            ["s_lookup_if[2]",
                ["Master",
                    {"name": "req", "wave": "010...10................."},
                    {"name": "mac_addr", "wave": "x=x...=x.................", "data": ["A2", "A2"]}
                ],
                ["Slave",
                    {"name": "ack", "wave": "0....10...............10."},
                    {
                        "name": "port_bitmap",
                        "wave": "=....==...............==.",
                        "style": "font-size: 10px;",
                        "data": ["0b0000", "0b0100", "0b0000", "0b0100", "0b0000"]
                    }
                ]
            ],
            {},
            ["s_lookup_if[3]",
                ["Master",
                    {"name": "req", "wave": "0.....10................."},
                    {"name": "mac_addr", "wave": "x.....=x.................", "data": ["A3"]}
                ],
                ["Slave",
                    {"name": "ack", "wave": "0.........10............."},
                    {
                        "name": "port_bitmap",
                        "wave": "=.........==.............",
                        "style": "font-size: 10px;",
                        "data": ["0b0000", "0b1000", "0b0000"]
                    }
                ]
            ],
            {},
            ["m_lookup_if",
                ["Master",
                    {"name": "req", "wave": "0..10...10..10..10..10..."},
                    {
                        "name": "mac_addr",
                        "wave": "x..=x...=x..=x..=x..=x...",
                        "data": ["A2", "A3", "A0", "A1", "A2"]
                    }
                ],
                ["Slave",
                    {"name": "ack", "wave": "0....10...10..10..10..10."},
                    {
                        "name": "port_bitmap",
                        "wave": "x....=x...=x..=x..=x..=x.",
                        "style": "font-size: 10px;",
                        "data": ["0b0100", "0b1000", "0b0001", "0b0010", "0b0100"]
                    }
                ]
            ]
        ],
        "head": {"tick": 0},
        "config": {"hscale": 1}
    }

Captured pulses and a request held through acknowledgement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The first lookup waits while the shared table serves higher-priority CPU
reads. During that wait, two more clients submit requests:

.. list-table:: Requests retained while the first lookup is outstanding
   :class: documentation-table
   :header-rows: 1
   :widths: 12 22 24 42

   * - Client
     - First request tick
     - Captured MAC key
     - Request behavior
   * - 0
     - 1
     - ``A0``
     - One-cycle pulse; completes with 0b0001
   * - 1
     - 4
     - ``A1``
     - One-cycle pulse while client 0 is active; completes with 0b0010
   * - 2
     - 5
     - ``A2``
     - Holds req through acknowledgement; completes with 0b0100

Client 2 changes its live ``mac_addr`` to ``A3`` in tick 6 while
keeping ``req`` high. Its downstream request still carries ``A2``,
and its returned bitmap is ``0b0100``. Client 1's pulse is also retained
even though its source payload is no longer meaningful while it waits.
The responses arrive in ticks 11, 15, and 19, respectively. The held
request produces one downstream transaction and one acknowledgement.

.. wavedrom::
    :name: forwarding-arb-capture-timing
    :caption: Queued pulses and a held request retain their first captured MAC
    :alt: Queued pulses and a held request retain their first captured MAC.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p....................."},
            ["s_lookup_if[0]",
                ["Master",
                    {"name": "req", "wave": "010..................."},
                    {"name": "mac_addr", "wave": "x=x...................", "data": ["A0"]}
                ],
                ["Slave",
                    {"name": "ack", "wave": "0..........10........."},
                    {
                        "name": "port_bitmap",
                        "wave": "=..........==.........",
                        "style": "font-size: 12px;",
                        "data": ["0b0000", "0b0001", "0b0000"]
                    }
                ]
            ],
            {},
            ["s_lookup_if[1]",
                ["Master",
                    {"name": "req", "wave": "0...10................"},
                    {"name": "mac_addr", "wave": "x...=x................", "data": ["A1"]}
                ],
                ["Slave",
                    {"name": "ack", "wave": "0..............10....."},
                    {
                        "name": "port_bitmap",
                        "wave": "=..............==.....",
                        "style": "font-size: 10px;",
                        "data": ["0b0000", "0b0010", "0b0000"]
                    }
                ]
            ],
            {},
            ["s_lookup_if[2]",
                ["Master",
                    {"name": "req", "wave": "0....1..............0."},
                    {"name": "mac_addr", "wave": "x....==.............x.", "data": ["A2", "A3"]}
                ],
                ["Slave",
                    {"name": "ack", "wave": "0..................10."},
                    {
                        "name": "port_bitmap",
                        "wave": "=..................==.",
                        "style": "font-size: 10px;",
                        "data": ["0b0000", "0b0100", "0b0000"]
                    }
                ]
            ],
            {},
            ["s_lookup_if[3]",
                ["Master",
                    {"name": "req", "wave": "0....................."},
                    {"name": "mac_addr", "wave": "x....................."}
                ],
                ["Slave",
                    {"name": "ack", "wave": "0....................."},
                    {"name": "port_bitmap", "wave": "=.....................", "data": ["0b0000"]}
                ]
            ],
            {},
            ["m_lookup_if",
                ["Master",
                    {"name": "req", "wave": "0..10........10..10..."},
                    {
                        "name": "mac_addr",
                        "wave": "x..=x........=x..=x...",
                        "data": ["A0", "A1", "A2"]
                    }
                ],
                ["Slave",
                    {"name": "ack", "wave": "0..........10..10..10."},
                    {
                        "name": "port_bitmap",
                        "wave": "x..........=x..=x..=x.",
                        "style": "font-size: 10px;",
                        "data": ["0b0001", "0b0010", "0b0100"]
                    }
                ]
            ]
        ],
        "head": {"tick": 0},
        "config": {"hscale": 1}
    }

Independent lookup and learning arbitration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Four requests arrive together in tick 1. CPU table access is idle:

.. list-table:: Concurrent requests on the two channels
   :class: documentation-table
   :header-rows: 1
   :widths: 25 25 25 25

   * - Channel
     - Client
     - MAC key
     - Bitmap
   * - Lookup
     - 0
     - ``A0``
     - Returns ``0b0001``
   * - Lookup
     - 3
     - ``A3``
     - Returns ``0b1000``
   * - Learning
     - 1
     - ``A4``
     - Stores ``0b0010``
   * - Learning
     - 2
     - ``A5``
     - Stores ``0b0100``

Both arbiters launch their first request in tick 3. The table completes
lookup client 0 in tick 5 and learning client 1 in tick 7. The next
lookup request is already launched in tick 7, while the learning
acknowledgement belongs to its previous owner. The next learning request
follows in tick 9. Separate priority positions produce lookup order
0, 3 and learning order 1, 2.

Each MAC and learning bitmap remains associated with its captured client.
The table's sequential service completes the remaining lookup in tick 9
and learning request in tick 11; acknowledgements are routed independently.

.. wavedrom::
    :name: forwarding-arb-independent-timing
    :caption: Lookup and learning keep independent owners and request order
    :alt: Lookup and learning keep independent owners and request order.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p............."},
            ["s_lookup_if[0]",
                ["Master",
                    {"name": "req", "wave": "010..........."},
                    {"name": "mac_addr", "wave": "x=x...........", "data": ["A0"]}
                ],
                ["Slave",
                    {"name": "ack", "wave": "0....10......."},
                    {
                        "name": "port_bitmap",
                        "wave": "=....==.......",
                        "style": "font-size: 12px;",
                        "data": ["0b0000", "0b0001", "0b0000"]
                    }
                ]
            ],
            {},
            ["s_lookup_if[1]",
                ["Master",
                    {"name": "req", "wave": "0............."},
                    {"name": "mac_addr", "wave": "x............."}
                ],
                ["Slave",
                    {"name": "ack", "wave": "0............."},
                    {"name": "port_bitmap", "wave": "=.............", "data": ["0b0000"]}
                ]
            ],
            {},
            ["s_lookup_if[2]",
                ["Master",
                    {"name": "req", "wave": "0............."},
                    {"name": "mac_addr", "wave": "x............."}
                ],
                ["Slave",
                    {"name": "ack", "wave": "0............."},
                    {"name": "port_bitmap", "wave": "=.............", "data": ["0b0000"]}
                ]
            ],
            {},
            ["s_lookup_if[3]",
                ["Master",
                    {"name": "req", "wave": "010..........."},
                    {"name": "mac_addr", "wave": "x=x...........", "data": ["A3"]}
                ],
                ["Slave",
                    {"name": "ack", "wave": "0........10..."},
                    {
                        "name": "port_bitmap",
                        "wave": "=........==...",
                        "style": "font-size: 10px;",
                        "data": ["0b0000", "0b1000", "0b0000"]
                    }
                ]
            ],
            {},
            ["m_lookup_if",
                ["Master",
                    {"name": "req", "wave": "0..10..10....."},
                    {"name": "mac_addr", "wave": "x..=x..=x.....", "data": ["A0", "A3"]}
                ],
                ["Slave",
                    {"name": "ack", "wave": "0....10..10..."},
                    {
                        "name": "port_bitmap",
                        "wave": "x....=x..=x...",
                        "style": "font-size: 10px;",
                        "data": ["0b0001", "0b1000"]
                    }
                ]
            ],
            {},
            ["s_learning_if[0]",
                ["Master",
                    {"name": "req", "wave": "0............."},
                    {"name": "mac_addr", "wave": "x............."},
                    {"name": "port_bitmap", "wave": "x............."}
                ],
                ["Slave", {"name": "ack", "wave": "0............."}]
            ],
            {},
            ["s_learning_if[1]",
                ["Master",
                    {"name": "req", "wave": "010..........."},
                    {"name": "mac_addr", "wave": "x=x...........", "data": ["A4"]},
                    {
                        "name": "port_bitmap",
                        "wave": "x=x...........",
                        "style": "font-size: 10px;",
                        "data": ["0b0010"]
                    }
                ],
                ["Slave", {"name": "ack", "wave": "0......10....."}]
            ],
            {},
            ["s_learning_if[2]",
                ["Master",
                    {"name": "req", "wave": "010..........."},
                    {"name": "mac_addr", "wave": "x=x...........", "data": ["A5"]},
                    {
                        "name": "port_bitmap",
                        "wave": "x=x...........",
                        "style": "font-size: 10px;",
                        "data": ["0b0100"]
                    }
                ],
                ["Slave", {"name": "ack", "wave": "0..........10."}]
            ],
            {},
            ["s_learning_if[3]",
                ["Master",
                    {"name": "req", "wave": "0............."},
                    {"name": "mac_addr", "wave": "x............."},
                    {"name": "port_bitmap", "wave": "x............."}
                ],
                ["Slave", {"name": "ack", "wave": "0............."}]
            ],
            {},
            ["m_learning_if",
                ["Master",
                    {"name": "req", "wave": "0..10....10..."},
                    {"name": "mac_addr", "wave": "x..=x....=x...", "data": ["A4", "A5"]},
                    {
                        "name": "port_bitmap",
                        "wave": "x..=x....=x...",
                        "style": "font-size: 10px;",
                        "data": ["0b0010", "0b0100"]
                    }
                ],
                ["Slave", {"name": "ack", "wave": "0......10..10."}]
            ]
        ],
        "head": {"tick": 0},
        "config": {"hscale": 1}
    }

Reset cancels active and queued requests
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Initially the requests are:

.. list-table:: Work submitted before reset
   :class: documentation-table
   :header-rows: 1
   :widths: 25 25 25 25

   * - Channel
     - Client
     - Request tick
     - Payload
   * - Lookup
     - 0
     - 1
     - ``A0``
   * - Lookup
     - 1
     - 2
     - ``A1``
   * - Learning
     - 2
     - 1
     - ``A4/0b0100``

The first lookup and learning requests reach the table in tick 3;
the second lookup remains queued. Reset is asserted in ticks 4 and 5
for the clients, arbiter, and table. None of those requests receives a
completion or is replayed after reset.

Client 3 issues a fresh lookup for ``A3`` in tick 7. It is forwarded
in tick 9 and acknowledged in tick 11. The bitmap is ``0b1111`` because
the coordinated table reset has also cleared the initial entries.

.. wavedrom::
    :name: forwarding-arb-reset-timing
    :caption: Reset discards active and queued requests before a fresh lookup
    :alt: Reset discards active and queued requests before a fresh lookup.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p............."},
            {"name": "rst", "wave": "0...1.0......."},
            ["s_lookup_if[0]",
                ["Master",
                    {"name": "req", "wave": "010..........."},
                    {"name": "mac_addr", "wave": "x=x...........", "data": ["A0"]}
                ],
                ["Slave",
                    {"name": "ack", "wave": "0............."},
                    {"name": "port_bitmap", "wave": "=.............", "data": ["0b0000"]}
                ]
            ],
            {},
            ["s_lookup_if[1]",
                ["Master",
                    {"name": "req", "wave": "0.10.........."},
                    {"name": "mac_addr", "wave": "x.=x..........", "data": ["A1"]}
                ],
                ["Slave",
                    {"name": "ack", "wave": "0............."},
                    {"name": "port_bitmap", "wave": "=.............", "data": ["0b0000"]}
                ]
            ],
            {},
            ["s_lookup_if[2]",
                ["Master",
                    {"name": "req", "wave": "0............."},
                    {"name": "mac_addr", "wave": "x............."}
                ],
                ["Slave",
                    {"name": "ack", "wave": "0............."},
                    {"name": "port_bitmap", "wave": "=.............", "data": ["0b0000"]}
                ]
            ],
            {},
            ["s_lookup_if[3]",
                ["Master",
                    {"name": "req", "wave": "0......10....."},
                    {"name": "mac_addr", "wave": "x......=x.....", "data": ["A3"]}
                ],
                ["Slave",
                    {"name": "ack", "wave": "0..........10."},
                    {
                        "name": "port_bitmap",
                        "wave": "=..........==.",
                        "style": "font-size: 12px;",
                        "data": ["0b0000", "0b1111", "0b0000"]
                    }
                ]
            ],
            {},
            ["m_lookup_if",
                ["Master",
                    {"name": "req", "wave": "0..10....10..."},
                    {"name": "mac_addr", "wave": "x..=x....=x...", "data": ["A0", "A3"]}
                ],
                ["Slave",
                    {"name": "ack", "wave": "0..........10."},
                    {
                        "name": "port_bitmap",
                        "wave": "x..........=x.",
                        "style": "font-size: 12px;",
                        "data": ["0b1111"]
                    }
                ]
            ],
            {},
            ["s_learning_if[0]",
                ["Master",
                    {"name": "req", "wave": "0............."},
                    {"name": "mac_addr", "wave": "x............."},
                    {"name": "port_bitmap", "wave": "x............."}
                ],
                ["Slave", {"name": "ack", "wave": "0............."}]
            ],
            {},
            ["s_learning_if[1]",
                ["Master",
                    {"name": "req", "wave": "0............."},
                    {"name": "mac_addr", "wave": "x............."},
                    {"name": "port_bitmap", "wave": "x............."}
                ],
                ["Slave", {"name": "ack", "wave": "0............."}]
            ],
            {},
            ["s_learning_if[2]",
                ["Master",
                    {"name": "req", "wave": "010..........."},
                    {"name": "mac_addr", "wave": "x=x...........", "data": ["A4"]},
                    {
                        "name": "port_bitmap",
                        "wave": "x=x...........",
                        "style": "font-size: 10px;",
                        "data": ["0b0100"]
                    }
                ],
                ["Slave", {"name": "ack", "wave": "0............."}]
            ],
            {},
            ["s_learning_if[3]",
                ["Master",
                    {"name": "req", "wave": "0............."},
                    {"name": "mac_addr", "wave": "x............."},
                    {"name": "port_bitmap", "wave": "x............."}
                ],
                ["Slave", {"name": "ack", "wave": "0............."}]
            ],
            {},
            ["m_learning_if",
                ["Master",
                    {"name": "req", "wave": "0..10........."},
                    {"name": "mac_addr", "wave": "x..=x.........", "data": ["A4"]},
                    {
                        "name": "port_bitmap",
                        "wave": "x..=x.........",
                        "style": "font-size: 10px;",
                        "data": ["0b0100"]
                    }
                ],
                ["Slave", {"name": "ack", "wave": "0............."}]
            ]
        ],
        "head": {"tick": 0},
        "config": {"hscale": 1}
    }

.. _verification-openenoc-forwarding-table-arb-mux:

Verification
------------

The test suite is in ``dv/core/openenoc_forwarding_table_arb_mux/``.

Testbench
~~~~~~~~~

This suite validates ``openenoc_forwarding_table_arb_mux`` as a stand-alone module. The real
forwarding table, forwarding engines and Ethernet datapath are not instantiated. Cocotb drives
all lookup and learning masters directly and models the two forwarding-table slave interfaces
with independently variable response delays.

The module contains two independent round-robin arbiters:

- all per-port lookup interfaces share one downstream lookup interface;

- all per-port learning interfaces share one downstream learning interface.

Every source can have one outstanding request per channel. The arbiter captures the one-cycle
request and its payload, queues simultaneous requests, keeps the selected owner until the slave
acknowledges the transaction, and returns the response only to that owner. Lookup and learning
may be active concurrently.

Coverage
~~~~~~~~

The TestFactory matrix combines three arrival patterns, four slave timing profiles and three
channel selections:

.. list-table::
   :class: rtl-reference-table
   :header-rows: 1
   :widths: 30 70

   * - Dimension
     - Values
   * - Request arrival
     - consecutive source requests, request during an active transaction, all ports
       simultaneously
   * - Slave response delay
     - minimum, alternating short/long, deterministic random, long
   * - Active channels
     - lookup only, learning only, lookup and learning concurrently

Additional directed tests cover:

- independent completion timing between lookup and learning;

- new requests arriving on the same edge as a slave acknowledge;

- requests held until acknowledge producing exactly one transaction;

- repeatable randomized arrivals and variable response delays;

- reset while transactions are active and queued.

The scoreboard checks every captured request, payload snapshot, downstream request strobe,
round-robin selection, registered owner, acknowledge target and lookup bitmap. Inactive payloads
are deliberately overwritten after request capture so that using live source data instead of the
saved request is detected.

Parameter sweep
~~~~~~~~~~~~~~~

The pytest runner sweeps ``NUM_OF_INTERFACES`` over 2, 4, 5, 8 and 32 ports. The five-port
configuration checks round-robin pointer wrap for a port count that is not a power of two.
