/* SPDX-FileCopyrightText: 2026 Enio Kaljic
 * SPDX-License-Identifier: AGPL-3.0-or-later
 */

#define OPENENOC_ENDPOINT_IMPLEMENTATION
#include "openenoc_endpoint.h"

openenoc_endpoint_status_t openenoc_endpoint_get_config(
    const volatile csr__endpoint_interface_t *endpoint, openenoc_endpoint_config_t *config) {
    if (endpoint == NULL || ((uintptr_t)endpoint & 3U) != 0U || config == NULL) {
        return OPENENOC_ENDPOINT_STATUS_INVALID_ARGUMENT;
    }
    openenoc_endpoint_mac_unpack(endpoint->config.mac_address.f.lo_word,
        endpoint->config.mac_address.f.hi_word, &config->mac_address);
    openenoc_endpoint_mac_unpack(endpoint->config.multicast_address.f.lo_word,
        endpoint->config.multicast_address.f.hi_word, &config->multicast_address);
    config->receive_mode =
        (openenoc_endpoint_receive_mode_t)endpoint->config.non_oetp_control.f.receive_mode;
    config->rmem_timeout_cycles = endpoint->config.rmem_timeout.f.cycles;
    config->dma_timeout_cycles = endpoint->config.dma_timeout.f.cycles;
    config->dma_max_fragment_size_bytes = endpoint->config.dma_max_fragment_size.f.bytes;
    return OPENENOC_ENDPOINT_STATUS_OK;
}

static bool multicast_address_valid(const openenoc_endpoint_mac_t *address) {
    openenoc_endpoint_mac_words_t words = openenoc_endpoint_mac_pack(address);

    return (words.lower == 0U && words.upper == 0U) || (address->octet[0] & 1U) != 0U;
}

openenoc_endpoint_status_t openenoc_endpoint_set_config(
    volatile csr__endpoint_interface_t *endpoint, const openenoc_endpoint_config_t *config) {
    uint32_t effective;

    if (endpoint == NULL || ((uintptr_t)endpoint & 3U) != 0U || config == NULL ||
        (config->mac_address.octet[0] & 1U) != 0U ||
        !multicast_address_valid(&config->multicast_address) ||
        (unsigned int)config->receive_mode > OPENENOC_ENDPOINT_RECEIVE_PROMISCUOUS) {
        return OPENENOC_ENDPOINT_STATUS_INVALID_ARGUMENT;
    }
    effective = config->dma_max_fragment_size_bytes & ~3U;
    if ((CSR__HAS_PEER_DMA != 0U) &&
        (effective < 4U || effective > openenoc_endpoint_max_peer_fragment_size())) {
        return OPENENOC_ENDPOINT_STATUS_OUT_OF_RANGE;
    }
    {
        openenoc_endpoint_mac_words_t words = openenoc_endpoint_mac_pack(&config->mac_address);

        endpoint->config.mac_address.f.lo_word = words.lower;
        endpoint->config.mac_address.f.hi_word = words.upper;
    }
    {
        openenoc_endpoint_mac_words_t words =
            openenoc_endpoint_mac_pack(&config->multicast_address);

        endpoint->config.multicast_address.f.lo_word = words.lower;
        endpoint->config.multicast_address.f.hi_word = words.upper;
    }
    endpoint->config.non_oetp_control.f.receive_mode = config->receive_mode;
    endpoint->config.rmem_timeout.f.cycles = config->rmem_timeout_cycles;
    endpoint->config.dma_timeout.f.cycles = config->dma_timeout_cycles;
    endpoint->config.dma_max_fragment_size.f.bytes = config->dma_max_fragment_size_bytes;
    return OPENENOC_ENDPOINT_STATUS_OK;
}

openenoc_endpoint_status_t openenoc_endpoint_set_mac_address(
    volatile csr__endpoint_interface_t *endpoint, const openenoc_endpoint_mac_t *address) {
    if (endpoint == NULL || ((uintptr_t)endpoint & 3U) != 0U || address == NULL ||
        (address->octet[0] & 1U) != 0U) {
        return OPENENOC_ENDPOINT_STATUS_INVALID_ARGUMENT;
    }
    {
        openenoc_endpoint_mac_words_t words = openenoc_endpoint_mac_pack(address);

        endpoint->config.mac_address.f.lo_word = words.lower;
        endpoint->config.mac_address.f.hi_word = words.upper;
    }
    return OPENENOC_ENDPOINT_STATUS_OK;
}

