.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-axil-crossbar:

AXI4-Lite crossbar -- openenoc_axil_crossbar
============================================

.. index::
   single: openenoc_axil_crossbar

Connects several AXI4-Lite initiators to a shared set of memory and register
targets.

**Source:** :download:`openenoc_axil_crossbar.sv <../../../hw/rtl/core/openenoc_axil_crossbar.sv>`.

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
     - Routing-context capacity per source in each read/write path. Source 0
       occupies the least-significant slice; buffered responses are additional.
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
   * - ``M_CONNECT_RD``
     - ``{M_COUNT{{ S_COUNT{1'b1}}}}``
     - M_COUNT*S_COUNT-bit mask
     - Permitted read paths; bit m*S_COUNT+s connects source s to target m.
   * - ``M_CONNECT_WR``
     - ``{M_COUNT{{ S_COUNT{1'b1}}}}``
     - M_COUNT*S_COUNT-bit mask
     - Permitted write paths; bit m*S_COUNT+s connects source s to target m.
   * - ``M_ISSUE``
     - ``{M_COUNT{32'd16}}``
     - One positive 32-bit count per target
     - Routing-context capacity per target in each read/write path, including
       buffered requests. Target 0 occupies the least-significant slice.
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
   :widths: 24 25 17 34

   * - Name
     - Type
     - Direction / role
     - Description
   * - ``clk``
     - ``logic``
     - input
     - Common clock for both fabrics and all connected interfaces.
   * - ``rst``
     - ``logic``
     - input
     - Active-high synchronous reset of routing, arbitration, and channel buffers.
       New source request acceptance is inhibited while reset is asserted.
   * - ``s_axil_wr[S_COUNT]``
     - ``taxi_axil_if.wr_slv``
     - bidirectional (wr_slv)
     - Incoming AXI4-Lite write channels.
   * - ``s_axil_rd[S_COUNT]``
     - ``taxi_axil_if.rd_slv``
     - bidirectional (rd_slv)
     - Incoming AXI4-Lite read channels.
   * - ``m_axil_wr[M_COUNT]``
     - ``taxi_axil_if.wr_mst``
     - bidirectional (wr_mst)
     - Outgoing AXI4-Lite write channels.
   * - ``m_axil_rd[M_COUNT]``
     - ``taxi_axil_if.rd_mst``
     - bidirectional (rd_mst)
     - Outgoing AXI4-Lite read channels.

Architecture and operation
--------------------------

The wrapper combines the independent :ref:`read <rtl-axil-crossbar-rd>` and
:ref:`write <rtl-axil-crossbar-wr>` fabrics. Source index s identifies the
upstream initiator connected to ``s_axil_rd[s]`` and ``s_axil_wr[s]``;
target index m identifies the downstream slave on ``m_axil_rd[m]`` and
``m_axil_wr[m]``. Reads and writes have separate arbitration, routing state,
capacity limits, and responses. They can progress concurrently, including
when they address the same target. Different targets arbitrate independently.

Each target has round-robin AR and AW selection among eligible sources.
After reset, a tie starts with source 0; accepting an address advances that
target's corresponding priority. Requests admitted to an empty address
buffer appear at the downstream interface in the following interval.
After the pipeline fills, an unstalled target can receive an address every
cycle. The :ref:`address decoder <rtl-axil-crossbar-addr>` selects the target
from the address and PROT attributes. Addresses are forwarded unchanged.

Each target AW, W, and AR channel, and each source B and R channel, uses a
two-entry AXI4-Lite channel register slice (skid buffer). These buffers hold
VALID and payload stable during backpressure. AW admission establishes
the W route, so source W acceptance starts after its AW has been admitted.
W can then progress independently of the downstream AW handshake, while
its association with the correct source and target is retained.

Responses retain the request order separately for each source's read and
write streams, even when consecutive requests address different targets.
A faster response from a later target waits until the earlier response can
enter the source response buffer. Target response order identifies the
requesting source without AXI IDs. A response is then registered before
being presented upstream. Read and write response order is independent;
there is no combined B/R ordering constraint.

``S_ACCEPT`` and ``M_ISSUE`` limit routing contexts separately in each
fabric. Admission reserves a source entry and, for a mapped request, a target
entry, including requests still in a downstream channel buffer. The entries
are released when the response enters the source response buffer. A source
may therefore still hold buffered responses after routing capacity becomes
available for new requests. A response transfer can free capacity for a new
address at the same edge. These limits are not end-to-end counts of all
requests awaiting consumption of their upstream B or R response.

Address regions use target-major packing: region m/r occupies slice
``m*M_REGIONS+r`` in ``M_BASE_ADDR`` and ``M_ADDR_W``. A width w enables
a ``2**w``-byte region; width zero disables it. An entirely zero
``M_BASE_ADDR`` selects automatic aligned placement in that packed order.
Use aligned, nonoverlapping regions. ``M_CONNECT_RD`` and ``M_CONNECT_WR``
are independent matrices with bit ``m*S_COUNT+s`` controlling source s to
target m. ``M_SECURE[m]`` rejects that target's accesses with ``PROT[1] = 1``.
All connected interfaces must use matching address, data, strobe, and
applicable USER widths.

An unmapped address, a disabled connection, or a rejected nonsecure access
produces local DECERR (``0b11``) without forwarding that request to a target.
An invalid read returns zero data in its proper source order. An invalid
write first accepts AW and consumes its associated W beat, then returns B
with DECERR. Responses from an accessed target retain that target's response
code. WSTRB is forwarded with write data.

Reset inhibits new source AW, W, and AR acceptance. At a rising edge with
RST high, arbitration, routing queues, and channel buffers are cleared.
Already buffered downstream VALID or upstream BVALID/RVALID clears at that
edge, rather than combinationally when RST rises. Reset must also clear the
connected endpoints' in-flight accesses so no old request or response is
reintroduced after the fabric state is discarded.

Functional scenarios
--------------------

The examples use two sources, two targets, 32-bit addresses/data, and four
write strobes. S0/S1 denote source indices 0/1; M0/M1 denote target indices
0/1. Each uses the correspondingly indexed public read/write interfaces.
All illustrated writes use ``WSTRB = 0xF``. ``A0``, ``A1``, ... identify byte
addresses and ``D0``, ``D1``, ... identify data words, local to each scenario.

The configuration is the same in all examples:

.. code-block:: systemverilog

    .S_COUNT(2),
    .M_COUNT(2),
    .ADDR_W(32),
    .S_ACCEPT({32'd2, 32'd2}),
    .M_REGIONS(1),
    .M_BASE_ADDR('0),
    .M_ADDR_W({32'd16, 32'd16}),
    .M_CONNECT_RD(4'b1111),
    .M_CONNECT_WR(4'b0111),
    .M_ISSUE({32'd2, 32'd2}),
    .M_SECURE(2'b10)

.. list-table:: Address map and permitted paths
   :class: documentation-table
   :header-rows: 1
   :widths: 12 32 28 28

   * - Target
     - Automatically placed region
     - Reads
     - Writes
   * - M0
     - ``0x00000000`` through ``0x0000FFFF``
     - S0 and S1
     - S0 and S1
   * - M1
     - ``0x00010000`` through ``0x0001FFFF``
     - S0 and S1, secure accesses only
     - S0 only, secure accesses only

PROT is zero except for the explicitly nonsecure request below. A numbered
tick denotes a clock interval; transfers occur at its ending rising edge
when VALID and READY are high. ``x`` marks payloads or response codes that
are irrelevant while their VALID is low.

Parallel write and read to independent targets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: Concurrent accesses
   :class: documentation-table
   :header-rows: 1
   :widths: 22 33 11 34

   * - Access
     - Upstream request
     - Target
     - Result
   * - S0 write ``A0`` / ``D0``
     - AW and W offered from tick 1
     - M0
     - Successful B response
   * - S1 read ``A1``
     - AR offered in tick 1
     - M1
     - Successful R response with ``D1``

S0's AW and S1's AR are both accepted in tick 1. The corresponding target
addresses appear in tick 2. S0's W waits for the write route established
by AW, is accepted in tick 2, and transfers to M0 in tick 3.

M1 returns ``D1`` in tick 3 and S1 receives it in tick 4. M0's B response
transfers in tick 4 and reaches S0 in tick 5. Read progress does not wait
for the write data or B response; the two transactions use independent
request and response paths.

.. wavedrom::
    :name: axil-crossbar-parallel-timing
    :caption: Independent read and write paths advance through their channel buffers
    :alt: Independent read and write paths advance through their channel buffers.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p......."},
            {"name": "rst", "wave": "0......."},
            ["s_axil_wr[0]",
                ["Master",
                    {"name": "awvalid", "wave": "010....."},
                    {"name": "awaddr", "wave": "x=x.....", "data": ["A0"]},
                    {"name": "wvalid", "wave": "01.0...."},
                    {"name": "wdata", "wave": "x=.x....", "data": ["D0"]},
                    {"name": "bready", "wave": "1......."}
                ],
                ["Slave",
                    {"name": "awready", "wave": "010....."},
                    {"name": "wready", "wave": "0.10...."},
                    {"name": "bvalid", "wave": "0....10."},
                    {"name": "bresp", "wave": "x....=x.", "data": ["OKAY"]}
                ]
            ],
            {},
            ["s_axil_rd[1]",
                ["Master",
                    {"name": "arvalid", "wave": "010....."},
                    {"name": "araddr", "wave": "x=x.....", "data": ["A1"]},
                    {"name": "rready", "wave": "1......."}
                ],
                ["Slave",
                    {"name": "arready", "wave": "010....."},
                    {"name": "rvalid", "wave": "0...10.."},
                    {"name": "rdata", "wave": "x...=x..", "data": ["D1"]},
                    {"name": "rresp", "wave": "x...=x..", "data": ["OKAY"]}
                ]
            ],
            {},
            ["m_axil_wr[0]",
                ["Master",
                    {"name": "awvalid", "wave": "0.10...."},
                    {"name": "awaddr", "wave": "x.=x....", "data": ["A0"]},
                    {"name": "wvalid", "wave": "0..10..."},
                    {"name": "wdata", "wave": "x..=x...", "data": ["D0"]},
                    {"name": "bready", "wave": "0.1..0.."}
                ],
                ["Slave",
                    {"name": "awready", "wave": "1......."},
                    {"name": "wready", "wave": "1......."},
                    {"name": "bvalid", "wave": "0...10.."},
                    {"name": "bresp", "wave": "x...=x..", "data": ["OKAY"]}
                ]
            ],
            {},
            ["m_axil_rd[1]",
                ["Master",
                    {"name": "arvalid", "wave": "0.10...."},
                    {"name": "araddr", "wave": "x.=x....", "data": ["A1"]},
                    {"name": "rready", "wave": "0.1.0..."}
                ],
                ["Slave",
                    {"name": "arready", "wave": "1......."},
                    {"name": "rvalid", "wave": "0..10..."},
                    {"name": "rdata", "wave": "x..=x...", "data": ["D1"]},
                    {"name": "rresp", "wave": "x..=x...", "data": ["OKAY"]}
                ]
            ],
            {}
        ],
        "head": {"tick": 0},
        "config": {"hscale": 2}
    }

Target contention, capacity limits, and response order
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: Read requests and offered target responses
   :class: documentation-table
   :header-rows: 1
   :widths: 12 20 12 56

   * - Source
     - Address / data
     - Target
     - Request and response availability
   * - S0
     - ``A0`` / ``D0``
     - M0
     - Request from tick 1; target response from tick 6
   * - S0
     - ``A1`` / ``D1``
     - M1
     - Request from tick 2; target response from tick 4
   * - S1
     - ``A2`` / ``D2``
     - M0
     - Request from tick 1; target response from tick 7
   * - S0
     - ``A3`` / ``D3``
     - M1
     - Request from tick 3; target response from tick 8
   * - S1
     - ``A4`` / ``D4``
     - M0
     - Request from tick 3; target response from tick 8

Both sources initially request M0. Its reset priority accepts S0's ``A0``
in tick 1, then S1's ``A2`` in tick 2. M0 sees those addresses in ticks 2
and 3. S0's independent request ``A1`` to M1 is admitted in tick 2 and
appears at M1's target interface in tick 3.

S0 then holds ``A3`` with ARVALID high in ticks 3 through 6. Its two source
routing entries are occupied by ``A0`` and ``A1``. S1 holds ``A4`` over the
same interval because both M0 target entries are occupied by ``A0`` and
``A2``. Neither request loses its address while waiting.

M1 offers ``D1`` from tick 4, but its RREADY remains low through tick 6:
S0's earlier ``A0`` response has not yet arrived. M0 returns ``D0`` in
tick 6. Capturing it frees routing capacity and permits both waiting AR
requests to be admitted at that same edge, even though S0 still holds
its upstream RREADY low.

In tick 7, M1's ``D1`` and M0's ``D2`` transfer into their respective source
response buffers. S1 receives ``D2`` in tick 8 and ``D4`` in tick 9.
S0's output holds ``D0`` unchanged in ticks 7 through 10. Its buffer also
retains ``D1``, so M1's next response ``D3`` waits in ticks 8 through 10.
After S0 resumes, it consumes ``D0``, ``D1``, and ``D3`` in ticks 10, 11,
and 12. The accepted request order survives both differing target latency
and upstream backpressure.

.. wavedrom::
    :name: axil-crossbar-ordering-timing
    :caption: Routing capacity recovers while buffered responses preserve source order
    :alt: Routing capacity recovers while buffered responses preserve source order.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p............."},
            {"name": "rst", "wave": "0............."},
            ["s_axil_rd[0]",
                ["Master",
                    {"name": "arvalid", "wave": "01.....0......"},
                    {"name": "araddr", "wave": "x===...x......", "data": ["A0", "A1", "A3"]},
                    {"name": "rready", "wave": "0.........1..."}
                ],
                ["Slave",
                    {"name": "arready", "wave": "01.0..10......"},
                    {"name": "rvalid", "wave": "0......1.....0"},
                    {"name": "rdata", "wave": "x......=...==x", "data": ["D0", "D1", "D3"]},
                    {"name": "rresp", "wave": "x......=.....x", "data": ["OKAY"]}
                ]
            ],
            {},
            ["s_axil_rd[1]",
                ["Master",
                    {"name": "arvalid", "wave": "01.....0......"},
                    {"name": "araddr", "wave": "x=.=...x......", "data": ["A2", "A4"]},
                    {"name": "rready", "wave": "1............."}
                ],
                ["Slave",
                    {"name": "arready", "wave": "0.10..10......"},
                    {"name": "rvalid", "wave": "0.......1.0..."},
                    {"name": "rdata", "wave": "x.......==x...", "data": ["D2", "D4"]},
                    {"name": "rresp", "wave": "x.......=.x...", "data": ["OKAY"]}
                ]
            ],
            {},
            ["m_axil_rd[0]",
                ["Master",
                    {"name": "arvalid", "wave": "0.1.0..10....."},
                    {"name": "araddr", "wave": "x.==x..=x.....", "data": ["A0", "A2", "A4"]},
                    {"name": "rready", "wave": "0.1......0...."}
                ],
                ["Slave",
                    {"name": "arready", "wave": "1............."},
                    {"name": "rvalid", "wave": "0.....1..0...."},
                    {"name": "rdata", "wave": "x.....===x....", "data": ["D0", "D2", "D4"]},
                    {"name": "rresp", "wave": "x.....=..x....", "data": ["OKAY"]}
                ]
            ],
            {},
            ["m_axil_rd[1]",
                ["Master",
                    {"name": "arvalid", "wave": "0..10..10....."},
                    {"name": "araddr", "wave": "x..=x..=x.....", "data": ["A1", "A3"]},
                    {"name": "rready", "wave": "0......10..10."}
                ],
                ["Slave",
                    {"name": "arready", "wave": "1............."},
                    {"name": "rvalid", "wave": "0...1.......0."},
                    {"name": "rdata", "wave": "x...=...=...x.", "data": ["D1", "D3"]},
                    {"name": "rresp", "wave": "x...=.......x.", "data": ["OKAY"]}
                ]
            ],
            {}
        ],
        "head": {"tick": 0},
        "config": {"hscale": 2}
    }

Local errors for address and permission failures
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All requests here originate at S1.

.. list-table:: Rejected accesses and an allowed retry
   :class: documentation-table
   :header-rows: 1
   :widths: 30 34 36

   * - Access
     - Address / attributes
     - Result
   * - Read ``A0`` in tick 1
     - Outside both configured regions
     - Local DECERR with zero read data
   * - Write ``A1`` / ``D1`` from tick 1
     - M1, secure
     - Local DECERR because the S1-to-M1 write path is disabled
   * - Read ``A2`` in tick 5
     - M1, ``ARPROT = 0b010``
     - Local DECERR because M1 requires a secure access
   * - Read ``A2`` in tick 8
     - Same address, ``ARPROT = 0b000``
     - Forwarded to M1 and returns ``D2`` with OKAY

The unmapped AR is accepted in tick 1 and returns local R/DECERR with zero
data in tick 3. The blocked write's AW is also accepted in tick 1, its W
is consumed locally in tick 2, and B/DECERR appears in tick 4. No target
AW or W transfer is generated for that write.

The nonsecure read in tick 5 returns local R/DECERR with zero data in tick 7.
Repeating ``A2`` with secure attributes in tick 8 permits routing: M1
accepts AR in tick 9, returns ``D2`` in tick 10, and S1 receives R/OKAY
in tick 11. Only this final read reaches a downstream target.

.. wavedrom::
    :name: axil-crossbar-errors-timing
    :caption: Rejected accesses return local DECERR and only the secure read reaches M1
    :alt: Rejected accesses return local DECERR and only the secure read reaches M1.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p............"},
            {"name": "rst", "wave": "0............"},
            ["s_axil_wr[1]",
                ["Master",
                    {"name": "awvalid", "wave": "010.........."},
                    {"name": "awaddr", "wave": "x=x..........", "data": ["A1"]},
                    {"name": "wvalid", "wave": "01.0........."},
                    {"name": "wdata", "wave": "x=.x.........", "data": ["D1"]},
                    {"name": "bready", "wave": "1............"}
                ],
                ["Slave",
                    {"name": "awready", "wave": "010.........."},
                    {"name": "wready", "wave": "0.10........."},
                    {"name": "bvalid", "wave": "0...10......."},
                    {"name": "bresp", "wave": "x...=x.......", "data": ["DECERR"]}
                ]
            ],
            {},
            ["s_axil_rd[1]",
                ["Master",
                    {"name": "arvalid", "wave": "010..10.10..."},
                    {"name": "araddr", "wave": "x=x..=x.=x...", "data": ["A0", "A2", "A2"]},
                    {"name": "arprot", "wave": "x=x..=x.=x...", "data": ["0b000", "0b010", "0b000"]},
                    {"name": "rready", "wave": "1............"}
                ],
                ["Slave",
                    {"name": "arready", "wave": "010..10.10..."},
                    {"name": "rvalid", "wave": "0..10..10..10"},
                    {"name": "rdata", "wave": "x..=x..=x..=x", "data": ["0", "0", "D2"]},
                    {"name": "rresp", "wave": "x..=x..=x..=x", "data": ["DECERR", "DECERR", "OKAY"]}
                ]
            ],
            {},
            ["m_axil_wr[0]",
                ["Master",
                    {"name": "awvalid", "wave": "0............"},
                    {"name": "wvalid", "wave": "0............"}
                ],
                {}
            ],
            ["m_axil_rd[0]", ["Master", {"name": "arvalid", "wave": "0............"}, {}], {}],
            {},
            ["m_axil_wr[1]",
                ["Master",
                    {"name": "awvalid", "wave": "0............"},
                    {"name": "wvalid", "wave": "0............"}
                ],
                {}
            ],
            {},
            ["m_axil_rd[1]",
                ["Master",
                    {"name": "arvalid", "wave": "0........10.."},
                    {"name": "araddr", "wave": "x........=x..", "data": ["A2"]},
                    {"name": "arprot", "wave": "x........=x..", "data": ["0b000"]},
                    {"name": "rready", "wave": "0........1.0."}
                ],
                ["Slave",
                    {"name": "arready", "wave": "1............"},
                    {"name": "rvalid", "wave": "0.........10."},
                    {"name": "rdata", "wave": "x.........=x.", "data": ["D2"]},
                    {"name": "rresp", "wave": "x.........=x.", "data": ["OKAY"]}
                ]
            ],
            {}
        ],
        "head": {"tick": 0},
        "config": {"hscale": 2}
    }

Reset clears held responses and queued target requests
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Both targets reset with the fabric. S0 initially holds RREADY low, and M1
holds ARREADY low until reset is released.

.. list-table:: Accesses across reset
   :class: documentation-table
   :header-rows: 1
   :widths: 26 44 30

   * - Access
     - State before reset
     - Result
   * - S0 read ``A0`` from M0
     - ``D0`` is held at the source response output
     - Buffered response discarded
   * - S1 read ``A1`` from M1
     - AR is buffered and waits for target READY
     - Queued target request discarded
   * - S0 read ``A2`` from M1
     - Offered after reset
     - New request returns ``D2``

Both initial AR requests are admitted in tick 1. M0 accepts ``A0`` in
tick 2 and returns ``D0`` in tick 3; S0's RVALID holds that data from
tick 4. M1's ARVALID holds ``A1`` from tick 2 because ARREADY remains low.

RST is asserted in ticks 5 and 6. Source ARREADY is already low in tick 5,
but the buffered ``D0`` and pending target ARVALID remain visible until
the reset sampling edge. Both VALID outputs are zero in tick 6. Neither
the held source response nor the unaccepted target request is replayed.

RST is released in tick 7. The registered channel readiness recovers at
that interval's ending edge, so the new ``A2`` request offered in tick 7
is accepted in tick 8. M1 receives it in tick 9, returns ``D2`` in tick 10,
and S0 consumes the response in tick 11.

.. wavedrom::
    :name: axil-crossbar-reset-timing
    :caption: Reset removes a held response and an unaccepted downstream address
    :alt: Reset removes a held response and an unaccepted downstream address.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p............."},
            {"name": "rst", "wave": "0....1.0......"},
            ["s_axil_rd[0]",
                ["Master",
                    {"name": "arvalid", "wave": "010....1.0...."},
                    {"name": "araddr", "wave": "x=x....=.x....", "data": ["A0", "A2"]},
                    {"name": "rready", "wave": "0......1......"}
                ],
                ["Slave",
                    {"name": "arready", "wave": "010.....10...."},
                    {"name": "rvalid", "wave": "0...1.0....10."},
                    {"name": "rdata", "wave": "x...=.x....=x.", "data": ["D0", "D2"]},
                    {"name": "rresp", "wave": "x...=.x....=x.", "data": ["OKAY", "OKAY"]}
                ]
            ],
            {},
            ["s_axil_rd[1]",
                ["Master",
                    {"name": "arvalid", "wave": "010..........."},
                    {"name": "araddr", "wave": "x=x...........", "data": ["A1"]},
                    {"name": "rready", "wave": "0......1......"}
                ],
                ["Slave",
                    {"name": "arready", "wave": "010..........."},
                    {"name": "rvalid", "wave": "0............."},
                    {"name": "rdata", "wave": "x............."},
                    {"name": "rresp", "wave": "x............."}
                ]
            ],
            {},
            ["m_axil_rd[0]",
                ["Master",
                    {"name": "arvalid", "wave": "0.10.........."},
                    {"name": "araddr", "wave": "x.=x..........", "data": ["A0"]},
                    {"name": "rready", "wave": "0.1.0........."}
                ],
                ["Slave",
                    {"name": "arready", "wave": "1............."},
                    {"name": "rvalid", "wave": "0..10........."},
                    {"name": "rdata", "wave": "x..=x.........", "data": ["D0"]},
                    {"name": "rresp", "wave": "x..=x.........", "data": ["OKAY"]}
                ]
            ],
            {},
            ["m_axil_rd[1]",
                ["Master",
                    {"name": "arvalid", "wave": "0.1...0..10..."},
                    {"name": "araddr", "wave": "x.=...x..=x...", "data": ["A1", "A2"]},
                    {"name": "rready", "wave": "0.1...0..1.0.."}
                ],
                ["Slave",
                    {"name": "arready", "wave": "0......1......"},
                    {"name": "rvalid", "wave": "0.........10.."},
                    {"name": "rdata", "wave": "x.........=x..", "data": ["D2"]},
                    {"name": "rresp", "wave": "x.........=x..", "data": ["OKAY"]}
                ]
            ],
            {}
        ],
        "head": {"tick": 0},
        "config": {"hscale": 2}
    }

.. _verification-openenoc-axil-crossbar:

Verification
------------

The test suite is in ``dv/core/openenoc_axil_crossbar/``.

Testbench
~~~~~~~~~

This cocotb suite verifies the AXI4-Lite crossbar and its address decoder, read/write paths, and
channel skid buffers.

Coverage
~~~~~~~~

The suite covers:

- address routing, decode errors, and reset;

- simultaneous initiators and response ordering across targets;

- independent AW/W backpressure and stable stalled payloads;

- sustained traffic with consecutive target-side AR, AW, and W handshakes when uncontended.
