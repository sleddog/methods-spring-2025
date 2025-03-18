import sys

def bobcatbuzz(n):
    for i in range(1, n + 1):
        if i % 5 == 0 and i % 3 == 0:
            print("BobCat")
        elif i % 5 == 0:
            print("Cat")
        elif i % 3 == 0:
            print("Bob")
        else:
            print(i)

if __name__ == "__main__":

    print("\nOutput:\n")
    bobcatbuzz(int(sys.argv[1]))
