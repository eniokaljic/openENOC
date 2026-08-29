/* SPDX-FileCopyrightText: 2026 Enio Kaljic
 * SPDX-License-Identifier: AGPL-3.0-or-later
 */

#include <stdint.h>

#include "csr.h"
#include "memory_map.h"
#include "openenoc_endpoint_axis.h"

#define CSR_SMOKE_PATTERN UINT32_C(0xa5a55a5a)
#define CSR_SMOKE_RUNNING UINT32_C(0x00000000)
#define CSR_SMOKE_PASSED  UINT32_C(0x600d600d)
#define CSR_SMOKE_FAILED  UINT32_C(0xbad0bad0)
#define SWITCH_FORWARDING_PATTERN UINT32_C(0xa)
#define AXIS_LOOPBACK_WORD_COUNT 17U
#define AXIS_LOOPBACK_FULL_KEEP UINT8_C(0xf)
#define AXIS_LOOPBACK_LAST_KEEP UINT8_C(0x3)

static const uint32_t axis_loopback_words[AXIS_LOOPBACK_WORD_COUNT] = {
    UINT32_C(0x00000000), UINT32_C(0x01234567),
    UINT32_C(0x89abcdef), UINT32_C(0xffffffff),
    UINT32_C(0xa5a55a5a), UINT32_C(0x5a5aa5a5),
    UINT32_C(0x00000001), UINT32_C(0x80000000),
    UINT32_C(0x11111111), UINT32_C(0x22222222),
    UINT32_C(0x33333333), UINT32_C(0x44444444),
    UINT32_C(0xdeadbeef), UINT32_C(0xc001d00d),
    UINT32_C(0x13579bdf), UINT32_C(0x2468ace0),
    UINT32_C(0x0000beef),
};

/* A simulator or debugger can inspect this symbol after main returns. */
volatile uint32_t csr_smoke_status = CSR_SMOKE_RUNNING;

int main(void) {
    volatile csr_t *const csr =
        (volatile csr_t *)(uintptr_t)CSR_BASE_ADDR;

    // Verify basic software-writable CSR access.
    csr->test_reg.f.test_field = CSR_SMOKE_PATTERN;

    if (csr->test_reg.f.test_field != CSR_SMOKE_PATTERN) {
        csr_smoke_status = CSR_SMOKE_FAILED;
        return 1;
    }

    // Configure the switch and verify software and hardware-driven fields.
    csr->switch_interface.forwarding_control.f.operation_mode = 1U;
    csr->switch_interface.default_forwarding.f.bitmap =
        SWITCH_FORWARDING_PATTERN;
    csr->switch_interface.forwarding_control.f.pause_request = 1U;

    if (csr->switch_interface.forwarding_control.f.operation_mode != 1U ||
        csr->switch_interface.forwarding_control.f.pause_request != 1U ||
        csr->switch_interface.forwarding_control.f.pause_done != 1U ||
        csr->switch_interface.default_forwarding.f.bitmap !=
            SWITCH_FORWARDING_PATTERN) {
        csr_smoke_status = CSR_SMOKE_FAILED;
        return 1;
    }

    // Send a 66-byte frame, with only two valid bytes in the final word.
    for (uint32_t i = 0; i < AXIS_LOOPBACK_WORD_COUNT; ++i) {
        bool last = i == AXIS_LOOPBACK_WORD_COUNT - 1U;

        while (openenoc_endpoint_axis_send(
            &csr->endpoint_interface.axis_if,
            axis_loopback_words[i],
            last ? AXIS_LOOPBACK_LAST_KEEP : AXIS_LOOPBACK_FULL_KEEP,
            last) == OPENENOC_ENDPOINT_AXIS_STATUS_NOT_READY) {
        }
    }

    // Receive the loopback frame and check its payload and AXIS sidebands.
    for (uint32_t i = 0; i < AXIS_LOOPBACK_WORD_COUNT; ++i) {
        bool expected_last = i == AXIS_LOOPBACK_WORD_COUNT - 1U;
        uint8_t expected_keep =
            expected_last ? AXIS_LOOPBACK_LAST_KEEP : AXIS_LOOPBACK_FULL_KEEP;
        uint32_t received;
        uint8_t keep;
        bool last;

        while (openenoc_endpoint_axis_receive(
            &csr->endpoint_interface.axis_if,
            &received,
            &keep,
            &last) == OPENENOC_ENDPOINT_AXIS_STATUS_NOT_READY) {
        }

        if (received != axis_loopback_words[i] || keep != expected_keep ||
            last != expected_last) {
            csr_smoke_status = CSR_SMOKE_FAILED;
            return 1;
        }
    }

    csr_smoke_status = CSR_SMOKE_PASSED;
    return 0;
}
