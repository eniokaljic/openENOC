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

// Lookup interface
logic        lookup_req;
logic [47:0] lookup_mac_addr;

logic                         lookup_ack;
logic [NUM_OF_INTERFACES-1:0] lookup_port_bitmap;

// Learning interface
logic                         learning_req;
logic [47:0]                  learning_mac_addr;
logic [NUM_OF_INTERFACES-1:0] learning_port_bitmap;

logic learning_ack;

openenoc_forwarding_table #(
    .NUM_OF_INTERFACES(NUM_OF_INTERFACES),
    .TABLE_DEPTH(TABLE_DEPTH)
)
uut (
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

    .lookup_req(lookup_req),
    .lookup_mac_addr(lookup_mac_addr),

    .lookup_ack(lookup_ack),
    .lookup_port_bitmap(lookup_port_bitmap),

    .learning_req(learning_req),
    .learning_mac_addr(learning_mac_addr),
    .learning_port_bitmap(learning_port_bitmap),

    .learning_ack(learning_ack)
);

endmodule

`resetall
