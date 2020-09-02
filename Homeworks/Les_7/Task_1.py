"""
1. Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д.
"""

import random

class Matrix:

    def __init__(self, matrix: list = None):
        if matrix:
            self.matrix = matrix
        else:
            # Создать рандомную матрицу, размером 3х3
            self.matrix = [[random.randint(0, 99), random.randint(0, 99), random.randint(0, 99)] for _ in range(3)]

    def __str__(self):
        str_0 = ''
        # Переберём список списков.
        for count in self.matrix:
            # Взять каждый список из списка при помощи map преобразовать каждый элемент в тип str
            # и передать в join для преобразовании строки.
            str_0 += '  '.join(map(str, count)) + '\n'
        return str_0

    def __add__(self, other: 'Matrix'):
        result = []
        # Перебрать matrix, как шаблон и получить индексы.
        for idx in range(len(self.matrix)):
            # функция zip формирует из двух списков на каждой итерации цикла кортеж,
            # который при помощи функции map сумируется и формируется в список.
            result.append(map(sum, zip(self.matrix[idx], other.matrix[idx])))
        return Matrix(result)


list_m1 = Matrix([[1, 2, 3], [4, 5, 6], [1, 2, 3]])
list_m2 = Matrix([[1, 2, 3], [4, 5, 6], [1, 2, 3]])
list_m3 = Matrix()
list_m4 = Matrix()
print(list_m1 + list_m2)
print(list_m3 + list_m4)

