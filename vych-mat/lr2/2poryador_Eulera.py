def f2(x,y,z):
    return y + z / x
a = 1
b = 1.5
x = a
h = 0.1
y = 0.77
z = -0.44
y0 = y
x += h
while x < b+h:
    y += h * z
    z -= h * f2(x, y0, z)
    print('x = ', x, ' ', 'y = ', ' ', y, ' ', 'z = ', z)
    x += h
    y0 = y

