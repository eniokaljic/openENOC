`resetall
`default_nettype none
`resetall
`resetall
`default_nettype none
`resetall
`resetall
`default_nettype none
`resetall
`resetall
`default_nettype none
module taxi_sync_reset (
	clk,
	rst,
	out
);
	parameter N = 2;
	input wire clk;
	input wire rst;
	output wire out;
	(* async_reg = "true", srl_style = "register", shreg_extract = "no" *) reg [N - 1:0] sync_reg = 1'sb1;
	assign out = sync_reg[N - 1];
	always @(posedge clk or posedge rst)
		if (rst)
			sync_reg <= 1'sb1;
		else
			sync_reg <= {sync_reg[N - 2:0], 1'b0};
endmodule
`resetall
`resetall
`default_nettype none
module taxi_sync_signal (
	clk,
	in,
	out
);
	parameter WIDTH = 1;
	parameter N = 2;
	input wire clk;
	input wire [WIDTH - 1:0] in;
	output wire [WIDTH - 1:0] out;
	(* async_reg = "true", srl_style = "register", shreg_extract = "no" *) reg [WIDTH - 1:0] sync_reg [N - 1:0];
	assign out = sync_reg[N - 1];
	always @(posedge clk) begin
		sync_reg[0] <= in;
		begin : sv2v_autoblock_1
			integer k;
			for (k = 1; k < N; k = k + 1)
				sync_reg[k] <= sync_reg[k - 1];
		end
	end
