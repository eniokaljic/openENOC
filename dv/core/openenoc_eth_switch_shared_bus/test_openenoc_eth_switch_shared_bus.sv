// SPDX-FileCopyrightText: 2026 Kerim Bavcic
// SPDX-License-Identifier: AGPL-3.0-or-later

`resetall
`timescale 1ns / 1ps
`default_nettype none

/*
 * openENOC shared-bus switch testbench
 *
 * The real CSR block is intentionally not instantiated.  Cocotb drives the
 * flattened control signals below, which are bridged directly to switch_if.
 */
module test_openenoc_eth_switch_shared_bus #
(
    /* verilator lint_off WIDTHTRUNC */
    parameter int NUM_OF_INTERFACES = 4,
    parameter int TABLE_DEPTH = 8,
    parameter int DATA_W = 32,
    parameter int KEEP_W = (DATA_W+7)/8,
    parameter logic KEEP_EN = KEEP_W > 1,
    parameter int FABRIC_DATA_W = 32,
    parameter int PORT_FIFO_DEPTH = 64,
    parameter logic [NUM_OF_INTERFACES-1:0] PORT_SIDE = '1,
    localparam int FORWARDING_TABLE_ADDR_W = $clog2(TABLE_DEPTH * 16),
    localparam int PORT_INDEX_W = $clog2(NUM_OF_INTERFACES)
    /* verilator lint_on WIDTHTRUNC */
)
();

    logic clk;
    logic rst;

    localparam logic SIDE_B = 1'b1;

    /*
     * Flattened CSR controls and status for cocotb.
     */
    logic                              operation_mode;
    logic                              pause_request;
    logic [NUM_OF_INTERFACES-1:0]      default_forwarding;
    logic                              cpuif_req;
    logic [FORWARDING_TABLE_ADDR_W-1:0] cpuif_addr;
    logic                              cpuif_req_is_wr;
    logic [31:0]                       cpuif_wr_data;
    logic [31:0]                       cpuif_wr_biten;

    wire logic        pause_done;
    wire logic        cpuif_wr_ack;
    wire logic        cpuif_rd_ack;
    wire logic [31:0] cpuif_rd_data;

    wire logic [NUM_OF_INTERFACES-1:0] ingress_tvalid;
    wire logic [NUM_OF_INTERFACES-1:0] ingress_tready;
    wire logic [NUM_OF_INTERFACES-1:0] egress_tvalid;
    wire logic [NUM_OF_INTERFACES-1:0] egress_tready;
    wire logic                         arb_tvalid;
    wire logic                         arb_tready;
    wire logic                         arb_tlast;
    wire logic [PORT_INDEX_W-1:0]      arb_tid;
    wire logic                         forwarding_tvalid;
    wire logic                         forwarding_tready;

    openenoc_switch_if #(
        .NUM_OF_INTERFACES (NUM_OF_INTERFACES),
        .TABLE_DEPTH       (TABLE_DEPTH)
    ) switch_if (
        .clk (clk),
        .rst (rst)
    );

    always_comb begin
        switch_if.csr_to_core = '{default: '0};
        switch_if.csr_to_core.info.table_depth.value = 16'(TABLE_DEPTH);
        switch_if.csr_to_core.info.num_of_interfaces.value = 6'(NUM_OF_INTERFACES);
        switch_if.csr_to_core.forwarding_control.operation_mode.value = operation_mode;
        switch_if.csr_to_core.forwarding_control.pause_request.value = pause_request;
        switch_if.csr_to_core.default_forwarding.bitmap.value = default_forwarding;
        switch_if.csr_to_core.forwarding_table.req = cpuif_req;
        switch_if.csr_to_core.forwarding_table.addr = cpuif_addr;
        switch_if.csr_to_core.forwarding_table.req_is_wr = cpuif_req_is_wr;
        switch_if.csr_to_core.forwarding_table.wr_data = cpuif_wr_data;
        switch_if.csr_to_core.forwarding_table.wr_biten = cpuif_wr_biten;
    end

    assign pause_done   = switch_if.core_to_csr.forwarding_control.pause_done.next;
    assign cpuif_wr_ack = switch_if.core_to_csr.forwarding_table.wr_ack;
    assign cpuif_rd_ack = switch_if.core_to_csr.forwarding_table.rd_ack;
    assign cpuif_rd_data = switch_if.core_to_csr.forwarding_table.rd_data;

    /*
     * The wrapper acts as the peer opposite each configured switch port.  The
     * interface array itself is exposed to cocotb; no endpoint model is needed.
     */
    openenoc_eth_if #(
        .DATA_W  (DATA_W),
        .KEEP_W  (KEEP_W),
        .KEEP_EN (KEEP_EN),
        .STRB_EN (1'b0),
        .LAST_EN (1'b1),
        .ID_EN   (1'b1),
        .ID_W    (PORT_INDEX_W),
        .DEST_EN (1'b1),
        .DEST_W  (8),
        .USER_EN (1'b1),
        .USER_W  (NUM_OF_INTERFACES)
    ) eth_if[NUM_OF_INTERFACES-1:0] (
        .clk (clk),
        .rst (rst)
    );

    /*
     * Verilator-friendly stream arrays exposed to cocotb.  They bridge to the
     * side-A directions of the nested openenoc_eth_if array with constant
     * generate indices.
     */
    taxi_axis_if #(
        .DATA_W  (DATA_W),
        .KEEP_W  (KEEP_W),
        .KEEP_EN (KEEP_EN),
        .STRB_EN (1'b0),
        .LAST_EN (1'b1),
        .ID_EN   (1'b1),
        .ID_W    (PORT_INDEX_W),
        .DEST_EN (1'b1),
        .DEST_W  (8),
        .USER_EN (1'b1),
        .USER_W  (NUM_OF_INTERFACES)
    ) port_rx_axis_if[NUM_OF_INTERFACES](), port_tx_axis_if[NUM_OF_INTERFACES]();

    for (genvar n = 0; n < NUM_OF_INTERFACES; n++) begin : g_eth_bridge
        if (PORT_SIDE[n] == SIDE_B) begin : g_switch_side_b
            assign eth_if[n].a2b_axis_if.tdata = port_rx_axis_if[n].tdata;
            assign eth_if[n].a2b_axis_if.tkeep = port_rx_axis_if[n].tkeep;
            assign eth_if[n].a2b_axis_if.tstrb = port_rx_axis_if[n].tstrb;
            assign eth_if[n].a2b_axis_if.tid = port_rx_axis_if[n].tid;
            assign eth_if[n].a2b_axis_if.tdest = port_rx_axis_if[n].tdest;
            assign eth_if[n].a2b_axis_if.tuser = port_rx_axis_if[n].tuser;
            assign eth_if[n].a2b_axis_if.tlast = port_rx_axis_if[n].tlast;
            assign eth_if[n].a2b_axis_if.tvalid = port_rx_axis_if[n].tvalid;
            assign port_rx_axis_if[n].tready = eth_if[n].a2b_axis_if.tready;

            assign port_tx_axis_if[n].tdata = eth_if[n].b2a_axis_if.tdata;
            assign port_tx_axis_if[n].tkeep = eth_if[n].b2a_axis_if.tkeep;
            assign port_tx_axis_if[n].tstrb = eth_if[n].b2a_axis_if.tstrb;
            assign port_tx_axis_if[n].tid = eth_if[n].b2a_axis_if.tid;
            assign port_tx_axis_if[n].tdest = eth_if[n].b2a_axis_if.tdest;
            assign port_tx_axis_if[n].tuser = eth_if[n].b2a_axis_if.tuser;
            assign port_tx_axis_if[n].tlast = eth_if[n].b2a_axis_if.tlast;
            assign port_tx_axis_if[n].tvalid = eth_if[n].b2a_axis_if.tvalid;
            assign eth_if[n].b2a_axis_if.tready = port_tx_axis_if[n].tready;
        end else begin : g_switch_side_a
            assign eth_if[n].b2a_axis_if.tdata = port_rx_axis_if[n].tdata;
            assign eth_if[n].b2a_axis_if.tkeep = port_rx_axis_if[n].tkeep;
            assign eth_if[n].b2a_axis_if.tstrb = port_rx_axis_if[n].tstrb;
            assign eth_if[n].b2a_axis_if.tid = port_rx_axis_if[n].tid;
            assign eth_if[n].b2a_axis_if.tdest = port_rx_axis_if[n].tdest;
            assign eth_if[n].b2a_axis_if.tuser = port_rx_axis_if[n].tuser;
            assign eth_if[n].b2a_axis_if.tlast = port_rx_axis_if[n].tlast;
            assign eth_if[n].b2a_axis_if.tvalid = port_rx_axis_if[n].tvalid;
            assign port_rx_axis_if[n].tready = eth_if[n].b2a_axis_if.tready;

            assign port_tx_axis_if[n].tdata = eth_if[n].a2b_axis_if.tdata;
            assign port_tx_axis_if[n].tkeep = eth_if[n].a2b_axis_if.tkeep;
            assign port_tx_axis_if[n].tstrb = eth_if[n].a2b_axis_if.tstrb;
            assign port_tx_axis_if[n].tid = eth_if[n].a2b_axis_if.tid;
            assign port_tx_axis_if[n].tdest = eth_if[n].a2b_axis_if.tdest;
            assign port_tx_axis_if[n].tuser = eth_if[n].a2b_axis_if.tuser;
            assign port_tx_axis_if[n].tlast = eth_if[n].a2b_axis_if.tlast;
            assign port_tx_axis_if[n].tvalid = eth_if[n].a2b_axis_if.tvalid;
            assign eth_if[n].a2b_axis_if.tready = port_tx_axis_if[n].tready;
        end
    end

    openenoc_eth_switch_shared_bus #(
        .NUM_OF_INTERFACES (NUM_OF_INTERFACES),
        .TABLE_DEPTH       (TABLE_DEPTH),
        .FABRIC_DATA_W     (FABRIC_DATA_W),
        .PORT_SIDE         (PORT_SIDE),
        .PORT_FIFO_DEPTH   (PORT_FIFO_DEPTH)
    )
    u_openenoc_eth_switch_shared_bus (
        .clk       (clk),
        .rst       (rst),
        .switch_if (switch_if),
        .eth_if    (eth_if)
    );

    for (genvar n = 0; n < NUM_OF_INTERFACES; n++) begin : g_observe
        assign ingress_tvalid[n] = u_openenoc_eth_switch_shared_bus.ingress_axis_if[n].tvalid;
        assign ingress_tready[n] = u_openenoc_eth_switch_shared_bus.ingress_axis_if[n].tready;
        assign egress_tvalid[n] = u_openenoc_eth_switch_shared_bus.egress_axis_if[n].tvalid;
        assign egress_tready[n] = u_openenoc_eth_switch_shared_bus.egress_axis_if[n].tready;
    end

    assign arb_tvalid = u_openenoc_eth_switch_shared_bus.arb_axis_if.tvalid;
    assign arb_tready = u_openenoc_eth_switch_shared_bus.arb_axis_if.tready;
    assign arb_tlast = u_openenoc_eth_switch_shared_bus.arb_axis_if.tlast;
    assign arb_tid = u_openenoc_eth_switch_shared_bus.arb_axis_if.tid;
    assign forwarding_tvalid = u_openenoc_eth_switch_shared_bus.forwarding_axis_if.tvalid;
    assign forwarding_tready = u_openenoc_eth_switch_shared_bus.forwarding_axis_if.tready;

endmodule

`resetall
