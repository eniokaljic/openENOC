<!-- SPDX-FileCopyrightText: 2026 Enio Kaljic -->
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# PicoRV32 Platform

This directory supplies CPU startup, the linker script template and interrupt
utilities selected by `PLATFORM=picorv32`. General build configuration is
documented in the [software README](../../README.md).

## PicoRV32 Interrupts

The linker reserves a reset jump at IMEM base `0x0` and an IRQ jump at `0x10`,
matching the full endpoint's CPU vectors. Ordinary startup follows those jumps,
initializes `sp` and `gp`, copies `.data` into DMEM, and clears `.bss` before
calling `main`.

The platform `irq_entry` wrapper saves all integer registers and the `q0`
return PC on the interrupted stack, preserving 16-byte alignment. It calls
`openenoc_endpoint_irq_handler(uintptr_t cpu_irq_state)` directly with the CPU's
`q1` bitmask, restores the context, and executes `retirq`. The HAL entry uses
platform utilities to classify that opaque CPU state. An unbound HAL entry
masks all CPU sources; polling applications start and remain masked.

The platform-local `irq.h` exposes `irq_set_mask(mask)`, which returns
the previous mask. A one bit masks its IRQ. The endpoint's level-sensitive IRQ
uses CPU input 3, so `~(UINT32_C(1) << 3)` enables only that input.

The shared API and internal `_openenoc_endpoint_irq_*` hook contracts are
documented in the [IRQ HAL reference](../../lib/hal/README.md#endpoint-irq-hal).
