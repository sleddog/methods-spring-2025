def fizzbuzz(n):
    output = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            output.append("BobCat")
        elif i % 3 == 0:
            output.append("Bob")
        elif i % 5 == 0:
            output.append("Cat")
        else:
            output.append(i)
    return output