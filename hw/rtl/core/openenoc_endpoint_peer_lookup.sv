// SPDX-FileCopyrightText: 2026 Enio Kaljic
// SPDX-License-Identifier: CERN-OHL-S-2.0

`resetall
`timescale 1ns / 1ps
`default_nettype none

/* Shared endpoint peer-table lookup with round-robin arbitration. */
module openenoc_endpoint_peer_lookup #(
    parameter int LOOKUP_PORTS = 2,
    parameter int NUM_OF_PEERS = 4,
    parameter int PEER_IDX_W = NUM_OF_PEERS > 1 ? $clog2(NUM_OF_PEERS) : 1,
    parameter int ADDR_W = 32
) (
    input wire logic clk,
    input wire logic rst,
    openenoc_endpoint_if.core endpoint_if,
    openenoc_peer_lookup_if.slv lookup_if[LOOKUP_PORTS]
);

    localparam int PORT_IDX_W = LOOKUP_PORTS > 1 ? $clog2(LOOKUP_PORTS) : 1;
    localparam logic [1:0] LOOKUP_BY_INDEX = lookup_if[0].LOOKUP_BY_INDEX;
    localparam logic [1:0] LOOKUP_BY_RMEM = lookup_if[0].LOOKUP_BY_RMEM;
    localparam logic [1:0] LOOKUP_BY_MAC = lookup_if[0].LOOKUP_BY_MAC;

    // Check configuration
    /* verilator lint_off GENUNNAMED */
    if (LOOKUP_PORTS < 1) $fatal(0, "Error: LOOKUP_PORTS must be at least 1 (instance %m)");
    if (NUM_OF_PEERS < 1) $fatal(0, "Error: NUM_OF_PEERS must be at least 1 (instance %m)");
    if (PEER_IDX_W < 1) $fatal(0, "Error: PEER_IDX_W must be at least 1 (instance %m)");
    if (PEER_IDX_W < (NUM_OF_PEERS > 1 ? $clog2(NUM_OF_PEERS) : 1))
        $fatal(0, {"Error: PEER_IDX_W cannot represent every peer ", "(instance %m)"});
    if (ADDR_W != 32)
        $fatal(0, {"Error: ADDR_W must match the 32-bit peer CSR ", "fields (instance %m)"});
    if (endpoint_if.NUM_OF_PEERS != NUM_OF_PEERS)
        $fatal(0, {"Error: endpoint interface peer count mismatch ", "(instance %m)"});
    /* verilator lint_on GENUNNAMED */

    typedef enum logic [1:0] {
        EMPTY,
        ONE,
        FULL
    } queue_state_t;
    queue_state_t queue_state_reg;

    logic [PORT_IDX_W-1:0] arbitration_cursor_reg;
    logic queue_head_reg, queue_tail_reg;

    logic [LOOKUP_PORTS-1:0] request_ready_reg, response_valid_reg;
    logic [LOOKUP_PORTS-1:0] request_valid, response_ready;
    logic [1:0] request_type[LOOKUP_PORTS];
    logic [3:0] request_mode_mask[LOOKUP_PORTS];
    logic [PEER_IDX_W-1:0] request_peer_index[LOOKUP_PORTS];
    logic [ADDR_W-1:0] request_rmem_address[LOOKUP_PORTS];
    logic [47:0] request_mac_address[LOOKUP_PORTS];

    typedef struct packed {
        logic hit;
        logic [PEER_IDX_W-1:0] peer_idx;
        logic [47:0] mac_addr;
        logic [ADDR_W-1:0] rmem_offset, local_addr, remote_addr, size;
        logic [1:0] dma_mode;
        logic irq_enable;
    } response_t;
    response_t response_reg[LOOKUP_PORTS];

    for (genvar port = 0; port < LOOKUP_PORTS; port++) begin : g_lookup_port
        if (lookup_if[port].NUM_OF_PEERS != NUM_OF_PEERS || lookup_if[port].PEER_IDX_W != PEER_IDX_W
            || lookup_if[port].ADDR_W != ADDR_W) begin : g_bad_interface
            initial $fatal(0, {"Error: lookup interface parameter mismatch ", "(instance %m)"});
        end
        assign request_valid[port] = lookup_if[port].req_valid;
        assign request_type[port] = lookup_if[port].req_type;
        assign request_mode_mask[port] = lookup_if[port].req_mode_mask;
        assign request_peer_index[port] = lookup_if[port].req_peer_idx;
        assign request_rmem_address[port] = lookup_if[port].req_rmem_addr;
        assign request_mac_address[port] = lookup_if[port].req_mac_addr;
        assign response_ready[port] = lookup_if[port].rsp_ready;
        assign lookup_if[port].req_ready = request_ready_reg[port];
        assign lookup_if[port].rsp_valid = response_valid_reg[port];
        assign lookup_if[port].rsp_hit = response_reg[port].hit;
        assign lookup_if[port].rsp_peer_idx = response_reg[port].peer_idx;
        assign lookup_if[port].rsp_mac_addr = response_reg[port].mac_addr;
        assign lookup_if[port].rsp_rmem_offset = response_reg[port].rmem_offset;
        assign lookup_if[port].rsp_local_addr = response_reg[port].local_addr;
        assign lookup_if[port].rsp_remote_addr = response_reg[port].remote_addr;
        assign lookup_if[port].rsp_size = response_reg[port].size;
        assign lookup_if[port].rsp_dma_mode = response_reg[port].dma_mode;
        assign lookup_if[port].rsp_irq_enable = response_reg[port].irq_enable;
    end

    typedef struct packed {
        logic [PORT_IDX_W-1:0] owner;
        response_t result;
    } queued_response_t;
    queued_response_t queue_reg[2];

    wire [1:0] peer_dma_mode[NUM_OF_PEERS];
    wire [15:0] peer_mac_address_hi_word[NUM_OF_PEERS];
    wire [31:0] peer_mac_address_lo_word[NUM_OF_PEERS];
    wire [31:0] peer_rmem_address_offset[NUM_OF_PEERS];
    wire [31:0] peer_size_bytes[NUM_OF_PEERS];
    wire [31:0] peer_local_address_base[NUM_OF_PEERS];
    wire [31:0] peer_remote_address_base[NUM_OF_PEERS];
    wire [0:0] peer_dma_irq_enable[NUM_OF_PEERS];

    for (genvar peer = 0; peer < NUM_OF_PEERS; peer++) begin : peer_config
        assign peer_dma_mode[peer] = endpoint_if.csr_to_core.peers.entry[peer].dma.mode.value;
        assign peer_mac_address_hi_word[peer] =
            endpoint_if.csr_to_core.peers.entry[peer].mac_address.hi_word.value;
        assign peer_mac_address_lo_word[peer] =
            endpoint_if.csr_to_core.peers.entry[peer].mac_address.lo_word.value;
        assign peer_rmem_address_offset[peer] =
            endpoint_if.csr_to_core.peers.entry[peer].rmem_address.offset.value;
        assign peer_size_bytes[peer] = endpoint_if.csr_to_core.peers.entry[peer].size.bytes.value;
        assign peer_local_address_base[peer] =
            endpoint_if.csr_to_core.peers.entry[peer].local_address.base.value;
        assign peer_remote_address_base[peer] =
            endpoint_if.csr_to_core.peers.entry[peer].remote_address.base.value;
        assign peer_dma_irq_enable[peer] =
            endpoint_if.csr_to_core.peers.entry[peer].dma.irq_enable.value;
    end

    always_ff @(posedge clk) begin : response_queue
        logic head, tail;
        logic [1:0] count;
        logic [PORT_IDX_W-1:0] arbitration_cursor;
        logic selected;
        logic pushed;
        logic push_index;
        queued_response_t pushed_response, head_response;

        head = queue_head_reg;
        tail = queue_tail_reg;
        count = 2'(queue_state_reg);
        arbitration_cursor = arbitration_cursor_reg;
        selected = 1'b0;
        pushed = 1'b0;
        push_index = queue_tail_reg;
        pushed_response = '0;
        request_ready_reg <= '0;
        response_valid_reg <= '0;

        for (int port = 0; port < LOOKUP_PORTS; port++) begin
            response_reg[port] <= '0;
        end

        if (count != 0 && response_ready[queue_reg[head].owner]) begin
            count = count - 1'b1;
            head = !head;
        end

        for (int port = 0; port < LOOKUP_PORTS; port++) begin
            if (request_ready_reg[port] && request_valid[port]) begin
                response_t result;

                result = '0;
                for (int peer = 0; peer < NUM_OF_PEERS; peer++) begin
                    logic [1:0] mode;
                    logic [47:0] mac;
                    logic [31:0] base_addr, size;
                    logic match_key;

                    mode = peer_dma_mode[peer];
                    mac = {peer_mac_address_hi_word[peer], peer_mac_address_lo_word[peer]};
                    base_addr = peer_rmem_address_offset[peer];
                    size = peer_size_bytes[peer];
                    match_key = 1'b0;

                    case (request_type[port])
                        LOOKUP_BY_INDEX:
                            match_key = (mode == 2 || mode == 3)
                                && request_peer_index[port] == PEER_IDX_W'(peer);
                        LOOKUP_BY_RMEM:
                            match_key = mode == 1 && size != 0 &&
                                {1'b0, request_rmem_address[port]} >= {1'b0, base_addr} &&
                                {1'b0, request_rmem_address[port]} < {1'b0, base_addr} + {1'b0,
                                    size};
                        LOOKUP_BY_MAC: match_key = mode != 0 && request_mac_address[port] == mac;
                        default: begin
                        end
                    endcase

                    if (!result.hit && match_key && request_mode_mask[port][mode]) begin
                        result.hit = 1'b1;
                        result.peer_idx = PEER_IDX_W'(peer);
                        result.mac_addr = mac;
                        result.rmem_offset = base_addr;
                        result.local_addr = peer_local_address_base[peer];
                        result.remote_addr = peer_remote_address_base[peer];
                        result.size = size;
                        result.dma_mode = mode;
                        result.irq_enable = peer_dma_irq_enable[peer];
                    end
                end

                pushed = 1'b1;
                push_index = tail;
                pushed_response = '{
                    owner: PORT_IDX_W'(port),
                    result: result
                };
                queue_reg[tail] <= pushed_response;
                tail = !tail;
                count = count + 1'b1;
                arbitration_cursor = port == LOOKUP_PORTS - 1 ? '0 : PORT_IDX_W'(port + 1);
            end
        end

        if (count < 2) begin
            for (int offset = 0; offset < LOOKUP_PORTS; offset++) begin
                int candidate;

                candidate = int'(arbitration_cursor) + offset;
                if (candidate >= LOOKUP_PORTS) begin
                    candidate -= LOOKUP_PORTS;
                end
                if (!selected && request_valid[candidate]) begin
                    selected = 1'b1;
                    request_ready_reg[candidate] <= 1'b1;
                end
            end
        end

        if (count != 0) begin
            head_response = pushed && push_index == head ? pushed_response : queue_reg[head];
            response_valid_reg[head_response.owner] <= 1'b1;
            response_reg[head_response.owner] <= head_response.result;
        end

        queue_state_reg <= queue_state_t'(count);
        queue_head_reg <= head;
        queue_tail_reg <= tail;
        arbitration_cursor_reg <= arbitration_cursor;

        if (rst) begin
            queue_state_reg <= EMPTY;
            queue_head_reg <= 1'b0;
            queue_tail_reg <= 1'b0;
            arbitration_cursor_reg <= '0;
            request_ready_reg <= '0;
            response_valid_reg <= '0;
            for (int port = 0; port < LOOKUP_PORTS; port++) begin
                response_reg[port] <= '0;
            end
        end
    end
endmodule

`resetall
