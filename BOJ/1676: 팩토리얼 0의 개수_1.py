from math import factorial
import sys

num = int(sys.stdin.readline())
fac = factorial(num)

fac = str(fac)
result = 0
for i in range(len(fac)-1, 0, -1):
    if fac[i] == '0':
        result += 1
    else:
        break

print(result)
