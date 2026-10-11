.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-FileCopyrightText: 2026 Kerim Bavcic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-axis-header-parser:

Header parser -- openenoc_axis_header_parser
============================================

Captures an Ethernet header and attaches it as metadata to the unchanged frame
stream.

**Source:** :download:`openenoc_axis_header_parser.sv <../../../hw/rtl/core/openenoc_axis_header_parser.sv>`.

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
   * - ``DEPTH``
     - ``0``
     - 0 or positive integer; rounded FIFO must hold the header
     - Requested buffer beats, rounded up to a power of two with minimum two. Zero
       selects twice the beat count for the first 16 bytes.
   * - ``M_REG_TYPE``
     - ``2``
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
   * - ``s_axis``
     - ``taxi_axis_if.snk``
     - sink
     - Incoming AXI4-Stream payload and metadata.
   * - ``m_axis``
     - ``taxi_axis_if.src``
     - source
     - Outgoing AXI4-Stream payload and metadata.

Architecture and operation
--------------------------

The parser snoops the first 16 frame bytes and presents them as a raw 128-bit
``m_axis.tuser`` value, stable for the entire output frame. ``TDATA`` passes
unchanged with a header-sized delay, allowing metadata to accompany the first
output beat. Byte zero, the first byte on the wire, is the most significant
byte of the metadata.

.. list-table:: Header metadata
   :header-rows: 1
   :widths: 25 75

   * - TUSER bits
     - Field
   * - 127:80
     - Destination MAC
   * - 79:32
     - Source MAC
   * - 31:16
     - EtherType
   * - 15:8
     - oETP Magic
   * - 7:0
     - oETP Cmd

``DEPTH = 0`` selects automatic buffering of twice the header beat count.
``M_REG_TYPE`` selects bypass (0), simple (1), or skid (2) output registration.
``s_axis`` and ``m_axis`` share ``clk/rst``. This block captures the header;
the detailed command parser belongs to :ref:`rtl-oetp-engine`.

**Verification:** ``dv/core/openenoc_axis_header_parser/``. Short-frame and
partial-beat timing diagrams remain to be added to the reference.

Functional scenarios
--------------------

This section reserves space for scenario descriptions and WaveDrom timing
diagrams. The current outline is:

* Complete header capture and byte ordering.
* Short frames and partially populated final beats.
* Header buffering and output backpressure.
