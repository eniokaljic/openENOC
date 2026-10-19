.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-cpuif-axil-adapter:

CPUIF to AXI4-Lite -- openenoc_cpuif_axil_adapter
=================================================

.. index::
   single: openenoc_cpuif_axil_adapter

Converts native CPU register accesses into AXI4-Lite memory transactions.

**Source:** :download:`openenoc_cpuif_axil_adapter.sv <../../../hw/rtl/core/openenoc_cpuif_axil_adapter.sv>`.

Parameters
----------

.. list-table:: Parameters
   :class: rtl-reference-table
   :header-rows: 1
   :widths: 26 18 20 36

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

Interface ports contain channels in both directions. The table identifies
the selected modport or stream role; member directions follow that interface.

.. list-table:: Public signals and interfaces
   :class: rtl-reference-table
   :header-rows: 1
   :widths: 16 27 17 40

   * - Name
     - Type
     - Direction / role
     - Description
   * - ``clk``
     - ``logic``
     - input
     - Common sampling clock for the CPUIF and AXI4-Lite interfaces.
   * - ``rst``
     - ``logic``
     - input
     - Active-high synchronous reset of retained request state; immediately
       suppresses AXI VALID/READY outputs and CPUIF acknowledgements.
   * - ``s_cpuif``
     - ``openenoc_cpuif_if.slv``
     - bidirectional (slv)
     - Native register-access slave accepting requests.
   * - ``m_axil_wr``
     - ``taxi_axil_if.wr_mst``
     - bidirectional (wr_mst)
     - Outgoing AXI4-Lite write channels.
   * - ``m_axil_rd``
     - ``taxi_axil_if.rd_mst``
     - bidirectional (rd_mst)
     - Outgoing AXI4-Lite read channels.

Architecture and operation
--------------------------

``s_cpuif`` is the native slave; ``m_axil_wr`` and ``m_axil_rd`` are AXI4-Lite
master views. Their address/data widths must agree. DATA width must be a
multiple of eight, with one AXI write strobe per byte. Addresses pass through
unchanged. AWPROT, ARPROT, and request USER fields are zero; response USER
fields do not affect native completion.

The adapter retains one active request and has no queue for additional native
requests. The requester pulses REQ with the complete address, operation type,
write data, and bit enables, then waits for the matching acknowledgement.
A new request is accepted when idle or in the preceding operation's
acknowledgement interval. A REQ pulse earlier in an active operation is not
buffered. Holding REQ through completion presents another request at that
edge, so the requester must distinguish the old request from its successor.

An accepted request drives the corresponding AXI VALID and payload signals
directly in its launch interval. If an AXI channel is not ready, the adapter
stores the request and keeps that channel's VALID and payload stable until
its handshake. AW and W complete independently: accepting one does not
withdraw the other, and an accepted channel is not sent again. AR follows
the same retention rule for reads. Native request fields may change after
the REQ interval without disturbing a stalled AXI transfer.

CPUIF write enables must be uniform within each byte to preserve their
meaning across this boundary. Each WSTRB bit is the reduction AND of the
corresponding eight ``wr_biten`` bits. A fully enabled byte produces one;
a fully disabled byte produces zero. A partially enabled byte also produces
zero, and the adapter does not report an error for that conversion.
Arbitrary per-bit masks therefore require a different access mechanism.

Once the active request has been registered, BREADY is high for a write or
RREADY is high for a read. The selected READY remains high even while an
address or write-data channel is stalled. The AXI target supplies a response
only after accepting the required request channels.

For an active write, BVALID produces ``wr_ack`` in the same interval as the
B handshake. For an active read, RVALID produces ``rd_ack`` in the same
interval as the R handshake, with ``rd_data`` taken directly from RDATA.
There is no extra registered response stage or response FIFO. ``OKAY``
(``0b00``) gives ERR zero; any nonzero BRESP or RRESP gives the matching
native ERR together with ACK. ACK is not conditional on the current REQ
level. Native read data is meaningful only with ``rd_ack``.

If the requester presents the next request with that acknowledgement, its
AXI request channels can handshake at the same edge as the old response.
The old response still completes the old native operation; the newly
launched request becomes active after that edge. Its response READY is
then selected according to its own operation type.

