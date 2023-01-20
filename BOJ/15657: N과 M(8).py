import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = sorted(list(map(int, input().split())))
s = []

def dfs(start):
    if len(s) == m:
        print(" ".join(map(str, s)))
        return

    for i in range(start, n):
        s.append(num[i])
        dfs(i)
        s.pop()

dfs(0)