// SPDX-FileCopyrightText: 2026 Enio Kaljic
// SPDX-License-Identifier: CERN-OHL-S-2.0

`resetall
`timescale 1ns / 1ps
`default_nettype none

/*
 * openENOC full endpoint including PicoRV32 CPU, instruction/data memories, generated CSR block and interfaces
 */
module openenoc_endpoint_full #
(
    // Optional $readmemh-compatible memory initialization files
    parameter IMEM_INIT_FILE = "",
    parameter DMEM_INIT_FILE = ""
)
(
    input  wire logic clk,
    input  wire logic rst,

    openenoc_switch_if.csr switch_if,
    openenoc_eth_if eth_if
);

    localparam INITIATOR_COUNT = 3;
    localparam TARGET_COUNT = 3;
    localparam AXIL_ADDR_W = 32;
    localparam AXIL_DATA_W = openenoc_endpoint_full_pkg::OPENENOC_ENDPOINT_FULL_DATA_WIDTH;
    localparam AXIL_STRB_W = AXIL_DATA_W/8;

    localparam IMEM_ADDR_W = $clog2(
        openenoc_endpoint_full_pkg::IMEM_DEPTH * AXIL_STRB_W
    );
    localparam DMEM_ADDR_W = $clog2(
        openenoc_endpoint_full_pkg::DMEM_DEPTH * AXIL_STRB_W
    );
    localparam CSR_ADDR_W =
        openenoc_endpoint_full_csr_pkg::OPENENOC_ENDPOINT_FULL_CSR_MIN_ADDR_WIDTH;

    openenoc_endpoint_full_csr_pkg::openenoc_endpoint_full_csr__in_t  csr_hwif_in;
    openenoc_endpoint_full_csr_pkg::openenoc_endpoint_full_csr__out_t csr_hwif_out;

    openenoc_endpoint_if #(
        .RMEM_TOTAL_DEPTH (openenoc_endpoint_full_csr_pkg::RMEM_TOTAL_DEPTH),
        .NUM_OF_PEERS     (openenoc_endpoint_full_csr_pkg::NUM_OF_PEERS)
    ) endpoint_if (
        .clk (clk),
        .rst (rst)
    );

    openenoc_endpoint_full_csr_bridge u_csr_bridge (
        .csr_hwif_out (csr_hwif_out),
        .csr_hwif_in  (csr_hwif_in),
        .endpoint_if  (endpoint_if),
        .switch_if    (switch_if)
    );

    /*
    * Taxi numbers interfaces from the least-significant concatenation field in the order: DMEM, IMEM, CSR
    */
    localparam AXIL_TARGET_BASE_ADDR = {
        AXIL_ADDR_W'(openenoc_endpoint_full_pkg::CSR_BASE_ADDR),
        AXIL_ADDR_W'(openenoc_endpoint_full_pkg::IMEM_BASE_ADDR),
        AXIL_ADDR_W'(openenoc_endpoint_full_pkg::DMEM_BASE_ADDR)
    };
    localparam AXIL_TARGET_ADDR_W = {
        32'(CSR_ADDR_W),
        32'(IMEM_ADDR_W),
        32'(DMEM_ADDR_W)
    };

    // Check generated memory-map and CSR interface parameters
    if (AXIL_DATA_W !=
            openenoc_endpoint_full_csr_pkg::OPENENOC_ENDPOINT_FULL_CSR_DATA_WIDTH) begin : g_csr_data_width_error
        $fatal(0, "Error: endpoint and CSR data widths do not match (instance %m)");
    end

    if (2**$clog2(openenoc_endpoint_full_pkg::IMEM_DEPTH) !=
            openenoc_endpoint_full_pkg::IMEM_DEPTH) begin : g_imem_depth_error
        $fatal(0, "Error: IMEM depth must be a power of two (instance %m)");
    end

    if (2**$clog2(openenoc_endpoint_full_pkg::DMEM_DEPTH) !=
            openenoc_endpoint_full_pkg::DMEM_DEPTH) begin : g_dmem_depth_error
        $fatal(0, "Error: DMEM depth must be a power of two (instance %m)");
    end

    /*
    * Taxi calls the initiator-facing ports slave interfaces (s_axil_if) and the
    * target-facing ports master interfaces (m_axil_if).
    *
    * Initiator order: PicoRV32, reserved endpoint interface, reserved debug interface
    */
    taxi_axil_if #(
        .DATA_W (AXIL_DATA_W),
        .ADDR_W (AXIL_ADDR_W),
        .STRB_W (AXIL_STRB_W)
    ) s_axil_if[INITIATOR_COUNT]();

    taxi_axil_if #(
        .DATA_W (AXIL_DATA_W),
        .ADDR_W (AXIL_ADDR_W),
        .STRB_W (AXIL_STRB_W)
    ) m_axil_if[TARGET_COUNT]();

    /*
    * Individually named AXI4-Lite interfaces
    */
    taxi_axil_if #(
        .DATA_W (AXIL_DATA_W),
        .ADDR_W (AXIL_ADDR_W),
        .STRB_W (AXIL_STRB_W)
    ) cpu_axil_if();

    taxi_axil_if #(
        .DATA_W (AXIL_DATA_W),
        .ADDR_W (AXIL_ADDR_W),
        .STRB_W (AXIL_STRB_W)
    ) endpoint_axil_if();

    taxi_axil_if #(
        .DATA_W (AXIL_DATA_W),
        .ADDR_W (AXIL_ADDR_W),
        .STRB_W (AXIL_STRB_W)
    ) debug_axil_if();

    taxi_axil_if #(
        .DATA_W (AXIL_DATA_W),
        .ADDR_W (AXIL_ADDR_W),
        .STRB_W (AXIL_STRB_W)
    ) dmem_axil_if();

    taxi_axil_if #(
        .DATA_W (AXIL_DATA_W),
        .ADDR_W (AXIL_ADDR_W),
        .STRB_W (AXIL_STRB_W)
    ) imem_axil_if();

    taxi_axil_if #(
        .DATA_W (AXIL_DATA_W),
        .ADDR_W (AXIL_ADDR_W),
        .STRB_W (AXIL_STRB_W)
    ) csr_axil_if();

    /*
    * AXI4-Lite crossbar interconnect
    */
    openenoc_axil_crossbar #(
        .S_COUNT      (INITIATOR_COUNT),
        .M_COUNT      (TARGET_COUNT),
        .ADDR_W       (AXIL_ADDR_W),
        .M_BASE_ADDR  (AXIL_TARGET_BASE_ADDR),
        .M_ADDR_W     (AXIL_TARGET_ADDR_W),
        .M_CONNECT_RD ({TARGET_COUNT{{INITIATOR_COUNT{1'b1}}}}),
        .M_CONNECT_WR ({TARGET_COUNT{{INITIATOR_COUNT{1'b1}}}})
    )
    u_axil_crossbar (
        .clk       (clk),
        .rst       (rst),
        .s_axil_wr (s_axil_if),
        .s_axil_rd (s_axil_if),
        .m_axil_wr (m_axil_if),
        .m_axil_rd (m_axil_if)
    );

    /*
    * Initiator 0: PicoRV32 unified AXI4-Lite instruction/data master
    */
    logic cpu_trap;

    assign s_axil_if[0].awaddr  = cpu_axil_if.awaddr;
    assign s_axil_if[0].awprot  = cpu_axil_if.awprot;
    assign s_axil_if[0].awuser  = cpu_axil_if.awuser;
    assign s_axil_if[0].awvalid = cpu_axil_if.awvalid;
    assign cpu_axil_if.awready  = s_axil_if[0].awready;

    assign s_axil_if[0].wdata   = cpu_axil_if.wdata;
    assign s_axil_if[0].wstrb   = cpu_axil_if.wstrb;
    assign s_axil_if[0].wuser   = cpu_axil_if.wuser;
    assign s_axil_if[0].wvalid  = cpu_axil_if.wvalid;
    assign cpu_axil_if.wready   = s_axil_if[0].wready;

    assign cpu_axil_if.bresp    = s_axil_if[0].bresp;
    assign cpu_axil_if.buser    = s_axil_if[0].buser;
    assign cpu_axil_if.bvalid   = s_axil_if[0].bvalid;
    assign s_axil_if[0].bready  = cpu_axil_if.bready;

    assign s_axil_if[0].araddr  = cpu_axil_if.araddr;
    assign s_axil_if[0].arprot  = cpu_axil_if.arprot;
    assign s_axil_if[0].aruser  = cpu_axil_if.aruser;
    assign s_axil_if[0].arvalid = cpu_axil_if.arvalid;
    assign cpu_axil_if.arready  = s_axil_if[0].arready;

    assign cpu_axil_if.rdata    = s_axil_if[0].rdata;
    assign cpu_axil_if.rresp    = s_axil_if[0].rresp;
    assign cpu_axil_if.ruser    = s_axil_if[0].ruser;
    assign cpu_axil_if.rvalid   = s_axil_if[0].rvalid;
    assign s_axil_if[0].rready  = cpu_axil_if.rready;

    assign cpu_axil_if.awuser = '0;
    assign cpu_axil_if.wuser  = '0;
    assign cpu_axil_if.aruser = '0;

    openenoc_picorv32 #(
        .PROGADDR_RESET (AXIL_ADDR_W'(openenoc_endpoint_full_pkg::IMEM_BASE_ADDR)),
        .STACKADDR      (AXIL_ADDR_W'(
            openenoc_endpoint_full_pkg::DMEM_BASE_ADDR +
            openenoc_endpoint_full_pkg::DMEM_DEPTH * AXIL_STRB_W
        ))
    )
    u_cpu (
        .clk             (clk),
        .resetn          (!rst),
        .trap            (cpu_trap),

        .mem_axi_awvalid (cpu_axil_if.awvalid),
        .mem_axi_awready (cpu_axil_if.awready),
        .mem_axi_awaddr  (cpu_axil_if.awaddr),
        .mem_axi_awprot  (cpu_axil_if.awprot),
        .mem_axi_wvalid  (cpu_axil_if.wvalid),
        .mem_axi_wready  (cpu_axil_if.wready),
        .mem_axi_wdata   (cpu_axil_if.wdata),
        .mem_axi_wstrb   (cpu_axil_if.wstrb),
        .mem_axi_bvalid  (cpu_axil_if.bvalid),
        .mem_axi_bready  (cpu_axil_if.bready),
        .mem_axi_arvalid (cpu_axil_if.arvalid),
        .mem_axi_arready (cpu_axil_if.arready),
        .mem_axi_araddr  (cpu_axil_if.araddr),
        .mem_axi_arprot  (cpu_axil_if.arprot),
        .mem_axi_rvalid  (cpu_axil_if.rvalid),
        .mem_axi_rready  (cpu_axil_if.rready),
        .mem_axi_rdata   (cpu_axil_if.rdata),

        .pcpi_valid      (),
        .pcpi_insn       (),
        .pcpi_rs1        (),
        .pcpi_rs2        (),
        .pcpi_wr         (1'b0),
        .pcpi_rd         ('0),
        .pcpi_wait       (1'b0),
        .pcpi_ready      (1'b0),
        .irq             ('0),
        .eoi             (),
        .trace_valid     (),
        .trace_data      ()
    );

    /*
    * Initiator 1: reserved endpoint interface master
    */
    assign s_axil_if[1].awaddr      = endpoint_axil_if.awaddr;
    assign s_axil_if[1].awprot      = endpoint_axil_if.awprot;
    assign s_axil_if[1].awuser      = endpoint_axil_if.awuser;
    assign s_axil_if[1].awvalid     = endpoint_axil_if.awvalid;
    assign endpoint_axil_if.awready = s_axil_if[1].awready;

    assign s_axil_if[1].wdata       = endpoint_axil_if.wdata;
    assign s_axil_if[1].wstrb       = endpoint_axil_if.wstrb;
    assign s_axil_if[1].wuser       = endpoint_axil_if.wuser;
    assign s_axil_if[1].wvalid      = endpoint_axil_if.wvalid;
    assign endpoint_axil_if.wready  = s_axil_if[1].wready;

    assign endpoint_axil_if.bresp   = s_axil_if[1].bresp;
    assign endpoint_axil_if.buser   = s_axil_if[1].buser;
    assign endpoint_axil_if.bvalid  = s_axil_if[1].bvalid;
    assign s_axil_if[1].bready      = endpoint_axil_if.bready;

    assign s_axil_if[1].araddr      = endpoint_axil_if.araddr;
    assign s_axil_if[1].arprot      = endpoint_axil_if.arprot;
    assign s_axil_if[1].aruser      = endpoint_axil_if.aruser;
    assign s_axil_if[1].arvalid     = endpoint_axil_if.arvalid;
    assign endpoint_axil_if.arready = s_axil_if[1].arready;

    assign endpoint_axil_if.rdata   = s_axil_if[1].rdata;
    assign endpoint_axil_if.rresp   = s_axil_if[1].rresp;
    assign endpoint_axil_if.ruser   = s_axil_if[1].ruser;
    assign endpoint_axil_if.rvalid  = s_axil_if[1].rvalid;
    assign s_axil_if[1].rready      = endpoint_axil_if.rready;

    openenoc_endpoint_interface u_endpoint_interface (
        .clk         (clk),
        .rst         (rst),
        .endpoint_if (endpoint_if),
        .eth_if      (eth_if),
        .m_axil_wr   (endpoint_axil_if),
        .m_axil_rd   (endpoint_axil_if)
    );

    /*
    * Initiator 2: reserved debug/program master
    */
    assign s_axil_if[2].awaddr   = debug_axil_if.awaddr;
    assign s_axil_if[2].awprot   = debug_axil_if.awprot;
    assign s_axil_if[2].awuser   = debug_axil_if.awuser;
    assign s_axil_if[2].awvalid  = debug_axil_if.awvalid;
    assign debug_axil_if.awready = s_axil_if[2].awready;

    assign s_axil_if[2].wdata    = debug_axil_if.wdata;
    assign s_axil_if[2].wstrb    = debug_axil_if.wstrb;
    assign s_axil_if[2].wuser    = debug_axil_if.wuser;
    assign s_axil_if[2].wvalid   = debug_axil_if.wvalid;
    assign debug_axil_if.wready  = s_axil_if[2].wready;

    assign debug_axil_if.bresp   = s_axil_if[2].bresp;
    assign debug_axil_if.buser   = s_axil_if[2].buser;
    assign debug_axil_if.bvalid  = s_axil_if[2].bvalid;
    assign s_axil_if[2].bready   = debug_axil_if.bready;

    assign s_axil_if[2].araddr   = debug_axil_if.araddr;
    assign s_axil_if[2].arprot   = debug_axil_if.arprot;
    assign s_axil_if[2].aruser   = debug_axil_if.aruser;
    assign s_axil_if[2].arvalid  = debug_axil_if.arvalid;
    assign debug_axil_if.arready = s_axil_if[2].arready;

    assign debug_axil_if.rdata   = s_axil_if[2].rdata;
    assign debug_axil_if.rresp   = s_axil_if[2].rresp;
    assign debug_axil_if.ruser   = s_axil_if[2].ruser;
    assign debug_axil_if.rvalid  = s_axil_if[2].rvalid;
    assign s_axil_if[2].rready   = debug_axil_if.rready;

    assign debug_axil_if.awaddr  = '0;
    assign debug_axil_if.awprot  = '0;
    assign debug_axil_if.awuser  = '0;
    assign debug_axil_if.awvalid = 1'b0;
    assign debug_axil_if.wdata   = '0;
    assign debug_axil_if.wstrb   = '0;
    assign debug_axil_if.wuser   = '0;
    assign debug_axil_if.wvalid  = 1'b0;
    assign debug_axil_if.bready  = 1'b0;
    assign debug_axil_if.araddr  = '0;
    assign debug_axil_if.arprot  = '0;
    assign debug_axil_if.aruser  = '0;
    assign debug_axil_if.arvalid = 1'b0;
    assign debug_axil_if.rready  = 1'b0;

    /*
    * Target 0: data memory
    */
    assign dmem_axil_if.awaddr   = m_axil_if[0].awaddr;
    assign dmem_axil_if.awprot   = m_axil_if[0].awprot;
    assign dmem_axil_if.awuser   = m_axil_if[0].awuser;
    assign dmem_axil_if.awvalid  = m_axil_if[0].awvalid;
    assign m_axil_if[0].awready  = dmem_axil_if.awready;

    assign dmem_axil_if.wdata    = m_axil_if[0].wdata;
    assign dmem_axil_if.wstrb    = m_axil_if[0].wstrb;
    assign dmem_axil_if.wuser    = m_axil_if[0].wuser;
    assign dmem_axil_if.wvalid   = m_axil_if[0].wvalid;
    assign m_axil_if[0].wready   = dmem_axil_if.wready;

    assign m_axil_if[0].bresp    = dmem_axil_if.bresp;
    assign m_axil_if[0].buser    = dmem_axil_if.buser;
    assign m_axil_if[0].bvalid   = dmem_axil_if.bvalid;
    assign dmem_axil_if.bready   = m_axil_if[0].bready;

    assign dmem_axil_if.araddr   = m_axil_if[0].araddr;
    assign dmem_axil_if.arprot   = m_axil_if[0].arprot;
    assign dmem_axil_if.aruser   = m_axil_if[0].aruser;
    assign dmem_axil_if.arvalid  = m_axil_if[0].arvalid;
    assign m_axil_if[0].arready  = dmem_axil_if.arready;

    assign m_axil_if[0].rdata    = dmem_axil_if.rdata;
    assign m_axil_if[0].rresp    = dmem_axil_if.rresp;
    assign m_axil_if[0].ruser    = dmem_axil_if.ruser;
    assign m_axil_if[0].rvalid   = dmem_axil_if.rvalid;
    assign dmem_axil_if.rready   = m_axil_if[0].rready;

    openenoc_axil_ram #(
        .ADDR_W    (DMEM_ADDR_W),
        .INIT_FILE (DMEM_INIT_FILE)
    )
    u_dmem (
        .clk       (clk),
        .rst       (rst),
        .s_axil_wr (dmem_axil_if),
        .s_axil_rd (dmem_axil_if)
    );

    /*
    * Target 1: instruction memory
    */
    assign imem_axil_if.awaddr   = m_axil_if[1].awaddr;
    assign imem_axil_if.awprot   = m_axil_if[1].awprot;
    assign imem_axil_if.awuser   = m_axil_if[1].awuser;
    assign imem_axil_if.awvalid  = m_axil_if[1].awvalid;
    assign m_axil_if[1].awready  = imem_axil_if.awready;

    assign imem_axil_if.wdata    = m_axil_if[1].wdata;
    assign imem_axil_if.wstrb    = m_axil_if[1].wstrb;
    assign imem_axil_if.wuser    = m_axil_if[1].wuser;
    assign imem_axil_if.wvalid   = m_axil_if[1].wvalid;
    assign m_axil_if[1].wready   = imem_axil_if.wready;

    assign m_axil_if[1].bresp    = imem_axil_if.bresp;
    assign m_axil_if[1].buser    = imem_axil_if.buser;
    assign m_axil_if[1].bvalid   = imem_axil_if.bvalid;
    assign imem_axil_if.bready   = m_axil_if[1].bready;

    assign imem_axil_if.araddr   = m_axil_if[1].araddr;
    assign imem_axil_if.arprot   = m_axil_if[1].arprot;
    assign imem_axil_if.aruser   = m_axil_if[1].aruser;
    assign imem_axil_if.arvalid  = m_axil_if[1].arvalid;
    assign m_axil_if[1].arready  = imem_axil_if.arready;

    assign m_axil_if[1].rdata    = imem_axil_if.rdata;
    assign m_axil_if[1].rresp    = imem_axil_if.rresp;
    assign m_axil_if[1].ruser    = imem_axil_if.ruser;
    assign m_axil_if[1].rvalid   = imem_axil_if.rvalid;
    assign imem_axil_if.rready   = m_axil_if[1].rready;

    openenoc_axil_ram #(
        .ADDR_W    (IMEM_ADDR_W),
        .INIT_FILE (IMEM_INIT_FILE)
    )
    u_imem (
        .clk       (clk),
        .rst       (rst),
        .s_axil_wr (imem_axil_if),
        .s_axil_rd (imem_axil_if)
    );

    /*
    * Target 2: generated CSR block
    */
    assign csr_axil_if.awaddr   = m_axil_if[2].awaddr;
    assign csr_axil_if.awprot   = m_axil_if[2].awprot;
    assign csr_axil_if.awuser   = m_axil_if[2].awuser;
    assign csr_axil_if.awvalid  = m_axil_if[2].awvalid;
    assign m_axil_if[2].awready = csr_axil_if.awready;

    assign csr_axil_if.wdata    = m_axil_if[2].wdata;
    assign csr_axil_if.wstrb    = m_axil_if[2].wstrb;
    assign csr_axil_if.wuser    = m_axil_if[2].wuser;
    assign csr_axil_if.wvalid   = m_axil_if[2].wvalid;
    assign m_axil_if[2].wready  = csr_axil_if.wready;

    assign m_axil_if[2].bresp   = csr_axil_if.bresp;
    assign m_axil_if[2].buser   = csr_axil_if.buser;
    assign m_axil_if[2].bvalid  = csr_axil_if.bvalid;
    assign csr_axil_if.bready   = m_axil_if[2].bready;

    assign csr_axil_if.araddr   = m_axil_if[2].araddr;
    assign csr_axil_if.arprot   = m_axil_if[2].arprot;
    assign csr_axil_if.aruser   = m_axil_if[2].aruser;
    assign csr_axil_if.arvalid  = m_axil_if[2].arvalid;
    assign m_axil_if[2].arready = csr_axil_if.arready;

    assign m_axil_if[2].rdata   = csr_axil_if.rdata;
    assign m_axil_if[2].rresp   = csr_axil_if.rresp;
    assign m_axil_if[2].ruser   = csr_axil_if.ruser;
    assign m_axil_if[2].rvalid  = csr_axil_if.rvalid;
    assign csr_axil_if.rready   = m_axil_if[2].rready;

    assign csr_axil_if.buser = '0;
    assign csr_axil_if.ruser = '0;

    openenoc_endpoint_full_csr u_csr (
        .clk            (clk),
        .rst            (rst),

        .s_axil_awready (csr_axil_if.awready),
        .s_axil_awvalid (csr_axil_if.awvalid),
        .s_axil_awaddr  (csr_axil_if.awaddr[CSR_ADDR_W-1:0]),
        .s_axil_awprot  (csr_axil_if.awprot),
        .s_axil_wready  (csr_axil_if.wready),
        .s_axil_wvalid  (csr_axil_if.wvalid),
        .s_axil_wdata   (csr_axil_if.wdata),
        .s_axil_wstrb   (csr_axil_if.wstrb),
        .s_axil_bready  (csr_axil_if.bready),
        .s_axil_bvalid  (csr_axil_if.bvalid),
        .s_axil_bresp   (csr_axil_if.bresp),
        .s_axil_arready (csr_axil_if.arready),
        .s_axil_arvalid (csr_axil_if.arvalid),
        .s_axil_araddr  (csr_axil_if.araddr[CSR_ADDR_W-1:0]),
        .s_axil_arprot  (csr_axil_if.arprot),
        .s_axil_rready  (csr_axil_if.rready),
        .s_axil_rvalid  (csr_axil_if.rvalid),
        .s_axil_rdata   (csr_axil_if.rdata),
        .s_axil_rresp   (csr_axil_if.rresp),

        .hwif_in        (csr_hwif_in),
        .hwif_out       (csr_hwif_out)
    );

endmodule

`resetall
