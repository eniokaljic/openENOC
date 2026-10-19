.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-axil-crossbar-wr:

Crossbar write path -- openenoc_axil_crossbar_wr
================================================

.. index::
   single: openenoc_axil_crossbar_wr

Routes AXI4-Lite write transactions and preserves response ordering for each
initiator.

**Source:** :download:`openenoc_axil_crossbar_wr.sv <../../../hw/rtl/core/openenoc_axil_crossbar_wr.sv>`.

Parameters
----------

.. list-table:: Parameters
   :class: rtl-reference-table
   :header-rows: 1
   :widths: 18 25 29 28

   * - Name
     - Default value
     - Allowed values
     - Description
   * - ``S_COUNT``
     - ``4``
     - Integer >= 1
     - Number of upstream initiator interfaces.
   * - ``M_COUNT``
     - ``4``
     - Integer >= 1
     - Number of downstream target/output interfaces.
   * - ``ADDR_W``
     - ``32``
     - Integer >= 1
     - Byte-address width in bits; connected interfaces must agree.
   * - ``S_ACCEPT``
     - ``{S_COUNT{32'd16}}``
     - One positive 32-bit count per source
     - Routing-context capacity per source; source 0 occupies the least-significant
       slice. Responses already buffered upstream are additional.
   * - ``M_REGIONS``
     - ``1``
     - Integer >= 1
     - Number of decode regions per target.
   * - ``M_BASE_ADDR``
     - ``'0``
     - Packed aligned addresses; zero selects automatic placement
     - One ADDR_W-bit base per target region; region index m*M_REGIONS+r starts in
       the least-significant slice.
   * - ``M_ADDR_W``
     - ``{M_COUNT{{ M_REGIONS{32'd24}}}}``
     - Zero, or log2(STRB_W)..ADDR_W in crossbar integration
     - Region span is 2**width bytes; zero disables the region. Packing follows
       M_BASE_ADDR.
   * - ``M_CONNECT``
     - ``{M_COUNT{{ S_COUNT{1'b1}}}}``
     - M_COUNT*S_COUNT-bit mask
     - Permitted paths; bit m*S_COUNT+s connects source s to target m.
   * - ``M_ISSUE``
     - ``{M_COUNT{32'd16}}``
     - One positive 32-bit count per target
     - Routing-context capacity per target, including buffered addresses; target 0
       occupies the least-significant slice.
   * - ``M_SECURE``
     - ``{M_COUNT{1'b0}}``
     - M_COUNT-bit mask
     - A set bit disallows nonsecure accesses to that target.

Signals
-------

Interface ports contain channels in both directions. The table identifies
the selected modport or stream role; member directions follow that interface.

.. list-table:: Public signals and interfaces
   :class: rtl-reference-table
   :header-rows: 1
   :widths: 25 25 17 33

   * - Name
     - Type
     - Direction / role
     - Description
   * - ``clk``
     - ``logic``
     - input
     - Clock for this component or interface domain.
   * - ``rst``
     - ``logic``
     - input
     - Active-high synchronous reset of routing, arbitration, and channel buffers.
   * - ``s_axil_wr[S_COUNT]``
     - ``taxi_axil_if.wr_slv``
     - bidirectional (wr_slv)
     - Incoming AXI4-Lite write channels.
   * - ``m_axil_wr[M_COUNT]``
     - ``taxi_axil_if.wr_mst``
     - bidirectional (wr_mst)
     - Outgoing AXI4-Lite write channels.

Architecture and operation
--------------------------

Each target independently arbitrates eligible AW requests. Address admission
reserves routing entries for both the source and target and places AW in a
two-entry AXI4-Lite channel register slice (skid buffer). Per-source routing
order identifies the target of each W beat; per-target routing order
identifies its source. W transfers when both queue heads agree and its target
W buffer can accept data. This retains the AW/W association without AXI IDs.

A source may offer W before AW, but WREADY stays low until an admitted AW
establishes its route. Once admitted, W can traverse its own registered
channel independently of target AWREADY. A target can therefore accept W
before the corresponding AW. The AXI target returns B only after receiving
both request channels. WSTRB and enabled USER fields travel with their
respective channel payloads.

Separate W and B progress positions let write data move ahead of older
responses. Source B order still follows source AW order across all targets;
target B order identifies the original source. Capturing B in a source's
two-entry response buffer releases source and target response-routing capacity.
The response is visible upstream in the following interval. ``S_ACCEPT``
and ``M_ISSUE`` therefore bound routing entries, with response-buffer storage
in addition to those entries.

An unmapped or disallowed AW creates a local error entry without a target
request. Its associated W beat is consumed locally in source order before
that entry becomes eligible for B/DECERR. The error then waits behind earlier
B responses. This prevents a rejected address from leaving its W beat to
be mistaken for a later write.

Address-map packing and permissions follow the :ref:`crossbar
<rtl-axil-crossbar>` and :ref:`decoder <rtl-axil-crossbar-addr>` references.
Reset immediately inhibits new source AW/W acceptance and clears routing,
arbitration, and buffered VALID state at the sampling edge. Targets reset
with the fabric to discard any separately accepted AW or W.

Functional scenarios
--------------------

The examples use two sources and targets, 32-bit addresses/data, ``WSTRB = 0xF``,
and two routing entries per source and target, as in the crossbar reference.
M0's region starts at zero; M1's at ``0x00010000``. Accesses are secure.
S0/S1 and M0/M1 identify the corresponding indexed public interfaces. A tick
is an interval ending at a rising sampling edge. ``x`` marks fields without
VALID. Labels are local to each example.

Write data advances while target AW is stalled
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: Writes to M0
   :class: documentation-table
   :header-rows: 1
   :widths: 16 16 68

   * - Source
     - Write
     - Offered channels
   * - S0
     - ``A0`` / ``D0``
     - AW and W from tick 1
   * - S1
     - ``A1`` / ``D1``
     - AW from tick 1; W from tick 5

AW arbitration admits S0 in tick 1 and S1 in tick 2. M0 holds AWREADY low
through tick 5, retaining ``A0`` at its output and ``A1`` behind it.
S0's W transfers into the fabric in tick 2 and reaches M0 in tick 3.
S1's later W is accepted in tick 5 and reaches M0 in tick 6.

M0 accepts ``A0`` and ``A1`` in ticks 6 and 7, after their respective data
beats. The independent channels preserve the pairings ``A0``/``D0`` and
``A1``/``D1``. Target B responses transfer in ticks 7 and 8 and reach S0
and S1 in ticks 8 and 9.

.. wavedrom::
    :name: memory-write-skew-timing
    :caption: Independent W routing preserves write pairing while target AW is stalled
    :alt: Independent W routing preserves write pairing while target AW is stalled.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p.........."},
            {"name": "rst", "wave": "0.........."},
            ["s_axil_wr[0]",
                ["Master",
                    {"name": "awvalid", "wave": "010........"},
                    {"name": "awaddr", "wave": "x=x........", "data": ["A0"]},
                    {"name": "wvalid", "wave": "01.0......."},
                    {"name": "wdata", "wave": "x=.x.......", "data": ["D0"]},
                    {"name": "bready", "wave": "1.........."}
                ],
                ["Slave",
                    {"name": "awready", "wave": "010........"},
                    {"name": "wready", "wave": "0.10......."},
                    {"name": "bvalid", "wave": "0.......10."},
                    {"name": "bresp", "wave": "x.......=x.", "data": ["OKAY"]}
                ]
            ],
            {},
            ["s_axil_wr[1]",
                ["Master",
                    {"name": "awvalid", "wave": "01.0......."},
                    {"name": "awaddr", "wave": "x=.x.......", "data": ["A1"]},
                    {"name": "wvalid", "wave": "0....10...."},
                    {"name": "wdata", "wave": "x....=x....", "data": ["D1"]},
                    {"name": "bready", "wave": "1.........."}
                ],
                ["Slave",
                    {"name": "awready", "wave": "0.10......."},
                    {"name": "wready", "wave": "0..1..0...."},
                    {"name": "bvalid", "wave": "0........10"},
                    {"name": "bresp", "wave": "x........=x", "data": ["OKAY"]}
                ]
            ],
            {},
            ["m_axil_wr[0]",
                ["Master",
                    {"name": "awvalid", "wave": "0.1.....0.."},
                    {"name": "awaddr", "wave": "x.=....=x..", "data": ["A0", "A1"]},
                    {"name": "wvalid", "wave": "0..10.10..."},
                    {"name": "wdata", "wave": "x..=x.=x...", "data": ["D0", "D1"]},
                    {"name": "bready", "wave": "0.1......0."}
                ],
                ["Slave",
                    {"name": "awready", "wave": "0.....1...."},
                    {"name": "wready", "wave": "1.........."},
                    {"name": "bvalid", "wave": "0......1.0."},
                    {"name": "bresp", "wave": "x......=.x.", "data": ["OKAY"]}
                ]
            ],
            {}
        ],
        "head": {"tick": 0},
        "config": {"hscale": 2}
    }

A rejected write drains its W beat before ordered DECERR
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

S0 offers mapped write ``A0``/``D0`` to M0, followed by unmapped write
``A1``/``D1``. AW is accepted in ticks 1 and 2. ``D0`` is accepted from S0
in tick 2; ``D1`` is deliberately offered later, in tick 7.

M0 receives only ``A0`` and ``D0``, in ticks 2 and 3, and returns its B
response in tick 8. The invalid write's W beat is consumed locally in
tick 7. Its error is then ready, but cannot pass the older mapped response.
S0 receives B/OKAY in tick 9 and B/DECERR in tick 10. No target receives
``A1`` or ``D1``.

.. wavedrom::
    :name: memory-write-error-order-timing
    :caption: The rejected write consumes its data before returning an ordered DECERR
    :alt: The rejected write consumes its data before returning an ordered DECERR.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p..........."},
            {"name": "rst", "wave": "0..........."},
            ["s_axil_wr[0]",
                ["Master",
                    {"name": "awvalid", "wave": "01.0........"},
                    {"name": "awaddr", "wave": "x==x........", "data": ["A0", "A1"]},
                    {"name": "wvalid", "wave": "01.0...10..."},
                    {"name": "wdata", "wave": "x=.x...=x...", "data": ["D0", "D1"]},
                    {"name": "bready", "wave": "1..........."}
                ],
                ["Slave",
                    {"name": "awready", "wave": "01.0........"},
                    {"name": "wready", "wave": "0.1.....0..."},
                    {"name": "bvalid", "wave": "0........1.0"},
                    {"name": "bresp", "wave": "x........==x", "data": ["OKAY", "DECERR"]}
                ]
            ],
            {},
            ["m_axil_wr[0]",
                ["Master",
                    {"name": "awvalid", "wave": "0.10........"},
                    {"name": "awaddr", "wave": "x.=x........", "data": ["A0"]},
                    {"name": "wvalid", "wave": "0..10......."},
                    {"name": "wdata", "wave": "x..=x.......", "data": ["D0"]},
                    {"name": "bready", "wave": "0.1......0.."}
                ],
                ["Slave",
                    {"name": "awready", "wave": "1..........."},
                    {"name": "wready", "wave": "1..........."},
                    {"name": "bvalid", "wave": "0.......10.."},
                    {"name": "bresp", "wave": "x.......=x..", "data": ["OKAY"]}
                ]
            ],
            {}
        ],
        "head": {"tick": 0},
        "config": {"hscale": 2}
    }
