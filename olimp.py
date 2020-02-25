def inp(arg):
    ar = str(arg).split()
    a, b, c = int(ar[-1]), int(ar[-2]), int(ar[-3])
    d = a + b + c
    if a < 40 or b < 40 or c < 40:
        return None
    return d


base = []
with open('input.txt', encoding='utf8') as file:
    n = int(file.readline())
    for line in file:
        my_list = inp(line.strip())
        if my_list is None:
            continue
        else:
            base.append(my_list)
base.sort(reverse=True)
otvet = ''
if len(base) <= n:
    otvet = 0
elif n == 0:
    otvet = 0
elif base[n-1] == base[n]:
    while base[n-1] == base[n]:
        n = n-1
        if n == 0:
            otvet = 1
            break
        otvet = base[n - 1]
else:
    otvet = base[n-1]
with open('output.txt', 'w', encoding='utf8') as f:
    f.write(str(otvet))
