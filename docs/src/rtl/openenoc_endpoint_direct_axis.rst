.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-endpoint-direct-axis:

Direct AXIS over CSR -- openenoc_endpoint_direct_axis
=====================================================

.. index::
   single: openenoc_endpoint_direct_axis

Connects software-controlled direct frame streams to endpoint transport and
interrupt reporting.

**Source:**
:download:`RTL source <../../../hw/rtl/core/openenoc_endpoint_direct_axis.sv>`.

Parameters
----------

.. list-table:: Parameters
   :class: rtl-reference-table
   :header-rows: 1
   :widths: 20 18 32 30

   * - Name
     - Default value
     - Allowed values
     - Description
   * - ``ROUTE_DIRECT``
     - Required
     - ``initiator_if.ROUTE_DIRECT``
     - Direct-stream route encoding supplied from the DMA transfer interface.

Signals
-------

Interface ports contain channels in both directions. The table identifies
the selected modport or stream role; member directions follow that interface.

.. list-table:: Public signals and interfaces
   :class: rtl-reference-table
   :header-rows: 1
   :widths: 20 36 17 27

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
     - Active-high reset of transaction and control state.
   * - ``tx_frame_done``
     - ``logic``
     - input
     - Final direct-frame beat accepted at the oETP input after FIFO/mux transport.
   * - ``endpoint_if``
     - ``openenoc_endpoint_if.core``
     - bidirectional (core)
     - Direct TX data/control, RX data/status, and hardware command clears.
   * - ``m_axis_csr_tx``
     - ``taxi_axis_if.src``
     - source
     - Software-controlled transmit frame stream.
   * - ``s_axis_csr_rx``
     - ``taxi_axis_if.snk``
     - sink
     - Receive frame stream consumed through CSR reads.
   * - ``tx_event_if``
     - ``openenoc_irq_event_if.producer``
     - bidirectional (producer)
     - Direct transmit completion-event producer.
   * - ``rx_event_if``
     - ``openenoc_irq_event_if.producer``
     - bidirectional (producer)
     - Direct receive-availability event producer.

Architecture and operation
--------------------------

This block bridges the direct CSR stream registers in ``endpoint_if`` to
``m_axis_csr_tx`` and ``s_axis_csr_rx``. The CSR path carries 32-bit data
and four-bit KEEP masks. :ref:`rtl-endpoint-interface` connects both streams
at that width and provides FIFO/mux transport toward the Ethernet link.
The block preserves payload bytes, KEEP, and LAST; software supplies the
Ethernet header as part of the frame. ``ROUTE_DIRECT`` identifies the
internal direct-stream route.

Separate TX and RX clocked processes own stream state and CSR
acknowledgements. Each AXIS boundary uses a two-entry AXI-Stream register
slice (skid buffer), including a registered READY path. CSR data/status
and hardware-clear outputs are registered.
An empty slice can accept words while its output is stalled; backpressure
reaches the preceding stage when its two storage slots are occupied.

For TX, software writes ``axis_if.source.data.tdata``, sets KEEP/LAST in
``source.control``, and finally sets ``source.control.tvalid``. It retains
the word until hardware clears that command. ``source.status.tready`` is
registered readiness status; the command-clear handshake confirms that
the word was accepted into the local TX slice. Software may submit the
next word after ``control.tvalid`` reads zero. In particular, the stream
HAL's return after submitting the final word does not imply TX completion.

Without a direct TX event, ``source.status.tready`` is a registered copy
of READY at the TX slice input. It follows downstream backpressure through
the slice's registered READY path. An empty slice can remain ready while
its output is stalled, until both storage slots are occupied. CSR command
acknowledgements and frame boundaries do not themselves lower this status.

With a direct TX event enabled, readiness additionally requires frame
admission. Software presents the first word and sets ``control.tvalid``
to request admission. Its handshake opens the frame and enables readiness
when the slice has capacity. Acceptance of ``tlast`` closes the frame and
deasserts readiness on that same edge. Readiness then stays low until the
next frame receives its own admission. The IRQ controller checks and reserves
event space during admission; TX readiness does not inspect queue occupancy.
Completing or removing a queued IRQ event does not itself reopen the frame.
The active frame retains the controller's reserved/unreserved decision even
if software changes the event-enable bit.

The readiness status and CSR command acknowledgement have separate roles.
Software retains data, KEEP, and LAST until ``control.tvalid`` clears,
including when the readiness status remains high during that acknowledgement.

