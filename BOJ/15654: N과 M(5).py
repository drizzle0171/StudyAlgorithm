import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = sorted(list(map(int, input().split())))
s = []

def dfs():
    if len(s) == m:
        print(" ".join(map(str, s)))
        return
    
    for i in range(n):
        if num[i] not in s:
            s.append(num[i])
            dfs()
            s.pop()

dfs()