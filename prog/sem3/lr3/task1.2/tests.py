import unittest
from calculate import calculate, convert_precision


class TestCalculator(unittest.TestCase):

    def test_convert_precision(self):
        self.assertEqual(convert_precision(1e-6), 6)
        self.assertEqual(convert_precision(1e-3), 3)
        self.assertEqual(convert_precision(1e-1), 1)
        self.assertEqual(convert_precision(1), 0)
        self.assertEqual(convert_precision(0.001), 3)  # 1e-3

    def test_calculate(self):
        self.assertEqual(calculate("mean", 1, 2, 3, 4, 5), 3.0)
        self.assertEqual(calculate("variance", 1, 2, 3, 4, 5), 2.5)
        self.assertEqual(calculate("std_deviation", 1, 2, 3, 4, 5), 1.581139)
        self.assertEqual(calculate("median", 1, 2, 3, 4, 5), 3.0)
        self.assertEqual(calculate("iqr", 1, 2, 3, 4, 5), 3.0)
        self.assertEqual(calculate("mean", 5, 10, 15, tolerance=1e-2), 10.0)

if __name__ == '__main__':
    unittest.main()
