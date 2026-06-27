<!-- SPDX-FileCopyrightText: 2026 Enio Kaljic -->
<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->

# openENOC HAL CSR Generation

This directory contains a Makefile for generating openENOC HAL CSR artifacts from the SystemRDL specifications located under `src/`.

The build covers three CSR descriptions:

* `openenoc_csr`
* `openenoc_switch`
* `openenoc_endpoint`

## Requirements

Create and activate a Python virtual environment, then install the required Python packages:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

The required packages are PeakRDL and the exporters used for Markdown and Python model generation.

## Running the Build

Run the Makefile from the directory that contains it:

```bash
make
```

This generates the HAL CSR artifacts in the build and documentation directories, including:

* C header file for the top-level CSR map
* SystemVerilog CSR RTL
* PeakRDL Python model
* HTML register documentation
* Markdown register documentation for the generated documentation tree

## Running Unit Tests

After generating the Python model, run:

```bash
make unittest
```

This executes the unit tests generated together with the PeakRDL Python model.

## Cleaning Generated Files

To remove generated artifacts, run:

```bash
make clean
```

## Notes

The Makefile uses paths relative to the current working directory, so it should be executed directly from this directory.
