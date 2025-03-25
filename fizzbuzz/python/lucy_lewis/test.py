import unittest
from io import StringIO
import sys

# Read and exec only the fizzbuzz() function from main.py
namespace = {}
with open("main.py") as f:
    code = f.read()

# Extract only the fizzbuzz() definition (assumes it's defined before main())
fizzbuzz_code = code.split("def main():")[0]
exec(fizzbuzz_code, namespace)

# Now we can use namespace["fizzbuzz"] safely without running main()
fizzbuzz = namespace["fizzbuzz"]

class TestFizzBuzz(unittest.TestCase):
    def capture_output(self, n):
        captured_output = StringIO()
        sys.stdout = captured_output
        fizzbuzz(n)
        sys.stdout = sys.__stdout__
        return captured_output.getvalue().strip().split('\n')

    def test_bobcat(self):
        output = self.capture_output(15)
        self.assertEqual(output[14], "BobCat")

    def test_bob(self):
        output = self.capture_output(9)
        self.assertEqual(output[2], "Bob")
        self.assertEqual(output[5], "Bob")
        self.assertEqual(output[8], "Bob")

    def test_cat(self):
        output = self.capture_output(10)
        self.assertEqual(output[4], "Cat")
        self.assertEqual(output[9], "Cat")

    def test_number(self):
        output = self.capture_output(7)
        self.assertEqual(output[0], "1")
        self.assertEqual(output[1], "2")
        self.assertEqual(output[3], "4")
        self.assertEqual(output[6], "7")

if __name__ == "__main__":
    unittest.main()
