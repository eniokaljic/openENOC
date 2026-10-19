.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-picorv32-axil-adapter:

PicoRV32 AXI4-Lite adapter -- openenoc_picorv32_axil_adapter
============================================================

.. index::
   single: openenoc_picorv32_axil_adapter

Bridges the processor native memory interface to AXI4-Lite using optional look-
ahead capture.

**Source:** :download:`openenoc_picorv32_axil_adapter.sv <../../../hw/rtl/core/openenoc_picorv32_axil_adapter.sv>`.

Parameters
----------

.. list-table:: Parameters
   :class: rtl-reference-table
   :header-rows: 1
   :widths: 12 18 20 50

   * - Name
     - Default value
     - Allowed values
     - Description
   * - None
     - —
     - —
     - This component has no elaboration parameters.

Signals
-------

.. list-table:: Public signals and interfaces
   :class: rtl-reference-table
   :header-rows: 1
   :widths: 22 22 17 39

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
     - Active-low synchronous reset of retained request and channel state.
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
   * - ``mem_valid``
     - ``logic``
     - input
     - Native processor memory request is active.
   * - ``mem_instr``
     - ``logic``
     - input
     - Native memory request is an instruction fetch.
   * - ``mem_ready``
     - ``logic``
     - output
     - Native memory request completed.
   * - ``mem_addr``
     - ``logic [31:0]``
     - input
     - Native byte address.
   * - ``mem_wdata``
     - ``logic [31:0]``
     - input
     - Native write word.
   * - ``mem_wstrb``
     - ``logic [3:0]``
     - input
     - Native write-byte mask; zero selects a read.
   * - ``mem_rdata``
     - ``logic [31:0]``
     - output
     - Native read word.
   * - ``mem_la_read``
     - ``logic``
     - input
     - Look-ahead read request for capture.
   * - ``mem_la_write``
     - ``logic``
     - input
     - Look-ahead write request for capture.
   * - ``mem_la_addr``
     - ``logic [31:0]``
     - input
     - Look-ahead byte address.
   * - ``mem_la_wdata``
     - ``logic [31:0]``
     - input
     - Look-ahead write word.
   * - ``mem_la_wstrb``
     - ``logic [3:0]``
     - input
     - Look-ahead write-byte mask.

Architecture and operation
--------------------------

This adapter retains one native processor request and drives independent
AXI4-Lite AW/W/B and AR/R channels with 32-bit addresses/data and four byte
strobes. While idle, a look-ahead read or write is captured at a rising edge;
its AXI VALID and payload appear in the following interval. Look-ahead read
and write indications are mutually exclusive. If neither is supplied, an
active ``mem_valid`` request is captured instead. In that fallback path,
nonzero ``mem_wstrb`` selects a write and zero selects a read.

Captured address, write data, and strobes stay stable through independent
AW/W or AR stalls. Each request channel stops asserting VALID after its
own handshake. The native processor keeps ``mem_valid`` asserted until
``mem_ready`` completes the access. BREADY/RREADY are qualified by that
native VALID, so a look-ahead request can launch AXI before native VALID
while its returned response waits for the processor.

A matching B or R handshake produces ``mem_ready`` in the same interval;
``mem_rdata`` directly follows AXI RDATA and is meaningful for a completed
read. If a new look-ahead request accompanies that completion, it is captured
at the same edge and launches its AXI request in the next interval. Other
look-ahead requests arriving during an active access are not queued.

AWPROT is zero. ARPROT is ``0b100`` for live ``mem_instr = 1`` and ``0b000``
otherwise. Unlike the captured address, this attribute follows ``mem_instr``
directly, so it must remain appropriate and stable while ARVALID is pending.
There are no BRESP or RRESP inputs and no native error result at this boundary.
Native completion alone therefore does not report an AXI access error.

Active-low ``resetn`` clears retained state at a rising edge. The AXI outputs
and native completion are not combinationally masked by resetn; they reflect
the old active request until that edge. The processor and AXI target reset
with the adapter so partially accepted accesses are cancelled consistently.

Functional scenarios
--------------------

Ticks denote intervals ending at a rising sampling edge. A0, A1, and A2 are
byte addresses; D0, D1, and D2 are data words. ``x`` marks payload fields
without their request, VALID, or completion qualifier.

