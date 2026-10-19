.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-FileCopyrightText: 2026 Kerim Bavcic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-forwarding-table:

Forwarding table -- openenoc_forwarding_table
=============================================

.. index::
   single: openenoc_forwarding_table

Stores Ethernet address-to-port mappings and supports lookup, learning, and
software management.

**Source:** :download:`openenoc_forwarding_table.sv <../../../hw/rtl/core/openenoc_forwarding_table.sv>`.

Parameters
----------

.. list-table:: Parameters
   :class: rtl-reference-table
   :header-rows: 1
   :widths: 24 28 22 26

   * - Name
     - Default value
     - Allowed values
     - Description
   * - ``NUM_OF_INTERFACES``
     - ``8``
     - 1..32
     - Port count and forwarding-bitmap width.
   * - ``TABLE_DEPTH``
     - ``32``
     - Integer >= 1
     - Number of forwarding-table entries.
   * - ``ENTRY_BYTES``
     - ``16``
     - Fixed local parameter
     - CPU-visible entry stride; not overridable.
   * - ``ADDR_WIDTH``
     - ``$clog2(TABLE_DEPTH*16)``
     - Derived from TABLE_DEPTH*16
     - Forwarding-table byte-address width; not overridable.

Signals
-------

Interface ports contain channels in both directions. The table identifies
the selected modport or stream role; member directions follow that interface.

.. list-table:: Public signals and interfaces
   :class: rtl-reference-table
   :header-rows: 1
   :widths: 24 34 17 25

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
     - Active-high synchronous reset; clears entries, pending requests, and the
       learning allocation pointer.
   * - ``default_forwarding``
     - ``logic [NUM_OF_INTERFACES-1:0]``
     - input
     - Bitmap returned when the table has no enabled match.
   * - ``operation_mode``
     - ``logic``
     - input
     - Zero enables autonomous learning; one selects software-managed entries.
   * - ``cpuif_req``
     - ``logic``
     - input
     - Rising-edge request for one external table-register access.
   * - ``cpuif_addr``
     - ``logic [ADDR_WIDTH-1:0]``
     - input
     - Byte address within the forwarding-table aperture.
   * - ``cpuif_req_is_wr``
     - ``logic``
     - input
     - One selects a write; zero selects a read.
   * - ``cpuif_wr_data``
     - ``logic [31:0]``
     - input
     - External write data.
   * - ``cpuif_wr_biten``
     - ``logic [31:0]``
     - input
     - Per-bit write enables for the table register word.
   * - ``cpuif_wr_ack``
     - ``logic``
     - output
     - Write completion acknowledgement.
   * - ``cpuif_rd_ack``
     - ``logic``
     - output
     - Read completion acknowledgement.
   * - ``cpuif_rd_data``
     - ``logic [31:0]``
     - output
     - Read result for the acknowledged register access.
   * - ``lookup_if``
     - ``openenoc_lookup_if.slv``
     - bidirectional (slv)
     - Destination lookup request and returned forwarding bitmap.
   * - ``learning_if``
     - ``openenoc_learning_if.slv``
     - bidirectional (slv)
     - Source-address learning request and acknowledgement.

Architecture and operation
--------------------------

The table maps 48-bit MAC addresses to ``NUM_OF_INTERFACES``-bit port bitmaps.
``TABLE_DEPTH`` sets entry count. Entries occupy 16 bytes in the CPU-visible
aperture. ``ADDR_WIDTH`` is derived as ``$clog2(TABLE_DEPTH * 16)`` for
``cpuif_addr``. The module serves external ``cpuif_*`` signals,
:ref:`rtl-lookup-if`, and :ref:`rtl-learning-if` in the fabric domain.

.. index::
   single: operation_mode

Each entry contains a MAC key, a port bitmap, and an enable bit. Only enabled
entries participate in comparisons. If several enabled entries have the same
MAC key, the lowest entry index wins. A lookup with no enabled match returns
``default_forwarding``. An enabled match with bitmap zero returns zero;
it does not fall back to the default bitmap. The table returns the selected
bitmap unchanged; ingress-port exclusion belongs to the forwarding engine.

