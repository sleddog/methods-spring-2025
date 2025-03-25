#!/bin/bash

echo "running unit tests"


python -m unittest test_fizzbuzz.py

if [ $? -eq 0 ]; then
  echo "All tests passed"
else
  echo "Test Failed"
fi