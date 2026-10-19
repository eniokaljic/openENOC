.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-FileCopyrightText: 2026 Kerim Bavcic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-axis-forwarding-engine:

Forwarding engine -- openenoc_axis_forwarding_engine
====================================================

.. index::
   single: openenoc_axis_forwarding_engine

Determines Ethernet forwarding destinations and learns source addresses for
received frames.

**Source:** :download:`openenoc_axis_forwarding_engine.sv <../../../hw/rtl/core/openenoc_axis_forwarding_engine.sv>`.

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
     - Port count and forwarding-bitmap width; both table interfaces use the
       same value.

Signals
-------

Interface ports contain channels in both directions. The table identifies
the selected modport or stream role; member directions follow that interface.

.. list-table:: Public signals and interfaces
   :class: rtl-reference-table
   :header-rows: 1
   :widths: 20 30 17 33

   * - Name
     - Type
     - Direction / role
     - Description
   * - ``clk``
     - ``logic``
     - input
     - Common clock for the frame stream and table interfaces.
   * - ``rst``
     - ``logic``
     - input
     - Active-high synchronous reset of parsing, requests, and buffered data.
   * - ``pause_request``
     - ``logic``
     - input
     - Requests a pause at the next frame boundary.
   * - ``pause_done``
     - ``logic``
     - output
     - Indicates active frame and output pipeline have drained for pause.
   * - ``s_axis``
     - ``taxi_axis_if.snk``
     - sink
     - Complete frame bytes; TID identifies the ingress port.
   * - ``m_axis``
     - ``taxi_axis_if.src``
     - source
     - Unchanged frame bytes; TUSER carries the egress-port bitmap.
   * - ``lookup_if``
     - ``openenoc_lookup_if.mst``
     - bidirectional (mst)
     - Destination lookup request and returned forwarding bitmap.
   * - ``learning_if``
     - ``openenoc_learning_if.mst``
     - bidirectional (mst)
     - Source-address learning request and acknowledgement.

Architecture and operation
--------------------------

The engine extracts the first six valid frame bytes as the destination MAC
and the next six as the source MAC. The first frame byte occupies the lowest
byte lane of TDATA and the most significant byte of its 48-bit MAC address.
The header stays in the frame: output data, KEEP, and LAST retain their input
values. Input TID is captured with the first accepted beat for lookup and
learning decisions, and should remain constant throughout that frame.

After accepting a complete destination address, the engine pulses
``lookup_if.req`` for one cycle and waits for its acknowledgement. Input
READY is low during this wait, and no frame data is released. The returned
bitmap is masked to remove the ingress port:
``egress_bitmap = lookup_if.port_bitmap & ~(1 << ingress_port)``.
The remaining source-address bytes are then accepted. A wide beat may
already contain the complete source address when lookup finishes.

Once all 12 address bytes are available, the engine pulses
``learning_if.req`` with the source MAC and a one-hot ingress bitmap.
It waits for ``learning_if.ack`` before making the frame available at
``m_axis``. Each request payload remains stable while its acknowledgement
is pending. The learning request is generated even if the selected output
bitmap is zero; any managed-mode learning policy belongs to the table.
The table can connect directly or through
:ref:`rtl-forwarding-table-arb-mux`.

The header buffer is a chain of two-entry AXI-Stream register slices
(skid buffers), with ``ceil(12 / KEEP_W)`` slices. It retains the accepted
prefix while table operations are pending. Once learning completes, the
buffer drains and the remaining input bytes can enter. This is streaming
storage rather than a complete-frame FIFO. Input timing, table response
latency, and output readiness determine when buffered data is available.
The next frame cannot enter until the current output TLAST is accepted.

Every output beat carries the same egress bitmap in the low
``NUM_OF_INTERFACES`` TUSER bits; any higher TUSER bits are zero.
Input TUSER is replaced, while TID and TDEST pass through with casts to
their output widths. Enabled STRB also follows the buffered data.
The egress bitmap is internal switch metadata and does not add frame bytes.
Data and metadata remain stable while output VALID is high and READY is low.

