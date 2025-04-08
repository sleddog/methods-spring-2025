import unittest
import sys

from main import snow_conditions

class TestSnowConditions(unittest.TestCase):
    def test_powder_snow(self):
        self.assertEqual(snow_conditions(5), "Powder Snow")

    def test_packed_snow_lower_bound(self):
        self.assertEqual(snow_conditions(10), "Packed Snow")

    def test_packed_snow_middle(self):
        self.assertEqual(snow_conditions(20), "Packed Snow")

    def test_packed_snow_upper_bound(self):
        self.assertEqual(snow_conditions(32), "Packed Snow")

    def test_slushy_snow(self):
        self.assertEqual(snow_conditions(33), "Slushy Snow")

if __name__ == "__main__":
    unittest.main()

