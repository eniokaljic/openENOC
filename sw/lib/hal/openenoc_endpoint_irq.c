/* SPDX-FileCopyrightText: 2026 Enio Kaljic
 * SPDX-License-Identifier: AGPL-3.0-or-later
 */

#define OPENENOC_ENDPOINT_IMPLEMENTATION
#include "openenoc_endpoint.h"

static volatile csr__endpoint_interface_t *bound_endpoint;
static const openenoc_endpoint_irq_callbacks_t *bound_callbacks;

void openenoc_endpoint_irq_mask(void) {
    _openenoc_endpoint_irq_disable_all();
}

void openenoc_endpoint_irq_unmask(void) {
    _openenoc_endpoint_irq_enable_endpoint();
}

openenoc_endpoint_irq_result_t openenoc_endpoint_irq_handler(uintptr_t cpu_irq_state) {
    unsigned int result = OPENENOC_ENDPOINT_IRQ_RESULT_OK;

    if (_openenoc_endpoint_irq_has_unhandled_sources(cpu_irq_state)) {
        result |= OPENENOC_ENDPOINT_IRQ_RESULT_UNHANDLED_CPU_IRQ;
        openenoc_endpoint_irq_mask();
    }
    if (bound_endpoint == NULL) {
        result |= OPENENOC_ENDPOINT_IRQ_RESULT_NOT_BOUND;
        openenoc_endpoint_irq_mask();
    } else if (_openenoc_endpoint_irq_is_endpoint(cpu_irq_state)) {
        result |= openenoc_endpoint_irq_service(bound_endpoint, bound_callbacks, 32U, NULL);
    }
    if (result != OPENENOC_ENDPOINT_IRQ_RESULT_OK &&
        bound_callbacks != NULL && bound_callbacks->error != NULL) {
        bound_callbacks->error((openenoc_endpoint_irq_result_t)result, bound_callbacks->context);
    }
    return (openenoc_endpoint_irq_result_t)result;
}

static bool event_source_valid(openenoc_endpoint_irq_source_t source) {
    return source >= OPENENOC_ENDPOINT_IRQ_SOURCE_PEER_DMA_COMPLETE &&
        source <= OPENENOC_ENDPOINT_IRQ_SOURCE_RMEM_ERROR;
}

static bool event_supported(openenoc_endpoint_irq_source_t source) {
    switch (source) {
    case OPENENOC_ENDPOINT_IRQ_SOURCE_PEER_DMA_COMPLETE:
        return CSR__HAS_PEER_DMA != 0U;
    case OPENENOC_ENDPOINT_IRQ_SOURCE_NON_OETP_DMA_TX_COMPLETE:
    case OPENENOC_ENDPOINT_IRQ_SOURCE_NON_OETP_DMA_RX_COMPLETE:
        return CSR__HAS_NON_OETP_DMA != 0U;
    case OPENENOC_ENDPOINT_IRQ_SOURCE_NON_OETP_DIRECT_TX_COMPLETE:
    case OPENENOC_ENDPOINT_IRQ_SOURCE_NON_OETP_DIRECT_RX_AVAILABLE:
        return CSR__HAS_DIRECT_AXIS != 0U;
    case OPENENOC_ENDPOINT_IRQ_SOURCE_RMEM_ERROR:
        return CSR__HAS_RMEM != 0U;
    default:
        return false;
    }
}

openenoc_endpoint_status_t openenoc_endpoint_irq_get_config(
    const volatile csr__endpoint_interface_t *endpoint, openenoc_endpoint_irq_config_t *config) {
    if (CSR__HAS_IRQ == 0U) {
        return OPENENOC_ENDPOINT_STATUS_UNSUPPORTED;
    }
    if (config == NULL) {
        return OPENENOC_ENDPOINT_STATUS_INVALID_ARGUMENT;
    }
    if (endpoint == NULL || ((uintptr_t)endpoint & 3U) != 0U) {
        return OPENENOC_ENDPOINT_STATUS_INVALID_ARGUMENT;
    }
    config->global_enable = endpoint->irq.control.f.global_enable != 0U;
    config->peer_dma_complete = endpoint->irq.event_enable.f.peer_dma_complete != 0U;
    config->non_oetp_dma_tx_complete = endpoint->irq.event_enable.f.non_oetp_dma_tx_complete != 0U;
    config->non_oetp_dma_rx_complete = endpoint->irq.event_enable.f.non_oetp_dma_rx_complete != 0U;
    config->non_oetp_direct_tx_complete =
        endpoint->irq.event_enable.f.non_oetp_direct_tx_complete != 0U;
    config->non_oetp_direct_rx_available =
        endpoint->irq.event_enable.f.non_oetp_direct_rx_available != 0U;
    config->rmem_error = endpoint->irq.event_enable.f.rmem_error != 0U;
    return OPENENOC_ENDPOINT_STATUS_OK;
}