A zero egress bitmap does not suppress the output stream. The complete input
still leaves ``m_axis`` with TUSER zero; a downstream routing block decides
how to handle that bitmap. An input ending before six valid bytes produces
neither lookup nor learning. An input with a complete destination but fewer
than 12 valid bytes performs lookup but no learning. Both truncated cases
are released unchanged with a zero bitmap, without a separate error signal.

``pause_request`` blocks the first beat of a new frame at a frame boundary.
A frame already admitted continues through lookup, learning, and output.
``pause_done`` becomes high only after its output TLAST has transferred and
the header buffer and request strobes are idle. It stays high while the
request is held at that boundary. Removing ``pause_request`` permits the next
frame to enter. Reset abandons partial frames and pending operations; reset
must be coordinated with the attached table or arbiter.

Use byte-granular DATA widths from 8 through 512 bits, with
``KEEP_W = DATA_W / 8`` and matching input/output DATA, KEEP, and KEEP-enable
settings. Both streams require LAST and ID. Input ID must encode all port
indices, and output USER must be enabled and at least
``NUM_OF_INTERFACES`` bits wide. Use ingress indices in
``0 .. NUM_OF_INTERFACES - 1``. Non-final beats have all KEEP bits set;
a partial final beat uses contiguous valid low byte lanes. The parser does
not validate Ethernet length, EtherType, FCS, or sparse KEEP patterns.

Functional scenarios
--------------------

The examples use ``NUM_OF_INTERFACES = 4``, 64-bit input/output DATA,
``KEEP_W = 8``, enabled KEEP, LAST, and ID, and four output USER bits.
The engine connects directly to an unmanaged :ref:`rtl-forwarding-table`
with eight entries. Reset and initial table setup have already completed.
All interfaces share a 10 ns clock.

``A0`` and ``A1`` are distinct destination MACs, while ``A2`` and ``A3``
are their corresponding source MACs. Initial table entries map
``A0`` to ``0b1110`` and ``A1`` to ``0b0100``. Port bit ``n`` selects
port ``n``. TUSER and table-interface bitmaps show all four bits in port
order ``[3:0]``. The source presents each queued input continuously while
it is waiting for acceptance.

``FA`` uses data labels ``DA0``, ``DA1``, and subsequent beats; ``FB``
uses ``DB0``, ``DB1``, and subsequent beats. Labels stay the same at the
input and output. Each complete 66-byte Ethernet frame includes its Ethernet
header and excludes preamble, SFD, and FCS. It has eight full beats with
KEEP ``0xFF`` and one final two-byte beat with KEEP ``0x03`` and TLAST.
The deliberately truncated inputs below are not complete Ethernet frames.

A numbered tick marks a clock interval. A beat transfers at its ending
rising edge when VALID and READY are high. Requests and acknowledgements
are sampled at the same edge. ``x`` marks irrelevant payload outside an
active stream beat, request, or acknowledgement.

Destination lookup, source learning, and ingress exclusion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: Frame and forwarding decision
   :class: documentation-table
   :header-rows: 1
   :widths: 13 13 30 13 31

   * - Frame
     - Length
     - Destination / source
     - Ingress
     - Lookup / output bitmap
   * - ``FA``
     - 66 bytes
     - ``A0`` / ``A2``
     - Port 1
     - ``0b1110`` / ``0b1100``

``DA0`` transfers in tick 1 and contains all six destination bytes plus
the first two source bytes. Lookup requests ``A0`` in tick 2; its
acknowledgement in tick 4 returns ``0b1110``. Removing ingress port 1
leaves ``0b1100``. Input ``DA1`` transfers in tick 5 and completes the
source address. Learning requests ``A2/0b0010`` in tick 6 and completes
in tick 8.

Output starts in tick 9, with TUSER ``0b1100`` on every beat. ``DA0`` through
``DA8`` leave consecutively in ticks 9 through 17, while the remaining
input data enters behind the buffered prefix. The output preserves both
address fields and the final two-byte KEEP mask.

