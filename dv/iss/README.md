<!-- SPDX-FileCopyrightText: 2026 Kerim Bavcic -->
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# openENOC ISS Co-Verification

This directory contains the host-side infrastructure for executing RISC-V
firmware with Spike while endpoint hardware is simulated with cocotb and
Verilator.

Spike is embedded through its `processor_t` and `simif_t` APIs and hidden
behind a versioned C ABI in `include/openenoc_iss.h`. Each endpoint handle owns
one RV32I+Zicsr hart and one native worker thread. A worker publishes external data
accesses through a single request slot and waits while Python/cocotb services
the corresponding AXI4-Lite transaction. The cocotb simulator thread remains
free to advance RTL and service other endpoints.

The integration runs the existing, unchanged `csr_smoke` C application on Spike
while the endpoint crossbar, DMEM, generated CSR block, endpoint logic, and
AXIS loopback remain RTL simulated by Verilator. Its `PLATFORM=iss` firmware
uses standard M-mode CSRs and `mret`, so its ELF is different from the
PicoRV32 ELF, which uses PicoRV32-specific IRQ instructions. A dedicated `iss_startup`
firmware also qualifies the platform's data initialization, BSS clearing,
read-only data, and stack behavior.

Memory ranges come from the endpoint's RDL-generated
`build/hal/<endpoint>/sw/memory_map.h`. `HAL_EP` selects the default map for
ISS commands (`openenoc_endpoint_full` by default). The C ABI passes IMEM,
DMEM, and CSR ranges per endpoint handle; Python callers may pass a distinct
`memory_map=load_memory_map(path)` to `create_endpoint` and `load_elf` for each
instance. Native tests qualify two different maps in one process. The existing
RTL test top and firmware targets still instantiate/build
`openenoc_endpoint_full`; mixed RTL endpoint types require a corresponding
test top, RTL source selection, and firmware build for each type.

## Prerequisites

On Ubuntu, install the upstream Spike and bare-metal firmware build
dependencies:

```bash
sudo apt-get install \
	device-tree-compiler libboost-regex-dev libboost-system-dev \
	gcc-riscv64-unknown-elf binutils-riscv64-unknown-elf
```

Initialize the submodule after cloning the repository:

```bash
git submodule update --init libs/riscv-isa-sim
```

The RTL tests use the repository Python environment and OSS CAD Suite. Activate
them in this order before running an RTL target:

```bash
source /path/to/oss-cad-suite/environment
source venv/bin/activate
pip install -r dv/requirements.txt
```

## Build And Check

From the repository root, run:

```bash
make -C dv/iss check
```

