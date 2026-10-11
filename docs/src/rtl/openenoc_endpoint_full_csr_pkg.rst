.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-endpoint-full-csr-pkg:

CSR types package -- openenoc_endpoint_full_csr_pkg
===================================================

Defines the generated register-bank types and configuration constants used by
its consumers.

**Source:** :download:`openenoc_endpoint_full_csr_pkg.sv <../../../build/hal/openenoc_endpoint_full/rtl/openenoc_endpoint_full_csr_pkg.sv>`.

Parameters
----------

These are generated local constants, rather than instance parameters. Change
the RDL and regenerate the package to change their values.

.. list-table:: Parameters
   :class: rtl-reference-table
   :header-rows: 1
   :widths: 30 18 22 30

   * - Name
     - Default value
     - Allowed values
     - Description
   * - ``OPENENOC_ENDPOINT_FULL_CSR_DATA_WIDTH``
     - ``32``
     - Generated constant; not overridable in SV
     - CSR data width in bits.
   * - ``OPENENOC_ENDPOINT_FULL_CSR_MIN_ADDR_WIDTH``
     - ``13``
     - Generated constant; not overridable in SV
     - Minimum CSR byte-address width.
   * - ``OPENENOC_ENDPOINT_FULL_CSR_SIZE``
     - ``'h1100``
     - Generated constant; not overridable in SV
     - Implemented CSR address span in bytes.
   * - ``NUM_OF_PEERS``
     - ``'h4``
     - Generated constant; not overridable in SV
     - Number of generated peer entries.
   * - ``RMEM_TOTAL_DEPTH``
     - ``'h100``
     - Generated constant; not overridable in SV
     - External RMEM aperture size in 32-bit words.
   * - ``MAX_RAW_FRAME_SIZE``
     - ``'h2000``
     - Generated constant; not overridable in SV
     - Synthesized raw Ethernet frame ceiling, excluding FCS.
   * - ``HAS_PEER_DMA``
     - ``'h1``
     - Generated constant; not overridable in SV
     - Peer DMA capability flag.
   * - ``HAS_NON_OETP_DMA``
     - ``'h1``
     - Generated constant; not overridable in SV
     - Raw DMA capability flag.
   * - ``HAS_DIRECT_AXIS``
     - ``'h1``
     - Generated constant; not overridable in SV
     - Direct software stream capability flag.
   * - ``HAS_RMEM``
     - ``'h1``
     - Generated constant; not overridable in SV
     - Scalar RMEM capability flag.
   * - ``HAS_IRQ``
     - ``'h1``
     - Generated constant; not overridable in SV
     - Endpoint interrupt capability flag.
   * - ``NUM_OF_INTERFACES``
     - ``'h4``
     - Generated constant; not overridable in SV
     - Switch port count.
   * - ``TABLE_DEPTH``
     - ``'h8``
     - Generated constant; not overridable in SV
     - Forwarding-table entry count.

Signals
-------

.. list-table:: Public signals and interfaces
   :class: rtl-reference-table
   :header-rows: 1
   :widths: 26 27 17 30

   * - Name
     - Type
     - Direction / role
     - Description
   * - None
     - —
     - —
     - This package has no runtime ports or signals.

Architecture and operation
--------------------------

The package defines CSR hardware-interface types, register constants, and
elaborated CSR parameters shared by the generated register block and bridge.
It has no runtime ports or state and must be compiled before its users.

``OPENENOC_ENDPOINT_FULL_CSR_DATA_WIDTH`` and
``OPENENOC_ENDPOINT_FULL_CSR_MIN_ADDR_WIDTH`` define the register-bus shape.
``NUM_OF_PEERS``, ``RMEM_TOTAL_DEPTH``, and ``MAX_RAW_FRAME_SIZE`` configure the
endpoint boundary and memory-transfer infrastructure. The ``HAS_*`` constants
report elaborated capabilities; ``NUM_OF_INTERFACES`` and ``TABLE_DEPTH``
configure the associated switch boundary.

.. list-table:: Exported hardware-interface types
   :class: rtl-reference-table
   :header-rows: 1
   :widths: 45 55

   * - Type
     - Description
   * - ``openenoc_endpoint_full_csr__in_t``
     - Hardware next-value updates, hardware clears, and external responses.
   * - ``openenoc_endpoint_full_csr__out_t``
     - Stored software controls and external register-file requests.

Nested field types compose these two structures. Their field names and widths
follow :doc:`../hal`; the generated source provides the complete type tree.
Consumers do not instantiate the package and do not drive its constants.

Functional scenarios
--------------------

This section reserves space for scenario descriptions and WaveDrom timing
diagrams. The current outline is:

* Compilation before the register bank and bridge.
* Configuration constants derived from the endpoint RDL.
* Hardware update and software control structures used at the bridge.
