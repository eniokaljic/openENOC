// SPDX-FileCopyrightText: 2026 Kerim Bavcic
// SPDX-License-Identifier: CERN-OHL-S-2.0

`resetall
`timescale 1ns / 1ps
`default_nettype none

/*
 * openENOC forwarding table (CAM + RAM)
 */
module openenoc_forwarding_table #
(
    parameter int NUM_OF_INTERFACES = 8,
    parameter int TABLE_DEPTH       = 32,
    // derived, not intended to be set manually
    localparam int ENTRY_BYTES      = 16,
    localparam int ADDR_WIDTH       = $clog2(TABLE_DEPTH * ENTRY_BYTES)
)
(
    input  wire logic                         clk,
    input  wire logic                         rst,

    input  wire logic [NUM_OF_INTERFACES-1:0] default_forwarding,
    input  wire logic                         operation_mode,

    /*
     * CPU interface (openENOC Switch Interface CSR, external regfile)
     */
    input  wire logic                         cpuif_req,
    input  wire logic [ADDR_WIDTH-1:0]        cpuif_addr,
    input  wire logic                         cpuif_req_is_wr,
    input  wire logic [31:0]                  cpuif_wr_data,
    input  wire logic [31:0]                  cpuif_wr_biten,

    output logic                              cpuif_wr_ack,
    output logic                              cpuif_rd_ack,
    output logic [31:0]                       cpuif_rd_data,

    /*
     * Lookup interface
     */
    openenoc_lookup_if.slv                    lookup_if,

    /*
     * Learning interface
     */
    openenoc_learning_if.slv                  learning_if
);

    // ---------------------------------------------------------------------------
    // parameters
    // ---------------------------------------------------------------------------
    localparam int MAC_W = 48;
    localparam int IDX_W = (TABLE_DEPTH > 1) ? $clog2(TABLE_DEPTH) : 1;

    // 32-bit word select within a forwarding table entry
    localparam logic [1:0] WORD_MAC_LO = 2'd0;
    localparam logic [1:0] WORD_MAC_HI = 2'd1;
    localparam logic [1:0] WORD_IFACE  = 2'd2;
    localparam logic [1:0] WORD_CONFIG = 2'd3;

    // check configuration
    /* verilator lint_off GENUNNAMED */
    if (NUM_OF_INTERFACES < 1 || NUM_OF_INTERFACES > 32)
        $fatal(0, "Error: NUM_OF_INTERFACES must be in range 1 to 32 (instance %m)");

    if (TABLE_DEPTH < 1)
        $fatal(0, "Error: TABLE_DEPTH must be at least 1 (instance %m)");
    /* verilator lint_on GENUNNAMED */

    // ---------------------------------------------------------------------------
    // table storage
    // ---------------------------------------------------------------------------
    logic [MAC_W-1:0]             cam_mac[TABLE_DEPTH];
    logic [NUM_OF_INTERFACES-1:0] ram_bitmap[TABLE_DEPTH];
    logic [TABLE_DEPTH-1:0]       entry_en;

    // circular write pointer used by the learning process
    logic [IDX_W-1:0] learn_ptr;

    // ---------------------------------------------------------------------------
    // request snapshots, taken while the corresponding *_req strobe is asserted
    // ---------------------------------------------------------------------------
    logic                  cpu_pending;
    logic [ADDR_WIDTH-1:0] cpu_addr;
    logic                  cpu_is_wr;
    logic [31:0]           cpu_wr_data;
    logic [31:0]           cpu_wr_biten;

    logic             lookup_pending;
    logic [MAC_W-1:0] lookup_mac;

    logic                         learn_pending;
    logic [MAC_W-1:0]             learn_mac;
    logic [NUM_OF_INTERFACES-1:0] learn_bitmap;

    // delayed request strobes, used for rising edge detection
    logic cpuif_req_d;
    logic lookup_req_d;
    logic learning_req_d;

    // ---------------------------------------------------------------------------
    // CAM compare
    // ---------------------------------------------------------------------------
    logic             lookup_hit;
    logic [IDX_W-1:0] lookup_hit_idx;
    logic             learn_hit;
    logic [IDX_W-1:0] learn_hit_idx;

    // lowest matching index wins (loop counts down, so index 0 assigns last)
    always_comb begin
        lookup_hit     = 1'b0;
        lookup_hit_idx = '0;
        learn_hit      = 1'b0;
        learn_hit_idx  = '0;

        for (int i = TABLE_DEPTH-1; i >= 0; i--) begin
            if (entry_en[i] && (cam_mac[i] == lookup_mac)) begin
                lookup_hit     = 1'b1;
                lookup_hit_idx = IDX_W'(i);
            end
            if (entry_en[i] && (cam_mac[i] == learn_mac)) begin
                learn_hit     = 1'b1;
                learn_hit_idx = IDX_W'(i);
            end
        end
    end

    // ---------------------------------------------------------------------------
    // CPU access decode
    // ---------------------------------------------------------------------------

    // zero extended so that the entry index slice stays in range for any depth,
    // the padding and the byte offset bits [1:0] are unused by design
    /* verilator lint_off UNUSEDSIGNAL */
    logic [ADDR_WIDTH+IDX_W-1:0] cpu_addr_ext;
    /* verilator lint_on UNUSEDSIGNAL */
    logic [IDX_W-1:0]            cpu_idx;
    logic [1:0]                  cpu_word;
    logic                        cpu_idx_valid;

    assign cpu_addr_ext  = {{IDX_W{1'b0}}, cpu_addr};
    assign cpu_idx       = cpu_addr_ext[4 +: IDX_W];
    assign cpu_word      = cpu_addr[3:2];
    assign cpu_idx_valid = (32'(cpu_idx) < TABLE_DEPTH);

    always_comb begin
        cpuif_rd_data = 32'd0;
        if (cpu_idx_valid) begin
            case (cpu_word)
                WORD_MAC_LO: cpuif_rd_data = cam_mac[cpu_idx][31:0];
                WORD_MAC_HI: cpuif_rd_data = 32'(cam_mac[cpu_idx][MAC_W-1:32]);
                WORD_IFACE:  cpuif_rd_data = 32'(ram_bitmap[cpu_idx]);
                WORD_CONFIG: cpuif_rd_data = 32'(entry_en[cpu_idx]);
                default:     cpuif_rd_data = 32'd0;
            endcase
        end
    end

    // ---------------------------------------------------------------------------
    // access arbitration
    // ---------------------------------------------------------------------------
    typedef enum logic [1:0] {
        ST_IDLE,
        ST_CPU,
        ST_LOOKUP,
        ST_LEARN
    } state_t;

    state_t state;

    logic cpu_start;
    logic lookup_start;
    logic learn_start;

    // the CPU interface has the highest priority, lookup is served before learning
    assign cpu_start    = (state == ST_IDLE) && cpu_pending;
    assign lookup_start = (state == ST_IDLE) && !cpu_pending && lookup_pending;
    assign learn_start  = (state == ST_IDLE) && !cpu_pending && !lookup_pending && learn_pending;

    logic [NUM_OF_INTERFACES-1:0] lookup_result;

    always_ff @(posedge clk) begin
        if (rst) begin
            state          <= ST_IDLE;
            cpu_pending    <= 1'b0;
            cpu_addr       <= '0;
            cpu_is_wr      <= 1'b0;
            cpu_wr_data    <= '0;
            cpu_wr_biten   <= '0;
            lookup_pending <= 1'b0;
            lookup_mac     <= '0;
            learn_pending  <= 1'b0;
            learn_mac      <= '0;
            learn_bitmap   <= '0;
            cpuif_req_d    <= 1'b0;
            lookup_req_d   <= 1'b0;
            learning_req_d <= 1'b0;
            learn_ptr      <= '0;
            entry_en       <= '0;
            lookup_result  <= '0;

            for (int i = 0; i < TABLE_DEPTH; i++) begin
                cam_mac[i]    <= '0;
                ram_bitmap[i] <= '0;
            end
        end else begin
            case (state)
                ST_IDLE: begin
                    if (cpu_start) begin
                        state       <= ST_CPU;
                        cpu_pending <= 1'b0;
                    end else if (lookup_start) begin
                        state          <= ST_LOOKUP;
                        lookup_pending <= 1'b0;
                        lookup_result  <= lookup_hit ? ram_bitmap[lookup_hit_idx] : default_forwarding;
                    end else if (learn_start) begin
                        state         <= ST_LEARN;
                        learn_pending <= 1'b0;

                        // learning is bypassed in managed mode
                        if (!operation_mode) begin
                            if (learn_hit) begin
                                // known MAC address, refresh the port bitmap only
                                ram_bitmap[learn_hit_idx] <= learn_bitmap;
                            end else begin
                                // new MAC address, circular allocation
                                cam_mac[learn_ptr]    <= learn_mac;
                                ram_bitmap[learn_ptr] <= learn_bitmap;
                                entry_en[learn_ptr]   <= 1'b1;
                                learn_ptr             <= (32'(learn_ptr) == TABLE_DEPTH-1) ? '0 : learn_ptr + IDX_W'(1);
                            end
                        end
                    end
                end

                ST_CPU: begin
                    // software writes are only accepted in managed mode
                    if (cpu_is_wr && operation_mode && cpu_idx_valid) begin
                        case (cpu_word)
                            WORD_MAC_LO: begin
                                cam_mac[cpu_idx][31:0] <= (cam_mac[cpu_idx][31:0] & ~cpu_wr_biten)
                                                        | (cpu_wr_data & cpu_wr_biten);
                            end
                            WORD_MAC_HI: begin
                                cam_mac[cpu_idx][MAC_W-1:32] <= (cam_mac[cpu_idx][MAC_W-1:32] & ~cpu_wr_biten[15:0])
                                                            | (cpu_wr_data[15:0] & cpu_wr_biten[15:0]);
                            end
                            WORD_IFACE: begin
                                ram_bitmap[cpu_idx] <= (ram_bitmap[cpu_idx] & ~cpu_wr_biten[NUM_OF_INTERFACES-1:0])
                                                    | (cpu_wr_data[NUM_OF_INTERFACES-1:0] & cpu_wr_biten[NUM_OF_INTERFACES-1:0]);
                            end
                            WORD_CONFIG: begin
                                if (cpu_wr_biten[0]) entry_en[cpu_idx] <= cpu_wr_data[0];
                            end
                            default: ;
                        endcase
                    end

                    state <= ST_IDLE;
                end

                // the result is presented together with the acknowledge
                ST_LOOKUP: state <= ST_IDLE;

                ST_LEARN: state <= ST_IDLE;

                default: state <= ST_IDLE;
            endcase

            // request capture, the *_req strobes act as a clock enable. This is
            // placed after the state machine on purpose, a request arriving in the
            // same cycle in which the previous one is taken for processing must
            // still be captured. Capturing on the rising edge of the strobe keeps
            // a request that is held until the acknowledge a single transaction.
            cpuif_req_d    <= cpuif_req;
            lookup_req_d   <= lookup_if.req;
            learning_req_d <= learning_if.req;

            if (cpuif_req && !cpuif_req_d && !cpu_pending) begin
                cpu_pending  <= 1'b1;
                cpu_addr     <= cpuif_addr;
                cpu_is_wr    <= cpuif_req_is_wr;
                cpu_wr_data  <= cpuif_wr_data;
                cpu_wr_biten <= cpuif_wr_biten;
            end

            if (lookup_if.req && !lookup_req_d && !lookup_pending) begin
                lookup_pending <= 1'b1;
                lookup_mac     <= lookup_if.mac_addr;
            end

            if (learning_if.req && !learning_req_d && !learn_pending) begin
                learn_pending <= 1'b1;
                learn_mac     <= learning_if.mac_addr;
                learn_bitmap  <= learning_if.port_bitmap;
            end
        end
    end

    // ---------------------------------------------------------------------------
    // outputs
    // ---------------------------------------------------------------------------
    assign cpuif_wr_ack = (state == ST_CPU) && cpu_is_wr;
    assign cpuif_rd_ack = (state == ST_CPU) && !cpu_is_wr;

    assign lookup_if.ack         = (state == ST_LOOKUP);
    assign lookup_if.port_bitmap = lookup_result;

    assign learning_if.ack = (state == ST_LEARN);

endmodule

`resetall
