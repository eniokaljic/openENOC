# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Shared SystemRDL model helpers for openENOC hardware-interface exporters."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
import re
import tempfile
from typing import Any, Iterable

from peakrdl_regblock.identifier_filter import kw_filter
from peakrdl_regblock.udps import ALL_UDPS
from systemrdl import RDLCompiler
from systemrdl.ast import (
    binary,
    boolean,
    cast,
    conditional,
    exponential,
    literals,
    reduction,
    references,
    relational,
    unary,
)
from systemrdl.node import (
    AddressableNode,
    FieldNode,
    Node,
    RegNode,
    RegfileNode,
    SignalNode,
)


CSR_TO_CORE = "csr_to_core"
CORE_TO_CSR = "core_to_csr"


class ExportError(RuntimeError):
    """Raised when an RDL model cannot be represented by an exported HWIF."""


@dataclass(frozen=True)
class Dimension:
    expression: str
    value: int


@dataclass(frozen=True)
class PathElement:
    name: str
    dimensions: tuple[Dimension, ...] = ()
    packed: bool = False


@dataclass(frozen=True)
class Signal:
    """A leaf in one of the two directional hardware-interface trees."""

    path: tuple[PathElement, ...]
    name: str
    direction: str
    packed_range: str = ""
    signed: bool = False
    dimensions: tuple[Dimension, ...] = ()

    @property
    def declaration(self) -> str:
        signed = " signed" if self.signed else ""
        packed = f" {self.packed_range}" if self.packed_range else ""
        unpacked = "".join(
            f"[{dimension.expression}]" for dimension in self.dimensions
        )
        return f"logic{signed}{packed} {self.name}{unpacked};"


@dataclass(frozen=True)
class LocalParameter:
    name: str
    expression: str


@dataclass(frozen=True)
class StructDefinition:
    name: str
    members: tuple[str, ...]
    packed: bool = False


@dataclass
class _StructTree:
    children: dict[str, "_StructTree"] = field(default_factory=dict)
    child_dimensions: dict[str, tuple[Dimension, ...]] = field(default_factory=dict)
    child_packed: dict[str, bool] = field(default_factory=dict)
    leaves: list[Signal] = field(default_factory=list)


class ExpressionRenderer:
    """Render the numeric subset of the SystemRDL AST as SystemVerilog."""

    binary_operators = {
        binary.Add: "+",
        binary.Sub: "-",
        binary.Mult: "*",
        binary.Div: "/",
        binary.Mod: "%",
        binary.BitwiseAnd: "&",
        binary.BitwiseOr: "|",
        binary.BitwiseXor: "^",
        binary.BitwiseXnor: "^~",
        exponential.Exponent: "**",
        exponential.LShift: "<<",
        exponential.RShift: ">>",
        relational.Eq: "==",
        relational.Neq: "!=",
        relational.Lt: "<",
        relational.Gt: ">",
        relational.Leq: "<=",
        relational.Geq: ">=",
        boolean.BoolAnd: "&&",
        boolean.BoolOr: "||",
    }
    unary_operators = {
        unary.UnaryPlus: "+",
        unary.UnaryMinus: "-",
        unary.BitwiseInvert: "~",
        reduction.AndReduce: "&",
        reduction.NandReduce: "~&",
        reduction.OrReduce: "|",
        reduction.NorReduce: "~|",
        reduction.XorReduce: "^",
        reduction.XnorReduce: "~^",
        reduction.BoolNot: "!",
    }

    def __init__(self) -> None:
        self.used_parameters: set[str] = set()

    def render(self, expression: Any) -> str:
        if isinstance(expression, cast.AssignmentCast):
            return self.render(expression.v)
        if isinstance(expression, cast.Width64Cast):
            return f"64'({self.render(expression.v)})"
        if isinstance(expression, cast.WidthCast):
            return f"{self.render(expression.w_expr)}'({self.render(expression.v)})"
        if isinstance(expression, cast.BoolCast):
            return f"logic'({self.render(expression.n)})"

        if isinstance(expression, references.ParameterRef):
            self.used_parameters.add(expression.param_name)
            return expression.param_name

        if isinstance(expression, literals.IntLiteral):
            return str(expression.val)
        if isinstance(expression, literals.BoolLiteral):
            return "1'b1" if expression.val else "1'b0"
        if isinstance(expression, literals.StringLiteral):
            return self._quote_string(expression.val)
        if isinstance(expression, literals.ExternalLiteral):
            return str(expression.value)

        for expression_type, operator in self.binary_operators.items():
            if isinstance(expression, expression_type):
                return (
                    f"({self.render(expression.l)} {operator} "
                    f"{self.render(expression.r)})"
                )

        for expression_type, operator in self.unary_operators.items():
            if isinstance(expression, expression_type):
                return f"({operator}{self.render(expression.n)})"

        if isinstance(expression, conditional.Conditional):
            return (
                f"({self.render(expression.i)} ? {self.render(expression.j)} : "
                f"{self.render(expression.k)})"
            )

        raise ExportError(
            "unsupported parameter expression in the hardware interface: "
            f"{type(expression).__name__}"
        )

    @staticmethod
    def _quote_string(value: str) -> str:
        escaped = value.replace("\\", "\\\\").replace('"', '\\"')
        return f'"{escaped}"'


