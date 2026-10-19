.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-endpoint-full-pkg:

Endpoint configuration package -- openenoc_endpoint_full_pkg
============================================================

.. index::
   single: openenoc_endpoint_full_pkg

Defines the generated memory map and configuration types for the reference
endpoint.

**Source:** :download:`openenoc_endpoint_full_pkg.sv <../../../build/hal/openenoc_endpoint_full/rtl/openenoc_endpoint_full_pkg.sv>`.

Parameters
----------

These are generated local constants, rather than instance parameters. Change
the RDL and regenerate the package to change their values.

.. list-table:: Parameters
   :class: rtl-reference-table
   :header-rows: 1
   :widths: 45 17 19 19

   * - Name
     - Default value
     - Allowed values
     - Description
   * - ``OPENENOC_ENDPOINT_FULL_DATA_WIDTH``
     - ``32``
     - Generated constant; not overridable in SV
     - Endpoint memory data width in bits.
   * - ``OPENENOC_ENDPOINT_FULL_MIN_ADDR_WIDTH``
     - ``30``
     - Generated constant; not overridable in SV
     - Minimum endpoint memory-map address width.
   * - ``OPENENOC_ENDPOINT_FULL_SIZE``
     - ``'h20001100``
     - Generated constant; not overridable in SV
     - Endpoint address-map span in bytes.
   * - ``IMEM_DEPTH``
     - ``'h2000``
     - Generated constant; not overridable in SV
     - Instruction-memory depth in 32-bit words.
   * - ``IMEM_BASE_ADDR``
     - ``'h0``
     - Generated constant; not overridable in SV
     - Instruction-memory byte base address.
   * - ``DMEM_DEPTH``
     - ``'h2000``
     - Generated constant; not overridable in SV
     - Data-memory depth in 32-bit words.
   * - ``DMEM_BASE_ADDR``
     - ``'h10000000``
     - Generated constant; not overridable in SV
     - Data-memory byte base address.
   * - ``CSR_BASE_ADDR``
     - ``'h20000000``
     - Generated constant; not overridable in SV
     - Register-bank byte base address.

Signals
-------

.. list-table:: Public signals and interfaces
   :class: rtl-reference-table
   :header-rows: 1
   :widths: 12 18 20 50

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

The package exports the full endpoint's data width, memory depths/base addresses,
and elaborated configuration parameters. :ref:`rtl-endpoint-full` consumes
these constants to construct the memory map and synthesize infrastructure.
It has no runtime state. Compile it before the endpoint module.

SystemRDL allows register ``accesswidth`` and memory-map organization to be
configured. PeakRDL derives the generated CPUIF data width from the largest
register ``accesswidth`` in the scope it exports. This top-level map contains
only external IMEM, DMEM, and CSR blocks, so PeakRDL cannot infer the width
from their registers and defaults ``OPENENOC_ENDPOINT_FULL_DATA_WIDTH`` to 32.

The current endpoint components and oETP protocol implementation require
32-bit data and address buses. The full endpoint checks that the generated
endpoint and CSR data widths equal 32 and that both address maps fit within
the 32-bit address space. RDL configurations used with these components must
respect those constraints.

``IMEM_DEPTH`` and ``DMEM_DEPTH`` count 32-bit memory words; multiplying by
four gives each RAM aperture in bytes. ``IMEM_BASE_ADDR``, ``DMEM_BASE_ADDR``,
and ``CSR_BASE_ADDR`` set the crossbar target bases.
``OPENENOC_ENDPOINT_FULL_MIN_ADDR_WIDTH`` describes the minimum address width
needed for the map, and ``OPENENOC_ENDPOINT_FULL_SIZE`` gives its byte span.
The current minimum is 30 bits; the AXI and AXI4-Lite address buses remain
fixed at 32 bits.

.. list-table:: Exported configuration types
   :class: rtl-reference-table
   :header-rows: 1
   :widths: 34 66

   * - Type
     - Description
   * - ``openenoc_endpoint_full__in_t``
     - Native memory/register acknowledgements and read data for all regions.
   * - ``openenoc_endpoint_full__out_t``
     - Native requests, addresses, write data, and bit enables for all regions.

Per-region ``__imem__*``, ``__dmem__*``, and ``__csr__*`` types compose these
structures. Their address widths come from the generated memory apertures.
The current AXI4-Lite wrapper consumes the constants directly rather than
using these aggregate native request/response structures as runtime ports.
