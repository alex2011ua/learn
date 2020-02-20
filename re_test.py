def poisk(list2):
    list2.sort()
    summ = 0
    i = 0
    while summ < inp[0]:
        summ += list2[i]
        i += 1
    return i - 1


inp = list(map(int, (input().split())))
list_1 = []
summ = 0
for i in range(inp[1]):
    s = int(input())
    list_1.append(s)
    summ += s
if summ <= inp[0]:
    print(inp[1])
else:
    print(poisk(list_1))
