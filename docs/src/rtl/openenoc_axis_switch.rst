.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-FileCopyrightText: 2026 Kerim Bavcic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-axis-switch:

Stream switch -- openenoc_axis_switch
=====================================

.. index::
   single: openenoc_axis_switch

Connects multiple frame streams using unicast or multicast routing and
arbitration.

**Source:** :download:`openenoc_axis_switch.sv <../../../hw/rtl/core/openenoc_axis_switch.sv>`.

Parameters
----------

.. list-table:: Parameters
   :class: rtl-reference-table
   :header-rows: 1
   :widths: 16 22 20 40

   * - Name
     - Default value
     - Allowed values
     - Description
   * - ``S_COUNT``
     - ``4``
     - Integer >= 1; see scan-range limitation
     - Number of upstream input streams.
   * - ``M_COUNT``
     - ``4``
     - Integer >= 1
     - Number of downstream output streams and routing-bitmap bits.
   * - ``M_CONNECT``
     - ``'{M_COUNT{ '{S_COUNT{1'b1}}}}``
     - M_COUNT by S_COUNT array of 0/1
     - Entry [m][s] permits source s to reach output m.
   * - ``S_REG_TYPE``
     - ``2``
     - 0, 1, or 2
     - 0 bypasses input registration; 1 uses a simple one-entry register;
       2 uses a two-entry AXI-Stream register slice (skid buffer).
   * - ``M_REG_TYPE``
     - ``0``
     - 0, 1, or 2
     - Selects the same register modes independently for every output;
       mode 1 inserts bubbles, while mode 2 can sustain one beat per cycle.

Signals
-------

Interface ports contain channels in both directions. The table identifies
the selected modport or stream role; member directions follow that interface.

.. list-table:: Public signals and interfaces
   :class: rtl-reference-table
   :header-rows: 1
   :widths: 24 24 17 35

   * - Name
     - Type
     - Direction / role
     - Description
   * - ``clk``
     - ``logic``
     - input
     - Common clock for all streams, frame admission, and output ownership.
   * - ``rst``
     - ``logic``
     - input
     - Active-high synchronous reset of arbitration, frame ownership,
       pending copies, and register-slice VALID state.
   * - ``tuser_bitmap_route``
     - ``logic``
     - input
     - Routing mode sampled when a frame is admitted: low M_COUNT USER bits
       when one, or the most significant DEST index bits when zero.
   * - ``s_axis[S_COUNT]``
     - ``taxi_axis_if.snk``
     - sink
     - Incoming frame bytes and routing metadata on each input.
   * - ``m_axis[M_COUNT]``
     - ``taxi_axis_if.src``
     - source
     - Routed or replicated frames on each independently stalled output.

Architecture and operation
--------------------------

The switch connects multiple AXI-Stream inputs to multiple outputs. It routes
frame bytes using metadata already prepared by upstream processing, such as
:ref:`rtl-axis-forwarding-engine`. Lookup and source learning belong to those
upstream blocks. Once admitted, frames with disjoint output sets can progress
concurrently, with one beat per cycle on each ready path.

For ``tuser_bitmap_route = 0``, the most significant
``$clog2(M_COUNT)`` input TDEST bits select one output. A single-output
configuration selects output zero. For ``tuser_bitmap_route = 1``, the low
``M_COUNT`` TUSER bits form the requested output bitmap. Bit n selects
output n. In either mode, ``M_CONNECT[m][s]`` filters the requested route
for source s: an unset permission removes output m from its destination set.
A partially permitted multicast reaches the surviving outputs. An empty
effective route consumes the frame through TLAST without emitting a copy
or reserving an output.

Each input passes through its configured register slice before frame
admission. A rotating scanner examines one input per cycle, starting at
input zero after reset. It advances every cycle, including when that input
is idle, already active, or waiting for an occupied output. It does not skip
to another requesting input within the same cycle. A candidate frame is
admitted when all outputs in its effective route are free; a frame selected
for discard can be admitted without output ownership. At most one new frame
is admitted per cycle, while all previously active routes can transfer data
in parallel.

The route and routing mode are evaluated at admission, after any input
register buffering. An active frame keeps its captured route until its
final beat has completed on every selected path. Later metadata or mode
changes do not redirect that active frame. A queued frame that has not yet
been admitted uses the mode present when its scan succeeds.

Admission reserves all selected outputs together. A waiting multicast does
not reserve an idle subset while another requested output is occupied.
An active source keeps its output ownership during input gaps and output
stalls, preventing another frame from interleaving on those outputs.
Ownership is released after the final beat completes; a competing admission
uses the ownership state from the beginning of its cycle and cannot reuse
an output on that same completion edge. Its next opportunity also depends
on the rotating scan position.

Each output independently accepts its copy of the current beat. VALID stays
asserted with stable payload while that output is unready. Once one output
accepts the beat, its VALID is suppressed for that beat while the remaining
copies wait. The input beat advances after every selected output has either
accepted its copy earlier or accepts it in the current cycle. A fast output
therefore receives each beat exactly once, even when another copy stalls.
Different multicast copies can transfer in different cycles. Input register
storage can accept later beats until its available space fills.

``S_REG_TYPE`` and ``M_REG_TYPE`` control independent register slices on
all inputs and outputs. Type 0 bypasses the slice. Type 1 provides one stored
beat and inserts bubbles between transfers. Type 2 provides two stored beats
and supports uninterrupted one-beat-per-cycle traffic. These slices buffer
beats rather than complete frames. The default input slices can accept a
prefix while a source waits for admission. Added output slices can accept
the final copies and release switch ownership before those copies reach
the external consumers; each output slice preserves frame order.

DATA, KEEP, LAST, and enabled STRB retain their frame-byte meaning. TID and
TDEST are cast to their output widths, preserving the low output-width bits.
TUSER on a surviving copy retains the original input metadata, including
requested destinations removed by the connectivity filter. The switch does
not rewrite TUSER to the filtered route or remove an ingress port from it.

Use consistent stream settings within each input/output array and matching
DATA widths between the arrays. Enabled KEEP requires matching KEEP widths.
Both DEST and USER must be enabled on both sides, even when only one is
used for routing. Input TDEST needs at least
``max(1, $clog2(M_COUNT))`` bits and input USER needs at least M_COUNT bits.
Use unicast indices in ``0 .. M_COUNT - 1``. TLAST must identify frame
boundaries. Reset clears the scan position,
ownership, active-frame state, pending copies, and buffered VALID state;
partial frames are abandoned.

The current scan counter wraps at its encoded width,
``max(1, $clog2(S_COUNT))``, without an explicit wrap or bounds skip at
S_COUNT. Four-input configurations use all encoded positions. Input counts
that leave unused encodings require scanner range handling before use.

Functional scenarios
--------------------

All examples use four inputs and four outputs, 64-bit DATA, ``KEEP_W = 8``,
enabled KEEP and LAST, ``S_REG_TYPE = 2``, and ``M_REG_TYPE = 0``.
Input TDEST is six bits wide; output TDEST is four bits wide. USER is
enabled and four bits wide on both sides. All streams share a 10 ns clock,
and reset has already been released. The scanner examines input 0 in tick 0,
followed by inputs 1, 2, and 3 in ticks 1, 2, and 3.

All frames are 66 bytes, including the Ethernet header and excluding
preamble, SFD, and FCS. Eight full beats use KEEP ``0xFF``; the final
two-byte beat uses KEEP ``0x03`` and TLAST. Frame FA uses ``DA0`` through
``DA8``, FB uses ``DB0`` through ``DB8``, and subsequent frames follow
the same naming pattern. Every copy retains its frame's data labels.
Each source continuously presents its queued frames while they are pending.
TUSER bitmaps use the ``0b`` prefix and port order ``[3:0]``.
These metadata fields belong to the internal processing streams and do not
add Ethernet frame bytes.

A numbered tick marks a clock interval. A beat transfers at its ending
rising edge when VALID and READY are high. ``x`` marks irrelevant payload
values while VALID is low. Consecutive diagrams within a scenario show
adjacent clock intervals.

Independent unicast routes progress together
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``tuser_bitmap_route = 0`` and all M_CONNECT entries are one. Every output
is ready. The high two input TDEST bits select the output; the low four
bits remain on output TDEST.

.. list-table:: Frames offered together in tick 1
   :class: documentation-table
   :header-rows: 1
   :widths: 12 12 36 20 20

   * - Frame
     - Input
     - Data beats
     - Input TDEST
     - Output / TDEST
   * - ``FA``
     - 0
     - ``DA0`` through ``DA8``
     - ``0b100001``
     - 2 / ``0b0001``
   * - ``FB``
     - 1
     - ``DB0`` through ``DB8``
     - ``0b000010``
     - 0 / ``0b0010``
   * - ``FC``
     - 2
     - ``DC0`` through ``DC8``
     - ``0b110011``
     - 3 / ``0b0011``
   * - ``FD``
     - 3
     - ``DD0`` through ``DD8``
     - ``0b010100``
     - 1 / ``0b0100``

Each input first fills its available register storage while waiting for
admission. FC and FD start leaving outputs 3 and 1 in ticks 3 and 4;
FA and FB follow on outputs 2 and 0 in ticks 5 and 6. These start times
reflect the scanner and input buffering, rather than a shared output-data
bus. From tick 6 through tick 11, all four outputs transfer a beat every
cycle. The final beats complete in ticks 11 through 14 on their respective
outputs, each retaining KEEP ``0x03`` and TLAST.

.. wavedrom::
    :name: axis-switch-disjoint-timing
    :caption: Four disjoint unicast routes progress concurrently after separate admissions
    :alt: Four disjoint unicast routes progress concurrently after separate admissions.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p................."},
            {"name": "tuser_bitmap_route", "wave": "0................."},
            [
                "s_axis[0]",
                [
                    "Source",
                    {"name": "tvalid", "wave": "01...........0...."},
                    {
                        "name": "tdata",
                        "wave": "x===...======x....",
                        "data": ["DA0", "DA1", "DA2", "DA3", "DA4", "DA5", "DA6", "DA7", "DA8"]
                    },
                    {
                        "name": "tkeep",
                        "wave": "x=..........=x....",
                        "data": ["0xFF", "0x03"]
                    },
                    {"name": "tlast", "wave": "x0..........1x...."},
                    {
                        "name": "tdest",
                        "wave": "x=...........x....",
                        "data": ["0b100001"]
                    }
                ],
                ["Sink", {"name": "tready", "wave": "1..0..1..........."}]
            ],
            {},
            [
                "s_axis[1]",
                [
                    "Source",
                    {"name": "tvalid", "wave": "01............0..."},
                    {
                        "name": "tdata",
                        "wave": "x===....======x...",
                        "data": ["DB0", "DB1", "DB2", "DB3", "DB4", "DB5", "DB6", "DB7", "DB8"]
                    },
                    {
                        "name": "tkeep",
                        "wave": "x=...........=x...",
                        "data": ["0xFF", "0x03"]
                    },
                    {"name": "tlast", "wave": "x0...........1x..."},
                    {
                        "name": "tdest",
                        "wave": "x=............x...",
                        "data": ["0b000010"]
                    }
                ],
                ["Sink", {"name": "tready", "wave": "1..0...1.........."}]
            ],
            {},
            [
                "s_axis[2]",
                [
                    "Source",
                    {"name": "tvalid", "wave": "01.........0......"},
                    {
                        "name": "tdata",
                        "wave": "x===.======x......",
                        "data": ["DC0", "DC1", "DC2", "DC3", "DC4", "DC5", "DC6", "DC7", "DC8"]
                    },
                    {
                        "name": "tkeep",
                        "wave": "x=........=x......",
                        "data": ["0xFF", "0x03"]
                    },
                    {"name": "tlast", "wave": "x0........1x......"},
                    {
                        "name": "tdest",
                        "wave": "x=.........x......",
                        "data": ["0b110011"]
                    }
                ],
                ["Sink", {"name": "tready", "wave": "1..01............."}]
            ],
            {},
            [
                "s_axis[3]",
                [
                    "Source",
                    {"name": "tvalid", "wave": "01..........0....."},
                    {
                        "name": "tdata",
                        "wave": "x===..======x.....",
                        "data": ["DD0", "DD1", "DD2", "DD3", "DD4", "DD5", "DD6", "DD7", "DD8"]
                    },
                    {
                        "name": "tkeep",
                        "wave": "x=.........=x.....",
                        "data": ["0xFF", "0x03"]
                    },
                    {"name": "tlast", "wave": "x0.........1x....."},
                    {
                        "name": "tdest",
                        "wave": "x=..........x.....",
                        "data": ["0b010100"]
                    }
                ],
                ["Sink", {"name": "tready", "wave": "1..0.1............"}]
            ],
            {},
            [
                "m_axis[0]",
                [
                    "Source",
                    {"name": "tvalid", "wave": "0.....1........0.."},
                    {
                        "name": "tdata",
                        "wave": "x.....=========x..",
                        "data": ["DB0", "DB1", "DB2", "DB3", "DB4", "DB5", "DB6", "DB7", "DB8"]
                    },
                    {
                        "name": "tkeep",
                        "wave": "x.....=.......=x..",
                        "data": ["0xFF", "0x03"]
                    },
                    {"name": "tlast", "wave": "x.....0.......1x.."},
                    {"name": "tdest", "wave": "x.....=........x..", "data": ["0b0010"]}
                ],
                ["Sink", {"name": "tready", "wave": "1................."}]
            ],
            {},
            [
                "m_axis[1]",
                [
                    "Source",
                    {"name": "tvalid", "wave": "0...1........0...."},
                    {
                        "name": "tdata",
                        "wave": "x...=========x....",
                        "data": ["DD0", "DD1", "DD2", "DD3", "DD4", "DD5", "DD6", "DD7", "DD8"]
                    },
                    {
                        "name": "tkeep",
                        "wave": "x...=.......=x....",
                        "data": ["0xFF", "0x03"]
                    },
                    {"name": "tlast", "wave": "x...0.......1x...."},
                    {"name": "tdest", "wave": "x...=........x....", "data": ["0b0100"]}
                ],
                ["Sink", {"name": "tready", "wave": "1................."}]
            ],
            {},
            [
                "m_axis[2]",
                [
                    "Source",
                    {"name": "tvalid", "wave": "0....1........0..."},
                    {
                        "name": "tdata",
                        "wave": "x....=========x...",
                        "data": ["DA0", "DA1", "DA2", "DA3", "DA4", "DA5", "DA6", "DA7", "DA8"]
                    },
                    {
                        "name": "tkeep",
                        "wave": "x....=.......=x...",
                        "data": ["0xFF", "0x03"]
                    },
                    {"name": "tlast", "wave": "x....0.......1x..."},
                    {"name": "tdest", "wave": "x....=........x...", "data": ["0b0001"]}
                ],
                ["Sink", {"name": "tready", "wave": "1................."}]
            ],
            {},
            [
                "m_axis[3]",
                [
                    "Source",
                    {"name": "tvalid", "wave": "0..1........0....."},
                    {
                        "name": "tdata",
                        "wave": "x..=========x.....",
                        "data": ["DC0", "DC1", "DC2", "DC3", "DC4", "DC5", "DC6", "DC7", "DC8"]
                    },
                    {
                        "name": "tkeep",
                        "wave": "x..=.......=x.....",
                        "data": ["0xFF", "0x03"]
                    },
                    {"name": "tlast", "wave": "x..0.......1x....."},
                    {"name": "tdest", "wave": "x..=........x.....", "data": ["0b0011"]}
                ],
                ["Sink", {"name": "tready", "wave": "1................."}]
            ],
            {}
        ],
        "head": {"tick": 0},
        "config": {"hscale": 1}
    }

