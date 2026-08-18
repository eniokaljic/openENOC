#!/usr/bin/env bash
# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: AGPL-3.0-or-later

set -euo pipefail

export PATH=/usr/bin:$PATH

case "${1:-}" in
    pytest)
        pytest test_openenoc_full_endpoint.py -v
        ;;
    waves)
        WAVES=1 make
        ;;
    clean)
        rm -f results.xml dump.fst
        rm -rf sim_build .pytest_cache __pycache__
        ;;
    *)
        echo "Usage: ./run_tests.sh [pytest|waves|clean]"
        exit 1
        ;;
esac
