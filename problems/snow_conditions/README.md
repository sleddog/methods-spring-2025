# Snow Conditions Python Program 

## About
This project implements a simple Python program that tells you the snow condition based on the temperature (int) inputted.

It includes a shell script and a Flask web API to run the logic

## Files in Project
- 'main.py'
  A Python program that contains the logic for predicting snow condition
- 'run.sh'
  A shell script that collects user input and runs main.py with the provided input
- 'app.py'
  A Flask web server exposing the snow conditions logic as an API

## Usage 

### 1. Running the Shell Script

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
### 2. Running the server

Start the flask server with python app.py

Then use curl to call

'''
curl "http://127.0.0.1:5000/snow_condition?temp=<int>"
'''

### Example 
'''
curl "http://127.0.0.1:5000/snow_condition?temp=25"
'''

**Output**
'''
{
  "temperature": 25,
  "condition": "Packed Snow"
}
'''


## Installation and Setup (shell script)

1. Ensure you have Python installed
2. Give execution permissions to the shell script:
'''sh
chmod +x run.sh
'''
3. Run the script

## Installation and Setup (server)

1. Ensure you have Python installed
2. Install Flask
'''sh
pip install flask
'''
3. Run the server