For RX, software waits for ``axis_if.sink.control.tready = 0`` and
``sink.status.tvalid = 1``, reads data/KEEP/LAST, and then sets
``sink.control.tready``. Hardware consumes the pending word and clears
that command. The word stays stable while visible and unacknowledged.
Pending-beat flags suppress duplicate acceptance while a CSR VALID or
READY remains set during its registered acknowledgement.

Each frame requests admission on its own :ref:`rtl-irq-event-if` producer.
TX uses source 3 (``NON_OETP_DIRECT_TX_COMPLETE``); RX uses source 4
(``NON_OETP_DIRECT_RX_AVAILABLE``). Both drive ``admit_enable = 1``
and commit with peer index zero. An enabled source needs a reservation
before the frame can proceed. A disabled source can be admitted with
``admit_reserved = 0`` and produces no later commit. Masking the physical
IRQ alone does not disable event collection or remove this credit limit.

One direct TX frame is active at a time. A reserved event retains its
credit through the FIFO/mux transport until ``tx_frame_done`` reports
acceptance of the final direct beat at the oETP input. Its subsequent commit
must finish before another TX frame is admitted. Without a reservation,
``tx_frame_done`` alone releases the active-frame context. This completion
identifies the local frame boundary; reception at a remote endpoint is not
acknowledged.

RX commits its availability event when the first word becomes visible,
so notification can precede the rest of the frame. The remaining words
use that frame's admission, without reserving another event per word.
When admission is blocked, the input slice may still prefetch up to two
words, but the first word is not exposed in the CSR status until admission
can proceed. ``rst`` clears slice contents, pending-beat flags, active-frame
state, and local event context.

Functional scenarios
--------------------

The examples use the firmware's 66-byte raw Ethernet frame on the 32-bit
direct path. Frame length excludes preamble, SFD, and FCS. A frame has
16 full words with ``tkeep = 0xF`` and a final word with ``tkeep = 0x3``
and ``tlast = 1``. ``DA0`` through ``DA16`` denote transmitted words;
``DB0`` through ``DB16`` denote received words.

CSR field paths are relative to ``endpoint_if``. Generated
``.value``/``.next`` wrappers are omitted, and ``.hwclr`` denotes a
registered hardware acknowledgement. ``clk`` is the common module clock.
Numbered intervals end at the rising edge that samples their values.
Gaps marked ``|`` omit software execution, intermediate word handshakes,
and FIFO/mux waiting time; they do not specify fixed firmware or transport
latency. Shaded ``x`` values are irrelevant outside their valid interval.

Transmit a 66-byte frame without an IRQ event
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Software disables the direct TX event source by clearing
``irq.event_enable.non_oetp_direct_tx_complete`` before starting the
frame. This selects operation without a TX notification; the physical
IRQ mask is independent of event generation. The producer still requests
admission for source 3 with ``admit_enable = 1``, but the controller
accepts it with ``admit_reserved = 0``. This admission consumes no IRQ
credit and can proceed even when the IRQ queue is full.

Software can wait for the initially asserted ``source.status.tready``.
It writes data, KEEP, and LAST before setting
``source.control.tvalid``. It polls that command until hardware clears
it, then submits the next word. The example transmits ``DA0`` through
``DA16``: 16 full words followed by a two-byte final word. The first
gap omits the CSR and AXIS handshakes for ``DA1`` through ``DA15``.
No interrupt handler or claim completion is needed to advance the stream.

After ``DA16`` is acknowledged, software can queue ``DA17``, the first
word of the next frame. That CSR command remains pending while the
previous frame drains through the downstream transport. Its data, full
KEEP, and LAST clear remain unchanged during the wait.

``tx_frame_done`` releases the previous frame's context directly,
because no event was reserved. The next frame then receives its own
unreserved admission, and hardware accepts and acknowledges ``DA17``.
``commit_valid`` remains low throughout. The rest of that next frame
continues beyond the shown interval.

The CSR acknowledgement confirms word acceptance into the local slice.
Polling the final command's clear therefore confirms submission, while
the later ``tx_frame_done`` establishes the local downstream frame
boundary. Hardware sequences queued frames across that boundary without
requiring a software TX-completion interrupt.

