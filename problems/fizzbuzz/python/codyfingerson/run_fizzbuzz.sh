#!/bin/bash

if [ "$#" -eq 0 ]; then
    echo "Usage: ./run_fizzbuzz.sh <num1> <num2> ..."
    exit 1
fi

python3 main.py "$@"