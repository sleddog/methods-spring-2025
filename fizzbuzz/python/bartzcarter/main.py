import sys

def fizzbuzz(n):
    for i in range(1,int(n)+1):
        # Div by both 3 and 5
        if i % 3 == 0 and i % 5 == 0:
            print("BobCat")
        # Div by 5
        elif i % 5 == 0:
            print("Cat")
        # Div by 3
        elif i % 3 == 0:
            print("Bob")
        # Not div by either 3 or 5
        else:
            print(i)

if __name__ == "__main__":
    # Argument passed
    if len(sys.argv) > 1:
        print(f"Calling fizzbuzz with {sys.argv[1]}")
        fizzbuzz(sys.argv[1])
    # No argument passed
    else:
        print("No arguments passed ... calling fizzbuzz() with 15")
        fizzbuzz(15)
