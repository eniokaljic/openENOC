.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-axil-crossbar-addr:

Address decoder -- openenoc_axil_crossbar_addr
==============================================

Decodes a memory address and access permissions into a crossbar target
selection.

**Source:** :download:`openenoc_axil_crossbar_addr.sv <../../../hw/rtl/core/openenoc_axil_crossbar_addr.sv>`.

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
   * - ``S``
     - ``0``
     - 0..S_COUNT-1
     - Source index used for connectivity checks.
   * - ``S_COUNT``
     - ``4``
     - Integer >= 1
     - Number of upstream initiator interfaces.
   * - ``M_COUNT``
     - ``4``
     - Integer >= 1
     - Number of downstream target/output interfaces.
   * - ``SELECT_W``
     - ``M_COUNT > 1 ? $clog2(M_COUNT) : 1``
     - >= max(1, ceil(log2(M_COUNT)))
     - Width of the decoded target index.
   * - ``ADDR_W``
     - ``32``
     - Integer >= 1
     - Byte-address width in bits; connected interfaces must agree.
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
   * - ``M_SECURE``
     - ``{M_COUNT{1'b0}}``
     - M_COUNT-bit mask
     - A set bit disallows nonsecure accesses to that target.

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
   * - ``addr``
     - ``logic [ADDR_W-1:0]``
     - input
     - Byte address presented to the native interface or decoder.
   * - ``prot``
     - ``logic [2:0]``
     - input
     - AXI access attributes; bit 1 indicates a nonsecure access.
   * - ``match``
     - ``logic``
     - output
     - At least one permitted enabled target region matched.
   * - ``select``
     - ``logic [SELECT_W-1:0]``
     - output
     - Index of the matched target; meaningful only when match is set.

Architecture and operation
--------------------------

The combinational decoder takes ``addr/prot`` and returns ``match/select``.
``S`` identifies the source for connectivity checks; ``S_COUNT/M_COUNT`` and
``SELECT_W`` set matrix/index sizes. Region, connection, and security parameters
follow the crossbar. A zero ``M_BASE_ADDR`` selects automatically placed aligned
regions. ``M_ADDR_W`` defines each enabled region's address span.

There is no clock or reset state. Further reference detail should show aligned
base calculation, disabled regions, and decode miss/security examples.

Functional scenarios
--------------------

This section reserves space for scenario descriptions and WaveDrom timing
diagrams. The current outline is:

* Automatically placed and explicitly configured address regions.
* Disabled regions, connectivity restrictions, and secure accesses.
* Address match and decode miss.
