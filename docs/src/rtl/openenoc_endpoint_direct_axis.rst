.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-endpoint-direct-axis:

Direct CSR stream -- openenoc_endpoint_direct_axis
==================================================

Connects software-controlled direct frame streams to endpoint transport and
interrupt reporting.

**Source:** :download:`openenoc_endpoint_direct_axis.sv <../../../hw/rtl/core/openenoc_endpoint_direct_axis.sv>`.

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
   * - ``tx_frame_done``
     - ``logic``
     - input
     - Final direct-frame beat accepted at the oETP input after FIFO/mux transport.
   * - ``endpoint_if``
     - ``openenoc_endpoint_if.core``
     - bidirectional (core)
     - Endpoint configuration, commands, status, and external scalar-memory access.
   * - ``m_axis_csr_tx``
     - ``taxi_axis_if.src``
     - source
     - Software-controlled transmit frame stream.
   * - ``s_axis_csr_rx``
     - ``taxi_axis_if.snk``
     - sink
     - Receive frame stream consumed through CSR reads.
   * - ``tx_event_if``
     - ``openenoc_irq_event_if.producer``
     - bidirectional (producer)
     - Direct transmit completion-event producer.
   * - ``rx_event_if``
     - ``openenoc_irq_event_if.producer``
     - bidirectional (producer)
     - Direct receive-availability event producer.

Architecture and operation
--------------------------

This block translates direct CSR stream handshakes to ``m_axis_csr_tx`` and
``s_axis_csr_rx``. ``endpoint_if`` carries data/control/status, while
``tx_event_if`` and ``rx_event_if`` provide separate IRQ producers.

Separate TX and RX clocked processes own direct-stream state and CSR
acknowledgements. Two-entry register slices isolate both stream boundaries,
including READY. CSR data, status, and hardware-clear outputs are registered.
A pending-beat flag prevents a held CSR VALID or READY from accepting the same
word again while its registered acknowledgement clears the CSR control bit.

One direct TX frame is admitted at a time. Retain its IRQ reservation through
the FIFO and mux until ``tx_frame_done`` reports that the oETP input accepted
the final beat. Acceptance into an earlier FIFO alone is not TX completion.
RX availability uses its own event path. ``rst`` clears active direct-stream
state and pending event context.

**Verification:** integrated direct-stream cases in
``dv/core/openenoc_endpoint_interface/``.

Functional scenarios
--------------------

This section reserves space for scenario descriptions and WaveDrom timing
diagrams. The current outline is:

* Single-frame transmit and completion after the downstream frame boundary.
* Receive availability before the complete frame arrives.
* Held CSR commands, stream stalls, and IRQ admission.
