// SPDX-FileCopyrightText: 2021-2025 FPGA Ninja, LLC
// SPDX-FileCopyrightText: 2026 Enio Kaljic
// SPDX-License-Identifier: CERN-OHL-S-2.0

`resetall
`timescale 1ns / 1ps
`default_nettype none

/*
 * Bubble-free pipelined AXI4-Lite crossbar read path.
 */
module openenoc_axil_crossbar_rd #(
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
    taxi_axil_if.rd_slv  s_axil_rd[S_COUNT],
    taxi_axil_if.rd_mst  m_axil_rd[M_COUNT]
);

    localparam DATA_W = s_axil_rd[0].DATA_W;
    localparam ARUSER_W = s_axil_rd[0].ARUSER_W;
    localparam RUSER_W = s_axil_rd[0].RUSER_W;
    localparam logic ARUSER_EN = s_axil_rd[0].ARUSER_EN && m_axil_rd[0].ARUSER_EN;
    localparam logic RUSER_EN = s_axil_rd[0].RUSER_EN && m_axil_rd[0].RUSER_EN;

    localparam S_SELECT_W = S_COUNT > 1 ? $clog2(S_COUNT) : 1;
    localparam M_SELECT_W = M_COUNT > 1 ? $clog2(M_COUNT) : 1;
    localparam AR_PAYLOAD_W = ADDR_W + 3 + ARUSER_W;
    localparam R_PAYLOAD_W = DATA_W + 2 + RUSER_W;

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

    logic [ADDR_W-1:0] s_araddr[S_COUNT];
    logic [2:0] s_arprot[S_COUNT];
    logic [ARUSER_W-1:0] s_aruser[S_COUNT];
    logic s_arvalid[S_COUNT];
    logic s_arready[S_COUNT];

    logic [DATA_W-1:0] m_rdata[M_COUNT];
    logic [1:0] m_rresp[M_COUNT];
    logic [RUSER_W-1:0] m_ruser[M_COUNT];
    logic m_rvalid[M_COUNT];
    logic m_rready[M_COUNT];

    logic decode_match[S_COUNT];
    logic [M_SELECT_W-1:0] decode_select[S_COUNT];

    logic [M_SELECT_W-1:0] s_route_target_mem[S_COUNT][S_FIFO_DEPTH];
    logic s_route_decerr_mem[S_COUNT][S_FIFO_DEPTH];
    logic [S_PTR_W-1:0] s_route_wr_ptr_reg[S_COUNT];
    logic [S_PTR_W-1:0] s_route_rd_ptr_reg[S_COUNT];
    logic [S_COUNT_W-1:0] s_route_count_reg[S_COUNT];
    logic s_route_push[S_COUNT];
    logic s_route_pop[S_COUNT];
    logic s_route_available[S_COUNT];
    logic [M_SELECT_W-1:0] s_route_head_target[S_COUNT];
    logic s_route_head_decerr[S_COUNT];

    logic [S_SELECT_W-1:0] m_route_source_mem[M_COUNT][M_FIFO_DEPTH];
    logic [M_PTR_W-1:0] m_route_wr_ptr_reg[M_COUNT];
    logic [M_PTR_W-1:0] m_route_rd_ptr_reg[M_COUNT];
    logic [M_COUNT_W-1:0] m_route_count_reg[M_COUNT];
    logic m_route_push[M_COUNT];
    logic m_route_pop[M_COUNT];
    logic m_route_available[M_COUNT];
    logic [S_SELECT_W-1:0] m_route_head_source[M_COUNT];

    logic [S_COUNT-1:0] ar_request[M_COUNT];
    logic [S_COUNT-1:0] ar_grant[M_COUNT];
    logic ar_grant_valid[M_COUNT];
    logic [S_SELECT_W-1:0] ar_grant_index[M_COUNT];
    logic ar_arb_accept[M_COUNT];

    logic [AR_PAYLOAD_W-1:0] ar_input_data[M_COUNT];
    logic ar_input_valid[M_COUNT];
    logic ar_input_ready[M_COUNT];
    logic [AR_PAYLOAD_W-1:0] ar_output_data[M_COUNT];
    logic ar_output_valid[M_COUNT];

    logic [R_PAYLOAD_W-1:0] r_input_data[S_COUNT];
    logic r_input_valid[S_COUNT];
    logic r_input_ready[S_COUNT];
    logic [R_PAYLOAD_W-1:0] r_output_data[S_COUNT];
    logic r_output_valid[S_COUNT];

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
        assign s_araddr[s] = s_axil_rd[s].araddr;
        assign s_arprot[s] = s_axil_rd[s].arprot;
        assign s_aruser[s] = s_axil_rd[s].aruser;
        assign s_arvalid[s] = s_axil_rd[s].arvalid;
        assign s_axil_rd[s].arready = s_arready[s];

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
            .addr(s_araddr[s]),
            .prot(s_arprot[s]),
            .match(decode_match[s]),
            .select(decode_select[s])
        );

        openenoc_axil_crossbar_skid_buffer #(
            .DATA_W(R_PAYLOAD_W)
        ) r_buffer_inst (
            .clk(clk),
            .rst(rst),
            .s_data(r_input_data[s]),
            .s_valid(r_input_valid[s]),
            .s_ready(r_input_ready[s]),
            .m_data(r_output_data[s]),
            .m_valid(r_output_valid[s]),
            .m_ready(s_axil_rd[s].rready)
        );

        assign {
            s_axil_rd[s].rdata,
            s_axil_rd[s].rresp,
            s_axil_rd[s].ruser
        } = r_output_data[s];
        assign s_axil_rd[s].rvalid = r_output_valid[s];
    end

    for (genvar m = 0; m < M_COUNT; m = m + 1) begin : g_targets
        assign m_rdata[m] = m_axil_rd[m].rdata;
        assign m_rresp[m] = m_axil_rd[m].rresp;
        assign m_ruser[m] = m_axil_rd[m].ruser;
        assign m_rvalid[m] = m_axil_rd[m].rvalid;
        assign m_axil_rd[m].rready = m_rready[m];

        openenoc_axil_crossbar_arbiter #(
            .PORTS(S_COUNT),
            .INDEX_W(S_SELECT_W)
        ) ar_arbiter_inst (
            .clk(clk),
            .rst(rst),
            .request(ar_request[m]),
            .accept(ar_arb_accept[m]),
            .grant(ar_grant[m]),
            .grant_valid(ar_grant_valid[m]),
            .grant_index(ar_grant_index[m])
        );

        openenoc_axil_crossbar_skid_buffer #(
            .DATA_W(AR_PAYLOAD_W)
        ) ar_buffer_inst (
            .clk(clk),
            .rst(rst),
            .s_data(ar_input_data[m]),
            .s_valid(ar_input_valid[m]),
            .s_ready(ar_input_ready[m]),
            .m_data(ar_output_data[m]),
            .m_valid(ar_output_valid[m]),
            .m_ready(m_axil_rd[m].arready)
        );

        assign {
            m_axil_rd[m].araddr,
            m_axil_rd[m].arprot,
            m_axil_rd[m].aruser
        } = ar_output_data[m];
        assign m_axil_rd[m].arvalid = ar_output_valid[m];
    end

    always_comb begin
        for (integer s = 0; s < S_COUNT; s = s + 1) begin
            s_route_head_target[s] = '0;
            s_route_head_decerr[s] = 1'b0;
            if (s_route_count_reg[s] != 0) begin
                s_route_head_target[s] =
                    s_route_target_mem[s][s_route_rd_ptr_reg[s]];
                s_route_head_decerr[s] =
                    s_route_decerr_mem[s][s_route_rd_ptr_reg[s]];
            end
        end

        for (integer m = 0; m < M_COUNT; m = m + 1) begin
            m_route_head_source[m] = '0;
            if (m_route_count_reg[m] != 0) begin
                m_route_head_source[m] =
                    m_route_source_mem[m][m_route_rd_ptr_reg[m]];
            end
        end
    end

    always_comb begin
        for (integer s = 0; s < S_COUNT; s = s + 1) begin
            r_input_data[s] = '0;
            r_input_valid[s] = 1'b0;
            s_route_pop[s] = 1'b0;

            if (s_route_count_reg[s] != 0) begin
                if (s_route_head_decerr[s]) begin
                    r_input_data[s] = {
                        {DATA_W{1'b0}}, 2'b11, {RUSER_W{1'b0}}
                    };
                    r_input_valid[s] = 1'b1;
                end else if (m_route_count_reg[s_route_head_target[s]] != 0 &&
                        m_route_head_source[s_route_head_target[s]] ==
                            S_SELECT_W'(s)) begin
                    r_input_data[s] = {
                        m_rdata[s_route_head_target[s]],
                        m_rresp[s_route_head_target[s]],
                        RUSER_EN ? m_ruser[s_route_head_target[s]] : '0
                    };
                    r_input_valid[s] = m_rvalid[s_route_head_target[s]];
                end
            end

            s_route_pop[s] = r_input_valid[s] && r_input_ready[s];
            s_route_available[s] =
                s_route_count_reg[s] < S_COUNT_W'(S_ACCEPT_INT[s]) ||
                s_route_pop[s];
        end

        for (integer m = 0; m < M_COUNT; m = m + 1) begin
            m_rready[m] = 1'b0;
            m_route_pop[m] = 1'b0;

            if (m_route_count_reg[m] != 0 &&
                    s_route_count_reg[m_route_head_source[m]] != 0 &&
                    !s_route_head_decerr[m_route_head_source[m]] &&
                    s_route_head_target[m_route_head_source[m]] ==
                        M_SELECT_W'(m)) begin
                m_rready[m] = r_input_ready[m_route_head_source[m]];
            end

            m_route_pop[m] = m_rvalid[m] && m_rready[m];
            m_route_available[m] =
                m_route_count_reg[m] < M_COUNT_W'(M_ISSUE_INT[m]) ||
                m_route_pop[m];
        end
    end

    always_comb begin
        for (integer m = 0; m < M_COUNT; m = m + 1) begin
            ar_request[m] = '0;
            ar_input_data[m] = '0;
            ar_input_valid[m] = ar_grant_valid[m];

            for (integer s = 0; s < S_COUNT; s = s + 1) begin
                ar_request[m][s] = !rst && s_arvalid[s] &&
                    decode_match[s] && decode_select[s] == M_SELECT_W'(m) &&
                    s_route_available[s] && m_route_available[m];
            end

            if (ar_grant_valid[m]) begin
                ar_input_data[m] = {
                    s_araddr[ar_grant_index[m]],
                    s_arprot[ar_grant_index[m]],
                    ARUSER_EN ? s_aruser[ar_grant_index[m]] : '0
                };
            end

            ar_arb_accept[m] = ar_input_valid[m] && ar_input_ready[m];
            m_route_push[m] = ar_arb_accept[m];
        end
    end

    always_comb begin
        for (integer s = 0; s < S_COUNT; s = s + 1) begin
            s_arready[s] = 1'b0;
            if (!rst && s_route_available[s]) begin
                if (!decode_match[s]) begin
                    s_arready[s] = 1'b1;
                end else begin
                    s_arready[s] =
                        ar_grant[decode_select[s]][s] &&
                        ar_input_ready[decode_select[s]];
                end
            end
            s_route_push[s] = s_arvalid[s] && s_arready[s];
        end
    end

    always_ff @(posedge clk) begin
        for (integer s = 0; s < S_COUNT; s = s + 1) begin
            if (s_route_push[s]) begin
                s_route_target_mem[s][s_route_wr_ptr_reg[s]] <= decode_select[s];
                s_route_decerr_mem[s][s_route_wr_ptr_reg[s]] <= !decode_match[s];
                if (s_route_wr_ptr_reg[s] == S_PTR_W'(S_ACCEPT_INT[s]-1)) begin
                    s_route_wr_ptr_reg[s] <= '0;
                end else begin
                    s_route_wr_ptr_reg[s] <= s_route_wr_ptr_reg[s] + 1'b1;
                end
            end

            if (s_route_pop[s]) begin
                if (s_route_rd_ptr_reg[s] == S_PTR_W'(S_ACCEPT_INT[s]-1)) begin
                    s_route_rd_ptr_reg[s] <= '0;
                end else begin
                    s_route_rd_ptr_reg[s] <= s_route_rd_ptr_reg[s] + 1'b1;
                end
            end

            case ({s_route_push[s], s_route_pop[s]})
                2'b10: s_route_count_reg[s] <= s_route_count_reg[s] + 1'b1;
                2'b01: s_route_count_reg[s] <= s_route_count_reg[s] - 1'b1;
                default: s_route_count_reg[s] <= s_route_count_reg[s];
            endcase

            if (rst) begin
                s_route_wr_ptr_reg[s] <= '0;
                s_route_rd_ptr_reg[s] <= '0;
                s_route_count_reg[s] <= '0;
            end
        end

        for (integer m = 0; m < M_COUNT; m = m + 1) begin
            if (m_route_push[m]) begin
                m_route_source_mem[m][m_route_wr_ptr_reg[m]] <=
                    ar_grant_index[m];
                if (m_route_wr_ptr_reg[m] == M_PTR_W'(M_ISSUE_INT[m]-1)) begin
                    m_route_wr_ptr_reg[m] <= '0;
                end else begin
                    m_route_wr_ptr_reg[m] <= m_route_wr_ptr_reg[m] + 1'b1;
                end
            end

            if (m_route_pop[m]) begin
                if (m_route_rd_ptr_reg[m] == M_PTR_W'(M_ISSUE_INT[m]-1)) begin
                    m_route_rd_ptr_reg[m] <= '0;
                end else begin
                    m_route_rd_ptr_reg[m] <= m_route_rd_ptr_reg[m] + 1'b1;
                end
            end

            case ({m_route_push[m], m_route_pop[m]})
                2'b10: m_route_count_reg[m] <= m_route_count_reg[m] + 1'b1;
                2'b01: m_route_count_reg[m] <= m_route_count_reg[m] - 1'b1;
                default: m_route_count_reg[m] <= m_route_count_reg[m];
            endcase

            if (rst) begin
                m_route_wr_ptr_reg[m] <= '0;
                m_route_rd_ptr_reg[m] <= '0;
                m_route_count_reg[m] <= '0;
            end
        end
    end

endmodule

`resetall
