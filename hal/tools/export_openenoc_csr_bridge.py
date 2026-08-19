#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Generate an endpoint-specific bridge between PeakRDL HWIFs and interfaces."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import sys

from jinja2 import Environment, FileSystemLoader, StrictUndefined
from systemrdl import RDLCompileError

from openenoc_hwif import (
    CORE_TO_CSR,
    CSR_TO_CORE,
    ExportError,
    InterfaceBuilder,
    Signal,
    compile_rdl,
    find_interface_components,
    relative_instance_path,
    reusable_component_type,
    sv_identifier,
    write_if_changed,
)


@dataclass(frozen=True)
class InterfacePort:
    interface_type: str
    name: str
    component_path: tuple[str, ...]
    builder: InterfaceBuilder
    parameters: tuple[str, ...]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("rdl_file", type=Path, help="endpoint SystemRDL file")
    parser.add_argument("--top", default="csr", help="CSR addrmap name")
    parser.add_argument(
        "--module-name",
        required=True,
        help="generated bridge module name without package suffix",
    )
    parser.add_argument("-I", "--include", action="append", type=Path, default=[])
    parser.add_argument("-o", "--output", required=True, type=Path)
    parser.add_argument(
        "--template-dir",
        type=Path,
        default=Path(__file__).resolve().parent.parent / "templates",
    )
    return parser.parse_args()


def port_name(component_path: tuple[str, ...]) -> str:
    parts = list(component_path)
    last = parts[-1]
    if last.endswith("_interface"):
        last = last[: -len("_interface")]
    parts[-1] = f"{last}_if"
    return sv_identifier("__".join(parts))


def interface_type(component_type: str) -> str:
    if not component_type.endswith("_interface"):
        raise ExportError(f"unexpected interface component type '{component_type}'")
    return f"{component_type[: -len('_interface')]}_if"


def signal_access(
    root: str,
    signal: Signal,
    indexes: tuple[tuple[str, ...], ...],
) -> str:
    parts = [root]
    for element, element_indexes in zip(signal.path, indexes):
        suffix = "".join(f"[{index}]" for index in element_indexes)
        parts.append(f"{element.name}{suffix}")
    parts.append(signal.name)
    return ".".join(parts)


def assignment_lines(
    assignment_id: int,
    lhs_root: str,
    rhs_root: str,
    signal: Signal,
) -> list[str]:
    loops: list[tuple[str, int]] = []
    indexes: list[tuple[str, ...]] = []
    dimension_id = 0
    for element in signal.path:
        element_indexes = []
        for dimension in element.dimensions:
            index = f"i{assignment_id}_{dimension_id}"
            dimension_id += 1
            loops.append((index, dimension.value))
            element_indexes.append(index)
        indexes.append(tuple(element_indexes))

    indent = "        "
    lines = []
    for index, bound in loops:
        lines.append(
            f"{indent}for (int unsigned {index} = 0; "
            f"{index} < {bound}; {index}++) begin"
        )
        indent += "    "

    indexed = tuple(indexes)
    lhs = signal_access(lhs_root, signal, indexed)
    rhs = signal_access(rhs_root, signal, indexed)
    lines.append(f"{indent}{lhs} = {rhs};")

    for _ in reversed(loops):
        indent = indent[:-4]
        lines.append(f"{indent}end")
    return lines


def main() -> int:
    args = parse_args()
    try:
        root = compile_rdl(args.rdl_file, args.include, args.top)
        components = find_interface_components(root)
        if not components:
            raise ExportError(f"'{root.get_path()}' contains no openENOC interfaces")

        ports: list[InterfacePort] = []
        seen_port_names: set[str] = set()
        for component in components:
            component_type = reusable_component_type(component)
            assert component_type is not None
            path = relative_instance_path(component, root)
            name = port_name(path)
            if name in seen_port_names:
                raise ExportError(f"duplicate generated bridge port '{name}'")
            seen_port_names.add(name)

            builder = InterfaceBuilder(component)
            builder.build()
            parameters = tuple(
                name
                for name in component.parameters
                if name != "INST_NAME"
            )
            ports.append(
                InterfacePort(
                    interface_type(component_type),
                    name,
                    path,
                    builder,
                    parameters,
                )
            )

        assignments: list[str] = []
        assignment_id = 0
        for port in ports:
            csr_root = ".".join(("csr_hwif_in", *port.component_path))
            interface_root = f"{port.name}.{CORE_TO_CSR}"
            for signal in port.builder.signals:
                if signal.direction != CORE_TO_CSR:
                    continue
                assignments.extend(
                    assignment_lines(
                        assignment_id,
                        csr_root,
                        interface_root,
                        signal,
                    )
                )
                assignment_id += 1

            csr_root = ".".join(("csr_hwif_out", *port.component_path))
            interface_root = f"{port.name}.{CSR_TO_CORE}"
            for signal in port.builder.signals:
                if signal.direction != CSR_TO_CORE:
                    continue
                assignments.extend(
                    assignment_lines(
                        assignment_id,
                        interface_root,
                        csr_root,
                        signal,
                    )
                )
                assignment_id += 1

        environment = Environment(
            loader=FileSystemLoader(args.template_dir),
            undefined=StrictUndefined,
            trim_blocks=True,
            lstrip_blocks=True,
            keep_trailing_newline=True,
        )
        content = environment.get_template("openenoc_csr_bridge.sv.j2").render(
            source_name=args.rdl_file.name,
            bridge_name=f"{args.module_name}_bridge",
            csr_package=f"{args.module_name}_pkg",
            csr_input_type=f"{args.module_name}__in_t",
            csr_output_type=f"{args.module_name}__out_t",
            ports=ports,
            assignments=assignments,
        )
        write_if_changed(args.output, content)
    except (ExportError, RDLCompileError, OSError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
