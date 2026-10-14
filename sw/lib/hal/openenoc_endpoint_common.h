/* SPDX-FileCopyrightText: 2026 Enio Kaljic
 * SPDX-License-Identifier: AGPL-3.0-or-later
 */

#ifndef OPENENOC_ENDPOINT_COMMON_H
#define OPENENOC_ENDPOINT_COMMON_H

#include <stdbool.h>
#include <stdint.h>

#include "csr.h"

#ifdef __cplusplus
extern "C" {
#endif

typedef enum {
    OPENENOC_ENDPOINT_STATUS_OK = 0,
    OPENENOC_ENDPOINT_STATUS_NOT_READY = 2,
    OPENENOC_ENDPOINT_STATUS_INVALID_ARGUMENT = 3,
    OPENENOC_ENDPOINT_STATUS_OUT_OF_RANGE = 4,
    OPENENOC_ENDPOINT_STATUS_UNSUPPORTED = 5,
    OPENENOC_ENDPOINT_STATUS_HARDWARE_MISMATCH = 6
} openenoc_endpoint_status_t;

typedef enum {
    OPENENOC_ENDPOINT_ERROR_NONE = 0,
    OPENENOC_ENDPOINT_ERROR_LOCAL_INVALID = 1,
    OPENENOC_ENDPOINT_ERROR_LOCAL_STREAM = 2,
    OPENENOC_ENDPOINT_ERROR_LOCAL_SIZE = 3,
    OPENENOC_ENDPOINT_ERROR_LOCAL_READ_SLVERR = 4,
    OPENENOC_ENDPOINT_ERROR_LOCAL_READ_DECERR = 5,
    OPENENOC_ENDPOINT_ERROR_LOCAL_WRITE_SLVERR = 6,
    OPENENOC_ENDPOINT_ERROR_LOCAL_WRITE_DECERR = 7,
    OPENENOC_ENDPOINT_ERROR_TIMEOUT = 8,
    OPENENOC_ENDPOINT_ERROR_REMOTE_INVALID = 9,
    OPENENOC_ENDPOINT_ERROR_REMOTE_STREAM = 10,
    OPENENOC_ENDPOINT_ERROR_REMOTE_SIZE = 11,
    OPENENOC_ENDPOINT_ERROR_REMOTE_READ_SLVERR = 12,
    OPENENOC_ENDPOINT_ERROR_REMOTE_READ_DECERR = 13,
    OPENENOC_ENDPOINT_ERROR_REMOTE_WRITE_SLVERR = 14,
    OPENENOC_ENDPOINT_ERROR_REMOTE_WRITE_DECERR = 15
} openenoc_endpoint_error_t;

typedef struct {
    uint8_t octet[6];
} openenoc_endpoint_mac_t;

typedef struct {
    uint32_t rmem_word_count;
    uint32_t peer_count;
    uint32_t max_raw_frame_size_bytes;
    uint32_t max_peer_fragment_size_bytes;
    bool peer_dma_supported;
    bool non_oetp_dma_supported;
    bool direct_axis_supported;
    bool rmem_supported;
    bool irq_supported;
} openenoc_endpoint_info_t;

openenoc_endpoint_status_t openenoc_endpoint_init(
    volatile csr__endpoint_interface_t *endpoint);

openenoc_endpoint_status_t openenoc_endpoint_get_info(
    const volatile csr__endpoint_interface_t *endpoint, openenoc_endpoint_info_t *info);

#ifdef __cplusplus
}
#endif

/* Shared implementation helpers use the generated interface structure. */
#ifdef OPENENOC_ENDPOINT_IMPLEMENTATION
#include <stddef.h>

static inline uint32_t openenoc_endpoint_max_peer_fragment_size(void) {
    return CSR__HAS_PEER_DMA && CSR__MAX_RAW_FRAME_SIZE > 32U ?
        (CSR__MAX_RAW_FRAME_SIZE - 32U) & ~3U : 0U;
}

typedef struct {
    uint32_t lower;
    uint32_t upper;
} openenoc_endpoint_mac_words_t;

static inline openenoc_endpoint_mac_words_t openenoc_endpoint_mac_pack(
    const openenoc_endpoint_mac_t *address) {
    openenoc_endpoint_mac_words_t words;

    words.upper = ((uint32_t)address->octet[0] << 8) | address->octet[1];
    words.lower = ((uint32_t)address->octet[2] << 24) |
        ((uint32_t)address->octet[3] << 16) |
        ((uint32_t)address->octet[4] << 8) | address->octet[5];
    return words;
}

static inline void openenoc_endpoint_mac_unpack(
    uint32_t lower, uint32_t upper, openenoc_endpoint_mac_t *address) {
    address->octet[0] = (uint8_t)(upper >> 8);
    address->octet[1] = (uint8_t)upper;
    address->octet[2] = (uint8_t)(lower >> 24);
    address->octet[3] = (uint8_t)(lower >> 16);
    address->octet[4] = (uint8_t)(lower >> 8);
    address->octet[5] = (uint8_t)lower;
}

static inline bool openenoc_endpoint_address_range_valid(uint32_t address, uint32_t size) {
    return size != 0U && size - 1U <= UINT32_MAX - address;
}

#endif

#endif
