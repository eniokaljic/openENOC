// SPDX-FileCopyrightText: 2026 Enio Kaljic
// SPDX-License-Identifier: AGPL-3.0-or-later

`resetall
`timescale 1ns / 1ps
`default_nettype none

/*
 * AXI4-Lite crossbar testbench
 */
module test_openenoc_axil_crossbar #(
    /* verilator lint_off WIDTHTRUNC */
    parameter S_COUNT = 3,
    parameter M_COUNT = 3,
    parameter DATA_W = 32,
    parameter ADDR_W = 32,
    parameter STRB_W = DATA_W/8,
    parameter TARGET_ADDR_W = 16,
    parameter S_ACCEPT = {S_COUNT{32'd16}},
    parameter M_ISSUE = {M_COUNT{32'd16}}
    /* verilator lint_on WIDTHTRUNC */
) ();

    logic clk;
    logic rst;

    taxi_axil_if #(
        .DATA_W(DATA_W),
        .ADDR_W(ADDR_W),
        .STRB_W(STRB_W)
    ) s_axil[S_COUNT]();

    taxi_axil_if #(
        .DATA_W(DATA_W),
        .ADDR_W(ADDR_W),
        .STRB_W(STRB_W)
    ) m_axil[M_COUNT]();

    openenoc_axil_crossbar #(
        .S_COUNT(S_COUNT),
        .M_COUNT(M_COUNT),
        .ADDR_W(ADDR_W),
        .S_ACCEPT(S_ACCEPT),
        .M_ADDR_W({M_COUNT{32'(TARGET_ADDR_W)}}),
        .M_CONNECT_RD({M_COUNT{{S_COUNT{1'b1}}}}),
        .M_CONNECT_WR({M_COUNT{{S_COUNT{1'b1}}}}),
        .M_ISSUE(M_ISSUE)
    ) uut (
        .clk(clk),
        .rst(rst),
        .s_axil_wr(s_axil),
        .s_axil_rd(s_axil),
        .m_axil_wr(m_axil),
        .m_axil_rd(m_axil)
    );

endmodule

`resetall