endmodule
`resetall
`resetall
`default_nettype none
`resetall
`resetall
`default_nettype none
`resetall
`resetall
`default_nettype none
module test_openenoc_eth_adapter;
	parameter A_DATA_W = 8;
	parameter A_KEEP_W = (A_DATA_W + 7) / 8;
	parameter [0:0] A_KEEP_EN = A_KEEP_W > 1;
	parameter [0:0] A_STRB_EN = 1'b0;
	parameter [0:0] A_LAST_EN = 1'b1;
	parameter [0:0] A_ID_EN = 1'b0;
	parameter A_ID_W = 8;
	parameter [0:0] A_DEST_EN = 1'b0;
	parameter A_DEST_W = 8;
	parameter [0:0] A_USER_EN = 1'b0;
	parameter A_USER_W = 1;
	parameter B_DATA_W = 8;
	parameter B_KEEP_W = (B_DATA_W + 7) / 8;
	parameter [0:0] B_KEEP_EN = B_KEEP_W > 1;
	parameter [0:0] B_STRB_EN = 1'b0;
	parameter [0:0] B_LAST_EN = 1'b1;
	parameter [0:0] B_ID_EN = 1'b0;
	parameter B_ID_W = 8;
	parameter [0:0] B_DEST_EN = 1'b0;
	parameter B_DEST_W = 8;
	parameter [0:0] B_USER_EN = 1'b0;
	parameter B_USER_W = 1;
	parameter DEPTH = 4096;
	parameter RAM_PIPELINE = 1;
	parameter [0:0] OUTPUT_FIFO_EN = 1'b0;
	parameter [0:0] FRAME_FIFO = 1'b0;
	parameter USER_BAD_FRAME_VALUE = 1'b1;
	parameter USER_BAD_FRAME_MASK = 1'b1;
	parameter [0:0] DROP_OVERSIZE_FRAME = FRAME_FIFO;
	parameter [0:0] DROP_BAD_FRAME = 1'b0;
	parameter [0:0] DROP_WHEN_FULL = 1'b0;
	parameter [0:0] MARK_WHEN_FULL = 1'b0;
	parameter [0:0] FRAME_PAUSE = FRAME_FIFO;
	wire clk_a;
	wire rst_a;
	wire clk_b;
	wire rst_b;
	localparam _param_DF0CF_DATA_W = A_DATA_W;
	localparam _param_DF0CF_KEEP_W = A_KEEP_W;
	localparam _param_DF0CF_KEEP_EN = A_KEEP_EN;
	localparam _param_DF0CF_STRB_EN = A_STRB_EN;
	localparam _param_DF0CF_LAST_EN = A_LAST_EN;
	localparam _param_DF0CF_ID_EN = A_ID_EN;
	localparam _param_DF0CF_ID_W = A_ID_W;
	localparam _param_DF0CF_DEST_EN = A_DEST_EN;
	localparam _param_DF0CF_DEST_W = A_DEST_W;
	localparam _param_DF0CF_USER_EN = A_USER_EN;
	localparam _param_DF0CF_USER_W = A_USER_W;
	generate
		if (1) begin : eth_a
			localparam DATA_W = _param_DF0CF_DATA_W;
			localparam KEEP_W = _param_DF0CF_KEEP_W;
			localparam [0:0] KEEP_EN = _param_DF0CF_KEEP_EN;
			localparam [0:0] STRB_EN = _param_DF0CF_STRB_EN;
			localparam [0:0] LAST_EN = _param_DF0CF_LAST_EN;
			localparam [0:0] ID_EN = _param_DF0CF_ID_EN;
			localparam ID_W = _param_DF0CF_ID_W;
			localparam [0:0] DEST_EN = _param_DF0CF_DEST_EN;
			localparam DEST_W = _param_DF0CF_DEST_W;
			localparam [0:0] USER_EN = _param_DF0CF_USER_EN;
			localparam USER_W = _param_DF0CF_USER_W;
			wire clk;
			wire rst;
			localparam _param_15287_DATA_W = DATA_W;
			localparam _param_15287_KEEP_W = KEEP_W;
			localparam _param_15287_KEEP_EN = KEEP_EN;
			localparam _param_15287_STRB_EN = STRB_EN;
			localparam _param_15287_LAST_EN = LAST_EN;
			localparam _param_15287_ID_EN = ID_EN;
			localparam _param_15287_ID_W = ID_W;
			localparam _param_15287_DEST_EN = DEST_EN;
			localparam _param_15287_DEST_W = DEST_W;
			localparam _param_15287_USER_EN = USER_EN;
			localparam _param_15287_USER_W = USER_W;
			if (1) begin : a2b
				localparam DATA_W = _param_15287_DATA_W;
				localparam KEEP_W = _param_15287_KEEP_W;
				localparam [0:0] KEEP_EN = _param_15287_KEEP_EN;
				localparam [0:0] STRB_EN = _param_15287_STRB_EN;
				localparam [0:0] LAST_EN = _param_15287_LAST_EN;
				localparam [0:0] ID_EN = _param_15287_ID_EN;
				localparam ID_W = _param_15287_ID_W;
				localparam [0:0] DEST_EN = _param_15287_DEST_EN;
				localparam DEST_W = _param_15287_DEST_W;
				localparam [0:0] USER_EN = _param_15287_USER_EN;
				localparam USER_W = _param_15287_USER_W;
				wire [DATA_W - 1:0] tdata;
				wire [KEEP_W - 1:0] tkeep;
				wire [KEEP_W - 1:0] tstrb;
				wire [ID_W - 1:0] tid;
				wire [DEST_W - 1:0] tdest;
				wire [USER_W - 1:0] tuser;
				wire tlast;
				wire tvalid;
				wire tready;
			end
			localparam _param_0326D_DATA_W = DATA_W;
			localparam _param_0326D_KEEP_W = KEEP_W;
			localparam _param_0326D_KEEP_EN = KEEP_EN;
			localparam _param_0326D_STRB_EN = STRB_EN;
			localparam _param_0326D_LAST_EN = LAST_EN;
			localparam _param_0326D_ID_EN = ID_EN;
			localparam _param_0326D_ID_W = ID_W;
			localparam _param_0326D_DEST_EN = DEST_EN;
			localparam _param_0326D_DEST_W = DEST_W;
			localparam _param_0326D_USER_EN = USER_EN;
			localparam _param_0326D_USER_W = USER_W;
			if (1) begin : b2a
				localparam DATA_W = _param_0326D_DATA_W;
				localparam KEEP_W = _param_0326D_KEEP_W;
				localparam [0:0] KEEP_EN = _param_0326D_KEEP_EN;
				localparam [0:0] STRB_EN = _param_0326D_STRB_EN;
				localparam [0:0] LAST_EN = _param_0326D_LAST_EN;
				localparam [0:0] ID_EN = _param_0326D_ID_EN;
				localparam ID_W = _param_0326D_ID_W;
				localparam [0:0] DEST_EN = _param_0326D_DEST_EN;
				localparam DEST_W = _param_0326D_DEST_W;
				localparam [0:0] USER_EN = _param_0326D_USER_EN;
				localparam USER_W = _param_0326D_USER_W;
				wire [DATA_W - 1:0] tdata;
				wire [KEEP_W - 1:0] tkeep;
				wire [KEEP_W - 1:0] tstrb;
				wire [ID_W - 1:0] tid;
				wire [DEST_W - 1:0] tdest;
				wire [USER_W - 1:0] tuser;
				wire tlast;
				wire tvalid;
				wire tready;
			end
		end
	endgenerate
	assign eth_a.clk = clk_a;
	assign eth_a.rst = rst_a;
	localparam _param_79F58_DATA_W = B_DATA_W;
	localparam _param_79F58_KEEP_W = B_KEEP_W;
	localparam _param_79F58_KEEP_EN = B_KEEP_EN;
	localparam _param_79F58_STRB_EN = B_STRB_EN;
	localparam _param_79F58_LAST_EN = B_LAST_EN;
	localparam _param_79F58_ID_EN = B_ID_EN;
	localparam _param_79F58_ID_W = B_ID_W;
	localparam _param_79F58_DEST_EN = B_DEST_EN;
	localparam _param_79F58_DEST_W = B_DEST_W;
	localparam _param_79F58_USER_EN = B_USER_EN;
	localparam _param_79F58_USER_W = B_USER_W;
	generate
		if (1) begin : eth_b
			localparam DATA_W = _param_79F58_DATA_W;
			localparam KEEP_W = _param_79F58_KEEP_W;
			localparam [0:0] KEEP_EN = _param_79F58_KEEP_EN;
			localparam [0:0] STRB_EN = _param_79F58_STRB_EN;
			localparam [0:0] LAST_EN = _param_79F58_LAST_EN;
			localparam [0:0] ID_EN = _param_79F58_ID_EN;
			localparam ID_W = _param_79F58_ID_W;
			localparam [0:0] DEST_EN = _param_79F58_DEST_EN;
			localparam DEST_W = _param_79F58_DEST_W;
			localparam [0:0] USER_EN = _param_79F58_USER_EN;
			localparam USER_W = _param_79F58_USER_W;
			wire clk;
			wire rst;
			localparam _param_F347A_DATA_W = DATA_W;
			localparam _param_F347A_KEEP_W = KEEP_W;
			localparam _param_F347A_KEEP_EN = KEEP_EN;
			localparam _param_F347A_STRB_EN = STRB_EN;
			localparam _param_F347A_LAST_EN = LAST_EN;
			localparam _param_F347A_ID_EN = ID_EN;
			localparam _param_F347A_ID_W = ID_W;
			localparam _param_F347A_DEST_EN = DEST_EN;
			localparam _param_F347A_DEST_W = DEST_W;
			localparam _param_F347A_USER_EN = USER_EN;
			localparam _param_F347A_USER_W = USER_W;
			if (1) begin : a2b
				localparam DATA_W = _param_F347A_DATA_W;
				localparam KEEP_W = _param_F347A_KEEP_W;
				localparam [0:0] KEEP_EN = _param_F347A_KEEP_EN;
				localparam [0:0] STRB_EN = _param_F347A_STRB_EN;
				localparam [0:0] LAST_EN = _param_F347A_LAST_EN;
				localparam [0:0] ID_EN = _param_F347A_ID_EN;
				localparam ID_W = _param_F347A_ID_W;
				localparam [0:0] DEST_EN = _param_F347A_DEST_EN;
				localparam DEST_W = _param_F347A_DEST_W;
				localparam [0:0] USER_EN = _param_F347A_USER_EN;
				localparam USER_W = _param_F347A_USER_W;
				wire [DATA_W - 1:0] tdata;
				wire [KEEP_W - 1:0] tkeep;
				wire [KEEP_W - 1:0] tstrb;
				wire [ID_W - 1:0] tid;
				wire [DEST_W - 1:0] tdest;
				wire [USER_W - 1:0] tuser;
				wire tlast;
				wire tvalid;
				wire tready;
			end
			localparam _param_28470_DATA_W = DATA_W;
			localparam _param_28470_KEEP_W = KEEP_W;
			localparam _param_28470_KEEP_EN = KEEP_EN;
			localparam _param_28470_STRB_EN = STRB_EN;
			localparam _param_28470_LAST_EN = LAST_EN;
			localparam _param_28470_ID_EN = ID_EN;
			localparam _param_28470_ID_W = ID_W;
			localparam _param_28470_DEST_EN = DEST_EN;
			localparam _param_28470_DEST_W = DEST_W;
			localparam _param_28470_USER_EN = USER_EN;
			localparam _param_28470_USER_W = USER_W;
			if (1) begin : b2a
				localparam DATA_W = _param_28470_DATA_W;
				localparam KEEP_W = _param_28470_KEEP_W;
				localparam [0:0] KEEP_EN = _param_28470_KEEP_EN;
				localparam [0:0] STRB_EN = _param_28470_STRB_EN;
				localparam [0:0] LAST_EN = _param_28470_LAST_EN;
				localparam [0:0] ID_EN = _param_28470_ID_EN;
				localparam ID_W = _param_28470_ID_W;
				localparam [0:0] DEST_EN = _param_28470_DEST_EN;
				localparam DEST_W = _param_28470_DEST_W;
				localparam [0:0] USER_EN = _param_28470_USER_EN;
				localparam USER_W = _param_28470_USER_W;
				wire [DATA_W - 1:0] tdata;
				wire [KEEP_W - 1:0] tkeep;
				wire [KEEP_W - 1:0] tstrb;
				wire [ID_W - 1:0] tid;
				wire [DEST_W - 1:0] tdest;
				wire [USER_W - 1:0] tuser;
				wire tlast;
				wire tvalid;
				wire tready;
			end
		end
	endgenerate
	assign eth_b.clk = clk_b;
	assign eth_b.rst = rst_b;
	localparam _param_177B3_DEPTH = DEPTH;
	localparam _param_177B3_RAM_PIPELINE = RAM_PIPELINE;
	localparam _param_177B3_OUTPUT_FIFO_EN = OUTPUT_FIFO_EN;
	localparam _param_177B3_FRAME_FIFO = FRAME_FIFO;
	localparam _param_177B3_USER_BAD_FRAME_VALUE = USER_BAD_FRAME_VALUE;
	localparam _param_177B3_USER_BAD_FRAME_MASK = USER_BAD_FRAME_MASK;
	localparam _param_177B3_DROP_OVERSIZE_FRAME = DROP_OVERSIZE_FRAME;
	localparam _param_177B3_DROP_BAD_FRAME = DROP_BAD_FRAME;
	localparam _param_177B3_DROP_WHEN_FULL = DROP_WHEN_FULL;
	localparam _param_177B3_MARK_WHEN_FULL = MARK_WHEN_FULL;
	localparam _param_177B3_FRAME_PAUSE = FRAME_PAUSE;
	generate
		if (1) begin : uut
			localparam DEPTH = _param_177B3_DEPTH;
			localparam RAM_PIPELINE = _param_177B3_RAM_PIPELINE;
			localparam [0:0] OUTPUT_FIFO_EN = _param_177B3_OUTPUT_FIFO_EN;
			localparam [0:0] FRAME_FIFO = _param_177B3_FRAME_FIFO;
			localparam USER_BAD_FRAME_VALUE = _param_177B3_USER_BAD_FRAME_VALUE;
			localparam USER_BAD_FRAME_MASK = _param_177B3_USER_BAD_FRAME_MASK;
			localparam [0:0] DROP_OVERSIZE_FRAME = _param_177B3_DROP_OVERSIZE_FRAME;
			localparam [0:0] DROP_BAD_FRAME = _param_177B3_DROP_BAD_FRAME;
			localparam [0:0] DROP_WHEN_FULL = _param_177B3_DROP_WHEN_FULL;
			localparam [0:0] MARK_WHEN_FULL = _param_177B3_MARK_WHEN_FULL;
			localparam [0:0] FRAME_PAUSE = _param_177B3_FRAME_PAUSE;
			localparam _param_32DB7_DATA_W = _param_DF0CF_DATA_W;
			localparam _param_32DB7_KEEP_W = _param_DF0CF_KEEP_W;
			localparam _param_32DB7_KEEP_EN = _param_DF0CF_KEEP_EN;
			localparam _param_32DB7_STRB_EN = _param_DF0CF_STRB_EN;
			localparam _param_32DB7_LAST_EN = _param_DF0CF_LAST_EN;
			localparam _param_32DB7_ID_EN = _param_DF0CF_ID_EN;
			localparam _param_32DB7_ID_W = _param_DF0CF_ID_W;
			localparam _param_32DB7_DEST_EN = _param_DF0CF_DEST_EN;
			localparam _param_32DB7_DEST_W = _param_DF0CF_DEST_W;
			localparam _param_32DB7_USER_EN = _param_DF0CF_USER_EN;
			localparam _param_32DB7_USER_W = _param_DF0CF_USER_W;
			if (1) begin : fifo_a2b_s_axis
				localparam DATA_W = _param_32DB7_DATA_W;
				localparam KEEP_W = _param_32DB7_KEEP_W;
				localparam [0:0] KEEP_EN = _param_32DB7_KEEP_EN;
				localparam [0:0] STRB_EN = _param_32DB7_STRB_EN;
				localparam [0:0] LAST_EN = _param_32DB7_LAST_EN;
				localparam [0:0] ID_EN = _param_32DB7_ID_EN;
				localparam ID_W = _param_32DB7_ID_W;
				localparam [0:0] DEST_EN = _param_32DB7_DEST_EN;
				localparam DEST_W = _param_32DB7_DEST_W;
				localparam [0:0] USER_EN = _param_32DB7_USER_EN;
				localparam USER_W = _param_32DB7_USER_W;
				wire [DATA_W - 1:0] tdata;
				wire [KEEP_W - 1:0] tkeep;
				wire [KEEP_W - 1:0] tstrb;
				wire [ID_W - 1:0] tid;
				wire [DEST_W - 1:0] tdest;
				wire [USER_W - 1:0] tuser;
				wire tlast;
				wire tvalid;
				wire tready;
			end
			localparam _param_368DC_DATA_W = _param_79F58_DATA_W;
			localparam _param_368DC_KEEP_W = _param_79F58_KEEP_W;
			localparam _param_368DC_KEEP_EN = _param_79F58_KEEP_EN;
			localparam _param_368DC_STRB_EN = _param_79F58_STRB_EN;
			localparam _param_368DC_LAST_EN = _param_79F58_LAST_EN;
			localparam _param_368DC_ID_EN = _param_79F58_ID_EN;
			localparam _param_368DC_ID_W = _param_79F58_ID_W;
			localparam _param_368DC_DEST_EN = _param_79F58_DEST_EN;
			localparam _param_368DC_DEST_W = _param_79F58_DEST_W;
			localparam _param_368DC_USER_EN = _param_79F58_USER_EN;
			localparam _param_368DC_USER_W = _param_79F58_USER_W;
			if (1) begin : fifo_a2b_m_axis
				localparam DATA_W = _param_368DC_DATA_W;
				localparam KEEP_W = _param_368DC_KEEP_W;
				localparam [0:0] KEEP_EN = _param_368DC_KEEP_EN;
				localparam [0:0] STRB_EN = _param_368DC_STRB_EN;
				localparam [0:0] LAST_EN = _param_368DC_LAST_EN;
				localparam [0:0] ID_EN = _param_368DC_ID_EN;
				localparam ID_W = _param_368DC_ID_W;
				localparam [0:0] DEST_EN = _param_368DC_DEST_EN;
				localparam DEST_W = _param_368DC_DEST_W;
				localparam [0:0] USER_EN = _param_368DC_USER_EN;
				localparam USER_W = _param_368DC_USER_W;
				wire [DATA_W - 1:0] tdata;
				wire [KEEP_W - 1:0] tkeep;
				wire [KEEP_W - 1:0] tstrb;
				wire [ID_W - 1:0] tid;
				wire [DEST_W - 1:0] tdest;
				wire [USER_W - 1:0] tuser;
				wire tlast;
				wire tvalid;
				wire tready;
			end
			localparam _param_2EBF5_DATA_W = _param_79F58_DATA_W;
			localparam _param_2EBF5_KEEP_W = _param_79F58_KEEP_W;
			localparam _param_2EBF5_KEEP_EN = _param_79F58_KEEP_EN;
			localparam _param_2EBF5_STRB_EN = _param_79F58_STRB_EN;
			localparam _param_2EBF5_LAST_EN = _param_79F58_LAST_EN;
			localparam _param_2EBF5_ID_EN = _param_79F58_ID_EN;
			localparam _param_2EBF5_ID_W = _param_79F58_ID_W;
			localparam _param_2EBF5_DEST_EN = _param_79F58_DEST_EN;
			localparam _param_2EBF5_DEST_W = _param_79F58_DEST_W;
			localparam _param_2EBF5_USER_EN = _param_79F58_USER_EN;
			localparam _param_2EBF5_USER_W = _param_79F58_USER_W;
			if (1) begin : fifo_b2a_s_axis
				localparam DATA_W = _param_2EBF5_DATA_W;
				localparam KEEP_W = _param_2EBF5_KEEP_W;
				localparam [0:0] KEEP_EN = _param_2EBF5_KEEP_EN;
				localparam [0:0] STRB_EN = _param_2EBF5_STRB_EN;
				localparam [0:0] LAST_EN = _param_2EBF5_LAST_EN;
				localparam [0:0] ID_EN = _param_2EBF5_ID_EN;
				localparam ID_W = _param_2EBF5_ID_W;
				localparam [0:0] DEST_EN = _param_2EBF5_DEST_EN;
				localparam DEST_W = _param_2EBF5_DEST_W;
				localparam [0:0] USER_EN = _param_2EBF5_USER_EN;
				localparam USER_W = _param_2EBF5_USER_W;
				wire [DATA_W - 1:0] tdata;
				wire [KEEP_W - 1:0] tkeep;
				wire [KEEP_W - 1:0] tstrb;
				wire [ID_W - 1:0] tid;
				wire [DEST_W - 1:0] tdest;
				wire [USER_W - 1:0] tuser;
				wire tlast;
				wire tvalid;
				wire tready;
			end
			localparam _param_330AD_DATA_W = _param_DF0CF_DATA_W;
			localparam _param_330AD_KEEP_W = _param_DF0CF_KEEP_W;
			localparam _param_330AD_KEEP_EN = _param_DF0CF_KEEP_EN;
			localparam _param_330AD_STRB_EN = _param_DF0CF_STRB_EN;
			localparam _param_330AD_LAST_EN = _param_DF0CF_LAST_EN;
			localparam _param_330AD_ID_EN = _param_DF0CF_ID_EN;
			localparam _param_330AD_ID_W = _param_DF0CF_ID_W;
			localparam _param_330AD_DEST_EN = _param_DF0CF_DEST_EN;
			localparam _param_330AD_DEST_W = _param_DF0CF_DEST_W;
			localparam _param_330AD_USER_EN = _param_DF0CF_USER_EN;
			localparam _param_330AD_USER_W = _param_DF0CF_USER_W;
			if (1) begin : fifo_b2a_m_axis
				localparam DATA_W = _param_330AD_DATA_W;
				localparam KEEP_W = _param_330AD_KEEP_W;
				localparam [0:0] KEEP_EN = _param_330AD_KEEP_EN;
				localparam [0:0] STRB_EN = _param_330AD_STRB_EN;
				localparam [0:0] LAST_EN = _param_330AD_LAST_EN;
				localparam [0:0] ID_EN = _param_330AD_ID_EN;
				localparam ID_W = _param_330AD_ID_W;
				localparam [0:0] DEST_EN = _param_330AD_DEST_EN;
				localparam DEST_W = _param_330AD_DEST_W;
				localparam [0:0] USER_EN = _param_330AD_USER_EN;
				localparam USER_W = _param_330AD_USER_W;
				wire [DATA_W - 1:0] tdata;
				wire [KEEP_W - 1:0] tkeep;
				wire [KEEP_W - 1:0] tstrb;
				wire [ID_W - 1:0] tid;
				wire [DEST_W - 1:0] tdest;
				wire [USER_W - 1:0] tuser;
				wire tlast;
				wire tvalid;
				wire tready;
			end
			assign fifo_a2b_s_axis.tdata = test_openenoc_eth_adapter.eth_a.a2b.tdata;
			assign fifo_a2b_s_axis.tkeep = test_openenoc_eth_adapter.eth_a.a2b.tkeep;
			assign fifo_a2b_s_axis.tstrb = test_openenoc_eth_adapter.eth_a.a2b.tstrb;
			assign fifo_a2b_s_axis.tid = test_openenoc_eth_adapter.eth_a.a2b.tid;
			assign fifo_a2b_s_axis.tdest = test_openenoc_eth_adapter.eth_a.a2b.tdest;
			assign fifo_a2b_s_axis.tuser = test_openenoc_eth_adapter.eth_a.a2b.tuser;
			assign fifo_a2b_s_axis.tlast = test_openenoc_eth_adapter.eth_a.a2b.tlast;
			assign fifo_a2b_s_axis.tvalid = test_openenoc_eth_adapter.eth_a.a2b.tvalid;
			assign test_openenoc_eth_adapter.eth_a.a2b.tready = fifo_a2b_s_axis.tready;
			assign test_openenoc_eth_adapter.eth_b.a2b.tdata = fifo_a2b_m_axis.tdata;
			assign test_openenoc_eth_adapter.eth_b.a2b.tkeep = fifo_a2b_m_axis.tkeep;
			assign test_openenoc_eth_adapter.eth_b.a2b.tstrb = fifo_a2b_m_axis.tstrb;
			assign test_openenoc_eth_adapter.eth_b.a2b.tid = fifo_a2b_m_axis.tid;
			assign test_openenoc_eth_adapter.eth_b.a2b.tdest = fifo_a2b_m_axis.tdest;
			assign test_openenoc_eth_adapter.eth_b.a2b.tuser = fifo_a2b_m_axis.tuser;
			assign test_openenoc_eth_adapter.eth_b.a2b.tlast = fifo_a2b_m_axis.tlast;
			assign test_openenoc_eth_adapter.eth_b.a2b.tvalid = fifo_a2b_m_axis.tvalid;
			assign fifo_a2b_m_axis.tready = test_openenoc_eth_adapter.eth_b.a2b.tready;
			assign fifo_b2a_s_axis.tdata = test_openenoc_eth_adapter.eth_b.b2a.tdata;
			assign fifo_b2a_s_axis.tkeep = test_openenoc_eth_adapter.eth_b.b2a.tkeep;
			assign fifo_b2a_s_axis.tstrb = test_openenoc_eth_adapter.eth_b.b2a.tstrb;
			assign fifo_b2a_s_axis.tid = test_openenoc_eth_adapter.eth_b.b2a.tid;
			assign fifo_b2a_s_axis.tdest = test_openenoc_eth_adapter.eth_b.b2a.tdest;
			assign fifo_b2a_s_axis.tuser = test_openenoc_eth_adapter.eth_b.b2a.tuser;
			assign fifo_b2a_s_axis.tlast = test_openenoc_eth_adapter.eth_b.b2a.tlast;
			assign fifo_b2a_s_axis.tvalid = test_openenoc_eth_adapter.eth_b.b2a.tvalid;
			assign test_openenoc_eth_adapter.eth_b.b2a.tready = fifo_b2a_s_axis.tready;
			assign test_openenoc_eth_adapter.eth_a.b2a.tdata = fifo_b2a_m_axis.tdata;
			assign test_openenoc_eth_adapter.eth_a.b2a.tkeep = fifo_b2a_m_axis.tkeep;
			assign test_openenoc_eth_adapter.eth_a.b2a.tstrb = fifo_b2a_m_axis.tstrb;
			assign test_openenoc_eth_adapter.eth_a.b2a.tid = fifo_b2a_m_axis.tid;
			assign test_openenoc_eth_adapter.eth_a.b2a.tdest = fifo_b2a_m_axis.tdest;
			assign test_openenoc_eth_adapter.eth_a.b2a.tuser = fifo_b2a_m_axis.tuser;
			assign test_openenoc_eth_adapter.eth_a.b2a.tlast = fifo_b2a_m_axis.tlast;
			assign test_openenoc_eth_adapter.eth_a.b2a.tvalid = fifo_b2a_m_axis.tvalid;
			assign fifo_b2a_m_axis.tready = test_openenoc_eth_adapter.eth_a.b2a.tready;
			localparam _param_259FE_DEPTH = DEPTH;
			localparam _param_259FE_RAM_PIPELINE = RAM_PIPELINE;
			localparam _param_259FE_OUTPUT_FIFO_EN = OUTPUT_FIFO_EN;
			localparam _param_259FE_FRAME_FIFO = FRAME_FIFO;
			localparam _param_259FE_USER_BAD_FRAME_VALUE = USER_BAD_FRAME_VALUE;
			localparam _param_259FE_USER_BAD_FRAME_MASK = USER_BAD_FRAME_MASK;
			localparam _param_259FE_DROP_OVERSIZE_FRAME = DROP_OVERSIZE_FRAME;
			localparam _param_259FE_DROP_BAD_FRAME = DROP_BAD_FRAME;
			localparam _param_259FE_DROP_WHEN_FULL = DROP_WHEN_FULL;
			localparam _param_259FE_MARK_WHEN_FULL = MARK_WHEN_FULL;
			localparam _param_259FE_PAUSE_EN = 1'b0;
			localparam _param_259FE_FRAME_PAUSE = FRAME_PAUSE;
			if (1) begin : fifo_a2b_inst
				localparam DEPTH = _param_259FE_DEPTH;
				localparam RAM_PIPELINE = _param_259FE_RAM_PIPELINE;
				localparam [0:0] OUTPUT_FIFO_EN = _param_259FE_OUTPUT_FIFO_EN;
				localparam [0:0] FRAME_FIFO = _param_259FE_FRAME_FIFO;
				localparam USER_BAD_FRAME_VALUE = _param_259FE_USER_BAD_FRAME_VALUE;
				localparam USER_BAD_FRAME_MASK = _param_259FE_USER_BAD_FRAME_MASK;
				localparam [0:0] DROP_OVERSIZE_FRAME = _param_259FE_DROP_OVERSIZE_FRAME;
				localparam [0:0] DROP_BAD_FRAME = _param_259FE_DROP_BAD_FRAME;
				localparam [0:0] DROP_WHEN_FULL = _param_259FE_DROP_WHEN_FULL;
				localparam [0:0] MARK_WHEN_FULL = _param_259FE_MARK_WHEN_FULL;
				localparam [0:0] PAUSE_EN = _param_259FE_PAUSE_EN;
				localparam [0:0] FRAME_PAUSE = _param_259FE_FRAME_PAUSE;
				wire s_clk;
				wire s_rst;
				wire m_clk;
				wire m_rst;
				wire s_pause_req;
				wire s_pause_ack;
				wire m_pause_req;
				wire m_pause_ack;
				wire [$clog2(DEPTH):0] s_status_depth;
				wire [$clog2(DEPTH):0] s_status_depth_commit;
				wire s_status_overflow;
				wire s_status_bad_frame;
				wire s_status_good_frame;
				wire [$clog2(DEPTH):0] m_status_depth;
				wire [$clog2(DEPTH):0] m_status_depth_commit;
				wire m_status_overflow;
				wire m_status_bad_frame;
				wire m_status_good_frame;
				localparam S_DATA_W = _param_32DB7_DATA_W;
				localparam [0:0] S_KEEP_EN = _param_32DB7_KEEP_EN;
				localparam S_KEEP_W = _param_32DB7_KEEP_W;
				localparam [0:0] S_STRB_EN = _param_32DB7_STRB_EN;
				localparam M_DATA_W = _param_368DC_DATA_W;
				localparam [0:0] M_KEEP_EN = _param_368DC_KEEP_EN;
				localparam M_KEEP_W = _param_368DC_KEEP_W;
				localparam [0:0] M_STRB_EN = _param_368DC_STRB_EN;
				localparam S_BYTE_LANES = (S_KEEP_EN ? S_KEEP_W : 1);
				localparam M_BYTE_LANES = (M_KEEP_EN ? M_KEEP_W : 1);
				localparam S_BYTE_SIZE = S_DATA_W / S_BYTE_LANES;
				localparam M_BYTE_SIZE = M_DATA_W / M_BYTE_LANES;
				localparam EXPAND_BUS = M_BYTE_LANES > S_BYTE_LANES;
				localparam DATA_W = (EXPAND_BUS ? M_DATA_W : S_DATA_W);
				localparam KEEP_W = (EXPAND_BUS ? M_BYTE_LANES : S_BYTE_LANES);
				localparam KEEP_EN = (EXPAND_BUS ? M_KEEP_EN : S_KEEP_EN);
				localparam STRB_EN = M_STRB_EN && S_STRB_EN;
				if ((S_BYTE_SIZE * S_BYTE_LANES) != S_DATA_W) begin : genblk1
					initial begin
						$display("Fatal [elaboration] /home/enio/Projects/openENOC/libs/taxi/src/axis/rtl/taxi_axis_async_fifo_adapter.sv:122:5 - taxi_axis_async_fifo_adapter.genblk1\n msg: ", "Error: input data width not evenly divisible (instance %m)");
						$finish(0);
					end
				end
				if ((M_BYTE_SIZE * M_BYTE_LANES) != M_DATA_W) begin : genblk2
					initial begin
						$display("Fatal [elaboration] /home/enio/Projects/openENOC/libs/taxi/src/axis/rtl/taxi_axis_async_fifo_adapter.sv:125:5 - taxi_axis_async_fifo_adapter.genblk2\n msg: ", "Error: output data width not evenly divisible (instance %m)");
						$finish(0);
					end
				end
				if (S_BYTE_SIZE != M_BYTE_SIZE) begin : genblk3
					initial begin
						$display("Fatal [elaboration] /home/enio/Projects/openENOC/libs/taxi/src/axis/rtl/taxi_axis_async_fifo_adapter.sv:128:5 - taxi_axis_async_fifo_adapter.genblk3\n msg: ", "Error: byte size mismatch (instance %m)");
						$finish(0);
					end
				end
				localparam _param_D01DF_DATA_W = DATA_W;
				localparam _param_D01DF_KEEP_EN = KEEP_EN;
				localparam _param_D01DF_KEEP_W = KEEP_W;
				localparam _param_D01DF_STRB_EN = _param_32DB7_STRB_EN;
				localparam _param_D01DF_LAST_EN = _param_32DB7_LAST_EN;
				localparam _param_D01DF_ID_EN = _param_32DB7_ID_EN;
				localparam _param_D01DF_ID_W = _param_32DB7_ID_W;
				localparam _param_D01DF_DEST_EN = _param_32DB7_DEST_EN;
				localparam _param_D01DF_DEST_W = _param_32DB7_DEST_W;
				localparam _param_D01DF_USER_EN = _param_32DB7_USER_EN;
				localparam _param_D01DF_USER_W = _param_32DB7_USER_W;
				if (1) begin : axis_pre_fifo
					localparam DATA_W = _param_D01DF_DATA_W;
					localparam KEEP_W = _param_D01DF_KEEP_W;
					localparam [0:0] KEEP_EN = _param_D01DF_KEEP_EN;
					localparam [0:0] STRB_EN = _param_D01DF_STRB_EN;
					localparam [0:0] LAST_EN = _param_D01DF_LAST_EN;
					localparam [0:0] ID_EN = _param_D01DF_ID_EN;
					localparam ID_W = _param_D01DF_ID_W;
					localparam [0:0] DEST_EN = _param_D01DF_DEST_EN;
					localparam DEST_W = _param_D01DF_DEST_W;
					localparam [0:0] USER_EN = _param_D01DF_USER_EN;
					localparam USER_W = _param_D01DF_USER_W;
					wire [DATA_W - 1:0] tdata;
					wire [KEEP_W - 1:0] tkeep;
					wire [KEEP_W - 1:0] tstrb;
					wire [ID_W - 1:0] tid;
					wire [DEST_W - 1:0] tdest;
					wire [USER_W - 1:0] tuser;
					wire tlast;
					wire tvalid;
					wire tready;
				end
				localparam _param_66B8B_DATA_W = DATA_W;
				localparam _param_66B8B_KEEP_EN = KEEP_EN;
				localparam _param_66B8B_KEEP_W = KEEP_W;
				localparam _param_66B8B_STRB_EN = _param_368DC_STRB_EN;
				localparam _param_66B8B_LAST_EN = _param_368DC_LAST_EN;
				localparam _param_66B8B_ID_EN = _param_368DC_ID_EN;
				localparam _param_66B8B_ID_W = _param_368DC_ID_W;
				localparam _param_66B8B_DEST_EN = _param_368DC_DEST_EN;
				localparam _param_66B8B_DEST_W = _param_368DC_DEST_W;
				localparam _param_66B8B_USER_EN = _param_368DC_USER_EN;
				localparam _param_66B8B_USER_W = _param_368DC_USER_W;
				if (1) begin : axis_post_fifo
					localparam DATA_W = _param_66B8B_DATA_W;
					localparam KEEP_W = _param_66B8B_KEEP_W;
					localparam [0:0] KEEP_EN = _param_66B8B_KEEP_EN;
					localparam [0:0] STRB_EN = _param_66B8B_STRB_EN;
					localparam [0:0] LAST_EN = _param_66B8B_LAST_EN;
					localparam [0:0] ID_EN = _param_66B8B_ID_EN;
					localparam ID_W = _param_66B8B_ID_W;
					localparam [0:0] DEST_EN = _param_66B8B_DEST_EN;
					localparam DEST_W = _param_66B8B_DEST_W;
					localparam [0:0] USER_EN = _param_66B8B_USER_EN;
					localparam USER_W = _param_66B8B_USER_W;
					wire [DATA_W - 1:0] tdata;
					wire [KEEP_W - 1:0] tkeep;
					wire [KEEP_W - 1:0] tstrb;
					wire [ID_W - 1:0] tid;
					wire [DEST_W - 1:0] tdest;
					wire [USER_W - 1:0] tuser;
					wire tlast;
					wire tvalid;
					wire tready;
				end
				if (1) begin : pre_fifo_adapter_inst
					wire clk;
					wire rst;
					localparam S_DATA_W = _param_32DB7_DATA_W;
					localparam [0:0] S_KEEP_EN = _param_32DB7_KEEP_EN;
					localparam S_KEEP_W = _param_32DB7_KEEP_W;
					localparam [0:0] STRB_EN = _param_32DB7_STRB_EN && _param_D01DF_STRB_EN;
					localparam [0:0] LAST_EN = _param_32DB7_LAST_EN;
					localparam [0:0] ID_EN = _param_32DB7_ID_EN && _param_D01DF_ID_EN;
					localparam ID_W = _param_32DB7_ID_W;
					localparam [0:0] DEST_EN = _param_32DB7_DEST_EN && _param_D01DF_DEST_EN;
					localparam DEST_W = _param_32DB7_DEST_W;
					localparam [0:0] USER_EN = _param_32DB7_USER_EN && _param_D01DF_USER_EN;
					localparam USER_W = _param_32DB7_USER_W;
					localparam M_DATA_W = _param_D01DF_DATA_W;
					localparam [0:0] M_KEEP_EN = _param_D01DF_KEEP_EN;
					localparam M_KEEP_W = _param_D01DF_KEEP_W;
					localparam S_BYTE_LANES = (S_KEEP_EN ? S_KEEP_W : 1);
					localparam M_BYTE_LANES = (M_KEEP_EN ? M_KEEP_W : 1);
					localparam S_BYTE_SIZE = S_DATA_W / S_BYTE_LANES;
					localparam M_BYTE_SIZE = M_DATA_W / M_BYTE_LANES;
					if ((S_BYTE_SIZE * S_BYTE_LANES) != S_DATA_W) begin : genblk1
						initial begin
							$display("Fatal [elaboration] /home/enio/Projects/openENOC/libs/taxi/src/axis/rtl/taxi_axis_adapter.sv:61:5 - taxi_axis_adapter.genblk1\n msg: ", "Error: input data width not evenly divisible (instance %m)");
							$finish(0);
						end
					end
					if ((M_BYTE_SIZE * M_BYTE_LANES) != M_DATA_W) begin : genblk2
						initial begin
							$display("Fatal [elaboration] /home/enio/Projects/openENOC/libs/taxi/src/axis/rtl/taxi_axis_adapter.sv:64:5 - taxi_axis_adapter.genblk2\n msg: ", "Error: output data width not evenly divisible (instance %m)");
							$finish(0);
						end
					end
					if (S_BYTE_SIZE != M_BYTE_SIZE) begin : genblk3
						initial begin
							$display("Fatal [elaboration] /home/enio/Projects/openENOC/libs/taxi/src/axis/rtl/taxi_axis_adapter.sv:67:5 - taxi_axis_adapter.genblk3\n msg: ", "Error: byte size mismatch (instance %m)");
							$finish(0);
						end
					end
					wire [S_KEEP_W - 1:0] s_axis_tkeep_int = (S_KEEP_EN ? test_openenoc_eth_adapter.uut.fifo_a2b_s_axis.tkeep : {_param_32DB7_KEEP_W {1'sb1}});
					if (M_BYTE_LANES == S_BYTE_LANES) begin : bypass
						assign test_openenoc_eth_adapter.uut.fifo_a2b_s_axis.tready = test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_pre_fifo.tready;
						assign test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_pre_fifo.tdata = test_openenoc_eth_adapter.uut.fifo_a2b_s_axis.tdata;
						assign test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_pre_fifo.tkeep = (M_KEEP_EN && S_KEEP_EN ? test_openenoc_eth_adapter.uut.fifo_a2b_s_axis.tkeep : {_param_D01DF_KEEP_W {1'sb1}});
						assign test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_pre_fifo.tstrb = (STRB_EN ? test_openenoc_eth_adapter.uut.fifo_a2b_s_axis.tstrb : test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_pre_fifo.tkeep);
						assign test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_pre_fifo.tvalid = test_openenoc_eth_adapter.uut.fifo_a2b_s_axis.tvalid;
						assign test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_pre_fifo.tlast = (LAST_EN ? test_openenoc_eth_adapter.uut.fifo_a2b_s_axis.tlast : 1'b1);
						assign test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_pre_fifo.tid = (ID_EN ? test_openenoc_eth_adapter.uut.fifo_a2b_s_axis.tid : {_param_D01DF_ID_W {1'sb0}});
						assign test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_pre_fifo.tdest = (DEST_EN ? test_openenoc_eth_adapter.uut.fifo_a2b_s_axis.tdest : {_param_D01DF_DEST_W {1'sb0}});
						assign test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_pre_fifo.tuser = (USER_EN ? test_openenoc_eth_adapter.uut.fifo_a2b_s_axis.tuser : {_param_D01DF_USER_W {1'sb0}});
					end
					else if (M_BYTE_LANES > S_BYTE_LANES) begin : upsize
						localparam SEG_COUNT = M_BYTE_LANES / S_BYTE_LANES;
						localparam SEG_DATA_W = M_DATA_W / SEG_COUNT;
						localparam SEG_KEEP_W = M_BYTE_LANES / SEG_COUNT;
						localparam CL_SEG_COUNT = $clog2(SEG_COUNT);
						reg [CL_SEG_COUNT - 1:0] seg_reg = 1'sb0;
						reg [S_DATA_W - 1:0] s_axis_tdata_reg = 1'sb0;
						reg [S_KEEP_W - 1:0] s_axis_tkeep_reg = 1'sb0;
						reg [S_KEEP_W - 1:0] s_axis_tstrb_reg = 1'sb0;
						reg s_axis_tvalid_reg = 1'b0;
						reg s_axis_tlast_reg = 1'b0;
						reg [ID_W - 1:0] s_axis_tid_reg = 1'sb0;
						reg [DEST_W - 1:0] s_axis_tdest_reg = 1'sb0;
						reg [USER_W - 1:0] s_axis_tuser_reg = 1'sb0;
						reg [M_DATA_W - 1:0] m_axis_tdata_reg = 1'sb0;
						reg [M_KEEP_W - 1:0] m_axis_tkeep_reg = 1'sb0;
						reg [M_KEEP_W - 1:0] m_axis_tstrb_reg = 1'sb0;
						reg m_axis_tvalid_reg = 1'b0;
						reg m_axis_tlast_reg = 1'b0;
						reg [ID_W - 1:0] m_axis_tid_reg = 1'sb0;
						reg [DEST_W - 1:0] m_axis_tdest_reg = 1'sb0;
						reg [USER_W - 1:0] m_axis_tuser_reg = 1'sb0;
						assign test_openenoc_eth_adapter.uut.fifo_a2b_s_axis.tready = !s_axis_tvalid_reg;
						assign test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_pre_fifo.tdata = m_axis_tdata_reg;
						assign test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_pre_fifo.tkeep = (M_KEEP_EN ? m_axis_tkeep_reg : {_param_D01DF_KEEP_W {1'sb1}});
						assign test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_pre_fifo.tstrb = (STRB_EN ? m_axis_tstrb_reg : test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_pre_fifo.tkeep);
						assign test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_pre_fifo.tvalid = m_axis_tvalid_reg;
						assign test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_pre_fifo.tlast = (LAST_EN ? m_axis_tlast_reg : 1'b1);
						assign test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_pre_fifo.tid = (ID_EN ? m_axis_tid_reg : {_param_D01DF_ID_W {1'sb0}});
						assign test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_pre_fifo.tdest = (DEST_EN ? m_axis_tdest_reg : {_param_D01DF_DEST_W {1'sb0}});
						assign test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_pre_fifo.tuser = (USER_EN ? m_axis_tuser_reg : {_param_D01DF_USER_W {1'sb0}});
						always @(posedge clk) begin
							m_axis_tvalid_reg <= m_axis_tvalid_reg && !test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_pre_fifo.tready;
							if (!m_axis_tvalid_reg || test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_pre_fifo.tready) begin
								if (seg_reg == 0) begin
									m_axis_tdata_reg[seg_reg * SEG_DATA_W+:SEG_DATA_W] <= (s_axis_tvalid_reg ? s_axis_tdata_reg : test_openenoc_eth_adapter.uut.fifo_a2b_s_axis.tdata);
									begin : sv2v_autoblock_1
										reg [M_KEEP_W - 1:0] sv2v_tmp_cast;
										sv2v_tmp_cast = (s_axis_tvalid_reg ? s_axis_tkeep_reg : s_axis_tkeep_int);
										m_axis_tkeep_reg <= sv2v_tmp_cast;
									end
									begin : sv2v_autoblock_2
										reg [M_KEEP_W - 1:0] sv2v_tmp_cast_1;
										sv2v_tmp_cast_1 = (s_axis_tvalid_reg ? s_axis_tstrb_reg : test_openenoc_eth_adapter.uut.fifo_a2b_s_axis.tstrb);
										m_axis_tstrb_reg <= sv2v_tmp_cast_1;
									end
								end
								else begin
									m_axis_tdata_reg[seg_reg * SEG_DATA_W+:SEG_DATA_W] <= test_openenoc_eth_adapter.uut.fifo_a2b_s_axis.tdata;
									m_axis_tkeep_reg[seg_reg * SEG_KEEP_W+:SEG_KEEP_W] <= s_axis_tkeep_int;
									m_axis_tstrb_reg[seg_reg * SEG_KEEP_W+:SEG_KEEP_W] <= test_openenoc_eth_adapter.uut.fifo_a2b_s_axis.tstrb;
								end
								m_axis_tlast_reg <= (s_axis_tvalid_reg ? s_axis_tlast_reg : test_openenoc_eth_adapter.uut.fifo_a2b_s_axis.tlast);
								m_axis_tid_reg <= (s_axis_tvalid_reg ? s_axis_tid_reg : test_openenoc_eth_adapter.uut.fifo_a2b_s_axis.tid);
								m_axis_tdest_reg <= (s_axis_tvalid_reg ? s_axis_tdest_reg : test_openenoc_eth_adapter.uut.fifo_a2b_s_axis.tdest);
								m_axis_tuser_reg <= (s_axis_tvalid_reg ? s_axis_tuser_reg : test_openenoc_eth_adapter.uut.fifo_a2b_s_axis.tuser);
								if (s_axis_tvalid_reg) begin
									s_axis_tvalid_reg <= 1'b0;
									begin : sv2v_autoblock_3
										reg signed [CL_SEG_COUNT - 1:0] sv2v_tmp_cast;
										sv2v_tmp_cast = SEG_COUNT - 1;
										if ((LAST_EN && s_axis_tlast_reg) || (seg_reg == sv2v_tmp_cast)) begin
											seg_reg <= 1'sb0;
											m_axis_tvalid_reg <= 1'b1;
										end
										else
											seg_reg <= seg_reg + 1;
									end
								end
								else if (test_openenoc_eth_adapter.uut.fifo_a2b_s_axis.tvalid) begin : sv2v_autoblock_4
									reg signed [CL_SEG_COUNT - 1:0] sv2v_tmp_cast;
									sv2v_tmp_cast = SEG_COUNT - 1;
									if ((LAST_EN && test_openenoc_eth_adapter.uut.fifo_a2b_s_axis.tlast) || (seg_reg == sv2v_tmp_cast)) begin
										seg_reg <= 1'sb0;
										m_axis_tvalid_reg <= 1'b1;
									end
									else
										seg_reg <= seg_reg + 1;
								end
							end
							else if (test_openenoc_eth_adapter.uut.fifo_a2b_s_axis.tvalid && test_openenoc_eth_adapter.uut.fifo_a2b_s_axis.tready) begin
								s_axis_tdata_reg <= test_openenoc_eth_adapter.uut.fifo_a2b_s_axis.tdata;
								s_axis_tkeep_reg <= s_axis_tkeep_int;
								s_axis_tstrb_reg <= test_openenoc_eth_adapter.uut.fifo_a2b_s_axis.tstrb;
								s_axis_tvalid_reg <= 1'b1;
								s_axis_tlast_reg <= test_openenoc_eth_adapter.uut.fifo_a2b_s_axis.tlast;
								s_axis_tid_reg <= test_openenoc_eth_adapter.uut.fifo_a2b_s_axis.tid;
								s_axis_tdest_reg <= test_openenoc_eth_adapter.uut.fifo_a2b_s_axis.tdest;
								s_axis_tuser_reg <= test_openenoc_eth_adapter.uut.fifo_a2b_s_axis.tuser;
							end
							if (rst) begin
								seg_reg <= 1'sb0;
								s_axis_tvalid_reg <= 1'b0;
								m_axis_tvalid_reg <= 1'b0;
							end
						end
					end
					else begin : downsize
						localparam SEG_COUNT = S_BYTE_LANES / M_BYTE_LANES;
						localparam SEG_DATA_W = S_DATA_W / SEG_COUNT;
						localparam SEG_KEEP_W = S_BYTE_LANES / SEG_COUNT;
						reg [S_DATA_W - 1:0] s_axis_tdata_reg = 1'sb0;
						reg [S_KEEP_W - 1:0] s_axis_tkeep_reg = 1'sb0;
						reg [S_KEEP_W - 1:0] s_axis_tstrb_reg = 1'sb0;
						reg s_axis_tvalid_reg = 1'b0;
						reg s_axis_tlast_reg = 1'b0;
						reg [ID_W - 1:0] s_axis_tid_reg = 1'sb0;
						reg [DEST_W - 1:0] s_axis_tdest_reg = 1'sb0;
						reg [USER_W - 1:0] s_axis_tuser_reg = 1'sb0;
						reg [M_DATA_W - 1:0] m_axis_tdata_reg = 1'sb0;
						reg [M_KEEP_W - 1:0] m_axis_tkeep_reg = 1'sb0;
						reg [M_KEEP_W - 1:0] m_axis_tstrb_reg = 1'sb0;
						reg m_axis_tvalid_reg = 1'b0;
						reg m_axis_tlast_reg = 1'b0;
						reg [ID_W - 1:0] m_axis_tid_reg = 1'sb0;
						reg [DEST_W - 1:0] m_axis_tdest_reg = 1'sb0;
						reg [USER_W - 1:0] m_axis_tuser_reg = 1'sb0;
						assign test_openenoc_eth_adapter.uut.fifo_a2b_s_axis.tready = !s_axis_tvalid_reg;
						assign test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_pre_fifo.tdata = m_axis_tdata_reg;
						assign test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_pre_fifo.tkeep = (M_KEEP_EN ? m_axis_tkeep_reg : {_param_D01DF_KEEP_W {1'sb1}});
						assign test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_pre_fifo.tstrb = (STRB_EN ? m_axis_tstrb_reg : test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_pre_fifo.tkeep);
						assign test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_pre_fifo.tvalid = m_axis_tvalid_reg;
						assign test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_pre_fifo.tlast = m_axis_tlast_reg;
						assign test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_pre_fifo.tid = (ID_EN ? m_axis_tid_reg : {_param_D01DF_ID_W {1'sb0}});
						assign test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_pre_fifo.tdest = (DEST_EN ? m_axis_tdest_reg : {_param_D01DF_DEST_W {1'sb0}});
						assign test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_pre_fifo.tuser = (USER_EN ? m_axis_tuser_reg : {_param_D01DF_USER_W {1'sb0}});
						always @(posedge clk) begin
							m_axis_tvalid_reg <= m_axis_tvalid_reg && !test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_pre_fifo.tready;
							if (!m_axis_tvalid_reg || test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_pre_fifo.tready) begin
								begin : sv2v_autoblock_5
									reg [M_DATA_W - 1:0] sv2v_tmp_cast;
									sv2v_tmp_cast = (s_axis_tvalid_reg ? s_axis_tdata_reg : test_openenoc_eth_adapter.uut.fifo_a2b_s_axis.tdata);
									m_axis_tdata_reg <= sv2v_tmp_cast;
								end
								begin : sv2v_autoblock_6
									reg [M_KEEP_W - 1:0] sv2v_tmp_cast_1;
									sv2v_tmp_cast_1 = (s_axis_tvalid_reg ? s_axis_tkeep_reg : s_axis_tkeep_int);
									m_axis_tkeep_reg <= sv2v_tmp_cast_1;
								end
								begin : sv2v_autoblock_7
									reg [M_KEEP_W - 1:0] sv2v_tmp_cast_2;
									sv2v_tmp_cast_2 = (s_axis_tvalid_reg ? s_axis_tstrb_reg : test_openenoc_eth_adapter.uut.fifo_a2b_s_axis.tstrb);
									m_axis_tstrb_reg <= sv2v_tmp_cast_2;
								end
								m_axis_tlast_reg <= 1'b0;
								m_axis_tid_reg <= (s_axis_tvalid_reg ? s_axis_tid_reg : test_openenoc_eth_adapter.uut.fifo_a2b_s_axis.tid);
								m_axis_tdest_reg <= (s_axis_tvalid_reg ? s_axis_tdest_reg : test_openenoc_eth_adapter.uut.fifo_a2b_s_axis.tdest);
								m_axis_tuser_reg <= (s_axis_tvalid_reg ? s_axis_tuser_reg : test_openenoc_eth_adapter.uut.fifo_a2b_s_axis.tuser);
								if (s_axis_tvalid_reg) begin
									s_axis_tdata_reg <= s_axis_tdata_reg >> SEG_DATA_W;
									s_axis_tkeep_reg <= s_axis_tkeep_reg >> SEG_KEEP_W;
									s_axis_tstrb_reg <= s_axis_tstrb_reg >> SEG_KEEP_W;
									m_axis_tvalid_reg <= 1'b1;
									if ((s_axis_tkeep_reg >> SEG_KEEP_W) == 0) begin
										s_axis_tvalid_reg <= 1'b0;
										m_axis_tlast_reg <= s_axis_tlast_reg;
									end
								end
								else if (test_openenoc_eth_adapter.uut.fifo_a2b_s_axis.tvalid && test_openenoc_eth_adapter.uut.fifo_a2b_s_axis.tready) begin
									s_axis_tdata_reg <= test_openenoc_eth_adapter.uut.fifo_a2b_s_axis.tdata >> SEG_DATA_W;
									s_axis_tkeep_reg <= s_axis_tkeep_int >> SEG_KEEP_W;
									s_axis_tstrb_reg <= test_openenoc_eth_adapter.uut.fifo_a2b_s_axis.tstrb >> SEG_KEEP_W;
									s_axis_tlast_reg <= test_openenoc_eth_adapter.uut.fifo_a2b_s_axis.tlast;
									s_axis_tid_reg <= test_openenoc_eth_adapter.uut.fifo_a2b_s_axis.tid;
									s_axis_tdest_reg <= test_openenoc_eth_adapter.uut.fifo_a2b_s_axis.tdest;
									s_axis_tuser_reg <= test_openenoc_eth_adapter.uut.fifo_a2b_s_axis.tuser;
									m_axis_tvalid_reg <= 1'b1;
									if (S_KEEP_EN && ((s_axis_tkeep_int >> SEG_KEEP_W) == 0)) begin
										s_axis_tvalid_reg <= 1'b0;
										m_axis_tlast_reg <= test_openenoc_eth_adapter.uut.fifo_a2b_s_axis.tlast;
									end
									else
										s_axis_tvalid_reg <= 1'b1;
								end
							end
							else if (test_openenoc_eth_adapter.uut.fifo_a2b_s_axis.tvalid && test_openenoc_eth_adapter.uut.fifo_a2b_s_axis.tready) begin
								s_axis_tdata_reg <= test_openenoc_eth_adapter.uut.fifo_a2b_s_axis.tdata;
								s_axis_tkeep_reg <= s_axis_tkeep_int;
								s_axis_tstrb_reg <= test_openenoc_eth_adapter.uut.fifo_a2b_s_axis.tstrb;
								s_axis_tvalid_reg <= 1'b1;
								s_axis_tlast_reg <= test_openenoc_eth_adapter.uut.fifo_a2b_s_axis.tlast;
								s_axis_tid_reg <= test_openenoc_eth_adapter.uut.fifo_a2b_s_axis.tid;
								s_axis_tdest_reg <= test_openenoc_eth_adapter.uut.fifo_a2b_s_axis.tdest;
								s_axis_tuser_reg <= test_openenoc_eth_adapter.uut.fifo_a2b_s_axis.tuser;
							end
							if (rst) begin
								s_axis_tvalid_reg <= 1'b0;
								m_axis_tvalid_reg <= 1'b0;
							end
						end
					end
				end
				assign pre_fifo_adapter_inst.clk = s_clk;
				assign pre_fifo_adapter_inst.rst = s_rst;
				localparam _param_23657_DEPTH = DEPTH;
				localparam _param_23657_RAM_PIPELINE = RAM_PIPELINE;
				localparam _param_23657_OUTPUT_FIFO_EN = OUTPUT_FIFO_EN;
				localparam _param_23657_FRAME_FIFO = FRAME_FIFO;
				localparam _param_23657_USER_BAD_FRAME_VALUE = USER_BAD_FRAME_VALUE;
				localparam _param_23657_USER_BAD_FRAME_MASK = USER_BAD_FRAME_MASK;
				localparam _param_23657_DROP_OVERSIZE_FRAME = DROP_OVERSIZE_FRAME;
				localparam _param_23657_DROP_BAD_FRAME = DROP_BAD_FRAME;
				localparam _param_23657_DROP_WHEN_FULL = DROP_WHEN_FULL;
				localparam _param_23657_MARK_WHEN_FULL = MARK_WHEN_FULL;
				localparam _param_23657_PAUSE_EN = PAUSE_EN;
				localparam _param_23657_FRAME_PAUSE = FRAME_PAUSE;
				if (1) begin : fifo_inst
					localparam DEPTH = _param_23657_DEPTH;
					localparam FIFO_RAMSTYLE = "auto";
					localparam RAM_PIPELINE = _param_23657_RAM_PIPELINE;
					localparam [0:0] OUTPUT_FIFO_EN = _param_23657_OUTPUT_FIFO_EN;
					localparam OUTPUT_FIFO_RAMSTYLE = "distributed";
					localparam [0:0] FRAME_FIFO = _param_23657_FRAME_FIFO;
					localparam USER_BAD_FRAME_VALUE = _param_23657_USER_BAD_FRAME_VALUE;
					localparam USER_BAD_FRAME_MASK = _param_23657_USER_BAD_FRAME_MASK;
					localparam [0:0] DROP_OVERSIZE_FRAME = _param_23657_DROP_OVERSIZE_FRAME;
					localparam [0:0] DROP_BAD_FRAME = _param_23657_DROP_BAD_FRAME;
					localparam [0:0] DROP_WHEN_FULL = _param_23657_DROP_WHEN_FULL;
					localparam [0:0] MARK_WHEN_FULL = _param_23657_MARK_WHEN_FULL;
					localparam [0:0] PAUSE_EN = _param_23657_PAUSE_EN;
					localparam [0:0] FRAME_PAUSE = _param_23657_FRAME_PAUSE;
					wire s_clk;
					wire s_rst;
					wire m_clk;
					wire m_rst;
					wire s_pause_req;
					wire s_pause_ack;
					wire m_pause_req;
					wire m_pause_ack;
					wire [$clog2(DEPTH):0] s_status_depth;
					wire [$clog2(DEPTH):0] s_status_depth_commit;
					wire s_status_overflow;
					wire s_status_bad_frame;
					wire s_status_good_frame;
					wire [$clog2(DEPTH):0] m_status_depth;
					wire [$clog2(DEPTH):0] m_status_depth_commit;
					wire m_status_overflow;
					wire m_status_bad_frame;
					wire m_status_good_frame;
					localparam DATA_W = _param_D01DF_DATA_W;
					localparam [0:0] KEEP_EN = _param_D01DF_KEEP_EN && _param_66B8B_KEEP_EN;
					localparam KEEP_W = _param_D01DF_KEEP_W;
					localparam [0:0] STRB_EN = _param_D01DF_STRB_EN && _param_66B8B_STRB_EN;
					localparam [0:0] LAST_EN = _param_D01DF_LAST_EN && _param_66B8B_LAST_EN;
					localparam [0:0] ID_EN = _param_D01DF_ID_EN && _param_66B8B_ID_EN;
					localparam ID_W = _param_D01DF_ID_W;
					localparam [0:0] DEST_EN = _param_D01DF_DEST_EN && _param_66B8B_DEST_EN;
					localparam DEST_W = _param_D01DF_DEST_W;
					localparam [0:0] USER_EN = _param_D01DF_USER_EN && _param_66B8B_USER_EN;
					localparam USER_W = _param_D01DF_USER_W;
					localparam CL_DEPTH = $clog2(DEPTH);
					localparam CL_KEEP_W = $clog2(KEEP_W);
					localparam FIFO_AW = (KEEP_EN && (KEEP_W > 1) ? $clog2(DEPTH / KEEP_W) : CL_DEPTH);
					localparam OUTPUT_FIFO_AW = (RAM_PIPELINE < 2 ? 3 : $clog2((RAM_PIPELINE * 2) + 7));
					if (FRAME_FIFO && !LAST_EN) begin : genblk1
						initial begin
							$display("Fatal [elaboration] /home/enio/Projects/openENOC/libs/taxi/src/axis/rtl/taxi_axis_async_fifo.sv:119:5 - taxi_axis_async_fifo.genblk1\n msg: ", "Error: FRAME_FIFO set requires LAST_EN set (instance %m)");
							$finish(0);
						end
					end
					if (DROP_OVERSIZE_FRAME && !FRAME_FIFO) begin : genblk2
						initial begin
							$display("Fatal [elaboration] /home/enio/Projects/openENOC/libs/taxi/src/axis/rtl/taxi_axis_async_fifo.sv:122:5 - taxi_axis_async_fifo.genblk2\n msg: ", "Error: DROP_OVERSIZE_FRAME set requires FRAME_FIFO set (instance %m)");
							$finish(0);
						end
					end
					if (DROP_BAD_FRAME && !(FRAME_FIFO && DROP_OVERSIZE_FRAME)) begin : genblk3
						initial begin
							$display("Fatal [elaboration] /home/enio/Projects/openENOC/libs/taxi/src/axis/rtl/taxi_axis_async_fifo.sv:125:5 - taxi_axis_async_fifo.genblk3\n msg: ", "Error: DROP_BAD_FRAME set requires FRAME_FIFO and DROP_OVERSIZE_FRAME set (instance %m)");
							$finish(0);
						end
					end
					if (DROP_WHEN_FULL && !(FRAME_FIFO && DROP_OVERSIZE_FRAME)) begin : genblk4
						initial begin
							$display("Fatal [elaboration] /home/enio/Projects/openENOC/libs/taxi/src/axis/rtl/taxi_axis_async_fifo.sv:128:5 - taxi_axis_async_fifo.genblk4\n msg: ", "Error: DROP_WHEN_FULL set requires FRAME_FIFO and DROP_OVERSIZE_FRAME set (instance %m)");
							$finish(0);
						end
					end
					function automatic [USER_W - 1:0] sv2v_cast_30231;
						input reg [USER_W - 1:0] inp;
						sv2v_cast_30231 = inp;
					endfunction
					if ((DROP_BAD_FRAME || MARK_WHEN_FULL) && ((sv2v_cast_30231(USER_BAD_FRAME_MASK) & {USER_W {1'b1}}) == 0)) begin : genblk5
						initial begin
							$display("Fatal [elaboration] /home/enio/Projects/openENOC/libs/taxi/src/axis/rtl/taxi_axis_async_fifo.sv:131:5 - taxi_axis_async_fifo.genblk5\n msg: ", "Error: Invalid USER_BAD_FRAME_MASK value (instance %m)");
							$finish(0);
						end
					end
					if (MARK_WHEN_FULL && FRAME_FIFO) begin : genblk6
						initial begin
							$display("Fatal [elaboration] /home/enio/Projects/openENOC/libs/taxi/src/axis/rtl/taxi_axis_async_fifo.sv:134:5 - taxi_axis_async_fifo.genblk6\n msg: ", "Error: MARK_WHEN_FULL is not compatible with FRAME_FIFO (instance %m)");
							$finish(0);
						end
					end
					if (MARK_WHEN_FULL && !LAST_EN) begin : genblk7
						initial begin
							$display("Fatal [elaboration] /home/enio/Projects/openENOC/libs/taxi/src/axis/rtl/taxi_axis_async_fifo.sv:137:5 - taxi_axis_async_fifo.genblk7\n msg: ", "Error: MARK_WHEN_FULL set requires LAST_EN set (instance %m)");
							$finish(0);
						end
					end
					if (_param_66B8B_DATA_W != DATA_W) begin : genblk8
						initial begin
							$display("Fatal [elaboration] /home/enio/Projects/openENOC/libs/taxi/src/axis/rtl/taxi_axis_async_fifo.sv:140:5 - taxi_axis_async_fifo.genblk8\n msg: ", "Error: Interface DATA_W parameter mismatch (instance %m)");
							$finish(0);
						end
					end
					if (KEEP_EN && (_param_66B8B_KEEP_W != KEEP_W)) begin : genblk9
						initial begin
							$display("Fatal [elaboration] /home/enio/Projects/openENOC/libs/taxi/src/axis/rtl/taxi_axis_async_fifo.sv:143:5 - taxi_axis_async_fifo.genblk9\n msg: ", "Error: Interface KEEP_W parameter mismatch (instance %m)");
							$finish(0);
						end
					end
					if (DROP_BAD_FRAME && !_param_D01DF_USER_EN) begin : genblk10
						initial begin
							$display("Fatal [elaboration] /home/enio/Projects/openENOC/libs/taxi/src/axis/rtl/taxi_axis_async_fifo.sv:146:5 - taxi_axis_async_fifo.genblk10\n msg: ", "Error: DROP_BAD_FRAME set requires s_axis.USER_EN (instance %m)");
							$finish(0);
						end
					end
					if (MARK_WHEN_FULL && !_param_66B8B_USER_EN) begin : genblk11
						initial begin
							$display("Fatal [elaboration] /home/enio/Projects/openENOC/libs/taxi/src/axis/rtl/taxi_axis_async_fifo.sv:149:5 - taxi_axis_async_fifo.genblk11\n msg: ", "Error: MARK_WHEN_FULL set requires m_axis.USER_EN (instance %m)");
							$finish(0);
						end
					end
					localparam KEEP_OFFSET = DATA_W;
					localparam STRB_OFFSET = KEEP_OFFSET + (KEEP_EN ? KEEP_W : 0);
					localparam LAST_OFFSET = STRB_OFFSET + (STRB_EN ? KEEP_W : 0);
					localparam ID_OFFSET = LAST_OFFSET + (LAST_EN ? 1 : 0);
					localparam DEST_OFFSET = ID_OFFSET + (ID_EN ? ID_W : 0);
					localparam USER_OFFSET = DEST_OFFSET + (DEST_EN ? DEST_W : 0);
					localparam WIDTH = USER_OFFSET + (USER_EN ? USER_W : 0);
					function [FIFO_AW:0] bin2gray;
						input [FIFO_AW:0] b;
						bin2gray = b ^ (b >> 1);
					endfunction
					function [FIFO_AW:0] gray2bin;
						input [FIFO_AW:0] g;
						integer i;
						for (i = 0; i <= FIFO_AW; i = i + 1)
							gray2bin[i] = ^(g >> i);
					endfunction
					reg [FIFO_AW:0] wr_ptr_reg = 1'sb0;
					reg [FIFO_AW:0] wr_ptr_commit_reg = 1'sb0;
					reg [FIFO_AW:0] wr_ptr_gray_reg = 1'sb0;
					reg [FIFO_AW:0] wr_ptr_sync_commit_reg = 1'sb0;
					reg [FIFO_AW:0] rd_ptr_reg = 1'sb0;
					reg [FIFO_AW:0] rd_ptr_gray_reg = 1'sb0;
					reg [FIFO_AW:0] wr_ptr_conv_reg = 1'sb0;
					reg [FIFO_AW:0] rd_ptr_conv_reg = 1'sb0;
					reg [FIFO_AW:0] wr_ptr_temp;
					reg [FIFO_AW:0] rd_ptr_temp;
					(* SHREG_EXTRACT = "NO" *) reg [FIFO_AW:0] wr_ptr_gray_sync1_reg = 1'sb0;
					(* SHREG_EXTRACT = "NO" *) reg [FIFO_AW:0] wr_ptr_gray_sync2_reg = 1'sb0;
					(* SHREG_EXTRACT = "NO" *) reg [FIFO_AW:0] wr_ptr_commit_sync_reg = 1'sb0;
					(* SHREG_EXTRACT = "NO" *) reg [FIFO_AW:0] rd_ptr_gray_sync1_reg = 1'sb0;
					(* SHREG_EXTRACT = "NO" *) reg [FIFO_AW:0] rd_ptr_gray_sync2_reg = 1'sb0;
					reg wr_ptr_update_valid_reg = 1'b0;
					reg wr_ptr_update_reg = 1'b0;
					(* SHREG_EXTRACT = "NO" *) reg wr_ptr_update_sync1_reg = 1'b0;
					(* SHREG_EXTRACT = "NO" *) reg wr_ptr_update_sync2_reg = 1'b0;
					(* SHREG_EXTRACT = "NO" *) reg wr_ptr_update_sync3_reg = 1'b0;
					(* SHREG_EXTRACT = "NO" *) reg wr_ptr_update_ack_sync1_reg = 1'b0;
					(* SHREG_EXTRACT = "NO" *) reg wr_ptr_update_ack_sync2_reg = 1'b0;
					wire s_rst_sync;
					wire m_rst_sync;
					(* ramstyle = "no_rw_check" *) reg [WIDTH - 1:0] mem [0:(2 ** FIFO_AW) - 1];
					reg mem_read_data_valid_reg = 1'b0;
					(* shreg_extract = "no" *) reg [WIDTH - 1:0] mem_rd_data_pipe_reg [RAM_PIPELINE + 0:0];
					reg [RAM_PIPELINE + 0:0] mem_rd_valid_pipe_reg = 0;
					wire full = wr_ptr_gray_reg == (rd_ptr_gray_sync2_reg ^ {2'b11, {FIFO_AW - 1 {1'b0}}});
					wire empty = (FRAME_FIFO ? rd_ptr_reg == wr_ptr_commit_sync_reg : rd_ptr_gray_reg == wr_ptr_gray_sync2_reg);
					wire full_wr = wr_ptr_reg == (wr_ptr_commit_reg ^ {1'b1, {FIFO_AW {1'b0}}});
					wire write;
					wire read;
					wire store_output;
					reg s_frame_reg = 1'b0;
					reg m_frame_reg = 1'b0;
					reg drop_frame_reg = 1'b0;
					reg mark_frame_reg = 1'b0;
					reg send_frame_reg = 1'b0;
					reg overflow_reg = 1'b0;
					reg bad_frame_reg = 1'b0;
					reg good_frame_reg = 1'b0;
					reg m_empty_pipe_reg = 1'b0;
					reg m_terminate_frame_reg = 1'b0;
					reg [FIFO_AW:0] s_depth_reg = 1'sb0;
					reg [FIFO_AW:0] s_depth_commit_reg = 1'sb0;
					reg [FIFO_AW:0] m_depth_reg = 1'sb0;
					reg [FIFO_AW:0] m_depth_commit_reg = 1'sb0;
					reg overflow_sync1_reg = 1'b0;
					reg overflow_sync2_reg = 1'b0;
					reg overflow_sync3_reg = 1'b0;
					reg overflow_sync4_reg = 1'b0;
					reg bad_frame_sync1_reg = 1'b0;
					reg bad_frame_sync2_reg = 1'b0;
					reg bad_frame_sync3_reg = 1'b0;
					reg bad_frame_sync4_reg = 1'b0;
					reg good_frame_sync1_reg = 1'b0;
					reg good_frame_sync2_reg = 1'b0;
					reg good_frame_sync3_reg = 1'b0;
					reg good_frame_sync4_reg = 1'b0;
					assign test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_pre_fifo.tready = (FRAME_FIFO ? (!full || (full_wr && DROP_OVERSIZE_FRAME)) || DROP_WHEN_FULL : !full || MARK_WHEN_FULL) && !s_rst_sync;
					wire [WIDTH - 1:0] mem_wr_data;
					assign mem_wr_data[DATA_W - 1:0] = test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_pre_fifo.tdata;
					if (KEEP_EN) begin : genblk12
						assign mem_wr_data[KEEP_OFFSET+:KEEP_W] = test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_pre_fifo.tkeep;
					end
					if (STRB_EN) begin : genblk13
						assign mem_wr_data[STRB_OFFSET+:KEEP_W] = test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_pre_fifo.tstrb;
					end
					if (LAST_EN) begin : genblk14
						assign mem_wr_data[LAST_OFFSET] = test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_pre_fifo.tlast | mark_frame_reg;
					end
					if (ID_EN) begin : genblk15
						assign mem_wr_data[ID_OFFSET+:ID_W] = test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_pre_fifo.tid;
					end
					if (DEST_EN) begin : genblk16
						assign mem_wr_data[DEST_OFFSET+:DEST_W] = test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_pre_fifo.tdest;
					end
					if (USER_EN) begin : genblk17
						function automatic [USER_W - 1:0] sv2v_cast_30231;
							input reg [USER_W - 1:0] inp;
							sv2v_cast_30231 = inp;
						endfunction
						assign mem_wr_data[USER_OFFSET+:USER_W] = (mark_frame_reg ? sv2v_cast_30231(USER_BAD_FRAME_VALUE) : test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_pre_fifo.tuser);
					end
					wire [WIDTH - 1:0] mem_rd_data = mem_rd_data_pipe_reg[RAM_PIPELINE + 0];
					wire m_axis_tready_pipe;
					wire m_axis_tvalid_pipe = mem_rd_valid_pipe_reg[RAM_PIPELINE + 0];
					wire [DATA_W - 1:0] m_axis_tdata_pipe = mem_rd_data[DATA_W - 1:0];
					wire [KEEP_W - 1:0] m_axis_tkeep_pipe;
					wire [KEEP_W - 1:0] m_axis_tstrb_pipe;
					wire m_axis_tlast_pipe;
					wire [ID_W - 1:0] m_axis_tid_pipe;
					wire [DEST_W - 1:0] m_axis_tdest_pipe;
					wire [USER_W - 1:0] m_axis_tuser_pipe;
					if (KEEP_EN) begin : genblk18
						assign m_axis_tkeep_pipe = mem_rd_data[KEEP_OFFSET+:KEEP_W];
					end
					else begin : genblk18
						assign m_axis_tkeep_pipe = 1'sb1;
					end
					if (STRB_EN) begin : genblk19
						assign m_axis_tstrb_pipe = mem_rd_data[STRB_OFFSET+:KEEP_W];
					end
					else begin : genblk19
						assign m_axis_tstrb_pipe = m_axis_tkeep_pipe;
					end
					if (LAST_EN) begin : genblk20
						assign m_axis_tlast_pipe = mem_rd_data[LAST_OFFSET] | m_terminate_frame_reg;
					end
					else begin : genblk20
						assign m_axis_tlast_pipe = 1'b1;
					end
					if (ID_EN) begin : genblk21
						assign m_axis_tid_pipe = mem_rd_data[ID_OFFSET+:ID_W];
					end
					else begin : genblk21
						assign m_axis_tid_pipe = 1'sb0;
					end
					if (DEST_EN) begin : genblk22
						assign m_axis_tdest_pipe = mem_rd_data[DEST_OFFSET+:DEST_W];
					end
					else begin : genblk22
						assign m_axis_tdest_pipe = 1'sb0;
					end
					if (USER_EN) begin : genblk23
						function automatic [USER_W - 1:0] sv2v_cast_30231;
							input reg [USER_W - 1:0] inp;
							sv2v_cast_30231 = inp;
						endfunction
						assign m_axis_tuser_pipe = (m_terminate_frame_reg ? sv2v_cast_30231(USER_BAD_FRAME_VALUE) : mem_rd_data[USER_OFFSET+:USER_W]);
					end
					else begin : genblk23
						assign m_axis_tuser_pipe = 1'sb0;
					end
					wire m_axis_tready_out;
					wire m_axis_tvalid_out;
					wire [DATA_W - 1:0] m_axis_tdata_out;
					wire [KEEP_W - 1:0] m_axis_tkeep_out;
					wire [KEEP_W - 1:0] m_axis_tstrb_out;
					wire m_axis_tlast_out;
					wire [ID_W - 1:0] m_axis_tid_out;
					wire [DEST_W - 1:0] m_axis_tdest_out;
					wire [USER_W - 1:0] m_axis_tuser_out;
					wire pipe_ready;
					function automatic [((CL_DEPTH + 0) >= 0 ? CL_DEPTH + 1 : 1 - (CL_DEPTH + 0)) - 1:0] sv2v_cast_FF327;
						input reg [((CL_DEPTH + 0) >= 0 ? CL_DEPTH + 1 : 1 - (CL_DEPTH + 0)) - 1:0] inp;
						sv2v_cast_FF327 = inp;
					endfunction
					assign s_status_depth = (KEEP_EN && (KEEP_W > 1) ? {s_depth_reg, {CL_KEEP_W {1'b0}}} : sv2v_cast_FF327(s_depth_reg));
					assign s_status_depth_commit = (KEEP_EN && (KEEP_W > 1) ? {s_depth_commit_reg, {CL_KEEP_W {1'b0}}} : sv2v_cast_FF327(s_depth_commit_reg));
					assign s_status_overflow = overflow_reg;
					assign s_status_bad_frame = bad_frame_reg;
					assign s_status_good_frame = good_frame_reg;
					assign m_status_depth = (KEEP_EN && (KEEP_W > 1) ? {m_depth_reg, {CL_KEEP_W {1'b0}}} : sv2v_cast_FF327(m_depth_reg));
					assign m_status_depth_commit = (KEEP_EN && (KEEP_W > 1) ? {m_depth_commit_reg, {CL_KEEP_W {1'b0}}} : sv2v_cast_FF327(m_depth_commit_reg));
					assign m_status_overflow = overflow_sync3_reg ^ overflow_sync4_reg;
					assign m_status_bad_frame = bad_frame_sync3_reg ^ bad_frame_sync4_reg;
					assign m_status_good_frame = good_frame_sync3_reg ^ good_frame_sync4_reg;
					taxi_sync_reset #(.N(4)) s_reset_sync_inst(
						.clk(s_clk),
						.rst(m_rst),
						.out(s_rst_sync)
					);
					taxi_sync_reset #(.N(4)) m_reset_sync_inst(
						.clk(m_clk),
						.rst(s_rst),
						.out(m_rst_sync)
					);
					always @(posedge s_clk) begin
						overflow_reg <= 1'b0;
						bad_frame_reg <= 1'b0;
						good_frame_reg <= 1'b0;
						if (FRAME_FIFO && wr_ptr_update_valid_reg) begin
							if (wr_ptr_update_reg == wr_ptr_update_ack_sync2_reg) begin
								wr_ptr_update_valid_reg <= 1'b0;
								wr_ptr_sync_commit_reg <= wr_ptr_commit_reg;
								wr_ptr_update_reg <= !wr_ptr_update_ack_sync2_reg;
							end
						end
						if ((test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_pre_fifo.tready && test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_pre_fifo.tvalid) && LAST_EN)
							s_frame_reg <= !test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_pre_fifo.tlast;
						if (s_rst_sync && LAST_EN) begin
							if (s_frame_reg && !((test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_pre_fifo.tready && test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_pre_fifo.tvalid) && test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_pre_fifo.tlast))
								drop_frame_reg <= 1'b1;
							if ((test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_pre_fifo.tready && test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_pre_fifo.tvalid) && !test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_pre_fifo.tlast)
								drop_frame_reg <= 1'b1;
						end
						if (FRAME_FIFO) begin
							if (test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_pre_fifo.tready && test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_pre_fifo.tvalid) begin
								if (((full && DROP_WHEN_FULL) || (full_wr && DROP_OVERSIZE_FRAME)) || drop_frame_reg) begin
									drop_frame_reg <= 1'b1;
									if (test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_pre_fifo.tlast) begin
										wr_ptr_temp = wr_ptr_commit_reg;
										wr_ptr_reg <= wr_ptr_temp;
										wr_ptr_gray_reg <= bin2gray(wr_ptr_temp);
										drop_frame_reg <= 1'b0;
										overflow_reg <= 1'b1;
									end
								end
								else begin
									mem[wr_ptr_reg[FIFO_AW - 1:0]] <= mem_wr_data;
									wr_ptr_temp = wr_ptr_reg + 1;
									wr_ptr_reg <= wr_ptr_temp;
									wr_ptr_gray_reg <= bin2gray(wr_ptr_temp);
									if (test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_pre_fifo.tlast || (!DROP_OVERSIZE_FRAME && (full_wr || send_frame_reg))) begin
										send_frame_reg <= !test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_pre_fifo.tlast;
										begin : sv2v_autoblock_8
											reg [USER_W - 1:0] sv2v_tmp_cast;
											reg [USER_W - 1:0] sv2v_tmp_cast_1;
											sv2v_tmp_cast = USER_BAD_FRAME_MASK;
											sv2v_tmp_cast_1 = USER_BAD_FRAME_VALUE;
											if ((test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_pre_fifo.tlast && DROP_BAD_FRAME) && ((sv2v_tmp_cast & ~(test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_pre_fifo.tuser ^ sv2v_tmp_cast_1)) != 0)) begin
												wr_ptr_temp = wr_ptr_commit_reg;
												wr_ptr_reg <= wr_ptr_temp;
												wr_ptr_gray_reg <= bin2gray(wr_ptr_temp);
												bad_frame_reg <= 1'b1;
											end
											else begin
												wr_ptr_temp = wr_ptr_reg + 1;
												wr_ptr_reg <= wr_ptr_temp;
												wr_ptr_commit_reg <= wr_ptr_temp;
												wr_ptr_gray_reg <= bin2gray(wr_ptr_temp);
												if (wr_ptr_update_reg == wr_ptr_update_ack_sync2_reg) begin
													wr_ptr_update_valid_reg <= 1'b0;
													wr_ptr_sync_commit_reg <= wr_ptr_temp;
													wr_ptr_update_reg <= !wr_ptr_update_ack_sync2_reg;
												end
												else
													wr_ptr_update_valid_reg <= 1'b1;
												good_frame_reg <= test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_pre_fifo.tlast;
											end
										end
									end
								end
							end
							else if (((test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_pre_fifo.tvalid && full_wr) && FRAME_FIFO) && !DROP_OVERSIZE_FRAME) begin
								send_frame_reg <= 1'b1;
								wr_ptr_temp = wr_ptr_reg;
								wr_ptr_reg <= wr_ptr_temp;
								wr_ptr_commit_reg <= wr_ptr_temp;
								wr_ptr_gray_reg <= bin2gray(wr_ptr_temp);
								if (wr_ptr_update_reg == wr_ptr_update_ack_sync2_reg) begin
									wr_ptr_update_valid_reg <= 1'b0;
									wr_ptr_sync_commit_reg <= wr_ptr_temp;
									wr_ptr_update_reg <= !wr_ptr_update_ack_sync2_reg;
								end
								else
									wr_ptr_update_valid_reg <= 1'b1;
							end
						end
						else if (test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_pre_fifo.tready && test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_pre_fifo.tvalid) begin
							if (drop_frame_reg && LAST_EN) begin
								if (test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_pre_fifo.tlast) begin
									if ((!full && mark_frame_reg) && MARK_WHEN_FULL) begin
										mark_frame_reg <= 1'b0;
										mem[wr_ptr_reg[FIFO_AW - 1:0]] <= mem_wr_data;
										wr_ptr_temp = wr_ptr_reg + 1;
										wr_ptr_reg <= wr_ptr_temp;
										wr_ptr_commit_reg <= wr_ptr_temp;
										wr_ptr_gray_reg <= bin2gray(wr_ptr_temp);
									end
									drop_frame_reg <= 1'b0;
									overflow_reg <= 1'b1;
								end
							end
							else if ((full || mark_frame_reg) && MARK_WHEN_FULL) begin
								drop_frame_reg <= 1'b1;
								mark_frame_reg <= mark_frame_reg || s_frame_reg;
								if (test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_pre_fifo.tlast) begin
									drop_frame_reg <= 1'b0;
									overflow_reg <= 1'b1;
								end
							end
							else begin
								mem[wr_ptr_reg[FIFO_AW - 1:0]] <= mem_wr_data;
								wr_ptr_temp = wr_ptr_reg + 1;
								wr_ptr_reg <= wr_ptr_temp;
								wr_ptr_commit_reg <= wr_ptr_temp;
								wr_ptr_gray_reg <= bin2gray(wr_ptr_temp);
							end
						end
						else if (((!full && !drop_frame_reg) && mark_frame_reg) && MARK_WHEN_FULL) begin
							mark_frame_reg <= 1'b0;
							mem[wr_ptr_reg[FIFO_AW - 1:0]] <= mem_wr_data;
							wr_ptr_temp = wr_ptr_reg + 1;
							wr_ptr_reg <= wr_ptr_temp;
							wr_ptr_commit_reg <= wr_ptr_temp;
							wr_ptr_gray_reg <= bin2gray(wr_ptr_temp);
						end
						if (s_rst_sync) begin
							wr_ptr_reg <= 1'sb0;
							wr_ptr_commit_reg <= 1'sb0;
							wr_ptr_gray_reg <= 1'sb0;
							wr_ptr_sync_commit_reg <= 1'sb0;
							wr_ptr_update_valid_reg <= 1'b0;
							wr_ptr_update_reg <= 1'b0;
						end
						if (s_rst) begin
							wr_ptr_reg <= 1'sb0;
							wr_ptr_commit_reg <= 1'sb0;
							wr_ptr_gray_reg <= 1'sb0;
							wr_ptr_sync_commit_reg <= 1'sb0;
							wr_ptr_update_valid_reg <= 1'b0;
							wr_ptr_update_reg <= 1'b0;
							s_frame_reg <= 1'b0;
							drop_frame_reg <= 1'b0;
							mark_frame_reg <= 1'b0;
							send_frame_reg <= 1'b0;
							overflow_reg <= 1'b0;
							bad_frame_reg <= 1'b0;
							good_frame_reg <= 1'b0;
						end
					end
					always @(posedge s_clk) begin
						rd_ptr_conv_reg <= gray2bin(rd_ptr_gray_sync2_reg);
						s_depth_reg <= wr_ptr_reg - rd_ptr_conv_reg;
						s_depth_commit_reg <= wr_ptr_commit_reg - rd_ptr_conv_reg;
					end
					always @(posedge s_clk) begin
						rd_ptr_gray_sync1_reg <= rd_ptr_gray_reg;
						rd_ptr_gray_sync2_reg <= rd_ptr_gray_sync1_reg;
						wr_ptr_update_ack_sync1_reg <= wr_ptr_update_sync3_reg;
						wr_ptr_update_ack_sync2_reg <= wr_ptr_update_ack_sync1_reg;
						if (s_rst) begin
							rd_ptr_gray_sync1_reg <= 1'sb0;
							rd_ptr_gray_sync2_reg <= 1'sb0;
							wr_ptr_update_ack_sync1_reg <= 1'b0;
							wr_ptr_update_ack_sync2_reg <= 1'b0;
						end
					end
					always @(posedge m_clk) begin
						wr_ptr_gray_sync1_reg <= wr_ptr_gray_reg;
						wr_ptr_gray_sync2_reg <= wr_ptr_gray_sync1_reg;
						if (FRAME_FIFO && (wr_ptr_update_sync2_reg ^ wr_ptr_update_sync3_reg))
							wr_ptr_commit_sync_reg <= wr_ptr_sync_commit_reg;
						wr_ptr_update_sync1_reg <= wr_ptr_update_reg;
						wr_ptr_update_sync2_reg <= wr_ptr_update_sync1_reg;
						wr_ptr_update_sync3_reg <= wr_ptr_update_sync2_reg;
						if (FRAME_FIFO && m_rst_sync)
							wr_ptr_gray_sync1_reg <= 1'sb0;
						if (m_rst) begin
							wr_ptr_gray_sync1_reg <= 1'sb0;
							wr_ptr_gray_sync2_reg <= 1'sb0;
							wr_ptr_commit_sync_reg <= 1'sb0;
							wr_ptr_update_sync1_reg <= 1'b0;
							wr_ptr_update_sync2_reg <= 1'b0;
							wr_ptr_update_sync3_reg <= 1'b0;
						end
					end
					always @(posedge s_clk) begin
						overflow_sync1_reg <= overflow_sync1_reg ^ overflow_reg;
						bad_frame_sync1_reg <= bad_frame_sync1_reg ^ bad_frame_reg;
						good_frame_sync1_reg <= good_frame_sync1_reg ^ good_frame_reg;
						if (s_rst) begin
							overflow_sync1_reg <= 1'b0;
							bad_frame_sync1_reg <= 1'b0;
							good_frame_sync1_reg <= 1'b0;
						end
					end
					always @(posedge m_clk) begin
						overflow_sync2_reg <= overflow_sync1_reg;
						overflow_sync3_reg <= overflow_sync2_reg;
						overflow_sync4_reg <= overflow_sync3_reg;
						bad_frame_sync2_reg <= bad_frame_sync1_reg;
						bad_frame_sync3_reg <= bad_frame_sync2_reg;
						bad_frame_sync4_reg <= bad_frame_sync3_reg;
						good_frame_sync2_reg <= good_frame_sync1_reg;
						good_frame_sync3_reg <= good_frame_sync2_reg;
						good_frame_sync4_reg <= good_frame_sync3_reg;
						if (m_rst) begin
							overflow_sync2_reg <= 1'b0;
							overflow_sync3_reg <= 1'b0;
							overflow_sync4_reg <= 1'b0;
							bad_frame_sync2_reg <= 1'b0;
							bad_frame_sync3_reg <= 1'b0;
							bad_frame_sync4_reg <= 1'b0;
							good_frame_sync2_reg <= 1'b0;
							good_frame_sync3_reg <= 1'b0;
							good_frame_sync4_reg <= 1'b0;
						end
					end
					always @(posedge m_clk) begin
						if (m_axis_tready_pipe) begin
							mem_rd_valid_pipe_reg[RAM_PIPELINE + 0] <= 1'b0;
							m_terminate_frame_reg <= 1'b0;
						end
						begin : sv2v_autoblock_9
							integer j;
							for (j = RAM_PIPELINE + 0; j > 0; j = j - 1)
								begin : sv2v_autoblock_10
									reg [((RAM_PIPELINE + 0) >= 0 ? RAM_PIPELINE + 1 : 1 - (RAM_PIPELINE + 0)) - 1:0] sv2v_tmp_cast;
									sv2v_tmp_cast = ~mem_rd_valid_pipe_reg;
									if (m_axis_tready_pipe || ((sv2v_tmp_cast >> j) != 0)) begin
										mem_rd_valid_pipe_reg[j] <= mem_rd_valid_pipe_reg[j - 1];
										mem_rd_data_pipe_reg[j] <= mem_rd_data_pipe_reg[j - 1];
										mem_rd_valid_pipe_reg[j - 1] <= 1'b0;
									end
								end
						end
						if (m_axis_tready_pipe || (&mem_rd_valid_pipe_reg == 0)) begin
							mem_rd_valid_pipe_reg[0] <= 1'b0;
							mem_rd_data_pipe_reg[0] <= mem[rd_ptr_reg[FIFO_AW - 1:0]];
							if (((!empty && !m_rst_sync) && !m_empty_pipe_reg) && pipe_ready) begin
								mem_rd_valid_pipe_reg[0] <= 1'b1;
								rd_ptr_temp = rd_ptr_reg + 1;
								rd_ptr_reg <= rd_ptr_temp;
								rd_ptr_gray_reg <= bin2gray(rd_ptr_temp);
							end
						end
						if (m_axis_tvalid_pipe && LAST_EN) begin
							if (m_axis_tlast_pipe && m_axis_tready_pipe)
								m_frame_reg <= 1'b0;
							else
								m_frame_reg <= 1'b1;
						end
						if ((m_empty_pipe_reg && (mem_rd_valid_pipe_reg == 0)) && LAST_EN) begin
							if (m_frame_reg) begin
								mem_rd_valid_pipe_reg[RAM_PIPELINE + 0] <= 1'b1;
								m_terminate_frame_reg <= 1'b1;
							end
							m_empty_pipe_reg <= 1'b0;
						end
						if (m_rst_sync && LAST_EN)
							m_empty_pipe_reg <= 1'b1;
						if (m_rst_sync) begin
							rd_ptr_reg <= 1'sb0;
							rd_ptr_gray_reg <= 1'sb0;
						end
						if (m_rst) begin
							rd_ptr_reg <= 1'sb0;
							rd_ptr_gray_reg <= 1'sb0;
							mem_rd_valid_pipe_reg <= 1'sb0;
							m_frame_reg <= 1'b0;
							m_empty_pipe_reg <= 1'b0;
							m_terminate_frame_reg <= 1'b0;
						end
					end
					always @(posedge m_clk) begin
						wr_ptr_conv_reg <= gray2bin(wr_ptr_gray_sync2_reg);
						m_depth_reg <= wr_ptr_conv_reg - rd_ptr_reg;
						m_depth_commit_reg <= (FRAME_FIFO ? wr_ptr_commit_sync_reg - rd_ptr_reg : wr_ptr_conv_reg - rd_ptr_reg);
					end
					if (!OUTPUT_FIFO_EN) begin : genblk24
						assign pipe_ready = 1'b1;
						assign m_axis_tready_pipe = m_axis_tready_out;
						assign m_axis_tvalid_out = m_axis_tvalid_pipe;
						assign m_axis_tdata_out = m_axis_tdata_pipe;
						assign m_axis_tkeep_out = m_axis_tkeep_pipe;
						assign m_axis_tstrb_out = m_axis_tstrb_pipe;
						assign m_axis_tlast_out = m_axis_tlast_pipe;
						assign m_axis_tid_out = m_axis_tid_pipe;
						assign m_axis_tdest_out = m_axis_tdest_pipe;
						assign m_axis_tuser_out = m_axis_tuser_pipe;
					end
					else begin : output_fifo
						reg [DATA_W - 1:0] m_axis_tdata_reg = 1'sb0;
						reg [KEEP_W - 1:0] m_axis_tkeep_reg = 1'sb0;
						reg [KEEP_W - 1:0] m_axis_tstrb_reg = 1'sb0;
						reg m_axis_tvalid_reg = 1'b0;
						reg m_axis_tlast_reg = 1'b0;
						reg [ID_W - 1:0] m_axis_tid_reg = 1'sb0;
						reg [DEST_W - 1:0] m_axis_tdest_reg = 1'sb0;
						reg [USER_W - 1:0] m_axis_tuser_reg = 1'sb0;
						reg [OUTPUT_FIFO_AW + 0:0] out_fifo_wr_ptr_reg = 0;
						reg [OUTPUT_FIFO_AW + 0:0] out_fifo_rd_ptr_reg = 0;
						reg out_fifo_half_full_reg = 1'b0;
						wire out_fifo_full = out_fifo_wr_ptr_reg == (out_fifo_rd_ptr_reg ^ {1'b1, {OUTPUT_FIFO_AW {1'b0}}});
						wire out_fifo_empty = out_fifo_wr_ptr_reg == out_fifo_rd_ptr_reg;
						(* ram_style = "distributed", ramstyle = "no_rw_check, mlab" *) reg [DATA_W - 1:0] out_fifo_tdata [0:(2 ** OUTPUT_FIFO_AW) - 1];
						(* ram_style = "distributed", ramstyle = "no_rw_check, mlab" *) reg [KEEP_W - 1:0] out_fifo_tkeep [0:(2 ** OUTPUT_FIFO_AW) - 1];
						(* ram_style = "distributed", ramstyle = "no_rw_check, mlab" *) reg [KEEP_W - 1:0] out_fifo_tstrb [0:(2 ** OUTPUT_FIFO_AW) - 1];
						(* ram_style = "distributed", ramstyle = "no_rw_check, mlab" *) reg out_fifo_tlast [0:(2 ** OUTPUT_FIFO_AW) - 1];
						(* ram_style = "distributed", ramstyle = "no_rw_check, mlab" *) reg [ID_W - 1:0] out_fifo_tid [0:(2 ** OUTPUT_FIFO_AW) - 1];
						(* ram_style = "distributed", ramstyle = "no_rw_check, mlab" *) reg [DEST_W - 1:0] out_fifo_tdest [0:(2 ** OUTPUT_FIFO_AW) - 1];
						(* ram_style = "distributed", ramstyle = "no_rw_check, mlab" *) reg [USER_W - 1:0] out_fifo_tuser [0:(2 ** OUTPUT_FIFO_AW) - 1];
						assign pipe_ready = !out_fifo_half_full_reg;
						assign m_axis_tready_pipe = 1'b1;
						assign m_axis_tdata_out = m_axis_tdata_reg;
						assign m_axis_tkeep_out = (KEEP_EN ? m_axis_tkeep_reg : {KEEP_W {1'sb1}});
						assign m_axis_tstrb_out = (STRB_EN ? m_axis_tkeep_reg : m_axis_tkeep_out);
						assign m_axis_tvalid_out = m_axis_tvalid_reg;
						assign m_axis_tlast_out = (LAST_EN ? m_axis_tlast_reg : 1'b1);
						assign m_axis_tid_out = (ID_EN ? m_axis_tid_reg : {ID_W {1'sb0}});
						assign m_axis_tdest_out = (DEST_EN ? m_axis_tdest_reg : {DEST_W {1'sb0}});
						assign m_axis_tuser_out = (USER_EN ? m_axis_tuser_reg : {USER_W {1'sb0}});
						always @(posedge m_clk) begin
							m_axis_tvalid_reg <= m_axis_tvalid_reg && !m_axis_tready_out;
							out_fifo_half_full_reg <= $unsigned(out_fifo_wr_ptr_reg - out_fifo_rd_ptr_reg) >= (2 ** (OUTPUT_FIFO_AW - 1));
							if (!out_fifo_full && m_axis_tvalid_pipe) begin
								out_fifo_tdata[out_fifo_wr_ptr_reg[OUTPUT_FIFO_AW - 1:0]] <= m_axis_tdata_pipe;
								out_fifo_tkeep[out_fifo_wr_ptr_reg[OUTPUT_FIFO_AW - 1:0]] <= m_axis_tkeep_pipe;
								out_fifo_tstrb[out_fifo_wr_ptr_reg[OUTPUT_FIFO_AW - 1:0]] <= m_axis_tstrb_pipe;
								out_fifo_tlast[out_fifo_wr_ptr_reg[OUTPUT_FIFO_AW - 1:0]] <= m_axis_tlast_pipe;
								out_fifo_tid[out_fifo_wr_ptr_reg[OUTPUT_FIFO_AW - 1:0]] <= m_axis_tid_pipe;
								out_fifo_tdest[out_fifo_wr_ptr_reg[OUTPUT_FIFO_AW - 1:0]] <= m_axis_tdest_pipe;
								out_fifo_tuser[out_fifo_wr_ptr_reg[OUTPUT_FIFO_AW - 1:0]] <= m_axis_tuser_pipe;
								out_fifo_wr_ptr_reg <= out_fifo_wr_ptr_reg + 1;
							end
							if (!out_fifo_empty && (!m_axis_tvalid_reg || m_axis_tready_out)) begin
								m_axis_tdata_reg <= out_fifo_tdata[out_fifo_rd_ptr_reg[OUTPUT_FIFO_AW - 1:0]];
								m_axis_tkeep_reg <= out_fifo_tkeep[out_fifo_rd_ptr_reg[OUTPUT_FIFO_AW - 1:0]];
								m_axis_tstrb_reg <= out_fifo_tstrb[out_fifo_rd_ptr_reg[OUTPUT_FIFO_AW - 1:0]];
								m_axis_tvalid_reg <= 1'b1;
								m_axis_tlast_reg <= out_fifo_tlast[out_fifo_rd_ptr_reg[OUTPUT_FIFO_AW - 1:0]];
								m_axis_tid_reg <= out_fifo_tid[out_fifo_rd_ptr_reg[OUTPUT_FIFO_AW - 1:0]];
								m_axis_tdest_reg <= out_fifo_tdest[out_fifo_rd_ptr_reg[OUTPUT_FIFO_AW - 1:0]];
								m_axis_tuser_reg <= out_fifo_tuser[out_fifo_rd_ptr_reg[OUTPUT_FIFO_AW - 1:0]];
								out_fifo_rd_ptr_reg <= out_fifo_rd_ptr_reg + 1;
							end
							if (m_rst) begin
								out_fifo_wr_ptr_reg <= 0;
								out_fifo_rd_ptr_reg <= 0;
								m_axis_tvalid_reg <= 1'b0;
							end
						end
					end
					if (PAUSE_EN) begin : pause
						reg pause_reg = 1'b0;
						reg pause_frame_reg = 1'b0;
						wire s_pause_req_sync;
						taxi_sync_signal #(
							.WIDTH(1),
							.N(2)
						) pause_req_sync_inst(
							.clk(m_clk),
							.in(s_pause_req),
							.out(s_pause_req_sync)
						);
						taxi_sync_signal #(
							.WIDTH(1),
							.N(2)
						) pause_ack_sync_inst(
							.clk(s_clk),
							.in(pause_reg),
							.out(s_pause_ack)
						);
						assign m_axis_tready_out = test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tready && !pause_reg;
						assign test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tvalid = m_axis_tvalid_out && !pause_reg;
						assign test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tdata = m_axis_tdata_out;
						assign test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tkeep = m_axis_tkeep_out;
						assign test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tstrb = m_axis_tstrb_out;
						assign test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tlast = m_axis_tlast_out;
						assign test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tid = m_axis_tid_out;
						assign test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tdest = m_axis_tdest_out;
						assign test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tuser = m_axis_tuser_out;
						assign m_pause_ack = pause_reg;
						always @(posedge m_clk) begin
							if (FRAME_PAUSE) begin
								if (pause_reg)
									pause_reg <= m_pause_req || s_pause_req_sync;
								else if (m_axis_tvalid_out) begin
									pause_frame_reg <= 1'b1;
									if (test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tready && test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tlast) begin
										pause_frame_reg <= 1'b0;
										pause_reg <= m_pause_req || s_pause_req_sync;
									end
								end
								else if (!pause_frame_reg)
									pause_reg <= m_pause_req || s_pause_req_sync;
							end
							else
								pause_reg <= m_pause_req || s_pause_req_sync;
							if (m_rst) begin
								pause_frame_reg <= 1'b0;
								pause_reg <= 1'b0;
							end
						end
					end
					else begin : genblk25
						assign m_axis_tready_out = test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tready;
						assign test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tvalid = m_axis_tvalid_out;
						assign test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tdata = m_axis_tdata_out;
						assign test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tkeep = m_axis_tkeep_out;
						assign test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tstrb = m_axis_tstrb_out;
						assign test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tlast = m_axis_tlast_out;
						assign test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tid = m_axis_tid_out;
						assign test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tdest = m_axis_tdest_out;
						assign test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tuser = m_axis_tuser_out;
						assign s_pause_ack = 1'b0;
						assign m_pause_ack = 1'b0;
					end
				end
				assign fifo_inst.s_clk = s_clk;
				assign fifo_inst.s_rst = s_rst;
				assign fifo_inst.m_clk = m_clk;
				assign fifo_inst.m_rst = m_rst;
				assign fifo_inst.s_pause_req = s_pause_req;
				assign s_pause_ack = fifo_inst.s_pause_ack;
				assign fifo_inst.m_pause_req = m_pause_req;
				assign m_pause_ack = fifo_inst.m_pause_ack;
				assign s_status_depth = fifo_inst.s_status_depth;
				assign s_status_depth_commit = fifo_inst.s_status_depth_commit;
				assign s_status_overflow = fifo_inst.s_status_overflow;
				assign s_status_bad_frame = fifo_inst.s_status_bad_frame;
				assign s_status_good_frame = fifo_inst.s_status_good_frame;
				assign m_status_depth = fifo_inst.m_status_depth;
				assign m_status_depth_commit = fifo_inst.m_status_depth_commit;
				assign m_status_overflow = fifo_inst.m_status_overflow;
				assign m_status_bad_frame = fifo_inst.m_status_bad_frame;
				assign m_status_good_frame = fifo_inst.m_status_good_frame;
				if (1) begin : post_fifo_adapter_inst
					wire clk;
					wire rst;
					localparam S_DATA_W = _param_66B8B_DATA_W;
					localparam [0:0] S_KEEP_EN = _param_66B8B_KEEP_EN;
					localparam S_KEEP_W = _param_66B8B_KEEP_W;
					localparam [0:0] STRB_EN = _param_66B8B_STRB_EN && _param_368DC_STRB_EN;
					localparam [0:0] LAST_EN = _param_66B8B_LAST_EN;
					localparam [0:0] ID_EN = _param_66B8B_ID_EN && _param_368DC_ID_EN;
					localparam ID_W = _param_66B8B_ID_W;
					localparam [0:0] DEST_EN = _param_66B8B_DEST_EN && _param_368DC_DEST_EN;
					localparam DEST_W = _param_66B8B_DEST_W;
					localparam [0:0] USER_EN = _param_66B8B_USER_EN && _param_368DC_USER_EN;
					localparam USER_W = _param_66B8B_USER_W;
					localparam M_DATA_W = _param_368DC_DATA_W;
					localparam [0:0] M_KEEP_EN = _param_368DC_KEEP_EN;
					localparam M_KEEP_W = _param_368DC_KEEP_W;
					localparam S_BYTE_LANES = (S_KEEP_EN ? S_KEEP_W : 1);
					localparam M_BYTE_LANES = (M_KEEP_EN ? M_KEEP_W : 1);
					localparam S_BYTE_SIZE = S_DATA_W / S_BYTE_LANES;
					localparam M_BYTE_SIZE = M_DATA_W / M_BYTE_LANES;
					if ((S_BYTE_SIZE * S_BYTE_LANES) != S_DATA_W) begin : genblk1
						initial begin
							$display("Fatal [elaboration] /home/enio/Projects/openENOC/libs/taxi/src/axis/rtl/taxi_axis_adapter.sv:61:5 - taxi_axis_adapter.genblk1\n msg: ", "Error: input data width not evenly divisible (instance %m)");
							$finish(0);
						end
					end
					if ((M_BYTE_SIZE * M_BYTE_LANES) != M_DATA_W) begin : genblk2
						initial begin
							$display("Fatal [elaboration] /home/enio/Projects/openENOC/libs/taxi/src/axis/rtl/taxi_axis_adapter.sv:64:5 - taxi_axis_adapter.genblk2\n msg: ", "Error: output data width not evenly divisible (instance %m)");
							$finish(0);
						end
					end
					if (S_BYTE_SIZE != M_BYTE_SIZE) begin : genblk3
						initial begin
							$display("Fatal [elaboration] /home/enio/Projects/openENOC/libs/taxi/src/axis/rtl/taxi_axis_adapter.sv:67:5 - taxi_axis_adapter.genblk3\n msg: ", "Error: byte size mismatch (instance %m)");
							$finish(0);
						end
					end
					wire [S_KEEP_W - 1:0] s_axis_tkeep_int = (S_KEEP_EN ? test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tkeep : {_param_66B8B_KEEP_W {1'sb1}});
					if (M_BYTE_LANES == S_BYTE_LANES) begin : bypass
						assign test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tready = test_openenoc_eth_adapter.uut.fifo_a2b_m_axis.tready;
						assign test_openenoc_eth_adapter.uut.fifo_a2b_m_axis.tdata = test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tdata;
						assign test_openenoc_eth_adapter.uut.fifo_a2b_m_axis.tkeep = (M_KEEP_EN && S_KEEP_EN ? test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tkeep : {_param_368DC_KEEP_W {1'sb1}});
						assign test_openenoc_eth_adapter.uut.fifo_a2b_m_axis.tstrb = (STRB_EN ? test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tstrb : test_openenoc_eth_adapter.uut.fifo_a2b_m_axis.tkeep);
						assign test_openenoc_eth_adapter.uut.fifo_a2b_m_axis.tvalid = test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tvalid;
						assign test_openenoc_eth_adapter.uut.fifo_a2b_m_axis.tlast = (LAST_EN ? test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tlast : 1'b1);
						assign test_openenoc_eth_adapter.uut.fifo_a2b_m_axis.tid = (ID_EN ? test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tid : {_param_368DC_ID_W {1'sb0}});
						assign test_openenoc_eth_adapter.uut.fifo_a2b_m_axis.tdest = (DEST_EN ? test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tdest : {_param_368DC_DEST_W {1'sb0}});
						assign test_openenoc_eth_adapter.uut.fifo_a2b_m_axis.tuser = (USER_EN ? test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tuser : {_param_368DC_USER_W {1'sb0}});
					end
					else if (M_BYTE_LANES > S_BYTE_LANES) begin : upsize
						localparam SEG_COUNT = M_BYTE_LANES / S_BYTE_LANES;
						localparam SEG_DATA_W = M_DATA_W / SEG_COUNT;
						localparam SEG_KEEP_W = M_BYTE_LANES / SEG_COUNT;
						localparam CL_SEG_COUNT = $clog2(SEG_COUNT);
						reg [CL_SEG_COUNT - 1:0] seg_reg = 1'sb0;
						reg [S_DATA_W - 1:0] s_axis_tdata_reg = 1'sb0;
						reg [S_KEEP_W - 1:0] s_axis_tkeep_reg = 1'sb0;
						reg [S_KEEP_W - 1:0] s_axis_tstrb_reg = 1'sb0;
						reg s_axis_tvalid_reg = 1'b0;
						reg s_axis_tlast_reg = 1'b0;
						reg [ID_W - 1:0] s_axis_tid_reg = 1'sb0;
						reg [DEST_W - 1:0] s_axis_tdest_reg = 1'sb0;
						reg [USER_W - 1:0] s_axis_tuser_reg = 1'sb0;
						reg [M_DATA_W - 1:0] m_axis_tdata_reg = 1'sb0;
						reg [M_KEEP_W - 1:0] m_axis_tkeep_reg = 1'sb0;
						reg [M_KEEP_W - 1:0] m_axis_tstrb_reg = 1'sb0;
						reg m_axis_tvalid_reg = 1'b0;
						reg m_axis_tlast_reg = 1'b0;
						reg [ID_W - 1:0] m_axis_tid_reg = 1'sb0;
						reg [DEST_W - 1:0] m_axis_tdest_reg = 1'sb0;
						reg [USER_W - 1:0] m_axis_tuser_reg = 1'sb0;
						assign test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tready = !s_axis_tvalid_reg;
						assign test_openenoc_eth_adapter.uut.fifo_a2b_m_axis.tdata = m_axis_tdata_reg;
						assign test_openenoc_eth_adapter.uut.fifo_a2b_m_axis.tkeep = (M_KEEP_EN ? m_axis_tkeep_reg : {_param_368DC_KEEP_W {1'sb1}});
						assign test_openenoc_eth_adapter.uut.fifo_a2b_m_axis.tstrb = (STRB_EN ? m_axis_tstrb_reg : test_openenoc_eth_adapter.uut.fifo_a2b_m_axis.tkeep);
						assign test_openenoc_eth_adapter.uut.fifo_a2b_m_axis.tvalid = m_axis_tvalid_reg;
						assign test_openenoc_eth_adapter.uut.fifo_a2b_m_axis.tlast = (LAST_EN ? m_axis_tlast_reg : 1'b1);
						assign test_openenoc_eth_adapter.uut.fifo_a2b_m_axis.tid = (ID_EN ? m_axis_tid_reg : {_param_368DC_ID_W {1'sb0}});
						assign test_openenoc_eth_adapter.uut.fifo_a2b_m_axis.tdest = (DEST_EN ? m_axis_tdest_reg : {_param_368DC_DEST_W {1'sb0}});
						assign test_openenoc_eth_adapter.uut.fifo_a2b_m_axis.tuser = (USER_EN ? m_axis_tuser_reg : {_param_368DC_USER_W {1'sb0}});
						always @(posedge clk) begin
							m_axis_tvalid_reg <= m_axis_tvalid_reg && !test_openenoc_eth_adapter.uut.fifo_a2b_m_axis.tready;
							if (!m_axis_tvalid_reg || test_openenoc_eth_adapter.uut.fifo_a2b_m_axis.tready) begin
								if (seg_reg == 0) begin
									m_axis_tdata_reg[seg_reg * SEG_DATA_W+:SEG_DATA_W] <= (s_axis_tvalid_reg ? s_axis_tdata_reg : test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tdata);
									begin : sv2v_autoblock_11
										reg [M_KEEP_W - 1:0] sv2v_tmp_cast;
										sv2v_tmp_cast = (s_axis_tvalid_reg ? s_axis_tkeep_reg : s_axis_tkeep_int);
										m_axis_tkeep_reg <= sv2v_tmp_cast;
									end
									begin : sv2v_autoblock_12
										reg [M_KEEP_W - 1:0] sv2v_tmp_cast_1;
										sv2v_tmp_cast_1 = (s_axis_tvalid_reg ? s_axis_tstrb_reg : test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tstrb);
										m_axis_tstrb_reg <= sv2v_tmp_cast_1;
									end
								end
								else begin
									m_axis_tdata_reg[seg_reg * SEG_DATA_W+:SEG_DATA_W] <= test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tdata;
									m_axis_tkeep_reg[seg_reg * SEG_KEEP_W+:SEG_KEEP_W] <= s_axis_tkeep_int;
									m_axis_tstrb_reg[seg_reg * SEG_KEEP_W+:SEG_KEEP_W] <= test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tstrb;
								end
								m_axis_tlast_reg <= (s_axis_tvalid_reg ? s_axis_tlast_reg : test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tlast);
								m_axis_tid_reg <= (s_axis_tvalid_reg ? s_axis_tid_reg : test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tid);
								m_axis_tdest_reg <= (s_axis_tvalid_reg ? s_axis_tdest_reg : test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tdest);
								m_axis_tuser_reg <= (s_axis_tvalid_reg ? s_axis_tuser_reg : test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tuser);
								if (s_axis_tvalid_reg) begin
									s_axis_tvalid_reg <= 1'b0;
									begin : sv2v_autoblock_13
										reg signed [CL_SEG_COUNT - 1:0] sv2v_tmp_cast;
										sv2v_tmp_cast = SEG_COUNT - 1;
										if ((LAST_EN && s_axis_tlast_reg) || (seg_reg == sv2v_tmp_cast)) begin
											seg_reg <= 1'sb0;
											m_axis_tvalid_reg <= 1'b1;
										end
										else
											seg_reg <= seg_reg + 1;
									end
								end
								else if (test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tvalid) begin : sv2v_autoblock_14
									reg signed [CL_SEG_COUNT - 1:0] sv2v_tmp_cast;
									sv2v_tmp_cast = SEG_COUNT - 1;
									if ((LAST_EN && test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tlast) || (seg_reg == sv2v_tmp_cast)) begin
										seg_reg <= 1'sb0;
										m_axis_tvalid_reg <= 1'b1;
									end
									else
										seg_reg <= seg_reg + 1;
								end
							end
							else if (test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tvalid && test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tready) begin
								s_axis_tdata_reg <= test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tdata;
								s_axis_tkeep_reg <= s_axis_tkeep_int;
								s_axis_tstrb_reg <= test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tstrb;
								s_axis_tvalid_reg <= 1'b1;
								s_axis_tlast_reg <= test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tlast;
								s_axis_tid_reg <= test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tid;
								s_axis_tdest_reg <= test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tdest;
								s_axis_tuser_reg <= test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tuser;
							end
							if (rst) begin
								seg_reg <= 1'sb0;
								s_axis_tvalid_reg <= 1'b0;
								m_axis_tvalid_reg <= 1'b0;
							end
						end
					end
					else begin : downsize
						localparam SEG_COUNT = S_BYTE_LANES / M_BYTE_LANES;
						localparam SEG_DATA_W = S_DATA_W / SEG_COUNT;
						localparam SEG_KEEP_W = S_BYTE_LANES / SEG_COUNT;
						reg [S_DATA_W - 1:0] s_axis_tdata_reg = 1'sb0;
						reg [S_KEEP_W - 1:0] s_axis_tkeep_reg = 1'sb0;
						reg [S_KEEP_W - 1:0] s_axis_tstrb_reg = 1'sb0;
						reg s_axis_tvalid_reg = 1'b0;
						reg s_axis_tlast_reg = 1'b0;
						reg [ID_W - 1:0] s_axis_tid_reg = 1'sb0;
						reg [DEST_W - 1:0] s_axis_tdest_reg = 1'sb0;
						reg [USER_W - 1:0] s_axis_tuser_reg = 1'sb0;
						reg [M_DATA_W - 1:0] m_axis_tdata_reg = 1'sb0;
						reg [M_KEEP_W - 1:0] m_axis_tkeep_reg = 1'sb0;
						reg [M_KEEP_W - 1:0] m_axis_tstrb_reg = 1'sb0;
						reg m_axis_tvalid_reg = 1'b0;
						reg m_axis_tlast_reg = 1'b0;
						reg [ID_W - 1:0] m_axis_tid_reg = 1'sb0;
						reg [DEST_W - 1:0] m_axis_tdest_reg = 1'sb0;
						reg [USER_W - 1:0] m_axis_tuser_reg = 1'sb0;
						assign test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tready = !s_axis_tvalid_reg;
						assign test_openenoc_eth_adapter.uut.fifo_a2b_m_axis.tdata = m_axis_tdata_reg;
						assign test_openenoc_eth_adapter.uut.fifo_a2b_m_axis.tkeep = (M_KEEP_EN ? m_axis_tkeep_reg : {_param_368DC_KEEP_W {1'sb1}});
						assign test_openenoc_eth_adapter.uut.fifo_a2b_m_axis.tstrb = (STRB_EN ? m_axis_tstrb_reg : test_openenoc_eth_adapter.uut.fifo_a2b_m_axis.tkeep);
						assign test_openenoc_eth_adapter.uut.fifo_a2b_m_axis.tvalid = m_axis_tvalid_reg;
						assign test_openenoc_eth_adapter.uut.fifo_a2b_m_axis.tlast = m_axis_tlast_reg;
						assign test_openenoc_eth_adapter.uut.fifo_a2b_m_axis.tid = (ID_EN ? m_axis_tid_reg : {_param_368DC_ID_W {1'sb0}});
						assign test_openenoc_eth_adapter.uut.fifo_a2b_m_axis.tdest = (DEST_EN ? m_axis_tdest_reg : {_param_368DC_DEST_W {1'sb0}});
						assign test_openenoc_eth_adapter.uut.fifo_a2b_m_axis.tuser = (USER_EN ? m_axis_tuser_reg : {_param_368DC_USER_W {1'sb0}});
						always @(posedge clk) begin
							m_axis_tvalid_reg <= m_axis_tvalid_reg && !test_openenoc_eth_adapter.uut.fifo_a2b_m_axis.tready;
							if (!m_axis_tvalid_reg || test_openenoc_eth_adapter.uut.fifo_a2b_m_axis.tready) begin
								begin : sv2v_autoblock_15
									reg [M_DATA_W - 1:0] sv2v_tmp_cast;
									sv2v_tmp_cast = (s_axis_tvalid_reg ? s_axis_tdata_reg : test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tdata);
									m_axis_tdata_reg <= sv2v_tmp_cast;
								end
								begin : sv2v_autoblock_16
									reg [M_KEEP_W - 1:0] sv2v_tmp_cast_1;
									sv2v_tmp_cast_1 = (s_axis_tvalid_reg ? s_axis_tkeep_reg : s_axis_tkeep_int);
									m_axis_tkeep_reg <= sv2v_tmp_cast_1;
								end
								begin : sv2v_autoblock_17
									reg [M_KEEP_W - 1:0] sv2v_tmp_cast_2;
									sv2v_tmp_cast_2 = (s_axis_tvalid_reg ? s_axis_tstrb_reg : test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tstrb);
									m_axis_tstrb_reg <= sv2v_tmp_cast_2;
								end
								m_axis_tlast_reg <= 1'b0;
								m_axis_tid_reg <= (s_axis_tvalid_reg ? s_axis_tid_reg : test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tid);
								m_axis_tdest_reg <= (s_axis_tvalid_reg ? s_axis_tdest_reg : test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tdest);
								m_axis_tuser_reg <= (s_axis_tvalid_reg ? s_axis_tuser_reg : test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tuser);
								if (s_axis_tvalid_reg) begin
									s_axis_tdata_reg <= s_axis_tdata_reg >> SEG_DATA_W;
									s_axis_tkeep_reg <= s_axis_tkeep_reg >> SEG_KEEP_W;
									s_axis_tstrb_reg <= s_axis_tstrb_reg >> SEG_KEEP_W;
									m_axis_tvalid_reg <= 1'b1;
									if ((s_axis_tkeep_reg >> SEG_KEEP_W) == 0) begin
										s_axis_tvalid_reg <= 1'b0;
										m_axis_tlast_reg <= s_axis_tlast_reg;
									end
								end
								else if (test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tvalid && test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tready) begin
									s_axis_tdata_reg <= test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tdata >> SEG_DATA_W;
									s_axis_tkeep_reg <= s_axis_tkeep_int >> SEG_KEEP_W;
									s_axis_tstrb_reg <= test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tstrb >> SEG_KEEP_W;
									s_axis_tlast_reg <= test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tlast;
									s_axis_tid_reg <= test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tid;
									s_axis_tdest_reg <= test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tdest;
									s_axis_tuser_reg <= test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tuser;
									m_axis_tvalid_reg <= 1'b1;
									if (S_KEEP_EN && ((s_axis_tkeep_int >> SEG_KEEP_W) == 0)) begin
										s_axis_tvalid_reg <= 1'b0;
										m_axis_tlast_reg <= test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tlast;
									end
									else
										s_axis_tvalid_reg <= 1'b1;
								end
							end
							else if (test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tvalid && test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tready) begin
								s_axis_tdata_reg <= test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tdata;
								s_axis_tkeep_reg <= s_axis_tkeep_int;
								s_axis_tstrb_reg <= test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tstrb;
								s_axis_tvalid_reg <= 1'b1;
								s_axis_tlast_reg <= test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tlast;
								s_axis_tid_reg <= test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tid;
								s_axis_tdest_reg <= test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tdest;
								s_axis_tuser_reg <= test_openenoc_eth_adapter.uut.fifo_a2b_inst.axis_post_fifo.tuser;
							end
							if (rst) begin
								s_axis_tvalid_reg <= 1'b0;
								m_axis_tvalid_reg <= 1'b0;
							end
						end
					end
				end
				assign post_fifo_adapter_inst.clk = m_clk;
				assign post_fifo_adapter_inst.rst = m_rst;
			end
			assign fifo_a2b_inst.s_clk = test_openenoc_eth_adapter.eth_a.clk;
			assign fifo_a2b_inst.s_rst = test_openenoc_eth_adapter.eth_a.rst;
			assign fifo_a2b_inst.m_clk = test_openenoc_eth_adapter.eth_b.clk;
			assign fifo_a2b_inst.m_rst = test_openenoc_eth_adapter.eth_b.rst;
			assign fifo_a2b_inst.s_pause_req = 1'b0;
			assign fifo_a2b_inst.m_pause_req = 1'b0;
			localparam _param_F2F03_DEPTH = DEPTH;
			localparam _param_F2F03_RAM_PIPELINE = RAM_PIPELINE;
			localparam _param_F2F03_OUTPUT_FIFO_EN = OUTPUT_FIFO_EN;
			localparam _param_F2F03_FRAME_FIFO = FRAME_FIFO;
			localparam _param_F2F03_USER_BAD_FRAME_VALUE = USER_BAD_FRAME_VALUE;
			localparam _param_F2F03_USER_BAD_FRAME_MASK = USER_BAD_FRAME_MASK;
			localparam _param_F2F03_DROP_OVERSIZE_FRAME = DROP_OVERSIZE_FRAME;
			localparam _param_F2F03_DROP_BAD_FRAME = DROP_BAD_FRAME;
			localparam _param_F2F03_DROP_WHEN_FULL = DROP_WHEN_FULL;
			localparam _param_F2F03_MARK_WHEN_FULL = MARK_WHEN_FULL;
			localparam _param_F2F03_PAUSE_EN = 1'b0;
			localparam _param_F2F03_FRAME_PAUSE = FRAME_PAUSE;
			if (1) begin : fifo_b2a_inst
				localparam DEPTH = _param_F2F03_DEPTH;
				localparam RAM_PIPELINE = _param_F2F03_RAM_PIPELINE;
				localparam [0:0] OUTPUT_FIFO_EN = _param_F2F03_OUTPUT_FIFO_EN;
				localparam [0:0] FRAME_FIFO = _param_F2F03_FRAME_FIFO;
				localparam USER_BAD_FRAME_VALUE = _param_F2F03_USER_BAD_FRAME_VALUE;
				localparam USER_BAD_FRAME_MASK = _param_F2F03_USER_BAD_FRAME_MASK;
				localparam [0:0] DROP_OVERSIZE_FRAME = _param_F2F03_DROP_OVERSIZE_FRAME;
				localparam [0:0] DROP_BAD_FRAME = _param_F2F03_DROP_BAD_FRAME;
				localparam [0:0] DROP_WHEN_FULL = _param_F2F03_DROP_WHEN_FULL;
				localparam [0:0] MARK_WHEN_FULL = _param_F2F03_MARK_WHEN_FULL;
				localparam [0:0] PAUSE_EN = _param_F2F03_PAUSE_EN;
				localparam [0:0] FRAME_PAUSE = _param_F2F03_FRAME_PAUSE;
				wire s_clk;
				wire s_rst;
				wire m_clk;
				wire m_rst;
				wire s_pause_req;
				wire s_pause_ack;
				wire m_pause_req;
				wire m_pause_ack;
				wire [$clog2(DEPTH):0] s_status_depth;
				wire [$clog2(DEPTH):0] s_status_depth_commit;
				wire s_status_overflow;
				wire s_status_bad_frame;
				wire s_status_good_frame;
				wire [$clog2(DEPTH):0] m_status_depth;
				wire [$clog2(DEPTH):0] m_status_depth_commit;
				wire m_status_overflow;
				wire m_status_bad_frame;
				wire m_status_good_frame;
				localparam S_DATA_W = _param_2EBF5_DATA_W;
				localparam [0:0] S_KEEP_EN = _param_2EBF5_KEEP_EN;
				localparam S_KEEP_W = _param_2EBF5_KEEP_W;
				localparam [0:0] S_STRB_EN = _param_2EBF5_STRB_EN;
				localparam M_DATA_W = _param_330AD_DATA_W;
				localparam [0:0] M_KEEP_EN = _param_330AD_KEEP_EN;
				localparam M_KEEP_W = _param_330AD_KEEP_W;
				localparam [0:0] M_STRB_EN = _param_330AD_STRB_EN;
				localparam S_BYTE_LANES = (S_KEEP_EN ? S_KEEP_W : 1);
				localparam M_BYTE_LANES = (M_KEEP_EN ? M_KEEP_W : 1);
				localparam S_BYTE_SIZE = S_DATA_W / S_BYTE_LANES;
				localparam M_BYTE_SIZE = M_DATA_W / M_BYTE_LANES;
				localparam EXPAND_BUS = M_BYTE_LANES > S_BYTE_LANES;
				localparam DATA_W = (EXPAND_BUS ? M_DATA_W : S_DATA_W);
				localparam KEEP_W = (EXPAND_BUS ? M_BYTE_LANES : S_BYTE_LANES);
				localparam KEEP_EN = (EXPAND_BUS ? M_KEEP_EN : S_KEEP_EN);
				localparam STRB_EN = M_STRB_EN && S_STRB_EN;
				if ((S_BYTE_SIZE * S_BYTE_LANES) != S_DATA_W) begin : genblk1
					initial begin
						$display("Fatal [elaboration] /home/enio/Projects/openENOC/libs/taxi/src/axis/rtl/taxi_axis_async_fifo_adapter.sv:122:5 - taxi_axis_async_fifo_adapter.genblk1\n msg: ", "Error: input data width not evenly divisible (instance %m)");
						$finish(0);
					end
				end
				if ((M_BYTE_SIZE * M_BYTE_LANES) != M_DATA_W) begin : genblk2
					initial begin
						$display("Fatal [elaboration] /home/enio/Projects/openENOC/libs/taxi/src/axis/rtl/taxi_axis_async_fifo_adapter.sv:125:5 - taxi_axis_async_fifo_adapter.genblk2\n msg: ", "Error: output data width not evenly divisible (instance %m)");
						$finish(0);
					end
				end
				if (S_BYTE_SIZE != M_BYTE_SIZE) begin : genblk3
					initial begin
						$display("Fatal [elaboration] /home/enio/Projects/openENOC/libs/taxi/src/axis/rtl/taxi_axis_async_fifo_adapter.sv:128:5 - taxi_axis_async_fifo_adapter.genblk3\n msg: ", "Error: byte size mismatch (instance %m)");
						$finish(0);
					end
				end
				localparam _param_A20E1_DATA_W = DATA_W;
				localparam _param_A20E1_KEEP_EN = KEEP_EN;
				localparam _param_A20E1_KEEP_W = KEEP_W;
				localparam _param_A20E1_STRB_EN = _param_2EBF5_STRB_EN;
				localparam _param_A20E1_LAST_EN = _param_2EBF5_LAST_EN;
				localparam _param_A20E1_ID_EN = _param_2EBF5_ID_EN;
				localparam _param_A20E1_ID_W = _param_2EBF5_ID_W;
				localparam _param_A20E1_DEST_EN = _param_2EBF5_DEST_EN;
				localparam _param_A20E1_DEST_W = _param_2EBF5_DEST_W;
				localparam _param_A20E1_USER_EN = _param_2EBF5_USER_EN;
				localparam _param_A20E1_USER_W = _param_2EBF5_USER_W;
				if (1) begin : axis_pre_fifo
					localparam DATA_W = _param_A20E1_DATA_W;
					localparam KEEP_W = _param_A20E1_KEEP_W;
					localparam [0:0] KEEP_EN = _param_A20E1_KEEP_EN;
					localparam [0:0] STRB_EN = _param_A20E1_STRB_EN;
					localparam [0:0] LAST_EN = _param_A20E1_LAST_EN;
					localparam [0:0] ID_EN = _param_A20E1_ID_EN;
					localparam ID_W = _param_A20E1_ID_W;
					localparam [0:0] DEST_EN = _param_A20E1_DEST_EN;
					localparam DEST_W = _param_A20E1_DEST_W;
					localparam [0:0] USER_EN = _param_A20E1_USER_EN;
					localparam USER_W = _param_A20E1_USER_W;
					wire [DATA_W - 1:0] tdata;
					wire [KEEP_W - 1:0] tkeep;
					wire [KEEP_W - 1:0] tstrb;
					wire [ID_W - 1:0] tid;
					wire [DEST_W - 1:0] tdest;
					wire [USER_W - 1:0] tuser;
					wire tlast;
					wire tvalid;
					wire tready;
				end
				localparam _param_A087B_DATA_W = DATA_W;
				localparam _param_A087B_KEEP_EN = KEEP_EN;
				localparam _param_A087B_KEEP_W = KEEP_W;
				localparam _param_A087B_STRB_EN = _param_330AD_STRB_EN;
				localparam _param_A087B_LAST_EN = _param_330AD_LAST_EN;
				localparam _param_A087B_ID_EN = _param_330AD_ID_EN;
				localparam _param_A087B_ID_W = _param_330AD_ID_W;
				localparam _param_A087B_DEST_EN = _param_330AD_DEST_EN;
				localparam _param_A087B_DEST_W = _param_330AD_DEST_W;
				localparam _param_A087B_USER_EN = _param_330AD_USER_EN;
				localparam _param_A087B_USER_W = _param_330AD_USER_W;
				if (1) begin : axis_post_fifo
					localparam DATA_W = _param_A087B_DATA_W;
					localparam KEEP_W = _param_A087B_KEEP_W;
					localparam [0:0] KEEP_EN = _param_A087B_KEEP_EN;
					localparam [0:0] STRB_EN = _param_A087B_STRB_EN;
					localparam [0:0] LAST_EN = _param_A087B_LAST_EN;
					localparam [0:0] ID_EN = _param_A087B_ID_EN;
					localparam ID_W = _param_A087B_ID_W;
					localparam [0:0] DEST_EN = _param_A087B_DEST_EN;
					localparam DEST_W = _param_A087B_DEST_W;
					localparam [0:0] USER_EN = _param_A087B_USER_EN;
					localparam USER_W = _param_A087B_USER_W;
					wire [DATA_W - 1:0] tdata;
					wire [KEEP_W - 1:0] tkeep;
					wire [KEEP_W - 1:0] tstrb;
					wire [ID_W - 1:0] tid;
					wire [DEST_W - 1:0] tdest;
					wire [USER_W - 1:0] tuser;
					wire tlast;
					wire tvalid;
					wire tready;
				end
				if (1) begin : pre_fifo_adapter_inst
					wire clk;
					wire rst;
					localparam S_DATA_W = _param_2EBF5_DATA_W;
					localparam [0:0] S_KEEP_EN = _param_2EBF5_KEEP_EN;
					localparam S_KEEP_W = _param_2EBF5_KEEP_W;
					localparam [0:0] STRB_EN = _param_2EBF5_STRB_EN && _param_A20E1_STRB_EN;
					localparam [0:0] LAST_EN = _param_2EBF5_LAST_EN;
					localparam [0:0] ID_EN = _param_2EBF5_ID_EN && _param_A20E1_ID_EN;
					localparam ID_W = _param_2EBF5_ID_W;
					localparam [0:0] DEST_EN = _param_2EBF5_DEST_EN && _param_A20E1_DEST_EN;
					localparam DEST_W = _param_2EBF5_DEST_W;
					localparam [0:0] USER_EN = _param_2EBF5_USER_EN && _param_A20E1_USER_EN;
					localparam USER_W = _param_2EBF5_USER_W;
					localparam M_DATA_W = _param_A20E1_DATA_W;
					localparam [0:0] M_KEEP_EN = _param_A20E1_KEEP_EN;
					localparam M_KEEP_W = _param_A20E1_KEEP_W;
					localparam S_BYTE_LANES = (S_KEEP_EN ? S_KEEP_W : 1);
					localparam M_BYTE_LANES = (M_KEEP_EN ? M_KEEP_W : 1);
					localparam S_BYTE_SIZE = S_DATA_W / S_BYTE_LANES;
					localparam M_BYTE_SIZE = M_DATA_W / M_BYTE_LANES;
					if ((S_BYTE_SIZE * S_BYTE_LANES) != S_DATA_W) begin : genblk1
						initial begin
							$display("Fatal [elaboration] /home/enio/Projects/openENOC/libs/taxi/src/axis/rtl/taxi_axis_adapter.sv:61:5 - taxi_axis_adapter.genblk1\n msg: ", "Error: input data width not evenly divisible (instance %m)");
							$finish(0);
						end
					end
					if ((M_BYTE_SIZE * M_BYTE_LANES) != M_DATA_W) begin : genblk2
						initial begin
							$display("Fatal [elaboration] /home/enio/Projects/openENOC/libs/taxi/src/axis/rtl/taxi_axis_adapter.sv:64:5 - taxi_axis_adapter.genblk2\n msg: ", "Error: output data width not evenly divisible (instance %m)");
							$finish(0);
						end
					end
					if (S_BYTE_SIZE != M_BYTE_SIZE) begin : genblk3
						initial begin
							$display("Fatal [elaboration] /home/enio/Projects/openENOC/libs/taxi/src/axis/rtl/taxi_axis_adapter.sv:67:5 - taxi_axis_adapter.genblk3\n msg: ", "Error: byte size mismatch (instance %m)");
							$finish(0);
						end
					end
					wire [S_KEEP_W - 1:0] s_axis_tkeep_int = (S_KEEP_EN ? test_openenoc_eth_adapter.uut.fifo_b2a_s_axis.tkeep : {_param_2EBF5_KEEP_W {1'sb1}});
					if (M_BYTE_LANES == S_BYTE_LANES) begin : bypass
						assign test_openenoc_eth_adapter.uut.fifo_b2a_s_axis.tready = test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_pre_fifo.tready;
						assign test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_pre_fifo.tdata = test_openenoc_eth_adapter.uut.fifo_b2a_s_axis.tdata;
						assign test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_pre_fifo.tkeep = (M_KEEP_EN && S_KEEP_EN ? test_openenoc_eth_adapter.uut.fifo_b2a_s_axis.tkeep : {_param_A20E1_KEEP_W {1'sb1}});
						assign test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_pre_fifo.tstrb = (STRB_EN ? test_openenoc_eth_adapter.uut.fifo_b2a_s_axis.tstrb : test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_pre_fifo.tkeep);
						assign test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_pre_fifo.tvalid = test_openenoc_eth_adapter.uut.fifo_b2a_s_axis.tvalid;
						assign test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_pre_fifo.tlast = (LAST_EN ? test_openenoc_eth_adapter.uut.fifo_b2a_s_axis.tlast : 1'b1);
						assign test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_pre_fifo.tid = (ID_EN ? test_openenoc_eth_adapter.uut.fifo_b2a_s_axis.tid : {_param_A20E1_ID_W {1'sb0}});
						assign test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_pre_fifo.tdest = (DEST_EN ? test_openenoc_eth_adapter.uut.fifo_b2a_s_axis.tdest : {_param_A20E1_DEST_W {1'sb0}});
						assign test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_pre_fifo.tuser = (USER_EN ? test_openenoc_eth_adapter.uut.fifo_b2a_s_axis.tuser : {_param_A20E1_USER_W {1'sb0}});
					end
					else if (M_BYTE_LANES > S_BYTE_LANES) begin : upsize
						localparam SEG_COUNT = M_BYTE_LANES / S_BYTE_LANES;
						localparam SEG_DATA_W = M_DATA_W / SEG_COUNT;
						localparam SEG_KEEP_W = M_BYTE_LANES / SEG_COUNT;
						localparam CL_SEG_COUNT = $clog2(SEG_COUNT);
						reg [CL_SEG_COUNT - 1:0] seg_reg = 1'sb0;
						reg [S_DATA_W - 1:0] s_axis_tdata_reg = 1'sb0;
						reg [S_KEEP_W - 1:0] s_axis_tkeep_reg = 1'sb0;
						reg [S_KEEP_W - 1:0] s_axis_tstrb_reg = 1'sb0;
						reg s_axis_tvalid_reg = 1'b0;
						reg s_axis_tlast_reg = 1'b0;
						reg [ID_W - 1:0] s_axis_tid_reg = 1'sb0;
						reg [DEST_W - 1:0] s_axis_tdest_reg = 1'sb0;
						reg [USER_W - 1:0] s_axis_tuser_reg = 1'sb0;
						reg [M_DATA_W - 1:0] m_axis_tdata_reg = 1'sb0;
						reg [M_KEEP_W - 1:0] m_axis_tkeep_reg = 1'sb0;
						reg [M_KEEP_W - 1:0] m_axis_tstrb_reg = 1'sb0;
						reg m_axis_tvalid_reg = 1'b0;
						reg m_axis_tlast_reg = 1'b0;
						reg [ID_W - 1:0] m_axis_tid_reg = 1'sb0;
						reg [DEST_W - 1:0] m_axis_tdest_reg = 1'sb0;
						reg [USER_W - 1:0] m_axis_tuser_reg = 1'sb0;
						assign test_openenoc_eth_adapter.uut.fifo_b2a_s_axis.tready = !s_axis_tvalid_reg;
						assign test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_pre_fifo.tdata = m_axis_tdata_reg;
						assign test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_pre_fifo.tkeep = (M_KEEP_EN ? m_axis_tkeep_reg : {_param_A20E1_KEEP_W {1'sb1}});
						assign test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_pre_fifo.tstrb = (STRB_EN ? m_axis_tstrb_reg : test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_pre_fifo.tkeep);
						assign test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_pre_fifo.tvalid = m_axis_tvalid_reg;
						assign test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_pre_fifo.tlast = (LAST_EN ? m_axis_tlast_reg : 1'b1);
						assign test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_pre_fifo.tid = (ID_EN ? m_axis_tid_reg : {_param_A20E1_ID_W {1'sb0}});
						assign test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_pre_fifo.tdest = (DEST_EN ? m_axis_tdest_reg : {_param_A20E1_DEST_W {1'sb0}});
						assign test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_pre_fifo.tuser = (USER_EN ? m_axis_tuser_reg : {_param_A20E1_USER_W {1'sb0}});
						always @(posedge clk) begin
							m_axis_tvalid_reg <= m_axis_tvalid_reg && !test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_pre_fifo.tready;
							if (!m_axis_tvalid_reg || test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_pre_fifo.tready) begin
								if (seg_reg == 0) begin
									m_axis_tdata_reg[seg_reg * SEG_DATA_W+:SEG_DATA_W] <= (s_axis_tvalid_reg ? s_axis_tdata_reg : test_openenoc_eth_adapter.uut.fifo_b2a_s_axis.tdata);
									begin : sv2v_autoblock_18
										reg [M_KEEP_W - 1:0] sv2v_tmp_cast;
										sv2v_tmp_cast = (s_axis_tvalid_reg ? s_axis_tkeep_reg : s_axis_tkeep_int);
										m_axis_tkeep_reg <= sv2v_tmp_cast;
									end
									begin : sv2v_autoblock_19
										reg [M_KEEP_W - 1:0] sv2v_tmp_cast_1;
										sv2v_tmp_cast_1 = (s_axis_tvalid_reg ? s_axis_tstrb_reg : test_openenoc_eth_adapter.uut.fifo_b2a_s_axis.tstrb);
										m_axis_tstrb_reg <= sv2v_tmp_cast_1;
									end
								end
								else begin
									m_axis_tdata_reg[seg_reg * SEG_DATA_W+:SEG_DATA_W] <= test_openenoc_eth_adapter.uut.fifo_b2a_s_axis.tdata;
									m_axis_tkeep_reg[seg_reg * SEG_KEEP_W+:SEG_KEEP_W] <= s_axis_tkeep_int;
									m_axis_tstrb_reg[seg_reg * SEG_KEEP_W+:SEG_KEEP_W] <= test_openenoc_eth_adapter.uut.fifo_b2a_s_axis.tstrb;
								end
								m_axis_tlast_reg <= (s_axis_tvalid_reg ? s_axis_tlast_reg : test_openenoc_eth_adapter.uut.fifo_b2a_s_axis.tlast);
								m_axis_tid_reg <= (s_axis_tvalid_reg ? s_axis_tid_reg : test_openenoc_eth_adapter.uut.fifo_b2a_s_axis.tid);
								m_axis_tdest_reg <= (s_axis_tvalid_reg ? s_axis_tdest_reg : test_openenoc_eth_adapter.uut.fifo_b2a_s_axis.tdest);
								m_axis_tuser_reg <= (s_axis_tvalid_reg ? s_axis_tuser_reg : test_openenoc_eth_adapter.uut.fifo_b2a_s_axis.tuser);
								if (s_axis_tvalid_reg) begin
									s_axis_tvalid_reg <= 1'b0;
									begin : sv2v_autoblock_20
										reg signed [CL_SEG_COUNT - 1:0] sv2v_tmp_cast;
										sv2v_tmp_cast = SEG_COUNT - 1;
										if ((LAST_EN && s_axis_tlast_reg) || (seg_reg == sv2v_tmp_cast)) begin
											seg_reg <= 1'sb0;
											m_axis_tvalid_reg <= 1'b1;
										end
										else
											seg_reg <= seg_reg + 1;
									end
								end
								else if (test_openenoc_eth_adapter.uut.fifo_b2a_s_axis.tvalid) begin : sv2v_autoblock_21
									reg signed [CL_SEG_COUNT - 1:0] sv2v_tmp_cast;
									sv2v_tmp_cast = SEG_COUNT - 1;
									if ((LAST_EN && test_openenoc_eth_adapter.uut.fifo_b2a_s_axis.tlast) || (seg_reg == sv2v_tmp_cast)) begin
										seg_reg <= 1'sb0;
										m_axis_tvalid_reg <= 1'b1;
									end
									else
										seg_reg <= seg_reg + 1;
								end
							end
							else if (test_openenoc_eth_adapter.uut.fifo_b2a_s_axis.tvalid && test_openenoc_eth_adapter.uut.fifo_b2a_s_axis.tready) begin
								s_axis_tdata_reg <= test_openenoc_eth_adapter.uut.fifo_b2a_s_axis.tdata;
								s_axis_tkeep_reg <= s_axis_tkeep_int;
								s_axis_tstrb_reg <= test_openenoc_eth_adapter.uut.fifo_b2a_s_axis.tstrb;
								s_axis_tvalid_reg <= 1'b1;
								s_axis_tlast_reg <= test_openenoc_eth_adapter.uut.fifo_b2a_s_axis.tlast;
								s_axis_tid_reg <= test_openenoc_eth_adapter.uut.fifo_b2a_s_axis.tid;
								s_axis_tdest_reg <= test_openenoc_eth_adapter.uut.fifo_b2a_s_axis.tdest;
								s_axis_tuser_reg <= test_openenoc_eth_adapter.uut.fifo_b2a_s_axis.tuser;
							end
							if (rst) begin
								seg_reg <= 1'sb0;
								s_axis_tvalid_reg <= 1'b0;
								m_axis_tvalid_reg <= 1'b0;
							end
						end
					end
					else begin : downsize
						localparam SEG_COUNT = S_BYTE_LANES / M_BYTE_LANES;
						localparam SEG_DATA_W = S_DATA_W / SEG_COUNT;
						localparam SEG_KEEP_W = S_BYTE_LANES / SEG_COUNT;
						reg [S_DATA_W - 1:0] s_axis_tdata_reg = 1'sb0;
						reg [S_KEEP_W - 1:0] s_axis_tkeep_reg = 1'sb0;
						reg [S_KEEP_W - 1:0] s_axis_tstrb_reg = 1'sb0;
						reg s_axis_tvalid_reg = 1'b0;
						reg s_axis_tlast_reg = 1'b0;
						reg [ID_W - 1:0] s_axis_tid_reg = 1'sb0;
						reg [DEST_W - 1:0] s_axis_tdest_reg = 1'sb0;
						reg [USER_W - 1:0] s_axis_tuser_reg = 1'sb0;
						reg [M_DATA_W - 1:0] m_axis_tdata_reg = 1'sb0;
						reg [M_KEEP_W - 1:0] m_axis_tkeep_reg = 1'sb0;
						reg [M_KEEP_W - 1:0] m_axis_tstrb_reg = 1'sb0;
						reg m_axis_tvalid_reg = 1'b0;
						reg m_axis_tlast_reg = 1'b0;
						reg [ID_W - 1:0] m_axis_tid_reg = 1'sb0;
						reg [DEST_W - 1:0] m_axis_tdest_reg = 1'sb0;
						reg [USER_W - 1:0] m_axis_tuser_reg = 1'sb0;
						assign test_openenoc_eth_adapter.uut.fifo_b2a_s_axis.tready = !s_axis_tvalid_reg;
						assign test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_pre_fifo.tdata = m_axis_tdata_reg;
						assign test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_pre_fifo.tkeep = (M_KEEP_EN ? m_axis_tkeep_reg : {_param_A20E1_KEEP_W {1'sb1}});
						assign test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_pre_fifo.tstrb = (STRB_EN ? m_axis_tstrb_reg : test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_pre_fifo.tkeep);
						assign test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_pre_fifo.tvalid = m_axis_tvalid_reg;
						assign test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_pre_fifo.tlast = m_axis_tlast_reg;
						assign test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_pre_fifo.tid = (ID_EN ? m_axis_tid_reg : {_param_A20E1_ID_W {1'sb0}});
						assign test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_pre_fifo.tdest = (DEST_EN ? m_axis_tdest_reg : {_param_A20E1_DEST_W {1'sb0}});
						assign test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_pre_fifo.tuser = (USER_EN ? m_axis_tuser_reg : {_param_A20E1_USER_W {1'sb0}});
						always @(posedge clk) begin
							m_axis_tvalid_reg <= m_axis_tvalid_reg && !test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_pre_fifo.tready;
							if (!m_axis_tvalid_reg || test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_pre_fifo.tready) begin
								begin : sv2v_autoblock_22
									reg [M_DATA_W - 1:0] sv2v_tmp_cast;
									sv2v_tmp_cast = (s_axis_tvalid_reg ? s_axis_tdata_reg : test_openenoc_eth_adapter.uut.fifo_b2a_s_axis.tdata);
									m_axis_tdata_reg <= sv2v_tmp_cast;
								end
								begin : sv2v_autoblock_23
									reg [M_KEEP_W - 1:0] sv2v_tmp_cast_1;
									sv2v_tmp_cast_1 = (s_axis_tvalid_reg ? s_axis_tkeep_reg : s_axis_tkeep_int);
									m_axis_tkeep_reg <= sv2v_tmp_cast_1;
								end
								begin : sv2v_autoblock_24
									reg [M_KEEP_W - 1:0] sv2v_tmp_cast_2;
									sv2v_tmp_cast_2 = (s_axis_tvalid_reg ? s_axis_tstrb_reg : test_openenoc_eth_adapter.uut.fifo_b2a_s_axis.tstrb);
									m_axis_tstrb_reg <= sv2v_tmp_cast_2;
								end
								m_axis_tlast_reg <= 1'b0;
								m_axis_tid_reg <= (s_axis_tvalid_reg ? s_axis_tid_reg : test_openenoc_eth_adapter.uut.fifo_b2a_s_axis.tid);
								m_axis_tdest_reg <= (s_axis_tvalid_reg ? s_axis_tdest_reg : test_openenoc_eth_adapter.uut.fifo_b2a_s_axis.tdest);
								m_axis_tuser_reg <= (s_axis_tvalid_reg ? s_axis_tuser_reg : test_openenoc_eth_adapter.uut.fifo_b2a_s_axis.tuser);
								if (s_axis_tvalid_reg) begin
									s_axis_tdata_reg <= s_axis_tdata_reg >> SEG_DATA_W;
									s_axis_tkeep_reg <= s_axis_tkeep_reg >> SEG_KEEP_W;
									s_axis_tstrb_reg <= s_axis_tstrb_reg >> SEG_KEEP_W;
									m_axis_tvalid_reg <= 1'b1;
									if ((s_axis_tkeep_reg >> SEG_KEEP_W) == 0) begin
										s_axis_tvalid_reg <= 1'b0;
										m_axis_tlast_reg <= s_axis_tlast_reg;
									end
								end
								else if (test_openenoc_eth_adapter.uut.fifo_b2a_s_axis.tvalid && test_openenoc_eth_adapter.uut.fifo_b2a_s_axis.tready) begin
									s_axis_tdata_reg <= test_openenoc_eth_adapter.uut.fifo_b2a_s_axis.tdata >> SEG_DATA_W;
									s_axis_tkeep_reg <= s_axis_tkeep_int >> SEG_KEEP_W;
									s_axis_tstrb_reg <= test_openenoc_eth_adapter.uut.fifo_b2a_s_axis.tstrb >> SEG_KEEP_W;
									s_axis_tlast_reg <= test_openenoc_eth_adapter.uut.fifo_b2a_s_axis.tlast;
									s_axis_tid_reg <= test_openenoc_eth_adapter.uut.fifo_b2a_s_axis.tid;
									s_axis_tdest_reg <= test_openenoc_eth_adapter.uut.fifo_b2a_s_axis.tdest;
									s_axis_tuser_reg <= test_openenoc_eth_adapter.uut.fifo_b2a_s_axis.tuser;
									m_axis_tvalid_reg <= 1'b1;
									if (S_KEEP_EN && ((s_axis_tkeep_int >> SEG_KEEP_W) == 0)) begin
										s_axis_tvalid_reg <= 1'b0;
										m_axis_tlast_reg <= test_openenoc_eth_adapter.uut.fifo_b2a_s_axis.tlast;
									end
									else
										s_axis_tvalid_reg <= 1'b1;
								end
							end
							else if (test_openenoc_eth_adapter.uut.fifo_b2a_s_axis.tvalid && test_openenoc_eth_adapter.uut.fifo_b2a_s_axis.tready) begin
								s_axis_tdata_reg <= test_openenoc_eth_adapter.uut.fifo_b2a_s_axis.tdata;
								s_axis_tkeep_reg <= s_axis_tkeep_int;
								s_axis_tstrb_reg <= test_openenoc_eth_adapter.uut.fifo_b2a_s_axis.tstrb;
								s_axis_tvalid_reg <= 1'b1;
								s_axis_tlast_reg <= test_openenoc_eth_adapter.uut.fifo_b2a_s_axis.tlast;
								s_axis_tid_reg <= test_openenoc_eth_adapter.uut.fifo_b2a_s_axis.tid;
								s_axis_tdest_reg <= test_openenoc_eth_adapter.uut.fifo_b2a_s_axis.tdest;
								s_axis_tuser_reg <= test_openenoc_eth_adapter.uut.fifo_b2a_s_axis.tuser;
							end
							if (rst) begin
								s_axis_tvalid_reg <= 1'b0;
								m_axis_tvalid_reg <= 1'b0;
							end
						end
					end
				end
				assign pre_fifo_adapter_inst.clk = s_clk;
				assign pre_fifo_adapter_inst.rst = s_rst;
				localparam _param_BDF4F_DEPTH = DEPTH;
				localparam _param_BDF4F_RAM_PIPELINE = RAM_PIPELINE;
				localparam _param_BDF4F_OUTPUT_FIFO_EN = OUTPUT_FIFO_EN;
				localparam _param_BDF4F_FRAME_FIFO = FRAME_FIFO;
				localparam _param_BDF4F_USER_BAD_FRAME_VALUE = USER_BAD_FRAME_VALUE;
				localparam _param_BDF4F_USER_BAD_FRAME_MASK = USER_BAD_FRAME_MASK;
				localparam _param_BDF4F_DROP_OVERSIZE_FRAME = DROP_OVERSIZE_FRAME;
				localparam _param_BDF4F_DROP_BAD_FRAME = DROP_BAD_FRAME;
				localparam _param_BDF4F_DROP_WHEN_FULL = DROP_WHEN_FULL;
				localparam _param_BDF4F_MARK_WHEN_FULL = MARK_WHEN_FULL;
				localparam _param_BDF4F_PAUSE_EN = PAUSE_EN;
				localparam _param_BDF4F_FRAME_PAUSE = FRAME_PAUSE;
				if (1) begin : fifo_inst
					localparam DEPTH = _param_BDF4F_DEPTH;
					localparam FIFO_RAMSTYLE = "auto";
					localparam RAM_PIPELINE = _param_BDF4F_RAM_PIPELINE;
					localparam [0:0] OUTPUT_FIFO_EN = _param_BDF4F_OUTPUT_FIFO_EN;
					localparam OUTPUT_FIFO_RAMSTYLE = "distributed";
					localparam [0:0] FRAME_FIFO = _param_BDF4F_FRAME_FIFO;
					localparam USER_BAD_FRAME_VALUE = _param_BDF4F_USER_BAD_FRAME_VALUE;
					localparam USER_BAD_FRAME_MASK = _param_BDF4F_USER_BAD_FRAME_MASK;
					localparam [0:0] DROP_OVERSIZE_FRAME = _param_BDF4F_DROP_OVERSIZE_FRAME;
					localparam [0:0] DROP_BAD_FRAME = _param_BDF4F_DROP_BAD_FRAME;
					localparam [0:0] DROP_WHEN_FULL = _param_BDF4F_DROP_WHEN_FULL;
					localparam [0:0] MARK_WHEN_FULL = _param_BDF4F_MARK_WHEN_FULL;
					localparam [0:0] PAUSE_EN = _param_BDF4F_PAUSE_EN;
					localparam [0:0] FRAME_PAUSE = _param_BDF4F_FRAME_PAUSE;
					wire s_clk;
					wire s_rst;
					wire m_clk;
					wire m_rst;
					wire s_pause_req;
					wire s_pause_ack;
					wire m_pause_req;
					wire m_pause_ack;
					wire [$clog2(DEPTH):0] s_status_depth;
					wire [$clog2(DEPTH):0] s_status_depth_commit;
					wire s_status_overflow;
					wire s_status_bad_frame;
					wire s_status_good_frame;
					wire [$clog2(DEPTH):0] m_status_depth;
					wire [$clog2(DEPTH):0] m_status_depth_commit;
					wire m_status_overflow;
					wire m_status_bad_frame;
					wire m_status_good_frame;
					localparam DATA_W = _param_A20E1_DATA_W;
					localparam [0:0] KEEP_EN = _param_A20E1_KEEP_EN && _param_A087B_KEEP_EN;
					localparam KEEP_W = _param_A20E1_KEEP_W;
					localparam [0:0] STRB_EN = _param_A20E1_STRB_EN && _param_A087B_STRB_EN;
					localparam [0:0] LAST_EN = _param_A20E1_LAST_EN && _param_A087B_LAST_EN;
					localparam [0:0] ID_EN = _param_A20E1_ID_EN && _param_A087B_ID_EN;
					localparam ID_W = _param_A20E1_ID_W;
					localparam [0:0] DEST_EN = _param_A20E1_DEST_EN && _param_A087B_DEST_EN;
					localparam DEST_W = _param_A20E1_DEST_W;
					localparam [0:0] USER_EN = _param_A20E1_USER_EN && _param_A087B_USER_EN;
					localparam USER_W = _param_A20E1_USER_W;
					localparam CL_DEPTH = $clog2(DEPTH);
					localparam CL_KEEP_W = $clog2(KEEP_W);
					localparam FIFO_AW = (KEEP_EN && (KEEP_W > 1) ? $clog2(DEPTH / KEEP_W) : CL_DEPTH);
					localparam OUTPUT_FIFO_AW = (RAM_PIPELINE < 2 ? 3 : $clog2((RAM_PIPELINE * 2) + 7));
					if (FRAME_FIFO && !LAST_EN) begin : genblk1
						initial begin
							$display("Fatal [elaboration] /home/enio/Projects/openENOC/libs/taxi/src/axis/rtl/taxi_axis_async_fifo.sv:119:5 - taxi_axis_async_fifo.genblk1\n msg: ", "Error: FRAME_FIFO set requires LAST_EN set (instance %m)");
							$finish(0);
						end
					end
					if (DROP_OVERSIZE_FRAME && !FRAME_FIFO) begin : genblk2
						initial begin
							$display("Fatal [elaboration] /home/enio/Projects/openENOC/libs/taxi/src/axis/rtl/taxi_axis_async_fifo.sv:122:5 - taxi_axis_async_fifo.genblk2\n msg: ", "Error: DROP_OVERSIZE_FRAME set requires FRAME_FIFO set (instance %m)");
							$finish(0);
						end
					end
					if (DROP_BAD_FRAME && !(FRAME_FIFO && DROP_OVERSIZE_FRAME)) begin : genblk3
						initial begin
							$display("Fatal [elaboration] /home/enio/Projects/openENOC/libs/taxi/src/axis/rtl/taxi_axis_async_fifo.sv:125:5 - taxi_axis_async_fifo.genblk3\n msg: ", "Error: DROP_BAD_FRAME set requires FRAME_FIFO and DROP_OVERSIZE_FRAME set (instance %m)");
							$finish(0);
						end
					end
					if (DROP_WHEN_FULL && !(FRAME_FIFO && DROP_OVERSIZE_FRAME)) begin : genblk4
						initial begin
							$display("Fatal [elaboration] /home/enio/Projects/openENOC/libs/taxi/src/axis/rtl/taxi_axis_async_fifo.sv:128:5 - taxi_axis_async_fifo.genblk4\n msg: ", "Error: DROP_WHEN_FULL set requires FRAME_FIFO and DROP_OVERSIZE_FRAME set (instance %m)");
							$finish(0);
						end
					end
					function automatic [USER_W - 1:0] sv2v_cast_30231;
						input reg [USER_W - 1:0] inp;
						sv2v_cast_30231 = inp;
					endfunction
					if ((DROP_BAD_FRAME || MARK_WHEN_FULL) && ((sv2v_cast_30231(USER_BAD_FRAME_MASK) & {USER_W {1'b1}}) == 0)) begin : genblk5
						initial begin
							$display("Fatal [elaboration] /home/enio/Projects/openENOC/libs/taxi/src/axis/rtl/taxi_axis_async_fifo.sv:131:5 - taxi_axis_async_fifo.genblk5\n msg: ", "Error: Invalid USER_BAD_FRAME_MASK value (instance %m)");
							$finish(0);
						end
					end
					if (MARK_WHEN_FULL && FRAME_FIFO) begin : genblk6
						initial begin
							$display("Fatal [elaboration] /home/enio/Projects/openENOC/libs/taxi/src/axis/rtl/taxi_axis_async_fifo.sv:134:5 - taxi_axis_async_fifo.genblk6\n msg: ", "Error: MARK_WHEN_FULL is not compatible with FRAME_FIFO (instance %m)");
							$finish(0);
						end
					end
					if (MARK_WHEN_FULL && !LAST_EN) begin : genblk7
						initial begin
							$display("Fatal [elaboration] /home/enio/Projects/openENOC/libs/taxi/src/axis/rtl/taxi_axis_async_fifo.sv:137:5 - taxi_axis_async_fifo.genblk7\n msg: ", "Error: MARK_WHEN_FULL set requires LAST_EN set (instance %m)");
							$finish(0);
						end
					end
					if (_param_A087B_DATA_W != DATA_W) begin : genblk8
						initial begin
							$display("Fatal [elaboration] /home/enio/Projects/openENOC/libs/taxi/src/axis/rtl/taxi_axis_async_fifo.sv:140:5 - taxi_axis_async_fifo.genblk8\n msg: ", "Error: Interface DATA_W parameter mismatch (instance %m)");
							$finish(0);
						end
					end
					if (KEEP_EN && (_param_A087B_KEEP_W != KEEP_W)) begin : genblk9
						initial begin
							$display("Fatal [elaboration] /home/enio/Projects/openENOC/libs/taxi/src/axis/rtl/taxi_axis_async_fifo.sv:143:5 - taxi_axis_async_fifo.genblk9\n msg: ", "Error: Interface KEEP_W parameter mismatch (instance %m)");
							$finish(0);
						end
					end
					if (DROP_BAD_FRAME && !_param_A20E1_USER_EN) begin : genblk10
						initial begin
							$display("Fatal [elaboration] /home/enio/Projects/openENOC/libs/taxi/src/axis/rtl/taxi_axis_async_fifo.sv:146:5 - taxi_axis_async_fifo.genblk10\n msg: ", "Error: DROP_BAD_FRAME set requires s_axis.USER_EN (instance %m)");
							$finish(0);
						end
					end
					if (MARK_WHEN_FULL && !_param_A087B_USER_EN) begin : genblk11
						initial begin
							$display("Fatal [elaboration] /home/enio/Projects/openENOC/libs/taxi/src/axis/rtl/taxi_axis_async_fifo.sv:149:5 - taxi_axis_async_fifo.genblk11\n msg: ", "Error: MARK_WHEN_FULL set requires m_axis.USER_EN (instance %m)");
							$finish(0);
						end
					end
					localparam KEEP_OFFSET = DATA_W;
					localparam STRB_OFFSET = KEEP_OFFSET + (KEEP_EN ? KEEP_W : 0);
					localparam LAST_OFFSET = STRB_OFFSET + (STRB_EN ? KEEP_W : 0);
					localparam ID_OFFSET = LAST_OFFSET + (LAST_EN ? 1 : 0);
					localparam DEST_OFFSET = ID_OFFSET + (ID_EN ? ID_W : 0);
					localparam USER_OFFSET = DEST_OFFSET + (DEST_EN ? DEST_W : 0);
					localparam WIDTH = USER_OFFSET + (USER_EN ? USER_W : 0);
					function [FIFO_AW:0] bin2gray;
						input [FIFO_AW:0] b;
						bin2gray = b ^ (b >> 1);
					endfunction
					function [FIFO_AW:0] gray2bin;
						input [FIFO_AW:0] g;
						integer i;
						for (i = 0; i <= FIFO_AW; i = i + 1)
							gray2bin[i] = ^(g >> i);
					endfunction
					reg [FIFO_AW:0] wr_ptr_reg = 1'sb0;
					reg [FIFO_AW:0] wr_ptr_commit_reg = 1'sb0;
					reg [FIFO_AW:0] wr_ptr_gray_reg = 1'sb0;
					reg [FIFO_AW:0] wr_ptr_sync_commit_reg = 1'sb0;
					reg [FIFO_AW:0] rd_ptr_reg = 1'sb0;
					reg [FIFO_AW:0] rd_ptr_gray_reg = 1'sb0;
					reg [FIFO_AW:0] wr_ptr_conv_reg = 1'sb0;
					reg [FIFO_AW:0] rd_ptr_conv_reg = 1'sb0;
					reg [FIFO_AW:0] wr_ptr_temp;
					reg [FIFO_AW:0] rd_ptr_temp;
					(* SHREG_EXTRACT = "NO" *) reg [FIFO_AW:0] wr_ptr_gray_sync1_reg = 1'sb0;
					(* SHREG_EXTRACT = "NO" *) reg [FIFO_AW:0] wr_ptr_gray_sync2_reg = 1'sb0;
					(* SHREG_EXTRACT = "NO" *) reg [FIFO_AW:0] wr_ptr_commit_sync_reg = 1'sb0;
					(* SHREG_EXTRACT = "NO" *) reg [FIFO_AW:0] rd_ptr_gray_sync1_reg = 1'sb0;
					(* SHREG_EXTRACT = "NO" *) reg [FIFO_AW:0] rd_ptr_gray_sync2_reg = 1'sb0;
					reg wr_ptr_update_valid_reg = 1'b0;
					reg wr_ptr_update_reg = 1'b0;
					(* SHREG_EXTRACT = "NO" *) reg wr_ptr_update_sync1_reg = 1'b0;
					(* SHREG_EXTRACT = "NO" *) reg wr_ptr_update_sync2_reg = 1'b0;
					(* SHREG_EXTRACT = "NO" *) reg wr_ptr_update_sync3_reg = 1'b0;
					(* SHREG_EXTRACT = "NO" *) reg wr_ptr_update_ack_sync1_reg = 1'b0;
					(* SHREG_EXTRACT = "NO" *) reg wr_ptr_update_ack_sync2_reg = 1'b0;
					wire s_rst_sync;
					wire m_rst_sync;
					(* ramstyle = "no_rw_check" *) reg [WIDTH - 1:0] mem [0:(2 ** FIFO_AW) - 1];
					reg mem_read_data_valid_reg = 1'b0;
					(* shreg_extract = "no" *) reg [WIDTH - 1:0] mem_rd_data_pipe_reg [RAM_PIPELINE + 0:0];
					reg [RAM_PIPELINE + 0:0] mem_rd_valid_pipe_reg = 0;
					wire full = wr_ptr_gray_reg == (rd_ptr_gray_sync2_reg ^ {2'b11, {FIFO_AW - 1 {1'b0}}});
					wire empty = (FRAME_FIFO ? rd_ptr_reg == wr_ptr_commit_sync_reg : rd_ptr_gray_reg == wr_ptr_gray_sync2_reg);
					wire full_wr = wr_ptr_reg == (wr_ptr_commit_reg ^ {1'b1, {FIFO_AW {1'b0}}});
					wire write;
					wire read;
					wire store_output;
					reg s_frame_reg = 1'b0;
					reg m_frame_reg = 1'b0;
					reg drop_frame_reg = 1'b0;
					reg mark_frame_reg = 1'b0;
					reg send_frame_reg = 1'b0;
					reg overflow_reg = 1'b0;
					reg bad_frame_reg = 1'b0;
					reg good_frame_reg = 1'b0;
					reg m_empty_pipe_reg = 1'b0;
					reg m_terminate_frame_reg = 1'b0;
					reg [FIFO_AW:0] s_depth_reg = 1'sb0;
					reg [FIFO_AW:0] s_depth_commit_reg = 1'sb0;
					reg [FIFO_AW:0] m_depth_reg = 1'sb0;
					reg [FIFO_AW:0] m_depth_commit_reg = 1'sb0;
					reg overflow_sync1_reg = 1'b0;
					reg overflow_sync2_reg = 1'b0;
					reg overflow_sync3_reg = 1'b0;
					reg overflow_sync4_reg = 1'b0;
					reg bad_frame_sync1_reg = 1'b0;
					reg bad_frame_sync2_reg = 1'b0;
					reg bad_frame_sync3_reg = 1'b0;
					reg bad_frame_sync4_reg = 1'b0;
					reg good_frame_sync1_reg = 1'b0;
					reg good_frame_sync2_reg = 1'b0;
					reg good_frame_sync3_reg = 1'b0;
					reg good_frame_sync4_reg = 1'b0;
					assign test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_pre_fifo.tready = (FRAME_FIFO ? (!full || (full_wr && DROP_OVERSIZE_FRAME)) || DROP_WHEN_FULL : !full || MARK_WHEN_FULL) && !s_rst_sync;
					wire [WIDTH - 1:0] mem_wr_data;
					assign mem_wr_data[DATA_W - 1:0] = test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_pre_fifo.tdata;
					if (KEEP_EN) begin : genblk12
						assign mem_wr_data[KEEP_OFFSET+:KEEP_W] = test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_pre_fifo.tkeep;
					end
					if (STRB_EN) begin : genblk13
						assign mem_wr_data[STRB_OFFSET+:KEEP_W] = test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_pre_fifo.tstrb;
					end
					if (LAST_EN) begin : genblk14
						assign mem_wr_data[LAST_OFFSET] = test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_pre_fifo.tlast | mark_frame_reg;
					end
					if (ID_EN) begin : genblk15
						assign mem_wr_data[ID_OFFSET+:ID_W] = test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_pre_fifo.tid;
					end
					if (DEST_EN) begin : genblk16
						assign mem_wr_data[DEST_OFFSET+:DEST_W] = test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_pre_fifo.tdest;
					end
					if (USER_EN) begin : genblk17
						function automatic [USER_W - 1:0] sv2v_cast_30231;
							input reg [USER_W - 1:0] inp;
							sv2v_cast_30231 = inp;
						endfunction
						assign mem_wr_data[USER_OFFSET+:USER_W] = (mark_frame_reg ? sv2v_cast_30231(USER_BAD_FRAME_VALUE) : test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_pre_fifo.tuser);
					end
					wire [WIDTH - 1:0] mem_rd_data = mem_rd_data_pipe_reg[RAM_PIPELINE + 0];
					wire m_axis_tready_pipe;
					wire m_axis_tvalid_pipe = mem_rd_valid_pipe_reg[RAM_PIPELINE + 0];
					wire [DATA_W - 1:0] m_axis_tdata_pipe = mem_rd_data[DATA_W - 1:0];
					wire [KEEP_W - 1:0] m_axis_tkeep_pipe;
					wire [KEEP_W - 1:0] m_axis_tstrb_pipe;
					wire m_axis_tlast_pipe;
					wire [ID_W - 1:0] m_axis_tid_pipe;
					wire [DEST_W - 1:0] m_axis_tdest_pipe;
					wire [USER_W - 1:0] m_axis_tuser_pipe;
					if (KEEP_EN) begin : genblk18
						assign m_axis_tkeep_pipe = mem_rd_data[KEEP_OFFSET+:KEEP_W];
					end
					else begin : genblk18
						assign m_axis_tkeep_pipe = 1'sb1;
					end
					if (STRB_EN) begin : genblk19
						assign m_axis_tstrb_pipe = mem_rd_data[STRB_OFFSET+:KEEP_W];
					end
					else begin : genblk19
						assign m_axis_tstrb_pipe = m_axis_tkeep_pipe;
					end
					if (LAST_EN) begin : genblk20
						assign m_axis_tlast_pipe = mem_rd_data[LAST_OFFSET] | m_terminate_frame_reg;
					end
					else begin : genblk20
						assign m_axis_tlast_pipe = 1'b1;
					end
					if (ID_EN) begin : genblk21
						assign m_axis_tid_pipe = mem_rd_data[ID_OFFSET+:ID_W];
					end
					else begin : genblk21
						assign m_axis_tid_pipe = 1'sb0;
					end
					if (DEST_EN) begin : genblk22
						assign m_axis_tdest_pipe = mem_rd_data[DEST_OFFSET+:DEST_W];
					end
					else begin : genblk22
						assign m_axis_tdest_pipe = 1'sb0;
					end
					if (USER_EN) begin : genblk23
						function automatic [USER_W - 1:0] sv2v_cast_30231;
							input reg [USER_W - 1:0] inp;
							sv2v_cast_30231 = inp;
						endfunction
						assign m_axis_tuser_pipe = (m_terminate_frame_reg ? sv2v_cast_30231(USER_BAD_FRAME_VALUE) : mem_rd_data[USER_OFFSET+:USER_W]);
					end
					else begin : genblk23
						assign m_axis_tuser_pipe = 1'sb0;
					end
					wire m_axis_tready_out;
					wire m_axis_tvalid_out;
					wire [DATA_W - 1:0] m_axis_tdata_out;
					wire [KEEP_W - 1:0] m_axis_tkeep_out;
					wire [KEEP_W - 1:0] m_axis_tstrb_out;
					wire m_axis_tlast_out;
					wire [ID_W - 1:0] m_axis_tid_out;
					wire [DEST_W - 1:0] m_axis_tdest_out;
					wire [USER_W - 1:0] m_axis_tuser_out;
					wire pipe_ready;
					function automatic [((CL_DEPTH + 0) >= 0 ? CL_DEPTH + 1 : 1 - (CL_DEPTH + 0)) - 1:0] sv2v_cast_FF327;
						input reg [((CL_DEPTH + 0) >= 0 ? CL_DEPTH + 1 : 1 - (CL_DEPTH + 0)) - 1:0] inp;
						sv2v_cast_FF327 = inp;
					endfunction
					assign s_status_depth = (KEEP_EN && (KEEP_W > 1) ? {s_depth_reg, {CL_KEEP_W {1'b0}}} : sv2v_cast_FF327(s_depth_reg));
					assign s_status_depth_commit = (KEEP_EN && (KEEP_W > 1) ? {s_depth_commit_reg, {CL_KEEP_W {1'b0}}} : sv2v_cast_FF327(s_depth_commit_reg));
					assign s_status_overflow = overflow_reg;
					assign s_status_bad_frame = bad_frame_reg;
					assign s_status_good_frame = good_frame_reg;
					assign m_status_depth = (KEEP_EN && (KEEP_W > 1) ? {m_depth_reg, {CL_KEEP_W {1'b0}}} : sv2v_cast_FF327(m_depth_reg));
					assign m_status_depth_commit = (KEEP_EN && (KEEP_W > 1) ? {m_depth_commit_reg, {CL_KEEP_W {1'b0}}} : sv2v_cast_FF327(m_depth_commit_reg));
					assign m_status_overflow = overflow_sync3_reg ^ overflow_sync4_reg;
					assign m_status_bad_frame = bad_frame_sync3_reg ^ bad_frame_sync4_reg;
					assign m_status_good_frame = good_frame_sync3_reg ^ good_frame_sync4_reg;
					taxi_sync_reset #(.N(4)) s_reset_sync_inst(
						.clk(s_clk),
						.rst(m_rst),
						.out(s_rst_sync)
					);
					taxi_sync_reset #(.N(4)) m_reset_sync_inst(
						.clk(m_clk),
						.rst(s_rst),
						.out(m_rst_sync)
					);
					always @(posedge s_clk) begin
						overflow_reg <= 1'b0;
						bad_frame_reg <= 1'b0;
						good_frame_reg <= 1'b0;
						if (FRAME_FIFO && wr_ptr_update_valid_reg) begin
							if (wr_ptr_update_reg == wr_ptr_update_ack_sync2_reg) begin
								wr_ptr_update_valid_reg <= 1'b0;
								wr_ptr_sync_commit_reg <= wr_ptr_commit_reg;
								wr_ptr_update_reg <= !wr_ptr_update_ack_sync2_reg;
							end
						end
						if ((test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_pre_fifo.tready && test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_pre_fifo.tvalid) && LAST_EN)
							s_frame_reg <= !test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_pre_fifo.tlast;
						if (s_rst_sync && LAST_EN) begin
							if (s_frame_reg && !((test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_pre_fifo.tready && test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_pre_fifo.tvalid) && test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_pre_fifo.tlast))
								drop_frame_reg <= 1'b1;
							if ((test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_pre_fifo.tready && test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_pre_fifo.tvalid) && !test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_pre_fifo.tlast)
								drop_frame_reg <= 1'b1;
						end
						if (FRAME_FIFO) begin
							if (test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_pre_fifo.tready && test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_pre_fifo.tvalid) begin
								if (((full && DROP_WHEN_FULL) || (full_wr && DROP_OVERSIZE_FRAME)) || drop_frame_reg) begin
									drop_frame_reg <= 1'b1;
									if (test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_pre_fifo.tlast) begin
										wr_ptr_temp = wr_ptr_commit_reg;
										wr_ptr_reg <= wr_ptr_temp;
										wr_ptr_gray_reg <= bin2gray(wr_ptr_temp);
										drop_frame_reg <= 1'b0;
										overflow_reg <= 1'b1;
									end
								end
								else begin
									mem[wr_ptr_reg[FIFO_AW - 1:0]] <= mem_wr_data;
									wr_ptr_temp = wr_ptr_reg + 1;
									wr_ptr_reg <= wr_ptr_temp;
									wr_ptr_gray_reg <= bin2gray(wr_ptr_temp);
									if (test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_pre_fifo.tlast || (!DROP_OVERSIZE_FRAME && (full_wr || send_frame_reg))) begin
										send_frame_reg <= !test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_pre_fifo.tlast;
										begin : sv2v_autoblock_25
											reg [USER_W - 1:0] sv2v_tmp_cast;
											reg [USER_W - 1:0] sv2v_tmp_cast_1;
											sv2v_tmp_cast = USER_BAD_FRAME_MASK;
											sv2v_tmp_cast_1 = USER_BAD_FRAME_VALUE;
											if ((test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_pre_fifo.tlast && DROP_BAD_FRAME) && ((sv2v_tmp_cast & ~(test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_pre_fifo.tuser ^ sv2v_tmp_cast_1)) != 0)) begin
												wr_ptr_temp = wr_ptr_commit_reg;
												wr_ptr_reg <= wr_ptr_temp;
												wr_ptr_gray_reg <= bin2gray(wr_ptr_temp);
												bad_frame_reg <= 1'b1;
											end
											else begin
												wr_ptr_temp = wr_ptr_reg + 1;
												wr_ptr_reg <= wr_ptr_temp;
												wr_ptr_commit_reg <= wr_ptr_temp;
												wr_ptr_gray_reg <= bin2gray(wr_ptr_temp);
												if (wr_ptr_update_reg == wr_ptr_update_ack_sync2_reg) begin
													wr_ptr_update_valid_reg <= 1'b0;
													wr_ptr_sync_commit_reg <= wr_ptr_temp;
													wr_ptr_update_reg <= !wr_ptr_update_ack_sync2_reg;
												end
												else
													wr_ptr_update_valid_reg <= 1'b1;
												good_frame_reg <= test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_pre_fifo.tlast;
											end
										end
									end
								end
							end
							else if (((test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_pre_fifo.tvalid && full_wr) && FRAME_FIFO) && !DROP_OVERSIZE_FRAME) begin
								send_frame_reg <= 1'b1;
								wr_ptr_temp = wr_ptr_reg;
								wr_ptr_reg <= wr_ptr_temp;
								wr_ptr_commit_reg <= wr_ptr_temp;
								wr_ptr_gray_reg <= bin2gray(wr_ptr_temp);
								if (wr_ptr_update_reg == wr_ptr_update_ack_sync2_reg) begin
									wr_ptr_update_valid_reg <= 1'b0;
									wr_ptr_sync_commit_reg <= wr_ptr_temp;
									wr_ptr_update_reg <= !wr_ptr_update_ack_sync2_reg;
								end
								else
									wr_ptr_update_valid_reg <= 1'b1;
							end
						end
						else if (test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_pre_fifo.tready && test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_pre_fifo.tvalid) begin
							if (drop_frame_reg && LAST_EN) begin
								if (test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_pre_fifo.tlast) begin
									if ((!full && mark_frame_reg) && MARK_WHEN_FULL) begin
										mark_frame_reg <= 1'b0;
										mem[wr_ptr_reg[FIFO_AW - 1:0]] <= mem_wr_data;
										wr_ptr_temp = wr_ptr_reg + 1;
										wr_ptr_reg <= wr_ptr_temp;
										wr_ptr_commit_reg <= wr_ptr_temp;
										wr_ptr_gray_reg <= bin2gray(wr_ptr_temp);
									end
									drop_frame_reg <= 1'b0;
									overflow_reg <= 1'b1;
								end
							end
							else if ((full || mark_frame_reg) && MARK_WHEN_FULL) begin
								drop_frame_reg <= 1'b1;
								mark_frame_reg <= mark_frame_reg || s_frame_reg;
								if (test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_pre_fifo.tlast) begin
									drop_frame_reg <= 1'b0;
									overflow_reg <= 1'b1;
								end
							end
							else begin
								mem[wr_ptr_reg[FIFO_AW - 1:0]] <= mem_wr_data;
								wr_ptr_temp = wr_ptr_reg + 1;
								wr_ptr_reg <= wr_ptr_temp;
								wr_ptr_commit_reg <= wr_ptr_temp;
								wr_ptr_gray_reg <= bin2gray(wr_ptr_temp);
							end
						end
						else if (((!full && !drop_frame_reg) && mark_frame_reg) && MARK_WHEN_FULL) begin
							mark_frame_reg <= 1'b0;
							mem[wr_ptr_reg[FIFO_AW - 1:0]] <= mem_wr_data;
							wr_ptr_temp = wr_ptr_reg + 1;
							wr_ptr_reg <= wr_ptr_temp;
							wr_ptr_commit_reg <= wr_ptr_temp;
							wr_ptr_gray_reg <= bin2gray(wr_ptr_temp);
						end
						if (s_rst_sync) begin
							wr_ptr_reg <= 1'sb0;
							wr_ptr_commit_reg <= 1'sb0;
							wr_ptr_gray_reg <= 1'sb0;
							wr_ptr_sync_commit_reg <= 1'sb0;
							wr_ptr_update_valid_reg <= 1'b0;
							wr_ptr_update_reg <= 1'b0;
						end
						if (s_rst) begin
							wr_ptr_reg <= 1'sb0;
							wr_ptr_commit_reg <= 1'sb0;
							wr_ptr_gray_reg <= 1'sb0;
							wr_ptr_sync_commit_reg <= 1'sb0;
							wr_ptr_update_valid_reg <= 1'b0;
							wr_ptr_update_reg <= 1'b0;
							s_frame_reg <= 1'b0;
							drop_frame_reg <= 1'b0;
							mark_frame_reg <= 1'b0;
							send_frame_reg <= 1'b0;
							overflow_reg <= 1'b0;
							bad_frame_reg <= 1'b0;
							good_frame_reg <= 1'b0;
						end
					end
					always @(posedge s_clk) begin
						rd_ptr_conv_reg <= gray2bin(rd_ptr_gray_sync2_reg);
						s_depth_reg <= wr_ptr_reg - rd_ptr_conv_reg;
						s_depth_commit_reg <= wr_ptr_commit_reg - rd_ptr_conv_reg;
					end
					always @(posedge s_clk) begin
						rd_ptr_gray_sync1_reg <= rd_ptr_gray_reg;
						rd_ptr_gray_sync2_reg <= rd_ptr_gray_sync1_reg;
						wr_ptr_update_ack_sync1_reg <= wr_ptr_update_sync3_reg;
						wr_ptr_update_ack_sync2_reg <= wr_ptr_update_ack_sync1_reg;
						if (s_rst) begin
							rd_ptr_gray_sync1_reg <= 1'sb0;
							rd_ptr_gray_sync2_reg <= 1'sb0;
							wr_ptr_update_ack_sync1_reg <= 1'b0;
							wr_ptr_update_ack_sync2_reg <= 1'b0;
						end
					end
					always @(posedge m_clk) begin
						wr_ptr_gray_sync1_reg <= wr_ptr_gray_reg;
						wr_ptr_gray_sync2_reg <= wr_ptr_gray_sync1_reg;
						if (FRAME_FIFO && (wr_ptr_update_sync2_reg ^ wr_ptr_update_sync3_reg))
							wr_ptr_commit_sync_reg <= wr_ptr_sync_commit_reg;
						wr_ptr_update_sync1_reg <= wr_ptr_update_reg;
						wr_ptr_update_sync2_reg <= wr_ptr_update_sync1_reg;
						wr_ptr_update_sync3_reg <= wr_ptr_update_sync2_reg;
						if (FRAME_FIFO && m_rst_sync)
							wr_ptr_gray_sync1_reg <= 1'sb0;
						if (m_rst) begin
							wr_ptr_gray_sync1_reg <= 1'sb0;
							wr_ptr_gray_sync2_reg <= 1'sb0;
							wr_ptr_commit_sync_reg <= 1'sb0;
							wr_ptr_update_sync1_reg <= 1'b0;
							wr_ptr_update_sync2_reg <= 1'b0;
							wr_ptr_update_sync3_reg <= 1'b0;
						end
					end
					always @(posedge s_clk) begin
						overflow_sync1_reg <= overflow_sync1_reg ^ overflow_reg;
						bad_frame_sync1_reg <= bad_frame_sync1_reg ^ bad_frame_reg;
						good_frame_sync1_reg <= good_frame_sync1_reg ^ good_frame_reg;
						if (s_rst) begin
							overflow_sync1_reg <= 1'b0;
							bad_frame_sync1_reg <= 1'b0;
							good_frame_sync1_reg <= 1'b0;
						end
					end
					always @(posedge m_clk) begin
						overflow_sync2_reg <= overflow_sync1_reg;
						overflow_sync3_reg <= overflow_sync2_reg;
						overflow_sync4_reg <= overflow_sync3_reg;
						bad_frame_sync2_reg <= bad_frame_sync1_reg;
						bad_frame_sync3_reg <= bad_frame_sync2_reg;
						bad_frame_sync4_reg <= bad_frame_sync3_reg;
						good_frame_sync2_reg <= good_frame_sync1_reg;
						good_frame_sync3_reg <= good_frame_sync2_reg;
						good_frame_sync4_reg <= good_frame_sync3_reg;
						if (m_rst) begin
							overflow_sync2_reg <= 1'b0;
							overflow_sync3_reg <= 1'b0;
							overflow_sync4_reg <= 1'b0;
							bad_frame_sync2_reg <= 1'b0;
							bad_frame_sync3_reg <= 1'b0;
							bad_frame_sync4_reg <= 1'b0;
							good_frame_sync2_reg <= 1'b0;
							good_frame_sync3_reg <= 1'b0;
							good_frame_sync4_reg <= 1'b0;
						end
					end
					always @(posedge m_clk) begin
						if (m_axis_tready_pipe) begin
							mem_rd_valid_pipe_reg[RAM_PIPELINE + 0] <= 1'b0;
							m_terminate_frame_reg <= 1'b0;
						end
						begin : sv2v_autoblock_26
							integer j;
							for (j = RAM_PIPELINE + 0; j > 0; j = j - 1)
								begin : sv2v_autoblock_27
									reg [((RAM_PIPELINE + 0) >= 0 ? RAM_PIPELINE + 1 : 1 - (RAM_PIPELINE + 0)) - 1:0] sv2v_tmp_cast;
									sv2v_tmp_cast = ~mem_rd_valid_pipe_reg;
									if (m_axis_tready_pipe || ((sv2v_tmp_cast >> j) != 0)) begin
										mem_rd_valid_pipe_reg[j] <= mem_rd_valid_pipe_reg[j - 1];
										mem_rd_data_pipe_reg[j] <= mem_rd_data_pipe_reg[j - 1];
										mem_rd_valid_pipe_reg[j - 1] <= 1'b0;
									end
								end
						end
						if (m_axis_tready_pipe || (&mem_rd_valid_pipe_reg == 0)) begin
							mem_rd_valid_pipe_reg[0] <= 1'b0;
							mem_rd_data_pipe_reg[0] <= mem[rd_ptr_reg[FIFO_AW - 1:0]];
							if (((!empty && !m_rst_sync) && !m_empty_pipe_reg) && pipe_ready) begin
								mem_rd_valid_pipe_reg[0] <= 1'b1;
								rd_ptr_temp = rd_ptr_reg + 1;
								rd_ptr_reg <= rd_ptr_temp;
								rd_ptr_gray_reg <= bin2gray(rd_ptr_temp);
							end
						end
						if (m_axis_tvalid_pipe && LAST_EN) begin
							if (m_axis_tlast_pipe && m_axis_tready_pipe)
								m_frame_reg <= 1'b0;
							else
								m_frame_reg <= 1'b1;
						end
						if ((m_empty_pipe_reg && (mem_rd_valid_pipe_reg == 0)) && LAST_EN) begin
							if (m_frame_reg) begin
								mem_rd_valid_pipe_reg[RAM_PIPELINE + 0] <= 1'b1;
								m_terminate_frame_reg <= 1'b1;
							end
							m_empty_pipe_reg <= 1'b0;
						end
						if (m_rst_sync && LAST_EN)
							m_empty_pipe_reg <= 1'b1;
						if (m_rst_sync) begin
							rd_ptr_reg <= 1'sb0;
							rd_ptr_gray_reg <= 1'sb0;
						end
						if (m_rst) begin
							rd_ptr_reg <= 1'sb0;
							rd_ptr_gray_reg <= 1'sb0;
							mem_rd_valid_pipe_reg <= 1'sb0;
							m_frame_reg <= 1'b0;
							m_empty_pipe_reg <= 1'b0;
							m_terminate_frame_reg <= 1'b0;
						end
					end
					always @(posedge m_clk) begin
						wr_ptr_conv_reg <= gray2bin(wr_ptr_gray_sync2_reg);
						m_depth_reg <= wr_ptr_conv_reg - rd_ptr_reg;
						m_depth_commit_reg <= (FRAME_FIFO ? wr_ptr_commit_sync_reg - rd_ptr_reg : wr_ptr_conv_reg - rd_ptr_reg);
					end
					if (!OUTPUT_FIFO_EN) begin : genblk24
						assign pipe_ready = 1'b1;
						assign m_axis_tready_pipe = m_axis_tready_out;
						assign m_axis_tvalid_out = m_axis_tvalid_pipe;
						assign m_axis_tdata_out = m_axis_tdata_pipe;
						assign m_axis_tkeep_out = m_axis_tkeep_pipe;
						assign m_axis_tstrb_out = m_axis_tstrb_pipe;
						assign m_axis_tlast_out = m_axis_tlast_pipe;
						assign m_axis_tid_out = m_axis_tid_pipe;
						assign m_axis_tdest_out = m_axis_tdest_pipe;
						assign m_axis_tuser_out = m_axis_tuser_pipe;
					end
					else begin : output_fifo
						reg [DATA_W - 1:0] m_axis_tdata_reg = 1'sb0;
						reg [KEEP_W - 1:0] m_axis_tkeep_reg = 1'sb0;
						reg [KEEP_W - 1:0] m_axis_tstrb_reg = 1'sb0;
						reg m_axis_tvalid_reg = 1'b0;
						reg m_axis_tlast_reg = 1'b0;
						reg [ID_W - 1:0] m_axis_tid_reg = 1'sb0;
						reg [DEST_W - 1:0] m_axis_tdest_reg = 1'sb0;
						reg [USER_W - 1:0] m_axis_tuser_reg = 1'sb0;
						reg [OUTPUT_FIFO_AW + 0:0] out_fifo_wr_ptr_reg = 0;
						reg [OUTPUT_FIFO_AW + 0:0] out_fifo_rd_ptr_reg = 0;
						reg out_fifo_half_full_reg = 1'b0;
						wire out_fifo_full = out_fifo_wr_ptr_reg == (out_fifo_rd_ptr_reg ^ {1'b1, {OUTPUT_FIFO_AW {1'b0}}});
						wire out_fifo_empty = out_fifo_wr_ptr_reg == out_fifo_rd_ptr_reg;
						(* ram_style = "distributed", ramstyle = "no_rw_check, mlab" *) reg [DATA_W - 1:0] out_fifo_tdata [0:(2 ** OUTPUT_FIFO_AW) - 1];
						(* ram_style = "distributed", ramstyle = "no_rw_check, mlab" *) reg [KEEP_W - 1:0] out_fifo_tkeep [0:(2 ** OUTPUT_FIFO_AW) - 1];
						(* ram_style = "distributed", ramstyle = "no_rw_check, mlab" *) reg [KEEP_W - 1:0] out_fifo_tstrb [0:(2 ** OUTPUT_FIFO_AW) - 1];
						(* ram_style = "distributed", ramstyle = "no_rw_check, mlab" *) reg out_fifo_tlast [0:(2 ** OUTPUT_FIFO_AW) - 1];
						(* ram_style = "distributed", ramstyle = "no_rw_check, mlab" *) reg [ID_W - 1:0] out_fifo_tid [0:(2 ** OUTPUT_FIFO_AW) - 1];
						(* ram_style = "distributed", ramstyle = "no_rw_check, mlab" *) reg [DEST_W - 1:0] out_fifo_tdest [0:(2 ** OUTPUT_FIFO_AW) - 1];
						(* ram_style = "distributed", ramstyle = "no_rw_check, mlab" *) reg [USER_W - 1:0] out_fifo_tuser [0:(2 ** OUTPUT_FIFO_AW) - 1];
						assign pipe_ready = !out_fifo_half_full_reg;
						assign m_axis_tready_pipe = 1'b1;
						assign m_axis_tdata_out = m_axis_tdata_reg;
						assign m_axis_tkeep_out = (KEEP_EN ? m_axis_tkeep_reg : {KEEP_W {1'sb1}});
						assign m_axis_tstrb_out = (STRB_EN ? m_axis_tkeep_reg : m_axis_tkeep_out);
						assign m_axis_tvalid_out = m_axis_tvalid_reg;
						assign m_axis_tlast_out = (LAST_EN ? m_axis_tlast_reg : 1'b1);
						assign m_axis_tid_out = (ID_EN ? m_axis_tid_reg : {ID_W {1'sb0}});
						assign m_axis_tdest_out = (DEST_EN ? m_axis_tdest_reg : {DEST_W {1'sb0}});
						assign m_axis_tuser_out = (USER_EN ? m_axis_tuser_reg : {USER_W {1'sb0}});
						always @(posedge m_clk) begin
							m_axis_tvalid_reg <= m_axis_tvalid_reg && !m_axis_tready_out;
							out_fifo_half_full_reg <= $unsigned(out_fifo_wr_ptr_reg - out_fifo_rd_ptr_reg) >= (2 ** (OUTPUT_FIFO_AW - 1));
							if (!out_fifo_full && m_axis_tvalid_pipe) begin
								out_fifo_tdata[out_fifo_wr_ptr_reg[OUTPUT_FIFO_AW - 1:0]] <= m_axis_tdata_pipe;
								out_fifo_tkeep[out_fifo_wr_ptr_reg[OUTPUT_FIFO_AW - 1:0]] <= m_axis_tkeep_pipe;
								out_fifo_tstrb[out_fifo_wr_ptr_reg[OUTPUT_FIFO_AW - 1:0]] <= m_axis_tstrb_pipe;
								out_fifo_tlast[out_fifo_wr_ptr_reg[OUTPUT_FIFO_AW - 1:0]] <= m_axis_tlast_pipe;
								out_fifo_tid[out_fifo_wr_ptr_reg[OUTPUT_FIFO_AW - 1:0]] <= m_axis_tid_pipe;
								out_fifo_tdest[out_fifo_wr_ptr_reg[OUTPUT_FIFO_AW - 1:0]] <= m_axis_tdest_pipe;
								out_fifo_tuser[out_fifo_wr_ptr_reg[OUTPUT_FIFO_AW - 1:0]] <= m_axis_tuser_pipe;
								out_fifo_wr_ptr_reg <= out_fifo_wr_ptr_reg + 1;
							end
							if (!out_fifo_empty && (!m_axis_tvalid_reg || m_axis_tready_out)) begin
								m_axis_tdata_reg <= out_fifo_tdata[out_fifo_rd_ptr_reg[OUTPUT_FIFO_AW - 1:0]];
								m_axis_tkeep_reg <= out_fifo_tkeep[out_fifo_rd_ptr_reg[OUTPUT_FIFO_AW - 1:0]];
								m_axis_tstrb_reg <= out_fifo_tstrb[out_fifo_rd_ptr_reg[OUTPUT_FIFO_AW - 1:0]];
								m_axis_tvalid_reg <= 1'b1;
								m_axis_tlast_reg <= out_fifo_tlast[out_fifo_rd_ptr_reg[OUTPUT_FIFO_AW - 1:0]];
								m_axis_tid_reg <= out_fifo_tid[out_fifo_rd_ptr_reg[OUTPUT_FIFO_AW - 1:0]];
								m_axis_tdest_reg <= out_fifo_tdest[out_fifo_rd_ptr_reg[OUTPUT_FIFO_AW - 1:0]];
								m_axis_tuser_reg <= out_fifo_tuser[out_fifo_rd_ptr_reg[OUTPUT_FIFO_AW - 1:0]];
								out_fifo_rd_ptr_reg <= out_fifo_rd_ptr_reg + 1;
							end
							if (m_rst) begin
								out_fifo_wr_ptr_reg <= 0;
								out_fifo_rd_ptr_reg <= 0;
								m_axis_tvalid_reg <= 1'b0;
							end
						end
					end
					if (PAUSE_EN) begin : pause
						reg pause_reg = 1'b0;
						reg pause_frame_reg = 1'b0;
						wire s_pause_req_sync;
						taxi_sync_signal #(
							.WIDTH(1),
							.N(2)
						) pause_req_sync_inst(
							.clk(m_clk),
							.in(s_pause_req),
							.out(s_pause_req_sync)
						);
						taxi_sync_signal #(
							.WIDTH(1),
							.N(2)
						) pause_ack_sync_inst(
							.clk(s_clk),
							.in(pause_reg),
							.out(s_pause_ack)
						);
						assign m_axis_tready_out = test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tready && !pause_reg;
						assign test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tvalid = m_axis_tvalid_out && !pause_reg;
						assign test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tdata = m_axis_tdata_out;
						assign test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tkeep = m_axis_tkeep_out;
						assign test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tstrb = m_axis_tstrb_out;
						assign test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tlast = m_axis_tlast_out;
						assign test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tid = m_axis_tid_out;
						assign test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tdest = m_axis_tdest_out;
						assign test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tuser = m_axis_tuser_out;
						assign m_pause_ack = pause_reg;
						always @(posedge m_clk) begin
							if (FRAME_PAUSE) begin
								if (pause_reg)
									pause_reg <= m_pause_req || s_pause_req_sync;
								else if (m_axis_tvalid_out) begin
									pause_frame_reg <= 1'b1;
									if (test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tready && test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tlast) begin
										pause_frame_reg <= 1'b0;
										pause_reg <= m_pause_req || s_pause_req_sync;
									end
								end
								else if (!pause_frame_reg)
									pause_reg <= m_pause_req || s_pause_req_sync;
							end
							else
								pause_reg <= m_pause_req || s_pause_req_sync;
							if (m_rst) begin
								pause_frame_reg <= 1'b0;
								pause_reg <= 1'b0;
							end
						end
					end
					else begin : genblk25
						assign m_axis_tready_out = test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tready;
						assign test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tvalid = m_axis_tvalid_out;
						assign test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tdata = m_axis_tdata_out;
						assign test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tkeep = m_axis_tkeep_out;
						assign test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tstrb = m_axis_tstrb_out;
						assign test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tlast = m_axis_tlast_out;
						assign test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tid = m_axis_tid_out;
						assign test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tdest = m_axis_tdest_out;
						assign test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tuser = m_axis_tuser_out;
						assign s_pause_ack = 1'b0;
						assign m_pause_ack = 1'b0;
					end
				end
				assign fifo_inst.s_clk = s_clk;
				assign fifo_inst.s_rst = s_rst;
				assign fifo_inst.m_clk = m_clk;
				assign fifo_inst.m_rst = m_rst;
				assign fifo_inst.s_pause_req = s_pause_req;
				assign s_pause_ack = fifo_inst.s_pause_ack;
				assign fifo_inst.m_pause_req = m_pause_req;
				assign m_pause_ack = fifo_inst.m_pause_ack;
				assign s_status_depth = fifo_inst.s_status_depth;
				assign s_status_depth_commit = fifo_inst.s_status_depth_commit;
				assign s_status_overflow = fifo_inst.s_status_overflow;
				assign s_status_bad_frame = fifo_inst.s_status_bad_frame;
				assign s_status_good_frame = fifo_inst.s_status_good_frame;
				assign m_status_depth = fifo_inst.m_status_depth;
				assign m_status_depth_commit = fifo_inst.m_status_depth_commit;
				assign m_status_overflow = fifo_inst.m_status_overflow;
				assign m_status_bad_frame = fifo_inst.m_status_bad_frame;
				assign m_status_good_frame = fifo_inst.m_status_good_frame;
				if (1) begin : post_fifo_adapter_inst
					wire clk;
					wire rst;
					localparam S_DATA_W = _param_A087B_DATA_W;
					localparam [0:0] S_KEEP_EN = _param_A087B_KEEP_EN;
					localparam S_KEEP_W = _param_A087B_KEEP_W;
					localparam [0:0] STRB_EN = _param_A087B_STRB_EN && _param_330AD_STRB_EN;
					localparam [0:0] LAST_EN = _param_A087B_LAST_EN;
					localparam [0:0] ID_EN = _param_A087B_ID_EN && _param_330AD_ID_EN;
					localparam ID_W = _param_A087B_ID_W;
					localparam [0:0] DEST_EN = _param_A087B_DEST_EN && _param_330AD_DEST_EN;
					localparam DEST_W = _param_A087B_DEST_W;
					localparam [0:0] USER_EN = _param_A087B_USER_EN && _param_330AD_USER_EN;
					localparam USER_W = _param_A087B_USER_W;
					localparam M_DATA_W = _param_330AD_DATA_W;
					localparam [0:0] M_KEEP_EN = _param_330AD_KEEP_EN;
					localparam M_KEEP_W = _param_330AD_KEEP_W;
					localparam S_BYTE_LANES = (S_KEEP_EN ? S_KEEP_W : 1);
					localparam M_BYTE_LANES = (M_KEEP_EN ? M_KEEP_W : 1);
					localparam S_BYTE_SIZE = S_DATA_W / S_BYTE_LANES;
					localparam M_BYTE_SIZE = M_DATA_W / M_BYTE_LANES;
					if ((S_BYTE_SIZE * S_BYTE_LANES) != S_DATA_W) begin : genblk1
						initial begin
							$display("Fatal [elaboration] /home/enio/Projects/openENOC/libs/taxi/src/axis/rtl/taxi_axis_adapter.sv:61:5 - taxi_axis_adapter.genblk1\n msg: ", "Error: input data width not evenly divisible (instance %m)");
							$finish(0);
						end
					end
					if ((M_BYTE_SIZE * M_BYTE_LANES) != M_DATA_W) begin : genblk2
						initial begin
							$display("Fatal [elaboration] /home/enio/Projects/openENOC/libs/taxi/src/axis/rtl/taxi_axis_adapter.sv:64:5 - taxi_axis_adapter.genblk2\n msg: ", "Error: output data width not evenly divisible (instance %m)");
							$finish(0);
						end
					end
					if (S_BYTE_SIZE != M_BYTE_SIZE) begin : genblk3
						initial begin
							$display("Fatal [elaboration] /home/enio/Projects/openENOC/libs/taxi/src/axis/rtl/taxi_axis_adapter.sv:67:5 - taxi_axis_adapter.genblk3\n msg: ", "Error: byte size mismatch (instance %m)");
							$finish(0);
						end
					end
					wire [S_KEEP_W - 1:0] s_axis_tkeep_int = (S_KEEP_EN ? test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tkeep : {_param_A087B_KEEP_W {1'sb1}});
					if (M_BYTE_LANES == S_BYTE_LANES) begin : bypass
						assign test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tready = test_openenoc_eth_adapter.uut.fifo_b2a_m_axis.tready;
						assign test_openenoc_eth_adapter.uut.fifo_b2a_m_axis.tdata = test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tdata;
						assign test_openenoc_eth_adapter.uut.fifo_b2a_m_axis.tkeep = (M_KEEP_EN && S_KEEP_EN ? test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tkeep : {_param_330AD_KEEP_W {1'sb1}});
						assign test_openenoc_eth_adapter.uut.fifo_b2a_m_axis.tstrb = (STRB_EN ? test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tstrb : test_openenoc_eth_adapter.uut.fifo_b2a_m_axis.tkeep);
						assign test_openenoc_eth_adapter.uut.fifo_b2a_m_axis.tvalid = test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tvalid;
						assign test_openenoc_eth_adapter.uut.fifo_b2a_m_axis.tlast = (LAST_EN ? test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tlast : 1'b1);
						assign test_openenoc_eth_adapter.uut.fifo_b2a_m_axis.tid = (ID_EN ? test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tid : {_param_330AD_ID_W {1'sb0}});
						assign test_openenoc_eth_adapter.uut.fifo_b2a_m_axis.tdest = (DEST_EN ? test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tdest : {_param_330AD_DEST_W {1'sb0}});
						assign test_openenoc_eth_adapter.uut.fifo_b2a_m_axis.tuser = (USER_EN ? test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tuser : {_param_330AD_USER_W {1'sb0}});
					end
					else if (M_BYTE_LANES > S_BYTE_LANES) begin : upsize
						localparam SEG_COUNT = M_BYTE_LANES / S_BYTE_LANES;
						localparam SEG_DATA_W = M_DATA_W / SEG_COUNT;
						localparam SEG_KEEP_W = M_BYTE_LANES / SEG_COUNT;
						localparam CL_SEG_COUNT = $clog2(SEG_COUNT);
						reg [CL_SEG_COUNT - 1:0] seg_reg = 1'sb0;
						reg [S_DATA_W - 1:0] s_axis_tdata_reg = 1'sb0;
						reg [S_KEEP_W - 1:0] s_axis_tkeep_reg = 1'sb0;
						reg [S_KEEP_W - 1:0] s_axis_tstrb_reg = 1'sb0;
						reg s_axis_tvalid_reg = 1'b0;
						reg s_axis_tlast_reg = 1'b0;
						reg [ID_W - 1:0] s_axis_tid_reg = 1'sb0;
						reg [DEST_W - 1:0] s_axis_tdest_reg = 1'sb0;
						reg [USER_W - 1:0] s_axis_tuser_reg = 1'sb0;
						reg [M_DATA_W - 1:0] m_axis_tdata_reg = 1'sb0;
						reg [M_KEEP_W - 1:0] m_axis_tkeep_reg = 1'sb0;
						reg [M_KEEP_W - 1:0] m_axis_tstrb_reg = 1'sb0;
						reg m_axis_tvalid_reg = 1'b0;
						reg m_axis_tlast_reg = 1'b0;
						reg [ID_W - 1:0] m_axis_tid_reg = 1'sb0;
						reg [DEST_W - 1:0] m_axis_tdest_reg = 1'sb0;
						reg [USER_W - 1:0] m_axis_tuser_reg = 1'sb0;
						assign test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tready = !s_axis_tvalid_reg;
						assign test_openenoc_eth_adapter.uut.fifo_b2a_m_axis.tdata = m_axis_tdata_reg;
						assign test_openenoc_eth_adapter.uut.fifo_b2a_m_axis.tkeep = (M_KEEP_EN ? m_axis_tkeep_reg : {_param_330AD_KEEP_W {1'sb1}});
						assign test_openenoc_eth_adapter.uut.fifo_b2a_m_axis.tstrb = (STRB_EN ? m_axis_tstrb_reg : test_openenoc_eth_adapter.uut.fifo_b2a_m_axis.tkeep);
						assign test_openenoc_eth_adapter.uut.fifo_b2a_m_axis.tvalid = m_axis_tvalid_reg;
						assign test_openenoc_eth_adapter.uut.fifo_b2a_m_axis.tlast = (LAST_EN ? m_axis_tlast_reg : 1'b1);
						assign test_openenoc_eth_adapter.uut.fifo_b2a_m_axis.tid = (ID_EN ? m_axis_tid_reg : {_param_330AD_ID_W {1'sb0}});
						assign test_openenoc_eth_adapter.uut.fifo_b2a_m_axis.tdest = (DEST_EN ? m_axis_tdest_reg : {_param_330AD_DEST_W {1'sb0}});
						assign test_openenoc_eth_adapter.uut.fifo_b2a_m_axis.tuser = (USER_EN ? m_axis_tuser_reg : {_param_330AD_USER_W {1'sb0}});
						always @(posedge clk) begin
							m_axis_tvalid_reg <= m_axis_tvalid_reg && !test_openenoc_eth_adapter.uut.fifo_b2a_m_axis.tready;
							if (!m_axis_tvalid_reg || test_openenoc_eth_adapter.uut.fifo_b2a_m_axis.tready) begin
								if (seg_reg == 0) begin
									m_axis_tdata_reg[seg_reg * SEG_DATA_W+:SEG_DATA_W] <= (s_axis_tvalid_reg ? s_axis_tdata_reg : test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tdata);
									begin : sv2v_autoblock_28
										reg [M_KEEP_W - 1:0] sv2v_tmp_cast;
										sv2v_tmp_cast = (s_axis_tvalid_reg ? s_axis_tkeep_reg : s_axis_tkeep_int);
										m_axis_tkeep_reg <= sv2v_tmp_cast;
									end
									begin : sv2v_autoblock_29
										reg [M_KEEP_W - 1:0] sv2v_tmp_cast_1;
										sv2v_tmp_cast_1 = (s_axis_tvalid_reg ? s_axis_tstrb_reg : test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tstrb);
										m_axis_tstrb_reg <= sv2v_tmp_cast_1;
									end
								end
								else begin
									m_axis_tdata_reg[seg_reg * SEG_DATA_W+:SEG_DATA_W] <= test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tdata;
									m_axis_tkeep_reg[seg_reg * SEG_KEEP_W+:SEG_KEEP_W] <= s_axis_tkeep_int;
									m_axis_tstrb_reg[seg_reg * SEG_KEEP_W+:SEG_KEEP_W] <= test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tstrb;
								end
								m_axis_tlast_reg <= (s_axis_tvalid_reg ? s_axis_tlast_reg : test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tlast);
								m_axis_tid_reg <= (s_axis_tvalid_reg ? s_axis_tid_reg : test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tid);
								m_axis_tdest_reg <= (s_axis_tvalid_reg ? s_axis_tdest_reg : test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tdest);
								m_axis_tuser_reg <= (s_axis_tvalid_reg ? s_axis_tuser_reg : test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tuser);
								if (s_axis_tvalid_reg) begin
									s_axis_tvalid_reg <= 1'b0;
									begin : sv2v_autoblock_30
										reg signed [CL_SEG_COUNT - 1:0] sv2v_tmp_cast;
										sv2v_tmp_cast = SEG_COUNT - 1;
										if ((LAST_EN && s_axis_tlast_reg) || (seg_reg == sv2v_tmp_cast)) begin
											seg_reg <= 1'sb0;
											m_axis_tvalid_reg <= 1'b1;
										end
										else
											seg_reg <= seg_reg + 1;
									end
								end
								else if (test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tvalid) begin : sv2v_autoblock_31
									reg signed [CL_SEG_COUNT - 1:0] sv2v_tmp_cast;
									sv2v_tmp_cast = SEG_COUNT - 1;
									if ((LAST_EN && test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tlast) || (seg_reg == sv2v_tmp_cast)) begin
										seg_reg <= 1'sb0;
										m_axis_tvalid_reg <= 1'b1;
									end
									else
										seg_reg <= seg_reg + 1;
								end
							end
							else if (test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tvalid && test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tready) begin
								s_axis_tdata_reg <= test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tdata;
								s_axis_tkeep_reg <= s_axis_tkeep_int;
								s_axis_tstrb_reg <= test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tstrb;
								s_axis_tvalid_reg <= 1'b1;
								s_axis_tlast_reg <= test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tlast;
								s_axis_tid_reg <= test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tid;
								s_axis_tdest_reg <= test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tdest;
								s_axis_tuser_reg <= test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tuser;
							end
							if (rst) begin
								seg_reg <= 1'sb0;
								s_axis_tvalid_reg <= 1'b0;
								m_axis_tvalid_reg <= 1'b0;
							end
						end
					end
					else begin : downsize
						localparam SEG_COUNT = S_BYTE_LANES / M_BYTE_LANES;
						localparam SEG_DATA_W = S_DATA_W / SEG_COUNT;
						localparam SEG_KEEP_W = S_BYTE_LANES / SEG_COUNT;
						reg [S_DATA_W - 1:0] s_axis_tdata_reg = 1'sb0;
						reg [S_KEEP_W - 1:0] s_axis_tkeep_reg = 1'sb0;
						reg [S_KEEP_W - 1:0] s_axis_tstrb_reg = 1'sb0;
						reg s_axis_tvalid_reg = 1'b0;
						reg s_axis_tlast_reg = 1'b0;
						reg [ID_W - 1:0] s_axis_tid_reg = 1'sb0;
						reg [DEST_W - 1:0] s_axis_tdest_reg = 1'sb0;
						reg [USER_W - 1:0] s_axis_tuser_reg = 1'sb0;
						reg [M_DATA_W - 1:0] m_axis_tdata_reg = 1'sb0;
						reg [M_KEEP_W - 1:0] m_axis_tkeep_reg = 1'sb0;
						reg [M_KEEP_W - 1:0] m_axis_tstrb_reg = 1'sb0;
						reg m_axis_tvalid_reg = 1'b0;
						reg m_axis_tlast_reg = 1'b0;
						reg [ID_W - 1:0] m_axis_tid_reg = 1'sb0;
						reg [DEST_W - 1:0] m_axis_tdest_reg = 1'sb0;
						reg [USER_W - 1:0] m_axis_tuser_reg = 1'sb0;
						assign test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tready = !s_axis_tvalid_reg;
						assign test_openenoc_eth_adapter.uut.fifo_b2a_m_axis.tdata = m_axis_tdata_reg;
						assign test_openenoc_eth_adapter.uut.fifo_b2a_m_axis.tkeep = (M_KEEP_EN ? m_axis_tkeep_reg : {_param_330AD_KEEP_W {1'sb1}});
						assign test_openenoc_eth_adapter.uut.fifo_b2a_m_axis.tstrb = (STRB_EN ? m_axis_tstrb_reg : test_openenoc_eth_adapter.uut.fifo_b2a_m_axis.tkeep);
						assign test_openenoc_eth_adapter.uut.fifo_b2a_m_axis.tvalid = m_axis_tvalid_reg;
						assign test_openenoc_eth_adapter.uut.fifo_b2a_m_axis.tlast = m_axis_tlast_reg;
						assign test_openenoc_eth_adapter.uut.fifo_b2a_m_axis.tid = (ID_EN ? m_axis_tid_reg : {_param_330AD_ID_W {1'sb0}});
						assign test_openenoc_eth_adapter.uut.fifo_b2a_m_axis.tdest = (DEST_EN ? m_axis_tdest_reg : {_param_330AD_DEST_W {1'sb0}});
						assign test_openenoc_eth_adapter.uut.fifo_b2a_m_axis.tuser = (USER_EN ? m_axis_tuser_reg : {_param_330AD_USER_W {1'sb0}});
						always @(posedge clk) begin
							m_axis_tvalid_reg <= m_axis_tvalid_reg && !test_openenoc_eth_adapter.uut.fifo_b2a_m_axis.tready;
							if (!m_axis_tvalid_reg || test_openenoc_eth_adapter.uut.fifo_b2a_m_axis.tready) begin
								begin : sv2v_autoblock_32
									reg [M_DATA_W - 1:0] sv2v_tmp_cast;
									sv2v_tmp_cast = (s_axis_tvalid_reg ? s_axis_tdata_reg : test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tdata);
									m_axis_tdata_reg <= sv2v_tmp_cast;
								end
								begin : sv2v_autoblock_33
									reg [M_KEEP_W - 1:0] sv2v_tmp_cast_1;
									sv2v_tmp_cast_1 = (s_axis_tvalid_reg ? s_axis_tkeep_reg : s_axis_tkeep_int);
									m_axis_tkeep_reg <= sv2v_tmp_cast_1;
								end
								begin : sv2v_autoblock_34
									reg [M_KEEP_W - 1:0] sv2v_tmp_cast_2;
									sv2v_tmp_cast_2 = (s_axis_tvalid_reg ? s_axis_tstrb_reg : test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tstrb);
									m_axis_tstrb_reg <= sv2v_tmp_cast_2;
								end
								m_axis_tlast_reg <= 1'b0;
								m_axis_tid_reg <= (s_axis_tvalid_reg ? s_axis_tid_reg : test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tid);
								m_axis_tdest_reg <= (s_axis_tvalid_reg ? s_axis_tdest_reg : test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tdest);
								m_axis_tuser_reg <= (s_axis_tvalid_reg ? s_axis_tuser_reg : test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tuser);
								if (s_axis_tvalid_reg) begin
									s_axis_tdata_reg <= s_axis_tdata_reg >> SEG_DATA_W;
									s_axis_tkeep_reg <= s_axis_tkeep_reg >> SEG_KEEP_W;
									s_axis_tstrb_reg <= s_axis_tstrb_reg >> SEG_KEEP_W;
									m_axis_tvalid_reg <= 1'b1;
									if ((s_axis_tkeep_reg >> SEG_KEEP_W) == 0) begin
										s_axis_tvalid_reg <= 1'b0;
										m_axis_tlast_reg <= s_axis_tlast_reg;
									end
								end
								else if (test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tvalid && test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tready) begin
									s_axis_tdata_reg <= test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tdata >> SEG_DATA_W;
									s_axis_tkeep_reg <= s_axis_tkeep_int >> SEG_KEEP_W;
									s_axis_tstrb_reg <= test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tstrb >> SEG_KEEP_W;
									s_axis_tlast_reg <= test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tlast;
									s_axis_tid_reg <= test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tid;
									s_axis_tdest_reg <= test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tdest;
									s_axis_tuser_reg <= test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tuser;
									m_axis_tvalid_reg <= 1'b1;
									if (S_KEEP_EN && ((s_axis_tkeep_int >> SEG_KEEP_W) == 0)) begin
										s_axis_tvalid_reg <= 1'b0;
										m_axis_tlast_reg <= test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tlast;
									end
									else
										s_axis_tvalid_reg <= 1'b1;
								end
							end
							else if (test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tvalid && test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tready) begin
								s_axis_tdata_reg <= test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tdata;
								s_axis_tkeep_reg <= s_axis_tkeep_int;
								s_axis_tstrb_reg <= test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tstrb;
								s_axis_tvalid_reg <= 1'b1;
								s_axis_tlast_reg <= test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tlast;
								s_axis_tid_reg <= test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tid;
								s_axis_tdest_reg <= test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tdest;
								s_axis_tuser_reg <= test_openenoc_eth_adapter.uut.fifo_b2a_inst.axis_post_fifo.tuser;
							end
							if (rst) begin
								s_axis_tvalid_reg <= 1'b0;
								m_axis_tvalid_reg <= 1'b0;
							end
						end
					end
				end
				assign post_fifo_adapter_inst.clk = m_clk;
				assign post_fifo_adapter_inst.rst = m_rst;
			end
			assign fifo_b2a_inst.s_clk = test_openenoc_eth_adapter.eth_b.clk;
			assign fifo_b2a_inst.s_rst = test_openenoc_eth_adapter.eth_b.rst;
			assign fifo_b2a_inst.m_clk = test_openenoc_eth_adapter.eth_a.clk;
			assign fifo_b2a_inst.m_rst = test_openenoc_eth_adapter.eth_a.rst;
			assign fifo_b2a_inst.s_pause_req = 1'b0;
			assign fifo_b2a_inst.m_pause_req = 1'b0;
		end
	endgenerate
endmodule
`resetall