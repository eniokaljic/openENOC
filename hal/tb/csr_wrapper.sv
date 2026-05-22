module csr_wrapper;

    import csr_pkg::*;

    //
    // Clock / reset
    //
    logic clk;
    logic rst;

    //
    // AXI-Lite slave signals
    //
    logic        s_axil_awready;
    logic        s_axil_awvalid;
    logic [2:0]  s_axil_awaddr;
    logic [2:0]  s_axil_awprot;

    logic        s_axil_wready;
    logic        s_axil_wvalid;
    logic [31:0] s_axil_wdata;
    logic [3:0]  s_axil_wstrb;

    logic        s_axil_bready;
    logic        s_axil_bvalid;
    logic [1:0]  s_axil_bresp;

    logic        s_axil_arready;
    logic        s_axil_arvalid;
    logic [2:0]  s_axil_araddr;
    logic [2:0]  s_axil_arprot;

    logic        s_axil_rready;
    logic        s_axil_rvalid;
    logic [31:0] s_axil_rdata;
    logic [1:0]  s_axil_rresp;

    //
    // Hardware interface structs
    //
    //csr__in_t  hwif_in;
    csr__out_t hwif_out;

    //
    // DUT
    //
    csr dut (
        .clk(clk),
        .rst(rst),

        .s_axil_awready(s_axil_awready),
        .s_axil_awvalid(s_axil_awvalid),
        .s_axil_awaddr(s_axil_awaddr),
        .s_axil_awprot(s_axil_awprot),

        .s_axil_wready(s_axil_wready),
        .s_axil_wvalid(s_axil_wvalid),
        .s_axil_wdata(s_axil_wdata),
        .s_axil_wstrb(s_axil_wstrb),

        .s_axil_bready(s_axil_bready),
        .s_axil_bvalid(s_axil_bvalid),
        .s_axil_bresp(s_axil_bresp),

        .s_axil_arready(s_axil_arready),
        .s_axil_arvalid(s_axil_arvalid),
        .s_axil_araddr(s_axil_araddr),
        .s_axil_arprot(s_axil_arprot),

        .s_axil_rready(s_axil_rready),
        .s_axil_rvalid(s_axil_rvalid),
        .s_axil_rdata(s_axil_rdata),
        .s_axil_rresp(s_axil_rresp),

        //.hwif_in(hwif_in),
        .hwif_out(hwif_out)
    );

endmodule

