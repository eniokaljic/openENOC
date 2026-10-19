.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-lookup-if:

Forwarding lookup -- openenoc_lookup_if
=======================================

.. index::
   single: openenoc_lookup_if

Defines an Ethernet destination lookup request and returned forwarding bitmap.

**Source:** :download:`openenoc_lookup_if.sv <../../../hw/rtl/core/openenoc_lookup_if.sv>`.

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
     - ``8``
     - 1..32
     - Port count and forwarding-bitmap width.

Connected interfaces must use the same bitmap width.

Signals
-------

Directions are relative to the ``mst`` and ``slv`` modports.

.. list-table:: Public signals and interfaces
   :class: rtl-reference-table
   :header-rows: 1
   :widths: 18 35 16 31

   * - Name
     - Type
     - Direction / role
     - Description
   * - ``req``
     - ``logic``
     - mst: output; slv: input
     - Destination lookup request strobe; one outstanding request per requester.
   * - ``mac_addr``
     - ``logic [47:0]``
     - mst: output; slv: input
     - Destination MAC address, captured with req.
   * - ``ack``
     - ``logic``
     - mst: input; slv: output
     - Completes the outstanding lookup; port_bitmap is valid with ack.
   * - ``port_bitmap``
     - ``logic [NUM_OF_INTERFACES-1:0]``
     - mst: input; slv: output
     - Returned egress selection; bit k selects port k.

Architecture and operation
--------------------------

**Parameter and roles:** ``NUM_OF_INTERFACES`` defaults to 8 and sets the
width of ``port_bitmap``. Modports are ``mst`` and ``slv``.

The requester presents a 48-bit destination ``mac_addr`` with a one-cycle
``req`` pulse, then waits for ``ack`` before issuing another lookup.
The existing RTL producers return ``req`` low on the following cycle and
wait for completion with ``req = 0``. The responder captures requests on
the low-to-high transition of ``req``. A request held through acknowledgement
is also accepted as one transaction; another request needs a new low-to-high
transition.

The receiver captures the MAC address with the request, so the requester
need not retain it after the request cycle. Keeping the address stable
until acknowledgement is also valid. When ``req`` remains high, the
acknowledgement still refers to the address captured in its first active
cycle; later address changes do not replace that request.

``ack`` qualifies ``port_bitmap`` and completes the transaction. There
is no request-ready or response-ready signal, so the requester must sample
the bitmap in the acknowledgement cycle. Multiple set bits select multiple
ports; an all-zero bitmap selects none.

Clock and reset belong to the connected modules. The interface contains
signals and modports, with no clock/reset ports or internal storage.

Functional scenarios
--------------------

The examples use ``NUM_OF_INTERFACES = 8``. ``A0`` and ``A1`` denote
destination MAC addresses. Port bitmaps show all eight bits in port order
``[7:0]``: ``0b00000001`` selects port 0 and ``0b00000010`` selects port 1.
Address labels are local to each diagram.

``clk`` is the common clock of the connected logic, shown as a sampling
reference. Numbered cycles label intervals between rising edges; values are
sampled at each interval's ending rising edge. Shaded ``x`` regions mark
irrelevant values, not a requirement to drive unknowns. Response bitmaps
are meaningful only with ``ack = 1``. The illustrated latencies depend
on the connected responder and are not an interface guarantee.

Lookup request and acknowledged bitmap
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In cycle 1, the requester pulses ``req`` with ``mac_addr = A0``.
The receiver captures ``A0`` at the end of that cycle. ``req`` returns
low in cycle 2 while the lookup is pending. This requester retains the
address through completion, although only the request cycle needs it.

In cycle 3, the responder asserts ``ack`` with ``port_bitmap = 0b00000001``.
The requester samples ``0b00000001`` at that cycle's ending rising edge.
Acknowledgement is a completion event, not a request to hold ``req``
high. The requester may issue another lookup after this completion.

.. wavedrom::
    :name: lookup-if-request-timing
    :caption: Lookup request and acknowledged forwarding bitmap
    :alt: Request for A0 in cycle 1 returns bitmap 0b00000001 with acknowledgement in cycle 3.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p....."},
            ["Master",
                {"name": "req", "wave": "010..."},
                {"name": "mac_addr", "wave": "x=..x.", "data": ["A0"]}
            ],
            ["Slave",
                {"name": "ack", "wave": "0..10."},
                {
                    "name": "port_bitmap",
                    "wave": "x..=x.",
                    "style": "font-size: 12px;",
                    "data": ["0b00000001"]
                }
            ]
        ],
        "head": {"tick": 0},
        "config": {"hscale": 2}
    }

Sequential lookup transactions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The requester pulses ``req`` with ``A0`` in cycle 1 and waits for
``ack`` with ``0b00000001`` in cycle 3. After that lookup completes, it issues
another request for ``A1`` in cycle 5. The responder returns ``0b00000010``
with ``ack`` in cycle 7. Each request therefore has its own completion,
and no two lookups from this requester are outstanding at the same time.

.. wavedrom::
    :name: lookup-if-sequential-timing
    :caption: Sequential lookup requests with their corresponding response bitmaps
    :alt: A0 and A1 requests complete with bitmaps 0b00000001 and 0b00000010, respectively.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p........"},
            ["Master",
                {"name": "req", "wave": "010..10.."},
                {"name": "mac_addr", "wave": "x=..x=..x", "data": ["A0", "A1"]}
            ],
            ["Slave",
                {"name": "ack", "wave": "0..10..10"},
                {
                    "name": "port_bitmap",
                    "wave": "x..=x..=x",
                    "style": "font-size: 12px;",
                    "data": ["0b00000001", "0b00000010"]
                }
            ]
        ],
        "head": {"tick": 0},
        "config": {"hscale": 2}
    }

Returned bitmaps can select one, multiple, or no ports and are sampled only
with their matching acknowledgements. An all-zero bitmap completes the
request in the same way as any other bitmap value.

Request held until acknowledgement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The requester raises ``req`` with ``A0`` in cycle 1 and keeps it high
through cycle 7. The responder captures ``A0`` at the ending rising edge
of cycle 1, the first active request cycle.

In cycle 2, the requester changes ``mac_addr`` to ``A1`` while
``req`` is still high. With no new low-to-high request transition,
``A1`` does not start another lookup or modify the captured ``A0``.

The responder completes the original ``A0`` request in cycle 7 with
``ack = 1`` and ``port_bitmap = 0b00000001``. The acknowledgement refers to
the first-cycle address, even though ``A1`` is now on the address signal.
After sampling the completion, the requester deasserts ``req`` in
cycle 8. Another request requires a fresh low-to-high transition.

.. wavedrom::
    :name: lookup-if-retained-payload-timing
    :caption: Held request acknowledged for its first-cycle destination address
    :alt: Held REQ completes for A0 and bitmap 0b00000001 from cycle 1 despite later A1.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p........."},
            ["Master",
                {"name": "req", "wave": "01......0."},
                {"name": "mac_addr", "wave": "x==.......", "data": ["A0", "A1"]}
            ],
            ["Slave",
                {"name": "ack", "wave": "0......10."},
                {
                    "name": "port_bitmap",
                    "wave": "x......=x.",
                    "style": "font-size: 12px;",
                    "data": ["0b00000001"]
                }
            ]
        ],
        "head": {"tick": 0},
        "config": {"hscale": 2}
    }

The requester must not pulse another request while its earlier lookup is
outstanding. No fixed completion latency is implied by the interface.
