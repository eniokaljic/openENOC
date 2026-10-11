#include <stdbool.h>
#include <stdint.h>

#include "openenoc_endpoint_irq.h"

#define MACHINE_EXTERNAL_INTERRUPT UINT32_C(0x8000000b)

volatile uint32_t iss_trap_fault_cause;
volatile uint32_t iss_trap_fault_pc;
volatile uint32_t iss_irq_entries;
volatile uint32_t iss_irq_returns;

void _openenoc_endpoint_irq_disable_all(void) {
    __asm__ volatile("csrw mie, zero" ::: "memory");
}

void _openenoc_endpoint_irq_enable_endpoint(void) {
    const uintptr_t external = UINT32_C(1) << 11;
    const uintptr_t global = UINT32_C(1) << 3;
    __asm__ volatile("csrs mie, %0\n\tcsrs mstatus, %1" ::
                     "r"(external), "r"(global) : "memory");
}

bool _openenoc_endpoint_irq_is_endpoint(uintptr_t cpu_irq_state) {
    return cpu_irq_state == MACHINE_EXTERNAL_INTERRUPT;
}

bool _openenoc_endpoint_irq_has_unhandled_sources(uintptr_t cpu_irq_state) {
    return cpu_irq_state != MACHINE_EXTERNAL_INTERRUPT;
}