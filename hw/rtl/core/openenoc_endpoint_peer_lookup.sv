// SPDX-FileCopyrightText: 2026 Enio Kaljic
// SPDX-License-Identifier: CERN-OHL-S-2.0

`resetall
`timescale 1ns / 1ps
`default_nettype none

/*
 * openENOC endpoint peer-table lookup
 *
 * Requests from the lookup clients are arbitrated round-robin. The selected
 * peer entry is sampled from the CSR interface when the request is accepted,
 * and the registered response is presented one cycle later. Response data is
 * retained until its client accepts it.
 *
 * Disabled entries never match. Index lookups select peer-DMA entries, RMEM
 * lookups select transparent-RMEM entries whose half-open region contains the
 * requested address, and MAC lookups select any enabled entry. req_mode_mask
 * can further restrict the accepted modes for every lookup type.
 */
module openenoc_endpoint_peer_lookup #(
    parameter int LOOKUP_PORTS = 2,
    parameter int NUM_OF_PEERS = 4,
    parameter int PEER_IDX_W = NUM_OF_PEERS > 1 ? $clog2(NUM_OF_PEERS) : 1,
    parameter int ADDR_W = 32
) (
    input  wire logic                    clk,
    input  wire logic                    rst,

    openenoc_endpoint_if.core            endpoint_if,
    openenoc_peer_lookup_if.slv           lookup_if[LOOKUP_PORTS]
);

    localparam int PORT_IDX_W = LOOKUP_PORTS > 1 ? $clog2(LOOKUP_PORTS) : 1;
    localparam logic [1:0] LOOKUP_BY_INDEX = lookup_if[0].LOOKUP_BY_INDEX;
    localparam logic [1:0] LOOKUP_BY_RMEM  = lookup_if[0].LOOKUP_BY_RMEM;
    localparam logic [1:0] LOOKUP_BY_MAC   = lookup_if[0].LOOKUP_BY_MAC;

    // Check configuration
    /* verilator lint_off GENUNNAMED */
    if (LOOKUP_PORTS < 1)
        $fatal(0, "Error: LOOKUP_PORTS must be at least 1 (instance %m)");
    if (NUM_OF_PEERS < 1)
        $fatal(0, "Error: NUM_OF_PEERS must be at least 1 (instance %m)");
    if (PEER_IDX_W < 1)
        $fatal(0, "Error: PEER_IDX_W must be at least 1 (instance %m)");
    if (ADDR_W != 32)
        $fatal(0, "Error: ADDR_W must match the 32-bit peer CSR fields (instance %m)");
    if (endpoint_if.NUM_OF_PEERS != NUM_OF_PEERS)
        $fatal(0, "Error: endpoint interface peer count mismatch (instance %m)");
    /* verilator lint_on GENUNNAMED */

    wire [LOOKUP_PORTS-1:0] request;
    wire [LOOKUP_PORTS-1:0] grant;
    wire                    grant_valid;
    wire [PORT_IDX_W-1:0]   grant_index;
    wire [1:0]              req_type[LOOKUP_PORTS];
    wire [3:0]              req_mode_mask[LOOKUP_PORTS];
    wire [PEER_IDX_W-1:0]   req_peer_idx[LOOKUP_PORTS];
    wire [ADDR_W-1:0]       req_rmem_addr[LOOKUP_PORTS];
    wire [47:0]             req_mac_addr[LOOKUP_PORTS];
    wire [LOOKUP_PORTS-1:0] rsp_ready;

    logic                   rsp_valid_reg;
    logic [PORT_IDX_W-1:0]  rsp_owner_reg;
    logic                   rsp_hit_reg;
    logic [PEER_IDX_W-1:0]  rsp_peer_idx_reg;
    logic [47:0]            rsp_mac_addr_reg;
    logic [ADDR_W-1:0]      rsp_rmem_offset_reg;
    logic [ADDR_W-1:0]      rsp_local_addr_reg;
    logic [ADDR_W-1:0]      rsp_remote_addr_reg;
    logic [ADDR_W-1:0]      rsp_size_reg;
    logic [1:0]             rsp_dma_mode_reg;
    logic                   rsp_irq_enable_reg;

    logic                   response_ready;
    wire                    response_slot_available = !rsp_valid_reg || response_ready;
    wire                    request_accept = !rst && response_slot_available && grant_valid;

    openenoc_rr_arbiter #(
        .PORTS   (LOOKUP_PORTS),
        .INDEX_W (PORT_IDX_W)
    )
    u_request_arbiter (
        .clk         (clk),
        .rst         (rst),
        .request     (request),
        .accept      (request_accept),
        .grant       (grant),
        .grant_valid (grant_valid),
        .grant_index (grant_index)
    );

    logic [1:0]                selected_req_type;
    logic [3:0]                selected_req_mode_mask;
    logic [PEER_IDX_W-1:0]     selected_req_peer_idx;
    logic [ADDR_W-1:0]         selected_req_rmem_addr;
    logic [47:0]               selected_req_mac_addr;

    always_comb begin
        selected_req_type = '0;
        selected_req_mode_mask = '0;
        selected_req_peer_idx = '0;
        selected_req_rmem_addr = '0;
        selected_req_mac_addr = '0;

        for (int port = 0; port < LOOKUP_PORTS; port++) begin
            if (grant[port]) begin
                selected_req_type = req_type[port];
                selected_req_mode_mask = req_mode_mask[port];
                selected_req_peer_idx = req_peer_idx[port];
                selected_req_rmem_addr = req_rmem_addr[port];
                selected_req_mac_addr = req_mac_addr[port];
            end
        end
    end

    logic                   lookup_hit_next;
    logic [PEER_IDX_W-1:0]  lookup_peer_idx_next;
    logic [47:0]            lookup_mac_addr_next;
    logic [ADDR_W-1:0]      lookup_rmem_offset_next;
    logic [ADDR_W-1:0]      lookup_local_addr_next;
    logic [ADDR_W-1:0]      lookup_remote_addr_next;
    logic [ADDR_W-1:0]      lookup_size_next;
    logic [1:0]             lookup_dma_mode_next;
    logic                   lookup_irq_enable_next;

    always_comb begin
        lookup_hit_next = 1'b0;
        lookup_peer_idx_next = '0;
        lookup_mac_addr_next = '0;
        lookup_rmem_offset_next = '0;
        lookup_local_addr_next = '0;
        lookup_remote_addr_next = '0;
        lookup_size_next = '0;
        lookup_dma_mode_next = '0;
        lookup_irq_enable_next = 1'b0;

        for (int peer = 0; peer < NUM_OF_PEERS; peer++) begin
            logic [1:0] peer_mode;
            logic [47:0] peer_mac_addr;
            logic [ADDR_W-1:0] peer_rmem_offset;
            logic [ADDR_W-1:0] peer_size;
            logic type_match;
            logic key_match;

            peer_mode = endpoint_if.csr_to_core.peers.entry[peer].dma.mode.value;
            peer_mac_addr = {
                endpoint_if.csr_to_core.peers.entry[peer].mac_address.hi_word.value,
                endpoint_if.csr_to_core.peers.entry[peer].mac_address.lo_word.value
            };
            peer_rmem_offset =
                endpoint_if.csr_to_core.peers.entry[peer].rmem_address.offset.value;
            peer_size = endpoint_if.csr_to_core.peers.entry[peer].size.bytes.value;
            type_match = 1'b0;
            key_match = 1'b0;

            case (selected_req_type)
                LOOKUP_BY_INDEX: begin
                    type_match = peer_mode == 2'd2 || peer_mode == 2'd3;
                    key_match = selected_req_peer_idx == PEER_IDX_W'(peer);
                end
                LOOKUP_BY_RMEM: begin
                    type_match = peer_mode == 2'd1;
                    key_match = peer_size != 0 &&
                        {1'b0, selected_req_rmem_addr} >= {1'b0, peer_rmem_offset} &&
                        {1'b0, selected_req_rmem_addr} <
                            ({1'b0, peer_rmem_offset} + {1'b0, peer_size});
                end
                LOOKUP_BY_MAC: begin
                    type_match = peer_mode != 2'd0;
                    key_match = selected_req_mac_addr == peer_mac_addr;
                end
                default: begin
                    type_match = 1'b0;
                    key_match = 1'b0;
                end
            endcase

            if (!lookup_hit_next && type_match && key_match &&
                    selected_req_mode_mask[peer_mode]) begin
                lookup_hit_next = 1'b1;
                lookup_peer_idx_next = PEER_IDX_W'(peer);
                lookup_mac_addr_next = peer_mac_addr;
                lookup_rmem_offset_next = peer_rmem_offset;
                lookup_local_addr_next =
                    endpoint_if.csr_to_core.peers.entry[peer].local_address.base.value;
                lookup_remote_addr_next =
                    endpoint_if.csr_to_core.peers.entry[peer].remote_address.base.value;
                lookup_size_next = peer_size;
                lookup_dma_mode_next = peer_mode;
                lookup_irq_enable_next =
                    endpoint_if.csr_to_core.peers.entry[peer].dma.irq_enable.value;
            end
        end
    end

    always_comb begin
        response_ready = 1'b0;

        for (int port = 0; port < LOOKUP_PORTS; port++) begin
            if (rsp_valid_reg && rsp_owner_reg == PORT_IDX_W'(port)) begin
                response_ready = rsp_ready[port];
            end
        end
    end

    for (genvar port = 0; port < LOOKUP_PORTS; port++) begin : g_lookup_port
        /* verilator lint_off GENUNNAMED */
        if (lookup_if[port].NUM_OF_PEERS != NUM_OF_PEERS ||
                lookup_if[port].PEER_IDX_W != PEER_IDX_W ||
                lookup_if[port].ADDR_W != ADDR_W)
            $fatal(0, "Error: lookup interface parameter mismatch (instance %m)");
        /* verilator lint_on GENUNNAMED */

        wire port_rsp_valid = rsp_valid_reg && rsp_owner_reg == PORT_IDX_W'(port);

        assign request[port] = lookup_if[port].req_valid;
        assign req_type[port] = lookup_if[port].req_type;
        assign req_mode_mask[port] = lookup_if[port].req_mode_mask;
        assign req_peer_idx[port] = lookup_if[port].req_peer_idx;
        assign req_rmem_addr[port] = lookup_if[port].req_rmem_addr;
        assign req_mac_addr[port] = lookup_if[port].req_mac_addr;
        assign rsp_ready[port] = lookup_if[port].rsp_ready;
        assign lookup_if[port].req_ready = !rst && response_slot_available && grant[port];
        assign lookup_if[port].rsp_valid = port_rsp_valid;
        assign lookup_if[port].rsp_hit = port_rsp_valid ? rsp_hit_reg : 1'b0;
        assign lookup_if[port].rsp_peer_idx = port_rsp_valid ? rsp_peer_idx_reg : '0;
        assign lookup_if[port].rsp_mac_addr = port_rsp_valid ? rsp_mac_addr_reg : '0;
        assign lookup_if[port].rsp_rmem_offset =
            port_rsp_valid ? rsp_rmem_offset_reg : '0;
        assign lookup_if[port].rsp_local_addr =
            port_rsp_valid ? rsp_local_addr_reg : '0;
        assign lookup_if[port].rsp_remote_addr =
            port_rsp_valid ? rsp_remote_addr_reg : '0;
        assign lookup_if[port].rsp_size = port_rsp_valid ? rsp_size_reg : '0;
        assign lookup_if[port].rsp_dma_mode = port_rsp_valid ? rsp_dma_mode_reg : '0;
        assign lookup_if[port].rsp_irq_enable =
            port_rsp_valid ? rsp_irq_enable_reg : 1'b0;
    end

    always_ff @(posedge clk) begin
        if (rst) begin
            rsp_valid_reg <= 1'b0;
            rsp_owner_reg <= '0;
            rsp_hit_reg <= 1'b0;
            rsp_peer_idx_reg <= '0;
            rsp_mac_addr_reg <= '0;
            rsp_rmem_offset_reg <= '0;
            rsp_local_addr_reg <= '0;
            rsp_remote_addr_reg <= '0;
            rsp_size_reg <= '0;
            rsp_dma_mode_reg <= '0;
            rsp_irq_enable_reg <= 1'b0;
        end else if (request_accept) begin
            rsp_valid_reg <= 1'b1;
            rsp_owner_reg <= grant_index;
            rsp_hit_reg <= lookup_hit_next;
            rsp_peer_idx_reg <= lookup_peer_idx_next;
            rsp_mac_addr_reg <= lookup_mac_addr_next;
            rsp_rmem_offset_reg <= lookup_rmem_offset_next;
            rsp_local_addr_reg <= lookup_local_addr_next;
            rsp_remote_addr_reg <= lookup_remote_addr_next;
            rsp_size_reg <= lookup_size_next;
            rsp_dma_mode_reg <= lookup_dma_mode_next;
            rsp_irq_enable_reg <= lookup_irq_enable_next;
        end else if (response_ready) begin
            rsp_valid_reg <= 1'b0;
        end
    end

endmodule

`resetall
