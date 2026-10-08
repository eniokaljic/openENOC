<!-- SPDX-FileCopyrightText: 2026 Enio Kaljic -->
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# openENOC oETP Engine Test Suite

## Overview

This cocotb suite verifies the oETP engine independently of memory, CSR, and
IRQ implementations. The wrapper supplies Ethernet/memory streams, transaction
channels, and a registered peer-lookup fixture. Fifteen cases run at local/
Ethernet widths 32/32, 64/8, and 32/64. Counter-wrap and response-at-expiry
checks use public VPI registers; normal traffic uses the module interfaces.

Component architecture and operation are described in the
[RTL Reference](../../../docs/src/rtl/openenoc_endpoint_oetp_engine.rst).

## Test Coverage

The suite covers:

- all nine commands, Ethernet octet order, little-endian parameters, scalar
  data, and BitEnable;
- DMA lengths 1, 3, 4, 5, and 8160 bytes, word rounding, exact memory bytes,
  and marker placement;
- full-width ERROR_RSP validation and local/remote error mapping;
- streaming before terminal memory status, early/late source failures, and
  draining before reuse;
- RX truncation, missing/bad trailers, excess data, MAC padding, and errors
  after memory TLAST;
- unicast/multicast writes, multicast read rejection, local completion, and
  response suppression;
- raw receive modes, wrong magic, unknown peers/commands, and one-time
  descriptor claims;
- independent initiator/responder roles, equal metadata, reply priority, and
  busy-responder draining;
- Ethernet-TLAST timeout start, snapshots, disabled timeout, late replies,
  abort, and expiry precedence;
- backpressure, hard reset, Request ID wrap, and registered output stability
  between clock edges.

## Running Tests

Run the full pytest parameter sweep:

```bash
./run_tests.sh pytest
```

Run the default configuration and generate an FST waveform:

```bash
./run_tests.sh waves
```

Remove generated simulation artifacts:

```bash
./run_tests.sh clean
```
