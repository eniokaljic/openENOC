// SPDX-FileCopyrightText: 2026 Enio Kaljic
// SPDX-License-Identifier: AGPL-3.0-or-later

`resetall
`timescale 1ns / 1ps
`default_nettype none

/*
 * Scalar test wrapper for the openENOC endpoint interrupt controller
 */
module test_openenoc_endpoint_irq_controller #(
    parameter int EVENT_PORTS = 4,
    parameter int FIFO_DEPTH = 4,
    parameter int PEER_IDX_W = 5,
    parameter int SEQUENCE_W = 4
) ();

    logic clk;
    logic rst;

    logic                        global_enable;
    logic [4:0]                  event_enable;
    logic                        clear_errors;
    wire                         clear_errors_hwclr;

    logic                        complete_valid;
    logic [PEER_IDX_W-1:0]       complete_peer_idx;
    logic [3:0]                  complete_source;
    logic [SEQUENCE_W-1:0]       complete_sequence;
    wire                         complete_valid_hwclr;

    wire                         claim_valid;
    wire [PEER_IDX_W-1:0]        claim_peer_idx;
    wire [3:0]                   claim_source;
    wire [SEQUENCE_W-1:0]        claim_sequence;

    wire                         claim_pending;
    wire                         credit_full;
    wire                         overflow;
    wire                         invalid_complete;
    wire                         irq_asserted;
    wire [7:0]                   fifo_level;
    wire [7:0]                   reserved_count;
    wire                         irq;

    logic [EVENT_PORTS-1:0]      admit_valid;
    wire  [EVENT_PORTS-1:0]      admit_ready;
    logic [EVENT_PORTS*4-1:0]    admit_source;
    logic [EVENT_PORTS-1:0]      admit_enable;
    wire  [EVENT_PORTS-1:0]      admit_reserved;

    logic [EVENT_PORTS-1:0]      commit_valid;
    wire  [EVENT_PORTS-1:0]      commit_ready;
    logic [EVENT_PORTS*4-1:0]    commit_source;
    logic [EVENT_PORTS*PEER_IDX_W-1:0] commit_peer_idx;

    openenoc_irq_event_if #(
        .PEER_IDX_W(PEER_IDX_W)
    ) event_if[EVENT_PORTS]();

    for (genvar n = 0; n < EVENT_PORTS; n++) begin : g_bridge
        assign event_if[n].admit_valid = admit_valid[n];
        assign event_if[n].admit_source = admit_source[n*4 +: 4];
        assign event_if[n].admit_enable = admit_enable[n];
        assign admit_ready[n] = event_if[n].admit_ready;
        assign admit_reserved[n] = event_if[n].admit_reserved;

        assign event_if[n].commit_valid = commit_valid[n];
        assign event_if[n].commit_source = commit_source[n*4 +: 4];
        assign event_if[n].commit_peer_idx =
            commit_peer_idx[n*PEER_IDX_W +: PEER_IDX_W];
        assign commit_ready[n] = event_if[n].commit_ready;
    end

    openenoc_endpoint_irq_controller #(
        .EVENT_PORTS(EVENT_PORTS),
        .FIFO_DEPTH(FIFO_DEPTH),
        .PEER_IDX_W(PEER_IDX_W),
        .SEQUENCE_W(SEQUENCE_W)
    ) dut (
        .clk(clk),
        .rst(rst),

        .global_enable(global_enable),
        .event_enable(event_enable),
        .clear_errors(clear_errors),
        .clear_errors_hwclr(clear_errors_hwclr),

        .complete_valid(complete_valid),
        .complete_peer_idx(complete_peer_idx),
        .complete_source(complete_source),
        .complete_sequence(complete_sequence),
        .complete_valid_hwclr(complete_valid_hwclr),

        .claim_valid(claim_valid),
        .claim_peer_idx(claim_peer_idx),
        .claim_source(claim_source),
        .claim_sequence(claim_sequence),

        .claim_pending(claim_pending),
        .credit_full(credit_full),
        .overflow(overflow),
        .invalid_complete(invalid_complete),
        .irq_asserted(irq_asserted),
        .fifo_level(fifo_level),
        .reserved_count(reserved_count),
        .irq(irq),

        .event_if(event_if)
    );

endmodule

`resetall
