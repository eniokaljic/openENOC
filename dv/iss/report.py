# SPDX-FileCopyrightText: 2026 Kerim Bavcic
# SPDX-License-Identifier: AGPL-3.0-or-later

import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from importlib.metadata import version
from pathlib import Path
from xml.etree import ElementTree

sys.path.insert(0, str(Path(__file__).resolve().parent / "python"))
from openenoc_iss.elf import default_memory_map


ROOT = Path(__file__).resolve().parents[2]
BUILD = ROOT / "build/dv/iss"
REPORTS = BUILD / "reports"
SUITES = (
    "native-smoke", "python-smoke", "elf-smoke", "rtl-smoke", "rtl-lanes-smoke",
    "rtl-bridge-smoke", "rtl-lifecycle-smoke", "rtl-firmware-smoke",
    "rtl-startup-smoke", "rtl-system-smoke",
)
FIRMWARE = (
    ROOT / "build/sw/openenoc_endpoint_full/csr_smoke.elf",
    BUILD / "firmware/openenoc_endpoint_full/iss_startup.elf",
    BUILD / "firmware/openenoc_endpoint_full/iss_link.elf",
)


def command(*args):
    return subprocess.check_output(args, text=True).strip().splitlines()[0]


def build_report():
    memory_map = default_memory_map()
    results = {}
    for name in SUITES:
        suites = list(ElementTree.parse(REPORTS / f"{name}.xml").getroot().iter("testsuite"))
        counts = {
            field: sum(int(suite.get(field, "0")) for suite in suites)
            for field in ("tests", "failures", "errors", "skipped")
        }
        if not counts["tests"] or counts["failures"] or counts["errors"]:
            raise ValueError(f"{name} did not pass: {counts}")
        results[name] = counts

    spike_commit = command("git", "-C", str(ROOT / "libs/riscv-isa-sim"), "rev-parse", "HEAD")
    compatibility = json.loads((ROOT / "dv/iss/compatibility.json").read_text())
    if spike_commit != compatibility["spike"]["commit"]:
        raise ValueError("Spike checkout does not match compatibility.json")

    return {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "repository_commit": command("git", "-C", str(ROOT), "rev-parse", "HEAD"),
        "tracked_worktree_dirty": bool(subprocess.check_output(
            ("git", "-C", str(ROOT), "status", "--porcelain", "--untracked-files=no"),
            text=True,
        ).strip()),
        "spike_commit": spike_commit,
        "cpu_profile": compatibility["initial_cpu_profile"],
        "memory": {
            "private_imem": {"base": memory_map.imem_base, "size": memory_map.imem_size},
            "rtl_dmem": {"base": memory_map.dmem_base, "size": memory_map.dmem_size},
            "rtl_csr": {"base": memory_map.csr_base, "size": memory_map.csr_size},
        },
        "tools": {
            "python": sys.version.split()[0],
            "cocotb": version("cocotb"),
            "verilator": command("verilator", "--version"),
            "riscv_gcc": command("riscv64-unknown-elf-gcc", "--version"),
        },
        "firmware_sha256": {
            path.name: hashlib.sha256(path.read_bytes()).hexdigest()
            for path in FIRMWARE
        },
        "iss_library_sha256": hashlib.sha256(
            (BUILD / "lib/libopenenoc_iss.so").read_bytes()
        ).hexdigest(),
        "results": results,
    }


if __name__ == "__main__":
    report = build_report()
    path = REPORTS / "manifest.json"
    temporary = path.with_suffix(".tmp")
    temporary.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    temporary.replace(path)
    print(f"ISS regression manifest: {path}")