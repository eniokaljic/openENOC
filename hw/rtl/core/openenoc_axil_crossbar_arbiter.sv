// SPDX-FileCopyrightText: 2014-2025 FPGA Ninja, LLC
// SPDX-FileCopyrightText: 2026 Enio Kaljic
// SPDX-License-Identifier: CERN-OHL-S-2.0

`resetall
`timescale 1ns / 1ps
`default_nettype none

/*
 * Bubble-free combinational round-robin arbiter.
 *
 * The grant is selected combinationally from the current requests.  Only the
 * round-robin pointer is registered, so a completed grant can be followed by
 * another grant on the next clock cycle without an empty arbitration cycle.
 */
module openenoc_axil_crossbar_arbiter #(
    parameter PORTS = 2,
    parameter INDEX_W = PORTS > 1 ? $clog2(PORTS) : 1
) (
    input  wire logic               clk,
    input  wire logic               rst,
    input  wire logic [PORTS-1:0]   request,
    input  wire logic               accept,
    output wire logic [PORTS-1:0]   grant,
    output wire logic               grant_valid,
    output wire logic [INDEX_W-1:0] grant_index
);

    logic [INDEX_W-1:0] pointer_reg;
    logic [PORTS-1:0] grant_int;
    logic grant_valid_int;
    logic [INDEX_W-1:0] grant_index_int;

    always_comb begin
        grant_int = '0;
        grant_valid_int = 1'b0;
        grant_index_int = pointer_reg;

        for (integer offset = 0; offset < PORTS; offset = offset + 1) begin
            integer candidate;
            candidate = int'(pointer_reg);
            candidate = candidate + offset;
            if (candidate >= PORTS) begin
                candidate = candidate - PORTS;
            end

            if (!grant_valid_int && request[candidate]) begin
                grant_int[candidate] = 1'b1;
                grant_valid_int = 1'b1;
                grant_index_int = INDEX_W'(candidate);
            end
        end
    end

    assign grant = grant_int;
    assign grant_valid = grant_valid_int;
    assign grant_index = grant_index_int;

    always_ff @(posedge clk) begin
        if (rst) begin
            pointer_reg <= '0;
        end else if (accept && grant_valid_int) begin
            if (grant_index_int == INDEX_W'(PORTS-1)) begin
                pointer_reg <= '0;
            end else begin
                pointer_reg <= grant_index_int + 1'b1;
            end
        end
    end

endmodule

`resetall
