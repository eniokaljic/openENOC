// SPDX-FileCopyrightText: 2026 Enio Kaljic
// SPDX-License-Identifier: CERN-OHL-S-2.0

`resetall
`timescale 1ns / 1ps
`default_nettype none

interface openenoc_lookup_if #(
    parameter int NUM_OF_INTERFACES = 8
);
    logic                         req;
    logic [47:0]                  mac_addr;
    logic                         ack;
    logic [NUM_OF_INTERFACES-1:0] port_bitmap;

    modport mst (
        output req,
        output mac_addr,

        input  ack,
        input  port_bitmap
    );

    modport slv (
        input  req,
        input  mac_addr,

        output ack,
        output port_bitmap
    );

endinterface

`resetall
