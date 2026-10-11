/* SPDX-FileCopyrightText: 2026 Enio Kaljic
 * SPDX-License-Identifier: AGPL-3.0-or-later
 */

#include <stddef.h>

#include "openenoc_endpoint_irq.h"

static volatile csr__endpoint_interface__irq_t *bound_irq;
static const openenoc_endpoint_irq_callbacks_t *bound_callbacks;

void openenoc_endpoint_irq_mask(void) {
    _openenoc_endpoint_irq_disable_all();
}

void openenoc_endpoint_irq_unmask(void) {
    _openenoc_endpoint_irq_enable_endpoint();
}

void openenoc_endpoint_irq_bind(
    volatile csr__endpoint_interface__irq_t *irq,
    const openenoc_endpoint_irq_callbacks_t *callbacks) {
    bound_irq = irq;
    bound_callbacks = callbacks;
}

openenoc_endpoint_irq_result_t openenoc_endpoint_irq_handler(uintptr_t cpu_irq_state) {
    unsigned int result = OPENENOC_ENDPOINT_IRQ_RESULT_OK;

    if (_openenoc_endpoint_irq_has_unhandled_sources(cpu_irq_state)) {
        result |= OPENENOC_ENDPOINT_IRQ_RESULT_UNHANDLED_CPU_IRQ;
        openenoc_endpoint_irq_mask();
    }
    if (bound_irq == NULL) {
        result |= OPENENOC_ENDPOINT_IRQ_RESULT_NOT_BOUND;
        openenoc_endpoint_irq_mask();
    } else if (_openenoc_endpoint_irq_is_endpoint(cpu_irq_state)) {
        result |= openenoc_endpoint_irq_service(bound_irq, bound_callbacks);
    }

    if (result != OPENENOC_ENDPOINT_IRQ_RESULT_OK &&
        bound_callbacks != NULL && bound_callbacks->error != NULL) {
        bound_callbacks->error((openenoc_endpoint_irq_result_t)result,
                               bound_callbacks->context);
    }
    return (openenoc_endpoint_irq_result_t)result;
}

void openenoc_endpoint_irq_configure(
    volatile csr__endpoint_interface__irq_t *irq,
    const openenoc_endpoint_irq_config_t *config) {
    openenoc_endpoint_irq_set_global_enable(irq, false);
    irq->event_enable.f.peer_dma_complete = config->peer_dma_complete;
    irq->event_enable.f.non_oetp_dma_tx_complete = config->non_oetp_dma_tx_complete;
    irq->event_enable.f.non_oetp_dma_rx_complete = config->non_oetp_dma_rx_complete;
    irq->event_enable.f.non_oetp_direct_tx_complete = config->non_oetp_direct_tx_complete;
    irq->event_enable.f.non_oetp_direct_rx_available = config->non_oetp_direct_rx_available;
    irq->event_enable.f.rmem_error = config->rmem_error;
    openenoc_endpoint_irq_set_global_enable(irq, config->global_enable);
}

void openenoc_endpoint_irq_get_config(
    volatile csr__endpoint_interface__irq_t *irq,
    openenoc_endpoint_irq_config_t *config) {
    config->global_enable = irq->control.f.global_enable != 0U;
    config->peer_dma_complete = irq->event_enable.f.peer_dma_complete != 0U;
    config->non_oetp_dma_tx_complete = irq->event_enable.f.non_oetp_dma_tx_complete != 0U;
    config->non_oetp_dma_rx_complete = irq->event_enable.f.non_oetp_dma_rx_complete != 0U;
    config->non_oetp_direct_tx_complete = irq->event_enable.f.non_oetp_direct_tx_complete != 0U;
    config->non_oetp_direct_rx_available = irq->event_enable.f.non_oetp_direct_rx_available != 0U;
    config->rmem_error = irq->event_enable.f.rmem_error != 0U;
}

void openenoc_endpoint_irq_set_global_enable(
    volatile csr__endpoint_interface__irq_t *irq,
    bool enable) {
    irq->control.f.global_enable = enable;
}

