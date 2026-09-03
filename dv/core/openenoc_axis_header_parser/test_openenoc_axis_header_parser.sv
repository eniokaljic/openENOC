// SPDX-FileCopyrightText: 2026 Kerim Bavcic
// SPDX-License-Identifier: AGPL-3.0-or-later

`resetall
`timescale 1ns / 1ps
`default_nettype none

/*
 * AXI4-Stream openENOC header parser testbench
 */
module test_openenoc_axis_header_parser #
(
	/* verilator lint_off WIDTHTRUNC */
	parameter DATA_W = 32,
	parameter logic KEEP_EN = (DATA_W > 8),
	parameter KEEP_W = ((DATA_W + 7) / 8),
	parameter logic STRB_EN = 1'b0,
	parameter logic LAST_EN = 1'b1,
	parameter USER_W = 128,
	parameter DEPTH = 0,
	parameter M_REG_TYPE = 2
	/* verilator lint_on WIDTHTRUNC */
)
();

	logic clk;
	logic rst;

	// input: raw frames, no sideband
	taxi_axis_if #(
		.DATA_W(DATA_W),
		.KEEP_EN(KEEP_EN),
		.KEEP_W(KEEP_W),
		.STRB_EN(STRB_EN),
		.LAST_EN(LAST_EN),
		.USER_EN(1'b0),
		.USER_W(1)
	) s_axis_if();

	// output: delayed frames, 128-bit header on tuser
	taxi_axis_if #(
		.DATA_W(DATA_W),
		.KEEP_EN(KEEP_EN),
		.KEEP_W(KEEP_W),
		.STRB_EN(STRB_EN),
		.LAST_EN(LAST_EN),
		.USER_EN(1'b1),
		.USER_W(USER_W)
	) m_axis_if();

	openenoc_axis_header_parser #(
		.DEPTH(DEPTH),
		.M_REG_TYPE(M_REG_TYPE)
	)
	u_openenoc_axis_header_parser (
		.clk(clk),
		.rst(rst),
		.s_axis(s_axis_if),
		.m_axis(m_axis_if)
	);

endmodule

`resetall
