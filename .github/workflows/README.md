<!-- SPDX-FileCopyrightText: 2026 Kerim Bavcic -->
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# GitHub Actions Workflows

| Workflow | Trigger | Description |
| --- | --- | --- |
| [`docs.yml`](docs.yml) | Push to `main` or `dev/documentation`, manual | Builds the Sphinx documentation in `docs/` and deploys it to GitHub Pages. |
| [`dv-sim.yml`](dv-sim.yml) | Every push | Runs the simulation regression of all test suites under `dv/` (core, endpoints, HAL, traffic, and ISS). Each suite runs as a separate job. |
| [`self-hosted-smoke.yml`](self-hosted-smoke.yml) | Manual, push that changes the workflow | Runs one `dv/core` suite on the self-hosted runner to check that the runner and its preinstalled tools work. |

## DV Simulation Regression

`dv-sim.yml` discovers the test suites automatically, so a new suite
directory under `dv/` is picked up without changing the workflow. The
`DV result` job passes only when every suite passes; use it as the required
status check for merging into `main`.

Tool versions are pinned: the OSS CAD Suite release (Verilator) in the
workflow, the Python packages in `dv/requirements.txt` and
`hal/requirements.txt`, and Spike through the `libs/riscv-isa-sim` submodule
and `dv/iss/compatibility.json`. OSS CAD Suite and the Spike build are
cached, so they are downloaded or built only when their pinned version
changes.

Test reports of each suite are uploaded as workflow artifacts and kept for
14 days.

## Self-Hosted Runner

The self-hosted runner is a VM on the lab server, used for synthesis,
bitstream generation, and hardware smoke tests. Jobs select it with
`runs-on: [self-hosted, Linux, X64]`. Tools are installed on the VM once
instead of in the workflow:

- System packages: `git curl ca-certificates build-essential python3-dev python3-venv`
- OSS CAD Suite (same release as `dv-sim.yml`) in `~/tools/oss-cad-suite` of the runner user (`/home/openenoc/tools/oss-cad-suite`)

`self-hosted-smoke.yml` checks the runner setup. Start it from the Actions
tab (*Run workflow*) once it is on the default branch, or push a change to
the workflow file.
