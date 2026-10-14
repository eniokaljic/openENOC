/* SPDX-FileCopyrightText: 2026 Enio Kaljic
 * SPDX-License-Identifier: AGPL-3.0-or-later
 */

#ifndef OPENENOC_ENDPOINT_AXIS_H
#define OPENENOC_ENDPOINT_AXIS_H

#include "openenoc_endpoint_common.h"

#ifdef __cplusplus
extern "C" {
#endif

openenoc_endpoint_status_t openenoc_endpoint_axis_send(
    volatile csr__endpoint_interface_t *endpoint,
    uint32_t data,
    uint8_t keep,
    bool last);

openenoc_endpoint_status_t openenoc_endpoint_axis_receive(
    volatile csr__endpoint_interface_t *endpoint,
    uint32_t *data,
    uint8_t *keep,
    bool *last);

openenoc_endpoint_status_t openenoc_endpoint_axis_send_stream(
    volatile csr__endpoint_interface_t *endpoint,
    const void *buffer,
    uint32_t byte_count);

openenoc_endpoint_status_t openenoc_endpoint_axis_receive_stream(
    volatile csr__endpoint_interface_t *endpoint,
    void *buffer,
    uint32_t buffer_capacity_bytes,
    uint32_t *received_bytes);

#ifdef __cplusplus
}
#endif

#endif
