import timeit
import matplotlib.pyplot as plt
import numpy as np
from rec_tree import gen_bin_tree
from nonrec_tree import gen_bin_tree_nonrec

def setup_data():
    heights = range(1, 6)
    roots = range(1, 6)
    params = [(h, r) for h in heights for r in roots]
    return params

def timeit_recursive(params):
    times = []
    for height, root in params:
        timer = timeit.Timer(lambda: gen_bin_tree(height, root))
        times.append(timer.timeit(number=100))
    return times

def timeit_non_recursive(params):
    times = []
    for height, root in params:
        timer = timeit.Timer(lambda: gen_bin_tree_nonrec(height, root))
        times.append(timer.timeit(number=100))
    return times

def plot_results(rec_times, non_rec_times, params):
    plt.figure(figsize=(12, 6))
    heights = [f'Height: {h}, Root: {r}' for h, r in params]
    x = np.arange(len(heights))

    plt.bar(x - 0.2, rec_times, width=0.4, label='Рекурсивный', color='b')
    plt.bar(x + 0.2, non_rec_times, width=0.4, label='Нерекурсивный', color='g')

    plt.xlabel('Параметры (высота, корень)')
    plt.ylabel('Время выполнения (сек)')
    plt.title('Сравнение времени выполнения')
    plt.xticks(x, heights, rotation=45, ha='right')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.savefig('result.png')
    plt.show()

if __name__ == "__main__":
    params = setup_data()
    rec_times = timeit_recursive(params)
    non_rec_times = timeit_non_recursive(params)
    plot_results(rec_times, non_rec_times, params)