Overlapping multicast routes wait for the complete output set
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``tuser_bitmap_route = 1`` and all M_CONNECT entries are one. All outputs
remain ready; inputs 2 and 3 have no queued frames.

.. list-table:: Competing multicast frames
   :class: documentation-table
   :header-rows: 1
   :widths: 12 12 36 20 20

   * - Frame
     - Input
     - Data beats
     - Input TUSER
     - Outputs
   * - ``FA``
     - 0
     - ``DA0`` through ``DA8``
     - ``0b0011``
     - 0 and 1
   * - ``FB``
     - 1
     - ``DB0`` through ``DB8``
     - ``0b0110``
     - 1 and 2

FA acquires outputs 0 and 1 and sends both copies in ticks 5 through 13.
FB's prefix enters its input register slice, but its remaining input data
waits because output 1 belongs to FA. Output 2 stays idle even though it
is free and ready: FB cannot begin using only the available part of its
requested route. Neither FA copy interleaves with FB.

.. wavedrom::
    :name: axis-switch-contention-start-timing
    :caption: A multicast waits for its whole route while FA owns the shared output
    :alt: A multicast waits for its whole route while FA owns the shared output.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p.............."},
            {"name": "tuser_bitmap_route", "wave": "1.............."},
            [
                "s_axis[0]",
                [
                    "Source",
                    {"name": "tvalid", "wave": "01...........0."},
                    {
                        "name": "tdata",
                        "wave": "x===...======x.",
                        "data": ["DA0", "DA1", "DA2", "DA3", "DA4", "DA5", "DA6", "DA7", "DA8"]
                    },
                    {
                        "name": "tkeep",
                        "wave": "x=..........=x.",
                        "data": ["0xFF", "0x03"]
                    },
                    {"name": "tlast", "wave": "x0..........1x."},
                    {"name": "tuser", "wave": "x=...........x.", "data": ["0b0011"]}
                ],
                ["Sink", {"name": "tready", "wave": "1..0..1........"}]
            ],
            {},
            [
                "s_axis[1]",
                [
                    "Source",
                    {"name": "tvalid", "wave": "01............."},
                    {
                        "name": "tdata",
                        "wave": "x===...........",
                        "data": ["DB0", "DB1", "DB2"]
                    },
                    {"name": "tkeep", "wave": "x=.............", "data": ["0xFF"]},
                    {"name": "tlast", "wave": "x0............."},
                    {"name": "tuser", "wave": "x=.............", "data": ["0b0110"]}
                ],
                ["Sink", {"name": "tready", "wave": "1..0..........."}]
            ],
            {},
            [
                "s_axis[2]",
                [
                    "Source",
                    {"name": "tvalid", "wave": "0.............."},
                    {"name": "tdata", "wave": "x.............."},
                    {"name": "tkeep", "wave": "x.............."},
                    {"name": "tlast", "wave": "x.............."},
                    {"name": "tuser", "wave": "x.............."}
                ],
                ["Sink", {"name": "tready", "wave": "1.............."}]
            ],
            {},
            [
                "s_axis[3]",
                [
                    "Source",
                    {"name": "tvalid", "wave": "0.............."},
                    {"name": "tdata", "wave": "x.............."},
                    {"name": "tkeep", "wave": "x.............."},
                    {"name": "tlast", "wave": "x.............."},
                    {"name": "tuser", "wave": "x.............."}
                ],
                ["Sink", {"name": "tready", "wave": "1.............."}]
            ],
            {},
            [
                "m_axis[0]",
                [
                    "Source",
                    {"name": "tvalid", "wave": "0....1........0"},
                    {
                        "name": "tdata",
                        "wave": "x....=========x",
                        "data": ["DA0", "DA1", "DA2", "DA3", "DA4", "DA5", "DA6", "DA7", "DA8"]
                    },
                    {
                        "name": "tkeep",
                        "wave": "x....=.......=x",
                        "data": ["0xFF", "0x03"]
                    },
                    {"name": "tlast", "wave": "x....0.......1x"},
                    {"name": "tuser", "wave": "x....=........x", "data": ["0b0011"]}
                ],
                ["Sink", {"name": "tready", "wave": "1.............."}]
            ],
            {},
            [
                "m_axis[1]",
                [
                    "Source",
                    {"name": "tvalid", "wave": "0....1........0"},
                    {
                        "name": "tdata",
                        "wave": "x....=========x",
                        "data": ["DA0", "DA1", "DA2", "DA3", "DA4", "DA5", "DA6", "DA7", "DA8"]
                    },
                    {
                        "name": "tkeep",
                        "wave": "x....=.......=x",
                        "data": ["0xFF", "0x03"]
                    },
                    {"name": "tlast", "wave": "x....0.......1x"},
                    {"name": "tuser", "wave": "x....=........x", "data": ["0b0011"]}
                ],
                ["Sink", {"name": "tready", "wave": "1.............."}]
            ],
            {},
            [
                "m_axis[2]",
                [
                    "Source",
                    {"name": "tvalid", "wave": "0.............."},
                    {"name": "tdata", "wave": "x.............."},
                    {"name": "tkeep", "wave": "x.............."},
                    {"name": "tlast", "wave": "x.............."},
                    {"name": "tuser", "wave": "x.............."}
                ],
                ["Sink", {"name": "tready", "wave": "1.............."}]
            ],
            {},
            [
                "m_axis[3]",
                [
                    "Source",
                    {"name": "tvalid", "wave": "0.............."},
                    {"name": "tdata", "wave": "x.............."},
                    {"name": "tkeep", "wave": "x.............."},
                    {"name": "tlast", "wave": "x.............."},
                    {"name": "tuser", "wave": "x.............."}
                ],
                ["Sink", {"name": "tready", "wave": "1.............."}]
            ],
            {}
        ],
        "head": {"tick": 0},
        "config": {"hscale": 1}
    }

