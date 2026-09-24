// SPDX-FileCopyrightText: 2026 Kerim Bavcic
// SPDX-License-Identifier: AGPL-3.0-or-later

`resetall
`timescale 1ns / 1ps
`default_nettype none

/* verilator lint_off DECLFILENAME */
/* verilator lint_off UNUSEDPARAM */
module openenoc_picorv32 #(
    parameter [31:0] PROGADDR_RESET = 32'h0000_0000,
    parameter [31:0] STACKADDR = 32'hffff_ffff
) (
    input  wire logic        clk,
    input  wire logic        resetn,
    output wire logic        trap,

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

    output wire logic        pcpi_valid,
    output wire logic [31:0] pcpi_insn,
    output wire logic [31:0] pcpi_rs1,
    output wire logic [31:0] pcpi_rs2,
    input  wire logic        pcpi_wr,
    input  wire logic [31:0] pcpi_rd,
    input  wire logic        pcpi_wait,
    input  wire logic        pcpi_ready,

    input  wire logic [31:0] irq,
    output wire logic [31:0] eoi,
    output wire logic        trace_valid,
    output wire logic [35:0] trace_data
);

    logic        dv_mem_axi_awvalid;
    logic [31:0] dv_mem_axi_awaddr;
    logic [2:0]  dv_mem_axi_awprot;
    logic        dv_mem_axi_wvalid;
    logic [31:0] dv_mem_axi_wdata;
    logic [3:0]  dv_mem_axi_wstrb;
    logic        dv_mem_axi_bready;
    logic        dv_mem_axi_arvalid;
    logic [31:0] dv_mem_axi_araddr;
    logic [2:0]  dv_mem_axi_arprot;
    logic        dv_mem_axi_rready;

    assign mem_axi_awvalid = dv_mem_axi_awvalid;
    assign mem_axi_awaddr  = dv_mem_axi_awaddr;
    assign mem_axi_awprot  = dv_mem_axi_awprot;
    assign mem_axi_wvalid  = dv_mem_axi_wvalid;
    assign mem_axi_wdata   = dv_mem_axi_wdata;
    assign mem_axi_wstrb   = dv_mem_axi_wstrb;
    assign mem_axi_bready  = dv_mem_axi_bready;
    assign mem_axi_arvalid = dv_mem_axi_arvalid;
    assign mem_axi_araddr  = dv_mem_axi_araddr;
    assign mem_axi_arprot  = dv_mem_axi_arprot;
    assign mem_axi_rready  = dv_mem_axi_rready;

    assign trap        = 1'b0;
    assign pcpi_valid  = 1'b0;
    assign pcpi_insn   = '0;
    assign pcpi_rs1    = '0;
    assign pcpi_rs2    = '0;
    assign eoi         = '0;
    assign trace_valid = 1'b0;
    assign trace_data  = '0;

endmodule
/* verilator lint_on UNUSEDPARAM */
/* verilator lint_on DECLFILENAME */

`resetall
