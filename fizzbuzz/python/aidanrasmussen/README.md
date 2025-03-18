# FizzBuzz

This program contains a solution to the FizzBuzz problem, 
Write a function that prints numbers from 1 to n, but:
For multiples of 3, print "Bob"
For multiples of 5, print "Cat".
For multiples of both 3 and 5, print "BobCat"

## How to run

Simply run the run.sh script and when prompted enter a number.

## Testing the bobcatbuzz function

Unit tests can be found in `fizzbuzz/python/aidanrasmussen/test_bobcatbuzz.py`.

### **Running the Tests via Shell Script**

To run the tests, you can use the provided `run_tests.sh` shell script. This will execute all unit tests and display whether they pass or fail.

### **Steps to Run the Tests:**

1. **Make the shell script executable**:
    ```bash
    chmod +x run_tests.sh
    ```

2. **Run the shell script to invoke the tests**:
    ```bash
    ./run_tests.sh
    ```

### **Test Implementation Details**

The tests are written using Python's `unittest` framework. The function `bobcatbuzz` prints output to the console, so the tests use `StringIO` to capture and compare this output to the expected results.

The tests check the following cases:

- **test_bob**: Verifies that the program prints "Bob" for multiples of 3.
- **test_cat**: Verifies that the program prints "Cat" for multiples of 5.
- **test_bobcat**: Verifies that the program prints "BobCat" for multiples of both 3 and 5.
- **test_no_bobcat**: Verifies that the program prints the correct numbers when neither 3 nor 5 is a factor.