.. wavedrom::
    :name: forwarding-engine-complete-timing
    :caption: Lookup and learning complete before the unchanged frame is released
    :alt: Lookup and learning complete before the unchanged frame is released.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p..................."},
            [
                "FSM",
                {
                    "name": "state_reg",
                    "wave": "=.=..==..=........=.",
                    "data": [
                        "ST_\nPARSE_DA",
                        "ST_WAIT_LOOKUP",
                        "ST_\nPARSE_\nSA",
                        "ST_WAIT_LEARNING",
                        "ST_RELEASE",
                        "ST_PARSE_DA"
                    ],
                    "style": "font-size: 10px;"
                }
            ],
            [
                "s_axis",
                [
                    "Source",
                    {"name": "tvalid", "wave": "01..............0..."},
                    {
                        "name": "tdata",
                        "wave": "x==...=...======x...",
                        "data": ["DA0", "DA1", "DA2", "DA3", "DA4", "DA5", "DA6", "DA7", "DA8"]
                    },
                    {
                        "name": "tkeep",
                        "wave": "x=.............=x...",
                        "data": ["0xFF", "0x03"]
                    },
                    {"name": "tlast", "wave": "x0.............1x..."},
                    {"name": "tid", "wave": "x=..............x...", "data": ["1"]}
                ],
                ["Sink", {"name": "tready", "wave": "1.0..10..1......0.1."}]
            ],
            {},
            [
                "m_axis",
                [
                    "Source",
                    {"name": "tvalid", "wave": "0........1........0."},
                    {
                        "name": "tdata",
                        "wave": "x........=========x.",
                        "data": ["DA0", "DA1", "DA2", "DA3", "DA4", "DA5", "DA6", "DA7", "DA8"]
                    },
                    {
                        "name": "tkeep",
                        "wave": "x........=.......=x.",
                        "data": ["0xFF", "0x03"]
                    },
                    {"name": "tlast", "wave": "x........0.......1x."},
                    {"name": "tid", "wave": "x........=........x.", "data": ["1"]},
                    {"name": "tuser", "wave": "x........=........x.", "data": ["0b1100"]}
                ],
                ["Sink", {"name": "tready", "wave": "1..................."}]
            ],
            {},
            [
                "lookup_if",
                [
                    "Master",
                    {"name": "req", "wave": "0.10................"},
                    {
                        "name": "mac_addr",
                        "wave": "x.=..x..............",
                        "data": ["A0"]
                    }
                ],
                [
                    "Slave",
                    {"name": "ack", "wave": "0...10.............."},
                    {
                        "name": "port_bitmap",
                        "wave": "x...=x..............",
                        "style": "font-size: 10px;",
                        "data": ["0b1110"]
                    }
                ]
            ],
            {},
            [
                "learning_if",
                [
                    "Master",
                    {"name": "req", "wave": "0.....10............"},
                    {
                        "name": "mac_addr",
                        "wave": "x.....=..x..........",
                        "data": ["A2"]
                    },
                    {
                        "name": "port_bitmap",
                        "wave": "x.....=..x..........",
                        "data": ["0b0010"]
                    }
                ],
                ["Slave", {"name": "ack", "wave": "0.......10.........."}]
            ],
            {}
        ],
        "head": {"tick": 0},
        "config": {"hscale": 1}
    }

Incomplete destination and source addresses
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: Consecutive truncated inputs
   :class: documentation-table
   :header-rows: 1
   :widths: 10 12 16 40 22

   * - Input
     - Length
     - Data beats
     - Address bytes present
     - Table operations
   * - ``FA``
     - 5 bytes
     - ``DA0``
     - Incomplete destination
     - None
   * - ``FB``
     - 9 bytes
     - ``DB0``, ``DB1``
     - Complete ``A1``; incomplete source
     - Lookup only

