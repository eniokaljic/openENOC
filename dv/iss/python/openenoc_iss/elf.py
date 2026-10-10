# SPDX-FileCopyrightText: 2026 Kerim Bavcic
# SPDX-License-Identifier: AGPL-3.0-or-later

from __future__ import annotations

import hashlib
import io
import os
import re
import struct
from dataclasses import dataclass
from pathlib import Path
from types import MappingProxyType
from typing import Mapping

from elftools.common.exceptions import ELFError
from elftools.elf.elffile import ELFFile
from elftools.elf.sections import RISCVAttributesSection, SymbolTableSection

_ADDRESS_SPACE_SIZE = 1 << 32
_PF_EXECUTE = 1
_PF_WRITE = 2
_RV32I_ARCH = re.compile(r"rv32i(?:\d+p\d+)?")
_ALLOWED_METADATA_SEGMENTS = {
    "PT_NULL",
    "PT_NOTE",
    "PT_PHDR",
    "PT_GNU_STACK",
    "PT_RISCV_ATTRIBUTES",
}


class ElfValidationError(ValueError):
    pass


@dataclass(frozen=True)
class MemoryMap:
    imem_base: int
    imem_size: int
    dmem_base: int
    dmem_size: int
    csr_base: int
    csr_size: int


def load_memory_map(path: str | Path) -> MemoryMap:
    definitions = dict(re.findall(
        r"^#define\s+(\w+)\s+(0x[0-9a-fA-F]+|[0-9]+)\s*$",
        Path(path).read_text(), re.MULTILINE,
    ))
    try:
        values = {name: int(definitions[name], 0) for name in (
            "IMEM_BASE_ADDR", "IMEM_DEPTH", "DMEM_BASE_ADDR", "DMEM_DEPTH",
            "CSR_BASE_ADDR", "CSR_SIZE_BYTES",
        )}
    except KeyError as error:
        raise ValueError(f"memory map {path} is missing {error.args[0]}") from error
    return MemoryMap(
        imem_base=values["IMEM_BASE_ADDR"],
        imem_size=values["IMEM_DEPTH"] * 4,
        dmem_base=values["DMEM_BASE_ADDR"],
        dmem_size=values["DMEM_DEPTH"] * 4,
        csr_base=values["CSR_BASE_ADDR"],
        csr_size=values["CSR_SIZE_BYTES"],
    )


def default_memory_map() -> MemoryMap:
    return load_memory_map(os.environ["OPENENOC_MEMORY_MAP"])


@dataclass(frozen=True)
class LoadSegment:
    load_address: int
    virtual_address: int
    memory_size: int
    flags: int
    data: bytes


@dataclass(frozen=True)
class ElfSymbol:
    name: str
    address: int
    size: int
    symbol_type: str


@dataclass(frozen=True)
class BootImage:
    entry_pc: int
    segments: tuple[LoadSegment, ...]
    symbols: Mapping[str, ElfSymbol]
    sha256: str

    def __post_init__(self) -> None:
        object.__setattr__(self, "symbols", MappingProxyType(dict(self.symbols)))

    def symbol_address(self, name: str) -> int:
        try:
            return self.symbols[name].address
        except KeyError as error:
            raise KeyError(f"ELF symbol not found: {name}") from error


@dataclass(frozen=True)
class _ProgramRange:
    virtual_start: int
    virtual_end: int
    load_start: int
    load_end: int
    file_virtual_end: int
    flags: int


def load_elf(
    path: str | Path,
    *,
    memory_map: MemoryMap | None = None,
) -> BootImage:
    return parse_elf(
        Path(path).read_bytes(),
        memory_map=memory_map,
    )


def parse_elf(
    image: bytes | bytearray | memoryview,
    *,
    memory_map: MemoryMap | None = None,
) -> BootImage:
    memory_map = memory_map or default_memory_map()
    imem_base, imem_size = memory_map.imem_base, memory_map.imem_size
    dmem_base, dmem_size = memory_map.dmem_base, memory_map.dmem_size
    raw_image = bytes(image)
    if not raw_image:
        raise ElfValidationError("ELF image is empty")

    _validate_region("IMEM", imem_base, imem_size)
    _validate_region("DMEM", dmem_base, dmem_size)

    try:
        elf = ELFFile(io.BytesIO(raw_image))
        return _parse_elf(
            elf,
            raw_image,
            imem_base=imem_base,
            imem_size=imem_size,
            dmem_base=dmem_base,
            dmem_size=dmem_size,
        )
    except ElfValidationError:
        raise
    except (ELFError, KeyError, struct.error, TypeError, ValueError) as error:
        raise ElfValidationError(f"malformed ELF image: {error}") from error


def _parse_elf(
    elf: ELFFile,
    raw_image: bytes,
    *,
    imem_base: int,
    imem_size: int,
    dmem_base: int,
    dmem_size: int,
) -> BootImage:
    _validate_header(elf)
    _validate_riscv_attributes(elf)

    load_segments: list[LoadSegment] = []
    program_ranges: list[_ProgramRange] = []
    for index, segment in enumerate(elf.iter_segments()):
        segment_type = segment["p_type"]
        if segment_type != "PT_LOAD":
            if segment_type not in _ALLOWED_METADATA_SEGMENTS:
                raise ElfValidationError(
                    f"unsupported program segment {index}: {segment_type}"
                )
            continue

        file_size = int(segment["p_filesz"])
        memory_size = int(segment["p_memsz"])
        file_offset = int(segment["p_offset"])
        virtual_address = int(segment["p_vaddr"])
        load_address = int(segment["p_paddr"])
        flags = int(segment["p_flags"])
        alignment = int(segment["p_align"])

        if file_size > memory_size:
            raise ElfValidationError(
                f"PT_LOAD segment {index} has p_filesz greater than p_memsz"
            )
        if alignment not in (0, 1) and alignment & (alignment - 1):
            raise ElfValidationError(
                f"PT_LOAD segment {index} has non-power-of-two alignment"
            )
        if alignment > 1 and virtual_address % alignment != file_offset % alignment:
            raise ElfValidationError(
                f"PT_LOAD segment {index} violates ELF alignment"
            )
        if flags & _PF_EXECUTE and flags & _PF_WRITE:
            raise ElfValidationError(
                f"PT_LOAD segment {index} is both writable and executable"
            )
        if flags & _PF_EXECUTE and load_address != virtual_address:
            raise ElfValidationError(
                f"PT_LOAD segment {index} has distinct executable load and runtime addresses"
            )

        virtual_end = _checked_end(
            virtual_address, memory_size, f"PT_LOAD segment {index} virtual range"
        )
        file_virtual_end = _checked_end(
            virtual_address, file_size, f"PT_LOAD segment {index} file range"
        )
        if memory_size and not (
            _range_contains(imem_base, imem_size, virtual_address, memory_size)
            or _range_contains(dmem_base, dmem_size, virtual_address, memory_size)
        ):
            raise ElfValidationError(
                f"PT_LOAD segment {index} virtual range is outside IMEM and DMEM"
            )

        if file_offset > len(raw_image) or file_size > len(raw_image) - file_offset:
            raise ElfValidationError(
                f"PT_LOAD segment {index} file range exceeds the ELF image"
            )

        load_end = _checked_end(
            load_address, file_size, f"PT_LOAD segment {index} load range"
        )
        if file_size and not _range_contains(
            imem_base, imem_size, load_address, file_size
        ):
            raise ElfValidationError(
                f"PT_LOAD segment {index} file-backed bytes are outside IMEM"
            )

        current_range = _ProgramRange(
            virtual_start=virtual_address,
            virtual_end=virtual_end,
            load_start=load_address,
            load_end=load_end,
            file_virtual_end=file_virtual_end,
            flags=flags,
        )
        _reject_overlap(index, current_range, program_ranges)
        program_ranges.append(current_range)

        if file_size:
            load_segments.append(
                LoadSegment(
                    load_address=load_address,
                    virtual_address=virtual_address,
                    memory_size=memory_size,
                    flags=flags,
                    data=raw_image[file_offset:file_offset + file_size],
                )
            )

    if not load_segments:
        raise ElfValidationError("ELF contains no file-backed PT_LOAD segments")

    entry_pc = int(elf.header["e_entry"])
    if entry_pc % 4:
        raise ElfValidationError("ELF entry point is not RV32I instruction aligned")
    if not any(
        program_range.flags & _PF_EXECUTE
        and program_range.virtual_start <= entry_pc
        and entry_pc + 4 <= program_range.file_virtual_end
        and program_range.load_start
        + entry_pc
        - program_range.virtual_start
        == entry_pc
        for program_range in program_ranges
    ):
        raise ElfValidationError(
            "ELF entry point is not backed by a locally loaded executable segment"
        )

    return BootImage(
        entry_pc=entry_pc,
        segments=tuple(sorted(load_segments, key=lambda item: item.load_address)),
        symbols=_read_symbols(elf),
        sha256=hashlib.sha256(raw_image).hexdigest(),
    )


