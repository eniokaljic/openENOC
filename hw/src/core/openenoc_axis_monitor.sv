// SPDX-FileCopyrightText: 2026 Enio Kaljic
// SPDX-License-Identifier: CERN-OHL-S-2.0

`resetall
`timescale 1ns / 1ps
`default_nettype none

/*
 * AXI4-Stream monitor
 */
module openenoc_axis_monitor
(
    input wire logic  clk,
    input wire logic  rst,

    /*
     * AXI4-Stream input (sink)
     */
    taxi_axis_if.snk  s_axis,

    /*
     * AXI4-Stream output (source)
     */
    taxi_axis_if.src  m_axis,

    /*
     * Monitor interface
     */
    output wire logic is_idle
);

// extract parameters
localparam DATA_W = s_axis.DATA_W;
localparam logic KEEP_EN = s_axis.KEEP_EN && m_axis.KEEP_EN;
localparam KEEP_W = s_axis.KEEP_W;
localparam logic STRB_EN = s_axis.STRB_EN && m_axis.STRB_EN;
localparam logic LAST_EN = s_axis.LAST_EN && m_axis.LAST_EN;
localparam logic ID_EN = s_axis.ID_EN && m_axis.ID_EN;
localparam ID_W = s_axis.ID_W;
localparam logic DEST_EN = s_axis.DEST_EN && m_axis.DEST_EN;
localparam DEST_W = s_axis.DEST_W;
localparam logic USER_EN = s_axis.USER_EN && m_axis.USER_EN;
localparam USER_W = s_axis.USER_W;

// check configuration
if (m_axis.DATA_W != DATA_W)
    $fatal(0, "Error: Interface DATA_W parameter mismatch (instance %m)");

if (KEEP_EN && m_axis.KEEP_W != KEEP_W)
    $fatal(0, "Error: Interface KEEP_W parameter mismatch (instance %m)");

assign m_axis.tdata  = s_axis.tdata;
assign m_axis.tkeep  = KEEP_EN ? s_axis.tkeep : '1;
assign m_axis.tstrb  = STRB_EN ? s_axis.tstrb : m_axis.tkeep;
assign m_axis.tvalid = s_axis.tvalid;
assign m_axis.tlast  = LAST_EN ? s_axis.tlast : 1'b1;
assign m_axis.tid    = ID_EN   ? s_axis.tid   : '0;
assign m_axis.tdest  = DEST_EN ? s_axis.tdest : '0;
assign m_axis.tuser  = USER_EN ? s_axis.tuser : '0;

assign s_axis.tready = m_axis.tready;

// monitor logic
logic is_idle_reg;

assign is_idle = is_idle_reg;

always_ff @(posedge clk) begin
    is_idle_reg <= s_axis.tvalid;

    if (rst) begin
        is_idle_reg <= 1'b0;
    end
end

endmodule

`resetall