The five-byte ``DA0`` transfers in tick 1 with KEEP ``0x1F`` and TLAST.
It leaves in tick 3 with TUSER zero, without any table request.
The next input starts with ``DB0`` in tick 4. Its complete destination
``A1`` produces the lookup pulse in tick 5 and response ``0b0100`` in tick 7.
``DB1`` then transfers in tick 8 with KEEP ``0x01`` and TLAST, before
all source bytes have arrived. Both output beats carry TUSER zero in
ticks 9 and 10, and learning remains inactive.

.. wavedrom::
    :name: forwarding-engine-short-timing
    :caption: Truncated address fields suppress learning and select a zero bitmap
    :alt: Truncated address fields suppress learning and select a zero bitmap.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p............"},
            [
                "FSM",
                {
                    "name": "state_reg",
                    "wave": "=.=.==..==.=.",
                    "data": [
                        "ST_\nPARSE_DA",
                        "ST_RELEASE",
                        "ST_\nPARSE_\nDA",
                        "ST_WAIT_LOOKUP",
                        "ST_\nPARSE_\nSA",
                        "ST_RELEASE",
                        "ST_PARSE_DA"
                    ],
                    "style": "font-size: 10px;"
                }
            ],
            [
                "s_axis",
                [
                    "Source",
                    {"name": "tvalid", "wave": "01.......0..."},
                    {
                        "name": "tdata",
                        "wave": "x==..=...x...",
                        "data": ["DA0", "DB0", "DB1"]
                    },
                    {
                        "name": "tkeep",
                        "wave": "x==..=...x...",
                        "data": ["0x1F", "0xFF", "0x01"]
                    },
                    {"name": "tlast", "wave": "x10..1...x..."},
                    {"name": "tid", "wave": "x==......x...", "data": ["1", "2"]}
                ],
                ["Sink", {"name": "tready", "wave": "1.0.10..10.1."}]
            ],
            {},
            [
                "m_axis",
                [
                    "Source",
                    {"name": "tvalid", "wave": "0..10....1.0."},
                    {
                        "name": "tdata",
                        "wave": "x..=x....==x.",
                        "data": ["DA0", "DB0", "DB1"]
                    },
                    {
                        "name": "tkeep",
                        "wave": "x..=x....==x.",
                        "data": ["0x1F", "0xFF", "0x01"]
                    },
                    {"name": "tlast", "wave": "x..1x....01x."},
                    {"name": "tid", "wave": "x..=x....=.x.", "data": ["1", "2"]},
                    {
                        "name": "tuser",
                        "wave": "x..=x....=.x.",
                        "style": "font-size: 10px;",
                        "data": ["0b0000", "0b0000"]
                    }
                ],
                ["Sink", {"name": "tready", "wave": "1............"}]
            ],
            {},
            [
                "lookup_if",
                [
                    "Master",
                    {"name": "req", "wave": "0....10......"},
                    {"name": "mac_addr", "wave": "x....=..x....", "data": ["A1"]}
                ],
                [
                    "Slave",
                    {"name": "ack", "wave": "0......10...."},
                    {"name": "port_bitmap", "wave": "x......=x....", "style": "font-size: 10px;", "data": ["0b0100"]}
                ]
            ],
            {},
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
            {}
        ],
        "head": {"tick": 0},
        "config": {"hscale": 1}
    }

Frame-boundary pause, drain, and resume
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: Frames queued before the pause request
   :class: documentation-table
   :header-rows: 1
   :widths: 13 13 30 13 31

   * - Frame
     - Length
     - Destination / source
     - Ingress
     - Lookup / output bitmap
   * - ``FA``
     - 66 bytes
     - ``A0`` / ``A2``
     - Port 1
     - ``0b1110`` / ``0b1100``
   * - ``FB``
     - 66 bytes
     - ``A1`` / ``A3``
     - Port 2
     - ``0b0100`` / ``0b0000``

``pause_request`` rises in tick 12 while FA is in progress. The engine
continues accepting its remaining beats; ``DA8`` enters in tick 15.
Although ``DB0`` is already offered from tick 16, it cannot enter yet.
Output READY is low in ticks 17 through 20, holding the final ``DA8``
beat with KEEP ``0x03``, TLAST, and TUSER ``0b1100`` unchanged. ``pause_done``
stays low until this beat transfers in tick 21, then rises in tick 22.
The two diagrams show consecutive clock intervals.

