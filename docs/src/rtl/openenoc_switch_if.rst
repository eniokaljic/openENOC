.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-switch-if:

Switch CSR/core interface -- openenoc_switch_if
===============================================

.. index::
   single: openenoc_switch_if

Defines the structured configuration and status boundary for switch hardware
and its register bank.

**Source:** :download:`openenoc_switch_if.sv <../../../build/hal/rtl/openenoc_switch_if.sv>`.
**RDL:** :download:`openenoc_switch_interface.rdl <../../../hal/interfaces/openenoc_switch_interface.rdl>`.

Parameters
----------

.. list-table:: Parameters
   :class: rtl-reference-table
   :header-rows: 1
   :widths: 24 18 20 38

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
   :widths: 20 20 17 43

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

Shared-bus and crossbar switches use the same configuration and status fields:
``forwarding_control.operation_mode`` selects managed or unmanaged operation,
``default_forwarding.bitmap`` supplies the destination set for a table miss,
and ``forwarding_table`` exposes one common table through CPUIF. Table entries
and the default route both use egress-port bitmaps, including multicast sets.
``forwarding_control.pause_request`` and ``pause_done`` coordinate forwarding
pause. Arbitration of the crossbar's per-ingress lookup and learning requests
is internal and adds no per-engine software table or control port.

The hardware architecture is selected by ``SWITCH_TYPE`` on
:ref:`rtl-eth-switch` at elaboration, independently of the runtime operation
mode exposed here.
