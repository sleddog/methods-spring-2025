# FizzBuzz Implementation

By: Nathan Dekeyrel

## What This Program Does

This program implements the classic FizzBuzz problem with a twist. It prints numbers from 1 to n, but:

- For multiples of 3, it prints "Bob"
- For multiples of 5, it prints "Cat"
- For multiples of both 3 and 5, it prints "BobCat"

## Implementation Approach

Fizzbuzz itself is a fairly straightforward problem. It can be solved using a couple if-statements in a loop to check a set of rules. A common follow-up to this problem is seeing how a programmer would modify their code to handle changes to the rules. My implementation uses a dictionary/map to store the rules. This design choice provides:

- **Extensibility:** New rules can be added by simply adding a new entry to the map
- **Maintainability:** Rules can be modified in one central location
- **Separation of concerns:** The rules are separated from the logic that applies them

## How to Run

The program can be run using the provided shell script:

For example:

```
./run.sh 15
```

The shell script executes the following command:

```
python main.py 15
```

## Example Output

Running `./run.sh` produces:

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

## Unit Testing

to run the unit tests in the `test_fizzbuzz.py` file simply run the `run_test.sh` file

you may have to update the permissions of `run_test.sh` by running `chmod +x run_test.sh`

The final line of the output will tell you if the tests have passed or failed

## API

This solution is also available via an API. You can spin up a local server using `python app.py`, and in another terminal window, run `curl http://localhost:5000/fizzbuzz` to get back:
```
  "result": [
    "1",
    "2",
    "Bob",
    "4",
    "Cat",
    "Bob",
    "7",
    "8",
    "Bob",
    "Cat",
    "11",
    "Bob",
    "13",
    "14",
    "BobCat"
  ]

```

You can also pass an optional argument like `curl http://localhost:5000/fizzbuzz?number=5` to get back:
```
  "result": [
    "1",
    "2",
    "Bob",
    "4",
    "Cat"
  ]
```