.. wavedrom::
    :name: forwarding-engine-pause-start-timing
    :caption: Pause waits for the final output handshake before completing
    :alt: Pause waits for the final output handshake before completing.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p........................."},
            [
                "FSM",
                {
                    "name": "state_reg",
                    "wave": "=.=..==..=............=...",
                    "data": [
                        "ST_\nPARSE_DA",
                        "ST_WAIT_LOOKUP",
                        "ST_\nPARSE_\nSA",
                        "ST_WAIT_LEARNING",
                        "ST_RELEASE",
                        "ST_PARSE_DA"
                    ],
                    "style": "font-size: 10px;"
                }
            ],
            {"name": "pause_request", "wave": "0...........1............."},
            {"name": "pause_done", "wave": "0.....................1..."},
            [
                "s_axis",
                [
                    "Source",
                    {"name": "tvalid", "wave": "01........................"},
                    {
                        "name": "tdata",
                        "wave": "x==...=...=======.........",
                        "data": [
                            "DA0",
                            "DA1",
                            "DA2",
                            "DA3",
                            "DA4",
                            "DA5",
                            "DA6",
                            "DA7",
                            "DA8",
                            "DB0"
                        ]
                    },
                    {
                        "name": "tkeep",
                        "wave": "x=.............==.........",
                        "data": ["0xFF", "0x03", "0xFF"]
                    },
                    {"name": "tlast", "wave": "x0.............10........."},
                    {
                        "name": "tid",
                        "wave": "x=..............=.........",
                        "data": ["1", "2"]
                    }
                ],
                ["Sink", {"name": "tready", "wave": "1.0..10..1......0........."}]
            ],
            {},
            [
                "m_axis",
                [
                    "Source",
                    {"name": "tvalid", "wave": "0........1............0..."},
                    {
                        "name": "tdata",
                        "wave": "x........=========....x...",
                        "data": ["DA0", "DA1", "DA2", "DA3", "DA4", "DA5", "DA6", "DA7", "DA8"]
                    },
                    {
                        "name": "tkeep",
                        "wave": "x........=.......=....x...",
                        "data": ["0xFF", "0x03"]
                    },
                    {"name": "tlast", "wave": "x........0.......1....x..."},
                    {
                        "name": "tid",
                        "wave": "x........=............x...",
                        "data": ["1"]
                    },
                    {
                        "name": "tuser",
                        "wave": "x........=............x...",
                        "data": ["0b1100"]
                    }
                ],
                ["Sink", {"name": "tready", "wave": "1................0...1...."}]
            ],
            {},
            [
                "lookup_if",
                [
                    "Master",
                    {"name": "req", "wave": "0.10......................"},
                    {
                        "name": "mac_addr",
                        "wave": "x.=..x....................",
                        "data": ["A0"]
                    }
                ],
                [
                    "Slave",
                    {"name": "ack", "wave": "0...10...................."},
                    {
                        "name": "port_bitmap",
                        "wave": "x...=x....................",
                        "style": "font-size: 10px;",
                        "data": ["0b1110"]
                    }
                ]
            ],
            {},
            [
                "learning_if",
                [
                    "Master",
                    {"name": "req", "wave": "0.....10.................."},
                    {
                        "name": "mac_addr",
                        "wave": "x.....=..x................",
                        "data": ["A2"]
                    },
                    {
                        "name": "port_bitmap",
                        "wave": "x.....=..x................",
                        "data": ["0b0010"]
                    }
                ],
                ["Slave", {"name": "ack", "wave": "0.......10................"}]
            ],
            {}
        ],
        "head": {"tick": 0},
        "config": {"hscale": 1}
    }

With ``pause_request`` still high, ``pause_done`` remains high and
``DB0`` remains pending. Removing the request in tick 31 permits that
beat to transfer. Lookup for ``A1`` runs from the request in tick 32
to acknowledgement in tick 34; learning ``A3/0b0100`` runs from tick 36
to tick 38. Output FB then occupies ticks 39 through 47.

