// SPDX-FileCopyrightText: 2026 Enio Kaljic
// SPDX-License-Identifier: CERN-OHL-S-2.0

`resetall
`timescale 1ns / 1ps
`default_nettype none

/* Endpoint IRQ admission, event queue, and claim completion. */
module openenoc_endpoint_irq_controller #(
    parameter int EVENT_PORTS = 6,
    parameter int FIFO_DEPTH = 16,
    parameter int PEER_IDX_W = 1,
    parameter int SEQUENCE_W = 16,
    parameter logic [EVENT_PORTS-1:0] SAMPLED_ENABLE_MASK = '0
) (
    input wire logic clk,
    input wire logic rst,
    openenoc_endpoint_if.core endpoint_if,
    output logic irq,
    openenoc_irq_event_if.controller event_if[EVENT_PORTS]
);

    localparam int PORT_INDEX_W = EVENT_PORTS > 1 ? $clog2(EVENT_PORTS) : 1;
    localparam int FIFO_COUNT_W = $clog2(FIFO_DEPTH + 1);
    localparam int QUEUE_INDEX_W = FIFO_DEPTH > 1 ? $clog2(FIFO_DEPTH) : 1;
    localparam int CLAIM_DATA_W = PEER_IDX_W + 4 + SEQUENCE_W;
    localparam int CSR_PEER_IDX_W = $bits(claim_peer_idx_reg);
    localparam int CSR_SEQUENCE_W = $bits(claim_sequence_reg);

    localparam logic [3:0] EVENT_PEER_DMA_COMPLETE = event_if[0].EVENT_PEER_DMA_COMPLETE;
    localparam logic[3:0] EVENT_NON_OETP_DMA_TX_COMPLETE =
        event_if[0].EVENT_NON_OETP_DMA_TX_COMPLETE;
    localparam logic[3:0] EVENT_NON_OETP_DMA_RX_COMPLETE =
        event_if[0].EVENT_NON_OETP_DMA_RX_COMPLETE;
    localparam logic[3:0] EVENT_NON_OETP_DIRECT_TX_COMPLETE =
        event_if[0].EVENT_NON_OETP_DIRECT_TX_COMPLETE;
    localparam logic[3:0] EVENT_NON_OETP_DIRECT_RX_AVAILABLE =
        event_if[0].EVENT_NON_OETP_DIRECT_RX_AVAILABLE;
    localparam logic [3:0] EVENT_RMEM_ERROR = event_if[0].EVENT_RMEM_ERROR;

    // check configuration
    /* verilator lint_off GENUNNAMED */
    if (EVENT_PORTS < 1) $fatal(0, "Error: EVENT_PORTS must be at least 1 (instance %m)");
    if (FIFO_DEPTH < 1) $fatal(0, "Error: FIFO_DEPTH must be at least 1 (instance %m)");
    if (PEER_IDX_W < 1 || PEER_IDX_W > CSR_PEER_IDX_W)
        $fatal(0, {"Error: PEER_IDX_W must fit the CSR peer index ", "field (instance %m)"});
    if (SEQUENCE_W < 1 || SEQUENCE_W > CSR_SEQUENCE_W)
        $fatal(0, {"Error: SEQUENCE_W must fit the CSR sequence ", "field (instance %m)"});
    /* verilator lint_on GENUNNAMED */

    wire global_enable = endpoint_if.csr_to_core.irq.control.global_enable.value;
    wire [5:0] event_enable = {
        endpoint_if.csr_to_core.irq.event_enable.rmem_error.value,
        endpoint_if.csr_to_core.irq.event_enable.non_oetp_direct_rx_available.value,
        endpoint_if.csr_to_core.irq.event_enable.non_oetp_direct_tx_complete.value,
        endpoint_if.csr_to_core.irq.event_enable.non_oetp_dma_rx_complete.value,
        endpoint_if.csr_to_core.irq.event_enable.non_oetp_dma_tx_complete.value,
        endpoint_if.csr_to_core.irq.event_enable.peer_dma_complete.value
    };
    wire clear_errors = endpoint_if.csr_to_core.irq.control.clear_errors.value;
    wire complete_valid = endpoint_if.csr_to_core.irq.complete.valid.value;

    function automatic logic source_is_enabled(input logic [3:0] source, input logic [5:0] enables);
        case (source)
            EVENT_PEER_DMA_COMPLETE: return enables[0];
            EVENT_NON_OETP_DMA_TX_COMPLETE: return enables[1];
            EVENT_NON_OETP_DMA_RX_COMPLETE: return enables[2];
            EVENT_NON_OETP_DIRECT_TX_COMPLETE: return enables[3];
            EVENT_NON_OETP_DIRECT_RX_AVAILABLE: return enables[4];
            EVENT_RMEM_ERROR: return enables[5];
            default: return 1'b0;
        endcase
    endfunction

    logic [FIFO_COUNT_W-1:0] fifo_count_reg;
    logic [FIFO_COUNT_W-1:0] reserved_count_reg;
    logic [FIFO_COUNT_W-1:0] port_reserved_count_reg[EVENT_PORTS];
    logic [SEQUENCE_W-1:0] next_sequence_reg;
    logic overflow_reg;
    logic invalid_complete_reg;

    typedef enum logic {
        SELECT,
        OFFER
    } state_t;
    state_t admission_state_reg, commit_state_reg;
    logic [EVENT_PORTS-1:0] admission_ready_reg, admission_reserved_reg, commit_ready_reg;
    logic [EVENT_PORTS-1:0] admission_valid, admission_enable, commit_valid;
    logic [3:0] admission_source[EVENT_PORTS], commit_source[EVENT_PORTS];
    logic [PEER_IDX_W-1:0] commit_peer_idx[EVENT_PORTS];
    logic [PORT_INDEX_W-1:0] admission_cursor_reg, commit_cursor_reg;
    logic [CLAIM_DATA_W-1:0] queue_reg[FIFO_DEPTH];
    logic [QUEUE_INDEX_W-1:0] head_reg, tail_reg;
    logic claim_valid_reg;
    logic [CLAIM_DATA_W-1:0] claim_reg;

    for (genvar port = 0; port < EVENT_PORTS; port++) begin : g_event_port
        assign admission_valid[port] = event_if[port].admit_valid;
        assign admission_enable[port] = event_if[port].admit_enable;
        assign admission_source[port] = event_if[port].admit_source;
        assign commit_valid[port] = event_if[port].commit_valid;
        assign commit_source[port] = event_if[port].commit_source;
        assign commit_peer_idx[port] = event_if[port].commit_peer_idx;
        assign event_if[port].admit_ready = admission_ready_reg[port];
        assign event_if[port].admit_reserved = admission_reserved_reg[port];
        assign event_if[port].commit_ready = commit_ready_reg[port];
    end

    localparam int CLAIM_PEER_IDX_W = $bits(endpoint_if.core_to_csr.irq.claim.peer_idx.next);
    logic [CLAIM_PEER_IDX_W-1:0] claim_peer_idx_reg;
    assign endpoint_if.core_to_csr.irq.claim.peer_idx.next = claim_peer_idx_reg;
    localparam int CLAIM_SEQUENCE_W = $bits(endpoint_if.core_to_csr.irq.claim.sequence_.next);
    logic [CLAIM_SEQUENCE_W-1:0] claim_sequence_reg;
    assign endpoint_if.core_to_csr.irq.claim.sequence_.next = claim_sequence_reg;
    localparam int CLAIM_SOURCE_W = $bits(endpoint_if.core_to_csr.irq.claim.source.next);
    logic [CLAIM_SOURCE_W-1:0] claim_source_reg;
    assign endpoint_if.core_to_csr.irq.claim.source.next = claim_source_reg;
    assign endpoint_if.core_to_csr.irq.claim.valid.next = claim_valid_reg;
    localparam int COMPLETE_VALID_HWCLR_W = $bits(endpoint_if.core_to_csr.irq.complete.valid.hwclr);
    logic [COMPLETE_VALID_HWCLR_W-1:0] complete_valid_hwclr_reg;
    assign endpoint_if.core_to_csr.irq.complete.valid.hwclr = complete_valid_hwclr_reg;
    localparam int CONTROL_CLEAR_ERRORS_HWCLR_W =
        $bits(endpoint_if.core_to_csr.irq.control.clear_errors.hwclr);
    logic [CONTROL_CLEAR_ERRORS_HWCLR_W-1:0] control_clear_errors_hwclr_reg;
    assign endpoint_if.core_to_csr.irq.control.clear_errors.hwclr = control_clear_errors_hwclr_reg;
    localparam int STATUS_CLAIM_PENDING_W =
        $bits(endpoint_if.core_to_csr.irq.status.claim_pending.next);
    logic [STATUS_CLAIM_PENDING_W-1:0] status_claim_pending_reg;
    assign endpoint_if.core_to_csr.irq.status.claim_pending.next = status_claim_pending_reg;
    localparam int STATUS_CREDIT_FULL_W =
        $bits(endpoint_if.core_to_csr.irq.status.credit_full.next);
    logic [STATUS_CREDIT_FULL_W-1:0] status_credit_full_reg;
    assign endpoint_if.core_to_csr.irq.status.credit_full.next = status_credit_full_reg;
    localparam int STATUS_FIFO_LEVEL_W = $bits(endpoint_if.core_to_csr.irq.status.fifo_level.next);
    logic [STATUS_FIFO_LEVEL_W-1:0] status_fifo_level_reg;
    assign endpoint_if.core_to_csr.irq.status.fifo_level.next = status_fifo_level_reg;
    localparam int STATUS_INVALID_COMPLETE_W =
        $bits(endpoint_if.core_to_csr.irq.status.invalid_complete.next);
    logic [STATUS_INVALID_COMPLETE_W-1:0] status_invalid_complete_reg;
    assign endpoint_if.core_to_csr.irq.status.invalid_complete.next = status_invalid_complete_reg;
    localparam int STATUS_IRQ_ASSERTED_W =
        $bits(endpoint_if.core_to_csr.irq.status.irq_asserted.next);
    logic [STATUS_IRQ_ASSERTED_W-1:0] status_irq_asserted_reg;
    assign endpoint_if.core_to_csr.irq.status.irq_asserted.next = status_irq_asserted_reg;
    localparam int STATUS_OVERFLOW_W = $bits(endpoint_if.core_to_csr.irq.status.overflow.next);
    logic [STATUS_OVERFLOW_W-1:0] status_overflow_reg;
    assign endpoint_if.core_to_csr.irq.status.overflow.next = status_overflow_reg;
    localparam int STATUS_RESERVED_COUNT_W =
        $bits(endpoint_if.core_to_csr.irq.status.reserved_count.next);
    logic [STATUS_RESERVED_COUNT_W-1:0] status_reserved_count_reg;
    assign endpoint_if.core_to_csr.irq.status.reserved_count.next = status_reserved_count_reg;

    logic [EVENT_PORTS-1:0] admission_offer, admission_reservation;
    logic [PORT_INDEX_W-1:0] admission_cursor;
    wire completion_command = complete_valid && !complete_valid_hwclr_reg;
    wire completion_matches = claim_valid_reg
        && endpoint_if.csr_to_core.irq.complete.peer_idx.value
        == CSR_PEER_IDX_W '(claim_reg[0+:PEER_IDX_W])
        && endpoint_if.csr_to_core.irq.complete.source.value == claim_reg[PEER_IDX_W+:4]
        && endpoint_if.csr_to_core.irq.complete.sequence_.value
        == CSR_SEQUENCE_W'(claim_reg[PEER_IDX_W+4+:SEQUENCE_W]);
    wire queue_pop = completion_command && completion_matches;

    always_comb begin : select_admission
        logic enabled_found;
        int occupied;

        admission_offer = '0;
        admission_reservation = '0;
        admission_cursor = admission_cursor_reg;
        enabled_found = 1'b0;
        occupied = int'(fifo_count_reg) + int'(reserved_count_reg) - int'(queue_pop);
        for (int offset = 0; offset < EVENT_PORTS; offset++) begin
            int port;
            logic enabled;

            port = int'(admission_cursor_reg) + offset;
            if (port >= EVENT_PORTS) port -= EVENT_PORTS;
            enabled = admission_enable[port]
                && (SAMPLED_ENABLE_MASK[port]
                    || source_is_enabled(admission_source[port], event_enable));
            if (admission_state_reg == SELECT && admission_valid[port]
                && (!enabled || (!enabled_found && occupied < FIFO_DEPTH))) begin
                admission_offer[port] = 1'b1;
                admission_reservation[port] = enabled;
                if (enabled) begin
                    enabled_found = 1'b1;
                    admission_cursor = port == EVENT_PORTS - 1 ? '0 : PORT_INDEX_W'(port + 1);
                end
            end
        end
    end

    always_ff @(posedge clk) begin : admission_control
        if (rst) begin
            admission_state_reg <= SELECT;
            admission_ready_reg <= '0;
            admission_reserved_reg <= '0;
            admission_cursor_reg <= '0;
        end else begin
            case (admission_state_reg)
                SELECT: begin
                    admission_ready_reg <= admission_offer;
                    admission_reserved_reg <= admission_reservation;
                    admission_cursor_reg <= admission_cursor;
                    if (|admission_offer) admission_state_reg <= OFFER;
                end
                OFFER: begin
                    admission_ready_reg <= '0;
                    admission_reserved_reg <= '0;
                    admission_state_reg <= SELECT;
                end
            endcase
        end
    end

    always_ff @(posedge clk) begin : commit_control
        if (rst) begin
            commit_state_reg <= SELECT;
            commit_ready_reg <= '0;
            commit_cursor_reg <= '0;
        end else begin
            case (commit_state_reg)
                SELECT: begin
                    logic selected;

                    selected = 1'b0;
                    for (int offset = 0; offset < EVENT_PORTS; offset++) begin
                        int port;

                        port = int'(commit_cursor_reg) + offset;
                        if (port >= EVENT_PORTS) port -= EVENT_PORTS;
                        if (!selected && commit_valid[port]) begin
                            selected = 1'b1;
                            commit_ready_reg[port] <= 1'b1;
                            commit_cursor_reg <= port == EVENT_PORTS - 1 ? '0
                                : PORT_INDEX_W'(port + 1);
                            commit_state_reg <= OFFER;
                        end
                    end
                end
                OFFER: begin
                    commit_ready_reg <= '0;
                    commit_state_reg <= SELECT;
                end
            endcase
        end
    end

    always_ff @(posedge clk) begin : event_queue
        logic [FIFO_COUNT_W-1:0] queued, reserved;
        logic [QUEUE_INDEX_W-1:0] head, tail;
        logic [CLAIM_DATA_W-1:0] push_data, head_data;
        logic pushed;
        logic [QUEUE_INDEX_W-1:0] push_index;
        logic overflow_value, invalid_value;

        queued = fifo_count_reg;
        reserved = reserved_count_reg;
        head = head_reg;
        tail = tail_reg;
        pushed = 1'b0;
        push_data = '0;
        push_index = tail_reg;
        overflow_value = overflow_reg;
        invalid_value = invalid_complete_reg;
        control_clear_errors_hwclr_reg <= clear_errors;
        complete_valid_hwclr_reg <= complete_valid;
        if (clear_errors && !control_clear_errors_hwclr_reg) begin
            overflow_value = 1'b0;
            invalid_value = 1'b0;
        end
        if (queue_pop) begin
            queued = queued - 1'b1;
            head = head == QUEUE_INDEX_W'(FIFO_DEPTH - 1) ? '0 : head + 1'b1;
        end else if (completion_command) begin
            invalid_value = 1'b1;
        end
        for (int port = 0; port < EVENT_PORTS; port++) begin
            logic [FIFO_COUNT_W-1:0] port_credit;

            port_credit = port_reserved_count_reg[port];
            if (admission_reservation[port]) begin
                port_credit = port_credit + 1'b1;
                reserved = reserved + 1'b1;
            end
            if (admission_state_reg == OFFER && admission_ready_reg[port]
                && admission_reserved_reg[port] && !admission_valid[port]) begin
                port_credit = port_credit - 1'b1;
                reserved = reserved - 1'b1;
            end
            if (commit_state_reg == OFFER && commit_ready_reg[port] && commit_valid[port]) begin
                if (port_credit == 0 || queued == FIFO_COUNT_W'(FIFO_DEPTH)) begin
                    overflow_value = 1'b1;
                end else begin
                    pushed = 1'b1;
                    push_index = tail;
                    push_data = {
                        next_sequence_reg,
                        commit_source[port],
                        (commit_source[port] == EVENT_PEER_DMA_COMPLETE || commit_source[port] ==
                        EVENT_RMEM_ERROR) ? commit_peer_idx[port] : PEER_IDX_W'(0)
                    };
                    tail = tail == QUEUE_INDEX_W'(FIFO_DEPTH - 1) ? '0 : tail + 1'b1;
                    queued = queued + 1'b1;
                    reserved = reserved - 1'b1;
                    port_credit = port_credit - 1'b1;
                    next_sequence_reg <= next_sequence_reg + 1'b1;
                end
            end
            port_reserved_count_reg[port] <= port_credit;
        end
        fifo_count_reg <= queued;
        reserved_count_reg <= reserved;
        head_reg <= head;
        tail_reg <= tail;
        if (pushed) queue_reg[push_index] <= push_data;
        head_data = queued != 0 ? (pushed && push_index == head ? push_data : queue_reg[head]) : '0;
        overflow_reg <= overflow_value;
        invalid_complete_reg <= invalid_value;
        claim_valid_reg <= queued != 0;
        claim_reg <= head_data;
        claim_peer_idx_reg <= queued != 0 ? CSR_PEER_IDX_W'(head_data[0+:PEER_IDX_W]) : '0;
        claim_source_reg <= queued != 0 ? head_data[PEER_IDX_W+:4] : '0;
        claim_sequence_reg <= queued != 0 ? CSR_SEQUENCE_W'(head_data[PEER_IDX_W+4+:SEQUENCE_W])
            : '0;
        status_claim_pending_reg <= queued != 0;
        status_credit_full_reg <= int'(queued) + int'(reserved) >= FIFO_DEPTH;
        status_overflow_reg <= overflow_value;
        status_invalid_complete_reg <= invalid_value;
        status_fifo_level_reg <= int'(queued) > 255 ? 8'hff : 8'(queued);
        status_reserved_count_reg <= int'(reserved) > 255 ? 8'hff : 8'(reserved);
        irq <= global_enable && queued != 0;
        status_irq_asserted_reg <= global_enable && queued != 0;
        if (rst) begin
            fifo_count_reg <= '0;
            reserved_count_reg <= '0;
            head_reg <= '0;
            tail_reg <= '0;
            next_sequence_reg <= '0;
            overflow_reg <= 1'b0;
            invalid_complete_reg <= 1'b0;
            claim_valid_reg <= 1'b0;
            claim_reg <= '0;
            for (int port = 0; port < EVENT_PORTS; port++) begin
                port_reserved_count_reg[port] <= '0;
            end
            claim_valid_reg <= 1'b0;
            claim_peer_idx_reg <= '0;
            claim_source_reg <= '0;
            claim_sequence_reg <= '0;
            status_claim_pending_reg <= 1'b0;
            status_credit_full_reg <= 1'b0;
            status_overflow_reg <= 1'b0;
            status_invalid_complete_reg <= 1'b0;
            status_fifo_level_reg <= '0;
            status_reserved_count_reg <= '0;
            status_irq_asserted_reg <= 1'b0;
            control_clear_errors_hwclr_reg <= 1'b0;
            complete_valid_hwclr_reg <= 1'b0;
            irq <= 1'b0;
        end
    end
endmodule

`resetall
