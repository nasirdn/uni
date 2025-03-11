from calculate import calculate

if __name__ == '__main__':
    '''
    Ввод данных пользователем первого, второго операндов и оператора.
    '''
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    operator = input('Введите оператор("+", "-", "*", "/"): ')
    tolerance = float(input("Введите допустимую точность (по умолчанию 1e-6): ") or 1e-6)

    '''Вывод ответа в консоль. Вызов функции calculate() с параметрами.'''
    print(calculate(num1, num2, operator, tolerance))
