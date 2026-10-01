// SPDX-FileCopyrightText: 2026 Enio Kaljic
// SPDX-License-Identifier: CERN-OHL-S-2.0

`resetall
`timescale 1ns / 1ps
`default_nettype none

/*
 * Native CPUIF slave to AXI4-Lite master adapter
 *
 * A CPUIF request may launch directly into the AXI address/data channels. The
 * request is retained until every applicable request channel is accepted and
 * the AXI response completes. A new request may be launched in the same cycle
 * as the preceding CPUIF acknowledgement, so consecutive transfers do not
 * require an idle cycle.
 *
 * CPUIF write bit enables must be byte-uniform because AXI4-Lite only exposes
 * one write strobe per byte lane.
 */
module openenoc_cpuif_axil_adapter (
    input  wire logic       clk,
    input  wire logic       rst,

    openenoc_cpuif_if.slv   s_cpuif,
    taxi_axil_if.wr_mst     m_axil_wr,
    taxi_axil_if.rd_mst     m_axil_rd
);

    localparam int unsigned DATA_W = s_cpuif.DATA_W;
    localparam int unsigned ADDR_W = s_cpuif.ADDR_W;
    localparam int unsigned STRB_W = DATA_W/8;
    localparam int unsigned BYTE_W = DATA_W/STRB_W;

    if (DATA_W % 8 != 0) begin : g_data_width_error
        $fatal(0, "Error: CPUIF data width must be a multiple of eight (instance %m)");
    end

    if (m_axil_wr.DATA_W != DATA_W || m_axil_rd.DATA_W != DATA_W ||
            m_axil_wr.STRB_W != STRB_W || m_axil_rd.STRB_W != STRB_W) begin : g_data_width_mismatch
        $fatal(0, "Error: CPUIF and AXI4-Lite data widths do not match (instance %m)");
    end

    if (m_axil_wr.ADDR_W != ADDR_W || m_axil_rd.ADDR_W != ADDR_W) begin : g_addr_width_mismatch
        $fatal(0, "Error: CPUIF and AXI4-Lite address widths do not match (instance %m)");
    end

    function automatic logic [STRB_W-1:0] biten_to_strb(
        input logic [DATA_W-1:0] biten
    );
        for (int unsigned lane = 0; lane < STRB_W; lane++) begin
            biten_to_strb[lane] = &biten[lane*BYTE_W +: BYTE_W];
        end
    endfunction

    logic                  request_active_reg;
    logic                  request_write_reg;
    logic [ADDR_W-1:0]     request_addr_reg;
    logic [DATA_W-1:0]     request_wdata_reg;
    logic [STRB_W-1:0]     request_wstrb_reg;
    logic                  aw_pending_reg;
    logic                  w_pending_reg;
    logic                  ar_pending_reg;

    wire logic write_complete = !rst && request_active_reg && request_write_reg &&
        m_axil_wr.bvalid;
    wire logic read_complete = !rst && request_active_reg && !request_write_reg &&
        m_axil_rd.rvalid;
    wire logic request_complete = write_complete || read_complete;

    /*
     * CPUIF permits the next request in the acknowledgement cycle. Selecting
     * that live request here lets its AXI request handshake at the same edge.
     */
    wire logic launch_request = !rst && s_cpuif.req &&
        (!request_active_reg || request_complete);
    wire logic launch_write = launch_request && s_cpuif.req_is_wr;
    wire logic launch_read = launch_request && !s_cpuif.req_is_wr;

    assign m_axil_wr.awvalid = !rst && (launch_request ? launch_write :
        (request_active_reg && request_write_reg && aw_pending_reg));
    assign m_axil_wr.awaddr = launch_request ? s_cpuif.addr : request_addr_reg;
    assign m_axil_wr.awprot = 3'b000;
    assign m_axil_wr.awuser = '0;

    assign m_axil_wr.wvalid = !rst && (launch_request ? launch_write :
        (request_active_reg && request_write_reg && w_pending_reg));
    assign m_axil_wr.wdata = launch_request ? s_cpuif.wr_data : request_wdata_reg;
    assign m_axil_wr.wstrb = launch_request ?
        biten_to_strb(s_cpuif.wr_biten) : request_wstrb_reg;
    assign m_axil_wr.wuser = '0;

    assign m_axil_wr.bready = !rst && request_active_reg && request_write_reg;

    assign m_axil_rd.arvalid = !rst && (launch_request ? launch_read :
        (request_active_reg && !request_write_reg && ar_pending_reg));
    assign m_axil_rd.araddr = launch_request ? s_cpuif.addr : request_addr_reg;
    assign m_axil_rd.arprot = 3'b000;
    assign m_axil_rd.aruser = '0;

    assign m_axil_rd.rready = !rst && request_active_reg && !request_write_reg;

    assign s_cpuif.wr_ack = write_complete;
    assign s_cpuif.wr_err = write_complete && (m_axil_wr.bresp != 2'b00);
    assign s_cpuif.rd_ack = read_complete;
    assign s_cpuif.rd_err = read_complete && (m_axil_rd.rresp != 2'b00);
    assign s_cpuif.rd_data = m_axil_rd.rdata;

    always_ff @(posedge clk) begin
        if (rst) begin
            request_active_reg <= 1'b0;
            request_write_reg <= 1'b0;
            request_addr_reg <= '0;
            request_wdata_reg <= '0;
            request_wstrb_reg <= '0;
            aw_pending_reg <= 1'b0;
            w_pending_reg <= 1'b0;
            ar_pending_reg <= 1'b0;
        end else if (launch_request) begin
            request_active_reg <= 1'b1;
            request_write_reg <= s_cpuif.req_is_wr;
            request_addr_reg <= s_cpuif.addr;
            request_wdata_reg <= s_cpuif.wr_data;
            request_wstrb_reg <= biten_to_strb(s_cpuif.wr_biten);
            aw_pending_reg <= launch_write && !m_axil_wr.awready;
            w_pending_reg <= launch_write && !m_axil_wr.wready;
            ar_pending_reg <= launch_read && !m_axil_rd.arready;
        end else if (request_complete) begin
            request_active_reg <= 1'b0;
            aw_pending_reg <= 1'b0;
            w_pending_reg <= 1'b0;
            ar_pending_reg <= 1'b0;
        end else begin
            if (m_axil_wr.awvalid && m_axil_wr.awready) begin
                aw_pending_reg <= 1'b0;
            end

            if (m_axil_wr.wvalid && m_axil_wr.wready) begin
                w_pending_reg <= 1'b0;
            end

            if (m_axil_rd.arvalid && m_axil_rd.arready) begin
                ar_pending_reg <= 1'b0;
            end
        end
    end

endmodule

`resetall