Asserting ``rst`` immediately lowers AWVALID, WVALID, ARVALID, BREADY,
RREADY, and both native ACK/ERR pairs. The next rising edge clears the
retained request and pending channels. Reset can thus withdraw a stalled
channel without returning a completion for the cancelled native request.
The connected AXI target must also discard any part of that aborted access
before new traffic resumes.

Functional scenarios
--------------------

The examples use 32-bit addresses and data with four AXI byte strobes.
A numbered tick denotes a clock interval. Native request sampling,
AXI handshakes, and native completion occur at its ending rising edge.
``x`` marks fields that are irrelevant without REQ, VALID, or ACK.
Labels ``A0``, ``A1``, ... denote byte addresses, ``D0``, ``D1``, ... denote
data words, and ``M0``/``M1`` denote native bit masks. Labels are local
to each scenario. Native payload fields change after each REQ pulse;
the stalled AXI channels retain the captured values.

Byte-enabled writes with independent AW and W acceptance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: Write accesses
   :class: documentation-table
   :header-rows: 1
   :widths: 20 24 30 26

   * - Access
     - Native request
     - AXI request acceptance
     - Completion
   * - ``A0`` / ``D0`` / ``M0``
     - REQ pulse in tick 1
     - W in tick 1; AW in tick 4
     - B/OKAY and native write ACK in tick 5
   * - ``A1`` / ``D1`` / ``M1``
     - REQ pulse in tick 7
     - AW in tick 7; W in tick 10
     - B/OKAY and native write ACK in tick 11

For the first write, ``M0 = 0x00FF00FF`` enables bytes 0 and 2 and becomes
``S0 = 0b0101`` on WSTRB. WREADY is high when REQ arrives in tick 1, so
``D0`` and ``S0`` transfer immediately. AWREADY remains low through tick 3.
AWVALID stays high with ``A0`` until its tick-4 handshake, even though
native REQ has already returned low. WVALID drops after tick 1 because the
data has been accepted. The successful B response in tick 5 produces
``wr_ack = 1`` and ``wr_err = 0`` in that same interval.

The second write reverses the acceptance order. ``M1 = 0xFFFFFFFF`` becomes
``S1 = 0b1111``. AW transfers in tick 7, while WVALID holds ``D1`` and
``S1`` through the W handshake in tick 10. AWVALID stays low after its
earlier acceptance. The read channels remain idle for both writes.

.. wavedrom::
    :name: cpuif-axil-write-timing
    :caption: Write address and data remain pending independently until accepted
    :alt: Write address and data remain pending independently until accepted.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p............"},
            {"name": "rst", "wave": "0............"},
            [
                "s_cpuif",
                [
                    "Master",
                    {"name": "req", "wave": "010....10...."},
                    {"name": "req_is_wr", "wave": "x1x....1x...."},
                    {"name": "addr", "wave": "x=x....=x....", "data": ["A0", "A1"]},
                    {"name": "wr_data", "wave": "x=x....=x....", "data": ["D0", "D1"]},
                    {"name": "wr_biten", "wave": "x=x....=x....", "data": ["M0", "M1"]}
                ],
                [
                    "Slave",
                    {"name": "wr_ack", "wave": "0....10....10"},
                    {"name": "wr_err", "wave": "x....0x....0x"}
                ]
            ],
            {},
            [
                "m_axil_wr",
                [
                    "Master",
                    {"name": "awvalid", "wave": "01...0.10...."},
                    {"name": "awaddr", "wave": "x=...x.=x....", "data": ["A0", "A1"]},
                    {"name": "wvalid", "wave": "010....1...0."},
                    {"name": "wdata", "wave": "x=x....=...x.", "data": ["D0", "D1"]},
                    {"name": "wstrb", "wave": "x=x....=...x.", "data": ["S0", "S1"]},
                    {"name": "bready", "wave": "0.1...0.1...0"}
                ],
                [
                    "Slave",
                    {"name": "awready", "wave": "10..1........"},
                    {"name": "wready", "wave": "1......0..1.."},
                    {"name": "bvalid", "wave": "0....10....10"},
                    {
                        "name": "bresp",
                        "wave": "x....=x....=x",
                        "data": ["OKAY", "OKAY"]
                    }
                ]
            ],
            {}
        ],
        "head": {"tick": 0},
        "config": {"hscale": 2}
    }

Read address stalls and overlapping completion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All AXI write byte strobes are enabled in this example.

