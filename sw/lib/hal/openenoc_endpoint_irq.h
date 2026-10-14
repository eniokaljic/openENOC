/* SPDX-FileCopyrightText: 2026 Enio Kaljic
 * SPDX-License-Identifier: AGPL-3.0-or-later
 */

#ifndef OPENENOC_ENDPOINT_IRQ_H
#define OPENENOC_ENDPOINT_IRQ_H

#include "openenoc_endpoint_common.h"

#ifdef __cplusplus
extern "C" {
#endif

typedef enum {
    OPENENOC_ENDPOINT_IRQ_SOURCE_PEER_DMA_COMPLETE = 0,
    OPENENOC_ENDPOINT_IRQ_SOURCE_NON_OETP_DMA_TX_COMPLETE = 1,
    OPENENOC_ENDPOINT_IRQ_SOURCE_NON_OETP_DMA_RX_COMPLETE = 2,
    OPENENOC_ENDPOINT_IRQ_SOURCE_NON_OETP_DIRECT_TX_COMPLETE = 3,
    OPENENOC_ENDPOINT_IRQ_SOURCE_NON_OETP_DIRECT_RX_AVAILABLE = 4,
    OPENENOC_ENDPOINT_IRQ_SOURCE_RMEM_ERROR = 5,
} openenoc_endpoint_irq_source_t;

typedef struct {
    bool global_enable;
    bool peer_dma_complete;
    bool non_oetp_dma_tx_complete;
    bool non_oetp_dma_rx_complete;
    bool non_oetp_direct_tx_complete;
    bool non_oetp_direct_rx_available;
    bool rmem_error;
} openenoc_endpoint_irq_config_t;

typedef struct {
    bool claim_pending;
    bool credit_full;
    bool overflow;
    bool invalid_complete;
    bool irq_asserted;
    uint8_t fifo_level;
    uint8_t reserved_count;
} openenoc_endpoint_irq_status_t;

// Combinable result flags.
typedef enum {
    OPENENOC_ENDPOINT_IRQ_RESULT_OK = 0,
    OPENENOC_ENDPOINT_IRQ_RESULT_UNHANDLED_SOURCE = 1,
    OPENENOC_ENDPOINT_IRQ_RESULT_OVERFLOW = 2,
    OPENENOC_ENDPOINT_IRQ_RESULT_INVALID_COMPLETE = 4,
    OPENENOC_ENDPOINT_IRQ_RESULT_UNHANDLED_CPU_IRQ = 8,
    OPENENOC_ENDPOINT_IRQ_RESULT_NOT_BOUND = 16,
    OPENENOC_ENDPOINT_IRQ_RESULT_UNSUPPORTED = 32,
    OPENENOC_ENDPOINT_IRQ_RESULT_INVALID_ARGUMENT = 64,
} openenoc_endpoint_irq_result_t;

typedef void (*openenoc_endpoint_irq_error_callback_t)(
    openenoc_endpoint_irq_result_t result,
    void *context);

typedef struct {
    openenoc_endpoint_irq_source_t source;
    uint16_t peer_index;
    uint16_t sequence;
} openenoc_endpoint_irq_claim_t;

typedef void (*openenoc_endpoint_irq_callback_t)(
    volatile csr__endpoint_interface_t *endpoint,
    const openenoc_endpoint_irq_claim_t *claim,
    void *context);

typedef struct {
    openenoc_endpoint_irq_callback_t peer_dma_complete;
    openenoc_endpoint_irq_callback_t non_oetp_dma_tx_complete;
    openenoc_endpoint_irq_callback_t non_oetp_dma_rx_complete;
    openenoc_endpoint_irq_callback_t non_oetp_direct_tx_complete;
    openenoc_endpoint_irq_callback_t non_oetp_direct_rx_available;
    openenoc_endpoint_irq_callback_t rmem_error;
    openenoc_endpoint_irq_error_callback_t error;
    void *context;
} openenoc_endpoint_irq_callbacks_t;

openenoc_endpoint_status_t openenoc_endpoint_irq_set_config(
    volatile csr__endpoint_interface_t *endpoint, const openenoc_endpoint_irq_config_t *config);

openenoc_endpoint_status_t openenoc_endpoint_irq_get_config(
    const volatile csr__endpoint_interface_t *endpoint, openenoc_endpoint_irq_config_t *config);

openenoc_endpoint_status_t openenoc_endpoint_irq_set_global_enable(
    volatile csr__endpoint_interface_t *endpoint, bool enable);

openenoc_endpoint_status_t openenoc_endpoint_irq_set_event_enable(
    volatile csr__endpoint_interface_t *endpoint,
    openenoc_endpoint_irq_source_t source, bool enable);

openenoc_endpoint_status_t openenoc_endpoint_irq_get_status(
    const volatile csr__endpoint_interface_t *endpoint, openenoc_endpoint_irq_status_t *status);

openenoc_endpoint_status_t openenoc_endpoint_irq_get_claim(
    const volatile csr__endpoint_interface_t *endpoint, openenoc_endpoint_irq_claim_t *claim);

openenoc_endpoint_status_t openenoc_endpoint_irq_request_complete(
    volatile csr__endpoint_interface_t *endpoint, const openenoc_endpoint_irq_claim_t *claim);

openenoc_endpoint_status_t openenoc_endpoint_irq_request_clear_errors(
    volatile csr__endpoint_interface_t *endpoint);

openenoc_endpoint_status_t openenoc_endpoint_irq_get_pending_commands(
    const volatile csr__endpoint_interface_t *endpoint,
    bool *clear_errors_pending, bool *complete_pending);

openenoc_endpoint_irq_result_t openenoc_endpoint_irq_service(
    volatile csr__endpoint_interface_t *endpoint,
    const openenoc_endpoint_irq_callbacks_t *callbacks,
    uint32_t event_budget, uint32_t *handled_events);

openenoc_endpoint_status_t openenoc_endpoint_irq_bind(
    volatile csr__endpoint_interface_t *endpoint,
    const openenoc_endpoint_irq_callbacks_t *callbacks);

void openenoc_endpoint_irq_mask(void);

void openenoc_endpoint_irq_unmask(void);

openenoc_endpoint_status_t openenoc_endpoint_irq_complete(
    volatile csr__endpoint_interface_t *endpoint);
openenoc_endpoint_status_t openenoc_endpoint_irq_clear_errors(
    volatile csr__endpoint_interface_t *endpoint);
openenoc_endpoint_irq_result_t openenoc_endpoint_irq_handler(uintptr_t cpu_irq_state);

void _openenoc_endpoint_irq_disable_all(void);
void _openenoc_endpoint_irq_enable_endpoint(void);
bool _openenoc_endpoint_irq_is_endpoint(uintptr_t cpu_irq_state);
bool _openenoc_endpoint_irq_has_unhandled_sources(uintptr_t cpu_irq_state);

#ifdef __cplusplus
}
#endif

#endif
