// SPDX-FileCopyrightText: 2026 Enio Kaljic
// SPDX-License-Identifier: CERN-OHL-S-2.0

`resetall
`timescale 1ns / 1ps
`default_nettype none

/*
 * CSR-facing endpoint interface with clock-domain crossing to the Ethernet link
 */
module openenoc_endpoint_interface #
(
    // FIFO depth in bytes
    parameter FIFO_DEPTH = 4096,
    // Number of RAM pipeline registers in each FIFO
    parameter FIFO_RAM_PIPELINE = 1
)
(
    input wire logic clk,
    input wire logic rst,

    openenoc_endpoint_if.core endpoint_if,
    openenoc_eth_if eth_if,

    taxi_axil_if.wr_mst m_axil_wr,
    taxi_axil_if.rd_mst m_axil_rd
);

    localparam CSR_AXIS_DATA_W = 32;
    localparam CSR_AXIS_KEEP_W = CSR_AXIS_DATA_W/8;

    /*
     * Local AXI4-Stream interfaces provide explicit bridges between the
     * generated CSR interface, the asynchronous FIFOs, and the nested
     * Ethernet AXI4-Stream interfaces.
     */
    taxi_axis_if #(
        .DATA_W  (CSR_AXIS_DATA_W),
        .KEEP_W  (CSR_AXIS_KEEP_W),
        .KEEP_EN (1'b1),
        .STRB_EN (1'b0),
        .LAST_EN (1'b1)
    ) csr_source_axis_if();

    taxi_axis_if #(
        .DATA_W  (eth_if.DATA_W),
        .KEEP_W  (eth_if.KEEP_W),
        .KEEP_EN (eth_if.KEEP_EN),
        .STRB_EN (eth_if.STRB_EN),
        .LAST_EN (eth_if.LAST_EN),
        .ID_EN   (eth_if.ID_EN),
        .ID_W    (eth_if.ID_W),
        .DEST_EN (eth_if.DEST_EN),
        .DEST_W  (eth_if.DEST_W),
        .USER_EN (eth_if.USER_EN),
        .USER_W  (eth_if.USER_W)
    ) eth_source_axis_if();

    taxi_axis_if #(
        .DATA_W  (eth_if.DATA_W),
        .KEEP_W  (eth_if.KEEP_W),
        .KEEP_EN (eth_if.KEEP_EN),
        .STRB_EN (eth_if.STRB_EN),
        .LAST_EN (eth_if.LAST_EN),
        .ID_EN   (eth_if.ID_EN),
        .ID_W    (eth_if.ID_W),
        .DEST_EN (eth_if.DEST_EN),
        .DEST_W  (eth_if.DEST_W),
        .USER_EN (eth_if.USER_EN),
        .USER_W  (eth_if.USER_W)
    ) eth_sink_axis_if();

    taxi_axis_if #(
        .DATA_W  (CSR_AXIS_DATA_W),
        .KEEP_W  (CSR_AXIS_KEEP_W),
        .KEEP_EN (1'b1),
        .STRB_EN (1'b0),
        .LAST_EN (1'b1)
    ) csr_sink_axis_if();

    // CSR source -> FIFO input
    assign csr_source_axis_if.tdata =
        endpoint_if.csr_to_core.axis_if.source.data.tdata.value;
    assign csr_source_axis_if.tkeep =
        endpoint_if.csr_to_core.axis_if.source.control.tkeep.value;
    assign csr_source_axis_if.tstrb  = csr_source_axis_if.tkeep;
    assign csr_source_axis_if.tid    = '0;
    assign csr_source_axis_if.tdest  = '0;
    assign csr_source_axis_if.tuser  = '0;
    assign csr_source_axis_if.tlast =
        endpoint_if.csr_to_core.axis_if.source.control.tlast.value;
    assign csr_source_axis_if.tvalid =
        endpoint_if.csr_to_core.axis_if.source.control.tvalid.value;

    // Source FIFO output -> Ethernet transmit direction
    assign eth_if.a2b_axis_if.tdata       = eth_source_axis_if.tdata;
    assign eth_if.a2b_axis_if.tkeep       = eth_source_axis_if.tkeep;
    assign eth_if.a2b_axis_if.tstrb       = eth_source_axis_if.tstrb;
    assign eth_if.a2b_axis_if.tid         = eth_source_axis_if.tid;
    assign eth_if.a2b_axis_if.tdest       = eth_source_axis_if.tdest;
    assign eth_if.a2b_axis_if.tuser       = eth_source_axis_if.tuser;
    assign eth_if.a2b_axis_if.tlast       = eth_source_axis_if.tlast;
    assign eth_if.a2b_axis_if.tvalid      = eth_source_axis_if.tvalid;
    assign eth_source_axis_if.tready = eth_if.a2b_axis_if.tready;

    // Ethernet receive direction -> sink FIFO input
    assign eth_sink_axis_if.tdata  = eth_if.b2a_axis_if.tdata;
    assign eth_sink_axis_if.tkeep  = eth_if.b2a_axis_if.tkeep;
    assign eth_sink_axis_if.tstrb  = eth_if.b2a_axis_if.tstrb;
    assign eth_sink_axis_if.tid    = eth_if.b2a_axis_if.tid;
    assign eth_sink_axis_if.tdest  = eth_if.b2a_axis_if.tdest;
    assign eth_sink_axis_if.tuser  = eth_if.b2a_axis_if.tuser;
    assign eth_sink_axis_if.tlast  = eth_if.b2a_axis_if.tlast;
    assign eth_sink_axis_if.tvalid = eth_if.b2a_axis_if.tvalid;
    assign eth_if.b2a_axis_if.tready    = eth_sink_axis_if.tready;

    // Sink FIFO output -> CSR sink
    assign csr_sink_axis_if.tready =
        endpoint_if.csr_to_core.axis_if.sink.control.tready.value;

    always_comb begin
        endpoint_if.core_to_csr = '{default: '0};

        endpoint_if.core_to_csr.axis_if.source.control.tvalid.hwclr =
            csr_source_axis_if.tvalid && csr_source_axis_if.tready;
        endpoint_if.core_to_csr.axis_if.source.status.tready.next =
            csr_source_axis_if.tready;

        endpoint_if.core_to_csr.axis_if.sink.data.tdata.next =
            csr_sink_axis_if.tdata;
        endpoint_if.core_to_csr.axis_if.sink.control.tready.hwclr =
            csr_sink_axis_if.tvalid && csr_sink_axis_if.tready;
        endpoint_if.core_to_csr.axis_if.sink.status.tvalid.next =
            csr_sink_axis_if.tvalid;
        endpoint_if.core_to_csr.axis_if.sink.status.tlast.next =
            csr_sink_axis_if.tlast;
        endpoint_if.core_to_csr.axis_if.sink.status.tkeep.next =
            csr_sink_axis_if.tkeep;
    end

    taxi_axis_async_fifo_adapter #(
        .DEPTH        (FIFO_DEPTH),
        .RAM_PIPELINE (FIFO_RAM_PIPELINE)
    )
    u_source_fifo (
        .s_clk  (clk),
        .s_rst  (rst),
        .s_axis (csr_source_axis_if),

        .m_clk  (eth_if.clk),
        .m_rst  (eth_if.rst),
        .m_axis (eth_source_axis_if),

        .s_pause_req (1'b0),
        .s_pause_ack (),
        .m_pause_req (1'b0),
        .m_pause_ack (),

        .s_status_depth        (),
        .s_status_depth_commit (),
        .s_status_overflow     (),
        .s_status_bad_frame    (),
        .s_status_good_frame   (),
        .m_status_depth        (),
        .m_status_depth_commit (),
        .m_status_overflow     (),
        .m_status_bad_frame    (),
        .m_status_good_frame   ()
    );

    taxi_axis_async_fifo_adapter #(
        .DEPTH        (FIFO_DEPTH),
        .RAM_PIPELINE (FIFO_RAM_PIPELINE)
    )
    u_sink_fifo (
        .s_clk  (eth_if.clk),
        .s_rst  (eth_if.rst),
        .s_axis (eth_sink_axis_if),

        .m_clk  (clk),
        .m_rst  (rst),
        .m_axis (csr_sink_axis_if),

        .s_pause_req (1'b0),
        .s_pause_ack (),
        .m_pause_req (1'b0),
        .m_pause_ack (),

        .s_status_depth        (),
        .s_status_depth_commit (),
        .s_status_overflow     (),
        .s_status_bad_frame    (),
        .s_status_good_frame   (),
        .m_status_depth        (),
        .m_status_depth_commit (),
        .m_status_overflow     (),
        .m_status_bad_frame    (),
        .m_status_good_frame   ()
    );

    // The endpoint AXI4-Lite initiator is reserved for future use.
    assign m_axil_wr.awaddr  = '0;
    assign m_axil_wr.awprot  = '0;
    assign m_axil_wr.awuser  = '0;
    assign m_axil_wr.awvalid = 1'b0;
    assign m_axil_wr.wdata   = '0;
    assign m_axil_wr.wstrb   = '0;
    assign m_axil_wr.wuser   = '0;
    assign m_axil_wr.wvalid  = 1'b0;
    assign m_axil_wr.bready  = 1'b0;

    assign m_axil_rd.araddr  = '0;
    assign m_axil_rd.arprot  = '0;
    assign m_axil_rd.aruser  = '0;
    assign m_axil_rd.arvalid = 1'b0;
    assign m_axil_rd.rready  = 1'b0;

endmodule

`resetall
