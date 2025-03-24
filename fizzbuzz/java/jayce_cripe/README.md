# FizzBuzz Java Implementation

## What is FizzBuzz

FizzBuzz is a problem that prints numbers from 1 to n, but (for our class)
Multiples of 3, print `Bob`
Multiples of 5, print `Cat`
Multiples of both 3 and 5, print `Bobcat`

## How to run:

1. Clone the repo if you haven't already
2. Go to `fizzbuzz/java/jayce-cripe` directory
3. Make `run.sh` script executable:
   ```bash
   chmod +x run.sh
    ```

4. Run the script with a number as the input argument (15 is an example)
    ```bash
   ./run.sh 15
    ```

5. The output should resemble:
   `1`
   `2`
   `Bob`
   `4`
   `Cat`
   `Bob`
   `7`
   `8`
   `Bob`
   `Cat`
   `11`
   `Bob`
   `13`
   `14`
   `BobCat`

## How to test
1. Clone the repo if you haven't already
2. Go to `fizzbuzz/java/jayce-cripe` directory
3. Make `run.sh --test` script executable:
   ```bash
   chmod +x run.sh
    ```

4. Run the script with a number as the input argument (15 is an example)
    ```bash
   ./run.sh --test
    ```

5. The output should resemble:
``` plaintext
💚 Thanks for using JUnit! Support its development at https://junit.org/sponsoring

╷
├─ JUnit Platform Suite ✔
├─ JUnit Jupiter ✔
│  └─ FizzBuzzTest ✔
│     ├─ testNoArguments() ✔
│     └─ testFizzBuzzOutput() ✔
└─ JUnit Vintage ✔

Test run finished after 125 ms
[         4 containers found      ]
[         0 containers skipped    ]
[         4 containers started    ]
[         0 containers aborted    ]
[         4 containers successful ]
[         0 containers failed     ]
[         2 tests found           ]
[         0 tests skipped         ]
[         2 tests started         ]
[         0 tests aborted         ]
[         2 tests successful      ]
[         0 tests failed          ]
```