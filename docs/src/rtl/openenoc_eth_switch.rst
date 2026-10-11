.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-FileCopyrightText: 2026 Kerim Bavcic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-eth-switch:

Switch architecture selector -- openenoc_eth_switch
===================================================

Selects and instantiates the Ethernet switching fabric for a group of links.

**Source:** :download:`openenoc_eth_switch.sv <../../../hw/rtl/core/openenoc_eth_switch.sv>`.

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
   * - ``SWITCH_TYPE``
     - ``0``
     - 0 or 1
     - Selects shared-bus or crossbar switching architecture.
   * - ``NUM_OF_INTERFACES``
     - ``4``
     - 2..32
     - Number of Ethernet ports and forwarding-bitmap width; match the switch
       interface.
   * - ``TABLE_DEPTH``
     - ``32``
     - Integer >= 1
     - Number of forwarding-table entries.
   * - ``FABRIC_DATA_W``
     - ``32``
     - 8..512 bits, multiple of 8 in forwarding integration
     - Internal switching stream width; link/fabric widths must have an integer
       ratio.
   * - ``PORT_SIDE``
     - ``'1``
     - NUM_OF_INTERFACES-bit mask
     - Port orientation: zero is side A, one is side B.
   * - ``PORT_FIFO_DEPTH``
     - ``64``
     - Bytes; >= 2 widest-side words, power-of-two word count
     - Per-port asynchronous FIFO capacity; divisible by the widest link/fabric
       word size.

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
     - ``openenoc_switch_if.core``
     - bidirectional (core)
     - Switch configuration, pause status, and forwarding-table CPU access.
   * - ``eth_if [NUM_OF_INTERFACES-1:0]``
     - ``openenoc_eth_if``
     - bidirectional; PORT_SIDE per port
     - Per-port bidirectional links, each with its own clock/reset domain.

Architecture and operation
--------------------------

``SWITCH_TYPE`` selects the implementation at elaboration: 0 for
:ref:`rtl-eth-switch-shared-bus`, 1 for :ref:`rtl-eth-switch-crossbar`.
The public ``clk/rst``, ``switch_if``, and ``eth_if`` array are common to both.

Both variants expose ``NUM_OF_INTERFACES``, ``TABLE_DEPTH``, ``FABRIC_DATA_W``,
``PORT_SIDE``, and ``PORT_FIFO_DEPTH``. ``PORT_SIDE[i]`` identifies whether the
switch is side A (0) or side B (1) of port i; the default is side B for every
port. Per-port FIFO adapters bridge link domains into the fabric domain.
Forwarding control and table access come from :ref:`rtl-switch-if`.

Functional scenarios
--------------------

This section reserves space for scenario descriptions and WaveDrom timing
diagrams. The current outline is:

* Shared-bus and crossbar implementations.
* Port orientation and asynchronous link adaptation.
* Forwarding control, table access, and pause propagation.