bool openenoc_endpoint_irq_set_event_enable(
    volatile csr__endpoint_interface__irq_t *irq,
    openenoc_endpoint_irq_source_t source,
    bool enable) {
    switch (source) {
    case OPENENOC_ENDPOINT_IRQ_SOURCE_PEER_DMA_COMPLETE:
        irq->event_enable.f.peer_dma_complete = enable;
        break;
    case OPENENOC_ENDPOINT_IRQ_SOURCE_NON_OETP_DMA_TX_COMPLETE:
        irq->event_enable.f.non_oetp_dma_tx_complete = enable;
        break;
    case OPENENOC_ENDPOINT_IRQ_SOURCE_NON_OETP_DMA_RX_COMPLETE:
        irq->event_enable.f.non_oetp_dma_rx_complete = enable;
        break;
    case OPENENOC_ENDPOINT_IRQ_SOURCE_NON_OETP_DIRECT_TX_COMPLETE:
        irq->event_enable.f.non_oetp_direct_tx_complete = enable;
        break;
    case OPENENOC_ENDPOINT_IRQ_SOURCE_NON_OETP_DIRECT_RX_AVAILABLE:
        irq->event_enable.f.non_oetp_direct_rx_available = enable;
        break;
    case OPENENOC_ENDPOINT_IRQ_SOURCE_RMEM_ERROR:
        irq->event_enable.f.rmem_error = enable;
        break;
    default:
        return false;
    }
    return true;
}

void openenoc_endpoint_irq_get_status(
    volatile csr__endpoint_interface__irq_t *irq,
    openenoc_endpoint_irq_status_t *status) {
    status->claim_pending = irq->status.f.claim_pending != 0U;
    status->credit_full = irq->status.f.credit_full != 0U;
    status->overflow = irq->status.f.overflow != 0U;
    status->invalid_complete = irq->status.f.invalid_complete != 0U;
    status->irq_asserted = irq->status.f.irq_asserted != 0U;
    status->fifo_level = (uint8_t)irq->status.f.fifo_level;
    status->reserved_count = (uint8_t)irq->status.f.reserved_count;
}

void openenoc_endpoint_irq_clear_errors(
    volatile csr__endpoint_interface__irq_t *irq) {
    irq->control.f.clear_errors = 1U;
    while (irq->control.f.clear_errors != 0U) {
    }
}

void openenoc_endpoint_irq_complete(
    volatile csr__endpoint_interface__irq_t *irq) {
    irq->complete.f.peer_idx = irq->claim.f.peer_idx;
    irq->complete.f.source = irq->claim.f.source;
    irq->complete.f.sequence = irq->claim.f.sequence;
    irq->complete.f.valid = 1U;
    while (irq->complete.f.valid != 0U) {
    }
}

openenoc_endpoint_irq_result_t openenoc_endpoint_irq_service(
    volatile csr__endpoint_interface__irq_t *irq,
    const openenoc_endpoint_irq_callbacks_t *callbacks) {
    unsigned int result = OPENENOC_ENDPOINT_IRQ_RESULT_OK;

    while (irq->claim.f.valid != 0U) {
        openenoc_endpoint_irq_callback_t callback = NULL;
        if (callbacks != NULL) {
            switch (irq->claim.f.source) {
            case OPENENOC_ENDPOINT_IRQ_SOURCE_PEER_DMA_COMPLETE:
                callback = callbacks->peer_dma_complete;
                break;
            case OPENENOC_ENDPOINT_IRQ_SOURCE_NON_OETP_DMA_TX_COMPLETE:
                callback = callbacks->non_oetp_dma_tx_complete;
                break;
            case OPENENOC_ENDPOINT_IRQ_SOURCE_NON_OETP_DMA_RX_COMPLETE:
                callback = callbacks->non_oetp_dma_rx_complete;
                break;
            case OPENENOC_ENDPOINT_IRQ_SOURCE_NON_OETP_DIRECT_TX_COMPLETE:
                callback = callbacks->non_oetp_direct_tx_complete;
                break;
            case OPENENOC_ENDPOINT_IRQ_SOURCE_NON_OETP_DIRECT_RX_AVAILABLE:
                callback = callbacks->non_oetp_direct_rx_available;
                break;
            case OPENENOC_ENDPOINT_IRQ_SOURCE_RMEM_ERROR:
                callback = callbacks->rmem_error;
                break;
            default:
                break;
            }
        }

        if (callback != NULL) {
            callback(irq, callbacks->context);
        } else {
            result |= OPENENOC_ENDPOINT_IRQ_RESULT_UNHANDLED_SOURCE;
        }
        openenoc_endpoint_irq_complete(irq);
    }

    if (irq->status.f.overflow != 0U) {
        result |= OPENENOC_ENDPOINT_IRQ_RESULT_OVERFLOW;
    }
    if (irq->status.f.invalid_complete != 0U) {
        result |= OPENENOC_ENDPOINT_IRQ_RESULT_INVALID_COMPLETE;
    }
    return (openenoc_endpoint_irq_result_t)result;
}
