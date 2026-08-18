// SPDX-FileCopyrightText: 2026 Enio Kaljic
// SPDX-License-Identifier: CERN-OHL-S-2.0

`resetall
`timescale 1ns / 1ps
`default_nettype none

/*
 * Control and status interface for an openENOC Switch
 */
interface openenoc_switch_if #
(
    parameter int NUM_OF_INTERFACES = 8,
    parameter int TABLE_DEPTH       = 32,

    // Must match the forwarding table layout defined in SystemRDL
    localparam int TABLE_ENTRY_BYTES = 16,
    localparam int TABLE_ADDR_W = $clog2(TABLE_DEPTH * TABLE_ENTRY_BYTES)
)
(
    input wire logic clk,
    input wire logic rst
);

    /*
     * Forwarding control and status
     */
    logic                         operation_mode;
    logic                         pause_request;
    logic                         pause_done;
    logic [NUM_OF_INTERFACES-1:0] default_forwarding;

    /*
     * CSR access to the external forwarding table
     */
    logic                    table_req;
    logic [TABLE_ADDR_W-1:0] table_addr;
    logic                    table_req_is_wr;
    logic [31:0]             table_wr_data;
    logic [31:0]             table_wr_biten;

    logic                    table_wr_ack;
    logic                    table_rd_ack;
    logic [31:0]             table_rd_data;

    /*
     * Generated CSR block or CSR adapter side
     */
    modport csr (
        input  clk,
        input  rst,

        output operation_mode,
        output pause_request,
        output default_forwarding,

        input  pause_done,

        output table_req,
        output table_addr,
        output table_req_is_wr,
        output table_wr_data,
        output table_wr_biten,

        input  table_wr_ack,
        input  table_rd_ack,
        input  table_rd_data
    );

    /*
     * Switch implementation side
     */
    modport core (
        input  clk,
        input  rst,

        input  operation_mode,
        input  pause_request,
        input  default_forwarding,

        output pause_done,

        input  table_req,
        input  table_addr,
        input  table_req_is_wr,
        input  table_wr_data,
        input  table_wr_biten,

        output table_wr_ack,
        output table_rd_ack,
        output table_rd_data
    );

endinterface

`resetall
