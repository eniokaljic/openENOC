# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: AGPL-3.0-or-later

.section .text.irq_entry, "ax", @progbits
.balign 4
.globl irq_entry
.type irq_entry, @function
irq_entry:
    # Preserve the interrupted context on its stack, aligned to 16 bytes.
    # Word zero holds q0 (the return PC); words 1-31 hold the integer registers.
    addi sp, sp, -128
    sw x1, 4(sp)
    sw x5, 20(sp)
    addi x5, sp, 128
    sw x5, 8(sp)
    sw x3, 12(sp)
    sw x4, 16(sp)
    sw x6, 24(sp)
    sw x7, 28(sp)
    sw x8, 32(sp)
    sw x9, 36(sp)
    sw x10, 40(sp)
    sw x11, 44(sp)
    sw x12, 48(sp)
    sw x13, 52(sp)
    sw x14, 56(sp)
    sw x15, 60(sp)
    sw x16, 64(sp)
    sw x17, 68(sp)
    sw x18, 72(sp)
    sw x19, 76(sp)
    sw x20, 80(sp)
    sw x21, 84(sp)
    sw x22, 88(sp)
    sw x23, 92(sp)
    sw x24, 96(sp)
    sw x25, 100(sp)
    sw x26, 104(sp)
    sw x27, 108(sp)
    sw x28, 112(sp)
    sw x29, 116(sp)
    sw x30, 120(sp)
    sw x31, 124(sp)

    .insn r 0x0b, 4, 0, x5, x0, x0 # getq x5, q0
    sw x5, 0(sp)
    .insn r 0x0b, 4, 0, a0, x1, x0 # getq a0, q1 (x1 encodes the q1 index)
    call openenoc_endpoint_irq_handler

    lw x5, 0(sp)
    .insn r 0x0b, 2, 1, x0, x5, x0 # setq q0, x5
    lw x1, 4(sp)
    lw x3, 12(sp)
    lw x4, 16(sp)
    lw x5, 20(sp)
    lw x6, 24(sp)
    lw x7, 28(sp)
    lw x8, 32(sp)
    lw x9, 36(sp)
    lw x10, 40(sp)
    lw x11, 44(sp)
    lw x12, 48(sp)
    lw x13, 52(sp)
    lw x14, 56(sp)
    lw x15, 60(sp)
    lw x16, 64(sp)
    lw x17, 68(sp)
    lw x18, 72(sp)
    lw x19, 76(sp)
    lw x20, 80(sp)
    lw x21, 84(sp)
    lw x22, 88(sp)
    lw x23, 92(sp)
    lw x24, 96(sp)
    lw x25, 100(sp)
    lw x26, 104(sp)
    lw x27, 108(sp)
    lw x28, 112(sp)
    lw x29, 116(sp)
    lw x30, 120(sp)
    lw x31, 124(sp)
    lw sp, 8(sp)
    .insn r 0x0b, 0, 2, x0, x0, x0 # retirq
.size irq_entry, . - irq_entry

.section .text.irq_mask, "ax", @progbits
.balign 4
.globl irq_set_mask
.type irq_set_mask, @function
irq_set_mask:
    .insn r 0x0b, 6, 3, a0, a0, x0 # maskirq a0, a0
    ret
.size irq_set_mask, . - irq_set_mask
