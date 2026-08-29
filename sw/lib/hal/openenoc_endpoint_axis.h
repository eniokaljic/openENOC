/* SPDX-FileCopyrightText: 2026 Enio Kaljic
 * SPDX-License-Identifier: AGPL-3.0-or-later
 */

#ifndef OPENENOC_ENDPOINT_AXIS_H
#define OPENENOC_ENDPOINT_AXIS_H

#include <stdbool.h>
#include <stdint.h>

#include "csr.h"

typedef enum {
    OPENENOC_ENDPOINT_AXIS_STATUS_OK = 0,
    OPENENOC_ENDPOINT_AXIS_STATUS_NOT_READY = 1,
} openenoc_endpoint_axis_status_t;

// Non-blocking: OK means the CSR accepted the transfer request.
openenoc_endpoint_axis_status_t openenoc_endpoint_axis_send(
    volatile csr__endpoint_interface__axis_if_t *axis_if,
    uint32_t data,
    uint8_t keep,
    bool last);

// Output arguments are updated only when OK is returned.
openenoc_endpoint_axis_status_t openenoc_endpoint_axis_receive(
    volatile csr__endpoint_interface__axis_if_t *axis_if,
    uint32_t *data,
    uint8_t *keep,
    bool *last);

#endif
