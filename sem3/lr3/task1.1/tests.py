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
        self.assertEqual(calculate(5, 3, '+', 1e-6), 8.0)
        self.assertEqual(calculate(5, 3, '-', 1e-6), 2.0)
        self.assertEqual(calculate(5, 3, '*', 1e-6), 15.0)
        self.assertEqual(calculate(5, 3, '/', 1e-6), 1.666667)
        self.assertEqual(calculate(5, 0, '/', 1e-6), "Деление на ноль невозможно")
        self.assertEqual(calculate(5, 3, '+', 1e-3), 8.0)  # Проверка с другой точностью
        self.assertEqual(calculate(5.55555, 3.33333, '+', 1e-5), 8.88888)


if __name__ == '__main__':
    unittest.main()
