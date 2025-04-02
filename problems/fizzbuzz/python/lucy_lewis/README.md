# Fizzbuzz

### Description
This project includes a Python implementation of the classic **FizzBuzz** challenge but with customized outputs. 

A  shell script is used to collect user input and run the Python program with the specified number.
The Python program then prints numbers from 1 to the given number *n*, applying the following rules: 
- For multiples of **3**, print **"Bob"**
- For multiples of **5**, print **"Cat"**
- For multiples of both **3 and 5**, print **"BobCat"**

## Files in the Project
- **main.py:**  
  A Python program that contains the FizzBuzz logic.
- **run.sh:**  
  A shell script that prompts the user for a number and then runs `main.py` with the provided input.

## Prerequisites
- **Python 3.x** must be installed on your system.

## How to Run the Program
1. Open a terminal and navigate to the project directory.
2. Make the shell script executable by running:   
   ```chmod +x run.sh```
3. Run the shell script with
   ```./run.sh```
4. Enter a number when prompted. 

## Unit Testing (Jayce)
- Have created a test.py file for unit tests on your fizzbuzz solution. Had to work around the call to main at the bottom of main.py so that's why there is some harder logic at the beginning of the testing file. 
- Have created run_test.sh which can be accessed by running: 
```chmod +x run_test.sh```
and followed by 
```./run_test.sh```
- NOTE: I tried not to change any of Lucy's work, but changed her ```run.sh``` to run python instead of python3 since Windows has an issue with that. 
