.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

HAL Architecture Specification
==============================

Introduction
------------

The Hardware Abstraction Layer (HAL) provides a software-visible representation of openENOC hardware components and defines a standardized mechanism for accessing their Control and Status Registers (CSRs). The HAL serves as the primary interface between software and hardware, enabling configuration, monitoring, diagnostics, and runtime control of openENOC subsystems.

This document specifies the HAL architecture and CSR organization for the openENOC Switch and the openENOC Endpoint Interface. The described CSR definitions establish a common programming model for software components and serve as the authoritative reference for hardware/software integration.

CSR Specification Methodology
-----------------------------

Within this flow, Control and Status Registers are defined using `Accellera's SystemRDL 2.0 <https://www.accellera.org/downloads/standards/systemrdl>`_ as the authoritative specification format for all openENOC hardware components.

For artefact generation, the openENOC toolchain is based on `PeakRDL <https://github.com/SystemRDL/PeakRDL>`_, which processes the SystemRDL description and produces the corresponding CSR-related outputs used throughout the build and verification flow. Since the current PeakRDL implementation `does not support all features <https://peakrdl-regblock.readthedocs.io/en/latest/limitations.html>`_ of the SystemRDL 2.0 standard, CSR definitions are written with this limitation in mind to ensure that the complete register specification can be translated into all required generated artefacts without manual intervention or post-processing.

openENOC Switch Interface HAL Architecture
------------------------------------------

The openENOC Switch provides frame-forwarding and management functionality within the openENOC system. Software access to switch resources is provided through the openENOC Switch Interface, which exposes a memory-mapped CSR space.

The switch interface HAL defines the software-visible representation of switch functionality and provides a consistent programming model independent of implementation-specific details.

Architecture
~~~~~~~~~~~~

The switch interface HAL is organized around a CSR-based management interface that exposes configuration, status, monitoring, and diagnostic functionality. Software components interact with switch resources through register accesses performed over the openENOC Switch Interface. The HAL architecture establishes a clear separation between software-visible behavior and the underlying frame-forwarding implementation, allowing internal switch architectures to evolve while maintaining software compatibility.

A central configuration aspect of the switch interface HAL is the selection of the switch operating mode. In unmanaged mode, the switch operates autonomously and forwarding state is maintained by internal hardware logic. In this mode, the switch may learn forwarding table entries from observed traffic and update its forwarding state without software intervention. In managed mode, forwarding behavior is controlled through software-visible configuration mechanisms exposed by the openENOC Switch Interface. This allows an external processor to populate, update, inspect, or invalidate forwarding table entries according to system-specific requirements.

The operating mode is controlled through switch configuration registers. These registers define whether the switch operates autonomously or under software control, and they provide the foundation for additional management functions such as forwarding table updates, status inspection, diagnostics, and event handling. Status registers expose the current operational state of the switch and allow software to determine whether the switch is active, idle, paused, or operating under a specific management mode.

The default forwarding behavior for frames that do not match any enabled forwarding table entry is defined through a dedicated register containing a destination interface bitmap. This register specifies the set of output interfaces to which unmatched frames shall be forwarded. In managed mode, this mechanism allows unmatched frames to be redirected toward a switch controller implemented on one of the openENOC endpoints. Such frames are delivered to the controller using the standard openENOC Endpoint Interface, preserving the same data-plane abstraction used by other endpoint-to-network communication.

Since forwarding table updates may affect the active forwarding behavior of the switch, the HAL includes a switch-level flow control mechanism used during managed reconfiguration. This mechanism is exposed through a Flow Control Register and allows software to temporarily stop or pause the flow of frames through the switch before modifying forwarding state. After the pause request is issued, software can observe the corresponding status indication to determine when the switch has reached a safe state for table modification.

