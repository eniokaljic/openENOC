.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _runtime-endpoint-config:

Endpoint configuration
======================

| Header: :download:`openenoc_endpoint_config.h <../../../sw/lib/hal/openenoc_endpoint_config.h>`
| Implementation: :download:`openenoc_endpoint_config.c <../../../sw/lib/hal/openenoc_endpoint_config.c>`

Multi-register configuration requires quiescent local and remote users. MAC addresses are six octets in network order. Zero multicast disables oETP group reception. Response timeouts count endpoint clock cycles; zero disables timeout. They begin after request transmission and do not bound complete API-call or whole-transfer duration.

.. c:function:: openenoc_endpoint_status_t openenoc_endpoint_get_config(const volatile csr__endpoint_interface_t *endpoint, openenoc_endpoint_config_t *config)

   Read the current endpoint configuration.

   :param endpoint: In; required mapped, word-aligned endpoint-interface pointer.
   :param config: Out; required configuration destination.
   :returns: ``OK``; ``INVALID_ARGUMENT`` for an invalid endpoint pointer or required argument.
   :Side effects: Reads configuration CSRs; returns the written fragment value, before rounding.

.. c:function:: openenoc_endpoint_status_t openenoc_endpoint_set_config(volatile csr__endpoint_interface_t *endpoint, const openenoc_endpoint_config_t *config)

   Apply all endpoint configuration values.

   :param endpoint: In; required mapped, word-aligned endpoint-interface pointer.
   :param config: In; required configuration. Unicast I/G must be zero; multicast must be zero or a group address; receive mode must be valid.
   :returns: ``OK``; ``INVALID_ARGUMENT`` for invalid pointers, MACs or receive mode; ``OUT_OF_RANGE`` for an invalid effective fragment limit when peer DMA is supported.
   :Preconditions: Local and remote users must be quiescent; this call does not enforce an atomic hardware-wide update.
   :Side effects: Writes MACs, receive policy, both timeouts, and the requested fragment size after validation.

.. c:function:: openenoc_endpoint_status_t openenoc_endpoint_set_mac_address(volatile csr__endpoint_interface_t *endpoint, const openenoc_endpoint_mac_t *address)

   Set the endpoint source and individual destination MAC.

   :param endpoint: In; required mapped, word-aligned endpoint-interface pointer.
   :param address: In; required six-octet address with its first-octet I/G bit zero.
   :returns: ``OK``; ``INVALID_ARGUMENT`` for an invalid endpoint pointer, null address, or group MAC.
   :Preconditions: Coordinate users affected by the MAC change.
   :Side effects: Writes the generated lower and upper MAC fields.

.. c:function:: openenoc_endpoint_status_t openenoc_endpoint_set_multicast_address(volatile csr__endpoint_interface_t *endpoint, const openenoc_endpoint_mac_t *address)

   Set the exact oETP group destination filter.

   :param endpoint: In; required mapped, word-aligned endpoint-interface pointer.
   :param address: In; required zero address or address with its first-octet I/G bit set.
   :returns: ``OK``; ``INVALID_ARGUMENT`` for an invalid endpoint pointer, null address, or nonzero individual MAC.
   :Preconditions: Coordinate users affected by the filter change.
   :Side effects: Writes the generated lower and upper multicast fields.

.. c:function:: openenoc_endpoint_status_t openenoc_endpoint_set_receive_mode(volatile csr__endpoint_interface_t *endpoint, openenoc_endpoint_receive_mode_t mode)

   Set the non-oETP receive policy.

   :param endpoint: In; required mapped, word-aligned endpoint-interface pointer.
   :param mode: In; DROP, FILTERED, MULTICAST, or PROMISCUOUS receive enum.
   :returns: ``OK``; ``INVALID_ARGUMENT`` for an invalid endpoint pointer or receive mode.
   :Side effects: Writes the receive policy. FILTERED accepts local unicast and broadcast; MULTICAST additionally accepts group traffic.

.. c:function:: openenoc_endpoint_status_t openenoc_endpoint_set_rmem_timeout(volatile csr__endpoint_interface_t *endpoint, uint32_t cycles)

   Set the response timeout for transparent RMEM.

   :param endpoint: In; required mapped, word-aligned endpoint-interface pointer.
   :param cycles: In; maximum response-wait cycles, or zero for no timeout.
   :returns: ``OK``; ``INVALID_ARGUMENT`` for an invalid endpoint pointer; ``UNSUPPORTED`` when RMEM is absent.
   :Side effects: Writes the timeout sampled for subsequent RMEM operations.

.. c:function:: openenoc_endpoint_status_t openenoc_endpoint_set_dma_timeout(volatile csr__endpoint_interface_t *endpoint, uint32_t cycles)

   Set the common unicast peer-DMA fragment response timeout.

   :param endpoint: In; required mapped, word-aligned endpoint-interface pointer.
   :param cycles: In; maximum response-wait cycles per fragment, or zero for no timeout.
   :returns: ``OK``; ``INVALID_ARGUMENT`` for an invalid endpoint pointer; ``UNSUPPORTED`` when peer DMA is absent.
   :Side effects: Writes the timeout sampled for subsequent fragment requests. It does not apply to raw DMA or multicast writes.

.. c:function:: openenoc_endpoint_status_t openenoc_endpoint_set_dma_max_fragment_size(volatile csr__endpoint_interface_t *endpoint, uint32_t requested_bytes, uint32_t *effective_bytes)

   Set the requested peer-DMA fragment limit.

   :param endpoint: In; required mapped, word-aligned endpoint-interface pointer.
   :param requested_bytes: In; written memory-byte limit; hardware executes its value rounded down to a multiple of four.
   :param effective_bytes: Out; optional rounded byte limit; may be null.
   :returns: ``OK``; ``INVALID_ARGUMENT`` for an invalid endpoint pointer; ``UNSUPPORTED`` when peer DMA is absent; ``OUT_OF_RANGE`` when the rounded value is below four or above the advertised fragment ceiling.
   :Preconditions: The upper bound is ``4 * floor((max_raw_frame_size_bytes - 32) / 4)``. Hardware snapshots the limit at block acceptance.
   :Side effects: Writes the original requested value and, on success, returns its effective value when requested.

Public declarations
-------------------

The maintained header below provides the exact public type and enum definitions.

.. index::
   single: openenoc_endpoint_receive_mode_t
   single: openenoc_endpoint_config_t

.. literalinclude:: ../../../sw/lib/hal/openenoc_endpoint_config.h
   :language: c
   :caption: Configuration types
   :start-at: typedef enum {
   :end-before: openenoc_endpoint_status_t openenoc_endpoint_get_config
   :linenos:
