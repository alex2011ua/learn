summ = 0
n = int(input())
for i in range(1, n+1):
    summ += (1/i**2)
print('{0:.6f}'.format(summ))
