# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: AGPL-3.0-or-later

.section .text.boot, "ax", @progbits
.balign 4
.globl _start
.type _start, @function

_start:
    # Establish the RISC-V ABI state before entering compiled C code.
    la sp, __stack_top

    # Suppress relaxation here so gp is formed from its absolute linker symbol.
    .option push
    .option norelax
    la gp, __global_pointer$
    .option pop

    # Move the initialized writable image from read-only IMEM into DMEM.
    la t0, __data_load_start
    la t1, __data_start
    la t2, __data_end

.Lcopy_data:
    bgeu t1, t2, .Lclear_bss_setup
    lw t3, 0(t0)
    sw t3, 0(t1)
    addi t0, t0, 4
    addi t1, t1, 4
    j .Lcopy_data

    # C requires every object in .bss to contain zero before main starts.
.Lclear_bss_setup:
    la t0, __bss_start
    la t1, __bss_end

.Lclear_bss:
    bgeu t0, t1, .Lenter_main
    sw zero, 0(t0)
    addi t0, t0, 4
    j .Lclear_bss

    # No command-line or environment objects exist in this bare-metal runtime.
.Lenter_main:
    mv a0, zero
    mv a1, zero
    mv a2, zero
    call main

    # A returned main has nowhere to transfer control, so stop in place.
.Lhalt:
    j .Lhalt

.size _start, . - _start
