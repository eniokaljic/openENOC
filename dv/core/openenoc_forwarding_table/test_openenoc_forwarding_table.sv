// SPDX-FileCopyrightText: 2026 Kerim Bavcic
// SPDX-License-Identifier: AGPL-3.0-or-later

`resetall
`timescale 1ns / 1ps
`default_nettype none

/*
 * openENOC forwarding table testbench
 */
module test_openenoc_forwarding_table #
(
    parameter int NUM_OF_INTERFACES = 8,
    parameter int TABLE_DEPTH       = 32,
    localparam int ADDR_WIDTH       = $clog2(TABLE_DEPTH * 16)
)
();

    logic clk;
    logic rst;

    logic [NUM_OF_INTERFACES-1:0] default_forwarding;
    logic                         operation_mode;

    // CPU interface
    logic                  cpuif_req;
    logic [ADDR_WIDTH-1:0] cpuif_addr;
    logic                  cpuif_req_is_wr;
    logic [31:0]           cpuif_wr_data;
    logic [31:0]           cpuif_wr_biten;

    logic                  cpuif_wr_ack;
    logic                  cpuif_rd_ack;
    logic [31:0]           cpuif_rd_data;

    openenoc_lookup_if #(
        .NUM_OF_INTERFACES(NUM_OF_INTERFACES)
    ) lookup_if();

    openenoc_learning_if #(
        .NUM_OF_INTERFACES(NUM_OF_INTERFACES)
    ) learning_if();

    openenoc_forwarding_table #(
        .NUM_OF_INTERFACES(NUM_OF_INTERFACES),
        .TABLE_DEPTH(TABLE_DEPTH)
    )
    u_openenoc_forwarding_table (
        .clk(clk),
        .rst(rst),

        .default_forwarding(default_forwarding),
        .operation_mode(operation_mode),

        .cpuif_req(cpuif_req),
        .cpuif_addr(cpuif_addr),
        .cpuif_req_is_wr(cpuif_req_is_wr),
        .cpuif_wr_data(cpuif_wr_data),
        .cpuif_wr_biten(cpuif_wr_biten),

        .cpuif_wr_ack(cpuif_wr_ack),
        .cpuif_rd_ack(cpuif_rd_ack),
        .cpuif_rd_data(cpuif_rd_data),

        .lookup_if(lookup_if),
        .learning_if(learning_if)
    );

endmodule

`resetall