The lookup bitmap ``0b0100`` contains only FB's ingress port. Excluding it
leaves zero, but source learning still completes and every frame beat
is emitted with TUSER zero. Its final ``DB8`` transfers once, in tick 47,
with KEEP ``0x03`` and TLAST.

.. wavedrom::
    :name: forwarding-engine-pause-resume-timing
    :caption: The next frame resumes after pause and retains its zero egress bitmap
    :alt: The next frame resumes after pause and retains its zero egress bitmap.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p........................"},
            [
                "FSM",
                {
                    "name": "state_reg",
                    "wave": "=.....=..==..=........=..",
                    "data": [
                        "ST_PARSE_DA",
                        "ST_WAIT_LOOKUP",
                        "ST_\nPARSE_\nSA",
                        "ST_WAIT_LEARNING",
                        "ST_RELEASE",
                        "ST_PARSE_DA"
                    ],
                    "style": "font-size: 10px;"
                }
            ],
            {"name": "pause_request", "wave": "1....0..................."},
            {"name": "pause_done", "wave": "1....0..................."},
            [
                "s_axis",
                [
                    "Source",
                    {"name": "tvalid", "wave": "1...................0...."},
                    {
                        "name": "tdata",
                        "wave": "=.....=...=...======x....",
                        "data": ["DB0", "DB1", "DB2", "DB3", "DB4", "DB5", "DB6", "DB7", "DB8"]
                    },
                    {
                        "name": "tkeep",
                        "wave": "=..................=x....",
                        "data": ["0xFF", "0x03"]
                    },
                    {"name": "tlast", "wave": "0..................1x...."},
                    {"name": "tid", "wave": "=...................x....", "data": ["2"]}
                ],
                ["Sink", {"name": "tready", "wave": "0....10..10..1......0.1.."}]
            ],
            {},
            [
                "m_axis",
                [
                    "Source",
                    {"name": "tvalid", "wave": "0............1........0.."},
                    {
                        "name": "tdata",
                        "wave": "x............=========x..",
                        "data": ["DB0", "DB1", "DB2", "DB3", "DB4", "DB5", "DB6", "DB7", "DB8"]
                    },
                    {
                        "name": "tkeep",
                        "wave": "x............=.......=x..",
                        "data": ["0xFF", "0x03"]
                    },
                    {"name": "tlast", "wave": "x............0.......1x.."},
                    {"name": "tid", "wave": "x............=........x..", "data": ["2"]},
                    {
                        "name": "tuser",
                        "wave": "x............=........x..",
                        "data": ["0b0000"]
                    }
                ],
                ["Sink", {"name": "tready", "wave": "1........................"}]
            ],
            {},
            [
                "lookup_if",
                [
                    "Master",
                    {"name": "req", "wave": "0.....10................."},
                    {
                        "name": "mac_addr",
                        "wave": "x.....=..x...............",
                        "data": ["A1"]
                    }
                ],
                [
                    "Slave",
                    {"name": "ack", "wave": "0.......10..............."},
                    {
                        "name": "port_bitmap",
                        "wave": "x.......=x...............",
                        "style": "font-size: 10px;",
                        "data": ["0b0100"]
                    }
                ]
            ],
            {},
            [
                "learning_if",
                [
                    "Master",
                    {"name": "req", "wave": "0.........10............."},
                    {
                        "name": "mac_addr",
                        "wave": "x.........=..x...........",
                        "data": ["A3"]
                    },
                    {
                        "name": "port_bitmap",
                        "wave": "x.........=..x...........",
                        "data": ["0b0100"]
                    }
                ],
                ["Slave", {"name": "ack", "wave": "0...........10..........."}]
            ],
            {}
        ],
        "head": {"tick": 26},
        "config": {"hscale": 1}
    }

.. _verification-openenoc-axis-forwarding-engine:

Verification
------------

