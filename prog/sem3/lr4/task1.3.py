'''Закаблукова Анастасия Эдуардовна 2 курс, ИВТ-1.1'''
'''Комплект 1. Задание 1.3'''

'''Функция two_sum_hashed() с параметрами lst и target'''
def two_sum_hashed(lst, target):
    indexs = {}
    index_pairs = []
    for i, num in enumerate(lst):
        d = target - num
        if d in indexs:
            index_pairs.append((indexs[d], i))
        indexs[num] = i
    return index_pairs

'''Объявление списка lst'''
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

'''Сумма элементов должна быть ровна этой переменной'''
target = int(input("Введите сумму элементов: "))

'''Вызов функции two_sum() и объявление полученного кортежа в переменную result'''
result = two_sum_hashed(lst, target)

'''Объявление переменной в консоли'''
print(result)