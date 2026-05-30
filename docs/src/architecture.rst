.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

System Architecture
===================

The **openENOC** architecture is based on an Ethernet-inspired Network-on-Chip (NoC) that uses Layer-2 packet switching to interconnect CPUs, accelerators, peripherals, and memories within scalable MPSoC systems through a uniform communication model. This approach allows both on-chip and off-chip communication to be handled in a consistent way, making the architecture modular, extensible, and well suited for heterogeneous computing platforms targeting cryptography, AI, and edge workloads.

.. image:: ../images/openENOC-Architecture.svg
   :alt: Overall openENOC system architecture
   :align: center
   :width: 100%

.. raw:: html

   <br>

The architecture illustrated above is built around three main building blocks: the **openENOC Switch**, the **openENOC Control Interface**, and the **openENOC Endpoint Interface**. Together, these components define how data is transported, how switching behavior is configured, and how computation, memory, and peripherals are attached to the network.

.. index:: Switch

openENOC Switch
---------------

The **openENOC Switch** is the central on-chip Ethernet switch that connects processors, accelerators, peripherals, and memories through the **openENOC Endpoint Interface**. It supports an arbitrary number of ports, and the bandwidth of each port can be configured independently by selecting the desired bus width and clock frequency. The switching core itself may also operate at its own independently chosen performance point. This flexibility allows the switch to be adapted to a wide range of application-specific communication requirements.

The switch can operate in two modes:

* **Unmanaged mode**: the switch operates autonomously and passively learns MAC address-to-port relationships from the traffic passing through it. This functionality is implemented by an integrated RTL controller.
* **Managed mode**: the switch is configured by an external processor connected through the **openENOC Control Interface**. In this mode, MAC learning and forwarding behavior can be controlled using static, dynamic, or hybrid policies.

In addition to on-chip connectivity, switch ports may also be connected to **Ethernet MAC & PHY controllers** to extend communication beyond the chip boundary. This allows openENOC-based systems to scale from a single MPSoC instance to multi-FPGA deployments and distributed clusters.

.. index:: Control Interface

openENOC Control Interface
--------------------------

The **openENOC Control Interface** is a memory-mapped interface used to configure and monitor the **openENOC Switch**. It exposes configuration and status registers (CSRs), the memory model of the MAC table, and interrupt registers required for dynamic switch management.

When the switch operates in managed mode, a processor accesses this interface to define forwarding behavior, populate or update MAC address mappings, inspect switch state, and react to network events through interrupts. In this way, the control interface provides software-defined control over the switching fabric while preserving the Ethernet-based data plane.

.. index:: Endpoint Interface

openENOC Endpoint Interface
---------------------------

The **openENOC Endpoint Interface** is the termination point for Ethernet communication arriving from the **openENOC Switch**. It provides a dual integration model through both **memory-mapped** and **streaming** interfaces, allowing processors, accelerators, peripherals, and memories to be attached in different ways depending on application needs.

The endpoint can operate in two modes:

* **Standalone mode**: the integrated controller autonomously handles DMA transfer coordination, memory range mapping, and data replication and synchronization.
* **Non-standalone mode**: the endpoint is connected to a processor through its own CSR interface. In this case, the processor controls DMA-related functions such as interrupts, descriptors, and transfer coordination. This mode also provides registers that allow bypassing the memory-mapped path in favor of a direct streaming-oriented data path for streaming applications.

This makes the endpoint suitable both for memory-centric communication and for low-latency dataflow-oriented processing.

Architectural Relationships
---------------------------

At the system level, the **openENOC Switch** forms the communication backbone, while each functional block is attached through an **openENOC Endpoint Interface**. The **openENOC Control Interface** is only required when switch management is performed by software. As a result, data transport and control-plane management are cleanly separated:

* the **switch** forwards Ethernet frames between ports,
* the **endpoint** adapts Ethernet communication to local computation, memory, or peripheral logic,
* the **control interface** provides optional software control over switch behavior.

This separation enables the architecture to scale in several directions: multiple endpoints can share a common switch, specialized switches can be introduced for subsystems with different bandwidth or latency requirements, and Ethernet links can connect multiple FPGA systems without changing the endpoint programming model.

Use Cases
---------

EP A1: Managed switch operation with processor-coordinated DMA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**EP A1** illustrates a configuration in which **openENOC Switch A** operates in **managed mode**. A processor is connected to the switch configuration port through the **openENOC Control Interface**, allowing software to control MAC learning and forwarding policies. In the same endpoint, the **openENOC Endpoint Interface** uses DMA to transfer data to and from memory, while the processor coordinates these DMA operations.

This use case is suitable for systems that require explicit software control over network behavior, for example when traffic policies must be tuned at runtime or when integration with higher-level resource management software is needed.

Because the switch provides only a single configuration port, this managed setup typically applies to one controlling endpoint in that switch domain. Other endpoints connected to the same switch, such as **EP A2**, are then integrated without their own control path to the switch.