The test suite is in ``dv/core/openenoc_axis_forwarding_engine/``.

Testbench
~~~~~~~~~

This test suite validates the ``openenoc_axis_forwarding_engine`` module, which parses the
destination and source MAC addresses from each AXI Stream frame and connects the stream data
path to the lookup and learning interfaces of the openENOC forwarding table.

The forwarding table is not instantiated. Its lookup and learning interfaces are driven by a
behavioral model in the Python testbench so that the forwarding engine can be verified
stand-alone.

The engine starts a lookup as soon as the six-byte destination MAC address is complete.
Source-address learning starts only after the destination lookup has been acknowledged and the
complete six-byte source MAC address has arrived. If the source MAC is already present in a wide
input beat, learning starts as soon as the lookup completes; otherwise, the engine resumes
parsing until the source MAC is complete and then issues the learning request. Destination
lookup and source-address learning both apply backpressure as needed, and the buffered frame is
released only after all forwarding-table transactions associated with its header have been
acknowledged. This ordering prevents the next frame from starting a new lookup while learning
for the current frame is still pending on the table's shared internal arbitration path.

The lookup result is attached to the released frame on ``m_axis.tuser``. The ingress interface
index is carried on ``s_axis.tid`` and is removed from the egress bitmap to prevent forwarding a
frame back to its source interface.

AXI Stream Input Contract
~~~~~~~~~~~~~~~~~~~~~~~~~

The MAC parser expects canonical packet-oriented ``tkeep`` usage:

- Every beat except the final beat of a frame must have all byte lanes valid.

- On the final beat (``tlast = 1``), valid bytes must be contiguous from the least-significant
  byte lane. Gaps in ``tkeep`` are not supported.

- When ``KEEP_EN`` is disabled, every byte lane is treated as valid.

The byte-counting and MAC-address extraction logic relies on this contract. Frames with sparse
``tkeep``, or with invalid lanes before valid lanes, are outside the supported input format.

Forwarding Table Model
~~~~~~~~~~~~~~~~~~~~~~

The testbench implements the openENOC request/acknowledge handshake. The engine asserts
``lookup_if.req`` or ``learning_if.req`` for one clock cycle and keeps the associated payload
stable while it waits. The model returns a single-cycle acknowledge after a configurable
latency. During each wait, the testbench checks that the input is stalled and no buffered output
beat is released.

Known destination MAC addresses are resolved using the model's entry map. A lookup miss returns
the configured default forwarding bitmap. Every accepted lookup and learning request is recorded
and checked for correct ordering and contents.

Coverage
~~~~~~~~

**Functional checks:**

- Destination and source MAC extraction across different AXI Stream widths

- Lookup hit and miss handling

- Ingress interface removal from the forwarding bitmap

- Correct learning MAC address and one-hot ingress interface bitmap

- Frame payload integrity and ``tid``/``tdest`` pass-through

- Forwarding bitmap alignment on ``m_axis.tuser``

- Zero forwarding bitmap with no lookup or learning for incomplete 1-5 byte destination addresses

- Zero forwarding bitmap and no learning for incomplete 6-11 byte headers

- Input stalling while lookup and learning acknowledgements are pending

- Stable request payloads throughout configurable acknowledgement latency

**Directed scenarios:**

- ``test_incomplete_destination_address_sets_zero_bitmap``: frames ending before the complete
  six-byte destination address are released with ``tuser = 0`` and do not generate lookup or
  learning requests.

- ``test_incomplete_source_address_sets_zero_bitmap``: frames containing a complete six-byte
  destination address but an incomplete source address are released with ``tuser = 0`` and do not
  generate learning requests.

**Scenarios (TestFactory):**

- Back-to-back frames with known and unknown destination MAC addresses

- Frame lengths of 32, 60, 79, and 128 bytes

- Idle insertion and output backpressure combinations

- Lookup and learning acknowledgement latencies of 2, 4, and 256 cycles

**Parameter sweep (pytest):**

- ``DATA_W`` in {8, 16, 24, 64, 128, 512}
