.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _runtime-endpoint-irq:

IRQ
===

IRQ configuration and claims
----------------------------

| Header: :download:`openenoc_endpoint_irq.h <../../../sw/lib/hal/openenoc_endpoint_irq.h>`
| Implementation: :download:`openenoc_endpoint_irq.c <../../../sw/lib/hal/openenoc_endpoint_irq.c>`

These functions require advertised IRQ support. Global output masking preserves enabled queued events. Event-enable changes affect future admissions. Peer-DMA and RMEM claims identify a peer; other claim sources have a deterministic zero peer index. Sequence numbers identify IRQ events, not DMA requests or their result.

.. c:function:: openenoc_endpoint_status_t openenoc_endpoint_irq_set_config(volatile csr__endpoint_interface_t *endpoint, const openenoc_endpoint_irq_config_t *config)

   Apply event enables and the global output gate.

   :param endpoint: In; required mapped, word-aligned endpoint-interface pointer.
   :param config: In; required desired IRQ configuration.
   :returns: ``OK``; ``INVALID_ARGUMENT`` for invalid arguments; ``UNSUPPORTED`` when IRQ or an enabled event's feature is absent; ``NOT_READY`` while an IRQ error-clear command is pending.
   :Side effects: Suppresses output while updating event enables, then applies the requested global enable; preserves queued claims and reservations.

.. c:function:: openenoc_endpoint_status_t openenoc_endpoint_irq_get_config(const volatile csr__endpoint_interface_t *endpoint, openenoc_endpoint_irq_config_t *config)

   Read current IRQ enables.

   :param endpoint: In; required mapped, word-aligned endpoint-interface pointer.
   :param config: Out; required IRQ-configuration destination.
   :returns: ``OK``; ``INVALID_ARGUMENT`` for invalid arguments, or ``UNSUPPORTED`` when IRQ is absent.
   :Side effects: Reads IRQ control and event-enable registers.

.. c:function:: openenoc_endpoint_status_t openenoc_endpoint_irq_set_global_enable(volatile csr__endpoint_interface_t *endpoint, bool enable)

   Set the endpoint IRQ-output gate.

   :param endpoint: In; required mapped, word-aligned endpoint-interface pointer.
   :param enable: In; requested output enable.
   :returns: ``OK``; ``INVALID_ARGUMENT`` for invalid arguments; ``UNSUPPORTED`` when IRQ is absent; ``NOT_READY`` while an IRQ error-clear command is pending.
   :Side effects: Changes the physical output gate; enabled event capture continues while it is disabled.

.. c:function:: openenoc_endpoint_status_t openenoc_endpoint_irq_set_event_enable(volatile csr__endpoint_interface_t *endpoint, openenoc_endpoint_irq_source_t source, bool enable)

   Set one IRQ event admission enable.

   :param endpoint: In; required mapped, word-aligned endpoint-interface pointer.
   :param source: In; one defined openenoc_endpoint_irq_source_t value.
   :param enable: In; requested event enable.
   :returns: ``OK``; ``INVALID_ARGUMENT`` for invalid endpoint pointer/source; ``UNSUPPORTED`` when IRQ is absent or the enabled source feature is absent.
   :Side effects: Updates the selected event enable while preserving existing claims/reservations.

.. c:function:: openenoc_endpoint_status_t openenoc_endpoint_irq_get_status(const volatile csr__endpoint_interface_t *endpoint, openenoc_endpoint_irq_status_t *status)

   Read IRQ FIFO, reservation, output and sticky-error state.

   :param endpoint: In; required mapped, word-aligned endpoint-interface pointer.
   :param status: Out; required IRQ-status destination.
   :returns: ``OK``; ``INVALID_ARGUMENT`` for invalid arguments, or ``UNSUPPORTED`` when IRQ is absent.
   :Side effects: Reads status without consuming claims or clearing errors.

