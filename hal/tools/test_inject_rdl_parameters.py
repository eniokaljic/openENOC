#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Unit tests for C-header SystemRDL parameter formatting."""

import unittest

from inject_rdl_parameters import c_value
from openenoc_hwif import ExportError


class CValueTest(unittest.TestCase):
    def test_boolean_values(self) -> None:
        self.assertEqual(c_value(False), "0")
        self.assertEqual(c_value(True), "1")

    def test_unsigned_integer_width(self) -> None:
        self.assertEqual(c_value(0), "UINT32_C(0)")
        self.assertEqual(c_value((1 << 32) - 1), "UINT32_C(4294967295)")
        self.assertEqual(c_value(1 << 32), "UINT64_C(4294967296)")
        self.assertEqual(
            c_value((1 << 64) - 1),
            "UINT64_C(18446744073709551615)",
        )

    def test_signed_integer_width(self) -> None:
        self.assertEqual(c_value(-1), "INT32_C(-1)")
        self.assertEqual(c_value(-(1 << 31)), "INT32_C(-2147483648)")
        self.assertEqual(c_value(-(1 << 31) - 1), "INT64_C(-2147483649)")
        self.assertEqual(
            c_value(-(1 << 63)),
            "INT64_C(-9223372036854775808)",
        )

    def test_out_of_range_integer(self) -> None:
        with self.assertRaises(ExportError):
            c_value(1 << 64)
        with self.assertRaises(ExportError):
            c_value(-(1 << 63) - 1)

    def test_string_value(self) -> None:
        self.assertEqual(c_value('a\\b"c'), '"a\\\\b\\"c"')


if __name__ == "__main__":
    unittest.main()
