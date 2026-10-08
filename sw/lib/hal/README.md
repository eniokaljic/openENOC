<!-- SPDX-FileCopyrightText: 2026 Enio Kaljic -->
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# openENOC Endpoint HAL

The HAL library exposes endpoint CSR operations through the generated register
types for the selected endpoint. General build and platform configuration are
documented in the [software README](../../README.md).

## Endpoint AXIS HAL

[openenoc_endpoint_axis.h](openenoc_endpoint_axis.h) and
[openenoc_endpoint_axis.c](openenoc_endpoint_axis.c) provide non-blocking,
beat-level access to the endpoint CSR AXI4-Stream source and sink. Both functions
take a mapped `volatile csr__endpoint_interface__axis_if_t *axis_if`.

| Function | Purpose |
| --- | --- |
| `openenoc_endpoint_axis_send` | Submit one TX beat with `data`, `keep` and `last` through the CSR source |
| `openenoc_endpoint_axis_receive` | Read one RX beat from the CSR sink and acknowledge it after capturing its fields |

Both functions return `openenoc_endpoint_axis_status_t`:

| Status | Meaning |
| --- | --- |
| `OPENENOC_ENDPOINT_AXIS_STATUS_OK` | The TX request was submitted, or an RX beat was captured and acknowledged |
| `OPENENOC_ENDPOINT_AXIS_STATUS_NOT_READY` | The source is busy, or the sink has no available beat or an acknowledgement is still pending |

A successful send means the CSR accepted the request; AXI4-Stream transfer
completion can occur later under backpressure. Receive output arguments are
updated only on `OK`. Its `data` pointer is required; `keep` and `last` may be
null when those fields are not needed.

Frames are handled through successive calls, with `last` representing TLAST.
The same receive API can be used from polling code or an IRQ callback.

## Endpoint IRQ HAL

`sw/lib/hal/openenoc_endpoint_irq.h` and `.c` expose the endpoint interrupt
controller with CPU utilities supplied by the selected platform. All CSR
accesses use the generated register fields and a caller-provided mapped `irq`
block. The CPU IRQ entry point lives in this HAL. Its only CPU dependency is
the internal `_openenoc_endpoint_irq_*` contract declared in
`openenoc_endpoint_irq.h`.
Applications use the public `openenoc_endpoint_irq_*` API. HAL includes no
platform-specific headers or aliases. The selected `sw/platform/<platform>`
directory supplies the implementations at link time, with no endpoint CSR
access or C calls into HAL.

| Internal HAL hook | Contract |
| --- | --- |
| `_openenoc_endpoint_irq_disable_all` | Disable all CPU IRQ sources, including after return from an active IRQ |
| `_openenoc_endpoint_irq_enable_endpoint` | Enable only the endpoint CPU IRQ source and any required global CPU gate |
| `_openenoc_endpoint_irq_is_endpoint` | Report whether the opaque IRQ state includes the endpoint source |
| `_openenoc_endpoint_irq_has_unhandled_sources` | Report whether the opaque IRQ state includes unsupported sources |

Each platform defines the encoding of `cpu_irq_state`. The two classification
functions inspect it without consuming claims or changing interrupt state.
The assembly wrapper passes this value directly to the HAL entry and handles
platform interrupt-controller acknowledgement when needed.

| Function | Purpose |
| --- | --- |
| `openenoc_endpoint_irq_mask` | Mask all CPU IRQ sources through the platform utilities |
| `openenoc_endpoint_irq_unmask` | Enable only the endpoint CPU IRQ source through the platform utilities |
| `openenoc_endpoint_irq_bind` | Bind the CSR block and persistent callback descriptor to the HAL entry point |
| `openenoc_endpoint_irq_configure` | Set all six event enables and the global output enable |
| `openenoc_endpoint_irq_get_config` | Read the current enables |
| `openenoc_endpoint_irq_set_global_enable` | Gate the endpoint IRQ output without discarding claims |
| `openenoc_endpoint_irq_set_event_enable` | Enable or disable one event source; reject unknown sources |
| `openenoc_endpoint_irq_get_status` | Read pending/full/error flags and FIFO/reservation counts |
| `openenoc_endpoint_irq_clear_errors` | Clear sticky errors and wait for the maintenance command to clear |
| `openenoc_endpoint_irq_complete` | Complete the current valid claim and wait for hardware acknowledgement |
| `openenoc_endpoint_irq_handler` | CPU IRQ entry: classify the native CPU IRQ state, service the bound endpoint, and report errors |
| `openenoc_endpoint_irq_service` | Dispatch claims for an explicit CSR block and complete them; also supports polling |

The IRQ entry serves one bound endpoint. Call `openenoc_endpoint_irq_bind`
while CPU interrupts are masked and keep its callback descriptor and context
alive. Applications use the flow `main -> openenoc_endpoint_irq_* ->
_openenoc_endpoint_irq_*` to reach the CPU utilities through HAL.
Porting the CPU requires a new platform implementation, startup and context
wrapper; HAL and application callbacks keep the same API.

The [PicoRV32 platform documentation](../../platform/picorv32/README.md#picorv32-interrupts)
describes its context wrapper and CPU interrupt masking.

`openenoc_endpoint_irq_callbacks_t` provides one callback for each of the six
sources, an error callback, and an application context pointer. The service
function calls the selected callback with the IRQ register block and that
context while the claim is still stable. It completes the token only after
the callback returns. A direct RX callback can therefore receive successive
beats through TLAST. Callbacks must
not complete the claim themselves.

The `rmem_error` callback handles source 5, including RMEM timeout and remote
ERROR_RSP failures. The claim identifies the peer, and the endpoint's
`peers.entry[peer_idx].dma.error` and `.error_code` hold the shared RMEM/DMA
error record. Writing one to `.clear_error` clears that record independently
of completing the IRQ claim. RMEM and bulk DMA retain their separate IRQ sources.
Actual RMEM failure production will be implemented with the oETP engine.

Missing callbacks and unknown sources are reported as `UNHANDLED_SOURCE`; their
claims are completed so they do not block the FIFO head. The handler also
reports sticky `OVERFLOW` and `INVALID_COMPLETE` errors. Its result is a bitmask
of `OPENENOC_ENDPOINT_IRQ_RESULT_*` values. The CPU entry additionally reports
`UNHANDLED_CPU_IRQ` and `NOT_BOUND`, masking CPU interrupts in those cases.
It passes a nonzero result to `callbacks.error`; explicit service callers
receive the result directly. Hardware error flags are cleared explicitly
through `openenoc_endpoint_irq_clear_errors`.

Configuration briefly suppresses the endpoint IRQ output while updating all
event enables, then applies the requested global enable. Event enable changes
apply to future admissions and preserve existing claims and reservations.

Endpoint event capture and output assertion are separately configured through
CSR `irq.event_enable` and `irq.control.global_enable`. Software completes a
claim by copying its `peer_idx`, `source`, and `sequence` fields into
`irq.complete`, then setting `complete.valid` last. Wait for hardware to clear
`complete.valid` before assembling another completion. CPU EOI does not remove
the event.

The CPU platform supplies mask/source utilities and the assembly context
wrapper. Endpoint CSR configuration, claim handling and dispatch stay in HAL.
The host tests in `dv/sw/openenoc_endpoint_irq` check the CPU entry's unbound
and unexpected-source paths, error callbacks and CPU mask policy. A separate
test compiles HAL without any CPU platform headers or sources and supplies
the common API with a different IRQ-state encoding. The full endpoint test
checks actual claim completion and RX/TX callbacks against RTL.
