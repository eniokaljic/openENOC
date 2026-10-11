/* SPDX-FileCopyrightText: 2026 Enio Kaljic
 * SPDX-License-Identifier: AGPL-3.0-or-later
 */

#include <assert.h>
#include <stddef.h>
#include <stdint.h>

#include "irq.h"
#include "openenoc_endpoint_irq.h"

// Host replacement for the PicoRV32 maskirq instruction. The real platform
// C utilities are linked into this test; no endpoint CSR hardware is needed.
static uint32_t cpu_mask = UINT32_MAX;
static unsigned int mask_calls;

uint32_t irq_set_mask(uint32_t mask) {
    uint32_t previous = cpu_mask;
    cpu_mask = mask;
    ++mask_calls;
    return previous;
}

struct error_context {
    unsigned int calls;
    openenoc_endpoint_irq_result_t result;
};

static void record_error(openenoc_endpoint_irq_result_t result, void *context) {
    struct error_context *error = context;
    ++error->calls;
    error->result = result;
}

int main(void) {
    // Main reaches the CPU mask policy exclusively through HAL.
    openenoc_endpoint_irq_unmask();
    assert(cpu_mask == ~(UINT32_C(1) << 3));
    openenoc_endpoint_irq_mask();
    assert(cpu_mask == UINT32_MAX);
    assert(mask_calls == 2U);

    // An accidental entry before binding masks the CPU without dereferencing
    // a nonexistent endpoint or requiring an application dispatch handler.
    openenoc_endpoint_irq_bind(NULL, NULL);
    unsigned int before = mask_calls;
    assert(openenoc_endpoint_irq_handler(8U) == OPENENOC_ENDPOINT_IRQ_RESULT_NOT_BOUND);
    assert(mask_calls == before + 1U);

    struct error_context error = {0};
    const openenoc_endpoint_irq_callbacks_t callbacks = {
        .error = record_error,
        .context = &error,
    };

    // A non-endpoint CPU source must not touch endpoint CSR memory. Use an
    // inaccessible address so an accidental CSR read makes the test fail.
    openenoc_endpoint_irq_bind(
        (volatile csr__endpoint_interface__irq_t *)(uintptr_t)1U, &callbacks);
    before = mask_calls;
    assert(openenoc_endpoint_irq_handler(1U) == OPENENOC_ENDPOINT_IRQ_RESULT_UNHANDLED_CPU_IRQ);
    assert(mask_calls == before + 1U);
    assert(error.calls == 1U);
    assert(error.result == OPENENOC_ENDPOINT_IRQ_RESULT_UNHANDLED_CPU_IRQ);

    // A combined CPU cause still services the endpoint and reports all sticky
    // errors once through the registered application context.
    volatile csr__endpoint_interface__irq_t irq = {0};
    irq.status.f.overflow = 1U;
    irq.status.f.invalid_complete = 1U;
    openenoc_endpoint_irq_bind(&irq, &callbacks);
    openenoc_endpoint_irq_result_t expected = (openenoc_endpoint_irq_result_t)(
        OPENENOC_ENDPOINT_IRQ_RESULT_UNHANDLED_CPU_IRQ |
        OPENENOC_ENDPOINT_IRQ_RESULT_OVERFLOW |
        OPENENOC_ENDPOINT_IRQ_RESULT_INVALID_COMPLETE);
    assert(openenoc_endpoint_irq_handler(9U) == expected);
    assert(error.calls == 2U);
    assert(error.result == expected);
    assert(irq.status.f.overflow == 1U);
    assert(irq.status.f.invalid_complete == 1U);

    // An explicit service call reports errors to its caller without invoking
    // the CPU entry's error notification or changing CPU masking.
    before = mask_calls;
    assert(openenoc_endpoint_irq_service(&irq, &callbacks) ==
        (OPENENOC_ENDPOINT_IRQ_RESULT_OVERFLOW |
         OPENENOC_ENDPOINT_IRQ_RESULT_INVALID_COMPLETE));
    assert(mask_calls == before);
    assert(error.calls == 2U);
    return 0;
}
