# Count Mountain Peaks

This is my implementation of the Count Mountain Peaks algorithm using python

## Introduction

This is a program that calculates the number of mountain peaks from a list of elevation values. The program takes elevation data as input and returns the number of peaks based on the given algorithm.

## Examples

Input: [4500, 7200, 6800, 8100, 7900, 9000, 8500]  
Output: 2  (Peaks at 7200 and 9000 feet)  

Input: [5000, 6000, 7000, 8000]  
Output: 0  (No peaks) 

## How to Use

To run the program, follow these steps:

1. Clone the repository to your local machine.
2. Run the Python script by passing a list of elevations.
3. Optionally, you can use the shell script to pass arguments easily.

## Example Usage

Command to run the Python script directly:

python ./count_mountain_peaks/python/sethullman/script.py 4500 7200 6800 8100 7900 9000 8500

Command to run with shell script

./count_mountain_peaks/python/sethullman/run.sh 4500 7200 6800 8100 7900 9000 8500

## Testing the count_mountain_peaks function

Unit tests can be found in `count_mountain_peaks/python/sethullman/test_Count_Mountain_Peaks.py`.

### **Running Unit Tests via Shell Script**

To run the tests, use the provided `run_tests.sh` shell script. This will exectute all tests and provide an output of test outputs.

**Make the shell script executable**:
```bash
chmod +x run_tests.sh
```

**Run the shell script**:
```bash
./run_tests.sh
```