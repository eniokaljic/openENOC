/* SPDX-FileCopyrightText: 2026 Enio Kaljic
 * SPDX-License-Identifier: AGPL-3.0-or-later
 */

#ifndef OPENENOC_ENDPOINT_PEER_H
#define OPENENOC_ENDPOINT_PEER_H

#include "openenoc_endpoint_common.h"

#ifdef __cplusplus
extern "C" {
#endif

typedef enum {
    OPENENOC_ENDPOINT_PEER_DISABLED = 0,
    OPENENOC_ENDPOINT_PEER_TRANSPARENT_RMEM = 1,
    OPENENOC_ENDPOINT_PEER_MIRROR_TO_LOCAL = 2,
    OPENENOC_ENDPOINT_PEER_MIRROR_TO_REMOTE = 3
} openenoc_endpoint_peer_mode_t;

typedef struct {
    openenoc_endpoint_mac_t mac_address;
    uint32_t rmem_offset_bytes;
    uint32_t local_address;
    uint32_t remote_address;
    uint32_t size_bytes;
    openenoc_endpoint_peer_mode_t mode;
    bool irq_enable;
} openenoc_endpoint_peer_config_t;

typedef struct {
    bool request_pending;
    bool clear_error_pending;
    bool idle;
    bool done;
    bool error;
    openenoc_endpoint_error_t error_code;
} openenoc_endpoint_peer_status_t;

openenoc_endpoint_status_t openenoc_endpoint_peer_get_config(
    const volatile csr__endpoint_interface_t *endpoint, uint16_t peer_index,
    openenoc_endpoint_peer_config_t *config);

openenoc_endpoint_status_t openenoc_endpoint_peer_set_config(
    volatile csr__endpoint_interface_t *endpoint, uint16_t peer_index,
    const openenoc_endpoint_peer_config_t *config);

openenoc_endpoint_status_t openenoc_endpoint_peer_dma_request(
    volatile csr__endpoint_interface_t *endpoint, uint16_t peer_index);

openenoc_endpoint_status_t openenoc_endpoint_peer_get_status(
    const volatile csr__endpoint_interface_t *endpoint, uint16_t peer_index,
    openenoc_endpoint_peer_status_t *status);

openenoc_endpoint_status_t openenoc_endpoint_peer_request_clear_error(
    volatile csr__endpoint_interface_t *endpoint, uint16_t peer_index);

#ifdef __cplusplus
}
#endif

#endif
