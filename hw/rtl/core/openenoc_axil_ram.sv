// SPDX-FileCopyrightText: 2018-2025 FPGA Ninja, LLC
// SPDX-FileCopyrightText: 2026 Enio Kaljic
// SPDX-License-Identifier: CERN-OHL-S-2.0

`resetall
`timescale 1ns / 1ps
`default_nettype none

/*
 * Generic AXI4-Lite RAM with optional file initialization
 */
module openenoc_axil_ram #
(
    // Width of the byte-addressed memory aperture
    parameter ADDR_W = 16,
    // Extra pipeline register on the read response
    parameter logic PIPELINE_OUTPUT = 1'b0,
    // Optional $readmemh-compatible initialization file
    parameter INIT_FILE = ""
)
(
    input  wire logic    clk,
    input  wire logic    rst,

    /*
     * AXI4-Lite slave interface
     */
    taxi_axil_if.wr_slv  s_axil_wr,
    taxi_axil_if.rd_slv  s_axil_rd
);

    // Extract interface parameters
    localparam DATA_W = s_axil_wr.DATA_W;
    localparam STRB_W = s_axil_wr.STRB_W;

    localparam ADDR_LSB = $clog2(STRB_W);
    localparam VALID_ADDR_W = ADDR_W - ADDR_LSB;
    localparam BYTE_LANES = STRB_W;
    localparam BYTE_W = DATA_W/BYTE_LANES;
    localparam DEPTH = 2**VALID_ADDR_W;

    // Check configuration
    if (BYTE_W * STRB_W != DATA_W) begin : g_data_width_error
        $fatal(0, "Error: AXI data width is not evenly divisible (instance %m)");
    end

    if (2**$clog2(BYTE_LANES) != BYTE_LANES) begin : g_byte_lane_count_error
        $fatal(0, "Error: AXI byte lane count must be a power of two (instance %m)");
    end

    if (ADDR_W <= ADDR_LSB) begin : g_aperture_width_error
        $fatal(0, "Error: RAM aperture must contain at least two words (instance %m)");
    end

    if (s_axil_wr.DATA_W != s_axil_rd.DATA_W ||
            s_axil_wr.STRB_W != s_axil_rd.STRB_W) begin : g_interface_config_error
        $fatal(0, "Error: AXI read and write interface configurations do not match (instance %m)");
    end

    if (s_axil_wr.ADDR_W < ADDR_W ||
            s_axil_rd.ADDR_W < ADDR_W) begin : g_interface_addr_width_error
        $fatal(0, "Error: AXI address width is insufficient (instance %m)");
    end

    /*
     * AXI4-Lite write frontend. AW and W are buffered independently and the
     * buffers are fall-through when empty.
     */
    logic aw_buf_valid_reg;
    logic [VALID_ADDR_W-1:0] aw_buf_addr_reg;
    logic w_buf_valid_reg;
    logic [DATA_W-1:0] w_buf_data_reg;
    logic [STRB_W-1:0] w_buf_strb_reg;
    logic bvalid_reg;

    wire logic write_response_ready = !bvalid_reg || s_axil_wr.bready;
    wire logic write_commit = !rst && write_response_ready &&
        (aw_buf_valid_reg || s_axil_wr.awvalid) &&
        (w_buf_valid_reg || s_axil_wr.wvalid);

    wire logic aw_fire = s_axil_wr.awvalid && s_axil_wr.awready;
    wire logic w_fire = s_axil_wr.wvalid && s_axil_wr.wready;

    wire logic [VALID_ADDR_W-1:0] s_axil_awaddr_valid =
        VALID_ADDR_W'(s_axil_wr.awaddr >> ADDR_LSB);
    wire logic [VALID_ADDR_W-1:0] mem_wr_addr =
        aw_buf_valid_reg ? aw_buf_addr_reg : s_axil_awaddr_valid;
    wire logic [DATA_W-1:0] mem_wr_data =
        w_buf_valid_reg ? w_buf_data_reg : s_axil_wr.wdata;
    wire logic [STRB_W-1:0] mem_wr_strb =
        w_buf_valid_reg ? w_buf_strb_reg : s_axil_wr.wstrb;

    /*
     * AXI4-Lite read frontend. The RAM output is an elastic response stage;
     * PIPELINE_OUTPUT adds a second elastic output register.
     */
    logic read_valid_reg;
    logic [DATA_W-1:0] mem_rd_data_reg;
    logic read_pipe_valid_reg;
    logic [DATA_W-1:0] read_pipe_data_reg;

    wire logic read_output_ready = PIPELINE_OUTPUT ?
        (!read_pipe_valid_reg || s_axil_rd.rready) : s_axil_rd.rready;
    wire logic read_stage_ready = !read_valid_reg || read_output_ready;
    wire logic mem_rd_en = s_axil_rd.arvalid && s_axil_rd.arready;
    wire logic [VALID_ADDR_W-1:0] mem_rd_addr =
        VALID_ADDR_W'(s_axil_rd.araddr >> ADDR_LSB);

    logic [DATA_W-1:0] mem[0:DEPTH-1];

    initial begin
        for (integer i = 0; i < DEPTH; i = i + 1) begin
            mem[i] = '0;
        end

        if (INIT_FILE != "") begin
            $readmemh(INIT_FILE, mem);
        end
    end

    assign s_axil_wr.awready = !rst &&
        (!aw_buf_valid_reg || (write_commit && aw_buf_valid_reg));
    assign s_axil_wr.wready = !rst &&
        (!w_buf_valid_reg || (write_commit && w_buf_valid_reg));
    assign s_axil_wr.bresp = 2'b00;
    assign s_axil_wr.buser = '0;
    assign s_axil_wr.bvalid = bvalid_reg;

    assign s_axil_rd.arready = !rst && read_stage_ready;
    assign s_axil_rd.rdata = PIPELINE_OUTPUT ? read_pipe_data_reg : mem_rd_data_reg;
    assign s_axil_rd.rresp = 2'b00;
    assign s_axil_rd.ruser = '0;
    assign s_axil_rd.rvalid = PIPELINE_OUTPUT ? read_pipe_valid_reg : read_valid_reg;

    /* AXI4-Lite write channel and response buffering. */
    always_ff @(posedge clk) begin
        if (rst) begin
            aw_buf_valid_reg <= 1'b0;
            w_buf_valid_reg <= 1'b0;
            bvalid_reg <= 1'b0;
        end else begin
            bvalid_reg <= write_commit || (bvalid_reg && !s_axil_wr.bready);

            aw_buf_valid_reg <=
                (aw_buf_valid_reg && !write_commit) ||
                (aw_fire && (aw_buf_valid_reg || !write_commit));
            if (aw_fire && (aw_buf_valid_reg || !write_commit)) begin
                aw_buf_addr_reg <= s_axil_awaddr_valid;
            end

            w_buf_valid_reg <=
                (w_buf_valid_reg && !write_commit) ||
                (w_fire && (w_buf_valid_reg || !write_commit));
            if (w_fire && (w_buf_valid_reg || !write_commit)) begin
                w_buf_data_reg <= s_axil_wr.wdata;
                w_buf_strb_reg <= s_axil_wr.wstrb;
            end
        end
    end

    /* AXI4-Lite read channel and response buffering. */
    always_ff @(posedge clk) begin
        if (rst) begin
            read_valid_reg <= 1'b0;
            read_pipe_valid_reg <= 1'b0;
        end else begin
            if (read_stage_ready) begin
                read_valid_reg <= mem_rd_en;
            end

            if (PIPELINE_OUTPUT && read_output_ready) begin
                read_pipe_valid_reg <= read_valid_reg;
                if (read_valid_reg) begin
                    read_pipe_data_reg <= mem_rd_data_reg;
                end
            end
        end
    end

    /*
     * Canonical byte-enabled synchronous RAM write port.
     */
    always_ff @(posedge clk) begin
        for (integer i = 0; i < BYTE_LANES; i = i + 1) begin
            if (write_commit && mem_wr_strb[i]) begin
                mem[mem_wr_addr][BYTE_W*i +: BYTE_W] <=
                    mem_wr_data[BYTE_W*i +: BYTE_W];
            end
        end
    end

    /*
     * Canonical synchronous RAM read port.
     */
    always_ff @(posedge clk) begin
        if (mem_rd_en) begin
            mem_rd_data_reg <= mem[mem_rd_addr];
        end
    end

endmodule

`resetall
