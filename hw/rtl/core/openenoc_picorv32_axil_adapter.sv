// SPDX-FileCopyrightText: 2026 Enio Kaljic
// SPDX-License-Identifier: CERN-OHL-S-2.0

`resetall
`timescale 1ns / 1ps
`default_nettype none

/*
 * PicoRV32 native memory interface to AXI4-Lite master adapter
 */
module openenoc_picorv32_axil_adapter (
    input  wire logic        clk,
    input  wire logic        resetn,

    /*
     * AXI4-Lite master memory interface
     */
    output wire logic        mem_axi_awvalid,
    input  wire logic        mem_axi_awready,
    output wire logic [31:0] mem_axi_awaddr,
    output wire logic [2:0]  mem_axi_awprot,

    output wire logic        mem_axi_wvalid,
    input  wire logic        mem_axi_wready,
    output wire logic [31:0] mem_axi_wdata,
    output wire logic [3:0]  mem_axi_wstrb,

    input  wire logic        mem_axi_bvalid,
    output wire logic        mem_axi_bready,

    output wire logic        mem_axi_arvalid,
    input  wire logic        mem_axi_arready,
    output wire logic [31:0] mem_axi_araddr,
    output wire logic [2:0]  mem_axi_arprot,

    input  wire logic        mem_axi_rvalid,
    output wire logic        mem_axi_rready,
    input  wire logic [31:0] mem_axi_rdata,

    /*
     * Native PicoRV32 memory interface
     */
    input  wire logic        mem_valid,
    input  wire logic        mem_instr,
    output wire logic        mem_ready,
    input  wire logic [31:0] mem_addr,
    input  wire logic [31:0] mem_wdata,
    input  wire logic [3:0]  mem_wstrb,
    output wire logic [31:0] mem_rdata,

    /*
     * Native PicoRV32 look-ahead interface
     */
    input  wire logic        mem_la_read,
    input  wire logic        mem_la_write,
    input  wire logic [31:0] mem_la_addr,
    input  wire logic [31:0] mem_la_wdata,
    input  wire logic [3:0]  mem_la_wstrb
);

    logic request_active_reg;
    logic request_write_reg;
    logic [31:0] request_addr_reg;
    logic [31:0] request_wdata_reg;
    logic [3:0] request_wstrb_reg;

    logic aw_pending_reg;
    logic w_pending_reg;
    logic ar_pending_reg;

    wire logic write_response =
        request_active_reg && request_write_reg && mem_valid && mem_axi_bvalid;
    wire logic read_response =
        request_active_reg && !request_write_reg && mem_valid && mem_axi_rvalid;
    wire logic native_complete = write_response || read_response;

    assign mem_axi_awvalid = request_active_reg && request_write_reg && aw_pending_reg;
    assign mem_axi_awaddr = request_addr_reg;
    assign mem_axi_awprot = 3'b000;

    assign mem_axi_wvalid = request_active_reg && request_write_reg && w_pending_reg;
    assign mem_axi_wdata = request_wdata_reg;
    assign mem_axi_wstrb = request_wstrb_reg;

    assign mem_axi_bready = request_active_reg && request_write_reg && mem_valid;

    assign mem_axi_arvalid = request_active_reg && !request_write_reg && ar_pending_reg;
    assign mem_axi_araddr = request_addr_reg;
    assign mem_axi_arprot = mem_instr ? 3'b100 : 3'b000;

    assign mem_axi_rready = request_active_reg && !request_write_reg && mem_valid;

    assign mem_ready = native_complete;
    assign mem_rdata = mem_axi_rdata;

    always_ff @(posedge clk) begin
        if (!resetn) begin
            request_active_reg <= 1'b0;
            request_write_reg <= 1'b0;
            request_addr_reg <= '0;
            request_wdata_reg <= '0;
            request_wstrb_reg <= '0;
            aw_pending_reg <= 1'b0;
            w_pending_reg <= 1'b0;
            ar_pending_reg <= 1'b0;
        end else if (native_complete) begin
            /*
             * PicoRV32 may present the next look-ahead request in the same
             * cycle in which the current native request completes.
             */
            if (mem_la_read || mem_la_write) begin
                request_active_reg <= 1'b1;
                request_write_reg <= mem_la_write;
                request_addr_reg <= mem_la_addr;
                request_wdata_reg <= mem_la_wdata;
                request_wstrb_reg <= mem_la_wstrb;
                aw_pending_reg <= mem_la_write;
                w_pending_reg <= mem_la_write;
                ar_pending_reg <= mem_la_read;
            end else begin
                request_active_reg <= 1'b0;
                aw_pending_reg <= 1'b0;
                w_pending_reg <= 1'b0;
                ar_pending_reg <= 1'b0;
            end
        end else if (!request_active_reg) begin
            if (mem_la_read || mem_la_write) begin
                request_active_reg <= 1'b1;
                request_write_reg <= mem_la_write;
                request_addr_reg <= mem_la_addr;
                request_wdata_reg <= mem_la_wdata;
                request_wstrb_reg <= mem_la_wstrb;
                aw_pending_reg <= mem_la_write;
                w_pending_reg <= mem_la_write;
                ar_pending_reg <= mem_la_read;
            end else if (mem_valid) begin
                /* Fallback for native masters that do not use look-ahead. */
                request_active_reg <= 1'b1;
                request_write_reg <= |mem_wstrb;
                request_addr_reg <= mem_addr;
                request_wdata_reg <= mem_wdata;
                request_wstrb_reg <= mem_wstrb;
                aw_pending_reg <= |mem_wstrb;
                w_pending_reg <= |mem_wstrb;
                ar_pending_reg <= ~|mem_wstrb;
            end
        end else begin
            if (mem_axi_awvalid && mem_axi_awready) begin
                aw_pending_reg <= 1'b0;
            end

            if (mem_axi_wvalid && mem_axi_wready) begin
                w_pending_reg <= 1'b0;
            end

            if (mem_axi_arvalid && mem_axi_arready) begin
                ar_pending_reg <= 1'b0;
            end
        end
    end

endmodule

`resetall
