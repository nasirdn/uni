import threading
import time
import math
import requests

# Задача 1.1 Несколько потоков
def task1_1():

    def worker():
        print(f"Поток запущен: {threading.current_thread().name}")

    threads = []

    for i in range(5):
        t = threading.Thread(target=worker, name=f"Thread-{id}")
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

# Задача 1.2 Одновременная загрузка нескольких файлов
def task1_2():

    def download_file(url, filename):
        response = requests.get(url)
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"Файл {filename} загружен")

    urls = [
        ("https://ru.pinterest.com/pin/860328335043004175/", "img1.png"),
        ("https://ru.pinterest.com/pin/320388961011668421/", "img2.png"),
        ("https://ru.pinterest.com/pin/1058557087429247986/", "img3.png"),
    ]

    threads = []

    for url, name in urls:
        t = threading.Thread(target=download_file, args=(url, name))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


# Задача 1.3 Одновременные HTTP-запросы
def task1_3():

    def fetch(url):
        response = requests.get(url)
        print(f"{url} -> {response.status_code}")

    urls = [
        "https://www.audi.com/",
        "https://www.toyota.ru/",
        "https://www.porsche.at/",
    ]

    threads = []

    for url in urls:
        t = threading.Thread(target=fetch, args=(url,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


# Задача 1.4 Вычисление факториала числа
def task1_4():

    def partial_factorial(start, end, result, lock):
        temp = 1
        for i in range(start, end + 1):
            temp *= i
        with lock:
            result[0] *= temp

    def factorial_threaded(n, num_threads=4):
        step = n // num_threads
        threads = []
        lock = threading.Lock()
        result = [1]

        for i in range(num_threads):
            start = i * step + 1
            end = (i + 1) * step if i != num_threads - 1 else n
            t = threading.Thread(
                target=partial_factorial,
                args=(start, end, result, lock)
            )
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        return result[0]

    print(f" Факториал 10 = {factorial_threaded(10)}")

# Задача 1.5 Многопоточный алгоритм быстрой сортировки
def task1_5():

    def quicksort(arr):
        if len(arr) <= 1:
            return arr

        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]

        left_sorted = []
        right_sorted = []

        def sort_left():
            nonlocal left_sorted
            left_sorted = quicksort(left)

        def sort_right():
            nonlocal right_sorted
            right_sorted = quicksort(right)

        t1 = threading.Thread(target=sort_left)
        t2 = threading.Thread(target=sort_right)

        t1.start()
        t2.start()
        t1.join()
        t2.join()

        return left_sorted + middle + right_sorted

    data = [5, 3, 8, 4, 2, 7, 1, 6]
    print(f"Изначальный: {data}")
    print(f"Отсортированный: {quicksort(data)}")

# task1_1()
# task1_2()
# task1_3()
# task1_4()
task1_5()