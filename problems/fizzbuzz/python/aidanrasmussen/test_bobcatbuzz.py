import unittest
from main import bobcatbuzz
from io import StringIO
import sys

class TestBobcatBuzz(unittest.TestCase):

    def capture_output(self, n):
        # Capture the printed output of bobcatbuzz
        captured_output = StringIO()
        sys.stdout = captured_output
        bobcatbuzz(n)  # Call the function which prints output
        sys.stdout = sys.__stdout__  # Reset stdout to its original value
        return captured_output.getvalue().strip().split("\n")

    def test_bob(self):
        self.assertEqual(self.capture_output(3), ['1', '2', 'Bob'])

    def test_cat(self):
        self.assertEqual(self.capture_output(5), ['1', '2', 'Bob', '4', 'Cat'])

    def test_bobcat(self):
        self.assertEqual(self.capture_output(15), [
            '1', '2', 'Bob', '4', 'Cat',
            'Bob', '7', '8', 'Bob', 'Cat',
            '11', 'Bob', '13', '14', 'BobCat'
        ])

    def test_no_bobcat(self):
        self.assertEqual(self.capture_output(2), ['1', '2'])

if __name__ == '__main__':
    unittest.main()