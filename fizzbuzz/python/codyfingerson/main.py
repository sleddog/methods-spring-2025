import sys

def bobcat_fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "BobCat"
    elif n % 5 == 0:
        return "Cat"
    elif n % 3 == 0 or n % 5 == 0:
        return "Bob"
    else:
        return str(n)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <num1> <num2> ...")
    else:
        numbers = map(int, sys.argv[1:])
        results = [bobcat_fizzbuzz(num) for num in numbers]
        print(" ".join(results))
