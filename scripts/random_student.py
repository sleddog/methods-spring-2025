import random

def read_students(file_name):
    with open(file_name, 'r') as file:
        return [line.strip() for line in file.readlines()]

def create_pairings(students):
    pairings = {}
    available_students = students.copy()
    current_student = 0
    while(len(available_students) > 0):
        student = students[current_student]
        i = random.randint(0, len(available_students) - 1)
        pairing = available_students[i]
        if student == pairing:
            continue
        pairings[student] = pairing
        # remove the student from the list
        available_students.pop(i)
        current_student += 1
    return pairings

def write_pairings(pairings, file_name="pairings.txt"):
    with open(file_name, 'w') as file:
        for student, pairing in pairings.items():
            file.write(f"{student} is adding unit tests to {pairing}'s solution\n")

def main(file_name):
    students = read_students(file_name)
    pairings = create_pairings(students)
    print(pairings)
    write_pairings(pairings)

if __name__ == '__main__':
    main("students.txt")