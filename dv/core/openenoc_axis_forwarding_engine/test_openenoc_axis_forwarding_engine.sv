// SPDX-FileCopyrightText: 2026 Kerim Bavcic
// SPDX-License-Identifier: AGPL-3.0-or-later

`resetall
`timescale 1ns / 1ps
`default_nettype none

/*
 * AXI4-Stream forwarding engine testbench
 */
module test_openenoc_axis_forwarding_engine #
(
    /* verilator lint_off WIDTHTRUNC */
    parameter NUM_OF_INTERFACES = 8,
    parameter DATA_W = 8,
    parameter logic KEEP_EN = (DATA_W>8),
    parameter KEEP_W = ((DATA_W+7)/8),
    parameter logic STRB_EN = 1'b0,
    parameter logic LAST_EN = 1'b1,
    parameter logic ID_EN = 1'b1,
    parameter ID_W = 8,
    parameter logic DEST_EN = 1'b1,
    parameter DEST_W = 8,
    parameter logic USER_EN = 1'b1,
    parameter USER_W = NUM_OF_INTERFACES
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
    .ID_W(ID_W),
    .DEST_EN(DEST_EN),
    .DEST_W(DEST_W),
    .USER_EN(1'b0),
    .USER_W(1)
) s_axis();

taxi_axis_if #(
    .DATA_W(DATA_W),
    .KEEP_EN(KEEP_EN),
    .KEEP_W(KEEP_W),
    .STRB_EN(STRB_EN),
    .LAST_EN(LAST_EN),
    .ID_EN(ID_EN),
    .ID_W(ID_W),
    .DEST_EN(DEST_EN),
    .DEST_W(DEST_W),
    .USER_EN(USER_EN),
    .USER_W(USER_W)
) m_axis();

logic pause_request;
logic pause_done;

openenoc_lookup_if #(
    .NUM_OF_INTERFACES(NUM_OF_INTERFACES)
) lookup_if();

openenoc_learning_if #(
    .NUM_OF_INTERFACES(NUM_OF_INTERFACES)
) learning_if();

openenoc_axis_forwarding_engine #(
    .NUM_OF_INTERFACES(NUM_OF_INTERFACES)
)
uut (
    .clk(clk),
    .rst(rst),

    .pause_request(pause_request),
    .pause_done(pause_done),

    /*
     * AXI4-Stream input (sink)
     */
    .s_axis(s_axis),

    /*
     * AXI4-Stream output (source)
     */
    .m_axis(m_axis),

    /*
     * Lookup interface
     */
    .lookup_if(lookup_if),

    /*
     * Learning interface
     */
    .learning_if(learning_if)
);

endmodule

`resetall
