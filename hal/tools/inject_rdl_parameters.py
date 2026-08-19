#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Insert elaborated top-level SystemRDL parameters into a generated C header."""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys
from typing import Any

from systemrdl import RDLCompileError

from openenoc_hwif import ExportError, compile_rdl, write_if_changed


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("rdl_file", type=Path, help="input SystemRDL file")
    parser.add_argument("--top", required=True, help="parameterized addrmap name")
    parser.add_argument("--header", required=True, type=Path, help="input C header")
    parser.add_argument("-I", "--include", action="append", type=Path, default=[])
    parser.add_argument("-o", "--output", required=True, type=Path)
    return parser.parse_args()


def macro_identifier(top_name: str, parameter_name: str) -> str:
    combined = f"{top_name}__{parameter_name}".upper()
    combined = re.sub(r"[^A-Z0-9_]", "_", combined)
    if not combined[0].isalpha() and combined[0] != "_":
        combined = f"RDL_{combined}"
    return combined


def c_value(value: Any) -> str:
    if isinstance(value, bool):
        return "1" if value else "0"
    if isinstance(value, int):
        macro = "UINT64_C" if value >= 0 else "INT64_C"
        return f"{macro}({value})"
    if isinstance(value, str):
        escaped = value.replace("\\", "\\\\").replace('"', '\\"')
        return f'"{escaped}"'
    raise ExportError(f"unsupported C-header parameter type: {type(value).__name__}")


def main() -> int:
    args = parse_args()
    try:
        root = compile_rdl(args.rdl_file, args.include, args.top)
        if not root.parameters:
            content = args.header.read_text(encoding="utf-8")
            write_if_changed(args.output, content)
            return 0

        header = args.header.read_text(encoding="utf-8")
        marker = "#include <assert.h>\n"
        if marker not in header:
            raise ExportError(
                f"cannot find the include section in '{args.header}'"
            )

        lines = [
            "",
            f"// Parameters from the {args.top} SystemRDL addrmap",
        ]
        width = max(
            len(macro_identifier(args.top, name))
            for name in root.parameters
        )
        for name, value in root.parameters.items():
            macro = macro_identifier(args.top, name)
            lines.append(f"#define {macro:<{width}} {c_value(value)}")
        lines.append("")
        parameter_section = "\n".join(lines)

        content = header.replace(marker, marker + parameter_section, 1)
        write_if_changed(args.output, content)
    except (ExportError, RDLCompileError, OSError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
