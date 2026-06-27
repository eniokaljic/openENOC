// SPDX-FileCopyrightText: 2026 Enio Kaljic
// SPDX-License-Identifier: AGPL-3.0-or-later

`resetall
`timescale 1ns / 1ps
`default_nettype none

/*
 * PCAP reader/writer testbench
 */
module test_traffic #
(
    /* verilator lint_off WIDTHTRUNC */
    parameter DATA_WIDTH = 8,
    parameter CLOCK_PERIOD = 10000,
    parameter PCAP_IN_FILENAME = "test1.pcap",
    parameter PCAP_OUT_FILENAME = "output.pcap"
    /* verilator lint_on WIDTHTRUNC */
) 
();
    logic clk;
    logic rst;
    logic pcapfinished;

    avalon_if #(.DATA_WIDTH(DATA_WIDTH)) avst(.clk(clk),.rst(rst));
    taxi_axis_if #(.DATA_W(DATA_WIDTH)) axis();

    pcapreader #(
        .PCAP_FILENAME(PCAP_IN_FILENAME),
        .SIGNAL_TYPE("axisif"),
        .DATA_WIDTH(DATA_WIDTH),
        .CLOCK_PERIOD(CLOCK_PERIOD)
    ) uut_pcapreader (
        .clk(clk),
        .rst(rst),
        .pktcount(),
        .newpkt(),
        .pcapfinished(pcapfinished),

        .from_reader_avalon(avst),
        .from_reader_axis(axis)
    );

    pcapwriter #(
        .PCAP_FILENAME(PCAP_OUT_FILENAME),
        .SIGNAL_TYPE("axisif"),
        .DATA_WIDTH(DATA_WIDTH),
        .CLOCK_PERIOD(CLOCK_PERIOD)
    ) uut_pcapwriter (
        .clk(clk),
        .rst(rst),

        .to_writer_avalon(avst),
        .to_writer_axis(axis),

        .pktcount()
    );
endmodule

`resetall