.. wavedrom::
    :name: endpoint-direct-axis-tx-no-irq-timing
    :caption: Polling transmission of a 66-byte frame without an IRQ event
    :alt: Unreserved TX admissions let a queued next frame proceed after tx_frame_done.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p........|......|..|..........."},
            ["endpoint_if",
                ["CSR",
                    {
                        "name": "axis_if.source.control.tvalid",
                        "wave": "01....0..|...1.0|1.|.......0..."
                    },
                    {
                        "name": "axis_if.source.data.tdata",
                        "wave": "x=....x..|...=.x|=.|.......x...",
                        "data": ["DA0", "DA16", "DA17"]
                    },
                    {
                        "name": "axis_if.source.control.tkeep",
                        "wave": "x=....x..|...=.x|=.|.......x...",
                        "data": ["0xF", "0x3", "0xF"]
                    },
                    {
                        "name": "axis_if.source.control.tlast",
                        "wave": "x0....x..|...1.x|0.|.......x..."
                    }
                ],
                ["Core",
                    {
                        "name": "axis_if.source.control.tvalid.hwclr",
                        "wave": "0....10..|....10|..|......10..."
                    },
                    {
                        "name": "axis_if.source.status.tready",
                        "wave": "1........|......|..|..........."
                    }
                ]
            ],
            ["m_axis_csr_tx",
                ["Source",
                    {"name": "tvalid", "wave": "0....10..|....10|..|......10..."},
                    {
                        "name": "tdata",
                        "wave": "x....=x..|....=x|..|......=x...",
                        "data": ["DA0", "DA16", "DA17"]
                    },
                    {
                        "name": "tkeep",
                        "wave": "x....=x..|....=x|..|......=x...",
                        "data": ["0xF", "0x3", "0xF"]
                    },
                    {"name": "tlast", "wave": "x....0x..|....1x|..|......0x..."}
                ],
                ["Sink", {"name": "tready", "wave": "1........|......|..|..........."}]
            ],
            {"name": "tx_frame_done", "wave": "0........|......|..|.10........"},
            ["tx_event_if",
                ["Producer",
                    {"name": "admit_valid", "wave": "0.1.0....|......|..|...1.0....."},
                    {"name": "admit_enable", "wave": "1........|......|..|..........."},
                    {"name": "commit_valid", "wave": "0........|......|..|..........."}
                ],
                ["Controller",
                    {"name": "admit_ready", "wave": "0..10....|......|..|....10....."},
                    {"name": "admit_reserved", "wave": "0........|......|..|..........."},
                    {"name": "commit_ready", "wave": "0........|......|..|..........."}
                ]
            ]
        ],
        "config": {"hscale": 1}
    }

Single-frame transmit and completion after the downstream frame boundary
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Software presents ``DA0`` with full KEEP and LAST clear, starting admission
for source 3. The controller grants a reservation before the word enters
the TX slice. ``source.status.tready`` then reflects the admitted frame's
downstream capacity. ``source.control.tvalid.hwclr`` acknowledges the
accepted word one clock later.
The registered AXIS output then presents that same word to the transport.
The acknowledgement can precede acceptance at ``m_axis_csr_tx`` if the
slice's output is stalled, as shown in the held-command scenario.

After the omitted handshakes for ``DA1`` through ``DA15``, software submits
``DA16`` with ``tkeep = 0x3`` and LAST set. Hardware acknowledges that
word and stops accepting another frame while the current one drains.
Acceptance of ``DA16`` at ``m_axis_csr_tx`` transfers it to the next
transport stage; the reserved event is still pending.

Only the later ``tx_frame_done`` pulse permits the TX event to commit.
The producer holds ``commit_valid`` while ``commit_ready`` is low,
retaining its reservation. The successful commit releases the frame
context. Both admission and commit identify source 3; the commit uses
peer index zero.

