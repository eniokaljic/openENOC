// SPDX-FileCopyrightText: 2026 Kerim Bavcic
// SPDX-License-Identifier: CERN-OHL-S-2.0

`resetall
`timescale 1ns / 1ps
`default_nettype none

/*
 * openENOC forwarding engine (AXI4-Stream)
 *
 * The engine parses the Ethernet destination and source MAC addresses
 * and sends them to the forwarding table for lookup and learning.
 *
 */
module openenoc_axis_forwarding_engine #
(
    parameter int NUM_OF_INTERFACES = 8
)
(
    input  wire logic                         clk,
    input  wire logic                         rst,

    /*
     * Pause at a frame boundary
     */
    input  wire logic                         pause_request,
    output logic                              pause_done,

    /*
     * AXI4-Stream input (sink), tid carries the ingress interface index
     */
    taxi_axis_if.snk                          s_axis,

    /*
     * AXI4-Stream output (source), tuser carries the egress interface bitmap
     */
    taxi_axis_if.src                          m_axis,

    /*
     * Lookup interface (openenoc_forwarding_table)
     */
    output logic                              lookup_req,
    output logic [47:0]                       lookup_mac_addr,
    input  wire logic                         lookup_ack,
    input  wire logic [NUM_OF_INTERFACES-1:0] lookup_port_bitmap,

    /*
     * Learning interface (openenoc_forwarding_table)
     */
    output logic                              learning_req,
    output logic [47:0]                       learning_mac_addr,
    output logic [NUM_OF_INTERFACES-1:0]      learning_port_bitmap,
    input  wire logic                         learning_ack
);

    localparam int   DATA_W   = s_axis.DATA_W;
    localparam int   KEEP_W   = s_axis.KEEP_W;
    localparam logic KEEP_EN  = s_axis.KEEP_EN;
    localparam logic STRB_EN  = s_axis.STRB_EN;
    localparam logic LAST_EN  = s_axis.LAST_EN;
    localparam logic ID_EN    = s_axis.ID_EN;
    localparam int   ID_W     = s_axis.ID_W;
    localparam int   DEST_W   = s_axis.DEST_W;
    localparam int   M_ID_W   = m_axis.ID_W;
    localparam int   M_DEST_W = m_axis.DEST_W;
    localparam int   M_USER_W = m_axis.USER_W;

    localparam int MAC_W        = 48;
    localparam int DA_BYTES     = 6;
    localparam int HEADER_BYTES = 12;
    localparam int HEADER_BEATS = (HEADER_BYTES + KEEP_W - 1) / KEEP_W;
    localparam int BYTE_CNT_W   = $clog2(HEADER_BYTES+1);
    localparam int VALID_CNT_W  = $clog2(KEEP_W+1);
    localparam int SUM_W        = ((BYTE_CNT_W > VALID_CNT_W) ? BYTE_CNT_W : VALID_CNT_W) + 1;
    localparam int CL_IFACE     = (NUM_OF_INTERFACES > 1) ? $clog2(NUM_OF_INTERFACES) : 1;

    /* verilator lint_off GENUNNAMED */
    if (NUM_OF_INTERFACES < 1 || NUM_OF_INTERFACES > 32)
        $fatal(0, "Error: NUM_OF_INTERFACES must be in range 1 to 32 (instance %m)");

    if (DATA_W < 8 || DATA_W > 512 || DATA_W % 8 != 0)
        $fatal(0, "Error: DATA_W must be a multiple of 8 in range 8 to 512 (instance %m)");

    if (KEEP_W * 8 != DATA_W)
        $fatal(0, "Error: interface requires byte granularity (instance %m)");

    if (m_axis.DATA_W != DATA_W || m_axis.KEEP_W != KEEP_W)
        $fatal(0, "Error: AXI4-Stream data interface parameter mismatch (instance %m)");

    if (m_axis.KEEP_EN != KEEP_EN)
        $fatal(0, "Error: s_axis and m_axis KEEP_EN must match (instance %m)");

    if (!LAST_EN || !ID_EN)
        $fatal(0, "Error: s_axis LAST_EN and ID_EN are required (instance %m)");

    if (!m_axis.LAST_EN || !m_axis.ID_EN)
        $fatal(0, "Error: m_axis LAST_EN and ID_EN are required (instance %m)");

    if (ID_W < CL_IFACE)
        $fatal(0, "Error: s_axis ID_W is too small for NUM_OF_INTERFACES (instance %m)");

    if (!m_axis.USER_EN || M_USER_W < NUM_OF_INTERFACES)
        $fatal(0, "Error: m_axis tuser is too small for the forwarding bitmap (instance %m)");
    /* verilator lint_on GENUNNAMED */

    function automatic logic [NUM_OF_INTERFACES-1:0] port_onehot(input logic [ID_W-1:0] index);
        if ({1'b0, index} < (ID_W+1)'(NUM_OF_INTERFACES))
            port_onehot = NUM_OF_INTERFACES'(1) << index;
        else
            port_onehot = '0;
    endfunction

    typedef enum logic [2:0] {
        ST_PARSE_DA,
        ST_WAIT_LOOKUP,
        ST_PARSE_SA,
        ST_WAIT_LEARNING,
        ST_RELEASE
    } state_t;

    state_t state_reg;

    logic [MAC_W-1:0] da_reg;
    logic [MAC_W-1:0] sa_reg;
    logic [MAC_W-1:0] da_next;
    logic [MAC_W-1:0] sa_next;
    logic [BYTE_CNT_W-1:0] byte_count_reg;
    logic [ID_W-1:0] ingress_port_reg;
    logic frame_input_done_reg;
    logic [NUM_OF_INTERFACES-1:0] forwarding_bitmap_reg;

    // ---------------------------------------------------------------------------
    // Register-only frame header buffer
    // ---------------------------------------------------------------------------
    taxi_axis_if #(
        .DATA_W(DATA_W),
        .KEEP_EN(KEEP_EN),
        .KEEP_W(KEEP_W),
        .STRB_EN(STRB_EN),
        .LAST_EN(LAST_EN),
        .ID_EN(ID_EN),
        .ID_W(ID_W),
        .DEST_EN(s_axis.DEST_EN),
        .DEST_W(DEST_W),
        .USER_EN(1'b0),
        .USER_W(1)
    ) buffer_s_axis(), buffer_m_axis();

    wire accept_frame_data = state_reg == ST_PARSE_DA ||
                            state_reg == ST_PARSE_SA ||
                            (state_reg == ST_RELEASE && !frame_input_done_reg);
    wire at_frame_boundary = state_reg == ST_PARSE_DA && byte_count_reg == '0;
    wire pause_new_frame = pause_request && at_frame_boundary;
    wire accept_enable = accept_frame_data && !pause_new_frame;

    assign buffer_s_axis.tdata  = s_axis.tdata;
    assign buffer_s_axis.tkeep  = s_axis.tkeep;
    assign buffer_s_axis.tstrb  = s_axis.tstrb;
    assign buffer_s_axis.tvalid = s_axis.tvalid && accept_enable;
    assign buffer_s_axis.tlast  = s_axis.tlast;
    assign buffer_s_axis.tid    = s_axis.tid;
    assign buffer_s_axis.tdest  = s_axis.tdest;
    assign buffer_s_axis.tuser  = '0;
    assign s_axis.tready        = buffer_s_axis.tready && accept_enable;

    // REG_TYPE=2 is the taxi skid-buffer implementation. Unlike taxi_axis_fifo,
    // all storage here is implemented as a small fixed chain of registers.
    taxi_axis_pipeline_register #(
        .REG_TYPE(2),
        .LENGTH(HEADER_BEATS)
    )
    header_buffer_inst (
        .clk(clk),
        .rst(rst),
        .s_axis(buffer_s_axis),
        .m_axis(buffer_m_axis)
    );

    wire release_frame = state_reg == ST_RELEASE;
    wire [KEEP_W-1:0] output_keep = m_axis.KEEP_EN ? buffer_m_axis.tkeep : '1;
    wire output_valid = buffer_m_axis.tvalid && release_frame;
    wire output_last = buffer_m_axis.tlast;

    assign m_axis.tdata  = buffer_m_axis.tdata;
    assign m_axis.tkeep  = output_keep;
    assign m_axis.tstrb  = m_axis.STRB_EN ? buffer_m_axis.tstrb : output_keep;
    assign m_axis.tvalid = output_valid;
    assign m_axis.tlast  = output_last;
    assign m_axis.tid    = M_ID_W'(buffer_m_axis.tid);
    assign m_axis.tdest  = M_DEST_W'(buffer_m_axis.tdest);
    assign m_axis.tuser  = M_USER_W'(forwarding_bitmap_reg);
    assign buffer_m_axis.tready = m_axis.tready && release_frame;

    wire s_fire = s_axis.tvalid && s_axis.tready;
    wire m_fire = output_valid && m_axis.tready;

    // ---------------------------------------------------------------------------
    // Ethernet MAC parser
    // ---------------------------------------------------------------------------
    wire [VALID_CNT_W-1:0] valid_bytes = KEEP_EN ?
        VALID_CNT_W'($countones(s_axis.tkeep)) : VALID_CNT_W'(KEEP_W);
    wire [SUM_W-1:0] byte_count_sum = SUM_W'(byte_count_reg) + SUM_W'(valid_bytes);
    wire da_complete = byte_count_sum >= SUM_W'(DA_BYTES);
    wire sa_complete = byte_count_sum >= SUM_W'(HEADER_BYTES);

    always_comb begin
        da_next = da_reg;
        sa_next = sa_reg;

        for (int lane = 0; lane < KEEP_W; lane++) begin
            int byte_index;
            byte_index = int'(byte_count_reg) + lane;

            if ((!KEEP_EN || s_axis.tkeep[lane]) && byte_index < HEADER_BYTES) begin
                if (byte_index < DA_BYTES)
                    da_next[MAC_W-1-byte_index*8 -: 8] = s_axis.tdata[lane*8 +: 8];
                else
                    sa_next[MAC_W-1-(byte_index-DA_BYTES)*8 -: 8] = s_axis.tdata[lane*8 +: 8];
            end
        end
    end

    // ---------------------------------------------------------------------------
    // Transaction sequencing
    // ---------------------------------------------------------------------------
    always_ff @(posedge clk) begin
        // Requests are one-cycle strobes. Payload registers remain stable while
        // the engine waits for the corresponding acknowledge.
        lookup_req   <= 1'b0;
        learning_req <= 1'b0;

        if (s_fire) begin
            da_reg <= da_next;
            sa_reg <= sa_next;

            if (byte_count_reg == 0)
                ingress_port_reg <= s_axis.tid;

            if (sa_complete)
                byte_count_reg <= BYTE_CNT_W'(HEADER_BYTES);
            else
                byte_count_reg <= BYTE_CNT_W'(byte_count_sum);

            if (s_axis.tlast)
                frame_input_done_reg <= 1'b1;
        end

        case (state_reg)
            ST_PARSE_DA: begin
                if (s_fire && s_axis.tlast && !da_complete) begin
                    // No complete destination address: no lookup or learning is
                    // possible. Release the malformed frame with bitmap zero.
                    forwarding_bitmap_reg <= '0;
                    state_reg <= ST_RELEASE;
                end else if (s_fire && da_complete) begin
                    lookup_mac_addr <= da_next;
                    lookup_req <= 1'b1;
                    state_reg <= ST_WAIT_LOOKUP;
                end
            end

            ST_WAIT_LOOKUP: begin
                if (lookup_ack) begin
                    forwarding_bitmap_reg <= lookup_port_bitmap &
                                            ~port_onehot(ingress_port_reg);

                    // A wide beat may already contain the whole source address.
                    if (byte_count_reg >= BYTE_CNT_W'(HEADER_BYTES)) begin
                        learning_mac_addr <= sa_reg;
                        learning_port_bitmap <= port_onehot(ingress_port_reg);
                        learning_req <= 1'b1;
                        state_reg <= ST_WAIT_LEARNING;
                    end else if (frame_input_done_reg) begin
                        // Frame ended after DA but before SA; lookup is valid but
                        // there is no complete source address to learn.
                        state_reg <= ST_RELEASE;
                    end else begin
                        state_reg <= ST_PARSE_SA;
                    end
                end
            end

            ST_PARSE_SA: begin
                if (s_fire && sa_complete) begin
                    // Every complete source address is sent to the table. Managed
                    // mode policy, if enabled, belongs to the table itself.
                    learning_mac_addr <= sa_next;
                    learning_port_bitmap <= port_onehot(ingress_port_reg);
                    learning_req <= 1'b1;
                    state_reg <= ST_WAIT_LEARNING;
                end else if (s_fire && s_axis.tlast) begin
                    // Incomplete SA: release after lookup, without learning.
                    state_reg <= ST_RELEASE;
                end
            end

            ST_WAIT_LEARNING: begin
                if (learning_ack)
                    state_reg <= ST_RELEASE;
            end

            ST_RELEASE: begin
                if (m_fire && output_last) begin
                    state_reg <= ST_PARSE_DA;
                    da_reg <= '0;
                    sa_reg <= '0;
                    byte_count_reg <= '0;
                    ingress_port_reg <= '0;
                    frame_input_done_reg <= 1'b0;
                    forwarding_bitmap_reg <= '0;
                end
            end

            default: state_reg <= ST_PARSE_DA;
        endcase

        if (rst) begin
            state_reg <= ST_PARSE_DA;
            da_reg <= '0;
            sa_reg <= '0;
            byte_count_reg <= '0;
            ingress_port_reg <= '0;
            frame_input_done_reg <= 1'b0;
            forwarding_bitmap_reg <= '0;
            lookup_req <= 1'b0;
            lookup_mac_addr <= '0;
            learning_req <= 1'b0;
            learning_mac_addr <= '0;
            learning_port_bitmap <= '0;
        end
    end

    // A pause is complete only at a frame boundary after the register pipeline has
    // drained. No new frame is accepted while pause_request remains asserted.
    assign pause_done = pause_request && at_frame_boundary &&
                        !buffer_m_axis.tvalid && !lookup_req && !learning_req;

endmodule

`resetall
