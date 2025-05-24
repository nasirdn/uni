import timeit
import matplotlib.pyplot as plt
from ferfact import fermat_factorization as py_ferma
from ferma_fact import fermat_factorization as cy_ferma

TEST_LST = [101, 9973, 104729, 101909, 609133, 1300039, 9999991, 99999959]

py_times = []
for n in TEST_LST:
    t = timeit.timeit(lambda: py_ferma(n), number=10)
    py_times.append(t)
    print(f"Python: {n} - {t:.5f} сек")
py_sum_time = sum((py_times))
print(f"Суммарное время: {py_sum_time:.5f}")

cy_times = []
for n in TEST_LST:
    t = timeit.timeit(lambda: cy_ferma(n), number=10)
    cy_times.append(t)
    print(f"Cython: {n} - {t:.5f} сек")
cy_sum_time = sum((cy_times))
print(f"Суммарное время: {cy_sum_time:.5f}")

plt.figure(figsize=(10, 6))
plt.bar(['Python', 'Cython'], [py_sum_time, cy_sum_time], color=['blue', 'green'])
plt.title('Суммарное время выполнения')
plt.ylabel('Секунды')
plt.show()