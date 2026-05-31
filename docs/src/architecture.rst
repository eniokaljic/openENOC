.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

openENOC Architecture
=====================

Introduction
------------

The proposed openENOC system architecture is motivated by the need for a scalable and modular communication substrate for modern MPSoC platforms. As the number of integrated processing elements, accelerators, memories, and peripherals continues to grow, traditional shared buses and point-to-point interconnects become increasingly difficult to scale in terms of bandwidth, latency, and design complexity. For this reason, the Network-on-Chip (NoC) paradigm has become a widely adopted architectural direction for complex SoCs, replacing ad hoc global wiring with structured packet-based communication and better supporting system expansion and integration [1]_.

The openENOC architecture is based on an Ethernet-inspired Network-on-Chip (NoC) that uses Layer-2 packet switching to interconnect CPUs, accelerators, peripherals, and memories within scalable MPSoC systems through a uniform communication model. This approach allows both on-chip and off-chip communication to be handled in a consistent way, making the architecture modular, extensible, and well suited for heterogeneous computing platforms targeting cryptography, AI, and edge workloads.

This architectural choice is further supported by the increasing heterogeneity of contemporary computing systems. Modern workloads combine general-purpose processors with specialized accelerators, producing communication patterns that are more diverse and demanding than those in conventional multicore designs. Recent research shows that NoC architectures for heterogeneous systems must provide flexible and scalable transport mechanisms capable of efficiently supporting different traffic types and bandwidth requirements [2]_. Designing openENOC as a packet-switched communication backbone directly addresses these needs.

The decision to adopt Ethernet-inspired Layer-2 packet switching is also practical from both implementation and system-design perspectives. Packet-based communication improves modularity and composability because system components interact through standardized frames rather than tightly coupled dedicated links. Prior work on scalable interconnection architectures has shown the value of using a unified communication model across both on-chip and off-chip domains, improving system integration and extensibility in complex MPSoC platforms [3]_. This makes Layer-2 switching a suitable foundation for an open and extensible hardware communication fabric.

Recent open-source NoC research also highlights the importance of scalable transport, support for parallel data streams, and efficient handling of both high-throughput and latency-sensitive traffic in accelerator-rich systems [4]_. These observations are aligned with the goals of openENOC, which seeks to provide a unified interconnect for CPUs, accelerators, peripherals, and memories across a broad range of application domains.

Finally, the proposed architecture is consistent with broader trends in open heterogeneous SoC design, where modular integration, standardized interfaces, and FPGA prototyping are key enablers for experimentation and deployment [5]_. In this context, an Ethernet-based NoC provides a forward-looking balance between scalability, implementation simplicity, and system interoperability.

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

References
----------

.. [1] T. Bjerregaard and S. Mahadevan, "A survey of research and practices of network-on-chip," in *ACM Computing Surveys*, vol. 38, no. 1, pp. 1–51, 2006. 
   `(link) <https://dl.acm.org/doi/10.1145/1132952.1132953>`_

.. [2] S. Biglari, F. Hosseini, A. Upadhyay and H. Zhao, "Survey of Network-on-Chip (NoC) for Heterogeneous Multicore Systems," *2024 IEEE 17th International Symposium on Embedded Multicore/Many-core Systems-on-Chip (MCSoC)*, Kuala Lumpur, Malaysia, 2024, pp. 155-162, doi: 10.1109/MCSoC64144.2024.00036.
   `(link) <https://par.nsf.gov/servlets/purl/10552564>`_

.. [3] A. Biagioni, F. Lo Cicero, A. Lonardo, P. S. Paolucci, M. Perra, D. Rossetti, C. Sidore, F. Simula, L. Tosoratto and P. Vicini, "The Distributed Network Processor: a novel off-chip and on-chip interconnection network architecture," arXiv preprint arXiv:1203.1536, 2012.
   `(link) <https://arxiv.org/abs/1203.1536>`_

.. [4] T. Fischer, M. Rogenmoser, T. Benz, F. K. Gürkaynak and L. Benini, "FlooNoC: A 645-Gb/s/link 0.15-pJ/B/hop Open-Source NoC With Wide Physical Links and End-to-End AXI4 Parallel Multistream Support," in *IEEE Transactions on Very Large Scale Integration (VLSI) Systems*, vol. 33, no. 4, pp. 1094-1107, April 2025, doi: 10.1109/TVLSI.2025.3527225.
   `(link) <https://arxiv.org/abs/2409.17606>`_

.. [5] J. Zuckerman, P. Mantovani, D. Giri and L. P. Carloni, "Enabling Heterogeneous, Multicore SoC Research with RISC-V and ESP," arXiv preprint arXiv:2206.01901, 2022.
   `(link) <https://arxiv.org/abs/2206.01901>`_
