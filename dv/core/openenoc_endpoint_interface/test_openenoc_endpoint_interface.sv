// SPDX-FileCopyrightText: 2026 Enio Kaljic
// SPDX-License-Identifier: AGPL-3.0-or-later

`resetall
`timescale 1ns / 1ps
`default_nettype none

module test_openenoc_endpoint_interface #(
    parameter int AXI_DATA_W = 32,
    parameter int ETH_DATA_W = 32
) ();
    logic clk, rst;
    logic [31:0] tx_data;
    logic [3:0] tx_keep;
    logic tx_last, tx_valid, rx_ready;
    wire tx_hwclr, tx_ready, rx_valid, rx_last, rx_hwclr;
    wire [31:0] rx_data;
    wire [3:0] rx_keep;
    logic irq_enable;
    logic [5:0] event_enable;
    logic [31:0] complete;
    logic clear_errors;
    wire irq, claim_valid, credit_full, overflow, invalid_complete;
    wire [31:0] claim;
    wire [7:0] fifo_level, reserved_count;
    logic [31:0] non_tx_address, non_tx_length, non_rx_address, non_rx_capacity;
    logic non_tx_request, non_rx_request;
    wire non_tx_hwclr, non_tx_idle, non_tx_done, non_tx_error;
    wire non_rx_hwclr, non_rx_armed, non_rx_idle;
    logic [47:0] mac_address, multicast_address, peer_mac;
    logic [1:0] receive_mode;
    logic [31:0] dma_timeout_cycles, fragment_size, peer_rmem_offset;
    logic peer_clear_error;
    logic [47:0] peer1_mac;
    logic [31:0] peer1_local_addr, peer1_remote_addr, peer1_size, peer1_rmem_offset;
    logic [1:0] peer1_mode;
    logic local_wr_ack, local_rd_ack, local_wr_err, local_rd_err;
    logic [31:0] local_rd_data;
    wire local_req, local_req_is_wr;
    wire [31:0] local_addr, local_wr_data, local_wr_biten;
    logic [1:0] peer_mode;
    logic [31:0] peer_local_addr, peer_remote_addr, peer_size;
    logic peer_request, peer_irq_enable;
    wire peer_hwclr, peer_idle, peer_done, peer_error;
    wire [3:0] peer_error_code;
    logic rmem_req, rmem_req_is_wr;
    logic [9:0] rmem_addr;
    logic [31:0] rmem_wr_data, rmem_wr_biten, rmem_timeout_cycles;
    wire rmem_ack, rmem_wr_ack, rmem_master_active;
    wire [31:0] rmem_rd_data, oetp_rmem_timeout_cycles;
    wire dma_rmem_req;
    wire [31:0] dma_rmem_addr, dma_rmem_wr_data, dma_rmem_wr_biten;

    openenoc_endpoint_if #(
        .NUM_OF_PEERS(2),
        .RMEM_TOTAL_DEPTH(256)
    ) endpoint_if (
        .clk(clk),
        .rst(rst)
    );

    openenoc_eth_if #(
        .DATA_W(ETH_DATA_W)
    ) eth_if (
        .clk(clk),
        .rst(rst)
    );

    taxi_axi_if #(
        .DATA_W(AXI_DATA_W),
        .ADDR_W(32),
        .ID_W(8)
    ) m_axi_if();

    openenoc_cpuif_if #(
        .ADDR_W(32),
        .DATA_W(32)
    ) rmem_cpuif();

    assign rmem_cpuif.wr_ack = local_wr_ack;
    assign rmem_cpuif.wr_err = local_wr_err;
    assign rmem_cpuif.rd_ack = local_rd_ack;
    assign rmem_cpuif.rd_err = local_rd_err;
    assign rmem_cpuif.rd_data = local_rd_data;
    assign rmem_master_active = rmem_cpuif.req;
    assign local_req = rmem_cpuif.req;
    assign local_req_is_wr = rmem_cpuif.req_is_wr;
    assign local_addr = rmem_cpuif.addr;
    assign local_wr_data = rmem_cpuif.wr_data;
    assign local_wr_biten = rmem_cpuif.wr_biten;
    always_comb begin
        endpoint_if.csr_to_core = '{default: '0};
        endpoint_if.csr_to_core.config_.dma_max_fragment_size.bytes.value = fragment_size;
        endpoint_if.csr_to_core.config_.mac_address.lo_word.value = mac_address[31:0];
        endpoint_if.csr_to_core.config_.mac_address.hi_word.value = mac_address[47:32];
        endpoint_if.csr_to_core.config_.multicast_address.lo_word.value = multicast_address[31:0];
        endpoint_if.csr_to_core.config_.multicast_address.hi_word.value = multicast_address[47:32];
        endpoint_if.csr_to_core.config_.non_oetp_control.receive_mode.value = receive_mode;
        endpoint_if.csr_to_core.config_.dma_timeout.cycles.value = dma_timeout_cycles;
        endpoint_if.csr_to_core.config_.rmem_timeout.cycles.value = rmem_timeout_cycles;
        endpoint_if.csr_to_core.axis_if.source.data.tdata.value = tx_data;
        endpoint_if.csr_to_core.axis_if.source.control.tkeep.value = tx_keep;
        endpoint_if.csr_to_core.axis_if.source.control.tlast.value = tx_last;
        endpoint_if.csr_to_core.axis_if.source.control.tvalid.value = tx_valid;
        endpoint_if.csr_to_core.axis_if.sink.control.tready.value = rx_ready;
        endpoint_if.csr_to_core.irq.control.global_enable.value = irq_enable;
        endpoint_if.csr_to_core.irq.control.clear_errors.value = clear_errors;
        endpoint_if.csr_to_core.irq.event_enable.rmem_error.value = event_enable[5];
        endpoint_if.csr_to_core.irq.event_enable.peer_dma_complete.value = event_enable[0];
        endpoint_if.csr_to_core.irq.event_enable.non_oetp_dma_tx_complete.value = event_enable[1];
        endpoint_if.csr_to_core.irq.event_enable.non_oetp_dma_rx_complete.value = event_enable[2];
        endpoint_if.csr_to_core.irq.event_enable.non_oetp_direct_tx_complete.value =
            event_enable[3];
        endpoint_if.csr_to_core.irq.event_enable.non_oetp_direct_rx_available.value =
            event_enable[4];
        endpoint_if.csr_to_core.irq.complete.peer_idx.value = complete[10:0];
        endpoint_if.csr_to_core.irq.complete.source.value = complete[14:11];
        endpoint_if.csr_to_core.irq.complete.sequence_.value = complete[30:15];
        endpoint_if.csr_to_core.irq.complete.valid.value = complete[31];
        endpoint_if.csr_to_core.non_oetp_dma.tx.buffer_address.base.value = non_tx_address;
        endpoint_if.csr_to_core.non_oetp_dma.tx.frame_length.bytes.value = non_tx_length;
        endpoint_if.csr_to_core.non_oetp_dma.tx.command_status.request.value = non_tx_request;
        endpoint_if.csr_to_core.non_oetp_dma.rx.buffer_address.base.value = non_rx_address;
        endpoint_if.csr_to_core.non_oetp_dma.rx.buffer_capacity.bytes.value = non_rx_capacity;
        endpoint_if.csr_to_core.non_oetp_dma.rx.command_status.request.value = non_rx_request;
        endpoint_if.csr_to_core.peers.entry[0].mac_address.lo_word.value = peer_mac[31:0];
        endpoint_if.csr_to_core.peers.entry[0].mac_address.hi_word.value = peer_mac[47:32];
        endpoint_if.csr_to_core.peers.entry[0].rmem_address.offset.value = peer_rmem_offset;
        endpoint_if.csr_to_core.peers.entry[0].dma.clear_error.value = peer_clear_error;
        endpoint_if.csr_to_core.peers.entry[0].dma.mode.value = peer_mode;
        endpoint_if.csr_to_core.peers.entry[0].dma.irq_enable.value = peer_irq_enable;
        endpoint_if.csr_to_core.peers.entry[0].dma.request.value = peer_request;
        endpoint_if.csr_to_core.peers.entry[0].local_address.base.value = peer_local_addr;
        endpoint_if.csr_to_core.peers.entry[0].remote_address.base.value = peer_remote_addr;
        endpoint_if.csr_to_core.peers.entry[0].size.bytes.value = peer_size;
        endpoint_if.csr_to_core.peers.entry[1].mac_address.lo_word.value = peer1_mac[31:0];
        endpoint_if.csr_to_core.peers.entry[1].mac_address.hi_word.value = peer1_mac[47:32];
        endpoint_if.csr_to_core.peers.entry[1].dma.mode.value = peer1_mode;
        endpoint_if.csr_to_core.peers.entry[1].local_address.base.value = peer1_local_addr;
        endpoint_if.csr_to_core.peers.entry[1].remote_address.base.value = peer1_remote_addr;
        endpoint_if.csr_to_core.peers.entry[1].size.bytes.value = peer1_size;
        endpoint_if.csr_to_core.peers.entry[1].rmem_address.offset.value = peer1_rmem_offset;
        endpoint_if.csr_to_core.rmem.req = rmem_req;
        endpoint_if.csr_to_core.rmem.addr = rmem_addr;
        endpoint_if.csr_to_core.rmem.req_is_wr = rmem_req_is_wr;
        endpoint_if.csr_to_core.rmem.wr_data = rmem_wr_data;
        endpoint_if.csr_to_core.rmem.wr_biten = rmem_wr_biten;
    end
    assign tx_hwclr = endpoint_if.core_to_csr.axis_if.source.control.tvalid.hwclr;
    assign tx_ready = endpoint_if.core_to_csr.axis_if.source.status.tready.next;
    assign rx_valid = endpoint_if.core_to_csr.axis_if.sink.status.tvalid.next;
    assign rx_last = endpoint_if.core_to_csr.axis_if.sink.status.tlast.next;
    assign rx_keep = endpoint_if.core_to_csr.axis_if.sink.status.tkeep.next;
    assign rx_data = endpoint_if.core_to_csr.axis_if.sink.data.tdata.next;
    assign rx_hwclr = endpoint_if.core_to_csr.axis_if.sink.control.tready.hwclr;
    assign claim_valid = endpoint_if.core_to_csr.irq.claim.valid.next;
    assign credit_full = endpoint_if.core_to_csr.irq.status.credit_full.next;
    assign overflow = endpoint_if.core_to_csr.irq.status.overflow.next;
    assign invalid_complete = endpoint_if.core_to_csr.irq.status.invalid_complete.next;
    assign fifo_level = endpoint_if.core_to_csr.irq.status.fifo_level.next;
    assign reserved_count = endpoint_if.core_to_csr.irq.status.reserved_count.next;
    assign non_tx_hwclr = endpoint_if.core_to_csr.non_oetp_dma.tx.command_status.request.hwclr;
    assign non_tx_idle = endpoint_if.core_to_csr.non_oetp_dma.tx.command_status.idle.next;
    assign non_tx_done = endpoint_if.core_to_csr.non_oetp_dma.tx.command_status.done.next;
    assign non_tx_error = endpoint_if.core_to_csr.non_oetp_dma.tx.command_status.error.next;
    assign non_rx_hwclr = endpoint_if.core_to_csr.non_oetp_dma.rx.command_status.request.hwclr;
    assign non_rx_armed = endpoint_if.core_to_csr.non_oetp_dma.rx.command_status.armed.next;
    assign non_rx_idle = endpoint_if.core_to_csr.non_oetp_dma.rx.command_status.idle.next;
    assign peer_hwclr = endpoint_if.core_to_csr.peers.entry[0].dma.request.hwclr;
    assign peer_idle = endpoint_if.core_to_csr.peers.entry[0].dma.idle.next;
    assign peer_done = endpoint_if.core_to_csr.peers.entry[0].dma.done.next;
    assign peer_error = endpoint_if.core_to_csr.peers.entry[0].dma.error.next;
    assign peer_error_code = endpoint_if.core_to_csr.peers.entry[0].dma.error_code.next;
    assign rmem_ack = endpoint_if.core_to_csr.rmem.rd_ack;
    assign rmem_wr_ack = endpoint_if.core_to_csr.rmem.wr_ack;
    assign rmem_rd_data = endpoint_if.core_to_csr.rmem.rd_data;
    assign oetp_rmem_timeout_cycles = u_endpoint_interface.u_oetp_engine.rmem_timeout_cycles;
    assign dma_rmem_req = u_endpoint_interface.u_dma_engine.rmem_cpuif.req;
    assign dma_rmem_addr = u_endpoint_interface.u_dma_engine.rmem_cpuif.addr;
    assign dma_rmem_wr_data = u_endpoint_interface.u_dma_engine.rmem_cpuif.wr_data;
    assign dma_rmem_wr_biten = u_endpoint_interface.u_dma_engine.rmem_cpuif.wr_biten;
    assign claim = {
        endpoint_if.core_to_csr.irq.claim.valid.next,
        endpoint_if.core_to_csr.irq.claim.sequence_.next,
        endpoint_if.core_to_csr.irq.claim.source.next,
        endpoint_if.core_to_csr.irq.claim.peer_idx.next
    };

    openenoc_endpoint_interface #(
        .FIFO_DEPTH(128),
        .IRQ_FIFO_DEPTH(2),
        .MAX_RAW_FRAME_SIZE(64),
        .FRAGMENT_SLOTS(4)
    ) u_endpoint_interface (
        .clk(clk),
        .rst(rst),
        .endpoint_if(endpoint_if),
        .eth_if(eth_if),
        .m_axi_wr(m_axi_if),
        .m_axi_rd(m_axi_if),
        .m_rmem_cpuif(rmem_cpuif),
        .irq(irq)
    );

endmodule

`resetall
