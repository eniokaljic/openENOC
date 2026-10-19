.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-FileCopyrightText: 2026 Kerim Bavcic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-axis-demux:

Stream demultiplexer -- openenoc_axis_demux
===========================================

.. index::
   single: openenoc_axis_demux

Routes or replicates each incoming stream frame to selected output paths.

**Source:** :download:`openenoc_axis_demux.sv <../../../hw/rtl/core/openenoc_axis_demux.sv>`.

Parameters
----------

.. list-table:: Parameters
   :class: rtl-reference-table
   :header-rows: 1
   :widths: 24 18 22 36

   * - Name
     - Default value
     - Allowed values
     - Description
   * - ``M_COUNT``
     - ``4``
     - Integer >= 1
     - Number of output streams; route metadata must represent every output.
   * - ``TID_ROUTE``
     - ``1'b0``
     - 0 or 1; exclusive routing selection
     - Routes by the most significant ID bits; requires enabled ID on both
       sides with enough input index bits.
   * - ``TDEST_ROUTE``
     - ``1'b0``
     - 0 or 1; exclusive routing selection
     - Routes by the most significant DEST bits; requires enabled DEST on
       both sides with enough input index bits.
   * - ``TUSER_BITMAP_ROUTE``
     - ``1'b0``
     - 0 or 1; exclusive routing selection
     - Routes to the low M_COUNT USER bits; requires enabled USER on both
       sides and USER width >= M_COUNT. Zero selects frame discard.

Signals
-------

Interface ports contain channels in both directions. The table identifies
the selected modport or stream role; member directions follow that interface.

.. list-table:: Public signals and interfaces
   :class: rtl-reference-table
   :header-rows: 1
   :widths: 24 26 17 33

   * - Name
     - Type
     - Direction / role
     - Description
   * - ``clk``
     - ``logic``
     - input
     - Common clock for the input, output streams, and control.
   * - ``rst``
     - ``logic``
     - input
     - Active-high synchronous reset of frame control and buffered data.
   * - ``s_axis``
     - ``taxi_axis_if.snk``
     - sink
     - Incoming frame bytes and routing metadata.
   * - ``m_axis[M_COUNT]``
     - ``taxi_axis_if.src``
     - source
     - Routed or replicated frame bytes and metadata.
   * - ``enable``
     - ``logic``
     - input
     - Gates input READY on every beat, including within a frame. Already
       buffered output data can drain while enable is low.
   * - ``drop``
     - ``logic``
     - input
     - In explicit mode, captures frame discard with the first accepted
       beat. Ignored when a metadata-routing option is enabled.
   * - ``select``
     - ``logic [$clog2(M_COUNT)-1:0]``
     - input
     - In explicit mode, output index captured with the first accepted
       beat. Ignored when a metadata-routing option is enabled.

Architecture and operation
--------------------------

One ``s_axis`` feeds ``M_COUNT`` output streams. At the first input
VALID/READY handshake of each frame, the block captures either one output
index or a multicast bitmap, together with the decision to discard that
frame. The decision remains in force through the accepted input TLAST.
Changes to ``select``, ``drop``, or routing metadata after the first accepted
beat do not redirect the remainder of that frame.

Let ``C = $clog2(M_COUNT)``. Routing options are mutually exclusive:

.. list-table:: Route selection
   :class: documentation-table
   :header-rows: 1
   :widths: 28 44 28

   * - Mode
     - Field sampled with the first accepted beat
     - Discard condition
   * - All routing options zero
     - Explicit ``select`` input
     - ``drop = 1`` or select >= M_COUNT
   * - ``TID_ROUTE = 1``
     - Most significant C bits of input TID
     - Index >= M_COUNT
   * - ``TDEST_ROUTE = 1``
     - Most significant C bits of input TDEST
     - Index >= M_COUNT
   * - ``TUSER_BITMAP_ROUTE = 1``
     - Low M_COUNT bits of input TUSER; bit n selects output n
     - Low M_COUNT bits are zero

