// SPDX-FileCopyrightText: 2026 Enio Kaljic
// SPDX-License-Identifier: AGPL-3.0-or-later

`resetall
`timescale 1ns / 1ps
`default_nettype none

/*
 * Isolated native CPUIF to AXI4-Lite adapter testbench
 */
module test_openenoc_cpuif_axil_adapter #(
    parameter int DATA_W = 32,
    parameter int ADDR_W = 32
) ();

    logic clk;
    logic rst;

    openenoc_cpuif_if #(
        .ADDR_W(ADDR_W),
        .DATA_W(DATA_W)
    ) cpuif();

    taxi_axil_if #(
        .DATA_W(DATA_W),
        .ADDR_W(ADDR_W),
        .STRB_W(DATA_W/8)
    ) axil();

    openenoc_cpuif_axil_adapter dut (
        .clk(clk),
        .rst(rst),
        .s_cpuif(cpuif),
        .m_axil_wr(axil),
        .m_axil_rd(axil)
    );

endmodule

`resetall
