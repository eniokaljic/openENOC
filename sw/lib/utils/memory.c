/* SPDX-FileCopyrightText: 2026 Enio Kaljic
 * SPDX-License-Identifier: AGPL-3.0-or-later
 */

#include <stddef.h>

/* Compiler support for aggregate initialization and copying in freestanding firmware. */
void *memset(void *destination, int value, size_t count) {
    unsigned char *bytes = destination;

    for (size_t index = 0; index < count; ++index) {
        bytes[index] = (unsigned char)value;
    }
    return destination;
}

void *memcpy(void *destination, const void *source, size_t count) {
    unsigned char *output = destination;
    const unsigned char *input = source;

    for (size_t index = 0; index < count; ++index) {
        output[index] = input[index];
    }
    return destination;
}
