import unittest
from main import bobcat_fizzbuzz


class FizzBuzzTest(unittest.TestCase):
    def test_number_2(self):
        self.assertEqual(bobcat_fizzbuzz(2), "1\n2\n")

    def test_number_3(self):
        self.assertEqual(bobcat_fizzbuzz(3), "1\n2\nBob\n")

    def test_number_5(self):
        self.assertEqual(bobcat_fizzbuzz(5), "1\n2\nBob\n4\nCat\n")

    def test_multiples_of_3_and_5(self):
        self.assertEqual(bobcat_fizzbuzz(15).splitlines()[-1], "BobCat")
        self.assertEqual(bobcat_fizzbuzz(30).splitlines()[-1], "BobCat")


if __name__ == '__main__':
    unittest.main()