Once the switch is paused, software may update forwarding table entries through the CSR space without interfering with active frame forwarding. After the update sequence is complete, software releases the pause condition and normal forwarding operation resumes. This mechanism provides a simple and deterministic way to perform controlled forwarding table reconfiguration while avoiding inconsistent lookup behavior during partial updates.

The flow control mechanism described here is local to switch management and should not be confused with link-level or protocol-level flow control. Its purpose is to coordinate software-driven CSR updates with the internal forwarding pipeline of the switch.

In managed mode, the HAL therefore provides both configuration access and operational control over the switch forwarding behavior. In unmanaged mode, the same hardware may operate without software intervention, and the openENOC Switch Interface may be omitted if no external configuration or monitoring functionality is required.

Forwarding Table
~~~~~~~~~~~~~~~~

A central software-visible structure of the openENOC Switch is the forwarding table, which defines how frames are forwarded based on their destination MAC address. The table is exposed through the CSR space and can be configured by software using the openENOC Switch Interface.

The forwarding table contains entries aligned to a 32-bit data bus. Each forwarding table entry is represented in the CSR space by fields containing a destination MAC address, an N-bit destination interface bitmap, a single enable bit, and padding bits required for alignment to the 32-bit bus width. The destination interface bitmap defines the set of output interfaces to which a matching frame shall be forwarded.

.. figure:: ../images/openENOC-SwitchForwardingTable.svg
   :align: center

   Example forwarding table for an 8-port openENOC Switch

The figure illustrates an example forwarding table for an openENOC Switch with 8 ports. The table contains several representative forwarding rules. Rule (1) defines unicast forwarding of frames with destination address ``0x020E0C000011`` to the first output interface. Rule (2) represents a disabled unicast rule that remains present in the table but is not applied during forwarding lookup. Rule (3) defines multicast forwarding of frames with destination address ``0x030E0C330000`` to the first, third, fifth, and seventh output interfaces. Rule (4) defines frame dropping for destination address ``0x020E0C123456`` by means of an enabled entry with an empty destination interface bitmap. Rule (M) defines the broadcast forwarding rule for frames with destination address ``0xFFFFFFFFFFFF``.

Register Definitions and CSR Memory Map
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The SystemRDL source shown below defines the CSR structure of the openENOC Switch. This source file is the maintained register specification used by the PeakRDL-based generation flow.

.. literalinclude:: ../../hal/interfaces/openenoc_switch_interface.rdl
   :language: systemverilog
   :caption: SystemRDL specification of the openENOC Switch CSR map
   :linenos:

The openENOC Switch CSR memory map and detailed register documentation are derived directly from this SystemRDL specification. The generated CSR documentation provides the corresponding human-readable description of the register hierarchy, address offsets, field layouts, access permissions, reset values, and associated register semantics.

The complete generated CSR documentation is available in :doc:`/generated/openenoc_switch_interface`.

openENOC Endpoint Interface HAL Architecture
--------------------------------------------

The openENOC Endpoint Interface provides the connection between processing elements and the openENOC network. It exposes endpoint control, status monitoring, and communication management functionality through a dedicated CSR space.

The endpoint interface HAL establishes a uniform software interface for accessing endpoint resources and controlling interactions with the network.

Architecture
~~~~~~~~~~~~

The endpoint interface HAL is organized around a CSR-based management interface that exposes endpoint configuration, software-visible stream access, remote peer configuration, DMA control, and a virtual remote-memory region. Software components interact with endpoint resources through register accesses performed over the openENOC Switch Interface. The HAL architecture establishes a clear separation between software-visible endpoint behavior and the underlying oETP frame handling, allowing internal buffering, DMA scheduling, and protocol processing logic to evolve while maintaining software compatibility.

A central configuration aspect of the endpoint interface HAL is the description of the local endpoint instance and the set of remote peers that it can access. The read-only information register exposes implementation parameters such as the total depth of the virtual remote-memory region and the number of supported remote peers. These values allow software to discover the size and structure of the endpoint address space without relying on hard-coded assumptions.

