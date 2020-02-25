'''
сортировка подсчетом
'''


def CountSort(my_list):
    djt = [-1]*101
    for item in my_list:
        djt[item] += 1
    my_sort_list = []
    for i in range(101):
        if djt[i] > -1:
            for j in range(djt[i]+1):
                my_sort_list.append(i)
    return my_sort_list


lst_no_sort = list(map(int, input().split()))
list_sort = CountSort(lst_no_sort)
print(*list_sort)
