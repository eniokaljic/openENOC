.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _runtime-endpoint-peer:

Peer configuration and DMA
==========================

.. index::
   single: Transparent RMEM

| Header: :download:`openenoc_endpoint_peer.h <../../../sw/lib/hal/openenoc_endpoint_peer.h>`
| Implementation: :download:`openenoc_endpoint_peer.c <../../../sw/lib/hal/openenoc_endpoint_peer.c>`

Peer mode 0 disables operations; mode 1 enables transparent RMEM; mode 2 fetches a block into local memory and permits incoming bulk writes; mode 3 sends a block to remote memory and permits incoming bulk reads. Mirror relationships require complementary modes 2 and 3. Local and remote addresses are 32-bit bus addresses, not CPU pointers.

.. c:function:: openenoc_endpoint_status_t openenoc_endpoint_peer_get_config(const volatile csr__endpoint_interface_t *endpoint, uint16_t peer_index, openenoc_endpoint_peer_config_t *config)

   Read one peer mapping and access policy.

   :param endpoint: In; required mapped, word-aligned endpoint-interface pointer.
   :param peer_index: In; zero-based index smaller than the advertised peer count.
   :param config: Out; required peer-configuration destination.
   :returns: ``OK``; ``INVALID_ARGUMENT``, ``OUT_OF_RANGE`` for an invalid peer index, or ``UNSUPPORTED`` when neither peer DMA nor RMEM is implemented.
   :Side effects: Reads the selected peer CSRs.

.. c:function:: openenoc_endpoint_status_t openenoc_endpoint_peer_set_config(volatile csr__endpoint_interface_t *endpoint, uint16_t peer_index, const openenoc_endpoint_peer_config_t *config)

   Apply one peer mapping and access policy.

   :param endpoint: In; required mapped, word-aligned endpoint-interface pointer.
   :param peer_index: In; zero-based index smaller than the advertised peer count.
   :param config: In; required peer mapping. Addresses/RMEM offset must be word-aligned; enabled regions must be nonempty and fit the 32-bit address spaces.
   :returns: ``OK``; ``INVALID_ARGUMENT`` for invalid arguments, alignment, mode, overlapping transparent mappings, or multicast mirror-to-local target; ``OUT_OF_RANGE`` for peer index or region bounds; ``UNSUPPORTED`` for unavailable features; ``NOT_READY`` for pending commands or active local peer DMA.
   :Preconditions: Transparent regions must fit RMEM, have a word-multiple size, and not overlap another transparent mapping. Local/remote users must be quiescent; idle alone does not prove incoming requests have stopped.
   :Side effects: Temporarily disables the selected peer, writes mapping registers, then applies mode and IRQ enable.

.. c:function:: openenoc_endpoint_status_t openenoc_endpoint_peer_dma_request(volatile csr__endpoint_interface_t *endpoint, uint16_t peer_index)

   Submit a transfer of the configured peer region.

   :param endpoint: In; required mapped, word-aligned endpoint-interface pointer.
   :param peer_index: In; zero-based index smaller than the advertised peer count.
   :returns: ``OK``; ``INVALID_ARGUMENT`` for an invalid endpoint pointer, non-mirror mode, zero block size or invalid configured fragment limit; ``OUT_OF_RANGE`` for peer index; ``UNSUPPORTED`` when peer DMA is absent; ``NOT_READY`` for pending commands or active local peer DMA.
   :Preconditions: Capture previous completion state before submission. Keep peer mapping and buffers stable while pending or active.
   :Side effects: Sets the peer request command without waiting for acceptance or completion.

.. c:function:: openenoc_endpoint_status_t openenoc_endpoint_peer_get_status(const volatile csr__endpoint_interface_t *endpoint, uint16_t peer_index, openenoc_endpoint_peer_status_t *status)

   Read local peer-DMA state and shared diagnostics.

   :param endpoint: In; required mapped, word-aligned endpoint-interface pointer.
   :param peer_index: In; zero-based index smaller than the advertised peer count.
   :param status: Out; required destination for pending commands, idle/done, and sticky error/code.
   :returns: ``OK``; ``INVALID_ARGUMENT``, ``OUT_OF_RANGE`` for an invalid peer index, or ``UNSUPPORTED`` when neither peer DMA nor RMEM is implemented.
   :Side effects: Reads the peer status; preserves commands and error state.

.. c:function:: openenoc_endpoint_status_t openenoc_endpoint_peer_request_clear_error(volatile csr__endpoint_interface_t *endpoint, uint16_t peer_index)

   Submit clearing of one shared peer error record.

   :param endpoint: In; required mapped, word-aligned endpoint-interface pointer.
   :param peer_index: In; zero-based index smaller than the advertised peer count.
   :returns: ``OK``; ``INVALID_ARGUMENT``, ``OUT_OF_RANGE`` for an invalid peer index, or ``UNSUPPORTED`` when neither peer DMA nor RMEM is implemented. ``NOT_READY`` when request or error-clear acknowledgement is pending.
   :Side effects: Sets clear_error without waiting; preserves mode and IRQ enable. Hardware clearing preserves active work and done state; new failures win a simultaneous clear.

Public declarations
-------------------

The maintained header below provides the exact public type and enum definitions.

.. index::
   single: openenoc_endpoint_peer_mode_t
   single: openenoc_endpoint_peer_config_t
   single: openenoc_endpoint_peer_status_t

.. literalinclude:: ../../../sw/lib/hal/openenoc_endpoint_peer.h
   :language: c
   :caption: Peer types
   :start-at: typedef enum {
   :end-before: openenoc_endpoint_status_t openenoc_endpoint_peer_get_config
   :linenos:
