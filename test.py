from sys import stdin
import copy

class Matrix():
    def __init__(self, mylst):
        self.list = copy.deepcopy(mylst)
        self.col_stroka = len(self.list)
        self.col_stolbec = len(self.list[0])


    def __str__(self):
        my_str = ""
        for line in self.list:
            for column in line:
                my_str = my_str + str(column) + "\t"
            my_str = my_str.strip() + "\n"
        return my_str.strip()

    def size(self):
        return self.col_stroka, self.col_stolbec


exec(stdin.read())
