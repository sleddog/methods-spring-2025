# FizzBuzz Go Program with Shell Script

## Files

- `Fizzbuzz.go` - A Go program that prints "Bob" for multiples of 3, "Cat" for multiples of 5, and "BobCat" for multiples of both
- `run_fizzbuzz.sh` - A shell script to run the Go program
- `Fizzbuzz_test.go` - A Go test file containing unit tests for Fizzbuzz.go
- `run_tests.sh` - A shell script to run the Go test file
- `go.mod` - A Go module file that manages dependencies and organizes the project for testing and builds.
- `README.md` - README documentation file.
- `index.html` - HTML documentation 

## Usage

### Running the Script
The `run_fizzbuzz.sh` script allows you to run the FizzBuzz program without manually running Go commands.

```sh
./run_fizzbuzz.sh <number>
```

Replace `<number>` with an integer 

### Example
```sh
./run_fizzbuzz.sh 15
```
**Output:**
```
1
2
Bob
4
Cat
Bob
7
8
Bob
Cat
11
Bob
13
14
BobCat
```

## Installation & Setup

1. Ensure you have [Go installed](https://go.dev/doc/install)
2. Give execution permissions to the shell script:
   ```sh
   chmod +x run_fizzbuzz.sh
   ```
3. Run the script


## Testing
Unit tests for the FizzBuzz program are located in the Fizzbuzz_test.go file. These tests ensure the program's correctness by verifying its output against expected results.

### Unit Test Description
Since the FizzBuzz program prints to the console, a helper function, `getFizzbuzzOutput`, is used to capture the output and compare it with the expected result.

The go test file includes the following test cases:
- `TestJustNumber`: Verifies that the program correctly prints the number itself when it is neither a multiple of 3 nor 5.

- `TestBob`: Verifies that the program prints "Bob" for numbers that are multiples of 3.

- `TestCat`: Verifies that the program prints "Cat" for numbers that are multiples of 5.

- `TestBobCat`: Verifies the program prints "BobCat" for numbers that are multiples of both 3 and 5.

### Prerequisites for Running Tests
1. Make sure you have [Go installed](https://go.dev/doc/install)
2. Run `go mod tidy` to download all the dependencies listed in the go.mod file and remove any unused ones.

### Running the Unit Tests
1. Open a terminal and navigate to the project directory.
2. Make the shell script executable by running:   
   ```chmod +x run_tests.sh```
3. Run the shell script with
   ```./run_tests.sh```
   to execute the tests.


