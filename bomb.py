n = int(input())
list_city = []
for i in range(n):
    list_city.append(tuple(int(input()), i))
m = int(input())
list_bomb = []
for i in range(m):
    list_bomb.append(tuple(int(input()), i))
list_city.sort()