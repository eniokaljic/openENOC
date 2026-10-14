# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: AGPL-3.0-or-later

import os
import sys
import tempfile
from pathlib import Path

import pytest

DV_ROOT = Path(__file__).resolve().parent
BUILD_ROOT = DV_ROOT.parent / "build/dv"
SHARED_OUTPUT = BUILD_ROOT / "common/pytest"


def set_output_paths(path):
    suite = path.parent if path.is_file() else path
    output = SHARED_OUTPUT
    if suite.is_relative_to(DV_ROOT) and (suite / "Makefile").is_file():
        output = BUILD_ROOT / suite.relative_to(DV_ROOT)
    sys.pycache_prefix = str(output / "__pycache__")
    os.environ["PYTHONPYCACHEPREFIX"] = sys.pycache_prefix
    temporary_dir = output / "tmp"
    temporary_dir.mkdir(parents=True, exist_ok=True)
    os.environ["TMPDIR"] = str(temporary_dir)
    tempfile.tempdir = str(temporary_dir)
    return output


set_output_paths(DV_ROOT)

# Pytest may cache this bootstrap module before its output hooks become active.
bootstrap_cache = DV_ROOT / "__pycache__"
if bootstrap_cache.exists():
    target = SHARED_OUTPUT / "__pycache__" / "bootstrap"
    target.mkdir(parents=True, exist_ok=True)
    for cache_file in bootstrap_cache.iterdir():
        cache_file.replace(target / cache_file.name)
    bootstrap_cache.rmdir()


def pytest_collectstart(collector):
    set_output_paths(collector.path)


def pytest_runtest_setup(item):
    set_output_paths(item.path)


@pytest.fixture
def sim_build_dir(request):
    output = set_output_paths(request.path)
    case_name = request.node.name.replace("[", "-").replace("]", "")
    return str(output / "sim_build/pytest" / case_name)


@pytest.fixture
def sim_trace_args(sim_build_dir):
    arguments = ["--trace-file", str(Path(sim_build_dir) / "dump.fst")]
    if int(os.environ.get("WAVES", "0")):
        arguments.insert(0, "--trace")
    return arguments