The endpoint configuration registers define the local unicast MAC address and a separate multicast destination address. The oETP receive filter compares an individual destination against ``config.mac_address`` and a group destination against ``config.multicast_address``. All endpoints in a replication group configure the same multicast address while retaining individual unicast identities; outgoing oETP frames use the unicast address as their source. A zero multicast address disables oETP group reception. The multicast register follows the unicast MAC register, with both response-timeout registers following the non-oETP receive policy. This destination filtering will be implemented in the oETP engine.

Remote communication targets are described through a peer table, where each entry contains the MAC address of a remote peer, the offset of the corresponding virtual remote-memory region, the local memory base address, the remote memory base address, and the size of the region. This structure allows software to describe how local memory resources are related to remote memory regions visible through the endpoint.

The HAL supports two complementary access models. The first model is a software-visible AXI4-Stream access path exposed through source and sink register files. The source register file allows software to provide stream data words, assert the corresponding valid indication, and mark the last word of a frame. Software observes the ready status to determine when the endpoint can accept the next transfer. Conversely, the sink register file allows hardware to present received stream data to software, together with valid and last indications, while software acknowledges reception through the ready control field.

This CSR-mapped AXI4-Stream interface mirrors the basic AXI4-Stream handshake semantics in software-visible form. It is useful for low-bandwidth communication, diagnostics, initialization sequences, and simple software-driven frame exchange. The mechanism does not prescribe the internal implementation of the endpoint datapath; it only defines how stream-oriented transfers are exposed through the HAL.

The second access model is memory-oriented communication through the virtual remote-memory region. This region provides a software-visible address space representing memory associated with one or more remote peers. The mapping between a remote peer and its corresponding portion of the virtual memory space is defined by the peer configuration registers. Accesses to this region may be handled directly or used as the basis for DMA-driven transfers, depending on the configured DMA mode for the selected peer.

The response-timeout configuration uses two 32-bit cycle counts: ``config.rmem_timeout.cycles`` for transparent RMEM and ``config.dma_timeout.cycles`` for individual unicast peer DMA fragments. The DMA setting is shared by all peers; there is no separate whole-transfer timeout. Both reset to zero, which permits an indefinite response wait. A DMA fragment timeout aborts the remaining fragments and reports peer DMA error code 8 (TIMEOUT). Software controls recovery and any restart; hardware does not retransmit automatically. Multicast writes complete locally without waiting for responses. These CSRs define the oETP timeout policy; runtime enforcement is part of the forthcoming oETP engine implementation.

An RMEM read timeout returns ``0xFFFFFFFF`` with ``cpuif_rd_ack``; an RMEM write timeout asserts ``cpuif_wr_ack``. The existing generated external-RMEM boundary carries ACK and read data and remains unchanged without ERR signals. Transparent RMEM (peer mode 1) and bulk DMA share ``peers.entry[].dma.error`` and the four-bit ``error_code``. Local timeout records code 8; a received ERROR_RSP requires an explicit wire-to-CSR code mapping. Starting or successfully completing another operation preserves the error. Writing one to the peer's ``dma.clear_error`` clears the flag and code; hardware acknowledges by clearing the command field. New failures take precedence over a simultaneous clear. The command does not abort active work, clear done, or complete an IRQ claim.

Failure reporting also covers received requests. The responder identifies the
peer by source MAC and records the servicing failure before exposing its failed
completion to the oETP engine. The initiator maps the valid ERROR_RSP cause to
remote code 9..15. An AXI write SLVERR therefore records local code 6 at the
responder and remote code 14 at the initiator. Received failures preserve the
responder's locally initiated ``dma.request``, ``idle``, and ``done`` state;
successful incoming requests preserve sticky errors and generate no IRQ.
An incomplete received DMA_WRITE_REQ or DMA_READ_RSP, including missing or
incorrect EndOfData, records remote code 10 directly. A truncated received
write returns ERROR_RSP wire cause 2, while its receiver retains CSR code 10.
Both endpoints can independently notify software that destination memory may
be partially updated. Multicast receivers retain local diagnostics and enabled
events while suppressing responses.

