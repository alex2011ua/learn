import sys

my_dict = {}
my_list = []
for line in sys.stdin:
    line_list = list(line.rstrip().split())
    for word in line_list:
        my_dict[word] = my_dict.get(word, 0) + 1
for i, item in my_dict.items():
    my_list.append((-item, i))
my_list.sort()
for i in my_list:
    print(i[1])
