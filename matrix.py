import copy
from rational import TRational
# задаём абстрактный тип number
number = TRational


# описываем класс "Квадратная матрица"
class Matrix:
    # задаём матрицу по умолчанию - единичная матрица 3х3
    # данные самой матрицы - private, поэтому два нижних подчёркивания перед data
    def __init__(self):
        self.__data = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

    # опредяляем метод для того, чтобы получать элемент матрицы через [][]
    def __getitem__(self, item: int):
        return self.__data[item]

    # метод, возвращающий число строк в матрице
    def get_number_of_rows(self):
        return len(self.__data)

    # метод, возвращающий число столбцов в матрице
    def get_number_of_columns(self):
        return len(self.__data[0])

    # метод получения k-ого минора
    def __get_minor(self, data, k):
        res = []
        for r in data[1:]:
            row = []
            for j in range(len(r)):
                if j != k:
                    row.append(r[j])
            res.append(row)
        return res

    # рекурсивный метод для вычисления определителя матрицы
    def __det_count(self, data):
        n = len(data)
        if n == 2:
            return data[0][0] * data[1][1] - data[0][1] * data[1][0]
        s = 0
        z = 1
        for i in range(n):
            s = s + z * data[0][i] * self.__det_count(self.__get_minor(data, i))
            z = -z
        return s

    # публичный метод для нахождения определителя матрицы
    def det(self):
        return self.__det_count(self.__data)

    # публичный метод для вывода матрицы на печать
    def print(self):
        print('Матрица:')
        for i in range(self.get_number_of_rows()):
            for j in range(self.get_number_of_columns()):
                print(self[i][j], end=' ')
            print('\n')
        print('')

    # публичный метод для расчёта ранга матрицы
    def rank(self):
        n = self.get_number_of_columns()
        m = self.get_number_of_rows()
        data = copy.deepcopy(self.__data)
        rank = max(n, m)
        lines = [False for x in range(n)]
        for i in range(0, m):
            for j in range(0, n):
                if (not lines[j]) and (abs(data[j][i]) > number(0)):
                    break
            if j == n:
                rank = rank - 1
            else:
                lines[j] = True
                for p in range(i + 1, m):
                    data[j][p] = data[j][p] / data[j][i]
                for k in range(0, n):
                    if (k != j) and (abs(data[k][i]) > number(0)):
                        for p in range(i + 1, m):
                            data[k][p] = data[k][p] - data[j][p] * data[k][i]
        return rank

    def transpose(self):
        n = self.get_number_of_columns()
        m = self.get_number_of_rows()
        for i in range(m):
            for j in range(n):
                if (i <= j):
                    self.__data[i][j], self.__data[j][i] = self.__data[j][i], self.__data[i][j]

    def set_data(self, data):
        self.__data = data
