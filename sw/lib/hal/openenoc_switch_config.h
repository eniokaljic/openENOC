/* SPDX-FileCopyrightText: 2026 Enio Kaljic
 * SPDX-License-Identifier: AGPL-3.0-or-later
 */

#ifndef OPENENOC_SWITCH_CONFIG_H
#define OPENENOC_SWITCH_CONFIG_H

#include "openenoc_switch_common.h"

#ifdef __cplusplus
extern "C" {
#endif

typedef enum {
    OPENENOC_SWITCH_UNMANAGED = 0,
    OPENENOC_SWITCH_MANAGED = 1
} openenoc_switch_operation_mode_t;

typedef struct {
    bool pause_requested;
    bool pause_done;
} openenoc_switch_forwarding_status_t;

openenoc_switch_status_t openenoc_switch_get_default_forwarding(
    const volatile csr__switch_interface_t *switch_interface, uint32_t *bitmap);

openenoc_switch_status_t openenoc_switch_set_default_forwarding(
    volatile csr__switch_interface_t *switch_interface, uint32_t bitmap);

openenoc_switch_status_t openenoc_switch_get_operation_mode(
    const volatile csr__switch_interface_t *switch_interface,
    openenoc_switch_operation_mode_t *mode);

openenoc_switch_status_t openenoc_switch_set_operation_mode(
    volatile csr__switch_interface_t *switch_interface, openenoc_switch_operation_mode_t mode);

openenoc_switch_status_t openenoc_switch_get_status(
    const volatile csr__switch_interface_t *switch_interface,
    openenoc_switch_forwarding_status_t *status);

openenoc_switch_status_t openenoc_switch_request_pause(
    volatile csr__switch_interface_t *switch_interface);

openenoc_switch_status_t openenoc_switch_resume(
    volatile csr__switch_interface_t *switch_interface);

#ifdef __cplusplus
}
#endif

#endif
