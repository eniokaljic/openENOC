/* SPDX-FileCopyrightText: 2026 Enio Kaljic
 * SPDX-License-Identifier: AGPL-3.0-or-later
 */

#define OPENENOC_ENDPOINT_IMPLEMENTATION
#include "openenoc_endpoint.h"

openenoc_endpoint_status_t openenoc_endpoint_peer_get_config(
    const volatile csr__endpoint_interface_t *endpoint, uint16_t peer_index,
    openenoc_endpoint_peer_config_t *config) {
    if (CSR__HAS_PEER_DMA == 0U && CSR__HAS_RMEM == 0U) {
        return OPENENOC_ENDPOINT_STATUS_UNSUPPORTED;
    }
    if (config == NULL) {
        return OPENENOC_ENDPOINT_STATUS_INVALID_ARGUMENT;
    }
    if (endpoint == NULL || ((uintptr_t)endpoint & 3U) != 0U) {
        return OPENENOC_ENDPOINT_STATUS_INVALID_ARGUMENT;
    }
    if (peer_index >= CSR__NUM_OF_PEERS) {
        return OPENENOC_ENDPOINT_STATUS_OUT_OF_RANGE;
    }
    openenoc_endpoint_mac_unpack(endpoint->peers.entry[peer_index].mac_address.f.lo_word,
        endpoint->peers.entry[peer_index].mac_address.f.hi_word, &config->mac_address);
    config->rmem_offset_bytes = endpoint->peers.entry[peer_index].rmem_address.f.offset;
    config->local_address = endpoint->peers.entry[peer_index].local_address.f.base;
    config->remote_address = endpoint->peers.entry[peer_index].remote_address.f.base;
    config->size_bytes = endpoint->peers.entry[peer_index].size.f.bytes;
    config->mode = (openenoc_endpoint_peer_mode_t)endpoint->peers.entry[peer_index].dma.f.mode;
    config->irq_enable = endpoint->peers.entry[peer_index].dma.f.irq_enable != 0U;
    return OPENENOC_ENDPOINT_STATUS_OK;
}