FA's final copies transfer in tick 13, releasing both outputs at that
interval's ending edge. The input-1 scan in tick 13 still sees the existing
ownership. Its next visit in tick 17 can admit FB, and FB's two copies
start in tick 18. They transfer consecutively through tick 26 on outputs
1 and 2. Output 0 remains free after FA completes, and output 3 is unused.

.. wavedrom::
    :name: axis-switch-contention-finish-timing
    :caption: The next input scan admits FB after the shared output is released
    :alt: The next input scan admits FB after the shared output is released.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p.............."},
            {"name": "tuser_bitmap_route", "wave": "1.............."},
            [
                "s_axis[0]",
                [
                    "Source",
                    {"name": "tvalid", "wave": "0.............."},
                    {"name": "tdata", "wave": "x.............."},
                    {"name": "tkeep", "wave": "x.............."},
                    {"name": "tlast", "wave": "x.............."},
                    {"name": "tuser", "wave": "x.............."}
                ],
                ["Sink", {"name": "tready", "wave": "1.............."}]
            ],
            {},
            [
                "s_axis[1]",
                [
                    "Source",
                    {"name": "tvalid", "wave": "1..........0..."},
                    {
                        "name": "tdata",
                        "wave": "=....======x...",
                        "data": ["DB2", "DB3", "DB4", "DB5", "DB6", "DB7", "DB8"]
                    },
                    {
                        "name": "tkeep",
                        "wave": "=.........=x...",
                        "data": ["0xFF", "0x03"]
                    },
                    {"name": "tlast", "wave": "0.........1x..."},
                    {"name": "tuser", "wave": "=..........x...", "data": ["0b0110"]}
                ],
                ["Sink", {"name": "tready", "wave": "0...1.........."}]
            ],
            {},
            [
                "s_axis[2]",
                [
                    "Source",
                    {"name": "tvalid", "wave": "0.............."},
                    {"name": "tdata", "wave": "x.............."},
                    {"name": "tkeep", "wave": "x.............."},
                    {"name": "tlast", "wave": "x.............."},
                    {"name": "tuser", "wave": "x.............."}
                ],
                ["Sink", {"name": "tready", "wave": "1.............."}]
            ],
            {},
            [
                "s_axis[3]",
                [
                    "Source",
                    {"name": "tvalid", "wave": "0.............."},
                    {"name": "tdata", "wave": "x.............."},
                    {"name": "tkeep", "wave": "x.............."},
                    {"name": "tlast", "wave": "x.............."},
                    {"name": "tuser", "wave": "x.............."}
                ],
                ["Sink", {"name": "tready", "wave": "1.............."}]
            ],
            {},
            [
                "m_axis[0]",
                [
                    "Source",
                    {"name": "tvalid", "wave": "0.............."},
                    {"name": "tdata", "wave": "x.............."},
                    {"name": "tkeep", "wave": "x.............."},
                    {"name": "tlast", "wave": "x.............."},
                    {"name": "tuser", "wave": "x.............."}
                ],
                ["Sink", {"name": "tready", "wave": "1.............."}]
            ],
            {},
            [
                "m_axis[1]",
                [
                    "Source",
                    {"name": "tvalid", "wave": "0..1........0.."},
                    {
                        "name": "tdata",
                        "wave": "x..=========x..",
                        "data": ["DB0", "DB1", "DB2", "DB3", "DB4", "DB5", "DB6", "DB7", "DB8"]
                    },
                    {
                        "name": "tkeep",
                        "wave": "x..=.......=x..",
                        "data": ["0xFF", "0x03"]
                    },
                    {"name": "tlast", "wave": "x..0.......1x.."},
                    {"name": "tuser", "wave": "x..=........x..", "data": ["0b0110"]}
                ],
                ["Sink", {"name": "tready", "wave": "1.............."}]
            ],
            {},
            [
                "m_axis[2]",
                [
                    "Source",
                    {"name": "tvalid", "wave": "0..1........0.."},
                    {
                        "name": "tdata",
                        "wave": "x..=========x..",
                        "data": ["DB0", "DB1", "DB2", "DB3", "DB4", "DB5", "DB6", "DB7", "DB8"]
                    },
                    {
                        "name": "tkeep",
                        "wave": "x..=.......=x..",
                        "data": ["0xFF", "0x03"]
                    },
                    {"name": "tlast", "wave": "x..0.......1x.."},
                    {"name": "tuser", "wave": "x..=........x..", "data": ["0b0110"]}
                ],
                ["Sink", {"name": "tready", "wave": "1.............."}]
            ],
            {},
            [
                "m_axis[3]",
                [
                    "Source",
                    {"name": "tvalid", "wave": "0.............."},
                    {"name": "tdata", "wave": "x.............."},
                    {"name": "tkeep", "wave": "x.............."},
                    {"name": "tlast", "wave": "x.............."},
                    {"name": "tuser", "wave": "x.............."}
                ],
                ["Sink", {"name": "tready", "wave": "1.............."}]
            ],
            {}
        ],
        "head": {"tick": 15},
        "config": {"hscale": 1}
    }

