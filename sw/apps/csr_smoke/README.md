<!-- SPDX-FileCopyrightText: 2026 Enio Kaljic -->
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# csr_smoke Firmware

`csr_smoke` verifies software access to the full endpoint's CSR block and an
IRQ-driven AXI4-Stream loopback. The application sends a frame, receives it
into a DMEM buffer through IRQ callbacks, and compares the received data in
`main` after reception reaches TLAST. It expects the transmitted frame to be
returned to the endpoint RX path.

The shared [IRQ HAL API](../../lib/hal/README.md#endpoint-irq-hal) defines callback
dispatch, claim completion and the CPU platform hooks used by this application.

## CSR Checks

The application first masks CPU interrupts through the IRQ HAL, then:

- writes `0xa5a55a5a` to `test_reg.test_field` and verifies its readback;
- sets switch `operation_mode=1`, `default_forwarding.bitmap=0xa`, and
  `pause_request=1`, then verifies those values and hardware `pause_done=1`;
- checks that the endpoint reports `info.irq_supported=1`.

A failed check publishes the failure status and returns before starting the
frame transfer.

## IRQ Loopback

`main` binds a persistent callback descriptor to the endpoint IRQ block and
enables direct RX-available and direct TX-complete events, together with the
global endpoint IRQ output. CPU utilities are reached through the flow
`main -> openenoc_endpoint_irq_* -> _openenoc_endpoint_irq_*`; the application
contains no platform-specific IRQ calls or CPU masks.

The application sends 66 bytes in 17 AXI4-Stream beats using
`openenoc_endpoint_axis_send`. The first 16 beats have `TKEEP=0xf`; the final
beat has `TKEEP=0x3` and `TLAST=1`.

CPU interrupts remain masked until the final TX beat is submitted. Endpoint
events can still be captured during transmission. This ordering prevents the
blocking loopback RX callback from preempting its sender before the rest of
the frame has been submitted.

After submitting the frame, `openenoc_endpoint_irq_unmask` enables the endpoint
CPU source. The assembly wrapper enters `openenoc_endpoint_irq_handler` directly,
and HAL dispatches the application callbacks:

- `receive_axis_frame` receives successive beats into DMEM using
  `openenoc_endpoint_axis_receive`. It waits through any gaps before TLAST,
  stores payload, TKEEP and TLAST, and publishes RX completion after TLAST.
- `notify_tx_complete` publishes TX completion.
- `notify_irq_error` records an IRQ handling error.

HAL completes each claim after its callback returns. `main` waits for RX and
TX completion or an IRQ error, masks CPU interrupts, and disables the endpoint
IRQ output. It checks the buffered words, beat count, byte count, TKEEP and
TLAST before publishing the result.

## Completion Status

The application publishes its result in the volatile `csr_smoke_status` word
at the beginning of DMEM.

| Value | Meaning |
| --- | --- |
| `0x00000000` | Application has not published a result |
| `0x600d600d` | CSR checks and frame comparison passed |
| `0xbad0bad0` | A CSR check, IRQ operation or frame comparison failed |

The existing 66-byte raw loopback fixture starts with a broadcast destination
and unicast source prefix so it passes the default filtered receive policy.
Its transfer count, IRQ flow, and function coverage are unchanged.
