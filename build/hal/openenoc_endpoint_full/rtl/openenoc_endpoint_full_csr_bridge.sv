// SPDX-FileCopyrightText: 2026 Enio Kaljic
// SPDX-License-Identifier: CERN-OHL-S-2.0

// Generated from openenoc_endpoint_full.rdl. Do not edit.

`resetall
`timescale 1ns / 1ps
`default_nettype none

module openenoc_endpoint_full_csr_bridge (
    input  openenoc_endpoint_full_csr_pkg::openenoc_endpoint_full_csr__out_t csr_hwif_out,
    output var openenoc_endpoint_full_csr_pkg::openenoc_endpoint_full_csr__in_t csr_hwif_in,
    openenoc_endpoint_if.csr endpoint_if,
    openenoc_switch_if.csr switch_if
);

    // endpoint_if parameters:
    //   RMEM_TOTAL_DEPTH = openenoc_endpoint_full_csr_pkg::RMEM_TOTAL_DEPTH
    //   NUM_OF_PEERS = openenoc_endpoint_full_csr_pkg::NUM_OF_PEERS
    // switch_if parameters:
    //   NUM_OF_INTERFACES = openenoc_endpoint_full_csr_pkg::NUM_OF_INTERFACES
    //   TABLE_DEPTH = openenoc_endpoint_full_csr_pkg::TABLE_DEPTH
    always_comb begin
        csr_hwif_in = '0;
        endpoint_if.csr_to_core = '0;
        switch_if.csr_to_core = '0;
        csr_hwif_in.endpoint_interface.config_.mac_address.lo_word.next = endpoint_if.core_to_csr.config_.mac_address.lo_word.next;
        csr_hwif_in.endpoint_interface.config_.mac_address.hi_word.next = endpoint_if.core_to_csr.config_.mac_address.hi_word.next;
        csr_hwif_in.endpoint_interface.axis_if.source.status.tready.next = endpoint_if.core_to_csr.axis_if.source.status.tready.next;
        csr_hwif_in.endpoint_interface.axis_if.sink.data.tdata.next = endpoint_if.core_to_csr.axis_if.sink.data.tdata.next;
        csr_hwif_in.endpoint_interface.axis_if.sink.status.tvalid.next = endpoint_if.core_to_csr.axis_if.sink.status.tvalid.next;
        csr_hwif_in.endpoint_interface.axis_if.sink.status.tlast.next = endpoint_if.core_to_csr.axis_if.sink.status.tlast.next;
        for (int unsigned i6_0 = 0; i6_0 < 4; i6_0++) begin
            csr_hwif_in.endpoint_interface.peers.entry[i6_0].mac_address.lo_word.next = endpoint_if.core_to_csr.peers.entry[i6_0].mac_address.lo_word.next;
        end
        for (int unsigned i7_0 = 0; i7_0 < 4; i7_0++) begin
            csr_hwif_in.endpoint_interface.peers.entry[i7_0].mac_address.hi_word.next = endpoint_if.core_to_csr.peers.entry[i7_0].mac_address.hi_word.next;
        end
        for (int unsigned i8_0 = 0; i8_0 < 4; i8_0++) begin
            csr_hwif_in.endpoint_interface.peers.entry[i8_0].dma.idle.next = endpoint_if.core_to_csr.peers.entry[i8_0].dma.idle.next;
        end
        for (int unsigned i9_0 = 0; i9_0 < 4; i9_0++) begin
            csr_hwif_in.endpoint_interface.peers.entry[i9_0].dma.done.next = endpoint_if.core_to_csr.peers.entry[i9_0].dma.done.next;
        end
        for (int unsigned i10_0 = 0; i10_0 < 4; i10_0++) begin
            csr_hwif_in.endpoint_interface.peers.entry[i10_0].dma.error.next = endpoint_if.core_to_csr.peers.entry[i10_0].dma.error.next;
        end
        csr_hwif_in.endpoint_interface.rmem.wr_ack = endpoint_if.core_to_csr.rmem.wr_ack;
        csr_hwif_in.endpoint_interface.rmem.rd_ack = endpoint_if.core_to_csr.rmem.rd_ack;
        csr_hwif_in.endpoint_interface.rmem.rd_data = endpoint_if.core_to_csr.rmem.rd_data;
        endpoint_if.csr_to_core.info.rmem_total_depth.value = csr_hwif_out.endpoint_interface.info.rmem_total_depth.value;
        endpoint_if.csr_to_core.info.num_of_peers.value = csr_hwif_out.endpoint_interface.info.num_of_peers.value;
        endpoint_if.csr_to_core.config_.mac_address.lo_word.value = csr_hwif_out.endpoint_interface.config_.mac_address.lo_word.value;
        endpoint_if.csr_to_core.config_.mac_address.hi_word.value = csr_hwif_out.endpoint_interface.config_.mac_address.hi_word.value;
        endpoint_if.csr_to_core.axis_if.source.data.tdata.value = csr_hwif_out.endpoint_interface.axis_if.source.data.tdata.value;
        endpoint_if.csr_to_core.axis_if.source.control.tvalid.value = csr_hwif_out.endpoint_interface.axis_if.source.control.tvalid.value;
        endpoint_if.csr_to_core.axis_if.source.control.tlast.value = csr_hwif_out.endpoint_interface.axis_if.source.control.tlast.value;
        endpoint_if.csr_to_core.axis_if.sink.control.tready.value = csr_hwif_out.endpoint_interface.axis_if.sink.control.tready.value;
        for (int unsigned i22_0 = 0; i22_0 < 4; i22_0++) begin
            endpoint_if.csr_to_core.peers.entry[i22_0].mac_address.lo_word.value = csr_hwif_out.endpoint_interface.peers.entry[i22_0].mac_address.lo_word.value;
        end
        for (int unsigned i23_0 = 0; i23_0 < 4; i23_0++) begin
            endpoint_if.csr_to_core.peers.entry[i23_0].mac_address.hi_word.value = csr_hwif_out.endpoint_interface.peers.entry[i23_0].mac_address.hi_word.value;
        end
        for (int unsigned i24_0 = 0; i24_0 < 4; i24_0++) begin
            endpoint_if.csr_to_core.peers.entry[i24_0].rmem_address.offset.value = csr_hwif_out.endpoint_interface.peers.entry[i24_0].rmem_address.offset.value;
        end
        for (int unsigned i25_0 = 0; i25_0 < 4; i25_0++) begin
            endpoint_if.csr_to_core.peers.entry[i25_0].local_address.base.value = csr_hwif_out.endpoint_interface.peers.entry[i25_0].local_address.base.value;
        end
        for (int unsigned i26_0 = 0; i26_0 < 4; i26_0++) begin
            endpoint_if.csr_to_core.peers.entry[i26_0].remote_address.base.value = csr_hwif_out.endpoint_interface.peers.entry[i26_0].remote_address.base.value;
        end
        for (int unsigned i27_0 = 0; i27_0 < 4; i27_0++) begin
            endpoint_if.csr_to_core.peers.entry[i27_0].size.bytes.value = csr_hwif_out.endpoint_interface.peers.entry[i27_0].size.bytes.value;
        end
        for (int unsigned i28_0 = 0; i28_0 < 4; i28_0++) begin
            endpoint_if.csr_to_core.peers.entry[i28_0].dma.mode.value = csr_hwif_out.endpoint_interface.peers.entry[i28_0].dma.mode.value;
        end
        for (int unsigned i29_0 = 0; i29_0 < 4; i29_0++) begin
            endpoint_if.csr_to_core.peers.entry[i29_0].dma.request.value = csr_hwif_out.endpoint_interface.peers.entry[i29_0].dma.request.value;
        end
        endpoint_if.csr_to_core.rmem.req = csr_hwif_out.endpoint_interface.rmem.req;
        endpoint_if.csr_to_core.rmem.addr = csr_hwif_out.endpoint_interface.rmem.addr;
        endpoint_if.csr_to_core.rmem.req_is_wr = csr_hwif_out.endpoint_interface.rmem.req_is_wr;
        endpoint_if.csr_to_core.rmem.wr_data = csr_hwif_out.endpoint_interface.rmem.wr_data;
        endpoint_if.csr_to_core.rmem.wr_biten = csr_hwif_out.endpoint_interface.rmem.wr_biten;
        csr_hwif_in.switch_interface.forwarding_control.pause_done.next = switch_if.core_to_csr.forwarding_control.pause_done.next;
        csr_hwif_in.switch_interface.forwarding_table.wr_ack = switch_if.core_to_csr.forwarding_table.wr_ack;
        csr_hwif_in.switch_interface.forwarding_table.rd_ack = switch_if.core_to_csr.forwarding_table.rd_ack;
        csr_hwif_in.switch_interface.forwarding_table.rd_data = switch_if.core_to_csr.forwarding_table.rd_data;
        switch_if.csr_to_core.info.table_depth.value = csr_hwif_out.switch_interface.info.table_depth.value;
        switch_if.csr_to_core.info.num_of_interfaces.value = csr_hwif_out.switch_interface.info.num_of_interfaces.value;
        switch_if.csr_to_core.forwarding_control.operation_mode.value = csr_hwif_out.switch_interface.forwarding_control.operation_mode.value;
        switch_if.csr_to_core.forwarding_control.pause_request.value = csr_hwif_out.switch_interface.forwarding_control.pause_request.value;
        switch_if.csr_to_core.default_forwarding.bitmap.value = csr_hwif_out.switch_interface.default_forwarding.bitmap.value;
        switch_if.csr_to_core.forwarding_table.req = csr_hwif_out.switch_interface.forwarding_table.req;
        switch_if.csr_to_core.forwarding_table.addr = csr_hwif_out.switch_interface.forwarding_table.addr;
        switch_if.csr_to_core.forwarding_table.req_is_wr = csr_hwif_out.switch_interface.forwarding_table.req_is_wr;
        switch_if.csr_to_core.forwarding_table.wr_data = csr_hwif_out.switch_interface.forwarding_table.wr_data;
        switch_if.csr_to_core.forwarding_table.wr_biten = csr_hwif_out.switch_interface.forwarding_table.wr_biten;
    end

endmodule

`resetall
