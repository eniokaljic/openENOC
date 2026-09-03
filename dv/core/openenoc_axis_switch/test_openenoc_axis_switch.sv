// SPDX-FileCopyrightText: 2026 Kerim Bavcic
// SPDX-License-Identifier: AGPL-3.0-or-later

`resetall
`timescale 1ns / 1ps
`default_nettype none

/*
 * AXI4-Stream switch testbench
 */
module test_openenoc_axis_switch #
(
    /* verilator lint_off WIDTHTRUNC */
    parameter S_COUNT = 4,
    parameter M_COUNT = 4,
    parameter DATA_W = 8,
    parameter logic KEEP_EN = (DATA_W > 8),
    parameter KEEP_W = ((DATA_W + 7) / 8),
    parameter logic STRB_EN = 1'b0,
    parameter logic LAST_EN = 1'b1,
    parameter logic ID_EN = 1'b1,
    parameter M_ID_W = 8,
    parameter S_ID_W = M_ID_W + $clog2(M_COUNT),
    parameter logic DEST_EN = 1'b1,
    parameter M_DEST_W = 8,
    parameter S_DEST_W = M_DEST_W + $clog2(M_COUNT),
    parameter logic USER_EN = 1'b1,
    parameter USER_W = M_COUNT,
    parameter logic TUSER_BITMAP_ROUTE = 1'b0,
    parameter logic M_CONNECT[M_COUNT][S_COUNT] = '{M_COUNT{'{S_COUNT{1'b1}}}},
    parameter S_REG_TYPE = 2,
    parameter M_REG_TYPE = 0
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
    ) s_axis_if[S_COUNT]();

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
    ) m_axis_if[M_COUNT]();

    openenoc_axis_switch #(
        .S_COUNT(S_COUNT),
        .M_COUNT(M_COUNT),
        .M_CONNECT(M_CONNECT),
        .S_REG_TYPE(S_REG_TYPE),
        .M_REG_TYPE(M_REG_TYPE)
    )
    u_openenoc_axis_switch (
        .clk(clk),
        .rst(rst),
        .tuser_bitmap_route(TUSER_BITMAP_ROUTE),
        .s_axis(s_axis_if),
        .m_axis(m_axis_if)
    );

endmodule

`resetall
