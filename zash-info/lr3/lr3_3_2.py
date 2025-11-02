# LR03, 3.2, Zakablukova Anastasia

import unittest

def mod_expon(a, x, m):
    n = bin(x)[2:]
    c = a
    while len(n) > 0:
        c = (c**2) % m
        if n[0] == '1':
            c = (c * a) % m
        n = n[1:]
    return c

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def phi(m):
    result = []
    for i in range(1, m+1):
        if gcd(m, i) == 1:
            result.append(i)
    return len(result)

def inverse(a, m):
    x = 'x'
    if gcd(a, m) == 1:
        x = (a ** (phi(m)-1) % m)
    return x

class Tests(unittest.TestCase):
    def test_mod_expon(self):

        self.assertEqual(mod_expon(147843136, 8512446241, 673634), 483170)

    # def test_gcd(self):
    #     self.assertEqual(gcd(21, 12), 3)
    #     self.assertEqual(gcd(30, 12), 6)
    #     self.assertEqual(gcd(24, 40), 8)
    #     self.assertEqual(gcd(33, 16), 1)
    #
    # def test_inverse(self):
    #     self.assertEqual(inverse(3, 7), 5)
    #     self.assertEqual(inverse(3, 53), 18)
    #     self.assertEqual(inverse(5, 8), 5)

if __name__ == "__main__":
    unittest.main()