.. wavedrom::
    :name: endpoint-direct-axis-tx-timing
    :caption: CSR transmit acknowledgements precede the final downstream TX event
    :alt: The final word enters transport before tx_frame_done allows the reserved event commit.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p........|......|......|...."},
            ["endpoint_if",
                ["CSR",
                    {
                        "name": "axis_if.source.control.tvalid",
                        "wave": "01....0..|...1.0|......|...."
                    },
                    {
                        "name": "axis_if.source.data.tdata",
                        "wave": "x=....x..|...=.x|......|....",
                        "data": ["DA0", "DA16"]
                    },
                    {
                        "name": "axis_if.source.control.tkeep",
                        "wave": "x=....x..|...=.x|......|....",
                        "data": ["0xF", "0x3"]
                    },
                    {"name": "axis_if.source.control.tlast", "wave": "x0....x..|...1.x|......|...."}
                ],
                ["Core",
                    {
                        "name": "axis_if.source.control.tvalid.hwclr",
                        "wave": "0....10..|....10|......|...."
                    },
                    {"name": "axis_if.source.status.tready", "wave": "0...1....|....0.|......|...."}
                ]
            ],
            ["m_axis_csr_tx",
                ["Source",
                    {"name": "tvalid", "wave": "0....10..|....10|......|...."},
                    {
                        "name": "tdata",
                        "wave": "x....=x..|....=x|......|....",
                        "data": ["DA0", "DA16"]
                    },
                    {
                        "name": "tkeep",
                        "wave": "x....=x..|....=x|......|....",
                        "data": ["0xF", "0x3"]
                    },
                    {"name": "tlast", "wave": "x....0x..|....1x|......|...."}
                ],
                ["Sink", {"name": "tready", "wave": "1........|......|......|...."}]
            ],
            {"name": "tx_frame_done", "wave": "0........|......|...10.|...."},
            ["tx_event_if",
                ["Producer",
                    {"name": "admit_valid", "wave": "0.1.0....|......|......|...."},
                    {"name": "commit_valid", "wave": "0........|......|....1.|..0."}
                ],
                ["Controller",
                    {"name": "admit_ready", "wave": "0..10....|......|......|...."},
                    {"name": "admit_reserved", "wave": "0..10....|......|......|...."},
                    {"name": "commit_ready", "wave": "0........|......|......|.10."}
                ]
            ]
        ],
        "config": {"hscale": 1}
    }

Receive a buffered 66-byte frame through CSR
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The FIFO connected to ``s_axis_csr_rx`` already contains the complete
66-byte Ethernet frame before the example starts. It asserts ``tvalid``
and presents each word until ``tready`` accepts it. Availability of later
words never stalls the source; all pauses result from the receiving block
and software's CSR acknowledgements.

The empty two-entry input slice first accepts ``DB0`` and ``DB1`` in
successive transfers. It then deasserts input ``tready`` while the FIFO
holds ``DB2``, full KEEP, and LAST clear. RX admission succeeds for source
4 with a reservation. ``DB0`` becomes visible through ``sink.data/status``,
and its availability event commits before software acknowledges the word.
Only one availability event is generated for the frame.

Software reads data, KEEP, and LAST before setting ``sink.control.tready``.
Hardware consumes one word and acknowledges it with the registered
``control.tready.hwclr``. The pending-beat protection prevents a held CSR
ready command from consuming another word. Freeing a slice entry permits
the FIFO to transfer its next word, so input READY rises in response to
CSR consumption rather than remaining high throughout the frame.

The middle gap omits FIFO transfers for ``DB3`` through ``DB15`` and
CSR acknowledgements for ``DB1`` through ``DB13``. After the gap, software
is reading ``DB14`` while the FIFO holds the final word ``DB16``.
Acknowledging ``DB14`` allows ``DB16`` into the input slice. The FIFO
then deasserts ``s_axis_csr_rx.tvalid`` because all 17 words have been
transferred, while ``DB15`` and ``DB16`` still await CSR consumption.

The first 16 words have ``tkeep = 0xF`` and LAST clear. The final word
has ``tkeep = 0x3`` and LAST set. Software acknowledges that last word
after reading its two valid bytes, completing a total of 66 bytes.

.. wavedrom::
    :name: endpoint-direct-axis-rx-timing
    :caption: CSR reception of a 66-byte frame already buffered in the input FIFO
    :alt: The FIFO holds each word until READY; CSR consumption frees input-slice capacity.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p........|..|.................."},
            ["s_axis_csr_rx",
                ["Source",
                    {"name": "tvalid", "wave": "01.......|..|....0............."},
                    {
                        "name": "tdata",
                        "wave": "x===.....|..|=...x.............",
                        "data": ["DB0", "DB1", "DB2", "DB16"]
                    },
                    {
                        "name": "tkeep",
                        "wave": "x=.......|..|=...x.............",
                        "data": ["0xF", "0x3"]
                    },
                    {"name": "tlast", "wave": "x0.......|..|1...x............."}
                ],
                ["Sink", {"name": "tready", "wave": "1..0.....|.1|0..10....1........"}]
            ],
            ["endpoint_if",
                ["CSR",
                    {
                        "name": "axis_if.sink.control.tready",
                        "wave": "0........|1.|0.1.0...1.0...1.0."
                    }
                ],
                ["Core",
                    {
                        "name": "axis_if.sink.status.tvalid",
                        "wave": "0....1...|.0|1..0..1..0..1..0.."
                    },
                    {
                        "name": "axis_if.sink.data.tdata",
                        "wave": "x....=...|.x|=..x..=..x..=..x..",
                        "data": ["DB0", "DB14", "DB15", "DB16"]
                    },
                    {
                        "name": "axis_if.sink.status.tkeep",
                        "wave": "x....=...|.x|=..x..=..x..=..x..",
                        "data": ["0xF", "0xF", "0xF", "0x3"]
                    },
                    {"name": "axis_if.sink.status.tlast", "wave": "x....0...|.x|0..x..0..x..1..x.."},
                    {
                        "name": "axis_if.sink.control.tready.hwclr",
                        "wave": "0........|.1|0..10....10....10."
                    }
                ]
            ],
            ["rx_event_if",
                ["Producer",
                    {"name": "admit_valid", "wave": "0..1.0...|..|.................."},
                    {"name": "commit_valid", "wave": "0....1.0.|..|.................."}
                ],
                ["Controller",
                    {"name": "admit_ready", "wave": "0...10...|..|.................."},
                    {"name": "admit_reserved", "wave": "0...10...|..|.................."},
                    {"name": "commit_ready", "wave": "0.....10.|..|.................."}
                ]
            ]
        ],
        "config": {"hscale": 1}
    }

