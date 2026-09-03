// SPDX-FileCopyrightText: 2026 Enio Kaljic
// SPDX-License-Identifier: CERN-OHL-S-2.0

`resetall
`timescale 1ns / 1ps
`default_nettype none

interface openenoc_eth_if #
(
    // Width of AXI stream interfaces in bits
    parameter DATA_W = 32,
    // tkeep signal width (bytes per cycle)
    parameter KEEP_W = ((DATA_W+7)/8),
    // Use tkeep signal
    parameter logic KEEP_EN = KEEP_W > 1,
    // Use tstrb signal
    parameter logic STRB_EN = 1'b0,
    // Use tlast signal
    parameter logic LAST_EN = 1'b1,
    // Use tid signal
    parameter logic ID_EN = 1'b0,
    // tid signal width
    parameter ID_W = 8,
    // Use tdest signal
    parameter logic DEST_EN = 1'b0,
    // tdest signal width
    parameter DEST_W = 8,
    // Use tuser signal
    parameter logic USER_EN = 1'b0,
    // tuser signal width
    parameter USER_W = 1
)
(
    input wire logic clk,
    input wire logic rst
);
    /*
     * Symmetric bidirectional Ethernet-like openENOC link.
     *
     * Direction a2b_axis_if:
     *   side A drives taxi_axis_if.src
     *   side B drives taxi_axis_if.snk
     *
     * Direction b2a_axis_if:
     *   side B drives taxi_axis_if.src
     *   side A drives taxi_axis_if.snk
     */

    taxi_axis_if #(
        .DATA_W  (DATA_W),
        .KEEP_W  (KEEP_W),
        .KEEP_EN (KEEP_EN),
        .STRB_EN (STRB_EN),
        .LAST_EN (LAST_EN),
        .ID_EN   (ID_EN),
        .ID_W    (ID_W),
        .DEST_EN (DEST_EN),
        .DEST_W  (DEST_W),
        .USER_EN (USER_EN),
        .USER_W  (USER_W)
    ) a2b_axis_if();

    taxi_axis_if #(
        .DATA_W  (DATA_W),
        .KEEP_W  (KEEP_W),
        .KEEP_EN (KEEP_EN),
        .STRB_EN (STRB_EN),
        .LAST_EN (LAST_EN),
        .ID_EN   (ID_EN),
        .ID_W    (ID_W),
        .DEST_EN (DEST_EN),
        .DEST_W  (DEST_W),
        .USER_EN (USER_EN),
        .USER_W  (USER_W)
    ) b2a_axis_if();

endinterface

`resetall
