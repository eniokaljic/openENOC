.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-picorv32:

PicoRV32 wrapper -- openenoc_picorv32
=====================================

Wraps the bundled RISC-V processor with the project memory-bus adapter.

**Source:** :download:`openenoc_picorv32.sv <../../../hw/rtl/core/openenoc_picorv32.sv>`.

Parameters
----------

.. list-table:: Parameters
   :class: rtl-reference-table
   :header-rows: 1
   :widths: 30 18 22 30

   * - Name
     - Default value
     - Allowed values
     - Description
   * - ``ENABLE_COUNTERS``
     - ``1``
     - 0 or 1
     - Enables instruction/cycle counter instructions.
   * - ``ENABLE_COUNTERS64``
     - ``1``
     - 0 or 1
     - Enables upper counter words when counters are enabled.
   * - ``ENABLE_REGS_16_31``
     - ``1``
     - 0 or 1
     - Includes the upper sixteen integer registers.
   * - ``ENABLE_REGS_DUALPORT``
     - ``1``
     - 0 or 1
     - Uses a dual-read-port integer register file.
   * - ``TWO_STAGE_SHIFT``
     - ``1``
     - 0 or 1
     - Uses the core two-stage shift implementation.
   * - ``BARREL_SHIFTER``
     - ``0``
     - 0 or 1
     - Selects the barrel-shifter implementation.
   * - ``TWO_CYCLE_COMPARE``
     - ``0``
     - 0 or 1
     - Adds a cycle to comparisons for timing.
   * - ``TWO_CYCLE_ALU``
     - ``0``
     - 0 or 1
     - Adds a cycle to the ALU path for timing.
   * - ``COMPRESSED_ISA``
     - ``0``
     - 0 or 1
     - Enables compressed RISC-V instructions.
   * - ``CATCH_MISALIGN``
     - ``1``
     - 0 or 1
     - Traps misaligned memory accesses.
   * - ``CATCH_ILLINSN``
     - ``1``
     - 0 or 1
     - Traps unsupported instructions.
   * - ``ENABLE_PCPI``
     - ``0``
     - 0 or 1
     - Enables the external coprocessor interface.
   * - ``ENABLE_MUL``
     - ``0``
     - 0 or 1
     - Enables the iterative multiplication unit.
   * - ``ENABLE_FAST_MUL``
     - ``0``
     - 0 or 1
     - Enables the fast multiplication unit.
   * - ``ENABLE_DIV``
     - ``0``
     - 0 or 1
     - Enables the division unit.
   * - ``ENABLE_IRQ``
     - ``0``
     - 0 or 1
     - Enables PicoRV32 interrupt support.
   * - ``ENABLE_IRQ_QREGS``
     - ``1``
     - 0 or 1
     - Uses the core interrupt context registers.
   * - ``ENABLE_IRQ_TIMER``
     - ``1``
     - 0 or 1
     - Enables the interrupt timer.
   * - ``ENABLE_TRACE``
     - ``0``
     - 0 or 1
     - Enables execution trace output.
   * - ``REGS_INIT_ZERO``
     - ``0``
     - 0 or 1
     - Initializes integer registers to zero.
   * - ``MASKED_IRQ``
     - ``32'h0000_0000``
     - 32-bit mask
     - Permanently masks the selected interrupt sources.
   * - ``LATCHED_IRQ``
     - ``32'hffff_ffff``
     - 32-bit mask
     - Selects edge-latched interrupts; cleared bits use level-sensitive inputs.
   * - ``PROGADDR_RESET``
     - ``32'h0000_0000``
     - 32-bit instruction address; aligned to enabled ISA
     - Processor reset vector.
   * - ``PROGADDR_IRQ``
     - ``32'h0000_0010``
     - 32-bit instruction address; aligned to enabled ISA
     - Processor interrupt vector.
   * - ``STACKADDR``
     - ``32'hffff_ffff``
     - 32-bit address; 0xffffffff disables initialization
     - Initial stack pointer value.

