.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-endpoint-full:

Full endpoint -- openenoc_endpoint_full
=======================================

Combines a processor, local memories, register control, and transport into a
complete reference endpoint.

**Source:** :download:`openenoc_endpoint_full.sv <../../../hw/rtl/endpoints/openenoc_endpoint_full.sv>`.

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
   * - ``IMEM_INIT_FILE``
     - ``""``
     - Empty string or readable memory file path
     - Optional instruction-memory $readmemh initialization.
   * - ``DMEM_INIT_FILE``
     - ``""``
     - Empty string or readable memory file path
     - Optional data-memory $readmemh initialization.

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
   * - ``switch_if``
     - ``openenoc_switch_if.csr``
     - bidirectional (csr)
     - Switch configuration, pause status, and forwarding-table CPU access.
   * - ``eth_if``
     - ``openenoc_eth_if``
     - bidirectional; endpoint is side A
     - Bidirectional Ethernet-like transport; this endpoint is side A.

Architecture and operation
--------------------------

The reference endpoint combines PicoRV32, instruction/data RAM, generated
CSR/HAL blocks, and :ref:`rtl-endpoint-interface`. Its public boundary is
``clk``, ``rst``, ``switch_if`` for switch control, and ``eth_if`` for transport.
``IMEM_INIT_FILE`` and ``DMEM_INIT_FILE`` optionally initialize memory using
``$readmemh``-compatible files.

Memory widths, depths, base addresses, and DMA infrastructure limits come from
the generated endpoint packages rather than a second handwritten map. The
AXI4-Lite interconnect has four initiators: CPU, DMA, debug/programming, and
local RMEM execution through the DMA-owned CPUIF. Its three targets are DMEM,
IMEM, and CSR, in that packed target order. Adapters connect the endpoint's
AXI/CPUIF boundaries to AXI4-Lite memory access.

Memory map and interrupt integration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The current generated configuration uses the following decode apertures. The
register map itself remains specified by :doc:`../hal`; these addresses are
obtained from ``openenoc_endpoint_full_pkg`` and
``openenoc_endpoint_full_csr_pkg``.

.. list-table:: Reference endpoint memory map
   :class: rtl-reference-table
   :header-rows: 1
   :widths: 20 30 25 25

   * - Target
     - Base address
     - Decode aperture
     - Crossbar target
   * - IMEM
     - ``0x0000_0000``
     - 32 KiB
     - 1
   * - DMEM
     - ``0x1000_0000``
     - 32 KiB
     - 0
   * - CSR
     - ``0x2000_0000``
     - 8 KiB
     - 2

``IMEM_INIT_FILE`` supplies the boot image; ``DMEM_INIT_FILE`` can independently
initialize data memory. The CPU initiator uses :ref:`rtl-picorv32` and its
native-to-AXI4-Lite adapter. The reserved debug/program initiator is currently
tied inactive. DMA memory access uses an AXI4-to-AXI4-Lite adapter; received
RMEM access uses :ref:`rtl-cpuif-axil-adapter`. Both memory-access paths belong
to DMA, while oETP performs protocol processing.

The endpoint interrupt drives processor ``irq[3]`` as a level-sensitive source;
inputs 0..2 remain available for the core's internal interrupt sources. The
generated capability reports ``info.irq_supported = 1``. Processor ``eoi`` does
not retire an endpoint claim: software completes its exact token through
``irq.complete``. The platform reset vector is ``0x0`` and its interrupt vector
is ``0x10``. The software interrupt wrapper saves the interrupted context,
calls ``openenoc_endpoint_irq_handler``, restores the context, and returns with
``retirq``.

The existing firmware acceptance test uses a 66-byte direct frame, a filtered
broadcast destination, and unicast source. Its IRQ handler consumes received
CSR words into DMEM before the final frame beat arrives. Active peer DMA and
RMEM operations are verified by the component and endpoint-interface suites;
the firmware smoke test retains its current direct-stream coverage.

**Verification:** ``dv/endpoints/openenoc_endpoint_full/`` and
``dv/hal/openenoc_endpoint_full/``. Further reference detail should describe
the complete reset/boot sequence and each initiator's memory-map permissions.

Functional scenarios
--------------------

This section reserves space for scenario descriptions and WaveDrom timing
diagrams. The current outline is:

* Memory initialization, reset, and firmware boot.
* Processor access to instruction memory, data memory, and registers.
* Direct frame loopback with continuous and stalled transport.
* Interrupt entry, token completion, and firmware success reporting.
