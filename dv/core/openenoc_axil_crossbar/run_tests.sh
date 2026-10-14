#!/usr/bin/env bash
# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: AGPL-3.0-or-later

set -euo pipefail

source "$(dirname -- "${BASH_SOURCE[0]}")/../../common/sim_paths.sh"

export PATH=/usr/bin:$PATH

case "${1:-}" in
    pytest)
        pytest test_openenoc_axil_crossbar.py -v
        ;;
    waves)
        WAVES=1 make
        ;;
    clean)
        rm -f "$dv_sim_output/sim_build/results.xml" "$dv_sim_output/sim_build/dump.fst"
        rm -rf "$dv_sim_output/sim_build" "$dv_sim_output/__pycache__" "$dv_sim_output/tmp" \
            .pytest_cache __pycache__
        ;;
    *)
        echo "Usage: ./run_tests.sh [pytest|waves|clean]"
        exit 1
        ;;
esac
