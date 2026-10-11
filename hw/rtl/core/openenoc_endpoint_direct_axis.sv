// SPDX-FileCopyrightText: 2026 Enio Kaljic
// SPDX-License-Identifier: CERN-OHL-S-2.0

`resetall
`timescale 1ns / 1ps
`default_nettype none

/* Direct CSR stream handshakes and IRQ events. */
module openenoc_endpoint_direct_axis (
    input wire logic clk,
    input wire logic rst,
    input wire logic tx_frame_done,
    openenoc_endpoint_if.core endpoint_if,
    taxi_axis_if.src m_axis_csr_tx,
    taxi_axis_if.snk s_axis_csr_rx,
    openenoc_irq_event_if.producer tx_event_if,
    openenoc_irq_event_if.producer rx_event_if
);

    taxi_axis_if #(
        .DATA_W(m_axis_csr_tx.DATA_W),
        .KEEP_W(m_axis_csr_tx.KEEP_W),
        .KEEP_EN(m_axis_csr_tx.KEEP_EN),
        .STRB_EN(m_axis_csr_tx.STRB_EN),
        .LAST_EN(m_axis_csr_tx.LAST_EN),
        .ID_EN(m_axis_csr_tx.ID_EN),
        .ID_W(m_axis_csr_tx.ID_W),
        .DEST_EN(m_axis_csr_tx.DEST_EN),
        .DEST_W(m_axis_csr_tx.DEST_W),
        .USER_EN(m_axis_csr_tx.USER_EN),
        .USER_W(m_axis_csr_tx.USER_W)
    ) tx_payload_if();

    taxi_axis_if #(
        .DATA_W(s_axis_csr_rx.DATA_W),
        .KEEP_W(s_axis_csr_rx.KEEP_W),
        .KEEP_EN(s_axis_csr_rx.KEEP_EN),
        .STRB_EN(s_axis_csr_rx.STRB_EN),
        .LAST_EN(s_axis_csr_rx.LAST_EN),
        .ID_EN(s_axis_csr_rx.ID_EN),
        .ID_W(s_axis_csr_rx.ID_W),
        .DEST_EN(s_axis_csr_rx.DEST_EN),
        .DEST_W(s_axis_csr_rx.DEST_W),
        .USER_EN(s_axis_csr_rx.USER_EN),
        .USER_W(s_axis_csr_rx.USER_W)
    ) rx_payload_if();

    taxi_axis_if #(
        .DATA_W(m_axis_csr_tx.DATA_W),
        .KEEP_W(m_axis_csr_tx.KEEP_W),
        .KEEP_EN(m_axis_csr_tx.KEEP_EN),
        .STRB_EN(m_axis_csr_tx.STRB_EN),
        .LAST_EN(m_axis_csr_tx.LAST_EN),
        .ID_EN(m_axis_csr_tx.ID_EN),
        .ID_W(m_axis_csr_tx.ID_W),
        .DEST_EN(m_axis_csr_tx.DEST_EN),
        .DEST_W(m_axis_csr_tx.DEST_W),
        .USER_EN(m_axis_csr_tx.USER_EN),
        .USER_W(m_axis_csr_tx.USER_W)
    ) tx_registered_if();

    taxi_axis_register #(
        .REG_TYPE(2)
    ) tx_output_register (
        .clk(clk),
        .rst(rst),
        .s_axis(tx_payload_if),
        .m_axis(tx_registered_if)
    );

    taxi_axis_register #(
        .REG_TYPE(2)
    ) rx_input_register (
        .clk(clk),
        .rst(rst),
        .s_axis(s_axis_csr_rx),
        .m_axis(rx_payload_if)
    );

    assign m_axis_csr_tx.tdata = tx_registered_if.tdata;
    assign m_axis_csr_tx.tkeep = tx_registered_if.tkeep;
    assign m_axis_csr_tx.tstrb = m_axis_csr_tx.STRB_EN ? tx_registered_if.tstrb
        : tx_registered_if.tkeep;
    assign m_axis_csr_tx.tvalid = tx_registered_if.tvalid;
    assign m_axis_csr_tx.tlast = tx_registered_if.tlast;
    assign m_axis_csr_tx.tid = tx_registered_if.tid;
    assign m_axis_csr_tx.tdest = tx_registered_if.tdest;
    assign m_axis_csr_tx.tuser = tx_registered_if.tuser;
    assign tx_registered_if.tready = m_axis_csr_tx.tready;

    localparam int PEER_IDX_W = m_axis_csr_tx.DEST_W - 2;
    logic tx_active_reg, tx_input_done_reg, tx_reserved_reg, tx_commit_reg;
    logic tx_beat_pending_reg, tx_admit_valid_reg;
    logic rx_frame_reg, rx_commit_reg, rx_admit_valid_reg;
    logic rx_beat_pending_reg;
    logic tx_clear_valid_reg, tx_ready_reg;
    logic [31:0] rx_data_reg;
    logic [3:0] rx_keep_reg;
    logic rx_clear_ready_reg, rx_valid_reg, rx_last_reg;

    wire tx_csr_valid = endpoint_if.csr_to_core.axis_if.source.control.tvalid.value;
    wire rx_csr_ready = endpoint_if.csr_to_core.axis_if.sink.control.tready.value;
    wire rx_visible = rx_payload_if.tvalid && !rx_beat_pending_reg
        && (rx_frame_reg || (!rx_commit_reg && rx_event_if.admit_ready));
    wire tx_input_fire = tx_payload_if.tvalid && tx_payload_if.tready;
    wire rx_input_fire = rx_payload_if.tvalid && rx_payload_if.tready;

    assign tx_event_if.admit_valid = tx_admit_valid_reg;
    assign tx_event_if.admit_source = tx_event_if.EVENT_NON_OETP_DIRECT_TX_COMPLETE;
    assign tx_event_if.admit_enable = 1'b1;
    assign tx_event_if.commit_valid = tx_commit_reg;
    assign tx_event_if.commit_source = tx_event_if.EVENT_NON_OETP_DIRECT_TX_COMPLETE;
    assign tx_event_if.commit_peer_idx = '0;
    assign rx_event_if.admit_valid = rx_admit_valid_reg;
    assign rx_event_if.admit_source = rx_event_if.EVENT_NON_OETP_DIRECT_RX_AVAILABLE;
    assign rx_event_if.admit_enable = 1'b1;
    assign rx_event_if.commit_valid = rx_commit_reg;
    assign rx_event_if.commit_source = rx_event_if.EVENT_NON_OETP_DIRECT_RX_AVAILABLE;
    assign rx_event_if.commit_peer_idx = '0;

    assign tx_payload_if.tdata = endpoint_if.csr_to_core.axis_if.source.data.tdata.value;
    assign tx_payload_if.tkeep = endpoint_if.csr_to_core.axis_if.source.control.tkeep.value;
    assign tx_payload_if.tstrb = tx_payload_if.tkeep;
    assign tx_payload_if.tlast = endpoint_if.csr_to_core.axis_if.source.control.tlast.value;
    assign tx_payload_if.tvalid = tx_active_reg && !tx_input_done_reg && !tx_beat_pending_reg
        && tx_csr_valid;
    assign tx_payload_if.tid = '0;
    assign tx_payload_if.tdest = {2'b10, {PEER_IDX_W{1'b0}}};
    assign tx_payload_if.tuser = '0;
    assign rx_payload_if.tready = rx_visible && rx_csr_ready;

    assign endpoint_if.core_to_csr.axis_if.source.control.tvalid.hwclr = tx_clear_valid_reg;
    assign endpoint_if.core_to_csr.axis_if.source.status.tready.next = tx_ready_reg;
    assign endpoint_if.core_to_csr.axis_if.sink.data.tdata.next = rx_data_reg;
    assign endpoint_if.core_to_csr.axis_if.sink.control.tready.hwclr = rx_clear_ready_reg;
    assign endpoint_if.core_to_csr.axis_if.sink.status.tvalid.next = rx_valid_reg;
    assign endpoint_if.core_to_csr.axis_if.sink.status.tlast.next = rx_last_reg;
    assign endpoint_if.core_to_csr.axis_if.sink.status.tkeep.next = rx_keep_reg;

    always_ff @(posedge clk) begin : transmit_control
        if (rst) begin
            tx_active_reg <= 1'b0;
            tx_input_done_reg <= 1'b0;
            tx_reserved_reg <= 1'b0;
            tx_commit_reg <= 1'b0;
            tx_admit_valid_reg <= 1'b0;
            tx_beat_pending_reg <= 1'b0;
            tx_clear_valid_reg <= 1'b0;
            tx_ready_reg <= 1'b0;
        end else begin
            tx_admit_valid_reg <= !tx_active_reg && tx_csr_valid
                && !(tx_event_if.admit_valid && tx_event_if.admit_ready);
            tx_clear_valid_reg <= tx_input_fire;
            tx_ready_reg <= tx_active_reg && !tx_input_done_reg && !tx_beat_pending_reg
                && tx_payload_if.tready;

            if (!tx_csr_valid) begin
                tx_beat_pending_reg <= 1'b0;
            end

            if (tx_input_fire) begin
                tx_beat_pending_reg <= 1'b1;
                tx_ready_reg <= 1'b0;
                if (tx_payload_if.tlast) begin
                    tx_input_done_reg <= 1'b1;
                end
            end

            if (tx_event_if.admit_valid && tx_event_if.admit_ready) begin
                tx_active_reg <= 1'b1;
                tx_input_done_reg <= 1'b0;
                tx_reserved_reg <= tx_event_if.admit_reserved;
            end

            if (tx_frame_done) begin
                if (tx_reserved_reg) begin
                    tx_commit_reg <= 1'b1;
                end else begin
                    tx_active_reg <= 1'b0;
                    tx_input_done_reg <= 1'b0;
                end
            end

            if (tx_event_if.commit_valid && tx_event_if.commit_ready) begin
                tx_commit_reg <= 1'b0;
                tx_reserved_reg <= 1'b0;
                tx_active_reg <= 1'b0;
                tx_input_done_reg <= 1'b0;
            end
        end
    end

    always_ff @(posedge clk) begin : receive_control
        if (rst) begin
            rx_frame_reg <= 1'b0;
            rx_commit_reg <= 1'b0;
            rx_admit_valid_reg <= 1'b0;
            rx_beat_pending_reg <= 1'b0;
            rx_clear_ready_reg <= 1'b0;
            rx_valid_reg <= 1'b0;
            rx_last_reg <= 1'b0;
            rx_keep_reg <= '0;
            rx_data_reg <= '0;
        end else begin
            rx_admit_valid_reg <= !rx_frame_reg && !rx_commit_reg && rx_payload_if.tvalid
                && !(rx_event_if.admit_valid && rx_event_if.admit_ready);
            rx_clear_ready_reg <= rx_input_fire;
            rx_valid_reg <= rx_visible;
            rx_last_reg <= rx_payload_if.tlast;
            rx_keep_reg <= rx_payload_if.tkeep;
            rx_data_reg <= rx_payload_if.tdata;

            if (!rx_csr_ready) begin
                rx_beat_pending_reg <= 1'b0;
            end

            if (rx_input_fire) begin
                rx_beat_pending_reg <= 1'b1;
                rx_valid_reg <= 1'b0;
                if (rx_payload_if.tlast) begin
                    rx_frame_reg <= 1'b0;
                end
            end

            if (rx_event_if.admit_valid && rx_event_if.admit_ready) begin
                rx_frame_reg <= 1'b1;
                rx_commit_reg <= rx_event_if.admit_reserved;
            end

            if (rx_event_if.commit_valid && rx_event_if.commit_ready) begin
                rx_commit_reg <= 1'b0;
            end
        end
    end
endmodule

`resetall
