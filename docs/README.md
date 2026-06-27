<!--
SPDX-FileCopyrightText: 2026 Tarik Hamedovic
SPDX-License-Identifier: CC-BY-SA-4.0
-->

# Build the Documentation

This section explains how to build the openENOC documentation locally and how it is configured for Read the Docs.

## Prerequisites

Make sure the following tools are installed on your system:

- Python 3
- `venv` (Python virtual environments)
- `make`

## Set Up a Virtual Environment

Create a virtual environment for building the documentation:

```bash
python3 -m venv ~/venvs/docs
```

Activate the environment:

```bash
source ~/venvs/docs/bin/activate
```

## Install Documentation Dependencies

Clone the repository if you have not already done so:

```bash
git clone <repository-url>
cd <repository-folder>
```

Install the required Python packages:

```bash
pip install -r docs/requirements.txt
```

## Build the HTML Documentation

Build the HTML documentation using Sphinx:

```bash
cd docs
make html
```

After the build finishes, open the generated documentation:

```bash
xdg-open build/html/index.html
```

> **Note**
>
> The output HTML files are generated inside the `build/html` directory.

## Read the Docs

The repository includes a `.readthedocs.yaml` file at the repository root. Read the Docs uses it to:

- build on Ubuntu 24.04
- use Python 3.11
- load the Sphinx configuration from `docs/source/conf.py`
- install dependencies from `docs/requirements.txt`

After importing the repository into Read the Docs, the hosted documentation will be available at a URL like:

```text
https://<project-name>.readthedocs.io/
```
