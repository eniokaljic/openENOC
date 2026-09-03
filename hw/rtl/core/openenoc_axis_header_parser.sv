// SPDX-FileCopyrightText: 2026 Kerim Bavcic
// SPDX-License-Identifier: CERN-OHL-S-2.0

`resetall
`timescale 1ns / 1ps
`default_nettype none

/*
 * AXI4-Stream openENOC header parser
 *
 * Snoops the first 16 bytes of each frame and presents them, stable for the
 * whole output frame, on the 128-bit m_axis.tuser. tdata is passed through
 * unchanged, delayed by the header (~16 bytes) so that tuser is valid from the
 * first output beat. No field splitting - raw 128-bit header on tuser.
 *
 *   tuser[127:80] = Destination MAC (6B)
 *   tuser[79:32]  = Source MAC      (6B)
 *   tuser[31:16]  = EtherType       (2B)
 *   tuser[15:8]   = oETP Magic      (1B)
 *   tuser[7:0]    = oETP Cmd        (1B)
 * (byte 0 = first byte on the wire = MSB)
 */
module openenoc_axis_header_parser #
(
    // Data buffer depth in cycles (0 = auto = 2x header beats)
    parameter DEPTH = 0,
    // Output interface register type
    // 0 to bypass, 1 for simple buffer, 2 for skid buffer
    parameter M_REG_TYPE = 2
)
(
    input  wire logic  clk,
    input  wire logic  rst,

    /*
     * AXI4-Stream input (sink) - raw frames
     */
    taxi_axis_if.snk   s_axis,

    /*
     * AXI4-Stream output (source) - delayed frames, 128-bit header on tuser
     */
    taxi_axis_if.src   m_axis
);

    // ---------------------------------------------------------------------------
    // parameters
    // ---------------------------------------------------------------------------
    localparam DATA_W = s_axis.DATA_W;
    localparam logic KEEP_EN = s_axis.KEEP_EN;
    localparam KEEP_W = s_axis.KEEP_W;
    localparam logic STRB_EN = s_axis.STRB_EN;
    localparam logic LAST_EN = s_axis.LAST_EN;

    localparam M_USER_W = m_axis.USER_W;

    localparam HDR_BYTES = 16;
    localparam HDR_W = HDR_BYTES*8;                        // 128
    localparam BCW = $clog2(HDR_BYTES+1);                  // byte-count width

    // number of full beats the header spans
    localparam DELAY_B = (HDR_BYTES + KEEP_W - 1)/KEEP_W;

    // data buffer sizing (power-of-2 cycles)
    localparam REQ_CYC = (DEPTH == 0) ? (2*DELAY_B) : DEPTH;
    localparam FIFO_AW = $clog2(REQ_CYC < 2 ? 2 : REQ_CYC);
    localparam FIFO_CYC = 2**FIFO_AW;

    // one header slot per possible buffered beat -> cannot overflow
    localparam HDR_SLOTS = FIFO_CYC;
    localparam HDR_AW = FIFO_AW;

    // check configuration
    /* verilator lint_off GENUNNAMED */
    if (DATA_W % 8 != 0)
        $fatal(0, "Error: DATA_W must be a multiple of 8 (instance %m)");

    if (m_axis.DATA_W != DATA_W)
        $fatal(0, "Error: Interface DATA_W parameter mismatch (instance %m)");

    if (M_USER_W < HDR_W)
        $fatal(0, "Error: m_axis USER_W must be >= 128 (instance %m)");

    if (!LAST_EN)
        $fatal(0, "Error: LAST_EN is required (instance %m)");
    /* verilator lint_on GENUNNAMED */

    // ---------------------------------------------------------------------------
    // data path: plain AXIS FIFO (delay line), s_axis -> buf_axis_if
    // ---------------------------------------------------------------------------
    taxi_axis_if #(
        .DATA_W(DATA_W),
        .KEEP_EN(KEEP_EN),
        .KEEP_W(KEEP_W),
        .STRB_EN(STRB_EN),
        .LAST_EN(LAST_EN),
        .ID_EN(1'b0),
        .DEST_EN(1'b0),
        .USER_EN(1'b0),
        .USER_W(1)
    ) buf_axis_if();

    taxi_axis_fifo #(
        .DEPTH(FIFO_CYC*KEEP_W),
        .FRAME_FIFO(1'b0)
    )
    u_data_fifo (
        .clk(clk),
        .rst(rst),
        .s_axis(s_axis),
        .m_axis(buf_axis_if),
        .pause_req(1'b0),
        .pause_ack(),
        .status_depth(),
        .status_depth_commit(),
        .status_overflow(),
        .status_bad_frame(),
        .status_good_frame()
    );

    // ---------------------------------------------------------------------------
    // input snoop: assemble the 16-byte header for the current input frame
    // ---------------------------------------------------------------------------
    wire s_fire = s_axis.tvalid && s_axis.tready;

    logic [HDR_W-1:0] cap_hdr_reg;
    logic [BCW-1:0]   cap_cnt_reg;    // bytes captured this frame (saturating at 16)
    logic             cap_done_reg;   // header already pushed for current frame

    logic [HDR_W-1:0] cap_hdr_comb;
    logic [BCW:0]     valid_bytes;

    always_comb begin
        valid_bytes = KEEP_EN ? (BCW+1)'($countones(s_axis.tkeep)) : (BCW+1)'(KEEP_W);

        cap_hdr_comb = cap_hdr_reg;
        for (int j = 0; j < KEEP_W; j++) begin
            int bidx;
            bidx = int'(cap_cnt_reg) + j;   // contiguous keep from lane 0 assumed
            if ((!KEEP_EN || s_axis.tkeep[j]) && bidx < HDR_BYTES)
                cap_hdr_comb[HDR_W-1 - bidx*8 -: 8] = s_axis.tdata[j*8 +: 8];
        end
    end

    wire hdr_complete_now =
        ((int'(cap_cnt_reg) + int'(valid_bytes)) >= HDR_BYTES) || s_axis.tlast;

    wire hdr_push = s_fire && !cap_done_reg && hdr_complete_now;

    always_ff @(posedge clk) begin
        if (s_fire) begin
            cap_hdr_reg <= cap_hdr_comb;
            cap_cnt_reg <= ((int'(cap_cnt_reg) + int'(valid_bytes)) >= HDR_BYTES)
                ? BCW'(HDR_BYTES) : cap_cnt_reg + BCW'(valid_bytes);
            if (hdr_complete_now)
                cap_done_reg <= 1'b1;
            if (s_axis.tlast) begin
                cap_hdr_reg  <= '0;
                cap_cnt_reg  <= '0;
                cap_done_reg <= 1'b0;
            end
        end

        if (rst) begin
            cap_hdr_reg  <= '0;
            cap_cnt_reg  <= '0;
            cap_done_reg <= 1'b0;
        end
    end

    // ---------------------------------------------------------------------------
    // header store: small FIFO, one 128-bit header per frame, in order
    // ---------------------------------------------------------------------------
    logic [HDR_W-1:0] hdr_mem[HDR_SLOTS];
    logic [HDR_AW:0]  hdr_wr_ptr, hdr_rd_ptr;

    wire hdr_empty = (hdr_wr_ptr == hdr_rd_ptr);
    wire [HDR_W-1:0] hdr_head = hdr_mem[hdr_rd_ptr[HDR_AW-1:0]];

    // ---------------------------------------------------------------------------
    // output gate: withhold frame start until its header is ready; drive tuser
    // gate_axis_if mirrors m_axis and feeds the optional output register
    // ---------------------------------------------------------------------------
    taxi_axis_if #(
        .DATA_W(DATA_W),
        .KEEP_EN(m_axis.KEEP_EN),
        .KEEP_W(m_axis.KEEP_W),
        .STRB_EN(m_axis.STRB_EN),
        .LAST_EN(m_axis.LAST_EN),
        .ID_EN(m_axis.ID_EN),
        .ID_W(m_axis.ID_W),
        .DEST_EN(m_axis.DEST_EN),
        .DEST_W(m_axis.DEST_W),
        .USER_EN(m_axis.USER_EN),
        .USER_W(M_USER_W)
    ) gate_axis_if();

    logic             out_active_reg;
    logic [HDR_W-1:0] cur_hdr_reg;

    wire out_go = out_active_reg || !hdr_empty;

    assign gate_axis_if.tvalid = buf_axis_if.tvalid && out_go;
    assign buf_axis_if.tready  = gate_axis_if.tready && out_go;

    assign gate_axis_if.tdata = buf_axis_if.tdata;
    assign gate_axis_if.tkeep = m_axis.KEEP_EN ? buf_axis_if.tkeep : '1;
    assign gate_axis_if.tstrb = m_axis.STRB_EN ? buf_axis_if.tstrb : gate_axis_if.tkeep;
    assign gate_axis_if.tlast = buf_axis_if.tlast;
    assign gate_axis_if.tid   = '0;
    assign gate_axis_if.tdest = '0;
    assign gate_axis_if.tuser = M_USER_W'(out_active_reg ? cur_hdr_reg : hdr_head);

    wire m_fire = gate_axis_if.tvalid && gate_axis_if.tready;

    always_ff @(posedge clk) begin
        // header FIFO write
        if (hdr_push) begin
            hdr_mem[hdr_wr_ptr[HDR_AW-1:0]] <= cap_hdr_comb;
            hdr_wr_ptr <= hdr_wr_ptr + 1;
        end

        // output frame tracking
        if (m_fire) begin
            if (!out_active_reg) begin
                out_active_reg <= 1'b1;
                cur_hdr_reg    <= hdr_head;
            end
            if (gate_axis_if.tlast) begin
                out_active_reg <= 1'b0;
                hdr_rd_ptr     <= hdr_rd_ptr + 1;   // pop consumed frame's header
            end
        end

        if (rst) begin
            hdr_wr_ptr     <= '0;
            hdr_rd_ptr     <= '0;
            out_active_reg <= 1'b0;
            cur_hdr_reg    <= '0;
        end
    end

    // ---------------------------------------------------------------------------
    // optional output register (skid), gate_axis_if -> m_axis
    // ---------------------------------------------------------------------------
    taxi_axis_register #(
        .REG_TYPE(M_REG_TYPE)
    )
    u_m_reg (
        .clk(clk),
        .rst(rst),
        .s_axis(gate_axis_if),
        .m_axis(m_axis)
    );

endmodule

`resetall