Independent multicast copies and connectivity filtering
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``tuser_bitmap_route = 1``. Only ``M_CONNECT[0][3]`` is zero; all other
paths are permitted. Input 3 queues FD followed immediately by FE.
Output 0 remains unready throughout the example.

.. list-table:: Requested routes and surviving frame copies
   :class: documentation-table
   :header-rows: 1
   :widths: 11 10 22 18 19 20

   * - Frame
     - Input
     - Data beats
     - Input TUSER
     - Effective route
     - Result
   * - ``FA``
     - 0
     - ``DA0`` through ``DA8``
     - ``0b1010``
     - ``0b1010``
     - Outputs 1 and 3
   * - ``FB``
     - 1
     - ``DB0`` through ``DB8``
     - ``0b0100``
     - ``0b0100``
     - Output 2
   * - ``FC``
     - 2
     - ``DC0`` through ``DC8``
     - ``0b0000``
     - ``0b0000``
     - Discard
   * - ``FD``
     - 3
     - ``DD0`` through ``DD8``
     - ``0b0001``
     - ``0b0000``
     - Discard
   * - ``FE``
     - 3
     - ``DE0`` through ``DE8``
     - ``0b1001``
     - ``0b1000``
     - Output 3

In tick 5, output 1 accepts ``DA0`` while output 3 is unready. Output 3
holds that same beat with VALID high through tick 8 and accepts it in
tick 9. Output 1 remains invalid in ticks 6 through 9, so it does not
accept ``DA0`` again. Both copies resume with ``DA1`` in tick 10 and
finish together with ``DA8`` in tick 17. Meanwhile FB transfers on output
2 in ticks 6 through 14.

