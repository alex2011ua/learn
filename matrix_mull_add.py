from sys import stdin
import copy


class MatrixError(BaseException):
    def __init__(self, fest, other):
        self.matrix1 = fest
        self.matrix2 = other


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

    def __mul__(self, other):
        result_matrix = [[0] * self.col_stolb for i in range(self.col_stroka)]
        if isinstance(other, int) or isinstance(other, float):
            for line in range(self.col_stroka):
                for column in range(self.col_stolb):
                    item = self.list[line][column] * other
                    result_matrix[line][column] = item
            return Matrix(result_matrix)
        elif isinstance(other, Matrix):
            if self.col_stolb == other.col_stroka:
                result_matrix = \
                    [[0] * other.col_stolb for i in range(self.col_stroka)]
                for line in range(self.col_stroka):
                    for column in range(other.col_stolb):
                        summa = 0
                        for num, ind_a in enumerate(self.list[line]):
                            summa += ind_a * other.list[num][column]
                        item = summa
                        result_matrix[line][column] = item
                return Matrix(result_matrix)
            else:
                raise MatrixError(self, other)
        else:
            raise MatrixError(self, other)

    __rmul__ = __mul__

#exec(stdin.read())

m1 = Matrix([[3, 2], [-10, 0], [14, 5]])

m2 = Matrix([[5, 2, 10], [-0.5, -0.25, 18], [-22, -2.5, -0.125]])

print(m2 * m1)

print(Matrix.transposed(m2 * m1))

print(m1.transpose() * m2.transpose())
'''Ответ:

135 60

253.0 89.0

-42.75 -44.625

135 253.0 -42.75

60 89.0 -44.625

135 253.0 -42.75

60 89.0 -44.625'''