def _validate_header(elf: ELFFile) -> None:
    if elf.elfclass != 32:
        raise ElfValidationError("ELF must use the 32-bit class")
    if not elf.little_endian:
        raise ElfValidationError("ELF must use little-endian encoding")
    if elf.header["e_type"] != "ET_EXEC":
        raise ElfValidationError("ELF must be an executable image")
    if elf.header["e_machine"] != "EM_RISCV":
        raise ElfValidationError("ELF machine must be RISC-V")
    if elf.header["e_version"] != "EV_CURRENT":
        raise ElfValidationError("ELF header version is unsupported")
    if int(elf.header["e_flags"]) != 0:
        raise ElfValidationError(
            "ELF flags require extensions outside the RV32I soft-float profile"
        )


def _validate_riscv_attributes(elf: ELFFile) -> None:
    section = elf.get_section_by_name(".riscv.attributes")
    if not isinstance(section, RISCVAttributesSection):
        raise ElfValidationError("ELF is missing RISC-V build attributes")

    architecture_values: set[str] = set()
    stack_alignments: set[int] = set()
    for subsection in section.iter_subsections("riscv"):
        for file_attributes in subsection.iter_subsubsections("TAG_FILE"):
            for attribute in file_attributes.iter_attributes():
                if attribute.tag == "TAG_ARCH":
                    architecture_values.add(str(attribute.value))
                elif attribute.tag == "TAG_STACK_ALIGN":
                    stack_alignments.add(int(attribute.value))

    if len(architecture_values) != 1:
        raise ElfValidationError("ELF must declare one RISC-V architecture")
    architecture = next(iter(architecture_values))
    if _RV32I_ARCH.fullmatch(architecture) is None:
        raise ElfValidationError(
            f"ELF architecture {architecture!r} is outside the RV32I profile"
        )
    if stack_alignments != {16}:
        raise ElfValidationError(
            "ELF must declare the 16-byte RV32I stack alignment"
        )


def _read_symbols(elf: ELFFile) -> Mapping[str, ElfSymbol]:
    symbols: dict[str, ElfSymbol] = {}
    for section in elf.iter_sections():
        if not isinstance(section, SymbolTableSection):
            continue
        for symbol in section.iter_symbols():
            name = symbol.name
            binding = symbol["st_info"]["bind"]
            if (
                not name
                or binding not in ("STB_GLOBAL", "STB_WEAK")
                or symbol["st_shndx"] == "SHN_UNDEF"
            ):
                continue

            candidate = ElfSymbol(
                name=name,
                address=int(symbol["st_value"]),
                size=int(symbol["st_size"]),
                symbol_type=str(symbol["st_info"]["type"]),
            )
            previous = symbols.get(name)
            if previous is not None and previous != candidate:
                raise ElfValidationError(f"ELF has conflicting symbols named {name}")
            symbols[name] = candidate
    return symbols


def _validate_region(name: str, base: int, size: int) -> None:
    if base < 0 or size <= 0 or base + size > _ADDRESS_SPACE_SIZE:
        raise ValueError(f"invalid {name} region")


def _checked_end(start: int, size: int, description: str) -> int:
    if start < 0 or size < 0 or start + size > _ADDRESS_SPACE_SIZE:
        raise ElfValidationError(f"{description} overflows the RV32 address space")
    return start + size


def _range_contains(base: int, size: int, address: int, length: int) -> bool:
    return address >= base and length <= size and address - base <= size - length


def _ranges_overlap(first_start: int, first_end: int, second_start: int, second_end: int) -> bool:
    return first_start < second_end and second_start < first_end


def _reject_overlap(
    index: int,
    current: _ProgramRange,
    previous_ranges: list[_ProgramRange],
) -> None:
    for previous in previous_ranges:
        if _ranges_overlap(
            current.virtual_start,
            current.virtual_end,
            previous.virtual_start,
            previous.virtual_end,
        ):
            raise ElfValidationError(
                f"PT_LOAD segment {index} overlaps another virtual range"
            )
        if _ranges_overlap(
            current.load_start,
            current.load_end,
            previous.load_start,
            previous.load_end,
        ):
            raise ElfValidationError(
                f"PT_LOAD segment {index} overlaps another file-backed load range"
            )