// SPDX-FileCopyrightText: 2026 Enio Kaljic
// SPDX-License-Identifier: AGPL-3.0-or-later

`resetall
`timescale 1ns / 1ps
`default_nettype none

/*
 * Full endpoint testbench
 */
module test_openenoc_endpoint_full #
(
    parameter IMEM_INIT_FILE = ""
)
();

    logic clk;
    logic rst;

    openenoc_switch_if #(
        .NUM_OF_INTERFACES (openenoc_endpoint_full_csr_pkg::NUM_OF_INTERFACES),
        .TABLE_DEPTH       (openenoc_endpoint_full_csr_pkg::TABLE_DEPTH)
    ) switch_if (
        .clk (clk),
        .rst (rst)
    );

    openenoc_eth_if eth (
        .clk (clk),
        .rst (rst)
    );

    // External side of the Ethernet-like link is idle in this test
    assign eth.a2b.tready = 1'b0;
    assign eth.b2a.tdata  = '0;
    assign eth.b2a.tkeep  = '0;
    assign eth.b2a.tstrb  = '0;
    assign eth.b2a.tid    = '0;
    assign eth.b2a.tdest  = '0;
    assign eth.b2a.tuser  = '0;
    assign eth.b2a.tlast  = 1'b0;
    assign eth.b2a.tvalid = 1'b0;

    initial begin
        switch_if.core_to_csr = '{default: '0};
        switch_if.core_to_csr.forwarding_control.pause_done.next = 1'b1;
    end

    openenoc_endpoint_full #(
        .IMEM_INIT_FILE (IMEM_INIT_FILE)
    )
    uut (
        .clk      (clk),
        .rst      (rst),
        .switch_if (switch_if),
        .eth      (eth)
    );

    /*
    * Verilator-friendly white-box observability. These are testbench-only
    * signals and do not expand the endpoint's external interface.
    */
    wire logic [31:0] imem_word0 = uut.imem_inst.mem[0];
    wire logic [31:0] dmem_status = uut.dmem_inst.mem[0];
    wire logic [31:0] csr_test_value = uut.csr_hwif_out.test_reg.test_field.value;
    wire logic cpu_trap = uut.cpu_trap;

    wire logic [15:0] switch_table_depth =
        switch_if.csr_to_core.info.table_depth.value;
    wire logic [5:0] switch_num_interfaces =
        switch_if.csr_to_core.info.num_of_interfaces.value;
    wire logic switch_pause_done_hwif =
        uut.csr_hwif_in.switch_interface.forwarding_control.pause_done.next;
    wire logic switch_operation_mode =
        switch_if.csr_to_core.forwarding_control.operation_mode.value;
    wire logic switch_pause_request =
        switch_if.csr_to_core.forwarding_control.pause_request.value;
    wire logic [3:0] switch_default_forwarding =
        switch_if.csr_to_core.default_forwarding.bitmap.value;
    wire logic [31:0] endpoint_mac_lo_hwif =
        uut.csr_hwif_in.endpoint_interface.config_.mac_address.lo_word.next;

    wire logic reserved_masters_inactive =
        !uut.endpoint_axil.awvalid && !uut.endpoint_axil.wvalid &&
        !uut.endpoint_axil.arvalid && !uut.endpoint_axil.bready &&
        !uut.endpoint_axil.rready &&
        !uut.debug_axil.awvalid && !uut.debug_axil.wvalid &&
        !uut.debug_axil.arvalid && !uut.debug_axil.bready &&
        !uut.debug_axil.rready;

    wire logic endpoint_eth_inactive = !eth.a2b.tvalid && !eth.b2a.tready;

endmodule

`resetall
