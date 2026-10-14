/* SPDX-FileCopyrightText: 2026 Enio Kaljic
 * SPDX-License-Identifier: AGPL-3.0-or-later
 */

#ifndef OPENENOC_SWITCH_COMMON_H
#define OPENENOC_SWITCH_COMMON_H

#include <stdbool.h>
#include <stdint.h>

#include "csr.h"

#ifdef __cplusplus
extern "C" {
#endif

typedef enum {
    OPENENOC_SWITCH_STATUS_OK = 0,
    OPENENOC_SWITCH_STATUS_NOT_READY = 2,
    OPENENOC_SWITCH_STATUS_INVALID_ARGUMENT = 3,
    OPENENOC_SWITCH_STATUS_OUT_OF_RANGE = 4,
    OPENENOC_SWITCH_STATUS_UNSUPPORTED = 5,
    OPENENOC_SWITCH_STATUS_HARDWARE_MISMATCH = 6,
    OPENENOC_SWITCH_STATUS_NOT_ALLOWED = 7
} openenoc_switch_status_t;

// MAC octets use network address order.
typedef struct {
    uint8_t octet[6];
} openenoc_switch_mac_t;

typedef struct {
    uint32_t interface_count;
    uint32_t table_depth;
} openenoc_switch_info_t;

openenoc_switch_status_t openenoc_switch_init(
    volatile csr__switch_interface_t *switch_interface);

openenoc_switch_status_t openenoc_switch_get_info(
    const volatile csr__switch_interface_t *switch_interface, openenoc_switch_info_t *info);

#ifdef __cplusplus
}
#endif

#ifdef OPENENOC_SWITCH_IMPLEMENTATION
#include <stddef.h>

static inline bool openenoc_switch_pointer_valid(
    const volatile csr__switch_interface_t *switch_interface) {
    return switch_interface != NULL && ((uintptr_t)switch_interface & 3U) == 0U;
}

static inline bool openenoc_switch_bitmap_valid(uint32_t bitmap) {
    return (bitmap & ~CSR__SWITCH_INTERFACE__DEFAULT_FORWARDING__BITMAP_bm) == 0U;
}

static inline bool openenoc_switch_paused(
    const volatile csr__switch_interface_t *switch_interface) {
    return switch_interface->forwarding_control.f.pause_request != 0U &&
        switch_interface->forwarding_control.f.pause_done != 0U;
}

static inline openenoc_switch_status_t openenoc_switch_write_ready(
    const volatile csr__switch_interface_t *switch_interface) {
    if (switch_interface->forwarding_control.f.operation_mode == 0U) {
        return OPENENOC_SWITCH_STATUS_NOT_ALLOWED;
    }
    return openenoc_switch_paused(switch_interface) ?
        OPENENOC_SWITCH_STATUS_OK : OPENENOC_SWITCH_STATUS_NOT_READY;
}

typedef struct {
    uint32_t lower;
    uint32_t upper;
} openenoc_switch_mac_words_t;

static inline openenoc_switch_mac_words_t openenoc_switch_mac_pack(
    const openenoc_switch_mac_t *address) {
    openenoc_switch_mac_words_t words;

    words.upper = ((uint32_t)address->octet[0] << 8) | address->octet[1];
    words.lower = ((uint32_t)address->octet[2] << 24) |
        ((uint32_t)address->octet[3] << 16) |
        ((uint32_t)address->octet[4] << 8) | address->octet[5];
    return words;
}

static inline void openenoc_switch_mac_unpack(
    uint32_t lower, uint32_t upper, openenoc_switch_mac_t *address) {
    address->octet[0] = (uint8_t)(upper >> 8);
    address->octet[1] = (uint8_t)upper;
    address->octet[2] = (uint8_t)(lower >> 24);
    address->octet[3] = (uint8_t)(lower >> 16);
    address->octet[4] = (uint8_t)(lower >> 8);
    address->octet[5] = (uint8_t)lower;
}

#endif

#endif
