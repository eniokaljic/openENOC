<!-- SPDX-FileCopyrightText: 2026 Enio Kaljic -->
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# endpoint_test Firmware

`endpoint_test` exercises the endpoint HAL through configuration, peer mappings,
direct RMEM accesses, AXIS, raw DMA, peer DMA and IRQ. It expects Ethernet TX to
be looped back to RX. The same application source builds against the selected
endpoint's generated headers and includes checks for that endpoint's supported
features.

General build configuration is described in the [software README](../../README.md).

## Feature Selection and Coverage

Initialization validates the endpoint pointer and its four-byte alignment without
MMIO access. The information API returns dimensions, frame limit and capability
values from generated constants. Integration must supply hardware matching the
selected generated header. Optional checks follow its feature flags; the 66-byte
AXIS and raw-DMA fixtures are skipped when the generated frame limit is smaller.
Successful groups set bits in `completed_checks`.

| Bit | Mask | Completed group |
| --- | --- | --- |
| 0 | `0x01` | Endpoint information and configuration |
| 1 | `0x02` | Peer configuration and shared error clearing |
| 2 | `0x04` | Direct RMEM loopback and response timeout |
| 3 | `0x08` | AXIS stream loopback, unaligned buffers and overflow drain |
| 4 | `0x10` | Non-oETP TX/RX DMA |
| 5 | `0x20` | Peer DMA timeout and available push/pull checks |
| 6 | `0x40` | IRQ handling and final controller state |

The default full endpoint completes all groups and reports `0x7f`. A skipped
group leaves its bit clear. Peer push/pull loopback requires at least two peer
entries; with one entry the peer-DMA group still exercises its timeout path.

## Tests

Each case has a descriptive `test_*` function in `main.c`. `run_tests` selects
available cases through the generated capability constants and combines their
coverage. HAL calls execute first and their saved results are checked with the
shared `assert`. When `NDEBUG` is absent, assertions evaluate their expressions
once; failure records the source file and line, publishes failure and traps the
CPU. With `NDEBUG`, assertions become `((void)0)` and their expressions are not
evaluated. HAL calls and transfers still execute. Test functions return `void`.
Saved results used only by assertions are marked unused for warning-free builds
in either mode. The software build defaults to `DEBUG=0`; select enabled
assertions with `DEBUG=1`. Full endpoint DV builds this application with
`DEBUG=1` automatically before simulation.

- **Configuration:** generated information fields and configuration readback, unicast/multicast MAC
  validation, receive policy, supported response timeouts, and fragment-limit
  rounding and bounds.
- **Peers:** disabled mapping readback, idle and pending state, out-of-range peer
  rejection, and acknowledged clearing of the shared sticky error record.
- **RMEM:** a transparent self mapping into DMEM, direct pointer writes and reads,
  then a missing-destination timeout. The failed read returns all ones and
  records the peer timeout; an enabled RMEM error event is checked separately.
- **Direct AXIS:** three 66-byte loopback frames sent and received exclusively
  through `axis_send_stream` and `axis_receive_stream`. Separate tests cover aligned
  buffers, unaligned byte buffers, and a 65-byte RX buffer. The overflow test checks
  `OUT_OF_RANGE`, the full 66-byte count, the stored prefix and boundary canaries,
  and draining through TLAST. RTL DV checks payload, TKEEP and TLAST for every beat.
- **Raw DMA:** arm a 66-byte RX buffer, reject rearming while busy, transmit the
  frame, compare received bytes and completion counts, and clear TX/RX errors
  independently. A zero-length TX request is rejected.
- **Peer DMA:** request a transfer to a missing destination and check timeout,
  completion state and explicit error clearing. With two peer entries, configure
  complementary mirror modes and push, then pull, a 12-byte block in three
  four-byte fragments each.
- **IRQ:** bind the six named source callbacks, enable available events, check an
  initially empty claim and blocking completion, clear errors through hardware
  acknowledgement while preserving global enable, observe expected notifications, and
  finish with no pending claims, reservations, overflow or invalid completion.

## IRQ and Stream Ownership

Callbacks receive the generated endpoint-interface pointer and a const claim. HAL submits claim
completion after each callback returns. The RX callback receives the entire frame
with `axis_receive_stream`; TX/DMA/error callbacks record their events.

The firmware masks CPU IRQs while submitting each direct AXIS frame and unmasks
after its final beat has been submitted. Enabled endpoint events remain queued
during that interval. This keeps the blocking RX callback from preempting TX work
needed to finish its loopback frame. On endpoints without IRQ, RX is polled.

## Result Report

The volatile `_openenoc_assert_status` is declared and instantiated through
`sw/lib/utils/assert.h`; `assert.c` enables its single definition. The PicoRV32
linker places `.data._openenoc_assert_status` at the start of DMEM. The application
updates coverage and publishes success; the shared assertion handler publishes
failure before executing `__builtin_trap()`.

| DMEM word | Field | Meaning |
| --- | --- | --- |
| 0 | `status` | Final result, initially zero |
| 1 | `completed_checks` | Bitmask of successfully completed groups |
| 2 | `failure_line` | Failing `assert` source line, or zero |
| 3 | `failure_file` | Pointer to the failing source filename in IMEM, or null |

| Status | Meaning |
| --- | --- |
| `0x00000000` | No final result has been published |
| `0x600d600d` | Selected groups completed; enabled assertions passed |
| `0xbad0bad0` | An assertion failed; inspect coverage, `failure_file` and `failure_line` |

The [full endpoint suite](../../../dv/endpoints/openenoc_endpoint_full/README.md)
checks this report along with transport data, master activity and IRQ completion.
