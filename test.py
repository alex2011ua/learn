list_a = []
list_b = []
with open('input.txt') as f:
    n, m = f.readline().strip().split()
    for i in range(int(n)):
        list_a.append(int(f.readline().strip()))
    for i in range(int(m)):
        list_b.append(int(f.readline().strip()))
bouth_set = set(list_a) & set(list_b)
print(len(bouth_set))
print(*sorted(list(bouth_set)))
set_a = set(list_a)
set_b = set(list_b)
set_a.difference_update(bouth_set)
print(len(set_a))
d = list(set_a)
d.sort()
print(*d)
set_b.difference_update(bouth_set)
print(len(set_b))
print(*sorted(list(set_b)))
