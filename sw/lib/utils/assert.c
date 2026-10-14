/* SPDX-FileCopyrightText: 2026 Enio Kaljic
 * SPDX-License-Identifier: AGPL-3.0-or-later
 */

#define OPENENOC_ASSERT_IMPLEMENTATION
#include "assert.h"

void openenoc_assert_fail(const char *file, uint32_t line) {
    _openenoc_assert_status.failure_file = file;
    _openenoc_assert_status.failure_line = line;
    _openenoc_assert_status.status = OPENENOC_ASSERT_STATUS_FAILED;
    __builtin_trap();
}
