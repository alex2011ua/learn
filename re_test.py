import math
a = float(input())
b = a - int(a)
if b == 0.5:
    print(math.ceil(a))
else:
    print(round(a))
