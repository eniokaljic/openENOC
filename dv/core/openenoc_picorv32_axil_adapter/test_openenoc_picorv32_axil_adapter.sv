// SPDX-FileCopyrightText: 2026 Enio Kaljic
// SPDX-License-Identifier: AGPL-3.0-or-later

`resetall
`timescale 1ns / 1ps
`default_nettype none

/*
 * PicoRV32 native memory to AXI4-Lite adapter testbench
 */
module test_openenoc_picorv32_axil_adapter;

    logic clk;
    logic resetn;

    wire logic        mem_axi_awvalid;
    logic             mem_axi_awready;
    wire logic [31:0] mem_axi_awaddr;
    wire logic [2:0]  mem_axi_awprot;

    wire logic        mem_axi_wvalid;
    logic             mem_axi_wready;
    wire logic [31:0] mem_axi_wdata;
    wire logic [3:0]  mem_axi_wstrb;

    logic             mem_axi_bvalid;
    wire logic        mem_axi_bready;

    wire logic        mem_axi_arvalid;
    logic             mem_axi_arready;
    wire logic [31:0] mem_axi_araddr;
    wire logic [2:0]  mem_axi_arprot;

    logic             mem_axi_rvalid;
    wire logic        mem_axi_rready;
    logic [31:0]      mem_axi_rdata;

    logic             mem_valid;
    logic             mem_instr;
    wire logic        mem_ready;
    logic [31:0]      mem_addr;
    logic [31:0]      mem_wdata;
    logic [3:0]       mem_wstrb;
    wire logic [31:0] mem_rdata;

    logic             mem_la_read;
    logic             mem_la_write;
    logic [31:0]      mem_la_addr;
    logic [31:0]      mem_la_wdata;
    logic [3:0]       mem_la_wstrb;

    openenoc_picorv32_axil_adapter u_openenoc_picorv32_axil_adapter (
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

endmodule

`resetall
