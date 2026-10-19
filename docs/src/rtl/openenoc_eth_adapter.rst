.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-eth-adapter:

Ethernet clock/width adapter -- openenoc_eth_adapter
====================================================

.. index::
   single: openenoc_eth_adapter

Bridges bidirectional Ethernet-like streams across clock domains and stream
widths.

**Source:** :download:`openenoc_eth_adapter.sv <../../../hw/rtl/core/openenoc_eth_adapter.sv>`.

Parameters
----------

The table describes the Ethernet profile, with byte-granular KEEP, frame
termination enabled, and no active stream ID, destination, or user metadata.

.. list-table:: Parameters
   :class: rtl-reference-table
   :header-rows: 1
   :widths: 26 18 22 34

   * - Name
     - Default value
     - Allowed values
     - Description
   * - ``DEPTH``
     - ``4096``
     - At least two beats at the wider link width
     - Capacity passed to TAXI; counts bytes with enabled KEEP and eight-bit lanes,
       otherwise whole stream words. Account for the wider side.
   * - ``RAM_PIPELINE``
     - ``1``
     - Integer >= 0
     - RAM pipeline register count in each asynchronous FIFO adapter.
   * - ``OUTPUT_FIFO_EN``
     - ``1'b0``
     - 0 or 1
     - Enables the FIFO adapter output FIFO.
   * - ``FRAME_FIFO``
     - ``1'b0``
     - 0 or 1
     - Holds complete frames before making them available at the output.
   * - ``DROP_OVERSIZE_FRAME``
     - ``FRAME_FIFO``
     - 0 or 1; requires FRAME_FIFO
     - Drops frames that exceed the frame FIFO capacity.
   * - ``DROP_WHEN_FULL``
     - ``1'b0``
     - 0 or 1; requires frame buffering and oversize dropping
     - Discards arriving frames instead of backpressuring when full.
   * - ``FRAME_PAUSE``
     - ``FRAME_FIFO``
     - 0 or 1
     - Frame-boundary pause policy; inactive because this wrapper has no pause
       requests and leaves TAXI PAUSE_EN disabled.

The generic TAXI marker options remain in the source declaration:
``USER_BAD_FRAME_VALUE = 1'b1``, ``USER_BAD_FRAME_MASK = 1'b1``,
``DROP_BAD_FRAME = 1'b0``, and ``MARK_WHEN_FULL = 1'b0``.
Marker-based dropping or overflow marking requires an enabled USER field;
keep both policies disabled for Ethernet links.

Signals
-------

Interface ports contain channels in both directions. The table identifies
the selected modport or stream role; member directions follow that interface.

.. list-table:: Public signals and interfaces
   :class: rtl-reference-table
   :header-rows: 1
   :widths: 12 22 17 49

   * - Name
     - Type
     - Direction / role
     - Description
   * - ``eth_a``
     - ``openenoc_eth_if``
     - bidirectional; A clock domain
     - Receives A-to-B frames and transmits B-to-A frames using this link's clock/reset.
   * - ``eth_b``
     - ``openenoc_eth_if``
     - bidirectional; B clock domain
     - Transmits A-to-B frames and receives B-to-A frames using this link's clock/reset.

.. list-table:: Stream roles relative to the adapter
   :class: rtl-reference-table
   :header-rows: 1
   :widths: 34 33 33

   * - Embedded stream
     - Adapter role
     - Clock/reset
   * - ``eth_a.a2b_axis_if``
     - Sink
     - ``eth_a.clk/rst``
   * - ``eth_b.a2b_axis_if``
     - Source
     - ``eth_b.clk/rst``
   * - ``eth_b.b2a_axis_if``
     - Sink
     - ``eth_b.clk/rst``
   * - ``eth_a.b2a_axis_if``
     - Source
     - ``eth_a.clk/rst``

Each stream uses ``tdata``, ``tkeep``, ``tlast``, ``tvalid``, and
``tready`` as described in :ref:`rtl-eth-if`. Widths follow the containing
link; READY travels in the opposite direction to frame data.

Architecture and operation
--------------------------

.. index::
   single: Asynchronous FIFO

The adapter connects ``eth_a`` and ``eth_b`` using one TAXI asynchronous FIFO
adapter per direction. The links provide their own ``clk/rst`` and AXIS widths.
The A-to-B path preserves ``a2b_axis_if`` orientation; the B-to-A path preserves
``b2a_axis_if`` orientation. Local TAXI interfaces bridge nested link interfaces
for tool compatibility.

``DEPTH``, ``RAM_PIPELINE``, and ``OUTPUT_FIFO_EN`` configure buffering.
``FRAME_FIFO`` and the drop options select frame policy. Defaults allow
streaming rather than requiring a whole frame before forwarding.
Each direction has its own storage and flow control; backpressure does not
propagate into the opposite-direction FIFO.

