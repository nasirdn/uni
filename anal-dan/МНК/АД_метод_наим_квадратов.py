#метод наименьших квадратов

import numpy as np
#Ввод данных

n = int(input('Введите размерность квадратной матрицы:'))


#Матрица Х
matrix_X = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        matrix_X[i][j] = int(input(f"Введите элемент [{i+1}][{j+1}] матрицы X:"))

print("Введенная матрица X: ")
for row in matrix_X:
    print(row)


#Матрица Y
nj = 1
matrix_Y = [[0 for _ in range(nj)] for _ in range(n)]
for i in range(n):
    for j in range(nj):
        matrix_Y[i][j] = int(input(f"Введите элемент [{i+1}][{j+1}] матрицы Y:"))

print("Введенная матрица Y: ")
for row in matrix_Y:
    print(row)


#Матрица Х^T
matrix_XT= [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        matrix_XT[j][i] = matrix_X[i][j]

print("Матрица X^T: ")
for row in matrix_XT:
    print(row)


#Перемножение C = X^T * X
matrix_C = np.dot(matrix_XT, matrix_X)

print("Перемножение X^T и X (C) : ")
for row in matrix_C:
    print(row)


#Перемножение Y1 = X^T * Y
matrix_Y1 = np.dot(matrix_XT, matrix_Y)

print("Перемножение X^T и Y (Y1): ")
for row in matrix_Y1:
    print(row)


#Надо решить C = A * Y1 => A = C^-1 * Y1
#Обратная матрица С (С^-1)
obratnay_C = np.round(np.linalg.inv(matrix_C), 5)

print("Обратная матрица С (С^-1) : ")
for row in obratnay_C:
    print(row)


#Перемножение C^-1 и Y1. Нахождение матрицы А (коэффициенты)
matrix_A = np.round(np.dot(obratnay_C, matrix_Y1), 5)

print("Матрица с коэффициентами a : ")
for row in matrix_A:
    print(row)