// SPDX-FileCopyrightText: 2026 Amina Tankovic
// SPDX-License-Identifier: AGPL-3.0-or-later

`timescale 1ns / 1ps
`define NULL 0

// Based on pcapwriter_10gb by Chris Shucksmith (https://github.com/shuckc/verilog-utils/blob/master/pcap/pcapwriter_10gbmac.v)
// Description: Write packets from an Avalon-ST or AXI4-Stream interfaces to the PCAP file

/* verilator lint_off PROCASSINIT */
module pcapwriter #
(
    parameter PCAP_FILENAME = "none",
    parameter PCAP_BUFFSZ   = 9000,
    parameter SIGNAL_TYPE   = "avalon",
    parameter DATA_WIDTH    = 512,
    parameter CLOCK_PERIOD  = 2560, //in picoseconds
    parameter KEEP_WIDTH    = DATA_WIDTH / 8
)
(
    input  logic        clk,
    input  logic        rst,

    avalon_if.in        to_writer_avalon,           // Avalon-ST interface input
    taxi_axis_if.snk    to_writer_axis,             // AXI4-Stream interface input

    output logic [7:0]  pktcount = 0
);
    logic [31:0] global_header [0:5];               // 6*32bit words = 24 bytes
    logic [31:0] packet_header [0:3];               // 4*32bit words = 16 bytes
    logic [7:0]  packet_buffer [0:PCAP_BUFFSZ];

    integer file = 0;
    integer r    = 0;
    integer eof  = 0;
    integer i    = 0;
    integer pktSz  = 0;
    integer diskSz = 0;
    integer newPkt = 0;
    integer bytes_data_out = DATA_WIDTH / 8;
    longint cnt_clk;
    integer timestamp =  32'd0;

    logic [31:0] pcap_buffsz32 = PCAP_BUFFSZ;

    initial begin
        // open pcap file
    	if (PCAP_FILENAME == "none") begin
	        $display("pcap filename parameter not set");
	        $finish;
	    end

        file = $fopen(PCAP_FILENAME, "wb");
	    if (file == `NULL) begin
	        $display("can't open pcap file %s for writing!", PCAP_FILENAME);
	        $finish;
	    end

	    // Write Global header
        $fwrite(file, "%u", 32'ha1b23c4d);  // magic number - little endian, nanoseconds
        $fwrite(file, "%u", 32'h00040002);  // major version (2), minor version (4)
        $fwrite(file, "%u", 32'd00000000);  // .thiszone - GMT to local correction (0)
        $fwrite(file, "%u", 32'd00000000);  // .sigfigs - Accuracy of timestamps (0)
        $fwrite(file, "%u", 32'h00040000);
        $fwrite(file, "%u", 32'h00000001);  // .network - data link type (Ethernet = 1)
    end

    logic [7:0] x = packet_buffer[i];
    logic finished = 0;
    logic first_sop = 0;

    // timer in picoseconds
    always_ff @(posedge clk)
    begin
        if (rst == 1) begin
	    cnt_clk <= 64'd0;
        end else begin
            cnt_clk <= cnt_clk + $bits(cnt_clk)'(CLOCK_PERIOD);
        end
    end

    /* verilator lint_off BLKSEQ */
    always @(posedge clk)
    begin
        if (to_writer_avalon.valid || to_writer_axis.tvalid) begin
            if (!first_sop) begin
	            if (to_writer_avalon.sop || to_writer_axis.tvalid) begin  // for AXI4-Stream interface - first occurence of data valid signal
                    timestamp = int'(cnt_clk/1000);
                    first_sop <= 1;
                end
	        end

            // Packet data
            for (i = 0; i < bytes_data_out; i = i + 1) begin
                if (SIGNAL_TYPE == "avalon") begin
                    packet_buffer[pktSz+bytes_data_out-1-i] = to_writer_avalon.data[i*8+:8];
                end else begin
                    packet_buffer[pktSz+bytes_data_out-1-i] = to_writer_axis.tdata[(bytes_data_out-1-i)*8+:8];
                end
            end

	    	if (SIGNAL_TYPE == "avalon") begin
                pktSz = ((to_writer_avalon.eop) ? bytes_data_out - int'(to_writer_avalon.empty) : bytes_data_out) + pktSz;
            end else begin
                pktSz = ((to_writer_axis.tlast) ? bytes_data_out - (KEEP_WIDTH-$countones(to_writer_axis.tkeep)): bytes_data_out) + pktSz;
	        end

    	    if (to_writer_avalon.eop || to_writer_axis.tlast) begin
                $fwrite(file, "%u%u%u%u", 32'd0, timestamp, pktSz, pktSz);
	            for (i = 0; i < pktSz; i = i + 1) begin
                    $fwrite(file, "%c", packet_buffer[i]);
	            end
	            $fflush(file);
	            pktSz = 0;
                first_sop <= 0;
            end
    	end
    end
    /* verilator lint_on BLKSEQ */

    assign to_writer_avalon.ready = 1'b1;
    assign to_writer_axis.tready = 1'b1;
endmodule
/* verilator lint_on PROCASSINIT */
