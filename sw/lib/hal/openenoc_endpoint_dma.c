/* SPDX-FileCopyrightText: 2026 Enio Kaljic
 * SPDX-License-Identifier: AGPL-3.0-or-later
 */

#define OPENENOC_ENDPOINT_IMPLEMENTATION
#include "openenoc_endpoint.h"

openenoc_endpoint_status_t openenoc_endpoint_non_oetp_dma_get_status(
    const volatile csr__endpoint_interface_t *endpoint, openenoc_endpoint_dma_channel_t channel,
    openenoc_endpoint_non_oetp_dma_status_t *status) {
    if (CSR__HAS_NON_OETP_DMA == 0U) {
        return OPENENOC_ENDPOINT_STATUS_UNSUPPORTED;
    }
    if (endpoint == NULL || ((uintptr_t)endpoint & 3U) != 0U || status == NULL ||
        (channel != OPENENOC_ENDPOINT_DMA_TX && channel != OPENENOC_ENDPOINT_DMA_RX)) {
        return OPENENOC_ENDPOINT_STATUS_INVALID_ARGUMENT;
    }
    if (channel == OPENENOC_ENDPOINT_DMA_TX) {
        status->request_pending = endpoint->non_oetp_dma.tx.command_status.f.request != 0U;
        status->clear_errors_pending =
            endpoint->non_oetp_dma.tx.command_status.f.clear_errors != 0U;
        status->idle = endpoint->non_oetp_dma.tx.command_status.f.idle != 0U;
        status->armed = false;
        status->done = endpoint->non_oetp_dma.tx.command_status.f.done != 0U;
        status->error = endpoint->non_oetp_dma.tx.command_status.f.error != 0U;
        status->error_code =
            (openenoc_endpoint_error_t)endpoint->non_oetp_dma.tx.command_status.f.error_code;
        status->transferred_bytes = endpoint->non_oetp_dma.tx.transferred_length.f.bytes;
    } else {
        status->request_pending = endpoint->non_oetp_dma.rx.command_status.f.request != 0U;
        status->clear_errors_pending =
            endpoint->non_oetp_dma.rx.command_status.f.clear_errors != 0U;
        status->idle = endpoint->non_oetp_dma.rx.command_status.f.idle != 0U;
        status->armed = endpoint->non_oetp_dma.rx.command_status.f.armed != 0U;
        status->done = endpoint->non_oetp_dma.rx.command_status.f.done != 0U;
        status->error = endpoint->non_oetp_dma.rx.command_status.f.error != 0U;
        status->error_code =
            (openenoc_endpoint_error_t)endpoint->non_oetp_dma.rx.command_status.f.error_code;
        status->transferred_bytes = endpoint->non_oetp_dma.rx.received_length.f.bytes;
    }
    return OPENENOC_ENDPOINT_STATUS_OK;
}

openenoc_endpoint_status_t openenoc_endpoint_non_oetp_dma_tx_request(
    volatile csr__endpoint_interface_t *endpoint,
    uint32_t buffer_address, uint32_t frame_length_bytes) {
    if (CSR__HAS_NON_OETP_DMA == 0U) {
        return OPENENOC_ENDPOINT_STATUS_UNSUPPORTED;
    }
    if (endpoint == NULL || ((uintptr_t)endpoint & 3U) != 0U) {
        return OPENENOC_ENDPOINT_STATUS_INVALID_ARGUMENT;
    }
    if (!openenoc_endpoint_address_range_valid(buffer_address, frame_length_bytes) ||
        frame_length_bytes > CSR__MAX_RAW_FRAME_SIZE) {
        return OPENENOC_ENDPOINT_STATUS_OUT_OF_RANGE;
    }
    if (endpoint->non_oetp_dma.tx.command_status.f.request ||
        endpoint->non_oetp_dma.tx.command_status.f.clear_errors ||
        !endpoint->non_oetp_dma.tx.command_status.f.idle) {
        return OPENENOC_ENDPOINT_STATUS_NOT_READY;
    }
    endpoint->non_oetp_dma.tx.buffer_address.f.base = buffer_address;
    endpoint->non_oetp_dma.tx.frame_length.f.bytes = frame_length_bytes;
    endpoint->non_oetp_dma.tx.command_status.f.request = 1U;
    return OPENENOC_ENDPOINT_STATUS_OK;
}

openenoc_endpoint_status_t openenoc_endpoint_non_oetp_dma_rx_arm(
    volatile csr__endpoint_interface_t *endpoint,
    uint32_t buffer_address, uint32_t buffer_capacity_bytes) {
    if (CSR__HAS_NON_OETP_DMA == 0U) {
        return OPENENOC_ENDPOINT_STATUS_UNSUPPORTED;
    }
    if (endpoint == NULL || ((uintptr_t)endpoint & 3U) != 0U) {
        return OPENENOC_ENDPOINT_STATUS_INVALID_ARGUMENT;
    }
    if (!openenoc_endpoint_address_range_valid(buffer_address, buffer_capacity_bytes) ||
        buffer_capacity_bytes > CSR__MAX_RAW_FRAME_SIZE) {
        return OPENENOC_ENDPOINT_STATUS_OUT_OF_RANGE;
    }
    if (endpoint->non_oetp_dma.rx.command_status.f.request ||
        endpoint->non_oetp_dma.rx.command_status.f.clear_errors ||
        !endpoint->non_oetp_dma.rx.command_status.f.idle) {
        return OPENENOC_ENDPOINT_STATUS_NOT_READY;
    }
    endpoint->non_oetp_dma.rx.buffer_address.f.base = buffer_address;
    endpoint->non_oetp_dma.rx.buffer_capacity.f.bytes = buffer_capacity_bytes;
    endpoint->non_oetp_dma.rx.command_status.f.request = 1U;
    return OPENENOC_ENDPOINT_STATUS_OK;
}

openenoc_endpoint_status_t openenoc_endpoint_non_oetp_dma_request_clear_errors(
    volatile csr__endpoint_interface_t *endpoint, openenoc_endpoint_dma_channel_t channel) {
    if (CSR__HAS_NON_OETP_DMA == 0U) {
        return OPENENOC_ENDPOINT_STATUS_UNSUPPORTED;
    }
    if (endpoint == NULL || ((uintptr_t)endpoint & 3U) != 0U ||
        (channel != OPENENOC_ENDPOINT_DMA_TX && channel != OPENENOC_ENDPOINT_DMA_RX)) {
        return OPENENOC_ENDPOINT_STATUS_INVALID_ARGUMENT;
    }
    if (channel == OPENENOC_ENDPOINT_DMA_TX) {
        if (endpoint->non_oetp_dma.tx.command_status.f.request ||
            endpoint->non_oetp_dma.tx.command_status.f.clear_errors) {
            return OPENENOC_ENDPOINT_STATUS_NOT_READY;
        }
        endpoint->non_oetp_dma.tx.command_status.f.clear_errors = 1U;
    } else {
        if (endpoint->non_oetp_dma.rx.command_status.f.request ||
            endpoint->non_oetp_dma.rx.command_status.f.clear_errors) {
            return OPENENOC_ENDPOINT_STATUS_NOT_READY;
        }
        endpoint->non_oetp_dma.rx.command_status.f.clear_errors = 1U;
    }
    return OPENENOC_ENDPOINT_STATUS_OK;
}
