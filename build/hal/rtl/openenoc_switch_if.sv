// SPDX-FileCopyrightText: 2026 Enio Kaljic
// SPDX-License-Identifier: CERN-OHL-S-2.0

// Generated from openenoc_switch_interface.rdl. Do not edit.

`resetall
`timescale 1ns / 1ps
`default_nettype none

interface openenoc_switch_if #
(
    parameter int NUM_OF_INTERFACES = 1,
    parameter int TABLE_DEPTH = 1,
    localparam int FORWARDING_TABLE_ADDR_W = ((TABLE_DEPTH * 16) > 1) ? $clog2(TABLE_DEPTH * 16) : 1
)(
    input wire logic clk,
    input wire logic rst
);

    typedef struct {
        logic next;
    } core_to_csr__forwarding_control__pause_done_t;

    typedef struct {
        core_to_csr__forwarding_control__pause_done_t pause_done;
    } core_to_csr__forwarding_control_t;

    typedef struct {
        logic wr_ack;
        logic rd_ack;
        logic [31:0] rd_data;
    } core_to_csr__forwarding_table_t;

    typedef struct {
        core_to_csr__forwarding_control_t forwarding_control;
        core_to_csr__forwarding_table_t forwarding_table;
    } core_to_csr_t;

    typedef struct {
        logic [15:0] value;
    } csr_to_core__info__table_depth_t;

    typedef struct {
        logic [5:0] value;
    } csr_to_core__info__num_of_interfaces_t;

    typedef struct {
        csr_to_core__info__table_depth_t table_depth;
        csr_to_core__info__num_of_interfaces_t num_of_interfaces;
    } csr_to_core__info_t;

    typedef struct {
        logic value;
    } csr_to_core__forwarding_control__operation_mode_t;

    typedef struct {
        logic value;
    } csr_to_core__forwarding_control__pause_request_t;

    typedef struct {
        csr_to_core__forwarding_control__operation_mode_t operation_mode;
        csr_to_core__forwarding_control__pause_request_t pause_request;
    } csr_to_core__forwarding_control_t;

    typedef struct {
        logic [(NUM_OF_INTERFACES - 1):0] value;
    } csr_to_core__default_forwarding__bitmap_t;

    typedef struct {
        csr_to_core__default_forwarding__bitmap_t bitmap;
    } csr_to_core__default_forwarding_t;

    typedef struct {
        logic req;
        logic [FORWARDING_TABLE_ADDR_W-1:0] addr;
        logic req_is_wr;
        logic [31:0] wr_data;
        logic [31:0] wr_biten;
    } csr_to_core__forwarding_table_t;

    typedef struct {
        csr_to_core__info_t info;
        csr_to_core__forwarding_control_t forwarding_control;
        csr_to_core__default_forwarding_t default_forwarding;
        csr_to_core__forwarding_table_t forwarding_table;
    } csr_to_core_t;

    core_to_csr_t core_to_csr;
    csr_to_core_t csr_to_core;

    modport csr (
        input  clk,
        input  rst,
        input  core_to_csr,
        output csr_to_core
    );

    modport core (
        input  clk,
        input  rst,
        output core_to_csr,
        input  csr_to_core
    );

endinterface

`resetall
