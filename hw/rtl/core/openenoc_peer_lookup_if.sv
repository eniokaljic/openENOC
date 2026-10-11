// SPDX-FileCopyrightText: 2026 Enio Kaljic
// SPDX-License-Identifier: CERN-OHL-S-2.0

`resetall
`timescale 1ns / 1ps
`default_nettype none

/* Ready/valid endpoint peer-table lookup interface. */
interface openenoc_peer_lookup_if #(
    parameter int unsigned NUM_OF_PEERS = 4,
    parameter int unsigned PEER_IDX_W = NUM_OF_PEERS > 1 ? $clog2(NUM_OF_PEERS) : 1,
    parameter int unsigned ADDR_W = 32
);
    localparam logic [1:0] LOOKUP_BY_INDEX = 2'd0;
    localparam logic [1:0] LOOKUP_BY_RMEM = 2'd1;
    localparam logic [1:0] LOOKUP_BY_MAC = 2'd2;

    /* Request channel. Only the key selected by req_type is meaningful. */
    logic req_valid;
    logic req_ready;
    logic [1:0] req_type;
    logic [3:0] req_mode_mask;
    logic [PEER_IDX_W-1:0] req_peer_idx;
    logic [ADDR_W-1:0] req_rmem_addr;
    logic [47:0] req_mac_addr;

    /*
     * Response channel. The entry fields form one coherent table snapshot. They are driven to
     * deterministic zero values when rsp_hit is clear.
     */
    logic rsp_valid;
    logic rsp_ready;
    logic rsp_hit;
    logic [PEER_IDX_W-1:0] rsp_peer_idx;
    logic [47:0] rsp_mac_addr;
    logic [ADDR_W-1:0] rsp_rmem_offset;
    logic [ADDR_W-1:0] rsp_local_addr;
    logic [ADDR_W-1:0] rsp_remote_addr;
    logic [ADDR_W-1:0] rsp_size;
    logic [1:0] rsp_dma_mode;
    logic rsp_irq_enable;

    modport mst(
        output req_valid,
        input req_ready,
        output req_type,
        output req_mode_mask,
        output req_peer_idx,
        output req_rmem_addr,
        output req_mac_addr,
        input rsp_valid,
        output rsp_ready,
        input rsp_hit,
        input rsp_peer_idx,
        input rsp_mac_addr,
        input rsp_rmem_offset,
        input rsp_local_addr,
        input rsp_remote_addr,
        input rsp_size,
        input rsp_dma_mode,
        input rsp_irq_enable
    );

    modport slv(
        input req_valid,
        output req_ready,
        input req_type,
        input req_mode_mask,
        input req_peer_idx,
        input req_rmem_addr,
        input req_mac_addr,
        output rsp_valid,
        input rsp_ready,
        output rsp_hit,
        output rsp_peer_idx,
        output rsp_mac_addr,
        output rsp_rmem_offset,
        output rsp_local_addr,
        output rsp_remote_addr,
        output rsp_size,
        output rsp_dma_mode,
        output rsp_irq_enable
    );

    modport mon(
        input req_valid,
        input req_ready,
        input req_type,
        input req_mode_mask,
        input req_peer_idx,
        input req_rmem_addr,
        input req_mac_addr,
        input rsp_valid,
        input rsp_ready,
        input rsp_hit,
        input rsp_peer_idx,
        input rsp_mac_addr,
        input rsp_rmem_offset,
        input rsp_local_addr,
        input rsp_remote_addr,
        input rsp_size,
        input rsp_dma_mode,
        input rsp_irq_enable
    );

endinterface

`resetall
