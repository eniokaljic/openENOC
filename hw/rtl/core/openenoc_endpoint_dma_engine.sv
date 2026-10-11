// SPDX-FileCopyrightText: 2026 Enio Kaljic
// SPDX-License-Identifier: CERN-OHL-S-2.0

`resetall
`timescale 1ns / 1ps
`default_nettype none

/* Shared endpoint memory DMA engine with RMEM interface ownership. */
module openenoc_endpoint_dma_engine #(
    parameter int unsigned NUM_OF_PEERS = 4,
    parameter int unsigned PEER_IDX_W = NUM_OF_PEERS > 1 ? $clog2(NUM_OF_PEERS) : 1,
    parameter int unsigned MAX_RAW_FRAME_SIZE = 8192,
    parameter int unsigned AXI_MAX_BURST_LEN = 16,
    parameter int unsigned FRAGMENT_SLOTS = 16,
    parameter bit SERIAL_PEER_REQUESTS = 1'b1,
    parameter bit UNALIGNED_EN = 1'b1
) (
    input wire logic clk,
    input wire logic rst,
    openenoc_endpoint_if.core endpoint_if,
    openenoc_peer_lookup_if.mst peer_lookup_if,
    openenoc_dma_transfer_if.requester initiator_if,
    openenoc_dma_transfer_if.executor responder_if,
    taxi_axis_if.src m_axis_oetp,
    taxi_axis_if.snk s_axis_oetp,
    taxi_axi_if.wr_mst m_axi_wr,
    taxi_axi_if.rd_mst m_axi_rd,
    openenoc_cpuif_if.mst m_local_cpuif,
    openenoc_irq_event_if.producer irq_event_if[3],
    openenoc_irq_event_if.producer rmem_irq_event_if,
    openenoc_irq_event_if.producer responder_irq_event_if
);

    taxi_axis_if #(
        .DATA_W(s_axis_oetp.DATA_W),
        .KEEP_W(s_axis_oetp.KEEP_W),
        .KEEP_EN(s_axis_oetp.KEEP_EN),
        .STRB_EN(s_axis_oetp.STRB_EN),
        .LAST_EN(s_axis_oetp.LAST_EN),
        .ID_EN(s_axis_oetp.ID_EN),
        .ID_W(s_axis_oetp.ID_W),
        .DEST_EN(s_axis_oetp.DEST_EN),
        .DEST_W(s_axis_oetp.DEST_W),
        .USER_EN(s_axis_oetp.USER_EN),
        .USER_W(s_axis_oetp.USER_W)
    ) memory_input();

    taxi_axis_register #(
        .REG_TYPE(2)
    ) u_memory_input_register (
        .clk(clk),
        .rst(rst),
        .s_axis(s_axis_oetp),
        .m_axis(memory_input)
    );

    taxi_axis_if #(
        .DATA_W(m_axis_oetp.DATA_W),
        .KEEP_W(m_axis_oetp.KEEP_W),
        .KEEP_EN(m_axis_oetp.KEEP_EN),
        .STRB_EN(m_axis_oetp.STRB_EN),
        .LAST_EN(m_axis_oetp.LAST_EN),
        .ID_EN(m_axis_oetp.ID_EN),
        .ID_W(m_axis_oetp.ID_W),
        .DEST_EN(m_axis_oetp.DEST_EN),
        .DEST_W(m_axis_oetp.DEST_W),
        .USER_EN(m_axis_oetp.USER_EN),
        .USER_W(m_axis_oetp.USER_W)
    ) memory_output();

    taxi_axis_if #(
        .DATA_W(m_axis_oetp.DATA_W),
        .KEEP_W(m_axis_oetp.KEEP_W),
        .KEEP_EN(m_axis_oetp.KEEP_EN),
        .STRB_EN(m_axis_oetp.STRB_EN),
        .LAST_EN(m_axis_oetp.LAST_EN),
        .ID_EN(m_axis_oetp.ID_EN),
        .ID_W(m_axis_oetp.ID_W),
        .DEST_EN(m_axis_oetp.DEST_EN),
        .DEST_W(m_axis_oetp.DEST_W),
        .USER_EN(m_axis_oetp.USER_EN),
        .USER_W(m_axis_oetp.USER_W)
    ) oetp_registered();

    assign m_axis_oetp.tdata = oetp_registered.tdata;
    assign m_axis_oetp.tkeep = oetp_registered.tkeep;
    assign m_axis_oetp.tvalid = oetp_registered.tvalid;
    assign m_axis_oetp.tlast = oetp_registered.tlast;
    assign m_axis_oetp.tid = oetp_registered.tid;
    assign m_axis_oetp.tdest = oetp_registered.tdest;
    assign m_axis_oetp.tuser = oetp_registered.tuser;
    assign m_axis_oetp.tstrb = m_axis_oetp.STRB_EN ? oetp_registered.tstrb : oetp_registered.tkeep;
    assign oetp_registered.tready = m_axis_oetp.tready;

    taxi_axis_register #(
        .REG_TYPE(2)
    ) u_memory_output_register (
        .clk(clk),
        .rst(rst),
        .s_axis(memory_output),
        .m_axis(oetp_registered)
    );

    taxi_axi_if #(
        .DATA_W(m_axi_rd.DATA_W),
        .ADDR_W(m_axi_rd.ADDR_W),
        .ID_W(m_axi_rd.ID_W),
        .ARUSER_EN(m_axi_rd.ARUSER_EN),
        .ARUSER_W(m_axi_rd.ARUSER_W),
        .RUSER_EN(m_axi_rd.RUSER_EN),
        .RUSER_W(m_axi_rd.RUSER_W)
    ) memory_read();

    taxi_axi_register_rd #(
        .AR_REG_TYPE(2),
        .R_REG_TYPE(2)
    ) u_memory_read_register (
        .clk(clk),
        .rst(rst),
        .s_axi_rd(memory_read),
        .m_axi_rd(m_axi_rd)
    );

    taxi_axi_if #(
        .DATA_W(m_axi_wr.DATA_W),
        .ADDR_W(m_axi_wr.ADDR_W),
        .ID_W(m_axi_wr.ID_W),
        .AWUSER_EN(m_axi_wr.AWUSER_EN),
        .AWUSER_W(m_axi_wr.AWUSER_W),
        .WUSER_EN(m_axi_wr.WUSER_EN),
        .WUSER_W(m_axi_wr.WUSER_W),
        .BUSER_EN(m_axi_wr.BUSER_EN),
        .BUSER_W(m_axi_wr.BUSER_W)
    ) memory_write();

    taxi_axi_register_wr #(
        .AW_REG_TYPE(2),
        .W_REG_TYPE(2),
        .B_REG_TYPE(2)
    ) u_memory_write_register (
        .clk(clk),
        .rst(rst),
        .s_axi_wr(memory_write),
        .m_axi_wr(m_axi_wr)
    );

    localparam int DMA_IRQ_PEER_W = irq_event_if[0].PEER_IDX_W;
    localparam int RMEM_IRQ_PEER_W = rmem_irq_event_if.PEER_IDX_W;
    localparam int RESPONDER_IRQ_PEER_W = responder_irq_event_if.PEER_IDX_W;
    localparam int unsigned ADDR_W = initiator_if.ADDR_W;
    localparam int unsigned LEN_W = initiator_if.LEN_W;
    localparam int unsigned SEQUENCE_W = initiator_if.SEQUENCE_W;
    localparam int unsigned ERROR_W = initiator_if.ERROR_W;
    localparam logic TRANSFER_KIND_DMA = initiator_if.TRANSFER_KIND_DMA;
    localparam logic TRANSFER_KIND_RMEM = initiator_if.TRANSFER_KIND_RMEM;
    localparam int unsigned AXI_DATA_W = memory_read.DATA_W;
    localparam int unsigned AXIS_KEEP_W = memory_output.KEEP_W;
    localparam int unsigned AXIS_DEST_W = PEER_IDX_W + 2;
    localparam int unsigned AXIS_USER_W = initiator_if.AXIS_USER_W;
    localparam int unsigned AXIS_USER_LAST_BIT = initiator_if.AXIS_USER_LAST_BIT;
    localparam int unsigned AXIS_USER_ROLE_BIT = initiator_if.AXIS_USER_ROLE_BIT;
    localparam logic TRANSFER_ROLE_INITIATOR = initiator_if.TRANSFER_ROLE_INITIATOR;
    localparam logic TRANSFER_ROLE_RESPONDER = initiator_if.TRANSFER_ROLE_RESPONDER;
    localparam int unsigned SLOT_IDX_W = FRAGMENT_SLOTS > 1 ? $clog2(FRAGMENT_SLOTS) : 1;
    localparam logic [1:0] ROUTE_PEER = initiator_if.ROUTE_PEER;
    localparam logic [1:0] ROUTE_NON_OETP_DMA = initiator_if.ROUTE_NON_OETP_DMA;

    localparam logic DMA_OP_READ = initiator_if.DMA_OP_READ;
    localparam logic DMA_OP_WRITE = initiator_if.DMA_OP_WRITE;

    localparam logic [1:0] DMA_MODE_MIRROR_TO_LOCAL = 2'd2;
    localparam logic [1:0] DMA_MODE_MIRROR_TO_REMOTE = 2'd3;

    localparam logic [ERROR_W-1:0] DMA_ERROR_NONE = initiator_if.ERROR_NONE;
    localparam logic [ERROR_W-1:0] DMA_ERROR_INVALID = initiator_if.ERROR_LOCAL_INVALID;
    localparam logic [ERROR_W-1:0] DMA_ERROR_AXIS = initiator_if.ERROR_LOCAL_AXIS;
    localparam logic [ERROR_W-1:0] DMA_ERROR_OVERFLOW = initiator_if.ERROR_LOCAL_OVERFLOW;

    // Ethernet (14), oETP write metadata (14), and EndOfData (4) take 32 bytes. Data parameters are
    // rounded to four bytes on the wire in both directions.
    localparam int unsigned MAX_DMA_FRAGMENT_SIZE_BYTES = MAX_RAW_FRAME_SIZE > 32
        ? ((MAX_RAW_FRAME_SIZE - 32) / 4) * 4 : 0;
    wire[31:0] configured_fragment_size =
        endpoint_if.csr_to_core.config_.dma_max_fragment_size.bytes.value;
    wire [31:0] effective_fragment_size = {configured_fragment_size[31:2], 2'b00};

    // CPUIF requests are converted to scalar transport commands.
    openenoc_cpuif_if #(
        .ADDR_W(32),
        .DATA_W(32)
    ) rmem_cpuif();

    assign rmem_cpuif.req = endpoint_if.csr_to_core.rmem.req;
    assign rmem_cpuif.addr = 32'(endpoint_if.csr_to_core.rmem.addr);
    assign rmem_cpuif.req_is_wr = endpoint_if.csr_to_core.rmem.req_is_wr;
    assign rmem_cpuif.wr_data = endpoint_if.csr_to_core.rmem.wr_data;
    assign rmem_cpuif.wr_biten = endpoint_if.csr_to_core.rmem.wr_biten;

    typedef enum logic [3:0] {
        RM_IDLE,
        RM_LOOKUP_REQ,
        RM_LOOKUP_RSP,
        RM_READY,
        RM_SEND,
        RM_WAIT,
        RM_DONE
    } rmem_state_t;
    rmem_state_t rmem_state_reg;

    typedef enum logic [1:0] {
        RM_IRQ_IDLE,
        RM_IRQ_ADMIT,
        RM_IRQ_COMMIT
    } rmem_irq_state_t;
    rmem_irq_state_t rmem_irq_state_reg;

    logic rmem_armed_reg, rmem_write_reg, rmem_hit_reg;
    logic [31:0] rmem_addr_reg, rmem_remote_addr_reg;
    logic [31:0] rmem_wdata_reg, rmem_biten_reg, rmem_rdata_reg;
    logic [PEER_IDX_W-1:0] rmem_peer_reg, rmem_irq_peer_reg;
    logic [SEQUENCE_W-1:0] rmem_sequence_reg;
    logic [ERROR_W-1:0] rmem_error_reg;
    logic rmem_irq_enable_reg;
    logic [NUM_OF_PEERS-1:0] rmem_irq_pending_reg;
    logic [PEER_IDX_W-1:0] rmem_irq_rr_reg;
    wire rmem_lookup_owner = rmem_state_reg == RM_LOOKUP_RSP
        || (rmem_state_reg == RM_LOOKUP_REQ && peer_state_reg != PEER_LOOKUP_REQ
            && peer_state_reg != PEER_LOOKUP_RSP);
    wire rmem_cpl_accept = initiator_cpl_fire && initiator_if.cpl_kind == TRANSFER_KIND_RMEM;
    wire rmem_error_valid = (rmem_cpl_accept && initiator_if.cpl_error)
        || (rmem_state_reg == RM_DONE && rmem_hit_reg && rmem_error_reg != 0);
    wire[PEER_IDX_W-1:0] rmem_error_peer_idx = rmem_state_reg == RM_DONE ? rmem_peer_reg
        : initiator_if.cpl_peer_idx;
    wire[ERROR_W-1:0] rmem_error_code = rmem_state_reg == RM_DONE ? rmem_error_reg
        : initiator_if.cpl_error_code;

    localparam logic [3:0] EVENT_PEER_DMA_COMPLETE = 4'd0;
    localparam logic [3:0] EVENT_NON_OETP_DMA_TX_COMPLETE = 4'd1;
    localparam logic [3:0] EVENT_NON_OETP_DMA_RX_COMPLETE = 4'd2;

    localparam logic [1:0] RD_CLIENT_PEER = 2'd0;
    localparam logic [1:0] RD_CLIENT_RESPONDER = 2'd1;
    localparam logic [1:0] RD_CLIENT_NON_OETP = 2'd2;

    localparam logic [1:0] WR_CLIENT_PEER = 2'd0;
    localparam logic [1:0] WR_CLIENT_RESPONDER = 2'd1;
    localparam logic [1:0] WR_CLIENT_NON_OETP = 2'd2;

    function automatic logic [LEN_W-1:0] fragment_length(input logic [LEN_W-1:0] remaining,
                                                        input logic [LEN_W-1:0] maximum);
        if (remaining > maximum) begin
            fragment_length = maximum;
        end else begin
            fragment_length = remaining;
        end
    endfunction

    function automatic logic [LEN_W-1:0] keep_count(input logic [AXIS_KEEP_W-1:0] keep);
        logic [LEN_W-1:0] count;

        count = '0;
        for (int unsigned n = 0; n < AXIS_KEEP_W; n++) begin
            count = count + LEN_W'(keep[n]);
        end
        return count;
    endfunction

    function automatic logic keep_contiguous(input logic [AXIS_KEEP_W-1:0] keep);
        logic [AXIS_KEEP_W:0] extended_keep;

        extended_keep = {1'b0, keep};
        return keep != '0 && (extended_keep & (extended_keep + 1'b1)) == '0;
    endfunction

    if (NUM_OF_PEERS < 1) begin : g_bad_num_peers
        $fatal(0, "Error: NUM_OF_PEERS must be at least one (instance %m)");
    end

    if (FRAGMENT_SLOTS < 1) begin : g_bad_fragment_slots
        $fatal(0, "Error: FRAGMENT_SLOTS must be positive (instance %m)");
    end

    if (MAX_RAW_FRAME_SIZE < 36 || MAX_RAW_FRAME_SIZE > 8192) begin : g_bad_max_frame
        $fatal(0, {"Error: MAX_RAW_FRAME_SIZE must be between 36 ", "and 8192 (instance %m)"});
    end

    if (memory_write.DATA_W != AXI_DATA_W
        || memory_write.ADDR_W != memory_read.ADDR_W) begin : g_bad_axi_pair
        $fatal(0, {"Error: AXI read and write interface widths must ", "match (instance %m)"});
    end

    if (ADDR_W != memory_read.ADDR_W) begin : g_bad_addr_width
        $fatal(0, {"Error: DMA transfer and AXI address widths must ", "match (instance %m)"});
    end

    if (responder_if.ADDR_W != ADDR_W || responder_if.LEN_W != LEN_W
        || responder_if.SEQUENCE_W != SEQUENCE_W
        || responder_if.ERROR_W != ERROR_W) begin : g_bad_transfer_pair
        $fatal(
            0,
            {
                "Error: initiator and responder transfer ",
                "interface widths must match (instance %m)"
            }
        );
    end

    if (peer_lookup_if.PEER_IDX_W != PEER_IDX_W || initiator_if.PEER_IDX_W != PEER_IDX_W
        || responder_if.PEER_IDX_W != PEER_IDX_W) begin : g_bad_peer_width
        $fatal(0, {"Error: peer index widths must match PEER_IDX_W ", "(instance %m)"});
    end

    if (memory_output.DATA_W != AXI_DATA_W
        || memory_input.DATA_W != AXI_DATA_W) begin : g_bad_axis_data_width
        $fatal(0, {"Error: AXI stream data widths must match ", "AXI_DATA_W (instance %m)"});
    end

    if (memory_output.ID_W < SEQUENCE_W || memory_input.ID_W < SEQUENCE_W
        || memory_output.DEST_W != AXIS_DEST_W || memory_input.DEST_W != AXIS_DEST_W
        || memory_output.USER_W < AXIS_USER_W
        || memory_input.USER_W < AXIS_USER_W) begin : g_bad_axis_metadata_width
        $fatal(0, {"Error: oETP AXI stream metadata widths are ", "insufficient (instance %m)"});
    end

    taxi_dma_desc_if #(
        .SRC_ADDR_W(ADDR_W),
        .DST_ADDR_W(ADDR_W),
        .LEN_W(LEN_W),
        .TAG_W(2),
        .ID_EN(1'b1),
        .ID_W(SEQUENCE_W),
        .DEST_EN(1'b1),
        .DEST_W(AXIS_DEST_W),
        .USER_EN(1'b1),
        .USER_W(AXIS_USER_W)
    ) memory_read_desc_if();

    taxi_dma_desc_if #(
        .SRC_ADDR_W(ADDR_W),
        .DST_ADDR_W(ADDR_W),
        .LEN_W(LEN_W),
        .TAG_W(2),
        .ID_EN(1'b1),
        .ID_W(SEQUENCE_W),
        .DEST_EN(1'b1),
        .DEST_W(AXIS_DEST_W),
        .USER_EN(1'b1),
        .USER_W(AXIS_USER_W)
    ) memory_write_desc_if();

    taxi_axis_if #(
        .DATA_W(AXI_DATA_W),
        .KEEP_EN(1'b1),
        .LAST_EN(1'b1),
        .ID_EN(1'b1),
        .ID_W(SEQUENCE_W),
        .DEST_EN(1'b1),
        .DEST_W(AXIS_DEST_W),
        .USER_EN(1'b1),
        .USER_W(AXIS_USER_W)
    ) dma_rd_axis();

    taxi_axis_if #(
        .DATA_W(AXI_DATA_W),
        .KEEP_EN(1'b1),
        .LAST_EN(1'b1),
        .ID_EN(1'b1),
        .ID_W(SEQUENCE_W),
        .DEST_EN(1'b1),
        .DEST_W(AXIS_DEST_W),
        .USER_EN(1'b1),
        .USER_W(AXIS_USER_W)
    ) dma_wr_axis();

    taxi_axi_dma #(
        .AXI_MAX_BURST_LEN(AXI_MAX_BURST_LEN),
        .UNALIGNED_EN(UNALIGNED_EN)
    ) taxi_axi_dma_inst (
        .clk(clk),
        .rst(rst),
        .rd_desc_req(memory_read_desc_if),
        .rd_desc_sts(memory_read_desc_if),
        .wr_desc_req(memory_write_desc_if),
        .wr_desc_sts(memory_write_desc_if),
        .m_axis_rd_data(dma_rd_axis),
        .s_axis_wr_data(dma_wr_axis),
        .m_axi_wr(memory_write),
        .m_axi_rd(memory_read),
        .read_enable(1'b1),
        .write_enable(1'b1),
        .write_abort(1'b0)
    );

    typedef enum logic [3:0] {
        PEER_IDLE,
        PEER_LOOKUP_REQ,
        PEER_LOOKUP_RSP,
        PEER_ADMIT
    } peer_state_t;

    typedef enum logic [2:0] {
        NON_TX_IDLE,
        NON_TX_ADMIT,
        NON_TX_QUEUE,
        NON_TX_WAIT,
        NON_TX_COMMIT
    } raw_tx_state_t;

    typedef enum logic [2:0] {
        NON_RX_IDLE,
        NON_RX_ADMIT,
        NON_RX_ARMED,
        NON_RX_QUEUE,
        NON_RX_WAIT,
        NON_RX_COMMIT
    } raw_rx_state_t;

    typedef enum logic [2:0] {
        RESP_IDLE,
        RESP_RD_QUEUE,
        RESP_WR_QUEUE,
        RESP_WAIT,
        RESP_RMEM_REQ,
        RESP_RMEM_WAIT,
        RESP_COMPLETE
    } responder_state_t;

    typedef enum logic [1:0] {
        RESP_IRQ_IDLE,
        RESP_IRQ_ADMIT,
        RESP_IRQ_COMMIT
    } responder_irq_state_t;

    typedef enum logic [1:0] {
        RD_IDLE,
        RD_DESC,
        RD_STREAM
    } memory_read_state_t;

    typedef enum logic [1:0] {
        WR_IDLE,
        WR_DESC,
        WR_STREAM
    } memory_write_state_t;

    peer_state_t peer_state_reg;
    raw_tx_state_t raw_tx_state_reg;
    raw_rx_state_t raw_rx_state_reg;
    responder_state_t responder_state_reg;
    responder_irq_state_t responder_irq_state_reg;
    logic [31:0] responder_biten_reg, responder_wdata_reg, responder_rdata_reg;
    logic responder_error_recorded_reg;
    logic responder_rx_required_reg;
    logic responder_rx_done_reg;
    logic responder_memory_done_reg;
    logic responder_payload_done_reg;
    logic [LEN_W-1:0] responder_rx_len_reg;
    logic [ERROR_W-1:0] responder_rx_error_reg;
    logic peer_tx_status_valid_reg;
    logic [PEER_IDX_W-1:0] peer_tx_status_peer_reg;
    logic [SEQUENCE_W-1:0] peer_tx_status_sequence_reg;
    logic [LEN_W-1:0] peer_tx_status_len_reg;
    logic [ERROR_W-1:0] peer_tx_status_error_reg;
    logic any_sent_fragment;
    wire responder_drop_payload = responder_state_reg == RESP_WAIT && responder_memory_done_reg &&
        responder_cpl_error_reg && responder_rx_required_reg && !responder_payload_done_reg &&
        memory_input.tvalid && memory_input.tdest == {ROUTE_PEER, responder_peer_idx_reg} &&
        memory_input.tuser[AXIS_USER_ROLE_BIT] == TRANSFER_ROLE_RESPONDER &&
        memory_input.tid == responder_sequence_reg;

    logic responder_irq_enable_reg;
    logic [3:0] responder_irq_source_reg;
    logic [PEER_IDX_W-1:0] responder_irq_peer_idx_reg;
    wire responder_error_valid = responder_state_reg == RESP_COMPLETE && responder_cpl_error_reg
        && !responder_error_recorded_reg;
    memory_read_state_t memory_read_state_reg;
    memory_write_state_t memory_write_state_reg;

    logic [NUM_OF_PEERS-1:0] peer_idle_reg;
    logic [NUM_OF_PEERS-1:0] peer_done_reg;
    logic [NUM_OF_PEERS-1:0] peer_error_reg;
    logic [ERROR_W-1:0] peer_error_code_reg[NUM_OF_PEERS];
    logic [NUM_OF_PEERS-1:0] peer_request_hwclr_reg;

    logic raw_tx_idle_reg;
    logic raw_tx_done_reg;
    logic raw_tx_error_reg;
    logic [ERROR_W-1:0] raw_tx_error_code_reg;
    logic [LEN_W-1:0] raw_tx_transferred_len_reg;
    logic raw_tx_request_hwclr_reg;

    logic raw_rx_idle_reg;
    logic raw_rx_armed_reg;
    logic raw_rx_done_reg;
    logic raw_rx_error_reg;
    logic [ERROR_W-1:0] raw_rx_error_code_reg;
    logic [LEN_W-1:0] raw_rx_received_len_reg;
    logic raw_rx_request_hwclr_reg;

    logic [PEER_IDX_W-1:0] peer_index_reg;
    logic [PEER_IDX_W-1:0] peer_rr_reg;
    logic [1:0] peer_mode_reg;
    logic peer_irq_enable_reg;
    logic [ADDR_W-1:0] peer_local_addr_reg;
    logic [ADDR_W-1:0] peer_remote_addr_reg;
    logic [LEN_W-1:0] peer_size_reg;
    // Accepted peers retain independent snapshots. Fragment slots form a bounded window of
    // commands, allowing responses to arrive in any peer/sequence order.
    typedef struct packed {
        logic [1:0] mode;
        logic [ADDR_W-1:0] local_addr;
        logic [ADDR_W-1:0] remote_addr;
        logic [LEN_W-1:0] size;
        logic [LEN_W-1:0] max_fragment_size;
        logic [LEN_W-1:0] issued;
        logic [SEQUENCE_W-1:0] next_sequence;
        logic [ERROR_W-1:0] error_code;
        logic irq_reserved;
    } peer_context_t;
    peer_context_t peer_context_reg[NUM_OF_PEERS];
    logic [NUM_OF_PEERS-1:0] peer_active_reg;
    logic [NUM_OF_PEERS-1:0] peer_commit_pending_reg;
    logic [NUM_OF_PEERS-1:0] peer_has_fragment;
    logic [PEER_IDX_W-1:0] issue_rr_reg;
    logic peer_commit_valid_reg;
    logic [PEER_IDX_W-1:0] peer_commit_index_reg;

    typedef struct packed {
        logic valid;
        logic command_sent;
        logic local_started;
        logic local_done;
        logic remote_done;
        logic op;
        logic [PEER_IDX_W-1:0] peer_idx;
        logic [SEQUENCE_W-1:0] sequence_;
        logic [ADDR_W-1:0] local_addr;
        logic [ADDR_W-1:0] remote_addr;
        logic [LEN_W-1:0] len;
        logic last;
        logic [ERROR_W-1:0] local_error;
        logic [ERROR_W-1:0] completion_error;
    } fragment_context_t;
    fragment_context_t fragment_reg[FRAGMENT_SLOTS];
    logic command_valid_reg;
    logic [SLOT_IDX_W-1:0] command_slot_reg;
    logic [SLOT_IDX_W-1:0] memory_read_slot_reg;
    logic [SLOT_IDX_W-1:0] memory_write_slot_reg;
    logic free_slot_found, command_slot_found, memory_read_slot_found, memory_write_slot_found;
    logic retire_slot_found, issue_peer_found, commit_peer_found;
    logic[SLOT_IDX_W-1:0] free_slot, command_slot, memory_read_slot, memory_write_slot, retire_slot;
    logic [PEER_IDX_W-1:0] issue_peer, commit_peer;
    logic cpl_slot_found;
    logic [SLOT_IDX_W-1:0] cpl_slot;

    logic [ADDR_W-1:0] raw_tx_addr_reg;
    logic [LEN_W-1:0] raw_tx_len_reg;
    logic raw_tx_irq_reserved_reg;

    logic [ADDR_W-1:0] raw_rx_addr_reg;
    logic [LEN_W-1:0] raw_rx_capacity_reg;
    logic raw_rx_irq_reserved_reg;

    logic responder_op_reg;
    logic responder_kind_reg;
    logic [ADDR_W-1:0] responder_addr_reg;
    logic [LEN_W-1:0] responder_len_reg;
    logic [PEER_IDX_W-1:0] responder_peer_idx_reg;
    logic [SEQUENCE_W-1:0] responder_sequence_reg;
    logic responder_last_reg;
    logic [LEN_W-1:0] responder_cpl_len_reg;
    logic responder_cpl_error_reg;
    logic [ERROR_W-1:0] responder_cpl_error_code_reg;

    logic [1:0] memory_read_rr_reg;
    logic [1:0] memory_read_client_reg;
    logic [ADDR_W-1:0] memory_read_addr_reg;
    logic [LEN_W-1:0] memory_read_len_reg;
    logic [LEN_W-1:0] memory_read_remaining_reg;
    logic [ERROR_W-1:0] memory_read_prior_error_reg;
    logic [PEER_IDX_W-1:0] memory_read_peer_idx_reg;
    logic [SEQUENCE_W-1:0] memory_read_sequence_reg;
    logic memory_read_last_reg;
    logic [LEN_W-1:0] memory_read_byte_count_reg;
    logic memory_read_saw_last_reg;
    logic memory_read_status_seen_reg;
    logic [ERROR_W-1:0] memory_read_status_error_reg;
    logic memory_read_accept_pulse_reg;
    logic [1:0] memory_read_accept_client_reg;
    logic memory_read_done_pulse_reg;
    logic [1:0] memory_read_done_client_reg;
    logic [LEN_W-1:0] memory_read_done_len_reg;
    logic [ERROR_W-1:0] memory_read_done_error_reg;

    logic [1:0] memory_write_rr_reg;
    logic [1:0] memory_write_client_reg;
    logic [ADDR_W-1:0] memory_write_addr_reg;
    logic [LEN_W-1:0] memory_write_len_reg;
    logic [PEER_IDX_W-1:0] memory_write_peer_idx_reg;
    logic [SEQUENCE_W-1:0] memory_write_sequence_reg;
    logic memory_write_last_reg;
    logic [LEN_W-1:0] memory_write_input_len_reg;
    logic memory_write_saw_last_reg;
    logic memory_write_status_seen_reg;
    logic [LEN_W-1:0] memory_write_status_len_reg;
    logic [ERROR_W-1:0] memory_write_status_error_reg;
    logic [ERROR_W-1:0] memory_write_stream_error_reg;
    logic memory_write_accept_pulse_reg;
    logic [1:0] memory_write_accept_client_reg;
    logic memory_write_first_pulse_reg;
    logic [1:0] memory_write_first_client_reg;
    logic memory_write_done_pulse_reg;
    logic [1:0] memory_write_done_client_reg;
    logic [LEN_W-1:0] memory_write_done_len_reg;
    logic [ERROR_W-1:0] memory_write_done_error_reg;

    logic [2:0] memory_read_job_valid;
    logic [2:0] memory_write_job_valid;
    logic memory_read_pick_valid;
    logic [1:0] memory_read_pick;
    logic memory_write_pick_valid;
    logic [1:0] memory_write_pick;

    logic [AXI_DATA_W-1:0] memory_write_src_tdata;
    logic [AXIS_KEEP_W-1:0] memory_write_src_tkeep;
    logic [SEQUENCE_W-1:0] memory_write_src_tid;
    logic [AXIS_DEST_W-1:0] memory_write_src_tdest;
    logic [AXIS_USER_W-1:0] memory_write_src_tuser;
    logic memory_write_src_tlast;
    logic memory_write_src_tvalid;
    logic memory_write_src_tready;

    logic peer_request_found;
    logic [PEER_IDX_W-1:0] peer_request_index;

    function automatic logic responder_window_valid(
        input logic [PEER_IDX_W-1:0] peer_idx, input logic kind, op,
        input logic [ADDR_W-1:0] addr, input logic [LEN_W-1:0] len);
        logic [32:0] base_addr, limit_addr, end_addr;
        logic [1:0] mode;
        if (int'(peer_idx) >= NUM_OF_PEERS) return 1'b0;
        base_addr = {1'b0, endpoint_if.csr_to_core.peers.entry[peer_idx].local_address.base.value};
        limit_addr = base_addr +
            {1'b0, endpoint_if.csr_to_core.peers.entry[peer_idx].size.bytes.value};
        end_addr = {1'b0, addr} + {1'b0, len};
        mode = endpoint_if.csr_to_core.peers.entry[peer_idx].dma.mode.value;
        return len != 0 && limit_addr <= 33'h100000000 && {1'b0, addr} >= base_addr && end_addr <=
            limit_addr && (kind == TRANSFER_KIND_RMEM ? (mode == 1 && len == 4 && addr[1:0] == 0) :
                        (op == DMA_OP_WRITE ? mode == 2 : mode == 3));
    endfunction

    always_comb begin
        peer_request_found = 1'b0;
        peer_request_index = peer_rr_reg;

        for (int unsigned offset = 0; offset < NUM_OF_PEERS; offset++) begin
            int unsigned candidate;
            candidate = int'(peer_rr_reg) + offset;
            if (candidate >= NUM_OF_PEERS) begin
                candidate = candidate - NUM_OF_PEERS;
            end

            if (!peer_request_found
                && endpoint_if.csr_to_core.peers.entry[candidate].dma.request.value
                && peer_idle_reg[candidate] && !peer_commit_pending_reg[candidate]
                && !(peer_commit_valid_reg
                    && peer_commit_index_reg == PEER_IDX_W'(candidate))) begin
                peer_request_found = 1'b1;
                peer_request_index = PEER_IDX_W'(candidate);
            end
        end
    end

    always_comb begin
        free_slot_found = 1'b0;
        command_slot_found = 1'b0;
        memory_read_slot_found = 1'b0;
        memory_write_slot_found = 1'b0;
        retire_slot_found = 1'b0;
        cpl_slot_found = 1'b0;
        free_slot = '0;
        command_slot = '0;
        memory_read_slot = '0;
        memory_write_slot = '0;
        retire_slot = '0;
        cpl_slot = '0;
        peer_has_fragment = '0;
        any_sent_fragment = 1'b0;
        for (int unsigned n = 0; n < FRAGMENT_SLOTS; n++) begin
            if (!fragment_reg[n].valid && !free_slot_found) begin
                free_slot_found = 1'b1;
                free_slot = SLOT_IDX_W'(n);
            end
            if (fragment_reg[n].valid) begin
                if (fragment_reg[n].command_sent) any_sent_fragment = 1'b1;
                peer_has_fragment[fragment_reg[n].peer_idx] = 1'b1;
                if (!fragment_reg[n].command_sent
                    && peer_context_reg[fragment_reg[n].peer_idx].error_code == DMA_ERROR_NONE
                    && !command_slot_found) begin
                    command_slot_found = 1'b1;
                    command_slot = SLOT_IDX_W'(n);
                end
                if (fragment_reg[n].command_sent && !fragment_reg[n].local_started
                    && !fragment_reg[n].local_done && fragment_reg[n].op == DMA_OP_WRITE
                    && !(initiator_if.cpl_valid && initiator_if.cpl_kind == TRANSFER_KIND_DMA
                        && initiator_if.cpl_error
                        && initiator_if.cpl_peer_idx == fragment_reg[n].peer_idx
                        && initiator_if.cpl_sequence == fragment_reg[n].sequence_)
                    && !memory_read_slot_found) begin
                    memory_read_slot_found = 1'b1;
                    memory_read_slot = SLOT_IDX_W'(n);
                end
                if (fragment_reg[n].command_sent && !fragment_reg[n].local_started
                    && !fragment_reg[n].local_done && fragment_reg[n].op == DMA_OP_READ
                    && memory_input.tvalid
                    && memory_input.tdest == {ROUTE_PEER, fragment_reg[n].peer_idx}
                    && memory_input.tuser[AXIS_USER_ROLE_BIT] == TRANSFER_ROLE_INITIATOR
                    && memory_input.tid == fragment_reg[n].sequence_
                    && !memory_write_slot_found) begin
                    memory_write_slot_found = 1'b1;
                    memory_write_slot = SLOT_IDX_W'(n);
                end
                if (fragment_reg[n].local_done && fragment_reg[n].remote_done
                    && !retire_slot_found) begin
                    retire_slot_found = 1'b1;
                    retire_slot = SLOT_IDX_W'(n);
                end
                if (initiator_if.cpl_kind == TRANSFER_KIND_DMA && fragment_reg[n].command_sent
                    && !fragment_reg[n].remote_done
                    && fragment_reg[n].peer_idx == initiator_if.cpl_peer_idx
                    && fragment_reg[n].sequence_ == initiator_if.cpl_sequence
                    && !cpl_slot_found) begin
                    cpl_slot_found = 1'b1;
                    cpl_slot = SLOT_IDX_W'(n);
                end
            end
        end

        issue_peer_found = 1'b0;
        commit_peer_found = 1'b0;
        issue_peer = '0;
        commit_peer = '0;
        for (int unsigned offset = 0; offset < NUM_OF_PEERS; offset++) begin
            int unsigned candidate;
            candidate = int'(issue_rr_reg) + offset;
            if (candidate >= NUM_OF_PEERS) candidate -= NUM_OF_PEERS;
            if (!issue_peer_found && peer_active_reg[candidate]
                && peer_context_reg[candidate].error_code == DMA_ERROR_NONE
                && peer_context_reg[candidate].issued < peer_context_reg[candidate].size) begin
                issue_peer_found = 1'b1;
                issue_peer = PEER_IDX_W'(candidate);
            end
            if (!commit_peer_found && peer_commit_pending_reg[candidate]) begin
                commit_peer_found = 1'b1;
                commit_peer = PEER_IDX_W'(candidate);
            end
        end

        memory_read_job_valid[RD_CLIENT_PEER] = memory_read_slot_found;
        memory_read_job_valid[RD_CLIENT_RESPONDER] = responder_state_reg == RESP_RD_QUEUE;
        memory_read_job_valid[RD_CLIENT_NON_OETP] = raw_tx_state_reg == NON_TX_QUEUE;

        // Descriptor selection follows the FIFO head, never a separate arbiter that could pair a
        // descriptor with another frame's payload.
        memory_write_job_valid[WR_CLIENT_PEER] = memory_write_slot_found;
        memory_write_job_valid[WR_CLIENT_RESPONDER] = responder_state_reg == RESP_WR_QUEUE &&
            memory_input.tvalid && memory_input.tdest == {ROUTE_PEER, responder_peer_idx_reg} &&
            memory_input.tuser[AXIS_USER_ROLE_BIT] == TRANSFER_ROLE_RESPONDER &&
            memory_input.tid == responder_sequence_reg;
        memory_write_job_valid[WR_CLIENT_NON_OETP] = raw_rx_state_reg == NON_RX_QUEUE
            && memory_input.tvalid && memory_input.tdest[PEER_IDX_W+:2] == ROUTE_NON_OETP_DMA;

        memory_read_pick_valid = 1'b0;
        memory_read_pick = memory_read_rr_reg;
        memory_write_pick_valid = 1'b0;
        memory_write_pick = memory_write_rr_reg;
        for (int unsigned offset = 0; offset < 3; offset++) begin
            int unsigned candidate;
            candidate = int'(memory_read_rr_reg) + offset;
            if (candidate >= 3) candidate -= 3;
            if (!memory_read_pick_valid && memory_read_job_valid[candidate]) begin
                memory_read_pick_valid = 1'b1;
                memory_read_pick = 2'(candidate);
            end
            candidate = int'(memory_write_rr_reg) + offset;
            if (candidate >= 3) candidate -= 3;
            if (!memory_write_pick_valid && memory_write_job_valid[candidate]) begin
                memory_write_pick_valid = 1'b1;
                memory_write_pick = 2'(candidate);
            end
        end
    end

    always_comb begin
        memory_output.tdata = dma_rd_axis.tdata;
        memory_output.tkeep = dma_rd_axis.tkeep;
        memory_output.tstrb = dma_rd_axis.tstrb;
        memory_output.tid = dma_rd_axis.tid;
        memory_output.tdest = dma_rd_axis.tdest;
        memory_output.tuser = memory_output.USER_W'(dma_rd_axis.tuser);
        memory_output.tlast = dma_rd_axis.tlast && memory_read_remaining_reg == 0;
        memory_output.tvalid = 1'b0;

        dma_rd_axis.tready = 1'b0;

        if (memory_read_state_reg == RD_STREAM) begin
            memory_output.tvalid = dma_rd_axis.tvalid;
            dma_rd_axis.tready = memory_output.tready;
        end
    end

    always_comb begin
        memory_write_src_tdata = memory_input.tdata;
        memory_write_src_tkeep = memory_input.tkeep;
        memory_write_src_tid = memory_input.tid;
        memory_write_src_tdest = memory_input.tdest;
        memory_write_src_tuser = memory_input.tuser[AXIS_USER_W-1:0];
        memory_write_src_tlast = memory_input.tlast;
        memory_write_src_tvalid = memory_input.tvalid && memory_write_state_reg == WR_STREAM;
        dma_wr_axis.tdata = memory_write_src_tdata;
        dma_wr_axis.tkeep = memory_write_src_tkeep;
        dma_wr_axis.tstrb = memory_write_src_tkeep;
        dma_wr_axis.tid = memory_write_src_tid;
        dma_wr_axis.tdest = memory_write_src_tdest;
        dma_wr_axis.tuser = memory_write_src_tuser;
        dma_wr_axis.tlast = memory_write_src_tlast;
        dma_wr_axis.tvalid = memory_write_src_tvalid;
        memory_write_src_tready = dma_wr_axis.tready;
        memory_input.tready = memory_write_state_reg == WR_STREAM ? dma_wr_axis.tready
            : responder_drop_payload;
    end

    assign endpoint_if.core_to_csr.non_oetp_dma.rx.command_status.armed.next = raw_rx_armed_reg;
    logic csr_raw_rx_clear_errors_hwclr_reg;
    assign endpoint_if.core_to_csr.non_oetp_dma.rx.command_status.clear_errors.hwclr =
        csr_raw_rx_clear_errors_hwclr_reg;
    assign endpoint_if.core_to_csr.non_oetp_dma.rx.command_status.done.next = raw_rx_done_reg;
    assign endpoint_if.core_to_csr.non_oetp_dma.rx.command_status.error.next = raw_rx_error_reg;
    assign endpoint_if.core_to_csr.non_oetp_dma.rx.command_status.error_code.next =
        raw_rx_error_code_reg;
    assign endpoint_if.core_to_csr.non_oetp_dma.rx.command_status.idle.next = raw_rx_idle_reg;
    assign endpoint_if.core_to_csr.non_oetp_dma.rx.command_status.request.hwclr =
        raw_rx_request_hwclr_reg;
    assign endpoint_if.core_to_csr.non_oetp_dma.rx.received_length.bytes.next =
        raw_rx_received_len_reg;
    logic csr_raw_tx_clear_errors_hwclr_reg;
    assign endpoint_if.core_to_csr.non_oetp_dma.tx.command_status.clear_errors.hwclr =
        csr_raw_tx_clear_errors_hwclr_reg;
    assign endpoint_if.core_to_csr.non_oetp_dma.tx.command_status.done.next = raw_tx_done_reg;
    assign endpoint_if.core_to_csr.non_oetp_dma.tx.command_status.error.next = raw_tx_error_reg;
    assign endpoint_if.core_to_csr.non_oetp_dma.tx.command_status.error_code.next =
        raw_tx_error_code_reg;
    assign endpoint_if.core_to_csr.non_oetp_dma.tx.command_status.idle.next = raw_tx_idle_reg;
    assign endpoint_if.core_to_csr.non_oetp_dma.tx.command_status.request.hwclr =
        raw_tx_request_hwclr_reg;
    assign endpoint_if.core_to_csr.non_oetp_dma.tx.transferred_length.bytes.next =
        raw_tx_transferred_len_reg;
    logic peer_csr_clear_error_hwclr_reg[NUM_OF_PEERS];
    assign endpoint_if.core_to_csr.rmem.rd_ack = rmem_cpuif.rd_ack;
    assign endpoint_if.core_to_csr.rmem.rd_data = rmem_cpuif.rd_data;
    assign endpoint_if.core_to_csr.rmem.wr_ack = rmem_cpuif.wr_ack;
    for (genvar n = 0; n < NUM_OF_PEERS; n++) begin : g_csr_peer_output
        assign endpoint_if.core_to_csr.peers.entry[n].dma.clear_error.hwclr =
            peer_csr_clear_error_hwclr_reg[n];
        assign endpoint_if.core_to_csr.peers.entry[n].dma.done.next = peer_done_reg[n];
        assign endpoint_if.core_to_csr.peers.entry[n].dma.error.next = peer_error_reg[n];
        assign endpoint_if.core_to_csr.peers.entry[n].dma.error_code.next = peer_error_code_reg[n];
        assign endpoint_if.core_to_csr.peers.entry[n].dma.idle.next = peer_idle_reg[n];
        assign endpoint_if.core_to_csr.peers.entry[n].dma.request.hwclr = peer_request_hwclr_reg[n];
    end

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
    wire rmem_irq_admit_fire = rmem_irq_event_if.admit_valid && rmem_irq_event_if.admit_ready;
    wire rmem_irq_commit_fire = rmem_irq_event_if.commit_valid && rmem_irq_event_if.commit_ready;
    wire responder_irq_admit_fire = responder_irq_event_if.admit_valid
        && responder_irq_event_if.admit_ready;
    wire responder_irq_commit_fire = responder_irq_event_if.commit_valid
        && responder_irq_event_if.commit_ready;
    wire peer_irq_admit_fire = irq_event_if[0].admit_valid && irq_event_if[0].admit_ready;
    wire peer_irq_commit_fire = irq_event_if[0].commit_valid && irq_event_if[0].commit_ready;
    wire raw_tx_irq_admit_fire = irq_event_if[1].admit_valid && irq_event_if[1].admit_ready;
    wire raw_tx_irq_commit_fire = irq_event_if[1].commit_valid && irq_event_if[1].commit_ready;
    wire raw_rx_irq_admit_fire = irq_event_if[2].admit_valid && irq_event_if[2].admit_ready;
    wire raw_rx_irq_commit_fire = irq_event_if[2].commit_valid && irq_event_if[2].commit_ready;
    wire memory_read_descriptor_req_fire = memory_read_desc_if.req_valid
        && memory_read_desc_if.req_ready;
    wire memory_write_descriptor_req_fire = memory_write_desc_if.req_valid
        && memory_write_desc_if.req_ready;

    always_ff @(posedge clk) begin : rmem_control
        peer_lookup_if.req_valid <= rst ? '0
            : ((rmem_lookup_owner ? rmem_state_reg == RM_LOOKUP_REQ
                    : peer_state_reg == PEER_LOOKUP_REQ) && !(lookup_req_fire));
        peer_lookup_if.req_type <= rst ? '0 : (rmem_lookup_owner ? 2'd1 : 2'd0);
        peer_lookup_if.req_mode_mask <= rst ? '0 : (rmem_lookup_owner ? 4'b0010 : 4'b1100);
        peer_lookup_if.req_peer_idx <= rst ? '0 : peer_index_reg;
        peer_lookup_if.req_rmem_addr <= rst ? '0 : rmem_addr_reg;
        peer_lookup_if.req_mac_addr <= '0;
        peer_lookup_if.rsp_ready <= rst ? '0
            : ((rmem_lookup_owner ? rmem_state_reg == RM_LOOKUP_RSP
                    : peer_state_reg == PEER_LOOKUP_RSP) && !(lookup_rsp_fire));
        rmem_cpuif.wr_ack <= rst ? '0 : (!rst && rmem_state_reg == RM_DONE && rmem_write_reg);
        rmem_cpuif.rd_ack <= rst ? '0 : (!rst && rmem_state_reg == RM_DONE && !rmem_write_reg);
        rmem_cpuif.wr_err <= 1'b0;
        rmem_cpuif.rd_err <= 1'b0;
        rmem_cpuif.rd_data <= rst ? '0 : (rmem_error_reg != 0 ? 32'hffffffff : rmem_rdata_reg);
        case (rmem_state_reg)
            RM_IDLE: if (rmem_cpuif.req && rmem_armed_reg) rmem_state_reg <= RM_LOOKUP_REQ;
            RM_LOOKUP_REQ:
                if (rmem_lookup_owner && lookup_req_fire) rmem_state_reg <= RM_LOOKUP_RSP;
            RM_LOOKUP_RSP: if (lookup_rsp_fire) rmem_state_reg <= RM_READY;
            RM_READY:
                if (rmem_error_reg != 0) rmem_state_reg <= RM_DONE;
                else if (!command_valid_reg && !any_sent_fragment) rmem_state_reg <= RM_SEND;
            RM_SEND:
                if (initiator_req_fire && initiator_if.req_kind == TRANSFER_KIND_RMEM)
                    rmem_state_reg <= RM_WAIT;
            RM_WAIT: if (rmem_cpl_accept) rmem_state_reg <= RM_DONE;
            RM_DONE: rmem_state_reg <= rmem_cpuif.req && rmem_armed_reg ? RM_LOOKUP_REQ : RM_IDLE;
            default: rmem_state_reg <= RM_IDLE;
        endcase
        if (!rmem_cpuif.req) rmem_armed_reg <= 1'b1;
        if ((rmem_state_reg == RM_IDLE || rmem_state_reg == RM_DONE) && rmem_cpuif.req
            && rmem_armed_reg) begin
            rmem_armed_reg <= 1'b0;
            rmem_addr_reg <= rmem_cpuif.addr;
            rmem_write_reg <= rmem_cpuif.req_is_wr;
            rmem_wdata_reg <= rmem_cpuif.wr_data;
            rmem_biten_reg <= rmem_cpuif.wr_biten;
            rmem_error_reg <= DMA_ERROR_NONE;
            rmem_hit_reg <= 1'b0;
        end
        if (rmem_state_reg == RM_LOOKUP_RSP && peer_lookup_if.rsp_valid) begin
            logic [32:0] displacement, remote_addr;

            displacement = {1'b0, rmem_addr_reg} - {1'b0, peer_lookup_if.rsp_rmem_offset};
            remote_addr = {1'b0, peer_lookup_if.rsp_remote_addr} + displacement;
            rmem_hit_reg <= peer_lookup_if.rsp_hit;
            rmem_peer_reg <= peer_lookup_if.rsp_peer_idx;
            rmem_irq_enable_reg <= endpoint_if.csr_to_core.irq.event_enable.rmem_error.value;
            rmem_remote_addr_reg <= remote_addr[31:0];
            if (!peer_lookup_if.rsp_hit || rmem_addr_reg[1:0] != 0
                || displacement + 33'd4 > {1'b0, peer_lookup_if.rsp_size}
                || remote_addr + 33'd4 > 33'h100000000 || remote_addr[1:0] != 0)
                rmem_error_reg <= DMA_ERROR_INVALID;
        end
        if (rmem_state_reg == RM_WAIT && rmem_cpl_accept) begin
            rmem_irq_enable_reg <= endpoint_if.csr_to_core.irq.event_enable.rmem_error.value;
            rmem_rdata_reg <= initiator_if.cpl_rdata;
            rmem_error_reg <= initiator_if.cpl_error ? initiator_if.cpl_error_code : DMA_ERROR_NONE;
            if (initiator_if.cpl_peer_idx != rmem_peer_reg
                || initiator_if.cpl_sequence != rmem_sequence_reg
                || initiator_if.cpl_op != rmem_write_reg
                || (!initiator_if.cpl_error && initiator_if.cpl_transferred_len != 4))
                rmem_error_reg <= DMA_ERROR_AXIS;
        end
        if (rmem_state_reg == RM_DONE) begin
            rmem_sequence_reg <= rmem_sequence_reg + 1'b1;
        end
        if (rst) begin
            rmem_state_reg <= RM_IDLE;
            rmem_armed_reg <= 1'b1;
            rmem_write_reg <= 1'b0;
            rmem_hit_reg <= 1'b0;
            rmem_addr_reg <= '0;
            rmem_remote_addr_reg <= '0;
            rmem_wdata_reg <= '0;
            rmem_biten_reg <= '0;
            rmem_rdata_reg <= '0;
            rmem_peer_reg <= '0;
            rmem_sequence_reg <= '0;
            rmem_error_reg <= '0;
            rmem_irq_enable_reg <= 1'b0;
        end
    end

    always_ff @(posedge clk) begin : rmem_irq_control
        logic rmem_irq_pending_found;
        logic [PEER_IDX_W-1:0] rmem_irq_pending_peer;

        rmem_irq_event_if.admit_valid <= rst ? '0 : ((rmem_irq_state_reg == RM_IRQ_ADMIT)
                && !(rmem_irq_admit_fire));
        rmem_irq_event_if.admit_source <= rst ? '0 : (rmem_irq_event_if.EVENT_RMEM_ERROR);
        rmem_irq_event_if.admit_enable <= rst ? '0 : 1'b1;
        rmem_irq_event_if.commit_valid <= rst ? '0 : ((rmem_irq_state_reg == RM_IRQ_COMMIT)
                && !(rmem_irq_commit_fire));
        rmem_irq_event_if.commit_source <= rst ? '0 : (rmem_irq_event_if.EVENT_RMEM_ERROR);
        rmem_irq_event_if.commit_peer_idx <= rst ? '0 : (RMEM_IRQ_PEER_W'(rmem_irq_peer_reg));
        rmem_irq_pending_found = 1'b0;
        rmem_irq_pending_peer = '0;
        for (int offset = 0; offset < NUM_OF_PEERS; offset++) begin
            int candidate;
            candidate = int'(rmem_irq_rr_reg) + offset;
            if (candidate >= NUM_OF_PEERS) candidate -= NUM_OF_PEERS;
            if (rmem_irq_pending_reg[candidate] && !rmem_irq_pending_found) begin
                rmem_irq_pending_found = 1'b1;
                rmem_irq_pending_peer = PEER_IDX_W'(candidate);
            end
        end
        case (rmem_irq_state_reg)
            RM_IRQ_IDLE: if (rmem_irq_pending_found) rmem_irq_state_reg <= RM_IRQ_ADMIT;
            RM_IRQ_ADMIT:
                if (rmem_irq_admit_fire)
                    rmem_irq_state_reg <= rmem_irq_event_if.admit_reserved ? RM_IRQ_COMMIT
                        : RM_IRQ_IDLE;
            RM_IRQ_COMMIT: if (rmem_irq_commit_fire) rmem_irq_state_reg <= RM_IRQ_IDLE;
            default: rmem_irq_state_reg <= RM_IRQ_IDLE;
        endcase

        if (rmem_irq_state_reg == RM_IRQ_IDLE && rmem_irq_pending_found)
            rmem_irq_peer_reg <= rmem_irq_pending_peer;
        if (rmem_irq_state_reg == RM_IRQ_ADMIT && rmem_irq_admit_fire) begin
            rmem_irq_pending_reg[rmem_irq_peer_reg] <= 1'b0;
            rmem_irq_rr_reg <= rmem_irq_peer_reg == PEER_IDX_W'(NUM_OF_PEERS - 1) ? '0
                : rmem_irq_peer_reg + 1'b1;
        end
        if (rmem_state_reg == RM_DONE && rmem_hit_reg && rmem_error_reg != 0 && rmem_irq_enable_reg)
            rmem_irq_pending_reg[rmem_peer_reg] <= 1'b1;
        if (rst) begin
            rmem_irq_state_reg <= RM_IRQ_IDLE;
            rmem_irq_peer_reg <= '0;
            rmem_irq_pending_reg <= '0;
            rmem_irq_rr_reg <= '0;
        end
    end

    always_ff @(posedge clk) begin : peer_control
        initiator_if.req_valid <= rst ? '0 : ((rmem_state_reg == RM_SEND || command_valid_reg)
                && !(initiator_req_fire));
        initiator_if.req_error_code <= '0;
        initiator_if.req_rx_status <= 1'b0;
        initiator_if.tx_status_valid <= !rst && peer_tx_status_valid_reg
            && !initiator_tx_status_fire;
        initiator_if.tx_status_peer_idx <= rst ? '0 : peer_tx_status_peer_reg;
        initiator_if.tx_status_sequence <= rst ? '0 : (peer_tx_status_sequence_reg);
        initiator_if.tx_status_len <= rst ? '0 : peer_tx_status_len_reg;
        initiator_if.tx_status_error_code <= rst ? '0 : (peer_tx_status_error_reg);
        initiator_if.rx_status_valid <= 1'b0;
        initiator_if.rx_status_peer_idx <= '0;
        initiator_if.rx_status_sequence <= '0;
        initiator_if.rx_status_len <= '0;
        initiator_if.rx_status_error_code <= '0;
        initiator_if.req_kind <= rst ? '0
            : (rmem_state_reg == RM_SEND ? TRANSFER_KIND_RMEM : TRANSFER_KIND_DMA);
        initiator_if.req_biten <= rst ? '0 : rmem_biten_reg;
        initiator_if.req_wdata <= rst ? '0 : rmem_wdata_reg;
        initiator_if.req_op <= rst ? '0
            : (rmem_state_reg == RM_SEND ? rmem_write_reg : fragment_reg[command_slot_reg].op);
        initiator_if.req_addr <= rst ? '0
            : (rmem_state_reg == RM_SEND ? rmem_remote_addr_reg
                : fragment_reg[command_slot_reg].remote_addr);
        initiator_if.req_len <= rst ? '0
            : (rmem_state_reg == RM_SEND ? LEN_W'(4) : fragment_reg[command_slot_reg].len);
        initiator_if.req_peer_idx <= rst ? '0
            : (rmem_state_reg == RM_SEND ? rmem_peer_reg : fragment_reg[command_slot_reg].peer_idx);
        initiator_if.req_sequence <= rst ? '0
            : (rmem_state_reg == RM_SEND ? rmem_sequence_reg
                : fragment_reg[command_slot_reg].sequence_);
        initiator_if.req_last <= rst ? '0
            : (rmem_state_reg == RM_SEND ? 1'b1 : fragment_reg[command_slot_reg].last);
        initiator_if.cpl_ready <= rst ? '0 : (!rst);
        initiator_if.non_oetp_rx_claim_valid <= 1'b0;
        irq_event_if[0].admit_valid <= rst ?
            '0 : ((peer_state_reg == PEER_ADMIT) && !(peer_irq_admit_fire));
        irq_event_if[0].admit_source <= rst ? '0 : EVENT_PEER_DMA_COMPLETE;
        irq_event_if[0].admit_enable <= rst ? '0 : peer_irq_enable_reg;
        irq_event_if[0].commit_valid <= rst ?
            '0 : ((peer_commit_valid_reg) && !(peer_irq_commit_fire));
        irq_event_if[0].commit_source <= rst ? '0 : EVENT_PEER_DMA_COMPLETE;
        irq_event_if[0].commit_peer_idx <= rst ? '0 : (DMA_IRQ_PEER_W'(peer_commit_index_reg));
        peer_request_hwclr_reg <= '0;
        for (int unsigned n = 0; n < NUM_OF_PEERS; n++) begin
            if (endpoint_if.csr_to_core.peers.entry[n].dma.clear_error.value
                && !peer_csr_clear_error_hwclr_reg[n]) begin
                peer_error_reg[n] <= 1'b0;
                peer_error_code_reg[n] <= DMA_ERROR_NONE;
            end
        end
        case (peer_state_reg)
            PEER_IDLE:
                if (peer_request_found) begin
                    peer_index_reg <= peer_request_index;
                    peer_state_reg <= PEER_LOOKUP_REQ;
                end
            PEER_LOOKUP_REQ:
                if (!rmem_lookup_owner && lookup_req_fire) peer_state_reg <= PEER_LOOKUP_RSP;
            PEER_LOOKUP_RSP:
                if (!rmem_lookup_owner && lookup_rsp_fire) begin
                    peer_mode_reg <= peer_lookup_if.rsp_hit ? peer_lookup_if.rsp_dma_mode : 2'd0;
                    peer_irq_enable_reg <= peer_lookup_if.rsp_irq_enable;
                    peer_local_addr_reg <= peer_lookup_if.rsp_local_addr;
                    peer_remote_addr_reg <= peer_lookup_if.rsp_remote_addr;
                    peer_size_reg <= peer_lookup_if.rsp_size;
                    peer_state_reg <= PEER_ADMIT;
                end
            PEER_ADMIT:
                if (peer_irq_admit_fire) begin
                    logic config_valid;

                    config_valid = (peer_mode_reg == DMA_MODE_MIRROR_TO_LOCAL
                            || peer_mode_reg == DMA_MODE_MIRROR_TO_REMOTE) && peer_size_reg != 0
                        && effective_fragment_size >= 4
                        && effective_fragment_size <= 32'(MAX_DMA_FRAGMENT_SIZE_BYTES)
                        && peer_local_addr_reg + ADDR_W'(peer_size_reg - 1'b1)
                        >= peer_local_addr_reg
                        && peer_remote_addr_reg + ADDR_W'(peer_size_reg - 1'b1)
                        >= peer_remote_addr_reg;
                    peer_context_reg[peer_index_reg].mode <= peer_mode_reg;
                    peer_context_reg[peer_index_reg].local_addr <= peer_local_addr_reg;
                    peer_context_reg[peer_index_reg].remote_addr <= peer_remote_addr_reg;
                    peer_context_reg[peer_index_reg].size <= peer_size_reg;
                    peer_context_reg[peer_index_reg].max_fragment_size <=
                        LEN_W'(effective_fragment_size);
                    peer_context_reg[peer_index_reg].issued <= '0;
                    peer_context_reg[peer_index_reg].next_sequence <= '0;
                    peer_context_reg[peer_index_reg].error_code <= DMA_ERROR_NONE;
                    peer_context_reg[peer_index_reg].irq_reserved <= irq_event_if[0].admit_reserved;
                    peer_request_hwclr_reg[peer_index_reg] <= 1'b1;
                    peer_idle_reg[peer_index_reg] <= !config_valid;
                    peer_done_reg[peer_index_reg] <= 1'b0;
                    if (!config_valid) begin
                        peer_error_reg[peer_index_reg] <= 1'b1;
                        peer_error_code_reg[peer_index_reg] <= DMA_ERROR_INVALID;
                    end
                    peer_active_reg[peer_index_reg] <= config_valid;
                    if (!config_valid)
                        peer_commit_pending_reg[peer_index_reg] <= irq_event_if[0].admit_reserved;
                    peer_rr_reg <= peer_index_reg == PEER_IDX_W'(NUM_OF_PEERS - 1) ? PEER_IDX_W'(0)
                        : peer_index_reg + 1'b1;
                    peer_state_reg <= PEER_IDLE;
                end
            default: peer_state_reg <= PEER_IDLE;
        endcase

        if (free_slot_found && issue_peer_found) begin
            logic [LEN_W-1:0] len;

            len = fragment_length(peer_context_reg[issue_peer].size
                    - peer_context_reg[issue_peer].issued,
                    peer_context_reg[issue_peer].max_fragment_size);
            fragment_reg[free_slot] <= '{
                valid: 1'b1,
                command_sent: 1'b0,
                local_started: 1'b0,
                local_done: 1'b0,
                remote_done: 1'b0,
                op: peer_context_reg[issue_peer].mode == DMA_MODE_MIRROR_TO_REMOTE,
                peer_idx: issue_peer,
                sequence_: peer_context_reg[issue_peer].next_sequence,
                local_addr: peer_context_reg[issue_peer].local_addr
                    + ADDR_W'(peer_context_reg[issue_peer].issued),
                remote_addr: peer_context_reg[issue_peer].remote_addr
                    + ADDR_W'(peer_context_reg[issue_peer].issued),
                len: len,
                last: peer_context_reg[issue_peer].issued + len
                    == peer_context_reg[issue_peer].size,
                local_error: DMA_ERROR_NONE,
                completion_error: DMA_ERROR_NONE
            };
            peer_context_reg[issue_peer].issued <= peer_context_reg[issue_peer].issued + len;
            peer_context_reg[issue_peer].next_sequence <=
                peer_context_reg[issue_peer].next_sequence + 1'b1;
            issue_rr_reg <= issue_peer == PEER_IDX_W'(NUM_OF_PEERS - 1) ? PEER_IDX_W'(0)
                : issue_peer + 1'b1;
        end
        if (!command_valid_reg && command_slot_found
            && (!SERIAL_PEER_REQUESTS || !any_sent_fragment) && rmem_state_reg == RM_IDLE
            && !rmem_cpuif.req) begin
            command_slot_reg <= command_slot;
            command_valid_reg <= 1'b1;
        end
        if (initiator_req_fire && initiator_if.req_kind == TRANSFER_KIND_DMA) begin
            fragment_reg[command_slot_reg].command_sent <= 1'b1;
            command_valid_reg <= 1'b0;
        end
        if (memory_read_accept_pulse_reg && memory_read_accept_client_reg == RD_CLIENT_PEER)
            fragment_reg[memory_read_slot_reg].local_started <= 1'b1;
        if (memory_write_accept_pulse_reg && memory_write_accept_client_reg == WR_CLIENT_PEER)
            fragment_reg[memory_write_slot_reg].local_started <= 1'b1;
        if (memory_read_done_pulse_reg && memory_read_done_client_reg == RD_CLIENT_PEER) begin
            fragment_reg[memory_read_slot_reg].local_done <= 1'b1;
            fragment_reg[memory_read_slot_reg].local_error <= memory_read_done_error_reg;
        end
        if (memory_write_done_pulse_reg && memory_write_done_client_reg == WR_CLIENT_PEER) begin
            fragment_reg[memory_write_slot_reg].local_done <= 1'b1;
            fragment_reg[memory_write_slot_reg].local_error <= memory_write_done_error_reg;
        end
        if (initiator_cpl_fire && initiator_if.cpl_kind == TRANSFER_KIND_DMA
            && cpl_slot_found) begin
            fragment_reg[cpl_slot].remote_done <= 1'b1;
            if (initiator_if.cpl_op != fragment_reg[cpl_slot].op
                || initiator_if.cpl_last != fragment_reg[cpl_slot].last
                || (!initiator_if.cpl_error
                    && initiator_if.cpl_transferred_len != fragment_reg[cpl_slot].len))
                fragment_reg[cpl_slot].completion_error <= DMA_ERROR_AXIS;
            else
                // The protocol completion already distinguishes local and remote causes.
                fragment_reg[cpl_slot].completion_error <= initiator_if.cpl_error ?
                    initiator_if.cpl_error_code : DMA_ERROR_NONE;
            // A rejected command has no payload. Do not issue a local descriptor for it; an already
            // running local transfer still drains to TLAST.
            if (initiator_if.cpl_error && initiator_if.cpl_transferred_len == 0
                && !fragment_reg[cpl_slot].local_started
                && !(memory_read_accept_pulse_reg && memory_read_accept_client_reg == RD_CLIENT_PEER
                    && memory_read_slot_reg == cpl_slot)
                && !(memory_write_accept_pulse_reg
                    && memory_write_accept_client_reg == WR_CLIENT_PEER
                    && memory_write_slot_reg == cpl_slot))
                fragment_reg[cpl_slot].local_done <= 1'b1;
        end
        for (int unsigned n = 0; n < FRAGMENT_SLOTS; n++) begin
            if (fragment_reg[n].valid && !fragment_reg[n].command_sent
                && peer_context_reg[fragment_reg[n].peer_idx].error_code != DMA_ERROR_NONE)
                fragment_reg[n].valid <= 1'b0;
        end
        if (retire_slot_found) begin
            if (peer_context_reg[fragment_reg[retire_slot].peer_idx].error_code
                == DMA_ERROR_NONE) begin
                peer_context_reg[fragment_reg[retire_slot].peer_idx].error_code <=
                    // A shortened RX AXIS is a consequence of the same remote frame failure when
                    // oETP has classified that failure as 10.
                    fragment_reg[retire_slot].local_error == DMA_ERROR_AXIS
                        && fragment_reg[retire_slot].completion_error
                        == initiator_if.ERROR_REMOTE_AXIS ? initiator_if.ERROR_REMOTE_AXIS
                        : fragment_reg[retire_slot].local_error != DMA_ERROR_NONE
                        ? fragment_reg[retire_slot].local_error
                        : fragment_reg[retire_slot].completion_error;
            end
            fragment_reg[retire_slot].valid <= 1'b0;
        end
        for (int unsigned n = 0; n < NUM_OF_PEERS; n++) begin
            if (peer_active_reg[n] && !peer_has_fragment[n]
                && (peer_context_reg[n].issued == peer_context_reg[n].size
                    || peer_context_reg[n].error_code != DMA_ERROR_NONE)) begin
                peer_active_reg[n] <= 1'b0;
                peer_idle_reg[n] <= 1'b1;
                peer_done_reg[n] <= peer_context_reg[n].error_code == DMA_ERROR_NONE;
                if (peer_context_reg[n].error_code != DMA_ERROR_NONE) begin
                    peer_error_reg[n] <= 1'b1;
                    peer_error_code_reg[n] <= peer_context_reg[n].error_code;
                end
                peer_commit_pending_reg[n] <= peer_context_reg[n].irq_reserved;
            end
        end
        if (!peer_commit_valid_reg && commit_peer_found) begin
            peer_commit_valid_reg <= 1'b1;
            peer_commit_index_reg <= commit_peer;
            peer_commit_pending_reg[commit_peer] <= 1'b0;
        end
        if (peer_irq_commit_fire) peer_commit_valid_reg <= 1'b0;

        // New failures win over clear_error. IRQ production stays with its owner.
        if (rmem_error_valid && int'(rmem_error_peer_idx) < NUM_OF_PEERS
            && rmem_error_code != 0) begin
            peer_error_reg[rmem_error_peer_idx] <= 1'b1;
            peer_error_code_reg[rmem_error_peer_idx] <= ERROR_W'(rmem_error_code);
        end

        // Received requests use the peer resolved from the source MAC. They update shared
        // diagnostics without completing a locally issued block.
        if (responder_error_valid && int'(responder_peer_idx_reg) < NUM_OF_PEERS) begin
            peer_error_reg[responder_peer_idx_reg] <= 1'b1;
            // The shortened incoming frame is a remote stream failure for this receiver. The
            // completion still supplies wire cause 2.
            peer_error_code_reg[responder_peer_idx_reg] <= responder_kind_reg == TRANSFER_KIND_DMA
                && responder_op_reg == DMA_OP_WRITE
                && responder_cpl_error_code_reg == DMA_ERROR_AXIS ? initiator_if.ERROR_REMOTE_AXIS
                : responder_cpl_error_code_reg;
        end

        if (rst) begin
            peer_index_reg <= '0;
            peer_mode_reg <= '0;
            peer_irq_enable_reg <= 1'b0;
            peer_local_addr_reg <= '0;
            peer_remote_addr_reg <= '0;
            peer_size_reg <= '0;
            peer_state_reg <= PEER_IDLE;
            peer_idle_reg <= '1;
            peer_done_reg <= '0;
            peer_error_reg <= '0;
            peer_request_hwclr_reg <= '0;
            peer_active_reg <= '0;
            peer_commit_pending_reg <= '0;
            peer_commit_valid_reg <= 1'b0;
            peer_commit_index_reg <= '0;
            command_valid_reg <= 1'b0;
            command_slot_reg <= '0;
            peer_rr_reg <= '0;
            issue_rr_reg <= '0;
            for (int unsigned n = 0; n < NUM_OF_PEERS; n++) begin
                peer_context_reg[n] <= '0;
                peer_error_code_reg[n] <= DMA_ERROR_NONE;
            end
            for (int unsigned n = 0; n < FRAGMENT_SLOTS; n++) fragment_reg[n] <= '0;
        end

    end

    always_ff @(posedge clk) begin : raw_transmit_control
        irq_event_if[1].admit_valid <= rst ?
            '0 : ((raw_tx_state_reg == NON_TX_ADMIT) && !(raw_tx_irq_admit_fire));
        irq_event_if[1].admit_source <= rst ? '0 : (EVENT_NON_OETP_DMA_TX_COMPLETE);
        irq_event_if[1].admit_enable <= rst ? '0 : 1'b1;
        irq_event_if[1].commit_valid <= rst ?
            '0 : ((raw_tx_state_reg == NON_TX_COMMIT && raw_tx_irq_reserved_reg) &&
                !(raw_tx_irq_commit_fire));
        irq_event_if[1].commit_source <= rst ? '0 : (EVENT_NON_OETP_DMA_TX_COMPLETE);
        irq_event_if[1].commit_peer_idx <= '0;
        raw_tx_request_hwclr_reg <= 1'b0;

        // A later failure assignment wins over a simultaneous clear command.
        if (endpoint_if.csr_to_core.non_oetp_dma.tx.command_status.clear_errors.value
            && !csr_raw_tx_clear_errors_hwclr_reg) begin
            raw_tx_error_reg <= 1'b0;
            raw_tx_error_code_reg <= DMA_ERROR_NONE;
        end

        case (raw_tx_state_reg)
            NON_TX_IDLE: begin
                if (endpoint_if.csr_to_core.non_oetp_dma.tx.command_status.request.value) begin
                    raw_tx_state_reg <= NON_TX_ADMIT;
                end
            end
            NON_TX_ADMIT: begin
                if (raw_tx_irq_admit_fire) begin
                    raw_tx_addr_reg
                        <= endpoint_if.csr_to_core.non_oetp_dma.tx.buffer_address.base.value;
                    raw_tx_len_reg
                        <= endpoint_if.csr_to_core.non_oetp_dma.tx.frame_length.bytes.value;
                    raw_tx_irq_reserved_reg <= irq_event_if[1].admit_reserved;
                    raw_tx_request_hwclr_reg <= 1'b1;
                    raw_tx_idle_reg <= 1'b0;
                    raw_tx_done_reg <= 1'b0;
                    raw_tx_transferred_len_reg <= '0;

                    if (endpoint_if.csr_to_core.non_oetp_dma.tx.frame_length.bytes.value == 0
                        || endpoint_if.csr_to_core.non_oetp_dma.tx.frame_length.bytes.value >
                        MAX_RAW_FRAME_SIZE) begin
                        raw_tx_idle_reg <= 1'b1;
                        raw_tx_error_reg <= 1'b1;
                        raw_tx_error_code_reg <= DMA_ERROR_INVALID;
                        raw_tx_state_reg <= NON_TX_COMMIT;
                        irq_event_if[1].commit_valid <= raw_tx_state_reg == NON_TX_ADMIT ?
                            irq_event_if[1].admit_reserved : raw_tx_irq_reserved_reg;
                    end else begin
                        raw_tx_state_reg <= NON_TX_QUEUE;
                    end
                end
            end
            NON_TX_QUEUE: begin
                if (memory_read_accept_pulse_reg
                    && memory_read_accept_client_reg == RD_CLIENT_NON_OETP) begin
                    raw_tx_state_reg <= NON_TX_WAIT;
                end
            end
            NON_TX_WAIT: begin
                if (memory_read_done_pulse_reg
                    && memory_read_done_client_reg == RD_CLIENT_NON_OETP) begin
                    raw_tx_idle_reg <= 1'b1;
                    raw_tx_transferred_len_reg <= memory_read_done_len_reg;
                    if (memory_read_done_error_reg == DMA_ERROR_NONE
                        && memory_read_done_len_reg == raw_tx_len_reg) begin
                        raw_tx_done_reg <= 1'b1;
                    end else begin
                        raw_tx_error_reg <= 1'b1;
                        if (memory_read_done_error_reg != DMA_ERROR_NONE) begin
                            raw_tx_error_code_reg <= memory_read_done_error_reg;
                        end else begin
                            raw_tx_error_code_reg <= DMA_ERROR_AXIS;
                        end
                    end
                    raw_tx_state_reg <= NON_TX_COMMIT;
                    irq_event_if[1].commit_valid <= raw_tx_state_reg == NON_TX_ADMIT ?
                        irq_event_if[1].admit_reserved : raw_tx_irq_reserved_reg;
                end
            end
            NON_TX_COMMIT: begin
                if (!raw_tx_irq_reserved_reg || (raw_tx_irq_commit_fire)) begin
                    raw_tx_irq_reserved_reg <= 1'b0;
                    raw_tx_state_reg <= NON_TX_IDLE;
                end
            end
            default: raw_tx_state_reg <= NON_TX_IDLE;
        endcase

        if (rst) begin
            raw_tx_addr_reg <= '0;
            raw_tx_len_reg <= '0;
            raw_tx_state_reg <= NON_TX_IDLE;
            raw_tx_idle_reg <= 1'b1;
            raw_tx_done_reg <= 1'b0;
            raw_tx_error_reg <= 1'b0;
            raw_tx_error_code_reg <= DMA_ERROR_NONE;
            raw_tx_transferred_len_reg <= '0;
            raw_tx_request_hwclr_reg <= 1'b0;
            raw_tx_irq_reserved_reg <= 1'b0;
        end

    end

    always_ff @(posedge clk) begin : raw_receive_control
        responder_if.non_oetp_rx_available <= rst ? '0 : (!rst && raw_rx_state_reg == NON_RX_ARMED
                && !(responder_non_oetp_rx_claim_fire));
        responder_if.non_oetp_rx_claim_ready <= rst ? '0 : ((!rst
                    && raw_rx_state_reg == NON_RX_ARMED) && !(responder_non_oetp_rx_claim_fire));
        irq_event_if[2].admit_valid <= rst ?
            '0 : ((raw_rx_state_reg == NON_RX_ADMIT) && !(raw_rx_irq_admit_fire));
        irq_event_if[2].admit_source <= rst ? '0 : (EVENT_NON_OETP_DMA_RX_COMPLETE);
        irq_event_if[2].admit_enable <= rst ? '0 : 1'b1;
        irq_event_if[2].commit_valid <= rst ?
            '0 : ((raw_rx_state_reg == NON_RX_COMMIT && raw_rx_irq_reserved_reg) &&
                !(raw_rx_irq_commit_fire));
        irq_event_if[2].commit_source <= rst ? '0 : (EVENT_NON_OETP_DMA_RX_COMPLETE);
        irq_event_if[2].commit_peer_idx <= '0;
        raw_rx_request_hwclr_reg <= 1'b0;

        // Clearing errors leaves the receive descriptor and IRQ reservation intact.
        if (endpoint_if.csr_to_core.non_oetp_dma.rx.command_status.clear_errors.value
            && !csr_raw_rx_clear_errors_hwclr_reg) begin
            raw_rx_error_reg <= 1'b0;
            raw_rx_error_code_reg <= DMA_ERROR_NONE;
        end

        case (raw_rx_state_reg)
            NON_RX_IDLE: begin
                if (endpoint_if.csr_to_core.non_oetp_dma.rx.command_status.request.value) begin
                    raw_rx_state_reg <= NON_RX_ADMIT;
                end
            end
            NON_RX_ADMIT: begin
                if (raw_rx_irq_admit_fire) begin
                    raw_rx_addr_reg
                        <= endpoint_if.csr_to_core.non_oetp_dma.rx.buffer_address.base.value;
                    raw_rx_capacity_reg
                        <= endpoint_if.csr_to_core.non_oetp_dma.rx.buffer_capacity.bytes.value;
                    raw_rx_irq_reserved_reg <= irq_event_if[2].admit_reserved;
                    raw_rx_request_hwclr_reg <= 1'b1;
                    raw_rx_idle_reg <= 1'b0;
                    raw_rx_armed_reg <= 1'b1;
                    raw_rx_done_reg <= 1'b0;
                    raw_rx_received_len_reg <= '0;

                    if (endpoint_if.csr_to_core.non_oetp_dma.rx.buffer_capacity.bytes.value == 0
                        || endpoint_if.csr_to_core.non_oetp_dma.rx.buffer_capacity.bytes.value >
                        MAX_RAW_FRAME_SIZE) begin
                        raw_rx_idle_reg <= 1'b1;
                        raw_rx_armed_reg <= 1'b0;
                        raw_rx_error_reg <= 1'b1;
                        raw_rx_error_code_reg <= DMA_ERROR_INVALID;
                        raw_rx_state_reg <= NON_RX_COMMIT;
                        irq_event_if[2].commit_valid <= raw_rx_state_reg == NON_RX_ADMIT ?
                            irq_event_if[2].admit_reserved : raw_rx_irq_reserved_reg;
                    end else begin
                        raw_rx_state_reg <= NON_RX_ARMED;
                    end
                end
            end
            NON_RX_ARMED: begin
                if (responder_non_oetp_rx_claim_fire) begin
                    raw_rx_armed_reg <= 1'b0;
                    raw_rx_state_reg <= NON_RX_QUEUE;
                end
            end
            NON_RX_QUEUE: begin
                if (memory_write_accept_pulse_reg
                    && memory_write_accept_client_reg == WR_CLIENT_NON_OETP) begin
                    raw_rx_state_reg <= NON_RX_WAIT;
                end
            end
            NON_RX_WAIT: begin
                if ((memory_write_first_pulse_reg
                        && memory_write_first_client_reg == WR_CLIENT_NON_OETP)
                    || (memory_write_state_reg == WR_STREAM
                        && memory_write_client_reg == WR_CLIENT_NON_OETP && memory_write_src_tvalid
                        && memory_write_src_tready && memory_write_input_len_reg == 0)) begin
                    raw_rx_armed_reg <= 1'b0;
                end
                if (memory_write_done_pulse_reg
                    && memory_write_done_client_reg == WR_CLIENT_NON_OETP) begin
                    raw_rx_idle_reg <= 1'b1;
                    raw_rx_armed_reg <= 1'b0;
                    raw_rx_received_len_reg <= memory_write_done_len_reg;
                    if (memory_write_done_error_reg == DMA_ERROR_NONE) begin
                        raw_rx_done_reg <= 1'b1;
                    end else begin
                        raw_rx_error_reg <= 1'b1;
                        raw_rx_error_code_reg <= memory_write_done_error_reg;
                    end
                    raw_rx_state_reg <= NON_RX_COMMIT;
                    irq_event_if[2].commit_valid <= raw_rx_state_reg == NON_RX_ADMIT ?
                        irq_event_if[2].admit_reserved : raw_rx_irq_reserved_reg;
                end
            end
            NON_RX_COMMIT: begin
                if (!raw_rx_irq_reserved_reg || (raw_rx_irq_commit_fire)) begin
                    raw_rx_irq_reserved_reg <= 1'b0;
                    raw_rx_state_reg <= NON_RX_IDLE;
                end
            end
            default: raw_rx_state_reg <= NON_RX_IDLE;
        endcase

        if (rst) begin
            raw_rx_addr_reg <= '0;
            raw_rx_capacity_reg <= '0;
            raw_rx_state_reg <= NON_RX_IDLE;
            raw_rx_idle_reg <= 1'b1;
            raw_rx_armed_reg <= 1'b0;
            raw_rx_done_reg <= 1'b0;
            raw_rx_error_reg <= 1'b0;
            raw_rx_error_code_reg <= DMA_ERROR_NONE;
            raw_rx_received_len_reg <= '0;
            raw_rx_request_hwclr_reg <= 1'b0;
            raw_rx_irq_reserved_reg <= 1'b0;
        end

    end

    always_ff @(posedge clk) begin : responder_control
        m_local_cpuif.req <= rst ? '0 : (!rst && responder_state_reg == RESP_RMEM_REQ);
        m_local_cpuif.addr <= rst ? '0 : responder_addr_reg;
        m_local_cpuif.req_is_wr <= rst ? '0 : responder_op_reg;
        m_local_cpuif.wr_data <= rst ? '0 : responder_wdata_reg;
        m_local_cpuif.wr_biten <= rst ? '0 : responder_biten_reg;
        responder_if.tx_status_ready <= 1'b0;
        responder_if.rx_status_ready <= rst ? '0 : ((responder_rx_required_reg
                    && !responder_rx_done_reg && responder_state_reg != RESP_IDLE)
                && !(responder_rx_status_fire));
        responder_if.req_ready <= rst ? '0 : ((!rst && responder_state_reg == RESP_IDLE
                    && responder_irq_state_reg == RESP_IRQ_IDLE) && !(responder_req_fire));
        responder_if.cpl_valid <= rst ? '0 : ((responder_state_reg == RESP_COMPLETE
                    && (!responder_cpl_error_reg || responder_error_recorded_reg))
                && !(responder_cpl_fire));
        responder_if.cpl_kind <= rst ? '0 : responder_kind_reg;
        responder_if.cpl_rdata <= rst ? '0 : responder_rdata_reg;
        responder_if.cpl_op <= rst ? '0 : responder_op_reg;
        responder_if.cpl_transferred_len <= rst ? '0 : responder_cpl_len_reg;
        responder_if.cpl_peer_idx <= rst ? '0 : responder_peer_idx_reg;
        responder_if.cpl_sequence <= rst ? '0 : responder_sequence_reg;
        responder_if.cpl_last <= rst ? '0 : responder_last_reg;
        responder_if.cpl_error <= rst ? '0 : responder_cpl_error_reg;
        responder_if.cpl_error_code <= rst ? '0 : (responder_cpl_error_code_reg);
        if (responder_error_valid) responder_error_recorded_reg <= 1'b1;
        if (responder_rx_status_fire) begin
            responder_rx_done_reg <= 1'b1;
            responder_rx_len_reg <= responder_if.rx_status_len;
            responder_rx_error_reg <= responder_if.rx_status_error_code;
            if (responder_if.rx_status_peer_idx != responder_peer_idx_reg
                || responder_if.rx_status_sequence != responder_sequence_reg)
                responder_rx_error_reg <= DMA_ERROR_AXIS;
            if (responder_if.rx_status_len == 0 && responder_if.rx_status_error_code != 0) begin
                responder_memory_done_reg <= 1'b1;
                responder_payload_done_reg <= 1'b1;
                responder_cpl_len_reg <= '0;
                responder_cpl_error_reg <= 1'b1;
                responder_cpl_error_code_reg <= responder_if.rx_status_error_code;
                if (responder_state_reg == RESP_WR_QUEUE) responder_state_reg <= RESP_WAIT;
            end
        end
        if (responder_drop_payload && memory_input.tready && memory_input.tlast)
            responder_payload_done_reg <= 1'b1;
        if (responder_state_reg == RESP_WAIT && responder_memory_done_reg
            && (!responder_rx_required_reg
                || (responder_rx_done_reg
                    && (responder_rx_len_reg == 0 || responder_payload_done_reg)))) begin
            if (responder_rx_error_reg != 0
                && !(responder_cpl_error_code_reg >= 4 && responder_cpl_error_code_reg <= 7)) begin
                responder_cpl_error_reg <= 1'b1;
                responder_cpl_error_code_reg <= responder_rx_error_reg;
            end
            responder_state_reg <= RESP_COMPLETE;
        end

        case (responder_state_reg)
            RESP_IDLE: begin
                if (responder_req_fire) begin
                    responder_kind_reg <= responder_if.req_kind;
                    responder_op_reg <= responder_if.req_op;
                    responder_addr_reg <= responder_if.req_addr;
                    responder_len_reg <= responder_if.req_len;
                    responder_peer_idx_reg <= responder_if.req_peer_idx;
                    responder_sequence_reg <= responder_if.req_sequence;
                    responder_last_reg <= responder_if.req_last;
                    responder_biten_reg <= responder_if.req_biten;
                    responder_wdata_reg <= responder_if.req_wdata;
                    responder_rdata_reg <= '0;
                    responder_cpl_len_reg <= '0;
                    responder_cpl_error_reg <= 1'b0;
                    responder_cpl_error_code_reg <= DMA_ERROR_NONE;
                    responder_error_recorded_reg <= 1'b0;
                    responder_rx_required_reg <= responder_if.req_rx_status;
                    responder_rx_done_reg <= !responder_if.req_rx_status;
                    responder_memory_done_reg <= 1'b0;
                    responder_payload_done_reg <= 1'b0;
                    responder_rx_error_reg <= '0;
                    responder_rx_len_reg <= '0;

                    if (responder_if.req_error_code != 0
                        || !responder_window_valid(responder_if.req_peer_idx, responder_if.req_kind,
                            responder_if.req_op, responder_if.req_addr, responder_if.req_len)
                        || responder_if.req_len == 0
                        || responder_if.req_len > LEN_W'(MAX_DMA_FRAGMENT_SIZE_BYTES)
                        || responder_if.req_addr
                        + ADDR_W'(responder_if.req_len - 1'b1) < responder_if.req_addr) begin
                        responder_cpl_error_reg <= 1'b1;
                        responder_cpl_error_code_reg <= responder_if.req_error_code != 0
                            ? responder_if.req_error_code : DMA_ERROR_INVALID;
                        responder_memory_done_reg <= 1'b1;
                        responder_state_reg <= responder_if.req_rx_status ? RESP_WAIT
                            : RESP_COMPLETE;
                    end else if (responder_if.req_kind == TRANSFER_KIND_RMEM) begin
                        if (responder_if.req_op == DMA_OP_WRITE
                            && responder_if.req_biten == 0) begin
                            responder_cpl_len_reg <= LEN_W'(4);
                            responder_state_reg <= RESP_COMPLETE;
                        end else responder_state_reg <= RESP_RMEM_REQ;
                    end else if (responder_if.req_op == DMA_OP_READ) begin
                        responder_state_reg <= RESP_RD_QUEUE;
                    end else begin
                        responder_state_reg <= RESP_WR_QUEUE;
                    end
                end
            end
            RESP_RD_QUEUE: begin
                if (memory_read_accept_pulse_reg
                    && memory_read_accept_client_reg == RD_CLIENT_RESPONDER) begin
                    responder_state_reg <= RESP_WAIT;
                end
            end
            RESP_WR_QUEUE: begin
                if (memory_write_accept_pulse_reg
                    && memory_write_accept_client_reg == WR_CLIENT_RESPONDER) begin
                    responder_state_reg <= RESP_WAIT;
                end
            end
            RESP_WAIT: begin
                if (memory_read_done_pulse_reg
                    && memory_read_done_client_reg == RD_CLIENT_RESPONDER) begin
                    responder_cpl_len_reg <= memory_read_done_len_reg;
                    responder_cpl_error_reg <= memory_read_done_error_reg != DMA_ERROR_NONE
                        || memory_read_done_len_reg != responder_len_reg;
                    responder_cpl_error_code_reg <= memory_read_done_error_reg != DMA_ERROR_NONE
                        ? memory_read_done_error_reg
                        : (memory_read_done_len_reg != responder_len_reg ? DMA_ERROR_AXIS
                            : DMA_ERROR_NONE);
                    responder_memory_done_reg <= 1'b1;
                    responder_payload_done_reg <= 1'b1;
                end
                if (memory_write_done_pulse_reg
                    && memory_write_done_client_reg == WR_CLIENT_RESPONDER) begin
                    responder_cpl_len_reg <= memory_write_done_len_reg;
                    responder_cpl_error_reg <= memory_write_done_error_reg != DMA_ERROR_NONE;
                    responder_cpl_error_code_reg <= memory_write_done_error_reg;
                    responder_memory_done_reg <= 1'b1;
                    responder_payload_done_reg <= 1'b1;
                end
            end
            RESP_RMEM_REQ: begin
                if ((responder_op_reg && m_local_cpuif.wr_ack)
                    || (!responder_op_reg && m_local_cpuif.rd_ack)) begin
                    responder_cpl_len_reg <= LEN_W'(4);
                    responder_rdata_reg <= m_local_cpuif.rd_data;
                    responder_cpl_error_reg <= responder_op_reg ? m_local_cpuif.wr_err
                        : m_local_cpuif.rd_err;
                    responder_cpl_error_code_reg <= responder_op_reg
                        ? (m_local_cpuif.wr_err ? ERROR_W'(6) : DMA_ERROR_NONE)
                        : (m_local_cpuif.rd_err ? ERROR_W'(4) : DMA_ERROR_NONE);
                    responder_state_reg <= RESP_COMPLETE;
                end else responder_state_reg <= RESP_RMEM_WAIT;
            end
            RESP_RMEM_WAIT: begin
                if ((responder_op_reg && m_local_cpuif.wr_ack)
                    || (!responder_op_reg && m_local_cpuif.rd_ack)) begin
                    responder_cpl_len_reg <= LEN_W'(4);
                    responder_rdata_reg <= m_local_cpuif.rd_data;
                    responder_cpl_error_reg <= responder_op_reg ? m_local_cpuif.wr_err
                        : m_local_cpuif.rd_err;
                    responder_cpl_error_code_reg <= responder_op_reg
                        ? (m_local_cpuif.wr_err ? ERROR_W'(6) : DMA_ERROR_NONE)
                        : (m_local_cpuif.rd_err ? ERROR_W'(4) : DMA_ERROR_NONE);
                    responder_state_reg <= RESP_COMPLETE;
                end
            end
            RESP_COMPLETE: begin
                if (responder_cpl_fire) begin
                    responder_state_reg <= RESP_IDLE;
                end
            end
            default: responder_state_reg <= RESP_IDLE;
        endcase

        if (rst) begin
            responder_biten_reg <= '0;
            responder_wdata_reg <= '0;
            responder_rdata_reg <= '0;
            responder_op_reg <= DMA_OP_READ;
            responder_addr_reg <= '0;
            responder_len_reg <= '0;
            responder_peer_idx_reg <= '0;
            responder_sequence_reg <= '0;
            responder_last_reg <= 1'b0;
            responder_cpl_len_reg <= '0;
            responder_state_reg <= RESP_IDLE;
            responder_error_recorded_reg <= 1'b0;
            responder_rx_required_reg <= 1'b0;
            responder_rx_done_reg <= 1'b0;
            responder_memory_done_reg <= 1'b0;
            responder_payload_done_reg <= 1'b0;
            responder_rx_error_reg <= '0;
            responder_rx_len_reg <= '0;
            responder_kind_reg <= TRANSFER_KIND_DMA;
            responder_cpl_error_reg <= 1'b0;
            responder_cpl_error_code_reg <= DMA_ERROR_NONE;
        end

    end

    always_ff @(posedge clk) begin : memory_read_control
        memory_read_desc_if.req_src_addr <= rst ? '0 : memory_read_addr_reg;
        memory_read_desc_if.req_src_sel <= '0;
        memory_read_desc_if.req_src_asid <= '0;
        memory_read_desc_if.req_dst_addr <= '0;
        memory_read_desc_if.req_dst_sel <= '0;
        memory_read_desc_if.req_dst_asid <= '0;
        memory_read_desc_if.req_imm <= '0;
        memory_read_desc_if.req_imm_en <= 1'b0;
        memory_read_desc_if.req_len <= rst ? '0 : memory_read_len_reg;
        memory_read_desc_if.req_tag <= rst ? '0 : memory_read_client_reg;
        memory_read_desc_if.req_id <= rst ? '0 : memory_read_sequence_reg;
        memory_read_desc_if.req_dest <= rst ?
            '0 : ({memory_read_client_reg == RD_CLIENT_NON_OETP ? ROUTE_NON_OETP_DMA : ROUTE_PEER,
                memory_read_peer_idx_reg});
        memory_read_desc_if.req_user <= '0;
        memory_read_desc_if.req_user[AXIS_USER_LAST_BIT] <= rst ? '0 : (memory_read_last_reg);
        memory_read_desc_if.req_user[AXIS_USER_ROLE_BIT] <= rst ? '0
            : (memory_read_client_reg == RD_CLIENT_RESPONDER ? TRANSFER_ROLE_RESPONDER
                : TRANSFER_ROLE_INITIATOR);
        memory_read_desc_if.req_valid <= rst ? '0 : ((memory_read_state_reg == RD_DESC)
                && !(memory_read_descriptor_req_fire));
        memory_read_accept_pulse_reg <= 1'b0;
        memory_read_done_pulse_reg <= 1'b0;

        case (memory_read_state_reg)
            RD_IDLE: begin
                if (memory_read_pick_valid) begin
                    memory_read_client_reg <= memory_read_pick;
                    memory_read_accept_client_reg <= memory_read_pick;
                    memory_read_accept_pulse_reg <= 1'b1;
                    memory_read_byte_count_reg <= '0;
                    memory_read_saw_last_reg <= 1'b0;
                    memory_read_status_seen_reg <= 1'b0;
                    memory_read_status_error_reg <= DMA_ERROR_NONE;
                    memory_read_remaining_reg <= '0;
                    memory_read_prior_error_reg <= DMA_ERROR_NONE;

                    case (memory_read_pick)
                        RD_CLIENT_PEER: begin
                            memory_read_slot_reg <= memory_read_slot;
                            memory_read_addr_reg <= fragment_reg[memory_read_slot].local_addr;
                            memory_read_len_reg <= fragment_reg[memory_read_slot].len;
                            memory_read_peer_idx_reg <= fragment_reg[memory_read_slot].peer_idx;
                            memory_read_sequence_reg <= fragment_reg[memory_read_slot].sequence_;
                            memory_read_last_reg <= fragment_reg[memory_read_slot].last;
                        end
                        RD_CLIENT_RESPONDER: begin
                            memory_read_addr_reg <= responder_addr_reg;
                            memory_read_len_reg <= responder_len_reg;
                            memory_read_peer_idx_reg <= responder_peer_idx_reg;
                            memory_read_sequence_reg <= responder_sequence_reg;
                            memory_read_last_reg <= responder_last_reg;
                        end
                        default: begin
                            memory_read_addr_reg <= raw_tx_addr_reg;
                            memory_read_len_reg <= raw_tx_len_reg;
                            // TAXI's 13-bit byte/cycle budget includes the first unaligned word.
                            // Read a full-size raw frame in two word-sized chunks; suppress only
                            // the internal TLAST. Peer fragments are already below this boundary.
                            if (UNALIGNED_EN && (raw_tx_addr_reg & ADDR_W'(AXIS_KEEP_W - 1)) != 0
                                && raw_tx_len_reg > LEN_W'(8192 - AXIS_KEEP_W)) begin
                                memory_read_len_reg <= LEN_W'(8192 - AXIS_KEEP_W);
                                memory_read_remaining_reg <= raw_tx_len_reg
                                    - LEN_W'(8192 - AXIS_KEEP_W);
                            end
                            memory_read_peer_idx_reg <= '0;
                            memory_read_sequence_reg <= '0;
                            memory_read_last_reg <= 1'b1;
                        end
                    endcase
                    memory_read_state_reg <= RD_DESC;
                end
            end
            RD_DESC: begin
                if (memory_read_descriptor_req_fire) begin
                    memory_read_state_reg <= RD_STREAM;
                end
            end
            RD_STREAM: begin
                logic beat_accepted;
                logic [LEN_W-1:0] next_byte_count;
                logic last_seen_now;
                logic status_seen_now;
                logic [ERROR_W-1:0] status_error_now;

                beat_accepted = dma_rd_axis.tvalid && dma_rd_axis.tready;
                next_byte_count = memory_read_byte_count_reg + (beat_accepted
                        ? keep_count(dma_rd_axis.tkeep) : LEN_W'(0));
                last_seen_now = memory_read_saw_last_reg || (beat_accepted && dma_rd_axis.tlast);
                status_seen_now = memory_read_status_seen_reg || memory_read_desc_if.sts_valid;
                status_error_now = memory_read_desc_if.sts_valid
                    ? ERROR_W'(memory_read_desc_if.sts_error) : memory_read_status_error_reg;

                if (dma_rd_axis.tvalid && dma_rd_axis.tready) begin
                    memory_read_byte_count_reg <= next_byte_count;
                    memory_read_saw_last_reg <= last_seen_now;
                end
                if (memory_read_desc_if.sts_valid) begin
                    memory_read_status_seen_reg <= 1'b1;
                    memory_read_status_error_reg <= ERROR_W'(memory_read_desc_if.sts_error);
                end
                if (last_seen_now && status_seen_now) begin
                    if (memory_read_remaining_reg != 0) begin
                        memory_read_addr_reg <= memory_read_addr_reg + ADDR_W'(memory_read_len_reg);
                        memory_read_len_reg <= memory_read_remaining_reg;
                        memory_read_remaining_reg <= '0;
                        memory_read_prior_error_reg <= memory_read_prior_error_reg != DMA_ERROR_NONE
                            ? memory_read_prior_error_reg : status_error_now;
                        memory_read_saw_last_reg <= 1'b0;
                        memory_read_status_seen_reg <= 1'b0;
                        memory_read_status_error_reg <= DMA_ERROR_NONE;
                        memory_read_state_reg <= RD_DESC;
                    end else begin
                        memory_read_done_pulse_reg <= 1'b1;
                        memory_read_done_client_reg <= memory_read_client_reg;
                        memory_read_done_len_reg <= next_byte_count;
                        memory_read_done_error_reg <= memory_read_prior_error_reg != DMA_ERROR_NONE
                            ? memory_read_prior_error_reg : status_error_now;
                        if (memory_read_client_reg == 2'd2) begin
                            memory_read_rr_reg <= 2'd0;
                        end else begin
                            memory_read_rr_reg <= memory_read_client_reg + 1'b1;
                        end
                        memory_read_state_reg <= RD_IDLE;
                    end
                end
            end
            default: memory_read_state_reg <= RD_IDLE;
        endcase

        if (rst) begin
            memory_read_client_reg <= RD_CLIENT_PEER;
            memory_read_addr_reg <= '0;
            memory_read_len_reg <= '0;
            memory_read_remaining_reg <= '0;
            memory_read_prior_error_reg <= '0;
            memory_read_peer_idx_reg <= '0;
            memory_read_sequence_reg <= '0;
            memory_read_last_reg <= 1'b0;
            memory_read_byte_count_reg <= '0;
            memory_read_accept_client_reg <= '0;
            memory_read_done_client_reg <= '0;
            memory_read_done_len_reg <= '0;
            memory_read_done_error_reg <= '0;
            memory_read_state_reg <= RD_IDLE;
            memory_read_slot_reg <= '0;
            memory_read_rr_reg <= RD_CLIENT_PEER;
            memory_read_accept_pulse_reg <= 1'b0;
            memory_read_done_pulse_reg <= 1'b0;
            memory_read_saw_last_reg <= 1'b0;
            memory_read_status_seen_reg <= 1'b0;
            memory_read_status_error_reg <= DMA_ERROR_NONE;
        end

    end

    always_ff @(posedge clk) begin : memory_write_control
        memory_write_desc_if.req_src_addr <= '0;
        memory_write_desc_if.req_src_sel <= '0;
        memory_write_desc_if.req_src_asid <= '0;
        memory_write_desc_if.req_dst_addr <= rst ? '0 : memory_write_addr_reg;
        memory_write_desc_if.req_dst_sel <= '0;
        memory_write_desc_if.req_dst_asid <= '0;
        memory_write_desc_if.req_imm <= '0;
        memory_write_desc_if.req_imm_en <= 1'b0;
        memory_write_desc_if.req_len <= rst ? '0 : memory_write_len_reg;
        memory_write_desc_if.req_tag <= rst ? '0 : memory_write_client_reg;
        memory_write_desc_if.req_id <= rst ? '0 : memory_write_sequence_reg;
        memory_write_desc_if.req_dest <= rst ?
            '0 : ({memory_write_client_reg == WR_CLIENT_NON_OETP ? ROUTE_NON_OETP_DMA : ROUTE_PEER,
                memory_write_peer_idx_reg});
        memory_write_desc_if.req_user <= '0;
        memory_write_desc_if.req_user[AXIS_USER_LAST_BIT] <= rst ? '0 : (memory_write_last_reg);
        memory_write_desc_if.req_user[AXIS_USER_ROLE_BIT] <= rst ? '0
            : (memory_write_client_reg == WR_CLIENT_RESPONDER ? TRANSFER_ROLE_RESPONDER
                : TRANSFER_ROLE_INITIATOR);
        memory_write_desc_if.req_valid <= rst ? '0 : ((memory_write_state_reg == WR_DESC)
                && !(memory_write_descriptor_req_fire));
        memory_write_accept_pulse_reg <= 1'b0;
        memory_write_first_pulse_reg <= 1'b0;
        memory_write_done_pulse_reg <= 1'b0;

        case (memory_write_state_reg)
            WR_IDLE: begin
                if (memory_write_pick_valid) begin
                    memory_write_client_reg <= memory_write_pick;
                    memory_write_accept_client_reg <= memory_write_pick;
                    memory_write_accept_pulse_reg <= 1'b1;
                    memory_write_input_len_reg <= '0;
                    memory_write_saw_last_reg <= 1'b0;
                    memory_write_status_seen_reg <= 1'b0;
                    memory_write_status_len_reg <= '0;
                    memory_write_status_error_reg <= DMA_ERROR_NONE;
                    memory_write_stream_error_reg <= DMA_ERROR_NONE;

                    case (memory_write_pick)
                        WR_CLIENT_PEER: begin
                            memory_write_slot_reg <= memory_write_slot;
                            memory_write_addr_reg <= fragment_reg[memory_write_slot].local_addr;
                            memory_write_len_reg <= fragment_reg[memory_write_slot].len;
                            memory_write_peer_idx_reg <= fragment_reg[memory_write_slot].peer_idx;
                            memory_write_sequence_reg <= fragment_reg[memory_write_slot].sequence_;
                            memory_write_last_reg <= fragment_reg[memory_write_slot].last;
                        end
                        WR_CLIENT_RESPONDER: begin
                            memory_write_addr_reg <= responder_addr_reg;
                            memory_write_len_reg <= responder_len_reg;
                            memory_write_peer_idx_reg <= responder_peer_idx_reg;
                            memory_write_sequence_reg <= responder_sequence_reg;
                            memory_write_last_reg <= responder_last_reg;
                        end
                        default: begin
                            memory_write_addr_reg <= raw_rx_addr_reg;
                            memory_write_len_reg <= raw_rx_capacity_reg;
                            memory_write_peer_idx_reg <= '0;
                            memory_write_sequence_reg <= '0;
                            memory_write_last_reg <= 1'b1;
                        end
                    endcase
                    memory_write_state_reg <= WR_DESC;
                end
            end
            WR_DESC: begin
                if (memory_write_descriptor_req_fire) begin
                    memory_write_state_reg <= WR_STREAM;
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

                beat_accepted = memory_write_src_tvalid && memory_write_src_tready;
                beat_len = keep_count(memory_write_src_tkeep);
                next_input_len = memory_write_input_len_reg + beat_len;
                last_seen_now = memory_write_saw_last_reg
                    || (beat_accepted && memory_write_src_tlast);
                status_seen_now = memory_write_status_seen_reg || memory_write_desc_if.sts_valid;
                status_len_now = memory_write_desc_if.sts_valid ? memory_write_desc_if.sts_len
                    : memory_write_status_len_reg;
                status_error_now = memory_write_desc_if.sts_valid
                    ? ERROR_W'(memory_write_desc_if.sts_error) : memory_write_status_error_reg;
                stream_error_now = memory_write_stream_error_reg;

                if (beat_accepted) begin
                    if (memory_write_input_len_reg == 0) begin
                        memory_write_first_pulse_reg <= 1'b1;
                        memory_write_first_client_reg <= memory_write_client_reg;
                    end

                    memory_write_input_len_reg <= next_input_len;
                    memory_write_saw_last_reg <= last_seen_now;

                    if (!keep_contiguous(memory_write_src_tkeep)
                        || (!memory_write_src_tlast && memory_write_src_tkeep != '1)) begin
                        stream_error_now = DMA_ERROR_AXIS;
                    end

                    if (memory_write_client_reg != WR_CLIENT_NON_OETP
                        && (memory_write_src_tid != memory_write_sequence_reg
                            || memory_write_src_tdest != {ROUTE_PEER, memory_write_peer_idx_reg}
                            || memory_write_src_tuser[AXIS_USER_LAST_BIT] != memory_write_last_reg
                            || memory_write_src_tuser[AXIS_USER_ROLE_BIT]
                            != (memory_write_client_reg == WR_CLIENT_RESPONDER
                                ? TRANSFER_ROLE_RESPONDER : TRANSFER_ROLE_INITIATOR))) begin
                        stream_error_now = DMA_ERROR_AXIS;
                    end

                    if (memory_write_client_reg == WR_CLIENT_NON_OETP) begin
                        if (next_input_len > memory_write_len_reg
                            || (!memory_write_src_tlast
                                && next_input_len >= memory_write_len_reg)) begin
                            stream_error_now = DMA_ERROR_OVERFLOW;
                        end
                    end else if
                        ((memory_write_src_tlast && next_input_len != memory_write_len_reg) ||
                        (!memory_write_src_tlast && next_input_len >= memory_write_len_reg)) begin
                        stream_error_now = DMA_ERROR_AXIS;
                    end
                end

                if (memory_write_desc_if.sts_valid) begin
                    memory_write_status_seen_reg <= 1'b1;
                    memory_write_status_len_reg <= memory_write_desc_if.sts_len;
                    memory_write_status_error_reg <= ERROR_W'(memory_write_desc_if.sts_error);
                end
                memory_write_stream_error_reg <= stream_error_now;

                if (last_seen_now && status_seen_now) begin
                    memory_write_done_pulse_reg <= 1'b1;
                    memory_write_done_client_reg <= memory_write_client_reg;
                    memory_write_done_len_reg <= status_len_now;
                    if (status_error_now != DMA_ERROR_NONE) begin
                        memory_write_done_error_reg <= status_error_now;
                    end else begin
                        memory_write_done_error_reg <= stream_error_now;
                    end
                    if (memory_write_client_reg == 2'd2) begin
                        memory_write_rr_reg <= 2'd0;
                    end else begin
                        memory_write_rr_reg <= memory_write_client_reg + 1'b1;
                    end
                    memory_write_state_reg <= WR_IDLE;
                end
            end
            default: memory_write_state_reg <= WR_IDLE;
        endcase

        if (rst) begin
            memory_write_client_reg <= WR_CLIENT_PEER;
            memory_write_addr_reg <= '0;
            memory_write_len_reg <= '0;
            memory_write_peer_idx_reg <= '0;
            memory_write_sequence_reg <= '0;
            memory_write_last_reg <= 1'b0;
            memory_write_input_len_reg <= '0;
            memory_write_saw_last_reg <= 1'b0;
            memory_write_status_seen_reg <= 1'b0;
            memory_write_status_len_reg <= '0;
            memory_write_status_error_reg <= '0;
            memory_write_stream_error_reg <= '0;
            memory_write_accept_client_reg <= '0;
            memory_write_first_client_reg <= '0;
            memory_write_done_client_reg <= '0;
            memory_write_done_len_reg <= '0;
            memory_write_done_error_reg <= '0;
            memory_write_state_reg <= WR_IDLE;
            memory_write_slot_reg <= '0;
            memory_write_rr_reg <= WR_CLIENT_PEER;
            memory_write_accept_pulse_reg <= 1'b0;
            memory_write_first_pulse_reg <= 1'b0;
            memory_write_done_pulse_reg <= 1'b0;
        end

    end

    always_ff @(posedge clk) begin : peer_transmit_status
        if (rst) begin
            peer_tx_status_valid_reg <= 1'b0;
            peer_tx_status_peer_reg <= '0;
            peer_tx_status_sequence_reg <= '0;
            peer_tx_status_len_reg <= '0;
            peer_tx_status_error_reg <= '0;
        end else begin
            if (initiator_tx_status_fire) peer_tx_status_valid_reg <= 1'b0;
            if (memory_read_done_pulse_reg && memory_read_done_client_reg == RD_CLIENT_PEER) begin
                peer_tx_status_valid_reg <= 1'b1;
                peer_tx_status_peer_reg <= memory_read_peer_idx_reg;
                peer_tx_status_sequence_reg <= memory_read_sequence_reg;
                peer_tx_status_len_reg <= memory_read_done_len_reg;
                peer_tx_status_error_reg <= memory_read_done_error_reg;
            end
        end

    end

    always_ff @(posedge clk) begin : responder_irq_control
        responder_irq_event_if.admit_valid <= rst ? '0
            : ((responder_irq_state_reg == RESP_IRQ_ADMIT) && !(responder_irq_admit_fire));
        responder_irq_event_if.admit_source <= rst ? '0 : (responder_irq_source_reg);
        responder_irq_event_if.admit_enable <= rst ? '0 : (responder_irq_enable_reg);
        responder_irq_event_if.commit_valid <= rst ? '0
            : ((responder_irq_state_reg == RESP_IRQ_COMMIT) && !(responder_irq_commit_fire));
        responder_irq_event_if.commit_source <= rst ? '0 : (responder_irq_source_reg);
        responder_irq_event_if.commit_peer_idx <= rst ? '0
            : (RESPONDER_IRQ_PEER_W'(responder_irq_peer_idx_reg));
        // Reserve IRQ capacity only for failed incoming requests. Successful requests need no
        // event. Retain a pending failure notification under backpressure, while allowing the
        // current error reply to proceed. The next incoming request waits until that notification
        // is accepted.
        if (responder_error_valid) begin
            if (int'(responder_peer_idx_reg) < NUM_OF_PEERS) begin
                responder_irq_peer_idx_reg <= responder_peer_idx_reg;
                responder_irq_source_reg <= responder_kind_reg == TRANSFER_KIND_RMEM
                    ? responder_irq_event_if.EVENT_RMEM_ERROR : EVENT_PEER_DMA_COMPLETE;
                responder_irq_enable_reg <= responder_kind_reg == TRANSFER_KIND_RMEM ||
                    endpoint_if.csr_to_core.peers.entry[
                    responder_peer_idx_reg].dma.irq_enable.value;
                responder_irq_state_reg <= RESP_IRQ_ADMIT;
            end
        end
        case (responder_irq_state_reg)
            RESP_IRQ_ADMIT:
                if (responder_irq_admit_fire) begin
                    responder_irq_state_reg <= responder_irq_event_if.admit_reserved
                        ? RESP_IRQ_COMMIT : RESP_IRQ_IDLE;
                end
            RESP_IRQ_COMMIT:
                if (responder_irq_commit_fire) responder_irq_state_reg <= RESP_IRQ_IDLE;
            default: begin
            end
        endcase

        if (rst) begin
            responder_irq_state_reg <= RESP_IRQ_IDLE;
            responder_irq_enable_reg <= 1'b0;
            responder_irq_source_reg <= EVENT_PEER_DMA_COMPLETE;
            responder_irq_peer_idx_reg <= '0;
        end
    end

    always_ff @(posedge clk) begin : csr_outputs
        csr_raw_tx_clear_errors_hwclr_reg <= rst ? '0 : (!rst
                && endpoint_if.csr_to_core.non_oetp_dma.tx.command_status.clear_errors.value);
        csr_raw_rx_clear_errors_hwclr_reg <= rst ? '0 : (!rst
                && endpoint_if.csr_to_core.non_oetp_dma.rx.command_status.clear_errors.value);
        for (int unsigned n = 0; n < NUM_OF_PEERS; n++) begin
            peer_csr_clear_error_hwclr_reg[n] <= rst ? '0 : (!rst
                    && endpoint_if.csr_to_core.peers.entry[n].dma.clear_error.value);
        end

    end

endmodule

`resetall