Held CSR commands, stream stalls, and IRQ admission
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example shows the beginning of another 66-byte TX frame;
``DA1`` through ``DA16`` continue beyond the displayed interval.
The TX register slice is initially empty and the enabled IRQ source
has no available credit. Software holds the first word ``DA0`` and
``control.tvalid`` while admission waits through cycle 4. No word
is accepted before admission transfers in cycle 5 with a reservation.
``source.status.tready`` remains low while that first command waits for
admission.

The empty slice accepts ``DA0`` in cycle 6 even though the external
``m_axis_csr_tx.tready`` remains low. In cycle 7, hardware asserts
``control.tvalid.hwclr`` and the output presents ``DA0``. The CSR command
is still high in that cycle, but the pending-beat flag prevents another
acceptance. The generated CSR clears the command in cycle 8.
``source.status.tready`` is already active in cycle 6: admission has
succeeded and the slice still has room for another word. Software retains
the current CSR command until its clear, independently of this status.

The output holds ``DA0``, full KEEP, and LAST clear until the transfer
in cycle 12. Exactly one copy reaches the downstream sink. Registered
``source.status.tready`` can become active before that transfer because the
slice has room for another word. It does not imply that the pending
output beat or the frame has finished. ``commit_valid`` stays low
because this frame's final downstream boundary has not occurred.

On RX, the corresponding held READY protection is shown in the preceding
scenario. When RX admission is blocked instead, prefetched words remain
in the input slice, ``sink.status.tvalid`` stays low, and upstream
backpressure follows once the slice fills. Freeing IRQ credit permits
the same pending frame to become visible without losing its first word.

.. wavedrom::
    :name: endpoint-direct-axis-admission-stall-timing
    :caption: A held TX command survives IRQ admission delay and downstream backpressure
    :alt: Admission permits one buffered DA0; registered acknowledgement prevents a duplicate.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p.............."},
            ["endpoint_if",
                ["CSR",
                    {"name": "axis_if.source.control.tvalid", "wave": "01......0......"},
                    {
                        "name": "axis_if.source.data.tdata",
                        "wave": "x=......x......",
                        "data": ["DA0"]
                    },
                    {
                        "name": "axis_if.source.control.tkeep",
                        "wave": "x=......x......",
                        "data": ["0xF"]
                    },
                    {"name": "axis_if.source.control.tlast", "wave": "x0......x......"}
                ],
                ["Core",
                    {"name": "axis_if.source.control.tvalid.hwclr", "wave": "0......10......"},
                    {"name": "axis_if.source.status.tready", "wave": "0.....1........"}
                ]
            ],
            ["m_axis_csr_tx",
                ["Source",
                    {"name": "tvalid", "wave": "0......1.....0."},
                    {"name": "tdata", "wave": "x......=.....x.", "data": ["DA0"]},
                    {"name": "tkeep", "wave": "x......=.....x.", "data": ["0xF"]},
                    {"name": "tlast", "wave": "x......0.....x."}
                ],
                ["Sink", {"name": "tready", "wave": "0...........1.."}]
            ],
            ["tx_event_if",
                ["Producer",
                    {"name": "admit_valid", "wave": "0.1...0........"},
                    {"name": "commit_valid", "wave": "0.............."}
                ],
                ["Controller",
                    {"name": "admit_ready", "wave": "0....10........"},
                    {"name": "admit_reserved", "wave": "0....10........"},
                    {"name": "commit_ready", "wave": "0.............."}
                ]
            ]
        ],
        "config": {"hscale": 1},
        "head": {"tick": 0}
    }
