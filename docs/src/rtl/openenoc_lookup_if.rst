.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-lookup-if:

Forwarding lookup -- openenoc_lookup_if
=======================================

Defines an Ethernet destination lookup request and returned forwarding bitmap.

**Source:** :download:`openenoc_lookup_if.sv <../../../hw/rtl/core/openenoc_lookup_if.sv>`.

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
   * - ``mac_addr``
     - ``logic [47:0]``
     - mst: output; slv: input
     - 48-bit Ethernet address for the request.
   * - ``ack``
     - ``logic``
     - mst: input; slv: output
     - Acknowledges the outstanding lookup or learning request.
   * - ``port_bitmap``
     - ``logic [NUM_OF_INTERFACES-1:0]``
     - mst: input; slv: output
     - Learned ingress bitmap or returned destination bitmap.

Architecture and operation
--------------------------

**Parameter and roles:** ``NUM_OF_INTERFACES`` defaults to 8 and sets the
width of ``port_bitmap``. Modports are ``mst`` and ``slv``.

The requester submits a 48-bit destination ``mac_addr`` with ``req``. The
table returns ``port_bitmap`` with ``ack``. This is a request/acknowledgement
interface, with no ready signal. The forwarding-table arbiter captures pending
requests and retains downstream ownership until acknowledgement; see
:ref:`rtl-forwarding-table-arb-mux`.

Functional scenarios
--------------------

This section reserves space for scenario descriptions and WaveDrom timing
diagrams. The current outline is:

* Lookup request and acknowledged bitmap.
* Hit/miss interpretation by the table.
* Delayed acknowledgement and retained request payload.
