my_list = []
my_dict = {}
count_line = 0

def mu_print(*arg):
    with open("output.txt", 'w', encoding='utf8') as file:
        for item in arg:
            lim = str(arg + '\n')
            file.writelines(lim)


with open('input.txt', encoding='utf8') as file:
    for line in file:
        count_line += 1
        s = line.strip()
        my_dict[s] = my_dict.get(s, 0) + 1
for key, count in my_dict.items():
    my_list.append((-count, key))
my_list.sort()
print(my_list[0][0]*-2, '&', count_line)
if my_list[0][0] * -2 > count_line:
    mu_print(my_list[0][1])
else:
    mu_print(my_list[0][1], my_list[1][1])
