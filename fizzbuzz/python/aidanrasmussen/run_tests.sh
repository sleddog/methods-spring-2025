#!/bin/bash

# Run unit tests using python3 and unittest
echo "Running unit tests for bobcatbuzz..."
python3 -m unittest discover

# Check the exit status of the last command and print a message accordingly
if [ $? -eq 0 ]; then
    echo "All tests passed successfully!"
else
    echo "Some tests failed. Please check the output above."
fi