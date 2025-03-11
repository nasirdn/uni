import math
import statistics


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


def calculate(action, *args, tolerance=1e-6):
    '''Программа-калькулятор. Выполняет различные математические операции.

    Аргументы:
    action -- действие (строка)
    *args -- переменное количество операндов (числа)
    tolerance -- допустимая точность (по умолчанию 1e-6)

    Возвращает:
    Результат вычисления или сообщение об ошибке.
    '''
    if not args:
        return "Ошибка: Необходимо передать хотя бы один операнд."

    # Проверка на корректность типов
    for arg in args:
        if not isinstance(arg, (int, float)):
            return f"Ошибка в операнде: {arg}"

    # Извлекаем порядок tolerance и используем для округления
    precision_order = convert_precision(tolerance)

    if action == "mean":
        return round(statistics.mean(args), precision_order)
    elif action == "variance":
        return round(statistics.variance(args), precision_order)
    elif action == "std_deviation":
        return round(statistics.stdev(args), precision_order)
    elif action == "median":
        return round(statistics.median(args), precision_order)
    elif action == "iqr":
        q1 = statistics.quantiles(args, n=4)[0]  # Первый квартиль
        q3 = statistics.quantiles(args, n=4)[2]  # Третий квартиль
        return round(q3 - q1, precision_order)
    else:
        return "Ошибка: Неизвестное действие."

