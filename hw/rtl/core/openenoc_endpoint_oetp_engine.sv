// SPDX-FileCopyrightText: 2026 Enio Kaljic
// SPDX-License-Identifier: CERN-OHL-S-2.0

`resetall
`timescale 1ns / 1ps
`default_nettype none

/* Streaming Ethernet/oETP command transport and transaction control. */
module openenoc_endpoint_oetp_engine #(
    parameter int unsigned MAX_RAW_FRAME_SIZE = 8192
) (
    input wire logic clk,
    input wire logic rst,
    openenoc_endpoint_if.core endpoint_if,
    taxi_axis_if.snk s_axis_local,
    taxi_axis_if.src m_axis_local,
    taxi_axis_if.snk s_axis_eth,
    taxi_axis_if.src m_axis_eth,
    openenoc_peer_lookup_if.mst peer_lookup_if,
    openenoc_dma_transfer_if.executor initiator_if,
    openenoc_dma_transfer_if.requester responder_if
);
    taxi_axis_if #(
        .DATA_W(s_axis_local.DATA_W),
        .KEEP_W(s_axis_local.KEEP_W),
        .KEEP_EN(s_axis_local.KEEP_EN),
        .STRB_EN(s_axis_local.STRB_EN),
        .LAST_EN(s_axis_local.LAST_EN),
        .ID_EN(s_axis_local.ID_EN),
        .ID_W(s_axis_local.ID_W),
        .DEST_EN(s_axis_local.DEST_EN),
        .DEST_W(s_axis_local.DEST_W),
        .USER_EN(s_axis_local.USER_EN),
        .USER_W(s_axis_local.USER_W)
    ) local_input();

    taxi_axis_register #(
        .REG_TYPE(2)
    ) u_local_input_register (
        .clk(clk),
        .rst(rst),
        .s_axis(s_axis_local),
        .m_axis(local_input)
    );

    taxi_axis_if #(
        .DATA_W(m_axis_local.DATA_W),
        .KEEP_W(m_axis_local.KEEP_W),
        .KEEP_EN(m_axis_local.KEEP_EN),
        .STRB_EN(m_axis_local.STRB_EN),
        .LAST_EN(m_axis_local.LAST_EN),
        .ID_EN(m_axis_local.ID_EN),
        .ID_W(m_axis_local.ID_W),
        .DEST_EN(m_axis_local.DEST_EN),
        .DEST_W(m_axis_local.DEST_W),
        .USER_EN(m_axis_local.USER_EN),
        .USER_W(m_axis_local.USER_W)
    ) local_output();

    taxi_axis_if #(
        .DATA_W(m_axis_local.DATA_W),
        .KEEP_W(m_axis_local.KEEP_W),
        .KEEP_EN(m_axis_local.KEEP_EN),
        .STRB_EN(m_axis_local.STRB_EN),
        .LAST_EN(m_axis_local.LAST_EN),
        .ID_EN(m_axis_local.ID_EN),
        .ID_W(m_axis_local.ID_W),
        .DEST_EN(m_axis_local.DEST_EN),
        .DEST_W(m_axis_local.DEST_W),
        .USER_EN(m_axis_local.USER_EN),
        .USER_W(m_axis_local.USER_W)
    ) local_registered();

    assign m_axis_local.tdata = local_registered.tdata;
    assign m_axis_local.tkeep = local_registered.tkeep;
    assign m_axis_local.tvalid = local_registered.tvalid;
    assign m_axis_local.tlast = local_registered.tlast;
    assign m_axis_local.tid = local_registered.tid;
    assign m_axis_local.tdest = local_registered.tdest;
    assign m_axis_local.tuser = local_registered.tuser;
    assign m_axis_local.tstrb = m_axis_local.STRB_EN ? local_registered.tstrb
        : local_registered.tkeep;
    assign local_registered.tready = m_axis_local.tready;

    taxi_axis_register #(
        .REG_TYPE(2)
    ) u_local_output_register (
        .clk(clk),
        .rst(rst),
        .s_axis(local_output),
        .m_axis(local_registered)
    );

    taxi_axis_if #(
        .DATA_W(s_axis_eth.DATA_W),
        .KEEP_W(s_axis_eth.KEEP_W),
        .KEEP_EN(s_axis_eth.KEEP_EN),
        .STRB_EN(s_axis_eth.STRB_EN),
        .LAST_EN(s_axis_eth.LAST_EN),
        .ID_EN(s_axis_eth.ID_EN),
        .ID_W(s_axis_eth.ID_W),
        .DEST_EN(s_axis_eth.DEST_EN),
        .DEST_W(s_axis_eth.DEST_W),
        .USER_EN(s_axis_eth.USER_EN),
        .USER_W(s_axis_eth.USER_W)
    ) eth_input();

    taxi_axis_register #(
        .REG_TYPE(2)
    ) u_eth_input_register (
        .clk(clk),
        .rst(rst),
        .s_axis(s_axis_eth),
        .m_axis(eth_input)
    );

    taxi_axis_if #(
        .DATA_W(m_axis_eth.DATA_W),
        .KEEP_W(m_axis_eth.KEEP_W),
        .KEEP_EN(m_axis_eth.KEEP_EN),
        .STRB_EN(m_axis_eth.STRB_EN),
        .LAST_EN(m_axis_eth.LAST_EN),
        .ID_EN(m_axis_eth.ID_EN),
        .ID_W(m_axis_eth.ID_W),
        .DEST_EN(m_axis_eth.DEST_EN),
        .DEST_W(m_axis_eth.DEST_W),
        .USER_EN(m_axis_eth.USER_EN),
        .USER_W(m_axis_eth.USER_W)
    ) eth_output();

    taxi_axis_if #(
        .DATA_W(m_axis_eth.DATA_W),
        .KEEP_W(m_axis_eth.KEEP_W),
        .KEEP_EN(m_axis_eth.KEEP_EN),
        .STRB_EN(m_axis_eth.STRB_EN),
        .LAST_EN(m_axis_eth.LAST_EN),
        .ID_EN(m_axis_eth.ID_EN),
        .ID_W(m_axis_eth.ID_W),
        .DEST_EN(m_axis_eth.DEST_EN),
        .DEST_W(m_axis_eth.DEST_W),
        .USER_EN(m_axis_eth.USER_EN),
        .USER_W(m_axis_eth.USER_W)
    ) eth_registered();

    assign m_axis_eth.tdata = eth_registered.tdata;
    assign m_axis_eth.tkeep = eth_registered.tkeep;
    assign m_axis_eth.tvalid = eth_registered.tvalid;
    assign m_axis_eth.tlast = eth_registered.tlast;
    assign m_axis_eth.tid = eth_registered.tid;
    assign m_axis_eth.tdest = eth_registered.tdest;
    assign m_axis_eth.tuser = eth_registered.tuser;
    assign m_axis_eth.tstrb = m_axis_eth.STRB_EN ? eth_registered.tstrb : eth_registered.tkeep;
    assign eth_registered.tready = m_axis_eth.tready;

    taxi_axis_register #(
        .REG_TYPE(2)
    ) u_eth_output_register (
        .clk(clk),
        .rst(rst),
        .s_axis(eth_output),
        .m_axis(eth_registered)
    );

    localparam int PEER_W = peer_lookup_if.PEER_IDX_W;
    localparam int SEQ_W = initiator_if.SEQUENCE_W;
    wire [31:0] rmem_timeout_cycles = endpoint_if.csr_to_core.config_.rmem_timeout.cycles.value;
    localparam int DEST_W = PEER_W + 2;
    localparam int MAX_FRAGMENT = ((MAX_RAW_FRAME_SIZE - 32) / 4) * 4;
    localparam logic [31:0] END_OF_DATA = 32'hE0D0E0D0;
    localparam logic[7:0] RMEM_READ_REQ = 8'h10, RMEM_READ_RSP = 8'h11, RMEM_WRITE_REQ = 8'h20,
        RMEM_WRITE_RSP = 8'h21, DMA_READ_REQ = 8'h30, DMA_READ_RSP = 8'h31, DMA_WRITE_REQ = 8'h40,
        DMA_WRITE_RSP = 8'h41, ERROR_RSP = 8'hff;

    if (MAX_RAW_FRAME_SIZE < 36 || MAX_RAW_FRAME_SIZE > 8192) begin : g_bad_limit
        $fatal(0, "Invalid oETP frame ceiling (instance %m)");
    end

    if (initiator_if.ADDR_W != 32 || initiator_if.LEN_W != 32 || responder_if.SEQUENCE_W != SEQ_W
        || local_input.USER_W < 2 || local_output.USER_W < 2 || local_input.DEST_W != DEST_W
        || local_output.DEST_W != DEST_W) begin : g_bad_interface
        $fatal(0, "Incompatible oETP interfaces (instance %m)");
    end

    taxi_axis_if #(
        .DATA_W(32),
        .KEEP_EN(1),
        .LAST_EN(1),
        .ID_EN(1),
        .DEST_EN(1),
        .USER_EN(1),
        .ID_W(SEQ_W),
        .DEST_W(DEST_W),
        .USER_W(2)
    ) local_tx(), local_rx();

    taxi_axis_if #(
        .DATA_W(32),
        .KEEP_EN(1),
        .LAST_EN(1)
    ) eth_rx(), eth_tx();

    taxi_axis_adapter u_local_tx (
        .clk(clk),
        .rst(rst),
        .s_axis(local_input),
        .m_axis(local_tx)
    );

    taxi_axis_adapter u_local_rx (
        .clk(clk),
        .rst(rst),
        .s_axis(local_rx),
        .m_axis(local_output)
    );

    taxi_axis_adapter u_eth_rx (
        .clk(clk),
        .rst(rst),
        .s_axis(eth_input),
        .m_axis(eth_rx)
    );

    taxi_axis_adapter u_eth_tx (
        .clk(clk),
        .rst(rst),
        .s_axis(eth_tx),
        .m_axis(eth_output)
    );

    function automatic logic [31:0] byte_count(input logic [3:0] keep);
        return 32'(keep[0]) + 32'(keep[1]) + 32'(keep[2]) + 32'(keep[3]);
    endfunction

    function automatic logic [3:0] byte_mask(input logic [31:0] count);
        case (count)
            0: return 4'b0000;
            1: return 4'b0001;
            2: return 4'b0011;
            3: return 4'b0111;
            default: return 4'b1111;
        endcase
    endfunction

    function automatic logic keep_valid(input logic [3:0] keep);
        return keep == 1 || keep == 3 || keep == 7 || keep == 15;
    endfunction

    function automatic logic [31:0] masked_word(input logic [31:0] data, input logic [3:0] keep);
        logic [31:0] result;
        for (int lane = 0; lane < 4; lane++)
            result[lane*8+:8] = keep[lane] ? data[lane*8+:8] : 8'd0;
        return result;
    endfunction

    function automatic logic frame_length_valid(input logic [31:0] actual, expected);
        return actual == expected || (expected < 60 && actual == 60);
    endfunction

    function automatic logic [3:0] metadata_words(input logic [7:0] cmd);
        case (cmd)
            RMEM_READ_REQ, RMEM_READ_RSP, ERROR_RSP: return 6;
            RMEM_WRITE_REQ: return 8;
            RMEM_WRITE_RSP, DMA_READ_RSP, DMA_WRITE_RSP: return 5;
            DMA_READ_REQ, DMA_WRITE_REQ: return 7;
            default: return 5;
        endcase
    endfunction

    function automatic logic known_command(input logic [7:0] cmd);
        return cmd == RMEM_READ_REQ || cmd == RMEM_READ_RSP || cmd == RMEM_WRITE_REQ
            || cmd == RMEM_WRITE_RSP || cmd == DMA_READ_REQ || cmd == DMA_READ_RSP
            || cmd == DMA_WRITE_REQ || cmd == DMA_WRITE_RSP || cmd == ERROR_RSP;
    endfunction

    function automatic logic response_command(input logic [7:0] cmd);
        return cmd == RMEM_READ_RSP || cmd == RMEM_WRITE_RSP || cmd == DMA_READ_RSP
            || cmd == DMA_WRITE_RSP || cmd == ERROR_RSP;
    endfunction

    function automatic logic [7:0] request_command(input logic kind, op);
        if (kind) return op ? RMEM_WRITE_REQ : RMEM_READ_REQ;
        return op ? DMA_WRITE_REQ : DMA_READ_REQ;
    endfunction

    typedef enum logic [3:0] {
        INITIATOR_IDLE,
        INITIATOR_LOOKUP,
        INITIATOR_LOOKUP_WAIT,
        INITIATOR_ACCEPT,
        INITIATOR_TX,
        INITIATOR_WAIT,
        INITIATOR_ABORT,
        INITIATOR_COMPLETE
    } initiator_state_t;

    typedef enum logic [1:0] {
        RESPONDER_IDLE,
        RESPONDER_EXECUTE
    } responder_state_t;

    typedef enum logic [4:0] {
        RX_IDLE,
        RX_HEADER,
        RX_CLASSIFY,
        RX_META,
        RX_MATCH,
        RX_LOOKUP,
        RX_LOOKUP_WAIT,
        RX_ADMIT,
        RX_REQUEST,
        RX_DATA,
        RX_EOD,
        RX_TAIL,
        RX_VALIDATE,
        RX_FINAL,
        RX_ABORT,
        RX_DROP,
        RX_RAW_CLAIM,
        RX_RAW_REPLAY,
        RX_RAW_STREAM,
        RX_RAW_FINISH
    } receive_state_t;

    typedef enum logic [3:0] {
        TX_IDLE,
        TX_PRIME,
        TX_HEADER,
        TX_DATA,
        TX_STATUS,
        TX_FLUSH,
        TX_EOD,
        TX_ERROR_FLUSH,
        TX_DRAIN,
        TX_WAIT_END,
        TX_RAW,
        TX_PRE_DRAIN
    } transmit_state_t;

    typedef enum logic [2:0] {
        LOOKUP_IDLE,
        LOOKUP_INITIATOR_REQ,
        LOOKUP_INITIATOR_RSP,
        LOOKUP_RX_REQ,
        LOOKUP_RX_RSP
    } lookup_state_t;

    initiator_state_t initiator_state_reg;
    responder_state_t responder_state_reg;
    receive_state_t rx_state_reg;
    transmit_state_t tx_state_reg;
    lookup_state_t lookup_state_reg;

    typedef struct packed {
        logic kind, op, last, group;
        logic [PEER_W-1:0] peer;
        logic [SEQ_W-1:0] sequence_;
        logic [31:0] addr, len, biten, data, id;
        logic [47:0] mac, local_mac;
    } context_t;
    context_t initiator_context_reg, responder_context_reg;

    logic [31:0] request_id_reg, responder_sequence_reg;
    logic [31:0] initiator_timeout_reg, timer_count_reg;
    logic timer_active_reg, initiator_config_valid_reg;
    logic [3:0] initiator_error_reg;
    logic [31:0] initiator_result_reg, initiator_delivered_reg;
    logic initiator_source_done_reg;
    logic [31:0] initiator_source_len_reg;
    logic [3:0] initiator_source_error_reg;
    logic responder_done_reg;
    logic [31:0] responder_result_reg, responder_completed_len_reg;
    logic [3:0] responder_error_reg;

    logic [31:0] rx_header_reg[8];
    logic [3:0] rx_header_keep_reg[8];
    logic rx_header_last_reg[8];
    logic [3:0] rx_header_count_reg, rx_meta_words_reg, rx_replay_reg;
    logic [7:0] rx_cmd_reg;
    logic [47:0] rx_local_mac_reg, rx_group_mac_reg;
    logic [1:0] rx_receive_mode_reg, rx_route_reg;
    logic [PEER_W-1:0] rx_peer_reg;
    logic [SEQ_W-1:0] rx_sequence_reg;
    logic [31:0] rx_frame_bytes_reg, rx_logical_bytes_reg, rx_length_reg, rx_data_bytes_reg;
    logic [3:0] rx_error_reg;
    logic rx_ended_reg, rx_own_reg, rx_request_sent_reg;
    logic [31:0] rx_hold_data_reg, rx_out_data_reg;
    logic [3:0] rx_hold_keep_reg, rx_out_keep_reg;
    logic rx_hold_valid_reg, rx_hold_last_reg, rx_out_valid_reg, rx_out_last_reg;

    wire [47:0] rx_destination = {
        rx_header_reg[0][7:0],
        rx_header_reg[0][15:8],
        rx_header_reg[0][23:16],
        rx_header_reg[0][31:24],
        rx_header_reg[1][7:0],
        rx_header_reg[1][15:8]
    };
    wire [47:0] rx_source = {
        rx_header_reg[1][23:16],
        rx_header_reg[1][31:24],
        rx_header_reg[2][7:0],
        rx_header_reg[2][15:8],
        rx_header_reg[2][23:16],
        rx_header_reg[2][31:24]
    };
    wire rx_group = rx_destination[40];
    wire rx_bulk = rx_cmd_reg == DMA_WRITE_REQ || rx_cmd_reg == DMA_READ_RSP;
    wire rx_is_response = response_command(rx_cmd_reg);
    wire rx_is_rmem = rx_cmd_reg[7:4] == 1 || rx_cmd_reg[7:4] == 2;
    wire rx_write = rx_cmd_reg == RMEM_WRITE_REQ || rx_cmd_reg == DMA_WRITE_REQ;
    wire rx_complete_response = rx_state_reg == RX_FINAL && rx_own_reg && !rx_hold_valid_reg
        && !rx_out_valid_reg;
    wire timer_expire = timer_active_reg && timer_count_reg == initiator_timeout_reg - 1
        && !rx_complete_response;
    wire rx_abort = timer_expire && rx_own_reg
        && (rx_state_reg == RX_DATA || rx_state_reg == RX_EOD || rx_state_reg == RX_TAIL
            || rx_state_reg == RX_VALIDATE || rx_state_reg == RX_FINAL);
    wire rx_input_fire = eth_rx.tvalid && eth_rx.tready;
    wire rx_output_fire = local_rx.tvalid && local_rx.tready;
    wire lookup_initiator_req_fire = lookup_state_reg == LOOKUP_INITIATOR_REQ && lookup_req_fire;
    wire lookup_initiator_rsp_fire = lookup_state_reg == LOOKUP_INITIATOR_RSP && lookup_rsp_fire;
    wire lookup_rx_req_fire = lookup_state_reg == LOOKUP_RX_REQ && lookup_req_fire;
    wire lookup_rx_rsp_fire = lookup_state_reg == LOOKUP_RX_RSP && lookup_rsp_fire;

    logic tx_responder_reg, tx_bulk_reg, tx_raw_reg;
    logic tx_input_done_reg, tx_eth_done_reg, tx_proto_turn_reg, tx_no_frame_reg;
    logic [31:0] tx_header_reg[8];
    logic [3:0] tx_header_words_reg, tx_header_index_reg;
    logic [31:0] tx_length_reg, tx_data_bytes_reg;
    logic [PEER_W-1:0] tx_peer_reg;
    logic [SEQ_W-1:0] tx_sequence_reg;
    logic tx_last_reg;
    logic [3:0] tx_fault_reg;
    logic [31:0] tx_hold_data_reg, tx_out_data_reg;
    logic [3:0] tx_hold_keep_reg, tx_out_keep_reg;
    logic tx_hold_valid_reg, tx_out_valid_reg, tx_out_last_reg;
    wire tx_source_done = tx_responder_reg ? responder_done_reg : initiator_source_done_reg;
    wire[3:0] tx_source_error = tx_responder_reg ? responder_error_reg : initiator_source_error_reg;
    wire[31:0] tx_source_len = tx_responder_reg ? responder_completed_len_reg
        : initiator_source_len_reg;
    wire[3:0] tx_final_error = tx_source_error != 0 ? tx_source_error : tx_fault_reg != 0
        ? tx_fault_reg : tx_source_len != tx_length_reg ? 4'd2 : 4'd0;
    wire local_is_raw = local_tx.tdest[PEER_W+:2] != initiator_if.ROUTE_PEER;
    wire local_matches_initiator = local_tx.tvalid && !local_is_raw && !local_tx.tuser[1]
        && local_tx.tdest[PEER_W-1:0] == initiator_context_reg.peer
        && local_tx.tid == initiator_context_reg.sequence_;
    wire local_matches_responder = local_tx.tvalid && !local_is_raw && local_tx.tuser[1]
        && local_tx.tdest[PEER_W-1:0] == responder_context_reg.peer
        && local_tx.tid == responder_context_reg.sequence_;
    wire local_matches_tx = local_tx.tvalid && !local_is_raw
        && local_tx.tuser[1] == tx_responder_reg && local_tx.tdest[PEER_W-1:0] == tx_peer_reg
        && local_tx.tid == tx_sequence_reg;
    wire tx_initiator_available = initiator_state_reg == INITIATOR_TX
        && (initiator_context_reg.kind || !initiator_context_reg.op || local_matches_initiator
            || (initiator_source_done_reg && initiator_source_error_reg != 0
                && initiator_source_len_reg == 0));
    wire tx_responder_available = responder_state_reg == RESPONDER_EXECUTE
        && !responder_context_reg.group
        && ((responder_context_reg.kind
                || responder_context_reg.op) ? responder_done_reg : (local_matches_responder
                || (responder_done_reg && responder_error_reg != 0
                    && responder_completed_len_reg == 0)));
    wire tx_select_responder = tx_responder_available;
    wire tx_select_initiator = !tx_responder_available && tx_initiator_available
        && (!local_tx.tvalid || !local_is_raw || tx_proto_turn_reg);
    wire tx_select_raw = !tx_responder_available && !tx_select_initiator && local_tx.tvalid
        && local_is_raw;
    wire tx_stream_fire = local_tx.tvalid && local_tx.tready;
    wire tx_output_fire = eth_tx.tvalid && eth_tx.tready;
    wire tx_wire_end = m_axis_eth.tvalid && m_axis_eth.tready && m_axis_eth.tlast;
    wire tx_done = tx_state_reg == TX_WAIT_END && tx_eth_done_reg
        && (!tx_bulk_reg || (tx_input_done_reg && tx_source_done));
    wire [3:0] tx_done_error = tx_bulk_reg ? tx_final_error : 4'd0;
    context_t tx_selected_context;
    logic [7:0] tx_selected_cmd;
    logic tx_selected_error, tx_selected_bulk;

    always_comb begin
        tx_selected_context = tx_select_responder ? responder_context_reg : initiator_context_reg;
        tx_selected_error = tx_select_responder && responder_done_reg && responder_error_reg != 0;
        if (tx_select_responder) begin
            if (tx_selected_error) tx_selected_cmd = ERROR_RSP;
            else
                tx_selected_cmd = request_command(responder_context_reg.kind,
                        responder_context_reg.op) | 8'h01;
        end else begin
            tx_selected_cmd = request_command(initiator_context_reg.kind, initiator_context_reg.op);
        end
        tx_selected_bulk = !tx_selected_error && !tx_selected_context.kind
            && (tx_select_responder ? !tx_selected_context.op : tx_selected_context.op);
    end

    wire initiator_rmem_valid = peer_lookup_if.rsp_dma_mode == 1
        && initiator_context_reg.addr[1:0] == 0 && initiator_context_reg.len == 4;
    wire initiator_dma_valid = peer_lookup_if.rsp_dma_mode == (initiator_context_reg.op ? 2'd3
            : 2'd2) && initiator_context_reg.len != 0
        && initiator_context_reg.len <= 32'(MAX_FRAGMENT);
    wire initiator_lookup_valid = peer_lookup_if.rsp_hit && !initiator_context_reg.local_mac[40] &&
        (!peer_lookup_if.rsp_mac_addr[40] || initiator_context_reg.op) &&
        (initiator_context_reg.kind ? initiator_rmem_valid : initiator_dma_valid) &&
        {1'b0, initiator_context_reg.addr} + {1'b0, initiator_context_reg.len} <= 33'h100000000;

    wire[7:0] expected_response_command = request_command(initiator_context_reg.kind,
            initiator_context_reg.op) | 8'h01;
    wire rx_response_matches = (initiator_state_reg == INITIATOR_WAIT
            || (initiator_state_reg == INITIATOR_TX && timer_active_reg)) && !rx_group
        && rx_source == initiator_context_reg.mac && rx_header_reg[4] == initiator_context_reg.id
        && (rx_cmd_reg == ERROR_RSP || rx_cmd_reg == expected_response_command);
    wire rx_protocol_header = rx_header_count_reg == 4 && rx_header_keep_reg[3][2:0] == 3'b111
        && rx_header_reg[3][23:0] == 24'h0eb588;
    wire rx_destination_matches = rx_group ? rx_destination == rx_group_mac_reg
        : rx_destination == rx_local_mac_reg;
    wire rx_raw_admitted = rx_receive_mode_reg != 0
        && (rx_receive_mode_reg == 3 || rx_destination == rx_local_mac_reg
            || rx_destination == 48'hffffffffffff || (rx_receive_mode_reg == 2 && rx_group));

    wire initiator_req_fire = initiator_if.req_valid && initiator_if.req_ready;
    wire initiator_cpl_fire = initiator_if.cpl_valid && initiator_if.cpl_ready;
    wire initiator_tx_status_fire = initiator_if.tx_status_valid && initiator_if.tx_status_ready;
    wire responder_req_fire = responder_if.req_valid && responder_if.req_ready;
    wire responder_cpl_fire = responder_if.cpl_valid && responder_if.cpl_ready;
    wire responder_rx_status_fire = responder_if.rx_status_valid && responder_if.rx_status_ready;
    wire responder_non_oetp_rx_claim_fire = responder_if.non_oetp_rx_claim_valid
        && responder_if.non_oetp_rx_claim_ready;
    wire lookup_req_fire = peer_lookup_if.req_valid && peer_lookup_if.req_ready;
    wire lookup_rsp_fire = peer_lookup_if.rsp_valid && peer_lookup_if.rsp_ready;

    always_ff @(posedge clk) begin : initiator_control
        initiator_if.req_ready <= rst ? '0 : ((initiator_state_reg == INITIATOR_ACCEPT)
                && !(initiator_req_fire));
        initiator_if.cpl_valid <= rst ? '0 : ((initiator_state_reg == INITIATOR_COMPLETE)
                && !(initiator_cpl_fire));
        initiator_if.cpl_kind <= rst ? '0 : initiator_context_reg.kind;
        initiator_if.cpl_op <= rst ? '0 : initiator_context_reg.op;
        initiator_if.cpl_peer_idx <= rst ? '0 : initiator_context_reg.peer;
        initiator_if.cpl_sequence <= rst ? '0 : (initiator_context_reg.sequence_);
        initiator_if.cpl_last <= rst ? '0 : initiator_context_reg.last;
        initiator_if.cpl_rdata <= rst ? '0 : initiator_result_reg;
        initiator_if.cpl_transferred_len <= rst ? '0
            : (initiator_error_reg == 0 ? initiator_context_reg.len : initiator_delivered_reg);
        initiator_if.cpl_error <= rst ? '0 : (initiator_error_reg != 0);
        initiator_if.cpl_error_code <= rst ? '0 : (initiator_if.ERROR_W'(initiator_error_reg));
        initiator_if.tx_status_ready <= rst ? '0 : ((initiator_state_reg == INITIATOR_TX
                    && !initiator_source_done_reg) && !(initiator_tx_status_fire));
        initiator_if.rx_status_ready <= 1'b0;
        initiator_if.non_oetp_rx_available <= 1'b0;
        initiator_if.non_oetp_rx_claim_ready <= 1'b0;

        if (rst) begin
            initiator_state_reg <= INITIATOR_IDLE;
            initiator_context_reg <= '0;
            request_id_reg <= 0;
            initiator_timeout_reg <= 0;
            timer_count_reg <= 0;
            timer_active_reg <= 0;
            initiator_config_valid_reg <= 0;
            initiator_error_reg <= 0;
            initiator_result_reg <= 0;
            initiator_delivered_reg <= 0;
            initiator_source_done_reg <= 0;
            initiator_source_len_reg <= 0;
            initiator_source_error_reg <= 0;
        end else begin
            case (initiator_state_reg)
                INITIATOR_IDLE: begin
                    if (initiator_if.req_valid) begin
                        initiator_state_reg <= INITIATOR_LOOKUP;
                    end
                end
                INITIATOR_LOOKUP: begin
                    if (lookup_initiator_req_fire) begin
                        initiator_state_reg <= INITIATOR_LOOKUP_WAIT;
                    end
                end
                INITIATOR_LOOKUP_WAIT: begin
                    if (lookup_initiator_rsp_fire) begin
                        initiator_state_reg <= INITIATOR_ACCEPT;
                    end
                end
                INITIATOR_ACCEPT: begin
                    if (initiator_req_fire) begin
                        initiator_state_reg <= initiator_config_valid_reg ? INITIATOR_TX
                            : INITIATOR_COMPLETE;
                    end
                end
                INITIATOR_TX: begin
                    if (tx_done && !tx_responder_reg && !tx_raw_reg) begin
                        initiator_state_reg <= tx_done_error != 0 ? INITIATOR_ABORT
                            : initiator_context_reg.group ? INITIATOR_COMPLETE : INITIATOR_WAIT;
                    end
                end
                INITIATOR_WAIT: begin
                    if (rx_complete_response) begin
                        initiator_state_reg <= INITIATOR_COMPLETE;
                    end
                end
                INITIATOR_ABORT: begin
                    if (!rx_own_reg || rx_state_reg == RX_IDLE) begin
                        initiator_state_reg <= INITIATOR_COMPLETE;
                    end
                end
                INITIATOR_COMPLETE: begin
                    if (initiator_cpl_fire) begin
                        initiator_state_reg <= INITIATOR_IDLE;
                    end
                end
                default: begin
                    initiator_state_reg <= INITIATOR_IDLE;
                end
            endcase

            if ((initiator_state_reg == INITIATOR_TX || initiator_state_reg == INITIATOR_WAIT)
                && rx_complete_response) begin
                initiator_state_reg <= INITIATOR_COMPLETE;
            end

            if (timer_expire) begin
                initiator_state_reg <= INITIATOR_ABORT;
            end

            if (initiator_state_reg == INITIATOR_IDLE && initiator_if.req_valid) begin
                initiator_context_reg.kind <= initiator_if.req_kind;
                initiator_context_reg.op <= initiator_if.req_op;
                initiator_context_reg.addr <= initiator_if.req_addr;
                initiator_context_reg.len <= initiator_if.req_len;
                initiator_context_reg.biten <= initiator_if.req_biten;
                initiator_context_reg.data <= initiator_if.req_wdata;
                initiator_context_reg.peer <= initiator_if.req_peer_idx;
                initiator_context_reg.sequence_ <= initiator_if.req_sequence;
                initiator_context_reg.last <= initiator_if.req_last;
                initiator_context_reg.mac <= {
                    endpoint_if.csr_to_core.peers.entry[
                        initiator_if.req_peer_idx].mac_address.hi_word.value,
                    endpoint_if.csr_to_core.peers.entry[
                        initiator_if.req_peer_idx].mac_address.lo_word.value
                };
                initiator_context_reg.local_mac <= {
                    endpoint_if.csr_to_core.config_.mac_address.hi_word.value,
                    endpoint_if.csr_to_core.config_.mac_address.lo_word.value
                };
                initiator_error_reg <= 0;
                initiator_result_reg <= 0;
                initiator_delivered_reg <= 0;
                initiator_source_done_reg <= 0;
                initiator_source_error_reg <= 0;
                initiator_source_len_reg <= 0;
            end

            if (lookup_initiator_rsp_fire) begin
                initiator_context_reg.mac <= peer_lookup_if.rsp_mac_addr;
                initiator_context_reg.group <= peer_lookup_if.rsp_mac_addr[40];
                initiator_config_valid_reg <= initiator_lookup_valid;
            end

            if (initiator_state_reg == INITIATOR_ACCEPT && initiator_req_fire) begin
                initiator_context_reg.id <= request_id_reg;
                request_id_reg <= request_id_reg + 1;
                initiator_timeout_reg <= initiator_context_reg.kind ? rmem_timeout_cycles
                    : endpoint_if.csr_to_core.config_.dma_timeout.cycles.value;
                if (!initiator_config_valid_reg) begin
                    initiator_error_reg <= 1;
                end
            end

            if (initiator_tx_status_fire) begin
                initiator_source_done_reg <= 1;
                initiator_source_len_reg <= initiator_if.tx_status_len;
                initiator_source_error_reg <= initiator_if.tx_status_peer_idx
                    != initiator_context_reg.peer
                    || initiator_if.tx_status_sequence != initiator_context_reg.sequence_ ? 4'd2
                    : 4'(initiator_if.tx_status_error_code);
            end

            if (tx_wire_end && !tx_responder_reg && !tx_raw_reg
                && initiator_state_reg == INITIATOR_TX && !initiator_context_reg.group
                && initiator_timeout_reg != 0 && (!tx_bulk_reg || tx_final_error == 0)) begin
                timer_active_reg <= 1;
                timer_count_reg <= 0;
            end else if (timer_active_reg) begin
                timer_count_reg <= timer_count_reg + 1;
            end

            if (tx_done && !tx_responder_reg && !tx_raw_reg) begin
                if (tx_done_error != 0) begin
                    initiator_error_reg <= tx_done_error;
                    initiator_delivered_reg <= 0;
                    timer_active_reg <= 0;
                end else if (initiator_context_reg.group) begin
                    initiator_delivered_reg <= initiator_context_reg.len;
                end
            end

            if (rx_complete_response) begin
                timer_active_reg <= 0;
                initiator_delivered_reg <= rx_data_bytes_reg;
                initiator_result_reg <= rx_header_reg[5];
                if (rx_error_reg != 0) begin
                    initiator_error_reg <= rx_error_reg;
                end else if (rx_cmd_reg == ERROR_RSP)
                    initiator_error_reg <= 4'(initiator_if.csr_error_from_wire(rx_header_reg[5]));
                else begin
                    initiator_error_reg <= 0;
                end
            end

            if (timer_expire) begin
                timer_active_reg <= 0;
                initiator_error_reg <= 8;
                initiator_delivered_reg <= rx_data_bytes_reg;
            end
        end
    end

    always_ff @(posedge clk) begin : responder_control
        responder_if.cpl_ready <= rst ? '0 : ((responder_state_reg == RESPONDER_EXECUTE
                    && !responder_done_reg) && !(responder_cpl_fire));
        if (rst) begin
            responder_state_reg <= RESPONDER_IDLE;
            responder_context_reg <= '0;
            responder_sequence_reg <= 0;
            responder_done_reg <= 0;
            responder_result_reg <= 0;
            responder_completed_len_reg <= 0;
            responder_error_reg <= 0;
        end else begin
            case (responder_state_reg)
                RESPONDER_IDLE: begin
                    if (responder_req_fire) begin
                        responder_state_reg <= RESPONDER_EXECUTE;
                    end
                end
                RESPONDER_EXECUTE: begin
                    if ((responder_context_reg.group && responder_done_reg)
                        || (tx_done && tx_responder_reg && !tx_raw_reg)) begin
                        responder_state_reg <= RESPONDER_IDLE;
                    end
                end
                default: begin
                    responder_state_reg <= RESPONDER_IDLE;
                end
            endcase

            if (responder_req_fire) begin
                responder_context_reg.kind <= rx_is_rmem;
                responder_context_reg.op <= rx_write;
                responder_context_reg.addr <= rx_header_reg[5];
                responder_context_reg.len <= responder_if.req_len;
                responder_context_reg.biten <= rx_header_reg[6];
                responder_context_reg.data <= rx_header_reg[7];
                responder_context_reg.peer <= rx_peer_reg;
                responder_context_reg.sequence_ <= rx_sequence_reg;
                responder_context_reg.last <= 1;
                responder_context_reg.group <= rx_group;
                responder_context_reg.id <= rx_header_reg[4];
                responder_context_reg.mac <= rx_source;
                responder_context_reg.local_mac <= rx_local_mac_reg;
                responder_sequence_reg <= responder_sequence_reg + 1;
                responder_done_reg <= 0;
                responder_error_reg <= 0;
                responder_result_reg <= 0;
                responder_completed_len_reg <= 0;
            end

            if (responder_cpl_fire) begin
                responder_done_reg <= 1;
                responder_result_reg <= responder_if.cpl_rdata;
                responder_completed_len_reg <= responder_if.cpl_transferred_len;
                responder_error_reg <= responder_if.cpl_error ? 4'(responder_if.cpl_error_code)
                    : 4'd0;
            end

        end
    end

    always_ff @(posedge clk) begin : lookup_control
        peer_lookup_if.req_valid <= rst ? '0 : ((lookup_state_reg == LOOKUP_INITIATOR_REQ
                    || lookup_state_reg == LOOKUP_RX_REQ) && !(lookup_req_fire));
        peer_lookup_if.req_type <= rst ? '0
            : (lookup_state_reg == LOOKUP_RX_REQ ? 2'd2
                : (initiator_context_reg.kind ? 2'd2 : 2'd0));
        peer_lookup_if.req_mode_mask <= rst ? '0 : (lookup_state_reg == LOOKUP_INITIATOR_REQ
                && initiator_context_reg.kind ? 4'b0010 : 4'b1110);
        peer_lookup_if.req_peer_idx <= rst ? '0 : initiator_context_reg.peer;
        peer_lookup_if.req_rmem_addr <= '0;
        peer_lookup_if.req_mac_addr <= rst ? '0
            : (lookup_state_reg == LOOKUP_RX_REQ ? rx_source : initiator_context_reg.mac);
        peer_lookup_if.rsp_ready <= rst ? '0 : ((lookup_state_reg == LOOKUP_INITIATOR_RSP
                    || lookup_state_reg == LOOKUP_RX_RSP) && !(lookup_rsp_fire));

        if (rst) begin
            lookup_state_reg <= LOOKUP_IDLE;
        end else begin
            case (lookup_state_reg)
                LOOKUP_IDLE: begin
                    if (rx_state_reg == RX_LOOKUP) begin
                        lookup_state_reg <= LOOKUP_RX_REQ;
                    end else if (initiator_state_reg == INITIATOR_LOOKUP) begin
                        lookup_state_reg <= LOOKUP_INITIATOR_REQ;
                    end
                end
                LOOKUP_INITIATOR_REQ: begin
                    if (lookup_req_fire) begin
                        lookup_state_reg <= LOOKUP_INITIATOR_RSP;
                    end
                end
                LOOKUP_INITIATOR_RSP: begin
                    if (lookup_rsp_fire) begin
                        lookup_state_reg <= LOOKUP_IDLE;
                    end
                end
                LOOKUP_RX_REQ: begin
                    if (lookup_req_fire) begin
                        lookup_state_reg <= LOOKUP_RX_RSP;
                    end
                end
                LOOKUP_RX_RSP: begin
                    if (lookup_rsp_fire) begin
                        lookup_state_reg <= LOOKUP_IDLE;
                    end
                end
                default: begin
                    lookup_state_reg <= LOOKUP_IDLE;
                end
            endcase
        end
    end

    always_ff @(posedge clk) begin : receive_path
        responder_if.req_valid <= rst ? '0 : ((rx_state_reg == RX_REQUEST)
                && !(responder_req_fire));
        responder_if.req_kind <= rst ? '0 : ((rx_cmd_reg[7:4] == 1 || rx_cmd_reg[7:4] == 2));
        responder_if.req_op <= rst ? '0 : ((rx_cmd_reg == RMEM_WRITE_REQ
                    || rx_cmd_reg == DMA_WRITE_REQ));
        responder_if.req_addr <= rst ? '0 : (rx_header_reg[5]);
        responder_if.req_len <= rst ? '0 : ((rx_cmd_reg[7:4] == 1
                    || rx_cmd_reg[7:4] == 2) ? 32'd4 : rx_length_reg);
        responder_if.req_biten <= rst ? '0 : (rx_header_reg[6]);
        responder_if.req_wdata <= rst ? '0 : (rx_header_reg[7]);
        responder_if.req_peer_idx <= rst ? '0 : rx_peer_reg;
        responder_if.req_sequence <= rst ? '0 : rx_sequence_reg;
        responder_if.req_last <= rst ? '0 : 1'b1;
        responder_if.req_error_code <= rst ? '0 : (responder_if.ERROR_W'(rx_error_reg));
        responder_if.req_rx_status <= rst ? '0 : (rx_cmd_reg == DMA_WRITE_REQ);
        responder_if.tx_status_valid <= 1'b0;
        responder_if.tx_status_peer_idx <= '0;
        responder_if.tx_status_sequence <= '0;
        responder_if.tx_status_len <= '0;
        responder_if.tx_status_error_code <= '0;
        responder_if.rx_status_valid <= rst ? '0 : ((rx_state_reg == RX_FINAL && !rx_own_reg
                    && !rx_hold_valid_reg && !rx_out_valid_reg)
                && !(responder_if.rx_status_valid && (responder_rx_status_fire)));
        responder_if.rx_status_peer_idx <= rst ? '0 : rx_peer_reg;
        responder_if.rx_status_sequence <= rst ? '0 : rx_sequence_reg;
        responder_if.rx_status_len <= rst ? '0 : rx_data_bytes_reg;
        responder_if.rx_status_error_code <= rst ? '0
            : (responder_if.ERROR_W'(rx_error_reg == 10 ? 4'd2 : rx_error_reg));
        responder_if.non_oetp_rx_claim_valid <= rst ? '0 : ((rx_state_reg == RX_RAW_CLAIM)
                && !(responder_non_oetp_rx_claim_fire));

        if (rst) begin
            rx_state_reg <= RX_IDLE;
            rx_header_count_reg <= 0;
            rx_meta_words_reg <= 0;
            rx_replay_reg <= 0;
            rx_cmd_reg <= 0;
            rx_local_mac_reg <= 0;
            rx_group_mac_reg <= 0;
            rx_receive_mode_reg <= 0;
            rx_route_reg <= 0;
            rx_peer_reg <= 0;
            rx_sequence_reg <= 0;
            rx_frame_bytes_reg <= 0;
            rx_logical_bytes_reg <= 0;
            rx_length_reg <= 0;
            rx_data_bytes_reg <= 0;
            rx_error_reg <= 0;
            rx_ended_reg <= 0;
            rx_own_reg <= 0;
            rx_request_sent_reg <= 0;
            rx_hold_data_reg <= 0;
            rx_hold_keep_reg <= 0;
            rx_hold_valid_reg <= 0;
            rx_hold_last_reg <= 0;
            rx_out_data_reg <= 0;
            rx_out_keep_reg <= 0;
            rx_out_valid_reg <= 0;
            rx_out_last_reg <= 0;
            for (int word_index = 0; word_index < 8; word_index++) begin
                rx_header_reg[word_index] <= 0;
                rx_header_keep_reg[word_index] <= 0;
                rx_header_last_reg[word_index] <= 0;
            end
        end else begin
            case (rx_state_reg)
                RX_IDLE: begin
                    if (rx_input_fire) begin
                        rx_state_reg <= eth_rx.tlast ? RX_CLASSIFY : RX_HEADER;
                    end
                end
                RX_HEADER: begin
                    if (rx_input_fire && (eth_rx.tlast || rx_header_count_reg == 3)) begin
                        rx_state_reg <= RX_CLASSIFY;
                    end
                end
                RX_CLASSIFY: begin
                    if (rx_protocol_header) begin
                        if (!rx_destination_matches || rx_source[40]
                            || !known_command(rx_header_reg[3][31:24]) || rx_ended_reg) begin
                            rx_state_reg <= RX_DROP;
                        end else begin
                            rx_state_reg <= RX_META;
                        end
                    end else if (!rx_raw_admitted) begin
                        rx_state_reg <= RX_DROP;
                    end else begin
                        rx_state_reg <= responder_if.non_oetp_rx_available ? RX_RAW_CLAIM
                            : RX_RAW_REPLAY;
                    end
                end
                RX_META: begin
                    if (rx_input_fire
                        && (eth_rx.tlast || rx_header_count_reg + 1 == rx_meta_words_reg)) begin
                        rx_state_reg <= response_command(rx_cmd_reg) ? RX_MATCH : RX_LOOKUP;
                    end
                end
                RX_MATCH: begin
                    if (!rx_response_matches) begin
                        rx_state_reg <= RX_DROP;
                    end else begin
                        rx_state_reg <= rx_cmd_reg == DMA_READ_RSP
                            ? (rx_ended_reg ? RX_VALIDATE : RX_DATA) : RX_TAIL;
                    end
                end
                RX_LOOKUP: begin
                    if (lookup_rx_req_fire) begin
                        rx_state_reg <= RX_LOOKUP_WAIT;
                    end
                end
                RX_LOOKUP_WAIT: begin
                    if (lookup_rx_rsp_fire) begin
                        rx_state_reg <= !peer_lookup_if.rsp_hit
                            || (rx_group
                                && !rx_write) ? RX_DROP : rx_cmd_reg == DMA_WRITE_REQ ? RX_ADMIT
                            : RX_TAIL;
                    end
                end
                RX_ADMIT: begin
                    rx_state_reg <= (responder_state_reg != RESPONDER_IDLE
                            || !responder_if.req_ready) ? RX_DROP : RX_REQUEST;
                end
                RX_REQUEST: begin
                    if (responder_req_fire) begin
                        rx_state_reg <= rx_cmd_reg == DMA_WRITE_REQ
                            ? (rx_ended_reg ? RX_VALIDATE : rx_error_reg != 0 ? RX_TAIL : RX_DATA)
                            : RX_IDLE;
                    end
                end
                RX_DATA: begin
                    if (rx_input_fire && (eth_rx.tlast || rx_data_bytes_reg + 4 >= rx_length_reg))
                    begin
                        rx_state_reg <= eth_rx.tlast ? RX_VALIDATE : RX_EOD;
                    end
                end
                RX_EOD: begin
                    if (rx_input_fire) begin
                        rx_state_reg <= eth_rx.tlast ? RX_VALIDATE : RX_TAIL;
                    end
                end
                RX_TAIL: begin
                    if (rx_ended_reg) begin
                        rx_state_reg <= RX_VALIDATE;
                    end
                end
                RX_VALIDATE: begin
                    rx_state_reg <= rx_is_response || rx_request_sent_reg ? RX_FINAL : RX_ADMIT;
                end
                RX_FINAL: begin
                    if (!rx_hold_valid_reg && !rx_out_valid_reg
                        && (rx_own_reg || (responder_rx_status_fire))) begin
                        rx_state_reg <= RX_IDLE;
                    end
                end
                RX_ABORT: begin
                    if (!rx_hold_valid_reg && !rx_out_valid_reg) begin
                        rx_state_reg <= RX_DROP;
                    end
                end
                RX_DROP: begin
                    if (rx_ended_reg || (rx_input_fire && eth_rx.tlast)) begin
                        rx_state_reg <= RX_IDLE;
                    end
                end
                RX_RAW_CLAIM: begin
                    if (responder_non_oetp_rx_claim_fire) begin
                        rx_state_reg <= RX_RAW_REPLAY;
                    end
                end
                RX_RAW_REPLAY: begin
                    if (rx_output_fire && rx_replay_reg + 1 == rx_header_count_reg) begin
                        rx_state_reg <= rx_ended_reg ? RX_RAW_FINISH : RX_RAW_STREAM;
                    end
                end
                RX_RAW_STREAM: begin
                    if (rx_input_fire && eth_rx.tlast) begin
                        rx_state_reg <= RX_RAW_FINISH;
                    end
                end
                RX_RAW_FINISH: begin
                    if (!rx_out_valid_reg) begin
                        rx_state_reg <= RX_IDLE;
                    end
                end
                default: begin
                    rx_state_reg <= RX_IDLE;
                end
            endcase

            if (rx_abort) begin
                rx_state_reg <= RX_ABORT;
            end

            if (rx_output_fire && rx_state_reg != RX_RAW_REPLAY) begin
                rx_out_valid_reg <= 0;
            end

            if (rx_input_fire) begin
                rx_frame_bytes_reg <= rx_frame_bytes_reg + byte_count(eth_rx.tkeep);
                if (eth_rx.tlast) begin
                    rx_ended_reg <= 1;
                end
                if (!keep_valid(eth_rx.tkeep) || (!eth_rx.tlast && eth_rx.tkeep != 4'hf)) begin
                    rx_error_reg <= rx_bulk ? 4'd10 : 4'd2;
                end
            end

            if (rx_state_reg == RX_IDLE && rx_input_fire) begin
                rx_header_reg[0] <= eth_rx.tdata;
                rx_header_keep_reg[0] <= eth_rx.tkeep;
                rx_header_last_reg[0] <= eth_rx.tlast;
                rx_header_count_reg <= 1;
                rx_frame_bytes_reg <= byte_count(eth_rx.tkeep);
                rx_ended_reg <= eth_rx.tlast;
                rx_error_reg <= !keep_valid(eth_rx.tkeep)
                    || (!eth_rx.tlast && eth_rx.tkeep != 4'hf) ? 4'd2 : 4'd0;
                rx_own_reg <= 0;
                rx_request_sent_reg <= 0;
                rx_data_bytes_reg <= 0;
                rx_length_reg <= 0;
                rx_peer_reg <= 0;
                rx_sequence_reg <= 0;
                rx_hold_valid_reg <= 0;
                rx_out_valid_reg <= 0;
                rx_replay_reg <= 0;
                for (int n = 1; n < 8; n++) begin
                    rx_header_reg[n] <= 0;
                    rx_header_keep_reg[n] <= 0;
                    rx_header_last_reg[n] <= 0;
                end
                rx_local_mac_reg <= {
                    endpoint_if.csr_to_core.config_.mac_address.hi_word.value,
                    endpoint_if.csr_to_core.config_.mac_address.lo_word.value
                };
                rx_group_mac_reg <= {
                    endpoint_if.csr_to_core.config_.multicast_address.hi_word.value,
                    endpoint_if.csr_to_core.config_.multicast_address.lo_word.value
                };
                rx_receive_mode_reg
                    <= endpoint_if.csr_to_core.config_.non_oetp_control.receive_mode.value;
            end

            if ((rx_state_reg == RX_HEADER || rx_state_reg == RX_META) && rx_input_fire) begin
                rx_header_reg[rx_header_count_reg[2:0]] <= eth_rx.tdata;
                rx_header_keep_reg[rx_header_count_reg[2:0]] <= eth_rx.tkeep;
                rx_header_last_reg[rx_header_count_reg[2:0]] <= eth_rx.tlast;
                rx_header_count_reg <= rx_header_count_reg + 1;
                if (rx_state_reg == RX_META && eth_rx.tlast
                    && rx_header_count_reg + 1 < rx_meta_words_reg) begin
                    rx_error_reg <= 2;
                end
            end

            if (rx_state_reg == RX_CLASSIFY) begin
                rx_cmd_reg <= rx_header_reg[3][31:24];
                rx_meta_words_reg <= metadata_words(rx_header_reg[3][31:24]);
                rx_logical_bytes_reg <= 32'(metadata_words(rx_header_reg[3][31:24])) * 4;
                rx_route_reg <= responder_if.non_oetp_rx_available ? initiator_if.ROUTE_NON_OETP_DMA
                    : initiator_if.ROUTE_DIRECT;
            end

            if (rx_state_reg == RX_MATCH && rx_response_matches && !rx_abort) begin
                rx_own_reg <= 1;
                rx_peer_reg <= initiator_context_reg.peer;
                rx_sequence_reg <= initiator_context_reg.sequence_;
                rx_route_reg <= initiator_if.ROUTE_PEER;
                rx_length_reg <= initiator_context_reg.len;
                if (rx_cmd_reg == DMA_READ_RSP) begin
                    rx_logical_bytes_reg <= 24 + ((initiator_context_reg.len + 3) & 32'hfffffffc);
                    if (rx_ended_reg) rx_error_reg <= 10;
                end
            end

            if (lookup_rx_rsp_fire && peer_lookup_if.rsp_hit) begin
                rx_peer_reg <= peer_lookup_if.rsp_peer_idx;
                rx_sequence_reg <= SEQ_W'(responder_sequence_reg);
                rx_length_reg <= rx_is_rmem ? 32'd4 : rx_header_reg[6];
                rx_route_reg <= initiator_if.ROUTE_PEER;
                if (rx_cmd_reg == DMA_WRITE_REQ) begin
                    rx_logical_bytes_reg <= 32 + ((rx_header_reg[6] + 3) & 32'hfffffffc);
                end
                if ((rx_is_rmem && (peer_lookup_if.rsp_dma_mode != 1 || rx_header_reg[5][1:0] != 0))
                    || (!rx_is_rmem && peer_lookup_if.rsp_dma_mode != (rx_write ? 2'd2 : 2'd3))
                    || (!rx_is_rmem && rx_header_reg[6] == 0)) begin
                    rx_error_reg <= 1;
                end else if (!rx_is_rmem && rx_header_reg[6] > 32'(MAX_FRAGMENT)) begin
                    rx_error_reg <= 3;
                end
            end

            if (rx_state_reg == RX_REQUEST && responder_req_fire) begin
                rx_request_sent_reg <= 1;
            end

            if (rx_state_reg == RX_DATA && rx_input_fire) begin
                if (rx_hold_valid_reg) begin
                    rx_out_data_reg <= rx_hold_data_reg;
                    rx_out_keep_reg <= rx_hold_keep_reg;
                    rx_out_last_reg <= 0;
                    rx_out_valid_reg <= 1;
                end
                rx_hold_data_reg <= eth_rx.tdata;
                rx_hold_keep_reg <= eth_rx.tkeep & byte_mask(rx_length_reg - rx_data_bytes_reg);
                rx_hold_valid_reg <= |(eth_rx.tkeep & byte_mask(rx_length_reg - rx_data_bytes_reg));
                rx_hold_last_reg <= eth_rx.tlast || rx_data_bytes_reg + 4 >= rx_length_reg;
                rx_data_bytes_reg <= rx_data_bytes_reg
                    + byte_count(eth_rx.tkeep & byte_mask(rx_length_reg - rx_data_bytes_reg));
                if (eth_rx.tlast) rx_error_reg <= 10;
            end

            if ((rx_state_reg == RX_EOD || rx_state_reg == RX_TAIL || rx_state_reg == RX_VALIDATE
                    || rx_state_reg == RX_FINAL || rx_state_reg == RX_ABORT) && rx_hold_valid_reg
                && !rx_out_valid_reg && (rx_hold_last_reg || rx_state_reg == RX_ABORT)) begin
                rx_out_data_reg <= rx_hold_data_reg;
                rx_out_keep_reg <= rx_hold_keep_reg;
                rx_out_last_reg <= 1;
                rx_out_valid_reg <= 1;
                rx_hold_valid_reg <= 0;
            end

            if (rx_state_reg == RX_EOD && rx_input_fire
                && (eth_rx.tdata != END_OF_DATA || eth_rx.tkeep != 4'hf)) begin
                rx_error_reg <= 10;
            end

            if (rx_state_reg == RX_VALIDATE && rx_error_reg == 0
                && (!frame_length_valid(rx_frame_bytes_reg, rx_logical_bytes_reg)
                    || rx_frame_bytes_reg > 32'(MAX_RAW_FRAME_SIZE))) begin
                rx_error_reg <= rx_bulk ? 4'd10 : 4'd2;
            end

            if (rx_state_reg == RX_RAW_REPLAY && rx_output_fire) begin
                rx_replay_reg <= rx_replay_reg + 1;
            end

            if (rx_state_reg == RX_RAW_STREAM && rx_input_fire) begin
                rx_out_data_reg <= eth_rx.tdata;
                rx_out_keep_reg <= eth_rx.tkeep;
                rx_out_last_reg <= eth_rx.tlast;
                rx_out_valid_reg <= 1;
            end
        end
    end

    always_ff @(posedge clk) begin : transmit_path
        if (rst) begin
            tx_state_reg <= TX_IDLE;
            tx_responder_reg <= 0;
            tx_bulk_reg <= 0;
            tx_raw_reg <= 0;
            tx_input_done_reg <= 0;
            tx_eth_done_reg <= 0;
            tx_proto_turn_reg <= 1;
            tx_no_frame_reg <= 0;
            tx_header_words_reg <= 0;
            tx_header_index_reg <= 0;
            tx_length_reg <= 0;
            tx_data_bytes_reg <= 0;
            tx_peer_reg <= 0;
            tx_sequence_reg <= 0;
            tx_last_reg <= 0;
            tx_fault_reg <= 0;
            tx_hold_data_reg <= 0;
            tx_hold_keep_reg <= 0;
            tx_hold_valid_reg <= 0;
            tx_out_data_reg <= 0;
            tx_out_keep_reg <= 0;
            tx_out_valid_reg <= 0;
            tx_out_last_reg <= 0;
            for (int word_index = 0; word_index < 8; word_index++) begin
                tx_header_reg[word_index] <= 0;
            end
        end else begin
            case (tx_state_reg)
                TX_IDLE: begin
                    if (tx_select_responder || tx_select_initiator) begin
                        if (tx_select_initiator && !initiator_context_reg.kind
                            && initiator_context_reg.op && initiator_source_done_reg
                            && initiator_source_error_reg != 0) begin
                            tx_state_reg <= initiator_source_len_reg != 0 ? TX_PRE_DRAIN
                                : TX_WAIT_END;
                        end else if (tx_selected_error && !responder_context_reg.kind
                            && !responder_context_reg.op && responder_completed_len_reg != 0) begin
                            tx_state_reg <= TX_PRE_DRAIN;
                        end else begin
                            tx_state_reg <= tx_selected_bulk ? TX_PRIME : TX_HEADER;
                        end
                    end else if (tx_select_raw) begin
                        tx_state_reg <= TX_RAW;
                    end
                end
                TX_PRE_DRAIN: begin
                    if (tx_stream_fire && local_tx.tlast) begin
                        tx_state_reg <= tx_no_frame_reg ? TX_WAIT_END : TX_HEADER;
                    end
                end
                TX_PRIME: begin
                    if (tx_stream_fire) begin
                        tx_state_reg <= TX_HEADER;
                    end
                end
                TX_HEADER: begin
                    if (tx_output_fire && tx_header_index_reg + 1 == tx_header_words_reg) begin
                        tx_state_reg <= tx_bulk_reg ? (tx_input_done_reg ? TX_STATUS : TX_DATA)
                            : TX_WAIT_END;
                    end
                end
                TX_DATA: begin
                    if (tx_source_done && tx_source_error != 0 && !tx_out_valid_reg) begin
                        tx_state_reg <= TX_ERROR_FLUSH;
                    end else if (tx_input_done_reg && !tx_out_valid_reg) begin
                        tx_state_reg <= TX_STATUS;
                    end
                end
                TX_STATUS: begin
                    if (tx_source_done) begin
                        tx_state_reg <= tx_final_error != 0 ? TX_ERROR_FLUSH : TX_FLUSH;
                    end
                end
                TX_FLUSH: begin
                    if (tx_output_fire) begin
                        tx_state_reg <= TX_EOD;
                    end
                end
                TX_EOD: begin
                    if (tx_output_fire) begin
                        tx_state_reg <= TX_WAIT_END;
                    end
                end
                TX_ERROR_FLUSH: begin
                    if (tx_output_fire) begin
                        tx_state_reg <= tx_input_done_reg ? TX_WAIT_END : TX_DRAIN;
                    end
                end
                TX_DRAIN: begin
                    if (tx_input_done_reg) begin
                        tx_state_reg <= TX_WAIT_END;
                    end
                end
                TX_WAIT_END: begin
                    if (tx_done) begin
                        tx_state_reg <= TX_IDLE;
                    end
                end
                TX_RAW: begin
                    if (tx_output_fire && tx_out_last_reg) begin
                        tx_state_reg <= TX_WAIT_END;
                    end
                end
                default: begin
                    tx_state_reg <= TX_IDLE;
                end
            endcase

            if (tx_state_reg == TX_IDLE) begin
                tx_eth_done_reg <= 0;
                tx_fault_reg <= 0;
                tx_input_done_reg <= 0;
                tx_hold_valid_reg <= 0;
                tx_out_valid_reg <= 0;
                tx_data_bytes_reg <= 0;
                tx_header_index_reg <= 0;

                if (tx_select_responder || tx_select_initiator) begin
                    tx_responder_reg <= tx_select_responder;
                    tx_bulk_reg <= tx_selected_bulk;
                    tx_raw_reg <= 0;
                    tx_length_reg <= tx_selected_context.len;
                    tx_no_frame_reg <= tx_select_initiator && tx_selected_bulk
                        && initiator_source_done_reg && initiator_source_error_reg != 0;

                    if (tx_select_initiator && tx_selected_bulk && initiator_source_done_reg
                        && initiator_source_error_reg != 0 && initiator_source_len_reg == 0) begin
                        tx_eth_done_reg <= 1;
                        tx_input_done_reg <= 1;
                    end

                    tx_peer_reg <= tx_selected_context.peer;
                    tx_sequence_reg <= tx_selected_context.sequence_;
                    tx_last_reg <= tx_selected_context.last;
                    tx_header_words_reg <= metadata_words(tx_selected_cmd);
                    tx_header_reg[0] <= {
                        tx_selected_context.mac[23:16],
                        tx_selected_context.mac[31:24],
                        tx_selected_context.mac[39:32],
                        tx_selected_context.mac[47:40]
                    };
                    tx_header_reg[1] <= {
                        tx_selected_context.local_mac[39:32],
                        tx_selected_context.local_mac[47:40],
                        tx_selected_context.mac[7:0],
                        tx_selected_context.mac[15:8]
                    };
                    tx_header_reg[2] <= {
                        tx_selected_context.local_mac[7:0],
                        tx_selected_context.local_mac[15:8],
                        tx_selected_context.local_mac[23:16],
                        tx_selected_context.local_mac[31:24]
                    };
                    tx_header_reg[3] <= {tx_selected_cmd, 24'h0eb588};
                    tx_header_reg[4] <= tx_selected_context.id;
                    tx_header_reg[5] <= tx_select_responder ?
                        (tx_selected_error ? {28'd0, responder_error_reg} : responder_result_reg) :
                        tx_selected_context.addr;
                    tx_header_reg[6] <= tx_selected_context.kind ? tx_selected_context.biten
                        : tx_selected_context.len;
                    tx_header_reg[7] <= tx_selected_context.data;

                    if (tx_selected_bulk) begin
                        tx_header_words_reg <= tx_select_responder ? 5 : 7;
                    end

                    tx_proto_turn_reg <= 0;
                end else if (tx_select_raw) begin
                    tx_bulk_reg <= 0;
                    tx_responder_reg <= 0;
                    tx_raw_reg <= 1;
                    tx_proto_turn_reg <= 1;
                end
            end

            if (tx_wire_end && tx_state_reg != TX_IDLE) begin
                tx_eth_done_reg <= 1;
            end

            if (tx_state_reg == TX_HEADER && tx_output_fire) begin
                tx_header_index_reg <= tx_header_index_reg + 1;
            end

            if ((tx_state_reg == TX_DATA || tx_state_reg == TX_RAW) && tx_output_fire) begin
                tx_out_valid_reg <= 0;
            end

            if ((tx_state_reg == TX_PRIME || tx_state_reg == TX_DATA) && tx_stream_fire) begin
                if (tx_state_reg == TX_DATA && tx_hold_valid_reg) begin
                    tx_out_data_reg <= tx_hold_data_reg;
                    tx_out_keep_reg <= tx_hold_keep_reg;
                    tx_out_valid_reg <= 1;
                end

                tx_hold_data_reg <= local_tx.tdata;
                tx_hold_keep_reg <= local_tx.tkeep;
                tx_hold_valid_reg <= 1;
                tx_data_bytes_reg <= tx_data_bytes_reg + byte_count(local_tx.tkeep);
                tx_input_done_reg <= local_tx.tlast;

                if (!local_matches_tx || local_tx.tuser[0] != tx_last_reg
                    || !keep_valid(local_tx.tkeep) || (!local_tx.tlast && local_tx.tkeep != 4'hf)
                    || (local_tx.tlast
                        && tx_data_bytes_reg + byte_count(local_tx.tkeep) != tx_length_reg)
                    || (!local_tx.tlast
                        && tx_data_bytes_reg + byte_count(local_tx.tkeep) >= tx_length_reg)) begin
                    tx_fault_reg <= 2;
                end
            end

            if ((tx_state_reg == TX_DRAIN || tx_state_reg == TX_PRE_DRAIN) && tx_stream_fire
                && local_tx.tlast) begin
                tx_input_done_reg <= 1;
                if (tx_no_frame_reg) tx_eth_done_reg <= 1;
            end

            if ((tx_state_reg == TX_FLUSH || tx_state_reg == TX_ERROR_FLUSH) && tx_output_fire)
            begin
                tx_hold_valid_reg <= 0;
            end

            if (tx_state_reg == TX_RAW && tx_stream_fire) begin
                tx_out_data_reg <= local_tx.tdata;
                tx_out_keep_reg <= local_tx.tkeep;
                tx_out_last_reg <= local_tx.tlast;
                tx_out_valid_reg <= 1;

                if (local_tx.tlast) begin
                    tx_input_done_reg <= 1;
                end
            end
        end
    end

    always_comb begin : receive_and_transmit_muxes
        eth_rx.tready = 1'b0;

        case (rx_state_reg)
            RX_IDLE, RX_HEADER, RX_META, RX_EOD: begin
                eth_rx.tready = 1'b1;
            end
            RX_DROP: begin
                eth_rx.tready = !rx_ended_reg;
            end
            RX_TAIL: begin
                eth_rx.tready = !rx_ended_reg;
            end
            RX_DATA: begin
                eth_rx.tready = !rx_hold_valid_reg || !rx_out_valid_reg;
            end
            RX_RAW_STREAM: begin
                eth_rx.tready = !rx_out_valid_reg;
            end
            default: begin
            end
        endcase

        local_rx.tdata = rx_out_data_reg;
        local_rx.tkeep = rx_out_keep_reg;
        local_rx.tstrb = rx_out_keep_reg;
        local_rx.tlast = rx_out_last_reg;
        local_rx.tvalid = rx_out_valid_reg;
        local_rx.tid = rx_sequence_reg;
        local_rx.tdest = {rx_route_reg, rx_peer_reg};
        local_rx.tuser = {rx_request_sent_reg, rx_own_reg ? initiator_context_reg.last : 1'b1};

        if (rx_route_reg != initiator_if.ROUTE_PEER) begin
            local_rx.tid = '0;
            local_rx.tuser = '0;
        end

        if (rx_state_reg == RX_RAW_REPLAY) begin
            local_rx.tdata = rx_header_reg[rx_replay_reg[2:0]];
            local_rx.tkeep = rx_header_keep_reg[rx_replay_reg[2:0]];
            local_rx.tstrb = rx_header_keep_reg[rx_replay_reg[2:0]];
            local_rx.tlast = rx_header_last_reg[rx_replay_reg[2:0]];
            local_rx.tvalid = 1'b1;
        end

        eth_tx.tdata = '0;
        eth_tx.tkeep = 4'hf;
        eth_tx.tstrb = 4'hf;
        eth_tx.tlast = 1'b0;
        eth_tx.tvalid = 1'b0;
        eth_tx.tid = '0;
        eth_tx.tdest = '0;
        eth_tx.tuser = '0;
        local_tx.tready = 1'b0;

        case (tx_state_reg)
            TX_PRIME: begin
                local_tx.tready = 1'b1;
            end
            TX_HEADER: begin
                eth_tx.tdata = tx_header_reg[tx_header_index_reg[2:0]];
                eth_tx.tvalid = 1'b1;
                eth_tx.tlast = !tx_bulk_reg && tx_header_index_reg + 1 == tx_header_words_reg;
            end
            TX_DATA: begin
                eth_tx.tdata = tx_out_data_reg;
                eth_tx.tkeep = tx_out_keep_reg;
                eth_tx.tstrb = tx_out_keep_reg;
                eth_tx.tvalid = tx_out_valid_reg;
                local_tx.tready = !tx_input_done_reg && !tx_out_valid_reg;
            end
            TX_FLUSH, TX_ERROR_FLUSH: begin
                eth_tx.tdata = masked_word(tx_hold_data_reg, tx_hold_keep_reg);
                eth_tx.tvalid = tx_hold_valid_reg;
                eth_tx.tlast = tx_state_reg == TX_ERROR_FLUSH;
                eth_tx.tkeep = tx_state_reg == TX_ERROR_FLUSH ? tx_hold_keep_reg : 4'hf;
                eth_tx.tstrb = eth_tx.tkeep;
            end
            TX_EOD: begin
                eth_tx.tdata = END_OF_DATA;
                eth_tx.tvalid = 1'b1;
                eth_tx.tlast = 1'b1;
            end
            TX_DRAIN, TX_PRE_DRAIN: begin
                local_tx.tready = 1'b1;
            end
            TX_RAW: begin
                eth_tx.tdata = tx_out_data_reg;
                eth_tx.tkeep = tx_out_keep_reg;
                eth_tx.tstrb = tx_out_keep_reg;
                eth_tx.tlast = tx_out_last_reg;
                eth_tx.tvalid = tx_out_valid_reg;
                local_tx.tready = !tx_out_valid_reg && !tx_input_done_reg;
            end
            default: begin
            end
        endcase
    end

endmodule

`resetall
