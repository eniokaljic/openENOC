/* SPDX-FileCopyrightText: 2026 Enio Kaljic
 * SPDX-License-Identifier: AGPL-3.0-or-later
 */

#include "openenoc_endpoint_axis.h"

openenoc_endpoint_axis_status_t openenoc_endpoint_axis_send(
    volatile csr__endpoint_interface__axis_if_t *axis_if,
    uint32_t data,
    uint8_t keep,
    bool last) {
    if (axis_if->source.control.f.tvalid != 0U) {
        return OPENENOC_ENDPOINT_AXIS_STATUS_NOT_READY;
    }

    // Set the payload and sideband fields before presenting a valid transfer.
    axis_if->source.data.f.tdata = data;
    axis_if->source.control.f.tkeep = keep;
    axis_if->source.control.f.tlast = last;
    axis_if->source.control.f.tvalid = 1U;

    return OPENENOC_ENDPOINT_AXIS_STATUS_OK;
}

openenoc_endpoint_axis_status_t openenoc_endpoint_axis_receive(
    volatile csr__endpoint_interface__axis_if_t *axis_if,
    uint32_t *data,
    uint8_t *keep,
    bool *last) {
    uint32_t received_data;
    uint8_t received_keep;
    bool received_last;

    if (axis_if->sink.control.f.tready != 0U ||
        axis_if->sink.status.f.tvalid == 0U) {
        return OPENENOC_ENDPOINT_AXIS_STATUS_NOT_READY;
    }

    // TDATA, TKEEP, and TLAST are stable while TVALID is set and TREADY is clear.
    received_data = axis_if->sink.data.f.tdata;
    received_keep = (uint8_t)axis_if->sink.status.f.tkeep;
    received_last = axis_if->sink.status.f.tlast != 0U;

    *data = received_data;
    if (keep != 0) {
        *keep = received_keep;
    }
    if (last != 0) {
        *last = received_last;
    }

    // Acknowledge only after all fields have been captured.
    axis_if->sink.control.f.tready = 1U;

    return OPENENOC_ENDPOINT_AXIS_STATUS_OK;
}
