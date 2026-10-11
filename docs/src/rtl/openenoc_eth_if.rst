.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-eth-if:

Bidirectional Ethernet link -- openenoc_eth_if
==============================================

Defines a bidirectional Ethernet-like link using two independent frame streams.

**Source:** :download:`openenoc_eth_if.sv <../../../hw/rtl/core/openenoc_eth_if.sv>`.

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
     - ``32``
     - Positive multiple of 8
     - Stream data width in bits, shared by both link directions.
   * - ``KEEP_W``
     - ``((DATA_W + 7) / 8)``
     - DATA_W/8 for byte-granular endpoint links
     - Number of byte-valid lanes per stream beat.
   * - ``KEEP_EN``
     - ``KEEP_W > 1``
     - 0 or 1
     - Enables byte-valid masks; disabled means every byte lane is valid.
   * - ``STRB_EN``
     - ``1'b0``
     - 0 or 1
     - Enables stream byte strobes.
   * - ``LAST_EN``
     - ``1'b1``
     - 0 or 1; endpoint frame links require 1
     - Enables frame/fragment termination.
   * - ``ID_EN``
     - ``1'b0``
     - 0 or 1
     - Enables stream ID metadata.
   * - ``ID_W``
     - ``8``
     - Integer >= 1
     - Width of stream ID metadata.
   * - ``DEST_EN``
     - ``1'b0``
     - 0 or 1
     - Enables stream destination metadata.
   * - ``DEST_W``
     - ``8``
     - Integer >= 1
     - Width of stream destination metadata.
   * - ``USER_EN``
     - ``1'b0``
     - 0 or 1
     - Enables stream user metadata.
   * - ``USER_W``
     - ``1``
     - Integer >= 1
     - Width of stream user metadata.

Signals
-------

Directions below are relative to the named link side. Each embedded stream
uses the TAXI source/sink roles; READY travels opposite to data.

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
   * - ``a2b_axis_if``
     - ``taxi_axis_if``
     - A to B; READY B to A
     - Frame stream from side A to side B, with reverse READY.
   * - ``b2a_axis_if``
     - ``taxi_axis_if``
     - B to A; READY A to B
     - Frame stream from side B to side A, with reverse READY.

.. list-table:: Embedded stream signals
   :class: rtl-reference-table
   :header-rows: 1
   :widths: 30 22 18 30

   * - Name
     - Type
     - Direction
     - Description
   * - ``a2b_axis_if.tdata``
     - ``logic [DATA_W-1:0]``
     - A to B
     - Frame data bytes.
   * - ``a2b_axis_if.tkeep``
     - ``logic [KEEP_W-1:0]``
     - A to B
     - Valid-byte mask when KEEP_EN is set.
   * - ``a2b_axis_if.tstrb``
     - ``logic [KEEP_W-1:0]``
     - A to B
     - Data-byte strobes when STRB_EN is set.
   * - ``a2b_axis_if.tid``
     - ``logic [ID_W-1:0]``
     - A to B
     - Stream identifier when ID_EN is set.
   * - ``a2b_axis_if.tdest``
     - ``logic [DEST_W-1:0]``
     - A to B
     - Stream destination when DEST_EN is set.
   * - ``a2b_axis_if.tuser``
     - ``logic [USER_W-1:0]``
     - A to B
     - User metadata when USER_EN is set.
   * - ``a2b_axis_if.tlast``
     - ``logic``
     - A to B
     - Final frame beat when LAST_EN is set.
   * - ``a2b_axis_if.tvalid``
     - ``logic``
     - A to B
     - Current beat is valid.
   * - ``a2b_axis_if.tready``
     - ``logic``
     - B to A
     - Receiver accepts the current beat.
   * - ``b2a_axis_if.tdata``
     - ``logic [DATA_W-1:0]``
     - B to A
     - Frame data bytes.
   * - ``b2a_axis_if.tkeep``
     - ``logic [KEEP_W-1:0]``
     - B to A
     - Valid-byte mask when KEEP_EN is set.
   * - ``b2a_axis_if.tstrb``
     - ``logic [KEEP_W-1:0]``
     - B to A
     - Data-byte strobes when STRB_EN is set.
   * - ``b2a_axis_if.tid``
     - ``logic [ID_W-1:0]``
     - B to A
     - Stream identifier when ID_EN is set.
   * - ``b2a_axis_if.tdest``
     - ``logic [DEST_W-1:0]``
     - B to A
     - Stream destination when DEST_EN is set.
   * - ``b2a_axis_if.tuser``
     - ``logic [USER_W-1:0]``
     - B to A
     - User metadata when USER_EN is set.
   * - ``b2a_axis_if.tlast``
     - ``logic``
     - B to A
     - Final frame beat when LAST_EN is set.
   * - ``b2a_axis_if.tvalid``
     - ``logic``
     - B to A
     - Current beat is valid.
   * - ``b2a_axis_if.tready``
     - ``logic``
     - A to B
     - Receiver accepts the current beat.

Architecture and operation
--------------------------

The link contains two independent ``taxi_axis_if`` instances. Side A drives
``a2b_axis_if`` as a source and receives ``b2a_axis_if`` as a sink; side B uses
the opposite roles. Each direction uses ordinary AXIS ready/valid handshakes,
``TKEEP`` for valid bytes, and ``TLAST`` for frame boundaries.
``DATA_W`` and ``KEEP_W`` set the shared lane geometry. Optional sidebands
are selected independently by their enable parameters; enabled widths must
agree with the connected stream adapters. ``LAST_EN`` is required by endpoint
frame processing.

On-chip Ethernet frames exclude preamble, SFD, and FCS. Internal endpoint
route, role, and sequence metadata does not become Ethernet wire fields.

Functional scenarios
--------------------

This section reserves space for scenario descriptions and WaveDrom timing
diagrams. The current outline is:

* Independent traffic in each direction.
* Partial final beats and optional metadata.
* Endpoint orientation and link clock/reset ownership.