FC's empty requested bitmap and FD's fully filtered route are both drained
without an output copy. FE's prefix can enter input 3's register slice,
but its surviving destination, output 3, remains owned by FA until FA
finishes. Output 0's low READY does not block any of these permitted paths.

.. wavedrom::
    :name: axis-switch-filtered-start-timing
    :caption: Each multicast output accepts its own copy once while other paths advance
    :alt: Each multicast output accepts its own copy once while other paths advance.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p................."},
            {"name": "tuser_bitmap_route", "wave": "1................."},
            [
                "s_axis[0]",
                [
                    "Source",
                    {"name": "tvalid", "wave": "01...............0"},
                    {
                        "name": "tdata",
                        "wave": "x===.......======x",
                        "data": ["DA0", "DA1", "DA2", "DA3", "DA4", "DA5", "DA6", "DA7", "DA8"]
                    },
                    {
                        "name": "tkeep",
                        "wave": "x=..............=x",
                        "data": ["0xFF", "0x03"]
                    },
                    {"name": "tlast", "wave": "x0..............1x"},
                    {"name": "tuser", "wave": "x=...............x", "data": ["0b1010"]}
                ],
                ["Sink", {"name": "tready", "wave": "1..0......1......."}]
            ],
            {},
            [
                "s_axis[1]",
                [
                    "Source",
                    {"name": "tvalid", "wave": "01............0..."},
                    {
                        "name": "tdata",
                        "wave": "x===....======x...",
                        "data": ["DB0", "DB1", "DB2", "DB3", "DB4", "DB5", "DB6", "DB7", "DB8"]
                    },
                    {
                        "name": "tkeep",
                        "wave": "x=...........=x...",
                        "data": ["0xFF", "0x03"]
                    },
                    {"name": "tlast", "wave": "x0...........1x..."},
                    {"name": "tuser", "wave": "x=............x...", "data": ["0b0100"]}
                ],
                ["Sink", {"name": "tready", "wave": "1..0...1.........."}]
            ],
            {},
            [
                "s_axis[2]",
                [
                    "Source",
                    {"name": "tvalid", "wave": "01.........0......"},
                    {
                        "name": "tdata",
                        "wave": "x===.======x......",
                        "data": ["DC0", "DC1", "DC2", "DC3", "DC4", "DC5", "DC6", "DC7", "DC8"]
                    },
                    {
                        "name": "tkeep",
                        "wave": "x=........=x......",
                        "data": ["0xFF", "0x03"]
                    },
                    {"name": "tlast", "wave": "x0........1x......"},
                    {"name": "tuser", "wave": "x=.........x......", "data": ["0b0000"]}
                ],
                ["Sink", {"name": "tready", "wave": "1..01............."}]
            ],
            {},
            [
                "s_axis[3]",
                [
                    "Source",
                    {"name": "tvalid", "wave": "01................"},
                    {
                        "name": "tdata",
                        "wave": "x===..=========...",
                        "data": [
                            "DD0",
                            "DD1",
                            "DD2",
                            "DD3",
                            "DD4",
                            "DD5",
                            "DD6",
                            "DD7",
                            "DD8",
                            "DE0",
                            "DE1",
                            "DE2"
                        ]
                    },
                    {
                        "name": "tkeep",
                        "wave": "x=.........==.....",
                        "data": ["0xFF", "0x03", "0xFF"]
                    },
                    {"name": "tlast", "wave": "x0.........10....."},
                    {
                        "name": "tuser",
                        "wave": "x=..........=.....",
                        "data": ["0b0001", "0b1001"]
                    }
                ],
                ["Sink", {"name": "tready", "wave": "1..0.1........0..."}]
            ],
            {},
            [
                "m_axis[0]",
                [
                    "Source",
                    {"name": "tvalid", "wave": "0................."},
                    {"name": "tdata", "wave": "x................."},
                    {"name": "tkeep", "wave": "x................."},
                    {"name": "tlast", "wave": "x................."},
                    {"name": "tuser", "wave": "x................."}
                ],
                ["Sink", {"name": "tready", "wave": "0................."}]
            ],
            {},
            [
                "m_axis[1]",
                [
                    "Source",
                    {"name": "tvalid", "wave": "0....10...1......."},
                    {
                        "name": "tdata",
                        "wave": "x....=x...========",
                        "data": ["DA0", "DA1", "DA2", "DA3", "DA4", "DA5", "DA6", "DA7", "DA8"]
                    },
                    {
                        "name": "tkeep",
                        "wave": "x....=x...=......=",
                        "data": ["0xFF", "0xFF", "0x03"]
                    },
                    {"name": "tlast", "wave": "x....0x...0......1"},
                    {
                        "name": "tuser",
                        "wave": "x....=x...=.......",
                        "style": "font-size: 10px;",
                        "data": ["0b1010", "0b1010"]
                    }
                ],
                ["Sink", {"name": "tready", "wave": "1................."}]
            ],
            {},
            [
                "m_axis[2]",
                [
                    "Source",
                    {"name": "tvalid", "wave": "0.....1........0.."},
                    {
                        "name": "tdata",
                        "wave": "x.....=========x..",
                        "data": ["DB0", "DB1", "DB2", "DB3", "DB4", "DB5", "DB6", "DB7", "DB8"]
                    },
                    {
                        "name": "tkeep",
                        "wave": "x.....=.......=x..",
                        "data": ["0xFF", "0x03"]
                    },
                    {"name": "tlast", "wave": "x.....0.......1x.."},
                    {"name": "tuser", "wave": "x.....=........x..", "data": ["0b0100"]}
                ],
                ["Sink", {"name": "tready", "wave": "1................."}]
            ],
            {},
            [
                "m_axis[3]",
                [
                    "Source",
                    {"name": "tvalid", "wave": "0....1............"},
                    {
                        "name": "tdata",
                        "wave": "x....=....========",
                        "data": ["DA0", "DA1", "DA2", "DA3", "DA4", "DA5", "DA6", "DA7", "DA8"]
                    },
                    {
                        "name": "tkeep",
                        "wave": "x....=...........=",
                        "data": ["0xFF", "0x03"]
                    },
                    {"name": "tlast", "wave": "x....0...........1"},
                    {"name": "tuser", "wave": "x....=............", "data": ["0b1010"]}
                ],
                ["Sink", {"name": "tready", "wave": "0........1........"}]
            ],
            {}
        ],
        "head": {"tick": 0},
        "config": {"hscale": 1}
    }

