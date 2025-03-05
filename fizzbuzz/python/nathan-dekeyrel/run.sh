#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Usage: ./run.sh [number]"
    exit 1
fi

python main.py $1
