import sys
import math

try:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = int(sys.argv[3])
except:
    a = 1
    b = -3
    c = -4

D = b * b - 4 * a * c
if D > 0:
    x1 = (-b + math.sqrt(D)) / 2 * a
    x2 = (-b - math.sqrt(D)) / 2 * a
    print(x1, x2, sep = "\n")

if D == 0:
    x = - b/2 * a
    print(x)