openenoc_endpoint_status_t openenoc_endpoint_irq_set_config(
    volatile csr__endpoint_interface_t *endpoint, const openenoc_endpoint_irq_config_t *config) {
    if (CSR__HAS_IRQ == 0U) {
        return OPENENOC_ENDPOINT_STATUS_UNSUPPORTED;
    }
    if (config == NULL) {
        return OPENENOC_ENDPOINT_STATUS_INVALID_ARGUMENT;
    }
    if (endpoint == NULL || ((uintptr_t)endpoint & 3U) != 0U) {
        return OPENENOC_ENDPOINT_STATUS_INVALID_ARGUMENT;
    }
    if ((config->peer_dma_complete && CSR__HAS_PEER_DMA == 0U) ||
        ((config->non_oetp_dma_tx_complete || config->non_oetp_dma_rx_complete) &&
         CSR__HAS_NON_OETP_DMA == 0U) ||
        ((config->non_oetp_direct_tx_complete || config->non_oetp_direct_rx_available) &&
         CSR__HAS_DIRECT_AXIS == 0U) || (config->rmem_error && CSR__HAS_RMEM == 0U)) {
        return OPENENOC_ENDPOINT_STATUS_UNSUPPORTED;
    }
    if (endpoint->irq.control.f.clear_errors) {
        return OPENENOC_ENDPOINT_STATUS_NOT_READY;
    }
    endpoint->irq.control.f.global_enable = 0U;
    endpoint->irq.event_enable.f.peer_dma_complete = config->peer_dma_complete;
    endpoint->irq.event_enable.f.non_oetp_dma_tx_complete = config->non_oetp_dma_tx_complete;
    endpoint->irq.event_enable.f.non_oetp_dma_rx_complete = config->non_oetp_dma_rx_complete;
    endpoint->irq.event_enable.f.non_oetp_direct_tx_complete = config->non_oetp_direct_tx_complete;
    endpoint->irq.event_enable.f.non_oetp_direct_rx_available =
        config->non_oetp_direct_rx_available;
    endpoint->irq.event_enable.f.rmem_error = config->rmem_error;
    endpoint->irq.control.f.global_enable = config->global_enable;
    return OPENENOC_ENDPOINT_STATUS_OK;
}

openenoc_endpoint_status_t openenoc_endpoint_irq_set_global_enable(
    volatile csr__endpoint_interface_t *endpoint, bool enable) {
    if (CSR__HAS_IRQ == 0U) {
        return OPENENOC_ENDPOINT_STATUS_UNSUPPORTED;
    }
    if (endpoint == NULL || ((uintptr_t)endpoint & 3U) != 0U) {
        return OPENENOC_ENDPOINT_STATUS_INVALID_ARGUMENT;
    }
    if (endpoint->irq.control.f.clear_errors) {
        return OPENENOC_ENDPOINT_STATUS_NOT_READY;
    }
    endpoint->irq.control.f.global_enable = enable;
    return OPENENOC_ENDPOINT_STATUS_OK;
}

