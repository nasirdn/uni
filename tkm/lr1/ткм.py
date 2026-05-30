#решение слау методом Гаусса (обнуление по столбцам)
print('Исходная матрица')
A = [[5,7,6,5,  23],
    [7,10,8,7,  32],
    [6,8,10,9,  33],
    [5,7,9,10,  31]]
for i in range(len(A)):
    for j in range(len(A[i])):
        print(A[i][j], end=' ')
    print()

def pryamoi(A, B):
    n = len(A)
    for i in range(n):
        # Прямой ход: обнуление под диагональю
        ved_row = i
        for j in range(i+1, n):
            if abs(A[j][i]) > abs(A[ved_row][i]):
                ved_row = j

        A[i], A[ved_row] = A[ved_row], A[i]
        B[i], B[ved_row] = B[ved_row], B[i]
        for j in range(i+1, n):
            ratio = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= ratio * A[i][k]
            B[j] -= ratio * B[i]

def obratny(A, B):
    n = len(A)
    x = [0] * n
    for i in range(n-1, -1, -1):
        x[i] = B[i] / A[i][i]
        for j in range(i+1, n):
            x[i] -= A[i][j] / A[i][i] * x[j]
    return x

def gauss(A, B):
    pryamoi(A, B)
    return obratny(A, B)

# Пример использования
A = [[5,7,6,5],
    [7,10,8,7],
    [6,8,10,9],
    [5,7,9,10]]
B = [23,32,33,31]
answer = gauss(A, B)
print('Результаты при решении методом Гаусса, обнуление по столбцам')
print('B = B', ' ', answer)

#изменение B на 0.1
A = [[5,7,6,5],
    [7,10,8,7],
    [6,8,10,9],
    [5,7,9,10]]
B = [23.1,32.1,33.1,31.1]
answer = gauss(A, B)
print('B = B + 0.1:', ' ', answer)

#изменение B на 0.01
B = [23.01,32.01,33.01,31.01]
answer = gauss(A, B)
print('B = B + 0.01:', ' ', answer)

#изменение B на 0.001
B = [23.001,32.001,33.001,31.001]
answer = gauss(A, B)
print('B = B + 0.001:', ' ', answer)


#решение слау методом Гаусса (исключение неизвестных)
def pryamoi(A, B):
    n = len(A)

    for i in range(n):
        for j in range(i+1, n):
            ratio = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= ratio * A[i][k]
            B[j] -= ratio * B[i]

def obratny(A, B):
    n = len(A)
    x = [0] * n

    for i in range(n-1, -1, -1):
        x[i] = B[i] / A[i][i]
        for j in range(i+1, n):
            x[i] -= A[i][j] / A[i][i] * x[j]

    return x

def gauss(A, B):
    pryamoi(A, B)
    return obratny(A, B)

# Пример использования
A = [[5,7,6,5],
    [7,10,8,7],
    [6,8,10,9],
    [5,7,9,10]]
B = [23,32,33,31]

answer = gauss(A, B)
print('Результаты при решении методом Гаусса, исключение неизвестных')
print('B = B', ' ', answer)

#изменение B на 0.1
A = [[5,7,6,5],
    [7,10,8,7],
    [6,8,10,9],
    [5,7,9,10]]
B = [23.1,32.1,33.1,31.1]
answer = gauss(A, B)
print('B = B + 0.1:', ' ', answer)

#изменение B на 0.01
A = [[5,7,6,5],
    [7,10,8,7],
    [6,8,10,9],
    [5,7,9,10]]
B = [23.01,32.01,33.01,31.01]
answer = gauss(A, B)
print('B = B + 0.01:', ' ', answer)

#изменение B на 0.001
A = [[5,7,6,5],
    [7,10,8,7],
    [6,8,10,9],
    [5,7,9,10]]
B = [23.001,32.001,33.001,31.001]
answer = gauss(A, B)
print('B = B + 0.001:', ' ', answer)


#решение СЛАУ методом Гаусса-Жордана
def gauss(A, B):
    n = len(A)

    for i in range(n):
        for j in range(n):
            if i != j:
                ratio = A[j][i] / A[i][i]

                for k in range(n):
                    A[j][k] = A[j][k] - ratio * A[i][k]
                B[j] = B[j] - ratio * B[i]

    for i in range(n):
        delit = A[i][i]
        for j in range(n):
            A[i][j] = A[i][j] / delit
        B[i] = B[i] / delit

    return B

# Пример использования
A = [[5,7,6,5],
    [7,10,8,7],
    [6,8,10,9],
    [5,7,9,10]]
B = [23,32,33,31]

answer = gauss(A, B)
print('Результаты при решении методом Гаусса-Жордана')
print('B = B', ' ', answer)

#изменение B на 0.1
A = [[5,7,6,5],
    [7,10,8,7],
    [6,8,10,9],
    [5,7,9,10]]
B = [23.1,32.1,33.1,31.1]
answer = gauss(A, B)
print('B = B + 0.1:', ' ', answer)

#изменение B на 0.01
A = [[5,7,6,5],
    [7,10,8,7],
    [6,8,10,9],
    [5,7,9,10]]
B = [23.01,32.01,33.01,31.01]
answer = gauss(A, B)
print('B = B + 0.01:', ' ', answer)

#изменение B на 0.001
A = [[5,7,6,5],
    [7,10,8,7],
    [6,8,10,9],
    [5,7,9,10]]
B = [23.001,32.001,33.001,31.001]
answer = gauss(A, B)
print('B = B + 0.001:', ' ', answer)





