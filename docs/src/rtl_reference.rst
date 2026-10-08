.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-reference:

RTL Reference
=============

This chapter describes RTL block responsibilities, interfaces, and behavior.
Each block description identifies the implemented functionality and the design
requirements that remain to be implemented.

The reference covers every project module and interface under ``hw/rtl``,
alongside the generated HAL interfaces, CSR modules, and packages. Each block
has its own RST file, named after its SV source. Each page begins with a brief
component description, followed by parameter and signal tables, architecture
and operation, and a functional-scenario outline. Parameter tables include
defaults and allowed values; signal tables include types and directions or
modport roles. Packages list generated constants and have no runtime signals.
Scenario outlines reserve space for WaveDrom timing diagrams and detailed
examples as each block evolves.
Implementation plans are kept here as explicitly marked TODO items; they do not
describe functionality already present in RTL. Testbench wrappers are described
in :doc:`verification`; third-party TAXI and PicoRV32 sources remain dependencies.

.. _rtl-interfaces:

Interfaces
----------

.. toctree::
   :maxdepth: 1
   :titlesonly:

   rtl/openenoc_cpuif_if
   rtl/openenoc_eth_if
   rtl/openenoc_lookup_if
   rtl/openenoc_learning_if
   rtl/openenoc_peer_lookup_if
   rtl/openenoc_irq_event_if
   rtl/openenoc_dma_transfer_if

Endpoint blocks
---------------

.. toctree::
   :maxdepth: 1
   :titlesonly:

   rtl/openenoc_endpoint_interface
   rtl/openenoc_endpoint_full
   rtl/openenoc_endpoint_direct_axis
   rtl/openenoc_endpoint_peer_lookup
   rtl/openenoc_endpoint_irq_controller
   rtl/openenoc_endpoint_dma_engine
   rtl/openenoc_endpoint_oetp_engine

Switching and stream transport
------------------------------

.. toctree::
   :maxdepth: 1
   :titlesonly:

   rtl/openenoc_eth_adapter
   rtl/openenoc_eth_switch
   rtl/openenoc_eth_switch_shared_bus
   rtl/openenoc_eth_switch_crossbar
   rtl/openenoc_forwarding_table
   rtl/openenoc_forwarding_table_arb_mux
   rtl/openenoc_axis_header_parser
   rtl/openenoc_axis_forwarding_engine
   rtl/openenoc_axis_demux
   rtl/openenoc_axis_switch
   rtl/openenoc_axis_monitor

Memory interconnect and processor
---------------------------------

.. toctree::
   :maxdepth: 1
   :titlesonly:

   rtl/openenoc_axil_cpuif_adapter
   rtl/openenoc_cpuif_axil_adapter
   rtl/openenoc_axil_crossbar
   rtl/openenoc_axil_crossbar_addr
   rtl/openenoc_axil_crossbar_rd
   rtl/openenoc_axil_crossbar_wr
   rtl/openenoc_axil_crossbar_skid_buffer
   rtl/openenoc_axil_ram
   rtl/openenoc_picorv32
   rtl/openenoc_picorv32_axil_adapter
   rtl/openenoc_rr_arbiter

.. _rtl-generated-hal:

Generated HAL RTL
-----------------

SystemRDL is the source of truth for generated interfaces, register blocks,
bridges, and endpoint packages. ``make -C hal all`` regenerates these artifacts.
RTL changes belong in the RDL, exporter, or template; generated SV is not edited
by hand. The software-visible register specification remains in :doc:`hal`.

.. toctree::
   :maxdepth: 1
   :titlesonly:

   rtl/openenoc_endpoint_if
   rtl/openenoc_switch_if
   rtl/openenoc_endpoint_full_csr
   rtl/openenoc_endpoint_full_csr_bridge
   rtl/openenoc_endpoint_full_csr_pkg
   rtl/openenoc_endpoint_full_pkg

``hal/tools/`` unit tests cover the exporters; ``dv/hal/openenoc_endpoint_full/``
checks the generated CSR model against RTL, and endpoint tests cover wiring.
Future reference additions should show generation dependencies and field
ownership at the bridge boundary, without maintaining a duplicate register map.
