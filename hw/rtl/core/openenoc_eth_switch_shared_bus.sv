// SPDX-FileCopyrightText: 2026 Kerim Bavcic
// SPDX-FileCopyrightText: 2026 Enio Kaljic
// SPDX-License-Identifier: CERN-OHL-S-2.0

`resetall
`timescale 1ns / 1ps
`default_nettype none

module openenoc_eth_switch_shared_bus #
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

    // Per-port asynchronous FIFO capacity in bytes
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

    localparam logic SIDE_B = 1'b1;

    localparam int unsigned FABRIC_KEEP_W = (FABRIC_DATA_W+7)/8;
    localparam int unsigned PORT_INDEX_W  = $clog2(NUM_OF_INTERFACES);

    /* verilator lint_off GENUNNAMED */
    if (NUM_OF_INTERFACES < 2 || NUM_OF_INTERFACES > 32)
        $fatal(0, "Error: NUM_OF_INTERFACES must be in range 2 to 32 (instance %m)");

    if (TABLE_DEPTH < 1)
        $fatal(0, "Error: TABLE_DEPTH must be at least 1 (instance %m)");

    if (FABRIC_DATA_W < 8 || FABRIC_DATA_W % 8 != 0)
        $fatal(0, "Error: FABRIC_DATA_W must be a multiple of 8 (instance %m)");

    if (switch_if.NUM_OF_INTERFACES != NUM_OF_INTERFACES)
        $fatal(0, "Error: switch_if NUM_OF_INTERFACES parameter mismatch (instance %m)");

    if (switch_if.TABLE_DEPTH != TABLE_DEPTH)
        $fatal(0, "Error: switch_if TABLE_DEPTH parameter mismatch (instance %m)");
    /* verilator lint_on GENUNNAMED */

    /*
     * Homogeneous switch fabric interfaces.
     *
     * tid carries the ingress port index after the arbitrated mux.  tuser
     * carries the egress port bitmap after the forwarding engine.
     */
    taxi_axis_if #(
        .DATA_W  (FABRIC_DATA_W),
        .KEEP_W  (FABRIC_KEEP_W),
        .KEEP_EN (FABRIC_KEEP_W > 1),
        .STRB_EN (eth_if[0].STRB_EN),
        .LAST_EN (1'b1),
        .ID_EN   (1'b1),
        .ID_W    (PORT_INDEX_W),
        .DEST_EN (eth_if[0].DEST_EN),
        .DEST_W  (eth_if[0].DEST_W),
        .USER_EN (1'b1),
        .USER_W  (NUM_OF_INTERFACES)
    ) ingress_axis[NUM_OF_INTERFACES](), egress_axis[NUM_OF_INTERFACES]();

    taxi_axis_if #(
        .DATA_W  (FABRIC_DATA_W),
        .KEEP_W  (FABRIC_KEEP_W),
        .KEEP_EN (FABRIC_KEEP_W > 1),
        .STRB_EN (eth_if[0].STRB_EN),
        .LAST_EN (1'b1),
        .ID_EN   (1'b1),
        .ID_W    (PORT_INDEX_W),
        .DEST_EN (eth_if[0].DEST_EN),
        .DEST_W  (eth_if[0].DEST_W),
        .USER_EN (1'b1),
        .USER_W  (NUM_OF_INTERFACES)
    ) arb_axis(), forwarding_axis();

    /*
     * Per-port ingress/egress adaptation
     */
    for (genvar n = 0; n < NUM_OF_INTERFACES; n++) begin : g_port

        localparam int unsigned PORT_BYTE_LANES = eth_if[n].KEEP_EN ? eth_if[n].KEEP_W : 1;
        localparam int unsigned FIFO_BYTE_LANES = PORT_BYTE_LANES > FABRIC_KEEP_W ?
                                                  PORT_BYTE_LANES : FABRIC_KEEP_W;
        localparam int unsigned FIFO_WORD_COUNT = PORT_FIFO_DEPTH / FIFO_BYTE_LANES;

        /* verilator lint_off GENUNNAMED */
        if (!eth_if[n].LAST_EN)
            $fatal(0, "Error: eth_if[%0d] LAST_EN must be enabled (instance %m)", n);

        if (eth_if[n].DATA_W != PORT_BYTE_LANES * 8)
            $fatal(0, "Error: eth_if[%0d] must use 8-bit byte lanes (instance %m)", n);

        if ((PORT_BYTE_LANES > FABRIC_KEEP_W && PORT_BYTE_LANES % FABRIC_KEEP_W != 0) ||
            (FABRIC_KEEP_W > PORT_BYTE_LANES && FABRIC_KEEP_W % PORT_BYTE_LANES != 0))
            $fatal(0, "Error: eth_if[%0d] and fabric widths must have an integer ratio (instance %m)", n);

        if (PORT_FIFO_DEPTH % FIFO_BYTE_LANES != 0)
            $fatal(0, "Error: PORT_FIFO_DEPTH must be a multiple of the widest data width for eth_if[%0d] (instance %m)", n);

        if (FIFO_WORD_COUNT < 2 || (FIFO_WORD_COUNT & (FIFO_WORD_COUNT - 1)) != 0)
            $fatal(0, "Error: PORT_FIFO_DEPTH must contain a power-of-two number of widest-side words, at least 2, for eth_if[%0d] (instance %m)", n);
        /* verilator lint_on GENUNNAMED */

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
            .m_axis (ingress_axis[n]),

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
            .s_axis (egress_axis[n]),

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
     * Frame-aware round-robin ingress arbitration.  UPDATE_TID replaces the
     * incoming tid with the selected ingress port index for the forwarding
     * and learning logic downstream.
     */
    taxi_axis_arb_mux #(
        .S_COUNT           (NUM_OF_INTERFACES),
        .UPDATE_TID        (1'b1),
        .ARB_ROUND_ROBIN   (1'b1),
        .ARB_LSB_HIGH_PRIO (1'b0)
    )
    ingress_arb_mux_inst (
        .clk    (clk),
        .rst    (rst),
        .s_axis (ingress_axis),
        .m_axis (arb_axis)
    );

    logic                              lookup_req;
    logic [47:0]                       lookup_mac_addr;
    logic                              lookup_ack;
    logic [NUM_OF_INTERFACES-1:0]      lookup_port_bitmap;
    logic                              learning_req;
    logic [47:0]                       learning_mac_addr;
    logic [NUM_OF_INTERFACES-1:0]      learning_port_bitmap;
    logic                              learning_ack;

    openenoc_axis_forwarding_engine #(
        .NUM_OF_INTERFACES (NUM_OF_INTERFACES)
    )
    forwarding_engine_inst (
        .clk                  (clk),
        .rst                  (rst),
        .pause_request        (switch_if.csr_to_core.forwarding_control.pause_request.value),
        .pause_done           (switch_if.core_to_csr.forwarding_control.pause_done.next),
        .s_axis               (arb_axis),
        .m_axis               (forwarding_axis),
        .lookup_req           (lookup_req),
        .lookup_mac_addr      (lookup_mac_addr),
        .lookup_ack           (lookup_ack),
        .lookup_port_bitmap   (lookup_port_bitmap),
        .learning_req         (learning_req),
        .learning_mac_addr    (learning_mac_addr),
        .learning_port_bitmap (learning_port_bitmap),
        .learning_ack         (learning_ack)
    );

    openenoc_forwarding_table #(
        .NUM_OF_INTERFACES (NUM_OF_INTERFACES),
        .TABLE_DEPTH       (TABLE_DEPTH)
    )
    forwarding_table_inst (
        .clk                  (clk),
        .rst                  (rst),
        .default_forwarding   (switch_if.csr_to_core.default_forwarding.bitmap.value),
        .operation_mode       (switch_if.csr_to_core.forwarding_control.operation_mode.value),
        .cpuif_req            (switch_if.csr_to_core.forwarding_table.req),
        .cpuif_addr           (switch_if.csr_to_core.forwarding_table.addr),
        .cpuif_req_is_wr      (switch_if.csr_to_core.forwarding_table.req_is_wr),
        .cpuif_wr_data        (switch_if.csr_to_core.forwarding_table.wr_data),
        .cpuif_wr_biten       (switch_if.csr_to_core.forwarding_table.wr_biten),
        .cpuif_wr_ack         (switch_if.core_to_csr.forwarding_table.wr_ack),
        .cpuif_rd_ack         (switch_if.core_to_csr.forwarding_table.rd_ack),
        .cpuif_rd_data        (switch_if.core_to_csr.forwarding_table.rd_data),
        .lookup_req           (lookup_req),
        .lookup_mac_addr      (lookup_mac_addr),
        .lookup_ack           (lookup_ack),
        .lookup_port_bitmap   (lookup_port_bitmap),
        .learning_req         (learning_req),
        .learning_mac_addr    (learning_mac_addr),
        .learning_port_bitmap (learning_port_bitmap),
        .learning_ack         (learning_ack)
    );

    /*
     * The forwarding engine places the egress port bitmap in tuser.  The
     * demultiplexer applies all-or-none multicast backpressure to that mask.
     */
    openenoc_axis_demux #(
        .M_COUNT            (NUM_OF_INTERFACES),
        .TID_ROUTE          (1'b0),
        .TDEST_ROUTE        (1'b0),
        .TUSER_BITMAP_ROUTE (1'b1)
    )
    egress_demux_inst (
        .clk    (clk),
        .rst    (rst),
        .s_axis (forwarding_axis),
        .m_axis (egress_axis),
        .enable (1'b1),
        .drop   (1'b0),
        .select ('0)
    );

endmodule

`resetall
