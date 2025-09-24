'''Закаблукова Анастасия Эдуардовна 2 курс, ИВТ-1.1'''
'''Комплект 2. Задание 2.3'''

import numpy as np
import matplotlib.pyplot as plt

'''Функции для первого окна'''
def f1(x):
    return np.sin(x)

def f2(x):
    return np.exp(-x)

'''Функция для второго окна'''
def f3(x):
    return np.cos(x)

'''Создание оси и окон для графиков'''
fig1, (ax1, ax2) = plt.subplots(1, 2)
fig2, ax3 = plt.subplots()

'''Диапазон значений по x для графиков'''
x = np.linspace(0, 100, 1000)

'''Построение графиков для первого окна'''
ax1.plot(x, f1(x), label="sin(x)")
ax1.legend()
ax2.plot(x, f2(x), label="exp(-x)")
ax2.legend()

'''Построение графика для второго окна'''
ax3.plot(x, f3(x), label="cos(x)")
ax3.legend()

'''Отображение окон с графиками'''
plt.show()