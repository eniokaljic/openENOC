.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-axil-crossbar:

AXI4-Lite crossbar -- openenoc_axil_crossbar
============================================

Connects several AXI4-Lite initiators to a shared set of memory and register
targets.

**Source:** :download:`openenoc_axil_crossbar.sv <../../../hw/rtl/core/openenoc_axil_crossbar.sv>`.

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
   * - ``M_CONNECT_RD``
     - ``{M_COUNT{{S_COUNT{1'b1}}}}``
     - M_COUNT*S_COUNT-bit mask
     - Permitted read paths; bit m*S_COUNT+s connects source s to target m.
   * - ``M_CONNECT_WR``
     - ``{M_COUNT{{S_COUNT{1'b1}}}}``
     - M_COUNT*S_COUNT-bit mask
     - Permitted write paths; bit m*S_COUNT+s connects source s to target m.
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
   * - ``s_axil_rd[S_COUNT]``
     - ``taxi_axil_if.rd_slv``
     - bidirectional (rd_slv)
     - Incoming AXI4-Lite read channels.
   * - ``m_axil_wr[M_COUNT]``
     - ``taxi_axil_if.wr_mst``
     - bidirectional (wr_mst)
     - Outgoing AXI4-Lite write channels.
   * - ``m_axil_rd[M_COUNT]``
     - ``taxi_axil_if.rd_mst``
     - bidirectional (rd_mst)
     - Outgoing AXI4-Lite read channels.

Architecture and operation
--------------------------

The wrapper combines independent read and write paths, connecting
``s_axil_rd/s_axil_wr[S_COUNT]`` to ``m_axil_rd/m_axil_wr[M_COUNT]``.
``ADDR_W`` sets decoding width. ``S_ACCEPT`` and ``M_ISSUE`` bound source
acceptance and target issue capacity. ``M_REGIONS``, ``M_BASE_ADDR``, and
``M_ADDR_W`` define target regions; ``M_CONNECT_RD/M_CONNECT_WR`` restrict
connectivity, and ``M_SECURE`` restricts nonsecure accesses.

**Verification:** ``dv/core/openenoc_axil_crossbar/`` and full-endpoint tests.
The detailed source/target queue relationships belong to the path descriptions
below; future reference work should add parameter packing and ordering examples.

Functional scenarios
--------------------

This section reserves space for scenario descriptions and WaveDrom timing
diagrams. The current outline is:

* Concurrent reads and writes to different targets.
* Competing initiators, acceptance limits, and ordered responses.
* Decode misses, restricted connectivity, and reset.
