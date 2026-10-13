.section .text.boot, "ax", @progbits
.balign 4
.globl _start
.type _start, @function
_start:
    csrw mie, zero
    la sp, __stack_top
    .option push
    .option norelax
    la gp, __global_pointer$
    .option pop
    la t0, irq_entry
    csrw mtvec, t0

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

.Lclear_bss_setup:
    la t0, __bss_start
    la t1, __bss_end
.Lclear_bss:
    bgeu t0, t1, .Lenter_main
    sw zero, 0(t0)
    addi t0, t0, 4
    j .Lclear_bss

.Lenter_main:
    mv a0, zero
    mv a1, zero
    mv a2, zero
    call main
.Lhalt:
    j .Lhalt
.size _start, . - _start