def compile_rdl(
    rdl_file: Path,
    include_paths: Iterable[Path],
    top_name: str,
) -> Node:
    compiler = RDLCompiler()
    for udp_definition in ALL_UDPS:
        compiler.register_udp(udp_definition)
    compiler.compile_file(
        str(rdl_file),
        incl_search_paths=[str(path) for path in include_paths],
    )
    return compiler.elaborate(top_def_name=top_name).top


def safe_property(node: Node, property_name: str, default: Any = None) -> Any:
    try:
        return node.get_property(property_name)
    except (LookupError, TypeError):
        return default


def sv_identifier(name: str) -> str:
    name = re.sub(r"[^a-zA-Z0-9_$]", "_", name)
    if not name or not re.match(r"[a-zA-Z_]", name):
        name = f"rdl_{name}"
    return kw_filter(name)


def upper_identifier(parts: Iterable[str]) -> str:
    return "_".join(sv_identifier(part) for part in parts).upper()


def original_children(original: Any) -> dict[str, Any]:
    return {child.inst_name: child for child in getattr(original, "children", [])}


def component_parameters(component: RegfileNode) -> list[Any]:
    return list(component.inst.original_def.parameters)


def reusable_component_type(node: Node) -> str | None:
    return getattr(node.inst.original_def, "type_name", None)


def find_component(root: Node, component_name: str) -> RegfileNode:
    matches = [
        node
        for node in root.descendants(unroll=False)
        if isinstance(node, RegfileNode)
        and (
            node.inst_name == component_name
            or reusable_component_type(node) == component_name
        )
    ]
    if len(matches) != 1:
        raise ExportError(
            f"expected exactly one regfile '{component_name}', found {len(matches)}"
        )
    return matches[0]


def find_interface_components(root: Node) -> list[RegfileNode]:
    components = []
    for node in root.descendants(unroll=False):
        if not isinstance(node, RegfileNode):
            continue
        type_name = reusable_component_type(node)
        if type_name and re.fullmatch(r"openenoc_.+_interface", type_name):
            components.append(node)
    return components


def relative_instance_path(node: Node, ancestor: Node) -> tuple[str, ...]:
    path: list[str] = []
    current = node
    while current is not ancestor:
        path.append(sv_identifier(current.inst_name))
        if current.parent is None:
            raise ExportError(
                f"'{ancestor.get_path()}' is not an ancestor of '{node.get_path()}'"
            )
        current = current.parent
    return tuple(reversed(path))


def write_if_changed(output_path: Path, content: str) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    if output_path.exists() and output_path.read_text(encoding="utf-8") == content:
        output_path.touch()
        return

    with tempfile.NamedTemporaryFile(
        mode="w",
        encoding="utf-8",
        dir=output_path.parent,
        prefix=f".{output_path.name}.",
        delete=False,
    ) as temporary_file:
        temporary_file.write(content)
        temporary_path = Path(temporary_file.name)
    temporary_path.replace(output_path)


