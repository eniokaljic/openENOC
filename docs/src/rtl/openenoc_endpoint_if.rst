.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-endpoint-if:

Endpoint CSR/core interface -- openenoc_endpoint_if
===================================================

Defines the structured control and status boundary between endpoint hardware
and its register bank.

**Source:** :download:`openenoc_endpoint_if.sv <../../../build/hal/rtl/openenoc_endpoint_if.sv>`.
**RDL:** :download:`openenoc_endpoint_interface.rdl <../../../hal/interfaces/openenoc_endpoint_interface.rdl>`.

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
   * - ``RMEM_TOTAL_DEPTH``
     - ``256``
     - Integer >= 1, in 32-bit words
     - Size of the external scalar-memory aperture.
   * - ``NUM_OF_PEERS``
     - ``1``
     - Integer >= 1; match generated CSR array
     - Number of peer-table entries.

Signals
-------

Directions are relative to the named modport. The monitor modport, where
present, observes signals as inputs and does not drive them.

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
   * - ``core_to_csr``
     - ``core_to_csr_t``
     - csr: input; core: output
     - Hardware status, next-value updates, acknowledgements, and command clears.
   * - ``csr_to_core``
     - ``csr_to_core_t``
     - csr: output; core: input
     - Stored software configuration, pending commands, and external register
       requests.

Architecture and operation
--------------------------

The interface provides ``csr_to_core`` and ``core_to_csr`` structured signals,
with ``csr`` and ``core`` modports. Parameters ``RMEM_TOTAL_DEPTH`` and
``NUM_OF_PEERS`` set the external RMEM aperture and peer array. The RMEM
byte-address width is derived from the aperture size. The interface carries
configuration, direct/raw DMA controls, IRQ state, peer fields, and the external
RMEM request/ACK/read-data boundary. ``clk/rst`` belong to the endpoint domain.
Each connected core block owns its assigned fields.

Functional scenarios
--------------------

This section reserves space for scenario descriptions and WaveDrom timing
diagrams. The current outline is:

* Configuration and per-peer control updates.
* Direct-stream, raw-DMA, and interrupt status exchange.
* External scalar memory request, acknowledgement, and read data.
