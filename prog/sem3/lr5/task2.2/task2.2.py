class BatchCalculatorContextManager:
    '''Класс BatchCalculatorContextManager предоставляет контекстный менеджер
       для управления вводом и выводом данных при расчетах.'''

    '''Инициализация объекта контекстного менеджера с указанием имени файла'''
    def __init__(self, filename):
        self.filename = filename  # имя файла с выходными данными

    '''Метод, который вызывается при входе в контекстный блок. 
       Открывает файл для чтения и возвращает экземпляр класса'''
    def __enter__(self):
        self.file = open(self.filename, 'r')
        return self

    '''Метод, который вызывается при выходе из контекстного блока. Закрывает файл'''
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

    '''Метод для выполнения вычислений с заданными числами и оператором'''
    def calculate(self, number1, operator, number2):
        result = None
        if operator == '+':
            result = number1 + number2
        elif operator == '-':
            result = number1 - number2
        elif operator == '*':
            result = number1 * number2
        elif operator == '/':
            if number2 == 0:
                result = "Деление на ноль невозможно"
            else:
                result = number1 / number2
        else:
            result = "Недопустимый оператор"
        return result

filename = 'calc_input.txt'

with BatchCalculatorContextManager(filename) as calculator:
    for line in calculator.file:
        try:
            num1, op, num2 = line.strip().split()
            result = calculator.calculate(int(num1), op, int(num2))
            print(result)
        except ValueError:
            print("Ошибка: Неправильный формат данных в строке:", line.strip())
        except Exception as e:
            print("Произошла ошибка:", e)
