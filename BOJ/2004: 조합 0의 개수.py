import sys

n, m = map(int, sys.stdin.readline().split())

factorial_n = 1
for i in range(1, n+1):
    factorial_n = factorial_n * i
factorial_m = 1
for j in range(1, m+1):
    factorial_m = factorial_m * j
factorial_rest = 1
for k in range(1, n-m+1):
    factorial_rest = factorial_rest * k

combination = str(round((factorial_n/factorial_m)/factorial_rest))

result = 0
for i in range(len(combination)-1, 0, -1):
    if combination[i] == '0':
        result += 1
    else:
        break

print(result)
