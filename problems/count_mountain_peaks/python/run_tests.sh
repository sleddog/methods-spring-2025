#!/bin/bash

echo "Running unit tests for Count_Mountain_Peaks..."
python3 -m unittest discover
exit_code=$?

if [ $exit_code -eq 0 ]; then
  echo "All tests passed successfully"
else
  echo "Some tests failed. Check output for details"
fi

exit $exit_code