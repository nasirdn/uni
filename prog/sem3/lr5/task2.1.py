#Комплекс 2. Задание 2.1
# Закаблукова Анастасия Эдуардовна. 2 курс, ИВТ-1.1

import time

'''Время запускается перед выполнением кода, а затем завершается 
   после его выполнения. Затраченное время выводится на экран'''
class Timer:
    '''Класс для замера времени выполнения операций'''
    def __enter__(self):
        '''Метод-контекстный менеджер, запускающий таймер перед выполнением кода'''
        self.start_time = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        '''Метод-контекстный менеджер, завершающий таймер после выполнения кода.
           Рассчитывает и выводит затраченное время.'''
        self.end_time = time.perf_counter()
        self.elapsed_time = self.end_time - self.start_time
        print(f'Затраченное время: {self.elapsed_time} секунд.')

def fibonacci(n):
    '''Функция, генерирующая последовательность чисел Фибоначчи'''
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a+b

with Timer() as timer:
    fib_num = list(fibonacci(6000))