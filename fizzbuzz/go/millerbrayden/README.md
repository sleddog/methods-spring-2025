# FizzBuzz Go Program with Shell Script

## Files

- `Fizzbuzz.go` - A Go program that prints "Bob" for multiples of 3, "Cat" for multiples of 5, and "BobCat" for multiples of both
- `run_fizzbuzz.sh` - A shell script to run the Go program
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