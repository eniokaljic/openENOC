.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

Scalable Ethernet-based Network-on-Chip
=======================================

Overview
--------

**openENOC** is an open-source hardware and software initiative that develops a modular and scalable Ethernet-based Network-on-Chip (NoC) architecture for FPGA SoCs and advanced MPSoC designs.

By adopting standard Ethernet Layer 2 as the native on-chip transport protocol, rather than relying on traditional mesh or proprietary interconnects, openENOC enables seamless integration with existing Ethernet infrastructure and establishes a unified communication and programming model across both on-chip and off-chip systems.

.. image:: ../images/openENOC.logo.svg
   :width: 25%
   :align: center

This approach allows processors, accelerators, and peripherals to be connected through a flexible, packet-switched network based on L2 switching, effectively bridging the gap between on-chip and off-chip networking while lowering the complexity of building large-scale systems.

Background
----------

The concept originated from practical challenges encountered during the development of the NLnet-funded `WireGuard FPGA project
<https://nlnet.nl/project/KlusterLab-Wireguard/>`_, where scaling cryptographic workloads such as Curve25519 and ChaCha20-Poly1305 exposed limitations of conventional interconnect architectures.

In response, openENOC introduces an Ethernet-based interconnect designed to
support efficient, network-oriented scaling of cryptographic processing, edge
computing, and AI acceleration workloads.

Goals
-----

openENOC aims to deliver a complete, freely licensed full-stack solution
combining reusable hardware and software gateware developed in SystemVerilog
and C/C++.

The project will provide RTL components, integration APIs, verification
infrastructure, and reference designs, forming a cohesive and production-ready
foundation.

Its primary goal is to unlock the potential of networked reconfigurable
computing by making it accessible, portable, and adaptable across a wide range
of use cases.

All results will be released openly to encourage reuse, strengthen the open
hardware ecosystem, and empower developers and organizations to build
interoperable, future-proof, and community-driven MPSoC solutions.

Project Plan
------------

The project is organized around `four global milestones (M1-M4)
<https://github.com/eniokaljic/openENOC/milestones>`_ representing successive
development phases of the openENOC platform: architecture definition,
functional prototyping, system integration, and final platform release.

.. image:: ../images/ProjectExecutionPlan.png
   :width: 100%
   :align: center

This structure ensures that hardware development, software integration,
verification, tooling, and documentation progress in parallel throughout the
project.

Work Packages
-------------

WP1 - RTL Gateware Development
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This work package delivers the complete openENOC RTL implementation forming the
hardware datapath of the Ethernet-based Network-on-Chip.

* ☐ `RTL1 - Core Switching Primitives <https://github.com/eniokaljic/openENOC/issues/1>`_
* ☐ `RTL2 - Packet Processing Pipeline <https://github.com/eniokaljic/openENOC/issues/2>`_
* ☐ `RTL3 - Forwarding & DMA Engines <https://github.com/eniokaljic/openENOC/issues/3>`_
* ☐ `RTL4 - Integrated NoC Fabric <https://github.com/eniokaljic/openENOC/issues/4>`_

WP2 - Integration HAL and Software API Development
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This work package provides the software interface layer required to configure
and control the NoC.

* ☐ `SW1 - HAL Architecture Specification <https://github.com/eniokaljic/openENOC/issues/5>`_
* ☐ `SW2 - RISC-V Platform Integration <https://github.com/eniokaljic/openENOC/issues/6>`_
* ☐ `SW3 - Runtime Control API <https://github.com/eniokaljic/openENOC/issues/7>`_
* ☐ `SW4 - Reference Applications <https://github.com/eniokaljic/openENOC/issues/8>`_

WP3 - Verification Infrastructure Development
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This work package establishes the verification infrastructure required to
validate both the hardware and software components of the platform.

* ☐ `DV1 - Simulation Framework <https://github.com/eniokaljic/openENOC/issues/9>`_
* ☐ `DV2 - Module-Level Verification <https://github.com/eniokaljic/openENOC/issues/10>`_
* ☐ `DV3 - HW/SW Co-Verification <https://github.com/eniokaljic/openENOC/issues/11>`_
* ☐ `DV4 - Continuous Verification Infrastructure <https://github.com/eniokaljic/openENOC/issues/12>`_

WP4 - Demo SoCs and Educational Kits Development
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This work package demonstrates the practical applicability of openENOC through
deployable FPGA-based systems.

* ☐ `DEM1 - Initial FPGA NoC Demo <https://github.com/eniokaljic/openENOC/issues/13>`_
* ☐ `DEM2 - Extended FPGA Demonstration Platform <https://github.com/eniokaljic/openENOC/issues/14>`_

WP5 - FOSS Synthesis & PnR Toolchains Integration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This work package ensures that openENOC can be built using a fully open-source
FPGA toolchain.

* ☐ `PNR1 - Open Synthesis Flow <https://github.com/eniokaljic/openENOC/issues/19>`_
* ☐ `PNR2 - Automated Bitstream Build Flow <https://github.com/eniokaljic/openENOC/issues/20>`_

WP6 - Repository & Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This work package produces the technical documentation and developer resources
necessary to make the project accessible and reusable by the wider open
hardware community.

* ☐ `DOC1 - Initial Architecture Documentation <https://github.com/eniokaljic/openENOC/issues/15>`_
* ☐ `DOC2 - Design Documentation <https://github.com/eniokaljic/openENOC/issues/16>`_
* ☐ `DOC3 - Tutorials & Developer Guides <https://github.com/eniokaljic/openENOC/issues/17>`_
* ☐ `DOC4 - Reproducible Build & Verification Documentation <https://github.com/eniokaljic/openENOC/issues/18>`_

WP7 - Results Dissemination
~~~~~~~~~~~~~~~~~~~~~~~~~~~

This work package focuses on communicating the results of the project to the
broader open hardware and research communities.

* ☐ `DIS1 - Technical Publication <https://github.com/eniokaljic/openENOC/issues/21>`_
* ☐ `DIS2 - Conference Presentation <https://github.com/eniokaljic/openENOC/issues/22>`_

Acknowledgements
----------------

We are grateful to **NLnet Foundation** for their sponsorship of this
development activity.

.. image:: https://nlnet.nl/logo/banner.svg
   :width: 25%
   :align: center

.. image:: https://nlnet.nl/image/logos/NGI0Core_tag.svg
   :width: 25%
   :align: center

This project was funded through the NGI0 Commons Fund, a fund established by
NLnet with financial support from the European Commission's Next Generation
Internet programme, under the aegis of DG Communications Networks, Content and
Technology under grant agreement No. 101135429. Additional funding is made
available by the Swiss State Secretariat for Education, Research and Innovation.
