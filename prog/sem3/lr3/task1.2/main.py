from calculate import calculate

if __name__ == '__main__':
    '''
    Ввод данных пользователем и выбор действия.
    '''
    action = input('Введите действие (mean, variance(дисперсия), std_deviation(станд отклонение), median(медиана), iqr): ')
    numbers = input("Введите числа через запятую: ")
    args = [float(num) for num in numbers.split(',')]
    tolerance = float(input("Введите допустимую точность (по умолчанию 1e-6): ") or 1e-6)

    '''Вывод ответа в консоль. Вызов функции calculate() с параметрами.'''
    result = calculate(action, *args, tolerance=tolerance)
    print(result)
