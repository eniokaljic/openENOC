.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-rr-arbiter:

Round-robin arbiter -- openenoc_rr_arbiter
==========================================

Selects requesting clients fairly using a rotating priority pointer.

**Source:** :download:`openenoc_rr_arbiter.sv <../../../hw/rtl/core/openenoc_rr_arbiter.sv>`.

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
   * - ``PORTS``
     - ``2``
     - Integer >= 1
     - Number of round-robin requesters.
   * - ``INDEX_W``
     - ``PORTS > 1 ? $clog2(PORTS) : 1``
     - >= max(1, ceil(log2(PORTS)))
     - Width of the winning requester index.

Signals
-------

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
   * - ``request``
     - ``logic [PORTS-1:0]``
     - input
     - Active requester bitmap.
   * - ``accept``
     - ``logic``
     - input
     - Consumer accepts the current winning grant.
   * - ``grant``
     - ``logic [PORTS-1:0]``
     - output
     - One-hot winning requester bitmap.
   * - ``grant_valid``
     - ``logic``
     - output
     - At least one requester is selected.
   * - ``grant_index``
     - ``logic [INDEX_W-1:0]``
     - output
     - Index of the winning requester.

Architecture and operation
--------------------------

``PORTS`` defaults to 2 and ``INDEX_W`` is derived with a minimum of one bit.
The arbiter selects a grant combinationally from the current ``request`` vector,
starting at the registered round-robin pointer. ``grant`` is one-hot when
``grant_valid`` is asserted; ``grant_index`` identifies the selected port.

Only the pointer is registered. An ``accept && grant_valid`` handshake advances
it past the accepted winner, wrapping at ``PORTS``. With no accepted grant it
retains its value; ``rst`` returns it to zero. A completed grant can therefore
be followed by another on the next cycle without an empty arbitration cycle.
The surrounding channel owner retains any transaction that needs a stable
grant under backpressure.

**Verification:** exercised by peer lookup, IRQ controller, and AXI4-Lite
crossbar tests. Further reference detail can show fairness and pointer advance
for non-power-of-two port counts.

Functional scenarios
--------------------

This section reserves space for scenario descriptions and WaveDrom timing
diagrams. The current outline is:

* Simultaneous requests and round-robin selection.
* Accepted grant, pointer advance, and wraparound.
* Unaccepted grants, empty requests, and reset.
