'''Закаблукова Анастасия Эдуардовна 2 курс, ИВТ-1.1'''
'''Комплект 1. Задание 1.4'''

from functools import cache

def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

# Пример использования
n = 10
print(f"Число Фибоначчи для {n}: {fibonacci_memo(n)}")


@cache
def fibonacci_cache(n):
    if n <= 1:
        return n
    return fibonacci_cache(n - 1) + fibonacci_cache(n - 2)

# Пример использования
n = 10
print(f"Число Фибоначчи для {n}: {fibonacci_cache(n)}")