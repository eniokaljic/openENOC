.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

openENOC Transport Protocol (oETP)
==================================

Introduction
------------

To support the communication patterns envisioned by the openENOC architecture, including remote memory access, processor-to-processor communication, accelerator integration, and transparent interconnection of FPGA and ASIC components into a unified system, it is necessary to define a transport protocol specifically tailored to Ethernet-based Network-on-Chip (NoC) environments. Among the existing Ethernet-based transport technologies, RDMA over Converged Ethernet (RoCE) represents the closest match to the requirements of openENOC due to its support for RDMA-style communication. However, a detailed analysis revealed that RoCE introduces substantial protocol and implementation complexity that is not justified by the requirements of the openENOC use cases.

RoCEv1 inherits a significant portion of the InfiniBand transport model, including Queue Pair (QP) abstractions, work request management, connection state tracking, completion queues, and memory registration mechanisms [1]_. Furthermore, RoCEv1 assumes a lossless Ethernet fabric and relies on Priority Flow Control (PFC) to prevent packet loss [2]_. While these design choices are acceptable in large-scale datacenter deployments, multiple studies have shown that PFC can introduce head-of-line blocking, congestion propagation, and deadlock scenarios, increasing the complexity of both network infrastructure and endpoint implementations [3]_. Such mechanisms are particularly difficult to justify in NoC environments, where available buffering resources are limited and implementation simplicity is a primary design objective.

For these reasons, the openENOC project defines the openENOC Transport Protocol (oETP), a lightweight transport protocol specifically designed for Ethernet-based NoC systems. Rather than adopting the complete RoCE transport stack, oETP provides a minimal RDMA-over-Ethernet transport layer optimized for communication between hardware components within FPGA-based systems. The protocol employs compact packet headers tailored to the small transactions commonly encountered in NoC environments, thereby reducing communication overhead and minimizing hardware resource consumption.

At the same time, oETP preserves the most valuable aspects of the RDMA programming model by supporting one-sided memory operations, including remote read and remote write transactions, without requiring Queue Pair infrastructure or the associated InfiniBand semantics. Instead of relying on Priority Flow Control, oETP uses credit-based flow control, a well-established technique in Network-on-Chip architectures that provides predictable behavior, efficient buffer utilization, and straightforward hardware implementation [4]_ [5]_. This approach combines the interoperability and ecosystem advantages of Ethernet with the efficiency and scalability traditionally associated with NoC architectures.

Existing RDMA-over-Ethernet solutions are primarily designed for datacenter environments and typically rely on InfiniBand-derived transport abstractions and lossless Ethernet fabrics. oETP explores an alternative design point that combines Ethernet framing, credit-based flow control, and RDMA-style one-sided memory operations for Network-on-Chip deployments. By focusing on the requirements of tightly coupled hardware systems rather than distributed datacenter infrastructure, oETP significantly reduces implementation complexity while preserving the benefits of direct memory access semantics.

The design philosophy of oETP is therefore to retain only those concepts that are essential for efficient memory-centric communication between hardware endpoints while avoiding transport abstractions that primarily address the requirements of large-scale datacenter networks. This results in a lightweight transport protocol optimized for implementation in FPGA and ASIC devices, where logic utilization, memory footprint, latency, and scalability are primary design constraints. The following sections describe the protocol architecture, packet formats, flow control mechanisms, endpoint model, and supported memory access operations in detail.

References
----------

.. [1] NVIDIA, *RDMA Aware Networks Programming User Manual*, NVIDIA Networking Documentation.
   `(link) <https://docs.nvidia.com/networking/display/rdmaawareprogrammingv17>`_

.. [2] NVIDIA, *RDMA over Converged Ethernet (RoCE)*, Cumulus Linux Documentation.
   `(link) <https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/Layer-1-and-Switch-Ports/Quality-of-Service/RDMA-over-Converged-Ethernet-RoCE/>`_

.. [3] R. Mittal, A. Shpiner, A. Panda, E. Zahavi, A. Krishnamurthy, S. Ratnasamy and S. Shenker, "Revisiting Network Support for RDMA," in *Proceedings of the ACM SIGCOMM Conference*, 2018.
   `(link) <https://arxiv.org/abs/1806.08159>`_

.. [4] M. Coenen, S. Murali, A. Radulescu, K. Goossens and G. De Micheli, "A Buffer-Sizing Algorithm for Networks-on-Chip Using TDMA and Credit-Based End-to-End Flow Control," in *Proceedings of CODES+ISSS*, 2006.
   `(link) <https://www.cs.york.ac.uk/rts/docs/CODES-EMSOFT-CASES-2006/codes/p130.pdf>`_

.. [5] N. Concer, L. Bononi, M. Soulie, R. Locatelli and L. P. Carloni, "The Connection-Then-Credit Flow Control Protocol for Heterogeneous Multicore Systems-on-Chip," in *IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems*, vol. 29, no. 6, pp. 869-882, June 2010, doi: 10.1109/TCAD.2010.2048592.
   `(link) <https://ieeexplore.ieee.org/document/5467323>`_

