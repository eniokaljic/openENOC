// SPDX-FileCopyrightText: 2026 Kerim Bavcic
// SPDX-License-Identifier: CERN-OHL-S-2.0

`resetall
`timescale 1ns / 1ps
`default_nettype none

/*
 * AXI4-Stream switch (prototype multicast-capable architecture)
 */
module openenoc_axis_switch #
(
	// Number of AXI stream inputs
	parameter S_COUNT = 4,
	// Number of AXI stream outputs
	parameter M_COUNT = 4,
	// Interface connection control
	parameter logic M_CONNECT[M_COUNT][S_COUNT] = '{M_COUNT{'{S_COUNT{1'b1}}}},
	// Input interface register type
	// 0 to bypass, 1 for simple buffer, 2 for skid buffer
	parameter S_REG_TYPE = 2,
	// Output interface register type
	// 0 to bypass, 1 for simple buffer, 2 for skid buffer
	parameter M_REG_TYPE = 0
)
(
	input  wire logic                      clk,
	input  wire logic                      rst,

	// 1: route via tuser bitmap (multicast), 0: route via tdest MSBs (unicast)
	input  wire logic                      tuser_bitmap_route,

	/*
	 * AXI4-Stream inputs (sink)
	 */
	taxi_axis_if.snk                       s_axis[S_COUNT],

	/*
	 * AXI4-Stream outputs (source)
	 */
	taxi_axis_if.src                       m_axis[M_COUNT]
);

	// extract parameters
	localparam DATA_W = s_axis[0].DATA_W;
	localparam logic KEEP_EN = s_axis[0].KEEP_EN && m_axis[0].KEEP_EN;
	localparam KEEP_W = s_axis[0].KEEP_W;
	localparam logic STRB_EN = s_axis[0].STRB_EN && m_axis[0].STRB_EN;
	localparam logic ID_EN = s_axis[0].ID_EN && m_axis[0].ID_EN;
	localparam S_ID_W = s_axis[0].ID_W;
	localparam M_ID_W = m_axis[0].ID_W;
	localparam logic DEST_EN = s_axis[0].DEST_EN && m_axis[0].DEST_EN;
	localparam S_DEST_W = s_axis[0].DEST_W;
	localparam M_DEST_W = m_axis[0].DEST_W;
	localparam logic USER_EN = s_axis[0].USER_EN && m_axis[0].USER_EN;
	localparam USER_W = s_axis[0].USER_W;

	localparam CL_M_COUNT = M_COUNT > 1 ? $clog2(M_COUNT) : 1;

	// check configuration
	/* verilator lint_off GENUNNAMED */
	if (m_axis[0].DATA_W != DATA_W)
		$fatal(0, "Error: Interface DATA_W parameter mismatch (instance %m)");

	if (KEEP_EN && m_axis[0].KEEP_W != KEEP_W)
		$fatal(0, "Error: Interface KEEP_W parameter mismatch (instance %m)");

	if (!DEST_EN)
		$fatal(0, "Error: DEST_EN is required (instance %m)");

	if (S_DEST_W < CL_M_COUNT)
		$fatal(0, "Error: S_DEST_W too small for port count (instance %m)");

	if (!USER_EN)
		$fatal(0, "Error: USER_EN is required (instance %m)");

	if (USER_W < M_COUNT)
		$fatal(0, "Error: USER_W too small for port count (instance %m)");
	/* verilator lint_on GENUNNAMED */

	taxi_axis_if #(
		.DATA_W(DATA_W),
		.KEEP_EN(KEEP_EN),
		.KEEP_W(KEEP_W),
		.STRB_EN(STRB_EN),
		.LAST_EN(s_axis[0].LAST_EN && m_axis[0].LAST_EN),
		.ID_EN(ID_EN),
		.ID_W(S_ID_W),
		.DEST_EN(DEST_EN),
		.DEST_W(S_DEST_W),
		.USER_EN(USER_EN),
		.USER_W(USER_W)
	) int_s_axis_if[S_COUNT]();

	taxi_axis_if #(
		.DATA_W(DATA_W),
		.KEEP_EN(KEEP_EN),
		.KEEP_W(KEEP_W),
		.STRB_EN(STRB_EN),
		.LAST_EN(s_axis[0].LAST_EN && m_axis[0].LAST_EN),
		.ID_EN(ID_EN),
		.ID_W(M_ID_W),
		.DEST_EN(DEST_EN),
		.DEST_W(M_DEST_W),
		.USER_EN(USER_EN),
		.USER_W(USER_W)
	) int_m_axis_if[M_COUNT]();

	for (genvar s = 0; s < S_COUNT; s = s + 1) begin : s_reg_gen
		taxi_axis_register #(
			.REG_TYPE(S_REG_TYPE)
		)
		u_s_reg (
			.clk(clk),
			.rst(rst),
			.s_axis(s_axis[s]),
			.m_axis(int_s_axis_if[s])
		);
	end

	for (genvar m = 0; m < M_COUNT; m = m + 1) begin : m_reg_gen
		taxi_axis_register #(
			.REG_TYPE(M_REG_TYPE)
		)
		u_m_reg (
			.clk(clk),
			.rst(rst),
			.s_axis(int_m_axis_if[m]),
			.m_axis(m_axis[m])
		);
	end

	logic [DATA_W-1:0]    in_tdata[S_COUNT];
	logic [KEEP_W-1:0]    in_tkeep[S_COUNT];
	logic [KEEP_W-1:0]    in_tstrb[S_COUNT];
	logic [S_ID_W-1:0]    in_tid[S_COUNT];
	logic [S_DEST_W-1:0]  in_tdest[S_COUNT];
	logic [USER_W-1:0]    in_tuser[S_COUNT];
	logic                 in_tlast[S_COUNT];
	logic                 in_tvalid[S_COUNT];
	logic                 in_tready[S_COUNT];

	logic [DATA_W-1:0]    out_tdata[M_COUNT];
	logic [KEEP_W-1:0]    out_tkeep[M_COUNT];
	logic [KEEP_W-1:0]    out_tstrb[M_COUNT];
	logic [M_ID_W-1:0]    out_tid[M_COUNT];
	logic [M_DEST_W-1:0]  out_tdest[M_COUNT];
	logic [USER_W-1:0]    out_tuser[M_COUNT];
	logic                 out_tlast[M_COUNT];
	logic                 out_tvalid[M_COUNT];
	logic                 out_tready[M_COUNT];

	for (genvar s = 0; s < S_COUNT; s = s + 1) begin : s_bridge
		assign in_tdata[s] = int_s_axis_if[s].tdata;
		assign in_tkeep[s] = int_s_axis_if[s].tkeep;
		assign in_tstrb[s] = int_s_axis_if[s].tstrb;
		assign in_tid[s] = int_s_axis_if[s].tid;
		assign in_tdest[s] = int_s_axis_if[s].tdest;
		assign in_tuser[s] = int_s_axis_if[s].tuser;
		assign in_tlast[s] = int_s_axis_if[s].tlast;
		assign in_tvalid[s] = int_s_axis_if[s].tvalid;
		assign int_s_axis_if[s].tready = in_tready[s];
	end

	for (genvar m = 0; m < M_COUNT; m = m + 1) begin : m_bridge
		assign int_m_axis_if[m].tdata = out_tdata[m];
		assign int_m_axis_if[m].tkeep = out_tkeep[m];
		assign int_m_axis_if[m].tstrb = out_tstrb[m];
		assign int_m_axis_if[m].tid = out_tid[m];
		assign int_m_axis_if[m].tdest = out_tdest[m];
		assign int_m_axis_if[m].tuser = out_tuser[m];
		assign int_m_axis_if[m].tlast = out_tlast[m];
		assign int_m_axis_if[m].tvalid = out_tvalid[m];
		assign out_tready[m] = int_m_axis_if[m].tready;
	end

	localparam CL_S_COUNT = S_COUNT > 1 ? $clog2(S_COUNT) : 1;

	logic [CL_S_COUNT-1:0] rr_ptr_reg, rr_ptr_next;

	logic [S_COUNT-1:0] active_reg, active_next;
	logic [S_COUNT-1:0] drop_reg, drop_next;
	logic [M_COUNT-1:0] route_mask_reg[S_COUNT], route_mask_next[S_COUNT];

	logic [M_COUNT-1:0] out_lock_reg, out_lock_next;
	logic [CL_S_COUNT-1:0] out_owner_reg[M_COUNT], out_owner_next[M_COUNT];

	logic [M_COUNT-1:0] out_ready_vec;
	logic [S_COUNT-1:0] in_all_targets_ready;
	logic [S_COUNT-1:0] in_fire;

	logic [M_COUNT-1:0] start_route_mask;
	logic start_route_drop;
	logic start_route_valid;
	logic start_grant;

	wire [CL_S_COUNT-1:0] scan_idx = rr_ptr_reg;

	function automatic logic all_targets_ready(
		logic [M_COUNT-1:0] mask,
		logic [M_COUNT-1:0] ready_vec
	);
		return &(ready_vec | ~mask);
	endfunction

	always_comb begin
		start_route_mask = '0;
		start_route_drop = 1'b1;
		start_route_valid = 1'b0;

		if (in_tvalid[scan_idx] && !active_reg[scan_idx]) begin
			start_route_valid = 1'b1;

			if (tuser_bitmap_route) begin
				start_route_mask = in_tuser[scan_idx][M_COUNT-1:0];
			end else begin
				start_route_mask = '0;
				if (M_COUNT == 1) begin
					start_route_mask[0] = 1'b1;
				end else begin
					start_route_mask[in_tdest[scan_idx][S_DEST_W-1:S_DEST_W-CL_M_COUNT]] = 1'b1;
				end
			end

			// apply input-to-output connectivity permissions
			for (integer om = 0; om < M_COUNT; om = om + 1) begin
				start_route_mask[om] = start_route_mask[om] && M_CONNECT[om][scan_idx];
			end

			start_route_drop = (start_route_mask == '0);
		end

		for (integer m = 0; m < M_COUNT; m = m + 1) begin
			out_ready_vec[m] = out_tready[m];
		end

		for (integer s = 0; s < S_COUNT; s = s + 1) begin
			in_all_targets_ready[s] = all_targets_ready(route_mask_reg[s], out_ready_vec);
		end
	end

	always_comb begin
		for (integer s = 0; s < S_COUNT; s = s + 1) begin
			in_fire[s] = in_tvalid[s] && in_tready[s];
		end
	end

	always_comb begin
		rr_ptr_next = rr_ptr_reg + CL_S_COUNT'(1);

		active_next = active_reg;
		drop_next = drop_reg;
		out_lock_next = out_lock_reg;

		for (integer s = 0; s < S_COUNT; s = s + 1) begin
			route_mask_next[s] = route_mask_reg[s];
		end

		for (integer m = 0; m < M_COUNT; m = m + 1) begin
			out_owner_next[m] = out_owner_reg[m];
		end

		start_grant = 1'b0;

		if (start_route_valid) begin
			if (start_route_drop) begin
				start_grant = 1'b1;
			end else if ((start_route_mask & out_lock_reg) == '0) begin
				start_grant = 1'b1;
			end
		end

		if (start_grant) begin
			active_next[scan_idx] = 1'b1;
			drop_next[scan_idx] = start_route_drop;
			route_mask_next[scan_idx] = start_route_mask;

			if (!start_route_drop) begin
				for (integer m = 0; m < M_COUNT; m = m + 1) begin
					if (start_route_mask[m]) begin
						out_lock_next[m] = 1'b1;
						out_owner_next[m] = scan_idx;
					end
				end
			end
		end

		// release output ownership at frame end
		for (integer s = 0; s < S_COUNT; s = s + 1) begin
			if (active_reg[s] && in_fire[s] && in_tlast[s]) begin
				active_next[s] = 1'b0;
				drop_next[s] = 1'b0;
				route_mask_next[s] = '0;

				for (integer m = 0; m < M_COUNT; m = m + 1) begin
					if (out_lock_reg[m] && out_owner_reg[m] == CL_S_COUNT'(s)) begin
						out_lock_next[m] = 1'b0;
					end
				end
			end
		end
	end

	always_ff @(posedge clk) begin
		rr_ptr_reg <= rr_ptr_next;
		active_reg <= active_next;
		drop_reg <= drop_next;
		out_lock_reg <= out_lock_next;

		for (integer s = 0; s < S_COUNT; s = s + 1) begin
			route_mask_reg[s] <= route_mask_next[s];
		end

		for (integer m = 0; m < M_COUNT; m = m + 1) begin
			out_owner_reg[m] <= out_owner_next[m];
		end

		if (rst) begin
			rr_ptr_reg <= '0;
			active_reg <= '0;
			drop_reg <= '0;
			out_lock_reg <= '0;

			for (integer s = 0; s < S_COUNT; s = s + 1) begin
				route_mask_reg[s] <= '0;
			end

			for (integer m = 0; m < M_COUNT; m = m + 1) begin
				out_owner_reg[m] <= '0;
			end
		end
	end

	for (genvar s = 0; s < S_COUNT; s = s + 1) begin : s_ready_gen
		always_comb begin
			in_tready[s] = 1'b0;

			if (active_reg[s]) begin
				if (drop_reg[s]) begin
					in_tready[s] = 1'b1;
				end else begin
					in_tready[s] = in_all_targets_ready[s];
				end
			end
		end
	end

	for (genvar m = 0; m < M_COUNT; m = m + 1) begin : m_data_gen
		always_comb begin
			logic [CL_S_COUNT-1:0] owner_idx;
			logic owner_active;
			logic owner_valid;

			owner_idx = out_owner_reg[m];
			owner_active = out_lock_reg[m] && active_reg[owner_idx] && !drop_reg[owner_idx] && route_mask_reg[owner_idx][m];
			owner_valid = owner_active && in_tvalid[owner_idx];

			out_tdata[m]  = in_tdata[owner_idx];
			out_tkeep[m]  = KEEP_EN ? in_tkeep[owner_idx] : '1;
			out_tstrb[m]  = STRB_EN ? in_tstrb[owner_idx] : out_tkeep[m];
			out_tvalid[m] = owner_valid;
			out_tlast[m]  = in_tlast[owner_idx];
			out_tid[m]    = ID_EN   ? M_ID_W'(in_tid[owner_idx]) : '0;
			out_tdest[m]  = DEST_EN ? M_DEST_W'(in_tdest[owner_idx]) : '0;
			out_tuser[m]  = USER_EN ? in_tuser[owner_idx] : '0;
		end
	end

endmodule

`resetall
