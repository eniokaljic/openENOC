.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-endpoint-full-csr:

Full endpoint register block -- openenoc_endpoint_full_csr
==========================================================

.. index::
   single: openenoc_endpoint_full_csr

Implements the generated software-visible register bank and its hardware update
boundary.

**Source:** :download:`openenoc_endpoint_full_csr.sv <../../../build/hal/openenoc_endpoint_full/rtl/openenoc_endpoint_full_csr.sv>`.
**RDL:** :download:`openenoc_endpoint_full.rdl <../../../hal/endpoints/openenoc_endpoint_full.rdl>`.

Parameters
----------

.. list-table:: Parameters
   :class: rtl-reference-table
   :header-rows: 1
   :widths: 12 18 20 50

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
   :widths: 20 38 17 25

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

Transport configuration and status
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The endpoint register interface exposes the following transport controls.
Names below are relative to the endpoint register file within the generated
CSR map.

.. list-table:: Transport controls and their hardware owners
   :class: rtl-reference-table
   :header-rows: 1
   :widths: 37 40 23

   * - Register field
     - Meaning
     - Hardware consumer or owner
   * - ``conf.mac_address`` / ``conf.multicast_address``
     - Individual identity and accepted group destination. Zero disables group
       reception; broadcast requires the broadcast address in the group field.
     - :ref:`rtl-oetp-engine`
   * - ``conf.rmem_timeout.cycles``
     - 32-bit unicast RMEM response wait in endpoint clock cycles; zero disables
       the timer.
     - :ref:`rtl-oetp-engine`
   * - ``conf.dma_timeout.cycles``
     - 32-bit response wait for each unicast DMA fragment; zero disables the
       timer. There is no whole-block timer.
     - :ref:`rtl-oetp-engine`
   * - ``conf.dma_max_fragment_size.bytes``
     - Maximum locally initiated fragment size, rounded down to four bytes and
       saved at block acceptance. Resets to 8160 bytes for the default frame limit.
     - :ref:`rtl-dma-engine`
   * - ``peers.entry[n].dma.error`` / ``error_code``
     - Shared sticky RMEM/DMA failure record, including received-request failures.
       Cleared by ``dma.clear_error``; a simultaneous new failure wins.
     - :ref:`rtl-dma-engine`

``MAX_RAW_FRAME_SIZE`` is an RDL synthesis parameter, not a writable transport
setting. It fixes the raw frame ceiling and the derived DMA fragment ceiling.
The software-selected fragment size affects locally initiated blocks; received
requests remain bounded by the synthesized ceiling. The size calculations and
timer start/stop rules are specified in :ref:`rtl-oetp-engine`.

RMEM and bulk DMA use the same peer error record but separate RMEM_ERROR and
PEER_DMA_COMPLETE notification sources. Error recording, IRQ enable, and IRQ
claim completion are independent: completing a claim does not clear the error.
Failed incoming requests preserve the status of independent locally initiated
work. Memory completion and error ownership belong to :ref:`rtl-dma-engine`;
event admission and software claims belong to :ref:`rtl-endpoint-irq-controller`.

.. _verification-openenoc-endpoint-full-csr:

Verification
------------

The test suite is in ``dv/hal/openenoc_endpoint_full/``.

Testbench
~~~~~~~~~

This cocotb suite verifies the generated full-endpoint CSR RTL through AXI4-Lite using the
generated PeakRDL Python register model. A thin SV wrapper supplies hardware status and command
acknowledgements. Seven existing cases run through the cocotb Makefile flow; this suite has no
pytest parameter sweep. FST tracing is enabled on every simulation run.

Coverage
~~~~~~~~

The suite covers:

- callback-driven Python register-model access to actual AXI4-Lite RTL;

- test register and multi-field register writes, readback, and defaults;

- full-width RMEM/DMA timeout storage and neighboring-register preservation;

- independent unicast/multicast MAC configuration and RMEM_ERROR IRQ enable;

- fragment-size reset, generated register ordering, and unrounded readback;

- per-peer sticky error status and independently acknowledged clear commands;

- independent raw TX/RX error records and held ``clear_errors`` acknowledgements.
