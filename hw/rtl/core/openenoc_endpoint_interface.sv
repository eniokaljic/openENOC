// SPDX-FileCopyrightText: 2026 Enio Kaljic
// SPDX-License-Identifier: CERN-OHL-S-2.0

`resetall
`timescale 1ns / 1ps
`default_nettype none

/* Single-clock endpoint integration, with field ownership in each submodule. */
module openenoc_endpoint_interface #(
    parameter int FIFO_DEPTH = 16384,
    parameter int FIFO_RAM_PIPELINE = 1,
    parameter int IRQ_FIFO_DEPTH = 16,
    parameter int MAX_RAW_FRAME_SIZE = 8192,
    parameter int FRAGMENT_SLOTS = 16
) (
    input wire logic clk,
    input wire logic rst,
    openenoc_endpoint_if.core endpoint_if,
    openenoc_eth_if eth_if,
    taxi_axi_if.wr_mst m_axi_wr,
    taxi_axi_if.rd_mst m_axi_rd,
    openenoc_cpuif_if.mst m_rmem_cpuif,
    output wire logic irq
);
    localparam int NUM_OF_PEERS = endpoint_if.NUM_OF_PEERS;
    localparam int PEER_IDX_W = NUM_OF_PEERS > 1 ? $clog2(NUM_OF_PEERS) : 1;
    localparam int AXIS_DEST_W = PEER_IDX_W + 2;
    localparam int DATA_W = m_axi_rd.DATA_W;
    localparam int SEQUENCE_W = 32;
    localparam int IRQ_PEER_IDX_W = 11;

    if (FIFO_DEPTH < MAX_RAW_FRAME_SIZE) begin : g_fifo_depth_error
        $fatal(0, {"Error: endpoint FIFO must hold the largest DMA ", "frame (instance %m)"});
    end
    if (NUM_OF_PEERS > 2047) begin : g_peer_count_error
        $fatal(0, {"Error: peer count exceeds the CSR index width ", "(instance %m)"});
    end

    openenoc_peer_lookup_if #(
        .NUM_OF_PEERS(NUM_OF_PEERS),
        .PEER_IDX_W(PEER_IDX_W),
        .ADDR_W(32)
    ) peer_lookup_if[2]();

    openenoc_dma_transfer_if #(
        .ADDR_W(32),
        .LEN_W(32),
        .PEER_IDX_W(PEER_IDX_W),
        .SEQUENCE_W(SEQUENCE_W)
    ) initiator_if(), responder_if();

    localparam int AXIS_USER_W = initiator_if.AXIS_USER_W;

    openenoc_irq_event_if #(
        .PEER_IDX_W(IRQ_PEER_IDX_W)
    ) irq_event_if[7]();

    taxi_axis_if #(
        .DATA_W(32),
        .KEEP_EN(1'b1),
        .LAST_EN(1'b1),
        .ID_EN(1'b1),
        .ID_W(SEQUENCE_W),
        .DEST_EN(1'b1),
        .DEST_W(AXIS_DEST_W),
        .USER_EN(1'b1),
        .USER_W(AXIS_USER_W)
    ) csr_source_axis_if();

    taxi_axis_if #(
        .DATA_W(32),
        .KEEP_EN(1'b1),
        .LAST_EN(1'b1),
        .ID_EN(1'b1),
        .ID_W(SEQUENCE_W),
        .DEST_EN(1'b1),
        .DEST_W(AXIS_DEST_W),
        .USER_EN(1'b1),
        .USER_W(AXIS_USER_W)
    ) csr_sink_axis_if();

    taxi_axis_if #(
        .DATA_W(DATA_W),
        .KEEP_EN(1'b1),
        .LAST_EN(1'b1),
        .ID_EN(1'b1),
        .ID_W(SEQUENCE_W),
        .DEST_EN(1'b1),
        .DEST_W(AXIS_DEST_W),
        .USER_EN(1'b1),
        .USER_W(AXIS_USER_W)
    ) dma_tx_axis_if(), dma_rx_axis_if(), oetp_tx_axis_if(), oetp_rx_axis_if();

    taxi_axis_if #(
        .DATA_W(DATA_W),
        .KEEP_EN(1'b1),
        .LAST_EN(1'b1),
        .ID_EN(1'b1),
        .ID_W(SEQUENCE_W),
        .DEST_EN(1'b1),
        .DEST_W(AXIS_DEST_W),
        .USER_EN(1'b1),
        .USER_W(AXIS_USER_W)
    ) tx_axis_if[2]();

    taxi_axis_if #(
        .DATA_W(DATA_W),
        .KEEP_EN(1'b1),
        .LAST_EN(1'b1),
        .ID_EN(1'b1),
        .ID_W(SEQUENCE_W),
        .DEST_EN(1'b1),
        .DEST_W(AXIS_DEST_W),
        .USER_EN(1'b1),
        .USER_W(AXIS_USER_W)
    ) rx_axis_if[2]();

    taxi_axis_if #(
        .DATA_W(eth_if.DATA_W),
        .KEEP_W(eth_if.KEEP_W),
        .KEEP_EN(eth_if.KEEP_EN),
        .LAST_EN(1'b1)
    ) eth_source_axis_if(), eth_sink_axis_if();

    assign eth_if.a2b_axis_if.tdata = eth_source_axis_if.tdata;
    assign eth_if.a2b_axis_if.tkeep = eth_source_axis_if.tkeep;
    assign eth_if.a2b_axis_if.tstrb = eth_source_axis_if.tstrb;
    assign eth_if.a2b_axis_if.tlast = eth_source_axis_if.tlast;
    assign eth_if.a2b_axis_if.tvalid = eth_source_axis_if.tvalid;
    assign eth_if.a2b_axis_if.tid = '0;
    assign eth_if.a2b_axis_if.tdest = '0;
    assign eth_if.a2b_axis_if.tuser = '0;
    assign eth_source_axis_if.tready = eth_if.a2b_axis_if.tready;
    assign eth_sink_axis_if.tdata = eth_if.b2a_axis_if.tdata;
    assign eth_sink_axis_if.tkeep = eth_if.b2a_axis_if.tkeep;
    assign eth_sink_axis_if.tstrb = eth_if.b2a_axis_if.tstrb;
    assign eth_sink_axis_if.tlast = eth_if.b2a_axis_if.tlast;
    assign eth_sink_axis_if.tvalid = eth_if.b2a_axis_if.tvalid;
    assign eth_sink_axis_if.tid = '0;
    assign eth_sink_axis_if.tdest = '0;
    assign eth_sink_axis_if.tuser = '0;
    assign eth_if.b2a_axis_if.tready = eth_sink_axis_if.tready;

    openenoc_endpoint_peer_lookup #(
        .LOOKUP_PORTS(2),
        .NUM_OF_PEERS(NUM_OF_PEERS),
        .PEER_IDX_W(PEER_IDX_W)
    ) u_peer_lookup (
        .clk(clk),
        .rst(rst),
        .endpoint_if(endpoint_if),
        .lookup_if(peer_lookup_if)
    );

    openenoc_endpoint_dma_engine #(
        .NUM_OF_PEERS(NUM_OF_PEERS),
        .PEER_IDX_W(PEER_IDX_W),
        .MAX_RAW_FRAME_SIZE(MAX_RAW_FRAME_SIZE),
        .FRAGMENT_SLOTS(FRAGMENT_SLOTS)
    ) u_dma_engine (
        .clk(clk),
        .rst(rst),
        .endpoint_if(endpoint_if),
        .peer_lookup_if(peer_lookup_if[0]),
        .initiator_if(initiator_if),
        .responder_if(responder_if),
        .m_axis_oetp(dma_tx_axis_if),
        .s_axis_oetp(dma_rx_axis_if),
        .m_axi_wr(m_axi_wr),
        .m_axi_rd(m_axi_rd),
        .m_local_cpuif(m_rmem_cpuif),
        .irq_event_if(irq_event_if[0:2]),
        .rmem_irq_event_if(irq_event_if[5]),
        .responder_irq_event_if(irq_event_if[6])
    );

    openenoc_endpoint_oetp_engine #(
        .MAX_RAW_FRAME_SIZE(MAX_RAW_FRAME_SIZE)
    ) u_oetp_engine (
        .clk(clk),
        .rst(rst),
        .endpoint_if(endpoint_if),
        .s_axis_local(oetp_tx_axis_if),
        .m_axis_local(oetp_rx_axis_if),
        .s_axis_eth(eth_sink_axis_if),
        .m_axis_eth(eth_source_axis_if),
        .peer_lookup_if(peer_lookup_if[1]),
        .initiator_if(initiator_if),
        .responder_if(responder_if)
    );

    // TX completion is measured at the oETP input, after FIFO and mux pipelines.
    wire direct_tx_done = oetp_tx_axis_if.tvalid && oetp_tx_axis_if.tready && oetp_tx_axis_if.tlast
        && oetp_tx_axis_if.tdest[PEER_IDX_W+:2] == initiator_if.ROUTE_DIRECT;

    openenoc_endpoint_direct_axis u_direct_axis (
        .clk(clk),
        .rst(rst),
        .tx_frame_done(direct_tx_done),
        .endpoint_if(endpoint_if),
        .m_axis_csr_tx(csr_source_axis_if),
        .s_axis_csr_rx(csr_sink_axis_if),
        .tx_event_if(irq_event_if[3]),
        .rx_event_if(irq_event_if[4])
    );

    taxi_axis_fifo_adapter #(
        .DEPTH(FIFO_DEPTH),
        .RAM_PIPELINE(FIFO_RAM_PIPELINE),
        .FRAME_FIFO(1'b0),
        .DROP_OVERSIZE_FRAME(1'b0),
        .DROP_BAD_FRAME(1'b0),
        .DROP_WHEN_FULL(1'b0),
        .MARK_WHEN_FULL(1'b0)
    ) u_direct_tx_fifo (
        .clk(clk),
        .rst(rst),
        .s_axis(csr_source_axis_if),
        .m_axis(tx_axis_if[0]),
        .pause_req(1'b0),
        .pause_ack(),
        .status_depth(),
        .status_depth_commit(),
        .status_overflow(),
        .status_bad_frame(),
        .status_good_frame()
    );

    taxi_axis_fifo_adapter #(
        .DEPTH(FIFO_DEPTH),
        .RAM_PIPELINE(FIFO_RAM_PIPELINE),
        .FRAME_FIFO(1'b0),
        .DROP_OVERSIZE_FRAME(1'b0),
        .DROP_BAD_FRAME(1'b0),
        .DROP_WHEN_FULL(1'b0),
        .MARK_WHEN_FULL(1'b0)
    ) u_dma_tx_fifo (
        .clk(clk),
        .rst(rst),
        .s_axis(dma_tx_axis_if),
        .m_axis(tx_axis_if[1]),
        .pause_req(1'b0),
        .pause_ack(),
        .status_depth(),
        .status_depth_commit(),
        .status_overflow(),
        .status_bad_frame(),
        .status_good_frame()
    );

    taxi_axis_fifo_adapter #(
        .DEPTH(FIFO_DEPTH),
        .RAM_PIPELINE(FIFO_RAM_PIPELINE),
        .FRAME_FIFO(1'b0),
        .DROP_OVERSIZE_FRAME(1'b0),
        .DROP_BAD_FRAME(1'b0),
        .DROP_WHEN_FULL(1'b0),
        .MARK_WHEN_FULL(1'b0)
    ) u_dma_rx_fifo (
        .clk(clk),
        .rst(rst),
        .s_axis(rx_axis_if[0]),
        .m_axis(dma_rx_axis_if),
        .pause_req(1'b0),
        .pause_ack(),
        .status_depth(),
        .status_depth_commit(),
        .status_overflow(),
        .status_bad_frame(),
        .status_good_frame()
    );

    taxi_axis_fifo_adapter #(
        .DEPTH(FIFO_DEPTH),
        .RAM_PIPELINE(FIFO_RAM_PIPELINE),
        .FRAME_FIFO(1'b0),
        .DROP_OVERSIZE_FRAME(1'b0),
        .DROP_BAD_FRAME(1'b0),
        .DROP_WHEN_FULL(1'b0),
        .MARK_WHEN_FULL(1'b0)
    ) u_direct_rx_fifo (
        .clk(clk),
        .rst(rst),
        .s_axis(rx_axis_if[1]),
        .m_axis(csr_sink_axis_if),
        .pause_req(1'b0),
        .pause_ack(),
        .status_depth(),
        .status_depth_commit(),
        .status_overflow(),
        .status_bad_frame(),
        .status_good_frame()
    );

    taxi_axis_arb_mux #(
        .S_COUNT(2),
        .UPDATE_TID(1'b0),
        .ARB_ROUND_ROBIN(1'b1),
        .ARB_LSB_HIGH_PRIO(1'b1)
    ) u_tx_mux (
        .clk(clk),
        .rst(rst),
        .s_axis(tx_axis_if),
        .m_axis(oetp_tx_axis_if)
    );

    taxi_axis_demux #(
        .M_COUNT(2),
        .TDEST_ROUTE(1'b0)
    ) u_rx_demux (
        .clk(clk),
        .rst(rst),
        .s_axis(oetp_rx_axis_if),
        .m_axis(rx_axis_if),
        .enable(1'b1),
        .drop(oetp_rx_axis_if.tdest[PEER_IDX_W+:2] == initiator_if.ROUTE_DROP),
        .select(oetp_rx_axis_if.tdest[PEER_IDX_W+:2] == initiator_if.ROUTE_DIRECT)
    );

    openenoc_endpoint_irq_controller #(
        .EVENT_PORTS(7),
        .FIFO_DEPTH(IRQ_FIFO_DEPTH),
        .PEER_IDX_W(IRQ_PEER_IDX_W),
        .SEQUENCE_W(16),
        .SAMPLED_ENABLE_MASK(7'b0100000)
    ) u_irq_controller (
        .clk(clk),
        .rst(rst),
        .endpoint_if(endpoint_if),
        .irq(irq),
        .event_if(irq_event_if)
    );

endmodule

`resetall
