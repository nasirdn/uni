#Комплекс 1. Заданиее 1.2
# Закаблукова Анастасия Эдуардовна. 2 курс, ИВТ-1.1

''''импорт модуля random, который позволяет генерировать случайные числа.'''
import random

'''Генераторная функция для генерации случайных чисел в указаном диапазоне.'''
def gen_random(count, minv, maxv):
    for i in range(count):
        yield random.randint(minv, maxv) #Возвращает каждое число

'''Вызов функции gen_random()'''
ran_num = gen_random(5, 1, 10)
for num in ran_num:
    print(num)