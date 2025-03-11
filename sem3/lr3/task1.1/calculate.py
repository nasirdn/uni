import math


def convert_precision(tolerance):
    '''Извлекает порядок значения tolerance в виде целого числа.

    Аргументы:
    tolerance -- значение, для которого требуется определить порядок

    Возвращает:
    Порядок значения tolerance как целое число.
    '''
    if tolerance <= 0:
        raise ValueError("Tolerance must be a positive number.")

    # Извлекаем порядок значения tolerance
    order = -int(math.floor(math.log10(tolerance)))
    return order


def calculate(num1, num2, operator, tolerance=1e-6):
    '''Программа-калькулятор. При вызове проверяет тип операндов и деление на ноль, 
    а далее выполняет операцию сложения, вычитания, умножения или деления. 
    Возвращает результат, округленный с учетом указанной точности.

    Аргументы:
    num1 -- первый операнд (число)
    num2 -- второй операнд (число)
    operator -- оператор (строка)
    tolerance -- допустимая точность (по умолчанию 1e-6)

    Возвращает:
    Результат вычисления или сообщение об ошибке.
    '''
    if (type(num1) != int and type(num1) != float):
        return "Ошибка в первом операнде"
    elif (type(num2) != int and type(num2) != float):
        return "Ошибка во втором операнде"
    else:
        # Извлекаем порядок tolerance и используем для округления
        precision_order = convert_precision(tolerance)
        if operator == "+":
            return round(num1 + num2, precision_order)
        elif operator == '-':
            return round(num1 - num2, precision_order)
        elif operator == "*":
            return round(num1 * num2, precision_order)
        elif operator == "/":
            if num2 == 0:
                return "Деление на ноль невозможно"
            else:
                return round(num1 / num2, precision_order)
