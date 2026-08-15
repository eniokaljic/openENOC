/* SPDX-FileCopyrightText: 2026 Enio Kaljic
 * SPDX-License-Identifier: AGPL-3.0-or-later
 */

#ifndef OPENENOC_MEMORY_MAP_H
#define OPENENOC_MEMORY_MAP_H

#include <stdint.h>

/* CPU-visible regions implemented by the PicoRV32 platform. */
#define OPENENOC_IMEM_BASE UINT32_C(0x00000000)
#define OPENENOC_IMEM_SIZE UINT32_C(0x00008000)

#define OPENENOC_DMEM_BASE UINT32_C(0x10000000)
#define OPENENOC_DMEM_SIZE UINT32_C(0x00008000)

/* Base address added to the register offsets from the generated CSR RAL. */
#define OPENENOC_CSR_BASE UINT32_C(0x20000000)

#endif /* OPENENOC_MEMORY_MAP_H */
