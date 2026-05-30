#метод касательных

import math
def f(x):
    return x**3 + 2*x - 6
def proizv_f(x):
    return 3*x**2 + 2
E= 0.000001
b = 20
a = -20
if f(a) * f(b) > 0:
    x = a
else:
    x = b
print("При начальном значение х =", x)
x1 = x - f(x) / proizv_f(x)
while abs(x1 - x) >= E:
    x = x1 - f(x1) / proizv_f(x1)
    x1 = x - f(x) / proizv_f(x)
print(x)
