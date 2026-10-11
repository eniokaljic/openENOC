.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-learning-if:

Forwarding learning -- openenoc_learning_if
===========================================

Defines an Ethernet source-learning request and acknowledgement channel.

**Source:** :download:`openenoc_learning_if.sv <../../../hw/rtl/core/openenoc_learning_if.sv>`.

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
   * - ``port_bitmap``
     - ``logic [NUM_OF_INTERFACES-1:0]``
     - mst: output; slv: input
     - Learned ingress bitmap or returned destination bitmap.
   * - ``ack``
     - ``logic``
     - mst: input; slv: output
     - Acknowledges the outstanding lookup or learning request.

Architecture and operation
--------------------------

**Parameter and roles:** ``NUM_OF_INTERFACES`` defaults to 8 and sets the
width of ``port_bitmap``. Modports are ``mst`` and ``slv``.

The requester supplies a 48-bit source ``mac_addr`` and its ingress
``port_bitmap`` with ``req``. The table acknowledges the operation with
``ack``. Lookup and learning are separate channels; learning can be bypassed
by the table's managed-mode policy while still completing the request.

Functional scenarios
--------------------

This section reserves space for scenario descriptions and WaveDrom timing
diagrams. The current outline is:

* Learning request with source address and ingress bitmap.
* Delayed acknowledgement and retained request payload.
* Independent operation alongside destination lookup.
