.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _runtime-switch-config:

Switch configuration and pause control
======================================

| Header: :download:`openenoc_switch_config.h <../../../sw/lib/hal/openenoc_switch_config.h>`
| Implementation: :download:`openenoc_switch_config.c <../../../sw/lib/hal/openenoc_switch_config.c>`

These functions manage the default forwarding bitmap, operation mode, and
explicit pause handshake. The shared pointer, serialization and return-value
contracts are specified in :ref:`runtime-switch-api`. Abbreviated status names
use the ``OPENENOC_SWITCH_STATUS_`` prefix.

The default bitmap applies when no enabled forwarding-table entry matches.
Its bits follow the RDL interface order; bits above the generated interface
count must be zero. A zero bitmap drops unmatched frames. Bitmap reads require
a completed pause in either mode, and bitmap writes require managed mode and a
completed pause. Neither operation changes mode or pause state.

Mode and status queries are available while forwarding is active. Changing mode
requires a completed pause and leaves the pause request asserted. The caller
controls when to resume after finishing an update. Pause and resume submissions
are non-blocking: a successful call is separate from hardware reaching the
requested state. The HAL supplies no polling loop or software timeout.

Default forwarding
------------------

.. index::
   single: Default forwarding

.. c:function:: openenoc_switch_status_t openenoc_switch_get_default_forwarding(const volatile csr__switch_interface_t *switch_interface, uint32_t *bitmap)

   Read the bitmap used for unmatched frames.

   :param switch_interface: In; required mapped, word-aligned switch-interface pointer.
   :param bitmap: Out; required destination for the current output-interface bitmap. In RDL interface order, bit ``interface_count - 1`` selects the first interface.
   :returns: ``OK``; ``INVALID_ARGUMENT`` for an invalid switch pointer or missing output; ``NOT_READY`` without a completed pause.
   :Preconditions: ``pause_request`` and ``pause_done`` must both be set. Either operation mode is allowed.
   :Side effects: Reads forwarding-control and default-bitmap CSRs. Updates the output only on success; preserves mode and pause state.

.. c:function:: openenoc_switch_status_t openenoc_switch_set_default_forwarding(volatile csr__switch_interface_t *switch_interface, uint32_t bitmap)

   Set the bitmap used for unmatched frames.

   :param switch_interface: In; required mapped, word-aligned switch-interface pointer.
   :param bitmap: In; output-interface selection, including zero for drop. In RDL interface order, bit ``interface_count - 1`` selects the first interface. Unimplemented bits must be zero.
   :returns: ``OK``; ``INVALID_ARGUMENT`` for an invalid switch pointer; ``OUT_OF_RANGE`` for bits outside the generated interface count; ``NOT_ALLOWED`` in unmanaged mode; ``NOT_READY`` in managed mode without a completed pause.
   :Preconditions: Managed mode and a completed pause. Argument validation precedes mode and pause checks; the mode check precedes the pause check.
   :Side effects: Writes the default bitmap after validation. Preserves mode, pause state, and table entries.

Operation mode
--------------

.. c:function:: openenoc_switch_status_t openenoc_switch_get_operation_mode(const volatile csr__switch_interface_t *switch_interface, openenoc_switch_operation_mode_t *mode)

   Read the current managed or unmanaged operation mode.

   :param switch_interface: In; required mapped, word-aligned switch-interface pointer.
   :param mode: Out; required destination for the current operation-mode enum.
   :returns: ``OK``; ``INVALID_ARGUMENT`` for an invalid switch pointer or missing output.
   :Preconditions: No pause is required.
   :Side effects: Reads the mode CSR field and updates the output only on success; preserves all switch state.

.. c:function:: openenoc_switch_status_t openenoc_switch_set_operation_mode(volatile csr__switch_interface_t *switch_interface, openenoc_switch_operation_mode_t mode)

   Explicitly change the switch operation mode.

   :param switch_interface: In; required mapped, word-aligned switch-interface pointer.
   :param mode: In; ``OPENENOC_SWITCH_UNMANAGED`` or ``OPENENOC_SWITCH_MANAGED``.
   :returns: ``OK``; ``INVALID_ARGUMENT`` for an invalid switch pointer or mode; ``NOT_READY`` without a completed pause, including a request to retain the current mode.
   :Preconditions: ``pause_request`` and ``pause_done`` must both be set. The current mode may be managed or unmanaged.
   :Side effects: Writes only the operation-mode field. Preserves pause request, default bitmap, and table contents. Unmanaged mode permits hardware learning after forwarding resumes.

Pause handshake
---------------

.. index::
   single: Pause handshake

.. c:function:: openenoc_switch_status_t openenoc_switch_get_status(const volatile csr__switch_interface_t *switch_interface, openenoc_switch_forwarding_status_t *status)

   Read the current pause request and hardware completion indication.

   :param switch_interface: In; required mapped, word-aligned switch-interface pointer.
   :param status: Out; required destination for ``pause_requested`` and ``pause_done``.
   :returns: ``OK``; ``INVALID_ARGUMENT`` for an invalid switch pointer or missing output.
   :Preconditions: No pause is required; callers can poll this function during a pause transition.
   :Side effects: Reads both forwarding-control fields and updates the output only on success. Does not clear status or change mode or pause request.

.. c:function:: openenoc_switch_status_t openenoc_switch_request_pause(volatile csr__switch_interface_t *switch_interface)

   Explicitly request a pause at a safe forwarding boundary.

   :param switch_interface: In; required mapped, word-aligned switch-interface pointer.
   :returns: ``OK`` after setting the request; ``INVALID_ARGUMENT`` for an invalid switch pointer.
   :Preconditions: Either mode and any current pause state are allowed.
   :Side effects: Sets ``pause_request`` to one and preserves operation mode. Repeated calls are idempotent. Does not wait for ``pause_done``; the caller polls status before data access.

.. c:function:: openenoc_switch_status_t openenoc_switch_resume(volatile csr__switch_interface_t *switch_interface)

   Explicitly release the pause request.

   :param switch_interface: In; required mapped, word-aligned switch-interface pointer.
   :returns: ``OK`` after clearing the request; ``INVALID_ARGUMENT`` for an invalid switch pointer.
   :Preconditions: Either mode and any current pause state are allowed.
   :Side effects: Clears ``pause_request`` and preserves operation mode. Repeated calls are idempotent. Does not wait for ``pause_done`` to clear; a remaining completion indication does not authorize data access after resume.

Public declarations
-------------------

The maintained header below provides the exact public mode and status types.

.. index::
   single: openenoc_switch_operation_mode_t
   single: openenoc_switch_forwarding_status_t
   single: OPENENOC_SWITCH_UNMANAGED
   single: OPENENOC_SWITCH_MANAGED

.. literalinclude:: ../../../sw/lib/hal/openenoc_switch_config.h
   :language: c
   :caption: Switch operation-mode and forwarding-status types
   :start-at: typedef enum {
   :end-before: openenoc_switch_status_t openenoc_switch_get_default_forwarding
   :linenos:
