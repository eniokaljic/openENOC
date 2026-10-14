/* SPDX-FileCopyrightText: 2026 Enio Kaljic
 * SPDX-License-Identifier: AGPL-3.0-or-later
 */

#define OPENENOC_SWITCH_IMPLEMENTATION
#include "openenoc_switch.h"

openenoc_switch_status_t openenoc_switch_init(
    volatile csr__switch_interface_t *switch_interface) {
    if (!openenoc_switch_pointer_valid(switch_interface)) {
        return OPENENOC_SWITCH_STATUS_INVALID_ARGUMENT;
    }
    return OPENENOC_SWITCH_STATUS_OK;
}

openenoc_switch_status_t openenoc_switch_get_info(
    const volatile csr__switch_interface_t *switch_interface, openenoc_switch_info_t *info) {
    if (!openenoc_switch_pointer_valid(switch_interface) || info == NULL) {
        return OPENENOC_SWITCH_STATUS_INVALID_ARGUMENT;
    }
    info->interface_count = CSR__NUM_OF_INTERFACES;
    info->table_depth = CSR__TABLE_DEPTH;
    return OPENENOC_SWITCH_STATUS_OK;
}
