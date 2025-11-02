import unittest

def func(n, m, b):
    return n**m % b

def Rem(n, m, b):
    if m == 0:
        result = 1
    elif m % 2 == 0:
        result = func(n ** 2 % b, m // 2, b)
    else:
        result = n * func(n ** 2 % b, (m - 1) // 2, b) % b
    return result


class Tests(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(Rem(11, 2, 3), 1)

    def test_case_2(self):
        self.assertEqual(Rem(5, 0, 2), 1)

    def test_case_3(self):
        self.assertEqual(Rem(2, 3, 5), 8)

    def test_case_4(self):
        self.assertEqual(Rem(4, 2, 3), 1)

    def test_case_5(self):
        self.assertEqual(Rem(3, 4, 7), 4)

if __name__ == "__main__":
    unittest.main()
    # n = 11
    # m = 0
    # b = 8
    # print(Rem(n, m, b))