.. c:function:: openenoc_endpoint_status_t openenoc_endpoint_irq_get_pending_commands(const volatile csr__endpoint_interface_t *endpoint, bool *clear_errors_pending, bool *complete_pending)

   Read maintenance-command acknowledgement state.

   :param endpoint: In; required mapped, word-aligned endpoint-interface pointer.
   :param clear_errors_pending: Out; optional error-clear pending flag; may be null.
   :param complete_pending: Out; optional completion pending flag; may be null.
   :returns: ``OK``; ``INVALID_ARGUMENT`` for invalid endpoint pointer or both outputs null; ``UNSUPPORTED`` when IRQ is absent.
   :Preconditions: At least one output pointer is required.
   :Side effects: Reads command registers and writes requested outputs; does not issue commands.

.. index::
   single: IRQ claim

.. c:function:: openenoc_endpoint_status_t openenoc_endpoint_irq_get_claim(const volatile csr__endpoint_interface_t *endpoint, openenoc_endpoint_irq_claim_t *claim)

   Read the stable FIFO-head claim.

   :param endpoint: In; required mapped, word-aligned endpoint-interface pointer.
   :param claim: Out; required source, peer-index and sequence destination.
   :returns: ``OK``; ``INVALID_ARGUMENT`` for invalid endpoint pointer/output; ``UNSUPPORTED`` when IRQ is absent; ``NOT_READY`` when no valid claim exists.
   :Side effects: Reads without consuming the claim. The output remains unchanged when no claim is available.

.. c:function:: openenoc_endpoint_status_t openenoc_endpoint_irq_request_complete(volatile csr__endpoint_interface_t *endpoint, const openenoc_endpoint_irq_claim_t *claim)

   Submit completion of the supplied current claim.

   :param endpoint: In; required mapped, word-aligned endpoint-interface pointer.
   :param claim: In; required claim identity returned by get_claim or the source callback.
   :returns: ``OK``; ``INVALID_ARGUMENT`` for invalid endpoint pointer/claim or stale/mismatching identity; ``UNSUPPORTED`` when IRQ is absent; ``NOT_READY`` while a previous completion command is pending.
   :Preconditions: Serialize claim ownership. ``source``, ``peer_index`` and ``seq`` must identify the current valid FIFO-head claim.
   :Side effects: Compares the three identity fields against the current claim, writes generated completion fields, and sets valid last. Returns without waiting for hardware acknowledgement. Error records are cleared independently.

.. c:function:: openenoc_endpoint_status_t openenoc_endpoint_irq_request_clear_errors(volatile csr__endpoint_interface_t *endpoint)

   Submit clearing of IRQ-controller sticky errors.

   :param endpoint: In; required mapped, word-aligned endpoint-interface pointer.
   :returns: ``OK``; ``INVALID_ARGUMENT`` for invalid arguments, or ``UNSUPPORTED`` when IRQ is absent. ``NOT_READY`` while the previous IRQ error-clear command is pending.
   :Side effects: Submits error clear without waiting. Hardware clears overflow/invalid-completion records without consuming claims.

IRQ dispatch, binding and maintenance
-------------------------------------

``openenoc_endpoint_irq_callbacks_t`` contains one named callback for each of the
six event sources, an optional error callback, and application context. A source
callback has the ``openenoc_endpoint_irq_callback_t`` signature: endpoint-interface pointer,
const current claim, and context. Its claim pointer is valid only during the
callback. HAL submits completion after the callback returns; callbacks must not
complete the claim themselves. Direct RX handling may continue through TLAST as
remaining frame beats arrive.

The CPU entry invokes the bound error callback for a nonzero accumulated result;
explicit service calls return their result to the caller. Missing selected
callbacks and unknown sources produce ``UNHANDLED_SOURCE`` while still submitting
claim completion. Controller ``OVERFLOW`` and ``INVALID_COMPLETE`` records are
reported until explicitly cleared. CPU EOI does not remove an endpoint claim.

RMEM failures use source 5 and the associated peer's shared error record. Peer-DMA
completion uses source 0 and also covers failed incoming bulk requests. Clearing
the error record and completing the event remain separate operations.

