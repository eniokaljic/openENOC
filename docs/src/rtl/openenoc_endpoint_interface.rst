.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-endpoint-interface:

Endpoint interface -- openenoc_endpoint_interface
=================================================

Integrates endpoint transport, memory access, direct software streams, peer
lookup, and interrupts.

**Source:** :download:`openenoc_endpoint_interface.sv <../../../hw/rtl/core/openenoc_endpoint_interface.sv>`.

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
   * - ``FIFO_DEPTH``
     - ``16384``
     - Bytes >= MAX_RAW_FRAME_SIZE
     - Capacity of each direct/DMA transport FIFO; supports one maximum raw frame.
   * - ``FIFO_RAM_PIPELINE``
     - ``1``
     - Integer >= 0
     - RAM pipeline stages in the transport FIFO adapters.
   * - ``IRQ_FIFO_DEPTH``
     - ``16``
     - Integer >= 1
     - Number of interrupt claims; power-of-two depth is not required.
   * - ``MAX_RAW_FRAME_SIZE``
     - ``8192``
     - 36..8192 bytes
     - Synthesized frame ceiling excluding FCS; reserves 32 bytes for the largest
       peer-frame overhead.
   * - ``FRAGMENT_SLOTS``
     - ``16``
     - Integer >= 1
     - Number of local fragment bookkeeping contexts; not wire credits.

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
   * - ``endpoint_if``
     - ``openenoc_endpoint_if.core``
     - bidirectional (core)
     - Endpoint configuration, commands, status, and external scalar-memory access.
   * - ``eth_if``
     - ``openenoc_eth_if``
     - bidirectional; endpoint is side A
     - Bidirectional Ethernet-like transport; this endpoint is side A.
   * - ``m_axi_wr``
     - ``taxi_axi_if.wr_mst``
     - bidirectional (wr_mst)
     - Outgoing AXI4 memory write address/data/response channels.
   * - ``m_axi_rd``
     - ``taxi_axi_if.rd_mst``
     - bidirectional (rd_mst)
     - Outgoing AXI4 memory read address/response channels.
   * - ``m_rmem_cpuif``
     - ``openenoc_cpuif_if.mst``
     - bidirectional (mst)
     - Local scalar-memory master supplied by the DMA engine.
   * - ``irq``
     - ``logic``
     - output
     - Level interrupt notification to software.

Architecture and operation
--------------------------

This single-clock integration module connects the generated ``endpoint_if``
to the bidirectional ``eth_if``, AXI memory masters ``m_axi_wr/m_axi_rd``,
local-memory CPUIF master ``m_rmem_cpuif``, and ``irq``. Each submodule owns
its corresponding hardware-driven CSR fields.

Two peer lookup clients serve DMA and oETP. Two transfer interfaces distinguish
initiator and responder commands. TX/RX FIFOs, stream adapters, a TX mux, and
an RX demux connect DMA and direct traffic to oETP. Internal FIFOs use streaming
operation without frame-drop policies. Endpoint route/sequence/role metadata
is kept inside the endpoint and cleared at the Ethernet boundary.

Seven IRQ producer ports carry three DMA events, two direct-stream events,
initiating RMEM errors, and received-request errors. The last port shares the
bulk/RMEM source encodings; port count and logical event count are distinct.
``rst`` clears the submodules and FIFOs in this clock domain.

The TX mux uses round-robin arbitration at frame boundaries. DMA peer commands
are sequential; protocol TX gives ready responses priority and RMEM initiation
precedes the next bulk fragment. All memory operations, error CSR updates, and
IRQ producers remain in DMA. The initiating RMEM error producer captures its
source enable before any delayed IRQ admission.

``FIFO_DEPTH`` specifies bytes for each transport FIFO, and
``FIFO_RAM_PIPELINE`` sets its RAM pipeline stages. These FIFOs use
``FRAME_FIFO = 0``, ``DROP_BAD_FRAME = 0``, ``DROP_WHEN_FULL = 0``,
``DROP_OVERSIZE_FRAME = 0``, and ``MARK_WHEN_FULL = 0``. They propagate
backpressure and permit streaming before a complete frame is buffered.
Direct CSR streams remain 32 bits wide; adapters connect them to the selected
Ethernet width. DMA streams use the memory-interface data width. Internal
``TUSER[0]`` denotes the final fragment and ``TUSER[1]`` distinguishes initiator
and responder payloads, as specified in :ref:`rtl-dma-transfer-if`.

**Verification:** ``dv/core/openenoc_endpoint_interface/`` exercises direct/raw
streams, both bulk modes, multiple fragments, incoming servicing, multicast,
RMEM initiation/execution, local/remote errors, timeout abort, and IRQ retention
with a full queue, at AXI/Ethernet widths 32/32, 64/32, 32/64, and 64/8.

Functional scenarios
--------------------

This section reserves space for scenario descriptions and WaveDrom timing
diagrams. The current outline is:

* Direct CSR frame transmit and receive.
* Raw DMA and sequential multi-fragment peer transfers.
* Incoming and locally initiated scalar memory accesses.
* Multicast, malformed trailers, memory failures, and timeout recovery.
* Width conversion, backpressure, and full IRQ queues.
