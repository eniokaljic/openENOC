/* SPDX-FileCopyrightText: 2026 Enio Kaljic
 * SPDX-License-Identifier: AGPL-3.0-or-later
 */

#include <stdint.h>

#include "csr.h"
#include "memory_map.h"

#define CSR_SMOKE_PATTERN UINT32_C(0xa5a55a5a)
#define CSR_SMOKE_RUNNING UINT32_C(0x00000000)
#define CSR_SMOKE_PASSED  UINT32_C(0x600d600d)
#define CSR_SMOKE_FAILED  UINT32_C(0xbad0bad0)
#define SWITCH_CONTROL_PATTERN                                                \
    (CSR__SWITCH_INTERFACE__FORWARDING_CONTROL__OPERATION_MODE_bm |          \
     CSR__SWITCH_INTERFACE__FORWARDING_CONTROL__PAUSE_REQUEST_bm)
#define SWITCH_CONTROL_READBACK                                               \
    (SWITCH_CONTROL_PATTERN |                                                 \
     CSR__SWITCH_INTERFACE__FORWARDING_CONTROL__PAUSE_DONE_bm)
#define SWITCH_FORWARDING_PATTERN UINT32_C(0xa)

/* A simulator or debugger can inspect this symbol after main returns. */
volatile uint32_t csr_smoke_status = CSR_SMOKE_RUNNING;

int main(void) {
    volatile csr_t *const csr =
        (volatile csr_t *)(uintptr_t)CSR_BASE_ADDR;

    csr->test_reg.w = CSR_SMOKE_PATTERN;

    if (csr->test_reg.w != CSR_SMOKE_PATTERN) {
        csr_smoke_status = CSR_SMOKE_FAILED;
        return 1;
    }

    csr->switch_interface.forwarding_control.w = SWITCH_CONTROL_PATTERN;
    csr->switch_interface.default_forwarding.w = SWITCH_FORWARDING_PATTERN;

    if (csr->switch_interface.forwarding_control.w != SWITCH_CONTROL_READBACK ||
        csr->switch_interface.default_forwarding.w != SWITCH_FORWARDING_PATTERN) {
        csr_smoke_status = CSR_SMOKE_FAILED;
        return 1;
    }

    csr_smoke_status = CSR_SMOKE_PASSED;
    return 0;
}