openenoc_endpoint_status_t openenoc_endpoint_peer_set_config(
    volatile csr__endpoint_interface_t *endpoint, uint16_t peer_index,
    const openenoc_endpoint_peer_config_t *config) {
    if (CSR__HAS_PEER_DMA == 0U && CSR__HAS_RMEM == 0U) {
        return OPENENOC_ENDPOINT_STATUS_UNSUPPORTED;
    }
    if (config == NULL || (unsigned int)config->mode > OPENENOC_ENDPOINT_PEER_MIRROR_TO_REMOTE ||
        ((config->rmem_offset_bytes | config->local_address | config->remote_address) & 3U) != 0U) {
        return OPENENOC_ENDPOINT_STATUS_INVALID_ARGUMENT;
    }
    if (endpoint == NULL || ((uintptr_t)endpoint & 3U) != 0U) {
        return OPENENOC_ENDPOINT_STATUS_INVALID_ARGUMENT;
    }
    if (peer_index >= CSR__NUM_OF_PEERS) {
        return OPENENOC_ENDPOINT_STATUS_OUT_OF_RANGE;
    }
    if ((config->mode == OPENENOC_ENDPOINT_PEER_TRANSPARENT_RMEM && CSR__HAS_RMEM == 0U) ||
        ((config->mode == OPENENOC_ENDPOINT_PEER_MIRROR_TO_LOCAL ||
          config->mode == OPENENOC_ENDPOINT_PEER_MIRROR_TO_REMOTE) && CSR__HAS_PEER_DMA == 0U) ||
        (config->irq_enable && CSR__HAS_IRQ == 0U)) {
        return OPENENOC_ENDPOINT_STATUS_UNSUPPORTED;
    }
    if (config->mode != OPENENOC_ENDPOINT_PEER_DISABLED &&
        (!openenoc_endpoint_address_range_valid(config->local_address, config->size_bytes) ||
         !openenoc_endpoint_address_range_valid(config->remote_address, config->size_bytes))) {
        return OPENENOC_ENDPOINT_STATUS_OUT_OF_RANGE;
    }
    if (config->mode == OPENENOC_ENDPOINT_PEER_MIRROR_TO_LOCAL &&
        (config->mac_address.octet[0] & 1U) != 0U) {
        return OPENENOC_ENDPOINT_STATUS_INVALID_ARGUMENT;
    }
    if (config->mode == OPENENOC_ENDPOINT_PEER_TRANSPARENT_RMEM) {
        uint32_t start_word = config->rmem_offset_bytes / 4U;
        uint32_t size_words = config->size_bytes / 4U;
        uint32_t end_word;

        if ((config->size_bytes & 3U) != 0U || start_word > CSR__RMEM_TOTAL_DEPTH ||
            size_words > CSR__RMEM_TOTAL_DEPTH - start_word) {
            return OPENENOC_ENDPOINT_STATUS_OUT_OF_RANGE;
        }
        end_word = start_word + size_words;
        for (uint16_t other = 0; other < CSR__NUM_OF_PEERS; ++other) {
            uint32_t existing_start_word;
            uint32_t existing_size_words;

            if (other == peer_index || endpoint->peers.entry[other].dma.f.mode !=
                OPENENOC_ENDPOINT_PEER_TRANSPARENT_RMEM) {
                continue;
            }
            existing_start_word = endpoint->peers.entry[other].rmem_address.f.offset / 4U;
            existing_size_words = endpoint->peers.entry[other].size.f.bytes / 4U;
            if (start_word < existing_start_word + existing_size_words &&
                existing_start_word < end_word) {
                return OPENENOC_ENDPOINT_STATUS_INVALID_ARGUMENT;
            }
        }
    }
    if (endpoint->peers.entry[peer_index].dma.f.request ||
        endpoint->peers.entry[peer_index].dma.f.clear_error ||
        !endpoint->peers.entry[peer_index].dma.f.idle) {
        return OPENENOC_ENDPOINT_STATUS_NOT_READY;
    }
    /* Disable new lookups during the multi-register update; existing snapshots need quiescence. */
    endpoint->peers.entry[peer_index].dma.f.mode = OPENENOC_ENDPOINT_PEER_DISABLED;
    {
        openenoc_endpoint_mac_words_t words = openenoc_endpoint_mac_pack(&config->mac_address);

        endpoint->peers.entry[peer_index].mac_address.f.lo_word = words.lower;
        endpoint->peers.entry[peer_index].mac_address.f.hi_word = words.upper;
    }
    endpoint->peers.entry[peer_index].rmem_address.f.offset = config->rmem_offset_bytes;
    endpoint->peers.entry[peer_index].local_address.f.base = config->local_address;
    endpoint->peers.entry[peer_index].remote_address.f.base = config->remote_address;
    endpoint->peers.entry[peer_index].size.f.bytes = config->size_bytes;
    endpoint->peers.entry[peer_index].dma.f.irq_enable = config->irq_enable;
    endpoint->peers.entry[peer_index].dma.f.mode = config->mode;
    return OPENENOC_ENDPOINT_STATUS_OK;
}

