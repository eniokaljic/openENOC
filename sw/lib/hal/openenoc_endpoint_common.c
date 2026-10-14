/* SPDX-FileCopyrightText: 2026 Enio Kaljic
 * SPDX-License-Identifier: AGPL-3.0-or-later
 */

#define OPENENOC_ENDPOINT_IMPLEMENTATION
#include "openenoc_endpoint.h"

openenoc_endpoint_status_t openenoc_endpoint_init(
    volatile csr__endpoint_interface_t *endpoint) {
    if (endpoint == NULL || ((uintptr_t)endpoint & 3U) != 0U) {
        return OPENENOC_ENDPOINT_STATUS_INVALID_ARGUMENT;
    }
    return OPENENOC_ENDPOINT_STATUS_OK;
}

openenoc_endpoint_status_t openenoc_endpoint_get_info(
    const volatile csr__endpoint_interface_t *endpoint, openenoc_endpoint_info_t *info) {
    if (endpoint == NULL || ((uintptr_t)endpoint & 3U) != 0U || info == NULL) {
        return OPENENOC_ENDPOINT_STATUS_INVALID_ARGUMENT;
    }
    info->rmem_word_count = CSR__RMEM_TOTAL_DEPTH;
    info->peer_count = CSR__NUM_OF_PEERS;
    info->max_raw_frame_size_bytes = CSR__MAX_RAW_FRAME_SIZE;
    info->peer_dma_supported = CSR__HAS_PEER_DMA != 0U;
    info->non_oetp_dma_supported = CSR__HAS_NON_OETP_DMA != 0U;
    info->direct_axis_supported = CSR__HAS_DIRECT_AXIS != 0U;
    info->rmem_supported = CSR__HAS_RMEM != 0U;
    info->irq_supported = CSR__HAS_IRQ != 0U;
    info->max_peer_fragment_size_bytes = openenoc_endpoint_max_peer_fragment_size();
    return OPENENOC_ENDPOINT_STATUS_OK;
}
