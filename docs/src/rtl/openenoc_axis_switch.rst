.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-FileCopyrightText: 2026 Kerim Bavcic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-axis-switch:

Stream switch -- openenoc_axis_switch
=====================================

Connects multiple frame streams using unicast or multicast routing and
arbitration.

**Source:** :download:`openenoc_axis_switch.sv <../../../hw/rtl/core/openenoc_axis_switch.sv>`.

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
   * - ``S_COUNT``
     - ``4``
     - Integer >= 1
     - Number of upstream initiator interfaces.
   * - ``M_COUNT``
     - ``4``
     - Integer >= 1
     - Number of downstream target/output interfaces.
   * - ``M_CONNECT``
     - ``'{M_COUNT{'{S_COUNT{1'b1}}}}``
     - M_COUNT by S_COUNT array of 0/1
     - Entry [m][s] permits source s to reach output m.
   * - ``S_REG_TYPE``
     - ``2``
     - 0, 1, or 2
     - Input registration: bypass, simple buffer, or skid buffer.
   * - ``M_REG_TYPE``
     - ``0``
     - 0, 1, or 2
     - Output registration: bypass, simple buffer, or skid buffer.

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
   * - ``tuser_bitmap_route``
     - ``logic``
     - input
     - One routes by USER bitmap; zero routes by DEST output index.
   * - ``s_axis[S_COUNT]``
     - ``taxi_axis_if.snk``
     - sink
     - Incoming AXI4-Stream payload and metadata.
   * - ``m_axis[M_COUNT]``
     - ``taxi_axis_if.src``
     - source
     - Outgoing AXI4-Stream payload and metadata.

Architecture and operation
--------------------------

The switch connects ``s_axis[S_COUNT]`` to ``m_axis[M_COUNT]`` using
``M_CONNECT`` for permitted paths. ``tuser_bitmap_route`` selects multicast
TUSER bitmap routing or unicast routing through TDEST's most significant bits.
``S_REG_TYPE`` and ``M_REG_TYPE`` select input/output registration.
Arbitration and frame ownership operate in ``clk/rst``.

**Verification:** ``dv/core/openenoc_axis_switch/`` and crossbar-switch tests.
Detailed arbitration, multicast acceptance, connectivity constraints, and
register-mode timing remain part of the reference skeleton.

Functional scenarios
--------------------

This section reserves space for scenario descriptions and WaveDrom timing
diagrams. The current outline is:

* Independent routes and output contention.
* Multicast fanout and restricted connectivity.
* Frame ownership and input/output registration choices.