``drop`` and ``select`` apply only in explicit mode. Metadata-routing modes
ignore both controls. For a single output, ID/DEST routing selects output
zero. With a non-power-of-two output count, unused encoded indices select
discard. A discarded frame is accepted through its input TLAST without
creating output beats. It does not cancel earlier buffered output data.

``enable`` gates input READY throughout a frame, rather than only at its
start. Deasserting it pauses input acceptance while preserving the captured
route or discard decision. Output data already accepted into the block can
continue draining. The next frame takes a fresh routing decision after the
current input TLAST; it can enter while that frame's output tail is still
buffered.

The output path implements a two-entry AXI-Stream register slice
(skid buffer). It stores the output mask alongside each beat, so buffered
beats retain their routing decisions across input frame boundaries. With
ready outputs and uninterrupted input, a beat appears at the output in the
clock interval after its input handshake, and one beat per cycle can follow.
Input READY is registered before the combinational ``enable`` gate.

Multicast copies of a beat transfer together. The implementation asserts
output VALID only when every selected output is READY. If one selected
output is not ready, VALID is low on all selected outputs, even when other
selected outputs are ready. The pending beat stays buffered, and input
stops when the available storage fills. Unselected outputs remain invalid
and their READY values do not block the selected transfer. Consumers must
assert READY independently of VALID to allow this readiness-qualified output
to progress. This behavior also applies to the single selected output in
unicast modes.

DATA, KEEP, LAST, and enabled STRB pass through without adding or removing
frame bytes. Enabled TUSER passes through on each beat; the captured route
does not replace its value. TID and TDEST are cast to the output widths,
preserving the low output-width bits. The routing bits are not separately
stripped: if an output metadata field is as wide as the input field, it
retains those bits as well. TUSER bitmap routing consumes a bitmap already
prepared by the forwarding engine; this block does not remove the ingress
port from it.

Use matching DATA widths and stream settings across all output interfaces.
KEEP widths must agree with the input when KEEP is enabled. Frame operation
requires TLAST. ID/DEST routing requires the selected metadata field to be
enabled on both sides, with at least C input bits. Bitmap routing similarly
requires enabled USER and at least M_COUNT input USER bits. Reset clears
the captured frame decision, READY state, and both buffered beats; partial
frames are abandoned.

Functional scenarios
--------------------

All examples use ``M_COUNT = 4``, 64-bit input/output DATA, ``KEEP_W = 8``,
and enabled KEEP and LAST. Input and output share a 10 ns clock, and reset
has already been released. Each example states its routing configuration.

Every frame is 66 bytes, including the Ethernet header and excluding
preamble, SFD, and FCS. Eight full beats use KEEP ``0xFF``; the final
two-byte beat uses KEEP ``0x03`` and TLAST. ``FA`` uses ``DA0`` through
``DA8``, ``FB`` uses ``DB0`` through ``DB8``, and ``FC`` uses ``DC0``
through ``DC8``. Copies retain the same labels on every selected output.
The source presents all queued frames continuously while they are pending.
TUSER bitmaps show all four bits with a ``0b`` prefix, in port order
``[3:0]``. Metadata belongs to the internal processing stream and does not
add Ethernet frame bytes.

A numbered tick marks a clock interval. A beat transfers at its ending
rising edge when VALID and READY are high. ``x`` marks irrelevant payload
values while VALID is low.

Explicit route retention, input gating, and frame discard
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All three routing options are zero. The output consumers remain ready.

.. list-table:: Queued frames and first-beat controls
   :class: documentation-table
   :header-rows: 1
   :widths: 15 25 20 20 20

   * - Frame
     - Data beats
     - select
     - drop
     - Result
   * - ``FA``
     - ``DA0`` through ``DA8``
     - 1
     - 0
     - Output 1
   * - ``FB``
     - ``DB0`` through ``DB8``
     - 3
     - 1
     - Discard
   * - ``FC``
     - ``DC0`` through ``DC8``
     - 2
     - 0
     - Output 2