Signals
-------

.. list-table:: Public signals and interfaces
   :class: rtl-reference-table
   :header-rows: 1
   :widths: 26 27 17 30

   * - Name
     - Type
     - Direction / role
     - Description
   * - ``clk``
     - ``logic``
     - input
     - Clock for this component or interface domain.
   * - ``resetn``
     - ``logic``
     - input
     - Active-low processor/adapter reset.
   * - ``trap``
     - ``logic``
     - output
     - Processor entered a trap state.
   * - ``mem_axi_awvalid``
     - ``logic``
     - output
     - Write-address channel is valid.
   * - ``mem_axi_awready``
     - ``logic``
     - input
     - Write-address channel acceptance.
   * - ``mem_axi_awaddr``
     - ``logic [31:0]``
     - output
     - Write byte address.
   * - ``mem_axi_awprot``
     - ``logic [2:0]``
     - output
     - Write access attributes.
   * - ``mem_axi_wvalid``
     - ``logic``
     - output
     - Write-data channel is valid.
   * - ``mem_axi_wready``
     - ``logic``
     - input
     - Write-data channel acceptance.
   * - ``mem_axi_wdata``
     - ``logic [31:0]``
     - output
     - Write data word.
   * - ``mem_axi_wstrb``
     - ``logic [3:0]``
     - output
     - Write-byte enables.
   * - ``mem_axi_bvalid``
     - ``logic``
     - input
     - Write response is valid.
   * - ``mem_axi_bready``
     - ``logic``
     - output
     - Write-response acceptance.
   * - ``mem_axi_arvalid``
     - ``logic``
     - output
     - Read-address channel is valid.
   * - ``mem_axi_arready``
     - ``logic``
     - input
     - Read-address channel acceptance.
   * - ``mem_axi_araddr``
     - ``logic [31:0]``
     - output
     - Read byte address.
   * - ``mem_axi_arprot``
     - ``logic [2:0]``
     - output
     - Read attributes; instruction fetch sets bit 2.
   * - ``mem_axi_rvalid``
     - ``logic``
     - input
     - Read response is valid.
   * - ``mem_axi_rready``
     - ``logic``
     - output
     - Read-response acceptance.
   * - ``mem_axi_rdata``
     - ``logic [31:0]``
     - input
     - Read data word.
   * - ``pcpi_valid``
     - ``logic``
     - output
     - Coprocessor instruction request is valid.
   * - ``pcpi_insn``
     - ``logic [31:0]``
     - output
     - Instruction presented to the coprocessor.
   * - ``pcpi_rs1``
     - ``logic [31:0]``
     - output
     - First coprocessor operand.
   * - ``pcpi_rs2``
     - ``logic [31:0]``
     - output
     - Second coprocessor operand.
   * - ``pcpi_wr``
     - ``logic``
     - input
     - Coprocessor result writes the destination register.
   * - ``pcpi_rd``
     - ``logic [31:0]``
     - input
     - Coprocessor result word.
   * - ``pcpi_wait``
     - ``logic``
     - input
     - Coprocessor is processing the instruction.
   * - ``pcpi_ready``
     - ``logic``
     - input
     - Coprocessor instruction completed.
   * - ``irq``
     - ``logic [31:0]``
     - input
     - Processor interrupt input bitmap; sources 0..2 include core internal events.
   * - ``eoi``
     - ``logic [31:0]``
     - output
     - Core end-of-interrupt indication bitmap.
   * - ``rvfi_valid``
     - ``logic``
     - output
     - Retirement observation is valid. Only with RISCV_FORMAL.
   * - ``rvfi_order``
     - ``logic [63:0]``
     - output
     - Retired instruction order. Only with RISCV_FORMAL.
   * - ``rvfi_insn``
     - ``logic [31:0]``
     - output
     - Retired instruction bits. Only with RISCV_FORMAL.
   * - ``rvfi_trap``
     - ``logic``
     - output
     - Retired instruction trapped. Only with RISCV_FORMAL.
   * - ``rvfi_halt``
     - ``logic``
     - output
     - Retirement halt indication. Only with RISCV_FORMAL.
   * - ``rvfi_intr``
     - ``logic``
     - output
     - Retirement interrupt indication. Only with RISCV_FORMAL.
   * - ``rvfi_rs1_addr``
     - ``logic [4:0]``
     - output
     - First source register index. Only with RISCV_FORMAL.
   * - ``rvfi_rs2_addr``
     - ``logic [4:0]``
     - output
     - Second source register index. Only with RISCV_FORMAL.
   * - ``rvfi_rs1_rdata``
     - ``logic [31:0]``
     - output
     - First source register value. Only with RISCV_FORMAL.
   * - ``rvfi_rs2_rdata``
     - ``logic [31:0]``
     - output
     - Second source register value. Only with RISCV_FORMAL.
   * - ``rvfi_rd_addr``
     - ``logic [4:0]``
     - output
     - Destination register index. Only with RISCV_FORMAL.
   * - ``rvfi_rd_wdata``
     - ``logic [31:0]``
     - output
     - Destination register value. Only with RISCV_FORMAL.
   * - ``rvfi_pc_rdata``
     - ``logic [31:0]``
     - output
     - Program counter before retirement. Only with RISCV_FORMAL.
   * - ``rvfi_pc_wdata``
     - ``logic [31:0]``
     - output
     - Program counter after retirement. Only with RISCV_FORMAL.
   * - ``rvfi_mem_addr``
     - ``logic [31:0]``
     - output
     - Observed memory byte address. Only with RISCV_FORMAL.
   * - ``rvfi_mem_rmask``
     - ``logic [3:0]``
     - output
     - Observed memory-read byte mask. Only with RISCV_FORMAL.
   * - ``rvfi_mem_wmask``
     - ``logic [3:0]``
     - output
     - Observed memory-write byte mask. Only with RISCV_FORMAL.
   * - ``rvfi_mem_rdata``
     - ``logic [31:0]``
     - output
     - Observed memory-read value. Only with RISCV_FORMAL.
   * - ``rvfi_mem_wdata``
     - ``logic [31:0]``
     - output
     - Observed memory-write value. Only with RISCV_FORMAL.
   * - ``trace_valid``
     - ``logic``
     - output
     - Execution trace word is valid.
   * - ``trace_data``
     - ``logic [35:0]``
     - output
     - Execution trace payload from the processor.

The ``rvfi_*`` ports exist only when ``RISCV_FORMAL`` is defined.

Architecture and operation
--------------------------

The wrapper combines the bundled PicoRV32 core with the project's AXI4-Lite
adapter. Its flattened ``mem_axi_*`` master connects to the endpoint memory
interconnect. ``clk`` and active-low ``resetn`` drive processor state; ``trap``,
PCPI, IRQ/EOI, trace, and optional ``RISCV_FORMAL`` ports expose processor
integration signals.

Parameters pass through the PicoRV32 feature choices: counters, register-file
options, shifts and ALU timing, compressed instructions, exception checks,
PCPI/multiply/divide, IRQ features, trace, and initial register values.
``PROGADDR_RESET``, ``PROGADDR_IRQ``, ``STACKADDR``, ``MASKED_IRQ``, and
``LATCHED_IRQ`` define boot/interrupt configuration. The vendor core under
``libs/picorv32`` remains the source for its instruction/feature semantics.

**Verification:** full-endpoint firmware tests and adapter-specific tests.
The reference skeleton should grow to cover the endpoint's selected feature
set, boot flow, and interrupt wiring.

Functional scenarios
--------------------

This section reserves space for scenario descriptions and WaveDrom timing
diagrams. The current outline is:

* Firmware boot and instruction/data memory accesses.
* Interrupt entry, end-of-interrupt indication, and return.
* Optional coprocessor, trace, and formal-observation interfaces.
