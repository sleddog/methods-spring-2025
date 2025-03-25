import unittest
from main import count_mountain_peaks

class TestCountMountainPeaks(unittest.TestCase):
    def test_single_peak(self):
        self.assertEqual(count_mountain_peaks([4500, 7200, 6800]), 1)
    
    def test_multiple_peaks(self):
        self.assertEqual(count_mountain_peaks([4500, 7200, 6800, 8100, 7900, 9000, 8500]), 3)
    
    def test_no_peak(self):
        self.assertEqual(count_mountain_peaks([5000, 6000, 7000, 8000]), 0)

if __name__ == "__main__":
    unittest.main()
