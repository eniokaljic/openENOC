.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-FileCopyrightText: 2026 Kerim Bavcic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-axis-header-parser:

Header parser -- openenoc_axis_header_parser
============================================

.. index::
   single: openenoc_axis_header_parser

Captures an Ethernet header and attaches it as metadata to the unchanged frame
stream.

**Source:** :download:`openenoc_axis_header_parser.sv <../../../hw/rtl/core/openenoc_axis_header_parser.sv>`.

Parameters
----------

.. list-table:: Parameters
   :class: rtl-reference-table
   :header-rows: 1
   :widths: 18 18 20 44

   * - Name
     - Default value
     - Allowed values
     - Description
   * - ``DEPTH``
     - ``0``
     - 0 or positive integer
     - Requested data FIFO capacity in beats, rounded up to a power of two with
       minimum two. Zero selects twice the beat count for the first 16 bytes.
   * - ``M_REG_TYPE``
     - ``2``
     - 0, 1, or 2
     - 0 bypasses output registration; 1 selects a simple buffer; 2 selects a
       two-entry AXI-Stream register slice (skid buffer).

Signals
-------

Interface ports contain channels in both directions. The table identifies
the selected modport or stream role; member directions follow that interface.

.. list-table:: Public signals and interfaces
   :class: rtl-reference-table
   :header-rows: 1
   :widths: 14 23 15 48

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
     - Active-high synchronous reset; flushes buffered data and headers and
       clears capture and output-frame tracking.
   * - ``s_axis``
     - ``taxi_axis_if.snk``
     - Sink
     - Incoming frame bytes, KEEP, and LAST. Input user metadata is not retained.
   * - ``m_axis``
     - ``taxi_axis_if.src``
     - Source
     - Unmodified frame bytes, KEEP, and LAST, with the captured 16-byte prefix
       in TUSER on every beat.

Architecture and operation
--------------------------

The parser copies the first 16 accepted bytes of each frame into a raw 128-bit
``m_axis.tuser`` value. The complete frame, including those bytes, remains in
``m_axis.tdata``; no header is stripped or inserted. Data and header records
are buffered in order. Output waits until the matching header record is ready,
so metadata accompanies the first output beat and stays the same through the
frame's final beat.

Input and output data widths must match and be multiples of eight bits.
Use matching byte-lane geometry, with ``KEEP_W = DATA_W / 8`` and
``LAST_EN = 1``. The Ethernet profile uses ``KEEP_EN = 1``: non-final
beats have all lanes enabled, and a partial final beat uses contiguous
enabled lanes starting at lane zero. Header capture advances only on accepted
input beats and uses KEEP to identify valid bytes.

The first frame byte occupies the least significant byte lane of its data
beat, but the most significant byte of the header metadata. For example,
with a 64-bit stream, ``DA0[7:0] = b0`` and ``DA0[63:56] = b7``;
the next beat carries ``b8`` through ``b15`` in the same lane order.
The captured header is ``HA = {b0, b1, ..., b15}``, with
``HA[127:120] = b0`` and ``HA[7:0] = b15``. The data beats themselves
are not byte-swapped.

.. list-table:: Header metadata
   :class: documentation-table
   :header-rows: 1
   :widths: 20 80

   * - TUSER bits
     - Field
   * - 127:80
     - Destination MAC
   * - 79:32
     - Source MAC
   * - 31:16
     - EtherType
   * - 15:8
     - Byte 14; oETP Magic when applicable
   * - 7:0
     - Byte 15; oETP Cmd when applicable

These field names assume an untagged Ethernet header. The parser copies
fixed byte positions without validating EtherType, Magic, or Cmd, and without
decoding VLAN tags. For other payload formats, bytes 14 and 15 remain raw
payload bytes. Detailed oETP command parsing belongs to :ref:`rtl-oetp-engine`.

