"""Задача: Лунные кратеры."""
count = 0


def deter(i: int, j: int) -> None:
    """Рекурсия определения, есть ли по бокам 1."""
    global count
    global matrix

    matrix[i][j] = 2
    if i > 0:
        if matrix[i - 1][j] == 1:
            deter(i - 1, j)
    if j > 0:
        if matrix[i][j - 1] == 1:
            deter(i, j - 1)

    if i < (matrix.__len__() - 1):
        if matrix[i + 1][j] == 1:
            deter(i + 1, j)

    if j < (matrix[i].__len__() - 1):
        if matrix[i][j + 1] == 1:
            deter(i, j + 1)


matrix = []

with open("craters.txt", "r") as f:
    for line in f:
        matrix.append(list(map(int, line.split())))

i = 0


def calculate(matrix: list) -> int:
    """Подсчет кратеров."""
    count = 0
    for i in range(matrix.__len__()):
        for j in range(matrix[i].__len__()):
            if matrix[i][j] == 1:
                count += 1
                deter(i, j)
    print(count)
    return count


calculate(matrix)
