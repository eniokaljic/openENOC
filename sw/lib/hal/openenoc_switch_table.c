/* SPDX-FileCopyrightText: 2026 Enio Kaljic
 * SPDX-License-Identifier: AGPL-3.0-or-later
 */

#define OPENENOC_SWITCH_IMPLEMENTATION
#include "openenoc_switch.h"

openenoc_switch_status_t openenoc_switch_table_get_entry(
    const volatile csr__switch_interface_t *switch_interface, uint16_t entry_index,
    openenoc_switch_table_entry_t *entry) {
    if (!openenoc_switch_pointer_valid(switch_interface) || entry == NULL) {
        return OPENENOC_SWITCH_STATUS_INVALID_ARGUMENT;
    }
    if (entry_index >= CSR__TABLE_DEPTH) {
        return OPENENOC_SWITCH_STATUS_OUT_OF_RANGE;
    }
    if (!openenoc_switch_paused(switch_interface)) {
        return OPENENOC_SWITCH_STATUS_NOT_READY;
    }
    openenoc_switch_mac_unpack(
        switch_interface->forwarding_table.entry[entry_index].mac_address.f.lo_word,
        switch_interface->forwarding_table.entry[entry_index].mac_address.f.hi_word,
        &entry->mac_address);
    entry->interface_bitmap = switch_interface->forwarding_table.entry[entry_index].iface.f.bitmap;
    entry->enabled = switch_interface->forwarding_table.entry[entry_index].config.f.enabled != 0U;
    return OPENENOC_SWITCH_STATUS_OK;
}

openenoc_switch_status_t openenoc_switch_table_set_entry(
    volatile csr__switch_interface_t *switch_interface, uint16_t entry_index,
    const openenoc_switch_table_entry_t *entry) {
    openenoc_switch_status_t status;
    openenoc_switch_mac_words_t words;

    if (!openenoc_switch_pointer_valid(switch_interface) || entry == NULL) {
        return OPENENOC_SWITCH_STATUS_INVALID_ARGUMENT;
    }
    if (entry_index >= CSR__TABLE_DEPTH || !openenoc_switch_bitmap_valid(entry->interface_bitmap)) {
        return OPENENOC_SWITCH_STATUS_OUT_OF_RANGE;
    }
    status = openenoc_switch_write_ready(switch_interface);
    if (status != OPENENOC_SWITCH_STATUS_OK) {
        return status;
    }
    words = openenoc_switch_mac_pack(&entry->mac_address);
    switch_interface->forwarding_table.entry[entry_index].config.f.enabled = 0U;
    switch_interface->forwarding_table.entry[entry_index].mac_address.f.lo_word = words.lower;
    switch_interface->forwarding_table.entry[entry_index].mac_address.f.hi_word = words.upper;
    switch_interface->forwarding_table.entry[entry_index].iface.f.bitmap = entry->interface_bitmap;
    switch_interface->forwarding_table.entry[entry_index].config.f.enabled = entry->enabled;
    return OPENENOC_SWITCH_STATUS_OK;
}

openenoc_switch_status_t openenoc_switch_table_set_entry_enabled(
    volatile csr__switch_interface_t *switch_interface, uint16_t entry_index, bool enabled) {
    openenoc_switch_status_t status;

    if (!openenoc_switch_pointer_valid(switch_interface)) {
        return OPENENOC_SWITCH_STATUS_INVALID_ARGUMENT;
    }
    if (entry_index >= CSR__TABLE_DEPTH) {
        return OPENENOC_SWITCH_STATUS_OUT_OF_RANGE;
    }
    status = openenoc_switch_write_ready(switch_interface);
    if (status != OPENENOC_SWITCH_STATUS_OK) {
        return status;
    }
    switch_interface->forwarding_table.entry[entry_index].config.f.enabled = enabled;
    return OPENENOC_SWITCH_STATUS_OK;
}

openenoc_switch_status_t openenoc_switch_table_clear(
    volatile csr__switch_interface_t *switch_interface) {
    openenoc_switch_status_t status;

    if (!openenoc_switch_pointer_valid(switch_interface)) {
        return OPENENOC_SWITCH_STATUS_INVALID_ARGUMENT;
    }
    status = openenoc_switch_write_ready(switch_interface);
    if (status != OPENENOC_SWITCH_STATUS_OK) {
        return status;
    }
    for (uint32_t entry_index = 0; entry_index < CSR__TABLE_DEPTH; ++entry_index) {
        switch_interface->forwarding_table.entry[entry_index].config.f.enabled = 0U;
    }
    return OPENENOC_SWITCH_STATUS_OK;
}
