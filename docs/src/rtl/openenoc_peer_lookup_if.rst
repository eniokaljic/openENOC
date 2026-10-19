.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-peer-lookup-if:

Endpoint peer lookup -- openenoc_peer_lookup_if
===============================================

.. index::
   single: openenoc_peer_lookup_if

Defines peer queries and coherent configuration responses for endpoint clients.

**Source:**
:download:`openenoc_peer_lookup_if.sv <../../../hw/rtl/core/openenoc_peer_lookup_if.sv>`.

Parameters
----------

.. list-table:: Parameters
   :class: rtl-reference-table
   :header-rows: 1
   :widths: 20 30 20 30

   * - Name
     - Default value
     - Allowed values
     - Description
   * - ``NUM_OF_PEERS``
     - ``4``
     - Integer >= 1; match generated CSR array
     - Number of peer-table entries.
   * - ``PEER_IDX_W``
     - ``NUM_OF_PEERS > 1 ? $clog2(NUM_OF_PEERS) : 1``
     - Integer >= 1; enough bits for the peer count
     - Width of local peer indices; all connected interfaces must agree.
   * - ``ADDR_W``
     - ``32``
     - Integer >= 1
     - Byte-address width in bits; connected interfaces must agree.

Connected interfaces must agree on all three parameters. The current
:ref:`rtl-endpoint-peer-lookup` implementation requires ``ADDR_W = 32``
to match the generated peer CSR fields.

Signals
-------

Directions are relative to the ``mst`` and ``slv`` modports. The ``mon``
modport observes all signals as inputs.

.. list-table:: Public signals and interfaces
   :class: rtl-reference-table
   :header-rows: 1
   :widths: 22 28 16 34

   * - Name
     - Type
     - Direction / role
     - Description
   * - ``req_valid``
     - ``logic``
     - mst: output; slv: input
     - Request fields are valid and retained until accepted.
   * - ``req_ready``
     - ``logic``
     - mst: input; slv: output
     - Accepts the request when req_valid is also asserted.
   * - ``req_type``
     - ``logic [1:0]``
     - mst: output; slv: input
     - Lookup kind: index, RMEM address, or MAC address.
   * - ``req_mode_mask``
     - ``logic [3:0]``
     - mst: output; slv: input
     - Eligible DMA-mode bitmap; zero permits no entry.
   * - ``req_peer_idx``
     - ``logic [PEER_IDX_W-1:0]``
     - mst: output; slv: input
     - Peer index used only for LOOKUP_BY_INDEX.
   * - ``req_rmem_addr``
     - ``logic [ADDR_W-1:0]``
     - mst: output; slv: input
     - Scalar-memory byte address used only for LOOKUP_BY_RMEM.
   * - ``req_mac_addr``
     - ``logic [47:0]``
     - mst: output; slv: input
     - MAC address used only for LOOKUP_BY_MAC.
   * - ``rsp_valid``
     - ``logic``
     - mst: input; slv: output
     - Response snapshot is valid and retained until accepted.
   * - ``rsp_ready``
     - ``logic``
     - mst: output; slv: input
     - Accepts the response when rsp_valid is also asserted.
   * - ``rsp_hit``
     - ``logic``
     - mst: input; slv: output
     - An eligible peer entry matched.
   * - ``rsp_peer_idx``
     - ``logic [PEER_IDX_W-1:0]``
     - mst: input; slv: output
     - Matched peer entry index; zero on a miss.
   * - ``rsp_mac_addr``
     - ``logic [47:0]``
     - mst: input; slv: output
     - Matched peer MAC address.
   * - ``rsp_rmem_offset``
     - ``logic [ADDR_W-1:0]``
     - mst: input; slv: output
     - Matched virtual scalar-memory base/offset.
   * - ``rsp_local_addr``
     - ``logic [ADDR_W-1:0]``
     - mst: input; slv: output
     - Matched local memory-window base.
   * - ``rsp_remote_addr``
     - ``logic [ADDR_W-1:0]``
     - mst: input; slv: output
     - Matched remote memory-window base.
   * - ``rsp_size``
     - ``logic [ADDR_W-1:0]``
     - mst: input; slv: output
     - Matched memory-window size in bytes.
   * - ``rsp_dma_mode``
     - ``logic [1:0]``
     - mst: input; slv: output
     - Matched peer mode: disabled, RMEM, mirror-to-remote, or mirror-to-local.
   * - ``rsp_irq_enable``
     - ``logic``
     - mst: input; slv: output
     - Matched peer DMA event-enable setting.

