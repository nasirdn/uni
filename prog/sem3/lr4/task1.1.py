#Закаблукова Анастасия Эдуардовна, 2 курс, ИВТ-1.1, 3 семестр
#Лабораторная работа №4
#Задание 1.1 Кортеж, где сумма элементов по индексам из равна переменной target

'''Функция two_sum() с параметрами lst и target'''
def two_sum(lst, target):

    '''Нахождение минимальных индексов в списке, сумма элементов с этими
       индексами равна target.'''
    minindex1 = len(lst)
    minindex2 = len(lst)
    for i in range(len(lst)):
        for j in range (i+1, len(lst)):
            if lst[i] + lst[j] == target:
                if i < minindex1:
                    minindex1 = i
                    minindex2 = j
                else:
                    if i == minindex1 and j < minindex2:
                        minindex2 = j
    return (minindex1, minindex2)



'''Объявление списка lst'''
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

'''Сумма элементов должна быть ровна этой переменной'''
target = int(input("Введите сумму элементов (не больше 17): "))

'''Вызов функции two_sum() и объявление полученного кортежа в переменную result'''
result = two_sum(lst, target)

'''Объявление переменной в консоли'''
print(result)