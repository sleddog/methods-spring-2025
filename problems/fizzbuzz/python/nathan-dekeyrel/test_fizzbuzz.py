import unittest
from main import fizzbuzz
import sys
from io import StringIO


class TestFizzBuzz(unittest.TestCase):

    def capture(self, n):
        output = StringIO()
        sys.stdout = output
        fizzbuzz(n)
        return output.getvalue().strip().split('\n')

    def test_bob(self):
        self.assertEqual(["1", "2", "Bob"], self.capture(3))

    def test_cat(self):
        self.assertEqual(["1", "2", "Bob", "4", "Cat"], self.capture(5))

    def test_bobcat(self):
        self.assertEqual(["1", "2", "Bob", "4", "Cat", "Bob", "7", "8", "Bob", "Cat", "11", "Bob", "13", "14", "BobCat"], self.capture(15))


if __name__ == '__main__':
    unittest.main()
