#метод деления отрезков

import math

def f(x):
    return x**3 + 2*x - 6

def delotr(a, b, E):
    while abs(b - a) > E:
        del_pol = (a + b) / 2
        if f(a) * f(del_pol) < 0:
            b = del_pol
        else:
            a = del_pol
    return (a + b) / 2

x = delotr(-20, 20, 0.000001)
print(x)
