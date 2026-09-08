// SPDX-FileCopyrightText: 2026 Kerim Bavcic
// SPDX-License-Identifier: AGPL-3.0-or-later

`resetall
`timescale 1ns / 1ps
`default_nettype none

/*
 * openENOC forwarding table arbiter multiplexer testbench
 */
module test_openenoc_forwarding_table_arb_mux #
(
    /* verilator lint_off WIDTHTRUNC */
    parameter int NUM_OF_INTERFACES = 4,
    localparam int INDEX_W          = $clog2(NUM_OF_INTERFACES)
    /* verilator lint_on WIDTHTRUNC */
)
();

    logic clk;
    logic rst;

    // Packed channel-major vectors: channel 0 lookup, channel 1 learning.
    logic [2*NUM_OF_INTERFACES-1:0]                     source_req;
    logic [2*NUM_OF_INTERFACES*48-1:0]                  source_mac;
    logic [NUM_OF_INTERFACES*NUM_OF_INTERFACES-1:0]     source_learning_bitmap;
    wire  [2*NUM_OF_INTERFACES-1:0]                     source_ack;
    wire  [NUM_OF_INTERFACES*NUM_OF_INTERFACES-1:0]     source_lookup_bitmap;

    wire  [1:0]                   slave_req;
    wire  [95:0]                  slave_mac;
    wire  [NUM_OF_INTERFACES-1:0] slave_learning_bitmap;
    logic [1:0]                   slave_ack;
    logic [NUM_OF_INTERFACES-1:0] slave_lookup_bitmap;

    // Passive observations for cycle-exact round-robin checks.
    wire [2*NUM_OF_INTERFACES-1:0] pending;
    wire [2*INDEX_W-1:0]           selected;
    wire [2*INDEX_W-1:0]           owner;
    wire [1:0]                     launch;
    wire [1:0]                     busy;

    openenoc_lookup_if #(
        .NUM_OF_INTERFACES(NUM_OF_INTERFACES)
    ) s_lookup_if[NUM_OF_INTERFACES]();

    openenoc_lookup_if #(
        .NUM_OF_INTERFACES(NUM_OF_INTERFACES)
    ) m_lookup_if();

    openenoc_learning_if #(
        .NUM_OF_INTERFACES(NUM_OF_INTERFACES)
    ) s_learning_if[NUM_OF_INTERFACES]();

    openenoc_learning_if #(
        .NUM_OF_INTERFACES(NUM_OF_INTERFACES)
    ) m_learning_if();

    for (genvar p = 0; p < NUM_OF_INTERFACES; p++) begin : g_bridge
        assign s_lookup_if[p].req          = source_req[p];
        assign s_lookup_if[p].mac_addr     = source_mac[p*48 +: 48];
        assign source_ack[p]               = s_lookup_if[p].ack;
        assign source_lookup_bitmap[p*NUM_OF_INTERFACES +: NUM_OF_INTERFACES] = s_lookup_if[p].port_bitmap;

        assign s_learning_if[p].req         = source_req[NUM_OF_INTERFACES + p];
        assign s_learning_if[p].mac_addr    = source_mac[(NUM_OF_INTERFACES + p)*48 +: 48];
        assign s_learning_if[p].port_bitmap = source_learning_bitmap[p*NUM_OF_INTERFACES +: NUM_OF_INTERFACES];
        assign source_ack[NUM_OF_INTERFACES + p] = s_learning_if[p].ack;
    end

    assign slave_req               = {m_learning_if.req, m_lookup_if.req};
    assign slave_mac               = {m_learning_if.mac_addr, m_lookup_if.mac_addr};
    assign slave_learning_bitmap   = m_learning_if.port_bitmap;
    assign m_lookup_if.ack         = slave_ack[0];
    assign m_learning_if.ack       = slave_ack[1];
    assign m_lookup_if.port_bitmap = slave_lookup_bitmap;

    openenoc_forwarding_table_arb_mux #(
        .NUM_OF_INTERFACES(NUM_OF_INTERFACES)
    )
    u_openenoc_forwarding_table_arb_mux (
        .clk(clk),
        .rst(rst),

        .s_lookup_if(s_lookup_if),
        .s_learning_if(s_learning_if),

        .m_lookup_if(m_lookup_if),
        .m_learning_if(m_learning_if)
    );

    for (genvar c = 0; c < 2; c++) begin : g_observe
        assign pending[c*NUM_OF_INTERFACES +: NUM_OF_INTERFACES] =
            u_openenoc_forwarding_table_arb_mux.g_channel[c].pending_reg;
        assign selected[c*INDEX_W +: INDEX_W] =
            u_openenoc_forwarding_table_arb_mux.selected[c];
        assign owner[c*INDEX_W +: INDEX_W] =
            u_openenoc_forwarding_table_arb_mux.g_channel[c].owner_reg;
        assign launch[c] = u_openenoc_forwarding_table_arb_mux.launch[c];
        assign busy[c]   = u_openenoc_forwarding_table_arb_mux.g_channel[c].busy_reg;
    end

endmodule

`resetall
