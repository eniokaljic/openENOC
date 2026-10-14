/* SPDX-FileCopyrightText: 2026 Enio Kaljic
 * SPDX-License-Identifier: AGPL-3.0-or-later
 */

#ifndef OPENENOC_FREESTANDING_ASSERT_H
#define OPENENOC_FREESTANDING_ASSERT_H

#include <stdint.h>

/* C11 exposes static assertions through <assert.h>; C++ has a keyword. */
#ifndef __cplusplus
#define static_assert _Static_assert
#endif

typedef struct {
    uint32_t status;
    uint32_t completed_checks;
    uint32_t failure_line;
    const char *failure_file;
} openenoc_assert_status_t;

#define OPENENOC_ASSERT_STATUS_PASSED UINT32_C(0x600d600d)
#define OPENENOC_ASSERT_STATUS_FAILED UINT32_C(0xbad0bad0)

#ifdef __cplusplus
extern "C" {
#endif

#ifdef OPENENOC_ASSERT_IMPLEMENTATION
volatile openenoc_assert_status_t _openenoc_assert_status
    __attribute__((section(".data._openenoc_assert_status"))) = {0};
#else
extern volatile openenoc_assert_status_t _openenoc_assert_status;
#endif

void openenoc_assert_fail(const char *file, uint32_t line) __attribute__((noreturn));

#ifdef __cplusplus
}
#endif

#ifdef NDEBUG
#define assert(expression) ((void)0)
#else
#define assert(expression) \
    ((expression) ? (void)0 : openenoc_assert_fail(__FILE__, (uint32_t)__LINE__))
#endif

#endif /* OPENENOC_FREESTANDING_ASSERT_H */
