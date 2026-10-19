.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-learning-if:

Forwarding learning -- openenoc_learning_if
===========================================

.. index::
   single: openenoc_learning_if

Defines an Ethernet source-learning request and acknowledgement channel.

**Source:** :download:`openenoc_learning_if.sv <../../../hw/rtl/core/openenoc_learning_if.sv>`.

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
     - Port count and ingress-bitmap width.

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
     - Source-learning request strobe; one outstanding request per requester.
   * - ``mac_addr``
     - ``logic [47:0]``
     - mst: output; slv: input
     - Source MAC address, captured with req.
   * - ``port_bitmap``
     - ``logic [NUM_OF_INTERFACES-1:0]``
     - mst: output; slv: input
     - Ingress-port bitmap captured with req; bit k identifies port k.
   * - ``ack``
     - ``logic``
     - mst: input; slv: output
     - Completes the outstanding learning request; no response payload.

Architecture and operation
--------------------------

**Parameter and roles:** ``NUM_OF_INTERFACES`` defaults to 8 and sets the
width of ``port_bitmap``. Modports are ``mst`` and ``slv``.

The requester presents a 48-bit source ``mac_addr`` and its ingress
``port_bitmap`` with a one-cycle ``req`` pulse. The existing RTL
producers return ``req`` low on the following cycle and wait for ``ack``
with ``req = 0``. The requester may have one learning request outstanding.

The responder captures both payload fields on the low-to-high transition of
``req``. They need not remain stable after the request cycle. Keeping
them stable until acknowledgement is also valid. A request held through
acknowledgement is accepted as one transaction; another request requires a
new low-to-high transition. That acknowledgement refers to both payload
fields captured in the first active ``req`` cycle, even if their values
change while ``req`` stays high.

``ack`` completes the learning transaction and carries no response payload.
In particular, ``port_bitmap`` travels with the request, whereas the bitmap
on :ref:`rtl-lookup-if` travels with the response. These interfaces have
separate request and acknowledgement signals. There is no request-ready or
response-ready signal.

Clock and reset belong to the connected modules. The interface contains
signals and modports, with no clock/reset ports or internal storage.

Functional scenarios
--------------------

The examples use ``NUM_OF_INTERFACES = 8``. ``A0`` and ``A1`` denote
MAC addresses. Port bitmaps show all eight bits in port order ``[7:0]``:
``0b00000001`` selects port 0 and ``0b00000010`` selects port 1. On the
learning channel, the MAC address is a source address and the bitmap
identifies its ingress port. Address labels are local to each diagram.

``clk`` is the common clock of the connected logic, shown as a sampling
reference. Numbered cycles label intervals between rising edges; values are
sampled at each interval's ending rising edge. Shaded ``x`` regions mark
irrelevant values, not a requirement to drive unknowns. The illustrated
completion latencies depend on the responder and are not an interface
guarantee.

Learning request with source address and ingress bitmap
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In cycle 1, the requester pulses ``req`` with ``mac_addr = A0`` and
``port_bitmap = 0b00000001``. The responder captures both fields at the end of
that cycle. ``req`` returns low in cycle 2, while the requester waits for
completion. This requester keeps both payload fields stable through the
acknowledgement, although only the request cycle needs them.

In cycle 3, the responder asserts ``ack``. The requester samples that
completion at the cycle's ending rising edge and may then issue another
learning request. There is no returned MAC address or bitmap to sample
with ``ack``.

.. wavedrom::
    :name: learning-if-request-timing
    :caption: Learning request carrying source address and ingress bitmap
    :alt: A learning pulse carries A0 and 0b00000001 in cycle 1 and completes with ACK in cycle 3.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p....."},
            ["Master",
                {"name": "req", "wave": "010..."},
                {"name": "mac_addr", "wave": "x=..x.", "data": ["A0"]},
                {
                    "name": "port_bitmap",
                    "wave": "x=..x.",
                    "style": "font-size: 12px;",
                    "data": ["0b00000001"]
                }
            ],
            ["Slave", {"name": "ack", "wave": "0..10."}, {}],
            {}
        ],
        "head": {"tick": 0},
        "config": {"hscale": 2}
    }

Request held until acknowledgement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The requester raises ``req`` with ``A0`` and ``0b00000001`` in cycle 1 and
keeps it high through cycle 7. The responder captures that pair at the ending
rising edge of cycle 1, the first active request cycle.

In cycle 2, the requester changes the signals to ``A1`` and ``0b00000010``
while ``req`` is still high. There is no new low-to-high transition,
so the changes do not create another request or modify the captured
``A0/0b00000001`` payload.

The responder asserts ``ack`` in cycle 7 for the original ``A0/0b00000001``
request. It does not acknowledge the ``A1/0b00000010`` values currently on the
signals. After sampling the completion, the requester deasserts ``req``
in cycle 8. Another request requires a fresh low-to-high transition.

.. wavedrom::
    :name: learning-if-retained-payload-timing
    :caption: Held learning request acknowledged for its first-cycle payload
    :alt: Held REQ completes for A0 and bitmap 0b00000001 from cycle 1 despite later values.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p........."},
            ["Master",
                {"name": "req", "wave": "01......0."},
                {"name": "mac_addr", "wave": "x==.......", "data": ["A0", "A1"]},
                {
                    "name": "port_bitmap",
                    "wave": "x==.......",
                    "style": "font-size: 12px;",
                    "data": ["0b00000001", "0b00000010"]
                }
            ],
            ["Slave", {"name": "ack", "wave": "0......10."}, {}],
            {}
        ],
        "head": {"tick": 0},
        "config": {"hscale": 2}
    }

Independent operation alongside destination lookup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The learning and lookup channels may each have a request outstanding at the
same time. In cycle 1 below, a learning request carries source address
``A1`` and ingress bitmap ``0b00000010``, while a lookup request carries
destination address ``A0``.

The lookup completes in cycle 3 with its own ``ack`` and returned bitmap
``0b00000001``. The learning request remains outstanding until its separate
``ack`` in cycle 5. Acknowledgement on one channel does not complete the
other channel's request. The shown completion order is illustrative.

.. wavedrom::
    :name: learning-if-independent-timing
    :caption: Independent learning and lookup request/acknowledgement channels
    :alt: Both channels request in cycle 1; lookup completes in cycle 3 and learning in cycle 5.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p......"},
            ["learning_if",
                ["Master",
                    {"name": "req", "wave": "010...."},
                    {"name": "mac_addr", "wave": "x=....x", "data": ["A1"]},
                    {
                        "name": "port_bitmap",
                        "wave": "x=....x",
                        "style": "font-size: 12px;",
                        "data": ["0b00000010"]
                    }
                ],
                ["Slave", {"name": "ack", "wave": "0....10"}, {}]
            ],
            {},
            ["lookup_if",
                ["Master",
                    {"name": "req", "wave": "010...."},
                    {"name": "mac_addr", "wave": "x=..x..", "data": ["A0"]}
                ],
                ["Slave",
                    {"name": "ack", "wave": "0..10.."},
                    {
                        "name": "port_bitmap",
                        "wave": "x..=x..",
                        "style": "font-size: 12px;",
                        "data": ["0b00000001"]
                    }
                ]
            ]
        ],
        "head": {"tick": 0},
        "config": {"hscale": 2}
    }
