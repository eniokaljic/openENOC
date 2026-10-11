.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-axil-crossbar-rd:

Crossbar read path -- openenoc_axil_crossbar_rd
===============================================

Routes AXI4-Lite read requests and returns their responses to the requesting
initiators.

**Source:** :download:`openenoc_axil_crossbar_rd.sv <../../../hw/rtl/core/openenoc_axil_crossbar_rd.sv>`.

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
   * - ``s_axil_rd[S_COUNT]``
     - ``taxi_axil_if.rd_slv``
     - bidirectional (rd_slv)
     - Incoming AXI4-Lite read channels.
   * - ``m_axil_rd[M_COUNT]``
     - ``taxi_axil_if.rd_mst``
     - bidirectional (rd_mst)
     - Outgoing AXI4-Lite read channels.

Architecture and operation
--------------------------

The pipelined read fabric arbitrates AR requests and retains routing context
for R responses. Source and target queues track outstanding operations within
``S_ACCEPT/M_ISSUE`` limits. ``s_axil_rd`` and ``m_axil_rd`` connect the slave
and master interface arrays. Address-map, ``M_CONNECT``, and security parameters
follow the wrapper. Reset clears routing and response state.

**Verification:** read scenarios in ``dv/core/openenoc_axil_crossbar/``.
State/queue timing, decode-error responses, and cross-target ordering examples
remain to be documented in detail.

Functional scenarios
--------------------

This section reserves space for scenario descriptions and WaveDrom timing
diagrams. The current outline is:

* Concurrent requests to independent targets.
* Target contention and outstanding-request limits.
* Response stalls, decode errors, and reset.
