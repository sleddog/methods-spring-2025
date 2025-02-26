# FizzBuzz Python and Shell Script

This project includes a Python program that implements a simple **FizzBuzz** algorithm with customized output, along with a shell script to run the Python program with optional arguments.

### FizzBuzz Logic

The program prints numbers from 1 to a given number `n` (defaults to 15 if no argument is provided). However, for numbers divisible by:

- 3, it prints **"Bob"**,
- 5, it prints **"Cat"**,
- and for numbers divisible by both 3 and 5, it prints **"BobCat"**.

### Files in the Project

- **`main.py`**: The Python program that contains the FizzBuzz implementation.
- **`run.sh`**: The shell script that checks if an argument is passed. If an argument is provided, it runs the Python script with that argument; if not, it runs the Python script with the default value `15`.

---

## How to Use

### 1. **Run the Python Program Directly**

You can run the Python program directly by executing:

```bash
python3 main.py [n]
```

from directory the file lives in or ...

### 2. **Run the Python Program with the Shell Script from the repo top level directory**

```bash
./fizzbuzz/python/bartzcarter/run.sh [n]
```
