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
    //   MAX_DMA_FRAME_SIZE_BYTES = openenoc_endpoint_full_csr_pkg::MAX_DMA_FRAME_SIZE_BYTES
    //   HAS_PEER_DMA = openenoc_endpoint_full_csr_pkg::HAS_PEER_DMA
    //   HAS_NON_OETP_DMA = openenoc_endpoint_full_csr_pkg::HAS_NON_OETP_DMA
    //   HAS_DIRECT_AXIS = openenoc_endpoint_full_csr_pkg::HAS_DIRECT_AXIS
    //   HAS_RMEM = openenoc_endpoint_full_csr_pkg::HAS_RMEM
    //   HAS_IRQ = openenoc_endpoint_full_csr_pkg::HAS_IRQ
    // switch_if parameters:
    //   NUM_OF_INTERFACES = openenoc_endpoint_full_csr_pkg::NUM_OF_INTERFACES
    //   TABLE_DEPTH = openenoc_endpoint_full_csr_pkg::TABLE_DEPTH
    always_comb begin
        csr_hwif_in = '{default: '0};
        endpoint_if.csr_to_core = '{default: '0};
        switch_if.csr_to_core = '{default: '0};
        csr_hwif_in.endpoint_interface.axis_if.source.control.tvalid.hwclr = endpoint_if.core_to_csr.axis_if.source.control.tvalid.hwclr;
        csr_hwif_in.endpoint_interface.axis_if.source.status.tready.next = endpoint_if.core_to_csr.axis_if.source.status.tready.next;
        csr_hwif_in.endpoint_interface.axis_if.sink.data.tdata.next = endpoint_if.core_to_csr.axis_if.sink.data.tdata.next;
        csr_hwif_in.endpoint_interface.axis_if.sink.control.tready.hwclr = endpoint_if.core_to_csr.axis_if.sink.control.tready.hwclr;
        csr_hwif_in.endpoint_interface.axis_if.sink.status.tvalid.next = endpoint_if.core_to_csr.axis_if.sink.status.tvalid.next;
        csr_hwif_in.endpoint_interface.axis_if.sink.status.tlast.next = endpoint_if.core_to_csr.axis_if.sink.status.tlast.next;
        csr_hwif_in.endpoint_interface.axis_if.sink.status.tkeep.next = endpoint_if.core_to_csr.axis_if.sink.status.tkeep.next;
        csr_hwif_in.endpoint_interface.non_oetp_dma.tx.command_status.request.hwclr = endpoint_if.core_to_csr.non_oetp_dma.tx.command_status.request.hwclr;
        csr_hwif_in.endpoint_interface.non_oetp_dma.tx.command_status.idle.next = endpoint_if.core_to_csr.non_oetp_dma.tx.command_status.idle.next;
        csr_hwif_in.endpoint_interface.non_oetp_dma.tx.command_status.done.next = endpoint_if.core_to_csr.non_oetp_dma.tx.command_status.done.next;
        csr_hwif_in.endpoint_interface.non_oetp_dma.tx.command_status.error.next = endpoint_if.core_to_csr.non_oetp_dma.tx.command_status.error.next;
        csr_hwif_in.endpoint_interface.non_oetp_dma.tx.command_status.error_code.next = endpoint_if.core_to_csr.non_oetp_dma.tx.command_status.error_code.next;
        csr_hwif_in.endpoint_interface.non_oetp_dma.tx.transferred_length.bytes.next = endpoint_if.core_to_csr.non_oetp_dma.tx.transferred_length.bytes.next;
        csr_hwif_in.endpoint_interface.non_oetp_dma.rx.command_status.request.hwclr = endpoint_if.core_to_csr.non_oetp_dma.rx.command_status.request.hwclr;
        csr_hwif_in.endpoint_interface.non_oetp_dma.rx.command_status.idle.next = endpoint_if.core_to_csr.non_oetp_dma.rx.command_status.idle.next;
        csr_hwif_in.endpoint_interface.non_oetp_dma.rx.command_status.armed.next = endpoint_if.core_to_csr.non_oetp_dma.rx.command_status.armed.next;
        csr_hwif_in.endpoint_interface.non_oetp_dma.rx.command_status.done.next = endpoint_if.core_to_csr.non_oetp_dma.rx.command_status.done.next;
        csr_hwif_in.endpoint_interface.non_oetp_dma.rx.command_status.error.next = endpoint_if.core_to_csr.non_oetp_dma.rx.command_status.error.next;
        csr_hwif_in.endpoint_interface.non_oetp_dma.rx.command_status.error_code.next = endpoint_if.core_to_csr.non_oetp_dma.rx.command_status.error_code.next;
        csr_hwif_in.endpoint_interface.non_oetp_dma.rx.received_length.bytes.next = endpoint_if.core_to_csr.non_oetp_dma.rx.received_length.bytes.next;
        for (int unsigned i20_0 = 0; i20_0 < 4; i20_0++) begin
            csr_hwif_in.endpoint_interface.peers.entry[i20_0].dma.request.hwclr = endpoint_if.core_to_csr.peers.entry[i20_0].dma.request.hwclr;
        end
        for (int unsigned i21_0 = 0; i21_0 < 4; i21_0++) begin
            csr_hwif_in.endpoint_interface.peers.entry[i21_0].dma.idle.next = endpoint_if.core_to_csr.peers.entry[i21_0].dma.idle.next;
        end
        for (int unsigned i22_0 = 0; i22_0 < 4; i22_0++) begin
            csr_hwif_in.endpoint_interface.peers.entry[i22_0].dma.done.next = endpoint_if.core_to_csr.peers.entry[i22_0].dma.done.next;
        end
        for (int unsigned i23_0 = 0; i23_0 < 4; i23_0++) begin
            csr_hwif_in.endpoint_interface.peers.entry[i23_0].dma.error.next = endpoint_if.core_to_csr.peers.entry[i23_0].dma.error.next;
        end
        for (int unsigned i24_0 = 0; i24_0 < 4; i24_0++) begin
            csr_hwif_in.endpoint_interface.peers.entry[i24_0].dma.error_code.next = endpoint_if.core_to_csr.peers.entry[i24_0].dma.error_code.next;
        end
        csr_hwif_in.endpoint_interface.rmem.wr_ack = endpoint_if.core_to_csr.rmem.wr_ack;
        csr_hwif_in.endpoint_interface.rmem.rd_ack = endpoint_if.core_to_csr.rmem.rd_ack;
        csr_hwif_in.endpoint_interface.rmem.rd_data = endpoint_if.core_to_csr.rmem.rd_data;
        endpoint_if.csr_to_core.info.rmem_total_depth.value = csr_hwif_out.endpoint_interface.info.rmem_total_depth.value;
        endpoint_if.csr_to_core.info.num_of_peers.value = csr_hwif_out.endpoint_interface.info.num_of_peers.value;
        endpoint_if.csr_to_core.info.peer_dma_supported.value = csr_hwif_out.endpoint_interface.info.peer_dma_supported.value;
        endpoint_if.csr_to_core.info.non_oetp_dma_supported.value = csr_hwif_out.endpoint_interface.info.non_oetp_dma_supported.value;
        endpoint_if.csr_to_core.info.direct_axis_supported.value = csr_hwif_out.endpoint_interface.info.direct_axis_supported.value;
        endpoint_if.csr_to_core.info.rmem_supported.value = csr_hwif_out.endpoint_interface.info.rmem_supported.value;
        endpoint_if.csr_to_core.info.irq_supported.value = csr_hwif_out.endpoint_interface.info.irq_supported.value;
        endpoint_if.csr_to_core.info.max_dma_frame_size_bytes.value = csr_hwif_out.endpoint_interface.info.max_dma_frame_size_bytes.value;
        endpoint_if.csr_to_core.config_.mac_address.lo_word.value = csr_hwif_out.endpoint_interface.config_.mac_address.lo_word.value;
        endpoint_if.csr_to_core.config_.mac_address.hi_word.value = csr_hwif_out.endpoint_interface.config_.mac_address.hi_word.value;
        endpoint_if.csr_to_core.config_.non_oetp_control.receive_mode.value = csr_hwif_out.endpoint_interface.config_.non_oetp_control.receive_mode.value;
        endpoint_if.csr_to_core.axis_if.source.data.tdata.value = csr_hwif_out.endpoint_interface.axis_if.source.data.tdata.value;
        endpoint_if.csr_to_core.axis_if.source.control.tvalid.value = csr_hwif_out.endpoint_interface.axis_if.source.control.tvalid.value;
        endpoint_if.csr_to_core.axis_if.source.control.tlast.value = csr_hwif_out.endpoint_interface.axis_if.source.control.tlast.value;
        endpoint_if.csr_to_core.axis_if.source.control.tkeep.value = csr_hwif_out.endpoint_interface.axis_if.source.control.tkeep.value;
        endpoint_if.csr_to_core.axis_if.sink.control.tready.value = csr_hwif_out.endpoint_interface.axis_if.sink.control.tready.value;
        endpoint_if.csr_to_core.non_oetp_dma.tx.buffer_address.base.value = csr_hwif_out.endpoint_interface.non_oetp_dma.tx.buffer_address.base.value;
        endpoint_if.csr_to_core.non_oetp_dma.tx.frame_length.bytes.value = csr_hwif_out.endpoint_interface.non_oetp_dma.tx.frame_length.bytes.value;
        endpoint_if.csr_to_core.non_oetp_dma.tx.command_status.request.value = csr_hwif_out.endpoint_interface.non_oetp_dma.tx.command_status.request.value;
        endpoint_if.csr_to_core.non_oetp_dma.rx.buffer_address.base.value = csr_hwif_out.endpoint_interface.non_oetp_dma.rx.buffer_address.base.value;
        endpoint_if.csr_to_core.non_oetp_dma.rx.buffer_capacity.bytes.value = csr_hwif_out.endpoint_interface.non_oetp_dma.rx.buffer_capacity.bytes.value;
        endpoint_if.csr_to_core.non_oetp_dma.rx.command_status.request.value = csr_hwif_out.endpoint_interface.non_oetp_dma.rx.command_status.request.value;
        for (int unsigned i50_0 = 0; i50_0 < 4; i50_0++) begin
            endpoint_if.csr_to_core.peers.entry[i50_0].mac_address.lo_word.value = csr_hwif_out.endpoint_interface.peers.entry[i50_0].mac_address.lo_word.value;
        end
        for (int unsigned i51_0 = 0; i51_0 < 4; i51_0++) begin
            endpoint_if.csr_to_core.peers.entry[i51_0].mac_address.hi_word.value = csr_hwif_out.endpoint_interface.peers.entry[i51_0].mac_address.hi_word.value;
        end
        for (int unsigned i52_0 = 0; i52_0 < 4; i52_0++) begin
            endpoint_if.csr_to_core.peers.entry[i52_0].rmem_address.offset.value = csr_hwif_out.endpoint_interface.peers.entry[i52_0].rmem_address.offset.value;
        end
        for (int unsigned i53_0 = 0; i53_0 < 4; i53_0++) begin
            endpoint_if.csr_to_core.peers.entry[i53_0].local_address.base.value = csr_hwif_out.endpoint_interface.peers.entry[i53_0].local_address.base.value;
        end
        for (int unsigned i54_0 = 0; i54_0 < 4; i54_0++) begin
            endpoint_if.csr_to_core.peers.entry[i54_0].remote_address.base.value = csr_hwif_out.endpoint_interface.peers.entry[i54_0].remote_address.base.value;
        end
        for (int unsigned i55_0 = 0; i55_0 < 4; i55_0++) begin
            endpoint_if.csr_to_core.peers.entry[i55_0].size.bytes.value = csr_hwif_out.endpoint_interface.peers.entry[i55_0].size.bytes.value;
        end
        for (int unsigned i56_0 = 0; i56_0 < 4; i56_0++) begin
            endpoint_if.csr_to_core.peers.entry[i56_0].dma.mode.value = csr_hwif_out.endpoint_interface.peers.entry[i56_0].dma.mode.value;
        end
        for (int unsigned i57_0 = 0; i57_0 < 4; i57_0++) begin
            endpoint_if.csr_to_core.peers.entry[i57_0].dma.request.value = csr_hwif_out.endpoint_interface.peers.entry[i57_0].dma.request.value;
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
