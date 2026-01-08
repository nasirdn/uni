from scipy.optimize import linprog
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

c = [-8000, -12000]
A_ub = [
    [2, 3],
    [4, 6],
    [1, 2]
]
b_ub = [240, 480, 150]
bounds = [(0, None), (0, None)]

result = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs')
print("=== Задача оптимизации производства электроники ===")
print(f"Статус: {result.message}")
print("Смартфоны: ", result.x[0])
print("Планшеты: ", result.x[1])
print("Максимальная прибыль: ", -result.fun)



fig, ax = plt.subplots(figsize=(10, 8))

# Диапазон x1
x1 = np.linspace(0, 150, 400)

# Ограничения (x2 выражаем через x1)
x2_cpu = (240 - 2 * x1) / 3          # процессорное время
x2_ram = (480 - 4 * x1) / 6          # оперативная память
x2_battery = (150 - x1) / 2          # аккумуляторы

# Отсекаем отрицательные значения
x2_cpu[x2_cpu < 0] = 0
x2_ram[x2_ram < 0] = 0
x2_battery[x2_battery < 0] = 0

# Построение линий ограничений
ax.plot(x1, x2_cpu, label='2x₁ + 3x₂ ≤ 240 (CPU)')
ax.plot(x1, x2_ram, label='4x₁ + 6x₂ ≤ 480 (RAM)')
ax.plot(x1, x2_battery, label='x₁ + 2x₂ ≤ 150 (Battery)')

# Вершины допустимой области
vertices = np.array([
    [0, 0],
    [0, 40],
    [60, 40],
    [120, 0]
])

# Закрашивание допустимой области
polygon = Polygon(vertices, alpha=0.3, label='Допустимая область')
ax.add_patch(polygon)

# Оптимальная точка
x_opt, y_opt = 60, 40
ax.plot(x_opt, y_opt, marker='o', markersize=8)
ax.text(x_opt + 2, y_opt + 2, 'Оптимум (60, 40)', fontsize=11)

# Линии уровня целевой функции
profit_levels = [400000, 600000, 800000, 960000]
for P in profit_levels:
    x2_profit = (P - 8000 * x1) / 12000
    ax.plot(x1, x2_profit, linestyle='--', alpha=0.7)

# Оформление
ax.set_xlim(0, 130)
ax.set_ylim(0, 90)
ax.set_xlabel('x₁ (смартфоны)', fontsize=12)
ax.set_ylabel('x₂ (планшеты)', fontsize=12)
ax.set_title('Оптимизация производства электроники', fontsize=14)
ax.legend()
ax.grid(True, alpha=0.3)

plt.show()