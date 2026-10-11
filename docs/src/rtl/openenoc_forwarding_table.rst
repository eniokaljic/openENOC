.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-FileCopyrightText: 2026 Kerim Bavcic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-forwarding-table:

Forwarding table -- openenoc_forwarding_table
=============================================

Stores Ethernet address-to-port mappings and supports lookup, learning, and
software management.

**Source:** :download:`openenoc_forwarding_table.sv <../../../hw/rtl/core/openenoc_forwarding_table.sv>`.

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
     - ``8``
     - 1..32
     - Port count and forwarding-bitmap width.
   * - ``TABLE_DEPTH``
     - ``32``
     - Integer >= 1
     - Number of forwarding-table entries.
   * - ``ADDR_WIDTH``
     - ``$clog2(TABLE_DEPTH * 16)``
     - Derived from TABLE_DEPTH*16
     - Forwarding-table byte-address width; not overridable.

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
   * - ``default_forwarding``
     - ``logic [NUM_OF_INTERFACES-1:0]``
     - input
     - Bitmap returned when the table has no enabled match.
   * - ``operation_mode``
     - ``logic``
     - input
     - Zero enables autonomous learning; one selects software-managed entries.
   * - ``cpuif_req``
     - ``logic``
     - input
     - External table-register access request.
   * - ``cpuif_addr``
     - ``logic [ADDR_WIDTH-1:0]``
     - input
     - Byte address within the forwarding-table aperture.
   * - ``cpuif_req_is_wr``
     - ``logic``
     - input
     - One selects a write; zero selects a read.
   * - ``cpuif_wr_data``
     - ``logic [31:0]``
     - input
     - External write data.
   * - ``cpuif_wr_biten``
     - ``logic [31:0]``
     - input
     - Per-bit write enables for the table register word.
   * - ``cpuif_wr_ack``
     - ``logic``
     - output
     - Write completion acknowledgement.
   * - ``cpuif_rd_ack``
     - ``logic``
     - output
     - Read completion acknowledgement.
   * - ``cpuif_rd_data``
     - ``logic [31:0]``
     - output
     - Read result for the acknowledged register access.
   * - ``lookup_if``
     - ``openenoc_lookup_if.slv``
     - bidirectional (slv)
     - Destination lookup request and returned forwarding bitmap.
   * - ``learning_if``
     - ``openenoc_learning_if.slv``
     - bidirectional (slv)
     - Source-address learning request and acknowledgement.

Architecture and operation
--------------------------

The table maps 48-bit MAC addresses to ``NUM_OF_INTERFACES``-bit port bitmaps.
``TABLE_DEPTH`` sets entry count. Entries occupy 16 bytes in the CPU-visible
aperture. ``ADDR_WIDTH`` is derived as ``$clog2(TABLE_DEPTH * 16)`` for
``cpuif_addr``. The module serves external ``cpuif_*`` signals,
:ref:`rtl-lookup-if`, and :ref:`rtl-learning-if` in the fabric domain.

Pending operations follow CPU, lookup, then learning priority. An enabled
matching lookup returns its stored bitmap; a miss returns ``default_forwarding``.
``operation_mode`` selects managed operation, where learning is bypassed and
CPU updates control the table, or autonomous learning. A learning write pointer
supports replacement in autonomous operation. Request capture and acknowledgement
are handled by the table's state machine.

**Verification:** ``dv/core/openenoc_forwarding_table/``. Full entry bit layout,
replacement/update timing, and reset contents remain reference expansion work;
the HAL remains authoritative for the software-visible format.

Functional scenarios
--------------------

This section reserves space for scenario descriptions and WaveDrom timing
diagrams. The current outline is:

* Lookup hit, miss, and default forwarding.
* Autonomous learning, replacement, and managed operation.
* Concurrent CPU/lookup/learning requests and CPU table access.
