.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-endpoint-full-csr:

Full endpoint register block -- openenoc_endpoint_full_csr
==========================================================

Implements the generated software-visible register bank and its hardware update
boundary.

**Source:** :download:`openenoc_endpoint_full_csr.sv <../../../build/hal/openenoc_endpoint_full/rtl/openenoc_endpoint_full_csr.sv>`.
**RDL:** :download:`openenoc_endpoint_full.rdl <../../../hal/endpoints/openenoc_endpoint_full.rdl>`.

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

The hardware-interface types are imported from
``openenoc_endpoint_full_csr_pkg``.

.. list-table:: Public signals and interfaces
   :class: rtl-reference-table
   :header-rows: 1
   :widths: 26 27 17 30

   * - Name
     - Type
     - Direction / role
     - Description
   * - ``clk``
     - ``wire``
     - input
     - Clock for this component or interface domain.
   * - ``rst``
     - ``wire``
     - input
     - Active-high reset of transaction and control state.
   * - ``s_axil_awready``
     - ``logic``
     - output
     - Write-address channel acceptance.
   * - ``s_axil_awvalid``
     - ``wire``
     - input
     - Write-address channel is valid.
   * - ``s_axil_awaddr``
     - ``[12:0]``
     - input
     - Write byte address.
   * - ``s_axil_awprot``
     - ``[2:0]``
     - input
     - Write access attributes.
   * - ``s_axil_wready``
     - ``logic``
     - output
     - Write-data channel acceptance.
   * - ``s_axil_wvalid``
     - ``wire``
     - input
     - Write-data channel is valid.
   * - ``s_axil_wdata``
     - ``[31:0]``
     - input
     - Write data word.
   * - ``s_axil_wstrb``
     - ``[3:0]``
     - input
     - Write-byte enables.
   * - ``s_axil_bready``
     - ``wire``
     - input
     - Write-response acceptance.
   * - ``s_axil_bvalid``
     - ``logic``
     - output
     - Write response is valid.
   * - ``s_axil_bresp``
     - ``logic [1:0]``
     - output
     - Write response: OKAY or AXI error.
   * - ``s_axil_arready``
     - ``logic``
     - output
     - Read-address channel acceptance.
   * - ``s_axil_arvalid``
     - ``wire``
     - input
     - Read-address channel is valid.
   * - ``s_axil_araddr``
     - ``[12:0]``
     - input
     - Read byte address.
   * - ``s_axil_arprot``
     - ``[2:0]``
     - input
     - Read attributes; instruction fetch sets bit 2.
   * - ``s_axil_rready``
     - ``wire``
     - input
     - Read-response acceptance.
   * - ``s_axil_rvalid``
     - ``logic``
     - output
     - Read response is valid.
   * - ``s_axil_rdata``
     - ``logic [31:0]``
     - output
     - Read data word.
   * - ``s_axil_rresp``
     - ``logic [1:0]``
     - output
     - Read response: OKAY or AXI error.
   * - ``hwif_in``
     - ``openenoc_endpoint_full_csr__in_t``
     - input
     - Hardware-driven register updates, command clears, and external target
       responses.
   * - ``hwif_out``
     - ``openenoc_endpoint_full_csr__out_t``
     - output
     - Stored software controls and external register-file requests.

Architecture and operation
--------------------------

PeakRDL-regblock generates the flattened AXI4-Lite CSR target and hardware
interface structures. It implements register storage, decode, readback, and
software/hardware field access semantics, forwarding external RMEM and table
accesses to their request/completion boundaries. Register addresses and field
layouts are derived from RDL; integration must use generated constants.

Functional scenarios
--------------------

This section reserves space for scenario descriptions and WaveDrom timing
diagrams. The current outline is:

* AXI4-Lite register reads and writes through the generated Python model.
* Configuration storage, reset values, and neighboring-field preservation.
* Hardware status injection and acknowledged error-clear commands.
