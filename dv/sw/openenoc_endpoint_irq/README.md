<!-- SPDX-FileCopyrightText: 2026 Enio Kaljic -->
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# Endpoint IRQ HAL Host Tests

These two C tests run on the host using GNU Make, a native GCC compiler and
GNU `timeout`. They verify the [IRQ HAL](../../../sw/lib/hal/README.md#endpoint-irq-hal)
without an RTL simulator or RISC-V toolchain.

- `test_openenoc_endpoint_irq.c` links the PicoRV32 C utilities and replaces
  `irq_set_mask` with a host stub. It checks CPU masking, unbound and unexpected
  IRQ entry paths, combined error reporting and error callbacks.
- `test_openenoc_endpoint_irq_portable.c` compiles HAL without platform headers
  or sources. Test hooks use a different IRQ-state encoding to verify that HAL
  does not depend on PicoRV32 interrupt semantics.

The [full endpoint suite](../../endpoints/openenoc_endpoint_full/README.md)
covers the assembly wrapper, CSR claim completion and RX/TX callbacks against RTL.

## Running Tests

From the repository root, build and run both tests:

```bash
make -C dv/sw/openenoc_endpoint_irq
```

Activate the HAL virtual environment before invoking Make if the generated
`build/hal/openenoc_endpoint_full/sw/csr.h` header needs regeneration. Missing or
outdated headers are regenerated through `hal/Makefile`.

Each invocation rebuilds both executables. A failed assertion, compiler error or
per-test timeout of 10 seconds makes Make fail. Outputs are written to
`build/dv/sw/openenoc_endpoint_irq/` and ignored by Git.

Additional commands:

```bash
make -C dv/sw/openenoc_endpoint_irq build
make -C dv/sw/openenoc_endpoint_irq test VERBOSE=1
make -C dv/sw/openenoc_endpoint_irq clean
make -C dv/sw/openenoc_endpoint_irq help
```

`CC`, `BUILD_ROOT`, `TEST_TIMEOUT` and the usual compiler/linker flags can be
overridden on the Make command line.
