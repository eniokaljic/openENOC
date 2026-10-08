// SPDX-FileCopyrightText: 2026 Enio Kaljic
// SPDX-License-Identifier: CERN-OHL-S-2.0

`resetall
`timescale 1ns / 1ps
`default_nettype none

/* Command/completion interface for bulk DMA and scalar RMEM. */
interface openenoc_dma_transfer_if #(
    parameter int unsigned ADDR_W = 32,
    parameter int unsigned LEN_W = 32,
    parameter int unsigned PEER_IDX_W = 1,
    parameter int unsigned SEQUENCE_W = 32,
    parameter int unsigned ERROR_W = 4
);
    localparam logic DMA_OP_READ = 1'b0;
    localparam logic DMA_OP_WRITE = 1'b1;
    localparam logic TRANSFER_KIND_DMA = 1'b0;
    localparam logic TRANSFER_KIND_RMEM = 1'b1;
    localparam int unsigned AXIS_USER_W = 2;
    localparam int unsigned AXIS_USER_LAST_BIT = 0;
    localparam int unsigned AXIS_USER_ROLE_BIT = 1;
    localparam logic TRANSFER_ROLE_INITIATOR = 1'b0;
    localparam logic TRANSFER_ROLE_RESPONDER = 1'b1;

    localparam logic [ERROR_W-1:0] ERROR_NONE = ERROR_W'(0);
    localparam logic [ERROR_W-1:0] ERROR_LOCAL_INVALID = ERROR_W'(1);
    localparam logic [ERROR_W-1:0] ERROR_LOCAL_AXIS = ERROR_W'(2);
    localparam logic [ERROR_W-1:0] ERROR_LOCAL_OVERFLOW = ERROR_W'(3);
    localparam logic [ERROR_W-1:0] ERROR_LOCAL_AXI_RD_SLVERR = ERROR_W'(4);
    localparam logic [ERROR_W-1:0] ERROR_LOCAL_AXI_RD_DECERR = ERROR_W'(5);
    localparam logic [ERROR_W-1:0] ERROR_LOCAL_AXI_WR_SLVERR = ERROR_W'(6);
    localparam logic [ERROR_W-1:0] ERROR_LOCAL_AXI_WR_DECERR = ERROR_W'(7);
    localparam logic [ERROR_W-1:0] ERROR_TIMEOUT = ERROR_W'(8);
    localparam logic [ERROR_W-1:0] ERROR_REMOTE_INVALID = ERROR_W'(9);
    localparam logic [ERROR_W-1:0] ERROR_REMOTE_AXIS = ERROR_W'(10);
    localparam logic [ERROR_W-1:0] ERROR_REMOTE_OVERFLOW = ERROR_W'(11);
    localparam logic [ERROR_W-1:0] ERROR_REMOTE_AXI_RD_SLVERR = ERROR_W'(12);
    localparam logic [ERROR_W-1:0] ERROR_REMOTE_AXI_RD_DECERR = ERROR_W'(13);
    localparam logic [ERROR_W-1:0] ERROR_REMOTE_AXI_WR_SLVERR = ERROR_W'(14);
    localparam logic [ERROR_W-1:0] ERROR_REMOTE_AXI_WR_DECERR = ERROR_W'(15);

    if (ERROR_W < 4) begin : g_error_width
        $fatal(0, {"Error: DMA completion codes require at ", "least four bits (instance %m)"});
    end

    function automatic logic [ERROR_W-1:0] csr_error_from_wire(input logic [31:0] wire_code);
        case (wire_code)
            32'd1: csr_error_from_wire = ERROR_REMOTE_INVALID;
            32'd2: csr_error_from_wire = ERROR_REMOTE_AXIS;
            32'd3: csr_error_from_wire = ERROR_REMOTE_OVERFLOW;
            32'd4: csr_error_from_wire = ERROR_REMOTE_AXI_RD_SLVERR;
            32'd5: csr_error_from_wire = ERROR_REMOTE_AXI_RD_DECERR;
            32'd6: csr_error_from_wire = ERROR_REMOTE_AXI_WR_SLVERR;
            32'd7: csr_error_from_wire = ERROR_REMOTE_AXI_WR_DECERR;
            default: csr_error_from_wire = ERROR_LOCAL_INVALID;
        endcase
    endfunction

    localparam logic [1:0] ROUTE_PEER = 2'b00;
    localparam logic [1:0] ROUTE_NON_OETP_DMA = 2'b01;
    localparam logic [1:0] ROUTE_DIRECT = 2'b10;
    localparam logic [1:0] ROUTE_DROP = 2'b11;

    /* Claim one armed raw RX descriptor before its frame. */
    logic non_oetp_rx_available;
    logic non_oetp_rx_claim_valid;
    logic non_oetp_rx_claim_ready;

    /* Request channel */
    logic req_valid;
    logic req_ready;
    logic req_kind;
    logic req_op;
    logic [ADDR_W-1:0] req_addr;
    logic [LEN_W-1:0] req_len;
    logic [PEER_IDX_W-1:0] req_peer_idx;
    logic [SEQUENCE_W-1:0] req_sequence;
    logic req_last;
    logic [31:0] req_biten;
    logic [31:0] req_wdata;

    logic [ERROR_W-1:0] req_error_code;
    logic req_rx_status;

    /* Source-read and receive-frame terminal status. */
    logic tx_status_valid, tx_status_ready;
    logic [PEER_IDX_W-1:0] tx_status_peer_idx;
    logic [SEQUENCE_W-1:0] tx_status_sequence;
    logic [LEN_W-1:0] tx_status_len;
    logic [ERROR_W-1:0] tx_status_error_code;
    logic rx_status_valid, rx_status_ready;
    logic [PEER_IDX_W-1:0] rx_status_peer_idx;
    logic [SEQUENCE_W-1:0] rx_status_sequence;
    logic [LEN_W-1:0] rx_status_len;
    logic [ERROR_W-1:0] rx_status_error_code;

    /* Completion channel */
    logic cpl_valid;
    logic cpl_ready;
    logic cpl_kind;
    logic cpl_op;
    logic [LEN_W-1:0] cpl_transferred_len;
    logic [PEER_IDX_W-1:0] cpl_peer_idx;
    logic [SEQUENCE_W-1:0] cpl_sequence;
    logic cpl_last;
    logic cpl_error;
    logic [ERROR_W-1:0] cpl_error_code;
    logic [31:0] cpl_rdata;

    modport requester(
        input non_oetp_rx_available,
        output non_oetp_rx_claim_valid,
        input non_oetp_rx_claim_ready,
        output req_valid,
        input req_ready,
        output req_kind,
        output req_op,
        output req_addr,
        output req_len,
        output req_peer_idx,
        output req_sequence,
        output req_last,
        output req_biten,
        output req_wdata,
        output req_error_code,
        output req_rx_status,
        output tx_status_valid,
        output tx_status_peer_idx,
        output tx_status_sequence,
        output tx_status_len,
        output tx_status_error_code,
        output rx_status_valid,
        output rx_status_peer_idx,
        output rx_status_sequence,
        output rx_status_len,
        output rx_status_error_code,
        input tx_status_ready,
        input rx_status_ready,
        input cpl_valid,
        output cpl_ready,
        input cpl_kind,
        input cpl_op,
        input cpl_transferred_len,
        input cpl_peer_idx,
        input cpl_sequence,
        input cpl_last,
        input cpl_error,
        input cpl_error_code,
        input cpl_rdata,
        import csr_error_from_wire
    );

    modport executor(
        output non_oetp_rx_available,
        input non_oetp_rx_claim_valid,
        output non_oetp_rx_claim_ready,
        input req_valid,
        output req_ready,
        input req_kind,
        input req_op,
        input req_addr,
        input req_len,
        input req_peer_idx,
        input req_sequence,
        input req_last,
        input req_biten,
        input req_wdata,
        input req_error_code,
        input req_rx_status,
        input tx_status_valid,
        input tx_status_peer_idx,
        input tx_status_sequence,
        input tx_status_len,
        input tx_status_error_code,
        input rx_status_valid,
        input rx_status_peer_idx,
        input rx_status_sequence,
        input rx_status_len,
        input rx_status_error_code,
        output tx_status_ready,
        output rx_status_ready,
        output cpl_valid,
        input cpl_ready,
        output cpl_kind,
        output cpl_op,
        output cpl_transferred_len,
        output cpl_peer_idx,
        output cpl_sequence,
        output cpl_last,
        output cpl_error,
        output cpl_error_code,
        output cpl_rdata,
        import csr_error_from_wire
    );

    modport mon(
        input non_oetp_rx_available,
        input non_oetp_rx_claim_valid,
        input non_oetp_rx_claim_ready,
        input req_valid,
        input req_ready,
        input req_kind,
        input req_op,
        input req_addr,
        input req_len,
        input req_peer_idx,
        input req_sequence,
        input req_last,
        input req_biten,
        input req_wdata,
        input req_error_code,
        input req_rx_status,
        input tx_status_valid,
        input tx_status_peer_idx,
        input tx_status_sequence,
        input tx_status_len,
        input tx_status_error_code,
        input rx_status_valid,
        input rx_status_peer_idx,
        input rx_status_sequence,
        input rx_status_len,
        input rx_status_error_code,
        input tx_status_ready,
        input rx_status_ready,
        input cpl_valid,
        input cpl_ready,
        input cpl_kind,
        input cpl_op,
        input cpl_transferred_len,
        input cpl_peer_idx,
        input cpl_sequence,
        input cpl_last,
        input cpl_error,
        input cpl_error_code,
        input cpl_rdata
    );

endinterface

`resetall
