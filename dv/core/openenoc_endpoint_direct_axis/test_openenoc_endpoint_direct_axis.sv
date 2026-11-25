// SPDX-FileCopyrightText: 2026 Kerim Bavcic
// SPDX-License-Identifier: AGPL-3.0-or-later

`resetall
`timescale 1ns / 1ps
`default_nettype none

/*
 * Direct endpoint AXI4-Stream testbench
 */
module test_openenoc_endpoint_direct_axis ();
    logic clk, rst, tx_frame_done;
    logic tx_valid, tx_last, tx_event_enable;
    logic [31:0] tx_data;
    logic [3:0] tx_keep;
    wire tx_clear_valid, tx_ready;
    logic rx_ready;
    wire rx_clear_ready, rx_valid, rx_last;
    wire [31:0] rx_data;
    wire [3:0] rx_keep;
    logic m_ready;
    wire m_valid, m_last;
    wire [31:0] m_data;
    wire [3:0] m_keep, m_strb;
    wire [5:0] m_dest;
    wire [0:0] m_id, m_user;
    logic s_valid, s_last;
    logic [31:0] s_data;
    logic [3:0] s_keep;
    wire s_ready;
    logic tx_admit_ready, tx_admit_reserved, tx_commit_ready;
    logic rx_admit_ready, rx_admit_reserved, rx_commit_ready;
    wire tx_admit_valid, tx_admit_enable, tx_commit_valid;
    wire rx_admit_valid, rx_admit_enable, rx_commit_valid;
    wire [3:0] tx_admit_source, tx_commit_source, rx_admit_source, rx_commit_source;
    wire [0:0] tx_commit_peer_idx, rx_commit_peer_idx;

    // Expose the CSR fields used by the direct path as cocotb signals.
    openenoc_endpoint_if endpoint_if (
        .clk(clk),
        .rst(rst)
    );
    always_comb begin
        endpoint_if.csr_to_core = '{default: '0};
        endpoint_if.csr_to_core.axis_if.source.data.tdata.value = tx_data;
        endpoint_if.csr_to_core.axis_if.source.control.tkeep.value = tx_keep;
        endpoint_if.csr_to_core.axis_if.source.control.tlast.value = tx_last;
        endpoint_if.csr_to_core.axis_if.source.control.tvalid.value = tx_valid;
        endpoint_if.csr_to_core.axis_if.sink.control.tready.value = rx_ready;
        endpoint_if.csr_to_core.irq.event_enable.non_oetp_direct_tx_complete.value =
            tx_event_enable;
    end
    assign tx_clear_valid = endpoint_if.core_to_csr.axis_if.source.control.tvalid.hwclr;
    assign tx_ready = endpoint_if.core_to_csr.axis_if.source.status.tready.next;
    assign rx_clear_ready = endpoint_if.core_to_csr.axis_if.sink.control.tready.hwclr;
    assign rx_valid = endpoint_if.core_to_csr.axis_if.sink.status.tvalid.next;
    assign rx_last = endpoint_if.core_to_csr.axis_if.sink.status.tlast.next;
    assign rx_keep = endpoint_if.core_to_csr.axis_if.sink.status.tkeep.next;
    assign rx_data = endpoint_if.core_to_csr.axis_if.sink.data.tdata.next;

    // The destination contains two route bits and four peer-index bits.
    taxi_axis_if #(
        .DATA_W(32),
        .KEEP_W(4),
        .DEST_EN(1'b1),
        .DEST_W(6),
        .ID_W(1),
        .USER_W(1)
    ) m_axis_csr_tx();
    taxi_axis_if #(
        .DATA_W(32),
        .KEEP_W(4),
        .DEST_EN(1'b1),
        .DEST_W(6),
        .ID_W(1),
        .USER_W(1)
    ) s_axis_csr_rx();
    assign m_axis_csr_tx.tready = m_ready;
    assign m_valid = m_axis_csr_tx.tvalid;
    assign m_last = m_axis_csr_tx.tlast;
    assign m_data = m_axis_csr_tx.tdata;
    assign m_keep = m_axis_csr_tx.tkeep;
    assign m_strb = m_axis_csr_tx.tstrb;
    assign m_dest = m_axis_csr_tx.tdest;
    assign m_id = m_axis_csr_tx.tid;
    assign m_user = m_axis_csr_tx.tuser;
    assign s_axis_csr_rx.tvalid = s_valid;
    assign s_axis_csr_rx.tlast = s_last;
    assign s_axis_csr_rx.tdata = s_data;
    assign s_axis_csr_rx.tkeep = s_keep;
    assign s_axis_csr_rx.tstrb = s_keep;
    assign s_axis_csr_rx.tid = '0;
    assign s_axis_csr_rx.tdest = '0;
    assign s_axis_csr_rx.tuser = '0;
    assign s_ready = s_axis_csr_rx.tready;

    // Cocotb supplies admission and commit responses in place of the IRQ controller.
    openenoc_irq_event_if tx_event_if();
    openenoc_irq_event_if rx_event_if();
    assign tx_event_if.admit_ready = tx_admit_ready;
    assign tx_event_if.admit_reserved = tx_admit_reserved;
    assign tx_event_if.commit_ready = tx_commit_ready;
    assign tx_admit_valid = tx_event_if.admit_valid;
    assign tx_admit_source = tx_event_if.admit_source;
    assign tx_admit_enable = tx_event_if.admit_enable;
    assign tx_commit_valid = tx_event_if.commit_valid;
    assign tx_commit_source = tx_event_if.commit_source;
    assign tx_commit_peer_idx = tx_event_if.commit_peer_idx;
    assign rx_event_if.admit_ready = rx_admit_ready;
    assign rx_event_if.admit_reserved = rx_admit_reserved;
    assign rx_event_if.commit_ready = rx_commit_ready;
    assign rx_admit_valid = rx_event_if.admit_valid;
    assign rx_admit_source = rx_event_if.admit_source;
    assign rx_admit_enable = rx_event_if.admit_enable;
    assign rx_commit_valid = rx_event_if.commit_valid;
    assign rx_commit_source = rx_event_if.commit_source;
    assign rx_commit_peer_idx = rx_event_if.commit_peer_idx;

    openenoc_endpoint_direct_axis #(
        .ROUTE_DIRECT(2'b10)
    )
    u_openenoc_endpoint_direct_axis (
        .clk(clk),
        .rst(rst),
        .tx_frame_done(tx_frame_done),
        .endpoint_if(endpoint_if),

        /*
         * AXI4-Stream output (TX) and input (RX)
         */
        .m_axis_csr_tx(m_axis_csr_tx),
        .s_axis_csr_rx(s_axis_csr_rx),

        /*
         * Interrupt event producers
         */
        .tx_event_if(tx_event_if),
        .rx_event_if(rx_event_if)
    );
endmodule

`resetall
