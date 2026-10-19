.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-axis-monitor:

Stream monitor -- openenoc_axis_monitor
=======================================

.. index::
   single: openenoc_axis_monitor

Passes an AXI-Stream directly through and exposes a registered sample of
input VALID.

**Source:** :download:`openenoc_axis_monitor.sv <../../../hw/rtl/core/openenoc_axis_monitor.sv>`.

Parameters
----------

.. list-table:: Parameters
   :class: rtl-reference-table
   :header-rows: 1
   :widths: 12 18 20 50

   * - Name
     - Default value
     - Allowed values
     - Description
   * - None
     - —
     - —
     - This component has no elaboration parameters.

Signals
-------

Interface ports contain channels in both directions. The table identifies
the selected modport or stream role; member directions follow that interface.

.. list-table:: Public signals and interfaces
   :class: rtl-reference-table
   :header-rows: 1
   :widths: 14 24 17 45

   * - Name
     - Type
     - Direction / role
     - Description
   * - ``clk``
     - ``logic``
     - input
     - Sampling clock for the status output; the stream path is combinational.
   * - ``rst``
     - ``logic``
     - input
     - Active-high synchronous reset of the status sample. Stream forwarding
       remains combinational during reset.
   * - ``s_axis``
     - ``taxi_axis_if.snk``
     - sink
     - Incoming payload, VALID, and sidebands; READY follows m_axis directly.
   * - ``m_axis``
     - ``taxi_axis_if.src``
     - source
     - Same-cycle payload and VALID, with enabled sidebands or their defaults.
   * - ``is_idle``
     - ``logic``
     - output
     - One when input VALID was high at the preceding sampling edge;
       reset forces zero. The implemented polarity indicates sampled activity.

Architecture and operation
--------------------------

The stream path has no storage or added clock-cycle latency.
``m_axis.tdata`` and ``m_axis.tvalid`` follow the corresponding input
signals directly, and ``s_axis.tready`` follows ``m_axis.tready``.
Consequently, a beat transfers on both interfaces at the same rising edge.
Downstream backpressure reaches the upstream source in the same interval;
the monitor does not accept or retain a beat separately from the consumer.

Each sideband is forwarded when its enable flag is set on both interfaces.
Disabling it on either side selects the corresponding output default:

.. list-table:: Sideband forwarding and defaults
   :class: documentation-table
   :header-rows: 1
   :widths: 20 40 40

   * - Output
     - Enabled on both sides
     - Disabled on either side
   * - ``tkeep``
     - Input KEEP
     - All KEEP bits set
   * - ``tstrb``
     - Input STRB
     - Output KEEP
   * - ``tlast``
     - Input LAST
     - One on every valid beat
   * - ``tid``
     - Input ID
     - All zero bits
   * - ``tdest``
     - Input DEST
     - All zero bits
   * - ``tuser``
     - Input USER
     - All zero bits

Input and output DATA widths must match. KEEP widths must also match when
KEEP is enabled on both sides. Matching ID, DEST, and USER widths preserve
their complete values; ordinary assignment-width conversion applies if
those metadata widths differ. Ethernet frame monitoring uses enabled KEEP
and LAST to preserve partial final beats and frame boundaries.

The status output implements this sampling rule, where k labels the
interval ending at a rising edge:
``is_idle[k+1] = rst[k] ? 0 : s_axis.tvalid[k]``.
Despite its name, a high ``is_idle`` reports that VALID was high at that
edge. It is low after a sampled idle interval. READY, LAST, KEEP, and frame
length do not participate in the status calculation. A pending beat with
READY low therefore produces the same status as a transferred beat, and
the sample stays high for one interval after VALID falls.

The block has no byte counter, frame counter, configuration registers, or
frame-in-progress state. This status sample cannot establish that a complete
frame has drained. The current project RTL has no instantiation of this
utility or consumer of its ``is_idle`` output.

At a rising edge with ``rst = 1``, the status sample becomes zero. Once
reset is released, the next edge resumes VALID sampling. Reset does not
gate DATA, VALID, READY, or sidebands. Connected endpoints that remain active
can therefore continue transferring data while this monitor is reset.

Functional scenarios
--------------------

