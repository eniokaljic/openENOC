/* SPDX-FileCopyrightText: 2026 Enio Kaljic
 * SPDX-License-Identifier: AGPL-3.0-or-later
 */

#ifndef OPENENOC_FREESTANDING_ASSERT_H
#define OPENENOC_FREESTANDING_ASSERT_H

/* C11 exposes static assertions through <assert.h>; C++ has a keyword. */
#ifndef __cplusplus
#define static_assert _Static_assert
#endif

#ifdef NDEBUG
#define assert(expression) ((void)0)
#else
/* Trap locally because this bare-metal environment has no process to abort. */
#define assert(expression) ((expression) ? (void)0 : __builtin_trap())
#endif

#endif /* OPENENOC_FREESTANDING_ASSERT_H */
