import sys

def bobcat_fizzbuzz(n):
    results = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            results.append("BobCat\n")
        elif i % 5 == 0:
            results.append("Cat\n")
        elif i % 3 == 0:
            results.append("Bob\n")
        else:
            results.append(str(i) + "\n")
    return "".join(results)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <number>")
    else:
        try:
            num = int(sys.argv[1])
            print(bobcat_fizzbuzz(num))
        except ValueError:
            print("Error: Please enter a valid integer.")
