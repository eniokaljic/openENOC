#!/usr/bin/env bash
export PATH=/usr/bin:$PATH

if [ "$1" = "pytest" ]; then
    rm -rf sim_build
    pytest test_openenoc_axis_demux.py -v
elif [ "$1" = "waves" ]; then
    rm -rf sim_build
    WAVES=1 make
    gtkwave dump.fst &
else
    echo "Usage: ./run.sh [pytest|waves]"
fi