.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-picorv32-axil-adapter:

PicoRV32 AXI4-Lite adapter -- openenoc_picorv32_axil_adapter
============================================================

Bridges the processor native memory interface to AXI4-Lite using optional look-
ahead capture.

**Source:** :download:`openenoc_picorv32_axil_adapter.sv <../../../hw/rtl/core/openenoc_picorv32_axil_adapter.sv>`.

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
   * - ``resetn``
     - ``logic``
     - input
     - Active-low processor/adapter reset.
   * - ``mem_axi_awvalid``
     - ``logic``
     - output
     - Write-address channel is valid.
   * - ``mem_axi_awready``
     - ``logic``
     - input
     - Write-address channel acceptance.
   * - ``mem_axi_awaddr``
     - ``logic [31:0]``
     - output
     - Write byte address.
   * - ``mem_axi_awprot``
     - ``logic [2:0]``
     - output
     - Write access attributes.
   * - ``mem_axi_wvalid``
     - ``logic``
     - output
     - Write-data channel is valid.
   * - ``mem_axi_wready``
     - ``logic``
     - input
     - Write-data channel acceptance.
   * - ``mem_axi_wdata``
     - ``logic [31:0]``
     - output
     - Write data word.
   * - ``mem_axi_wstrb``
     - ``logic [3:0]``
     - output
     - Write-byte enables.
   * - ``mem_axi_bvalid``
     - ``logic``
     - input
     - Write response is valid.
   * - ``mem_axi_bready``
     - ``logic``
     - output
     - Write-response acceptance.
   * - ``mem_axi_arvalid``
     - ``logic``
     - output
     - Read-address channel is valid.
   * - ``mem_axi_arready``
     - ``logic``
     - input
     - Read-address channel acceptance.
   * - ``mem_axi_araddr``
     - ``logic [31:0]``
     - output
     - Read byte address.
   * - ``mem_axi_arprot``
     - ``logic [2:0]``
     - output
     - Read attributes; instruction fetch sets bit 2.
   * - ``mem_axi_rvalid``
     - ``logic``
     - input
     - Read response is valid.
   * - ``mem_axi_rready``
     - ``logic``
     - output
     - Read-response acceptance.
   * - ``mem_axi_rdata``
     - ``logic [31:0]``
     - input
     - Read data word.
   * - ``mem_valid``
     - ``logic``
     - input
     - Native processor memory request is active.
   * - ``mem_instr``
     - ``logic``
     - input
     - Native memory request is an instruction fetch.
   * - ``mem_ready``
     - ``logic``
     - output
     - Native memory request completed.
   * - ``mem_addr``
     - ``logic [31:0]``
     - input
     - Native byte address.
   * - ``mem_wdata``
     - ``logic [31:0]``
     - input
     - Native write word.
   * - ``mem_wstrb``
     - ``logic [3:0]``
     - input
     - Native write-byte mask; zero selects a read.
   * - ``mem_rdata``
     - ``logic [31:0]``
     - output
     - Native read word.
   * - ``mem_la_read``
     - ``logic``
     - input
     - Look-ahead read request for capture.
   * - ``mem_la_write``
     - ``logic``
     - input
     - Look-ahead write request for capture.
   * - ``mem_la_addr``
     - ``logic [31:0]``
     - input
     - Look-ahead byte address.
   * - ``mem_la_wdata``
     - ``logic [31:0]``
     - input
     - Look-ahead write word.
   * - ``mem_la_wstrb``
     - ``logic [3:0]``
     - input
     - Look-ahead write-byte mask.

Architecture and operation
--------------------------

The adapter converts native ``mem_valid/mem_ready`` requests and look-ahead
``mem_la_*`` signals to flattened AXI4-Lite AW/W/B and AR/R channels.
It captures look-ahead address/data/strobes, retains the request through
independent channel stalls, and completes native memory access when the matching
AXI response is available. The boundary carries 32-bit address/data and four
byte strobes. ``clk/resetn`` use the processor's active-low reset convention.

This flattened processor-facing interface has no BRESP/RRESP inputs; detailed
error propagation must be considered at its integration boundary rather than
assumed from native completion alone.

**Verification:** ``dv/core/openenoc_picorv32_axil_adapter/``. Add timing diagrams
for consecutive look-ahead requests and independently stalled AXI channels.

Functional scenarios
--------------------

This section reserves space for scenario descriptions and WaveDrom timing
diagrams. The current outline is:

* Native requests with and without look-ahead.
* Independent write address/data handshakes and read stalls.
* Consecutive requests, partial writes, and reset recovery.
