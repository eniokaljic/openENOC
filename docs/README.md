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
xdg-open ../build/docs/html/index.html
```

> **Note**
>
> The output HTML files are generated inside `build/docs/html` at the repository
> root. Sphinx's doctree cache, Python bytecode, and temporary files also stay
> under `build/docs`.

## WaveDrom Timing Diagrams

Timing diagrams can be written as JSON directly inside an `.rst` file using
the `sphinxcontrib-wavedrom` extension:

```rst
.. wavedrom::
    :caption: Example read completion
    :alt: A request pulse followed by a read acknowledgement.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p...."},
            {"name": "req", "wave": "010.."},
            {"name": "rd_ack", "wave": "0..10"}
        ]
    }
```

The directive content is indented JSON, separated from the options by a blank
line. Keys and strings require double quotes.
The Native CPUIF RTL Reference contains complete read, masked-write, and
error-response examples.

`docs/requirements.txt` pins the Sphinx extension and Python WaveDrom renderer
versions. `docs/src/conf.py` enables build-time rendering with
`wavedrom_html_jsinline = False` and `render_using_wavedrompy = True`.
Sphinx generates SVG images during the HTML build using the Python renderer;
viewing the diagrams works offline and requires no browser JavaScript, CDN,
Node.js, or separately maintained image files. The existing Read the Docs
and GitHub Pages builds install the same documentation requirements.

The local extension `docs/src/_ext/openenoc_wavedrom.py` reads an optional CSS
`style` string on each signal and applies it to that signal's `data` labels.
The native WaveDrom renderer ignores this additional field; support comes from
the local extension. `font-size` accepts positive lengths in `px` or `pt`:

```json
{
    "name": "error_code",
    "wave": "x=.x",
    "data": ["LOCAL_\nAXI_RD_\nSLVERR"],
    "style": "font-size: 10px;"
}
```

Standard JSON newline escapes (`\n`) produce line breaks inside a `data` array
entry. Multiline labels require the array form because the WaveDrom string form
separates labels at whitespace. Font selection and line breaks are independent;
omitting `style` keeps the native font. Signal names and group labels retain
their normal styling.
The extension derives line spacing and lane height from the font size and
number of text lines, enlarging only the lanes that need more space.

The style also applies to labels containing binary bitmaps:

```json
{
    "name": "port_bitmap",
    "wave": "x==x",
    "data": ["0b1100", "0b0001"],
    "style": "font-size: 10px;"
}
```

Text is not wrapped automatically. Waveform timing, horizontal scale, and stroke
widths stay unchanged. Sphinx loads the extension through the `extensions` list
in `docs/src/conf.py`.

See the [extension documentation](https://github.com/bavovanachte/sphinx-wavedrom)
for directive options and the [WaveDrom tutorial](https://wavedrom.com/tutorial.html)
for waveform notation.

## Read the Docs

The repository includes a `.readthedocs.yaml` file at the repository root. Read the Docs uses it to:

- build on Ubuntu 24.04
- use Python 3.11
- load the Sphinx configuration from `docs/src/conf.py`
- install dependencies from `docs/requirements.txt`

After importing the repository into Read the Docs, the hosted documentation will be available at a URL like:

```text
https://<project-name>.readthedocs.io/
```
