import sys

TestNum = int(sys.stdin.readline())

for _ in range(TestNum):
    N, M = map(int, sys.stdin.readline().strip().split())
    priority = map(int, sys.stdin.readline().strip().split())

    order = 1
    for i in range(N, 0, -1):
        if i<M:
            order += 1
        if N == 1:
            print(1)
        elif i == M:
            print(order)
        else:
            print(True)
