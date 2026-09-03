// SPDX-FileCopyrightText: 2026 Enio Kaljic
// SPDX-License-Identifier: CERN-OHL-S-2.0

`resetall
`timescale 1ns / 1ps
`default_nettype none

/*
 * PicoRV32 wrapper with the openENOC AXI4-Lite adapter
 */
module openenoc_picorv32 #(
    parameter [0:0] ENABLE_COUNTERS = 1,
    parameter [0:0] ENABLE_COUNTERS64 = 1,
    parameter [0:0] ENABLE_REGS_16_31 = 1,
    parameter [0:0] ENABLE_REGS_DUALPORT = 1,
    parameter [0:0] TWO_STAGE_SHIFT = 1,
    parameter [0:0] BARREL_SHIFTER = 0,
    parameter [0:0] TWO_CYCLE_COMPARE = 0,
    parameter [0:0] TWO_CYCLE_ALU = 0,
    parameter [0:0] COMPRESSED_ISA = 0,
    parameter [0:0] CATCH_MISALIGN = 1,
    parameter [0:0] CATCH_ILLINSN = 1,
    parameter [0:0] ENABLE_PCPI = 0,
    parameter [0:0] ENABLE_MUL = 0,
    parameter [0:0] ENABLE_FAST_MUL = 0,
    parameter [0:0] ENABLE_DIV = 0,
    parameter [0:0] ENABLE_IRQ = 0,
    parameter [0:0] ENABLE_IRQ_QREGS = 1,
    parameter [0:0] ENABLE_IRQ_TIMER = 1,
    parameter [0:0] ENABLE_TRACE = 0,
    parameter [0:0] REGS_INIT_ZERO = 0,
    parameter [31:0] MASKED_IRQ = 32'h0000_0000,
    parameter [31:0] LATCHED_IRQ = 32'hffff_ffff,
    parameter [31:0] PROGADDR_RESET = 32'h0000_0000,
    parameter [31:0] PROGADDR_IRQ = 32'h0000_0010,
    parameter [31:0] STACKADDR = 32'hffff_ffff
) (
    input  wire logic        clk,
    input  wire logic        resetn,
    output wire logic        trap,

    /*
     * AXI4-Lite master memory interface
     */
    output wire logic        mem_axi_awvalid,
    input  wire logic        mem_axi_awready,
    output wire logic [31:0] mem_axi_awaddr,
    output wire logic [2:0]  mem_axi_awprot,

    output wire logic        mem_axi_wvalid,
    input  wire logic        mem_axi_wready,
    output wire logic [31:0] mem_axi_wdata,
    output wire logic [3:0]  mem_axi_wstrb,

    input  wire logic        mem_axi_bvalid,
    output wire logic        mem_axi_bready,

    output wire logic        mem_axi_arvalid,
    input  wire logic        mem_axi_arready,
    output wire logic [31:0] mem_axi_araddr,
    output wire logic [2:0]  mem_axi_arprot,

    input  wire logic        mem_axi_rvalid,
    output wire logic        mem_axi_rready,
    input  wire logic [31:0] mem_axi_rdata,

    /*
     * Pico Co-Processor Interface (PCPI)
     */
    output wire logic        pcpi_valid,
    output wire logic [31:0] pcpi_insn,
    output wire logic [31:0] pcpi_rs1,
    output wire logic [31:0] pcpi_rs2,
    input  wire logic        pcpi_wr,
    input  wire logic [31:0] pcpi_rd,
    input  wire logic        pcpi_wait,
    input  wire logic        pcpi_ready,

    /*
     * IRQ interface
     */
    input  wire logic [31:0] irq,
    output wire logic [31:0] eoi,

`ifdef RISCV_FORMAL
    output wire logic        rvfi_valid,
    output wire logic [63:0] rvfi_order,
    output wire logic [31:0] rvfi_insn,
    output wire logic        rvfi_trap,
    output wire logic        rvfi_halt,
    output wire logic        rvfi_intr,
    output wire logic [4:0]  rvfi_rs1_addr,
    output wire logic [4:0]  rvfi_rs2_addr,
    output wire logic [31:0] rvfi_rs1_rdata,
    output wire logic [31:0] rvfi_rs2_rdata,
    output wire logic [4:0]  rvfi_rd_addr,
    output wire logic [31:0] rvfi_rd_wdata,
    output wire logic [31:0] rvfi_pc_rdata,
    output wire logic [31:0] rvfi_pc_wdata,
    output wire logic [31:0] rvfi_mem_addr,
    output wire logic [3:0]  rvfi_mem_rmask,
    output wire logic [3:0]  rvfi_mem_wmask,
    output wire logic [31:0] rvfi_mem_rdata,
    output wire logic [31:0] rvfi_mem_wdata,
