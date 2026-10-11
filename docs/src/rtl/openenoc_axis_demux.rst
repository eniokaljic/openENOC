.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-FileCopyrightText: 2026 Kerim Bavcic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-axis-demux:

Stream demultiplexer -- openenoc_axis_demux
===========================================

Routes or replicates each incoming stream frame to selected output paths.

**Source:** :download:`openenoc_axis_demux.sv <../../../hw/rtl/core/openenoc_axis_demux.sv>`.

Parameters
----------

.. list-table:: Parameters
   :class: rtl-reference-table
   :header-rows: 1
   :widths: 30 18 22 30

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
     - Routes by stream ID; requires enabled ID with enough index bits.
   * - ``TDEST_ROUTE``
     - ``1'b0``
     - 0 or 1; exclusive routing selection
     - Routes by destination; requires enabled DEST with enough index bits.
   * - ``TUSER_BITMAP_ROUTE``
     - ``1'b0``
     - 0 or 1; exclusive routing selection
     - Replicates to the USER bitmap; requires USER width >= M_COUNT.

Signals
-------

Interface ports contain channels in both directions. The table identifies
the selected modport or stream role; member directions follow that interface.

.. list-table:: Public signals and interfaces
   :class: rtl-reference-table
   :header-rows: 1
   :widths: 26 27 17 30

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
     - Active-high reset of transaction and control state.
   * - ``s_axis``
     - ``taxi_axis_if.snk``
     - sink
     - Incoming AXI4-Stream payload and metadata.
   * - ``m_axis[M_COUNT]``
     - ``taxi_axis_if.src``
     - source
     - Outgoing AXI4-Stream payload and metadata.
   * - ``enable``
     - ``logic``
     - input
     - Allows admission of new input frames.
   * - ``drop``
     - ``logic``
     - input
     - Discards the admitted frame.
   * - ``select``
     - ``logic [$clog2(M_COUNT)-1:0]``
     - input
     - Explicit destination output index.

Architecture and operation
--------------------------

One ``s_axis`` feeds ``m_axis[M_COUNT]``. ``enable``, ``drop``, and ``select``
provide explicit control. ``TID_ROUTE``, ``TDEST_ROUTE``, or
``TUSER_BITMAP_ROUTE`` select metadata routing; bitmap mode supports fanout.
Frame routing is retained through the accepted last beat, under the shared
``clk/rst``. Selected multicast sinks participate in stream backpressure.

**Verification:** ``dv/core/openenoc_axis_demux/``. Reference expansion should
record route-field slicing, precedence of routing options, and per-frame
selection/drop examples from the implementation.

Functional scenarios
--------------------

This section reserves space for scenario descriptions and WaveDrom timing
diagrams. The current outline is:

* Explicit selection and frame dropping.
* Unicast metadata routing and multicast fanout.
* Selected-sink backpressure and route retention until frame end.
