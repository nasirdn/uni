def f(x, y):
    return y*(1-x)
x = 0
y = 1
a = 0
b = 1
n = 10
h = ((b - a) / n)
while x <= (b - h):
    k1 = f(x, y)
    k2 = f((x + h / 2), (y + (h / 2) * k1))
    k3 = f((x + h / 2), (y + (h / 2) * k2))
    k4 = f((x + h), (y + h * k3))
    y += ((h / 6) * (k1 + 2 * k2 + 2 * k3 + k4))
    print('x = ', x, ' ', 'y = ', ' ', y)
    x = x + h
