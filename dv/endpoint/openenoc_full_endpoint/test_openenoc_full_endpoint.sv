// SPDX-FileCopyrightText: 2026 Enio Kaljic
// SPDX-License-Identifier: AGPL-3.0-or-later

`resetall
`timescale 1ns / 1ps
`default_nettype none

/*
 * Full endpoint testbench
 */
module test_openenoc_full_endpoint #
(
    parameter IMEM_INIT_FILE = ""
)
();

logic clk;
logic rst;

openenoc_full_endpoint_csr_pkg::openenoc_full_endpoint_csr__in_t  hwif_in;
openenoc_full_endpoint_csr_pkg::openenoc_full_endpoint_csr__out_t hwif_out;

openenoc_eth_if eth (
    .clk (clk),
    .rst (rst)
);

// External side of the Ethernet-like link is idle in this test.
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
    hwif_in = '{default: '0};
end

openenoc_full_endpoint #(
    .IMEM_INIT_FILE (IMEM_INIT_FILE)
)
uut (
    .clk      (clk),
    .rst      (rst),
    .hwif_in  (hwif_in),
    .hwif_out (hwif_out),
    .eth      (eth)
);

/*
 * Verilator-friendly white-box observability. These are testbench-only
 * signals and do not expand the endpoint's external interface.
 */
wire logic [31:0] imem_word0 = uut.imem_inst.mem[0];
wire logic [31:0] dmem_status = uut.dmem_inst.mem[0];
wire logic [31:0] csr_test_value = hwif_out.test_reg.test_field.value;
wire logic cpu_trap = uut.cpu_trap;

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
