.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-axil-cpuif-adapter:

AXI4-Lite to CPUIF -- openenoc_axil_cpuif_adapter
=================================================

Bridges AXI4-Lite register accesses to a native CPU register interface.

**Source:** :download:`openenoc_axil_cpuif_adapter.sv <../../../hw/rtl/core/openenoc_axil_cpuif_adapter.sv>`.

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
   * - ``RESPONSE_FIFO_DEPTH``
     - ``2``
     - Integer >= 2
     - Number of buffered CPUIF responses, including reserved active-operation
       capacity.

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
   * - ``s_axil_wr``
     - ``taxi_axil_if.wr_slv``
     - bidirectional (wr_slv)
     - Incoming AXI4-Lite write channels.
   * - ``s_axil_rd``
     - ``taxi_axil_if.rd_slv``
     - bidirectional (rd_slv)
     - Incoming AXI4-Lite read channels.
   * - ``m_cpuif``
     - ``openenoc_cpuif_if.mst``
     - bidirectional (mst)
     - Native register-access master toward the target.

Architecture and operation
--------------------------

``s_axil_wr/s_axil_rd`` are AXI4-Lite slave views; ``m_cpuif`` is the native
master. ``RESPONSE_FIFO_DEPTH`` defaults to 2. AXI write address and data
channels are buffered independently. Read and complete write requests are
dispatched to CPUIF with round-robin arbitration.

The response FIFO reserves capacity for the active CPUIF operation, allowing
a new request in the same cycle as the preceding acknowledgement without
losing responses under AXI backpressure. AXI write strobes expand to groups
of eight CPUIF enable bits. CPUIF errors return an AXI error response.
Reset clears buffered requests, the active operation, and response state.

Only one CPUIF operation is outstanding. Both an acknowledgement in the request
cycle and one returned after an arbitrary delay are supported. The next request
can replace the completed operation on the same edge. At least two slots in
``RESPONSE_FIFO_DEPTH`` allow an existing response and a newly dispatched
operation to coexist during that handoff. Connected AXI4-Lite and CPUIF
address/data widths must agree, and native data width must be a multiple of
eight.

**Verification:** ``dv/core/openenoc_axil_cpuif_adapter/``. Queue occupancy
and simultaneous dispatch/completion timing remain reference expansion work.

Functional scenarios
--------------------

This section reserves space for scenario descriptions and WaveDrom timing
diagrams. The current outline is:

* Independent write address and data arrival.
* Read/write arbitration and acknowledgement overlap.
* Response backpressure, target error, and reset.