After FA releases output 3, the next eligible input-3 scan admits FE.
Its beats leave output 3 in ticks 20 through 28, with no copy on output 0.
Every FE output beat still carries TUSER ``0b1001``, while its effective
route selects only output 3. Its final ``DE8`` transfers once in tick 28
with KEEP ``0x03`` and TLAST.

.. wavedrom::
    :name: axis-switch-filtered-finish-timing
    :caption: Connectivity removes a destination while preserving the original TUSER
    :alt: Connectivity removes a destination while preserving the original TUSER.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p............."},
            {"name": "tuser_bitmap_route", "wave": "1............."},
            [
                "s_axis[0]",
                [
                    "Source",
                    {"name": "tvalid", "wave": "0............."},
                    {"name": "tdata", "wave": "x............."},
                    {"name": "tkeep", "wave": "x............."},
                    {"name": "tlast", "wave": "x............."},
                    {"name": "tuser", "wave": "x............."}
                ],
                ["Sink", {"name": "tready", "wave": "1............."}]
            ],
            {},
            [
                "s_axis[1]",
                [
                    "Source",
                    {"name": "tvalid", "wave": "0............."},
                    {"name": "tdata", "wave": "x............."},
                    {"name": "tkeep", "wave": "x............."},
                    {"name": "tlast", "wave": "x............."},
                    {"name": "tuser", "wave": "x............."}
                ],
                ["Sink", {"name": "tready", "wave": "1............."}]
            ],
            {},
            [
                "s_axis[2]",
                [
                    "Source",
                    {"name": "tvalid", "wave": "0............."},
                    {"name": "tdata", "wave": "x............."},
                    {"name": "tkeep", "wave": "x............."},
                    {"name": "tlast", "wave": "x............."},
                    {"name": "tuser", "wave": "x............."}
                ],
                ["Sink", {"name": "tready", "wave": "1............."}]
            ],
            {},
            [
                "s_axis[3]",
                [
                    "Source",
                    {"name": "tvalid", "wave": "1.........0..."},
                    {
                        "name": "tdata",
                        "wave": "=...======x...",
                        "data": ["DE2", "DE3", "DE4", "DE5", "DE6", "DE7", "DE8"]
                    },
                    {
                        "name": "tkeep",
                        "wave": "=........=x...",
                        "data": ["0xFF", "0x03"]
                    },
                    {"name": "tlast", "wave": "0........1x..."},
                    {"name": "tuser", "wave": "=.........x...", "data": ["0b1001"]}
                ],
                ["Sink", {"name": "tready", "wave": "0..1.........."}]
            ],
            {},
            [
                "m_axis[0]",
                [
                    "Source",
                    {"name": "tvalid", "wave": "0............."},
                    {"name": "tdata", "wave": "x............."},
                    {"name": "tkeep", "wave": "x............."},
                    {"name": "tlast", "wave": "x............."},
                    {"name": "tuser", "wave": "x............."}
                ],
                ["Sink", {"name": "tready", "wave": "0............."}]
            ],
            {},
            [
                "m_axis[1]",
                [
                    "Source",
                    {"name": "tvalid", "wave": "0............."},
                    {"name": "tdata", "wave": "x............."},
                    {"name": "tkeep", "wave": "x............."},
                    {"name": "tlast", "wave": "x............."},
                    {"name": "tuser", "wave": "x............."}
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
                    {"name": "tlast", "wave": "x............."},
                    {"name": "tuser", "wave": "x............."}
                ],
                ["Sink", {"name": "tready", "wave": "1............."}]
            ],
            {},
            [
                "m_axis[3]",
                [
                    "Source",
                    {"name": "tvalid", "wave": "0.1........0.."},
                    {
                        "name": "tdata",
                        "wave": "x.=========x..",
                        "data": ["DE0", "DE1", "DE2", "DE3", "DE4", "DE5", "DE6", "DE7", "DE8"]
                    },
                    {
                        "name": "tkeep",
                        "wave": "x.=.......=x..",
                        "data": ["0xFF", "0x03"]
                    },
                    {"name": "tlast", "wave": "x.0.......1x.."},
                    {"name": "tuser", "wave": "x.=........x..", "data": ["0b1001"]}
                ],
                ["Sink", {"name": "tready", "wave": "1............."}]
            ],
            {}
        ],
        "head": {"tick": 18},
        "config": {"hscale": 1}
    }

