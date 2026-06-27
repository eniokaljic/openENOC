// SPDX-FileCopyrightText: 2026 Enio Kaljic
// SPDX-License-Identifier: AGPL-3.0-or-later

`resetall
`timescale 1ns / 1ps
`default_nettype none

/*
 * openENOC Ethernet adapter testbench
 */
module test_openenoc_eth_adapter #
(
    /* verilator lint_off WIDTHTRUNC */

    /*
     * Side A AXI4-Stream configuration
     */
    parameter A_DATA_W = 8,
    parameter A_KEEP_W = ((A_DATA_W+7)/8),
    parameter logic A_KEEP_EN = A_KEEP_W > 1,
    parameter logic A_STRB_EN = 1'b0,
    parameter logic A_LAST_EN = 1'b1,
    parameter logic A_ID_EN = 1'b0,
    parameter A_ID_W = 8,
    parameter logic A_DEST_EN = 1'b0,
    parameter A_DEST_W = 8,
    parameter logic A_USER_EN = 1'b0,
    parameter A_USER_W = 1,

    /*
     * Side B AXI4-Stream configuration
     */
    parameter B_DATA_W = 8,
    parameter B_KEEP_W = ((B_DATA_W+7)/8),
    parameter logic B_KEEP_EN = B_KEEP_W > 1,
    parameter logic B_STRB_EN = 1'b0,
    parameter logic B_LAST_EN = 1'b1,
    parameter logic B_ID_EN = 1'b0,
    parameter B_ID_W = 8,
    parameter logic B_DEST_EN = 1'b0,
    parameter B_DEST_W = 8,
    parameter logic B_USER_EN = 1'b0,
    parameter B_USER_W = 1,

    /*
     * FIFO configuration
     */
    parameter DEPTH = 4096,
    parameter RAM_PIPELINE = 1,
    parameter logic OUTPUT_FIFO_EN = 1'b0,
    parameter logic FRAME_FIFO = 1'b0,
    parameter USER_BAD_FRAME_VALUE = 1'b1,
    parameter USER_BAD_FRAME_MASK = 1'b1,
    parameter logic DROP_OVERSIZE_FRAME = FRAME_FIFO,
    parameter logic DROP_BAD_FRAME = 1'b0,
    parameter logic DROP_WHEN_FULL = 1'b0,
    parameter logic MARK_WHEN_FULL = 1'b0,
    parameter logic FRAME_PAUSE = FRAME_FIFO

    /* verilator lint_on WIDTHTRUNC */
)
();
    logic clk_a;
    logic rst_a;

    logic clk_b;
    logic rst_b;

    /*
    * Side A openENOC Ethernet-like interface
    */
    openenoc_eth_if #(
        .DATA_W  (A_DATA_W),
        .KEEP_W  (A_KEEP_W),
        .KEEP_EN (A_KEEP_EN),
        .STRB_EN (A_STRB_EN),
        .LAST_EN (A_LAST_EN),
        .ID_EN   (A_ID_EN),
        .ID_W    (A_ID_W),
        .DEST_EN (A_DEST_EN),
        .DEST_W  (A_DEST_W),
        .USER_EN (A_USER_EN),
        .USER_W  (A_USER_W)
    ) eth_a(.clk(clk_a), .rst(rst_a));

    /*
    * Side B openENOC Ethernet-like interface
    */
    openenoc_eth_if #(
        .DATA_W  (B_DATA_W),
        .KEEP_W  (B_KEEP_W),
        .KEEP_EN (B_KEEP_EN),
        .STRB_EN (B_STRB_EN),
        .LAST_EN (B_LAST_EN),
        .ID_EN   (B_ID_EN),
        .ID_W    (B_ID_W),
        .DEST_EN (B_DEST_EN),
        .DEST_W  (B_DEST_W),
        .USER_EN (B_USER_EN),
        .USER_W  (B_USER_W)
    ) eth_b(.clk(clk_b), .rst(rst_b));

    openenoc_eth_adapter #(
        .DEPTH                  (DEPTH),
        .RAM_PIPELINE           (RAM_PIPELINE),
        .OUTPUT_FIFO_EN         (OUTPUT_FIFO_EN),
        .FRAME_FIFO             (FRAME_FIFO),
        .USER_BAD_FRAME_VALUE   (USER_BAD_FRAME_VALUE),
        .USER_BAD_FRAME_MASK    (USER_BAD_FRAME_MASK),
        .DROP_OVERSIZE_FRAME    (DROP_OVERSIZE_FRAME),
        .DROP_BAD_FRAME         (DROP_BAD_FRAME),
        .DROP_WHEN_FULL         (DROP_WHEN_FULL),
        .MARK_WHEN_FULL         (MARK_WHEN_FULL),
        .FRAME_PAUSE            (FRAME_PAUSE)
    )
    uut (
        /*
        * Ethernet-like openENOC link, side A clock domain
        */
        .eth_a (eth_a),

        /*
        * Ethernet-like openENOC link, side B clock domain
        */
        .eth_b (eth_b)
    );

endmodule

`resetall
