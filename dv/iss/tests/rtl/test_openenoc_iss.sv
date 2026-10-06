// SPDX-FileCopyrightText: 2026 Kerim Bavcic
// SPDX-License-Identifier: AGPL-3.0-or-later

`resetall
`timescale 1ns / 1ps
`default_nettype none

module test_openenoc_iss #(
    parameter bit TWO_ENDPOINTS = 1'b0
) ();

    logic clk;
    logic rst;

    logic [31:0] iss_axil_awaddr;
    logic [2:0]  iss_axil_awprot;
    logic        iss_axil_awvalid;
    wire logic   iss_axil_awready;
    logic [31:0] iss_axil_wdata;
    logic [3:0]  iss_axil_wstrb;
    logic        iss_axil_wvalid;
    wire logic   iss_axil_wready;
    wire logic [1:0] iss_axil_bresp;
    wire logic   iss_axil_bvalid;
    logic        iss_axil_bready;
    logic [31:0] iss_axil_araddr;
    logic [2:0]  iss_axil_arprot;
    logic        iss_axil_arvalid;
    wire logic   iss_axil_arready;
    wire logic [31:0] iss_axil_rdata;
    wire logic [1:0] iss_axil_rresp;
    wire logic   iss_axil_rvalid;
    logic        iss_axil_rready;

    openenoc_switch_if #(
        .NUM_OF_INTERFACES (openenoc_endpoint_full_csr_pkg::NUM_OF_INTERFACES),
        .TABLE_DEPTH       (openenoc_endpoint_full_csr_pkg::TABLE_DEPTH)
    ) switch_if (
        .clk (clk),
        .rst (rst)
    );

    openenoc_eth_if eth_if (
        .clk (clk),
        .rst (rst)
    );

    if (!TWO_ENDPOINTS) begin : g_loopback
        assign eth_if.a2b_axis_if.tready = eth_if.b2a_axis_if.tready;
        assign eth_if.b2a_axis_if.tdata  = eth_if.a2b_axis_if.tdata;
        assign eth_if.b2a_axis_if.tkeep  = eth_if.a2b_axis_if.tkeep;
        assign eth_if.b2a_axis_if.tstrb  = eth_if.a2b_axis_if.tstrb;
        assign eth_if.b2a_axis_if.tid    = eth_if.a2b_axis_if.tid;
        assign eth_if.b2a_axis_if.tdest  = eth_if.a2b_axis_if.tdest;
        assign eth_if.b2a_axis_if.tuser  = eth_if.a2b_axis_if.tuser;
        assign eth_if.b2a_axis_if.tlast  = eth_if.a2b_axis_if.tlast;
        assign eth_if.b2a_axis_if.tvalid = eth_if.a2b_axis_if.tvalid;
    end else begin : g_dual
        logic [31:0] iss1_axil_awaddr;
        logic [2:0] iss1_axil_awprot;
        logic iss1_axil_awvalid;
        wire logic iss1_axil_awready;
        logic [31:0] iss1_axil_wdata;
        logic [3:0] iss1_axil_wstrb;
        logic iss1_axil_wvalid;
        wire logic iss1_axil_wready;
        wire logic [1:0] iss1_axil_bresp;
        wire logic iss1_axil_bvalid;
        logic iss1_axil_bready;
        logic [31:0] iss1_axil_araddr;
        logic [2:0] iss1_axil_arprot;
        logic iss1_axil_arvalid;
        wire logic iss1_axil_arready;
        wire logic [31:0] iss1_axil_rdata;
        wire logic [1:0] iss1_axil_rresp;
        wire logic iss1_axil_rvalid;
        logic iss1_axil_rready;

        openenoc_switch_if #(
            .NUM_OF_INTERFACES (openenoc_endpoint_full_csr_pkg::NUM_OF_INTERFACES),
            .TABLE_DEPTH       (openenoc_endpoint_full_csr_pkg::TABLE_DEPTH)
        ) switch1_if (
            .clk (clk),
            .rst (rst)
        );

        openenoc_eth_if eth1_if (
            .clk (clk),
            .rst (rst)
        );

        assign eth_if.a2b_axis_if.tready = eth1_if.b2a_axis_if.tready;
        assign eth1_if.b2a_axis_if.tdata = eth_if.a2b_axis_if.tdata;
        assign eth1_if.b2a_axis_if.tkeep = eth_if.a2b_axis_if.tkeep;
        assign eth1_if.b2a_axis_if.tstrb = eth_if.a2b_axis_if.tstrb;
        assign eth1_if.b2a_axis_if.tid = eth_if.a2b_axis_if.tid;
        assign eth1_if.b2a_axis_if.tdest = eth_if.a2b_axis_if.tdest;
        assign eth1_if.b2a_axis_if.tuser = eth_if.a2b_axis_if.tuser;
        assign eth1_if.b2a_axis_if.tlast = eth_if.a2b_axis_if.tlast;
        assign eth1_if.b2a_axis_if.tvalid = eth_if.a2b_axis_if.tvalid;

        assign eth1_if.a2b_axis_if.tready = eth_if.b2a_axis_if.tready;
        assign eth_if.b2a_axis_if.tdata = eth1_if.a2b_axis_if.tdata;
        assign eth_if.b2a_axis_if.tkeep = eth1_if.a2b_axis_if.tkeep;
        assign eth_if.b2a_axis_if.tstrb = eth1_if.a2b_axis_if.tstrb;
        assign eth_if.b2a_axis_if.tid = eth1_if.a2b_axis_if.tid;
        assign eth_if.b2a_axis_if.tdest = eth1_if.a2b_axis_if.tdest;
        assign eth_if.b2a_axis_if.tuser = eth1_if.a2b_axis_if.tuser;
        assign eth_if.b2a_axis_if.tlast = eth1_if.a2b_axis_if.tlast;
        assign eth_if.b2a_axis_if.tvalid = eth1_if.a2b_axis_if.tvalid;

        initial begin
            switch1_if.core_to_csr = '{default: '0};
            switch1_if.core_to_csr.forwarding_control.pause_done.next = 1'b1;
        end

        openenoc_endpoint_full u_endpoint1 (
            .clk       (clk),
            .rst       (rst),
            .switch_if (switch1_if),
            .eth_if    (eth1_if)
        );

        assign u_endpoint1.u_cpu.dv_mem_axi_awvalid = iss1_axil_awvalid;
        assign u_endpoint1.u_cpu.dv_mem_axi_awaddr  = iss1_axil_awaddr;
        assign u_endpoint1.u_cpu.dv_mem_axi_awprot  = iss1_axil_awprot;
        assign u_endpoint1.u_cpu.dv_mem_axi_wvalid  = iss1_axil_wvalid;
        assign u_endpoint1.u_cpu.dv_mem_axi_wdata   = iss1_axil_wdata;
        assign u_endpoint1.u_cpu.dv_mem_axi_wstrb   = iss1_axil_wstrb;
        assign u_endpoint1.u_cpu.dv_mem_axi_bready  = iss1_axil_bready;
        assign u_endpoint1.u_cpu.dv_mem_axi_arvalid = iss1_axil_arvalid;
        assign u_endpoint1.u_cpu.dv_mem_axi_araddr  = iss1_axil_araddr;
        assign u_endpoint1.u_cpu.dv_mem_axi_arprot  = iss1_axil_arprot;
        assign u_endpoint1.u_cpu.dv_mem_axi_rready  = iss1_axil_rready;

        assign iss1_axil_awready = u_endpoint1.cpu_axil_if.awready;
        assign iss1_axil_wready  = u_endpoint1.cpu_axil_if.wready;
        assign iss1_axil_bresp   = u_endpoint1.cpu_axil_if.bresp;
        assign iss1_axil_bvalid  = u_endpoint1.cpu_axil_if.bvalid;
        assign iss1_axil_arready = u_endpoint1.cpu_axil_if.arready;
        assign iss1_axil_rdata   = u_endpoint1.cpu_axil_if.rdata;
        assign iss1_axil_rresp   = u_endpoint1.cpu_axil_if.rresp;
        assign iss1_axil_rvalid  = u_endpoint1.cpu_axil_if.rvalid;

        wire logic endpoint1_tx_valid = eth1_if.a2b_axis_if.tvalid;
        wire logic endpoint1_tx_ready = eth1_if.a2b_axis_if.tready;
        wire logic [31:0] endpoint1_tx_data = eth1_if.a2b_axis_if.tdata;
        wire logic [3:0] endpoint1_tx_keep = eth1_if.a2b_axis_if.tkeep;
        wire logic endpoint1_tx_last = eth1_if.a2b_axis_if.tlast;
        wire logic endpoint1_csr_sink_valid =
            u_endpoint1.u_endpoint_interface.csr_sink_axis_if.tvalid;
        wire logic endpoint1_csr_sink_ready =
            u_endpoint1.u_endpoint_interface.csr_sink_axis_if.tready;
        wire logic [31:0] endpoint1_csr_sink_data =
            u_endpoint1.u_endpoint_interface.csr_sink_axis_if.tdata;
        wire logic [3:0] endpoint1_csr_sink_keep =
            u_endpoint1.u_endpoint_interface.csr_sink_axis_if.tkeep;
        wire logic endpoint1_csr_sink_last =
            u_endpoint1.u_endpoint_interface.csr_sink_axis_if.tlast;
        wire logic endpoint1_imem_active =
            u_endpoint1.imem_axil_if.awvalid || u_endpoint1.imem_axil_if.arvalid;
    end

    initial begin
        switch_if.core_to_csr = '{default: '0};
        switch_if.core_to_csr.forwarding_control.pause_done.next = 1'b1;
    end

    openenoc_endpoint_full u_endpoint (
        .clk       (clk),
        .rst       (rst),
        .switch_if (switch_if),
        .eth_if    (eth_if)
    );

    assign u_endpoint.u_cpu.dv_mem_axi_awvalid = iss_axil_awvalid;
    assign u_endpoint.u_cpu.dv_mem_axi_awaddr  = iss_axil_awaddr;
    assign u_endpoint.u_cpu.dv_mem_axi_awprot  = iss_axil_awprot;
    assign u_endpoint.u_cpu.dv_mem_axi_wvalid  = iss_axil_wvalid;
    assign u_endpoint.u_cpu.dv_mem_axi_wdata   = iss_axil_wdata;
    assign u_endpoint.u_cpu.dv_mem_axi_wstrb   = iss_axil_wstrb;
    assign u_endpoint.u_cpu.dv_mem_axi_bready  = iss_axil_bready;
    assign u_endpoint.u_cpu.dv_mem_axi_arvalid = iss_axil_arvalid;
    assign u_endpoint.u_cpu.dv_mem_axi_araddr  = iss_axil_araddr;
    assign u_endpoint.u_cpu.dv_mem_axi_arprot  = iss_axil_arprot;
    assign u_endpoint.u_cpu.dv_mem_axi_rready  = iss_axil_rready;

    assign iss_axil_awready = u_endpoint.cpu_axil_if.awready;
    assign iss_axil_wready  = u_endpoint.cpu_axil_if.wready;
    assign iss_axil_bresp   = u_endpoint.cpu_axil_if.bresp;
    assign iss_axil_bvalid  = u_endpoint.cpu_axil_if.bvalid;
    assign iss_axil_arready = u_endpoint.cpu_axil_if.arready;
    assign iss_axil_rdata   = u_endpoint.cpu_axil_if.rdata;
    assign iss_axil_rresp   = u_endpoint.cpu_axil_if.rresp;
    assign iss_axil_rvalid  = u_endpoint.cpu_axil_if.rvalid;

    wire logic [31:0] dmem_word0 = u_endpoint.u_dmem.mem[0];
    wire logic imem_active =
        u_endpoint.imem_axil_if.awvalid || u_endpoint.imem_axil_if.arvalid;
    wire logic [31:0] csr_test_value =
        u_endpoint.csr_hwif_out.test_reg.test_field.value;
    wire logic switch_operation_mode =
        switch_if.csr_to_core.forwarding_control.operation_mode.value;
    wire logic switch_pause_request =
        switch_if.csr_to_core.forwarding_control.pause_request.value;
    wire logic [3:0] switch_default_forwarding =
        switch_if.csr_to_core.default_forwarding.bitmap.value;

    wire logic endpoint_tx_valid = eth_if.a2b_axis_if.tvalid;
    wire logic endpoint_tx_ready = eth_if.a2b_axis_if.tready;
    wire logic [31:0] endpoint_tx_data = eth_if.a2b_axis_if.tdata;
    wire logic [3:0] endpoint_tx_keep = eth_if.a2b_axis_if.tkeep;
    wire logic endpoint_tx_last = eth_if.a2b_axis_if.tlast;
    wire logic endpoint_csr_sink_valid =
        u_endpoint.u_endpoint_interface.csr_sink_axis_if.tvalid;
    wire logic endpoint_csr_sink_ready =
        u_endpoint.u_endpoint_interface.csr_sink_axis_if.tready;
    wire logic [31:0] endpoint_csr_sink_data =
        u_endpoint.u_endpoint_interface.csr_sink_axis_if.tdata;
    wire logic [3:0] endpoint_csr_sink_keep =
        u_endpoint.u_endpoint_interface.csr_sink_axis_if.tkeep;
    wire logic endpoint_csr_sink_last =
        u_endpoint.u_endpoint_interface.csr_sink_axis_if.tlast;

endmodule

`resetall
