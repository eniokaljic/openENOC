// SPDX-FileCopyrightText: 2026 Enio Kaljic
// SPDX-License-Identifier: CERN-OHL-S-2.0

`resetall
`timescale 1ns / 1ps
`default_nettype none

/*
 * openENOC endpoint interrupt controller
 *
 * Enabled operations reserve a FIFO credit through the admission channel
 * before they start. A later commit converts one reservation into a queued
 * claim without changing the total number of occupied credits. Disabled
 * operations are admitted immediately with admit_reserved clear.
 *
 * At most one enabled admission and one commit are accepted per cycle. Both
 * channels use independent round-robin arbiters. A matching completion removes
 * the claim at the FIFO head; an invalid completion leaves the FIFO unchanged.
 */
module openenoc_endpoint_irq_controller #(
    parameter int EVENT_PORTS = 5,
    parameter int FIFO_DEPTH = 16,
    parameter int PEER_IDX_W = 1,
    parameter int SEQUENCE_W = 16
) (
    input  wire logic                       clk,
    input  wire logic                       rst,

    input  wire logic                       global_enable,
    input  wire logic [4:0]                 event_enable,
    input  wire logic                       clear_errors,
    output wire logic                       clear_errors_hwclr,

    input  wire logic                       complete_valid,
    input  wire logic [PEER_IDX_W-1:0]      complete_peer_idx,
    input  wire logic [3:0]                 complete_source,
    input  wire logic [SEQUENCE_W-1:0]      complete_sequence,
    output wire logic                       complete_valid_hwclr,

    output wire logic                       claim_valid,
    output wire logic [PEER_IDX_W-1:0]      claim_peer_idx,
    output wire logic [3:0]                 claim_source,
    output wire logic [SEQUENCE_W-1:0]      claim_sequence,

    output wire logic                       claim_pending,
    output wire logic                       credit_full,
    output wire logic                       overflow,
    output wire logic                       invalid_complete,
    output wire logic                       irq_asserted,
    output wire logic [7:0]                 fifo_level,
    output wire logic [7:0]                 reserved_count,
    output wire logic                       irq,

    openenoc_irq_event_if.controller        event_if[EVENT_PORTS]
);

    localparam int PORT_INDEX_W = EVENT_PORTS > 1 ? $clog2(EVENT_PORTS) : 1;
    localparam int FIFO_COUNT_W = $clog2(FIFO_DEPTH+1);
    localparam int OCCUPIED_COUNT_W = FIFO_COUNT_W + 1;
    localparam int CLAIM_DATA_W = PEER_IDX_W + 4 + SEQUENCE_W;
    localparam int TAXI_FIFO_DEPTH = FIFO_DEPTH > 1 ? FIFO_DEPTH : 2;
    localparam logic [3:0] EVENT_PEER_DMA_COMPLETE =
        event_if[0].EVENT_PEER_DMA_COMPLETE;
    localparam logic [3:0] EVENT_NON_OETP_DMA_TX_COMPLETE =
        event_if[0].EVENT_NON_OETP_DMA_TX_COMPLETE;
    localparam logic [3:0] EVENT_NON_OETP_DMA_RX_COMPLETE =
        event_if[0].EVENT_NON_OETP_DMA_RX_COMPLETE;
    localparam logic [3:0] EVENT_NON_OETP_DIRECT_TX_COMPLETE =
        event_if[0].EVENT_NON_OETP_DIRECT_TX_COMPLETE;
    localparam logic [3:0] EVENT_NON_OETP_DIRECT_RX_AVAILABLE =
        event_if[0].EVENT_NON_OETP_DIRECT_RX_AVAILABLE;

    // check configuration
    /* verilator lint_off GENUNNAMED */
    if (EVENT_PORTS < 1)
        $fatal(0, "Error: EVENT_PORTS must be at least 1 (instance %m)");
    if (FIFO_DEPTH < 1)
        $fatal(0, "Error: FIFO_DEPTH must be at least 1 (instance %m)");
    if (PEER_IDX_W < 1)
        $fatal(0, "Error: PEER_IDX_W must be at least 1 (instance %m)");
    if (SEQUENCE_W < 1)
        $fatal(0, "Error: SEQUENCE_W must be at least 1 (instance %m)");
    /* verilator lint_on GENUNNAMED */

    function automatic logic source_is_enabled(
        input logic [3:0] source,
        input logic [4:0] enables
    );
        case (source)
            EVENT_PEER_DMA_COMPLETE:
                source_is_enabled = enables[0];
            EVENT_NON_OETP_DMA_TX_COMPLETE:
                source_is_enabled = enables[1];
            EVENT_NON_OETP_DMA_RX_COMPLETE:
                source_is_enabled = enables[2];
            EVENT_NON_OETP_DIRECT_TX_COMPLETE:
                source_is_enabled = enables[3];
            EVENT_NON_OETP_DIRECT_RX_AVAILABLE:
                source_is_enabled = enables[4];
            default: source_is_enabled = 1'b0;
        endcase
    endfunction

    logic [FIFO_COUNT_W-1:0] fifo_count_reg;
    logic [FIFO_COUNT_W-1:0] reserved_count_reg;
    logic [FIFO_COUNT_W-1:0] port_reserved_count_reg[EVENT_PORTS];
    logic [SEQUENCE_W-1:0]   next_sequence_reg;
    logic                    overflow_reg;
    logic                    invalid_complete_reg;

    taxi_axis_if #(
        .DATA_W(CLAIM_DATA_W),
        .KEEP_W(1),
        .KEEP_EN(1'b0),
        .STRB_EN(1'b0),
        .LAST_EN(1'b0),
        .ID_EN(1'b0),
        .DEST_EN(1'b0),
        .USER_EN(1'b0)
    ) claim_fifo_s_axis(), claim_fifo_m_axis();

    wire [OCCUPIED_COUNT_W-1:0] occupied_count =
        OCCUPIED_COUNT_W'(fifo_count_reg) + OCCUPIED_COUNT_W'(reserved_count_reg);

    wire complete_match = !rst && complete_valid && claim_valid &&
        complete_peer_idx == claim_peer_idx &&
        complete_source == claim_source &&
        complete_sequence == claim_sequence;
    wire claim_pop = complete_match;

    // A completion at the active edge releases a credit that an admission on
    // that same edge may reserve.
    wire credit_available = occupied_count < OCCUPIED_COUNT_W'(FIFO_DEPTH) || claim_pop;

    wire [EVENT_PORTS-1:0] admit_request;
    wire [EVENT_PORTS-1:0] admit_grant;
    wire                   admit_grant_valid;
    wire                   admit_accept = !rst && credit_available && admit_grant_valid;

    openenoc_rr_arbiter #(
        .PORTS(EVENT_PORTS),
        .INDEX_W(PORT_INDEX_W)
    ) u_admit_arbiter (
        .clk(clk),
        .rst(rst),
        .request(admit_request),
        .accept(admit_accept),
        .grant(admit_grant),
        .grant_valid(admit_grant_valid),
        .grant_index()
    );

    wire [EVENT_PORTS-1:0] commit_request;
    wire [EVENT_PORTS-1:0] commit_grant;
    wire                   commit_grant_valid;
    wire                   commit_accept = !rst && commit_grant_valid;

    openenoc_rr_arbiter #(
        .PORTS(EVENT_PORTS),
        .INDEX_W(PORT_INDEX_W)
    ) u_commit_arbiter (
        .clk(clk),
        .rst(rst),
        .request(commit_request),
        .accept(commit_accept),
        .grant(commit_grant),
        .grant_valid(commit_grant_valid),
        .grant_index()
    );

    wire [3:0]            commit_source[EVENT_PORTS];
    wire [PEER_IDX_W-1:0] commit_peer_idx[EVENT_PORTS];

    for (genvar n = 0; n < EVENT_PORTS; n++) begin : g_event_port
        /* verilator lint_off GENUNNAMED */
        if (event_if[n].PEER_IDX_W != PEER_IDX_W)
            $fatal(0, "Error: event interface parameter mismatch (instance %m)");
        /* verilator lint_on GENUNNAMED */

        assign admit_request[n] = event_if[n].admit_valid && event_if[n].admit_enable &&
            source_is_enabled(event_if[n].admit_source, event_enable);
        assign event_if[n].admit_ready = !rst &&
            (!admit_request[n] || (credit_available && admit_grant[n]));
        assign event_if[n].admit_reserved = event_if[n].admit_valid &&
            event_if[n].admit_ready && admit_request[n];

        assign commit_request[n] = event_if[n].commit_valid;
        assign event_if[n].commit_ready = !rst && commit_grant[n];
        assign commit_source[n] = event_if[n].commit_source;
        assign commit_peer_idx[n] = event_if[n].commit_peer_idx;
    end

    logic [3:0]            selected_commit_source;
    logic [PEER_IDX_W-1:0] selected_commit_peer_idx;
    logic                  selected_commit_has_reservation;

    always_comb begin
        selected_commit_source = '0;
        selected_commit_peer_idx = '0;
        selected_commit_has_reservation = 1'b0;

        for (int n = 0; n < EVENT_PORTS; n++) begin
            if (commit_grant[n]) begin
                selected_commit_source = commit_source[n];
                selected_commit_peer_idx = commit_peer_idx[n];
                selected_commit_has_reservation = port_reserved_count_reg[n] != 0;
            end
        end
    end

    wire commit_has_reservation = selected_commit_has_reservation;
    wire logical_enqueue_available =
        fifo_count_reg < FIFO_COUNT_W'(FIFO_DEPTH) || claim_pop;
    wire claim_push_request =
        commit_accept && commit_has_reservation && logical_enqueue_available;
    wire claim_push = claim_push_request && claim_fifo_s_axis.tready;
    wire commit_consumes_reservation = commit_accept && commit_has_reservation;
    wire fifo_status_overflow;
    wire overflow_event = fifo_status_overflow ||
        (commit_accept && (!commit_has_reservation || !logical_enqueue_available ||
            !claim_fifo_s_axis.tready));
    wire invalid_complete_event = !rst && complete_valid && !complete_match;

    assign claim_fifo_s_axis.tdata = {
        next_sequence_reg,
        selected_commit_source,
        selected_commit_source == EVENT_PEER_DMA_COMPLETE ?
            selected_commit_peer_idx : PEER_IDX_W'(0)
    };
    assign claim_fifo_s_axis.tkeep = '1;
    assign claim_fifo_s_axis.tstrb = '1;
    assign claim_fifo_s_axis.tlast = 1'b1;
    assign claim_fifo_s_axis.tid = '0;
    assign claim_fifo_s_axis.tdest = '0;
    assign claim_fifo_s_axis.tuser = '0;
    assign claim_fifo_s_axis.tvalid = claim_push_request;

    assign claim_fifo_m_axis.tready = claim_pop;

    assign claim_valid = claim_fifo_m_axis.tvalid;
    assign claim_peer_idx = claim_valid ?
        claim_fifo_m_axis.tdata[0 +: PEER_IDX_W] : '0;
    assign claim_source = claim_valid ?
        claim_fifo_m_axis.tdata[PEER_IDX_W +: 4] : '0;
    assign claim_sequence = claim_valid ?
        claim_fifo_m_axis.tdata[PEER_IDX_W+4 +: SEQUENCE_W] : '0;

    taxi_axis_fifo #(
        .DEPTH(TAXI_FIFO_DEPTH),
        .RAM_PIPELINE(1),
        .OUTPUT_FIFO_EN(1'b0),
        .FRAME_FIFO(1'b0)
    ) u_claim_fifo (
        .clk(clk),
        .rst(rst),
        .s_axis(claim_fifo_s_axis),
        .m_axis(claim_fifo_m_axis),
        .pause_req(1'b0),
        .pause_ack(),
        .status_depth(),
        .status_depth_commit(),
        .status_overflow(fifo_status_overflow),
        .status_bad_frame(),
        .status_good_frame()
    );

    assign claim_pending = claim_valid;
    assign credit_full = occupied_count >= OCCUPIED_COUNT_W'(FIFO_DEPTH);
    assign overflow = overflow_reg;
    assign invalid_complete = invalid_complete_reg;
    assign irq = global_enable && claim_pending;
    assign irq_asserted = irq;

    if (FIFO_DEPTH > 255) begin : g_saturating_status
        assign fifo_level = fifo_count_reg > FIFO_COUNT_W'(255) ?
            8'hff : 8'(fifo_count_reg);
        assign reserved_count = reserved_count_reg > FIFO_COUNT_W'(255) ?
            8'hff : 8'(reserved_count_reg);
    end else begin : g_exact_status
        assign fifo_level = 8'(fifo_count_reg);
        assign reserved_count = 8'(reserved_count_reg);
    end

    assign clear_errors_hwclr = !rst && clear_errors;
    assign complete_valid_hwclr = !rst && complete_valid;

    always_ff @(posedge clk) begin
        if (rst) begin
            fifo_count_reg <= '0;
            reserved_count_reg <= '0;
            next_sequence_reg <= '0;
            overflow_reg <= 1'b0;
            invalid_complete_reg <= 1'b0;
            for (int n = 0; n < EVENT_PORTS; n++)
                port_reserved_count_reg[n] <= '0;
        end else begin
            if (clear_errors) begin
                overflow_reg <= 1'b0;
                invalid_complete_reg <= 1'b0;
            end

            // A new error has priority over a simultaneous maintenance clear.
            if (overflow_event)
                overflow_reg <= 1'b1;
            if (invalid_complete_event)
                invalid_complete_reg <= 1'b1;

            if (claim_push)
                next_sequence_reg <= next_sequence_reg + 1'b1;

            case ({claim_push, claim_pop})
                2'b10: fifo_count_reg <= fifo_count_reg + 1'b1;
                2'b01: fifo_count_reg <= fifo_count_reg - 1'b1;
                default: fifo_count_reg <= fifo_count_reg;
            endcase

            case ({admit_accept, commit_consumes_reservation})
                2'b10: reserved_count_reg <= reserved_count_reg + 1'b1;
                2'b01: reserved_count_reg <= reserved_count_reg - 1'b1;
                default: reserved_count_reg <= reserved_count_reg;
            endcase

            for (int n = 0; n < EVENT_PORTS; n++) begin
                case ({admit_accept && admit_grant[n],
                        commit_consumes_reservation && commit_grant[n]})
                    2'b10: port_reserved_count_reg[n] <=
                        port_reserved_count_reg[n] + 1'b1;
                    2'b01: port_reserved_count_reg[n] <=
                        port_reserved_count_reg[n] - 1'b1;
                    default: port_reserved_count_reg[n] <= port_reserved_count_reg[n];
                endcase
            end
        end
    end

endmodule

`resetall
