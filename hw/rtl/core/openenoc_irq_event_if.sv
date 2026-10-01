// SPDX-FileCopyrightText: 2026 Enio Kaljic
// SPDX-License-Identifier: CERN-OHL-S-2.0

`resetall
`timescale 1ns / 1ps
`default_nettype none

/*
 * openENOC endpoint IRQ event producer interface
 *
 * The admission channel is used when an operation is accepted. The controller
 * combines admit_source with its event-enable state and admit_enable from the
 * producer. It accepts disabled events without reserving a credit and reports
 * the result through admit_reserved during the admission handshake.
 *
 * A producer must retain admit_reserved with the operation context. Every
 * operation with a reservation eventually submits exactly one commit. Commit
 * fields remain stable until the controller accepts them.
 */
interface openenoc_irq_event_if #(
    parameter int unsigned PEER_IDX_W = 1
);
    localparam logic [3:0] EVENT_PEER_DMA_COMPLETE            = 4'd0;
    localparam logic [3:0] EVENT_NON_OETP_DMA_TX_COMPLETE     = 4'd1;
    localparam logic [3:0] EVENT_NON_OETP_DMA_RX_COMPLETE     = 4'd2;
    localparam logic [3:0] EVENT_NON_OETP_DIRECT_TX_COMPLETE  = 4'd3;
    localparam logic [3:0] EVENT_NON_OETP_DIRECT_RX_AVAILABLE = 4'd4;

    /* Operation admission and credit reservation */
    logic                      admit_valid;
    logic                      admit_ready;
    logic [3:0]                admit_source;
    logic                      admit_enable;
    logic                      admit_reserved;

    /* Reserved event commit */
    logic                      commit_valid;
    logic                      commit_ready;
    logic [3:0]                commit_source;
    logic [PEER_IDX_W-1:0]     commit_peer_idx;

    modport producer (
        output admit_valid,
        input  admit_ready,
        output admit_source,
        output admit_enable,
        input  admit_reserved,

        output commit_valid,
        input  commit_ready,
        output commit_source,
        output commit_peer_idx
    );

    modport controller (
        input  admit_valid,
        output admit_ready,
        input  admit_source,
        input  admit_enable,
        output admit_reserved,

        input  commit_valid,
        output commit_ready,
        input  commit_source,
        input  commit_peer_idx
    );

    modport mon (
        input admit_valid,
        input admit_ready,
        input admit_source,
        input admit_enable,
        input admit_reserved,
        input commit_valid,
        input commit_ready,
        input commit_source,
        input commit_peer_idx
    );

endinterface

`resetall
