import sys
from math import gcd, sqrt

input = sys.stdin.readline

n = int(input())
n_list = []
sub = []
ans = []

for i in range(n):
    i = int(input())
    n_list.append(i)

for i in range(1, n):
    sub.append(n_list[i] - n_list[i-1])

first = sub[0]
for i in range(1, len(sub)):
    first = gcd(first, sub[i])

for i in range(2, int(sqrt(first))+1):
    if first % i:
        ans.append(i)
        ans.append(first//i)

ans.append(first)
ans = list(set(ans))
ans.sort()
print(*ans)