Enable output user metadata with ``m_axis.USER_EN = 1`` and
``m_axis.USER_W >= 128``. If the width is larger, bits above 127 are zero.
Input TUSER is replaced by the captured header; input ID and destination
metadata are not preserved, and output TID and TDEST are zero. This metadata
belongs to the internal processing stream and is not part of the Ethernet
frame bytes.

If TLAST arrives before 16 valid bytes have been accepted, it completes the
header record with the received prefix and zeroes in the missing trailing
positions. The short input passes through unchanged. The block does not drop
it or produce a separate short-header error indication. Capture restarts from
byte zero for the next frame, independently of output progress.

Let ``B = ceil(16 / KEEP_W)`` be the number of full beats needed for the
prefix. ``DEPTH = 0`` requests ``2 * B`` FIFO beats. A nonzero DEPTH
requests that many beats; the actual memory depth is the next power of two,
with a minimum of two beats. Provision enough memory for header capture to
finish before output can drain that frame; rounding the requested depth to
at least ``B`` beats is sufficient. Depth sets storage capacity rather than
a fixed delay in clock cycles.

The data FIFO uses streaming mode, ``FRAME_FIFO = 0``. Once the prefix is
available, output can begin before the complete frame arrives. Input pauses
can therefore produce output gaps after buffered data runs out. The optional
output register slice also contributes to buffering and timing. Under output
backpressure, data, KEEP, LAST, and TUSER stay stable on the offered beat.
Headers captured for later frames cannot replace the current output header.

Functional scenarios
--------------------

All examples use 64-bit input and output streams, ``KEEP_W = 8``,
``KEEP_EN = 1``, ``LAST_EN = 1``, ``DEPTH = 0``, and
``M_REG_TYPE = 2``. The automatic data FIFO memory holds four beats.
Output TUSER is enabled and 128 bits wide. Input and output share a
10 ns clock, and reset has already been released.

Frames enter ``s_axis`` and leave ``m_axis`` with the same data labels:
``FA`` uses ``DA0``, ``DA1``, and subsequent beats; ``FB`` uses
``DB0``, ``DB1``, and subsequent beats; ``FC`` uses ``DC0``,
``DC1``, and subsequent beats. ``HA``, ``HB``, and ``HC`` identify
their corresponding captured headers. The source presents each complete
input without deasserting VALID while that input is pending.

Each 66-byte Ethernet frame includes its Ethernet header and excludes
preamble, SFD, and FCS. It occupies eight full beats with KEEP ``0xFF``
and a final two-byte beat with KEEP ``0x03`` and TLAST. The nine-byte
truncated input in the second scenario is not a complete Ethernet frame;
it uses one full beat and one final beat with KEEP ``0x01``.

A numbered tick marks a clock interval. A beat transfers at the ending
rising edge when VALID and READY are both high. ``x`` marks irrelevant
payload values while VALID is low.

Complete prefix capture and unchanged frame delivery
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: Frame and metadata
   :class: documentation-table
   :header-rows: 1
   :widths: 15 15 35 35

   * - Frame
     - Length
     - Data beats
     - Output TUSER
   * - ``FA``
     - 66 bytes
     - ``DA0`` through ``DA8``
     - ``HA``: the first 16 bytes of FA

The first two accepted beats, ``DA0`` and ``DA1``, contain all 16
header bytes. Output starts with ``DA0`` in tick 5, while the input
is still sending the frame. Every output beat carries ``HA``, including
the unchanged header bytes on ``DA0`` and ``DA1``. The final ``DA8``
beat retains KEEP ``0x03`` and TLAST.

.. wavedrom::
    :name: header-parser-complete-timing
    :caption: The complete frame retains its captured prefix on every output beat
    :alt: The complete frame retains its captured prefix on every output beat.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p................"},
            [
                "s_axis",
                [
                    "Source",
                    {"name": "tvalid", "wave": "01........0......"},
                    {
                        "name": "tdata",
                        "wave": "x=========x......",
                        "data": ["DA0", "DA1", "DA2", "DA3", "DA4", "DA5", "DA6", "DA7", "DA8"]
                    },
                    {
                        "name": "tkeep",
                        "wave": "x=.......=x......",
                        "data": ["0xFF", "0x03"]
                    },
                    {"name": "tlast", "wave": "x0.......1x......"}
                ],
                ["Sink", {"name": "tready", "wave": "1................"}]
            ],
            {},
            [
                "m_axis",
                [
                    "Source",
                    {"name": "tvalid", "wave": "0....1........0.."},
                    {
                        "name": "tdata",
                        "wave": "x....=========x..",
                        "data": ["DA0", "DA1", "DA2", "DA3", "DA4", "DA5", "DA6", "DA7", "DA8"]
                    },
                    {
                        "name": "tkeep",
                        "wave": "x....=.......=x..",
                        "data": ["0xFF", "0x03"]
                    },
                    {"name": "tlast", "wave": "x....0.......1x.."},
                    {"name": "tuser", "wave": "x....=........x..", "data": ["HA"]}
                ],
                ["Sink", {"name": "tready", "wave": "1................"}]
            ]
        ],
        "head": {"tick": 0},
        "config": {"hscale": 1}
    }

Truncated prefix between complete frames
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: Consecutive inputs and their headers
   :class: documentation-table
   :header-rows: 1
   :widths: 15 15 35 35

   * - Frame
     - Length
     - Data beats
     - Output TUSER
   * - ``FA``
     - 66 bytes
     - ``DA0`` through ``DA8``
     - ``HA``: the first 16 bytes of FA
   * - ``FB``
     - 9 bytes, truncated
     - ``DB0`` and ``DB1``
     - ``HB``: nine received bytes followed by seven zero bytes
   * - ``FC``
     - 66 bytes
     - ``DC0`` through ``DC8``
     - ``HC``: the first 16 bytes of FC

The source offers the three inputs consecutively. ``FB`` ends before its
16-byte prefix is complete. Its TLAST still creates one header record,
``HB = {b0, ..., b8, 56'b0}``. The seven missing bytes do not retain
values from ``HA``. Both beats of the short input pass through, including
the final KEEP ``0x01``.

The next complete frame receives ``HC`` from its own first 16 bytes.
On the output, metadata changes from ``HA`` to ``HB`` to ``HC``
only as the corresponding frame changes. The short input is neither dropped
nor merged with its neighbours.

.. wavedrom::
    :name: header-parser-short-timing
    :caption: A truncated input gets a zero-padded header between two complete frames
    :alt: A truncated input gets a zero-padded header between two complete frames.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p.........................."},
            [
                "s_axis",
                [
                    "Source",
                    {"name": "tvalid", "wave": "01...................0....."},
                    {
                        "name": "tdata",
                        "wave": "x====================x.....",
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
                        "wave": "x=.......====.......=x.....",
                        "data": ["0xFF", "0x03", "0xFF", "0x01", "0xFF", "0x03"]
                    },
                    {"name": "tlast", "wave": "x0.......1010.......1x....."}
                ],
                ["Sink", {"name": "tready", "wave": "1.........................."}]
            ],
            {},
            [
                "m_axis",
                [
                    "Source",
                    {"name": "tvalid", "wave": "0....1...................0."},
                    {
                        "name": "tdata",
                        "wave": "x....====================x.",
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
                        "wave": "x....=.......====.......=x.",
                        "data": ["0xFF", "0x03", "0xFF", "0x01", "0xFF", "0x03"]
                    },
                    {"name": "tlast", "wave": "x....0.......1010.......1x."},
                    {
                        "name": "tuser",
                        "wave": "x....=........=.=........x.",
                        "data": ["HA", "HB", "HC"]
                    }
                ],
                ["Sink", {"name": "tready", "wave": "1.........................."}]
            ]
        ],
        "head": {"tick": 0},
        "config": {"hscale": 1}
    }

Following headers cannot replace a stalled final beat
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: Frames overlapping at the parser
   :class: documentation-table
   :header-rows: 1
   :widths: 15 15 35 35

   * - Frame
     - Length
     - Data beats
     - Output TUSER
   * - ``FA``
     - 66 bytes
     - ``DA0`` through ``DA8``
     - ``HA``
   * - ``FB``
     - 66 bytes
     - ``DB0`` through ``DB8``
     - ``HB``

