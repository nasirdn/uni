import math

x = math.pi/4
a = [1, 1.000000002, 1, -0.166666589, 1, 0.008333075, 1, -0.000198107, 1, 0.000002608]
eps = 0.000002
n = 9
k = 3
c = x
while k <= n:
    if k % 2 != 0:
        u = a[k] * (x**k)
        c += u
        if abs(u) <= eps:
            break
    k += 1

print(f'sin({round(x,6)}) = {round(c,6)}')


