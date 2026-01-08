from scipy.optimize import linprog
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

c = [8, 6, 10, 9, 7, 5]

A_eq = [
    [1,1,1,0,0,0],
    [0,0,0,1,1,1],
    [1,0,0,1,0,0],
    [0,1,0,0,1,0],
    [0,0,1,0,0,1]
]

b_eq = [150, 250, 120, 180, 100]

bounds = [(0, None)] * 6

result = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')

print(result.x)
print("Минимальная стоимость:", result.fun)




fig, ax = plt.subplots(figsize=(14, 10))

# Координаты узлов
warehouses = {
    'Склад 1': (2, 8),
    'Склад 2': (2, 3)
}

bases = {
    'Альфа': (10, 10),
    'Бета': (10, 5.5),
    'Гамма': (10, 1)
}

# Функция рисования узла
def draw_node(x, y, text, width=2.5, height=1.2):
    rect = FancyBboxPatch(
        (x - width/2, y - height/2),
        width, height,
        boxstyle="round,pad=0.3"
    )
    ax.add_patch(rect)
    ax.text(x, y, text, ha='center', va='center', fontsize=11, fontweight='bold')

# Рисуем склады
for name, (x, y) in warehouses.items():
    draw_node(x, y, name)

# Рисуем базы
for name, (x, y) in bases.items():
    draw_node(x, y, f'База {name}')

# Оптимальные потоки (из решения)
flows = [
    ('Склад 1', 'Бета', 150, 6),
    ('Склад 2', 'Альфа', 120, 9),
    ('Склад 2', 'Бета', 30, 7),
    ('Склад 2', 'Гамма', 100, 5)
]

# Рисуем потоки
for src, dst, volume, cost in flows:
    x1, y1 = warehouses[src]
    x2, y2 = bases[dst]

    arrow = FancyArrowPatch(
        (x1 + 1.5, y1),
        (x2 - 1.5, y2),
        arrowstyle='->',
        linewidth=1 + volume / 60,
        mutation_scale=15
    )
    ax.add_patch(arrow)

    # Подпись потока
    xm, ym = (x1 + x2) / 2, (y1 + y2) / 2
    ax.text(
        xm, ym + 0.3,
        f'{volume} т\nc={cost}',
        ha='center',
        va='center',
        fontsize=10
    )

# Оформление
ax.set_xlim(0, 12)
ax.set_ylim(0, 12)
ax.set_aspect('equal')
ax.axis('off')
ax.set_title(
    'Оптимальный план снабжения военных баз',
    fontsize=16,
    fontweight='bold'
)

plt.tight_layout()
plt.show()