The examples use 64-bit input/output DATA, ``KEEP_W = 8``, and enabled KEEP
and LAST. Input and output share a 10 ns clock. Each source presents its
complete queued frame continuously until it is accepted.

FA is a 66-byte Ethernet frame, including its header and excluding preamble,
SFD, and FCS. It occupies ``DA0`` through ``DA8``: eight full beats with
KEEP ``0xFF`` followed by a two-byte final beat with KEEP ``0x03`` and TLAST.
The same data labels identify the input and output bytes.

A numbered tick marks a clock interval. A beat transfers at the interval's
ending rising edge when VALID and READY are high. The status shown in an
interval reflects the VALID/reset sample taken at its beginning edge.
``x`` marks irrelevant payload values while VALID is low.

Same-cycle forwarding and a delayed VALID sample
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Reset has already been released and the consumer remains ready.

.. list-table:: Frame flow
   :class: documentation-table
   :header-rows: 1
   :widths: 16 24 60

   * - Frame
     - Data beats
     - Path
   * - ``FA``
     - ``DA0`` through ``DA8``
     - s_axis to m_axis in the same intervals

``DA0`` through ``DA8`` transfer on both interfaces in ticks 1 through 9.
Output VALID, data, KEEP, and LAST match the input in each interval.
``is_idle`` is still zero in tick 1, rises in tick 2 after VALID has
been sampled, and remains high through tick 10. VALID is already low in
tick 10; the status returns to zero in tick 11.

.. wavedrom::
    :name: axis-monitor-continuous-timing
    :caption: The frame passes directly while is_idle follows VALID one cycle later
    :alt: The frame passes directly while is_idle follows VALID one cycle later.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p............"},
            {"name": "rst", "wave": "0............"},
            {"name": "is_idle", "wave": "0.1........0."},
            [
                "s_axis",
                [
                    "Source",
                    {"name": "tvalid", "wave": "01........0.."},
                    {
                        "name": "tdata",
                        "wave": "x=========x..",
                        "data": ["DA0", "DA1", "DA2", "DA3", "DA4", "DA5", "DA6", "DA7", "DA8"]
                    },
                    {
                        "name": "tkeep",
                        "wave": "x=.......=x..",
                        "data": ["0xFF", "0x03"]
                    },
                    {"name": "tlast", "wave": "x0.......1x.."}
                ],
                ["Sink", {"name": "tready", "wave": "1............"}]
            ],
            {},
            [
                "m_axis",
                [
                    "Source",
                    {"name": "tvalid", "wave": "01........0.."},
                    {
                        "name": "tdata",
                        "wave": "x=========x..",
                        "data": ["DA0", "DA1", "DA2", "DA3", "DA4", "DA5", "DA6", "DA7", "DA8"]
                    },
                    {
                        "name": "tkeep",
                        "wave": "x=.......=x..",
                        "data": ["0xFF", "0x03"]
                    },
                    {"name": "tlast", "wave": "x0.......1x.."}
                ],
                ["Sink", {"name": "tready", "wave": "1............"}]
            ],
            {}
        ],
        "head": {"tick": 0},
        "config": {"hscale": 1}
    }

Status follows offered VALID during backpressure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Reset has already been released. The consumer initially holds READY low,
then stalls again on the final beat.

.. list-table:: Pending frame and held beats
   :class: documentation-table
   :header-rows: 1
   :widths: 16 24 60

   * - Frame
     - Data beats
     - Held payload
   * - ``FA``
     - ``DA0`` through ``DA8``
     - DA0 while starting; DA8 with final KEEP and TLAST

``DA0`` is offered from tick 1, but READY stays low through tick 4.
No beat has transferred when ``is_idle`` rises in tick 2. The first
transfer occurs in tick 5, followed by ``DA1`` through ``DA7`` in
ticks 6 through 12.

The final ``DA8`` then waits in ticks 13 through 15 with VALID, data,
KEEP ``0x03``, and TLAST unchanged on both sides. It transfers once in
tick 16. The status stays high throughout both stalls and through tick 17,
then returns to zero in tick 18. It follows the offered VALID level rather
than the transfer or frame-completion events.

.. wavedrom::
    :name: axis-monitor-stalled-timing
    :caption: A pending VALID beat produces status even while READY prevents transfer
    :alt: A pending VALID beat produces status even while READY prevents transfer.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p..................."},
            {"name": "rst", "wave": "0..................."},
            {"name": "is_idle", "wave": "0.1...............0."},
            [
                "s_axis",
                [
                    "Source",
                    {"name": "tvalid", "wave": "01...............0.."},
                    {
                        "name": "tdata",
                        "wave": "x=....========...x..",
                        "data": ["DA0", "DA1", "DA2", "DA3", "DA4", "DA5", "DA6", "DA7", "DA8"]
                    },
                    {
                        "name": "tkeep",
                        "wave": "x=...........=...x..",
                        "data": ["0xFF", "0x03"]
                    },
                    {"name": "tlast", "wave": "x0...........1...x.."}
                ],
                ["Sink", {"name": "tready", "wave": "10...1.......0..1..."}]
            ],
            {},
            [
                "m_axis",
                [
                    "Source",
                    {"name": "tvalid", "wave": "01...............0.."},
                    {
                        "name": "tdata",
                        "wave": "x=....========...x..",
                        "data": ["DA0", "DA1", "DA2", "DA3", "DA4", "DA5", "DA6", "DA7", "DA8"]
                    },
                    {
                        "name": "tkeep",
                        "wave": "x=...........=...x..",
                        "data": ["0xFF", "0x03"]
                    },
                    {"name": "tlast", "wave": "x0...........1...x.."}
                ],
                ["Sink", {"name": "tready", "wave": "10...1.......0..1..."}]
            ],
            {}
        ],
        "head": {"tick": 0},
        "config": {"hscale": 1}
    }

Synchronous status reset during an active frame
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Only the monitor's ``rst`` input is asserted in this example. The connected
source and consumer remain active, with READY high throughout the frame.

.. list-table:: Frame flow across monitor reset
   :class: documentation-table
   :header-rows: 1
   :widths: 16 24 60

   * - Frame
     - Data beats
     - Result
   * - ``FA``
     - ``DA0`` through ``DA8``
     - Complete frame passes while the status sample is reset

The frame still transfers in ticks 1 through 9. Asserting ``rst`` in
ticks 3 and 4 leaves DATA, VALID, READY, KEEP, and LAST forwarding intact.
The status becomes zero in tick 4, after the first rising edge that samples
reset high, and remains zero in tick 5. Sampling VALID resumes at the
ending edge of tick 5, so ``is_idle`` is high again in tick 6 while the
same frame continues. The final beat transfers in tick 9, and the usual
one-interval status tail appears in tick 10.

.. wavedrom::
    :name: axis-monitor-reset-timing
    :caption: Reset clears the status sample while the active stream keeps passing
    :alt: Reset clears the status sample while the active stream keeps passing.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p............"},
            {"name": "rst", "wave": "0..1.0......."},
            {"name": "is_idle", "wave": "0.1.0.1....0."},
            [
                "s_axis",
                [
                    "Source",
                    {"name": "tvalid", "wave": "01........0.."},
                    {
                        "name": "tdata",
                        "wave": "x=========x..",
                        "data": ["DA0", "DA1", "DA2", "DA3", "DA4", "DA5", "DA6", "DA7", "DA8"]
                    },
                    {
                        "name": "tkeep",
                        "wave": "x=.......=x..",
                        "data": ["0xFF", "0x03"]
                    },
                    {"name": "tlast", "wave": "x0.......1x.."}
                ],
                ["Sink", {"name": "tready", "wave": "1............"}]
            ],
            {},
            [
                "m_axis",
                [
                    "Source",
                    {"name": "tvalid", "wave": "01........0.."},
                    {
                        "name": "tdata",
                        "wave": "x=========x..",
                        "data": ["DA0", "DA1", "DA2", "DA3", "DA4", "DA5", "DA6", "DA7", "DA8"]
                    },
                    {
                        "name": "tkeep",
                        "wave": "x=.......=x..",
                        "data": ["0xFF", "0x03"]
                    },
                    {"name": "tlast", "wave": "x0.......1x.."}
                ],
                ["Sink", {"name": "tready", "wave": "1............"}]
            ],
            {}
        ],
        "head": {"tick": 0},
        "config": {"hscale": 1}
    }