For enabled KEEP with eight-bit lanes, ``DEPTH`` counts bytes. Internally the
FIFO stores the wider side's beats and rounds the cycle count up to a power
of two. The depth must therefore leave usable storage at that width. Link
widths must have an integer ratio for width adaptation. ``FRAME_FIFO = 0``
with all drop/mark policies clear permits a frame larger than the FIFO to
progress through backpressure as its receiver consumes bytes. This generic
adapter does not impose the endpoint oETP engine's frame-size ceiling.

Width conversion keeps byte order and frame boundaries. Widening gathers
successive narrow beats into the low, then high lanes of a wide beat.
Narrowing emits the low lanes first. A partial final beat is released on
TLAST without waiting for more bytes; KEEP identifies its valid lanes.

With ``FRAME_FIFO = 1``, a frame that fits in the FIFO is made visible to
the receiving clock domain only after its final input beat is accepted.
The default ``DROP_OVERSIZE_FRAME = 1`` discards an oversized frame.
If oversize dropping is disabled, TAXI can release an oversized frame in
pieces to make progress; size the FIFO for the largest frame when whole-frame
buffering is required. Pause requests are not exposed by this wrapper, so
``FRAME_PAUSE`` has no active pause request to control.

Reset flushes queued data and interrupts in-flight frames. For a clean restart,
coordinate reset with the attached sources and sinks in both link domains.
The opposite-domain reset is synchronized through four release stages in
each local domain. Keep both clocks running during release and restart frame
transmission through the ordinary READY handshake. There is no replay of
frames interrupted by reset.

Functional scenarios
--------------------

The examples use a 66-byte Ethernet frame, counted from Destination MAC
through the final payload byte and excluding preamble, SFD, and FCS.
``DA0``, ``DA1``, ... identify successive four-byte portions of an A-to-B
frame; ``DB0``, ``DB1``, ... identify the reverse frame. Word 16 contains
only the last two bytes. A packed label such as ``DA0/1`` means ``DA0``
in bits 31:0 and ``DA1`` in bits 63:32. Labels retain the same meaning
throughout a scenario and its continuation.

KEEP width follows each link's DATA width:

.. list-table:: Byte lanes in the examples
   :class: documentation-table
   :header-rows: 1
   :widths: 25 25 25 25

   * - DATA width
     - KEEP width
     - Full-beat mask
     - Final two-byte mask
   * - 32 bits
     - 4 bits
     - ``0xF``
     - ``0x3``
   * - 64 bits
     - 8 bits
     - ``0xFF``
     - ``0x03``

Both links use ``KEEP_EN = 1`` and ``LAST_EN = 1``. All scenarios use
``RAM_PIPELINE = 1``, ``OUTPUT_FIFO_EN = 0``, and disabled bad-frame,
overflow-marking, and drop-when-full policies. Resets have already been
released, and the links are otherwise idle.
A transfer occurs at the ending rising edge of its own link-clock interval
when VALID and READY are both high. ``x`` denotes irrelevant values while
VALID is low. Tick labels count 10 ns intervals; a 20 ns B-clock cycle
spans two of these intervals.

Concurrent widening and narrowing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use ``eth_a.DATA_W = 32``, ``eth_b.DATA_W = 64``, ``DEPTH = 128``,
and ``FRAME_FIFO = 0``. The A clock period is 10 ns and the B clock
period is 20 ns. Both sources send their 66-byte frames concurrently,
and both receivers remain ready.

The A-to-B path accepts 16 full four-byte beats followed by ``DA16``
with KEEP ``0x3`` and TLAST. It packs each successive pair into a full
64-bit word with KEEP ``0xFF``. The final word carries only ``DA16``;
KEEP ``0x03`` invalidates its six unused byte lanes. TLAST releases this
partial word without waiting for another narrow beat.
Forwarding begins while the source is still sending the frame: streaming
mode exposes available FIFO words after they cross the clock domain.

