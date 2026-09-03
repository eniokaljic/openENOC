// SPDX-FileCopyrightText: 2026 Enio Kaljic
// SPDX-License-Identifier: CERN-OHL-S-2.0

`resetall
`timescale 1ns / 1ps
`default_nettype none

interface openenoc_learning_if #(
    parameter int NUM_OF_INTERFACES = 8
);
    logic                         req;
    logic [47:0]                  mac_addr;
    logic [NUM_OF_INTERFACES-1:0] port_bitmap;
    logic                         ack;

    modport mst (
        output req,
        output mac_addr,
        output port_bitmap,

        input  ack
    );

    modport slv (
        input  req,
        input  mac_addr,
        input  port_bitmap,

        output ack
    );

endinterface

`resetall
