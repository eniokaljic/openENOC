.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _runtime-switch-table:

Switch forwarding table
=======================

| Header: :download:`openenoc_switch_table.h <../../../sw/lib/hal/openenoc_switch_table.h>`
| Implementation: :download:`openenoc_switch_table.c <../../../sw/lib/hal/openenoc_switch_table.c>`

Each entry contains a destination MAC address, an output-interface bitmap, and
an enable flag. The shared pointer, serialization and return-value contracts
are specified in :ref:`runtime-switch-api`. Abbreviated status names use the
``OPENENOC_SWITCH_STATUS_`` prefix.

All table reads and writes require both ``pause_request`` and ``pause_done``.
Reads are allowed in either operation mode. Writes require managed mode;
unmanaged writes return ``NOT_ALLOWED`` before pause readiness is checked.
Arguments are validated before these state checks. A data access never changes
the operation mode or pause request and never waits for a pause to complete.

Entry indices satisfy ``entry_index < table_depth``. MAC octets use network
address order, with no unicast-only restriction: multicast and broadcast keys
are valid. Bitmap bits follow the RDL interface order and bits beyond the
generated interface count must be zero. An enabled entry with an empty bitmap
drops matching frames. Disabling an entry removes it from lookup, allowing a
different enabled match or the default bitmap to determine forwarding.

The API accepts duplicate MAC keys. The current table RTL resolves multiple
enabled matches using the lowest entry index. The caller serializes table
management and prevents another software context from changing mode or pause
state until each access has finished.

Entry access
------------

.. c:function:: openenoc_switch_status_t openenoc_switch_table_get_entry(const volatile csr__switch_interface_t *switch_interface, uint16_t entry_index, openenoc_switch_table_entry_t *entry)

   Read all fields of one forwarding-table entry.

   :param switch_interface: In; required mapped, word-aligned switch-interface pointer.
   :param entry_index: In; zero-based index below the generated table depth.
   :param entry: Out; required destination for the MAC, bitmap, and enable flag.
   :returns: ``OK``; ``INVALID_ARGUMENT`` for an invalid switch pointer or missing output; ``OUT_OF_RANGE`` for an invalid index; ``NOT_READY`` without a completed pause.
   :Preconditions: A completed pause in either operation mode; serialize other software access.
   :Side effects: Reads forwarding-control and entry CSRs, unpacks the MAC into network-order octets, and updates the output only on success. Preserves mode, pause state, and table contents.

.. c:function:: openenoc_switch_status_t openenoc_switch_table_set_entry(volatile csr__switch_interface_t *switch_interface, uint16_t entry_index, const openenoc_switch_table_entry_t *entry)

   Set the complete contents and requested enable state of one entry.

   :param switch_interface: In; required mapped, word-aligned switch-interface pointer.
   :param entry_index: In; zero-based index below the generated table depth.
   :param entry: In; required MAC, valid output-interface bitmap, and desired enable state. Multicast and broadcast keys are valid; an enabled entry with bitmap zero drops matching frames.
   :returns: ``OK``; ``INVALID_ARGUMENT`` for an invalid switch pointer or missing entry; ``OUT_OF_RANGE`` for an invalid index or bitmap; ``NOT_ALLOWED`` in unmanaged mode; ``NOT_READY`` in managed mode without a completed pause.
   :Preconditions: Managed mode and a completed pause; serialize other software access. All argument checks complete before writing the entry.
   :Side effects: Disables the entry, writes lower and upper MAC fields and the bitmap, then writes the requested enable flag last. Preserves mode, pause state, and other entries.

Enable state and table clearing
-------------------------------

.. c:function:: openenoc_switch_status_t openenoc_switch_table_set_entry_enabled(volatile csr__switch_interface_t *switch_interface, uint16_t entry_index, bool enabled)

   Change only the enable state of an existing entry.

   :param switch_interface: In; required mapped, word-aligned switch-interface pointer.
   :param entry_index: In; zero-based index below the generated table depth.
   :param enabled: In; true to enable lookup matching, false to ignore the entry.
   :returns: ``OK``; ``INVALID_ARGUMENT`` for an invalid switch pointer; ``OUT_OF_RANGE`` for an invalid index; ``NOT_ALLOWED`` in unmanaged mode; ``NOT_READY`` in managed mode without a completed pause.
   :Preconditions: Managed mode and a completed pause; the caller has supplied the intended entry MAC and bitmap before enabling it.
   :Side effects: Writes only the selected entry's enable field. Preserves its MAC and bitmap, other entries, operation mode, and pause state.

.. c:function:: openenoc_switch_status_t openenoc_switch_table_clear(volatile csr__switch_interface_t *switch_interface)

   Disable all forwarding-table entries.

   :param switch_interface: In; required mapped, word-aligned switch-interface pointer.
   :returns: ``OK``; ``INVALID_ARGUMENT`` for an invalid switch pointer; ``NOT_ALLOWED`` in unmanaged mode; ``NOT_READY`` in managed mode without a completed pause.
   :Preconditions: Managed mode and a completed pause; keep mode and pause state stable throughout the iteration.
   :Side effects: Clears every entry's enable flag. Preserves stored MACs and bitmaps, the default bitmap, operation mode, and pause request. Subsequent lookups use the default bitmap until an entry is enabled.

Public declarations
-------------------

The maintained header below provides the exact public entry type.

.. index::
   single: openenoc_switch_table_entry_t

.. literalinclude:: ../../../sw/lib/hal/openenoc_switch_table.h
   :language: c
   :caption: Switch forwarding-table entry type
   :start-at: typedef struct {
   :end-before: openenoc_switch_status_t openenoc_switch_table_get_entry
   :linenos:
