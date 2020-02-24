n = int(input())
list_city = list(map(int, input().split()))
list_tuple_city = []
for i in range(n):
    list_tuple_city.append((list_city[i], i))
m = int(input())
list_bomb = list(map(int, input().split()))
list_tuple_bomb = []
for i in range(1, m + 1):
    list_tuple_bomb.append((list_bomb[i-1], i))

list_tuple_city.sort()
list_tuple_bomb.sort()
# print(list_tuple_city)
# print(list_tuple_bomb)
list_otvet = []
i = 0
j = 0
k = j + 1
if m == 1:
    print('1 ' * n)
else:
    while i < n:
        if abs(list_tuple_city[i][0] - list_tuple_bomb[j][0]) <= \
                abs(list_tuple_city[i][0] - list_tuple_bomb[k][0]):
            list_otvet.append((list_tuple_city[i][1], list_tuple_bomb[j][1]))
            i += 1
        else:
            j += 1
            k += 1

        if j > m-1:
            j = m-1
        if k >= m-1:
            k = m - 1

    list_otvet.sort()
    for item in list_otvet:
        print(item[1], end=' ')
