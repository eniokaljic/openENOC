# SPDX-FileCopyrightText: 2026 Kerim Bavcic
# SPDX-License-Identifier: AGPL-3.0-or-later

import os
import struct
import unittest
from dataclasses import replace

from openenoc_iss import ElfValidationError, load_elf, load_memory_map
from openenoc_iss.elf import parse_elf


class ElfLoaderTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.path = os.environ["OPENENOC_FIRMWARE_ELF"]
        cls.startup_path = os.environ["OPENENOC_STARTUP_FIRMWARE_ELF"]
        with open(cls.path, "rb") as firmware_file:
            cls.image = firmware_file.read()

    def test_loads_current_firmware_layout(self):
        boot_image = load_elf(self.path)

        self.assertEqual(boot_image.entry_pc, 0)
        self.assertEqual(len(boot_image.segments), 1)
        self.assertEqual(boot_image.segments[0].load_address, 0)
        self.assertEqual(boot_image.segments[0].virtual_address, 0)
        self.assertGreater(len(boot_image.segments[0].data), 0)
        self.assertEqual(
            boot_image.symbol_address("csr_smoke_status"), 0x10000000
        )
        self.assertEqual(boot_image.symbols["csr_smoke_status"].size, 4)
        self.assertEqual(len(boot_image.sha256), 64)

    def test_preserves_startup_load_and_runtime_addresses(self):
        boot_image = load_elf(self.startup_path)
        data_segment = next(
            segment
            for segment in boot_image.segments
            if segment.virtual_address == 0x10000000
        )

        self.assertEqual(len(boot_image.segments), 2)
        self.assertEqual(
            data_segment.load_address,
            boot_image.symbol_address("__data_load_start"),
        )
        self.assertEqual(
            data_segment.virtual_address,
            boot_image.symbol_address("__data_start"),
        )
        self.assertEqual(data_segment.data, bytes.fromhex("78563412efcdab89"))
        self.assertEqual(len(data_segment.data), 8)
        self.assertEqual(data_segment.memory_size, 16)
        self.assertEqual(
            boot_image.symbol_address("startup_bss"), 0x10000008
        )
        self.assertEqual(
            boot_image.symbol_address("iss_startup_status"), 0x1000000C
        )

    def test_rejects_firmware_for_another_endpoint_map(self):
        memory_map = load_memory_map(os.environ["OPENENOC_MEMORY_MAP"])
        other_map = replace(memory_map, dmem_base=0x30000000)
        with self.assertRaises(ElfValidationError):
            load_elf(self.startup_path, memory_map=other_map)

    def test_rejects_invalid_headers_and_segments(self):
        load_headers = self._load_program_headers(self.image)
        self.assertGreaterEqual(len(load_headers), 2)

        mutations = {
            "truncated": b"\x7fELF",
            "ELF64": self._patch_byte(4, 2),
            "big-endian": self._patch_byte(5, 2),
            "shared-object": self._patch_u16(16, 3),
            "wrong-machine": self._patch_u16(18, 3),
            "unsupported-flags": self._patch_u32(36, 1),
            "wrong-isa-profile": self.image.replace(
                b"rv32i2p1", b"rv32e2p1", 1
            ),
            "unaligned-entry": self._patch_u32(24, 2),
            "unsupported-segment": self._patch_u32(
                self._program_header_offsets(self.image)[0], 2
            ),
            "file-range-outside-image": self._patch_u32(
                load_headers[0] + 4, len(self.image) - 1
            ),
            "load-range-outside-imem": self._patch_u32(
                load_headers[0] + 12, 0x00008000
            ),
            "relocated-executable-segment": self._patch_u32(
                load_headers[0] + 12, 4
            ),
            "filesz-greater-than-memsz": self._patch_u32(
                load_headers[0] + 20,
                struct.unpack_from("<I", self.image, load_headers[0] + 16)[0]
                - 1,
            ),
            "overlapping-virtual-ranges": self._patch_many(
                (load_headers[1] + 8, 0),
                (load_headers[1] + 20, 4),
            ),
        }

        for description, image in mutations.items():
            with self.subTest(description=description):
                with self.assertRaises(ElfValidationError):
                    parse_elf(image)

    @staticmethod
    def _program_header_offsets(image):
        table_offset = struct.unpack_from("<I", image, 28)[0]
        entry_size = struct.unpack_from("<H", image, 42)[0]
        entry_count = struct.unpack_from("<H", image, 44)[0]
        return [
            table_offset + index * entry_size for index in range(entry_count)
        ]

    @classmethod
    def _load_program_headers(cls, image):
        return [
            offset
            for offset in cls._program_header_offsets(image)
            if struct.unpack_from("<I", image, offset)[0] == 1
        ]

    def _patch_byte(self, offset, value):
        image = bytearray(self.image)
        image[offset] = value
        return bytes(image)

    def _patch_u16(self, offset, value):
        image = bytearray(self.image)
        struct.pack_into("<H", image, offset, value)
        return bytes(image)

    def _patch_u32(self, offset, value):
        image = bytearray(self.image)
        struct.pack_into("<I", image, offset, value)
        return bytes(image)

    def _patch_many(self, *patches):
        image = bytearray(self.image)
        for offset, value in patches:
            struct.pack_into("<I", image, offset, value)
        return bytes(image)


if __name__ == "__main__":
    unittest.main()