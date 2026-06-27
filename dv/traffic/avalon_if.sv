// SPDX-FileCopyrightText: 2026 Amina Tankovic
// SPDX-License-Identifier: AGPL-3.0-or-later

interface avalon_if #
(
    parameter DATA_WIDTH = 512,
    parameter EMPTY_WIDTH = DATA_WIDTH > 8 ? $clog2(DATA_WIDTH / 8) : 1
)
(
    input logic   clk,
    input logic   rst
);
    logic                   ready;
    logic                   valid;
    logic [DATA_WIDTH-1:0]  data;
    logic                   sop;
    logic                   eop;
    logic [EMPTY_WIDTH-1:0] empty;

   modport out (
       input    clk,
       input    rst,
       input    ready,
       output   valid,
       output   data,
       output   sop,
       output   eop,
       output   empty
   );

   modport in (
       input    clk,
       input    rst,
       output   ready,
       input    valid,
       input    data,
       input    sop,
       input    eop,
       input    empty
   );
endinterface

