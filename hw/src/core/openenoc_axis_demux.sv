// SPDX-FileCopyrightText: 2026 Kerim Bavcic
// SPDX-License-Identifier: CERN-OHL-S-2.0

`resetall
`timescale 1ns / 1ps
`default_nettype none

/*
 * AXI4-Stream demultiplexer
 */
module openenoc_axis_demux #
(
    // Number of AXI stream outputs
    parameter M_COUNT = 4,
    // route via tid
    parameter logic TID_ROUTE = 1'b0,
    // route via tdest
    parameter logic TDEST_ROUTE = 1'b0,
    // route via tuser
    parameter logic TUSER_BITMAP_ROUTE = 1'b0
)
(
    input  wire logic                        clk,
    input  wire logic                        rst,

    /*
     * AXI4-Stream input (sink)
     */
    taxi_axis_if.snk                         s_axis,

    /*
     * AXI4-Stream output (source)
     */
    taxi_axis_if.src                         m_axis[M_COUNT],

    /*
     * Control
     */
    input  wire logic                        enable,
    input  wire logic                        drop,
    input  wire logic [$clog2(M_COUNT)-1:0]  select
);

// extract parameters
localparam DATA_W = s_axis.DATA_W;
localparam logic KEEP_EN = s_axis.KEEP_EN && m_axis[0].KEEP_EN;
localparam KEEP_W = s_axis.KEEP_W;
localparam logic STRB_EN = s_axis.STRB_EN && m_axis[0].STRB_EN;
localparam logic ID_EN = s_axis.ID_EN && m_axis[0].ID_EN;
localparam logic DEST_EN = s_axis.DEST_EN && m_axis[0].DEST_EN;
localparam S_ID_W = s_axis.ID_W;
localparam M_ID_W = m_axis[0].ID_W;
localparam S_DEST_W = s_axis.DEST_W;
localparam M_DEST_W = m_axis[0].DEST_W;
localparam logic USER_EN = s_axis.USER_EN && m_axis[0].USER_EN;
localparam USER_W = s_axis.USER_W;

localparam CL_M_COUNT = $clog2(M_COUNT);

// check configuration
/* verilator lint_off GENUNNAMED */
if (m_axis[0].DATA_W != DATA_W)
    $fatal(0, "Error: Interface DATA_W parameter mismatch (instance %m)");

if (KEEP_EN && m_axis[0].KEEP_W != KEEP_W)
    $fatal(0, "Error: Interface KEEP_W parameter mismatch (instance %m)");

if (TID_ROUTE) begin
    if (!ID_EN)
        $fatal(0, "Error: TID_ROUTE set requires ID_EN set (instance %m)");

    if (S_ID_W < CL_M_COUNT)
        $fatal(0, "Error: S_ID_W too small for port count (instance %m)");

    if (TDEST_ROUTE)
        $fatal(0, "Error: Cannot enable both TID_ROUTE and TDEST_ROUTE (instance %m)");
end

if (TDEST_ROUTE) begin
    if (!DEST_EN)
        $fatal(0, "Error: TDEST_ROUTE set requires DEST_EN set (instance %m)");

    if (S_DEST_W < CL_M_COUNT)
        $fatal(0, "Error: S_DEST_W too small for port count (instance %m)");
end

if (TUSER_BITMAP_ROUTE) begin
    if (!USER_EN)
        $fatal(0, "Error: TUSER_BITMAP_ROUTE set requires USER_EN set (instance %m)");

    if (USER_W < M_COUNT)
        $fatal(0, "Error: USER_W too small for port count (instance %m)");

    if (TID_ROUTE || TDEST_ROUTE)
        $fatal(0, "Error: Cannot enable TUSER_BITMAP_ROUTE with TID_ROUTE or TDEST_ROUTE");
end
/* verilator lint_on GENUNNAMED */

logic [CL_M_COUNT-1:0] select_reg, select_ctl, select_next;
logic [M_COUNT-1:0] dest_mask_reg, dest_mask_ctl, dest_mask_next;
logic drop_reg, drop_ctl, drop_next;
logic frame_reg, frame_ctl, frame_next;

logic s_axis_tready_reg, s_axis_tready_next;

// internal datapath
logic [DATA_W-1:0]    m_axis_tdata_int;
logic [KEEP_W-1:0]    m_axis_tkeep_int;
logic [KEEP_W-1:0]    m_axis_tstrb_int;
logic [M_COUNT-1:0]   m_axis_tvalid_int;
logic                 m_axis_tready_int_reg;
logic                 m_axis_tlast_int;
logic [M_ID_W-1:0]    m_axis_tid_int;
logic [M_DEST_W-1:0]  m_axis_tdest_int;
logic [USER_W-1:0]    m_axis_tuser_int;
wire                  m_axis_tready_int_early;

assign s_axis.tready = s_axis_tready_reg && enable;

always_comb begin
    select_next = select_reg;
    select_ctl = select_reg;
    dest_mask_next = dest_mask_reg;
    dest_mask_ctl = dest_mask_reg;
    drop_next = drop_reg;
    drop_ctl = drop_reg;
    frame_next = frame_reg;
    frame_ctl = frame_reg;

    if (s_axis.tvalid && s_axis.tready) begin
        // end of frame detection
        if (s_axis.tlast) begin
            frame_next = 1'b0;
            drop_next = 1'b0;
        end
    end

    if (!frame_reg && s_axis.tvalid && s_axis.tready) begin
        // start of frame, grab select value
        if (TID_ROUTE) begin
            if (M_COUNT > 1) begin
                select_ctl = s_axis.tid[S_ID_W-1:S_ID_W-CL_M_COUNT];
                drop_ctl = (CL_M_COUNT+1)'(select_ctl) >= (CL_M_COUNT+1)'(M_COUNT);
            end else begin
                select_ctl = '0;
                drop_ctl = 1'b0;
            end
        end else if (TDEST_ROUTE) begin
            if (M_COUNT > 1) begin
                select_ctl = s_axis.tdest[S_DEST_W-1:S_DEST_W-CL_M_COUNT];
                drop_ctl = (CL_M_COUNT+1)'(select_ctl) >= (CL_M_COUNT+1)'(M_COUNT);
            end else begin
                select_ctl = '0;
                drop_ctl = 1'b0;
            end
        end else if (TUSER_BITMAP_ROUTE) begin
            dest_mask_ctl = s_axis.tuser[M_COUNT-1:0];
            // tuser all zeros -> drop the package
            drop_ctl = (dest_mask_ctl == '0);
        end else begin
            select_ctl = select;
            drop_ctl = drop || (CL_M_COUNT+1)'(select) >= (CL_M_COUNT+1)'(M_COUNT);
        end

        if (!TUSER_BITMAP_ROUTE) begin
            dest_mask_ctl = '0;
            dest_mask_ctl[select_ctl] = 1'b1;
        end

        frame_ctl = 1'b1;
        if (!(s_axis.tready && s_axis.tvalid && s_axis.tlast)) begin
            select_next = select_ctl;
            dest_mask_next = dest_mask_ctl;
            drop_next = drop_ctl;
            frame_next = 1'b1;
        end
    end

    m_axis_tdata_int  = s_axis.tdata;
    m_axis_tkeep_int  = s_axis.tkeep;
    m_axis_tstrb_int  = s_axis.tstrb;
    m_axis_tvalid_int = '0;
    m_axis_tvalid_int = dest_mask_ctl & {M_COUNT{s_axis.tvalid && s_axis.tready && !drop_ctl}};
    m_axis_tlast_int  = s_axis.tlast;
    m_axis_tid_int    = M_ID_W'(s_axis.tid);
    m_axis_tdest_int  = M_DEST_W'(s_axis.tdest);
    m_axis_tuser_int  = s_axis.tuser;
end

always_comb begin
    s_axis_tready_next = (m_axis_tready_int_early || drop_ctl);
end

always_ff @(posedge clk) begin
    select_reg <= select_next;
    dest_mask_reg <= dest_mask_next;
    drop_reg <= drop_next;
    frame_reg <= frame_next;
    s_axis_tready_reg <= s_axis_tready_next;

    if (rst) begin
        select_reg <= '0;
        dest_mask_reg <= '0;
        drop_reg <= 1'b0;
        frame_reg <= 1'b0;
        s_axis_tready_reg <= 1'b0;
    end
end

// output datapath logic
logic [DATA_W-1:0]    m_axis_tdata_reg;
logic [KEEP_W-1:0]    m_axis_tkeep_reg;
logic [KEEP_W-1:0]    m_axis_tstrb_reg;
logic [M_COUNT-1:0]   m_axis_mask_reg, m_axis_mask_next;
logic                 m_axis_occupied_reg, m_axis_occupied_next;
logic                 m_axis_tlast_reg;
logic [M_ID_W-1:0]    m_axis_tid_reg;
logic [M_DEST_W-1:0]  m_axis_tdest_reg;
logic [USER_W-1:0]    m_axis_tuser_reg;

logic [DATA_W-1:0]    temp_m_axis_tdata_reg;
logic [KEEP_W-1:0]    temp_m_axis_tkeep_reg;
logic [KEEP_W-1:0]    temp_m_axis_tstrb_reg;
logic [M_COUNT-1:0]   temp_m_axis_mask_reg, temp_m_axis_mask_next;
logic                 temp_m_axis_occupied_reg, temp_m_axis_occupied_next;
logic                 temp_m_axis_tlast_reg;
logic [M_ID_W-1:0]    temp_m_axis_tid_reg;
logic [M_DEST_W-1:0]  temp_m_axis_tdest_reg;
logic [USER_W-1:0]    temp_m_axis_tuser_reg;

// datapath control
logic store_axis_int_to_output;
logic store_axis_int_to_temp;
logic store_axis_temp_to_output;

wire [M_COUNT-1:0] m_axis_tready;

// check all all ports from the mask are ready
function automatic logic all_targets_ready(
    logic [M_COUNT-1:0] mask,
    logic [M_COUNT-1:0] ready_vec
);
    return &(ready_vec | ~mask);
endfunction

wire output_targets_ready = all_targets_ready(m_axis_mask_reg, m_axis_tready);
wire temp_targets_ready   = all_targets_ready(temp_m_axis_mask_reg, m_axis_tready);

for (genvar k = 0; k < M_COUNT; k = k + 1) begin : m_axis_gen
    assign m_axis[k].tdata  = m_axis_tdata_reg;
    assign m_axis[k].tkeep  = KEEP_EN ? m_axis_tkeep_reg : '1;
    assign m_axis[k].tstrb  = STRB_EN ? m_axis_tstrb_reg : m_axis[k].tkeep;
    assign m_axis[k].tvalid = m_axis_occupied_reg && m_axis_mask_reg[k] && output_targets_ready;
    assign m_axis[k].tlast  = m_axis_tlast_reg;
    assign m_axis[k].tid    = ID_EN   ? m_axis_tid_reg   : '0;
    assign m_axis[k].tdest  = DEST_EN ? m_axis_tdest_reg : '0;
    assign m_axis[k].tuser  = USER_EN ? m_axis_tuser_reg : '0;

    assign m_axis_tready[k] = m_axis[k].tready;
end

// enable ready input next cycle if a free slot exists: output reg is empty or all targets are ready (draining), and temp reg is empty or will drain into output (all targets ready while output frees)
assign m_axis_tready_int_early =
    (!m_axis_occupied_reg || output_targets_ready)
    && (!temp_m_axis_occupied_reg || temp_targets_ready || !m_axis_occupied_reg || output_targets_ready);

always_comb begin
    m_axis_mask_next = m_axis_mask_reg;
    m_axis_occupied_next = m_axis_occupied_reg;
    temp_m_axis_mask_next = temp_m_axis_mask_reg;
    temp_m_axis_occupied_next = temp_m_axis_occupied_reg;

    store_axis_int_to_output = 1'b0;
    store_axis_int_to_temp = 1'b0;
    store_axis_temp_to_output = 1'b0;

    // check if output can be freed (handshake happened)
    if (m_axis_occupied_reg && output_targets_ready) begin
        m_axis_occupied_next = 1'b0;
    end

    // check if temp can be moved to output
    if (temp_m_axis_occupied_reg && temp_targets_ready &&
        (!m_axis_occupied_reg || output_targets_ready)) begin
        m_axis_mask_next = temp_m_axis_mask_reg;
        m_axis_occupied_next = 1'b1;
        temp_m_axis_occupied_next = 1'b0;
        store_axis_temp_to_output = 1'b1;
    end

    // input is ready
    if (m_axis_tready_int_reg && s_axis.tvalid && s_axis.tready && !drop_ctl) begin
        // output is ready, store directly to output
        if (!m_axis_occupied_reg || (output_targets_ready && !store_axis_temp_to_output)) begin
            m_axis_mask_next = dest_mask_ctl;
            m_axis_occupied_next = 1'b1;
            store_axis_int_to_output = 1'b1;
        end else begin
            // output is not ready, store input in temp
            temp_m_axis_mask_next = dest_mask_ctl;
            temp_m_axis_occupied_next = 1'b1;
            store_axis_int_to_temp = 1'b1;
        end
    end
end

always_ff @(posedge clk) begin
    m_axis_mask_reg <= m_axis_mask_next;
    m_axis_occupied_reg <= m_axis_occupied_next;
    m_axis_tready_int_reg <= m_axis_tready_int_early;
    temp_m_axis_mask_reg <= temp_m_axis_mask_next;
    temp_m_axis_occupied_reg <= temp_m_axis_occupied_next;

    // datapath
    if (store_axis_int_to_output) begin
        m_axis_tdata_reg <= m_axis_tdata_int;
        m_axis_tkeep_reg <= m_axis_tkeep_int;
        m_axis_tstrb_reg <= m_axis_tstrb_int;
        m_axis_tlast_reg <= m_axis_tlast_int;
        m_axis_tid_reg   <= m_axis_tid_int;
        m_axis_tdest_reg <= m_axis_tdest_int;
        m_axis_tuser_reg <= m_axis_tuser_int;
    end else if (store_axis_temp_to_output) begin
        m_axis_tdata_reg <= temp_m_axis_tdata_reg;
        m_axis_tkeep_reg <= temp_m_axis_tkeep_reg;
        m_axis_tstrb_reg <= temp_m_axis_tstrb_reg;
        m_axis_tlast_reg <= temp_m_axis_tlast_reg;
        m_axis_tid_reg   <= temp_m_axis_tid_reg;
        m_axis_tdest_reg <= temp_m_axis_tdest_reg;
        m_axis_tuser_reg <= temp_m_axis_tuser_reg;
    end

    if (store_axis_int_to_temp) begin
        temp_m_axis_tdata_reg <= m_axis_tdata_int;
        temp_m_axis_tkeep_reg <= m_axis_tkeep_int;
        temp_m_axis_tstrb_reg <= m_axis_tstrb_int;
        temp_m_axis_tlast_reg <= m_axis_tlast_int;
        temp_m_axis_tid_reg   <= m_axis_tid_int;
        temp_m_axis_tdest_reg <= m_axis_tdest_int;
        temp_m_axis_tuser_reg <= m_axis_tuser_int;
    end

    if (rst) begin
        m_axis_tready_int_reg <= 1'b0;

        m_axis_tdata_reg <= '0;
        m_axis_tkeep_reg <= '0;
        m_axis_tstrb_reg <= '0;
        m_axis_mask_reg <= '0;
        m_axis_occupied_reg <= 1'b0;
        m_axis_tlast_reg <= 1'b0;
        m_axis_tid_reg   <= '0;
        m_axis_tdest_reg <= '0;
        m_axis_tuser_reg <= '0;

        temp_m_axis_tdata_reg <= '0;
        temp_m_axis_tkeep_reg <= '0;
        temp_m_axis_tstrb_reg <= '0;
        temp_m_axis_mask_reg <= '0;
        temp_m_axis_occupied_reg <= 1'b0;
        temp_m_axis_tlast_reg <= 1'b0;
        temp_m_axis_tid_reg   <= '0;
        temp_m_axis_tdest_reg <= '0;
        temp_m_axis_tuser_reg <= '0;
    end
end
endmodule

`resetall
