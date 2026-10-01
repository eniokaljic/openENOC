// SPDX-FileCopyrightText: 2026 Enio Kaljic
// SPDX-License-Identifier: CERN-OHL-S-2.0

`resetall
`timescale 1ns / 1ps
`default_nettype none

/*
 * Command and completion interface for an openENOC DMA transfer
 *
 * The interface is symmetric and is intended to be instantiated twice between
 * the DMA and oETP engines:
 *
 *   - DMA initiator path: DMA is requester and oETP is executor.
 *   - DMA responder path: oETP is requester and DMA is executor.
 *
 * READ and WRITE are defined from the executor's point of view. req_addr is
 * the final byte address in the executor's target address space; address
 * translation is performed once by the requester. The executor may validate
 * the address against its permitted region, but does not translate it again.
 */
interface openenoc_dma_transfer_if #(
    parameter int unsigned ADDR_W = 32,
    parameter int unsigned LEN_W = 32,
    parameter int unsigned PEER_IDX_W = 1,
    parameter int unsigned SEQUENCE_W = 32,
    parameter int unsigned ERROR_W = 4
);
    localparam logic DMA_OP_READ  = 1'b0;
    localparam logic DMA_OP_WRITE = 1'b1;

    /* Request channel */
    logic                      req_valid;
    logic                      req_ready;
    logic                      req_op;
    logic [ADDR_W-1:0]         req_addr;
    logic [LEN_W-1:0]          req_len;
    logic [PEER_IDX_W-1:0]     req_peer_idx;
    logic [SEQUENCE_W-1:0]     req_sequence;
    logic                      req_last;

    /* Completion channel */
    logic                      cpl_valid;
    logic                      cpl_ready;
    logic                      cpl_op;
    logic [LEN_W-1:0]          cpl_transferred_len;
    logic [PEER_IDX_W-1:0]     cpl_peer_idx;
    logic [SEQUENCE_W-1:0]     cpl_sequence;
    logic                      cpl_last;
    logic                      cpl_error;
    logic [ERROR_W-1:0]        cpl_error_code;

    modport requester (
        output req_valid,
        input  req_ready,
        output req_op,
        output req_addr,
        output req_len,
        output req_peer_idx,
        output req_sequence,
        output req_last,

        input  cpl_valid,
        output cpl_ready,
        input  cpl_op,
        input  cpl_transferred_len,
        input  cpl_peer_idx,
        input  cpl_sequence,
        input  cpl_last,
        input  cpl_error,
        input  cpl_error_code
    );

    modport executor (
        input  req_valid,
        output req_ready,
        input  req_op,
        input  req_addr,
        input  req_len,
        input  req_peer_idx,
        input  req_sequence,
        input  req_last,

        output cpl_valid,
        input  cpl_ready,
        output cpl_op,
        output cpl_transferred_len,
        output cpl_peer_idx,
        output cpl_sequence,
        output cpl_last,
        output cpl_error,
        output cpl_error_code
    );

    modport mon (
        input req_valid,
        input req_ready,
        input req_op,
        input req_addr,
        input req_len,
        input req_peer_idx,
        input req_sequence,
        input req_last,
        input cpl_valid,
        input cpl_ready,
        input cpl_op,
        input cpl_transferred_len,
        input cpl_peer_idx,
        input cpl_sequence,
        input cpl_last,
        input cpl_error,
        input cpl_error_code
    );

endinterface

`resetall
