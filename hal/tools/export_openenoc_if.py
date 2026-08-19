#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Generate a hierarchical, parameterized SystemVerilog interface from RDL."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

from jinja2 import Environment, FileSystemLoader, StrictUndefined
from systemrdl import RDLCompileError

from openenoc_hwif import (
    CORE_TO_CSR,
    CSR_TO_CORE,
    ExportError,
    InterfaceBuilder,
    compile_rdl,
    find_component,
    write_if_changed,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("rdl_file", type=Path, help="input SystemRDL file")
    parser.add_argument("--top", required=True, help="top-level addrmap name")
    parser.add_argument(
        "--component",
        required=True,
        help="reusable regfile type or instance name to export",
    )
    parser.add_argument(
        "--interface-name",
        required=True,
        help="generated SystemVerilog interface identifier",
    )
    parser.add_argument("-I", "--include", action="append", type=Path, default=[])
    parser.add_argument("-o", "--output", required=True, type=Path)
    parser.add_argument(
        "--template-dir",
        type=Path,
        default=Path(__file__).resolve().parent.parent / "templates",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        root = compile_rdl(args.rdl_file, args.include, args.top)
        component = find_component(root, args.component)
        builder = InterfaceBuilder(component)
        builder.build()

        environment = Environment(
            loader=FileSystemLoader(args.template_dir),
            undefined=StrictUndefined,
            trim_blocks=True,
            lstrip_blocks=True,
            keep_trailing_newline=True,
        )
        content = environment.get_template("openenoc_if.sv.j2").render(
            source_name=args.rdl_file.name,
            interface_name=args.interface_name,
            parameter_declarations=builder.parameter_declarations(),
            core_to_csr_structs=builder.struct_definitions(CORE_TO_CSR),
            csr_to_core_structs=builder.struct_definitions(CSR_TO_CORE),
        )
        write_if_changed(args.output, content)
    except (ExportError, RDLCompileError, OSError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