EP A2: Data endpoint without switch control access
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**EP A2** shows a standard endpoint connected to **openENOC Switch A** without direct access to the switch control interface. It still uses the **openENOC Endpoint Interface** for communication with its local processor/accelerator and memory subsystem, but switch configuration is handled elsewhere, typically by the processor associated with **EP A1**.

This arrangement is useful when one software-visible control point manages a larger communication domain, while other endpoints remain focused on data exchange only.

EP A3: Direct processor/accelerator connection for streaming applications
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**EP A3** illustrates direct attachment of the **openENOC Endpoint Interface** to a processor or accelerator **without using DMA**. In this setup, incoming data is consumed directly by the computation element before any optional storage in memory.

This model is particularly suitable for **streaming-oriented applications**, where low-latency processing is more important than bulk memory transfers. Typical examples include packet inspection, signal processing, real-time inference pipelines, and other workloads where data should be processed as it arrives rather than first copied into memory.

Switch B: Dedicated high-bandwidth subnet for accelerators and shared memory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When multiple accelerators share a common memory and communicate intensively with it, connecting all traffic through a single general-purpose switch may become a scalability bottleneck. The architecture therefore allows such accelerators and the shared memory to be grouped behind a **dedicated switch**, illustrated as **openENOC Switch B**.

In the diagram, **EP B1** and **EP B2** represent accelerators, while **EP B3** represents shared memory. By isolating this traffic on a dedicated switch operating at speeds tuned to the acceleration workload, the system can scale more efficiently. This creates a local high-performance communication island while still allowing integration into the broader system through an uplink to the main switch.

This pattern is especially useful for accelerator clusters with heavy memory traffic, where communication characteristics differ significantly from those of the rest of the SoC.

Switch C: Dedicated low-speed or hierarchical peripheral subnet
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Some peripherals operate at substantially lower speeds than CPUs, accelerators, or memory subsystems. In such cases, attaching them directly to a high-performance switch may be inefficient. The architecture therefore supports connecting these peripherals through a **dedicated switch**, illustrated as **openENOC Switch C**.

In the diagram, **EP C1** and **EP C2** are peripheral endpoints connected to this lower-speed subsystem. This organization is also useful in **hierarchical communication topologies**, where different parts of the system are separated by performance class or priority level. In that sense, the arrangement is analogous to a **northbridge/southbridge** style decomposition in traditional computer architectures.

Using dedicated peripheral switches improves modularity and allows each subsystem to operate at a communication rate appropriate to its role.

Off-chip scaling across FPGA systems
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The architecture also supports scaling beyond a single FPGA-based MPSoC. By connecting **Ethernet MAC & PHY controllers** to switch ports, communication can be extended from **on-chip** to **off-chip**. In the diagram, this is illustrated by the connection between **FPGA 1** and **FPGA 2**, where **openENOC Switch A** communicates with **openENOC Switch D** through Ethernet controllers and an external network.

This enables multiple FPGA systems to be combined into a cluster while preserving the same endpoint abstraction. From the perspective of the endpoints, the communication model remains consistent, which simplifies system expansion and reduces software complexity.

When FPGA systems are geographically distributed or connected through the Internet, the external network must provide Ethernet connectivity at Layer 2, which may require appropriate **L2 VPN** infrastructure. Communication security in such deployments is outside the scope of openENOC itself and must be provided by the external network environment.

FPGA 2 domain: remote extension of the same communication model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On **FPGA 2**, **openENOC Switch D** mirrors the same architectural principles used on **FPGA 1**. **EP D1** shows a processor/accelerator plus memory subsystem with managed-switch capability through the **openENOC Control Interface**, while **EP D2** illustrates another endpoint connected for data communication. This demonstrates that the architecture can be replicated across multiple FPGA nodes without changing the fundamental design pattern.

In other words, openENOC is not limited to a single-chip NoC; it can be extended into a distributed Ethernet-based interconnect fabric spanning multiple FPGA platforms.

Summary
-------

Overall, the openENOC system architecture combines Ethernet-style packet switching with configurable endpoint integration to provide a scalable communication substrate for heterogeneous MPSoC systems. The **openENOC Switch** supplies flexible Layer-2 connectivity, the **openENOC Control Interface** enables optional software-defined management, and the **openENOC Endpoint Interface** adapts the network to processors, accelerators, peripherals, and memories through memory-mapped and streaming integration
styles.

The diagram demonstrates how this architecture supports several important deployment patterns: software-managed switching, DMA-based memory transfers, direct streaming data paths, dedicated subnetworks for accelerator clusters, dedicated low-speed peripheral domains, and transparent off-chip scaling across multiple FPGA systems. Together, these capabilities make openENOC suitable for building modular and scalable platforms across a wide range of embedded and high-performance applications.

