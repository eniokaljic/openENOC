# SPDX-FileCopyrightText: 2026 Kerim Bavcic
# SPDX-License-Identifier: AGPL-3.0-or-later

import subprocess
import sys
from pathlib import Path
from xml.etree import ElementTree


def main(paths):
    reports = Path(__file__).resolve().parents[2] / "build/dv/iss/reports"
    reports.mkdir(parents=True, exist_ok=True)
    suite = ElementTree.Element(
        "testsuite", name="native-smoke", tests=str(len(paths)), failures="0",
    )
    failures = 0
    for path in paths:
        result = subprocess.run([path], capture_output=True, text=True, check=False)
        case = ElementTree.SubElement(suite, "testcase", name=Path(path).name)
        if result.stdout:
            ElementTree.SubElement(case, "system-out").text = result.stdout
        if result.stderr:
            ElementTree.SubElement(case, "system-err").text = result.stderr
        if result.returncode:
            failures += 1
            ElementTree.SubElement(
                case, "failure", message=f"exit status {result.returncode}",
            ).text = result.stderr or result.stdout
        print(f"{Path(path).name}: {'PASS' if result.returncode == 0 else 'FAIL'}")
        if result.returncode and (result.stderr or result.stdout):
            print(result.stderr or result.stdout, file=sys.stderr)

    suite.set("failures", str(failures))
    ElementTree.ElementTree(suite).write(
        reports / "native-smoke.xml", encoding="utf-8", xml_declaration=True,
    )
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))