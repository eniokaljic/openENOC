/* SPDX-FileCopyrightText: 2026 Enio Kaljic
 * SPDX-License-Identifier: AGPL-3.0-or-later
 */

#ifndef OPENENOC_SWITCH_TABLE_H
#define OPENENOC_SWITCH_TABLE_H

#include "openenoc_switch_common.h"

#ifdef __cplusplus
extern "C" {
#endif

typedef struct {
    openenoc_switch_mac_t mac_address;
    uint32_t interface_bitmap;
    bool enabled;
} openenoc_switch_table_entry_t;

openenoc_switch_status_t openenoc_switch_table_get_entry(
    const volatile csr__switch_interface_t *switch_interface, uint16_t entry_index,
    openenoc_switch_table_entry_t *entry);

openenoc_switch_status_t openenoc_switch_table_set_entry(
    volatile csr__switch_interface_t *switch_interface, uint16_t entry_index,
    const openenoc_switch_table_entry_t *entry);

openenoc_switch_status_t openenoc_switch_table_set_entry_enabled(
    volatile csr__switch_interface_t *switch_interface, uint16_t entry_index, bool enabled);

openenoc_switch_status_t openenoc_switch_table_clear(
    volatile csr__switch_interface_t *switch_interface);

#ifdef __cplusplus
}
#endif

#endif
