/* SPDX-FileCopyrightText: 2026 Enio Kaljic
 * SPDX-License-Identifier: AGPL-3.0-or-later
 */

#include "irq.h"
#include "openenoc_endpoint_irq.h"

// The full endpoint connects its level-sensitive IRQ to PicoRV32 input 3.
#define ENDPOINT_CPU_IRQ_MASK (UINT32_C(1) << 3)

void _openenoc_endpoint_irq_disable_all(void) {
    irq_set_mask(UINT32_MAX);
}

void _openenoc_endpoint_irq_enable_endpoint(void) {
    irq_set_mask(~ENDPOINT_CPU_IRQ_MASK);
}

bool _openenoc_endpoint_irq_is_endpoint(uintptr_t cpu_irq_state) {
    return (cpu_irq_state & ENDPOINT_CPU_IRQ_MASK) != 0U;
}

bool _openenoc_endpoint_irq_has_unhandled_sources(uintptr_t cpu_irq_state) {
    return (cpu_irq_state & ~(uintptr_t)ENDPOINT_CPU_IRQ_MASK) != 0U;
}
