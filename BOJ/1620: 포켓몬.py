import sys
input = sys.stdin.readline
N, M = map(int, input().split())

pocket = dict()
for i in range(1, N+1):
    mon = input().rstrip()
    pocket[i] = mon
    pocket[mon] = i

for i in range(M):
    q = input().rstrip()
    if q.isdigit():
        print(pocket[int(q)])
    else:
        print(pocket[q])