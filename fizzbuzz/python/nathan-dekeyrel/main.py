import sys

def fizzbuzz(n: int) -> None:
    rules = {
            3: "Bob",
            5: "Cat"
            }

    for i in range(1, n+1):
        output = ""
        for divisor, word in rules.items():
            if i % divisor == 0:
                output += word

        print(output or i)


if __name__ == "__main__":
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("Error: Please provide a valid number")
        sys.exit(1)

    fizzbuzz(n)