.. c:function:: openenoc_endpoint_irq_result_t openenoc_endpoint_irq_service(volatile csr__endpoint_interface_t *endpoint, const openenoc_endpoint_irq_callbacks_t *callbacks, uint32_t event_budget, uint32_t *handled_events)

   Service a bounded number of claims without waiting for completion acknowledgements.

   :param endpoint: In; required mapped, word-aligned endpoint-interface pointer.
   :param callbacks: In; optional descriptor; a null descriptor/selected source callback makes available claims unhandled.
   :param event_budget: In; maximum claims processed in this call. Zero performs no dispatch and only reports error state.
   :param handled_events: Out; optional number of claims whose completion was submitted by this call; may be null. Set to zero even when access validation fails.
   :returns: ``openenoc_endpoint_irq_result_t`` bitmask: OK, UNHANDLED_SOURCE, OVERFLOW, INVALID_COMPLETE, UNSUPPORTED, or INVALID_ARGUMENT, with the ``OPENENOC_ENDPOINT_IRQ_RESULT_`` prefix.
   :Preconditions: Callbacks must preserve claim ownership and must not issue their own completion command.
   :Side effects: Invokes the matching named source callback for each handled claim, submits their completion, and returns when completion is pending or the budget is exhausted. Explicit callers receive error results directly.

.. c:function:: openenoc_endpoint_status_t openenoc_endpoint_irq_bind(volatile csr__endpoint_interface_t *endpoint, const openenoc_endpoint_irq_callbacks_t *callbacks)

   Bind the endpoint and source callbacks to the HAL CPU IRQ entry.

   :param endpoint: In; validated mapped interface pointer, or null together with callbacks to unbind.
   :param callbacks: In; optional persistent callback descriptor; may be null. Both arguments null remove the existing binding.
   :returns: ``OK``; ``INVALID_ARGUMENT`` for invalid arguments, or ``UNSUPPORTED`` when IRQ is absent.
   :Preconditions: CPU IRQs must be masked; retain the mapping, descriptor and context. The CPU entry serves one bound endpoint.
   :Side effects: Updates the single bound endpoint/callback context used by the CPU IRQ entry.

.. c:function:: void openenoc_endpoint_irq_mask(void)

   Disable all CPU IRQ sources through platform hooks.

   :returns: No value.
   :Side effects: Changes CPU interrupt masking, including the state restored after an active IRQ returns.

.. c:function:: void openenoc_endpoint_irq_unmask(void)

   Enable the endpoint CPU IRQ source through platform hooks.

   :returns: No value.
   :Side effects: Enables only the endpoint source and any required global CPU interrupt gate.

.. c:function:: openenoc_endpoint_irq_result_t openenoc_endpoint_irq_handler(uintptr_t cpu_irq_state)

   Handle the platform-native CPU IRQ state.

   :param cpu_irq_state: In; opaque native state passed by the platform assembly wrapper.
   :returns: openenoc_endpoint_irq_result_t bitmask; includes NOT_BOUND or UNHANDLED_CPU_IRQ for missing binding or unsupported CPU sources, and service result flags.
   :Side effects: Classifies CPU sources, services the bound endpoint, reports errors through the bound error callback, and masks CPU IRQs for unbound/unhandled CPU-source conditions.

.. c:function:: openenoc_endpoint_status_t openenoc_endpoint_irq_complete(volatile csr__endpoint_interface_t *endpoint)

   Complete the current claim and wait for hardware acknowledgement.

   :param endpoint: In; required mapped, word-aligned endpoint-interface pointer.
   :returns: ``OK`` after hardware accepts completion; ``INVALID_ARGUMENT`` for an invalid endpoint pointer or claim identity; ``UNSUPPORTED`` when IRQ is absent; ``NOT_READY`` when no current claim exists or a previous completion command is pending.
   :Preconditions: The caller owns claim completion and serializes consumers. Hardware must make progress; this function has no software wait timeout.
   :Side effects: Reads the current claim, validates and submits its completion, then polls until hardware clears completion valid. Sticky errors are unchanged.