Look-ahead launches before native VALID
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An instruction-read look-ahead for A0 is presented in tick 1. AR for A0 with
PROT ``0b100`` transfers in tick 2, while ``mem_valid`` is still low. The
target offers D0 from tick 3, but RREADY and native READY remain low.

In tick 4, the processor asserts ``mem_valid`` for that access. RREADY rises,
and the held D0 completes both the AXI read and native access at that edge.
``mem_instr`` remains one throughout the pending instruction address.

.. wavedrom::
    :name: memory-pico-lookahead-timing
    :caption: Look-ahead launches the AXI read before native VALID permits completion
    :alt: Look-ahead launches the AXI read before native VALID permits completion.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p......"},
            {"name": "resetn", "wave": "1......"},
            {"name": "mem_la_read", "wave": "010...."},
            {"name": "mem_la_addr", "wave": "x=x....", "data": ["A0"]},
            {"name": "mem_valid", "wave": "0...10."},
            {"name": "mem_addr", "wave": "x...=x.", "data": ["A0"]},
            {"name": "mem_wstrb", "wave": "x...=x.", "data": ["0"]},
            {"name": "mem_instr", "wave": "01...0."},
            {"name": "mem_ready", "wave": "0...10."},
            {"name": "mem_rdata", "wave": "x...=x.", "data": ["D0"]},
            {},
            {"name": "mem_axi_arvalid", "wave": "0.10..."},
            {"name": "mem_axi_araddr", "wave": "x.=x...", "data": ["A0"]},
            {"name": "mem_axi_arprot", "wave": "x.=x...", "data": ["0b100"]},
            {"name": "mem_axi_rready", "wave": "0...10."},
            {"name": "mem_axi_arready", "wave": "1......"},
            {"name": "mem_axi_rvalid", "wave": "0..1.0."},
            {"name": "mem_axi_rdata", "wave": "x..=.x.", "data": ["D0"]},
            {}
        ],
        "head": {"tick": 0},
        "config": {"hscale": 2}
    }

Fallback capture and independent write-channel acceptance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No look-ahead signals are asserted. The processor holds write A0/D0 with
``mem_wstrb = S0 = 0b0101`` from tick 1 until completion in tick 6. The
request is captured in tick 1; AW and W VALID first appear in tick 2.

AW transfers in tick 2. WREADY remains low through tick 4, retaining D0
and S0 until their transfer in tick 5. AWVALID stays low after its own
acceptance. B in tick 6 produces native READY without another response stage.

.. wavedrom::
    :name: memory-pico-fallback-timing
    :caption: Fallback captures native write state before independent AW and W transfers
    :alt: Fallback captures native write state before independent AW and W transfers.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p........"},
            {"name": "resetn", "wave": "1........"},
            {"name": "mem_valid", "wave": "01.....0."},
            {"name": "mem_addr", "wave": "x=.....x.", "data": ["A0"]},
            {"name": "mem_wstrb", "wave": "x=.....x.", "data": ["S0"]},
            {"name": "mem_wdata", "wave": "x=.....x.", "data": ["D0"]},
            {"name": "mem_ready", "wave": "0.....10."},
            {},
            {"name": "mem_axi_awvalid", "wave": "0.10....."},
            {"name": "mem_axi_awaddr", "wave": "x.=x.....", "data": ["A0"]},
            {"name": "mem_axi_wvalid", "wave": "0.1...0.."},
            {"name": "mem_axi_wdata", "wave": "x.=...x..", "data": ["D0"]},
            {"name": "mem_axi_wstrb", "wave": "x.=...x..", "data": ["S0"]},
            {"name": "mem_axi_bready", "wave": "0.1....0."},
            {"name": "mem_axi_awready", "wave": "1........"},
            {"name": "mem_axi_wready", "wave": "0....1..."},
            {"name": "mem_axi_bvalid", "wave": "0.....10."},
            {}
        ],
        "head": {"tick": 0},
        "config": {"hscale": 2}
    }

Completion captures the next look-ahead and reset cancels it
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A read of A0 is captured from look-ahead in tick 1. Its AR waits in ticks
2 and 3, transfers in tick 4, and returns D0 in tick 5. At the same time,
look-ahead describes write A1/D1 with all byte strobes enabled.

The old read completes in tick 5 and the new AW/W appear in tick 6.
AW transfers immediately; W remains pending because WREADY is low.
Resetn is low in ticks 7 and 8. WVALID remains visible in tick 7 and clears
at the reset edge; the cancelled write produces no native completion.

After reset release, a fallback read A2 is captured in tick 9. Its AR
transfers in tick 10, and D2 completes the native access in tick 11.

.. wavedrom::
    :name: memory-pico-chain-reset-timing
    :caption: Completion captures the next look-ahead before reset cancels its write
    :alt: Completion captures the next look-ahead before reset cancels its write.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p............."},
            {"name": "resetn", "wave": "1......0.1...."},
            {"name": "mem_la_read", "wave": "010..........."},
            {"name": "mem_la_write", "wave": "0....10......."},
            {"name": "mem_la_addr", "wave": "x=x..=x.......", "data": ["A0", "A1"]},
            {"name": "mem_la_wdata", "wave": "x....=x.......", "data": ["D1"]},
            {"name": "mem_la_wstrb", "wave": "x....=x.......", "data": ["0xF"]},
            {"name": "mem_valid", "wave": "0.1.....01..0."},
            {"name": "mem_addr", "wave": "x.=...=.x=..x.", "data": ["A0", "A1", "A2"]},
            {"name": "mem_wstrb", "wave": "x.=...=.x=..x.", "data": ["0", "0xF", "0"]},
            {"name": "mem_wdata", "wave": "x.....=.x.....", "data": ["D1"]},
            {"name": "mem_ready", "wave": "0....10....10."},
            {"name": "mem_rdata", "wave": "x....=x....=x.", "data": ["D0", "D2"]},
            {},
            {"name": "mem_axi_awvalid", "wave": "0.....10......"},
            {"name": "mem_axi_awaddr", "wave": "x.....=x......", "data": ["A1"]},
            {"name": "mem_axi_wvalid", "wave": "0.....1.0....."},
            {"name": "mem_axi_wdata", "wave": "x.....=.x.....", "data": ["D1"]},
            {"name": "mem_axi_wstrb", "wave": "x.....=.x.....", "data": ["0xF"]},
            {"name": "mem_axi_bready", "wave": "0.....1.0....."},
            {"name": "mem_axi_awready", "wave": "1......0.1...."},
            {"name": "mem_axi_wready", "wave": "1.....0..1...."},
            {"name": "mem_axi_bvalid", "wave": "0............."},
            {},
            {"name": "mem_axi_arvalid", "wave": "0.1..0....10.."},
            {"name": "mem_axi_araddr", "wave": "x.=..x....=x..", "data": ["A0", "A2"]},
            {"name": "mem_axi_rready", "wave": "0.1...0...1.0."},
            {"name": "mem_axi_arready", "wave": "1.0.1..0.1...."},
            {"name": "mem_axi_rvalid", "wave": "0....10....10."},
            {"name": "mem_axi_rdata", "wave": "x....=x....=x.", "data": ["D0", "D2"]},
            {}
        ],
        "head": {"tick": 0},
        "config": {"hscale": 2}
    }

.. _verification-openenoc-picorv32-axil-adapter:

Verification
------------

The test suite is in ``dv/core/openenoc_picorv32_axil_adapter/``.

Testbench
~~~~~~~~~

This cocotb suite verifies the ``openenoc_picorv32_axil_adapter`` bridge between the native
PicoRV32 memory interface, its look-ahead interface, and an AXI4-Lite master port.

Coverage
~~~~~~~~

The suite covers:

- independent AW and W handshakes in either order;

- stable AXI request payloads while ``VALID && !READY``;

- instruction/data ``ARPROT`` generation;

- partial writes through all non-zero ``WSTRB`` values;

- read and write response delivery to the native interface;

- randomized independent AW, W, and AR backpressure;

- response ordering with one native request outstanding;

- back-to-back look-ahead capture on a response cycle;

- direct native requests without look-ahead; and

- reset during a stalled transaction and recovery after reset.