``DA0`` transfers in tick 1 with ``select = 1`` and ``drop = 0``.
Changing those controls to ``select = 3`` and ``drop = 1`` in tick 3
does not redirect or discard FA. Input acceptance pauses in ticks 4 through
6 because ``enable = 0``. The buffered ``DA2`` still leaves output 1
in tick 4; the next input beat, ``DA3``, waits until tick 7. FA's final
``DA8`` enters in tick 12 and leaves output 1 in tick 13.

In tick 13, ``DB0`` also enters with the new select/drop decision. This
captures discard for FB while FA's output tail completes. The following
diagram continues directly from the interval shown here.

.. wavedrom::
    :name: axis-demux-explicit-start-timing
    :caption: The captured route survives control changes and an input pause
    :alt: The captured route survives control changes and an input pause.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p............."},
            {"name": "enable", "wave": "1...0..1......"},
            {"name": "drop", "wave": "0..1.........."},
            {"name": "select", "wave": "=..=..........", "data": ["1", "3"]},
            [
                "s_axis",
                [
                    "Source",
                    {"name": "tvalid", "wave": "01............"},
                    {
                        "name": "tdata",
                        "wave": "x====...======",
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
                        "wave": "x=..........==",
                        "data": ["0xFF", "0x03", "0xFF"]
                    },
                    {"name": "tlast", "wave": "x0..........10"}
                ],
                ["Sink", {"name": "tready", "wave": "1...0..1......"}]
            ],
            {},
            [
                "m_axis[0]",
                [
                    "Source",
                    {"name": "tvalid", "wave": "0............."},
                    {"name": "tdata", "wave": "x............."},
                    {"name": "tkeep", "wave": "x............."},
                    {"name": "tlast", "wave": "x............."}
                ],
                ["Sink", {"name": "tready", "wave": "1............."}]
            ],
            {},
            [
                "m_axis[1]",
                [
                    "Source",
                    {"name": "tvalid", "wave": "0.1..0..1....."},
                    {
                        "name": "tdata",
                        "wave": "x.===x..======",
                        "data": ["DA0", "DA1", "DA2", "DA3", "DA4", "DA5", "DA6", "DA7", "DA8"]
                    },
                    {
                        "name": "tkeep",
                        "wave": "x.=..x..=....=",
                        "data": ["0xFF", "0xFF", "0x03"]
                    },
                    {"name": "tlast", "wave": "x.0..x..0....1"}
                ],
                ["Sink", {"name": "tready", "wave": "1............."}]
            ],
            {},
            [
                "m_axis[2]",
                [
                    "Source",
                    {"name": "tvalid", "wave": "0............."},
                    {"name": "tdata", "wave": "x............."},
                    {"name": "tkeep", "wave": "x............."},
                    {"name": "tlast", "wave": "x............."}
                ],
                ["Sink", {"name": "tready", "wave": "1............."}]
            ],
            {},
            [
                "m_axis[3]",
                [
                    "Source",
                    {"name": "tvalid", "wave": "0............."},
                    {"name": "tdata", "wave": "x............."},
                    {"name": "tkeep", "wave": "x............."},
                    {"name": "tlast", "wave": "x............."}
                ],
                ["Sink", {"name": "tready", "wave": "1............."}]
            ],
            {}
        ],
        "head": {"tick": 0},
        "config": {"hscale": 1}
    }

From tick 14, ``drop`` returns to zero and ``select`` becomes 2.
FB remains discarded because its first beat already captured ``drop = 1``.
Its final ``DB8`` is accepted in tick 21, and none of its beats appears
on any output. FC starts in tick 22 with the new control values. It leaves
output 2 in ticks 23 through 31, preserving all bytes and the final
KEEP ``0x03`` mask.