.. c:function:: openenoc_endpoint_status_t openenoc_endpoint_irq_clear_errors(volatile csr__endpoint_interface_t *endpoint)

   Clear IRQ-controller sticky errors and wait for hardware acknowledgement.

   :param endpoint: In; required mapped, word-aligned endpoint-interface pointer.
   :returns: ``OK`` after hardware accepts clearing; ``INVALID_ARGUMENT`` for an invalid endpoint pointer; ``UNSUPPORTED`` when IRQ is absent; ``NOT_READY`` while a previous IRQ error-clear command is pending.
   :Preconditions: Hardware must make progress; this function has no software wait timeout.
   :Side effects: Submits clearing of overflow and invalid-completion errors, then polls until hardware clears the command. It preserves queued claims and DMA/RMEM error records.

CPU platform contract
---------------------

The CPU IRQ entry lives in HAL. The selected ``sw/platform/<platform>`` supplies
the internal mask and source-classification hooks declared in
``openenoc_endpoint_irq.h``, plus its startup and assembly context wrapper. HAL
includes no CPU-specific header; the platform implementation does not access
endpoint CSR registers or call the endpoint HAL.

Each platform defines the opaque encoding of ``cpu_irq_state``. Its assembly
wrapper passes this state to the HAL entry and performs processor interrupt
controller acknowledgement where required. Source-classification hooks inspect
that state without consuming endpoint claims. Porting to another CPU preserves
the application callback and runtime function contracts.

On PicoRV32, ``irq_entry`` saves the integer context and ``q0`` return PC,
passes the ``q1`` source bitmask to the HAL handler, restores the context,
and executes ``retirq``. CPU input 3 is the endpoint source; a set bit in
the CPU IRQ mask disables its source.

.. c:function:: void _openenoc_endpoint_irq_disable_all(void)

   Internal platform hook used by the public CPU mask function.

   :returns: No value.
   :Side effects: Disables all CPU IRQ sources, including the interrupt state restored after an active handler returns.

.. c:function:: void _openenoc_endpoint_irq_enable_endpoint(void)

   Internal platform hook used by the public CPU unmask function.

   :returns: No value.
   :Side effects: Enables only the endpoint CPU IRQ source and any required processor-wide interrupt gate.

.. c:function:: bool _openenoc_endpoint_irq_is_endpoint(uintptr_t cpu_irq_state)

   Classify whether the native CPU IRQ state includes the endpoint source.

   :param cpu_irq_state: In; opaque platform-native IRQ state supplied by the assembly wrapper.
   :returns: true when the endpoint source is represented; otherwise false.
   :Side effects: Inspects the supplied state without modifying CPU IRQ or endpoint claim state.

.. c:function:: bool _openenoc_endpoint_irq_has_unhandled_sources(uintptr_t cpu_irq_state)

   Classify whether the native state includes a source outside the endpoint IRQ.

   :param cpu_irq_state: In; opaque platform-native IRQ state supplied by the assembly wrapper.
   :returns: true when an unsupported CPU IRQ source is represented; otherwise false.
   :Side effects: Inspects the supplied state without modifying CPU IRQ or endpoint claim state.

Public declarations
-------------------

The maintained header below provides the exact public type and enum definitions.

.. index::
   single: openenoc_endpoint_irq_source_t
   single: openenoc_endpoint_irq_config_t
   single: openenoc_endpoint_irq_status_t
   single: openenoc_endpoint_irq_result_t
   single: openenoc_endpoint_irq_claim_t
   single: openenoc_endpoint_irq_callbacks_t
   single: openenoc_endpoint_irq_error_callback_t
   single: openenoc_endpoint_irq_callback_t

.. literalinclude:: ../../../sw/lib/hal/openenoc_endpoint_irq.h
   :language: c
   :caption: IRQ public types, claims and callbacks
   :start-at: typedef enum {
   :end-before: openenoc_endpoint_status_t openenoc_endpoint_irq_set_config
   :linenos:
