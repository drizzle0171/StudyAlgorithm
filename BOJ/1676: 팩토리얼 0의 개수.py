import sys

num = int(sys.stdin.readline())

factorial = 1
for i in range(1, num+1):
    factorial = factorial * i

factorial = str(factorial)
result = 0
for i in range(len(factorial)-1, 0, -1):
    if factorial[i] == '0':
        result += 1
    else:
        break

print(result)