openenoc_endpoint_status_t openenoc_endpoint_irq_set_event_enable(
    volatile csr__endpoint_interface_t *endpoint,
    openenoc_endpoint_irq_source_t source, bool enable) {
    if (CSR__HAS_IRQ == 0U) {
        return OPENENOC_ENDPOINT_STATUS_UNSUPPORTED;
    }
    if (endpoint == NULL || ((uintptr_t)endpoint & 3U) != 0U) {
        return OPENENOC_ENDPOINT_STATUS_INVALID_ARGUMENT;
    }
    if (!event_source_valid(source)) {
        return OPENENOC_ENDPOINT_STATUS_INVALID_ARGUMENT;
    }
    if (enable && !event_supported(source)) {
        return OPENENOC_ENDPOINT_STATUS_UNSUPPORTED;
    }
    switch (source) {
    case OPENENOC_ENDPOINT_IRQ_SOURCE_PEER_DMA_COMPLETE:
        endpoint->irq.event_enable.f.peer_dma_complete = enable;
        break;
    case OPENENOC_ENDPOINT_IRQ_SOURCE_NON_OETP_DMA_TX_COMPLETE:
        endpoint->irq.event_enable.f.non_oetp_dma_tx_complete = enable;
        break;
    case OPENENOC_ENDPOINT_IRQ_SOURCE_NON_OETP_DMA_RX_COMPLETE:
        endpoint->irq.event_enable.f.non_oetp_dma_rx_complete = enable;
        break;
    case OPENENOC_ENDPOINT_IRQ_SOURCE_NON_OETP_DIRECT_TX_COMPLETE:
        endpoint->irq.event_enable.f.non_oetp_direct_tx_complete = enable;
        break;
    case OPENENOC_ENDPOINT_IRQ_SOURCE_NON_OETP_DIRECT_RX_AVAILABLE:
        endpoint->irq.event_enable.f.non_oetp_direct_rx_available = enable;
        break;
    case OPENENOC_ENDPOINT_IRQ_SOURCE_RMEM_ERROR:
        endpoint->irq.event_enable.f.rmem_error = enable;
        break;
    default:
        return OPENENOC_ENDPOINT_STATUS_INVALID_ARGUMENT;
    }
    return OPENENOC_ENDPOINT_STATUS_OK;
}

openenoc_endpoint_status_t openenoc_endpoint_irq_get_status(
    const volatile csr__endpoint_interface_t *endpoint, openenoc_endpoint_irq_status_t *status) {
    if (CSR__HAS_IRQ == 0U) {
        return OPENENOC_ENDPOINT_STATUS_UNSUPPORTED;
    }
    if (status == NULL) {
        return OPENENOC_ENDPOINT_STATUS_INVALID_ARGUMENT;
    }
    if (endpoint == NULL || ((uintptr_t)endpoint & 3U) != 0U) {
        return OPENENOC_ENDPOINT_STATUS_INVALID_ARGUMENT;
    }
    status->claim_pending = endpoint->irq.status.f.claim_pending != 0U;
    status->credit_full = endpoint->irq.status.f.credit_full != 0U;
    status->overflow = endpoint->irq.status.f.overflow != 0U;
    status->invalid_complete = endpoint->irq.status.f.invalid_complete != 0U;
    status->irq_asserted = endpoint->irq.status.f.irq_asserted != 0U;
    status->fifo_level = (uint8_t)endpoint->irq.status.f.fifo_level;
    status->reserved_count = (uint8_t)endpoint->irq.status.f.reserved_count;
    return OPENENOC_ENDPOINT_STATUS_OK;
}

openenoc_endpoint_status_t openenoc_endpoint_irq_get_claim(
    const volatile csr__endpoint_interface_t *endpoint, openenoc_endpoint_irq_claim_t *claim) {
    if (CSR__HAS_IRQ == 0U) {
        return OPENENOC_ENDPOINT_STATUS_UNSUPPORTED;
    }
    if (claim == NULL) {
        return OPENENOC_ENDPOINT_STATUS_INVALID_ARGUMENT;
    }
    if (endpoint == NULL || ((uintptr_t)endpoint & 3U) != 0U) {
        return OPENENOC_ENDPOINT_STATUS_INVALID_ARGUMENT;
    }
    if (!endpoint->irq.claim.f.valid) {
        return OPENENOC_ENDPOINT_STATUS_NOT_READY;
    }
    claim->peer_index = endpoint->irq.claim.f.peer_idx;
    claim->source = (openenoc_endpoint_irq_source_t)endpoint->irq.claim.f.source;
    claim->sequence = endpoint->irq.claim.f.sequence;
    return OPENENOC_ENDPOINT_STATUS_OK;
}

