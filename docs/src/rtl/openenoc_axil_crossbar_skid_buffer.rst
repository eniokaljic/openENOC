.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-axil-crossbar-skid-buffer:

Crossbar elastic buffer -- openenoc_axil_crossbar_skid_buffer
=============================================================

Provides an elastic pipeline boundary that absorbs delayed downstream
backpressure.

**Source:** :download:`openenoc_axil_crossbar_skid_buffer.sv <../../../hw/rtl/core/openenoc_axil_crossbar_skid_buffer.sv>`.

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
   * - ``DATA_W``
     - ``1``
     - Integer >= 1
     - Packed channel payload width in bits.

Signals
-------

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
   * - ``s_data``
     - ``logic [DATA_W-1:0]``
     - input
     - Packed upstream payload.
   * - ``s_valid``
     - ``logic``
     - input
     - Upstream payload is valid.
   * - ``s_ready``
     - ``logic``
     - output
     - Registered upstream acceptance indication.
   * - ``m_data``
     - ``logic [DATA_W-1:0]``
     - output
     - Packed downstream payload.
   * - ``m_valid``
     - ``logic``
     - output
     - Downstream payload is valid.
   * - ``m_ready``
     - ``logic``
     - input
     - Downstream acceptance indication.

Architecture and operation
--------------------------

``DATA_W`` sets packed payload width. ``s_data/s_valid/s_ready`` and
``m_data/m_valid/m_ready`` form a two-entry elastic channel with registered
input READY. After initial fill it can accept and emit one transfer per clock.
The temporary register absorbs a transfer when downstream backpressure arrives
too late to withdraw registered input READY. Reset clears valid state.

**Verification:** exercised within crossbar channel/backpressure tests.
Timing diagrams for bypass, temporary occupancy, and recovery can extend this
reference skeleton.

Functional scenarios
--------------------

This section reserves space for scenario descriptions and WaveDrom timing
diagrams. The current outline is:

* Initial fill and continuous transfers.
* Downstream stall with temporary-buffer occupancy.
* Simultaneous refill, recovery, and reset.
