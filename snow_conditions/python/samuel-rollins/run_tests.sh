#!/bin/bash
echo "running tests..."

python3 -m unittest test_snow_conditions.py

if [ $? -eq 0 ]; then
    echo "all tests passed"
else
    echo "test(s) Failed"
fi
