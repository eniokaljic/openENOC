.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-axil-crossbar-wr:

Crossbar write path -- openenoc_axil_crossbar_wr
================================================

Routes AXI4-Lite write transactions and preserves response ordering for each
initiator.

**Source:** :download:`openenoc_axil_crossbar_wr.sv <../../../hw/rtl/core/openenoc_axil_crossbar_wr.sv>`.

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
   * - ``ADDR_W``
     - ``32``
     - Integer >= 1
     - Byte-address width in bits; connected interfaces must agree.
   * - ``S_ACCEPT``
     - ``{S_COUNT{32'd16}}``
     - One positive 32-bit count per source
     - Maximum accepted outstanding transactions for each source; source 0 occupies
       the least-significant slice.
   * - ``M_REGIONS``
     - ``1``
     - Integer >= 1
     - Number of decode regions per target.
   * - ``M_BASE_ADDR``
     - ``'0``
     - Packed aligned addresses; zero selects automatic placement
     - One ADDR_W-bit base per target region; region index m*M_REGIONS+r starts in
       the least-significant slice.
   * - ``M_ADDR_W``
     - ``{M_COUNT{{M_REGIONS{32'd24}}}}``
     - Zero, or log2(STRB_W)..ADDR_W in crossbar integration
     - Region span is 2**width bytes; zero disables the region. Packing follows
       M_BASE_ADDR.
   * - ``M_CONNECT``
     - ``{M_COUNT{{S_COUNT{1'b1}}}}``
     - Boolean connection matrix
     - Permitted source-to-target paths; target rows and source columns.
   * - ``M_ISSUE``
     - ``{M_COUNT{32'd16}}``
     - One positive 32-bit count per target
     - Maximum issued outstanding transactions for each target; target 0 occupies
       the least-significant slice.
   * - ``M_SECURE``
     - ``{M_COUNT{1'b0}}``
     - M_COUNT-bit mask
     - A set bit disallows nonsecure accesses to that target.

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
   * - ``s_axil_wr[S_COUNT]``
     - ``taxi_axil_if.wr_slv``
     - bidirectional (wr_slv)
     - Incoming AXI4-Lite write channels.
   * - ``m_axil_wr[M_COUNT]``
     - ``taxi_axil_if.wr_mst``
     - bidirectional (wr_mst)
     - Outgoing AXI4-Lite write channels.

Architecture and operation
--------------------------

The pipelined write fabric connects ``s_axil_wr`` to ``m_axil_wr`` arrays.
AW routing creates ordered per-source and per-target transaction queues.
They route independent W transfers to the matching target and retain enough
context to return B responses in source request order. Address-map,
``M_CONNECT``, security, and ``S_ACCEPT/M_ISSUE`` limits follow the wrapper.
Reset clears request routing, queue state, and pending responses.

**Verification:** write scenarios in ``dv/core/openenoc_axil_crossbar/``.
Detailed reference additions should cover separated AW/W arrival, simultaneous
queue progress, and response backpressure.

Functional scenarios
--------------------

This section reserves space for scenario descriptions and WaveDrom timing
diagrams. The current outline is:

* Separated write address and data arrival.
* Concurrent writes, target contention, and queue progress.
* Response backpressure, decode errors, and reset.
