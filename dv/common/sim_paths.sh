#!/usr/bin/env bash
# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: AGPL-3.0-or-later

dv_suite_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[1]}")" && pwd)"
dv_root_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
dv_repository_dir="$(cd -- "$dv_root_dir/.." && pwd)"
dv_suite_path="${dv_suite_dir#"$dv_root_dir/"}"
dv_sim_output="$dv_repository_dir/build/dv/$dv_suite_path"

export PYTHONPYCACHEPREFIX="$dv_sim_output/__pycache__"
export TMPDIR="$dv_sim_output/tmp"
mkdir -p "$TMPDIR"
cd "$dv_suite_dir"
