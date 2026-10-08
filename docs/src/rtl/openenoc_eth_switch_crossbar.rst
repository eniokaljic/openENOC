.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-FileCopyrightText: 2026 Kerim Bavcic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-eth-switch-crossbar:

Crossbar switch -- openenoc_eth_switch_crossbar
===============================================

Switches Ethernet traffic through parallel ingress processing and independently
progressing paths.

**Source:** :download:`openenoc_eth_switch_crossbar.sv <../../../hw/rtl/core/openenoc_eth_switch_crossbar.sv>`.

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

Each ingress has its own :ref:`rtl-axis-forwarding-engine`. Independent lookup
and learning requests share one table through
:ref:`rtl-forwarding-table-arb-mux`. The AXIS switch fabric routes forwarding
bitmaps to egress adapters, permitting independent paths to progress together.
Clock adaptation, ``PORT_SIDE``, public interfaces, and configuration parameters
match the shared-bus variant.

**Verification:** ``dv/core/openenoc_eth_switch_crossbar/``. The documentation
skeleton can be expanded with simultaneous-egress arbitration, multicast
backpressure, and pause/drain timing examples.

Functional scenarios
--------------------

This section reserves space for scenario descriptions and WaveDrom timing
diagrams. The current outline is:

* Concurrent independent routes and shared table arbitration.
* Egress contention and multicast backpressure.
* Per-link clock conversion and fabric pause/drain.