RMEM and bulk DMA retain separate IRQ sources: ``irq.event_enable.rmem_error``
enables source 5 for RMEM failures, while bulk DMA retains PEER_DMA_COMPLETE,
source 0, gated by the per-peer ``dma.irq_enable`` and global
``irq.event_enable.peer_dma_complete``. For a received bulk failure, the
per-peer enable is captured when recording the error and the global enable
is sampled at IRQ admission. Received RMEM failures use the separate global
RMEM gate at admission. Error recording is independent of IRQ enable; neither
releasing an RMEM access nor returning an error completion waits for IRQ FIFO
capacity. The responder retains a pending notification and defers its next
incoming request until the notification is admitted and committed. Clearing
the CSR error and completing an IRQ claim remain independent operations.

The DMA engine owns the shared status and receives tagged RMEM error
completions on the common transfer interface. Both RMEM CPUIF directions and
the RMEM IRQ producer belong to that engine. The locally initiating CPUIF
transaction controller and its event generation remain to be implemented;
the existing scalar CSR stub is retained. The responder already records
incoming failures and emits the appropriate error event, including unsupported
RMEM requests. The oETP engine owns protocol framing and response timeouts;
its parser and ERROR_RSP assembly remain to be implemented.

For non-oETP DMA, AXIS between the engines carries the complete raw Ethernet
frame without FCS. For oETP bulk DMA, it streams exactly the requested memory
bytes without headers, EndOfData, or padding, starting on the first matching
TVALID. The oETP engine appends the 32-bit ``0xE0D0E0D0`` EndOfData only after
successful final read completion; failures finish the frame without that
marker. The common oETP fragment maximum is 8160 bytes at the unchanged
8192-byte raw Ethernet frame limit. Final TX and late RX protocol outcomes
must be added to the internal transfer contract when implementing the parser.
Address and Length are command metadata, and RMEM data travels directly on
command/completion fields. Internal AXIS ``TUSER[0]`` retains the final-fragment
flag; ``TUSER[1]`` distinguishes initiator (0) from responder (1) when both
command paths use the same peer and sequence. This adds no software-visible
mode or wire field. The full contract is described in :ref:`rtl-oetp-engine`.

``MAX_RAW_FRAME_SIZE`` remains a synthesis-time endpoint RDL parameter and
defaults to 8192 bytes without FCS. The read-only
``info.max_dma_frame_size_bytes`` advertises that raw frame ceiling. The global
``config.dma_max_fragment_size.bytes`` register follows ``config.dma_timeout``
and selects the maximum memory bytes per locally initiated peer DMA fragment.
Its reset and upper bound are ``4 * floor((MAX_RAW_FRAME_SIZE - 32) / 4)``,
or 8160 bytes in the default build. Hardware rounds the written value down to
a multiple of four, then requires an effective MFS from four through that bound.
The CSR retains the original value: 31 selects 28, 7 selects four, and 8163
selects 8160. Values zero through three or a rounded value above the bound
reject a new DMA block with local error code 1. The final fragment retains the
exact remaining Length, even if it is shorter than four bytes.
The DMA engine snapshots the effective MFS at whole-transfer acceptance, so writes
during a transfer affect only later blocks. Received requests use the physical
fragment ceiling; raw non-oETP DMA, direct CSR streams, and RMEM are unaffected.

DMA behavior is controlled independently for each peer. When DMA operation is disabled, the peer entry remains configured but no automatic transfer is performed. In transparent mode, accesses to the virtual remote-memory region are translated into corresponding accesses to the remote peer memory region on a word-by-word basis. This mode is suitable when software requires a direct memory-mapped view of remote resources and when simple access semantics are preferred over bulk synchronization.

