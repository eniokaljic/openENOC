/* SPDX-FileCopyrightText: 2026 Enio Kaljic
 * SPDX-License-Identifier: AGPL-3.0-or-later
 */

#define OPENENOC_SWITCH_IMPLEMENTATION
#include "openenoc_switch.h"

openenoc_switch_status_t openenoc_switch_get_default_forwarding(
    const volatile csr__switch_interface_t *switch_interface, uint32_t *bitmap) {
    if (!openenoc_switch_pointer_valid(switch_interface) || bitmap == NULL) {
        return OPENENOC_SWITCH_STATUS_INVALID_ARGUMENT;
    }
    if (!openenoc_switch_paused(switch_interface)) {
        return OPENENOC_SWITCH_STATUS_NOT_READY;
    }
    *bitmap = switch_interface->default_forwarding.f.bitmap;
    return OPENENOC_SWITCH_STATUS_OK;
}

openenoc_switch_status_t openenoc_switch_set_default_forwarding(
    volatile csr__switch_interface_t *switch_interface, uint32_t bitmap) {
    openenoc_switch_status_t status;

    if (!openenoc_switch_pointer_valid(switch_interface)) {
        return OPENENOC_SWITCH_STATUS_INVALID_ARGUMENT;
    }
    if (!openenoc_switch_bitmap_valid(bitmap)) {
        return OPENENOC_SWITCH_STATUS_OUT_OF_RANGE;
    }
    status = openenoc_switch_write_ready(switch_interface);
    if (status != OPENENOC_SWITCH_STATUS_OK) {
        return status;
    }
    switch_interface->default_forwarding.f.bitmap = bitmap;
    return OPENENOC_SWITCH_STATUS_OK;
}

openenoc_switch_status_t openenoc_switch_get_operation_mode(
    const volatile csr__switch_interface_t *switch_interface,
    openenoc_switch_operation_mode_t *mode) {
    if (!openenoc_switch_pointer_valid(switch_interface) || mode == NULL) {
        return OPENENOC_SWITCH_STATUS_INVALID_ARGUMENT;
    }
    *mode = (openenoc_switch_operation_mode_t)switch_interface->forwarding_control.f.operation_mode;
    return OPENENOC_SWITCH_STATUS_OK;
}

openenoc_switch_status_t openenoc_switch_set_operation_mode(
    volatile csr__switch_interface_t *switch_interface, openenoc_switch_operation_mode_t mode) {
    if (!openenoc_switch_pointer_valid(switch_interface) ||
        (unsigned int)mode > OPENENOC_SWITCH_MANAGED) {
        return OPENENOC_SWITCH_STATUS_INVALID_ARGUMENT;
    }
    if (!openenoc_switch_paused(switch_interface)) {
        return OPENENOC_SWITCH_STATUS_NOT_READY;
    }
    switch_interface->forwarding_control.f.operation_mode = mode;
    return OPENENOC_SWITCH_STATUS_OK;
}

openenoc_switch_status_t openenoc_switch_get_status(
    const volatile csr__switch_interface_t *switch_interface,
    openenoc_switch_forwarding_status_t *status) {
    if (!openenoc_switch_pointer_valid(switch_interface) || status == NULL) {
        return OPENENOC_SWITCH_STATUS_INVALID_ARGUMENT;
    }
    status->pause_requested = switch_interface->forwarding_control.f.pause_request != 0U;
    status->pause_done = switch_interface->forwarding_control.f.pause_done != 0U;
    return OPENENOC_SWITCH_STATUS_OK;
}

openenoc_switch_status_t openenoc_switch_request_pause(
    volatile csr__switch_interface_t *switch_interface) {
    if (!openenoc_switch_pointer_valid(switch_interface)) {
        return OPENENOC_SWITCH_STATUS_INVALID_ARGUMENT;
    }
    switch_interface->forwarding_control.f.pause_request = 1U;
    return OPENENOC_SWITCH_STATUS_OK;
}

openenoc_switch_status_t openenoc_switch_resume(
    volatile csr__switch_interface_t *switch_interface) {
    if (!openenoc_switch_pointer_valid(switch_interface)) {
        return OPENENOC_SWITCH_STATUS_INVALID_ARGUMENT;
    }
    switch_interface->forwarding_control.f.pause_request = 0U;
    return OPENENOC_SWITCH_STATUS_OK;
}
