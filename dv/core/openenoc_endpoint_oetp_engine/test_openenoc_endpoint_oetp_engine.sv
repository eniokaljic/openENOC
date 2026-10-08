// SPDX-FileCopyrightText: 2026 Enio Kaljic
// SPDX-License-Identifier: AGPL-3.0-or-later

`timescale 1ns / 1ps
`default_nettype none

/* Isolated oETP transport wrapper. */
module test_openenoc_endpoint_oetp_engine #(
    parameter int LOCAL_DATA_W = 32,
    ETH_DATA_W = 32, MAX_RAW_FRAME_SIZE = 8192) ();
    logic clk, rst;
    logic [47:0] mac_address, multicast_address;
    logic [31:0] rmem_timeout, dma_timeout;
    logic [1:0] receive_mode;
    logic [191:0] peer_mac;

    openenoc_endpoint_if #(
        .NUM_OF_PEERS(4),
        .RMEM_TOTAL_DEPTH(256)
    ) endpoint_if (
        .clk(clk),
        .rst(rst)
    );

    openenoc_peer_lookup_if #(
        .NUM_OF_PEERS(4),
        .PEER_IDX_W(2)
    ) peer_lookup_if();

    openenoc_dma_transfer_if #(
        .PEER_IDX_W(2)
    ) initiator_if(), responder_if();

    logic initiator_req_valid;
    assign initiator_if.req_valid = initiator_req_valid;
    wire initiator_req_ready;
    assign initiator_req_ready = initiator_if.req_ready;
    logic initiator_req_kind;
    assign initiator_if.req_kind = initiator_req_kind;
    logic initiator_req_op;
    assign initiator_if.req_op = initiator_req_op;
    logic [31:0] initiator_req_addr;
    assign initiator_if.req_addr = initiator_req_addr;
    logic [31:0] initiator_req_len;
    assign initiator_if.req_len = initiator_req_len;
    logic [1:0] initiator_req_peer_idx;
    assign initiator_if.req_peer_idx = initiator_req_peer_idx;
    logic [31:0] initiator_req_sequence;
    assign initiator_if.req_sequence = initiator_req_sequence;
    logic initiator_req_last;
    assign initiator_if.req_last = initiator_req_last;
    logic [31:0] initiator_req_biten;
    assign initiator_if.req_biten = initiator_req_biten;
    logic [31:0] initiator_req_wdata;
    assign initiator_if.req_wdata = initiator_req_wdata;
    logic [3:0] initiator_req_error_code;
    assign initiator_if.req_error_code = initiator_req_error_code;
    logic initiator_req_rx_status;
    assign initiator_if.req_rx_status = initiator_req_rx_status;
    wire initiator_cpl_valid;
    assign initiator_cpl_valid = initiator_if.cpl_valid;
    logic initiator_cpl_ready;
    assign initiator_if.cpl_ready = initiator_cpl_ready;
    wire initiator_cpl_kind;
    assign initiator_cpl_kind = initiator_if.cpl_kind;
    wire initiator_cpl_op;
    assign initiator_cpl_op = initiator_if.cpl_op;
    wire [1:0] initiator_cpl_peer_idx;
    assign initiator_cpl_peer_idx = initiator_if.cpl_peer_idx;
    wire [31:0] initiator_cpl_sequence;
    assign initiator_cpl_sequence = initiator_if.cpl_sequence;
    wire initiator_cpl_last;
    assign initiator_cpl_last = initiator_if.cpl_last;
    wire [31:0] initiator_cpl_transferred_len;
    assign initiator_cpl_transferred_len = initiator_if.cpl_transferred_len;
    wire initiator_cpl_error;
    assign initiator_cpl_error = initiator_if.cpl_error;
    wire [3:0] initiator_cpl_error_code;
    assign initiator_cpl_error_code = initiator_if.cpl_error_code;
    wire [31:0] initiator_cpl_rdata;
    assign initiator_cpl_rdata = initiator_if.cpl_rdata;
    logic initiator_tx_status_valid;
    assign initiator_if.tx_status_valid = initiator_tx_status_valid;
    wire initiator_tx_status_ready;
    assign initiator_tx_status_ready = initiator_if.tx_status_ready;
    logic [1:0] initiator_tx_status_peer_idx;
    assign initiator_if.tx_status_peer_idx = initiator_tx_status_peer_idx;
    logic [31:0] initiator_tx_status_sequence;
    assign initiator_if.tx_status_sequence = initiator_tx_status_sequence;
    logic [31:0] initiator_tx_status_len;
    assign initiator_if.tx_status_len = initiator_tx_status_len;
    logic [3:0] initiator_tx_status_error_code;
    assign initiator_if.tx_status_error_code = initiator_tx_status_error_code;
    logic initiator_rx_status_valid;
    assign initiator_if.rx_status_valid = initiator_rx_status_valid;
    wire initiator_rx_status_ready;
    assign initiator_rx_status_ready = initiator_if.rx_status_ready;
    logic [1:0] initiator_rx_status_peer_idx;
    assign initiator_if.rx_status_peer_idx = initiator_rx_status_peer_idx;
    logic [31:0] initiator_rx_status_sequence;
    assign initiator_if.rx_status_sequence = initiator_rx_status_sequence;
    logic [31:0] initiator_rx_status_len;
    assign initiator_if.rx_status_len = initiator_rx_status_len;
    logic [3:0] initiator_rx_status_error_code;
    assign initiator_if.rx_status_error_code = initiator_rx_status_error_code;
    wire responder_req_valid;
    assign responder_req_valid = responder_if.req_valid;
    logic responder_req_ready;
    assign responder_if.req_ready = responder_req_ready;
    wire responder_req_kind;
    assign responder_req_kind = responder_if.req_kind;
    wire responder_req_op;
    assign responder_req_op = responder_if.req_op;
    wire [31:0] responder_req_addr;
    assign responder_req_addr = responder_if.req_addr;
    wire [31:0] responder_req_len;
    assign responder_req_len = responder_if.req_len;
    wire [1:0] responder_req_peer_idx;
    assign responder_req_peer_idx = responder_if.req_peer_idx;
    wire [31:0] responder_req_sequence;
    assign responder_req_sequence = responder_if.req_sequence;
    wire responder_req_last;
    assign responder_req_last = responder_if.req_last;
    wire [31:0] responder_req_biten;
    assign responder_req_biten = responder_if.req_biten;
    wire [31:0] responder_req_wdata;
    assign responder_req_wdata = responder_if.req_wdata;
    wire [3:0] responder_req_error_code;
    assign responder_req_error_code = responder_if.req_error_code;
    wire responder_req_rx_status;
    assign responder_req_rx_status = responder_if.req_rx_status;
    logic responder_cpl_valid;
    assign responder_if.cpl_valid = responder_cpl_valid;
    wire responder_cpl_ready;
    assign responder_cpl_ready = responder_if.cpl_ready;
    logic responder_cpl_kind;
    assign responder_if.cpl_kind = responder_cpl_kind;
    logic responder_cpl_op;
    assign responder_if.cpl_op = responder_cpl_op;
    logic [1:0] responder_cpl_peer_idx;
    assign responder_if.cpl_peer_idx = responder_cpl_peer_idx;
    logic [31:0] responder_cpl_sequence;
    assign responder_if.cpl_sequence = responder_cpl_sequence;
    logic responder_cpl_last;
    assign responder_if.cpl_last = responder_cpl_last;
    logic [31:0] responder_cpl_transferred_len;
    assign responder_if.cpl_transferred_len = responder_cpl_transferred_len;
    logic responder_cpl_error;
    assign responder_if.cpl_error = responder_cpl_error;
    logic [3:0] responder_cpl_error_code;
    assign responder_if.cpl_error_code = responder_cpl_error_code;
    logic [31:0] responder_cpl_rdata;
    assign responder_if.cpl_rdata = responder_cpl_rdata;
    wire responder_tx_status_valid;
    assign responder_tx_status_valid = responder_if.tx_status_valid;
    logic responder_tx_status_ready;
    assign responder_if.tx_status_ready = responder_tx_status_ready;
    wire [1:0] responder_tx_status_peer_idx;
    assign responder_tx_status_peer_idx = responder_if.tx_status_peer_idx;
    wire [31:0] responder_tx_status_sequence;
    assign responder_tx_status_sequence = responder_if.tx_status_sequence;
    wire [31:0] responder_tx_status_len;
    assign responder_tx_status_len = responder_if.tx_status_len;
    wire [3:0] responder_tx_status_error_code;
    assign responder_tx_status_error_code = responder_if.tx_status_error_code;
    wire responder_rx_status_valid;
    assign responder_rx_status_valid = responder_if.rx_status_valid;
    logic responder_rx_status_ready;
    assign responder_if.rx_status_ready = responder_rx_status_ready;
    wire [1:0] responder_rx_status_peer_idx;
    assign responder_rx_status_peer_idx = responder_if.rx_status_peer_idx;
    wire [31:0] responder_rx_status_sequence;
    assign responder_rx_status_sequence = responder_if.rx_status_sequence;
    wire [31:0] responder_rx_status_len;
    assign responder_rx_status_len = responder_if.rx_status_len;
    wire [3:0] responder_rx_status_error_code;
    assign responder_rx_status_error_code = responder_if.rx_status_error_code;
    wire lookup_req_valid;
    assign lookup_req_valid = peer_lookup_if.req_valid;
    logic lookup_req_ready;
    assign peer_lookup_if.req_ready = lookup_req_ready;
    wire [1:0] lookup_req_type;
    assign lookup_req_type = peer_lookup_if.req_type;
    wire [3:0] lookup_req_mode_mask;
    assign lookup_req_mode_mask = peer_lookup_if.req_mode_mask;
    wire [1:0] lookup_req_peer_idx;
    assign lookup_req_peer_idx = peer_lookup_if.req_peer_idx;
    wire [31:0] lookup_req_rmem_addr;
    assign lookup_req_rmem_addr = peer_lookup_if.req_rmem_addr;
    wire [47:0] lookup_req_mac_addr;
    assign lookup_req_mac_addr = peer_lookup_if.req_mac_addr;
    logic lookup_rsp_valid;
    assign peer_lookup_if.rsp_valid = lookup_rsp_valid;
    wire lookup_rsp_ready;
    assign lookup_rsp_ready = peer_lookup_if.rsp_ready;
    logic lookup_rsp_hit;
    assign peer_lookup_if.rsp_hit = lookup_rsp_hit;
    logic [1:0] lookup_rsp_peer_idx;
    assign peer_lookup_if.rsp_peer_idx = lookup_rsp_peer_idx;
    logic [47:0] lookup_rsp_mac_addr;
    assign peer_lookup_if.rsp_mac_addr = lookup_rsp_mac_addr;
    logic [31:0] lookup_rsp_rmem_offset;
    assign peer_lookup_if.rsp_rmem_offset = lookup_rsp_rmem_offset;
    logic [31:0] lookup_rsp_local_addr;
    assign peer_lookup_if.rsp_local_addr = lookup_rsp_local_addr;
    logic [31:0] lookup_rsp_remote_addr;
    assign peer_lookup_if.rsp_remote_addr = lookup_rsp_remote_addr;
    logic [31:0] lookup_rsp_size;
    assign peer_lookup_if.rsp_size = lookup_rsp_size;
    logic [1:0] lookup_rsp_dma_mode;
    assign peer_lookup_if.rsp_dma_mode = lookup_rsp_dma_mode;
    logic lookup_rsp_irq_enable;
    assign peer_lookup_if.rsp_irq_enable = lookup_rsp_irq_enable;
    logic raw_available, raw_claim_ready;
    wire raw_claim_valid;
    assign responder_if.non_oetp_rx_available = raw_available;
    assign responder_if.non_oetp_rx_claim_ready = raw_claim_ready;
    assign raw_claim_valid = responder_if.non_oetp_rx_claim_valid;
    always_comb begin
        endpoint_if.csr_to_core = '{default: '0};
        endpoint_if.csr_to_core.config_.mac_address.hi_word.value = mac_address[47:32];
        endpoint_if.csr_to_core.config_.mac_address.lo_word.value = mac_address[31:0];
        endpoint_if.csr_to_core.config_.multicast_address.hi_word.value = multicast_address[47:32];
        endpoint_if.csr_to_core.config_.multicast_address.lo_word.value = multicast_address[31:0];
        endpoint_if.csr_to_core.config_.rmem_timeout.cycles.value = rmem_timeout;
        endpoint_if.csr_to_core.config_.dma_timeout.cycles.value = dma_timeout;
        endpoint_if.csr_to_core.config_.non_oetp_control.receive_mode.value = receive_mode;
        for (int n = 0; n < 4; n++) begin
            endpoint_if.csr_to_core.peers.entry[n].mac_address.hi_word.value =
                peer_mac[n*48+32+:16];
            endpoint_if.csr_to_core.peers.entry[n].mac_address.lo_word.value = peer_mac[n*48+:32];
        end
    end

    taxi_axis_if #(
        .DATA_W(LOCAL_DATA_W),
        .KEEP_EN(1),
        .LAST_EN(1),
        .ID_EN(1),
        .DEST_EN(1),
        .USER_EN(1),
        .ID_W(32),
        .DEST_W(4),
        .USER_W(2)
    ) local_tx_if();

    taxi_axis_if #(
        .DATA_W(LOCAL_DATA_W),
        .KEEP_EN(1),
        .LAST_EN(1),
        .ID_EN(1),
        .DEST_EN(1),
        .USER_EN(1),
        .ID_W(32),
        .DEST_W(4),
        .USER_W(2)
    ) local_rx_if();

    taxi_axis_if #(
        .DATA_W(ETH_DATA_W),
        .KEEP_EN(1),
        .LAST_EN(1)
    ) eth_rx_if();

    taxi_axis_if #(
        .DATA_W(ETH_DATA_W),
        .KEEP_EN(1),
        .LAST_EN(1)
    ) eth_tx_if();

    openenoc_endpoint_oetp_engine #(
        .MAX_RAW_FRAME_SIZE(MAX_RAW_FRAME_SIZE)
    ) dut (
        .clk(clk),
        .rst(rst),
        .endpoint_if(endpoint_if),
        .s_axis_local(local_tx_if),
        .m_axis_local(local_rx_if),
        .s_axis_eth(eth_rx_if),
        .m_axis_eth(eth_tx_if),
        .peer_lookup_if(peer_lookup_if),
        .initiator_if(initiator_if),
        .responder_if(responder_if)
    );

endmodule
`resetall
