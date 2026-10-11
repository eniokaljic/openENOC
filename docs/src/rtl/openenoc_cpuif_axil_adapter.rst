.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-cpuif-axil-adapter:

CPUIF to AXI4-Lite -- openenoc_cpuif_axil_adapter
=================================================

Converts native CPU register accesses into AXI4-Lite memory transactions.

**Source:** :download:`openenoc_cpuif_axil_adapter.sv <../../../hw/rtl/core/openenoc_cpuif_axil_adapter.sv>`.

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
   * - ``s_cpuif``
     - ``openenoc_cpuif_if.slv``
     - bidirectional (slv)
     - Native register-access slave accepting requests.
   * - ``m_axil_wr``
     - ``taxi_axil_if.wr_mst``
     - bidirectional (wr_mst)
     - Outgoing AXI4-Lite write channels.
   * - ``m_axil_rd``
     - ``taxi_axil_if.rd_mst``
     - bidirectional (rd_mst)
     - Outgoing AXI4-Lite read channels.

Architecture and operation
--------------------------

``s_cpuif`` is the native slave; ``m_axil_wr/m_axil_rd`` are AXI4-Lite master
views. Address/data widths are taken from the interfaces and must agree.
CPUIF data width must be a multiple of eight.

A request may launch directly into the AXI address/data channels. Its context
is retained until every applicable request channel is accepted and the response
completes. A new request can launch in the preceding acknowledgement cycle,
allowing consecutive transfers without an idle cycle. Non-OKAY AXI responses
assert the corresponding CPUIF ERR with ACK.

CPUIF write enables must be uniform within each byte because AXI4-Lite provides
one strobe per byte lane. This boundary cannot preserve arbitrary independent
per-bit enables. Reset clears retained request and channel state.

**Verification:** ``dv/core/openenoc_cpuif_axil_adapter/``. Add request-channel
stall and completion overlap diagrams to the reference.

Functional scenarios
--------------------

This section reserves space for scenario descriptions and WaveDrom timing
diagrams. The current outline is:

* Read and byte-enabled write accesses.
* Independent request-channel stalls and completion overlap.
* AXI error response, acknowledgement, and reset.