.. wavedrom::
    :name: axis-demux-explicit-finish-timing
    :caption: The captured drop consumes FB before a fresh route sends FC to output 2
    :alt: The captured drop consumes FB before a fresh route sends FC to output 2.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p..................."},
            {"name": "enable", "wave": "1..................."},
            {"name": "drop", "wave": "0..................."},
            {"name": "select", "wave": "=...................", "data": ["2"]},
            [
                "s_axis",
                [
                    "Source",
                    {"name": "tvalid", "wave": "1................0.."},
                    {
                        "name": "tdata",
                        "wave": "=================x..",
                        "data": [
                            "DB1",
                            "DB2",
                            "DB3",
                            "DB4",
                            "DB5",
                            "DB6",
                            "DB7",
                            "DB8",
                            "DC0",
                            "DC1",
                            "DC2",
                            "DC3",
                            "DC4",
                            "DC5",
                            "DC6",
                            "DC7",
                            "DC8"
                        ]
                    },
                    {
                        "name": "tkeep",
                        "wave": "=......==.......=x..",
                        "data": ["0xFF", "0x03", "0xFF", "0x03"]
                    },
                    {"name": "tlast", "wave": "0......10.......1x.."}
                ],
                ["Sink", {"name": "tready", "wave": "1..................."}]
            ],
            {},
            [
                "m_axis[0]",
                [
                    "Source",
                    {"name": "tvalid", "wave": "0..................."},
                    {"name": "tdata", "wave": "x..................."},
                    {"name": "tkeep", "wave": "x..................."},
                    {"name": "tlast", "wave": "x..................."}
                ],
                ["Sink", {"name": "tready", "wave": "1..................."}]
            ],
            {},
            [
                "m_axis[1]",
                [
                    "Source",
                    {"name": "tvalid", "wave": "0..................."},
                    {"name": "tdata", "wave": "x..................."},
                    {"name": "tkeep", "wave": "x..................."},
                    {"name": "tlast", "wave": "x..................."}
                ],
                ["Sink", {"name": "tready", "wave": "1..................."}]
            ],
            {},
            [
                "m_axis[2]",
                [
                    "Source",
                    {"name": "tvalid", "wave": "0........1........0."},
                    {
                        "name": "tdata",
                        "wave": "x........=========x.",
                        "data": ["DC0", "DC1", "DC2", "DC3", "DC4", "DC5", "DC6", "DC7", "DC8"]
                    },
                    {
                        "name": "tkeep",
                        "wave": "x........=.......=x.",
                        "data": ["0xFF", "0x03"]
                    },
                    {"name": "tlast", "wave": "x........0.......1x."}
                ],
                ["Sink", {"name": "tready", "wave": "1..................."}]
            ],
            {},
            [
                "m_axis[3]",
                [
                    "Source",
                    {"name": "tvalid", "wave": "0..................."},
                    {"name": "tdata", "wave": "x..................."},
                    {"name": "tkeep", "wave": "x..................."},
                    {"name": "tlast", "wave": "x..................."}
                ],
                ["Sink", {"name": "tready", "wave": "1..................."}]
            ],
            {}
        ],
        "head": {"tick": 14},
        "config": {"hscale": 1}
    }

Unicast from the most significant destination bits
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``TDEST_ROUTE = 1``; the other routing options are zero. Input TDEST is
six bits wide, while output TDEST is four bits wide. The high two input
bits select one of the four outputs, and the low four bits pass through.
``select = 0`` and ``drop = 1`` are held throughout this example and are
ignored in this mode. All output consumers remain ready.

.. list-table:: Destination metadata and selected outputs
   :class: documentation-table
   :header-rows: 1
   :widths: 15 25 20 20 20

   * - Frame
     - Data beats
     - Input TDEST
     - Output
     - Output TDEST
   * - ``FA``
     - ``DA0`` through ``DA8``
     - ``0b110101``
     - 3
     - ``0b0101``
   * - ``FB``
     - ``DB0`` through ``DB8``
     - ``0b010110``
     - 1
     - ``0b0110``