`endif

    /*
     * Trace interface
     */
    output wire logic        trace_valid,
    output wire logic [35:0] trace_data
);

    wire logic        mem_valid;
    wire logic        mem_instr;
    wire logic        mem_ready;
    wire logic [31:0] mem_addr;
    wire logic [31:0] mem_wdata;
    wire logic [3:0]  mem_wstrb;
    wire logic [31:0] mem_rdata;

    wire logic        mem_la_read;
    wire logic        mem_la_write;
    wire logic [31:0] mem_la_addr;
    wire logic [31:0] mem_la_wdata;
    wire logic [3:0]  mem_la_wstrb;

    openenoc_picorv32_axil_adapter u_axil_adapter (
        .clk             (clk),
        .resetn          (resetn),

        .mem_axi_awvalid (mem_axi_awvalid),
        .mem_axi_awready (mem_axi_awready),
        .mem_axi_awaddr  (mem_axi_awaddr),
        .mem_axi_awprot  (mem_axi_awprot),
        .mem_axi_wvalid  (mem_axi_wvalid),
        .mem_axi_wready  (mem_axi_wready),
        .mem_axi_wdata   (mem_axi_wdata),
        .mem_axi_wstrb   (mem_axi_wstrb),
        .mem_axi_bvalid  (mem_axi_bvalid),
        .mem_axi_bready  (mem_axi_bready),
        .mem_axi_arvalid (mem_axi_arvalid),
        .mem_axi_arready (mem_axi_arready),
        .mem_axi_araddr  (mem_axi_araddr),
        .mem_axi_arprot  (mem_axi_arprot),
        .mem_axi_rvalid  (mem_axi_rvalid),
        .mem_axi_rready  (mem_axi_rready),
        .mem_axi_rdata   (mem_axi_rdata),

        .mem_valid       (mem_valid),
        .mem_instr       (mem_instr),
        .mem_ready       (mem_ready),
        .mem_addr        (mem_addr),
        .mem_wdata       (mem_wdata),
        .mem_wstrb       (mem_wstrb),
        .mem_rdata       (mem_rdata),

        .mem_la_read     (mem_la_read),
        .mem_la_write    (mem_la_write),
        .mem_la_addr     (mem_la_addr),
        .mem_la_wdata    (mem_la_wdata),
        .mem_la_wstrb    (mem_la_wstrb)
    );

    picorv32 #(
        .ENABLE_COUNTERS      (ENABLE_COUNTERS),
        .ENABLE_COUNTERS64    (ENABLE_COUNTERS64),
        .ENABLE_REGS_16_31    (ENABLE_REGS_16_31),
        .ENABLE_REGS_DUALPORT (ENABLE_REGS_DUALPORT),
        .TWO_STAGE_SHIFT      (TWO_STAGE_SHIFT),
        .BARREL_SHIFTER       (BARREL_SHIFTER),
        .TWO_CYCLE_COMPARE    (TWO_CYCLE_COMPARE),
        .TWO_CYCLE_ALU        (TWO_CYCLE_ALU),
        .COMPRESSED_ISA       (COMPRESSED_ISA),
        .CATCH_MISALIGN       (CATCH_MISALIGN),
        .CATCH_ILLINSN        (CATCH_ILLINSN),
        .ENABLE_PCPI          (ENABLE_PCPI),
        .ENABLE_MUL           (ENABLE_MUL),
        .ENABLE_FAST_MUL      (ENABLE_FAST_MUL),
        .ENABLE_DIV           (ENABLE_DIV),
        .ENABLE_IRQ           (ENABLE_IRQ),
        .ENABLE_IRQ_QREGS     (ENABLE_IRQ_QREGS),
        .ENABLE_IRQ_TIMER     (ENABLE_IRQ_TIMER),
        .ENABLE_TRACE         (ENABLE_TRACE),
        .REGS_INIT_ZERO       (REGS_INIT_ZERO),
        .MASKED_IRQ           (MASKED_IRQ),
        .LATCHED_IRQ          (LATCHED_IRQ),
        .PROGADDR_RESET       (PROGADDR_RESET),
        .PROGADDR_IRQ         (PROGADDR_IRQ),
        .STACKADDR            (STACKADDR)
    ) u_picorv32_core (
        .clk          (clk),
        .resetn       (resetn),
        .trap         (trap),

        .mem_valid    (mem_valid),
        .mem_instr    (mem_instr),
        .mem_ready    (mem_ready),
        .mem_addr     (mem_addr),
        .mem_wdata    (mem_wdata),
        .mem_wstrb    (mem_wstrb),
        .mem_rdata    (mem_rdata),

        .mem_la_read  (mem_la_read),
        .mem_la_write (mem_la_write),
        .mem_la_addr  (mem_la_addr),
        .mem_la_wdata (mem_la_wdata),
        .mem_la_wstrb (mem_la_wstrb),

        .pcpi_valid   (pcpi_valid),
        .pcpi_insn    (pcpi_insn),
        .pcpi_rs1     (pcpi_rs1),
        .pcpi_rs2     (pcpi_rs2),
        .pcpi_wr      (pcpi_wr),
        .pcpi_rd      (pcpi_rd),
        .pcpi_wait    (pcpi_wait),
        .pcpi_ready   (pcpi_ready),

        .irq          (irq),
        .eoi          (eoi),

`ifdef RISCV_FORMAL
        .rvfi_valid     (rvfi_valid),
        .rvfi_order     (rvfi_order),
        .rvfi_insn      (rvfi_insn),
        .rvfi_trap      (rvfi_trap),
        .rvfi_halt      (rvfi_halt),
        .rvfi_intr      (rvfi_intr),
        .rvfi_mode      (),
        .rvfi_ixl       (),
        .rvfi_rs1_addr  (rvfi_rs1_addr),
        .rvfi_rs2_addr  (rvfi_rs2_addr),
        .rvfi_rs1_rdata (rvfi_rs1_rdata),
        .rvfi_rs2_rdata (rvfi_rs2_rdata),
        .rvfi_rd_addr   (rvfi_rd_addr),
        .rvfi_rd_wdata  (rvfi_rd_wdata),
        .rvfi_pc_rdata  (rvfi_pc_rdata),
        .rvfi_pc_wdata  (rvfi_pc_wdata),
        .rvfi_mem_addr  (rvfi_mem_addr),
        .rvfi_mem_rmask (rvfi_mem_rmask),
        .rvfi_mem_wmask (rvfi_mem_wmask),
        .rvfi_mem_rdata (rvfi_mem_rdata),
        .rvfi_mem_wdata (rvfi_mem_wdata),
        .rvfi_csr_mcycle_rmask   (),
        .rvfi_csr_mcycle_wmask   (),
        .rvfi_csr_mcycle_rdata   (),
        .rvfi_csr_mcycle_wdata   (),
        .rvfi_csr_minstret_rmask (),
        .rvfi_csr_minstret_wmask (),
        .rvfi_csr_minstret_rdata (),
        .rvfi_csr_minstret_wdata (),
`endif

        .trace_valid  (trace_valid),
        .trace_data   (trace_data)
    );

endmodule

`resetall
