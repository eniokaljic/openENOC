.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-FileCopyrightText: 2026 Kerim Bavcic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-eth-switch-shared-bus:

Shared-bus switch -- openenoc_eth_switch_shared_bus
===================================================

Switches Ethernet traffic through one shared forwarding pipeline.

**Source:** :download:`openenoc_eth_switch_shared_bus.sv <../../../hw/rtl/core/openenoc_eth_switch_shared_bus.sv>`.

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

Ingress adapters feed a shared stream multiplexer. One
:ref:`rtl-axis-forwarding-engine` performs destination lookup and source
learning through one :ref:`rtl-forwarding-table`. A bitmap-controlled demux
replicates or drops the resulting frame at the egress boundary. Ingress
identity accompanies the stream for learning and ingress-port exclusion.
Multicast fanout applies all-or-none backpressure to the selected outputs.

The fabric uses ``clk/rst`` while each Ethernet port retains its own domain.
Pause control takes effect at a frame boundary through the forwarding engine.
Parameter meanings and port orientation follow :ref:`rtl-eth-switch`.

**Verification:** ``dv/core/openenoc_eth_switch_shared_bus/``. Detailed
reference work remains for arbitration timing, aggregate throughput, and
port reset behavior.

Functional scenarios
--------------------

This section reserves space for scenario descriptions and WaveDrom timing
diagrams. The current outline is:

* Ingress arbitration and destination lookup.
* Learning, ingress exclusion, and multicast fanout.
* Selected-output backpressure and frame-boundary pause.
