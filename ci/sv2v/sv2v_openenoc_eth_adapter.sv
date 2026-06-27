#!/usr/bin/env bash
# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: CERN-OHL-S-2.0 AND AGPL-3.0-or-later AND CC-BY-SA-4.0

set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"

DV_DIR="${REPO_ROOT}/dv/core/openenoc_eth_adapter"
HW_DIR="${REPO_ROOT}/hw"
CORE_DIR="${HW_DIR}/src/core"
TAXI_AXIS_DIR="${HW_DIR}/libs/taxi/src/axis/rtl"
TAXI_SYNC_DIR="${HW_DIR}/libs/taxi/src/sync/rtl"

OUT_DIR="${REPO_ROOT}/build/sv2v"
OUT_FILE="${OUT_DIR}/test_openenoc_eth_adapter.v"

mkdir -p "${OUT_DIR}"

sv2v \
    --top=test_openenoc_eth_adapter \
    -I "${CORE_DIR}" \
    -I "${TAXI_AXIS_DIR}" \
    -I "${TAXI_SYNC_DIR}" \
    -w "${OUT_FILE}" \
    "${TAXI_AXIS_DIR}/taxi_axis_if.sv" \
    "${TAXI_AXIS_DIR}/taxi_axis_adapter.sv" \
    "${TAXI_AXIS_DIR}/taxi_axis_async_fifo.sv" \
    "${TAXI_AXIS_DIR}/taxi_axis_async_fifo_adapter.sv" \
    "${TAXI_SYNC_DIR}/taxi_sync_reset.sv" \
    "${TAXI_SYNC_DIR}/taxi_sync_signal.sv" \
    "${CORE_DIR}/openenoc_eth_if.sv" \
    "${CORE_DIR}/openenoc_eth_adapter.sv" \
    "${DV_DIR}/test_openenoc_eth_adapter.sv"

grep -q "module test_openenoc_eth_adapter" "${OUT_FILE}" || {
    echo "error: sv2v output does not contain expected top module" >&2
    exit 1
}

echo "Generated: ${OUT_FILE}"
