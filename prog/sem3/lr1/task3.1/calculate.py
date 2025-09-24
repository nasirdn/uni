def calculate(num1, num2, operator):
  '''программа-калькулятор. при вызове проверяет тип операндов и деление на ноль, а далее
     выполняет операцую сложения, вычитание, умножение или деление. возвращает результат.'''
  if (type(num1) != int and type(num1) != float):
    return "Ошибка в первом операнде"
  elif (type(num2) != int and type(num2) != float):
    return "Ошибка во втором операнде"
  else:
    if operator == "+":
      return num1 + num2
    elif operator == '-':
      return num1 - num2
    elif operator == "*":
      return num1 * num2
    elif operator == "/":
      if num2 == 0:
        return "Дeление на ноль невозможно"
      else:
        return num1 / num2