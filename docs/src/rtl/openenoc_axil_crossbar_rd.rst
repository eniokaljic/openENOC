.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-axil-crossbar-rd:

Crossbar read path -- openenoc_axil_crossbar_rd
===============================================

.. index::
   single: openenoc_axil_crossbar_rd

Routes AXI4-Lite read requests and returns their responses to the requesting
initiators.

**Source:** :download:`openenoc_axil_crossbar_rd.sv <../../../hw/rtl/core/openenoc_axil_crossbar_rd.sv>`.

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
   * - ``s_axil_rd[S_COUNT]``
     - ``taxi_axil_if.rd_slv``
     - bidirectional (rd_slv)
     - Incoming AXI4-Lite read channels.
   * - ``m_axil_rd[M_COUNT]``
     - ``taxi_axil_if.rd_mst``
     - bidirectional (rd_mst)
     - Outgoing AXI4-Lite read channels.

Architecture and operation
--------------------------

Each source decodes its AR address and access attributes. Each target has
independent round-robin arbitration and a two-entry AXI4-Lite channel
register slice (skid buffer) for outgoing AR. Admitting an address reserves
one source and one target routing entry. The target may accept that buffered
address later. A source can have reads pending at several targets.

The target routing queue identifies the source of each R response. The
source routing queue preserves its own AR order across targets. A response
transfers only when those two queue heads agree and the source R buffer has
space. Once captured in that two-entry response buffer, routing entries
are released even if the upstream initiator has not consumed the response.
An R transfer into the buffer can admit a replacement AR on the same edge.
The buffer presents the response upstream in the following interval.

An unmapped or disallowed AR consumes a source routing entry and creates
an ordered local DECERR response with zero data. It consumes no target entry
and produces no target AR transfer. It waits behind earlier reads from that
source just as a target response would.

The map, connection matrix, security rules, and parameter packing follow
the :ref:`crossbar <rtl-axil-crossbar>` and
:ref:`decoder <rtl-axil-crossbar-addr>` references. Source and target limits
apply to routing entries; the R buffer adds response storage. Reset inhibits
AR admission immediately and clears arbitration, routing queues, and channel
VALID state at the sampling edge. Connected endpoints reset with the fabric.

Functional scenarios
--------------------

These examples use the crossbar reference's 2-source, 2-target configuration:
32-bit addresses/data, two routing entries per source and target, and one
64 KiB region per target. M0 begins at zero and M1 at ``0x00010000``.
All accesses are secure. S0/S1 and M0/M1 identify the indexed public source
and target interfaces. A tick is an interval ending at a rising sampling edge;
``x`` marks fields without VALID. Address/data labels are local to each example.

Continuous address and response pipelines
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

S0 offers four consecutive reads, ``A0`` through ``A3``, to M0. They return
``D0`` through ``D3`` in the same order. Source RREADY and target ARREADY
remain high; the target supplies each response one interval after its AR
handshake.

S0's AR transfers occur in ticks 1 through 4, and M0 receives them in
ticks 2 through 5. M0 returns data in ticks 3 through 6; S0 consumes it in
ticks 4 through 7. Capturing each response frees routing capacity for the
next address, allowing continuous progress with two routing entries.

