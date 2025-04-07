import sys
import unittest
from io import StringIO
from main import fizzbuzz


class TestFizzBuzz(unittest.TestCase):

    def capture_output(self, n):
        output = StringIO()
        sys.stdout = output
        fizzbuzz(n)
        return output.getvalue().strip().split('\n')

    def test_3_prints_bob(self):
        self.assertEqual(["1", "2", "Bob"], self.capture_output(3))

    def test_5_prints_cat(self):
        self.assertEqual(["1", "2", "Bob", "4", "Cat"], self.capture_output(5))

    def test_15_prints_bobcat(self):
        self.assertEqual(["1", "2", "Bob", "4", "Cat", "Bob", "7", "8", "Bob", "Cat", "11", "Bob", "13", "14", "BobCat"], self.capture_output(15))


if __name__ == '__main__':
    unittest.main()