openenoc_endpoint_status_t openenoc_endpoint_irq_request_complete(
    volatile csr__endpoint_interface_t *endpoint, const openenoc_endpoint_irq_claim_t *claim) {
    openenoc_endpoint_irq_claim_t current;

    if (CSR__HAS_IRQ == 0U) {
        return OPENENOC_ENDPOINT_STATUS_UNSUPPORTED;
    }
    if (claim == NULL) {
        return OPENENOC_ENDPOINT_STATUS_INVALID_ARGUMENT;
    }
    if (endpoint == NULL || ((uintptr_t)endpoint & 3U) != 0U) {
        return OPENENOC_ENDPOINT_STATUS_INVALID_ARGUMENT;
    }
    if (endpoint->irq.complete.f.valid) {
        return OPENENOC_ENDPOINT_STATUS_NOT_READY;
    }
    if (!endpoint->irq.claim.f.valid) {
        return OPENENOC_ENDPOINT_STATUS_INVALID_ARGUMENT;
    }
    current.peer_index = endpoint->irq.claim.f.peer_idx;
    current.source = (openenoc_endpoint_irq_source_t)endpoint->irq.claim.f.source;
    current.sequence = endpoint->irq.claim.f.sequence;
    if (current.source != claim->source || current.peer_index != claim->peer_index ||
        current.sequence != claim->sequence) {
        return OPENENOC_ENDPOINT_STATUS_INVALID_ARGUMENT;
    }
    endpoint->irq.complete.f.peer_idx = current.peer_index;
    endpoint->irq.complete.f.source = current.source;
    endpoint->irq.complete.f.sequence = current.sequence;
    endpoint->irq.complete.f.valid = 1U;
    return OPENENOC_ENDPOINT_STATUS_OK;
}

openenoc_endpoint_status_t openenoc_endpoint_irq_request_clear_errors(
    volatile csr__endpoint_interface_t *endpoint) {
    if (CSR__HAS_IRQ == 0U) {
        return OPENENOC_ENDPOINT_STATUS_UNSUPPORTED;
    }
    if (endpoint == NULL || ((uintptr_t)endpoint & 3U) != 0U) {
        return OPENENOC_ENDPOINT_STATUS_INVALID_ARGUMENT;
    }
    if (endpoint->irq.control.f.clear_errors) {
        return OPENENOC_ENDPOINT_STATUS_NOT_READY;
    }
    endpoint->irq.control.f.clear_errors = 1U;
    return OPENENOC_ENDPOINT_STATUS_OK;
}

openenoc_endpoint_status_t openenoc_endpoint_irq_get_pending_commands(
    const volatile csr__endpoint_interface_t *endpoint,
    bool *clear_errors_pending, bool *complete_pending) {
    if (CSR__HAS_IRQ == 0U) {
        return OPENENOC_ENDPOINT_STATUS_UNSUPPORTED;
    }
    if (clear_errors_pending == NULL && complete_pending == NULL) {
        return OPENENOC_ENDPOINT_STATUS_INVALID_ARGUMENT;
    }
    if (endpoint == NULL || ((uintptr_t)endpoint & 3U) != 0U) {
        return OPENENOC_ENDPOINT_STATUS_INVALID_ARGUMENT;
    }
    if (clear_errors_pending != NULL) {
        *clear_errors_pending = endpoint->irq.control.f.clear_errors != 0U;
    }
    if (complete_pending != NULL) {
        *complete_pending = endpoint->irq.complete.f.valid != 0U;
    }
    return OPENENOC_ENDPOINT_STATUS_OK;
}

