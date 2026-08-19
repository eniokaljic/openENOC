// SPDX-FileCopyrightText: 2026 Enio Kaljic
// SPDX-License-Identifier: AGPL-3.0-or-later

`resetall
`timescale 1ns / 1ps
`default_nettype none

/*
 * AXI4-Lite RAM testbench
 */
module test_openenoc_axil_ram #
(
    /* verilator lint_off WIDTHTRUNC */
    parameter DATA_W = 32,
    parameter ADDR_W = 10,
    parameter AXIL_ADDR_W = 32,
    parameter STRB_W = DATA_W/8,
    parameter logic PIPELINE_OUTPUT = 1'b0,
    parameter INIT_FILE = ""
    /* verilator lint_on WIDTHTRUNC */
)
();

    logic clk;
    logic rst;

    taxi_axil_if #(
        .DATA_W(DATA_W),
        .ADDR_W(AXIL_ADDR_W),
        .STRB_W(STRB_W)
    ) s_axil();

    openenoc_axil_ram #(
        .ADDR_W(ADDR_W),
        .PIPELINE_OUTPUT(PIPELINE_OUTPUT),
        .INIT_FILE(INIT_FILE)
    )
    uut (
        .clk(clk),
        .rst(rst),

        .s_axil_wr(s_axil),
        .s_axil_rd(s_axil)
    );

    endmodule

`resetall
