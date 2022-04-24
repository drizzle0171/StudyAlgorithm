import sys

N = int(sys.stdin.readline().strip())
Nlist = set(map(int, sys.stdin.readline().strip().split()))

M = int(sys.stdin.readline().strip())
Mlist = list(map(int, sys.stdin.readline().strip().split()))

for j in Mlist:
    if j in Nlist:
        print(1, end=" ")
    else:
        print(0, end=" ")