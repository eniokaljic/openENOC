// SPDX-FileCopyrightText: 2021-2025 FPGA Ninja, LLC
// SPDX-FileCopyrightText: 2026 Enio Kaljic
// SPDX-License-Identifier: CERN-OHL-S-2.0

`resetall
`timescale 1ns / 1ps
`default_nettype none

/*
 * Combinational AXI4-Lite crossbar address decoder.
 */
module openenoc_axil_crossbar_addr #(
    parameter S = 0,
    parameter S_COUNT = 4,
    parameter M_COUNT = 4,
    parameter SELECT_W = M_COUNT > 1 ? $clog2(M_COUNT) : 1,
    parameter ADDR_W = 32,
    parameter M_REGIONS = 1,
    parameter M_BASE_ADDR = '0,
    parameter M_ADDR_W = {M_COUNT{{M_REGIONS{32'd24}}}},
    parameter M_CONNECT = {M_COUNT{{S_COUNT{1'b1}}}},
    parameter M_SECURE = {M_COUNT{1'b0}}
) (
    input  wire logic [ADDR_W-1:0]   addr,
    input  wire logic [2:0]          prot,
    output wire logic                match,
    output wire logic [SELECT_W-1:0] select
);

    localparam [M_COUNT*M_REGIONS-1:0][31:0] M_ADDR_W_INT = M_ADDR_W;
    localparam [M_COUNT-1:0][S_COUNT-1:0] M_CONNECT_INT = M_CONNECT;
    localparam [M_COUNT-1:0] M_SECURE_INT = M_SECURE;

    function automatic [M_COUNT*M_REGIONS-1:0][ADDR_W-1:0]
            calc_base_addrs(input logic unused);
        logic [ADDR_W-1:0] base;
        logic [ADDR_W-1:0] mask;
        logic [ADDR_W-1:0] size;
        integer width;
        begin
            calc_base_addrs = '0;
            base = '0;
            for (integer i = 0; i < M_COUNT*M_REGIONS; i = i + 1) begin
                width = M_ADDR_W_INT[i];
                mask = {ADDR_W{1'b1}} >> (ADDR_W-width);
                size = mask + 1'b1;
                if (width > 0) begin
                    if ((base & mask) != 0) begin
                        base = base + size - (base & mask);
                    end
                    calc_base_addrs[i] = base;
                    base = base + size;
                end
            end
        end
    endfunction

    localparam [M_COUNT*M_REGIONS-1:0][ADDR_W-1:0] M_BASE_ADDR_INT =
        M_BASE_ADDR != 0 ?
        (M_COUNT*M_REGIONS*ADDR_W)'(M_BASE_ADDR) : calc_base_addrs(1'b0);

    logic match_int;
    logic [SELECT_W-1:0] select_int;

    always_comb begin
        match_int = 1'b0;
        select_int = '0;

        for (integer m = 0; m < M_COUNT; m = m + 1) begin
            for (integer region = 0; region < M_REGIONS; region = region + 1) begin
                if (M_ADDR_W_INT[m*M_REGIONS+region] != 0 &&
                        M_CONNECT_INT[m][S] &&
                        (!M_SECURE_INT[m] || !prot[1]) &&
                        (addr >> M_ADDR_W_INT[m*M_REGIONS+region]) ==
                        (M_BASE_ADDR_INT[m*M_REGIONS+region] >>
                            M_ADDR_W_INT[m*M_REGIONS+region])) begin
                    match_int = 1'b1;
                    select_int = SELECT_W'(m);
                end
            end
        end
    end

    assign match = match_int;
    assign select = select_int;

endmodule

`resetall
