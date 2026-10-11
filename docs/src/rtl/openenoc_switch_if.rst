.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-switch-if:

Switch CSR/core interface -- openenoc_switch_if
===============================================

Defines the structured configuration and status boundary for switch hardware
and its register bank.

**Source:** :download:`openenoc_switch_if.sv <../../../build/hal/rtl/openenoc_switch_if.sv>`.
**RDL:** :download:`openenoc_switch_interface.rdl <../../../hal/interfaces/openenoc_switch_interface.rdl>`.

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
   * - ``NUM_OF_INTERFACES``
     - ``1``
     - 1..32
     - Port count and forwarding-bitmap width.
   * - ``TABLE_DEPTH``
     - ``1``
     - Integer >= 1
     - Number of forwarding-table entries.

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

The ``csr`` and ``core`` modports connect forwarding control, pause handshake,
default forwarding bitmap, and external forwarding-table CPUIF signals.
``TABLE_DEPTH`` and ``NUM_OF_INTERFACES`` determine the table aperture and
port-bitmap width. The switch consumes the ``core`` view; the endpoint's
generated bridge drives the ``csr`` view.

Functional scenarios
--------------------

This section reserves space for scenario descriptions and WaveDrom timing
diagrams. The current outline is:

* Forwarding mode and default-bitmap configuration.
* Pause request and completed drain.
* External forwarding-table register accesses.
