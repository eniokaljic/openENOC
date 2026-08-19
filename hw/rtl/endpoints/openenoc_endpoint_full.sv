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
    openenoc_eth_if eth
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

    // The endpoint datapath is not implemented yet, so its CSR status inputs are idle
    assign endpoint_if.core_to_csr = '{default: '0};

    openenoc_endpoint_full_csr_bridge csr_bridge_inst (
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
    * Taxi calls the initiator-facing ports slave interfaces (s_axil) and the
    * target-facing ports master interfaces (m_axil).
    *
    * Initiator order: PicoRV32, reserved endpoint interface, reserved debug interface
    */
    taxi_axil_if #(
        .DATA_W (AXIL_DATA_W),
        .ADDR_W (AXIL_ADDR_W),
        .STRB_W (AXIL_STRB_W)
    ) s_axil[INITIATOR_COUNT]();

    taxi_axil_if #(
        .DATA_W (AXIL_DATA_W),
        .ADDR_W (AXIL_ADDR_W),
        .STRB_W (AXIL_STRB_W)
    ) m_axil[TARGET_COUNT]();

    /*
    * Individually named AXI4-Lite interfaces
    */
    taxi_axil_if #(
        .DATA_W (AXIL_DATA_W),
        .ADDR_W (AXIL_ADDR_W),
        .STRB_W (AXIL_STRB_W)
    ) cpu_axil();

    taxi_axil_if #(
        .DATA_W (AXIL_DATA_W),
        .ADDR_W (AXIL_ADDR_W),
        .STRB_W (AXIL_STRB_W)
    ) endpoint_axil();

    taxi_axil_if #(
        .DATA_W (AXIL_DATA_W),
        .ADDR_W (AXIL_ADDR_W),
        .STRB_W (AXIL_STRB_W)
    ) debug_axil();

    taxi_axil_if #(
        .DATA_W (AXIL_DATA_W),
        .ADDR_W (AXIL_ADDR_W),
        .STRB_W (AXIL_STRB_W)
    ) dmem_axil();

    taxi_axil_if #(
        .DATA_W (AXIL_DATA_W),
        .ADDR_W (AXIL_ADDR_W),
        .STRB_W (AXIL_STRB_W)
    ) imem_axil();

    taxi_axil_if #(
        .DATA_W (AXIL_DATA_W),
        .ADDR_W (AXIL_ADDR_W),
        .STRB_W (AXIL_STRB_W)
    ) csr_axil();

    /*
    * AXI4-Lite crossbar interconnect
    */
    taxi_axil_crossbar #(
        .S_COUNT      (INITIATOR_COUNT),
        .M_COUNT      (TARGET_COUNT),
        .ADDR_W       (AXIL_ADDR_W),
        .M_BASE_ADDR  (AXIL_TARGET_BASE_ADDR),
        .M_ADDR_W     (AXIL_TARGET_ADDR_W),
        .M_CONNECT_RD ({TARGET_COUNT{{INITIATOR_COUNT{1'b1}}}}),
        .M_CONNECT_WR ({TARGET_COUNT{{INITIATOR_COUNT{1'b1}}}})
    )
    axil_crossbar_inst (
        .clk       (clk),
        .rst       (rst),
        .s_axil_wr (s_axil),
        .s_axil_rd (s_axil),
        .m_axil_wr (m_axil),
        .m_axil_rd (m_axil)
    );

    /*
    * Initiator 0: PicoRV32 unified AXI4-Lite instruction/data master
    */
    logic cpu_trap;

    assign s_axil[0].awaddr  = cpu_axil.awaddr;
    assign s_axil[0].awprot  = cpu_axil.awprot;
    assign s_axil[0].awuser  = cpu_axil.awuser;
    assign s_axil[0].awvalid = cpu_axil.awvalid;
    assign cpu_axil.awready  = s_axil[0].awready;

    assign s_axil[0].wdata   = cpu_axil.wdata;
    assign s_axil[0].wstrb   = cpu_axil.wstrb;
    assign s_axil[0].wuser   = cpu_axil.wuser;
    assign s_axil[0].wvalid  = cpu_axil.wvalid;
    assign cpu_axil.wready   = s_axil[0].wready;

    assign cpu_axil.bresp    = s_axil[0].bresp;
    assign cpu_axil.buser    = s_axil[0].buser;
    assign cpu_axil.bvalid   = s_axil[0].bvalid;
    assign s_axil[0].bready  = cpu_axil.bready;

    assign s_axil[0].araddr  = cpu_axil.araddr;
    assign s_axil[0].arprot  = cpu_axil.arprot;
    assign s_axil[0].aruser  = cpu_axil.aruser;
    assign s_axil[0].arvalid = cpu_axil.arvalid;
    assign cpu_axil.arready  = s_axil[0].arready;

    assign cpu_axil.rdata    = s_axil[0].rdata;
    assign cpu_axil.rresp    = s_axil[0].rresp;
    assign cpu_axil.ruser    = s_axil[0].ruser;
    assign cpu_axil.rvalid   = s_axil[0].rvalid;
    assign s_axil[0].rready  = cpu_axil.rready;

    assign cpu_axil.awuser = '0;
    assign cpu_axil.wuser  = '0;
    assign cpu_axil.aruser = '0;

    picorv32_axi #(
        .PROGADDR_RESET (AXIL_ADDR_W'(openenoc_endpoint_full_pkg::IMEM_BASE_ADDR)),
        .STACKADDR      (AXIL_ADDR_W'(
            openenoc_endpoint_full_pkg::DMEM_BASE_ADDR +
            openenoc_endpoint_full_pkg::DMEM_DEPTH * AXIL_STRB_W
        ))
    )
    cpu_inst (
        .clk             (clk),
        .resetn          (!rst),
        .trap            (cpu_trap),

        .mem_axi_awvalid (cpu_axil.awvalid),
        .mem_axi_awready (cpu_axil.awready),
        .mem_axi_awaddr  (cpu_axil.awaddr),
        .mem_axi_awprot  (cpu_axil.awprot),
        .mem_axi_wvalid  (cpu_axil.wvalid),
        .mem_axi_wready  (cpu_axil.wready),
        .mem_axi_wdata   (cpu_axil.wdata),
        .mem_axi_wstrb   (cpu_axil.wstrb),
        .mem_axi_bvalid  (cpu_axil.bvalid),
        .mem_axi_bready  (cpu_axil.bready),
        .mem_axi_arvalid (cpu_axil.arvalid),
        .mem_axi_arready (cpu_axil.arready),
        .mem_axi_araddr  (cpu_axil.araddr),
        .mem_axi_arprot  (cpu_axil.arprot),
        .mem_axi_rvalid  (cpu_axil.rvalid),
        .mem_axi_rready  (cpu_axil.rready),
        .mem_axi_rdata   (cpu_axil.rdata),

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
    assign s_axil[1].awaddr      = endpoint_axil.awaddr;
    assign s_axil[1].awprot      = endpoint_axil.awprot;
    assign s_axil[1].awuser      = endpoint_axil.awuser;
    assign s_axil[1].awvalid     = endpoint_axil.awvalid;
    assign endpoint_axil.awready = s_axil[1].awready;

    assign s_axil[1].wdata       = endpoint_axil.wdata;
    assign s_axil[1].wstrb       = endpoint_axil.wstrb;
    assign s_axil[1].wuser       = endpoint_axil.wuser;
    assign s_axil[1].wvalid      = endpoint_axil.wvalid;
    assign endpoint_axil.wready  = s_axil[1].wready;

    assign endpoint_axil.bresp   = s_axil[1].bresp;
    assign endpoint_axil.buser   = s_axil[1].buser;
    assign endpoint_axil.bvalid  = s_axil[1].bvalid;
    assign s_axil[1].bready      = endpoint_axil.bready;

    assign s_axil[1].araddr      = endpoint_axil.araddr;
    assign s_axil[1].arprot      = endpoint_axil.arprot;
    assign s_axil[1].aruser      = endpoint_axil.aruser;
    assign s_axil[1].arvalid     = endpoint_axil.arvalid;
    assign endpoint_axil.arready = s_axil[1].arready;

    assign endpoint_axil.rdata   = s_axil[1].rdata;
    assign endpoint_axil.rresp   = s_axil[1].rresp;
    assign endpoint_axil.ruser   = s_axil[1].ruser;
    assign endpoint_axil.rvalid  = s_axil[1].rvalid;
    assign s_axil[1].rready      = endpoint_axil.rready;

    assign endpoint_axil.awaddr  = '0;
    assign endpoint_axil.awprot  = '0;
    assign endpoint_axil.awuser  = '0;
    assign endpoint_axil.awvalid = 1'b0;
    assign endpoint_axil.wdata   = '0;
    assign endpoint_axil.wstrb   = '0;
    assign endpoint_axil.wuser   = '0;
    assign endpoint_axil.wvalid  = 1'b0;
    assign endpoint_axil.bready  = 1'b0;
    assign endpoint_axil.araddr  = '0;
    assign endpoint_axil.arprot  = '0;
    assign endpoint_axil.aruser  = '0;
    assign endpoint_axil.arvalid = 1'b0;
    assign endpoint_axil.rready  = 1'b0;

    /*
    * Initiator 2: reserved debug/program master
    */
    assign s_axil[2].awaddr   = debug_axil.awaddr;
    assign s_axil[2].awprot   = debug_axil.awprot;
    assign s_axil[2].awuser   = debug_axil.awuser;
    assign s_axil[2].awvalid  = debug_axil.awvalid;
    assign debug_axil.awready = s_axil[2].awready;

    assign s_axil[2].wdata    = debug_axil.wdata;
    assign s_axil[2].wstrb    = debug_axil.wstrb;
    assign s_axil[2].wuser    = debug_axil.wuser;
    assign s_axil[2].wvalid   = debug_axil.wvalid;
    assign debug_axil.wready  = s_axil[2].wready;

    assign debug_axil.bresp   = s_axil[2].bresp;
    assign debug_axil.buser   = s_axil[2].buser;
    assign debug_axil.bvalid  = s_axil[2].bvalid;
    assign s_axil[2].bready   = debug_axil.bready;

    assign s_axil[2].araddr   = debug_axil.araddr;
    assign s_axil[2].arprot   = debug_axil.arprot;
    assign s_axil[2].aruser   = debug_axil.aruser;
    assign s_axil[2].arvalid  = debug_axil.arvalid;
    assign debug_axil.arready = s_axil[2].arready;

    assign debug_axil.rdata   = s_axil[2].rdata;
    assign debug_axil.rresp   = s_axil[2].rresp;
    assign debug_axil.ruser   = s_axil[2].ruser;
    assign debug_axil.rvalid  = s_axil[2].rvalid;
    assign s_axil[2].rready   = debug_axil.rready;

    assign debug_axil.awaddr  = '0;
    assign debug_axil.awprot  = '0;
    assign debug_axil.awuser  = '0;
    assign debug_axil.awvalid = 1'b0;
    assign debug_axil.wdata   = '0;
    assign debug_axil.wstrb   = '0;
    assign debug_axil.wuser   = '0;
    assign debug_axil.wvalid  = 1'b0;
    assign debug_axil.bready  = 1'b0;
    assign debug_axil.araddr  = '0;
    assign debug_axil.arprot  = '0;
    assign debug_axil.aruser  = '0;
    assign debug_axil.arvalid = 1'b0;
    assign debug_axil.rready  = 1'b0;

    /*
    * Target 0: data memory
    */
    assign dmem_axil.awaddr   = m_axil[0].awaddr;
    assign dmem_axil.awprot   = m_axil[0].awprot;
    assign dmem_axil.awuser   = m_axil[0].awuser;
    assign dmem_axil.awvalid  = m_axil[0].awvalid;
    assign m_axil[0].awready  = dmem_axil.awready;

    assign dmem_axil.wdata    = m_axil[0].wdata;
    assign dmem_axil.wstrb    = m_axil[0].wstrb;
    assign dmem_axil.wuser    = m_axil[0].wuser;
    assign dmem_axil.wvalid   = m_axil[0].wvalid;
    assign m_axil[0].wready   = dmem_axil.wready;

    assign m_axil[0].bresp    = dmem_axil.bresp;
    assign m_axil[0].buser    = dmem_axil.buser;
    assign m_axil[0].bvalid   = dmem_axil.bvalid;
    assign dmem_axil.bready   = m_axil[0].bready;

    assign dmem_axil.araddr   = m_axil[0].araddr;
    assign dmem_axil.arprot   = m_axil[0].arprot;
    assign dmem_axil.aruser   = m_axil[0].aruser;
    assign dmem_axil.arvalid  = m_axil[0].arvalid;
    assign m_axil[0].arready  = dmem_axil.arready;

    assign m_axil[0].rdata    = dmem_axil.rdata;
    assign m_axil[0].rresp    = dmem_axil.rresp;
    assign m_axil[0].ruser    = dmem_axil.ruser;
    assign m_axil[0].rvalid   = dmem_axil.rvalid;
    assign dmem_axil.rready   = m_axil[0].rready;

    openenoc_axil_ram #(
        .ADDR_W    (DMEM_ADDR_W),
        .INIT_FILE (DMEM_INIT_FILE)
    )
    dmem_inst (
        .clk       (clk),
        .rst       (rst),
        .s_axil_wr (dmem_axil),
        .s_axil_rd (dmem_axil)
    );

    /*
    * Target 1: instruction memory
    */
    assign imem_axil.awaddr   = m_axil[1].awaddr;
    assign imem_axil.awprot   = m_axil[1].awprot;
    assign imem_axil.awuser   = m_axil[1].awuser;
    assign imem_axil.awvalid  = m_axil[1].awvalid;
    assign m_axil[1].awready  = imem_axil.awready;

    assign imem_axil.wdata    = m_axil[1].wdata;
    assign imem_axil.wstrb    = m_axil[1].wstrb;
    assign imem_axil.wuser    = m_axil[1].wuser;
    assign imem_axil.wvalid   = m_axil[1].wvalid;
    assign m_axil[1].wready   = imem_axil.wready;

    assign m_axil[1].bresp    = imem_axil.bresp;
    assign m_axil[1].buser    = imem_axil.buser;
    assign m_axil[1].bvalid   = imem_axil.bvalid;
    assign imem_axil.bready   = m_axil[1].bready;

    assign imem_axil.araddr   = m_axil[1].araddr;
    assign imem_axil.arprot   = m_axil[1].arprot;
    assign imem_axil.aruser   = m_axil[1].aruser;
    assign imem_axil.arvalid  = m_axil[1].arvalid;
    assign m_axil[1].arready  = imem_axil.arready;

    assign m_axil[1].rdata    = imem_axil.rdata;
    assign m_axil[1].rresp    = imem_axil.rresp;
    assign m_axil[1].ruser    = imem_axil.ruser;
    assign m_axil[1].rvalid   = imem_axil.rvalid;
    assign imem_axil.rready   = m_axil[1].rready;

    openenoc_axil_ram #(
        .ADDR_W    (IMEM_ADDR_W),
        .INIT_FILE (IMEM_INIT_FILE)
    )
    imem_inst (
        .clk       (clk),
        .rst       (rst),
        .s_axil_wr (imem_axil),
        .s_axil_rd (imem_axil)
    );

    /*
    * Target 2: generated CSR block
    */
    assign csr_axil.awaddr   = m_axil[2].awaddr;
    assign csr_axil.awprot   = m_axil[2].awprot;
    assign csr_axil.awuser   = m_axil[2].awuser;
    assign csr_axil.awvalid  = m_axil[2].awvalid;
    assign m_axil[2].awready = csr_axil.awready;

    assign csr_axil.wdata    = m_axil[2].wdata;
    assign csr_axil.wstrb    = m_axil[2].wstrb;
    assign csr_axil.wuser    = m_axil[2].wuser;
    assign csr_axil.wvalid   = m_axil[2].wvalid;
    assign m_axil[2].wready  = csr_axil.wready;

    assign m_axil[2].bresp   = csr_axil.bresp;
    assign m_axil[2].buser   = csr_axil.buser;
    assign m_axil[2].bvalid  = csr_axil.bvalid;
    assign csr_axil.bready   = m_axil[2].bready;

    assign csr_axil.araddr   = m_axil[2].araddr;
    assign csr_axil.arprot   = m_axil[2].arprot;
    assign csr_axil.aruser   = m_axil[2].aruser;
    assign csr_axil.arvalid  = m_axil[2].arvalid;
    assign m_axil[2].arready = csr_axil.arready;

    assign m_axil[2].rdata   = csr_axil.rdata;
    assign m_axil[2].rresp   = csr_axil.rresp;
    assign m_axil[2].ruser   = csr_axil.ruser;
    assign m_axil[2].rvalid  = csr_axil.rvalid;
    assign csr_axil.rready   = m_axil[2].rready;

    assign csr_axil.buser = '0;
    assign csr_axil.ruser = '0;

    openenoc_endpoint_full_csr csr_inst (
        .clk            (clk),
        .rst            (rst),

        .s_axil_awready (csr_axil.awready),
        .s_axil_awvalid (csr_axil.awvalid),
        .s_axil_awaddr  (csr_axil.awaddr[CSR_ADDR_W-1:0]),
        .s_axil_awprot  (csr_axil.awprot),
        .s_axil_wready  (csr_axil.wready),
        .s_axil_wvalid  (csr_axil.wvalid),
        .s_axil_wdata   (csr_axil.wdata),
        .s_axil_wstrb   (csr_axil.wstrb),
        .s_axil_bready  (csr_axil.bready),
        .s_axil_bvalid  (csr_axil.bvalid),
        .s_axil_bresp   (csr_axil.bresp),
        .s_axil_arready (csr_axil.arready),
        .s_axil_arvalid (csr_axil.arvalid),
        .s_axil_araddr  (csr_axil.araddr[CSR_ADDR_W-1:0]),
        .s_axil_arprot  (csr_axil.arprot),
        .s_axil_rready  (csr_axil.rready),
        .s_axil_rvalid  (csr_axil.rvalid),
        .s_axil_rdata   (csr_axil.rdata),
        .s_axil_rresp   (csr_axil.rresp),

        .hwif_in        (csr_hwif_in),
        .hwif_out       (csr_hwif_out)
    );

    /*
    * TODO: implement openENOC endpoint interface. The endpoint owns side A: a2b is its
    * transmit direction and b2a is its receive direction.
    */
    assign eth.a2b.tdata  = '0;
    assign eth.a2b.tkeep  = '0;
    assign eth.a2b.tstrb  = '0;
    assign eth.a2b.tid    = '0;
    assign eth.a2b.tdest  = '0;
    assign eth.a2b.tuser  = '0;
    assign eth.a2b.tlast  = 1'b0;
    assign eth.a2b.tvalid = 1'b0;
    assign eth.b2a.tready = 1'b0;

endmodule

`resetall
