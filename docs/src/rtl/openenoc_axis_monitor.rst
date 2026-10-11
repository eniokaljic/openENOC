.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-axis-monitor:

Stream monitor -- openenoc_axis_monitor
=======================================

Passes a stream through while sampling its activity for a status output.

**Source:** :download:`openenoc_axis_monitor.sv <../../../hw/rtl/core/openenoc_axis_monitor.sv>`.

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
   * - ``m_axis``
     - ``taxi_axis_if.src``
     - source
     - Outgoing AXI4-Stream payload and metadata.
   * - ``is_idle``
     - ``logic``
     - output
     - Registered sample of preceding-cycle input TVALID; see operation caveat.

Architecture and operation
--------------------------

The monitor transparently connects ``s_axis`` to ``m_axis`` at equal data width,
passing ready/valid and enabled sidebands. Disabled sidebands are filled with
their default values. The output named ``is_idle`` currently samples the
preceding cycle's ``s_axis.tvalid`` and resets to zero; it is not derived from
accepted TLAST or a count of active frames. This records the current RTL
expression rather than defining a new idle/drain guarantee.

Further reference work should identify consumers and document the intended
meaning of this monitor output before it is used for frame-drain decisions.

Functional scenarios
--------------------

This section reserves space for scenario descriptions and WaveDrom timing
diagrams. The current outline is:

* Continuous transfers and idle gaps.
* Backpressure and disabled-sideband defaults.
* Reset and the implemented activity-sample semantics.
