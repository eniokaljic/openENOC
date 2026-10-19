.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _runtime-endpoint-rmem:

Remote memory
=============

.. index::
   single: RMEM

| Header: :download:`openenoc_endpoint_rmem.h <../../../sw/lib/hal/openenoc_endpoint_rmem.h>`
| Implementation: :download:`openenoc_endpoint_rmem.c <../../../sw/lib/hal/openenoc_endpoint_rmem.c>`

.. c:function:: openenoc_endpoint_status_t openenoc_endpoint_rmem_get_region(const volatile csr__endpoint_interface_t *endpoint, openenoc_endpoint_rmem_region_t *region)

   Return the one mapped RMEM memory window.

   :param endpoint: In; required mapped, word-aligned endpoint-interface pointer.
   :param region: Out; required mapped words pointer and capacity in 32-bit words.
   :returns: ``OK``; ``INVALID_ARGUMENT`` for invalid endpoint pointer/output; ``UNSUPPORTED`` when RMEM is absent.
   :Preconditions: Configure peer mappings before using the pointed-to region. Accessors select the peer in hardware; callers check subregion alignment/capacity and follow platform MMIO rules.
   :Side effects: Uses generated capability information and returns an existing mapping; performs no MMIO access, remote transaction or allocation.

Public declarations
-------------------

The maintained header below provides the exact public type and enum definitions.

.. index::
   single: openenoc_endpoint_rmem_region_t

.. literalinclude:: ../../../sw/lib/hal/openenoc_endpoint_rmem.h
   :language: c
   :caption: RMEM region type
   :start-at: typedef struct {
   :end-before: openenoc_endpoint_status_t openenoc_endpoint_rmem_get_region
   :linenos:
