.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _runtime-endpoint-dma:

Non-oETP DMA
============

.. index::
   single: Non-oETP DMA

| Header: :download:`openenoc_endpoint_dma.h <../../../sw/lib/hal/openenoc_endpoint_dma.h>`
| Implementation: :download:`openenoc_endpoint_dma.c <../../../sw/lib/hal/openenoc_endpoint_dma.c>`

These functions require advertised non-oETP DMA support. Frames include Ethernet header and payload, excluding preamble, SFD, and FCS. TX and RX maintain separate commands, byte counts, and sticky error records.

.. c:function:: openenoc_endpoint_status_t openenoc_endpoint_non_oetp_dma_tx_request(volatile csr__endpoint_interface_t *endpoint, uint32_t buffer_address, uint32_t frame_length_bytes)

   Submit one raw Ethernet frame for TX DMA.

   :param endpoint: In; required mapped, word-aligned endpoint-interface pointer.
   :param buffer_address: In; first-byte address on the local 32-bit memory bus.
   :param frame_length_bytes: In; nonzero complete-frame length, at most the advertised raw-frame limit.
   :returns: ``OK``; ``INVALID_ARGUMENT`` for an invalid endpoint pointer; ``UNSUPPORTED`` when raw DMA is absent; ``OUT_OF_RANGE`` for length or address-space overflow; ``NOT_READY`` for pending TX commands or active TX DMA.
   :Preconditions: Capture previous status/count first. Keep the buffer accessible and synchronized until completion.
   :Side effects: Writes the TX address and length, then submits request without waiting.

.. c:function:: openenoc_endpoint_status_t openenoc_endpoint_non_oetp_dma_rx_arm(volatile csr__endpoint_interface_t *endpoint, uint32_t buffer_address, uint32_t buffer_capacity_bytes)

   Submit a one-frame receive buffer for RX DMA.

   :param endpoint: In; required mapped, word-aligned endpoint-interface pointer.
   :param buffer_address: In; first-byte address on the local 32-bit memory bus.
   :param buffer_capacity_bytes: In; nonzero capacity, at most the advertised raw-frame limit.
   :returns: ``OK``; ``INVALID_ARGUMENT`` for an invalid endpoint pointer; ``UNSUPPORTED`` when raw DMA is absent; ``OUT_OF_RANGE`` for capacity or address-space overflow; ``NOT_READY`` for pending RX commands or active/armed RX DMA.
   :Preconditions: Capture previous status/count first. Keep the receive buffer accessible and synchronize it after completion.
   :Side effects: Writes the RX address and capacity, then submits arm without waiting. Once accepted and armed, eligible non-oETP traffic is routed to DMA.

.. c:function:: openenoc_endpoint_status_t openenoc_endpoint_non_oetp_dma_get_status(const volatile csr__endpoint_interface_t *endpoint, openenoc_endpoint_dma_channel_t channel, openenoc_endpoint_non_oetp_dma_status_t *status)

   Read a selected raw DMA channel status.

   :param endpoint: In; required mapped, word-aligned endpoint-interface pointer.
   :param channel: In; ``OPENENOC_ENDPOINT_DMA_TX`` or ``OPENENOC_ENDPOINT_DMA_RX``.
   :param status: Out; required channel-status destination. transferred_bytes is TX bytes or RX bytes written; armed is false for TX.
   :returns: ``OK``; ``INVALID_ARGUMENT`` for invalid endpoint pointer/channel/output; ``UNSUPPORTED`` when raw DMA is absent.
   :Side effects: Reads command/status and byte-count CSRs; preserves their state.

.. c:function:: openenoc_endpoint_status_t openenoc_endpoint_non_oetp_dma_request_clear_errors(volatile csr__endpoint_interface_t *endpoint, openenoc_endpoint_dma_channel_t channel)

   Submit error clearing for one raw DMA channel.

   :param endpoint: In; required mapped, word-aligned endpoint-interface pointer.
   :param channel: In; ``OPENENOC_ENDPOINT_DMA_TX`` or ``OPENENOC_ENDPOINT_DMA_RX``.
   :returns: ``OK``; ``INVALID_ARGUMENT`` for invalid endpoint pointer/channel; ``UNSUPPORTED`` when raw DMA is absent; ``NOT_READY`` while a channel request or clear command is pending.
   :Side effects: Submits clear without waiting. Hardware preserves active/armed work, done, byte count, and IRQ claims; new failures win a simultaneous clear.

Public declarations
-------------------

The maintained header below provides the exact public type and enum definitions.

.. index::
   single: openenoc_endpoint_dma_channel_t
   single: openenoc_endpoint_non_oetp_dma_status_t

.. literalinclude:: ../../../sw/lib/hal/openenoc_endpoint_dma.h
   :language: c
   :caption: DMA types
   :start-at: typedef enum {
   :end-before: openenoc_endpoint_status_t openenoc_endpoint_non_oetp_dma_tx_request
   :linenos:
