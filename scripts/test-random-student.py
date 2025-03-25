# test the random_student.py functions
import unittest

from random_student import read_students, create_pairings, write_pairings

def test_read_students():
    students = read_students("students.txt")
    assert len(students) == 11

def test_create_pairings():
    students = read_students("students.txt")
    pairings = create_pairings(students)
    assert len(pairings) == len(students)
    for student, pairing in pairings.items():
        assert student != pairing

def test_write_pairings():
    students = read_students("students.txt")
    pairings = create_pairings(students)
    write_pairings(pairings, "test_pairings.txt")
    with open("test_pairings.txt", "r") as file:
        lines = file.readlines()
        assert len(lines) == len(students)
        for line in lines:
            assert "is adding unit tests to" in line

if __name__ == '__main__':
    test_read_students()
    test_create_pairings()
    test_write_pairings()
    print("All tests passed.")