.. wavedrom::
    :name: eth-adapter-widen-timing
    :caption: A 66-byte frame widens from 32 to 64 bits across clock domains
    :alt: DA0 through DA16 become eight complete 64-bit words and a final two-byte word.
    :align: center

    {
        "signal": [
            {"name": "eth_a.clk", "wave": "p..............................."},
            ["eth_a",
                ["a2b_axis_if",
                    ["A",
                        {"name": "tvalid", "wave": "0.1................0............"},
                        {
                            "name": "tdata",
                            "wave": "x.=================x............",
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
                                "DA9",
                                "DA10",
                                "DA11",
                                "DA12",
                                "DA13",
                                "DA14",
                                "DA15",
                                "DA16"
                            ]
                        },
                        {
                            "name": "tkeep",
                            "wave": "x.=...............=x............",
                            "data": ["0xF", "0x3"]
                        },
                        {"name": "tlast", "wave": "x.0...............1x............"}
                    ],
                    ["B", {"name": "tready", "wave": "1..............................."}]
                ]
            ],
            {},
            {"name": "eth_b.clk", "wave": "p...............", "period": 2},
            ["eth_b",
                ["a2b_axis_if",
                    ["A",
                        {"name": "tvalid", "wave": "0.....1........0", "period": 2},
                        {
                            "name": "tdata",
                            "wave": "x.....=========x",
                            "data": [
                                "DA0/1",
                                "DA2/3",
                                "DA4/5",
                                "DA6/7",
                                "DA8/9",
                                "DA10/11",
                                "DA12/13",
                                "DA14/15",
                                "DA16"
                            ],
                            "period": 2
                        },
                        {
                            "name": "tkeep",
                            "wave": "x.....=.......=x",
                            "data": ["0xFF", "0x03"],
                            "period": 2
                        },
                        {"name": "tlast", "wave": "x.....0.......1x", "period": 2}
                    ],
                    ["B", {"name": "tready", "wave": "1...............", "period": 2}]
                ]
            ]
        ],
        "config": {"hscale": 1},
        "head": {"tick": 0}
    }

The reverse path accepts eight full 64-bit beats and one final beat with
KEEP ``0x03``. It emits the low 32-bit portion of each full beat first,
then its high portion. Thus ``DB0/1`` becomes ``DB0``, then ``DB1``.
The final partial wide word produces only ``DB16`` with KEEP ``0x3``
and TLAST; it produces no empty upper-half beat. The two directions
preserve their own byte ordering and frame boundaries independently.

.. wavedrom::
    :name: eth-adapter-narrow-timing
    :caption: The concurrent reverse frame narrows from 64 to 32 bits
    :alt: The reverse 66-byte frame retains its bytes and ends at DB16 without an empty extra beat.
    :align: center

    {
        "signal": [
            {"name": "eth_b.clk", "wave": "p.............", "period": 2},
            ["eth_b",
                ["b2a_axis_if",
                    ["B",
                        {"name": "tvalid", "wave": "01........0...", "period": 2},
                        {
                            "name": "tdata",
                            "wave": "x=========x...",
                            "data": [
                                "DB0/1",
                                "DB2/3",
                                "DB4/5",
                                "DB6/7",
                                "DB8/9",
                                "DB10/11",
                                "DB12/13",
                                "DB14/15",
                                "DB16"
                            ],
                            "period": 2
                        },
                        {
                            "name": "tkeep",
                            "wave": "x=.......=x...",
                            "data": ["0xFF", "0x03"],
                            "period": 2
                        },
                        {"name": "tlast", "wave": "x0.......1x...", "period": 2}
                    ],
                    ["A", {"name": "tready", "wave": "1.............", "period": 2}]
                ]
            ],
            {},
            {"name": "eth_a.clk", "wave": "p..........................."},
            ["eth_a",
                ["b2a_axis_if",
                    ["B",
                        {"name": "tvalid", "wave": "0........1................0."},
                        {
                            "name": "tdata",
                            "wave": "x........=================x.",
                            "data": [
                                "DB0",
                                "DB1",
                                "DB2",
                                "DB3",
                                "DB4",
                                "DB5",
                                "DB6",
                                "DB7",
                                "DB8",
                                "DB9",
                                "DB10",
                                "DB11",
                                "DB12",
                                "DB13",
                                "DB14",
                                "DB15",
                                "DB16"
                            ]
                        },
                        {
                            "name": "tkeep",
                            "wave": "x........=...............=x.",
                            "data": ["0xF", "0x3"]
                        },
                        {"name": "tlast", "wave": "x........0...............1x."}
                    ],
                    ["A", {"name": "tready", "wave": "1..........................."}]
                ]
            ]
        ],
        "config": {"hscale": 1},
        "head": {"tick": 0}
    }

Whole-frame buffering waits for commit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use 32-bit A and 64-bit B links, with clock periods of 10 ns and
20 ns, ``DEPTH = 128``, and ``FRAME_FIFO = 1``. Keep
``DROP_OVERSIZE_FRAME = 1`` and the other drop/mark policies disabled.
The frame occupies nine 64-bit FIFO locations, including its partial
last word, and fits within the 16 locations provided by this configuration.

The destination remains invalid while all 66 input bytes are accepted.
The final ``DA16`` with KEEP ``0x3`` and TLAST flushes the partial
packed word and commits the frame. The committed boundary then crosses
to the B domain before FIFO reads make the frame available.

