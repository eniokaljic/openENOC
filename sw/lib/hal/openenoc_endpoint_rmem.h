/* SPDX-FileCopyrightText: 2026 Enio Kaljic
 * SPDX-License-Identifier: AGPL-3.0-or-later
 */

#ifndef OPENENOC_ENDPOINT_RMEM_H
#define OPENENOC_ENDPOINT_RMEM_H

#include "openenoc_endpoint_common.h"

#ifdef __cplusplus
extern "C" {
#endif

typedef struct {
    volatile uint32_t *words;
    uint32_t word_count;
} openenoc_endpoint_rmem_region_t;

openenoc_endpoint_status_t openenoc_endpoint_rmem_get_region(
    const volatile csr__endpoint_interface_t *endpoint, openenoc_endpoint_rmem_region_t *region);

#ifdef __cplusplus
}
#endif

#endif
