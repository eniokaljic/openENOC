// SPDX-FileCopyrightText: 2026 Enio Kaljic
// SPDX-License-Identifier: CERN-OHL-S-2.0

`resetall
`timescale 1ns / 1ps
`default_nettype none

/* Native openENOC request/acknowledgement CPUIF. */
interface openenoc_cpuif_if #(
    parameter int unsigned ADDR_W = 32,
    parameter int unsigned DATA_W = 32
);
    logic req;
    logic [ADDR_W-1:0] addr;
    logic req_is_wr;
    logic [DATA_W-1:0] wr_data;
    logic [DATA_W-1:0] wr_biten;

    logic wr_ack;
    logic wr_err;
    logic rd_ack;
    logic rd_err;
    logic [DATA_W-1:0] rd_data;

    modport mst(
        output req,
        output addr,
        output req_is_wr,
        output wr_data,
        output wr_biten,
        input wr_ack,
        input wr_err,
        input rd_ack,
        input rd_err,
        input rd_data
    );

    modport slv(
        input req,
        input addr,
        input req_is_wr,
        input wr_data,
        input wr_biten,
        output wr_ack,
        output wr_err,
        output rd_ack,
        output rd_err,
        output rd_data
    );

    modport mon(
        input req,
        input addr,
        input req_is_wr,
        input wr_data,
        input wr_biten,
        input wr_ack,
        input wr_err,
        input rd_ack,
        input rd_err,
        input rd_data
    );

endinterface

`resetall
