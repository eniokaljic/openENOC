/* SPDX-FileCopyrightText: 2026 Enio Kaljic
 * SPDX-License-Identifier: AGPL-3.0-or-later
 */

#define OPENENOC_ENDPOINT_IMPLEMENTATION
#include "openenoc_endpoint.h"

openenoc_endpoint_status_t openenoc_endpoint_rmem_get_region(
    const volatile csr__endpoint_interface_t *endpoint, openenoc_endpoint_rmem_region_t *region) {
    if (CSR__HAS_RMEM == 0U) {
        return OPENENOC_ENDPOINT_STATUS_UNSUPPORTED;
    }
    if (endpoint == NULL || ((uintptr_t)endpoint & 3U) != 0U || region == NULL) {
        return OPENENOC_ENDPOINT_STATUS_INVALID_ARGUMENT;
    }
    _Static_assert(offsetof(csr__endpoint_interface_t, rmem) % _Alignof(uint32_t) == 0,
        "The generated RMEM window must be word aligned");
    _Static_assert(sizeof(endpoint->rmem.word[0]) == sizeof(uint32_t),
        "The generated RMEM words must be contiguous 32-bit words");
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Waddress-of-packed-member"
    region->words = (volatile uint32_t *)(volatile void *)&endpoint->rmem.word[0];
#pragma GCC diagnostic pop
    region->word_count = CSR__RMEM_TOTAL_DEPTH;
    return OPENENOC_ENDPOINT_STATUS_OK;
}
