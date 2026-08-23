#!/usr/bin/env bash
# SPDX-FileCopyrightText: 2026 Kerim Bavcic
# SPDX-License-Identifier: AGPL-3.0-or-later

export PATH=/usr/bin:$PATH

if [ "$1" = "pytest" ]; then
    rm -rf sim_build
    pytest test_openenoc_axis_forwarding_engine.py -v
elif [ "$1" = "waves" ]; then
    rm -rf sim_build
    WAVES=1 make
    gtkwave dump.fst &
elif [ "$1" = "clean" ]; then
    rm results.xml
    rm dump.fst
    rm -rf sim_build
    rm -rf .pytest_cache
    rm -rf __pycache__
else
    echo "Usage: ./run_tests.sh [pytest|waves|clean]"
fi