.. list-table:: Accesses and response association
   :class: documentation-table
   :header-rows: 1
   :widths: 20 22 24 32

   * - Access
     - Native REQ
     - AXI request accepted
     - AXI response and native completion
   * - Read ``A0``
     - Tick 1
     - AR in tick 3
     - R/OKAY with ``D0`` in tick 5
   * - Write ``A1`` / ``D1``
     - Tick 5, with the old read ACK
     - AW and W in tick 5
     - B/SLVERR in tick 7
   * - Read ``A2``
     - Tick 7, with the old write ACK
     - AR in tick 7
     - R/DECERR with ``D2`` in tick 9

The read REQ in tick 1 raises ARVALID immediately, but ARREADY is low in
ticks 1 and 2. ARADDR remains ``A0`` until the handshake in tick 3.
In tick 5, RVALID returns ``D0`` and produces ``rd_ack`` without an extra
clock interval. The simultaneous new REQ describes write ``A1`` / ``D1``;
its AW and W channels transfer at the same edge as the old R response.
``D0`` still belongs to ``A0``.

The write response in tick 7 has SLVERR (``0b10``), so ``wr_ack`` and
``wr_err`` rise together. The next read ``A2`` launches and its AR channel
transfers in that same interval. In tick 9, DECERR (``0b11``) produces
``rd_ack = rd_err = 1`` with ``rd_data = D2``. The response codes affect
the native error flags without delaying acknowledgement or changing the
association between a request and its data.

.. wavedrom::
    :name: cpuif-axil-handoff-timing
    :caption: Old responses complete while the next native request launches
    :alt: Old responses complete while the next native request launches.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p.........."},
            {"name": "rst", "wave": "0.........."},
            [
                "s_cpuif",
                [
                    "Master",
                    {"name": "req", "wave": "010..1010.."},
                    {"name": "req_is_wr", "wave": "x0x..1x0x.."},
                    {"name": "addr", "wave": "x=x..=x=x..", "data": ["A0", "A1", "A2"]},
                    {"name": "wr_data", "wave": "x....=x....", "data": ["D1"]}
                ],
                [
                    "Slave",
                    {"name": "wr_ack", "wave": "0......10.."},
                    {"name": "wr_err", "wave": "x......1x.."},
                    {"name": "rd_ack", "wave": "0....10..10"},
                    {"name": "rd_err", "wave": "x....0x..1x"},
                    {"name": "rd_data", "wave": "x....=x..=x", "data": ["D0", "D2"]}
                ]
            ],
            {},
            [
                "m_axil_wr",
                [
                    "Master",
                    {"name": "awvalid", "wave": "0....10...."},
                    {"name": "awaddr", "wave": "x....=x....", "data": ["A1"]},
                    {"name": "wvalid", "wave": "0....10...."},
                    {"name": "wdata", "wave": "x....=x....", "data": ["D1"]},
                    {"name": "bready", "wave": "0.....1.0.."}
                ],
                [
                    "Slave",
                    {"name": "awready", "wave": "1.........."},
                    {"name": "wready", "wave": "1.........."},
                    {"name": "bvalid", "wave": "0......10.."},
                    {"name": "bresp", "wave": "x......=x..", "data": ["SLVERR"]}
                ]
            ],
            {},
            [
                "m_axil_rd",
                [
                    "Master",
                    {"name": "arvalid", "wave": "01..0..10.."},
                    {"name": "araddr", "wave": "x=..x..=x..", "data": ["A0", "A2"]},
                    {"name": "rready", "wave": "0.1...0.1.0"}
                ],
                [
                    "Slave",
                    {"name": "arready", "wave": "10.1......."},
                    {"name": "rvalid", "wave": "0....10..10"},
                    {"name": "rdata", "wave": "x....=x..=x", "data": ["D0", "D2"]},
                    {
                        "name": "rresp",
                        "wave": "x....=x..=x",
                        "data": ["OKAY", "DECERR"]
                    }
                ]
            ],
            {}
        ],
        "head": {"tick": 0},
        "config": {"hscale": 2}
    }

Reset cancels a partially accepted write
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The AXI target is reset with the adapter and discards the partially accepted
old write. All write byte strobes are enabled.

