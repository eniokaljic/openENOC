// SPDX-FileCopyrightText: 2026 Kerim Bavcic
// SPDX-License-Identifier: AGPL-3.0-or-later

`resetall
`timescale 1ns / 1ps
`default_nettype none

/*
 * Round-robin arbiter testbench
 */
module test_openenoc_rr_arbiter #
(
    parameter int PORTS = 4,
    parameter int INDEX_W = PORTS > 1 ? $clog2(PORTS) : 1
)
();
    logic clk;
    logic rst;
    logic [PORTS-1:0] request;
    logic accept;
    wire [PORTS-1:0] grant;
    wire grant_valid;
    wire [INDEX_W-1:0] grant_index;

    openenoc_rr_arbiter #(
        .PORTS(PORTS),
        .INDEX_W(INDEX_W)
    )
    u_openenoc_rr_arbiter (
        .clk(clk),
        .rst(rst),
        .request(request),
        .accept(accept),
        .grant(grant),
        .grant_valid(grant_valid),
        .grant_index(grant_index)
    );
endmodule

`resetall
