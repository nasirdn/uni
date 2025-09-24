import unittest
from gen_fib import fib_elem_gen, my_gen

class TestFib(unittest.TestCase):

    def test_fib_elem_gen(self):
        """
        Тест для генератора чисел Фибоначчи.
        """
        gen = fib_elem_gen()

        #Провеяем первые 10 чисел Фибоначчи.
        expected_fib_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        for expected in expected_fib_list:
            self.assertEqual(next(gen), expected)

    """
    Тест для корутины my_gen.
    """
    def setUp(self):
        self.gen = my_gen()

    def test_send0(self):
        #Проверка, что при отправки 0 возвращается пустой список.
        self.assertEqual(self.gen.send(0), [])

    def test_send5(self):
        #Проверка, что при отправке 5 возвращаются 5 первых элементов Фибоначчи.
        self.assertEqual(self.gen.send(5), [0, 1, 1, 2, 3])

    def test_send10(self):
        # Проверка, что при отправке 10 возвращаются 10 первых элементов Фибоначчи.
        self.assertEqual(self.gen.send(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

    def test_send50(self):
        # Проверка, что при отправке 50 возвращаются 50 первых элементов Фибоначчи.
        self.assertEqual(self.gen.send(50), [0, 1, 1, 2, 3, 5, 8, 13, 21,
                                             34, 55, 89, 144, 233, 377, 610,
                                             987, 1597, 2584, 4181, 6765, 10946,
                                             17711, 28657, 46368, 75025, 121393,
                                             196418, 317811, 514229, 832040, 1346269,
                                             2178309, 3524578, 5702887, 9227465, 14930352,
                                             24157817, 39088169, 63245986, 102334155,
                                             165580141, 267914296, 433494437, 701408733,
                                             1134903170, 1836311903, 2971215073, 4807526976,
                                             7778742049])

if __name__ == "__main__":
    unittest.main()