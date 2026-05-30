#метод хорд

def f(x):
    return x**3 + 2*x - 6

def metod_chord(a, b, e, n):
    iter = 0
    while abs(f(b)) > e and iter < n:
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
        iter += 1
    return c

root = metod_chord(-20, 20, 0.000001, 1000)
print("Корень уравнения:", root)

