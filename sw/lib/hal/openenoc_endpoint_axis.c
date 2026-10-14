/* SPDX-FileCopyrightText: 2026 Enio Kaljic
 * SPDX-License-Identifier: AGPL-3.0-or-later
 */

#define OPENENOC_ENDPOINT_IMPLEMENTATION
#include "openenoc_endpoint.h"

openenoc_endpoint_status_t openenoc_endpoint_axis_send(
    volatile csr__endpoint_interface_t *endpoint,
    uint32_t data,
    uint8_t keep,
    bool last) {
    if (CSR__HAS_DIRECT_AXIS == 0U) {
        return OPENENOC_ENDPOINT_STATUS_UNSUPPORTED;
    }
    if (endpoint == NULL || ((uintptr_t)endpoint & 3U) != 0U) {
        return OPENENOC_ENDPOINT_STATUS_INVALID_ARGUMENT;
    }
    if (endpoint->axis_if.source.control.f.tvalid != 0U) {
        return OPENENOC_ENDPOINT_STATUS_NOT_READY;
    }

    // Set the payload and sideband fields before presenting a valid transfer.
    endpoint->axis_if.source.data.f.tdata = data;
    endpoint->axis_if.source.control.f.tkeep = keep;
    endpoint->axis_if.source.control.f.tlast = last;
    endpoint->axis_if.source.control.f.tvalid = 1U;

    return OPENENOC_ENDPOINT_STATUS_OK;
}

openenoc_endpoint_status_t openenoc_endpoint_axis_receive(
    volatile csr__endpoint_interface_t *endpoint,
    uint32_t *data,
    uint8_t *keep,
    bool *last) {
    uint32_t received_data;
    uint8_t received_keep;
    bool received_last;

    if (CSR__HAS_DIRECT_AXIS == 0U) {
        return OPENENOC_ENDPOINT_STATUS_UNSUPPORTED;
    }
    if (endpoint == NULL || ((uintptr_t)endpoint & 3U) != 0U || data == NULL) {
        return OPENENOC_ENDPOINT_STATUS_INVALID_ARGUMENT;
    }
    if (endpoint->axis_if.sink.control.f.tready != 0U ||
        endpoint->axis_if.sink.status.f.tvalid == 0U) {
        return OPENENOC_ENDPOINT_STATUS_NOT_READY;
    }

    // TDATA, TKEEP, and TLAST are stable while TVALID is set and TREADY is clear.
    received_data = endpoint->axis_if.sink.data.f.tdata;
    received_keep = (uint8_t)endpoint->axis_if.sink.status.f.tkeep;
    received_last = endpoint->axis_if.sink.status.f.tlast != 0U;

    *data = received_data;
    if (keep != NULL) {
        *keep = received_keep;
    }
    if (last != NULL) {
        *last = received_last;
    }

    // Acknowledge only after all fields have been captured.
    endpoint->axis_if.sink.control.f.tready = 1U;

    return OPENENOC_ENDPOINT_STATUS_OK;
}

openenoc_endpoint_status_t openenoc_endpoint_axis_send_stream(
    volatile csr__endpoint_interface_t *endpoint,
    const void *buffer,
    uint32_t byte_count) {
    const uint8_t *bytes = buffer;
    uint32_t offset = 0U;

    if (CSR__HAS_DIRECT_AXIS == 0U) {
        return OPENENOC_ENDPOINT_STATUS_UNSUPPORTED;
    }
    if (endpoint == NULL || ((uintptr_t)endpoint & 3U) != 0U ||
        buffer == NULL || byte_count == 0U) {
        return OPENENOC_ENDPOINT_STATUS_INVALID_ARGUMENT;
    }
    while (offset < byte_count) {
        uint32_t data = 0U;
        uint32_t count = byte_count - offset;
        uint8_t keep = 0U;

        if (count > 4U) {
            count = 4U;
        }
        for (uint32_t lane = 0U; lane < count; ++lane) {
            data |= (uint32_t)bytes[offset + lane] << (lane * 8U);
            keep |= (uint8_t)(1U << lane);
        }
        while (endpoint->axis_if.source.control.f.tvalid != 0U) {
        }
        endpoint->axis_if.source.data.f.tdata = data;
        endpoint->axis_if.source.control.f.tkeep = keep;
        endpoint->axis_if.source.control.f.tlast = count == byte_count - offset;
        endpoint->axis_if.source.control.f.tvalid = 1U;
        offset += count;
    }
    return OPENENOC_ENDPOINT_STATUS_OK;
}

openenoc_endpoint_status_t openenoc_endpoint_axis_receive_stream(
    volatile csr__endpoint_interface_t *endpoint,
    void *buffer,
    uint32_t buffer_capacity_bytes,
    uint32_t *received_bytes) {
    uint8_t *bytes = buffer;
    uint32_t count = 0U;
    bool last = false;
    bool overflow = false;

    if (CSR__HAS_DIRECT_AXIS == 0U) {
        if (received_bytes != NULL) {
            *received_bytes = 0U;
        }
        return OPENENOC_ENDPOINT_STATUS_UNSUPPORTED;
    }
    if (received_bytes == NULL || (buffer == NULL && buffer_capacity_bytes != 0U)) {
        return OPENENOC_ENDPOINT_STATUS_INVALID_ARGUMENT;
    }
    if (endpoint == NULL || ((uintptr_t)endpoint & 3U) != 0U) {
        *received_bytes = 0U;
        return OPENENOC_ENDPOINT_STATUS_INVALID_ARGUMENT;
    }
    while (!last) {
        uint32_t data;
        uint8_t keep;

        while (endpoint->axis_if.sink.control.f.tready != 0U) {
        }
        while (endpoint->axis_if.sink.status.f.tvalid == 0U) {
        }
        data = endpoint->axis_if.sink.data.f.tdata;
        keep = (uint8_t)endpoint->axis_if.sink.status.f.tkeep;
        last = endpoint->axis_if.sink.status.f.tlast != 0U;
        endpoint->axis_if.sink.control.f.tready = 1U;

        for (uint32_t lane = 0U; lane < 4U; ++lane) {
            if ((keep & (1U << lane)) == 0U) {
                continue;
            }
            if (count < buffer_capacity_bytes) {
                bytes[count] = (uint8_t)(data >> (lane * 8U));
            } else {
                overflow = true;
            }
            if (count == UINT32_MAX) {
                overflow = true;
            } else {
                ++count;
            }
        }
    }
    *received_bytes = count;
    return overflow ? OPENENOC_ENDPOINT_STATUS_OUT_OF_RANGE : OPENENOC_ENDPOINT_STATUS_OK;
}