.. _verification-openenoc-axis-switch:

Verification
------------

The test suite is in ``dv/core/openenoc_axis_switch/``.

Testbench
~~~~~~~~~

This test suite validates the ``openenoc_axis_switch`` module in isolation. The module routes
AXI Stream traffic from multiple inputs to multiple outputs.

Routing Modes
~~~~~~~~~~~~~

The switch verification currently targets two routing modes:

1. Unicast (TDEST-based Routing)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Routes each frame to one output port based on TDEST MSBs

- Useful for classical single-destination forwarding

- Activated when ``PARAM_TUSER_BITMAP_ROUTE := 0``

2. Multicast (TUSER Bitmap Routing)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Routes each frame based on TUSER bitmap bits

- Supports one-to-many delivery from one input to multiple outputs

- Includes empty-bitmap drop behavior

- Includes scheduler/contention scenarios between multiple inputs

- Activated when ``PARAM_TUSER_BITMAP_ROUTE := 1``

Coverage
~~~~~~~~

**Unicast (TDEST) tests:**

- Single-destination forwarding checks

- Multiple frame sizes

- Idle insertion and backpressure scenarios

**Multicast (TUSER bitmap) tests:**

- Multiple bitmap combinations (including all-target and subset delivery)

- Empty bitmap drop behavior

- Scheduler/contention scenario with overlapping output targets

- Idle insertion and backpressure scenarios
