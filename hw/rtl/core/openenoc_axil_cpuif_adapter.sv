// SPDX-FileCopyrightText: 2026 Enio Kaljic
// SPDX-License-Identifier: CERN-OHL-S-2.0

`resetall
`timescale 1ns / 1ps
`default_nettype none

/* AXI4-Lite slave to native CPUIF master adapter. */
module openenoc_axil_cpuif_adapter #(
    parameter int unsigned RESPONSE_FIFO_DEPTH = 2
) (
    input wire logic clk,
    input wire logic rst,
    taxi_axil_if.wr_slv s_axil_wr,
    taxi_axil_if.rd_slv s_axil_rd,
    openenoc_cpuif_if.mst m_cpuif
);

    localparam int unsigned DATA_W = m_cpuif.DATA_W;
    localparam int unsigned ADDR_W = m_cpuif.ADDR_W;
    localparam int unsigned STRB_W = DATA_W / 8;
    localparam int unsigned BYTE_W = DATA_W / STRB_W;
    localparam int unsigned RESP_PTR_W = RESPONSE_FIFO_DEPTH > 1 ? $clog2(RESPONSE_FIFO_DEPTH) : 1;
    localparam int unsigned RESP_COUNT_W = $clog2(RESPONSE_FIFO_DEPTH + 1);

    if (DATA_W % 8 != 0) begin : g_data_width_error
        $fatal(0, "Error: CPUIF data width must be a multiple of eight (instance %m)");
    end

    if (RESPONSE_FIFO_DEPTH < 2) begin : g_response_fifo_depth_error
        $fatal(0, "Error: response FIFO depth must be at least two (instance %m)");
    end

    if (s_axil_wr.DATA_W != DATA_W || s_axil_rd.DATA_W != DATA_W || s_axil_wr.STRB_W != STRB_W
        || s_axil_rd.STRB_W != STRB_W) begin : g_data_width_mismatch
        $fatal(0, "Error: CPUIF and AXI4-Lite data widths do not match (instance %m)");
    end

    if (s_axil_wr.ADDR_W != ADDR_W || s_axil_rd.ADDR_W != ADDR_W) begin : g_addr_width_mismatch
        $fatal(0, "Error: CPUIF and AXI4-Lite address widths do not match (instance %m)");
    end

    function automatic logic [DATA_W-1:0] strb_to_biten(input logic [STRB_W-1:0] strb);
        for (int unsigned lane = 0; lane < STRB_W; lane++) begin
            strb_to_biten[lane*BYTE_W+:BYTE_W] = {BYTE_W{strb[lane]}};
        end
    endfunction

    function automatic logic [RESP_PTR_W-1:0] next_resp_ptr(input logic [RESP_PTR_W-1:0] ptr);
        if (ptr == RESP_PTR_W'(RESPONSE_FIFO_DEPTH - 1)) begin
            next_resp_ptr = '0;
        end else begin
            next_resp_ptr = ptr + 1'b1;
        end
    endfunction

    /* Independent fall-through AXI request buffers. */
    logic aw_buf_valid_reg;
    logic [ADDR_W-1:0] aw_buf_addr_reg;
    logic w_buf_valid_reg;
    logic [DATA_W-1:0] w_buf_data_reg;
    logic [STRB_W-1:0] w_buf_strb_reg;
    logic ar_buf_valid_reg;
    logic [ADDR_W-1:0] ar_buf_addr_reg;

    /* One active CPUIF operation; CPUIF has no request-ready signal. */
    logic cpuif_pending_reg;
    logic cpuif_pending_write_reg;
    logic prev_was_read_reg;

    /* Ordered AXI response FIFO. */
    logic resp_write_mem[RESPONSE_FIFO_DEPTH];
    logic resp_error_mem[RESPONSE_FIFO_DEPTH];
    logic [DATA_W-1:0] resp_rdata_mem[RESPONSE_FIFO_DEPTH];
    logic [RESP_PTR_W-1:0] resp_write_ptr_reg;
    logic [RESP_PTR_W-1:0] resp_read_ptr_reg;
    logic [RESP_COUNT_W-1:0] resp_count_reg;

    wire logic cpuif_pending_complete = cpuif_pending_reg
        && ((cpuif_pending_write_reg && m_cpuif.wr_ack)
            || (!cpuif_pending_write_reg && m_cpuif.rd_ack));

    wire  logic resp_valid = resp_count_reg != 0;
    wire  logic resp_head_write = resp_write_mem[resp_read_ptr_reg];
    wire logic resp_pop = resp_valid && (resp_head_write ? s_axil_wr.bready : s_axil_rd.rready);

    /*
     * Count both queued responses and the slot reserved by an active CPUIF operation. A completing
     * operation changes form but not occupancy.
     */
    wire logic[RESP_COUNT_W-1:0] reserved_after_pop = resp_count_reg
        + RESP_COUNT_W'(cpuif_pending_reg) - RESP_COUNT_W'(resp_pop);
    wire logic response_slot_available = reserved_after_pop < RESP_COUNT_W'(RESPONSE_FIFO_DEPTH);
    wire logic dispatch_allowed = !rst && (!cpuif_pending_reg || cpuif_pending_complete)
        && response_slot_available;

    wire logic write_available = (aw_buf_valid_reg || s_axil_wr.awvalid)
        && (w_buf_valid_reg || s_axil_wr.wvalid);
    wire  logic read_available = ar_buf_valid_reg || s_axil_rd.arvalid;

    logic dispatch_write;
    logic dispatch_read;

    always_comb begin
        dispatch_write = 1'b0;
        dispatch_read = 1'b0;

        if (dispatch_allowed) begin
            if (read_available && write_available) begin
                if (prev_was_read_reg) begin
                    dispatch_write = 1'b1;
                end else begin
                    dispatch_read = 1'b1;
                end
            end else if (write_available) begin
                dispatch_write = 1'b1;
            end else if (read_available) begin
                dispatch_read = 1'b1;
            end
        end
    end

    wire  logic dispatch = dispatch_write || dispatch_read;
    wire logic cpuif_immediate_complete = !cpuif_pending_reg && dispatch
        && ((dispatch_write && m_cpuif.wr_ack) || (dispatch_read && m_cpuif.rd_ack));
    wire  logic cpuif_complete = cpuif_pending_complete || cpuif_immediate_complete;
    wire logic cpuif_complete_write = cpuif_pending_reg ? cpuif_pending_write_reg : dispatch_write;
    wire logic[ADDR_W-1:0] dispatch_write_addr = aw_buf_valid_reg ? aw_buf_addr_reg
        : s_axil_wr.awaddr;
    wire logic[DATA_W-1:0] dispatch_write_data = w_buf_valid_reg ? w_buf_data_reg : s_axil_wr.wdata;
    wire logic[STRB_W-1:0] dispatch_write_strb = w_buf_valid_reg ? w_buf_strb_reg : s_axil_wr.wstrb;
    wire logic[ADDR_W-1:0] dispatch_read_addr = ar_buf_valid_reg ? ar_buf_addr_reg
        : s_axil_rd.araddr;

    assign m_cpuif.req = dispatch;
    assign m_cpuif.req_is_wr = dispatch_write;
    assign m_cpuif.addr = dispatch_write ? dispatch_write_addr : dispatch_read_addr;
    assign m_cpuif.wr_data = dispatch_write ? dispatch_write_data : '0;
    assign m_cpuif.wr_biten = dispatch_write ? strb_to_biten(dispatch_write_strb) : '0;

    /* The consumed buffer can accept its replacement at the same edge. */
    assign s_axil_wr.awready = !rst && (!aw_buf_valid_reg || (dispatch_write && aw_buf_valid_reg));
    assign s_axil_wr.wready = !rst && (!w_buf_valid_reg || (dispatch_write && w_buf_valid_reg));
    assign s_axil_rd.arready = !rst && (!ar_buf_valid_reg || (dispatch_read && ar_buf_valid_reg));

    wire  logic aw_fire = s_axil_wr.awvalid && s_axil_wr.awready;
    wire  logic w_fire = s_axil_wr.wvalid && s_axil_wr.wready;
    wire  logic ar_fire = s_axil_rd.arvalid && s_axil_rd.arready;

    assign s_axil_wr.bvalid = resp_valid && resp_head_write;
    assign s_axil_wr.bresp = resp_error_mem[resp_read_ptr_reg] ? 2'b10 : 2'b00;
    assign s_axil_wr.buser = '0;

    assign s_axil_rd.rvalid = resp_valid && !resp_head_write;
    assign s_axil_rd.rdata = resp_rdata_mem[resp_read_ptr_reg];
    assign s_axil_rd.rresp = resp_error_mem[resp_read_ptr_reg] ? 2'b10 : 2'b00;
    assign s_axil_rd.ruser = '0;

    always_ff @(posedge clk) begin
        if (rst) begin
            aw_buf_valid_reg <= 1'b0;
            aw_buf_addr_reg <= '0;
            w_buf_valid_reg <= 1'b0;
            w_buf_data_reg <= '0;
            w_buf_strb_reg <= '0;
            ar_buf_valid_reg <= 1'b0;
            ar_buf_addr_reg <= '0;
        end else begin
            aw_buf_valid_reg <= (aw_buf_valid_reg && !dispatch_write)
                || (aw_fire && (aw_buf_valid_reg || !dispatch_write));
            if (aw_fire && (aw_buf_valid_reg || !dispatch_write)) begin
                aw_buf_addr_reg <= s_axil_wr.awaddr;
            end

            w_buf_valid_reg <= (w_buf_valid_reg && !dispatch_write)
                || (w_fire && (w_buf_valid_reg || !dispatch_write));
            if (w_fire && (w_buf_valid_reg || !dispatch_write)) begin
                w_buf_data_reg <= s_axil_wr.wdata;
                w_buf_strb_reg <= s_axil_wr.wstrb;
            end

            ar_buf_valid_reg <= (ar_buf_valid_reg && !dispatch_read)
                || (ar_fire && (ar_buf_valid_reg || !dispatch_read));
            if (ar_fire && (ar_buf_valid_reg || !dispatch_read)) begin
                ar_buf_addr_reg <= s_axil_rd.araddr;
            end
        end
    end

    always_ff @(posedge clk) begin
        if (rst) begin
            cpuif_pending_reg <= 1'b0;
            cpuif_pending_write_reg <= 1'b0;
            prev_was_read_reg <= 1'b0;
        end else begin
            if (dispatch) begin
                cpuif_pending_reg <= !cpuif_immediate_complete;
                cpuif_pending_write_reg <= dispatch_write;
                prev_was_read_reg <= dispatch_read;
            end else if (cpuif_pending_complete) begin
                cpuif_pending_reg <= 1'b0;
            end
        end
    end

    always_ff @(posedge clk) begin
        if (rst) begin
            for (int unsigned index = 0; index < RESPONSE_FIFO_DEPTH; index++) begin
                resp_write_mem[index] <= 1'b0;
                resp_error_mem[index] <= 1'b0;
                resp_rdata_mem[index] <= '0;
            end
            resp_write_ptr_reg <= '0;
            resp_read_ptr_reg <= '0;
            resp_count_reg <= '0;
        end else begin
            if (cpuif_complete) begin
                resp_write_mem[resp_write_ptr_reg] <= cpuif_complete_write;
                resp_error_mem[resp_write_ptr_reg] <= cpuif_complete_write ? m_cpuif.wr_err
                    : m_cpuif.rd_err;
                resp_rdata_mem[resp_write_ptr_reg] <= m_cpuif.rd_data;
                resp_write_ptr_reg <= next_resp_ptr(resp_write_ptr_reg);
            end

            if (resp_pop) begin
                resp_read_ptr_reg <= next_resp_ptr(resp_read_ptr_reg);
            end

            case ({
                cpuif_complete, resp_pop
            })
                2'b10: resp_count_reg <= resp_count_reg + 1'b1;
                2'b01: resp_count_reg <= resp_count_reg - 1'b1;
                default: resp_count_reg <= resp_count_reg;
            endcase
        end
    end

endmodule

`resetall
