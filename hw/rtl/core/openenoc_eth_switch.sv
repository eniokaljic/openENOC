// SPDX-FileCopyrightText: 2026 Kerim Bavcic
// SPDX-License-Identifier: CERN-OHL-S-2.0

`resetall
`timescale 1ns / 1ps
`default_nettype none

/*
 * Compile-time Ethernet switch architecture selector.
 *
 * Both implementations expose the same Ethernet and CSR interfaces.
 */
module openenoc_eth_switch #
(
    // Switch architecture:
    //   0 = shared bus
    //   1 = crossbar
    parameter int SWITCH_TYPE = 0,

    // Number of Ethernet interfaces
    parameter int unsigned NUM_OF_INTERFACES = 4,

    // Forwarding table depth in entries
    parameter int unsigned TABLE_DEPTH = 32,

    // Internal switch fabric data width
    parameter int unsigned FABRIC_DATA_W = 32,

    // Interface orientation:
    //   0 = switch is side A
    //   1 = switch is side B
    //
    // By default all switch ports operate as side B.
    parameter logic [NUM_OF_INTERFACES-1:0] PORT_SIDE = '1,

    // Per-port asynchronous FIFO capacity in bytes
    parameter int unsigned PORT_FIFO_DEPTH = 64
)
(
    /*
     * Switch fabric clock domain
     */
    input wire logic clk,
    input wire logic rst,

    /*
     * Control and status interface
     */
    openenoc_switch_if.core switch_if,

    /*
     * Ethernet-like openENOC interfaces
     */
    openenoc_eth_if eth_if [NUM_OF_INTERFACES-1:0]
);

    localparam int SWITCH_TYPE_SHARED_BUS = 0;
    localparam int SWITCH_TYPE_CROSSBAR   = 1;

    /* verilator lint_off GENUNNAMED */
    if (SWITCH_TYPE != SWITCH_TYPE_SHARED_BUS && SWITCH_TYPE != SWITCH_TYPE_CROSSBAR)
        $fatal(0, "Error: SWITCH_TYPE must be 0 (shared bus) or 1 (crossbar) (instance %m)");

    if (NUM_OF_INTERFACES < 2 || NUM_OF_INTERFACES > 32)
        $fatal(0, "Error: NUM_OF_INTERFACES must be in range 2 to 32 (instance %m)");

    if (TABLE_DEPTH < 1)
        $fatal(0, "Error: TABLE_DEPTH must be at least 1 (instance %m)");

    if (FABRIC_DATA_W < 8 || FABRIC_DATA_W > 512 || FABRIC_DATA_W % 8 != 0)
        $fatal(0, "Error: FABRIC_DATA_W must be a multiple of 8 in range 8 to 512 (instance %m)");

    if (switch_if.NUM_OF_INTERFACES != NUM_OF_INTERFACES || switch_if.TABLE_DEPTH != TABLE_DEPTH)
        $fatal(0, "Error: switch_if parameter mismatch (instance %m)");
    /* verilator lint_on GENUNNAMED */

    /*
     * Per-port width, clock, and FIFO checks remain in each implementation so
     * they also apply when the concrete switch is instantiated directly.
     */
    if (SWITCH_TYPE == SWITCH_TYPE_SHARED_BUS) begin : g_shared_bus

        openenoc_eth_switch_shared_bus #(
            .NUM_OF_INTERFACES (NUM_OF_INTERFACES),
            .TABLE_DEPTH       (TABLE_DEPTH),
            .FABRIC_DATA_W     (FABRIC_DATA_W),
            .PORT_SIDE         (PORT_SIDE),
            .PORT_FIFO_DEPTH   (PORT_FIFO_DEPTH)
        )
        u_switch (
            .clk       (clk),
            .rst       (rst),
            .switch_if (switch_if),
            .eth_if    (eth_if)
        );

    end else if (SWITCH_TYPE == SWITCH_TYPE_CROSSBAR) begin : g_crossbar

        openenoc_eth_switch_crossbar #(
            .NUM_OF_INTERFACES (NUM_OF_INTERFACES),
            .TABLE_DEPTH       (TABLE_DEPTH),
            .FABRIC_DATA_W     (FABRIC_DATA_W),
            .PORT_SIDE         (PORT_SIDE),
            .PORT_FIFO_DEPTH   (PORT_FIFO_DEPTH)
        )
        u_switch (
            .clk       (clk),
            .rst       (rst),
            .switch_if (switch_if),
            .eth_if    (eth_if)
        );

    end

endmodule

`resetall