The endpoint interface HAL also supports mirrored transfer modes. In mirror-to-local mode, the local memory region is used as the software-visible representation of the remote peer memory, and the state of the remote memory region is fetched from the remote peer on demand or periodically. In mirror-to-remote mode, the remote memory region is used as the destination representation, and the state of the local memory region is sent to the remote peer on demand or periodically. These modes allow software to configure endpoint-to-endpoint memory synchronization without directly managing individual transport frames.

DMA transfers are initiated through a peer-specific request field. The corresponding status fields indicate whether the DMA engine is idle, whether the requested transfer has completed successfully, or whether an error has occurred. A typical software sequence therefore consists of configuring the peer address mapping, selecting the DMA mode, issuing a transfer request, and observing the idle, done, and error status indications until the operation reaches a terminal state.

Peer DMA error status distinguishes locally detected causes 1..7, local
TIMEOUT = 8, and remote causes 9..15 reported through ERROR_RSP. Code 10 also
directly identifies an incomplete received DMA data frame or absent/incorrect
EndOfData, without requiring ERROR_RSP first. Wire causes
1..7 map to the remote CSR range by adding 8 after validating the complete
32-bit value. Local AXI read/write SLVERR and DECERR use codes 4..7; their
remote equivalents use 12..15. Invalid wire causes report local invalid-parameter
code 1. The initiator completion interface carries this final encoding, which
the DMA engine preserves for both RMEM and bulk DMA. Raw non-oETP DMA error
status describes local work. RMEM failure handling is described in :ref:`rtl-oetp-engine`.

Non-oETP TX and RX each expose ``command_status.clear_errors`` at bit 9.
Writing one clears that channel's ``error`` and ``error_code``; hardware clears
the command after accepting it. Starting or successfully completing another
transfer preserves a recorded error, and a new failure takes precedence over a
simultaneous clear. Clearing leaves an active or armed transfer, ``done``, byte
counts, and IRQ events intact. TX, RX, and per-peer error records clear independently.

The DMA control mechanism described here is local to endpoint management and should not be confused with Ethernet link-level or protocol-level flow control. Its purpose is to coordinate software-visible memory mappings and transfer requests with the internal endpoint datapath, DMA engine, and oETP processing logic.

The endpoint interface HAL therefore provides both a stream-oriented and a memory-oriented abstraction for communication with the openENOC network. The AXI4-Stream register interface offers a simple CSR-accessible path for direct frame exchange, while the peer table, virtual remote-memory region, and DMA controls provide a scalable mechanism for accessing and synchronizing memory resources across endpoints.

Register Definitions and CSR Memory Map
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The SystemRDL source shown below defines the CSR structure of the openENOC Endpoint Interface. This source file is the maintained register specification used by the PeakRDL-based generation flow.

.. literalinclude:: ../../hal/interfaces/openenoc_endpoint_interface.rdl
   :language: systemverilog
   :caption: SystemRDL specification of the openENOC Endpoint Interface CSR map
   :linenos:

The openENOC Endpoint Interface CSR memory map and detailed register documentation are derived directly from this SystemRDL specification. The generated CSR documentation provides the corresponding human-readable description of the register hierarchy, address offsets, field layouts, access permissions, reset values, and associated register semantics.

The complete generated CSR documentation is available in :doc:`/generated/openenoc_endpoint_interface`.

Summary
-------

This document defines the HAL architecture and CSR organization for the openENOC Switch and the openENOC Endpoint Interface.

The HAL establishes a consistent software-visible programming model based on memory-mapped Control and Status Registers, while the CSR specification provides the authoritative description of hardware/software interactions. Together, these mechanisms form the foundation for software development, system integration, and verification activities within the openENOC project.

.. toctree::
   :hidden:

   generated/openenoc_switch_interface
   generated/openenoc_endpoint_interface