Architecture and operation
--------------------------

**Parameters and roles:** ``NUM_OF_PEERS`` defaults to 4; ``PEER_IDX_W`` is
derived with a minimum of one bit; ``ADDR_W`` defaults to 32. Modports are
``mst``, ``slv``, and ``mon``.

Request and response channels use independent ready/valid handshakes. A
request transfers on a rising edge with ``req_valid && req_ready``; a
response transfers on a rising edge with ``rsp_valid && rsp_ready``.

The master asserts ``req_valid`` when a request is available, without
waiting for ``req_ready``. It retains the request and its meaningful fields
while ``req_valid && !req_ready``. After acceptance, it may deassert
``req_valid`` or present the next request. Keeping ``req_valid`` high does
not merge transfers: each edge with both request handshake signals high
accepts another request.

The slave retains ``rsp_valid`` and all response fields while
``rsp_valid && !rsp_ready``. The master samples the snapshot only when
both response handshake signals are high. Request acceptance and response
completion are separate events; neither a fixed response latency nor a
fixed number of outstanding requests is specified by the interface.

``req_type`` selects ``LOOKUP_BY_INDEX`` (0), ``LOOKUP_BY_RMEM`` (1), or
``LOOKUP_BY_MAC`` (2). Only the selected key, respectively ``req_peer_idx``,
``req_rmem_addr``, or ``req_mac_addr``, is meaningful. ``req_mode_mask[n]``
permits entries whose ``dma.mode`` is n. A zero mask matches nothing; callers
normally leave bit zero clear, and the current lookup block also excludes
disabled entries.

.. list-table:: Lookup request types
   :class: documentation-table
   :header-rows: 1
   :widths: 14 32 54

   * - Code
     - Interface constant
     - Selected key
   * - 0
     - ``LOOKUP_BY_INDEX``
     - ``req_peer_idx``
   * - 1
     - ``LOOKUP_BY_RMEM``
     - ``req_rmem_addr``
   * - 2
     - ``LOOKUP_BY_MAC``
     - ``req_mac_addr``

The interface defines ``DMA_MODE_DISABLED`` (0), ``DMA_MODE_RMEM`` (1),
``DMA_MODE_MIRROR_TO_LOCAL`` (2), and ``DMA_MODE_MIRROR_TO_REMOTE`` (3) for
``rsp_dma_mode`` and the mask bit indices. ``LOOKUP_RMEM_MODE_MASK`` selects
RMEM entries, ``LOOKUP_MIRROR_MODE_MASK`` selects both mirror modes, and
``LOOKUP_ACTIVE_MODE_MASK`` combines all three active modes. The masks are
derived from the mode constants.

.. list-table:: Peer DMA modes
   :class: documentation-table
   :header-rows: 1
   :widths: 14 32 54

   * - Code / mask bit
     - Interface constant
     - Meaning
   * - 0
     - ``DMA_MODE_DISABLED``
     - Disabled peer entry.
   * - 1
     - ``DMA_MODE_RMEM``
     - Scalar RMEM address mapping.
   * - 2
     - ``DMA_MODE_MIRROR_TO_LOCAL``
     - Bulk DMA copies remote memory into local memory.
   * - 3
     - ``DMA_MODE_MIRROR_TO_REMOTE``
     - Bulk DMA copies local memory into remote memory.

The response is a coherent snapshot: ``rsp_hit``, ``rsp_peer_idx``,
``rsp_mac_addr``, ``rsp_rmem_offset``, ``rsp_local_addr``, ``rsp_remote_addr``,
``rsp_size``, ``rsp_dma_mode``, and ``rsp_irq_enable``. Entry fields are zero
on a miss. The implementation is :ref:`rtl-endpoint-peer-lookup`.

Clock and reset belong to the connected modules. The interface contains no
clock/reset ports or internal storage.

Functional scenarios
--------------------

The examples use ``NUM_OF_PEERS = 4`` and ``ADDR_W = 32``.
``I0``, ``I1``, and ``I2`` denote peer indices; ``A0``, ``A1``,
and subsequent ``A`` labels denote addresses. ``M0``, ``M1``, and
``M2`` denote mode masks; ``S0`` and ``S1`` denote window sizes.
Labels are local to each diagram.

