// SPDX-FileCopyrightText: 2026 Enio Kaljic
// SPDX-License-Identifier: CERN-OHL-S-2.0

`resetall
`timescale 1ns / 1ps
`default_nettype none

/*
 * openENOC endpoint DMA engine
 *
 * A single TAXI AXI read DMA and a single TAXI AXI write DMA are shared by
 * peer DMA, non-oETP DMA, and incoming oETP DMA responder operations. Peer
 * configuration is obtained through the peer lookup interface and is
 * snapshotted when the CSR request is accepted. All operation classes share
 * one AXI stream in each direction between this block and the oETP engine.
 */
module openenoc_endpoint_dma_engine #(
    parameter int unsigned NUM_OF_PEERS = 4,
    parameter int unsigned PEER_IDX_W = NUM_OF_PEERS > 1 ? $clog2(NUM_OF_PEERS) : 1,
    parameter int unsigned MAX_DMA_FRAME_SIZE_BYTES = 8192,
    parameter int unsigned AXI_MAX_BURST_LEN = 16,
    parameter bit          UNALIGNED_EN = 1'b1
) (
    input  wire logic clk,
    input  wire logic rst,

    openenoc_endpoint_if.core endpoint_if,
    openenoc_peer_lookup_if.mst peer_lookup_if,

    openenoc_dma_transfer_if.requester initiator_if,
    openenoc_dma_transfer_if.executor responder_if,

    taxi_axis_if.src m_axis_oetp,
    taxi_axis_if.snk s_axis_oetp,

    taxi_axi_if.wr_mst m_axi_wr,
    taxi_axi_if.rd_mst m_axi_rd,

    openenoc_irq_event_if.producer irq_event_if[3]
);

    localparam int unsigned ADDR_W = initiator_if.ADDR_W;
    localparam int unsigned LEN_W = initiator_if.LEN_W;
    localparam int unsigned SEQUENCE_W = initiator_if.SEQUENCE_W;
    localparam int unsigned ERROR_W = initiator_if.ERROR_W;
    localparam int unsigned AXI_DATA_W = m_axi_rd.DATA_W;
    localparam int unsigned AXIS_KEEP_W = m_axis_oetp.KEEP_W;

    localparam logic DMA_OP_READ = 1'b0;
    localparam logic DMA_OP_WRITE = 1'b1;

    localparam logic [1:0] DMA_MODE_MIRROR_TO_LOCAL = 2'd2;
    localparam logic [1:0] DMA_MODE_MIRROR_TO_REMOTE = 2'd3;

    localparam logic [ERROR_W-1:0] DMA_ERROR_NONE = ERROR_W'(0);
    localparam logic [ERROR_W-1:0] DMA_ERROR_INVALID = ERROR_W'(1);
    localparam logic [ERROR_W-1:0] DMA_ERROR_AXIS = ERROR_W'(2);
    localparam logic [ERROR_W-1:0] DMA_ERROR_OVERFLOW = ERROR_W'(3);

    localparam logic [3:0] EVENT_PEER_DMA_COMPLETE = 4'd0;
    localparam logic [3:0] EVENT_NON_OETP_DMA_TX_COMPLETE = 4'd1;
    localparam logic [3:0] EVENT_NON_OETP_DMA_RX_COMPLETE = 4'd2;

    localparam logic [1:0] RD_CLIENT_PEER = 2'd0;
    localparam logic [1:0] RD_CLIENT_RESPONDER = 2'd1;
    localparam logic [1:0] RD_CLIENT_NON_OETP = 2'd2;

    localparam logic [1:0] WR_CLIENT_PEER = 2'd0;
    localparam logic [1:0] WR_CLIENT_RESPONDER = 2'd1;
    localparam logic [1:0] WR_CLIENT_NON_OETP = 2'd2;

    function automatic logic [LEN_W-1:0] fragment_length(
        input logic [LEN_W-1:0] remaining
    );
        if (remaining > LEN_W'(MAX_DMA_FRAME_SIZE_BYTES)) begin
            fragment_length = LEN_W'(MAX_DMA_FRAME_SIZE_BYTES);
        end else begin
            fragment_length = remaining;
        end
    endfunction

    function automatic logic [LEN_W-1:0] keep_count(
        input logic [AXIS_KEEP_W-1:0] keep
    );
        logic [LEN_W-1:0] count;
        count = '0;
        for (int unsigned n = 0; n < AXIS_KEEP_W; n++) begin
            count = count + LEN_W'(keep[n]);
        end
        return count;
    endfunction

    function automatic logic keep_contiguous(
        input logic [AXIS_KEEP_W-1:0] keep
    );
        logic [AXIS_KEEP_W:0] extended_keep;
        extended_keep = {1'b0, keep};
        return keep != '0 && (extended_keep & (extended_keep + 1'b1)) == '0;
    endfunction

    if (NUM_OF_PEERS < 1) begin : g_bad_num_peers
        $fatal(0, "Error: NUM_OF_PEERS must be at least one (instance %m)");
    end

    if (MAX_DMA_FRAME_SIZE_BYTES < 1) begin : g_bad_max_frame
        $fatal(0, "Error: MAX_DMA_FRAME_SIZE_BYTES must be at least one (instance %m)");
    end

    if (m_axi_wr.DATA_W != AXI_DATA_W || m_axi_wr.ADDR_W != m_axi_rd.ADDR_W) begin : g_bad_axi_pair
        $fatal(0, "Error: AXI read and write interface widths must match (instance %m)");
    end

    if (ADDR_W != m_axi_rd.ADDR_W) begin : g_bad_addr_width
        $fatal(0, "Error: DMA transfer and AXI address widths must match (instance %m)");
    end

    if (responder_if.ADDR_W != ADDR_W || responder_if.LEN_W != LEN_W ||
            responder_if.SEQUENCE_W != SEQUENCE_W ||
            responder_if.ERROR_W != ERROR_W) begin : g_bad_transfer_pair
        $fatal(0, "Error: initiator and responder transfer interface widths must match (instance %m)");
    end

    if (peer_lookup_if.PEER_IDX_W != PEER_IDX_W || initiator_if.PEER_IDX_W != PEER_IDX_W ||
            responder_if.PEER_IDX_W != PEER_IDX_W) begin : g_bad_peer_width
        $fatal(0, "Error: peer index widths must match PEER_IDX_W (instance %m)");
    end

    if (m_axis_oetp.DATA_W != AXI_DATA_W ||
            s_axis_oetp.DATA_W != AXI_DATA_W) begin : g_bad_axis_data_width
        $fatal(0, "Error: AXI stream data widths must match AXI_DATA_W (instance %m)");
    end

    if (m_axis_oetp.ID_W < SEQUENCE_W || s_axis_oetp.ID_W < SEQUENCE_W ||
            m_axis_oetp.DEST_W < PEER_IDX_W || s_axis_oetp.DEST_W < PEER_IDX_W ||
            m_axis_oetp.USER_W < 1 || s_axis_oetp.USER_W < 1) begin : g_bad_axis_metadata_width
        $fatal(0, "Error: oETP AXI stream metadata widths are insufficient (instance %m)");
    end

    taxi_dma_desc_if #(
        .SRC_ADDR_W (ADDR_W),
        .DST_ADDR_W (ADDR_W),
        .LEN_W      (LEN_W),
        .TAG_W      (2),
        .ID_EN      (1'b1),
        .ID_W       (SEQUENCE_W),
        .DEST_EN    (1'b1),
        .DEST_W     (PEER_IDX_W),
        .USER_EN    (1'b1),
        .USER_W     (1)
    ) rd_desc_if();

    taxi_dma_desc_if #(
        .SRC_ADDR_W (ADDR_W),
        .DST_ADDR_W (ADDR_W),
        .LEN_W      (LEN_W),
        .TAG_W      (2),
        .ID_EN      (1'b1),
        .ID_W       (SEQUENCE_W),
        .DEST_EN    (1'b1),
        .DEST_W     (PEER_IDX_W),
        .USER_EN    (1'b1),
        .USER_W     (1)
    ) wr_desc_if();

    taxi_axis_if #(
        .DATA_W  (AXI_DATA_W),
        .KEEP_EN (1'b1),
        .LAST_EN (1'b1),
        .ID_EN   (1'b1),
        .ID_W    (SEQUENCE_W),
        .DEST_EN (1'b1),
        .DEST_W  (PEER_IDX_W),
        .USER_EN (1'b1),
        .USER_W  (1)
    ) dma_rd_axis();

    taxi_axis_if #(
        .DATA_W  (AXI_DATA_W),
        .KEEP_EN (1'b1),
        .LAST_EN (1'b1),
        .ID_EN   (1'b1),
        .ID_W    (SEQUENCE_W),
        .DEST_EN (1'b1),
        .DEST_W  (PEER_IDX_W),
        .USER_EN (1'b1),
        .USER_W  (1)
    ) dma_wr_axis();

    taxi_axi_dma #(
        .AXI_MAX_BURST_LEN (AXI_MAX_BURST_LEN),
        .UNALIGNED_EN      (UNALIGNED_EN)
    ) taxi_axi_dma_inst (
        .clk            (clk),
        .rst            (rst),
        .rd_desc_req    (rd_desc_if),
        .rd_desc_sts    (rd_desc_if),
        .wr_desc_req    (wr_desc_if),
        .wr_desc_sts    (wr_desc_if),
        .m_axis_rd_data (dma_rd_axis),
        .s_axis_wr_data (dma_wr_axis),
        .m_axi_wr       (m_axi_wr),
        .m_axi_rd       (m_axi_rd),
        .read_enable    (1'b1),
        .write_enable   (1'b1),
        .write_abort    (1'b0)
    );

    typedef enum logic [3:0] {
        PEER_IDLE,
        PEER_LOOKUP_REQ,
        PEER_LOOKUP_RSP,
        PEER_ADMIT,
        PEER_RD_QUEUE,
        PEER_WR_QUEUE,
        PEER_COMMAND,
        PEER_WAIT,
        PEER_COMMIT
    } peer_state_t;

    typedef enum logic [2:0] {
        NON_TX_IDLE,
        NON_TX_ADMIT,
        NON_TX_QUEUE,
        NON_TX_WAIT,
        NON_TX_COMMIT
    } non_tx_state_t;

    typedef enum logic [2:0] {
        NON_RX_IDLE,
        NON_RX_ADMIT,
        NON_RX_ARMED,
        NON_RX_QUEUE,
        NON_RX_WAIT,
        NON_RX_COMMIT
    } non_rx_state_t;

    typedef enum logic [2:0] {
        RESP_IDLE,
        RESP_RD_QUEUE,
        RESP_WR_QUEUE,
        RESP_WAIT,
        RESP_COMPLETE
    } responder_state_t;

    typedef enum logic [1:0] {
        RD_IDLE,
        RD_DESC,
        RD_STREAM
    } rd_state_t;

    typedef enum logic [1:0] {
        WR_IDLE,
        WR_DESC,
        WR_STREAM
    } wr_state_t;

    peer_state_t peer_state_reg = PEER_IDLE;
    non_tx_state_t non_tx_state_reg = NON_TX_IDLE;
    non_rx_state_t non_rx_state_reg = NON_RX_IDLE;
    responder_state_t responder_state_reg = RESP_IDLE;
    rd_state_t rd_state_reg = RD_IDLE;
    wr_state_t wr_state_reg = WR_IDLE;

    logic [NUM_OF_PEERS-1:0] peer_idle_reg = '1;
    logic [NUM_OF_PEERS-1:0] peer_done_reg = '0;
    logic [NUM_OF_PEERS-1:0] peer_error_reg = '0;
    logic [ERROR_W-1:0] peer_error_code_reg[NUM_OF_PEERS];
    logic [NUM_OF_PEERS-1:0] peer_request_hwclr_reg = '0;

    logic non_tx_idle_reg = 1'b1;
    logic non_tx_done_reg = 1'b0;
    logic non_tx_error_reg = 1'b0;
    logic [ERROR_W-1:0] non_tx_error_code_reg = '0;
    logic [LEN_W-1:0] non_tx_transferred_len_reg = '0;
    logic non_tx_request_hwclr_reg = 1'b0;

    logic non_rx_idle_reg = 1'b1;
    logic non_rx_armed_reg = 1'b0;
    logic non_rx_done_reg = 1'b0;
    logic non_rx_error_reg = 1'b0;
    logic [ERROR_W-1:0] non_rx_error_code_reg = '0;
    logic [LEN_W-1:0] non_rx_received_len_reg = '0;
    logic non_rx_request_hwclr_reg = 1'b0;

    logic [PEER_IDX_W-1:0] peer_index_reg = '0;
    logic [PEER_IDX_W-1:0] peer_rr_reg = '0;
    logic [1:0] peer_mode_reg = '0;
    logic peer_irq_enable_reg = 1'b0;
    logic peer_irq_reserved_reg = 1'b0;
    logic [ADDR_W-1:0] peer_local_addr_reg = '0;
    logic [ADDR_W-1:0] peer_remote_addr_reg = '0;
    logic [LEN_W-1:0] peer_size_reg = '0;
    logic [LEN_W-1:0] peer_offset_reg = '0;
    logic [LEN_W-1:0] peer_remaining_reg = '0;
    logic [LEN_W-1:0] peer_fragment_len_reg = '0;
    logic [SEQUENCE_W-1:0] peer_sequence_reg = '0;
    logic peer_fragment_last_reg = 1'b0;
    logic peer_local_done_reg = 1'b0;
    logic peer_remote_done_reg = 1'b0;
    logic [ERROR_W-1:0] peer_local_error_reg = '0;
    logic [ERROR_W-1:0] peer_remote_error_reg = '0;

    logic [ADDR_W-1:0] non_tx_addr_reg = '0;
    logic [LEN_W-1:0] non_tx_len_reg = '0;
    logic non_tx_irq_reserved_reg = 1'b0;

    logic [ADDR_W-1:0] non_rx_addr_reg = '0;
    logic [LEN_W-1:0] non_rx_capacity_reg = '0;
    logic non_rx_irq_reserved_reg = 1'b0;

    logic responder_op_reg = DMA_OP_READ;
    logic [ADDR_W-1:0] responder_addr_reg = '0;
    logic [LEN_W-1:0] responder_len_reg = '0;
    logic [PEER_IDX_W-1:0] responder_peer_idx_reg = '0;
    logic [SEQUENCE_W-1:0] responder_sequence_reg = '0;
    logic responder_last_reg = 1'b0;
    logic [LEN_W-1:0] responder_cpl_len_reg = '0;
    logic responder_cpl_error_reg = 1'b0;
    logic [ERROR_W-1:0] responder_cpl_error_code_reg = '0;

    logic [1:0] rd_rr_reg = RD_CLIENT_PEER;
    logic [1:0] rd_client_reg = RD_CLIENT_PEER;
    logic [ADDR_W-1:0] rd_addr_reg = '0;
    logic [LEN_W-1:0] rd_len_reg = '0;
    logic [PEER_IDX_W-1:0] rd_peer_idx_reg = '0;
    logic [SEQUENCE_W-1:0] rd_sequence_reg = '0;
    logic rd_last_reg = 1'b0;
    logic [LEN_W-1:0] rd_byte_count_reg = '0;
    logic rd_saw_last_reg = 1'b0;
    logic rd_status_seen_reg = 1'b0;
    logic [ERROR_W-1:0] rd_status_error_reg = '0;
    logic rd_accept_pulse_reg = 1'b0;
    logic [1:0] rd_accept_client_reg = '0;
    logic rd_done_pulse_reg = 1'b0;
    logic [1:0] rd_done_client_reg = '0;
    logic [LEN_W-1:0] rd_done_len_reg = '0;
    logic [ERROR_W-1:0] rd_done_error_reg = '0;

    logic [1:0] wr_rr_reg = WR_CLIENT_PEER;
    logic [1:0] wr_client_reg = WR_CLIENT_PEER;
    logic [ADDR_W-1:0] wr_addr_reg = '0;
    logic [LEN_W-1:0] wr_len_reg = '0;
    logic [PEER_IDX_W-1:0] wr_peer_idx_reg = '0;
    logic [SEQUENCE_W-1:0] wr_sequence_reg = '0;
    logic wr_last_reg = 1'b0;
    logic [LEN_W-1:0] wr_input_len_reg = '0;
    logic wr_saw_last_reg = 1'b0;
    logic wr_status_seen_reg = 1'b0;
    logic [LEN_W-1:0] wr_status_len_reg = '0;
    logic [ERROR_W-1:0] wr_status_error_reg = '0;
    logic [ERROR_W-1:0] wr_stream_error_reg = '0;
    logic wr_accept_pulse_reg = 1'b0;
    logic [1:0] wr_accept_client_reg = '0;
    logic wr_first_pulse_reg = 1'b0;
    logic [1:0] wr_first_client_reg = '0;
    logic wr_done_pulse_reg = 1'b0;
    logic [1:0] wr_done_client_reg = '0;
    logic [LEN_W-1:0] wr_done_len_reg = '0;
    logic [ERROR_W-1:0] wr_done_error_reg = '0;

    logic [2:0] rd_job_valid;
    logic [2:0] wr_job_valid;
    logic rd_pick_valid;
    logic [1:0] rd_pick;
    logic wr_pick_valid;
    logic [1:0] wr_pick;

    logic [AXI_DATA_W-1:0] wr_src_tdata;
    logic [AXIS_KEEP_W-1:0] wr_src_tkeep;
    logic [SEQUENCE_W-1:0] wr_src_tid;
    logic [PEER_IDX_W-1:0] wr_src_tdest;
    logic wr_src_tuser;
    logic wr_src_tlast;
    logic wr_src_tvalid;
    logic wr_src_tready;

    logic peer_request_found;
    logic [PEER_IDX_W-1:0] peer_request_index;

    always_comb begin
        endpoint_if.core_to_csr.non_oetp_dma.tx.command_status.request.hwclr =
            non_tx_request_hwclr_reg;
        endpoint_if.core_to_csr.non_oetp_dma.tx.command_status.idle.next =
            non_tx_idle_reg;
        endpoint_if.core_to_csr.non_oetp_dma.tx.command_status.done.next =
            non_tx_done_reg;
        endpoint_if.core_to_csr.non_oetp_dma.tx.command_status.error.next =
            non_tx_error_reg;
        endpoint_if.core_to_csr.non_oetp_dma.tx.command_status.error_code.next =
            non_tx_error_code_reg;
        endpoint_if.core_to_csr.non_oetp_dma.tx.transferred_length.bytes.next =
            32'(non_tx_transferred_len_reg);

        endpoint_if.core_to_csr.non_oetp_dma.rx.command_status.request.hwclr =
            non_rx_request_hwclr_reg;
        endpoint_if.core_to_csr.non_oetp_dma.rx.command_status.idle.next =
            non_rx_idle_reg;
        endpoint_if.core_to_csr.non_oetp_dma.rx.command_status.armed.next =
            non_rx_armed_reg;
        endpoint_if.core_to_csr.non_oetp_dma.rx.command_status.done.next =
            non_rx_done_reg;
        endpoint_if.core_to_csr.non_oetp_dma.rx.command_status.error.next =
            non_rx_error_reg;
        endpoint_if.core_to_csr.non_oetp_dma.rx.command_status.error_code.next =
            non_rx_error_code_reg;
        endpoint_if.core_to_csr.non_oetp_dma.rx.received_length.bytes.next =
            32'(non_rx_received_len_reg);

        for (int unsigned n = 0; n < NUM_OF_PEERS; n++) begin
            endpoint_if.core_to_csr.peers.entry[n].dma.request.hwclr =
                peer_request_hwclr_reg[n];
            endpoint_if.core_to_csr.peers.entry[n].dma.idle.next = peer_idle_reg[n];
            endpoint_if.core_to_csr.peers.entry[n].dma.done.next = peer_done_reg[n];
            endpoint_if.core_to_csr.peers.entry[n].dma.error.next = peer_error_reg[n];
            endpoint_if.core_to_csr.peers.entry[n].dma.error_code.next =
                peer_error_code_reg[n];
        end
    end

    always_comb begin
        peer_request_found = 1'b0;
        peer_request_index = peer_rr_reg;

        for (int unsigned offset = 0; offset < NUM_OF_PEERS; offset++) begin
            int unsigned candidate;
            candidate = int'(peer_rr_reg) + offset;
            if (candidate >= NUM_OF_PEERS) begin
                candidate = candidate - NUM_OF_PEERS;
            end

            if (!peer_request_found &&
                    endpoint_if.csr_to_core.peers.entry[candidate].dma.request.value &&
                    peer_idle_reg[candidate]) begin
                peer_request_found = 1'b1;
                peer_request_index = PEER_IDX_W'(candidate);
            end
        end
    end

    always_comb begin
        peer_lookup_if.req_valid = peer_state_reg == PEER_LOOKUP_REQ;
        peer_lookup_if.req_type = 2'd0;
        peer_lookup_if.req_mode_mask = 4'b1100;
        peer_lookup_if.req_peer_idx = peer_index_reg;
        peer_lookup_if.req_rmem_addr = '0;
        peer_lookup_if.req_mac_addr = '0;
        peer_lookup_if.rsp_ready = peer_state_reg == PEER_LOOKUP_RSP;

        initiator_if.req_valid = peer_state_reg == PEER_COMMAND;
        initiator_if.req_op = peer_mode_reg == DMA_MODE_MIRROR_TO_REMOTE ?
            DMA_OP_WRITE : DMA_OP_READ;
        initiator_if.req_addr = peer_remote_addr_reg + ADDR_W'(peer_offset_reg);
        initiator_if.req_len = peer_fragment_len_reg;
        initiator_if.req_peer_idx = peer_index_reg;
        initiator_if.req_sequence = peer_sequence_reg;
        initiator_if.req_last = peer_fragment_last_reg;
        initiator_if.cpl_ready = peer_state_reg == PEER_WAIT && !peer_remote_done_reg;

        responder_if.req_ready = responder_state_reg == RESP_IDLE &&
            (responder_if.req_op == DMA_OP_READ ?
                (rd_state_reg == RD_IDLE && peer_state_reg == PEER_IDLE &&
                    non_tx_state_reg == NON_TX_IDLE) :
                (wr_state_reg == WR_IDLE && peer_state_reg == PEER_IDLE &&
                    (non_rx_state_reg == NON_RX_IDLE ||
                        non_rx_state_reg == NON_RX_ARMED)));
        responder_if.cpl_valid = responder_state_reg == RESP_COMPLETE;
        responder_if.cpl_op = responder_op_reg;
        responder_if.cpl_transferred_len = responder_cpl_len_reg;
        responder_if.cpl_peer_idx = responder_peer_idx_reg;
        responder_if.cpl_sequence = responder_sequence_reg;
        responder_if.cpl_last = responder_last_reg;
        responder_if.cpl_error = responder_cpl_error_reg;
        responder_if.cpl_error_code = responder_cpl_error_code_reg;

        irq_event_if[0].admit_valid = peer_state_reg == PEER_ADMIT;
        irq_event_if[0].admit_source = EVENT_PEER_DMA_COMPLETE;
        irq_event_if[0].admit_enable = peer_irq_enable_reg;
        irq_event_if[0].commit_valid =
            peer_state_reg == PEER_COMMIT && peer_irq_reserved_reg;
        irq_event_if[0].commit_source = EVENT_PEER_DMA_COMPLETE;
        irq_event_if[0].commit_peer_idx = peer_index_reg;

        irq_event_if[1].admit_valid = non_tx_state_reg == NON_TX_ADMIT;
        irq_event_if[1].admit_source = EVENT_NON_OETP_DMA_TX_COMPLETE;
        irq_event_if[1].admit_enable = 1'b1;
        irq_event_if[1].commit_valid =
            non_tx_state_reg == NON_TX_COMMIT && non_tx_irq_reserved_reg;
        irq_event_if[1].commit_source = EVENT_NON_OETP_DMA_TX_COMPLETE;
        irq_event_if[1].commit_peer_idx = '0;

        irq_event_if[2].admit_valid = non_rx_state_reg == NON_RX_ADMIT;
        irq_event_if[2].admit_source = EVENT_NON_OETP_DMA_RX_COMPLETE;
        irq_event_if[2].admit_enable = 1'b1;
        irq_event_if[2].commit_valid =
            non_rx_state_reg == NON_RX_COMMIT && non_rx_irq_reserved_reg;
        irq_event_if[2].commit_source = EVENT_NON_OETP_DMA_RX_COMPLETE;
        irq_event_if[2].commit_peer_idx = '0;
    end

    always_comb begin
        rd_job_valid[RD_CLIENT_PEER] = peer_state_reg == PEER_RD_QUEUE;
        rd_job_valid[RD_CLIENT_RESPONDER] = responder_state_reg == RESP_RD_QUEUE;
        rd_job_valid[RD_CLIENT_NON_OETP] = non_tx_state_reg == NON_TX_QUEUE;

        wr_job_valid[WR_CLIENT_PEER] = peer_state_reg == PEER_WR_QUEUE;
        wr_job_valid[WR_CLIENT_RESPONDER] = responder_state_reg == RESP_WR_QUEUE;
        wr_job_valid[WR_CLIENT_NON_OETP] = non_rx_state_reg == NON_RX_QUEUE;

        rd_pick_valid = 1'b0;
        rd_pick = rd_rr_reg;
        for (int unsigned offset = 0; offset < 3; offset++) begin
            int unsigned candidate;
            candidate = int'(rd_rr_reg) + offset;
            if (candidate >= 3) begin
                candidate = candidate - 3;
            end
            if (!rd_pick_valid && rd_job_valid[candidate]) begin
                rd_pick_valid = 1'b1;
                rd_pick = 2'(candidate);
            end
        end

        wr_pick_valid = 1'b0;
        wr_pick = wr_rr_reg;
        for (int unsigned offset = 0; offset < 3; offset++) begin
            int unsigned candidate;
            candidate = int'(wr_rr_reg) + offset;
            if (candidate >= 3) begin
                candidate = candidate - 3;
            end
            if (!wr_pick_valid && wr_job_valid[candidate]) begin
                wr_pick_valid = 1'b1;
                wr_pick = 2'(candidate);
            end
        end
    end

    always_comb begin
        rd_desc_if.req_src_addr = rd_addr_reg;
        rd_desc_if.req_src_sel = '0;
        rd_desc_if.req_src_asid = '0;
        rd_desc_if.req_dst_addr = '0;
        rd_desc_if.req_dst_sel = '0;
        rd_desc_if.req_dst_asid = '0;
        rd_desc_if.req_imm = '0;
        rd_desc_if.req_imm_en = 1'b0;
        rd_desc_if.req_len = rd_len_reg;
        rd_desc_if.req_tag = rd_client_reg;
        rd_desc_if.req_id = rd_sequence_reg;
        rd_desc_if.req_dest = rd_peer_idx_reg;
        rd_desc_if.req_user = rd_last_reg;
        rd_desc_if.req_valid = rd_state_reg == RD_DESC;

        wr_desc_if.req_src_addr = '0;
        wr_desc_if.req_src_sel = '0;
        wr_desc_if.req_src_asid = '0;
        wr_desc_if.req_dst_addr = wr_addr_reg;
        wr_desc_if.req_dst_sel = '0;
        wr_desc_if.req_dst_asid = '0;
        wr_desc_if.req_imm = '0;
        wr_desc_if.req_imm_en = 1'b0;
        wr_desc_if.req_len = wr_len_reg;
        wr_desc_if.req_tag = wr_client_reg;
        wr_desc_if.req_id = wr_sequence_reg;
        wr_desc_if.req_dest = wr_peer_idx_reg;
        wr_desc_if.req_user = wr_last_reg;
        wr_desc_if.req_valid = wr_state_reg == WR_DESC;
    end

    always_comb begin
        m_axis_oetp.tdata = dma_rd_axis.tdata;
        m_axis_oetp.tkeep = dma_rd_axis.tkeep;
        m_axis_oetp.tstrb = dma_rd_axis.tstrb;
        m_axis_oetp.tid = dma_rd_axis.tid;
        m_axis_oetp.tdest = dma_rd_axis.tdest;
        m_axis_oetp.tuser = dma_rd_axis.tuser;
        m_axis_oetp.tlast = dma_rd_axis.tlast;
        m_axis_oetp.tvalid = 1'b0;

        dma_rd_axis.tready = 1'b0;

        if (rd_state_reg == RD_STREAM) begin
            if (rd_client_reg != RD_CLIENT_PEER || peer_state_reg == PEER_WAIT) begin
                m_axis_oetp.tvalid = dma_rd_axis.tvalid;
                dma_rd_axis.tready = m_axis_oetp.tready;
            end
        end
    end

    always_comb begin
        wr_src_tdata = s_axis_oetp.tdata;
        wr_src_tkeep = s_axis_oetp.tkeep;
        wr_src_tid = s_axis_oetp.tid;
        wr_src_tdest = s_axis_oetp.tdest;
        wr_src_tuser = s_axis_oetp.tuser[0];
        wr_src_tlast = s_axis_oetp.tlast;
        wr_src_tvalid = s_axis_oetp.tvalid && wr_state_reg == WR_STREAM &&
            (wr_client_reg != WR_CLIENT_PEER || peer_state_reg == PEER_WAIT);
        dma_wr_axis.tdata = wr_src_tdata;
        dma_wr_axis.tkeep = wr_src_tkeep;
        dma_wr_axis.tstrb = wr_src_tkeep;
        dma_wr_axis.tid = wr_src_tid;
        dma_wr_axis.tdest = wr_src_tdest;
        dma_wr_axis.tuser = wr_src_tuser;
        dma_wr_axis.tlast = wr_src_tlast;
        dma_wr_axis.tvalid = wr_src_tvalid;
        wr_src_tready = dma_wr_axis.tready;
        s_axis_oetp.tready = wr_state_reg == WR_STREAM &&
            (wr_client_reg != WR_CLIENT_PEER || peer_state_reg == PEER_WAIT) ?
            dma_wr_axis.tready : 1'b0;
    end

    always_ff @(posedge clk) begin
        peer_request_hwclr_reg <= '0;

        case (peer_state_reg)
            PEER_IDLE: begin
                if (peer_request_found) begin
                    peer_index_reg <= peer_request_index;
                    peer_state_reg <= PEER_LOOKUP_REQ;
                end
            end
            PEER_LOOKUP_REQ: begin
                if (peer_lookup_if.req_valid && peer_lookup_if.req_ready) begin
                    peer_state_reg <= PEER_LOOKUP_RSP;
                end
            end
            PEER_LOOKUP_RSP: begin
                if (peer_lookup_if.rsp_valid && peer_lookup_if.rsp_ready) begin
                    peer_mode_reg <= peer_lookup_if.rsp_dma_mode;
                    peer_irq_enable_reg <= peer_lookup_if.rsp_irq_enable;
                    peer_local_addr_reg <= peer_lookup_if.rsp_local_addr;
                    peer_remote_addr_reg <= peer_lookup_if.rsp_remote_addr;
                    peer_size_reg <= peer_lookup_if.rsp_size;
                    peer_state_reg <= PEER_ADMIT;
                end
            end
            PEER_ADMIT: begin
                if (irq_event_if[0].admit_valid && irq_event_if[0].admit_ready) begin
                    logic config_valid;
                    config_valid = (peer_mode_reg == DMA_MODE_MIRROR_TO_LOCAL ||
                        peer_mode_reg == DMA_MODE_MIRROR_TO_REMOTE) &&
                        peer_size_reg != 0 &&
                        peer_local_addr_reg + ADDR_W'(peer_size_reg - 1'b1) >=
                            peer_local_addr_reg &&
                        peer_remote_addr_reg + ADDR_W'(peer_size_reg - 1'b1) >=
                            peer_remote_addr_reg;

                    peer_irq_reserved_reg <= irq_event_if[0].admit_reserved;
                    peer_request_hwclr_reg[peer_index_reg] <= 1'b1;
                    peer_idle_reg[peer_index_reg] <= 1'b0;
                    peer_done_reg[peer_index_reg] <= 1'b0;
                    peer_error_reg[peer_index_reg] <= 1'b0;
                    peer_error_code_reg[peer_index_reg] <= DMA_ERROR_NONE;
                    peer_offset_reg <= '0;
                    peer_remaining_reg <= peer_size_reg;
                    peer_fragment_len_reg <= fragment_length(peer_size_reg);
                    peer_sequence_reg <= '0;
                    peer_fragment_last_reg <=
                        peer_size_reg <= LEN_W'(MAX_DMA_FRAME_SIZE_BYTES);
                    peer_local_done_reg <= 1'b0;
                    peer_remote_done_reg <= 1'b0;
                    peer_local_error_reg <= DMA_ERROR_NONE;
                    peer_remote_error_reg <= DMA_ERROR_NONE;
                    if (peer_index_reg == PEER_IDX_W'(NUM_OF_PEERS-1)) begin
                        peer_rr_reg <= '0;
                    end else begin
                        peer_rr_reg <= peer_index_reg + 1'b1;
                    end

                    if (!config_valid) begin
                        peer_idle_reg[peer_index_reg] <= 1'b1;
                        peer_error_reg[peer_index_reg] <= 1'b1;
                        peer_error_code_reg[peer_index_reg] <= DMA_ERROR_INVALID;
                        peer_state_reg <= PEER_COMMIT;
                    end else if (peer_mode_reg == DMA_MODE_MIRROR_TO_REMOTE) begin
                        peer_state_reg <= PEER_RD_QUEUE;
                    end else begin
                        peer_state_reg <= PEER_WR_QUEUE;
                    end
                end
            end
            PEER_RD_QUEUE: begin
                if (rd_accept_pulse_reg && rd_accept_client_reg == RD_CLIENT_PEER) begin
                    peer_local_done_reg <= 1'b0;
                    peer_remote_done_reg <= 1'b0;
                    peer_local_error_reg <= DMA_ERROR_NONE;
                    peer_remote_error_reg <= DMA_ERROR_NONE;
                    peer_state_reg <= PEER_COMMAND;
                end
            end
            PEER_WR_QUEUE: begin
                if (wr_accept_pulse_reg && wr_accept_client_reg == WR_CLIENT_PEER) begin
                    peer_local_done_reg <= 1'b0;
                    peer_remote_done_reg <= 1'b0;
                    peer_local_error_reg <= DMA_ERROR_NONE;
                    peer_remote_error_reg <= DMA_ERROR_NONE;
                    peer_state_reg <= PEER_COMMAND;
                end
            end
            PEER_COMMAND: begin
                if (initiator_if.req_valid && initiator_if.req_ready) begin
                    peer_state_reg <= PEER_WAIT;
                end
            end
            PEER_WAIT: begin
                if (rd_done_pulse_reg && rd_done_client_reg == RD_CLIENT_PEER) begin
                    peer_local_done_reg <= 1'b1;
                    peer_local_error_reg <= rd_done_error_reg;
                end
                if (wr_done_pulse_reg && wr_done_client_reg == WR_CLIENT_PEER) begin
                    peer_local_done_reg <= 1'b1;
                    peer_local_error_reg <= wr_done_error_reg;
                end
                if (initiator_if.cpl_valid && initiator_if.cpl_ready) begin
                    peer_remote_done_reg <= 1'b1;
                    if (initiator_if.cpl_op !=
                            (peer_mode_reg == DMA_MODE_MIRROR_TO_REMOTE ?
                                DMA_OP_WRITE : DMA_OP_READ) ||
                            initiator_if.cpl_peer_idx != peer_index_reg ||
                            initiator_if.cpl_sequence != peer_sequence_reg ||
                            initiator_if.cpl_last != peer_fragment_last_reg ||
                            (!initiator_if.cpl_error &&
                                initiator_if.cpl_transferred_len != peer_fragment_len_reg)) begin
                        peer_remote_error_reg <= DMA_ERROR_AXIS;
                    end else if (initiator_if.cpl_error) begin
                        peer_remote_error_reg <= initiator_if.cpl_error_code;
                    end else begin
                        peer_remote_error_reg <= DMA_ERROR_NONE;
                    end
                end

                if (peer_local_done_reg && peer_remote_done_reg) begin
                    if (peer_local_error_reg != DMA_ERROR_NONE ||
                            peer_remote_error_reg != DMA_ERROR_NONE) begin
                        peer_idle_reg[peer_index_reg] <= 1'b1;
                        peer_error_reg[peer_index_reg] <= 1'b1;
                        if (peer_local_error_reg != DMA_ERROR_NONE) begin
                            peer_error_code_reg[peer_index_reg] <= peer_local_error_reg;
                        end else begin
                            peer_error_code_reg[peer_index_reg] <= peer_remote_error_reg;
                        end
                        peer_state_reg <= PEER_COMMIT;
                    end else if (peer_fragment_last_reg) begin
                        peer_idle_reg[peer_index_reg] <= 1'b1;
                        peer_done_reg[peer_index_reg] <= 1'b1;
                        peer_state_reg <= PEER_COMMIT;
                    end else begin
                        logic [LEN_W-1:0] next_remaining;
                        next_remaining = peer_remaining_reg - peer_fragment_len_reg;
                        peer_offset_reg <= peer_offset_reg + peer_fragment_len_reg;
                        peer_remaining_reg <= next_remaining;
                        peer_fragment_len_reg <= fragment_length(next_remaining);
                        peer_fragment_last_reg <=
                            next_remaining <= LEN_W'(MAX_DMA_FRAME_SIZE_BYTES);
                        peer_sequence_reg <= peer_sequence_reg + 1'b1;
                        peer_local_done_reg <= 1'b0;
                        peer_remote_done_reg <= 1'b0;
                        if (peer_mode_reg == DMA_MODE_MIRROR_TO_REMOTE) begin
                            peer_state_reg <= PEER_RD_QUEUE;
                        end else begin
                            peer_state_reg <= PEER_WR_QUEUE;
                        end
                    end
                end
            end
            PEER_COMMIT: begin
                if (!peer_irq_reserved_reg ||
                        (irq_event_if[0].commit_valid && irq_event_if[0].commit_ready)) begin
                    peer_irq_reserved_reg <= 1'b0;
                    peer_state_reg <= PEER_IDLE;
                end
            end
            default: peer_state_reg <= PEER_IDLE;
        endcase

        if (rst) begin
            peer_state_reg <= PEER_IDLE;
            peer_idle_reg <= '1;
            peer_done_reg <= '0;
            peer_error_reg <= '0;
            peer_request_hwclr_reg <= '0;
            peer_rr_reg <= '0;
            peer_irq_reserved_reg <= 1'b0;
            for (int unsigned n = 0; n < NUM_OF_PEERS; n++) begin
                peer_error_code_reg[n] <= DMA_ERROR_NONE;
            end
        end
    end

    always_ff @(posedge clk) begin
        non_tx_request_hwclr_reg <= 1'b0;

        case (non_tx_state_reg)
            NON_TX_IDLE: begin
                if (endpoint_if.csr_to_core.non_oetp_dma.tx.command_status.request.value) begin
                    non_tx_state_reg <= NON_TX_ADMIT;
                end
            end
            NON_TX_ADMIT: begin
                if (irq_event_if[1].admit_valid && irq_event_if[1].admit_ready) begin
                    non_tx_addr_reg <=
                        endpoint_if.csr_to_core.non_oetp_dma.tx.buffer_address.base.value;
                    non_tx_len_reg <=
                        endpoint_if.csr_to_core.non_oetp_dma.tx.frame_length.bytes.value;
                    non_tx_irq_reserved_reg <= irq_event_if[1].admit_reserved;
                    non_tx_request_hwclr_reg <= 1'b1;
                    non_tx_idle_reg <= 1'b0;
                    non_tx_done_reg <= 1'b0;
                    non_tx_error_reg <= 1'b0;
                    non_tx_error_code_reg <= DMA_ERROR_NONE;
                    non_tx_transferred_len_reg <= '0;

                    if (endpoint_if.csr_to_core.non_oetp_dma.tx.frame_length.bytes.value == 0 ||
                            endpoint_if.csr_to_core.non_oetp_dma.tx.frame_length.bytes.value >
                                MAX_DMA_FRAME_SIZE_BYTES) begin
                        non_tx_idle_reg <= 1'b1;
                        non_tx_error_reg <= 1'b1;
                        non_tx_error_code_reg <= DMA_ERROR_INVALID;
                        non_tx_state_reg <= NON_TX_COMMIT;
                    end else begin
                        non_tx_state_reg <= NON_TX_QUEUE;
                    end
                end
            end
            NON_TX_QUEUE: begin
                if (rd_accept_pulse_reg && rd_accept_client_reg == RD_CLIENT_NON_OETP) begin
                    non_tx_state_reg <= NON_TX_WAIT;
                end
            end
            NON_TX_WAIT: begin
                if (rd_done_pulse_reg && rd_done_client_reg == RD_CLIENT_NON_OETP) begin
                    non_tx_idle_reg <= 1'b1;
                    non_tx_transferred_len_reg <= rd_done_len_reg;
                    if (rd_done_error_reg == DMA_ERROR_NONE && rd_done_len_reg == non_tx_len_reg) begin
                        non_tx_done_reg <= 1'b1;
                    end else begin
                        non_tx_error_reg <= 1'b1;
                        if (rd_done_error_reg != DMA_ERROR_NONE) begin
                            non_tx_error_code_reg <= rd_done_error_reg;
                        end else begin
                            non_tx_error_code_reg <= DMA_ERROR_AXIS;
                        end
                    end
                    non_tx_state_reg <= NON_TX_COMMIT;
                end
            end
            NON_TX_COMMIT: begin
                if (!non_tx_irq_reserved_reg ||
                        (irq_event_if[1].commit_valid && irq_event_if[1].commit_ready)) begin
                    non_tx_irq_reserved_reg <= 1'b0;
                    non_tx_state_reg <= NON_TX_IDLE;
                end
            end
            default: non_tx_state_reg <= NON_TX_IDLE;
        endcase

        if (rst) begin
            non_tx_state_reg <= NON_TX_IDLE;
            non_tx_idle_reg <= 1'b1;
            non_tx_done_reg <= 1'b0;
            non_tx_error_reg <= 1'b0;
            non_tx_error_code_reg <= DMA_ERROR_NONE;
            non_tx_transferred_len_reg <= '0;
            non_tx_request_hwclr_reg <= 1'b0;
            non_tx_irq_reserved_reg <= 1'b0;
        end
    end

    always_ff @(posedge clk) begin
        non_rx_request_hwclr_reg <= 1'b0;

        case (non_rx_state_reg)
            NON_RX_IDLE: begin
                if (endpoint_if.csr_to_core.non_oetp_dma.rx.command_status.request.value) begin
                    non_rx_state_reg <= NON_RX_ADMIT;
                end
            end
            NON_RX_ADMIT: begin
                if (irq_event_if[2].admit_valid && irq_event_if[2].admit_ready) begin
                    non_rx_addr_reg <=
                        endpoint_if.csr_to_core.non_oetp_dma.rx.buffer_address.base.value;
                    non_rx_capacity_reg <=
                        endpoint_if.csr_to_core.non_oetp_dma.rx.buffer_capacity.bytes.value;
                    non_rx_irq_reserved_reg <= irq_event_if[2].admit_reserved;
                    non_rx_request_hwclr_reg <= 1'b1;
                    non_rx_idle_reg <= 1'b0;
                    non_rx_armed_reg <= 1'b1;
                    non_rx_done_reg <= 1'b0;
                    non_rx_error_reg <= 1'b0;
                    non_rx_error_code_reg <= DMA_ERROR_NONE;
                    non_rx_received_len_reg <= '0;

                    if (endpoint_if.csr_to_core.non_oetp_dma.rx.buffer_capacity.bytes.value == 0 ||
                            endpoint_if.csr_to_core.non_oetp_dma.rx.buffer_capacity.bytes.value >
                                MAX_DMA_FRAME_SIZE_BYTES) begin
                        non_rx_idle_reg <= 1'b1;
                        non_rx_armed_reg <= 1'b0;
                        non_rx_error_reg <= 1'b1;
                        non_rx_error_code_reg <= DMA_ERROR_INVALID;
                        non_rx_state_reg <= NON_RX_COMMIT;
                    end else begin
                        non_rx_state_reg <= NON_RX_ARMED;
                    end
                end
            end
            NON_RX_ARMED: begin
                if (s_axis_oetp.tvalid && wr_state_reg == WR_IDLE &&
                        responder_state_reg == RESP_IDLE &&
                        peer_state_reg == PEER_IDLE &&
                        !(responder_if.req_valid && responder_if.req_ready)) begin
                    non_rx_state_reg <= NON_RX_QUEUE;
                end
            end
            NON_RX_QUEUE: begin
                if (wr_accept_pulse_reg && wr_accept_client_reg == WR_CLIENT_NON_OETP) begin
                    non_rx_state_reg <= NON_RX_WAIT;
                end
            end
            NON_RX_WAIT: begin
                if ((wr_first_pulse_reg &&
                        wr_first_client_reg == WR_CLIENT_NON_OETP) ||
                        (wr_state_reg == WR_STREAM &&
                            wr_client_reg == WR_CLIENT_NON_OETP &&
                            wr_src_tvalid && wr_src_tready && wr_input_len_reg == 0)) begin
                    non_rx_armed_reg <= 1'b0;
                end
                if (wr_done_pulse_reg && wr_done_client_reg == WR_CLIENT_NON_OETP) begin
                    non_rx_idle_reg <= 1'b1;
                    non_rx_armed_reg <= 1'b0;
                    non_rx_received_len_reg <= wr_done_len_reg;
                    if (wr_done_error_reg == DMA_ERROR_NONE) begin
                        non_rx_done_reg <= 1'b1;
                    end else begin
                        non_rx_error_reg <= 1'b1;
                        non_rx_error_code_reg <= wr_done_error_reg;
                    end
                    non_rx_state_reg <= NON_RX_COMMIT;
                end
            end
            NON_RX_COMMIT: begin
                if (!non_rx_irq_reserved_reg ||
                        (irq_event_if[2].commit_valid && irq_event_if[2].commit_ready)) begin
                    non_rx_irq_reserved_reg <= 1'b0;
                    non_rx_state_reg <= NON_RX_IDLE;
                end
            end
            default: non_rx_state_reg <= NON_RX_IDLE;
        endcase

        if (rst) begin
            non_rx_state_reg <= NON_RX_IDLE;
            non_rx_idle_reg <= 1'b1;
            non_rx_armed_reg <= 1'b0;
            non_rx_done_reg <= 1'b0;
            non_rx_error_reg <= 1'b0;
            non_rx_error_code_reg <= DMA_ERROR_NONE;
            non_rx_received_len_reg <= '0;
            non_rx_request_hwclr_reg <= 1'b0;
            non_rx_irq_reserved_reg <= 1'b0;
        end
    end

    always_ff @(posedge clk) begin
        case (responder_state_reg)
            RESP_IDLE: begin
                if (responder_if.req_valid && responder_if.req_ready) begin
                    responder_op_reg <= responder_if.req_op;
                    responder_addr_reg <= responder_if.req_addr;
                    responder_len_reg <= responder_if.req_len;
                    responder_peer_idx_reg <= responder_if.req_peer_idx;
                    responder_sequence_reg <= responder_if.req_sequence;
                    responder_last_reg <= responder_if.req_last;
                    responder_cpl_len_reg <= '0;
                    responder_cpl_error_reg <= 1'b0;
                    responder_cpl_error_code_reg <= DMA_ERROR_NONE;

                    if (responder_if.req_len == 0 ||
                            responder_if.req_len > LEN_W'(MAX_DMA_FRAME_SIZE_BYTES) ||
                            responder_if.req_addr + ADDR_W'(responder_if.req_len - 1'b1) <
                                responder_if.req_addr) begin
                        responder_cpl_error_reg <= 1'b1;
                        responder_cpl_error_code_reg <= DMA_ERROR_INVALID;
                        responder_state_reg <= RESP_COMPLETE;
                    end else if (responder_if.req_op == DMA_OP_READ) begin
                        responder_state_reg <= RESP_RD_QUEUE;
                    end else begin
                        responder_state_reg <= RESP_WR_QUEUE;
                    end
                end
            end
            RESP_RD_QUEUE: begin
                if (rd_accept_pulse_reg && rd_accept_client_reg == RD_CLIENT_RESPONDER) begin
                    responder_state_reg <= RESP_WAIT;
                end
            end
            RESP_WR_QUEUE: begin
                if (wr_accept_pulse_reg && wr_accept_client_reg == WR_CLIENT_RESPONDER) begin
                    responder_state_reg <= RESP_WAIT;
                end
            end
            RESP_WAIT: begin
                if (rd_done_pulse_reg && rd_done_client_reg == RD_CLIENT_RESPONDER) begin
                    responder_cpl_len_reg <= rd_done_len_reg;
                    responder_cpl_error_reg <= rd_done_error_reg != DMA_ERROR_NONE ||
                        rd_done_len_reg != responder_len_reg;
                    responder_cpl_error_code_reg <= rd_done_error_reg != DMA_ERROR_NONE ?
                        rd_done_error_reg :
                        (rd_done_len_reg != responder_len_reg ? DMA_ERROR_AXIS : DMA_ERROR_NONE);
                    responder_state_reg <= RESP_COMPLETE;
                end
                if (wr_done_pulse_reg && wr_done_client_reg == WR_CLIENT_RESPONDER) begin
                    responder_cpl_len_reg <= wr_done_len_reg;
                    responder_cpl_error_reg <= wr_done_error_reg != DMA_ERROR_NONE;
                    responder_cpl_error_code_reg <= wr_done_error_reg;
                    responder_state_reg <= RESP_COMPLETE;
                end
            end
            RESP_COMPLETE: begin
                if (responder_if.cpl_valid && responder_if.cpl_ready) begin
                    responder_state_reg <= RESP_IDLE;
                end
            end
            default: responder_state_reg <= RESP_IDLE;
        endcase

        if (rst) begin
            responder_state_reg <= RESP_IDLE;
            responder_cpl_error_reg <= 1'b0;
            responder_cpl_error_code_reg <= DMA_ERROR_NONE;
        end
    end

    always_ff @(posedge clk) begin
        rd_accept_pulse_reg <= 1'b0;
        rd_done_pulse_reg <= 1'b0;

        case (rd_state_reg)
            RD_IDLE: begin
                if (rd_pick_valid) begin
                    rd_client_reg <= rd_pick;
                    rd_accept_client_reg <= rd_pick;
                    rd_accept_pulse_reg <= 1'b1;
                    rd_byte_count_reg <= '0;
                    rd_saw_last_reg <= 1'b0;
                    rd_status_seen_reg <= 1'b0;
                    rd_status_error_reg <= DMA_ERROR_NONE;

                    case (rd_pick)
                        RD_CLIENT_PEER: begin
                            rd_addr_reg <= peer_local_addr_reg + ADDR_W'(peer_offset_reg);
                            rd_len_reg <= peer_fragment_len_reg;
                            rd_peer_idx_reg <= peer_index_reg;
                            rd_sequence_reg <= peer_sequence_reg;
                            rd_last_reg <= peer_fragment_last_reg;
                        end
                        RD_CLIENT_RESPONDER: begin
                            rd_addr_reg <= responder_addr_reg;
                            rd_len_reg <= responder_len_reg;
                            rd_peer_idx_reg <= responder_peer_idx_reg;
                            rd_sequence_reg <= responder_sequence_reg;
                            rd_last_reg <= responder_last_reg;
                        end
                        default: begin
                            rd_addr_reg <= non_tx_addr_reg;
                            rd_len_reg <= non_tx_len_reg;
                            rd_peer_idx_reg <= '0;
                            rd_sequence_reg <= '0;
                            rd_last_reg <= 1'b1;
                        end
                    endcase
                    rd_state_reg <= RD_DESC;
                end
            end
            RD_DESC: begin
                if (rd_desc_if.req_valid && rd_desc_if.req_ready) begin
                    rd_state_reg <= RD_STREAM;
                end
            end
            RD_STREAM: begin
                logic beat_accepted;
                logic [LEN_W-1:0] next_byte_count;
                logic last_seen_now;
                logic status_seen_now;
                logic [ERROR_W-1:0] status_error_now;

                beat_accepted = dma_rd_axis.tvalid && dma_rd_axis.tready;
                next_byte_count = rd_byte_count_reg +
                    (beat_accepted ? keep_count(dma_rd_axis.tkeep) : LEN_W'(0));
                last_seen_now = rd_saw_last_reg ||
                    (beat_accepted && dma_rd_axis.tlast);
                status_seen_now = rd_status_seen_reg || rd_desc_if.sts_valid;
                status_error_now = rd_desc_if.sts_valid ?
                    ERROR_W'(rd_desc_if.sts_error) : rd_status_error_reg;

                if (dma_rd_axis.tvalid && dma_rd_axis.tready) begin
                    rd_byte_count_reg <= next_byte_count;
                    rd_saw_last_reg <= last_seen_now;
                end
                if (rd_desc_if.sts_valid) begin
                    rd_status_seen_reg <= 1'b1;
                    rd_status_error_reg <= ERROR_W'(rd_desc_if.sts_error);
                end
                if (last_seen_now && status_seen_now) begin
                    rd_done_pulse_reg <= 1'b1;
                    rd_done_client_reg <= rd_client_reg;
                    rd_done_len_reg <= next_byte_count;
                    rd_done_error_reg <= status_error_now;
                    if (rd_client_reg == 2'd2) begin
                        rd_rr_reg <= 2'd0;
                    end else begin
                        rd_rr_reg <= rd_client_reg + 1'b1;
                    end
                    rd_state_reg <= RD_IDLE;
                end
            end
            default: rd_state_reg <= RD_IDLE;
        endcase

        if (rst) begin
            rd_state_reg <= RD_IDLE;
            rd_rr_reg <= RD_CLIENT_PEER;
            rd_accept_pulse_reg <= 1'b0;
            rd_done_pulse_reg <= 1'b0;
            rd_saw_last_reg <= 1'b0;
            rd_status_seen_reg <= 1'b0;
            rd_status_error_reg <= DMA_ERROR_NONE;
        end
    end

    always_ff @(posedge clk) begin
        wr_accept_pulse_reg <= 1'b0;
        wr_first_pulse_reg <= 1'b0;
        wr_done_pulse_reg <= 1'b0;

        case (wr_state_reg)
            WR_IDLE: begin
                if (wr_pick_valid) begin
                    wr_client_reg <= wr_pick;
                    wr_accept_client_reg <= wr_pick;
                    wr_accept_pulse_reg <= 1'b1;
                    wr_input_len_reg <= '0;
                    wr_saw_last_reg <= 1'b0;
                    wr_status_seen_reg <= 1'b0;
                    wr_status_len_reg <= '0;
                    wr_status_error_reg <= DMA_ERROR_NONE;
                    wr_stream_error_reg <= DMA_ERROR_NONE;

                    case (wr_pick)
                        WR_CLIENT_PEER: begin
                            wr_addr_reg <= peer_local_addr_reg + ADDR_W'(peer_offset_reg);
                            wr_len_reg <= peer_fragment_len_reg;
                            wr_peer_idx_reg <= peer_index_reg;
                            wr_sequence_reg <= peer_sequence_reg;
                            wr_last_reg <= peer_fragment_last_reg;
                        end
                        WR_CLIENT_RESPONDER: begin
                            wr_addr_reg <= responder_addr_reg;
                            wr_len_reg <= responder_len_reg;
                            wr_peer_idx_reg <= responder_peer_idx_reg;
                            wr_sequence_reg <= responder_sequence_reg;
                            wr_last_reg <= responder_last_reg;
                        end
                        default: begin
                            wr_addr_reg <= non_rx_addr_reg;
                            wr_len_reg <= non_rx_capacity_reg;
                            wr_peer_idx_reg <= '0;
                            wr_sequence_reg <= '0;
                            wr_last_reg <= 1'b1;
                        end
                    endcase
                    wr_state_reg <= WR_DESC;
                end
            end
            WR_DESC: begin
                if (wr_desc_if.req_valid && wr_desc_if.req_ready) begin
                    wr_state_reg <= WR_STREAM;
                end
            end
            WR_STREAM: begin
                logic beat_accepted;
                logic [LEN_W-1:0] beat_len;
                logic [LEN_W-1:0] next_input_len;
                logic last_seen_now;
                logic status_seen_now;
                logic [LEN_W-1:0] status_len_now;
                logic [ERROR_W-1:0] status_error_now;
                logic [ERROR_W-1:0] stream_error_now;

                beat_accepted = wr_src_tvalid && wr_src_tready;
                beat_len = keep_count(wr_src_tkeep);
                next_input_len = wr_input_len_reg + beat_len;
                last_seen_now = wr_saw_last_reg || (beat_accepted && wr_src_tlast);
                status_seen_now = wr_status_seen_reg || wr_desc_if.sts_valid;
                status_len_now = wr_desc_if.sts_valid ?
                    wr_desc_if.sts_len : wr_status_len_reg;
                status_error_now = wr_desc_if.sts_valid ?
                    ERROR_W'(wr_desc_if.sts_error) : wr_status_error_reg;
                stream_error_now = wr_stream_error_reg;

                if (beat_accepted) begin
                    if (wr_input_len_reg == 0) begin
                        wr_first_pulse_reg <= 1'b1;
                        wr_first_client_reg <= wr_client_reg;
                    end

                    wr_input_len_reg <= next_input_len;
                    wr_saw_last_reg <= last_seen_now;

                    if (!keep_contiguous(wr_src_tkeep) ||
                            (!wr_src_tlast && wr_src_tkeep != '1)) begin
                        stream_error_now = DMA_ERROR_AXIS;
                    end

                    if (wr_client_reg != WR_CLIENT_NON_OETP &&
                            (wr_src_tid != wr_sequence_reg ||
                                wr_src_tdest != wr_peer_idx_reg ||
                                wr_src_tuser != wr_last_reg)) begin
                        stream_error_now = DMA_ERROR_AXIS;
                    end

                    if (wr_client_reg == WR_CLIENT_NON_OETP) begin
                        if (next_input_len > wr_len_reg ||
                                (!wr_src_tlast && next_input_len >= wr_len_reg)) begin
                            stream_error_now = DMA_ERROR_OVERFLOW;
                        end
                    end else if ((wr_src_tlast && next_input_len != wr_len_reg) ||
                            (!wr_src_tlast && next_input_len >= wr_len_reg)) begin
                        stream_error_now = DMA_ERROR_AXIS;
                    end
                end

                if (wr_desc_if.sts_valid) begin
                    wr_status_seen_reg <= 1'b1;
                    wr_status_len_reg <= wr_desc_if.sts_len;
                    wr_status_error_reg <= ERROR_W'(wr_desc_if.sts_error);
                end
                wr_stream_error_reg <= stream_error_now;

                if (last_seen_now && status_seen_now) begin
                    wr_done_pulse_reg <= 1'b1;
                    wr_done_client_reg <= wr_client_reg;
                    wr_done_len_reg <= status_len_now;
                    if (status_error_now != DMA_ERROR_NONE) begin
                        wr_done_error_reg <= status_error_now;
                    end else begin
                        wr_done_error_reg <= stream_error_now;
                    end
                    if (wr_client_reg == 2'd2) begin
                        wr_rr_reg <= 2'd0;
                    end else begin
                        wr_rr_reg <= wr_client_reg + 1'b1;
                    end
                    wr_state_reg <= WR_IDLE;
                end
            end
            default: wr_state_reg <= WR_IDLE;
        endcase

        if (rst) begin
            wr_state_reg <= WR_IDLE;
            wr_rr_reg <= WR_CLIENT_PEER;
            wr_accept_pulse_reg <= 1'b0;
            wr_first_pulse_reg <= 1'b0;
            wr_done_pulse_reg <= 1'b0;
        end
    end

endmodule

`resetall
