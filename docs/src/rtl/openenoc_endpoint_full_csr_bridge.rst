.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-endpoint-full-csr-bridge:

Full endpoint CSR bridge -- openenoc_endpoint_full_csr_bridge
=============================================================

Connects the generated register bank to endpoint and switch control interfaces.

**Source:** :download:`openenoc_endpoint_full_csr_bridge.sv <../../../build/hal/openenoc_endpoint_full/rtl/openenoc_endpoint_full_csr_bridge.sv>`.

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

Interface ports contain channels in both directions. The table identifies
the selected modport or stream role; member directions follow that interface.

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
   * - ``csr_hwif_out``
     - ``openenoc_endpoint_full_csr__out_t``
     - input
     - Register-bank controls mapped onto endpoint and switch interfaces.
   * - ``csr_hwif_in``
     - ``openenoc_endpoint_full_csr__in_t``
     - output
     - Core status and acknowledgements mapped back into the register bank.
   * - ``endpoint_if``
     - ``openenoc_endpoint_if.csr``
     - bidirectional (csr)
     - Endpoint configuration, commands, status, and external scalar-memory access.
   * - ``switch_if``
     - ``openenoc_switch_if.csr``
     - bidirectional (csr)
     - Switch configuration, pause status, and forwarding-table CPU access.

Architecture and operation
--------------------------

The project exporter connects PeakRDL ``csr_hwif_out/csr_hwif_in`` to
``endpoint_if`` and ``switch_if``. This generated wiring layer converts
matching struct views, including value, next, hardware-clear, and external
request/completion members. It does not execute memory or protocol operations.

Functional scenarios
--------------------

This section reserves space for scenario descriptions and WaveDrom timing
diagrams. The current outline is:

* Software configuration propagation to core interfaces.
* Hardware status and command-clear propagation to the register bank.
* External register-file request and acknowledgement mapping.
