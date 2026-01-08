import math
import timeit

def integrate(f, a, b, *, n_iter=1000):
    """
    Численное интегрирование функции f на отрезке [a, b] методом треугольников.
    :param f: интегрируемая функция
    :param a: нижний предел интегрирования
    :param b: верзний предел интегрирования
    :param n_iter: число разбиений (итераций)
    :return:
    """
    h = (b-a) / n_iter
    result = 0.0

    for i in range(n_iter):
        x = a + i*h
        result += f(x)

    return result*h

def integrate2(f, a, b, n_iter=1000):
    """
    Альтернативный вариант интегрирования.
    """
    h = (b-a) / n_iter
    result = 0.0

    for i in range(n_iter):
        result += f(a + i*h)

    return result*h

def time_test(n):
    return timeit.timeit(
        lambda: integrate(math.sin, 0, 1, n_iter=n),
        number=1
    )

for n in [10**4, 10**5, 10**6]:
    t = time_test(n)
    print(f"n_iter = {n:<7} время = {t:.6f} сек")