``clk`` is the common clock of the connected logic, shown as a sampling
reference. Numbered cycles label intervals between rising edges; transfers
occur at each interval's ending rising edge when VALID and READY are both
high. Shaded ``x`` regions mark irrelevant values, not a requirement to
drive unknowns. The shown response latencies are illustrative.

Query by peer index, scalar address, or MAC address
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Three requests use the same channel in sequence. The first presents
``req_peer_idx = I0`` with ``req_type = LOOKUP_BY_INDEX`` in cycle 1
and is accepted in cycle 2. Its response transfers in cycle 3 and contains
peer index ``I0`` with configured MAC address ``A2``.

The second presents scalar-memory address ``A0`` with
``req_type = LOOKUP_BY_RMEM`` in cycle 5 and is accepted in cycle 6.
Its response transfers in cycle 7 and identifies peer ``I1`` with MAC
address ``A3``. The third presents MAC address ``A1`` with
``req_type = LOOKUP_BY_MAC`` in cycle 9 and is accepted in cycle 10.
Its response transfers in cycle 11 and identifies peer ``I2`` with
the same MAC address ``A1``. Only the selected request key is meaningful.

All three requests select eligible entries, so ``rsp_hit = 1`` with
each response. The mode masks are ``M0 = 0xC`` for modes 2/3,
``M1 = 0x2`` for mode 1, and ``M2 = 0xE`` for modes 1/2/3.

.. wavedrom::
    :name: peer-lookup-if-query-types-timing
    :caption: Peer queries selected by index, scalar address, and MAC address
    :alt: Index, scalar-address, and MAC-address queries each return a peer response.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p..........."},
            ["Master",
                {"name": "req_valid", "wave": "01.0.1.0.1.0"},
                {
                    "name": "req_type",
                    "wave": "x=.x.=.x.=.x",
                    "data": ["LOOKUP_\nBY_INDEX", "LOOKUP_\nBY_RMEM", "LOOKUP_\nBY_MAC"]
                },
                {"name": "req_mode_mask", "wave": "x=.x.=.x.=.x", "data": ["M0", "M1", "M2"]},
                {"name": "req_peer_idx", "wave": "x=.x........", "data": ["I0"]},
                {"name": "req_rmem_addr", "wave": "x....=.x....", "data": ["A0"]},
                {"name": "req_mac_addr", "wave": "x........=.x", "data": ["A1"]},
                {"name": "rsp_ready", "wave": "1..........."}
            ],
            ["Slave",
                {"name": "req_ready", "wave": "0.10..10..10"},
                {"name": "rsp_valid", "wave": "0..10..10..1"},
                {"name": "rsp_hit", "wave": "x..1x..1x..1"},
                {"name": "rsp_peer_idx", "wave": "x..=x..=x..=", "data": ["I0", "I1", "I2"]},
                {"name": "rsp_mac_addr", "wave": "x..=x..=x..=", "data": ["A2", "A3", "A1"]}
            ]
        ],
        "head": {"tick": 0},
        "config": {"hscale": 1}
    }

Mode mask and response status
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Assume MAC address ``A0`` belongs to a single enabled peer ``I0``
whose DMA mode is ``DMA_MODE_MIRROR_TO_LOCAL``. Both requests use
``LOOKUP_BY_MAC`` and the same address; only ``req_mode_mask`` differs.

The first request uses ``M0 = 0x4``, permitting ``DMA_MODE_MIRROR_TO_LOCAL``. It is accepted
in cycle 2, and its response transfers in cycle 3 with ``rsp_hit = 1``,
``rsp_peer_idx = I0``, ``rsp_mac_addr = A0``, and
``rsp_dma_mode = DMA_MODE_MIRROR_TO_LOCAL``.

The second request uses ``M1 = 0x2``, permitting only ``DMA_MODE_RMEM``, and is
accepted in cycle 6. Its response transfers in cycle 7 with
``rsp_hit = 0`` and all entry fields zero. This response uses the same
VALID/READY handshake and completes normally. The status bit describes the
returned snapshot; it does not suppress completion.

