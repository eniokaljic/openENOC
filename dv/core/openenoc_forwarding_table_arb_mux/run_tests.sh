#!/usr/bin/env bash
# SPDX-FileCopyrightText: 2026 Kerim Bavcic
# SPDX-License-Identifier: AGPL-3.0-or-later

source "$(dirname -- "${BASH_SOURCE[0]}")/../../common/sim_paths.sh"

export PATH=/usr/bin:$PATH

if [ "$1" = "pytest" ]; then
    rm -rf "$dv_sim_output/sim_build"
    pytest test_openenoc_forwarding_table_arb_mux.py -v
elif [ "$1" = "waves" ]; then
    rm -rf "$dv_sim_output/sim_build"
    WAVES=1 make
    gtkwave "$dv_sim_output/sim_build/dump.fst" &
elif [ "$1" = "clean" ]; then
    rm -f "$dv_sim_output/sim_build/results.xml"
    rm -f "$dv_sim_output/sim_build/dump.fst"
    rm -rf "$dv_sim_output/sim_build"
    rm -rf "$dv_sim_output/__pycache__" "$dv_sim_output/tmp" .pytest_cache
    rm -rf __pycache__
else
    echo "Usage: ./run_tests.sh [pytest|waves|clean]"
fi
