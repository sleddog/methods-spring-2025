#!/bin/bash
echo "running tests..."

python -m unittest test.py

if [ $? -eq 0 ]; then
    echo "all tests passed"
else
    echo "test(s) Failed"
fi