.. list-table:: CPU word decode within each 16-byte entry
   :class: documentation-table
   :header-rows: 1
   :widths: 16 42 42

   * - Byte offset
     - Contents
     - Implemented word bits
   * - ``+0x0``
     - MAC address bits 31:0
     - 31:0
   * - ``+0x4``
     - MAC address bits 47:32
     - 15:0
   * - ``+0x8``
     - Port bitmap
     - NUM_OF_INTERFACES-1:0
   * - ``+0xC``
     - Entry enable
     - 0

``cpuif_wr_biten`` enables individual implemented bits. Unimplemented word
bits read as zero and ignore writes. The decoder ignores address bits 1:0.
For a non-power-of-two table depth, addresses selecting an entry beyond
``TABLE_DEPTH`` return zero on reads and ignore writes; both still receive
their normal acknowledgement. The software format and access contract,
including pause preconditions, are described in :ref:`runtime-switch-table`.
The table module itself has no pause input.

.. list-table:: Operation-mode effects
   :class: documentation-table
   :header-rows: 1
   :widths: 25 25 25 25

   * - operation_mode
     - Learning request
     - CPU write
     - CPU read
   * - ``0`` (unmanaged)
     - Updates the table
     - Acknowledged without changing entries
     - Reads the entry
   * - ``1`` (managed)
     - Acknowledged without changing entries
     - Updates enabled bits of the selected word
     - Reads the entry

In unmanaged mode, learning an enabled matching MAC replaces its bitmap
in place. Learning a MAC without an enabled match writes and enables the
entry at the circular allocation pointer, then advances that pointer modulo
``TABLE_DEPTH``. This allocation can overwrite an enabled entry; it does
not search for a free or least recently used entry. Refreshing a known MAC
does not advance the pointer. Managed CPU updates and ignored learning
requests do not advance it either. Reset clears all MACs, bitmaps, and enable
bits and returns the pointer to entry zero. Changing mode preserves entries
and pointer position.

Each request channel has its own pending slot. A low-to-high transition of
its request captures the associated payload; holding the request high does
not submit another operation. Each requester waits for its acknowledgement
before issuing another request. CPU, lookup, and learning requests may be
pending together. Whenever the table is idle, fixed priority selects CPU
first, then lookup, then learning. An operation already in progress finishes
before the next selection. ``operation_mode`` and ``default_forwarding``
are evaluated during service, rather than captured with the request payload.

Acknowledgements last one cycle. Lookup results are sampled with
``lookup_if.ack`` and CPU read data with ``cpuif_rd_ack``. A CPU write
takes effect at the ending edge of its acknowledgement interval. A learning
update is already visible in the interval containing ``learning_if.ack``.
An acknowledgement also completes operations whose table updates are
suppressed by the selected mode.

Functional scenarios
--------------------

The examples use ``NUM_OF_INTERFACES = 4``, a 10 ns clock period,
and released reset. ``A0``, ``A1``, and ``A2`` are distinct 48-bit
MAC addresses. Port bitmaps show all four bits in port order ``[3:0]``.
``0b0001``, ``0b0010``, ``0b0100``, and ``0b1000`` select ports 0 through 3,
respectively. ``0b1111`` is the default forwarding bitmap.
The table depth and initial contents are specified for each scenario.

A numbered tick marks a clock interval. Inputs are sampled at its ending
rising edge. ``x`` marks irrelevant payload values outside a request or
acknowledgement interval. The request and acknowledgement contracts are
described in :ref:`rtl-lookup-if` and :ref:`rtl-learning-if`.

Enabled matches, duplicate keys, and default forwarding
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use ``TABLE_DEPTH = 4``, ``operation_mode = 1``, and
``default_forwarding = 0b1111``. Software has already prepared these entries:

.. list-table:: Initial entries
   :class: documentation-table
   :header-rows: 1
   :widths: 25 25 25 25

   * - Entry index
     - MAC key
     - Bitmap
     - Enabled
   * - 0
     - ``A0``
     - ``0b0001``
     - 1
   * - 1
     - ``A0``
     - ``0b0010``
     - 1
   * - 2
     - ``A1``
     - ``0b0100``
     - 0
   * - 3
     - ``A2``
     - ``0b0000``
     - 1

The requests for ``A0``, ``A1``, and ``A2`` return ``0b0001``,
``0b1111``, and zero, respectively. The first lookup selects entry 0
over the duplicate at entry 1. The second ignores the disabled entry.
The third selects an enabled entry whose zero bitmap selects no output
ports, even though the default bitmap is nonzero.

.. wavedrom::
    :name: forwarding-table-selection-timing
    :caption: Enabled-entry selection distinguishes duplicates, default, and zero bitmap
    :alt: Enabled-entry selection distinguishes duplicates, default, and zero bitmap.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p..........."},
            [
                "FSM",
                {
                    "name": "state",
                    "wave": "=..==.==.==.",
                    "data": [
                        "ST_IDLE",
                        "ST_\nLOOKUP",
                        "ST_IDLE",
                        "ST_\nLOOKUP",
                        "ST_IDLE",
                        "ST_\nLOOKUP",
                        "ST_IDLE"
                    ],
                    "style": "font-size: 8px;"
                }
            ],
            {"name": "operation_mode", "wave": "1..........."},
            {"name": "default_forwarding", "wave": "=...........", "data": ["0b1111"]},
            [
                "lookup_if",
                [
                    "Master",
                    {"name": "req", "wave": "010.10.10..."},
                    {
                        "name": "mac_addr",
                        "wave": "x=x.=x.=x...",
                        "data": ["A0", "A1", "A2"]
                    }
                ],
                [
                    "Slave",
                    {"name": "ack", "wave": "0..10.10.10."},
                    {
                        "name": "port_bitmap",
                        "wave": "x..=x.=x.=x.",
                        "style": "font-size: 10px;",
                        "data": ["0b0001", "0b1111", "0b0000"]
                    }
                ]
            ]
        ],
        "head": {"tick": 0},
        "config": {"hscale": 1}
    }

Autonomous learning updates and circular replacement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use ``TABLE_DEPTH = 2``, ``operation_mode = 0``, and
``default_forwarding = 0b1111``. Both entries are initially disabled,
and allocation starts at entry zero. The learning operations are:

.. list-table:: Learning sequence and entry updates
   :class: documentation-table
   :header-rows: 1
   :widths: 14 14 14 58

   * - Order
     - MAC key
     - Bitmap
     - Table update
   * - 1
     - ``A0``
     - ``0b0001``
     - Allocate entry 0; next allocation uses entry 1
   * - 2
     - ``A1``
     - ``0b0010``
     - Allocate entry 1; next allocation wraps to entry 0
   * - 3
     - ``A0``
     - ``0b0100``
     - Update entry 0 in place; allocation remains at entry 0
   * - 4
     - ``A2``
     - ``0b1000``
     - Replace entry 0, removing its previous A0 mapping

Updating the known ``A0`` key changes its port association without
consuming a new entry. The following new key ``A2`` therefore replaces
entry 0, while the ``A1`` mapping remains in entry 1.

