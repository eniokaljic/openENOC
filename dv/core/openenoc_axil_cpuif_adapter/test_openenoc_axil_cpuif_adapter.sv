// SPDX-FileCopyrightText: 2026 Enio Kaljic
// SPDX-License-Identifier: AGPL-3.0-or-later

`resetall
`timescale 1ns / 1ps
`default_nettype none

/*
 * Isolated AXI4-Lite to native CPUIF adapter testbench
 */
module test_openenoc_axil_cpuif_adapter #(
    parameter int DATA_W = 32,
    parameter int ADDR_W = 32,
    parameter int RESPONSE_FIFO_DEPTH = 2
) ();

    logic clk;
    logic rst;

    taxi_axil_if #(
        .DATA_W(DATA_W),
        .ADDR_W(ADDR_W),
        .STRB_W(DATA_W/8)
    ) axil();

    openenoc_cpuif_if #(
        .ADDR_W(ADDR_W),
        .DATA_W(DATA_W)
    ) cpuif();

    openenoc_axil_cpuif_adapter #(
        .RESPONSE_FIFO_DEPTH(RESPONSE_FIFO_DEPTH)
    ) dut (
        .clk(clk),
        .rst(rst),
        .s_axil_wr(axil),
        .s_axil_rd(axil),
        .m_cpuif(cpuif)
    );

endmodule

`resetall
