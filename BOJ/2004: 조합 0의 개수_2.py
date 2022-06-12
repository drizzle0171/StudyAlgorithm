import sys
from math import factorial
n, m = map(int, sys.stdin.readline().split())

factorial_n = factorial(n)
factorial_m = factorial(m)
factorial_n_m = factorial(n-m)

combination = str(round((factorial_n/factorial_m)/factorial_n_m))

result = 0
for i in range(len(combination)-1, 0, -1):
    if combination[i] == '0':
        result += 1
    else:
        break

print(result)