.. wavedrom::
    :name: forwarding-table-learning-timing
    :caption: Known-address updates preserve the circular replacement position
    :alt: Known-address updates preserve the circular replacement position.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p............"},
            [
                "FSM",
                {
                    "name": "state",
                    "wave": "=..==.==.==.=",
                    "data": [
                        "ST_IDLE",
                        "ST_\nLEARN",
                        "ST_IDLE",
                        "ST_\nLEARN",
                        "ST_IDLE",
                        "ST_\nLEARN",
                        "ST_IDLE",
                        "ST_\nLEARN"
                    ],
                    "style": "font-size: 12px;"
                }
            ],
            {"name": "operation_mode", "wave": "0............"},
            {"name": "default_forwarding", "wave": "=............", "data": ["0b1111"]},
            [
                "learning_if",
                [
                    "Master",
                    {"name": "req", "wave": "010.10.10.10."},
                    {
                        "name": "mac_addr",
                        "wave": "x=x.=x.=x.=x.",
                        "data": ["A0", "A1", "A0", "A2"]
                    },
                    {
                        "name": "port_bitmap",
                        "wave": "x=x.=x.=x.=x.",
                        "style": "font-size: 10px;",
                        "data": ["0b0001", "0b0010", "0b0100", "0b1000"]
                    }
                ],
                ["Slave", {"name": "ack", "wave": "0..10.10.10.1"}]
            ],
            {},
            [
                "lookup_if",
                [
                    "Master",
                    {"name": "req", "wave": "0............"},
                    {"name": "mac_addr", "wave": "x............"}
                ],
                [
                    "Slave",
                    {"name": "ack", "wave": "0............"},
                    {"name": "port_bitmap", "wave": "x............"}
                ]
            ]
        ],
        "head": {"tick": 0},
        "config": {"hscale": 1}
    }

Subsequent lookups for ``A0``, ``A1``, and ``A2`` return ``0b1111``,
``0b0010``, and ``0b1000``. The old ``A0`` key no longer has an enabled
match; the other two return their stored bitmaps.

.. wavedrom::
    :name: forwarding-table-learned-lookups-timing
    :caption: Lookups retain the surviving mappings after circular replacement
    :alt: Lookups retain the surviving mappings after circular replacement.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p............"},
            [
                "FSM",
                {
                    "name": "state",
                    "wave": "=..==.==.==..",
                    "data": [
                        "ST_IDLE",
                        "ST_\nLOOKUP",
                        "ST_IDLE",
                        "ST_\nLOOKUP",
                        "ST_IDLE",
                        "ST_\nLOOKUP",
                        "ST_IDLE"
                    ],
                    "style": "font-size: 8px;"
                }
            ],
            {"name": "operation_mode", "wave": "0............"},
            {"name": "default_forwarding", "wave": "=............", "data": ["0b1111"]},
            [
                "learning_if",
                [
                    "Master",
                    {"name": "req", "wave": "0............"},
                    {"name": "mac_addr", "wave": "x............"},
                    {"name": "port_bitmap", "wave": "x............"}
                ],
                ["Slave", {"name": "ack", "wave": "0............"}]
            ],
            {},
            [
                "lookup_if",
                [
                    "Master",
                    {"name": "req", "wave": "010.10.10...."},
                    {
                        "name": "mac_addr",
                        "wave": "x=x.=x.=x....",
                        "data": ["A0", "A1", "A2"]
                    }
                ],
                [
                    "Slave",
                    {"name": "ack", "wave": "0..10.10.10.."},
                    {
                        "name": "port_bitmap",
                        "wave": "x..=x.=x.=x..",
                        "style": "font-size: 10px;",
                        "data": ["0b1111", "0b0010", "0b1000"]
                    }
                ]
            ]
        ],
        "head": {"tick": 13},
        "config": {"hscale": 1}
    }

Concurrent CPU, lookup, and learning requests
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use ``TABLE_DEPTH = 4``, ``operation_mode = 0``, and
``default_forwarding = 0b1111``. Reset has cleared all entries. In this
scenario, CPU byte address ``A3 = 0x08`` selects entry 0's bitmap word,
and ``D0 = 0`` is its initial 32-bit value.

.. list-table:: Requests presented together in tick 1
   :class: documentation-table
   :header-rows: 1
   :widths: 14 30 56

   * - Channel
     - Request
     - Result
   * - CPU
     - Read bitmap word at ``A3``
     - Returns ``D0`` before the learning update
   * - Lookup
     - Find ``A0``
     - Returns ``0b1111`` before the learning update
   * - Learning
     - Store ``A0`` with ``0b0010``
     - Enables entry 0 with the new mapping

