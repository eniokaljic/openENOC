// SPDX-FileCopyrightText: 2026 Enio Kaljic
// SPDX-License-Identifier: AGPL-3.0-or-later

`resetall
`timescale 1ns / 1ps
`default_nettype none

/* CSR-integrated scalar test wrapper for the openENOC peer lookup */
module test_openenoc_endpoint_peer_lookup #(
    parameter int LOOKUP_PORTS = 2
) ();

    localparam int NUM_OF_PEERS = openenoc_endpoint_full_csr_pkg::NUM_OF_PEERS;
    localparam int PEER_IDX_W = NUM_OF_PEERS > 1 ? $clog2(NUM_OF_PEERS) : 1;
    localparam int ADDR_W = 32;
    localparam int CSR_ADDR_W =
        openenoc_endpoint_full_csr_pkg::OPENENOC_ENDPOINT_FULL_CSR_MIN_ADDR_WIDTH;

    logic clk;
    logic rst;

    logic s_axil_awready;
    logic s_axil_awvalid;
    logic [CSR_ADDR_W-1:0] s_axil_awaddr;
    logic [2:0] s_axil_awprot;
    logic s_axil_wready;
    logic s_axil_wvalid;
    logic [31:0] s_axil_wdata;
    logic [3:0] s_axil_wstrb;
    logic s_axil_bready;
    logic s_axil_bvalid;
    logic [1:0] s_axil_bresp;
    logic s_axil_arready;
    logic s_axil_arvalid;
    logic [CSR_ADDR_W-1:0] s_axil_araddr;
    logic [2:0] s_axil_arprot;
    logic s_axil_rready;
    logic s_axil_rvalid;
    logic [31:0] s_axil_rdata;
    logic [1:0] s_axil_rresp;

    logic [LOOKUP_PORTS-1:0] req_valid;
    wire [LOOKUP_PORTS-1:0] req_ready;
    logic [LOOKUP_PORTS*2-1:0] req_type;
    logic [LOOKUP_PORTS*4-1:0] req_mode_mask;
    logic [LOOKUP_PORTS*PEER_IDX_W-1:0] req_peer_idx;
    logic [LOOKUP_PORTS*ADDR_W-1:0] req_rmem_addr;
    logic [LOOKUP_PORTS*48-1:0] req_mac_addr;

    wire [LOOKUP_PORTS-1:0] rsp_valid;
    logic [LOOKUP_PORTS-1:0] rsp_ready;
    wire [LOOKUP_PORTS-1:0] rsp_hit;
    wire [LOOKUP_PORTS*PEER_IDX_W-1:0] rsp_peer_idx;
    wire [LOOKUP_PORTS*48-1:0] rsp_mac_addr;
    wire [LOOKUP_PORTS*ADDR_W-1:0] rsp_rmem_offset;
    wire [LOOKUP_PORTS*ADDR_W-1:0] rsp_local_addr;
    wire [LOOKUP_PORTS*ADDR_W-1:0] rsp_remote_addr;
    wire [LOOKUP_PORTS*ADDR_W-1:0] rsp_size;
    wire [LOOKUP_PORTS*2-1:0] rsp_dma_mode;
    wire [LOOKUP_PORTS-1:0] rsp_irq_enable;

    openenoc_endpoint_full_csr_pkg::openenoc_endpoint_full_csr__in_t csr_hwif_in;
    openenoc_endpoint_full_csr_pkg::openenoc_endpoint_full_csr__out_t csr_hwif_out;

    openenoc_endpoint_if #(
        .RMEM_TOTAL_DEPTH(openenoc_endpoint_full_csr_pkg::RMEM_TOTAL_DEPTH),
        .NUM_OF_PEERS(NUM_OF_PEERS)
    ) endpoint_if (
        .clk(clk),
        .rst(rst)
    );

    openenoc_switch_if #(
        .NUM_OF_INTERFACES(openenoc_endpoint_full_csr_pkg::NUM_OF_INTERFACES),
        .TABLE_DEPTH(openenoc_endpoint_full_csr_pkg::TABLE_DEPTH)
    ) switch_if (
        .clk(clk),
        .rst(rst)
    );

    openenoc_peer_lookup_if #(
        .NUM_OF_PEERS(NUM_OF_PEERS),
        .PEER_IDX_W(PEER_IDX_W),
        .ADDR_W(ADDR_W)
    ) lookup_if[LOOKUP_PORTS]();

    always_comb begin
        endpoint_if.core_to_csr = '{default: '0};
        switch_if.core_to_csr = '{default: '0};
    end

    for (genvar port = 0; port < LOOKUP_PORTS; port++) begin : g_lookup_bridge
        assign lookup_if[port].req_valid = req_valid[port];
        assign lookup_if[port].req_type = req_type[port*2+:2];
        assign lookup_if[port].req_mode_mask = req_mode_mask[port*4+:4];
        assign lookup_if[port].req_peer_idx = req_peer_idx[port*PEER_IDX_W+:PEER_IDX_W];
        assign lookup_if[port].req_rmem_addr = req_rmem_addr[port*ADDR_W+:ADDR_W];
        assign lookup_if[port].req_mac_addr = req_mac_addr[port*48+:48];
        assign req_ready[port] = lookup_if[port].req_ready;

        assign rsp_valid[port] = lookup_if[port].rsp_valid;
        assign lookup_if[port].rsp_ready = rsp_ready[port];
        assign rsp_hit[port] = lookup_if[port].rsp_hit;
        assign rsp_peer_idx[port*PEER_IDX_W+:PEER_IDX_W] = lookup_if[port].rsp_peer_idx;
        assign rsp_mac_addr[port*48+:48] = lookup_if[port].rsp_mac_addr;
        assign rsp_rmem_offset[port*ADDR_W+:ADDR_W] = lookup_if[port].rsp_rmem_offset;
        assign rsp_local_addr[port*ADDR_W+:ADDR_W] = lookup_if[port].rsp_local_addr;
        assign rsp_remote_addr[port*ADDR_W+:ADDR_W] = lookup_if[port].rsp_remote_addr;
        assign rsp_size[port*ADDR_W+:ADDR_W] = lookup_if[port].rsp_size;
        assign rsp_dma_mode[port*2+:2] = lookup_if[port].rsp_dma_mode;
        assign rsp_irq_enable[port] = lookup_if[port].rsp_irq_enable;
    end

    openenoc_endpoint_peer_lookup #(
        .LOOKUP_PORTS(LOOKUP_PORTS),
        .NUM_OF_PEERS(NUM_OF_PEERS),
        .PEER_IDX_W(PEER_IDX_W),
        .ADDR_W(ADDR_W)
    ) dut (
        .clk(clk),
        .rst(rst),
        .endpoint_if(endpoint_if),
        .lookup_if(lookup_if)
    );

    openenoc_endpoint_full_csr_bridge u_csr_bridge (
        .csr_hwif_out(csr_hwif_out),
        .csr_hwif_in(csr_hwif_in),
        .endpoint_if(endpoint_if),
        .switch_if(switch_if)
    );

    openenoc_endpoint_full_csr u_csr (
        .clk(clk),
        .rst(rst),
        .s_axil_awready(s_axil_awready),
        .s_axil_awvalid(s_axil_awvalid),
        .s_axil_awaddr(s_axil_awaddr),
        .s_axil_awprot(s_axil_awprot),
        .s_axil_wready(s_axil_wready),
        .s_axil_wvalid(s_axil_wvalid),
        .s_axil_wdata(s_axil_wdata),
        .s_axil_wstrb(s_axil_wstrb),
        .s_axil_bready(s_axil_bready),
        .s_axil_bvalid(s_axil_bvalid),
        .s_axil_bresp(s_axil_bresp),
        .s_axil_arready(s_axil_arready),
        .s_axil_arvalid(s_axil_arvalid),
        .s_axil_araddr(s_axil_araddr),
        .s_axil_arprot(s_axil_arprot),
        .s_axil_rready(s_axil_rready),
        .s_axil_rvalid(s_axil_rvalid),
        .s_axil_rdata(s_axil_rdata),
        .s_axil_rresp(s_axil_rresp),
        .hwif_in(csr_hwif_in),
        .hwif_out(csr_hwif_out)
    );

endmodule

`resetall
