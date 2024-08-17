#!/usr/bin/env bash

mkdir -p results

python simulate.py --num-steps 500 \
                   --input-file reference/initial.csv \
                   --output-file results/final.csv

# check if the files differ using the diff command
if diff results/final.csv reference/reference.csv >/dev/null 2>&1; then
    echo "SUCCESS: The files are identical."
    exit 0
else
    echo "ERROR: The files differ."
    exit 1
fi
