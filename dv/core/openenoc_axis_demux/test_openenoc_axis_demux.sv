// SPDX-FileCopyrightText: 2026 Kerim Bavcic
// SPDX-License-Identifier: AGPL-3.0-or-later

`resetall
`timescale 1ns / 1ps
`default_nettype none

/*
 * AXI4-Stream demultiplexer testbench
 */
module test_openenoc_axis_demux #
(
    /* verilator lint_off WIDTHTRUNC */
    parameter M_COUNT = 4,
    parameter DATA_W = 8,
    parameter logic KEEP_EN = (DATA_W>8),
    parameter KEEP_W = ((DATA_W+7)/8),
    parameter logic STRB_EN = 1'b0,
    parameter logic LAST_EN = 1'b1,
    parameter logic ID_EN = 1'b0,
    parameter M_ID_W = 8,
    parameter S_ID_W = M_ID_W+$clog2(M_COUNT),
    parameter logic DEST_EN = 1'b0,
    parameter M_DEST_W = 8,
    parameter S_DEST_W = M_DEST_W+$clog2(M_COUNT),
    parameter logic USER_EN = 1'b1,
    parameter USER_W = M_COUNT,
    parameter logic TID_ROUTE = 1'b0,
    parameter logic TDEST_ROUTE = 1'b0,
    parameter logic TUSER_BITMAP_ROUTE = 1'b0
    /* verilator lint_on WIDTHTRUNC */
)
();

    logic clk;
    logic rst;

    taxi_axis_if #(
        .DATA_W(DATA_W),
        .KEEP_EN(KEEP_EN),
        .KEEP_W(KEEP_W),
        .STRB_EN(STRB_EN),
        .LAST_EN(LAST_EN),
        .ID_EN(ID_EN),
        .ID_W(S_ID_W),
        .DEST_EN(DEST_EN),
        .DEST_W(S_DEST_W),
        .USER_EN(USER_EN),
        .USER_W(USER_W)
    ) s_axis();

    taxi_axis_if #(
        .DATA_W(DATA_W),
        .KEEP_EN(KEEP_EN),
        .KEEP_W(KEEP_W),
        .STRB_EN(STRB_EN),
        .LAST_EN(LAST_EN),
        .ID_EN(ID_EN),
        .ID_W(M_ID_W),
        .DEST_EN(DEST_EN),
        .DEST_W(M_DEST_W),
        .USER_EN(USER_EN),
        .USER_W(USER_W)
    ) m_axis[M_COUNT]();

    logic enable;
    logic drop;
    logic [$clog2(M_COUNT)-1:0] select;

    openenoc_axis_demux #(
        .M_COUNT(M_COUNT),
        .TID_ROUTE(TID_ROUTE),
        .TDEST_ROUTE(TDEST_ROUTE),
        .TUSER_BITMAP_ROUTE(TUSER_BITMAP_ROUTE)
    )
    uut (
        .clk(clk),
        .rst(rst),

        /*
        * AXI4-Stream input (sink)
        */
        .s_axis(s_axis),

        /*
        * AXI4-Stream output (source)
        */
        .m_axis(m_axis),

        /*
        * Control
        */
        .enable(enable),
        .drop(drop),
        .select(select)
    );

endmodule

`resetall
