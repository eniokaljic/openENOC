# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: AGPL-3.0-or-later

__version__ = "0.0.1"

__all__ = [
    "HardwareInterface",
    "HardwareTest",
    "RTLSimulator",
    "Testbench",
]

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BUILD_PYTHON = ROOT / "build" / "python"

if str(BUILD_PYTHON) not in sys.path:
    sys.path.insert(0, str(BUILD_PYTHON))
