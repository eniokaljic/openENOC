/* SPDX-FileCopyrightText: 2026 Enio Kaljic
 * SPDX-License-Identifier: AGPL-3.0-or-later
 */

#ifndef OPENENOC_ENDPOINT_DMA_H
#define OPENENOC_ENDPOINT_DMA_H

#include "openenoc_endpoint_common.h"

#ifdef __cplusplus
extern "C" {
#endif

typedef enum {
    OPENENOC_ENDPOINT_DMA_TX = 0,
    OPENENOC_ENDPOINT_DMA_RX = 1
} openenoc_endpoint_dma_channel_t;

typedef struct {
    bool request_pending;
    bool clear_errors_pending;
    bool idle;
    bool armed;
    bool done;
    bool error;
    openenoc_endpoint_error_t error_code;
    uint32_t transferred_bytes;
} openenoc_endpoint_non_oetp_dma_status_t;

openenoc_endpoint_status_t openenoc_endpoint_non_oetp_dma_tx_request(
    volatile csr__endpoint_interface_t *endpoint,
    uint32_t buffer_address, uint32_t frame_length_bytes);

openenoc_endpoint_status_t openenoc_endpoint_non_oetp_dma_rx_arm(
    volatile csr__endpoint_interface_t *endpoint,
    uint32_t buffer_address, uint32_t buffer_capacity_bytes);

openenoc_endpoint_status_t openenoc_endpoint_non_oetp_dma_get_status(
    const volatile csr__endpoint_interface_t *endpoint, openenoc_endpoint_dma_channel_t channel,
    openenoc_endpoint_non_oetp_dma_status_t *status);

openenoc_endpoint_status_t openenoc_endpoint_non_oetp_dma_request_clear_errors(
    volatile csr__endpoint_interface_t *endpoint, openenoc_endpoint_dma_channel_t channel);

#ifdef __cplusplus
}
#endif

#endif
