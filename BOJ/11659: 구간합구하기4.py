import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nlist = list(map(int, input().split()))
prefix_total = [0]

temp = 0
for i in nlist:
    temp += i
    prefix_total.append(temp)

for _ in range(m):
    i, j = map(int, input().split())
    print(prefix_total[j] - prefix_total[i-1])
    