openenoc_endpoint_irq_result_t openenoc_endpoint_irq_service(
    volatile csr__endpoint_interface_t *endpoint,
    const openenoc_endpoint_irq_callbacks_t *callbacks,
    uint32_t event_budget, uint32_t *handled_events) {
    uint32_t handled = 0U;
    unsigned int result = OPENENOC_ENDPOINT_IRQ_RESULT_OK;

    if (CSR__HAS_IRQ == 0U) {
        if (handled_events != NULL) {
            *handled_events = 0U;
        }
        return OPENENOC_ENDPOINT_IRQ_RESULT_UNSUPPORTED;
    }
    if (handled_events != NULL) {
        *handled_events = 0U;
    }
    if (endpoint == NULL || ((uintptr_t)endpoint & 3U) != 0U) {
        return OPENENOC_ENDPOINT_IRQ_RESULT_INVALID_ARGUMENT;
    }
    while (handled < event_budget) {
        openenoc_endpoint_irq_claim_t claim;
        openenoc_endpoint_irq_callback_t callback = NULL;

        if (endpoint->irq.complete.f.valid || !endpoint->irq.claim.f.valid) {
            break;
        }
        claim.peer_index = endpoint->irq.claim.f.peer_idx;
        claim.source = (openenoc_endpoint_irq_source_t)endpoint->irq.claim.f.source;
        claim.sequence = endpoint->irq.claim.f.sequence;

        if (callbacks != NULL) {
            switch (claim.source) {
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
            callback(endpoint, &claim, callbacks->context);
        } else {
            result |= OPENENOC_ENDPOINT_IRQ_RESULT_UNHANDLED_SOURCE;
        }
        if (openenoc_endpoint_irq_request_complete(endpoint, &claim) !=
            OPENENOC_ENDPOINT_STATUS_OK) {
            result |= OPENENOC_ENDPOINT_IRQ_RESULT_INVALID_COMPLETE;
            break;
        }
        ++handled;
    }
    if (endpoint->irq.status.f.overflow) {
        result |= OPENENOC_ENDPOINT_IRQ_RESULT_OVERFLOW;
    }
    if (endpoint->irq.status.f.invalid_complete) {
        result |= OPENENOC_ENDPOINT_IRQ_RESULT_INVALID_COMPLETE;
    }
    if (handled_events != NULL) {
        *handled_events = handled;
    }
    return (openenoc_endpoint_irq_result_t)result;
}

openenoc_endpoint_status_t openenoc_endpoint_irq_bind(
    volatile csr__endpoint_interface_t *endpoint,
    const openenoc_endpoint_irq_callbacks_t *callbacks) {
    if (endpoint == NULL && callbacks == NULL) {
        bound_endpoint = NULL;
        bound_callbacks = NULL;
        return OPENENOC_ENDPOINT_STATUS_OK;
    }
    if (CSR__HAS_IRQ == 0U) {
        return OPENENOC_ENDPOINT_STATUS_UNSUPPORTED;
    }
    if (endpoint == NULL || ((uintptr_t)endpoint & 3U) != 0U) {
        return OPENENOC_ENDPOINT_STATUS_INVALID_ARGUMENT;
    }
    bound_endpoint = endpoint;
    bound_callbacks = callbacks;
    return OPENENOC_ENDPOINT_STATUS_OK;
}

openenoc_endpoint_status_t openenoc_endpoint_irq_complete(
    volatile csr__endpoint_interface_t *endpoint) {
    openenoc_endpoint_irq_claim_t claim;

    if (CSR__HAS_IRQ == 0U) {
        return OPENENOC_ENDPOINT_STATUS_UNSUPPORTED;
    }
    if (endpoint == NULL || ((uintptr_t)endpoint & 3U) != 0U) {
        return OPENENOC_ENDPOINT_STATUS_INVALID_ARGUMENT;
    }
    if (!endpoint->irq.claim.f.valid) {
        return OPENENOC_ENDPOINT_STATUS_NOT_READY;
    }
    if (endpoint->irq.complete.f.valid) {
        return OPENENOC_ENDPOINT_STATUS_NOT_READY;
    }
    claim.peer_index = endpoint->irq.claim.f.peer_idx;
    claim.source = (openenoc_endpoint_irq_source_t)endpoint->irq.claim.f.source;
    claim.sequence = endpoint->irq.claim.f.sequence;
    endpoint->irq.complete.f.peer_idx = claim.peer_index;
    endpoint->irq.complete.f.source = claim.source;
    endpoint->irq.complete.f.sequence = claim.sequence;
    endpoint->irq.complete.f.valid = 1U;
    while (endpoint->irq.complete.f.valid) {
    }
    return OPENENOC_ENDPOINT_STATUS_OK;
}

openenoc_endpoint_status_t openenoc_endpoint_irq_clear_errors(
    volatile csr__endpoint_interface_t *endpoint) {
    if (CSR__HAS_IRQ == 0U) {
        return OPENENOC_ENDPOINT_STATUS_UNSUPPORTED;
    }
    if (endpoint == NULL || ((uintptr_t)endpoint & 3U) != 0U) {
        return OPENENOC_ENDPOINT_STATUS_INVALID_ARGUMENT;
    }
    if (endpoint->irq.control.f.clear_errors) {
        return OPENENOC_ENDPOINT_STATUS_NOT_READY;
    }
    endpoint->irq.control.f.clear_errors = 1U;
    while (endpoint->irq.control.f.clear_errors) {
    }
    return OPENENOC_ENDPOINT_STATUS_OK;
}
