// SPDX-FileCopyrightText: 2026 Kerim Bavcic
// SPDX-FileCopyrightText: 2026 Enio Kaljic
// SPDX-License-Identifier: CERN-OHL-S-2.0

`resetall
`timescale 1ns / 1ps
`default_nettype none

module openenoc_switch_shared_fabric #
(
    // Number of Ethernet interfaces
    parameter int unsigned NUM_OF_INTERFACES = 4,

    // Forwarding table depth in entries
    parameter int unsigned TABLE_DEPTH = 32,

    // Internal switch fabric data width
    parameter int unsigned FABRIC_DATA_W = 32,

    // Interface orientation:
    //   0 = switch is side A
    //   1 = switch is side B
    //
    // By default all switch ports operate as side B.
    parameter logic [NUM_OF_INTERFACES-1:0] PORT_SIDE = '1,

    // Per-port asynchronous FIFO depth in words
    parameter int unsigned PORT_FIFO_DEPTH = 64
)
(
    /*
     * Switch fabric clock domain
     */
    input wire logic clk,
    input wire logic rst,

    /*
     * Control and status interface
     */
    openenoc_switch_if.core switch_if,

    /*
     * Ethernet-like openENOC interfaces
     */
    openenoc_eth_if eth_if [NUM_OF_INTERFACES-1:0]
);

    localparam logic SIDE_A = 1'b0;
    localparam logic SIDE_B = 1'b1;

    /*
     * Per-port ingress/egress adaptation
     */
    for (genvar n = 0; n < NUM_OF_INTERFACES; n++) begin : g_port

        /*
         * External port-side AXI stream interfaces:
         *
         * eth_if[n].DATA_W @ eth_if[n].clk
         */
        taxi_axis_if #(
            .DATA_W  (eth_if[n].DATA_W),
            .KEEP_W  (eth_if[n].KEEP_W),
            .KEEP_EN (eth_if[n].KEEP_EN),
            .STRB_EN (eth_if[n].STRB_EN),
            .LAST_EN (eth_if[n].LAST_EN),
            .ID_EN   (eth_if[n].ID_EN),
            .ID_W    (eth_if[n].ID_W),
            .DEST_EN (eth_if[n].DEST_EN),
            .DEST_W  (eth_if[n].DEST_W),
            .USER_EN (eth_if[n].USER_EN),
            .USER_W  (eth_if[n].USER_W)
        ) port_rx_axis();

        taxi_axis_if #(
            .DATA_W  (eth_if[n].DATA_W),
            .KEEP_W  (eth_if[n].KEEP_W),
            .KEEP_EN (eth_if[n].KEEP_EN),
            .STRB_EN (eth_if[n].STRB_EN),
            .LAST_EN (eth_if[n].LAST_EN),
            .ID_EN   (eth_if[n].ID_EN),
            .ID_W    (eth_if[n].ID_W),
            .DEST_EN (eth_if[n].DEST_EN),
            .DEST_W  (eth_if[n].DEST_W),
            .USER_EN (eth_if[n].USER_EN),
            .USER_W  (eth_if[n].USER_W)
        ) port_tx_axis();

        /*
         * Switch fabric-side AXI stream interfaces:
         *
         * FABRIC_DATA_W @ clk
         *
         * These interfaces are intentionally left unconnected toward
         * the switch fabric in this implementation draft.
         */
        taxi_axis_if #(
            .DATA_W  (FABRIC_DATA_W),
            .KEEP_W  ((FABRIC_DATA_W+7)/8),
            .KEEP_EN (((FABRIC_DATA_W+7)/8) > 1),
            .STRB_EN (eth_if[n].STRB_EN),
            .LAST_EN (eth_if[n].LAST_EN),
            .ID_EN   (eth_if[n].ID_EN),
            .ID_W    (eth_if[n].ID_W),
            .DEST_EN (eth_if[n].DEST_EN),
            .DEST_W  (eth_if[n].DEST_W),
            .USER_EN (eth_if[n].USER_EN),
            .USER_W  (eth_if[n].USER_W)
        ) ingress_axis();

        taxi_axis_if #(
            .DATA_W  (FABRIC_DATA_W),
            .KEEP_W  ((FABRIC_DATA_W+7)/8),
            .KEEP_EN (((FABRIC_DATA_W+7)/8) > 1),
            .STRB_EN (eth_if[n].STRB_EN),
            .LAST_EN (eth_if[n].LAST_EN),
            .ID_EN   (eth_if[n].ID_EN),
            .ID_W    (eth_if[n].ID_W),
            .DEST_EN (eth_if[n].DEST_EN),
            .DEST_W  (eth_if[n].DEST_W),
            .USER_EN (eth_if[n].USER_EN),
            .USER_W  (eth_if[n].USER_W)
        ) egress_axis();

        /*
         * Normalize A/B link orientation into RX/TX.
         */
        if (PORT_SIDE[n] == SIDE_B) begin : g_side_b

            /*
             * Ingress:
             *
             * eth_if[n].DATA_W @ eth_if[n].clk
             *
             * remote side A -> a2b -> switch side B
             */
            assign port_rx_axis.tdata    = eth_if[n].a2b.tdata;
            assign port_rx_axis.tkeep    = eth_if[n].a2b.tkeep;
            assign port_rx_axis.tstrb    = eth_if[n].a2b.tstrb;
            assign port_rx_axis.tid      = eth_if[n].a2b.tid;
            assign port_rx_axis.tdest    = eth_if[n].a2b.tdest;
            assign port_rx_axis.tuser    = eth_if[n].a2b.tuser;
            assign port_rx_axis.tlast    = eth_if[n].a2b.tlast;
            assign port_rx_axis.tvalid   = eth_if[n].a2b.tvalid;
            assign eth_if[n].a2b.tready = port_rx_axis.tready;

            /*
             * Egress:
             *
             * eth_if[n].DATA_W @ eth_if[n].clk
             *
             * switch side B -> b2a -> remote side A
             */
            assign eth_if[n].b2a.tdata   = port_tx_axis.tdata;
            assign eth_if[n].b2a.tkeep   = port_tx_axis.tkeep;
            assign eth_if[n].b2a.tstrb   = port_tx_axis.tstrb;
            assign eth_if[n].b2a.tid     = port_tx_axis.tid;
            assign eth_if[n].b2a.tdest   = port_tx_axis.tdest;
            assign eth_if[n].b2a.tuser   = port_tx_axis.tuser;
            assign eth_if[n].b2a.tlast   = port_tx_axis.tlast;
            assign eth_if[n].b2a.tvalid  = port_tx_axis.tvalid;
            assign port_tx_axis.tready   = eth_if[n].b2a.tready;

        end else begin : g_side_a

            /*
             * Ingress:
             *
             * eth_if[n].DATA_W @ eth_if[n].clk
             *
             * remote side B -> b2a -> switch side A
             */
            assign port_rx_axis.tdata    = eth_if[n].b2a.tdata;
            assign port_rx_axis.tkeep    = eth_if[n].b2a.tkeep;
            assign port_rx_axis.tstrb    = eth_if[n].b2a.tstrb;
            assign port_rx_axis.tid      = eth_if[n].b2a.tid;
            assign port_rx_axis.tdest    = eth_if[n].b2a.tdest;
            assign port_rx_axis.tuser    = eth_if[n].b2a.tuser;
            assign port_rx_axis.tlast    = eth_if[n].b2a.tlast;
            assign port_rx_axis.tvalid   = eth_if[n].b2a.tvalid;
            assign eth_if[n].b2a.tready = port_rx_axis.tready;

            /*
             * Egress:
             *
             * eth_if[n].DATA_W @ eth_if[n].clk
             *
             * switch side A -> a2b -> remote side B
             */
            assign eth_if[n].a2b.tdata   = port_tx_axis.tdata;
            assign eth_if[n].a2b.tkeep   = port_tx_axis.tkeep;
            assign eth_if[n].a2b.tstrb   = port_tx_axis.tstrb;
            assign eth_if[n].a2b.tid     = port_tx_axis.tid;
            assign eth_if[n].a2b.tdest   = port_tx_axis.tdest;
            assign eth_if[n].a2b.tuser   = port_tx_axis.tuser;
            assign eth_if[n].a2b.tlast   = port_tx_axis.tlast;
            assign eth_if[n].a2b.tvalid  = port_tx_axis.tvalid;
            assign port_tx_axis.tready   = eth_if[n].a2b.tready;

        end

        /*
         * Ingress CDC and width adaptation:
         *
         * eth_if[n].DATA_W @ eth_if[n].clk
         *              ->
         * FABRIC_DATA_W @ clk
         */
        taxi_axis_async_fifo_adapter #(
            .DEPTH       (PORT_FIFO_DEPTH),
            .FRAME_FIFO  (1'b0),
            .PAUSE_EN    (1'b0)
        )
        ingress_adapter_inst (
            .s_clk  (eth_if[n].clk),
            .s_rst  (eth_if[n].rst),
            .s_axis (port_rx_axis),

            .m_clk  (clk),
            .m_rst  (rst),
            .m_axis (ingress_axis),

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

        /*
         * Egress CDC and width adaptation:
         *
         * FABRIC_DATA_W @ clk
         *              ->
         * eth_if[n].DATA_W @ eth_if[n].clk
         */
        taxi_axis_async_fifo_adapter #(
            .DEPTH       (PORT_FIFO_DEPTH),
            .FRAME_FIFO  (1'b0),
            .PAUSE_EN    (1'b0)
        )
        egress_adapter_inst (
            .s_clk  (clk),
            .s_rst  (rst),
            .s_axis (egress_axis),

            .m_clk  (eth_if[n].clk),
            .m_rst  (eth_if[n].rst),
            .m_axis (port_tx_axis),

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

    end

    /*
     * Future switch fabric connections:
     *
     *   g_port[n].ingress_axis
     *   g_port[n].egress_axis
     *
     * FABRIC_DATA_W @ clk
     *
     * Intentionally left unconnected.
     */

endmodule

`resetall
