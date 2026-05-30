import math
t2 = 0.3
h = 0.03
t = 0
x = 2
y = 1
z = 1
while t < t2:
    print('t = ', t, ' ', 'x = ', x, ' ', 'y = ', y, ' ', 'z = ', z)
    x1 = x + (-2 * x + 5 * z) * h
    y1 = y + (math.sin(t - 1) * x - y + 3 * z) * h
    z1 = z + (-x + 2 * z) * h
    x = x1
    y = y1
    z = z1
    t += h