.. wavedrom::
    :name: eth-adapter-frame-commit-timing
    :caption: Frame buffering accepts the complete frame before release
    :alt: All 66 bytes enter the FIFO while the destination stream remains invalid.
    :align: center

    {
        "signal": [
            {"name": "eth_a.clk", "wave": "p........................."},
            ["eth_a",
                ["a2b_axis_if",
                    ["A",
                        {"name": "tvalid", "wave": "0.1................0......"},
                        {
                            "name": "tdata",
                            "wave": "x.=================x......",
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
                                "DA9",
                                "DA10",
                                "DA11",
                                "DA12",
                                "DA13",
                                "DA14",
                                "DA15",
                                "DA16"
                            ]
                        },
                        {
                            "name": "tkeep",
                            "wave": "x.=...............=x......",
                            "data": ["0xF", "0x3"]
                        },
                        {"name": "tlast", "wave": "x.0...............1x......"}
                    ],
                    ["B", {"name": "tready", "wave": "1........................."}]
                ]
            ],
            {},
            {"name": "eth_b.clk", "wave": "p............", "period": 2},
            ["eth_b",
                ["a2b_axis_if",
                    ["A",
                        {"name": "tvalid", "wave": "0............", "period": 2},
                        {"name": "tdata", "wave": "x............", "period": 2},
                        {"name": "tkeep", "wave": "x............", "period": 2},
                        {"name": "tlast", "wave": "x............", "period": 2}
                    ],
                    ["B", {"name": "tready", "wave": "1............", "period": 2}]
                ]
            ]
        ],
        "config": {"hscale": 1},
        "head": {"tick": 0}
    }

Nine consecutive B-clock transfers deliver the complete frame, ending
with KEEP ``0x03`` and TLAST. With the receiver ready and the complete
frame buffered, output VALID stays asserted through its final beat.
The adapter changes packing and delivery timing while preserving the
66 frame bytes.

.. wavedrom::
    :name: eth-adapter-frame-release-timing
    :caption: The committed frame crosses to the receiving clock domain
    :alt: After commit synchronization, nine 64-bit beats deliver the same 66-byte frame.
    :align: center

    {
        "signal": [
            {"name": "eth_a.clk", "wave": "p......................."},
            ["eth_a",
                ["a2b_axis_if",
                    ["A",
                        {"name": "tvalid", "wave": "0......................."},
                        {"name": "tdata", "wave": "x......................."},
                        {"name": "tkeep", "wave": "x......................."},
                        {"name": "tlast", "wave": "x......................."}
                    ],
                    ["B", {"name": "tready", "wave": "1......................."}]
                ]
            ],
            {},
            {"name": "eth_b.clk", "wave": "p...........", "period": 2},
            ["eth_b",
                ["a2b_axis_if",
                    ["A",
                        {"name": "tvalid", "wave": "0.1........0", "period": 2},
                        {
                            "name": "tdata",
                            "wave": "x.=========x",
                            "data": [
                                "DA0/1",
                                "DA2/3",
                                "DA4/5",
                                "DA6/7",
                                "DA8/9",
                                "DA10/11",
                                "DA12/13",
                                "DA14/15",
                                "DA16"
                            ],
                            "period": 2
                        },
                        {
                            "name": "tkeep",
                            "wave": "x.=.......=x",
                            "data": ["0xFF", "0x03"],
                            "period": 2
                        },
                        {"name": "tlast", "wave": "x.0.......1x", "period": 2}
                    ],
                    ["B", {"name": "tready", "wave": "1...........", "period": 2}]
                ]
            ]
        ],
        "config": {"hscale": 1},
        "head": {"tick": 26}
    }

.. _verification-openenoc-eth-adapter:

Verification
------------

The test suite is in ``dv/core/openenoc_eth_adapter/``.

Testbench
~~~~~~~~~

This cocotb suite verifies bidirectional Ethernet adaptation using independently clocked stream
fixtures. Pytest sweeps asymmetric pairs from widths 8, 16, 32, 64, 128, 256, and 512 bits. The
default waveform configuration uses 8/512-bit streams. The fixture uses two widest-side storage
beats and streaming FIFO policy.

Coverage
~~~~~~~~

The suite covers:

- A-to-B and B-to-A frame preservation with width conversion and clock-domain crossing;

- source idle insertion, sink backpressure, and TID/TDEST/TUSER preservation;

- simultaneous traffic without cross-direction corruption;

- initial sink pauses in each direction;

- directed frame lengths 20, 21, 31, 32, 33, 63, 64, 65, 127, 128, 129, 255, 256, 257, 511, and
  512 bytes;

- bidirectional stress with 30 random 20–256-byte frames and two 9000-byte jumbo frames.
