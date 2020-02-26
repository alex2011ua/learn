n = int(input())
my_set = set(i for i in range(1, n+1))
line_set = input()
while line_set != 'HELP':

    line_set = set(map(int, line_set.split()))

    my_set_yes = my_set & line_set

    if len(my_set_yes)*2 > len(my_set):
        print("YES")
        my_set = my_set_yes

    else:
        print('NO')
        my_set -= line_set

    line_set = input()
my_list = sorted(list(my_set))
print(*my_list)
