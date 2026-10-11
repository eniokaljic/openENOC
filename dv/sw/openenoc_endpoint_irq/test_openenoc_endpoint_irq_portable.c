/* SPDX-FileCopyrightText: 2026 Enio Kaljic
 * SPDX-License-Identifier: AGPL-3.0-or-later
 */

#include <assert.h>
#include <stddef.h>

#include "openenoc_endpoint_irq.h"

// Test-only encoding, deliberately different from the PicoRV32 IRQ bitmask.
#define ENDPOINT_STATE UINT32_C(0x8000000b)
#define OTHER_STATE UINT32_C(0x80000007)

static unsigned int mask_calls;
static unsigned int unmask_calls;
static unsigned int error_calls;
static openenoc_endpoint_irq_result_t last_error;

void _openenoc_endpoint_irq_disable_all(void) {
    ++mask_calls;
}

void _openenoc_endpoint_irq_enable_endpoint(void) {
    ++unmask_calls;
}

bool _openenoc_endpoint_irq_is_endpoint(uintptr_t cpu_irq_state) {
    return cpu_irq_state == ENDPOINT_STATE;
}

bool _openenoc_endpoint_irq_has_unhandled_sources(uintptr_t cpu_irq_state) {
    return cpu_irq_state != ENDPOINT_STATE;
}

static void record_error(openenoc_endpoint_irq_result_t result, void *context) {
    assert(context == &last_error);
    last_error = result;
    ++error_calls;
}

int main(void) {
    openenoc_endpoint_irq_mask();
    openenoc_endpoint_irq_unmask();
    assert(mask_calls == 1U);
    assert(unmask_calls == 1U);

    volatile csr__endpoint_interface__irq_t irq = {0};
    const openenoc_endpoint_irq_config_t config = {
        .global_enable = true,
        .peer_dma_complete = true,
        .rmem_error = true,
    };
    openenoc_endpoint_irq_configure(&irq, &config);
    openenoc_endpoint_irq_config_t actual = {0};
    openenoc_endpoint_irq_get_config(&irq, &actual);
    assert(actual.global_enable);
    assert(actual.peer_dma_complete);
    assert(actual.rmem_error);
    assert(!actual.non_oetp_dma_tx_complete);
    assert(!actual.non_oetp_dma_rx_complete);
    assert(!actual.non_oetp_direct_tx_complete);
    assert(!actual.non_oetp_direct_rx_available);
    assert(openenoc_endpoint_irq_set_event_enable(
        &irq, OPENENOC_ENDPOINT_IRQ_SOURCE_RMEM_ERROR, false));
    assert(irq.event_enable.f.rmem_error == 0U);
    assert(irq.event_enable.f.peer_dma_complete == 1U);
    assert(openenoc_endpoint_irq_set_event_enable(
        &irq, OPENENOC_ENDPOINT_IRQ_SOURCE_RMEM_ERROR, true));
    assert(irq.event_enable.f.rmem_error == 1U);

    irq.status.f.overflow = 1U;
    const openenoc_endpoint_irq_callbacks_t callbacks = {
        .error = record_error,
        .context = &last_error,
    };
    openenoc_endpoint_irq_bind(&irq, &callbacks);
    assert(openenoc_endpoint_irq_handler(ENDPOINT_STATE) ==
           OPENENOC_ENDPOINT_IRQ_RESULT_OVERFLOW);
    assert(last_error == OPENENOC_ENDPOINT_IRQ_RESULT_OVERFLOW);
    assert(error_calls == 1U);
    assert(mask_calls == 1U);

    // Reject unrelated IRQs without accessing the endpoint.
    openenoc_endpoint_irq_bind(
        (volatile csr__endpoint_interface__irq_t *)(uintptr_t)1U, &callbacks);
    assert(openenoc_endpoint_irq_handler(OTHER_STATE) ==
           OPENENOC_ENDPOINT_IRQ_RESULT_UNHANDLED_CPU_IRQ);
    assert(last_error == OPENENOC_ENDPOINT_IRQ_RESULT_UNHANDLED_CPU_IRQ);
    assert(error_calls == 2U);
    assert(mask_calls == 2U);
    return 0;
}
