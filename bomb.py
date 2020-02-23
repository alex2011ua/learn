n = int(input())
list_city = []
for i in range(n):
    list_city.append(tuple(map(int, input().split()), i))
m = int(input())
list_bomb = []
for i in range(m):
    list_bomb.append(tuple(map(int, input().split()), i))
list_city.sort()