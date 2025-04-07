#!/bin/bash

python3 -m unittest discover -s . -p "test_*.py"

if [ $? -eq 0 ]; then
    echo "Tests passed."
else
    echo "Some tests failed. Check output above."
fi