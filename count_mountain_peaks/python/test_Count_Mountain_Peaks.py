import unittest
from script import count_mountain_peaks


class TestMountainPeaks(unittest.TestCase):
    def test_single_peak(self):
        self.assertEqual(count_mountain_peaks([1000, 2000, 1500]), 1)

    def test_multiple_peaks(self):
        self.assertEqual(count_mountain_peaks([4500, 7200, 6800, 8100, 7900, 9000, 8500]), 3)

    def test_no_peaks(self):
        self.assertEqual(count_mountain_peaks([1000, 2000, 3000, 4000]), 0)
        self.assertEqual(count_mountain_peaks([4000, 3000, 2000, 1000]), 0)
        self.assertEqual(count_mountain_peaks([1000, 1000, 1000, 1000]), 0)

    def test_peak_at_end(self):
        self.assertEqual(count_mountain_peaks([1000, 2000, 3000, 2500]), 1)

    def test_plateau(self):
        self.assertEqual(count_mountain_peaks([1000, 2000, 2000, 1500]), 1)
        self.assertEqual(count_mountain_peaks([1000, 2000, 2000, 2500]), 0)

if __name__ == '__main__':
    unittest.main()