openenoc_endpoint_status_t openenoc_endpoint_set_multicast_address(
    volatile csr__endpoint_interface_t *endpoint, const openenoc_endpoint_mac_t *address) {
    if (endpoint == NULL || ((uintptr_t)endpoint & 3U) != 0U || address == NULL ||
        !multicast_address_valid(address)) {
        return OPENENOC_ENDPOINT_STATUS_INVALID_ARGUMENT;
    }
    {
        openenoc_endpoint_mac_words_t words = openenoc_endpoint_mac_pack(address);

        endpoint->config.multicast_address.f.lo_word = words.lower;
        endpoint->config.multicast_address.f.hi_word = words.upper;
    }
    return OPENENOC_ENDPOINT_STATUS_OK;
}

openenoc_endpoint_status_t openenoc_endpoint_set_receive_mode(
    volatile csr__endpoint_interface_t *endpoint, openenoc_endpoint_receive_mode_t mode) {
    if (endpoint == NULL || ((uintptr_t)endpoint & 3U) != 0U ||
        (unsigned int)mode > OPENENOC_ENDPOINT_RECEIVE_PROMISCUOUS) {
        return OPENENOC_ENDPOINT_STATUS_INVALID_ARGUMENT;
    }
    endpoint->config.non_oetp_control.f.receive_mode = mode;
    return OPENENOC_ENDPOINT_STATUS_OK;
}

openenoc_endpoint_status_t openenoc_endpoint_set_rmem_timeout(
    volatile csr__endpoint_interface_t *endpoint, uint32_t cycles) {
    if (CSR__HAS_RMEM == 0U) {
        return OPENENOC_ENDPOINT_STATUS_UNSUPPORTED;
    }
    if (endpoint == NULL || ((uintptr_t)endpoint & 3U) != 0U) {
        return OPENENOC_ENDPOINT_STATUS_INVALID_ARGUMENT;
    }
    endpoint->config.rmem_timeout.f.cycles = cycles;
    return OPENENOC_ENDPOINT_STATUS_OK;
}

openenoc_endpoint_status_t openenoc_endpoint_set_dma_timeout(
    volatile csr__endpoint_interface_t *endpoint, uint32_t cycles) {
    if (CSR__HAS_PEER_DMA == 0U) {
        return OPENENOC_ENDPOINT_STATUS_UNSUPPORTED;
    }
    if (endpoint == NULL || ((uintptr_t)endpoint & 3U) != 0U) {
        return OPENENOC_ENDPOINT_STATUS_INVALID_ARGUMENT;
    }
    endpoint->config.dma_timeout.f.cycles = cycles;
    return OPENENOC_ENDPOINT_STATUS_OK;
}

openenoc_endpoint_status_t openenoc_endpoint_set_dma_max_fragment_size(
    volatile csr__endpoint_interface_t *endpoint,
    uint32_t requested_bytes, uint32_t *effective_bytes) {
    uint32_t effective = requested_bytes & ~3U;

    if (CSR__HAS_PEER_DMA == 0U) {
        return OPENENOC_ENDPOINT_STATUS_UNSUPPORTED;
    }
    if (endpoint == NULL || ((uintptr_t)endpoint & 3U) != 0U) {
        return OPENENOC_ENDPOINT_STATUS_INVALID_ARGUMENT;
    }
    if (effective < 4U || effective > openenoc_endpoint_max_peer_fragment_size()) {
        return OPENENOC_ENDPOINT_STATUS_OUT_OF_RANGE;
    }
    endpoint->config.dma_max_fragment_size.f.bytes = requested_bytes;
    if (effective_bytes != NULL) {
        *effective_bytes = effective;
    }
    return OPENENOC_ENDPOINT_STATUS_OK;
}
