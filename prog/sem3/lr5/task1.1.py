#Комплекс 1. Заданиее 1.1
# Закаблукова Анастасия Эдуардовна. 2 курс, ИВТ-1.1

''''импорт модуля random, который позволяет генерировать случайные числа.'''
import random

'''Создаем класс RandomNumberIterator'''
class RandomNumberIterator:
    def __init__(self, count, minv, maxv):
        self.count = count #количество случайных чисел
        self.minv = minv #минимальное значение случайного числа
        self.maxv = maxv #максимальное значение случайного числа
        self.current_index = 0 #текущий индекс генерируемого случайного числа

    def __iter__(self):
        return self

    '''Проверяем, не достигло ли заданного количества случайных чисел. Если да, то
       вызываем исключение StopIteration для остановки итерации.'''
    def __next__(self):
        if self.current_index >= self.count:
            raise StopIteration

        '''Если не ддостигнуто, то генерируем случайное число с помощью random.randint
           и увеличиваем current_count на 1 и возвращает сгенерированное число.'''
        random_number = random.randint(self.minv, self.maxv)
        self.current_index += 1

        return random_number

iterator = RandomNumberIterator(5, 1, 10)
for num in iterator:
    print(num)

