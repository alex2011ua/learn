import re
import os
import os.path

def open_page(path, page):


    with open(os.path.join(path, page), encoding = "utf-8") as file:
        links = re.findall(r"(?<=/wiki/)[\w()]+", file.read())
        list_ref = set()
        for f in links:
            if os.path.exists(f) and f != page:
                list_ref.add(f)
        return list_ref


adj = [
#список смежности
    ['a','b'], # 0
    ['a','c','d','f'], # 1
    ['d','g'], # 2
    ['a','d','e'], # 3
    ['a','d'], # 4
    ['c','d','k'] # 5
]

level = [-1] * len(adj)
#список уровней вершин

def bfs(s):
    global level
    level[s] = 0
# уровень начальной вершины
    queue = [s]
 # добавляем начальную вершину в очередь
    while queue:
 # пока там что-то есть
        v = queue.pop(0)
 # извлекаем вершину
        for w in adj[v]:
# запускаем обход из вершины v

# проверка на посещенность
                queue.append(w)
# добавление вершины в очередь
                level[w] = level[v] + 1
# подсчитываем уровень вершины

for i in range(len(adj)):
    if level[i] == -1:
        bfs(i)
 # на случай, если имеется несколько компонент связности

print(level[2])
# уровень вершины 2