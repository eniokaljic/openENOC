// SPDX-FileCopyrightText: 2026 Kerim Bavcic
// SPDX-License-Identifier: CERN-OHL-S-2.0

`resetall
`timescale 1ns / 1ps
`default_nettype none

/*
 * Ethernet crossbar: one forwarding engine per ingress, one shared table.
 * Port adaptation and A/B orientation match openenoc_eth_switch_shared_bus.
 */
module openenoc_eth_switch_crossbar #
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

    localparam int unsigned FABRIC_KEEP_W = (FABRIC_DATA_W+7) / 8;
    localparam int unsigned PORT_INDEX_W  = $clog2(NUM_OF_INTERFACES);

    /* verilator lint_off GENUNNAMED */
    if (NUM_OF_INTERFACES < 2 || NUM_OF_INTERFACES > 32)
        $fatal(0, "Error: NUM_OF_INTERFACES must be in range 2 to 32 (instance %m)");

    if (TABLE_DEPTH < 1)
        $fatal(0, "Error: TABLE_DEPTH must be at least 1 (instance %m)");

    if (FABRIC_DATA_W < 8 || FABRIC_DATA_W > 512 || FABRIC_DATA_W % 8 != 0)
        $fatal(0, "Error: FABRIC_DATA_W must be a multiple of 8 in range 8 to 512 (instance %m)");

    if (switch_if.NUM_OF_INTERFACES != NUM_OF_INTERFACES)
        $fatal(0, "Error: switch_if NUM_OF_INTERFACES parameter mismatch (instance %m)");

    if (switch_if.TABLE_DEPTH != TABLE_DEPTH)
        $fatal(0, "Error: switch_if TABLE_DEPTH parameter mismatch (instance %m)");
    /* verilator lint_on GENUNNAMED */

    /*
     * Homogeneous per-ingress switch fabric interfaces.
     *
     * tid carries the physical ingress port index.  Each forwarding engine
     * places its egress port bitmap in tuser before the output crossbar.
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
    ) ingress_axis_if[NUM_OF_INTERFACES](),
      engine_axis_if[NUM_OF_INTERFACES](),
      forwarding_axis_if[NUM_OF_INTERFACES](),
      egress_axis_if[NUM_OF_INTERFACES]();

    openenoc_lookup_if #(
        .NUM_OF_INTERFACES (NUM_OF_INTERFACES)
    ) lookup_if[NUM_OF_INTERFACES]();

    openenoc_lookup_if #(
        .NUM_OF_INTERFACES (NUM_OF_INTERFACES)
    ) table_lookup_if();

    openenoc_learning_if #(
        .NUM_OF_INTERFACES (NUM_OF_INTERFACES)
    ) learning_if[NUM_OF_INTERFACES]();

    openenoc_learning_if #(
        .NUM_OF_INTERFACES (NUM_OF_INTERFACES)
    ) table_learning_if();

    wire [NUM_OF_INTERFACES-1:0] engine_pause_done;

    // Pause completes at engine frame boundaries, not at empty egress FIFOs.
    assign switch_if.core_to_csr.forwarding_control.pause_done.next = &engine_pause_done;

    /*
     * Per-port ingress processing and egress adaptation
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
        ) port_rx_axis_if();

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
        ) port_tx_axis_if();

        /*
         * Normalize A/B link orientation into RX/TX.
         */
        if (PORT_SIDE[n] == SIDE_B) begin : g_side_b

            assign port_rx_axis_if.tdata  = eth_if[n].a2b_axis_if.tdata;
            assign port_rx_axis_if.tkeep  = eth_if[n].a2b_axis_if.tkeep;
            assign port_rx_axis_if.tstrb  = eth_if[n].a2b_axis_if.tstrb;
            assign port_rx_axis_if.tid    = eth_if[n].a2b_axis_if.tid;
            assign port_rx_axis_if.tdest  = eth_if[n].a2b_axis_if.tdest;
            assign port_rx_axis_if.tuser  = eth_if[n].a2b_axis_if.tuser;
            assign port_rx_axis_if.tlast  = eth_if[n].a2b_axis_if.tlast;
            assign port_rx_axis_if.tvalid = eth_if[n].a2b_axis_if.tvalid;
            assign eth_if[n].a2b_axis_if.tready = port_rx_axis_if.tready;

            assign eth_if[n].b2a_axis_if.tdata  = port_tx_axis_if.tdata;
            assign eth_if[n].b2a_axis_if.tkeep  = port_tx_axis_if.tkeep;
            assign eth_if[n].b2a_axis_if.tstrb  = port_tx_axis_if.tstrb;
            assign eth_if[n].b2a_axis_if.tid    = port_tx_axis_if.tid;
            assign eth_if[n].b2a_axis_if.tdest  = port_tx_axis_if.tdest;
            assign eth_if[n].b2a_axis_if.tuser  = port_tx_axis_if.tuser;
            assign eth_if[n].b2a_axis_if.tlast  = port_tx_axis_if.tlast;
            assign eth_if[n].b2a_axis_if.tvalid = port_tx_axis_if.tvalid;
            assign port_tx_axis_if.tready = eth_if[n].b2a_axis_if.tready;

        end else begin : g_side_a

            assign port_rx_axis_if.tdata  = eth_if[n].b2a_axis_if.tdata;
            assign port_rx_axis_if.tkeep  = eth_if[n].b2a_axis_if.tkeep;
            assign port_rx_axis_if.tstrb  = eth_if[n].b2a_axis_if.tstrb;
            assign port_rx_axis_if.tid    = eth_if[n].b2a_axis_if.tid;
            assign port_rx_axis_if.tdest  = eth_if[n].b2a_axis_if.tdest;
            assign port_rx_axis_if.tuser  = eth_if[n].b2a_axis_if.tuser;
            assign port_rx_axis_if.tlast  = eth_if[n].b2a_axis_if.tlast;
            assign port_rx_axis_if.tvalid = eth_if[n].b2a_axis_if.tvalid;
            assign eth_if[n].b2a_axis_if.tready = port_rx_axis_if.tready;

            assign eth_if[n].a2b_axis_if.tdata  = port_tx_axis_if.tdata;
            assign eth_if[n].a2b_axis_if.tkeep  = port_tx_axis_if.tkeep;
            assign eth_if[n].a2b_axis_if.tstrb  = port_tx_axis_if.tstrb;
            assign eth_if[n].a2b_axis_if.tid    = port_tx_axis_if.tid;
            assign eth_if[n].a2b_axis_if.tdest  = port_tx_axis_if.tdest;
            assign eth_if[n].a2b_axis_if.tuser  = port_tx_axis_if.tuser;
            assign eth_if[n].a2b_axis_if.tlast  = port_tx_axis_if.tlast;
            assign eth_if[n].a2b_axis_if.tvalid = port_tx_axis_if.tvalid;
            assign port_tx_axis_if.tready = eth_if[n].a2b_axis_if.tready;

        end

        /*
         * Ingress CDC and width adaptation:
         *
         * eth_if[n].DATA_W @ eth_if[n].clk
         *              ->
         * FABRIC_DATA_W @ clk
         */
        taxi_axis_async_fifo_adapter #(
            .DEPTH      (PORT_FIFO_DEPTH),
            .FRAME_FIFO (1'b0),
            .PAUSE_EN   (1'b0)
        )
        u_ingress_adapter (
            .s_clk  (eth_if[n].clk),
            .s_rst  (eth_if[n].rst),
            .s_axis (port_rx_axis_if),

            .m_clk  (clk),
            .m_rst  (rst),
            .m_axis (ingress_axis_if[n]),

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
         * Physical ingress identity replaces the untrusted incoming tid before
         * the frame reaches its dedicated forwarding engine.
         */
        assign engine_axis_if[n].tdata  = ingress_axis_if[n].tdata;
        assign engine_axis_if[n].tkeep  = ingress_axis_if[n].tkeep;
        assign engine_axis_if[n].tstrb  = ingress_axis_if[n].tstrb;
        assign engine_axis_if[n].tid    = PORT_INDEX_W'(n);
        assign engine_axis_if[n].tdest  = ingress_axis_if[n].tdest;
        assign engine_axis_if[n].tuser  = '0;
        assign engine_axis_if[n].tlast  = ingress_axis_if[n].tlast;
        assign engine_axis_if[n].tvalid = ingress_axis_if[n].tvalid;
        assign ingress_axis_if[n].tready = engine_axis_if[n].tready;

        openenoc_axis_forwarding_engine #(
            .NUM_OF_INTERFACES (NUM_OF_INTERFACES)
        )
        u_forwarding_engine (
            .clk           (clk),
            .rst           (rst),
            .pause_request (switch_if.csr_to_core.forwarding_control.pause_request.value),
            .pause_done    (engine_pause_done[n]),
            .s_axis        (engine_axis_if[n]),
            .m_axis        (forwarding_axis_if[n]),
            .lookup_if     (lookup_if[n]),
            .learning_if   (learning_if[n])
        );

        /*
         * Egress CDC and width adaptation:
         *
         * FABRIC_DATA_W @ clk
         *              ->
         * eth_if[n].DATA_W @ eth_if[n].clk
         */
        taxi_axis_async_fifo_adapter #(
            .DEPTH      (PORT_FIFO_DEPTH),
            .FRAME_FIFO (1'b0),
            .PAUSE_EN   (1'b0)
        )
        u_egress_adapter (
            .s_clk  (clk),
            .s_rst  (rst),
            .s_axis (egress_axis_if[n]),

            .m_clk  (eth_if[n].clk),
            .m_rst  (eth_if[n].rst),
            .m_axis (port_tx_axis_if),

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
     * Independent round-robin arbitration joins the per-port lookup and
     * learning requests onto the two forwarding-table interfaces.
     */
    openenoc_forwarding_table_arb_mux #(
        .NUM_OF_INTERFACES (NUM_OF_INTERFACES)
    )
    u_forwarding_table_arb_mux (
        .clk           (clk),
        .rst           (rst),
        .s_lookup_if   (lookup_if),
        .s_learning_if (learning_if),
        .m_lookup_if   (table_lookup_if),
        .m_learning_if (table_learning_if)
    );

    openenoc_forwarding_table #(
        .NUM_OF_INTERFACES (NUM_OF_INTERFACES),
        .TABLE_DEPTH       (TABLE_DEPTH)
    )
    u_forwarding_table (
        .clk                (clk),
        .rst                (rst),
        .default_forwarding (switch_if.csr_to_core.default_forwarding.bitmap.value),
        .operation_mode     (switch_if.csr_to_core.forwarding_control.operation_mode.value),
        .cpuif_req          (switch_if.csr_to_core.forwarding_table.req),
        .cpuif_addr         (switch_if.csr_to_core.forwarding_table.addr),
        .cpuif_req_is_wr    (switch_if.csr_to_core.forwarding_table.req_is_wr),
        .cpuif_wr_data      (switch_if.csr_to_core.forwarding_table.wr_data),
        .cpuif_wr_biten     (switch_if.csr_to_core.forwarding_table.wr_biten),
        .cpuif_wr_ack       (switch_if.core_to_csr.forwarding_table.wr_ack),
        .cpuif_rd_ack       (switch_if.core_to_csr.forwarding_table.rd_ack),
        .cpuif_rd_data      (switch_if.core_to_csr.forwarding_table.rd_data),
        .lookup_if          (table_lookup_if),
        .learning_if        (table_learning_if)
    );

    /*
     * The per-ingress engines place egress bitmaps in tuser.  The output
     * crossbar forwards independent streams concurrently when their routes do
     * not contend and arbitrates each contested output independently.
     */
    openenoc_axis_switch #(
        .S_COUNT   (NUM_OF_INTERFACES),
        .M_COUNT   (NUM_OF_INTERFACES),
        .S_REG_TYPE(2),
        .M_REG_TYPE(0)
    )
    u_axis_switch (
        .clk                (clk),
        .rst                (rst),
        .tuser_bitmap_route (1'b1),
        .s_axis             (forwarding_axis_if),
        .m_axis             (egress_axis_if)
    );

endmodule

`resetall
