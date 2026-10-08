.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-axil-ram:

AXI4-Lite RAM -- openenoc_axil_ram
==================================

Provides byte-writable on-chip memory through an AXI4-Lite slave interface.

**Source:** :download:`openenoc_axil_ram.sv <../../../hw/rtl/core/openenoc_axil_ram.sv>`.

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
   * - ``ADDR_W``
     - ``16``
     - Integer > log2(STRB_W); slave address widths >= ADDR_W
     - Byte-addressed aperture size is 2**ADDR_W bytes; data width comes from the
       AXI4-Lite interfaces.
   * - ``PIPELINE_OUTPUT``
     - ``1'b0``
     - 0 or 1
     - Adds a register to the RAM read response when set.
   * - ``INIT_FILE``
     - ``""``
     - Empty string or readable memory file path
     - Optional $readmemh initialization; empty disables file loading.

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
   * - ``s_axil_wr``
     - ``taxi_axil_if.wr_slv``
     - bidirectional (wr_slv)
     - Incoming AXI4-Lite write channels.
   * - ``s_axil_rd``
     - ``taxi_axil_if.rd_slv``
     - bidirectional (rd_slv)
     - Incoming AXI4-Lite read channels.

Architecture and operation
--------------------------

``s_axil_wr/s_axil_rd`` expose a byte-addressed RAM aperture of width
``ADDR_W``. ``PIPELINE_OUTPUT`` optionally adds a read-response register;
``INIT_FILE`` optionally loads initial contents with ``$readmemh``.
Write strobes control byte lanes. Bus response state uses ``clk/rst``;
memory initialization is separate from transaction-state reset.

The native aperture contains ``2**ADDR_W / STRB_W`` words. ``ADDR_W`` must
allow at least two words, and each bus address must be wide enough to reach the
aperture. Higher system-address bits are truncated to the local RAM address.
The byte-lane count must be a power of two. File initialization fills the
selected words; remaining locations are zero initialized. Transaction reset
does not erase memory contents.

Simultaneous read/write access to one word has no portable read-during-write
value. An integration that requires a specific collision result must prevent
or resolve that collision. Independent addresses permit concurrent read and
write progress through ``s_axil_rd`` and ``s_axil_wr``.

**Verification:** ``dv/core/openenoc_axil_ram/`` and endpoint instruction/data
memory tests. Further reference work should document exact read/write latency,
same-address collision behavior, and initialization-file layout.

Functional scenarios
--------------------

This section reserves space for scenario descriptions and WaveDrom timing
diagrams. The current outline is:

* Read and partial-byte write accesses.
* Optional memory initialization and read-response pipeline.
* Response stalls, reset, and same-address accesses.
