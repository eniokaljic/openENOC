.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-eth-adapter:

Ethernet clock/width adapter -- openenoc_eth_adapter
====================================================

Bridges bidirectional Ethernet-like streams across clock domains and stream
widths.

**Source:** :download:`openenoc_eth_adapter.sv <../../../hw/rtl/core/openenoc_eth_adapter.sv>`.

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
   * - ``DEPTH``
     - ``4096``
     - Positive lane-word capacity, rounded to power-of-two FIFO beats
     - Capacity passed to TAXI; counts bytes with enabled KEEP and eight-bit lanes,
       otherwise whole stream words. Account for the wider side.
   * - ``RAM_PIPELINE``
     - ``1``
     - Integer >= 0
     - RAM pipeline register count in each asynchronous FIFO adapter.
   * - ``OUTPUT_FIFO_EN``
     - ``1'b0``
     - 0 or 1
     - Enables the FIFO adapter output FIFO.
   * - ``FRAME_FIFO``
     - ``1'b0``
     - 0 or 1
     - Holds complete frames before making them available at the output.
   * - ``USER_BAD_FRAME_VALUE``
     - ``1'b1``
     - Value fitting the stream USER width
     - USER pattern identifying a bad frame under the configured mask.
   * - ``USER_BAD_FRAME_MASK``
     - ``1'b1``
     - Mask fitting the stream USER width
     - USER bits compared against the bad-frame value.
   * - ``DROP_OVERSIZE_FRAME``
     - ``FRAME_FIFO``
     - 0 or 1; requires FRAME_FIFO
     - Drops frames that exceed the frame FIFO capacity.
   * - ``DROP_BAD_FRAME``
     - ``1'b0``
     - 0 or 1; requires frame buffering and oversize dropping
     - Drops frames matching the configured bad-frame marker.
   * - ``DROP_WHEN_FULL``
     - ``1'b0``
     - 0 or 1; requires frame buffering and oversize dropping
     - Discards arriving frames instead of backpressuring when full.
   * - ``MARK_WHEN_FULL``
     - ``1'b0``
     - 0 or 1; streaming mode only
     - Marks overflowed streaming frames as bad instead of ordinary backpressure.
   * - ``FRAME_PAUSE``
     - ``FRAME_FIFO``
     - 0 or 1
     - Frame-boundary pause policy; inactive because this wrapper has no pause
       requests and leaves TAXI PAUSE_EN disabled.

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
   * - ``eth_a``
     - ``openenoc_eth_if``
     - bidirectional; endpoint is side A
     - Side-A link and its clock/reset domain.
   * - ``eth_b``
     - ``openenoc_eth_if``
     - bidirectional; endpoint is side A
     - Side-B link and its clock/reset domain.

Architecture and operation
--------------------------

The adapter connects ``eth_a`` and ``eth_b`` using one TAXI asynchronous FIFO
adapter per direction. The links provide their own ``clk/rst`` and AXIS widths.
The A-to-B path preserves ``a2b_axis_if`` orientation; the B-to-A path preserves
``b2a_axis_if`` orientation. Local TAXI interfaces bridge nested link interfaces
for tool compatibility.

``DEPTH``, ``RAM_PIPELINE``, and ``OUTPUT_FIFO_EN`` configure buffering.
``FRAME_FIFO``, ``FRAME_PAUSE``, bad-frame value/mask, and the drop/mark options
select frame policy. Their defaults allow streaming rather than requiring a
whole frame before forwarding. Endpoint use must preserve the agreed lossless
internal transport. Reset behavior spans both link clock domains and follows
the asynchronous FIFO's reset contract.

For enabled KEEP with eight-bit lanes, ``DEPTH`` counts bytes. Internally the
FIFO stores the wider side's beats and rounds the cycle count up to a power
of two. The depth must therefore leave usable storage at that width. Link
widths must have an integer ratio for width adaptation. ``FRAME_FIFO = 0``
with all drop/mark policies clear permits a frame larger than the FIFO to
progress through backpressure as its receiver consumes bytes. This generic
adapter does not impose the endpoint oETP engine's frame-size ceiling.

``FRAME_FIFO = 1`` requires frame termination and holds data until frame
completion. Bad-frame dropping also requires oversize dropping and a usable
USER marker. Streaming overflow marking requires frame termination and a
nonzero marker mask. Pause requests are not exposed by this wrapper, so
``FRAME_PAUSE`` has no active pause request to control.

**Verification:** ``dv/core/openenoc_eth_adapter/``; the flattened
``ci/sv2v/sv2v_openenoc_eth_adapter.sv`` is a toolchain wrapper, not another
endpoint block. Future reference detail should describe reset coordination,
FIFO capacity units across width conversion, and optional frame policies.

Functional scenarios
--------------------

This section reserves space for scenario descriptions and WaveDrom timing
diagrams. The current outline is:

* Simultaneous traffic in both directions.
* Width conversion, FIFO pressure, and independent clock rates.
* Streaming/frame-buffered policies, bad frames, and coordinated reset.
