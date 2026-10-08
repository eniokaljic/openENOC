// SPDX-FileCopyrightText: 2026 Enio Kaljic
// SPDX-License-Identifier: AGPL-3.0-or-later

`resetall
`timescale 1ns / 1ps
`default_nettype none

/* Isolated test wrapper for the openENOC endpoint DMA engine */
module test_openenoc_endpoint_dma_engine #(
    parameter int NUM_OF_PEERS = 4,
    parameter int AXI_DATA_W = 32,
    parameter int AXI_ADDR_W = 32,
    parameter int AXI_ID_W = 8,
    parameter int SEQUENCE_W = 32,
    parameter int FRAGMENT_SLOTS = 8,
    parameter int MAX_RAW_FRAME_SIZE = 96
) ();

    localparam int PEER_IDX_W = NUM_OF_PEERS > 1 ? $clog2(NUM_OF_PEERS) : 1;

    logic clk;
    logic rst;
    logic [31:0] dma_max_fragment_size_bytes;

    logic [31:0] non_tx_buffer_address;
    logic [31:0] non_tx_frame_length;
    logic non_tx_request;
    logic non_tx_clear_errors;
    wire non_tx_request_hwclr;
    wire non_tx_clear_errors_hwclr;
    wire non_tx_idle;
    wire non_tx_done;
    wire non_tx_error;
    wire [3:0] non_tx_error_code;
    wire [31:0] non_tx_transferred_length;

    logic [31:0] non_rx_buffer_address;
    logic [31:0] non_rx_buffer_capacity;
    logic non_rx_request;
    logic non_rx_clear_errors;
    wire non_rx_request_hwclr;
    wire non_rx_clear_errors_hwclr;
    wire non_rx_idle;
    wire non_rx_armed;
    wire non_rx_done;
    wire non_rx_error;
    wire [3:0] non_rx_error_code;
    wire [31:0] non_rx_received_length;

    logic [NUM_OF_PEERS*AXI_ADDR_W-1:0] peer_local_address;
    logic [NUM_OF_PEERS*AXI_ADDR_W-1:0] peer_remote_address;
    logic [NUM_OF_PEERS*AXI_ADDR_W-1:0] peer_size;
    logic [NUM_OF_PEERS*2-1:0] peer_dma_mode;
    logic [NUM_OF_PEERS-1:0] peer_irq_enable;
    logic [NUM_OF_PEERS-1:0] peer_request;
    logic [NUM_OF_PEERS-1:0] peer_clear_error;
    wire [NUM_OF_PEERS-1:0] peer_request_hwclr;
    wire [NUM_OF_PEERS-1:0] peer_clear_error_hwclr;
    wire [NUM_OF_PEERS-1:0] peer_idle;
    wire [NUM_OF_PEERS-1:0] peer_done;
    wire [NUM_OF_PEERS-1:0] peer_error;
    wire [NUM_OF_PEERS*4-1:0] peer_error_code;
    logic rmem_error_valid;
    logic [PEER_IDX_W-1:0] rmem_error_peer_idx;
    logic [3:0] rmem_error_code;
    logic wire_error_enable;
    logic [31:0] wire_error_code;
    wire [3:0] wire_error_csr_code;

    wire peer_lookup_req_valid;
    logic peer_lookup_req_ready;
    wire [1:0] peer_lookup_req_type;
    wire [3:0] peer_lookup_req_mode_mask;
    wire [PEER_IDX_W-1:0] peer_lookup_req_peer_idx;
    wire [AXI_ADDR_W-1:0] peer_lookup_req_rmem_addr;
    wire [47:0] peer_lookup_req_mac_addr;
    logic peer_lookup_rsp_valid;
    wire peer_lookup_rsp_ready;
    logic peer_lookup_rsp_hit;
    logic [PEER_IDX_W-1:0] peer_lookup_rsp_peer_idx;
    logic [47:0] peer_lookup_rsp_mac_addr;
    logic [AXI_ADDR_W-1:0] peer_lookup_rsp_rmem_offset;
    logic [AXI_ADDR_W-1:0] peer_lookup_rsp_local_addr;
    logic [AXI_ADDR_W-1:0] peer_lookup_rsp_remote_addr;
    logic [AXI_ADDR_W-1:0] peer_lookup_rsp_size;
    logic [1:0] peer_lookup_rsp_dma_mode;
    logic peer_lookup_rsp_irq_enable;

    wire initiator_req_valid;
    logic initiator_req_ready;
    wire initiator_req_op;
    wire initiator_req_kind;
    wire [AXI_ADDR_W-1:0] initiator_req_addr;
    wire [31:0] initiator_req_len;
    wire [PEER_IDX_W-1:0] initiator_req_peer_idx;
    wire [SEQUENCE_W-1:0] initiator_req_sequence;
    wire initiator_req_last;
    logic initiator_cpl_valid;
    wire initiator_cpl_ready;
    logic initiator_cpl_op;
    logic initiator_cpl_kind;
    logic [31:0] initiator_cpl_transferred_len;
    logic [PEER_IDX_W-1:0] initiator_cpl_peer_idx;
    logic [SEQUENCE_W-1:0] initiator_cpl_sequence;
    logic initiator_cpl_last;
    logic initiator_cpl_error;
    logic [3:0] initiator_cpl_error_code;

    logic responder_req_valid;
    wire responder_req_ready;
    logic responder_req_op;
    logic responder_req_kind;
    logic [31:0] responder_req_biten, responder_req_wdata;
    logic [AXI_ADDR_W-1:0] responder_req_addr;
    logic [31:0] responder_req_len;
    logic [PEER_IDX_W-1:0] responder_req_peer_idx;
    logic [SEQUENCE_W-1:0] responder_req_sequence;
    logic responder_req_last;
    wire responder_cpl_valid;
    logic responder_cpl_ready;
    wire responder_cpl_op;
    wire responder_cpl_kind;
    wire [31:0] responder_cpl_rdata;
    wire [31:0] responder_cpl_transferred_len;
    wire [PEER_IDX_W-1:0] responder_cpl_peer_idx;
    wire [SEQUENCE_W-1:0] responder_cpl_sequence;
    wire responder_cpl_last;
    wire responder_cpl_error;
    wire [3:0] responder_cpl_error_code;

    wire non_oetp_rx_available;
    logic non_oetp_rx_claim_valid;
    wire non_oetp_rx_claim_ready;

    wire [2:0] irq_admit_valid;
    logic [2:0] irq_admit_ready;
    wire [11:0] irq_admit_source;
    wire [2:0] irq_admit_enable;
    logic [2:0] irq_admit_reserved;
    wire [2:0] irq_commit_valid;
    logic [2:0] irq_commit_ready;
    wire [11:0] irq_commit_source;
    wire [3*PEER_IDX_W-1:0] irq_commit_peer_idx;
    logic [5:0] event_enable;
    wire responder_irq_admit_valid, responder_irq_admit_enable;
    wire [3:0] responder_irq_admit_source;
    logic responder_irq_admit_ready;
    wire responder_irq_commit_valid;
    wire [3:0] responder_irq_commit_source;
    wire [PEER_IDX_W-1:0] responder_irq_commit_peer_idx;
    logic responder_irq_commit_ready;

    openenoc_endpoint_if #(
        .RMEM_TOTAL_DEPTH(256),
        .NUM_OF_PEERS(NUM_OF_PEERS)
    ) endpoint_if (
        .clk(clk),
        .rst(rst)
    );

    openenoc_peer_lookup_if #(
        .NUM_OF_PEERS(NUM_OF_PEERS),
        .PEER_IDX_W(PEER_IDX_W),
        .ADDR_W(AXI_ADDR_W)
    ) peer_lookup_if();

    openenoc_dma_transfer_if #(
        .ADDR_W(AXI_ADDR_W),
        .LEN_W(32),
        .PEER_IDX_W(PEER_IDX_W),
        .SEQUENCE_W(SEQUENCE_W),
        .ERROR_W(4)
    ) initiator_if();

    openenoc_dma_transfer_if #(
        .ADDR_W(AXI_ADDR_W),
        .LEN_W(32),
        .PEER_IDX_W(PEER_IDX_W),
        .SEQUENCE_W(SEQUENCE_W),
        .ERROR_W(4)
    ) responder_if();

    openenoc_irq_event_if #(
        .PEER_IDX_W(PEER_IDX_W)
    ) irq_event_if[3]();

    taxi_axis_if #(
        .DATA_W(AXI_DATA_W),
        .KEEP_EN(1'b1),
        .LAST_EN(1'b1),
        .ID_EN(1'b1),
        .ID_W(SEQUENCE_W),
        .DEST_EN(1'b1),
        .DEST_W(PEER_IDX_W + 2),
        .USER_EN(1'b1),
        .USER_W(initiator_if.AXIS_USER_W)
    ) m_axis_oetp_if();

    taxi_axis_if #(
        .DATA_W(AXI_DATA_W),
        .KEEP_EN(1'b1),
        .LAST_EN(1'b1),
        .ID_EN(1'b1),
        .ID_W(SEQUENCE_W),
        .DEST_EN(1'b1),
        .DEST_W(PEER_IDX_W + 2),
        .USER_EN(1'b1),
        .USER_W(initiator_if.AXIS_USER_W)
    ) s_axis_oetp_if();

    taxi_axi_if #(
        .DATA_W(AXI_DATA_W),
        .ADDR_W(AXI_ADDR_W),
        .ID_W(AXI_ID_W)
    ) m_axi_if();

    always_comb begin
        endpoint_if.csr_to_core = '{default: '0};
        endpoint_if.csr_to_core.config_.dma_max_fragment_size.bytes.value =
            dma_max_fragment_size_bytes;
        endpoint_if.csr_to_core.irq.event_enable.peer_dma_complete.value = event_enable[0];
        endpoint_if.csr_to_core.irq.event_enable.rmem_error.value = event_enable[5];

        endpoint_if.csr_to_core.non_oetp_dma.tx.buffer_address.base.value = non_tx_buffer_address;
        endpoint_if.csr_to_core.non_oetp_dma.tx.frame_length.bytes.value = non_tx_frame_length;
        endpoint_if.csr_to_core.non_oetp_dma.tx.command_status.request.value = non_tx_request;
        endpoint_if.csr_to_core.non_oetp_dma.tx.command_status.clear_errors.value =
            non_tx_clear_errors;

        endpoint_if.csr_to_core.non_oetp_dma.rx.buffer_address.base.value = non_rx_buffer_address;
        endpoint_if.csr_to_core.non_oetp_dma.rx.buffer_capacity.bytes.value =
            non_rx_buffer_capacity;
        endpoint_if.csr_to_core.non_oetp_dma.rx.command_status.request.value = non_rx_request;
        endpoint_if.csr_to_core.non_oetp_dma.rx.command_status.clear_errors.value =
            non_rx_clear_errors;

        for (int n = 0; n < NUM_OF_PEERS; n++) begin
            endpoint_if.csr_to_core.peers.entry[n].local_address.base.value =
                peer_local_address[n*AXI_ADDR_W+:AXI_ADDR_W];
            endpoint_if.csr_to_core.peers.entry[n].remote_address.base.value =
                peer_remote_address[n*AXI_ADDR_W+:AXI_ADDR_W];
            endpoint_if.csr_to_core.peers.entry[n].size.bytes.value =
                peer_size[n*AXI_ADDR_W+:AXI_ADDR_W];
            endpoint_if.csr_to_core.peers.entry[n].dma.mode.value = peer_dma_mode[n*2+:2];
            endpoint_if.csr_to_core.peers.entry[n].dma.irq_enable.value = peer_irq_enable[n];
            endpoint_if.csr_to_core.peers.entry[n].dma.request.value = peer_request[n];
            endpoint_if.csr_to_core.peers.entry[n].dma.clear_error.value = peer_clear_error[n];
        end
    end

    assign non_tx_request_hwclr =
        endpoint_if.core_to_csr.non_oetp_dma.tx.command_status.request.hwclr;
    assign non_tx_clear_errors_hwclr =
        endpoint_if.core_to_csr.non_oetp_dma.tx.command_status.clear_errors.hwclr;
    assign non_tx_idle = endpoint_if.core_to_csr.non_oetp_dma.tx.command_status.idle.next;
    assign non_tx_done = endpoint_if.core_to_csr.non_oetp_dma.tx.command_status.done.next;
    assign non_tx_error = endpoint_if.core_to_csr.non_oetp_dma.tx.command_status.error.next;
    assign non_tx_error_code =
        endpoint_if.core_to_csr.non_oetp_dma.tx.command_status.error_code.next;
    assign non_tx_transferred_length =
        endpoint_if.core_to_csr.non_oetp_dma.tx.transferred_length.bytes.next;

    assign non_rx_request_hwclr =
        endpoint_if.core_to_csr.non_oetp_dma.rx.command_status.request.hwclr;
    assign non_rx_clear_errors_hwclr =
        endpoint_if.core_to_csr.non_oetp_dma.rx.command_status.clear_errors.hwclr;
    assign non_rx_idle = endpoint_if.core_to_csr.non_oetp_dma.rx.command_status.idle.next;
    assign non_rx_armed = endpoint_if.core_to_csr.non_oetp_dma.rx.command_status.armed.next;
    assign non_rx_done = endpoint_if.core_to_csr.non_oetp_dma.rx.command_status.done.next;
    assign non_rx_error = endpoint_if.core_to_csr.non_oetp_dma.rx.command_status.error.next;
    assign non_rx_error_code =
        endpoint_if.core_to_csr.non_oetp_dma.rx.command_status.error_code.next;
    assign non_rx_received_length =
        endpoint_if.core_to_csr.non_oetp_dma.rx.received_length.bytes.next;

    for (genvar n = 0; n < NUM_OF_PEERS; n++) begin : g_peer_status
        assign peer_clear_error_hwclr[n] =
            endpoint_if.core_to_csr.peers.entry[n].dma.clear_error.hwclr;
        assign peer_request_hwclr[n] = endpoint_if.core_to_csr.peers.entry[n].dma.request.hwclr;
        assign peer_idle[n] = endpoint_if.core_to_csr.peers.entry[n].dma.idle.next;
        assign peer_done[n] = endpoint_if.core_to_csr.peers.entry[n].dma.done.next;
        assign peer_error[n] = endpoint_if.core_to_csr.peers.entry[n].dma.error.next;
        assign peer_error_code[n*4+:4] = endpoint_if.core_to_csr.peers.entry[n].dma.error_code.next;
    end

    assign peer_lookup_req_valid = peer_lookup_if.req_valid;
    assign peer_lookup_if.req_ready = peer_lookup_req_ready;
    assign peer_lookup_req_type = peer_lookup_if.req_type;
    assign peer_lookup_req_mode_mask = peer_lookup_if.req_mode_mask;
    assign peer_lookup_req_peer_idx = peer_lookup_if.req_peer_idx;
    assign peer_lookup_req_rmem_addr = peer_lookup_if.req_rmem_addr;
    assign peer_lookup_req_mac_addr = peer_lookup_if.req_mac_addr;
    assign peer_lookup_if.rsp_valid = peer_lookup_rsp_valid;
    assign peer_lookup_rsp_ready = peer_lookup_if.rsp_ready;
    assign peer_lookup_if.rsp_hit = peer_lookup_rsp_hit;
    assign peer_lookup_if.rsp_peer_idx = peer_lookup_rsp_peer_idx;
    assign peer_lookup_if.rsp_mac_addr = peer_lookup_rsp_mac_addr;
    assign peer_lookup_if.rsp_rmem_offset = peer_lookup_rsp_rmem_offset;
    assign peer_lookup_if.rsp_local_addr = peer_lookup_rsp_local_addr;
    assign peer_lookup_if.rsp_remote_addr = peer_lookup_rsp_remote_addr;
    assign peer_lookup_if.rsp_size = peer_lookup_rsp_size;
    assign peer_lookup_if.rsp_dma_mode = peer_lookup_rsp_dma_mode;
    assign peer_lookup_if.rsp_irq_enable = peer_lookup_rsp_irq_enable;

    openenoc_cpuif_if #(
        .ADDR_W(32),
        .DATA_W(32)
    ) local_cpuif();

    assign local_cpuif.wr_ack = 1'b0;
    assign local_cpuif.wr_err = 1'b0;
    assign local_cpuif.rd_ack = 1'b0;
    assign local_cpuif.rd_err = 1'b0;
    assign local_cpuif.rd_data = '0;

    openenoc_irq_event_if #(
        .PEER_IDX_W(PEER_IDX_W)
    ) rmem_irq_event_if();

    assign rmem_irq_event_if.admit_ready = 1'b1;
    assign rmem_irq_event_if.admit_reserved = 1'b0;
    assign rmem_irq_event_if.commit_ready = 1'b1;

    openenoc_irq_event_if #(
        .PEER_IDX_W(PEER_IDX_W)
    ) responder_irq_event_if();

    assign responder_irq_admit_valid = responder_irq_event_if.admit_valid;
    assign responder_irq_admit_source = responder_irq_event_if.admit_source;
    assign responder_irq_admit_enable = responder_irq_event_if.admit_enable;
    assign responder_irq_event_if.admit_ready = responder_irq_admit_ready;
    assign responder_irq_event_if.admit_reserved = responder_irq_admit_ready
        && responder_irq_event_if.admit_valid && responder_irq_event_if.admit_enable
        && responder_irq_event_if.admit_source < 6
        && event_enable[responder_irq_event_if.admit_source[2:0]];
    assign responder_irq_commit_valid = responder_irq_event_if.commit_valid;
    assign responder_irq_commit_source = responder_irq_event_if.commit_source;
    assign responder_irq_commit_peer_idx = responder_irq_event_if.commit_peer_idx;
    assign responder_irq_event_if.commit_ready = responder_irq_commit_ready;

    assign initiator_if.tx_status_ready = 1'b1;
    assign responder_if.req_error_code = '0;
    assign responder_if.req_rx_status = 1'b0;
    assign responder_if.rx_status_valid = 1'b0;
    assign responder_if.rx_status_peer_idx = '0;
    assign responder_if.rx_status_sequence = '0;
    assign responder_if.rx_status_len = '0;
    assign responder_if.rx_status_error_code = '0;
    assign responder_if.tx_status_valid = 1'b0;
    assign responder_if.tx_status_peer_idx = '0;
    assign responder_if.tx_status_sequence = '0;
    assign responder_if.tx_status_len = '0;
    assign responder_if.tx_status_error_code = '0;
    assign initiator_if.non_oetp_rx_available = 1'b0;
    assign initiator_if.non_oetp_rx_claim_ready = 1'b0;
    assign non_oetp_rx_available = responder_if.non_oetp_rx_available;
    assign responder_if.non_oetp_rx_claim_valid = non_oetp_rx_claim_valid;
    assign non_oetp_rx_claim_ready = responder_if.non_oetp_rx_claim_ready;

    assign initiator_req_valid = initiator_if.req_valid;
    assign initiator_if.req_ready = initiator_req_ready;
    assign initiator_req_op = initiator_if.req_op;
    assign initiator_req_kind = initiator_if.req_kind;
    assign initiator_req_addr = initiator_if.req_addr;
    assign initiator_req_len = initiator_if.req_len;
    assign initiator_req_peer_idx = initiator_if.req_peer_idx;
    assign initiator_req_sequence = initiator_if.req_sequence;
    assign initiator_req_last = initiator_if.req_last;
    // Mock RMEM error completions on the common interface, not a DUT sideband.
    assign initiator_if.cpl_valid = initiator_cpl_valid || rmem_error_valid;
    assign initiator_if.cpl_kind = rmem_error_valid ? initiator_if.TRANSFER_KIND_RMEM
        : initiator_cpl_kind;
    assign initiator_if.cpl_rdata = '0;
    assign initiator_cpl_ready = initiator_if.cpl_ready;
    assign initiator_if.cpl_op = initiator_cpl_op;
    assign initiator_if.cpl_transferred_len = initiator_cpl_transferred_len;
    assign initiator_if.cpl_peer_idx = rmem_error_valid ? rmem_error_peer_idx
        : initiator_cpl_peer_idx;
    assign initiator_if.cpl_sequence = initiator_cpl_sequence;
    assign initiator_if.cpl_last = initiator_cpl_last;
    assign initiator_if.cpl_error = rmem_error_valid || initiator_cpl_error;
    // Model ERROR_RSP decoding with the shared RTL mapping helper.
    assign wire_error_csr_code = initiator_if.csr_error_from_wire(wire_error_code);
    assign initiator_if.cpl_error_code = rmem_error_valid ? rmem_error_code : wire_error_enable
        ? wire_error_csr_code : initiator_cpl_error_code;

    assign responder_if.req_valid = responder_req_valid;
    assign responder_req_ready = responder_if.req_ready;
    assign responder_if.req_op = responder_req_op;
    assign responder_if.req_kind = responder_req_kind;
    assign responder_if.req_biten = responder_req_biten;
    assign responder_if.req_wdata = responder_req_wdata;
    assign responder_if.req_addr = responder_req_addr;
    assign responder_if.req_len = responder_req_len;
    assign responder_if.req_peer_idx = responder_req_peer_idx;
    assign responder_if.req_sequence = responder_req_sequence;
    assign responder_if.req_last = responder_req_last;
    assign responder_cpl_valid = responder_if.cpl_valid;
    assign responder_if.cpl_ready = responder_cpl_ready;
    assign responder_cpl_op = responder_if.cpl_op;
    assign responder_cpl_kind = responder_if.cpl_kind;
    assign responder_cpl_rdata = responder_if.cpl_rdata;
    assign responder_cpl_transferred_len = responder_if.cpl_transferred_len;
    assign responder_cpl_peer_idx = responder_if.cpl_peer_idx;
    assign responder_cpl_sequence = responder_if.cpl_sequence;
    assign responder_cpl_last = responder_if.cpl_last;
    assign responder_cpl_error = responder_if.cpl_error;
    assign responder_cpl_error_code = responder_if.cpl_error_code;

    for (genvar n = 0; n < 3; n++) begin : g_irq_bridge
        assign irq_admit_valid[n] = irq_event_if[n].admit_valid;
        assign irq_event_if[n].admit_ready = irq_admit_ready[n];
        assign irq_admit_source[n*4+:4] = irq_event_if[n].admit_source;
        assign irq_admit_enable[n] = irq_event_if[n].admit_enable;
        assign irq_event_if[n].admit_reserved = irq_admit_reserved[n];

        assign irq_commit_valid[n] = irq_event_if[n].commit_valid;
        assign irq_event_if[n].commit_ready = irq_commit_ready[n];
        assign irq_commit_source[n*4+:4] = irq_event_if[n].commit_source;
        assign irq_commit_peer_idx[n*PEER_IDX_W+:PEER_IDX_W] = irq_event_if[n].commit_peer_idx;
    end

    openenoc_endpoint_dma_engine #(
        .SERIAL_PEER_REQUESTS(1'b0),
        .NUM_OF_PEERS(NUM_OF_PEERS),
        .PEER_IDX_W(PEER_IDX_W),
        .MAX_RAW_FRAME_SIZE(MAX_RAW_FRAME_SIZE),
        .FRAGMENT_SLOTS(FRAGMENT_SLOTS)
    ) dut (
        .clk(clk),
        .rst(rst),
        .endpoint_if(endpoint_if),
        .peer_lookup_if(peer_lookup_if),
        .initiator_if(initiator_if),
        .responder_if(responder_if),
        .m_axis_oetp(m_axis_oetp_if),
        .s_axis_oetp(s_axis_oetp_if),
        .m_axi_wr(m_axi_if),
        .m_axi_rd(m_axi_if),
        .m_local_cpuif(local_cpuif),
        .irq_event_if(irq_event_if),
        .rmem_irq_event_if(rmem_irq_event_if),
        .responder_irq_event_if(responder_irq_event_if)
    );

endmodule

`resetall