FA enters in ticks 1 through 9 and leaves output 3 in ticks 2 through 10.
FB enters immediately afterwards, in ticks 10 through 18, and leaves
output 1 in ticks 11 through 19. Both frame boundaries and the reduced
destination metadata remain associated with the correct output data.
``TID_ROUTE`` applies the same most-significant-bit selection to TID
instead of TDEST.

.. wavedrom::
    :name: axis-demux-dest-timing
    :caption: The high destination bits select the output while the low bits pass through
    :alt: The high destination bits select the output while the low bits pass through.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p....................."},
            {"name": "enable", "wave": "1....................."},
            {"name": "drop", "wave": "1....................."},
            {"name": "select", "wave": "=.....................", "data": ["0"]},
            [
                "s_axis",
                [
                    "Source",
                    {"name": "tvalid", "wave": "01.................0.."},
                    {
                        "name": "tdata",
                        "wave": "x==================x..",
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
                            "DB0",
                            "DB1",
                            "DB2",
                            "DB3",
                            "DB4",
                            "DB5",
                            "DB6",
                            "DB7",
                            "DB8"
                        ]
                    },
                    {
                        "name": "tkeep",
                        "wave": "x=.......==.......=x..",
                        "data": ["0xFF", "0x03", "0xFF", "0x03"]
                    },
                    {"name": "tlast", "wave": "x0.......10.......1x.."},
                    {
                        "name": "tdest",
                        "wave": "x=........=........x..",
                        "data": ["0b110101", "0b010110"]
                    }
                ],
                ["Sink", {"name": "tready", "wave": "1....................."}]
            ],
            {},
            [
                "m_axis[0]",
                [
                    "Source",
                    {"name": "tvalid", "wave": "0....................."},
                    {"name": "tdata", "wave": "x....................."},
                    {"name": "tkeep", "wave": "x....................."},
                    {"name": "tlast", "wave": "x....................."},
                    {"name": "tdest", "wave": "x....................."}
                ],
                ["Sink", {"name": "tready", "wave": "1....................."}]
            ],
            {},
            [
                "m_axis[1]",
                [
                    "Source",
                    {"name": "tvalid", "wave": "0..........1........0."},
                    {
                        "name": "tdata",
                        "wave": "x..........=========x.",
                        "data": ["DB0", "DB1", "DB2", "DB3", "DB4", "DB5", "DB6", "DB7", "DB8"]
                    },
                    {
                        "name": "tkeep",
                        "wave": "x..........=.......=x.",
                        "data": ["0xFF", "0x03"]
                    },
                    {"name": "tlast", "wave": "x..........0.......1x."},
                    {
                        "name": "tdest",
                        "wave": "x..........=........x.",
                        "data": ["0b0110"]
                    }
                ],
                ["Sink", {"name": "tready", "wave": "1....................."}]
            ],
            {},
            [
                "m_axis[2]",
                [
                    "Source",
                    {"name": "tvalid", "wave": "0....................."},
                    {"name": "tdata", "wave": "x....................."},
                    {"name": "tkeep", "wave": "x....................."},
                    {"name": "tlast", "wave": "x....................."},
                    {"name": "tdest", "wave": "x....................."}
                ],
                ["Sink", {"name": "tready", "wave": "1....................."}]
            ],
            {},
            [
                "m_axis[3]",
                [
                    "Source",
                    {"name": "tvalid", "wave": "0.1........0.........."},
                    {
                        "name": "tdata",
                        "wave": "x.=========x..........",
                        "data": ["DA0", "DA1", "DA2", "DA3", "DA4", "DA5", "DA6", "DA7", "DA8"]
                    },
                    {
                        "name": "tkeep",
                        "wave": "x.=.......=x..........",
                        "data": ["0xFF", "0x03"]
                    },
                    {"name": "tlast", "wave": "x.0.......1x.........."},
                    {
                        "name": "tdest",
                        "wave": "x.=........x..........",
                        "data": ["0b0101"]
                    }
                ],
                ["Sink", {"name": "tready", "wave": "1....................."}]
            ],
            {}
        ],
        "head": {"tick": 0},
        "config": {"hscale": 1}
    }