All three requests are captured independently. CPU read acknowledgement
arrives in tick 3, lookup acknowledgement in tick 5, and learning
acknowledgement in tick 7. The CPU read sees the cleared bitmap, and
the first lookup returns the default because both operations precede
learning. The later lookup for the same ``A0`` key returns ``0b0010``.
Payload changes after the request pulses do not replace the captured
operations.

.. wavedrom::
    :name: forwarding-table-priority-timing
    :caption: CPU and lookup observe the table before the pending learning update
    :alt: CPU and lookup observe the table before the pending learning update.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p.............."},
            ["FSM",
                {
                    "name": "state",
                    "wave": "=..======...==.",
                    "data": ["ST_IDLE",
                        "ST_CPU",
                        "ST_IDLE",
                        "ST_\nLOOKUP",
                        "ST_IDLE",
                        "ST_LEARN",
                        "ST_IDLE",
                        "ST_\nLOOKUP",
                        "ST_IDLE"
                    ],
                    "style": "font-size: 8px;"
                }
            ],
            {"name": "operation_mode", "wave": "0.............."},
            {"name": "default_forwarding", "wave": "=..............", "data": ["0b1111"]},
            {"name": "cpuif_req", "wave": "010............"},
            {"name": "cpuif_req_is_wr", "wave": "0.............."},
            {"name": "cpuif_addr", "wave": "x=x............", "data": ["A3"]},
            {"name": "cpuif_wr_ack", "wave": "0.............."},
            {"name": "cpuif_rd_ack", "wave": "0..10.........."},
            {"name": "cpuif_rd_data", "wave": "x..=x..........", "data": ["D0"]},
            {},
            ["lookup_if",
                ["Master",
                    {"name": "req", "wave": "010.......10..."},
                    {"name": "mac_addr", "wave": "x=x.......=x...", "data": ["A0", "A0"]}
                ],
                ["Slave",
                    {"name": "ack", "wave": "0....10.....10."},
                    {
                        "name": "port_bitmap",
                        "wave": "x....=x.....=x.",
                        "style": "font-size: 10px;",
                        "data": ["0b1111", "0b0010"]
                    }
                ]
            ],
            {},
            ["learning_if",
                ["Master",
                    {"name": "req", "wave": "010............"},
                    {"name": "mac_addr", "wave": "x=x............", "data": ["A0"]},
                    {
                        "name": "port_bitmap",
                        "wave": "x=x............",
                        "style": "font-size: 10px;",
                        "data": ["0b0010"]
                    }
                ],
                ["Slave", {"name": "ack", "wave": "0......10......"}]
            ]
        ],
        "head": {"tick": 0},
        "config": {"hscale": 1}
    }

.. _verification-openenoc-forwarding-table:

Verification
------------

The test suite is in ``dv/core/openenoc_forwarding_table/``.

Testbench
~~~~~~~~~

This test suite validates the ``openenoc_forwarding_table`` module, the CAM + RAM forwarding
table of the openENOC Switch. The destination MAC address is stored in the CAM, the destination
interface bitmap and the entry enable bit in the companion RAM.

The module is verified stand-alone, i.e. without the openENOC Switch Interface CSR and without
any AXI4-Stream traffic. All interfaces are driven and sampled directly.

Entry layout
^^^^^^^^^^^^

Each entry occupies 16 bytes, all words are 32-bit aligned and match the
``forwarding_table.entry[]`` register file of the openENOC Switch Interface CSR:

.. list-table::
   :class: rtl-reference-table
   :header-rows: 1
   :widths: 12 28 60

   * - Offset
     - Register
     - Contents
   * - ``+0x0``
     - ``mac_address.lo_word``
     - MAC address ``[31:0]``
   * - ``+0x4``
     - ``mac_address.hi_word``
     - MAC address ``[47:32]``
   * - ``+0x8``
     - ``iface.bitmap``
     - destination interfaces
   * - ``+0xC``
     - ``conf.enabled``
     - entry valid

