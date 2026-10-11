// SPDX-FileCopyrightText: 2026 Enio Kaljic
// SPDX-License-Identifier: AGPL-3.0-or-later

`resetall
`timescale 1ns / 1ps
`default_nettype none

module test_openenoc_endpoint_full_csr;
    localparam int ADDR_W =
        openenoc_endpoint_full_csr_pkg::OPENENOC_ENDPOINT_FULL_CSR_MIN_ADDR_WIDTH;
    localparam int NUM_OF_PEERS = openenoc_endpoint_full_csr_pkg::NUM_OF_PEERS;

    logic clk, rst;
    logic s_axil_awvalid, s_axil_wvalid, s_axil_bready;
    logic s_axil_arvalid, s_axil_rready;
    wire s_axil_awready, s_axil_wready, s_axil_bvalid;
    wire s_axil_arready, s_axil_rvalid;
    logic [ADDR_W-1:0] s_axil_awaddr, s_axil_araddr;
    logic [2:0] s_axil_awprot, s_axil_arprot;
    logic [31:0] s_axil_wdata;
    wire [31:0] s_axil_rdata;
    logic [3:0] s_axil_wstrb;
    wire [1:0] s_axil_bresp, s_axil_rresp;

    logic [NUM_OF_PEERS-1:0] peer_error, peer_clear_error_hwclr;
    logic [NUM_OF_PEERS*4-1:0] peer_error_code;
    logic [1:0] non_error, non_clear_errors_hwclr;
    logic [7:0] non_error_code;

    openenoc_endpoint_full_csr_pkg::openenoc_endpoint_full_csr__in_t hwif_in;
    openenoc_endpoint_full_csr_pkg::openenoc_endpoint_full_csr__out_t hwif_out;

    always_comb begin
        hwif_in = '{default: '0};
        hwif_in.endpoint_interface.non_oetp_dma.tx.command_status.error.next = non_error[0];
        hwif_in.endpoint_interface.non_oetp_dma.tx.command_status.error_code.next =
            non_error_code[3:0];
        hwif_in.endpoint_interface.non_oetp_dma.tx.command_status.clear_errors.hwclr =
            non_clear_errors_hwclr[0];
        hwif_in.endpoint_interface.non_oetp_dma.rx.command_status.error.next = non_error[1];
        hwif_in.endpoint_interface.non_oetp_dma.rx.command_status.error_code.next =
            non_error_code[7:4];
        hwif_in.endpoint_interface.non_oetp_dma.rx.command_status.clear_errors.hwclr =
            non_clear_errors_hwclr[1];
        for (int n = 0; n < NUM_OF_PEERS; n++) begin
            hwif_in.endpoint_interface.peers.entry[n].dma.error.next = peer_error[n];
            hwif_in.endpoint_interface.peers.entry[n].dma.error_code.next = peer_error_code[n*4+:4];
            hwif_in.endpoint_interface.peers.entry[n].dma.clear_error.hwclr =
                peer_clear_error_hwclr[n];
        end
    end

    openenoc_endpoint_full_csr dut (
        .*
    );

endmodule

`resetall
