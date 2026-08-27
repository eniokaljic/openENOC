// SPDX-FileCopyrightText: 2021-2025 FPGA Ninja, LLC
// SPDX-FileCopyrightText: 2026 Enio Kaljic
// SPDX-License-Identifier: CERN-OHL-S-2.0

`resetall
`timescale 1ns / 1ps
`default_nettype none

/*
 * Bubble-free pipelined AXI4-Lite crossbar.
 */
module openenoc_axil_crossbar #(
    parameter S_COUNT = 4,
    parameter M_COUNT = 4,
    parameter ADDR_W = 32,
    parameter S_ACCEPT = {S_COUNT{32'd16}},
    parameter M_REGIONS = 1,
    parameter M_BASE_ADDR = '0,
    parameter M_ADDR_W = {M_COUNT{{M_REGIONS{32'd24}}}},
    parameter M_CONNECT_RD = {M_COUNT{{S_COUNT{1'b1}}}},
    parameter M_CONNECT_WR = {M_COUNT{{S_COUNT{1'b1}}}},
    parameter M_ISSUE = {M_COUNT{32'd16}},
    parameter M_SECURE = {M_COUNT{1'b0}}
) (
    input  wire logic    clk,
    input  wire logic    rst,
    taxi_axil_if.wr_slv  s_axil_wr[S_COUNT],
    taxi_axil_if.rd_slv  s_axil_rd[S_COUNT],
    taxi_axil_if.wr_mst  m_axil_wr[M_COUNT],
    taxi_axil_if.rd_mst  m_axil_rd[M_COUNT]
);

    localparam DATA_W = s_axil_wr[0].DATA_W;
    localparam STRB_W = s_axil_wr[0].STRB_W;
    localparam [M_COUNT*M_REGIONS-1:0][31:0] M_ADDR_W_INT = M_ADDR_W;

    initial begin
        if (S_COUNT < 1 || M_COUNT < 1 || M_REGIONS < 1) begin
            $fatal(0, "Error: crossbar dimensions must be positive (instance %m)");
        end
        if (s_axil_rd[0].DATA_W != DATA_W ||
                s_axil_rd[0].STRB_W != STRB_W) begin
            $fatal(0, "Error: read and write interface widths differ (instance %m)");
        end
        if (s_axil_wr[0].ADDR_W != ADDR_W ||
                s_axil_rd[0].ADDR_W != ADDR_W) begin
            $fatal(0, "Error: AXI address width mismatch (instance %m)");
        end
        for (integer i = 0; i < M_COUNT*M_REGIONS; i = i + 1) begin
            if (M_ADDR_W_INT[i] != 0 &&
                    (M_ADDR_W_INT[i] < $clog2(STRB_W) ||
                        M_ADDR_W_INT[i] > ADDR_W)) begin
                $fatal(0, "Error: target address width is out of range (instance %m)");
            end
        end
    end

    openenoc_axil_crossbar_wr #(
        .S_COUNT(S_COUNT),
        .M_COUNT(M_COUNT),
        .ADDR_W(ADDR_W),
        .S_ACCEPT(S_ACCEPT),
        .M_REGIONS(M_REGIONS),
        .M_BASE_ADDR(M_BASE_ADDR),
        .M_ADDR_W(M_ADDR_W),
        .M_CONNECT(M_CONNECT_WR),
        .M_ISSUE(M_ISSUE),
        .M_SECURE(M_SECURE)
    ) wr_inst (
        .clk(clk),
        .rst(rst),
        .s_axil_wr(s_axil_wr),
        .m_axil_wr(m_axil_wr)
    );

    openenoc_axil_crossbar_rd #(
        .S_COUNT(S_COUNT),
        .M_COUNT(M_COUNT),
        .ADDR_W(ADDR_W),
        .S_ACCEPT(S_ACCEPT),
        .M_REGIONS(M_REGIONS),
        .M_BASE_ADDR(M_BASE_ADDR),
        .M_ADDR_W(M_ADDR_W),
        .M_CONNECT(M_CONNECT_RD),
        .M_ISSUE(M_ISSUE),
        .M_SECURE(M_SECURE)
    ) rd_inst (
        .clk(clk),
        .rst(rst),
        .s_axil_rd(s_axil_rd),
        .m_axil_rd(m_axil_rd)
    );

endmodule

`resetall
