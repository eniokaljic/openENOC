// SPDX-FileCopyrightText: 2026 Enio Kaljic
// SPDX-License-Identifier: CERN-OHL-S-2.0

// Generated from openenoc_endpoint_interface.rdl. Do not edit.

`resetall
`timescale 1ns / 1ps
`default_nettype none

interface openenoc_endpoint_if #
(
    parameter int RMEM_TOTAL_DEPTH = 256,
    parameter int NUM_OF_PEERS = 1,
    localparam int RMEM_ADDR_W = ((RMEM_TOTAL_DEPTH * 4) > 1) ? $clog2(RMEM_TOTAL_DEPTH * 4) : 1
)(
    input wire logic clk,
    input wire logic rst
);

    typedef struct {
        logic [31:0] next;
    } core_to_csr__config___mac_address__lo_word_t;

    typedef struct {
        logic [15:0] next;
    } core_to_csr__config___mac_address__hi_word_t;

    typedef struct {
        core_to_csr__config___mac_address__lo_word_t lo_word;
        core_to_csr__config___mac_address__hi_word_t hi_word;
    } core_to_csr__config___mac_address_t;

    typedef struct {
        core_to_csr__config___mac_address_t mac_address;
    } core_to_csr__config__t;

    typedef struct {
        logic next;
    } core_to_csr__axis_if__source__status__tready_t;

    typedef struct {
        core_to_csr__axis_if__source__status__tready_t tready;
    } core_to_csr__axis_if__source__status_t;

    typedef struct {
        core_to_csr__axis_if__source__status_t status;
    } core_to_csr__axis_if__source_t;

    typedef struct {
        logic [31:0] next;
    } core_to_csr__axis_if__sink__data__tdata_t;

    typedef struct {
        core_to_csr__axis_if__sink__data__tdata_t tdata;
    } core_to_csr__axis_if__sink__data_t;

    typedef struct {
        logic next;
    } core_to_csr__axis_if__sink__status__tvalid_t;

    typedef struct {
        logic next;
    } core_to_csr__axis_if__sink__status__tlast_t;

    typedef struct {
        core_to_csr__axis_if__sink__status__tvalid_t tvalid;
        core_to_csr__axis_if__sink__status__tlast_t tlast;
    } core_to_csr__axis_if__sink__status_t;

    typedef struct {
        core_to_csr__axis_if__sink__data_t data;
        core_to_csr__axis_if__sink__status_t status;
    } core_to_csr__axis_if__sink_t;

    typedef struct {
        core_to_csr__axis_if__source_t source;
        core_to_csr__axis_if__sink_t sink;
    } core_to_csr__axis_if_t;

    typedef struct {
        logic [31:0] next;
    } core_to_csr__peers__entry__mac_address__lo_word_t;

    typedef struct {
        logic [15:0] next;
    } core_to_csr__peers__entry__mac_address__hi_word_t;

    typedef struct {
        core_to_csr__peers__entry__mac_address__lo_word_t lo_word;
        core_to_csr__peers__entry__mac_address__hi_word_t hi_word;
    } core_to_csr__peers__entry__mac_address_t;

    typedef struct {
        logic next;
    } core_to_csr__peers__entry__dma__idle_t;

    typedef struct {
        logic next;
    } core_to_csr__peers__entry__dma__done_t;

    typedef struct {
        logic next;
    } core_to_csr__peers__entry__dma__error_t;

    typedef struct {
        core_to_csr__peers__entry__dma__idle_t idle;
        core_to_csr__peers__entry__dma__done_t done;
        core_to_csr__peers__entry__dma__error_t error;
    } core_to_csr__peers__entry__dma_t;

    typedef struct {
        core_to_csr__peers__entry__mac_address_t mac_address;
        core_to_csr__peers__entry__dma_t dma;
    } core_to_csr__peers__entry_t;

    typedef struct {
        core_to_csr__peers__entry_t entry[NUM_OF_PEERS];
    } core_to_csr__peers_t;

    typedef struct {
        logic wr_ack;
        logic rd_ack;
        logic [31:0] rd_data;
    } core_to_csr__rmem_t;

    typedef struct {
        core_to_csr__config__t config_;
        core_to_csr__axis_if_t axis_if;
        core_to_csr__peers_t peers;
        core_to_csr__rmem_t rmem;
    } core_to_csr_t;

    typedef struct {
        logic [31:0] value;
    } csr_to_core__info__rmem_total_depth_t;

    typedef struct {
        logic [31:0] value;
    } csr_to_core__info__num_of_peers_t;

    typedef struct {
        csr_to_core__info__rmem_total_depth_t rmem_total_depth;
        csr_to_core__info__num_of_peers_t num_of_peers;
    } csr_to_core__info_t;

    typedef struct {
        logic [31:0] value;
    } csr_to_core__config___mac_address__lo_word_t;

    typedef struct {
        logic [15:0] value;
    } csr_to_core__config___mac_address__hi_word_t;

    typedef struct {
        csr_to_core__config___mac_address__lo_word_t lo_word;
        csr_to_core__config___mac_address__hi_word_t hi_word;
    } csr_to_core__config___mac_address_t;

    typedef struct {
        csr_to_core__config___mac_address_t mac_address;
    } csr_to_core__config__t;

    typedef struct {
        logic [31:0] value;
    } csr_to_core__axis_if__source__data__tdata_t;

    typedef struct {
        csr_to_core__axis_if__source__data__tdata_t tdata;
    } csr_to_core__axis_if__source__data_t;

    typedef struct {
        logic value;
    } csr_to_core__axis_if__source__control__tvalid_t;

    typedef struct {
        logic value;
    } csr_to_core__axis_if__source__control__tlast_t;

    typedef struct {
        csr_to_core__axis_if__source__control__tvalid_t tvalid;
        csr_to_core__axis_if__source__control__tlast_t tlast;
    } csr_to_core__axis_if__source__control_t;

    typedef struct {
        csr_to_core__axis_if__source__data_t data;
        csr_to_core__axis_if__source__control_t control;
    } csr_to_core__axis_if__source_t;

    typedef struct {
        logic value;
    } csr_to_core__axis_if__sink__control__tready_t;

    typedef struct {
        csr_to_core__axis_if__sink__control__tready_t tready;
    } csr_to_core__axis_if__sink__control_t;

    typedef struct {
        csr_to_core__axis_if__sink__control_t control;
    } csr_to_core__axis_if__sink_t;

    typedef struct {
        csr_to_core__axis_if__source_t source;
        csr_to_core__axis_if__sink_t sink;
    } csr_to_core__axis_if_t;

    typedef struct {
        logic [31:0] value;
    } csr_to_core__peers__entry__mac_address__lo_word_t;

    typedef struct {
        logic [15:0] value;
    } csr_to_core__peers__entry__mac_address__hi_word_t;

    typedef struct {
        csr_to_core__peers__entry__mac_address__lo_word_t lo_word;
        csr_to_core__peers__entry__mac_address__hi_word_t hi_word;
    } csr_to_core__peers__entry__mac_address_t;

    typedef struct {
        logic [31:0] value;
    } csr_to_core__peers__entry__rmem_address__offset_t;

    typedef struct {
        csr_to_core__peers__entry__rmem_address__offset_t offset;
    } csr_to_core__peers__entry__rmem_address_t;

    typedef struct {
        logic [31:0] value;
    } csr_to_core__peers__entry__local_address__base_t;

    typedef struct {
        csr_to_core__peers__entry__local_address__base_t base;
    } csr_to_core__peers__entry__local_address_t;

    typedef struct {
        logic [31:0] value;
    } csr_to_core__peers__entry__remote_address__base_t;

    typedef struct {
        csr_to_core__peers__entry__remote_address__base_t base;
    } csr_to_core__peers__entry__remote_address_t;

    typedef struct {
        logic [31:0] value;
    } csr_to_core__peers__entry__size__bytes_t;

    typedef struct {
        csr_to_core__peers__entry__size__bytes_t bytes;
    } csr_to_core__peers__entry__size_t;

    typedef struct {
        logic [1:0] value;
    } csr_to_core__peers__entry__dma__mode_t;

    typedef struct {
        logic value;
    } csr_to_core__peers__entry__dma__request_t;

    typedef struct {
        csr_to_core__peers__entry__dma__mode_t mode;
        csr_to_core__peers__entry__dma__request_t request;
    } csr_to_core__peers__entry__dma_t;

    typedef struct {
        csr_to_core__peers__entry__mac_address_t mac_address;
        csr_to_core__peers__entry__rmem_address_t rmem_address;
        csr_to_core__peers__entry__local_address_t local_address;
        csr_to_core__peers__entry__remote_address_t remote_address;
        csr_to_core__peers__entry__size_t size;
        csr_to_core__peers__entry__dma_t dma;
    } csr_to_core__peers__entry_t;

    typedef struct {
        csr_to_core__peers__entry_t entry[NUM_OF_PEERS];
    } csr_to_core__peers_t;

    typedef struct {
        logic req;
        logic [RMEM_ADDR_W-1:0] addr;
        logic req_is_wr;
        logic [31:0] wr_data;
        logic [31:0] wr_biten;
    } csr_to_core__rmem_t;

    typedef struct {
        csr_to_core__info_t info;
        csr_to_core__config__t config_;
        csr_to_core__axis_if_t axis_if;
        csr_to_core__peers_t peers;
        csr_to_core__rmem_t rmem;
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
