// SPDX-FileCopyrightText: 2026 Enio Kaljic
// SPDX-License-Identifier: AGPL-3.0-or-later

`resetall
`timescale 1ns / 1ps
`default_nettype none

/* Scalar cocotb bridge to the endpoint CSR and interrupt event interfaces */
module test_openenoc_endpoint_irq_controller #(
    parameter int EVENT_PORTS = 4,
    parameter int FIFO_DEPTH = 4,
    parameter int PEER_IDX_W = 5,
    parameter int SEQUENCE_W = 4
) ();

    logic clk;
    logic rst;

    logic global_enable;
    logic [5:0] event_enable;
    logic clear_errors;
    wire clear_errors_hwclr;

    logic complete_valid;
    logic [10:0] complete_peer_idx;
    logic [3:0] complete_source;
    logic [15:0] complete_sequence;
    wire complete_valid_hwclr;

    wire claim_valid;
    wire [10:0] claim_peer_idx;
    wire [3:0] claim_source;
    wire [15:0] claim_sequence;

    wire claim_pending;
    wire credit_full;
    wire overflow;
    wire invalid_complete;
    wire irq_asserted;
    wire [7:0] fifo_level;
    wire [7:0] reserved_count;
    wire irq;

    logic [EVENT_PORTS-1:0] admit_valid;
    wire [EVENT_PORTS-1:0] admit_ready;
    logic [EVENT_PORTS*4-1:0] admit_source;
    logic [EVENT_PORTS-1:0] admit_enable;
    wire [EVENT_PORTS-1:0] admit_reserved;

    logic [EVENT_PORTS-1:0] commit_valid;
    wire [EVENT_PORTS-1:0] commit_ready;
    logic [EVENT_PORTS*4-1:0] commit_source;
    logic [EVENT_PORTS*PEER_IDX_W-1:0] commit_peer_idx;

    openenoc_endpoint_if endpoint_if (
        .clk(clk),
        .rst(rst)
    );

    always_comb begin
        endpoint_if.csr_to_core = '{default: '0};
        endpoint_if.csr_to_core.irq.control.global_enable.value = global_enable;
        endpoint_if.csr_to_core.irq.control.clear_errors.value = clear_errors;
        endpoint_if.csr_to_core.irq.event_enable.peer_dma_complete.value = event_enable[0];
        endpoint_if.csr_to_core.irq.event_enable.non_oetp_dma_tx_complete.value = event_enable[1];
        endpoint_if.csr_to_core.irq.event_enable.non_oetp_dma_rx_complete.value = event_enable[2];
        endpoint_if.csr_to_core.irq.event_enable.non_oetp_direct_tx_complete.value =
            event_enable[3];
        endpoint_if.csr_to_core.irq.event_enable.non_oetp_direct_rx_available.value =
            event_enable[4];
        endpoint_if.csr_to_core.irq.event_enable.rmem_error.value = event_enable[5];
        endpoint_if.csr_to_core.irq.complete.valid.value = complete_valid;
        endpoint_if.csr_to_core.irq.complete.peer_idx.value = complete_peer_idx;
        endpoint_if.csr_to_core.irq.complete.source.value = complete_source;
        endpoint_if.csr_to_core.irq.complete.sequence_.value = complete_sequence;
    end

    assign clear_errors_hwclr = endpoint_if.core_to_csr.irq.control.clear_errors.hwclr;
    assign complete_valid_hwclr = endpoint_if.core_to_csr.irq.complete.valid.hwclr;
    assign claim_valid = endpoint_if.core_to_csr.irq.claim.valid.next;
    assign claim_peer_idx = endpoint_if.core_to_csr.irq.claim.peer_idx.next;
    assign claim_source = endpoint_if.core_to_csr.irq.claim.source.next;
    assign claim_sequence = endpoint_if.core_to_csr.irq.claim.sequence_.next;
    assign claim_pending = endpoint_if.core_to_csr.irq.status.claim_pending.next;
    assign credit_full = endpoint_if.core_to_csr.irq.status.credit_full.next;
    assign overflow = endpoint_if.core_to_csr.irq.status.overflow.next;
    assign invalid_complete = endpoint_if.core_to_csr.irq.status.invalid_complete.next;
    assign irq_asserted = endpoint_if.core_to_csr.irq.status.irq_asserted.next;
    assign fifo_level = endpoint_if.core_to_csr.irq.status.fifo_level.next;
    assign reserved_count = endpoint_if.core_to_csr.irq.status.reserved_count.next;

    openenoc_irq_event_if #(
        .PEER_IDX_W(PEER_IDX_W)
    ) event_if[EVENT_PORTS]();

    for (genvar n = 0; n < EVENT_PORTS; n++) begin : g_bridge
        assign event_if[n].admit_valid = admit_valid[n];
        assign event_if[n].admit_source = admit_source[n*4+:4];
        assign event_if[n].admit_enable = admit_enable[n];
        assign admit_ready[n] = event_if[n].admit_ready;
        assign admit_reserved[n] = event_if[n].admit_reserved;

        assign event_if[n].commit_valid = commit_valid[n];
        assign event_if[n].commit_source = commit_source[n*4+:4];
        assign event_if[n].commit_peer_idx = commit_peer_idx[n*PEER_IDX_W+:PEER_IDX_W];
        assign commit_ready[n] = event_if[n].commit_ready;
    end

    openenoc_endpoint_irq_controller #(
        .EVENT_PORTS(EVENT_PORTS),
        .FIFO_DEPTH(FIFO_DEPTH),
        .PEER_IDX_W(PEER_IDX_W),
        .SEQUENCE_W(SEQUENCE_W)
    ) dut (
        .clk(clk),
        .rst(rst),
        .endpoint_if(endpoint_if),
        .irq(irq),
        .event_if(event_if)
    );

endmodule

`resetall