.. wavedrom::
    :name: memory-read-stream-timing
    :caption: An unstalled read pipeline sustains consecutive addresses and responses
    :alt: An unstalled read pipeline sustains consecutive addresses and responses.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p........."},
            {"name": "rst", "wave": "0........."},
            ["s_axil_rd[0]",
                ["Master",
                    {"name": "arvalid", "wave": "01...0...."},
                    {"name": "araddr", "wave": "x====x....", "data": ["A0", "A1", "A2", "A3"]},
                    {"name": "rready", "wave": "1........."}
                ],
                ["Slave",
                    {"name": "arready", "wave": "01...0...."},
                    {"name": "rvalid", "wave": "0...1...0."},
                    {"name": "rdata", "wave": "x...====x.", "data": ["D0", "D1", "D2", "D3"]},
                    {"name": "rresp", "wave": "x...=...x.", "data": ["OKAY"]}
                ]
            ],
            {},
            ["m_axil_rd[0]",
                ["Master",
                    {"name": "arvalid", "wave": "0.1...0..."},
                    {"name": "araddr", "wave": "x.====x...", "data": ["A0", "A1", "A2", "A3"]},
                    {"name": "rready", "wave": "0.1....0.."}
                ],
                ["Slave",
                    {"name": "arready", "wave": "1........."},
                    {"name": "rvalid", "wave": "0..1...0.."},
                    {"name": "rdata", "wave": "x..====x..", "data": ["D0", "D1", "D2", "D3"]},
                    {"name": "rresp", "wave": "x..=...x..", "data": ["OKAY"]}
                ]
            ],
            {}
        ],
        "head": {"tick": 0},
        "config": {"hscale": 2}
    }

A local decode error remains in read order
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: Reads from S0
   :class: documentation-table
   :header-rows: 1
   :widths: 16 16 68

   * - Address
     - Destination
     - Response
   * - ``A0``
     - M0
     - Target returns ``D0`` in tick 6
   * - ``A1``
     - Unmapped
     - Local DECERR with zero data
   * - ``A2``
     - M1
     - Target returns ``D2`` in tick 8

The first two AR requests are admitted in ticks 1 and 2. S0 offers ``A2``
from tick 3, but both source entries remain occupied until the earlier M0
response is captured in tick 6. That edge also admits ``A2``.

The local error cannot overtake ``D0``. S0 sees consecutive responses:
``D0``/OKAY in tick 7, zero/DECERR in tick 8, and ``D2``/OKAY in tick 9.
Only ``A0`` and ``A2`` appear at target AR ports, in ticks 2 and 7.

.. wavedrom::
    :name: memory-read-error-order-timing
    :caption: A local decode error follows the earlier target response in source order
    :alt: A local decode error follows the earlier target response in source order.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p.........."},
            {"name": "rst", "wave": "0.........."},
            ["s_axil_rd[0]",
                ["Master",
                    {"name": "arvalid", "wave": "01.....0..."},
                    {"name": "araddr", "wave": "x===...x...", "data": ["A0", "A1", "A2"]},
                    {"name": "rready", "wave": "1.........."}
                ],
                ["Slave",
                    {"name": "arready", "wave": "01.0..10..."},
                    {"name": "rvalid", "wave": "0......1..0"},
                    {"name": "rdata", "wave": "x......===x", "data": ["D0", "0", "D2"]},
                    {"name": "rresp", "wave": "x......===x", "data": ["OKAY", "DECERR", "OKAY"]}
                ]
            ],
            {},
            ["m_axil_rd[0]",
                ["Master",
                    {"name": "arvalid", "wave": "0.10......."},
                    {"name": "araddr", "wave": "x.=x.......", "data": ["A0"]},
                    {"name": "rready", "wave": "0.1....0..."}
                ],
                ["Slave",
                    {"name": "arready", "wave": "1.........."},
                    {"name": "rvalid", "wave": "0.....10..."},
                    {"name": "rdata", "wave": "x.....=x...", "data": ["D0"]},
                    {"name": "rresp", "wave": "x.....=x...", "data": ["OKAY"]}
                ]
            ],
            {},
            ["m_axil_rd[1]",
                ["Master",
                    {"name": "arvalid", "wave": "0......10.."},
                    {"name": "araddr", "wave": "x......=x..", "data": ["A2"]},
                    {"name": "rready", "wave": "0.......10."}
                ],
                ["Slave",
                    {"name": "arready", "wave": "1.........."},
                    {"name": "rvalid", "wave": "0.......10."},
                    {"name": "rdata", "wave": "x.......=x.", "data": ["D2"]},
                    {"name": "rresp", "wave": "x.......=x.", "data": ["OKAY"]}
                ]
            ],
            {}
        ],
        "head": {"tick": 0},
        "config": {"hscale": 2}
    }