.. wavedrom::
    :name: peer-lookup-if-mode-mask-timing
    :caption: Mode masks carried with MAC queries and their response status
    :alt: The same MAC query uses two mode masks and completes with different response status.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p........"},
            ["Master",
                {"name": "req_valid", "wave": "01.0.1.0."},
                {
                    "name": "req_type",
                    "wave": "x=.x.=.x.",
                    "data": ["LOOKUP_\nBY_MAC", "LOOKUP_\nBY_MAC"]
                },
                {"name": "req_mode_mask", "wave": "x=.x.=.x.", "data": ["M0", "M1"]},
                {"name": "req_mac_addr", "wave": "x=.x.=.x.", "data": ["A0", "A0"]},
                {"name": "rsp_ready", "wave": "1........"}
            ],
            ["Slave",
                {"name": "req_ready", "wave": "0.10..10."},
                {"name": "rsp_valid", "wave": "0..10..10"},
                {"name": "rsp_hit", "wave": "x..1x..0x"},
                {"name": "rsp_peer_idx", "wave": "x..=x..=x", "data": ["I0", "0"]},
                {"name": "rsp_mac_addr", "wave": "x..=x..=x", "data": ["A0", "0"]},
                {
                    "name": "rsp_dma_mode",
                    "wave": "x..=x..=x",
                    "style": "font-size: 8px;",
                    "data": ["DMA_\nMODE_\nMIRROR_\nTO_\nLOCAL", "DMA_\nMODE_\nDISABLED"]
                }
            ]
        ],
        "head": {"tick": 0},
        "config": {"hscale": 1}
    }

Request backpressure and retained response snapshot
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The master presents an index query for ``I0`` in cycle 1. With
``req_ready = 0`` in cycles 1 and 2, it keeps ``req_valid = 1``,
the selected key, the lookup type, and ``M0 = 0x4`` unchanged.
The request is accepted in cycle 3 when ``req_ready = 1``.
The master deasserts ``req_valid`` in cycle 4.

The response becomes valid in cycle 4, while ``rsp_ready = 0``.
Its entire snapshot remains stable through cycle 7, including
``rsp_hit``, the peer index, all addresses, the window size, DMA mode,
and IRQ enable. For example, a peer-configuration update in cycle 5 does
not replace this pending response. The master asserts ``rsp_ready``
in cycle 7 and samples the original snapshot at the ending rising edge.

A new query for the same ``I0`` is presented in cycle 9 and accepted
in cycle 10. Its response transfers in cycle 11 and reflects the updated
configuration: the address fields change from ``A0/A2/A4/A6`` to
``A1/A3/A5/A7``, the size changes from ``S0`` to ``S1``, and
IRQ enable changes from 0 to 1. The peer index and DMA mode remain the same.
Each response therefore retains the entry captured for its accepted request.

.. wavedrom::
    :name: peer-lookup-if-backpressure-timing
    :caption: Request backpressure and a coherent response retained until acceptance
    :alt: A stalled request is accepted in cycle 3; its response stays stable until cycle 7.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p............"},
            ["Master",
                {"name": "req_valid", "wave": "01..0....1.0."},
                {
                    "name": "req_type",
                    "wave": "x=..x....=.x.",
                    "data": ["LOOKUP_\nBY_INDEX", "LOOKUP_\nBY_INDEX"]
                },
                {"name": "req_mode_mask", "wave": "x=..x....=.x.", "data": ["M0", "M0"]},
                {"name": "req_peer_idx", "wave": "x=..x....=.x.", "data": ["I0", "I0"]},
                {"name": "rsp_ready", "wave": "0......1....."}
            ],
            ["Slave",
                {"name": "req_ready", "wave": "0..10.....10."},
                {"name": "rsp_valid", "wave": "0...1...0..10"},
                {"name": "rsp_hit", "wave": "x...1...x..1x"},
                {"name": "rsp_peer_idx", "wave": "x...=...x..=x", "data": ["I0", "I0"]},
                {"name": "rsp_mac_addr", "wave": "x...=...x..=x", "data": ["A0", "A1"]},
                {"name": "rsp_rmem_offset", "wave": "x...=...x..=x", "data": ["A2", "A3"]},
                {"name": "rsp_local_addr", "wave": "x...=...x..=x", "data": ["A4", "A5"]},
                {"name": "rsp_remote_addr", "wave": "x...=...x..=x", "data": ["A6", "A7"]},
                {"name": "rsp_size", "wave": "x...=...x..=x", "data": ["S0", "S1"]},
                {
                    "name": "rsp_dma_mode",
                    "wave": "x...=...x..=x",
                    "style": "font-size: 8px;",
                    "data": ["DMA_MODE_MIRROR_TO_LOCAL", "DMA_\nMODE_\nMIRROR_\nTO_\nLOCAL"]
                },
                {"name": "rsp_irq_enable", "wave": "x...0...x..1x"}
            ]
        ],
        "head": {"tick": 0},
        "config": {"hscale": 1}
    }
