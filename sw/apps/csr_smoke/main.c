/* SPDX-FileCopyrightText: 2026 Enio Kaljic
 * SPDX-License-Identifier: AGPL-3.0-or-later
 */

#include <stdint.h>

#include "memory_map.h"
#include "csr.h"

#define CSR_SMOKE_PATTERN UINT32_C(0xa5a55a5a)
#define CSR_SMOKE_RUNNING UINT32_C(0x00000000)
#define CSR_SMOKE_PASSED  UINT32_C(0x600d600d)
#define CSR_SMOKE_FAILED  UINT32_C(0xbad0bad0)

/* A simulator or debugger can inspect this symbol after main returns. */
volatile uint32_t csr_smoke_status = CSR_SMOKE_RUNNING;

int main(void)
{
    volatile csr_t *const csr =
        (volatile csr_t *)(uintptr_t)OPENENOC_CSR_BASE;

    csr->test_reg.w = CSR_SMOKE_PATTERN;

    if (csr->test_reg.w != CSR_SMOKE_PATTERN) {
        csr_smoke_status = CSR_SMOKE_FAILED;
        return 1;
    }

    csr_smoke_status = CSR_SMOKE_PASSED;
    return 0;
}