Modes of operation
^^^^^^^^^^^^^^^^^^

.. list-table::
   :class: rtl-reference-table
   :header-rows: 1
   :widths: 20 20 60

   * - ``operation_mode``
     - Mode
     - Behaviour
   * - ``1``
     - managed
     - software owns the table, learning requests are acknowledged and ignored
   * - ``0``
     - unmanaged
     - the table learns autonomously, software writes are acknowledged and ignored (reads are
       allowed)

Interfaces
^^^^^^^^^^

All three interfaces share the same req/ack handshake, modelled after the
`PeakRDL internal cpuif protocol <https://peakrdl-regblock.readthedocs.io/en/latest/cpuif/internal_protocol.html>`_:
the master asserts ``*_req`` for a single clock cycle, the request payload only has to be valid
during that cycle, the table takes a snapshot of the request and answers with a single cycle
``*_ack`` once it has been processed. The master issues the next request only after it received
the acknowledge.

The snapshot is taken on the rising edge of ``*_req``, so a master that keeps its request
asserted until the acknowledge is served as well, and served exactly once.

- **CPU interface** (``cpuif_*``): 32-bit interface of the external ``forwarding_table`` regfile
  of the openENOC Switch Interface CSR (``hwif_out.forwarding_table.*`` /
  ``hwif_in.forwarding_table.*``).

- **Lookup interface**: the result is presented on ``lookup_if.port_bitmap`` together with
  ``lookup_if.ack``. A miss returns ``default_forwarding``
  (``hwif_out.default_forwarding.bitmap.value``).

- **Learning interface**: a known MAC address only refreshes its port bitmap, a new MAC address is
  written at the circular write pointer, replacing the oldest entry.

The table is a single shared resource, only one master is served at a time. The CPU interface
has the highest priority, followed by lookup and learning. Because every request is captured, a
request issued while the table is busy is served later instead of being lost.

Test cases
~~~~~~~~~~

.. list-table::
   :class: rtl-reference-table
   :header-rows: 1

   * - Test
     - Description
   * - ``run_reset_state``
     - table cleared after reset, lookup returns ``default_forwarding``
   * - ``run_cpu_program_and_readback``
     - software programs every entry and reads it back
   * - ``run_cpu_write_bit_enables``
     - ``cpuif_wr_biten`` masking of partial writes
   * - ``run_iface_bit_enables``
     - ``cpuif_wr_biten`` masking of the interface bitmap word
   * - ``run_lookup_managed``
     - lookup hit, miss, disabled entry and ``default_forwarding`` handling
   * - ``run_duplicate_mac_lowest_index_wins``
     - the same MAC address in two entries, the lowest index wins
   * - ``run_blackhole_entry``
     - a hit with an empty bitmap drops instead of falling back to flooding
   * - ``run_learning_ignored_in_managed_mode``
     - learning is acknowledged but leaves the table untouched
   * - ``run_learn_pointer_unaffected_by_managed_mode``
     - the circular write pointer does not move while in managed mode
   * - ``run_learning_unmanaged``
     - learning, bitmap refresh of a known MAC address and circular replacement
   * - ``run_cpu_write_ignored_in_unmanaged_mode``
     - software writes are acknowledged but ignored, reads still work
   * - ``run_cpu_address_out_of_range``
     - an address without an entry behind it is acknowledged, reads as zero and writes nowhere
   * - ``run_exclusive_access``
     - overlapping CPU and lookup accesses are serialized
   * - ``run_concurrent_requests``
     - requests issued on all interfaces in the same cycle are captured, all served and
       prioritized
   * - ``run_held_request``
     - a request held past the acknowledge results in exactly one transaction
   * - ``run_back_to_back_requests``
     - a new request in the cycle right after the acknowledge, without idle cycles
