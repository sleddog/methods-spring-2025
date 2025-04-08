#!/bin/bash

# Check if an argument is passed
if [ -z "$1" ]; then
    # No arguments passed
    python3 ./problems/fizzbuzz/python/bartzcarter/main.py
else
    # Argument passed
    python3 ./problems/fizzbuzz/python/bartzcarter/main.py "$1"
fi