Multicast waits for every selected output; a zero bitmap discards
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``TUSER_BITMAP_ROUTE = 1``; the other routing options are zero. USER is
enabled and four bits wide on both sides. ``select = 0`` and ``drop = 1``
are ignored. Output 0 stays unready throughout the example; it is not a
selected destination for either frame.

.. list-table:: Frame bitmaps and output copies
   :class: documentation-table
   :header-rows: 1
   :widths: 15 25 20 40

   * - Frame
     - Data beats
     - Input TUSER
     - Result
   * - ``FA``
     - ``DA0`` through ``DA8``
     - ``0b1010``
     - Identical copies on outputs 1 and 3
   * - ``FB``
     - ``DB0`` through ``DB8``
     - ``0b0000``
     - Discard

FA selects outputs 1 and 3. They receive ``DA0`` through ``DA2`` together
in ticks 2 through 4. In ticks 5 through 8, output 3 is not ready.
Output 1 remains ready, but both selected output VALID signals are low;
neither copy advances. Input accepts ``DA4`` in tick 5 into the remaining
buffer space, then holds ``DA5`` in ticks 6 through 9.

When output 3 becomes ready in tick 9, both outputs transfer the pending
``DA3``. Input resumes in tick 10, and the remaining copies continue
together. Both final ``DA8`` beats transfer once in tick 14 with
KEEP ``0x03`` and TLAST. Output 0's low READY never blocks them.

FB starts entering in tick 14 with TUSER ``0b0000`` and is consumed
through its final beat in tick 22 without an output copy. The externally
asserted ``drop`` did not suppress FA; bitmap routing used the captured
TUSER value for each frame.