.. list-table:: Accesses around reset
   :class: documentation-table
   :header-rows: 1
   :widths: 20 38 42

   * - Access
     - Request acceptance
     - Result
   * - Write ``A0`` / ``D0``
     - AW accepted in tick 1; W waits in ticks 1 and 2
     - Reset cancels the write without native ACK
   * - Read ``A1``
     - REQ and AR accepted in tick 5
     - ``D1`` and successful read ACK in tick 6
   * - Write ``A2`` / ``D2``
     - REQ, AW, and W accepted in tick 7
     - Successful write ACK in tick 8

RST is high in ticks 3 and 4. WVALID drops immediately in tick 3, so the
previously held ``D0`` cannot transfer even though WREADY is now high.
All request VALID and response READY outputs, and both native ACK/ERR pairs,
remain low during reset. The pending write state is cleared at the first
reset sampling edge.

After reset, read ``A1`` is accepted in tick 5 and completes in tick 6.
Write ``A2`` follows in tick 7 and completes in tick 8. No old address or
write data is replayed after reset, and no completion is fabricated for
the cancelled ``A0`` write.

.. wavedrom::
    :name: cpuif-axil-reset-timing
    :caption: Reset cancels pending write data before new accesses begin
    :alt: Reset cancels pending write data before new accesses begin.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p........."},
            {"name": "rst", "wave": "0..1.0...."},
            [
                "s_cpuif",
                [
                    "Master",
                    {"name": "req", "wave": "010..1010."},
                    {"name": "req_is_wr", "wave": "x1x..0x1x."},
                    {"name": "addr", "wave": "x=x..=x=x.", "data": ["A0", "A1", "A2"]},
                    {"name": "wr_data", "wave": "x=x....=x.", "data": ["D0", "D2"]}
                ],
                [
                    "Slave",
                    {"name": "wr_ack", "wave": "0.......10"},
                    {"name": "wr_err", "wave": "x.......0x"},
                    {"name": "rd_ack", "wave": "0.....10.."},
                    {"name": "rd_err", "wave": "x.....0x.."},
                    {"name": "rd_data", "wave": "x.....=x..", "data": ["D1"]}
                ]
            ],
            {},
            [
                "m_axil_wr",
                [
                    "Master",
                    {"name": "awvalid", "wave": "010....10."},
                    {"name": "awaddr", "wave": "x=x....=x.", "data": ["A0", "A2"]},
                    {"name": "wvalid", "wave": "01.0...10."},
                    {"name": "wdata", "wave": "x=.x...=x.", "data": ["D0", "D2"]},
                    {"name": "bready", "wave": "0.10....10"}
                ],
                [
                    "Slave",
                    {"name": "awready", "wave": "1........."},
                    {"name": "wready", "wave": "10.1......"},
                    {"name": "bvalid", "wave": "0.......10"},
                    {"name": "bresp", "wave": "x.......=x", "data": ["OKAY"]}
                ]
            ],
            {},
            [
                "m_axil_rd",
                [
                    "Master",
                    {"name": "arvalid", "wave": "0....10..."},
                    {"name": "araddr", "wave": "x....=x...", "data": ["A1"]},
                    {"name": "rready", "wave": "0.....10.."}
                ],
                [
                    "Slave",
                    {"name": "arready", "wave": "1........."},
                    {"name": "rvalid", "wave": "0.....10.."},
                    {"name": "rdata", "wave": "x.....=x..", "data": ["D1"]},
                    {"name": "rresp", "wave": "x.....=x..", "data": ["OKAY"]}
                ]
            ],
            {}
        ],
        "head": {"tick": 0},
        "config": {"hscale": 2}
    }

.. _verification-openenoc-cpuif-axil-adapter:

Verification
------------

The test suite is in ``dv/core/openenoc_cpuif_axil_adapter/``.

Testbench
~~~~~~~~~

This cocotb suite verifies ``openenoc_cpuif_axil_adapter`` in isolation with native CPUIF and
AXI4-Lite bus fixtures. The default fixture uses 32-bit addresses and data.

Coverage
~~~~~~~~

The suite covers:

- independent AXI write-address and write-data handshakes;

- write-data acceptance before write-address acceptance;

- stable AXI addresses and write payloads while stalled;

- CPUIF bit-enable to AXI byte-strobe conversion;

- AXI read-data delivery to CPUIF;

- propagation of AXI read and write response errors;

- one-cycle CPUIF acknowledgement strobes;

- simultaneous completion of one request and launch of the next request;

- bubble-free read-to-write handoff;

- suppression of AXI transfers and CPUIF acknowledgements during reset; and

- clearing a stalled transaction on reset.
