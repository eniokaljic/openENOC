// SPDX-FileCopyrightText: 2018-2025 FPGA Ninja, LLC
// SPDX-FileCopyrightText: 2026 Enio Kaljic
// SPDX-License-Identifier: CERN-OHL-S-2.0

`resetall
`timescale 1ns / 1ps
`default_nettype none

/*
 * Two-entry elastic buffer with registered input READY.
 *
 * The buffer can accept and emit one transfer per clock cycle after the
 * initial fill.  The temporary register absorbs one transfer when downstream
 * backpressure arrives too late to withdraw the registered input READY.
 */
module openenoc_axil_crossbar_skid_buffer #(
    parameter DATA_W = 1
) (
    input  wire logic              clk,
    input  wire logic              rst,

    input  wire logic [DATA_W-1:0] s_data,
    input  wire logic              s_valid,
    output wire logic              s_ready,

    output wire logic [DATA_W-1:0] m_data,
    output wire logic              m_valid,
    input  wire logic              m_ready
);

    logic [DATA_W-1:0] output_data_reg;
    logic output_valid_reg;
    logic [DATA_W-1:0] temp_data_reg;
    logic temp_valid_reg;
    logic input_ready_reg;

    logic output_valid_next;
    logic temp_valid_next;
    logic store_input_to_output;
    logic store_input_to_temp;
    logic store_temp_to_output;

    wire logic input_ready_early = m_ready ||
        (!temp_valid_reg && (!output_valid_reg || !s_valid));

    assign s_ready = input_ready_reg;
    assign m_data = output_data_reg;
    assign m_valid = output_valid_reg;

    always_comb begin
        output_valid_next = output_valid_reg;
        temp_valid_next = temp_valid_reg;

        store_input_to_output = 1'b0;
        store_input_to_temp = 1'b0;
        store_temp_to_output = 1'b0;

        if (input_ready_reg) begin
            if (m_ready || !output_valid_reg) begin
                output_valid_next = s_valid;
                store_input_to_output = 1'b1;
            end else begin
                temp_valid_next = s_valid;
                store_input_to_temp = 1'b1;
            end
        end else if (m_ready) begin
            output_valid_next = temp_valid_reg;
            temp_valid_next = 1'b0;
            store_temp_to_output = 1'b1;
        end
    end

    always_ff @(posedge clk) begin
        input_ready_reg <= input_ready_early;
        output_valid_reg <= output_valid_next;
        temp_valid_reg <= temp_valid_next;

        if (store_input_to_output) begin
            output_data_reg <= s_data;
        end else if (store_temp_to_output) begin
            output_data_reg <= temp_data_reg;
        end

        if (store_input_to_temp) begin
            temp_data_reg <= s_data;
        end

        if (rst) begin
            input_ready_reg <= 1'b0;
            output_valid_reg <= 1'b0;
            temp_valid_reg <= 1'b0;
        end
    end

endmodule

`resetall
