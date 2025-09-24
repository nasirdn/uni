import unittest
from fiblist import FibonacciLst

class TestFibList(unittest.TestCase):

    def test_no_fib_lst(self):
        """Тест для списка без чисел Фибоначчи."""
        self.gen = FibonacciLst([4, 6, 9])
        result = [x for x in self.gen]
        self.assertEqual(result, [])

    def test_only_fib_lst(self):
        """Тест для списка только с числами Фибоначчи."""
        self.gen = FibonacciLst([0, 1, 1, 2, 5, 13])
        result = [x for x in self.gen]
        self.assertEqual(result, [0, 1, 1, 2, 5, 13])

    def test_random_lst(self):
        """Тест для смешанного списка."""
        self.gen = FibonacciLst([0, 1, 1, 4, 7, 2, 5, 13, 4])
        result = [x for x in self.gen]
        self.assertEqual(result, [0, 1, 1, 2, 5, 13])

    def test_duplic_lst(self):
        """Тест для списка с повторяющимися числами."""
        self.gen = FibonacciLst([0, 1, 1, 2, 5, 5, 13, 13])
        result = [x for x in self.gen]
        self.assertEqual(result, [0, 1, 1, 2, 5, 5, 13, 13])

if __name__ == '__main__':
    unittest.main()