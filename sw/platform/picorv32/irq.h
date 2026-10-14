/* SPDX-FileCopyrightText: 2026 Enio Kaljic
 * SPDX-License-Identifier: AGPL-3.0-or-later
 */

#ifndef OPENENOC_IRQ_H
#define OPENENOC_IRQ_H

#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif

/* One masks an IRQ. Return the previous mask; reset starts with all ones. */
uint32_t irq_set_mask(uint32_t mask);

#ifdef __cplusplus
}
#endif

#endif