.. wavedrom::
    :name: axis-demux-bitmap-timing
    :caption: Multicast copies advance together and a zero bitmap discards the next frame
    :alt: Multicast copies advance together and a zero bitmap discards the next frame.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p........................"},
            {"name": "enable", "wave": "1........................"},
            {"name": "drop", "wave": "1........................"},
            {"name": "select", "wave": "=........................", "data": ["0"]},
            [
                "s_axis",
                [
                    "Source",
                    {"name": "tvalid", "wave": "01.....................0."},
                    {
                        "name": "tdata",
                        "wave": "x======....============x.",
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
                            "DB0",
                            "DB1",
                            "DB2",
                            "DB3",
                            "DB4",
                            "DB5",
                            "DB6",
                            "DB7",
                            "DB8"
                        ]
                    },
                    {
                        "name": "tkeep",
                        "wave": "x=...........==.......=x.",
                        "data": ["0xFF", "0x03", "0xFF", "0x03"]
                    },
                    {"name": "tlast", "wave": "x0...........10.......1x."},
                    {
                        "name": "tuser",
                        "wave": "x=............=........x.",
                        "data": ["0b1010", "0b0000"]
                    }
                ],
                ["Sink", {"name": "tready", "wave": "1.....0...1.............."}]
            ],
            {},
            [
                "m_axis[0]",
                [
                    "Source",
                    {"name": "tvalid", "wave": "0........................"},
                    {"name": "tdata", "wave": "x........................"},
                    {"name": "tkeep", "wave": "x........................"},
                    {"name": "tlast", "wave": "x........................"},
                    {"name": "tuser", "wave": "x........................"}
                ],
                ["Sink", {"name": "tready", "wave": "0........................"}]
            ],
            {},
            [
                "m_axis[1]",
                [
                    "Source",
                    {"name": "tvalid", "wave": "0.1..0...1.....0........."},
                    {
                        "name": "tdata",
                        "wave": "x.===x...======x.........",
                        "data": ["DA0", "DA1", "DA2", "DA3", "DA4", "DA5", "DA6", "DA7", "DA8"]
                    },
                    {
                        "name": "tkeep",
                        "wave": "x.=..x...=....=x.........",
                        "data": ["0xFF", "0xFF", "0x03"]
                    },
                    {"name": "tlast", "wave": "x.0..x...0....1x........."},
                    {
                        "name": "tuser",
                        "wave": "x.=..x...=.....x.........",
                        "data": ["0b1010", "0b1010"]
                    }
                ],
                ["Sink", {"name": "tready", "wave": "1........................"}]
            ],
            {},
            [
                "m_axis[2]",
                [
                    "Source",
                    {"name": "tvalid", "wave": "0........................"},
                    {"name": "tdata", "wave": "x........................"},
                    {"name": "tkeep", "wave": "x........................"},
                    {"name": "tlast", "wave": "x........................"},
                    {"name": "tuser", "wave": "x........................"}
                ],
                ["Sink", {"name": "tready", "wave": "1........................"}]
            ],
            {},
            [
                "m_axis[3]",
                [
                    "Source",
                    {"name": "tvalid", "wave": "0.1..0...1.....0........."},
                    {
                        "name": "tdata",
                        "wave": "x.===x...======x.........",
                        "data": ["DA0", "DA1", "DA2", "DA3", "DA4", "DA5", "DA6", "DA7", "DA8"]
                    },
                    {
                        "name": "tkeep",
                        "wave": "x.=..x...=....=x.........",
                        "data": ["0xFF", "0xFF", "0x03"]
                    },
                    {"name": "tlast", "wave": "x.0..x...0....1x........."},
                    {
                        "name": "tuser",
                        "wave": "x.=..x...=.....x.........",
                        "data": ["0b1010", "0b1010"]
                    }
                ],
                ["Sink", {"name": "tready", "wave": "1....0...1..............."}]
            ],
            {}
        ],
        "head": {"tick": 0},
        "config": {"hscale": 1}
    }

.. _verification-openenoc-axis-demux:

Verification
------------

The test suite is in ``dv/core/openenoc_axis_demux/``.

Testbench
~~~~~~~~~

This test suite validates the ``openenoc_axis_demux`` module, which demultiplexes AXI Stream
input into multiple outputs based on routing configuration.

Routing Modes
~~~~~~~~~~~~~

The demux supports four routing modes, but only two are currently tested:

1. TID_ROUTE (Unicast/ID-based Routing)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Routes packets based on the TID (Transaction ID) field

- **Currently not tested**

2. TDEST_ROUTE (Unicast/Destination-based Routing)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Routes packets based on the TDEST field

- Packets are distributed to a single output port determined by TDEST

- Useful for traditional address-based routing

3. TUSER_BITMAP_ROUTE (Multicast/User-Bitmap Routing)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Routes packets based on TUSER field interpreted as a bitmap

- Each bit in TUSER selects one or more output ports

- Supports multicast (one packet to multiple ports)

- Includes "all-or-nothing" atomic delivery: all targeted ports receive the packet simultaneously
  or none do

4. Route using "select" signal (Manual/Select-based Routing)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Routes packets using an external select signal to directly specify output port(s)

- Provides explicit control over routing decisions via a dedicated select input

- **Currently not tested**

Coverage
~~~~~~~~

**TDEST_ROUTE Tests:**

- Single-port unicast delivery

- Idle insertion and backpressure handling

- Multiple data widths and output port counts

**TUSER_BITMAP_ROUTE Tests:**

- Multicast to multiple ports

- Idle insertion and backpressure handling

- Multiple data widths and output port counts

- Drop packets (empty bitmap)

- All-or-nothing atomic delivery with varying backpressure per port
