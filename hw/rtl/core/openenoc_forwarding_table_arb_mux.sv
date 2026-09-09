// SPDX-FileCopyrightText: 2026 Kerim Bavcic
// SPDX-License-Identifier: CERN-OHL-S-2.0

`resetall
`timescale 1ns / 1ps
`default_nettype none

/*
 * Independent round-robin lookup and learning request multiplexers.
 *
 * Each source may have one outstanding request per channel. A request is a
 * one-cycle strobe; its payload is captured even when another source owns the
 * downstream channel. Holding req until ack is also accepted (edge detection).
 * Each downstream channel has one outstanding transaction, with a registered
 * owner until ack. The forwarding table retains its CPU/lookup/learning policy.
 */
module openenoc_forwarding_table_arb_mux #
(
    parameter int NUM_OF_INTERFACES = 4
)
(
    input  wire logic                         clk,
    input  wire logic                         rst,

    /*
     * Per-port lookup interfaces
     */
    openenoc_lookup_if.slv                    s_lookup_if[NUM_OF_INTERFACES],

    /*
     * Per-port learning interfaces
     */
    openenoc_learning_if.slv                  s_learning_if[NUM_OF_INTERFACES],

    /*
     * Forwarding table lookup interface
     */
    openenoc_lookup_if.mst                    m_lookup_if,

    /*
     * Forwarding table learning interface
     */
    openenoc_learning_if.mst                  m_learning_if
);

    // ---------------------------------------------------------------------------
    // parameters
    // ---------------------------------------------------------------------------
    localparam int INDEX_W = NUM_OF_INTERFACES > 1 ? $clog2(NUM_OF_INTERFACES) : 1;

    // check configuration
    /* verilator lint_off GENUNNAMED */
    if (NUM_OF_INTERFACES < 2 || NUM_OF_INTERFACES > 32)
        $fatal(0, "Error: NUM_OF_INTERFACES must be in range 2 to 32 (instance %m)");
    if (m_lookup_if.NUM_OF_INTERFACES != NUM_OF_INTERFACES ||
            m_learning_if.NUM_OF_INTERFACES != NUM_OF_INTERFACES)
        $fatal(0, "Error: downstream interface parameter mismatch (instance %m)");
    /* verilator lint_on GENUNNAMED */

    // ---------------------------------------------------------------------------
    // internal signals
    // ---------------------------------------------------------------------------

    // Channel 0 is lookup; channel 1 is learning. Interface arrays are accessed
    // through constant genvars, while only plain arrays are dynamically indexed.
    wire  [NUM_OF_INTERFACES-1:0] request[2];
    wire  [47:0]                  mac_addr[2][NUM_OF_INTERFACES];
    wire  [NUM_OF_INTERFACES-1:0] learning_bitmap[NUM_OF_INTERFACES];
    wire  [1:0]                   table_ack;
    wire  [1:0]                   table_req;
    wire  [47:0]                  table_mac[2];
    wire  [NUM_OF_INTERFACES-1:0] source_ack[2];
    logic [NUM_OF_INTERFACES-1:0] bitmap_reg[NUM_OF_INTERFACES];
    wire  [INDEX_W-1:0]           selected[2];
    wire  [1:0]                   launch;

    assign m_lookup_if.req          = table_req[0];
    assign m_lookup_if.mac_addr     = table_mac[0];
    assign m_learning_if.req        = table_req[1];
    assign m_learning_if.mac_addr = table_mac[1];
    assign table_ack                = {m_learning_if.ack, m_lookup_if.ack};

    // ---------------------------------------------------------------------------
    // source interface mapping
    // ---------------------------------------------------------------------------
    for (genvar n = 0; n < NUM_OF_INTERFACES; n++) begin : g_source
        /* verilator lint_off GENUNNAMED */
        if (s_lookup_if[n].NUM_OF_INTERFACES != NUM_OF_INTERFACES ||
                s_learning_if[n].NUM_OF_INTERFACES != NUM_OF_INTERFACES)
            $fatal(0, "Error: source interface parameter mismatch (instance %m)");
        /* verilator lint_on GENUNNAMED */

        assign request[0][n]              = s_lookup_if[n].req;
        assign request[1][n]              = s_learning_if[n].req;
        assign mac_addr[0][n]             = s_lookup_if[n].mac_addr;
        assign mac_addr[1][n]             = s_learning_if[n].mac_addr;
        assign learning_bitmap[n]         = s_learning_if[n].port_bitmap;
        assign s_lookup_if[n].ack          = source_ack[0][n];
        assign s_learning_if[n].ack        = source_ack[1][n];
        assign s_lookup_if[n].port_bitmap = source_ack[0][n] ? m_lookup_if.port_bitmap : '0;
    end

    // ---------------------------------------------------------------------------
    // independent lookup and learning arbitration
    // ---------------------------------------------------------------------------
    for (genvar channel = 0; channel < 2; channel++) begin : g_channel
        logic [NUM_OF_INTERFACES-1:0] pending_reg;
        logic [NUM_OF_INTERFACES-1:0] request_d;
        logic [47:0]                  mac_reg[NUM_OF_INTERFACES];
        logic                         busy_reg;
        logic [INDEX_W-1:0]           owner_reg;
        logic                         req_reg;
        logic [47:0]                  active_mac_reg;
        wire                          grant_valid;
        wire [NUM_OF_INTERFACES-1:0] capture = request[channel] & ~request_d;

        openenoc_rr_arbiter #(
            .PORTS(NUM_OF_INTERFACES),
            .INDEX_W(INDEX_W)
        ) u_arbiter (
            .clk(clk),
            .rst(rst),
            .request(pending_reg),
            .accept(launch[channel]),
            .grant(),
            .grant_valid(grant_valid),
            .grant_index(selected[channel])
        );

        assign launch[channel]    = !rst && !busy_reg && grant_valid;
        assign table_req[channel] = req_reg && !rst;
        assign table_mac[channel] = active_mac_reg;

        for (genvar n = 0; n < NUM_OF_INTERFACES; n++) begin : g_ack
            assign source_ack[channel][n] = !rst && busy_reg &&
                owner_reg == INDEX_W'(n) && table_ack[channel];
        end

        always_ff @(posedge clk) begin
            req_reg <= 1'b0;
            request_d <= request[channel];

            if (busy_reg && table_ack[channel]) begin
                busy_reg <= 1'b0;
            end

            if (launch[channel]) begin
                pending_reg[selected[channel]] <= 1'b0;
                owner_reg <= selected[channel];
                active_mac_reg <= mac_reg[selected[channel]];
                req_reg <= 1'b1;
                busy_reg <= 1'b1;
            end

            for (int n = 0; n < NUM_OF_INTERFACES; n++) begin
                if (capture[n]) begin
                    pending_reg[n] <= 1'b1;
                    mac_reg[n] <= mac_addr[channel][n];
                end
            end

            if (rst) begin
                pending_reg <= '0;
                request_d <= '0;
                busy_reg <= 1'b0;
                owner_reg <= '0;
                req_reg <= 1'b0;
                active_mac_reg <= '0;
                for (int n = 0; n < NUM_OF_INTERFACES; n++)
                    mac_reg[n] <= '0;
            end
        end

        // synthesis translate_off
        always @(posedge clk) begin
            if (!rst) begin
                for (int n = 0; n < NUM_OF_INTERFACES; n++) begin
                        if (capture[n] && (pending_reg[n] ||
                            (busy_reg && owner_reg == INDEX_W'(n) && !table_ack[channel]))) begin
                        $fatal(1, "Error: request reissued before ack, channel %0d port %0d (%m)", channel, n);
                        end
                end
            end
        end
        // synthesis translate_on

        if (channel == 1) begin : g_learning_payload
            always_ff @(posedge clk) begin
                for (int n = 0; n < NUM_OF_INTERFACES; n++) begin
                    if (capture[n]) begin
                        bitmap_reg[n] <= learning_bitmap[n];
                    end
                end
                if (launch[channel]) begin
                    m_learning_if.port_bitmap <= bitmap_reg[selected[channel]];
                end
                if (rst) begin
                    m_learning_if.port_bitmap <= '0;
                    for (int n = 0; n < NUM_OF_INTERFACES; n++) begin
                        bitmap_reg[n] <= '0;
                    end
                end
            end
        end
    end
endmodule

`resetall
