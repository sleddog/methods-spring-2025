# Snow Conditions Python Program 

## About
This project implements a simple Python program that tells you the snow condition based on the temperature (int) inputted.

A shell script is used to collect input and run the program

## Files in Project
- 'main.py'
  A Python program that contains the logic for predicting snow condition
- 'run.sh'
  A shell script that collects user input and runs main.py with the provided input

## Usage 

### Running the Script

Use 'run.sh' along with an integer to launch the program

'''sh
./run.sh <int>
'''

Replace '<int>' with an integer

### Example
'''sh
./run.sh 25
'''

**Output**
'''
Packed Snow
'''

## Installation and Setup

1. Ensure you have Python installed
2. Give execution permissions to the shell script:
'''sh
chmod +x run.sh
'''

3. Run the script

