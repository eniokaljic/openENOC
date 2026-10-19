.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _runtime-api-reference:

Runtime API Reference
=====================

This reference specifies the endpoint and switch HAL functions, their
parameters, return values, preconditions, and observable effects. The CSR
programming model is specified in :doc:`hal` and the generated
:doc:`endpoint CSR reference <generated/openenoc_endpoint_interface>` and
:doc:`switch CSR reference <generated/openenoc_switch_interface>`.

.. _runtime-endpoint-api:

Endpoint API
------------

HAL libraries
~~~~~~~~~~~~~

Each endpoint HAL library has its own page. The hierarchy below lists its
documented functions. Shared contracts, types and utilities are specified on
this page.

.. toctree::
   :maxdepth: 3

   runtime/openenoc_endpoint_config
   runtime/openenoc_endpoint_peer
   runtime/openenoc_endpoint_dma
   runtime/openenoc_endpoint_rmem
   runtime/openenoc_endpoint_axis
   runtime/openenoc_endpoint_irq


Public contract
~~~~~~~~~~~~~~~

| Umbrella header: :download:`openenoc_endpoint.h <../../sw/lib/hal/openenoc_endpoint.h>`

The runtime API follows the principle that existing function names, prototypes,
HAL-owned data layouts, and behavior remain stable across compatible RDL changes.
New functionality uses additive interfaces. Each group has a public
header and implementation. ``openenoc_endpoint.h`` includes the group headers;
``openenoc_endpoint_common.h`` includes the selected PeakRDL ``csr.h``.

Public function declarations use conditional ``extern "C"`` linkage in C++.
C++ applications can include the group headers directly and link with the
library sources compiled as C, using the same function names and prototypes.

The endpoint argument is the mapped ``csr__endpoint_interface_t`` pointer.
Mutating operations take ``volatile csr__endpoint_interface_t *``; read-only
queries take ``const volatile csr__endpoint_interface_t *``. The pointer is
required and word-aligned, except when explicitly unbinding IRQ callbacks. The
mapping, callbacks and context must remain valid while in use. Concurrent access
to the same command registers requires caller serialization.

``openenoc_endpoint_init`` validates that the endpoint pointer is non-null and
aligned to four bytes. It performs no MMIO access.
``openenoc_endpoint_get_info`` returns the generated dimensions, capabilities and
limits without MMIO. Feature-dependent functions check the generated
``CSR__HAS_*`` constants before validating arguments or touching registers. An
absent feature returns ``UNSUPPORTED`` immediately, except that explicit IRQ
unbinding remains available. Register operations access generated ``.f`` fields
directly through the endpoint pointer, without register-pointer lookup helpers.

Integration supplies the mapped ``openenoc_endpoint_interface`` subtree. HAL
accesses its generated ``.f`` fields directly and uses no manually computed MMIO
offsets, additional offset generator, root CSR type, switch block or
endpoint-specific base address. CSR values and address calculations use at most
32 bits; MAC values use lower 32-bit and upper 16-bit fields.

The generated register type follows the RDL layout. Integration must supply
hardware matching the selected generated header. Rebuild HAL with the matching
header after a layout change. The RMEM getter returns a 32-bit pointer to the first generated
``rmem.word`` element; the implementation verifies alignment and stride.
The software build requires explicit ``APP`` and ``EP`` selections;
``PLATFORM`` selects the CPU support implementation.

For functions returning ``openenoc_endpoint_status_t``, the abbreviated status
names below have the ``OPENENOC_ENDPOINT_STATUS_`` prefix. A successful command
submission is separate from hardware acceptance and completion.

.. list-table:: Local call-result values
   :class: documentation-table
   :header-rows: 1
   :widths: 30 70

   * - Status
     - Meaning
   * - ``OK``
     - The local call succeeded; submitted work may still be pending.
   * - ``NOT_READY``
     - Active work or pending commands prevent submission, no beat or claim is
       available, or the stream handshake is pending.
   * - ``INVALID_ARGUMENT``
     - A required pointer, its alignment, an enum, or a value is invalid.
   * - ``OUT_OF_RANGE``
     - An index, address range, length, or configured size exceeds its bounds.
   * - ``UNSUPPORTED``
     - The requested feature is absent from the selected generated specification.
   * - ``HARDWARE_MISMATCH``
     - Reserved for type stability; no current function returns this value.

.. index::
   single: DMA error state

Hardware errors use the separate ``openenoc_endpoint_error_t`` type. DMA error
state is sticky: new requests and successful completions preserve it. Explicit
error clearing is separate from IRQ claim completion. Peer error state is shared
by peer DMA, RMEM, and failures while servicing incoming requests, so it is not a
per-operation result. Concurrent failures may replace its code. Failed transfers
may leave memory partially updated.

The RMEM region is one contiguous window exposed as a volatile pointer. Peer
mapping selects the oETP transaction in hardware. Direct accesses are blocking
MMIO with an ACK-only failure boundary; all-ones read data is not a unique failure
indicator. Device-memory mapping, supported access widths, memory ordering, and
DMA coherency follow the target platform's requirements. The current CSR bus
supports aligned 32-bit accesses.

Public data types
~~~~~~~~~~~~~~~~~

.. index::
   single: csr__endpoint_interface_t

.. list-table:: Runtime type semantics
   :class: documentation-table
   :header-rows: 1
   :widths: 44 56

   * - Type
     - Meaning
   * - ``csr__endpoint_interface_t``
     - Generated endpoint-interface register type; passed as a mapped pointer.
   * - ``openenoc_endpoint_mac_t``
     - Six MAC octets in network address order.
   * - ``openenoc_endpoint_info_t``
     - Peer count, RMEM capacity in words, feature flags, raw-frame and peer-fragment limits in bytes.
   * - ``openenoc_endpoint_config_t``
     - MACs, receive policy, response timeouts in endpoint cycles, and written fragment size in bytes.
   * - ``openenoc_endpoint_peer_config_t``
     - Peer MAC, byte RMEM offset, 32-bit local/remote bus addresses, byte size, mode, and IRQ enable.
   * - ``openenoc_endpoint_peer_status_t``
     - Pending request/clear, local DMA idle/done, and shared sticky error/code.
   * - ``openenoc_endpoint_non_oetp_dma_status_t``
     - Pending commands, idle/armed/done, sticky error/code, and transferred or received byte count.
   * - ``openenoc_endpoint_rmem_region_t``
     - Mapped ``volatile uint32_t *words`` and capacity ``word_count``.
   * - ``openenoc_endpoint_irq_claim_t``
     - Event source, peer index, and sequence identifying the current claim.
   * - ``openenoc_endpoint_irq_config_t``
     - Global output enable and six independent event enables.
   * - ``openenoc_endpoint_irq_status_t``
     - Pending/full/errors/output state and saturated FIFO/reservation counts.
   * - ``openenoc_endpoint_irq_callbacks_t``
     - Six named source callbacks, optional error callback, and opaque application context.

The exact declarations and enum values are included from the common header
below and the group headers on their respective library pages.

Initialization and information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Header: :download:`openenoc_endpoint_common.h <../../sw/lib/hal/openenoc_endpoint_common.h>`
| Implementation: :download:`openenoc_endpoint_common.c <../../sw/lib/hal/openenoc_endpoint_common.c>`

.. c:function:: openenoc_endpoint_status_t openenoc_endpoint_init(volatile csr__endpoint_interface_t *endpoint)

   Validate the endpoint pointer and its alignment.

   :param endpoint: In; required mapped, word-aligned generated endpoint-interface pointer.
   :returns: ``OK`` for a non-null pointer aligned to four bytes; ``INVALID_ARGUMENT`` otherwise.
   :Preconditions: Integration supplies the mapped endpoint-interface subtree and hardware matching the selected generated header.
   :Side effects: None. Performs no MMIO access, allocation or state initialization.

.. c:function:: openenoc_endpoint_status_t openenoc_endpoint_get_info(const volatile csr__endpoint_interface_t *endpoint, openenoc_endpoint_info_t *info)

   Return dimensions, capabilities and limits from the generated specification.

   :param endpoint: In; required mapped, word-aligned endpoint-interface pointer.
   :param info: Out; required generated-information destination.
   :returns: ``OK``; ``INVALID_ARGUMENT`` for a null or unaligned endpoint pointer or missing output.
   :Preconditions: Integration supplies hardware matching the selected generated header.
   :Side effects: Writes metadata from generated constants to the output; performs no MMIO access.

Public declarations
~~~~~~~~~~~~~~~~~~~

The maintained common header below provides the exact shared type and enum
definitions. Group-specific declarations are included on the library pages.

.. index::
   single: openenoc_endpoint_status_t
   single: openenoc_endpoint_error_t
   single: openenoc_endpoint_mac_t
   single: openenoc_endpoint_info_t
   single: OPENENOC_ENDPOINT_STATUS_OK
   single: OPENENOC_ENDPOINT_STATUS_NOT_READY
   single: OPENENOC_ENDPOINT_STATUS_INVALID_ARGUMENT
   single: OPENENOC_ENDPOINT_STATUS_OUT_OF_RANGE
   single: OPENENOC_ENDPOINT_STATUS_UNSUPPORTED
   single: OPENENOC_ENDPOINT_STATUS_HARDWARE_MISMATCH

.. literalinclude:: ../../sw/lib/hal/openenoc_endpoint_common.h
   :language: c
   :caption: Endpoint common runtime types and declarations
   :start-at: typedef enum {
   :end-before: /* Shared implementation helpers
   :linenos:

.. _runtime-switch-api:

Switch API
----------

HAL libraries
~~~~~~~~~~~~~

The switch API contains common initialization and information queries,
configuration and pause control, and forwarding-table access. Each group has a
public header and implementation. The common contract and types are specified
here; the group pages describe each function's arguments and effects.

.. toctree::
   :maxdepth: 3

   runtime/openenoc_switch_config
   runtime/openenoc_switch_table

Public contract
~~~~~~~~~~~~~~~

| Umbrella header: :download:`openenoc_switch.h <../../sw/lib/hal/openenoc_switch.h>`

``openenoc_switch_common.h`` includes the selected generated ``csr.h``.
Public declarations provide conditional ``extern "C"`` linkage for C++ callers;
the implementations are compiled as C. Existing function names, prototypes,
HAL-owned types and behavior follow the same compatibility contract as the
endpoint API.

The switch argument is the mapped ``csr__switch_interface_t`` subtree. Mutating
operations take ``volatile csr__switch_interface_t *``; read-only operations
take ``const volatile csr__switch_interface_t *``. It must be non-null and
aligned to four bytes. Integration supplies hardware matching the selected
generated header and keeps the mapping valid while the API is in use. Register
operations access generated ``.f`` fields directly. MAC addresses use lower
32-bit and upper 16-bit fields; no software register offsets or root CSR pointer
are required by HAL.

``openenoc_switch_init`` only validates the pointer. It does not reset the
switch or alter its mode, pause request, default bitmap, or forwarding table.
``openenoc_switch_get_info`` returns ``CSR__NUM_OF_INTERFACES`` and
``CSR__TABLE_DEPTH`` from the selected generated header. Neither function
performs MMIO or verifies that live hardware matches the header.

The caller serializes all accesses to the same switch and keeps its mode and
pause state stable throughout a data access. Device-memory mapping and MMIO
ordering follow the target platform's requirements. Output arguments are
updated only when a getter returns ``OK``.

Pause and access rules
~~~~~~~~~~~~~~~~~~~~~~

.. index::
   single: pause_request
   single: pause_done

A completed pause requires both ``forwarding_control.pause_request`` and
``forwarding_control.pause_done`` to be set. A stale ``pause_done`` after resume
is not sufficient. The pause request is a level held until an explicit
``openenoc_switch_resume`` call. ``openenoc_switch_request_pause`` and
``openenoc_switch_resume`` are idempotent and do not wait for hardware progress.
Status and mode queries remain available during forwarding and pause transitions.

.. list-table:: Switch access requirements
   :class: documentation-table
   :header-rows: 1
   :widths: 42 24 34

   * - Operation
     - Required mode
     - Pause requirement
   * - Initialization and information
     - Either
     - None; no MMIO
   * - Mode and forwarding-status queries
     - Either
     - None
   * - Request pause or resume
     - Either
     - None
   * - Set operation mode
     - Either
     - Completed pause
   * - Read default bitmap or table entry
     - Either
     - Completed pause
   * - Write default bitmap, entry, enable state, or clear table
     - Managed
     - Completed pause

Default-bitmap and table operations preserve both operation mode and pause
request. A caller changes them only through the dedicated control functions.
For a safe update, request pause, poll status until both pause fields are set,
explicitly select managed mode, perform the desired writes, select any desired
final mode while still paused, and resume. The pause establishes a safe state
for forwarding-table access; already routed frames may remain in egress queues.

Arguments are validated before state-dependent MMIO checks or writes. For valid
write arguments, unmanaged mode returns ``NOT_ALLOWED`` before pause readiness
is checked. A managed write or any data read without a completed pause returns
``NOT_READY``. Returning an error does not modify switch configuration or caller
output destinations.

For ``openenoc_switch_status_t``, abbreviated values below use the
``OPENENOC_SWITCH_STATUS_`` prefix.

.. list-table:: Switch local call-result values
   :class: documentation-table
   :header-rows: 1
   :widths: 26 12 62

   * - Status
     - Value
     - Meaning
   * - ``OK``
     - 0
     - The local call succeeded. Pause or resume may still be propagating in hardware.
   * - ``NOT_READY``
     - 2
     - A data access or operation-mode change requires a completed pause.
   * - ``INVALID_ARGUMENT``
     - 3
     - The switch pointer, its alignment, a required argument, or a mode enum is invalid.
   * - ``OUT_OF_RANGE``
     - 4
     - A table index or destination bitmap exceeds the generated dimensions.
   * - ``UNSUPPORTED``
     - 5
     - Reserved for compatibility with endpoint statuses; currently not returned.
   * - ``HARDWARE_MISMATCH``
     - 6
     - Reserved for compatibility with endpoint statuses; currently not returned.
   * - ``NOT_ALLOWED``
     - 7
     - A data write was attempted in unmanaged mode.

Public data types
~~~~~~~~~~~~~~~~~

.. index::
   single: csr__switch_interface_t

.. list-table:: Switch runtime type semantics
   :class: documentation-table
   :header-rows: 1
   :widths: 44 56

   * - Type
     - Meaning
   * - ``csr__switch_interface_t``
     - Generated switch-interface register type; passed as a mapped subtree pointer.
   * - ``openenoc_switch_status_t``
     - Local call result, separate from forwarding state.
   * - ``openenoc_switch_mac_t``
     - Six destination-MAC octets in network address order.
   * - ``openenoc_switch_info_t``
     - Generated interface count and forwarding-table entry count.
   * - ``openenoc_switch_operation_mode_t``
     - ``OPENENOC_SWITCH_UNMANAGED`` (0) or ``OPENENOC_SWITCH_MANAGED`` (1).
   * - ``openenoc_switch_forwarding_status_t``
     - Current pause-request and pause-done fields; both are required for data access.
   * - ``openenoc_switch_table_entry_t``
     - Destination MAC, 32-bit output-interface bitmap, and entry enable state.

Bitmap bits follow the RDL interface order: bit ``interface_count - 1`` selects
the first interface and bit zero selects the last. Bits above the implemented
interface count must be zero. An empty bitmap is valid: it drops unmatched
frames when used as the default, or matching frames when used in an enabled
entry. A disabled entry is ignored by lookup. Multicast and broadcast MAC keys
are valid forwarding-table destinations.

Initialization and information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Header: :download:`openenoc_switch_common.h <../../sw/lib/hal/openenoc_switch_common.h>`
| Implementation: :download:`openenoc_switch_common.c <../../sw/lib/hal/openenoc_switch_common.c>`

.. c:function:: openenoc_switch_status_t openenoc_switch_init(volatile csr__switch_interface_t *switch_interface)

   Validate the switch pointer and its alignment.

   :param switch_interface: In; required mapped, word-aligned generated switch-interface pointer.
   :returns: ``OK`` for a non-null pointer aligned to four bytes; ``INVALID_ARGUMENT`` otherwise.
   :Preconditions: Integration supplies the mapped switch subtree and hardware matching the selected generated header.
   :Side effects: None. Performs no MMIO, allocation, or switch initialization writes.

.. c:function:: openenoc_switch_status_t openenoc_switch_get_info(const volatile csr__switch_interface_t *switch_interface, openenoc_switch_info_t *info)

   Return the switch dimensions from the generated specification.

   :param switch_interface: In; required mapped, word-aligned switch-interface pointer.
   :param info: Out; required destination for ``interface_count`` and ``table_depth``.
   :returns: ``OK``; ``INVALID_ARGUMENT`` for a null or unaligned switch pointer or missing output.
   :Side effects: Writes generated dimensions into the output; performs no MMIO and preserves switch state.

Public declarations
~~~~~~~~~~~~~~~~~~~

The maintained common header provides the exact public status values, common
types, and declarations. Group-specific types appear on their library pages.

.. index::
   single: openenoc_switch_status_t
   single: openenoc_switch_mac_t
   single: openenoc_switch_info_t
   single: OPENENOC_SWITCH_STATUS_OK
   single: OPENENOC_SWITCH_STATUS_NOT_READY
   single: OPENENOC_SWITCH_STATUS_INVALID_ARGUMENT
   single: OPENENOC_SWITCH_STATUS_OUT_OF_RANGE
   single: OPENENOC_SWITCH_STATUS_UNSUPPORTED
   single: OPENENOC_SWITCH_STATUS_HARDWARE_MISMATCH
   single: OPENENOC_SWITCH_STATUS_NOT_ALLOWED

.. literalinclude:: ../../sw/lib/hal/openenoc_switch_common.h
   :language: c
   :caption: Switch common runtime types and declarations
   :start-at: typedef enum {
   :end-before: #ifdef OPENENOC_SWITCH_IMPLEMENTATION
   :linenos:

.. _runtime-assertions:

Runtime assertions
------------------

.. index::
   single: Runtime assertions

| Header: :download:`assert.h <../../sw/lib/utils/assert.h>`
| Implementation: :download:`assert.c <../../sw/lib/utils/assert.c>`

These utilities are shared by endpoint and switch applications.

.. index::
   single: NDEBUG
   single: static_assert

The shared ``assert.h`` provides runtime assertions alongside the generated
header's C11 ``static_assert`` compatibility definition. Defining ``NDEBUG``
disables runtime assertions: the macro expands to ``((void)0)`` without evaluating
its argument. Calls and other required side effects must execute before an
assertion checks their results. Compile-time assertions remain enabled.

.. c:macro:: assert(expression)

   :param expression: Scalar condition; evaluated exactly once when ``NDEBUG`` is absent.
      Not evaluated when ``NDEBUG`` is defined.
   :returns: A void expression when disabled or when the condition is true.
      An enabled false condition never returns.
   :Side effects: An enabled failure passes ``__FILE__`` and ``__LINE__`` to
      ``openenoc_assert_fail``, which records diagnostics and traps the CPU.
      A disabled assertion has no side effects and generates no runtime operation.

.. c:function:: void openenoc_assert_fail(const char *file, uint32_t line)

   :param file: In; pointer to the source filename, normally the ``__FILE__`` string literal.
   :param line: In; source line number, normally ``__LINE__``.
   :returns: Never returns.
   :Side effects: Writes ``failure_file`` and ``failure_line`` into
      ``_openenoc_assert_status``, publishes ``OPENENOC_ASSERT_STATUS_FAILED``,
      then executes ``__builtin_trap()``. Completed coverage remains available.

.. index::
   single: openenoc_assert_status_t
   single: _openenoc_assert_status

``openenoc_assert_status_t`` and the volatile instance
``_openenoc_assert_status`` are declared in ``assert.h``. Its conditional
definition is enabled only by ``assert.c`` through
``OPENENOC_ASSERT_IMPLEMENTATION``; other translation units receive an extern
declaration. The instance is initialized to zero in
``.data._openenoc_assert_status``, which the PicoRV32 linker retains at the start
of DMEM. Applications write completed coverage and successful completion; the
failure handler writes diagnostics and the failure status before trapping.

.. index::
   single: completed_checks
   single: OPENENOC_ASSERT_STATUS_PASSED
   single: OPENENOC_ASSERT_STATUS_FAILED

.. list-table:: Assertion status fields
   :class: documentation-table
   :header-rows: 1
   :widths: 25 25 50

   * - Field
     - Type
     - Meaning
   * - ``status``
     - ``uint32_t``
     - Zero before a result; ``OPENENOC_ASSERT_STATUS_PASSED`` (``0x600d600d``)
       after success, or ``OPENENOC_ASSERT_STATUS_FAILED`` (``0xbad0bad0``) on failure.
   * - ``completed_checks``
     - ``uint32_t``
     - Application-defined bitmask of successfully completed test groups.
   * - ``failure_line``
     - ``uint32_t``
     - Failing source line; zero before failure.
   * - ``failure_file``
     - ``const char *``
     - Pointer to the failing source filename; null before failure.

Contract verification
---------------------

``sw/apps/endpoint_test/main.c`` implements capability-dependent endpoint
API and transfer checks. The ``dv/endpoints/openenoc_endpoint_full/`` suite
checks frames, memory, DMA and IRQ claims against RTL. Broader
hardware/software verification is documented in :doc:`verification`.