This performs Spike's upstream out-of-tree `configure`, `make`, and `make
install` flow without installing anything globally. It then runs the C++ API,
C ABI, threaded request-channel, and Python `ctypes` smoke tests. Individual
targets include:

```bash
make -C dv/iss processor-smoke
make -C dv/iss c-api-smoke
make -C dv/iss python-smoke
make -C dv/iss elf-smoke
```

Qualify the native worker and pinned Spike library for data races with a
separate ThreadSanitizer build:

```bash
make -C dv/iss tsan-smoke JOBS=4
```

The sanitizer target is intentionally not part of `check-all`: it rebuilds
Spike with instrumentation and requires a compiler-provided `libtsan` runtime.

Run the short Spike-to-RTL DMEM test with:

```bash
make -C dv/iss rtl-smoke
```

Exercise byte/halfword lanes and signed loads against RTL DMEM, and qualify
invalid requests, AXI errors, and blocked transactions with a deterministic
AXI responder:

```bash
make -C dv/iss rtl-lanes-smoke
make -C dv/iss rtl-bridge-smoke
```

Qualify coordinated stop and whole-top reset while AW/W, B, or R is blocked:

```bash
make -C dv/iss rtl-lifecycle-smoke
```

The cocotb harness resets the RTL and BFM together. For an accepted write
waiting on B, it first stops the worker and cancels the AXI service. For
blocked AW/W or R, a reset-flushed BFM operation explicitly stops the worker
instead of completing its MMIO request. A write accepted before reset remains
in RTL DMEM; an incomplete write does not. Each test restarts Spike in a new
epoch, rejecting late responses. These tests do not provide a standalone
reset API or safe replay of an in-flight transaction without coordinated bus
reset.

The bridge rejects malformed or out-of-range requests before issuing AXI.
AW, W, B, AR, and R backpressure is exercised against the real RTL endpoint;
Spike remains blocked until the final bus response. Within the supported ISS
address map the generated CSR and RAM blocks return `OKAY`, so an RTL-generated
`SLVERR`/`DECERR` cannot be triggered without changing that hardware profile.
An AXI error is returned to the ISS only after the bus operation completes;
a stalled operation times out after 10 us of simulation time and stops the
waiting worker. The error/timeout tests use a controlled responder, not an
RTL-generated `SLVERR`/`DECERR`. They do not claim CPU trap equivalence or
safe replay of an in-flight AXI write after a timeout. Reset/drain handling
for such writes belongs to the coordinated lifecycle tests.
The current `accepted_sim_tick` records submission to the AXI BFM, not the
exact AW/AR handshake; `completed_sim_tick` is recorded after its R/B response.

Build and run the unchanged `csr_smoke` C application through Spike and the
RTL endpoint with:

```bash
make -C dv/iss rtl-firmware-smoke
```

The target builds a separate `rv32i_zicsr` ELF under `build/dv/iss/irq-firmware`
and checks its own IMEM load image. The IRQ-enabled worker samples the actual
RTL CPU IRQ level as `mip.MEIP` and receives bounded instruction credit from
cocotb (initially 32 steps per sampled clock, not 32 PicoRV32 cycles). After
each AXI R/B response, the bridge publishes the stable IRQ level before
releasing the blocked Spike instruction. The test verifies trap entry/return,
both CSR claim completion tokens, high/low IRQ level, and the 17-beat frame
(66 valid bytes), including the last `TKEEP` and `TLAST`.

Run two independent IRQ-enabled `csr_smoke` instances with a separate RTL
Ethernet loopback for each endpoint:

```bash
make -C dv/iss rtl-irq-system-smoke JOBS=2
```

The dual IRQ target uses its own Verilator build directory; it does not replace
the older crossed-link `iss_link` test below.

Run two Spike contexts against separate RTL endpoints with directly crossed
Ethernet streams:

```bash
make -C dv/iss rtl-system-smoke
```

Both contexts execute the `iss_link` ELF independently, with roles selected
through their private RTL CSR blocks. The initiator sends a request; the
responder receives it before sending a distinct reply. Both frames carry a
broadcast Ethernet header, so the endpoint's default filtered non-oETP receive
policy admits them without disabling MAC filtering. Firmware validates the
header and payload; the test checks every transferred beat. The test holds
endpoint 0's AXI read address channel while endpoint 1 progresses, then
checks both physical stream directions, status words, received payloads and
isolated DMEM markers. No instruction-by-instruction host barrier is used.
The test uses a shared reset and a separate Verilator build directory from
one-endpoint tests. A separate case stops one worker in a local loop while
the other completes pending RTL MMIO without a shared reset. A six-beat request
also tests stopping its initiator after the header and first payload word,
before `TLAST`: the responder
remains active until coordinated stop, then a shared RTL/BFM reset discards the
partial frame before both workers restart and complete a fresh exchange.
Firmware tasks are cancelled and awaited before their endpoint handles close.
An AXI response that arrives after the worker stops is not applied to Spike,
including a stop racing the native completion call.
Continuing an interrupted frame without resetting both endpoints is not
supported.

Qualify the real bare-metal startup path with initialized data, dirty BSS, and
stack traffic through RTL DMEM:

```bash
make -C dv/iss rtl-startup-smoke
```

Run every native, Python, and RTL check with:

```bash
make -C dv/iss check-all
```

The old payload-only `iss_link` frames were rejected by the endpoint's new
default MAC filter after the RTL update. Adding the Ethernet header restores
the crossed request/reply and mid-frame recovery checks; local loopback is
still used only by the separate IRQ-enabled `csr_smoke` target. A successful
`check-all` manifest, not an individual smoke result, is the aggregate gate.

Each successful run writes per-target JUnit XML and a validated JSON manifest
under `build/dv/iss/reports`. The manifest records the repository and pinned
Spike commits, whether tracked source files are modified, the ISS library and
firmware SHA-256 hashes for both platform-specific `csr_smoke` ELFs,
CPU/memory/IRQ profile, tool versions, and test counts.
Missing or failing XML prevents manifest generation. `check-all` removes the
previous manifest before starting, so it cannot report a stale success.
Standalone `rtl-*` and `test-native` targets write their own JUnit files but
do not update the aggregate manifest.

To verify from a clean clone after committing, initialize the Spike submodule,
activate OSS CAD Suite and the DV Python environment as above, then run
`make -C dv/iss check-all JOBS=1`. A successful clean-clone run should have
`tracked_worktree_dirty: false` in its manifest. This workspace run does not
replace that post-commit check.

`JOBS` defaults to one to limit memory use under WSL and can be overridden
explicitly:

```bash
make -C dv/iss check JOBS=4
```

Remove all ISS build products with:

```bash
make -C dv/iss clean
```

The supported upstream commit and initial CPU profile are recorded in
`compatibility.json`. The build rejects a submodule checked out at a different
commit.

## ELF Loading

The Python loader accepts only ELF32 little-endian RISC-V executables matching
the RV32I soft-float profile and 16-byte stack ABI. It validates program-header
bounds, address overflow, segment alignment and overlap, supported memory
regions, and an executable entry point before exposing an immutable boot
image.

Only file-backed bytes from `PT_LOAD` segments are copied into private ISS
IMEM, using each segment's physical/load address (`p_paddr`). Writable data
keeps its DMEM runtime address (`p_vaddr`), so `boot.s` must copy `.data` from
IMEM to RTL DMEM. The loader does not initialize the remaining `p_memsz`
bytes, which leaves `.bss` clearing to `boot.s`. Completion addresses are read
from ELF symbols rather than fixed testbench constants.

## Current Profile

- RV32I+Zicsr, machine privilege mode, one hart per endpoint handle.
- Private 32 KiB ISS IMEM at `0x00000000`.
- RTL DMEM at `0x10000000-0x10007fff`.
- RTL CSR aperture at `0x20000000-0x20001fff`.
- The listed addresses are the current `openenoc_endpoint_full` HAL map, not
	constants in the native ISS library.
- One pending 1-, 2-, or 4-byte data request per endpoint.
- Opt-in, level-sensitive M-mode external IRQ through `mip.MEIP`; non-IRQ
  endpoint handles retain their unpaced execution behavior.
- IRQ-enabled handles receive bounded instruction credit, initially 32 steps
  per sampled RTL clock. This is not a PicoRV32 cycle model.
- No external instruction fetches.
- Validated ELF entry points, load segments, and symbols drive firmware tests.