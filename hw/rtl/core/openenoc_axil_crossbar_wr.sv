// SPDX-FileCopyrightText: 2021-2025 FPGA Ninja, LLC
// SPDX-FileCopyrightText: 2026 Enio Kaljic
// SPDX-License-Identifier: CERN-OHL-S-2.0

`resetall
`timescale 1ns / 1ps
`default_nettype none

/*
 * Bubble-free pipelined AXI4-Lite crossbar write path.
 *
 * AW routing creates ordered per-source and per-target transaction queues.
 * The queues route independent W transfers to the matching target and retain
 * enough information to return B responses in source request order.
 */
module openenoc_axil_crossbar_wr #(
    parameter S_COUNT = 4,
    parameter M_COUNT = 4,
    parameter ADDR_W = 32,
    parameter S_ACCEPT = {S_COUNT{32'd16}},
    parameter M_REGIONS = 1,
    parameter M_BASE_ADDR = '0,
    parameter M_ADDR_W = {M_COUNT{{M_REGIONS{32'd24}}}},
    parameter M_CONNECT = {M_COUNT{{S_COUNT{1'b1}}}},
    parameter M_ISSUE = {M_COUNT{32'd16}},
    parameter M_SECURE = {M_COUNT{1'b0}}
) (
    input  wire logic    clk,
    input  wire logic    rst,
    taxi_axil_if.wr_slv  s_axil_wr[S_COUNT],
    taxi_axil_if.wr_mst  m_axil_wr[M_COUNT]
);

    localparam DATA_W = s_axil_wr[0].DATA_W;
    localparam STRB_W = s_axil_wr[0].STRB_W;
    localparam AWUSER_W = s_axil_wr[0].AWUSER_W;
    localparam WUSER_W = s_axil_wr[0].WUSER_W;
    localparam BUSER_W = s_axil_wr[0].BUSER_W;
    localparam logic AWUSER_EN = s_axil_wr[0].AWUSER_EN && m_axil_wr[0].AWUSER_EN;
    localparam logic WUSER_EN = s_axil_wr[0].WUSER_EN && m_axil_wr[0].WUSER_EN;
    localparam logic BUSER_EN = s_axil_wr[0].BUSER_EN && m_axil_wr[0].BUSER_EN;

    localparam S_SELECT_W = S_COUNT > 1 ? $clog2(S_COUNT) : 1;
    localparam M_SELECT_W = M_COUNT > 1 ? $clog2(M_COUNT) : 1;
    localparam AW_PAYLOAD_W = ADDR_W + 3 + AWUSER_W;
    localparam W_PAYLOAD_W = DATA_W + STRB_W + WUSER_W;
    localparam B_PAYLOAD_W = 2 + BUSER_W;

    localparam [S_COUNT-1:0][31:0] S_ACCEPT_INT = S_ACCEPT;
    localparam [M_COUNT-1:0][31:0] M_ISSUE_INT = M_ISSUE;

    function automatic integer max_s_accept(input logic unused);
        integer value;
        begin
            value = 1;
            for (integer i = 0; i < S_COUNT; i = i + 1) begin
                if (S_ACCEPT_INT[i] > value) begin
                    value = S_ACCEPT_INT[i];
                end
            end
            max_s_accept = value;
        end
    endfunction

    function automatic integer max_m_issue(input logic unused);
        integer value;
        begin
            value = 1;
            for (integer i = 0; i < M_COUNT; i = i + 1) begin
                if (M_ISSUE_INT[i] > value) begin
                    value = M_ISSUE_INT[i];
                end
            end
            max_m_issue = value;
        end
    endfunction

    localparam S_FIFO_DEPTH = max_s_accept(1'b0);
    localparam M_FIFO_DEPTH = max_m_issue(1'b0);
    localparam S_PTR_W = S_FIFO_DEPTH > 1 ? $clog2(S_FIFO_DEPTH) : 1;
    localparam M_PTR_W = M_FIFO_DEPTH > 1 ? $clog2(M_FIFO_DEPTH) : 1;
    localparam S_COUNT_W = $clog2(S_FIFO_DEPTH+1);
    localparam M_COUNT_W = $clog2(M_FIFO_DEPTH+1);

    logic [ADDR_W-1:0] s_awaddr[S_COUNT];
    logic [2:0] s_awprot[S_COUNT];
    logic [AWUSER_W-1:0] s_awuser[S_COUNT];
    logic s_awvalid[S_COUNT];
    logic s_awready[S_COUNT];
    logic [DATA_W-1:0] s_wdata[S_COUNT];
    logic [STRB_W-1:0] s_wstrb[S_COUNT];
    logic [WUSER_W-1:0] s_wuser[S_COUNT];
    logic s_wvalid[S_COUNT];
    logic s_wready[S_COUNT];

    logic [1:0] m_bresp[M_COUNT];
    logic [BUSER_W-1:0] m_buser[M_COUNT];
    logic m_bvalid[M_COUNT];
    logic m_bready[M_COUNT];

    logic decode_match[S_COUNT];
    logic [M_SELECT_W-1:0] decode_select[S_COUNT];

    logic [M_SELECT_W-1:0] s_route_target_mem[S_COUNT][S_FIFO_DEPTH];
    logic s_route_decerr_mem[S_COUNT][S_FIFO_DEPTH];
    logic s_route_error_ready_mem[S_COUNT][S_FIFO_DEPTH];
    logic [S_PTR_W-1:0] s_route_wr_ptr_reg[S_COUNT];
    logic [S_PTR_W-1:0] s_w_rd_ptr_reg[S_COUNT];
    logic [S_PTR_W-1:0] s_b_rd_ptr_reg[S_COUNT];
    logic [S_COUNT_W-1:0] s_w_count_reg[S_COUNT];
    logic [S_COUNT_W-1:0] s_b_count_reg[S_COUNT];
    logic s_route_push[S_COUNT];
    logic s_w_pop[S_COUNT];
    logic s_b_pop[S_COUNT];
    logic s_b_available[S_COUNT];
    logic [M_SELECT_W-1:0] s_w_head_target[S_COUNT];
    logic s_w_head_decerr[S_COUNT];
    logic [M_SELECT_W-1:0] s_b_head_target[S_COUNT];
    logic s_b_head_decerr[S_COUNT];
    logic s_b_head_error_ready[S_COUNT];

    logic [S_SELECT_W-1:0] m_route_source_mem[M_COUNT][M_FIFO_DEPTH];
    logic [M_PTR_W-1:0] m_route_wr_ptr_reg[M_COUNT];
    logic [M_PTR_W-1:0] m_w_rd_ptr_reg[M_COUNT];
    logic [M_PTR_W-1:0] m_b_rd_ptr_reg[M_COUNT];
    logic [M_COUNT_W-1:0] m_w_count_reg[M_COUNT];
    logic [M_COUNT_W-1:0] m_b_count_reg[M_COUNT];
    logic m_route_push[M_COUNT];
    logic m_w_pop[M_COUNT];
    logic m_b_pop[M_COUNT];
    logic m_b_available[M_COUNT];
    logic [S_SELECT_W-1:0] m_w_head_source[M_COUNT];
    logic [S_SELECT_W-1:0] m_b_head_source[M_COUNT];

    logic [S_COUNT-1:0] aw_request[M_COUNT];
    logic [S_COUNT-1:0] aw_grant[M_COUNT];
    logic aw_grant_valid[M_COUNT];
    logic [S_SELECT_W-1:0] aw_grant_index[M_COUNT];
    logic aw_arb_accept[M_COUNT];

    logic [AW_PAYLOAD_W-1:0] aw_input_data[M_COUNT];
    logic aw_input_valid[M_COUNT];
    logic aw_input_ready[M_COUNT];
    logic [AW_PAYLOAD_W-1:0] aw_output_data[M_COUNT];
    logic aw_output_valid[M_COUNT];

    logic [W_PAYLOAD_W-1:0] w_input_data[M_COUNT];
    logic w_input_valid[M_COUNT];
    logic w_input_ready[M_COUNT];
    logic [W_PAYLOAD_W-1:0] w_output_data[M_COUNT];
    logic w_output_valid[M_COUNT];

    logic [B_PAYLOAD_W-1:0] b_input_data[S_COUNT];
    logic b_input_valid[S_COUNT];
    logic b_input_ready[S_COUNT];
    logic [B_PAYLOAD_W-1:0] b_output_data[S_COUNT];
    logic b_output_valid[S_COUNT];

    initial begin
        for (integer s = 0; s < S_COUNT; s = s + 1) begin
            if (S_ACCEPT_INT[s] < 1) begin
                $fatal(0, "Error: S_ACCEPT must be at least one (instance %m)");
            end
        end
        for (integer m = 0; m < M_COUNT; m = m + 1) begin
            if (M_ISSUE_INT[m] < 1) begin
                $fatal(0, "Error: M_ISSUE must be at least one (instance %m)");
            end
        end
    end

    for (genvar s = 0; s < S_COUNT; s = s + 1) begin : g_sources
        assign s_awaddr[s] = s_axil_wr[s].awaddr;
        assign s_awprot[s] = s_axil_wr[s].awprot;
        assign s_awuser[s] = s_axil_wr[s].awuser;
        assign s_awvalid[s] = s_axil_wr[s].awvalid;
        assign s_axil_wr[s].awready = s_awready[s];
        assign s_wdata[s] = s_axil_wr[s].wdata;
        assign s_wstrb[s] = s_axil_wr[s].wstrb;
        assign s_wuser[s] = s_axil_wr[s].wuser;
        assign s_wvalid[s] = s_axil_wr[s].wvalid;
        assign s_axil_wr[s].wready = s_wready[s];

        openenoc_axil_crossbar_addr #(
            .S(s),
            .S_COUNT(S_COUNT),
            .M_COUNT(M_COUNT),
            .SELECT_W(M_SELECT_W),
            .ADDR_W(ADDR_W),
            .M_REGIONS(M_REGIONS),
            .M_BASE_ADDR(M_BASE_ADDR),
            .M_ADDR_W(M_ADDR_W),
            .M_CONNECT(M_CONNECT),
            .M_SECURE(M_SECURE)
        ) addr_inst (
            .addr(s_awaddr[s]),
            .prot(s_awprot[s]),
            .match(decode_match[s]),
            .select(decode_select[s])
        );

        openenoc_axil_crossbar_skid_buffer #(
            .DATA_W(B_PAYLOAD_W)
        ) b_buffer_inst (
            .clk(clk),
            .rst(rst),
            .s_data(b_input_data[s]),
            .s_valid(b_input_valid[s]),
            .s_ready(b_input_ready[s]),
            .m_data(b_output_data[s]),
            .m_valid(b_output_valid[s]),
            .m_ready(s_axil_wr[s].bready)
        );

        assign {s_axil_wr[s].bresp, s_axil_wr[s].buser} = b_output_data[s];
        assign s_axil_wr[s].bvalid = b_output_valid[s];
    end

    for (genvar m = 0; m < M_COUNT; m = m + 1) begin : g_targets
        assign m_bresp[m] = m_axil_wr[m].bresp;
        assign m_buser[m] = m_axil_wr[m].buser;
        assign m_bvalid[m] = m_axil_wr[m].bvalid;
        assign m_axil_wr[m].bready = m_bready[m];

        openenoc_axil_crossbar_arbiter #(
            .PORTS(S_COUNT),
            .INDEX_W(S_SELECT_W)
        ) aw_arbiter_inst (
            .clk(clk),
            .rst(rst),
            .request(aw_request[m]),
            .accept(aw_arb_accept[m]),
            .grant(aw_grant[m]),
            .grant_valid(aw_grant_valid[m]),
            .grant_index(aw_grant_index[m])
        );

        openenoc_axil_crossbar_skid_buffer #(
            .DATA_W(AW_PAYLOAD_W)
        ) aw_buffer_inst (
            .clk(clk),
            .rst(rst),
            .s_data(aw_input_data[m]),
            .s_valid(aw_input_valid[m]),
            .s_ready(aw_input_ready[m]),
            .m_data(aw_output_data[m]),
            .m_valid(aw_output_valid[m]),
            .m_ready(m_axil_wr[m].awready)
        );

        assign {
            m_axil_wr[m].awaddr,
            m_axil_wr[m].awprot,
            m_axil_wr[m].awuser
        } = aw_output_data[m];
        assign m_axil_wr[m].awvalid = aw_output_valid[m];

        openenoc_axil_crossbar_skid_buffer #(
            .DATA_W(W_PAYLOAD_W)
        ) w_buffer_inst (
            .clk(clk),
            .rst(rst),
            .s_data(w_input_data[m]),
            .s_valid(w_input_valid[m]),
            .s_ready(w_input_ready[m]),
            .m_data(w_output_data[m]),
            .m_valid(w_output_valid[m]),
            .m_ready(m_axil_wr[m].wready)
        );

        assign {
            m_axil_wr[m].wdata,
            m_axil_wr[m].wstrb,
            m_axil_wr[m].wuser
        } = w_output_data[m];
        assign m_axil_wr[m].wvalid = w_output_valid[m];
    end

    always_comb begin
        for (integer s = 0; s < S_COUNT; s = s + 1) begin
            s_w_head_target[s] = '0;
            s_w_head_decerr[s] = 1'b0;
            s_b_head_target[s] = '0;
            s_b_head_decerr[s] = 1'b0;
            s_b_head_error_ready[s] = 1'b0;

            if (s_w_count_reg[s] != 0) begin
                s_w_head_target[s] =
                    s_route_target_mem[s][s_w_rd_ptr_reg[s]];
                s_w_head_decerr[s] =
                    s_route_decerr_mem[s][s_w_rd_ptr_reg[s]];
            end
            if (s_b_count_reg[s] != 0) begin
                s_b_head_target[s] =
                    s_route_target_mem[s][s_b_rd_ptr_reg[s]];
                s_b_head_decerr[s] =
                    s_route_decerr_mem[s][s_b_rd_ptr_reg[s]];
                s_b_head_error_ready[s] =
                    s_route_error_ready_mem[s][s_b_rd_ptr_reg[s]];
            end
        end

        for (integer m = 0; m < M_COUNT; m = m + 1) begin
            m_w_head_source[m] = '0;
            m_b_head_source[m] = '0;
            if (m_w_count_reg[m] != 0) begin
                m_w_head_source[m] =
                    m_route_source_mem[m][m_w_rd_ptr_reg[m]];
            end
            if (m_b_count_reg[m] != 0) begin
                m_b_head_source[m] =
                    m_route_source_mem[m][m_b_rd_ptr_reg[m]];
            end
        end
    end

    always_comb begin
        for (integer s = 0; s < S_COUNT; s = s + 1) begin
            b_input_data[s] = '0;
            b_input_valid[s] = 1'b0;
            s_b_pop[s] = 1'b0;

            if (s_b_count_reg[s] != 0) begin
                if (s_b_head_decerr[s]) begin
                    b_input_data[s] = {2'b11, {BUSER_W{1'b0}}};
                    b_input_valid[s] = s_b_head_error_ready[s];
                end else if (m_b_count_reg[s_b_head_target[s]] != 0 &&
                        m_b_head_source[s_b_head_target[s]] ==
                            S_SELECT_W'(s)) begin
                    b_input_data[s] = {
                        m_bresp[s_b_head_target[s]],
                        BUSER_EN ? m_buser[s_b_head_target[s]] : '0
                    };
                    b_input_valid[s] = m_bvalid[s_b_head_target[s]];
                end
            end

            s_b_pop[s] = b_input_valid[s] && b_input_ready[s];
            s_b_available[s] =
                s_b_count_reg[s] < S_COUNT_W'(S_ACCEPT_INT[s]) ||
                s_b_pop[s];
        end

        for (integer m = 0; m < M_COUNT; m = m + 1) begin
            m_bready[m] = 1'b0;
            if (m_b_count_reg[m] != 0 &&
                    s_b_count_reg[m_b_head_source[m]] != 0 &&
                    !s_b_head_decerr[m_b_head_source[m]] &&
                    s_b_head_target[m_b_head_source[m]] == M_SELECT_W'(m)) begin
                m_bready[m] = b_input_ready[m_b_head_source[m]];
            end

            m_b_pop[m] = m_bvalid[m] && m_bready[m];
            m_b_available[m] =
                m_b_count_reg[m] < M_COUNT_W'(M_ISSUE_INT[m]) ||
                m_b_pop[m];
        end
    end

    always_comb begin
        for (integer m = 0; m < M_COUNT; m = m + 1) begin
            w_input_data[m] = '0;
            w_input_valid[m] = 1'b0;

            if (m_w_count_reg[m] != 0 &&
                    s_w_count_reg[m_w_head_source[m]] != 0 &&
                    !s_w_head_decerr[m_w_head_source[m]] &&
                    s_w_head_target[m_w_head_source[m]] == M_SELECT_W'(m)) begin
                w_input_data[m] = {
                    s_wdata[m_w_head_source[m]],
                    s_wstrb[m_w_head_source[m]],
                    WUSER_EN ? s_wuser[m_w_head_source[m]] : '0
                };
                w_input_valid[m] = s_wvalid[m_w_head_source[m]];
            end

            m_w_pop[m] = w_input_valid[m] && w_input_ready[m];
        end

        for (integer s = 0; s < S_COUNT; s = s + 1) begin
            s_wready[s] = 1'b0;
            if (!rst && s_w_count_reg[s] != 0) begin
                if (s_w_head_decerr[s]) begin
                    s_wready[s] = 1'b1;
                end else if (m_w_count_reg[s_w_head_target[s]] != 0 &&
                        m_w_head_source[s_w_head_target[s]] ==
                            S_SELECT_W'(s)) begin
                    s_wready[s] = w_input_ready[s_w_head_target[s]];
                end
            end
            s_w_pop[s] = s_wvalid[s] && s_wready[s];
        end
    end

    always_comb begin
        for (integer m = 0; m < M_COUNT; m = m + 1) begin
            aw_request[m] = '0;
            aw_input_data[m] = '0;
            aw_input_valid[m] = aw_grant_valid[m];

            for (integer s = 0; s < S_COUNT; s = s + 1) begin
                aw_request[m][s] = !rst && s_awvalid[s] &&
                    decode_match[s] && decode_select[s] == M_SELECT_W'(m) &&
                    s_b_available[s] && m_b_available[m];
            end

            if (aw_grant_valid[m]) begin
                aw_input_data[m] = {
                    s_awaddr[aw_grant_index[m]],
                    s_awprot[aw_grant_index[m]],
                    AWUSER_EN ? s_awuser[aw_grant_index[m]] : '0
                };
            end

            aw_arb_accept[m] = aw_input_valid[m] && aw_input_ready[m];
            m_route_push[m] = aw_arb_accept[m];
        end
    end

    always_comb begin
        for (integer s = 0; s < S_COUNT; s = s + 1) begin
            s_awready[s] = 1'b0;
            if (!rst && s_b_available[s]) begin
                if (!decode_match[s]) begin
                    s_awready[s] = 1'b1;
                end else begin
                    s_awready[s] =
                        aw_grant[decode_select[s]][s] &&
                        aw_input_ready[decode_select[s]];
                end
            end
            s_route_push[s] = s_awvalid[s] && s_awready[s];
        end
    end

    always_ff @(posedge clk) begin
        for (integer s = 0; s < S_COUNT; s = s + 1) begin
            if (s_route_push[s]) begin
                s_route_target_mem[s][s_route_wr_ptr_reg[s]] <= decode_select[s];
                s_route_decerr_mem[s][s_route_wr_ptr_reg[s]] <= !decode_match[s];
                s_route_error_ready_mem[s][s_route_wr_ptr_reg[s]] <= 1'b0;
                if (s_route_wr_ptr_reg[s] == S_PTR_W'(S_ACCEPT_INT[s]-1)) begin
                    s_route_wr_ptr_reg[s] <= '0;
                end else begin
                    s_route_wr_ptr_reg[s] <= s_route_wr_ptr_reg[s] + 1'b1;
                end
            end

            if (s_w_pop[s]) begin
                if (s_w_head_decerr[s]) begin
                    s_route_error_ready_mem[s][s_w_rd_ptr_reg[s]] <= 1'b1;
                end
                if (s_w_rd_ptr_reg[s] == S_PTR_W'(S_ACCEPT_INT[s]-1)) begin
                    s_w_rd_ptr_reg[s] <= '0;
                end else begin
                    s_w_rd_ptr_reg[s] <= s_w_rd_ptr_reg[s] + 1'b1;
                end
            end

            if (s_b_pop[s]) begin
                if (s_b_rd_ptr_reg[s] == S_PTR_W'(S_ACCEPT_INT[s]-1)) begin
                    s_b_rd_ptr_reg[s] <= '0;
                end else begin
                    s_b_rd_ptr_reg[s] <= s_b_rd_ptr_reg[s] + 1'b1;
                end
            end

            case ({s_route_push[s], s_w_pop[s]})
                2'b10: s_w_count_reg[s] <= s_w_count_reg[s] + 1'b1;
                2'b01: s_w_count_reg[s] <= s_w_count_reg[s] - 1'b1;
                default: s_w_count_reg[s] <= s_w_count_reg[s];
            endcase

            case ({s_route_push[s], s_b_pop[s]})
                2'b10: s_b_count_reg[s] <= s_b_count_reg[s] + 1'b1;
                2'b01: s_b_count_reg[s] <= s_b_count_reg[s] - 1'b1;
                default: s_b_count_reg[s] <= s_b_count_reg[s];
            endcase

            if (rst) begin
                s_route_wr_ptr_reg[s] <= '0;
                s_w_rd_ptr_reg[s] <= '0;
                s_b_rd_ptr_reg[s] <= '0;
                s_w_count_reg[s] <= '0;
                s_b_count_reg[s] <= '0;
            end
        end

        for (integer m = 0; m < M_COUNT; m = m + 1) begin
            if (m_route_push[m]) begin
                m_route_source_mem[m][m_route_wr_ptr_reg[m]] <=
                    aw_grant_index[m];
                if (m_route_wr_ptr_reg[m] == M_PTR_W'(M_ISSUE_INT[m]-1)) begin
                    m_route_wr_ptr_reg[m] <= '0;
                end else begin
                    m_route_wr_ptr_reg[m] <= m_route_wr_ptr_reg[m] + 1'b1;
                end
            end

            if (m_w_pop[m]) begin
                if (m_w_rd_ptr_reg[m] == M_PTR_W'(M_ISSUE_INT[m]-1)) begin
                    m_w_rd_ptr_reg[m] <= '0;
                end else begin
                    m_w_rd_ptr_reg[m] <= m_w_rd_ptr_reg[m] + 1'b1;
                end
            end

            if (m_b_pop[m]) begin
                if (m_b_rd_ptr_reg[m] == M_PTR_W'(M_ISSUE_INT[m]-1)) begin
                    m_b_rd_ptr_reg[m] <= '0;
                end else begin
                    m_b_rd_ptr_reg[m] <= m_b_rd_ptr_reg[m] + 1'b1;
                end
            end

            case ({m_route_push[m], m_w_pop[m]})
                2'b10: m_w_count_reg[m] <= m_w_count_reg[m] + 1'b1;
                2'b01: m_w_count_reg[m] <= m_w_count_reg[m] - 1'b1;
                default: m_w_count_reg[m] <= m_w_count_reg[m];
            endcase

            case ({m_route_push[m], m_b_pop[m]})
                2'b10: m_b_count_reg[m] <= m_b_count_reg[m] + 1'b1;
                2'b01: m_b_count_reg[m] <= m_b_count_reg[m] - 1'b1;
                default: m_b_count_reg[m] <= m_b_count_reg[m];
            endcase

            if (rst) begin
                m_route_wr_ptr_reg[m] <= '0;
                m_w_rd_ptr_reg[m] <= '0;
                m_b_rd_ptr_reg[m] <= '0;
                m_w_count_reg[m] <= '0;
                m_b_count_reg[m] <= '0;
            end
        end
    end

endmodule

`resetall
