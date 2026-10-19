.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _runtime-endpoint-axis:

Direct AXIS
===========

| Header: :download:`openenoc_endpoint_axis.h <../../../sw/lib/hal/openenoc_endpoint_axis.h>`
| Implementation: :download:`openenoc_endpoint_axis.c <../../../sw/lib/hal/openenoc_endpoint_axis.c>`

.. index::
   single: TVALID

.. c:function:: openenoc_endpoint_status_t openenoc_endpoint_axis_send(volatile csr__endpoint_interface_t *endpoint, uint32_t data, uint8_t keep, bool last)

   Submit one direct 32-bit AXIS TX beat without waiting for hardware acceptance.

   :param endpoint: In; required mapped, word-aligned endpoint-interface pointer.
   :param data: In; 32-bit beat payload.
   :param keep: In; valid-byte-lane mask; the lower four bits are written to TKEEP.
   :param last: In; true marks the final beat of the frame.
   :returns: ``OK`` when the request has been submitted to CSR; ``INVALID_ARGUMENT`` for an invalid endpoint pointer; ``UNSUPPORTED`` when direct AXIS is absent; ``NOT_READY`` while the previous TX request is pending.
   :Side effects: Writes payload and sidebands, then sets TVALID; returns before downstream acceptance.

.. index::
   single: TREADY

.. c:function:: openenoc_endpoint_status_t openenoc_endpoint_axis_receive(volatile csr__endpoint_interface_t *endpoint, uint32_t *data, uint8_t *keep, bool *last)

   Capture and acknowledge one direct AXIS RX beat.

   :param endpoint: In; required mapped, word-aligned endpoint-interface pointer.
   :param data: Out; required 32-bit payload destination.
   :param keep: Out; optional valid-lane mask destination; may be null.
   :param last: Out; optional TLAST destination; may be null.
   :returns: ``OK``; ``INVALID_ARGUMENT`` for invalid endpoint pointer/data; ``UNSUPPORTED`` when direct AXIS is absent; ``NOT_READY`` when no beat is valid or a previous acknowledgement is pending.
   :Side effects: On OK, captures payload and sidebands before setting TREADY. Outputs remain unchanged on other statuses.

.. c:function:: openenoc_endpoint_status_t openenoc_endpoint_axis_send_stream(volatile csr__endpoint_interface_t *endpoint, const void *buffer, uint32_t byte_count)

   Submit a complete frame from a CPU byte buffer, waiting through beat backpressure.

   :param endpoint: In; required mapped, word-aligned endpoint-interface pointer.
   :param buffer: In; required readable CPU buffer; no alignment is required.
   :param byte_count: In; nonzero number of frame bytes to submit.
   :returns: ``OK`` when every beat has been submitted to CSR; ``INVALID_ARGUMENT`` for an invalid endpoint pointer, null buffer or zero length; ``UNSUPPORTED`` when direct AXIS is absent. ``OK`` does not confirm Ethernet completion.
   :Preconditions: The caller owns TX frame submission and retains the readable buffer throughout the call. Coordinate RX and ISR ownership so a blocking RX handler cannot preempt and wait for unfinished TX work on the same CPU.
   :Side effects: Reads consecutive bytes, packs lanes 0 through 3, sets TKEEP for actual bytes, and sets TLAST on the final beat. Before submitting each beat, polls source.control.f.tvalid until hardware clears the preceding request, without a software wait timeout. Writes payload and sidebands directly through the generated register fields before setting TVALID. The final beat may still be pending when the function returns. Does not change CPU IRQ masking.

.. c:function:: openenoc_endpoint_status_t openenoc_endpoint_axis_receive_stream(volatile csr__endpoint_interface_t *endpoint, void *buffer, uint32_t buffer_capacity_bytes, uint32_t *received_bytes)

   Receive one frame through TLAST and drain bytes beyond the supplied capacity.

   :param endpoint: In; required mapped, word-aligned endpoint-interface pointer.
   :param buffer: Out; writable CPU buffer with no alignment requirement. May be null only when buffer_capacity_bytes is zero, for draining.
   :param buffer_capacity_bytes: In; maximum bytes written to buffer; zero permits draining without storing data.
   :param received_bytes: Out; required actual byte-count destination. Counts valid TKEEP lanes, including drained bytes; saturates at UINT32_MAX.
   :returns: ``OK`` after TLAST when all bytes fit; ``OUT_OF_RANGE`` after draining an oversized frame, with the full representable count; ``INVALID_ARGUMENT`` for an invalid endpoint pointer, missing count pointer, or null buffer with nonzero capacity; ``UNSUPPORTED`` when direct AXIS is absent.
   :Preconditions: The caller owns RX consumption and retains the writable buffer throughout the call. Coordinate TX, RX and ISR ownership so blocking RX cannot preempt unfinished TX work needed to produce the rest of its frame.
   :Side effects: Waits for sink.control.f.tready to clear, then for sink.status.f.tvalid to be set, without a software timeout. Captures TDATA, TKEEP and TLAST directly through the generated register fields before setting TREADY. Copies valid lanes in order 0 through 3, preserving the first buffer_capacity_bytes bytes when oversized. At TLAST, writes the total byte count. When direct AXIS is absent, writes zero to received_bytes if provided and returns UNSUPPORTED. Invalid buffer/count arguments on a supported endpoint leave outputs unchanged. Does not change CPU IRQ masking.
