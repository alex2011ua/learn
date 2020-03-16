from sys import stdin
import copy


class Matrix():
    def __init__(self, mylst):
        self.list = copy.deepcopy(mylst)
        self.col_stroka = len(self.list)
        self.col_stolb = len(self.list[0])

    def __str__(self):
        my_str = ""
        for line in self.list:
            for column in line:
                my_str = my_str + str(column) + "\t"
            my_str = my_str.strip() + "\n"
        return my_str.strip()

    def size(self):
        return self.col_stroka, self.col_stolb

    def __add__(self, other):
        result_matrix = [[0] * self.col_stolb for i in range(self.col_stroka)]
        for line in range(self.col_stroka):
            for column in range(self.col_stolb):
                item = self.list[line][column] + other.list[line][column]
                result_matrix[line][column] = item
        return Matrix(result_matrix)

    def __mul__(self, cislo):
        result_matrix = [[0] * self.col_stolb for i in range(self.col_stroka)]
        for line in range(self.col_stroka):
            for column in range(self.col_stolb):
                item = self.list[line][column] * cislo
                result_matrix[line][column] = item
        return Matrix(result_matrix)

    __rmul__ = __mul__


exec(stdin.read())
