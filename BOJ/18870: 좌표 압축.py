import sys

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().strip().split()))
set_num = list(set(num))
set_num.sort()

cnt = []
for i in range(N):
    cnt.append(set_num.index(num[i]))

print(cnt)
for i in cnt:
    print(i, end=' ')