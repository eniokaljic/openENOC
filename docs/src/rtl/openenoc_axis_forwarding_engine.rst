.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-FileCopyrightText: 2026 Kerim Bavcic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-axis-forwarding-engine:

Forwarding engine -- openenoc_axis_forwarding_engine
====================================================

Determines Ethernet forwarding destinations and learns source addresses for
received frames.

**Source:** :download:`openenoc_axis_forwarding_engine.sv <../../../hw/rtl/core/openenoc_axis_forwarding_engine.sv>`.

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
   * - ``pause_request``
     - ``logic``
     - input
     - Requests a pause at the next frame boundary.
   * - ``pause_done``
     - ``logic``
     - output
     - Indicates active frame and output pipeline have drained for pause.
   * - ``s_axis``
     - ``taxi_axis_if.snk``
     - sink
     - Incoming AXI4-Stream payload and metadata.
   * - ``m_axis``
     - ``taxi_axis_if.src``
     - source
     - Outgoing AXI4-Stream payload and metadata.
   * - ``lookup_if``
     - ``openenoc_lookup_if.mst``
     - bidirectional (mst)
     - Destination lookup request and returned forwarding bitmap.
   * - ``learning_if``
     - ``openenoc_learning_if.mst``
     - bidirectional (mst)
     - Source-address learning request and acknowledgement.

Architecture and operation
--------------------------

The engine parses destination/source MAC addresses for forwarding lookup and
learning. ``s_axis.tid`` carries ingress identity; ``m_axis.tuser`` carries the
egress bitmap. ``NUM_OF_INTERFACES`` sets bitmap width. ``lookup_if`` and
``learning_if`` connect the forwarding table directly or through its arbiter.
The frame stream and state machine share ``clk/rst``.

The forwarding result excludes the ingress port. Incomplete address fields
follow the implemented short-frame handling rather than generating invalid
learning entries. ``pause_request`` prevents admission of a new frame at a
frame boundary; ``pause_done`` waits for active frame and output-pipeline
activity to drain. Resume follows removal of the request.

**Verification:** ``dv/core/openenoc_axis_forwarding_engine/``. Add state and
timing descriptions for lookup stalls, short frames, and pause completion as
the reference is expanded.

Functional scenarios
--------------------

This section reserves space for scenario descriptions and WaveDrom timing
diagrams. The current outline is:

* Known destination, lookup miss, and ingress-port exclusion.
* Source learning and incomplete Ethernet headers.
* Lookup stalls, frame-boundary pause, drain, and resume.