class InterfaceBuilder:
    """Build directional hierarchical signal trees from a reusable regfile."""

    def __init__(self, component: RegfileNode) -> None:
        self.component = component
        self.renderer = ExpressionRenderer()
        self.signals: list[Signal] = []
        self.local_parameters: list[LocalParameter] = []
        self._signal_paths: set[tuple[str, ...]] = set()
        self._local_parameter_names: set[str] = set()
        self._used_signal_paths: set[str] = set()
        self.data_width = self._cpuif_data_width()

    def build(self) -> None:
        self._find_used_signals(self.component)
        self._walk(self.component, self.component.inst.original_def, ())

    def _find_used_signals(self, node: Node) -> None:
        if node is not self.component and isinstance(node, AddressableNode) and node.external:
            return

        for property_name in node.list_properties():
            value = safe_property(node, property_name)
            if isinstance(value, SignalNode):
                relative_instance_path(value, self.component)
                self._used_signal_paths.add(value.get_path())

        if isinstance(node, SignalNode) and safe_property(node, "field_reset", False):
            self._used_signal_paths.add(node.get_path())

        for child in node.children(unroll=False):
            self._find_used_signals(child)

    def _walk(
        self,
        node: Node,
        original: Any,
        path: tuple[PathElement, ...],
    ) -> None:
        if isinstance(node, SignalNode):
            if node.get_path() in self._used_signal_paths:
                self._add_signal(
                    path,
                    sv_identifier(node.inst_name),
                    CORE_TO_CSR,
                    self._packed_range_from_width(node.width),
                )
            return

        node_path = path
        if node is not self.component:
            node_path = (
                *path,
                PathElement(
                    sv_identifier(node.inst_name),
                    self._dimensions(node, original),
                ),
            )

        if isinstance(node, FieldNode):
            self._add_field(node, original, node_path)
            return

        if isinstance(node, RegNode) and node.external:
            self._add_external_register(node, node_path)
            return

        if isinstance(node, AddressableNode) and node.external:
            self._add_external_block(node, original, node_path)
            return

        child_definitions = original_children(original)
        for child in node.children(unroll=False):
            child_original = child_definitions.get(child.inst_name)
            if child_original is None:
                raise ExportError(
                    f"cannot correlate '{child.get_path()}' with its RDL definition"
                )
            self._walk(child, child_original, node_path)

        if isinstance(node, RegNode):
            self._add_register_outputs(node, node_path)

    def _dimensions(self, node: Node, original: Any) -> tuple[Dimension, ...]:
        expressions = getattr(original, "array_dimensions", None) or []
        values = getattr(node, "array_dimensions", None) or []
        if len(expressions) != len(values):
            raise ExportError(f"array dimension mismatch at '{node.get_path()}'")
        return tuple(
            Dimension(self.renderer.render(expression), value)
            for expression, value in zip(expressions, values)
        )

    def _add_field(
        self,
        node: FieldNode,
        original: Any,
        path: tuple[PathElement, ...],
    ) -> None:
        packed_range = self._field_packed_range(node, original)
        signed = bool(safe_property(node, "is_signed", False))

        if node.is_hw_readable:
            self._add_signal(path, "value", CSR_TO_CORE, packed_range, signed)
        if node.is_hw_writable and safe_property(node, "next") is None:
            self._add_signal(path, "next", CORE_TO_CSR, packed_range, signed)

        for property_name in ("we", "wel", "swwe", "swwel", "hwclr", "hwset"):
            if safe_property(node, property_name) is True:
                self._add_signal(path, property_name, CORE_TO_CSR)

        for property_name, counter_enabled in (
            ("incr", node.is_up_counter),
            ("decr", node.is_down_counter),
        ):
            if not counter_enabled:
                continue
            if not safe_property(node, property_name):
                self._add_signal(path, property_name, CORE_TO_CSR)
            width = safe_property(node, f"{property_name}width")
            if width:
                self._add_signal(
                    path,
                    f"{property_name}value",
                    CORE_TO_CSR,
                    self._packed_range_from_width(width),
                )

        for property_name in (
            "anded",
            "ored",
            "xored",
            "swmod",
            "swacc",
            "rd_swacc",
            "wr_swacc",
            "overflow",
            "underflow",
        ):
            if safe_property(node, property_name):
                self._add_signal(path, property_name, CSR_TO_CORE)

        for property_name in ("incrthreshold", "decrthreshold"):
            if safe_property(node, property_name, False) is not False:
                self._add_signal(path, property_name, CSR_TO_CORE)

    def _add_register_outputs(
        self,
        node: RegNode,
        path: tuple[PathElement, ...],
    ) -> None:
        if node.is_interrupt_reg:
            self._add_signal(path, "intr", CSR_TO_CORE)
            if node.is_halt_reg:
                self._add_signal(path, "halt", CSR_TO_CORE)

    def _add_external_register(
        self,
        node: RegNode,
        path: tuple[PathElement, ...],
    ) -> None:
        width = min(self.data_width, node.get_property("regwidth"))
        subword_count = (
            node.get_property("regwidth") // node.get_property("accesswidth")
        )
        self._add_signal(
            path,
            "req",
            CSR_TO_CORE,
            self._packed_range_from_width(subword_count),
        )
        self._add_signal(path, "req_is_wr", CSR_TO_CORE)

        if node.has_sw_writable:
            self._add_external_register_data(
                node, path, "wr_data", CSR_TO_CORE, width, subword_count, False
            )
            self._add_external_register_data(
                node, path, "wr_biten", CSR_TO_CORE, width, subword_count, False
            )
            self._add_signal(path, "wr_ack", CORE_TO_CSR)
        if node.has_sw_readable:
            self._add_signal(path, "rd_ack", CORE_TO_CSR)
            self._add_external_register_data(
                node, path, "rd_data", CORE_TO_CSR, width, subword_count, True
            )

    def _add_external_register_data(
        self,
        node: RegNode,
        path: tuple[PathElement, ...],
        name: str,
        direction: str,
        width: int,
        subword_count: int,
        readable: bool,
    ) -> None:
        if subword_count != 1:
            self._add_signal(
                path,
                name,
                direction,
                self._packed_range_from_width(width),
            )
            return

        data_path = (*path, PathElement(name, packed=True))
        current_bit = width - 1
        for field_node in reversed(list(node.fields())):
            if readable and not field_node.is_sw_readable:
                continue
            if not readable and not field_node.is_sw_writable:
                continue
            if field_node.high < current_bit:
                reserved_low = field_node.high + 1
                self._add_signal(
                    data_path,
                    f"_reserved_{current_bit}_{reserved_low}",
                    direction,
                    self._packed_range_from_width(current_bit - field_node.high),
                )
            self._add_signal(
                data_path,
                sv_identifier(field_node.inst_name),
                direction,
                self._packed_range_from_width(field_node.width),
            )
            current_bit = field_node.low - 1

        if current_bit != -1:
            self._add_signal(
                data_path,
                f"_reserved_{current_bit}_0",
                direction,
                self._packed_range_from_width(current_bit + 1),
            )

    def _add_external_block(
        self,
        node: AddressableNode,
        original: Any,
        path: tuple[PathElement, ...],
    ) -> None:
        address_width_name = f"{upper_identifier(item.name for item in path)}_ADDR_W"
        size_expression = self._external_size_expression(node, original)
        self._add_local_parameter(
            address_width_name,
            f"(({size_expression}) > 1) ? $clog2({size_expression}) : 1",
        )

        address_range = f"[{address_width_name}-1:0]"
        data_range = self._packed_range_from_width(self.data_width)
        for name, packed_range in (
            ("req", ""),
            ("addr", address_range),
            ("req_is_wr", ""),
            ("wr_data", data_range),
            ("wr_biten", data_range),
        ):
            self._add_signal(path, name, CSR_TO_CORE, packed_range)

        for name, packed_range in (
            ("wr_ack", ""),
            ("rd_ack", ""),
            ("rd_data", data_range),
        ):
            self._add_signal(path, name, CORE_TO_CSR, packed_range)

    def _field_packed_range(self, node: FieldNode, original: Any) -> str:
        field_renderer = ExpressionRenderer()
        msb = field_renderer.render(original.msb)
        lsb = field_renderer.render(original.lsb)
        self.renderer.used_parameters.update(field_renderer.used_parameters)

        fractional_width = safe_property(node, "fracwidth") or 0
        if not field_renderer.used_parameters:
            low = -fractional_width
            high = low + node.width - 1
            return "" if high == 0 and low == 0 else f"[{high}:{low}]"

        width_expression = (
            f"({msb} + 1)" if lsb == "0" else f"(({msb}) - ({lsb}) + 1)"
        )
        if fractional_width:
            return (
                f"[({width_expression}) - {fractional_width} - 1:"
                f"-{fractional_width}]"
            )
        if lsb == "0":
            return f"[{msb}:0]"
        return f"[{width_expression} - 1:0]"

    @staticmethod
    def _packed_range_from_width(width: int) -> str:
        return "" if width == 1 else f"[{width - 1}:0]"

    def _external_size_expression(self, node: AddressableNode, original: Any) -> str:
        children = list(node.children(unroll=False))
        child_definitions = original_children(original)
        if len(children) == 1:
            child = children[0]
            child_original = child_definitions.get(child.inst_name)
            dimensions = getattr(child_original, "array_dimensions", None) or []
            if (
                child_original is not None
                and dimensions
                and child.raw_address_offset == 0
                and child.array_stride is not None
            ):
                factors = [self.renderer.render(value) for value in dimensions]
                factors.append(str(child.array_stride))
                return " * ".join(factors)
        return str(node.size)

    def _cpuif_data_width(self) -> int:
        widths = {
            register.get_property("accesswidth")
            for register in self.component.descendants(unroll=False)
            if isinstance(register, RegNode)
        }
        if not widths:
            raise ExportError(
                f"'{self.component.get_path()}' does not contain any registers"
            )
        return max(widths)

    def _add_signal(
        self,
        path: tuple[PathElement, ...],
        name: str,
        direction: str,
        packed_range: str = "",
        signed: bool = False,
        dimensions: tuple[Dimension, ...] = (),
    ) -> None:
        key = (direction, *(item.name for item in path), name)
        if key in self._signal_paths:
            raise ExportError(
                "hardware-interface signal collision: " + ".".join(key)
            )
        self._signal_paths.add(key)
        self.signals.append(
            Signal(path, sv_identifier(name), direction, packed_range, signed, dimensions)
        )

    def _add_local_parameter(self, name: str, expression: str) -> None:
        if name in self._local_parameter_names:
            raise ExportError(f"generated local parameter name collision: '{name}'")
        self._local_parameter_names.add(name)
        self.local_parameters.append(LocalParameter(name, expression))

    def parameter_declarations(self) -> list[str]:
        while True:
            used_before = set(self.renderer.used_parameters)
            for parameter in component_parameters(self.component):
                if parameter.name in self.renderer.used_parameters:
                    self.renderer.render(parameter.expr)
            if self.renderer.used_parameters == used_before:
                break

        parameter_types = {int: "int", bool: "logic", str: "string"}
        declarations: list[str] = []
        for parameter in component_parameters(self.component):
            if parameter.name not in self.renderer.used_parameters:
                continue
            sv_type = parameter_types.get(parameter.param_type)
            if sv_type is None:
                raise ExportError(
                    f"unsupported type for parameter '{parameter.name}'"
                )
            declarations.append(
                f"parameter {sv_type} {parameter.name} = "
                f"{self.renderer.render(parameter.expr)}"
            )

        declarations.extend(
            f"localparam int {parameter.name} = {parameter.expression}"
            for parameter in self.local_parameters
        )
        return declarations

    def struct_definitions(self, direction: str) -> list[StructDefinition]:
        tree = _StructTree()
        for signal in self.signals:
            if signal.direction != direction:
                continue
            current = tree
            for element in signal.path:
                if any(leaf.name == element.name for leaf in current.leaves):
                    raise ExportError(f"struct member collision at '{element.name}'")
                child = current.children.setdefault(element.name, _StructTree())
                previous_dimensions = current.child_dimensions.setdefault(
                    element.name, element.dimensions
                )
                if previous_dimensions != element.dimensions:
                    raise ExportError(
                        f"inconsistent array dimensions for '{element.name}'"
                    )
                previous_packed = current.child_packed.setdefault(
                    element.name, element.packed
                )
                if previous_packed != element.packed:
                    raise ExportError(
                        f"inconsistent packed qualifier for '{element.name}'"
                    )
                current = child
            if signal.name in current.children:
                raise ExportError(f"struct member collision at '{signal.name}'")
            if any(leaf.name == signal.name for leaf in current.leaves):
                raise ExportError(f"duplicate struct leaf '{signal.name}'")
            current.leaves.append(signal)

        definitions: list[StructDefinition] = []

        def type_name(path: tuple[str, ...]) -> str:
            suffix = "__".join(path)
            return f"{direction}__{suffix}_t" if suffix else f"{direction}_t"

        def emit(node: _StructTree, path: tuple[str, ...]) -> None:
            for child_name, child in node.children.items():
                emit(child, (*path, child_name))

            members = []
            for child_name in node.children:
                dimensions = "".join(
                    f"[{dimension.expression}]"
                    for dimension in node.child_dimensions[child_name]
                )
                members.append(
                    f"{type_name((*path, child_name))} {child_name}{dimensions};"
                )
            members.extend(signal.declaration for signal in node.leaves)
            if members:
                packed = False
                if path:
                    parent = tree
                    for element in path[:-1]:
                        parent = parent.children[element]
                    packed = parent.child_packed[path[-1]]
                definitions.append(
                    StructDefinition(type_name(path), tuple(members), packed)
                )

        emit(tree, ())
        return definitions
