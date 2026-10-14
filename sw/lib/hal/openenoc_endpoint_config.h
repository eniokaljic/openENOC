/* SPDX-FileCopyrightText: 2026 Enio Kaljic
 * SPDX-License-Identifier: AGPL-3.0-or-later
 */

#ifndef OPENENOC_ENDPOINT_CONFIG_H
#define OPENENOC_ENDPOINT_CONFIG_H

#include "openenoc_endpoint_common.h"

#ifdef __cplusplus
extern "C" {
#endif

typedef enum {
    OPENENOC_ENDPOINT_RECEIVE_DROP = 0,
    OPENENOC_ENDPOINT_RECEIVE_FILTERED = 1,
    OPENENOC_ENDPOINT_RECEIVE_MULTICAST = 2,
    OPENENOC_ENDPOINT_RECEIVE_PROMISCUOUS = 3
} openenoc_endpoint_receive_mode_t;

typedef struct {
    openenoc_endpoint_mac_t mac_address;
    openenoc_endpoint_mac_t multicast_address;
    openenoc_endpoint_receive_mode_t receive_mode;
    uint32_t rmem_timeout_cycles;
    uint32_t dma_timeout_cycles;
    uint32_t dma_max_fragment_size_bytes;
} openenoc_endpoint_config_t;

openenoc_endpoint_status_t openenoc_endpoint_get_config(
    const volatile csr__endpoint_interface_t *endpoint, openenoc_endpoint_config_t *config);

openenoc_endpoint_status_t openenoc_endpoint_set_config(
    volatile csr__endpoint_interface_t *endpoint, const openenoc_endpoint_config_t *config);

openenoc_endpoint_status_t openenoc_endpoint_set_mac_address(
    volatile csr__endpoint_interface_t *endpoint, const openenoc_endpoint_mac_t *address);

openenoc_endpoint_status_t openenoc_endpoint_set_multicast_address(
    volatile csr__endpoint_interface_t *endpoint, const openenoc_endpoint_mac_t *address);

openenoc_endpoint_status_t openenoc_endpoint_set_receive_mode(
    volatile csr__endpoint_interface_t *endpoint, openenoc_endpoint_receive_mode_t mode);

openenoc_endpoint_status_t openenoc_endpoint_set_rmem_timeout(
    volatile csr__endpoint_interface_t *endpoint, uint32_t cycles);

openenoc_endpoint_status_t openenoc_endpoint_set_dma_timeout(
    volatile csr__endpoint_interface_t *endpoint, uint32_t cycles);

openenoc_endpoint_status_t openenoc_endpoint_set_dma_max_fragment_size(
    volatile csr__endpoint_interface_t *endpoint,
    uint32_t requested_bytes, uint32_t *effective_bytes);

#ifdef __cplusplus
}
#endif

#endif