openenoc_endpoint_status_t openenoc_endpoint_peer_get_status(
    const volatile csr__endpoint_interface_t *endpoint, uint16_t peer_index,
    openenoc_endpoint_peer_status_t *status) {
    if (CSR__HAS_PEER_DMA == 0U && CSR__HAS_RMEM == 0U) {
        return OPENENOC_ENDPOINT_STATUS_UNSUPPORTED;
    }
    if (status == NULL) {
        return OPENENOC_ENDPOINT_STATUS_INVALID_ARGUMENT;
    }
    if (endpoint == NULL || ((uintptr_t)endpoint & 3U) != 0U) {
        return OPENENOC_ENDPOINT_STATUS_INVALID_ARGUMENT;
    }
    if (peer_index >= CSR__NUM_OF_PEERS) {
        return OPENENOC_ENDPOINT_STATUS_OUT_OF_RANGE;
    }
    status->request_pending = endpoint->peers.entry[peer_index].dma.f.request != 0U;
    status->clear_error_pending = endpoint->peers.entry[peer_index].dma.f.clear_error != 0U;
    status->idle = endpoint->peers.entry[peer_index].dma.f.idle != 0U;
    status->done = endpoint->peers.entry[peer_index].dma.f.done != 0U;
    status->error = endpoint->peers.entry[peer_index].dma.f.error != 0U;
    status->error_code =
        (openenoc_endpoint_error_t)endpoint->peers.entry[peer_index].dma.f.error_code;
    return OPENENOC_ENDPOINT_STATUS_OK;
}

openenoc_endpoint_status_t openenoc_endpoint_peer_dma_request(
    volatile csr__endpoint_interface_t *endpoint, uint16_t peer_index) {
    uint32_t mode;
    uint32_t effective;

    if (CSR__HAS_PEER_DMA == 0U) {
        return OPENENOC_ENDPOINT_STATUS_UNSUPPORTED;
    }
    if (endpoint == NULL || ((uintptr_t)endpoint & 3U) != 0U) {
        return OPENENOC_ENDPOINT_STATUS_INVALID_ARGUMENT;
    }
    if (peer_index >= CSR__NUM_OF_PEERS) {
        return OPENENOC_ENDPOINT_STATUS_OUT_OF_RANGE;
    }
    if (endpoint->peers.entry[peer_index].dma.f.request ||
        endpoint->peers.entry[peer_index].dma.f.clear_error ||
        !endpoint->peers.entry[peer_index].dma.f.idle) {
        return OPENENOC_ENDPOINT_STATUS_NOT_READY;
    }
    mode = endpoint->peers.entry[peer_index].dma.f.mode;
    effective = endpoint->config.dma_max_fragment_size.f.bytes & ~3U;
    if ((mode != OPENENOC_ENDPOINT_PEER_MIRROR_TO_LOCAL &&
         mode != OPENENOC_ENDPOINT_PEER_MIRROR_TO_REMOTE) ||
        endpoint->peers.entry[peer_index].size.f.bytes == 0U ||
        effective < 4U || effective > openenoc_endpoint_max_peer_fragment_size()) {
        return OPENENOC_ENDPOINT_STATUS_INVALID_ARGUMENT;
    }
    endpoint->peers.entry[peer_index].dma.f.request = 1U;
    return OPENENOC_ENDPOINT_STATUS_OK;
}

openenoc_endpoint_status_t openenoc_endpoint_peer_request_clear_error(
    volatile csr__endpoint_interface_t *endpoint, uint16_t peer_index) {
    if (CSR__HAS_PEER_DMA == 0U && CSR__HAS_RMEM == 0U) {
        return OPENENOC_ENDPOINT_STATUS_UNSUPPORTED;
    }
    if (endpoint == NULL || ((uintptr_t)endpoint & 3U) != 0U) {
        return OPENENOC_ENDPOINT_STATUS_INVALID_ARGUMENT;
    }
    if (peer_index >= CSR__NUM_OF_PEERS) {
        return OPENENOC_ENDPOINT_STATUS_OUT_OF_RANGE;
    }
    if (endpoint->peers.entry[peer_index].dma.f.request ||
        endpoint->peers.entry[peer_index].dma.f.clear_error) {
        return OPENENOC_ENDPOINT_STATUS_NOT_READY;
    }
    endpoint->peers.entry[peer_index].dma.f.clear_error = 1U;
    return OPENENOC_ENDPOINT_STATUS_OK;
}
