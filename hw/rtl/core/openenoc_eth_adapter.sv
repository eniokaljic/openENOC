// SPDX-FileCopyrightText: 2026 Enio Kaljic
// SPDX-License-Identifier: CERN-OHL-S-2.0

`resetall
`timescale 1ns / 1ps
`default_nettype none

module openenoc_eth_adapter #
(
    // FIFO depth in words
    parameter DEPTH = 4096,
    // Number of RAM pipeline registers
    parameter RAM_PIPELINE = 1,
    // Use output FIFO
    parameter logic OUTPUT_FIFO_EN = 1'b0,
    // Frame FIFO mode
    parameter logic FRAME_FIFO = 1'b0,
    // tuser value for bad frame marker
    parameter USER_BAD_FRAME_VALUE = 1'b1,
    // tuser mask for bad frame marker
    parameter USER_BAD_FRAME_MASK = 1'b1,
    // Drop frames larger than FIFO
    parameter logic DROP_OVERSIZE_FRAME = FRAME_FIFO,
    // Drop frames marked bad
    parameter logic DROP_BAD_FRAME = 1'b0,
    // Drop incoming frames when full
    parameter logic DROP_WHEN_FULL = 1'b0,
    // Mark incoming frames as bad frames when full
    parameter logic MARK_WHEN_FULL = 1'b0,
    // Pause between frames
    parameter logic FRAME_PAUSE = FRAME_FIFO
)
(
    /*
     * Ethernet-like openENOC link, side A clock domain
     */
    openenoc_eth_if eth_a,

    /*
     * Ethernet-like openENOC link, side B clock domain
     */
    openenoc_eth_if eth_b
);

    /*
     * Local taxi_axis_if instances used as Verilator-friendly bridge
     */
    taxi_axis_if #(
        .DATA_W  (eth_a.DATA_W),
        .KEEP_W  (eth_a.KEEP_W),
        .KEEP_EN (eth_a.KEEP_EN),
        .STRB_EN (eth_a.STRB_EN),
        .LAST_EN (eth_a.LAST_EN),
        .ID_EN   (eth_a.ID_EN),
        .ID_W    (eth_a.ID_W),
        .DEST_EN (eth_a.DEST_EN),
        .DEST_W  (eth_a.DEST_W),
        .USER_EN (eth_a.USER_EN),
        .USER_W  (eth_a.USER_W)
    ) fifo_a2b_s_axis_if();

    taxi_axis_if #(
        .DATA_W  (eth_b.DATA_W),
        .KEEP_W  (eth_b.KEEP_W),
        .KEEP_EN (eth_b.KEEP_EN),
        .STRB_EN (eth_b.STRB_EN),
        .LAST_EN (eth_b.LAST_EN),
        .ID_EN   (eth_b.ID_EN),
        .ID_W    (eth_b.ID_W),
        .DEST_EN (eth_b.DEST_EN),
        .DEST_W  (eth_b.DEST_W),
        .USER_EN (eth_b.USER_EN),
        .USER_W  (eth_b.USER_W)
    ) fifo_a2b_m_axis_if();

    taxi_axis_if #(
        .DATA_W  (eth_b.DATA_W),
        .KEEP_W  (eth_b.KEEP_W),
        .KEEP_EN (eth_b.KEEP_EN),
        .STRB_EN (eth_b.STRB_EN),
        .LAST_EN (eth_b.LAST_EN),
        .ID_EN   (eth_b.ID_EN),
        .ID_W    (eth_b.ID_W),
        .DEST_EN (eth_b.DEST_EN),
        .DEST_W  (eth_b.DEST_W),
        .USER_EN (eth_b.USER_EN),
        .USER_W  (eth_b.USER_W)
    ) fifo_b2a_s_axis_if();

    taxi_axis_if #(
        .DATA_W  (eth_a.DATA_W),
        .KEEP_W  (eth_a.KEEP_W),
        .KEEP_EN (eth_a.KEEP_EN),
        .STRB_EN (eth_a.STRB_EN),
        .LAST_EN (eth_a.LAST_EN),
        .ID_EN   (eth_a.ID_EN),
        .ID_W    (eth_a.ID_W),
        .DEST_EN (eth_a.DEST_EN),
        .DEST_W  (eth_a.DEST_W),
        .USER_EN (eth_a.USER_EN),
        .USER_W  (eth_a.USER_W)
    ) fifo_b2a_m_axis_if();

    // A -> B source bridge: eth_a.a2b_axis_if drives FIFO input
    assign fifo_a2b_s_axis_if.tdata  = eth_a.a2b_axis_if.tdata;
    assign fifo_a2b_s_axis_if.tkeep  = eth_a.a2b_axis_if.tkeep;
    assign fifo_a2b_s_axis_if.tstrb  = eth_a.a2b_axis_if.tstrb;
    assign fifo_a2b_s_axis_if.tid    = eth_a.a2b_axis_if.tid;
    assign fifo_a2b_s_axis_if.tdest  = eth_a.a2b_axis_if.tdest;
    assign fifo_a2b_s_axis_if.tuser  = eth_a.a2b_axis_if.tuser;
    assign fifo_a2b_s_axis_if.tlast  = eth_a.a2b_axis_if.tlast;
    assign fifo_a2b_s_axis_if.tvalid = eth_a.a2b_axis_if.tvalid;
    assign eth_a.a2b_axis_if.tready       = fifo_a2b_s_axis_if.tready;

    // A -> B sink bridge: FIFO output drives eth_b.a2b_axis_if
    assign eth_b.a2b_axis_if.tdata        = fifo_a2b_m_axis_if.tdata;
    assign eth_b.a2b_axis_if.tkeep        = fifo_a2b_m_axis_if.tkeep;
    assign eth_b.a2b_axis_if.tstrb        = fifo_a2b_m_axis_if.tstrb;
    assign eth_b.a2b_axis_if.tid          = fifo_a2b_m_axis_if.tid;
    assign eth_b.a2b_axis_if.tdest        = fifo_a2b_m_axis_if.tdest;
    assign eth_b.a2b_axis_if.tuser        = fifo_a2b_m_axis_if.tuser;
    assign eth_b.a2b_axis_if.tlast        = fifo_a2b_m_axis_if.tlast;
    assign eth_b.a2b_axis_if.tvalid       = fifo_a2b_m_axis_if.tvalid;
    assign fifo_a2b_m_axis_if.tready = eth_b.a2b_axis_if.tready;

    // B -> A source bridge: eth_b.b2a_axis_if drives FIFO input
    assign fifo_b2a_s_axis_if.tdata  = eth_b.b2a_axis_if.tdata;
    assign fifo_b2a_s_axis_if.tkeep  = eth_b.b2a_axis_if.tkeep;
    assign fifo_b2a_s_axis_if.tstrb  = eth_b.b2a_axis_if.tstrb;
    assign fifo_b2a_s_axis_if.tid    = eth_b.b2a_axis_if.tid;
    assign fifo_b2a_s_axis_if.tdest  = eth_b.b2a_axis_if.tdest;
    assign fifo_b2a_s_axis_if.tuser  = eth_b.b2a_axis_if.tuser;
    assign fifo_b2a_s_axis_if.tlast  = eth_b.b2a_axis_if.tlast;
    assign fifo_b2a_s_axis_if.tvalid = eth_b.b2a_axis_if.tvalid;
    assign eth_b.b2a_axis_if.tready       = fifo_b2a_s_axis_if.tready;

    // B -> A sink bridge: FIFO output drives eth_a.b2a_axis_if
    assign eth_a.b2a_axis_if.tdata        = fifo_b2a_m_axis_if.tdata;
    assign eth_a.b2a_axis_if.tkeep        = fifo_b2a_m_axis_if.tkeep;
    assign eth_a.b2a_axis_if.tstrb        = fifo_b2a_m_axis_if.tstrb;
    assign eth_a.b2a_axis_if.tid          = fifo_b2a_m_axis_if.tid;
    assign eth_a.b2a_axis_if.tdest        = fifo_b2a_m_axis_if.tdest;
    assign eth_a.b2a_axis_if.tuser        = fifo_b2a_m_axis_if.tuser;
    assign eth_a.b2a_axis_if.tlast        = fifo_b2a_m_axis_if.tlast;
    assign eth_a.b2a_axis_if.tvalid       = fifo_b2a_m_axis_if.tvalid;
    assign fifo_b2a_m_axis_if.tready = eth_a.b2a_axis_if.tready;

    /*
     * A -> B direction
     *
     * Source side:
     *   eth_a.clk / eth_a.rst
     *   eth_a.a2b_axis_if
     *
     * Destination side:
     *   eth_b.clk / eth_b.rst
     *   eth_b.a2b_axis_if
     */
    taxi_axis_async_fifo_adapter #(
        .DEPTH                  (DEPTH),
        .RAM_PIPELINE           (RAM_PIPELINE),
        .OUTPUT_FIFO_EN         (OUTPUT_FIFO_EN),
        .FRAME_FIFO             (FRAME_FIFO),
        .USER_BAD_FRAME_VALUE   (USER_BAD_FRAME_VALUE),
        .USER_BAD_FRAME_MASK    (USER_BAD_FRAME_MASK),
        .DROP_OVERSIZE_FRAME    (DROP_OVERSIZE_FRAME),
        .DROP_BAD_FRAME         (DROP_BAD_FRAME),
        .DROP_WHEN_FULL         (DROP_WHEN_FULL),
        .MARK_WHEN_FULL         (MARK_WHEN_FULL),
        .PAUSE_EN               (1'b0),
        .FRAME_PAUSE            (FRAME_PAUSE)
    )
    u_fifo_a2b (
        .s_clk  (eth_a.clk),
        .s_rst  (eth_a.rst),
        .s_axis (fifo_a2b_s_axis_if),

        .m_clk  (eth_b.clk),
        .m_rst  (eth_b.rst),
        .m_axis (fifo_a2b_m_axis_if),

        .s_pause_req(1'b0),
        .s_pause_ack(),
        .m_pause_req(1'b0),
        .m_pause_ack(),

        .s_status_depth(),
        .s_status_depth_commit(),
        .s_status_overflow(),
        .s_status_bad_frame(),
        .s_status_good_frame(),
        .m_status_depth(),
        .m_status_depth_commit(),
        .m_status_overflow(),
        .m_status_bad_frame(),
        .m_status_good_frame()
    );

    /*
     * B -> A direction
     *
     * Source side:
     *   eth_b.clk / eth_b.rst
     *   eth_b.b2a_axis_if
     *
     * Destination side:
     *   eth_a.clk / eth_a.rst
     *   eth_a.b2a_axis_if
     */
    taxi_axis_async_fifo_adapter #(
        .DEPTH                  (DEPTH),
        .RAM_PIPELINE           (RAM_PIPELINE),
        .OUTPUT_FIFO_EN         (OUTPUT_FIFO_EN),
        .FRAME_FIFO             (FRAME_FIFO),
        .USER_BAD_FRAME_VALUE   (USER_BAD_FRAME_VALUE),
        .USER_BAD_FRAME_MASK    (USER_BAD_FRAME_MASK),
        .DROP_OVERSIZE_FRAME    (DROP_OVERSIZE_FRAME),
        .DROP_BAD_FRAME         (DROP_BAD_FRAME),
        .DROP_WHEN_FULL         (DROP_WHEN_FULL),
        .MARK_WHEN_FULL         (MARK_WHEN_FULL),
        .PAUSE_EN               (1'b0),
        .FRAME_PAUSE            (FRAME_PAUSE)
    )
    u_fifo_b2a (
        .s_clk  (eth_b.clk),
        .s_rst  (eth_b.rst),
        .s_axis (fifo_b2a_s_axis_if),

        .m_clk  (eth_a.clk),
        .m_rst  (eth_a.rst),
        .m_axis (fifo_b2a_m_axis_if),

        .s_pause_req(1'b0),
        .s_pause_ack(),
        .m_pause_req(1'b0),
        .m_pause_ack(),

        .s_status_depth(),
        .s_status_depth_commit(),
        .s_status_overflow(),
        .s_status_bad_frame(),
        .s_status_good_frame(),
        .m_status_depth(),
        .m_status_depth_commit(),
        .m_status_overflow(),
        .m_status_bad_frame(),
        .m_status_good_frame()
    );

endmodule

`resetall