``FB`` starts entering in tick 10, so its first 16 bytes have already
been accepted when the final output beat of ``FA`` is held by READY low
in ticks 13 through 15. That beat keeps ``DA8``, KEEP ``0x03``,
TLAST, and ``HA`` throughout the wait, even though ``HB`` is already
available for the following frame.

READY returns high in tick 16 and accepts that final FA beat at the
ending edge. The first output beat of ``FB`` follows in tick 17 with
``HB``. Buffer pressure also holds input beat ``DB7`` for one extra
interval; this does not change either frame's metadata association.

.. wavedrom::
    :name: header-parser-boundary-timing
    :caption: A stalled final beat keeps its own header while the next frame enters
    :alt: A stalled final beat keeps its own header while the next frame enters.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p..........................."},
            [
                "s_axis",
                [
                    "Source",
                    {"name": "tvalid", "wave": "01..................0......."},
                    {
                        "name": "tdata",
                        "wave": "x=================.=x.......",
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
                   14 16 30 40         "DB5",
                            "DB6",
                            "DB7",
                            "DB8"
                        ]
                    },
                    {
                        "name": "tkeep",
                        "wave": "x=.......==........=x.......",
                        "data": ["0xFF", "0x03", "0xFF", "0x03"]
                    },
                    {"name": "tlast", "wave": "x0.......10........1x......."}
                ],
                ["Sink", {"name": "tready", "wave": "1................01........."}]
            ],
            {},
            [
                "m_axis",
                [
                    "Source",
                    {"name": "tvalid", "wave": "0....1....................0."},
                    {
                        "name": "tdata",
                        "wave": "x....=========...=========x.",
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
                        "wave": "x....=.......=...=.......=x.",
                        "data": ["0xFF", "0x03", "0xFF", "0x03"]
                    },
                    {"name": "tlast", "wave": "x....0.......1...0.......1x."},
                    {
                        "name": "tuser",
                        "wave": "x....=...........=........x.",
                        "data": ["HA", "HB"]
                    }
                ],
                ["Sink", {"name": "tready", "wave": "1............0..1..........."}]
            ]
        ],
        "head": {"tick": 0},
        "config": {"hscale": 1}
    }

.. _verification-openenoc-axis-header-parser:

Verification
------------

The test suite is in ``dv/core/openenoc_axis_header_parser/``.

Testbench
~~~~~~~~~

This test suite validates the ``openenoc_axis_header_parser`` module, which snoops the first 16
bytes of every AXI Stream frame and presents them as a stable 128-bit header on
``m_axis.tuser``. The frame payload (``tdata``) passes through unchanged, delayed by the header
so that ``tuser`` is valid from the first output beat. No field splitting is performed — the raw
128-bit header is exposed on ``tuser`` for a later block to parse.

Header layout (byte 0 = first byte on the wire = MSB of ``tuser``):

.. list-table::
   :class: rtl-reference-table
   :header-rows: 1
   :widths: 25 75

   * - Field
     - Bits
   * - Destination MAC
     - ``tuser[127:80]``
   * - Source MAC
     - ``tuser[79:32]``
   * - EtherType
     - ``tuser[31:16]``
   * - oETP Magic
     - ``tuser[15:8]``
   * - oETP Cmd
     - ``tuser[7:0]``

Coverage
~~~~~~~~

**Functional checks (per frame):**

- Payload (``tdata``) passes through unchanged

- 128-bit header is correct and stable on ``tuser`` for the whole frame

**Scenarios (TestFactory):**

- Multiple payload sizes, including header-only frames (0-byte payload)

- Back-to-back frames with distinct headers (header alignment under overlap)

- Idle insertion and backpressure combinations

**Parameter sweep (pytest):**

- ``DATA_W`` in {8, 16, 32, 64}
