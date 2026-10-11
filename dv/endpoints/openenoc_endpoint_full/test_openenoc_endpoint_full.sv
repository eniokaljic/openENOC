// SPDX-FileCopyrightText: 2026 Enio Kaljic
// SPDX-License-Identifier: AGPL-3.0-or-later

`resetall
`timescale 1ns / 1ps
`default_nettype none

/* Full endpoint testbench */
module test_openenoc_endpoint_full #(
    parameter IMEM_INIT_FILE = ""
) ();

    logic clk;
    logic rst;
    logic loopback_pause;

    openenoc_switch_if #(
        .NUM_OF_INTERFACES(openenoc_endpoint_full_csr_pkg::NUM_OF_INTERFACES),
        .TABLE_DEPTH(openenoc_endpoint_full_csr_pkg::TABLE_DEPTH)
    ) switch_if (
        .clk(clk),
        .rst(rst)
    );

    openenoc_eth_if eth_if (
        .clk(clk),
        .rst(rst)
    );

    // External Ethernet loopback: endpoint transmit is returned to receive.
    assign eth_if.a2b_axis_if.tready = eth_if.b2a_axis_if.tready && !loopback_pause;
    assign eth_if.b2a_axis_if.tdata = eth_if.a2b_axis_if.tdata;
    assign eth_if.b2a_axis_if.tkeep = eth_if.a2b_axis_if.tkeep;
    assign eth_if.b2a_axis_if.tstrb = eth_if.a2b_axis_if.tstrb;
    assign eth_if.b2a_axis_if.tid = eth_if.a2b_axis_if.tid;
    assign eth_if.b2a_axis_if.tdest = eth_if.a2b_axis_if.tdest;
    assign eth_if.b2a_axis_if.tuser = eth_if.a2b_axis_if.tuser;
    assign eth_if.b2a_axis_if.tlast = eth_if.a2b_axis_if.tlast;
    assign eth_if.b2a_axis_if.tvalid = eth_if.a2b_axis_if.tvalid && !loopback_pause;

    initial begin
        switch_if.core_to_csr = '{default: '0};
        switch_if.core_to_csr.forwarding_control.pause_done.next = 1'b1;
    end

    openenoc_endpoint_full #(
        .IMEM_INIT_FILE(IMEM_INIT_FILE)
    ) u_openenoc_endpoint_full (
        .clk(clk),
        .rst(rst),
        .switch_if(switch_if),
        .eth_if(eth_if)
    );

    /*
     * Verilator-friendly white-box observability. These are testbench-only signals and do not
     * expand the endpoint's external interface.
     */
    wire logic [31:0] imem_word0 = u_openenoc_endpoint_full.u_imem.mem[0];
    wire logic [31:0] dmem_status = u_openenoc_endpoint_full.u_dmem.mem[0];
    wire logic[31:0] csr_test_value =
        u_openenoc_endpoint_full.csr_hwif_out.test_reg.test_field.value;
    wire  logic cpu_trap = u_openenoc_endpoint_full.cpu_trap;
    wire  logic endpoint_irq = u_openenoc_endpoint_full.endpoint_irq;
    wire logic [31:0] cpu_irq = u_openenoc_endpoint_full.cpu_irq;
    wire logic [31:0] cpu_eoi = u_openenoc_endpoint_full.u_cpu.eoi;
    wire  logic cpu_irq_active = u_openenoc_endpoint_full.u_cpu.u_picorv32_core.irq_active;
    wire logic irq_complete_hwclr =
        u_openenoc_endpoint_full.endpoint_if.core_to_csr.irq.complete.valid.hwclr;
    wire logic [31:0] irq_claim_token = {
        u_openenoc_endpoint_full.endpoint_if.core_to_csr.irq.claim.valid.next,
        u_openenoc_endpoint_full.endpoint_if.core_to_csr.irq.claim.sequence_.next,
        u_openenoc_endpoint_full.endpoint_if.core_to_csr.irq.claim.source.next,
        u_openenoc_endpoint_full.endpoint_if.core_to_csr.irq.claim.peer_idx.next
    };
    wire logic [31:0] irq_complete_token = {
        u_openenoc_endpoint_full.endpoint_if.csr_to_core.irq.complete.valid.value,
        u_openenoc_endpoint_full.endpoint_if.csr_to_core.irq.complete.sequence_.value,
        u_openenoc_endpoint_full.endpoint_if.csr_to_core.irq.complete.source.value,
        u_openenoc_endpoint_full.endpoint_if.csr_to_core.irq.complete.peer_idx.value
    };
    wire logic irq_overflow =
        u_openenoc_endpoint_full.endpoint_if.core_to_csr.irq.status.overflow.next;
    wire logic irq_invalid_complete =
        u_openenoc_endpoint_full.endpoint_if.core_to_csr.irq.status.invalid_complete.next;
    wire logic[7:0] irq_fifo_level =
        u_openenoc_endpoint_full.endpoint_if.core_to_csr.irq.status.fifo_level.next;
    wire logic[7:0] irq_reserved_count =
        u_openenoc_endpoint_full.endpoint_if.core_to_csr.irq.status.reserved_count.next;

    wire logic [15:0] switch_table_depth = switch_if.csr_to_core.info.table_depth.value;
    wire logic[5:0] switch_num_interfaces = switch_if.csr_to_core.info.num_of_interfaces.value;
    wire logic switch_pause_done_hwif =
        u_openenoc_endpoint_full.csr_hwif_in.switch_interface.forwarding_control.pause_done.next;
    wire logic switch_operation_mode =
        switch_if.csr_to_core.forwarding_control.operation_mode.value;
    wire logic switch_pause_request = switch_if.csr_to_core.forwarding_control.pause_request.value;
    wire logic[3:0] switch_default_forwarding =
        switch_if.csr_to_core.default_forwarding.bitmap.value;
    wire logic[31:0] endpoint_mac_lo_hwif =
        u_openenoc_endpoint_full.endpoint_if.csr_to_core.config_.mac_address.lo_word.value;

    wire logic [31:0] endpoint_tx_data = eth_if.a2b_axis_if.tdata;
    wire logic [3:0] endpoint_tx_keep = eth_if.a2b_axis_if.tkeep;
    wire  logic endpoint_tx_last = eth_if.a2b_axis_if.tlast;
    wire  logic endpoint_tx_valid = eth_if.a2b_axis_if.tvalid;
    wire  logic endpoint_tx_ready = eth_if.a2b_axis_if.tready;

    wire logic[31:0] endpoint_csr_sink_data =
        u_openenoc_endpoint_full.u_endpoint_interface.u_direct_axis.rx_payload_if.tdata;
    wire logic[3:0] endpoint_csr_sink_keep =
        u_openenoc_endpoint_full.u_endpoint_interface.u_direct_axis.rx_payload_if.tkeep;
    wire logic endpoint_csr_sink_last =
        u_openenoc_endpoint_full.u_endpoint_interface.u_direct_axis.rx_payload_if.tlast;
    wire logic endpoint_csr_sink_valid =
        u_openenoc_endpoint_full.u_endpoint_interface.u_direct_axis.rx_payload_if.tvalid;
    wire logic endpoint_csr_sink_ready =
        u_openenoc_endpoint_full.u_endpoint_interface.u_direct_axis.rx_payload_if.tready;

    wire logic rmem_master_inactive = !u_openenoc_endpoint_full.rmem_cpuif.req
        && !u_openenoc_endpoint_full.s_axil_if[3].awvalid
        && !u_openenoc_endpoint_full.s_axil_if[3].wvalid
        && !u_openenoc_endpoint_full.s_axil_if[3].arvalid;

    wire logic reserved_masters_inactive = !u_openenoc_endpoint_full.endpoint_axil_if.awvalid
        && !u_openenoc_endpoint_full.endpoint_axil_if.wvalid
        && !u_openenoc_endpoint_full.endpoint_axil_if.arvalid
        && !u_openenoc_endpoint_full.endpoint_axil_if.bready
        && !u_openenoc_endpoint_full.endpoint_axil_if.rready
        && !u_openenoc_endpoint_full.debug_axil_if.awvalid
        && !u_openenoc_endpoint_full.debug_axil_if.wvalid
        && !u_openenoc_endpoint_full.debug_axil_if.arvalid
        && !u_openenoc_endpoint_full.debug_axil_if.bready
        && !u_openenoc_endpoint_full.debug_axil_if.rready;

endmodule

`resetall
