.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-cpuif-if:

Native CPUIF -- openenoc_cpuif_if
=================================

Defines a native request and acknowledgement interface for register and scalar
memory accesses.

**Source:** :download:`openenoc_cpuif_if.sv <../../../hw/rtl/core/openenoc_cpuif_if.sv>`.

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
   * - ``ADDR_W``
     - ``32``
     - Integer >= 1
     - Byte-address width in bits; connected interfaces must agree.
   * - ``DATA_W``
     - ``32``
     - Integer >= 1; AXI adapters require multiples of 8
     - Native data width and bit-enable width.

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
   * - ``req``
     - ``logic``
     - mst: output; slv: input
     - Native access, lookup, or learning request.
   * - ``addr``
     - ``logic [ADDR_W-1:0]``
     - mst: output; slv: input
     - Byte address presented to the native interface or decoder.
   * - ``req_is_wr``
     - ``logic``
     - mst: output; slv: input
     - One selects a write; zero selects a read.
   * - ``wr_data``
     - ``logic [DATA_W-1:0]``
     - mst: output; slv: input
     - Native write data.
   * - ``wr_biten``
     - ``logic [DATA_W-1:0]``
     - mst: output; slv: input
     - One enable per data bit for a native write.
   * - ``wr_ack``
     - ``logic``
     - mst: input; slv: output
     - Native write completion acknowledgement.
   * - ``wr_err``
     - ``logic``
     - mst: input; slv: output
     - Native write error, valid with write acknowledgement.
   * - ``rd_ack``
     - ``logic``
     - mst: input; slv: output
     - Native read completion acknowledgement.
   * - ``rd_err``
     - ``logic``
     - mst: input; slv: output
     - Native read error, valid with read acknowledgement.
   * - ``rd_data``
     - ``logic [DATA_W-1:0]``
     - mst: input; slv: output
     - Native read result, valid with read acknowledgement.

Architecture and operation
--------------------------

**Parameters and roles:** ``ADDR_W`` and ``DATA_W`` default to 32.
Modports ``mst``, ``slv``, and ``mon`` describe the master, slave, and monitor.
Clock and reset belong to the connected modules rather than this interface.

The request/completion convention follows the PeakRDL-regblock native CPUIF.
``req`` is a request strobe: the master presents the complete request with it
and waits for the matching read or write acknowledgement before issuing
another request. The slave captures any state needed after the request cycle;
the master need not hold ``req`` until acknowledgement.

``addr`` is a byte address. ``req_is_wr`` selects write or read. ``wr_data``
and ``wr_biten`` carry one enable per **data bit**, rather than per byte.
``wr_ack`` and ``rd_ack`` complete their respective operations; ``rd_data``
is valid with ``rd_ack``. ``wr_err`` and ``rd_err`` are meaningful only with
their corresponding acknowledgement. The generated external RMEM boundary
exposes ACK/read data without ERR signals; see :ref:`rtl-dma-engine`.

Functional scenarios
--------------------

This section reserves space for scenario descriptions and WaveDrom timing
diagrams. The current outline is:

* Read request and returned data.
* Write request with per-bit enables.
* Immediate or delayed acknowledgement and target error.
