import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
freind = 0
def dfs(x):
    global cnt
    global freind
    visited[x] = 1
    if len(graph[x]) == 0:
        print(freind)
        return
    if cnt == 3:
        print(freind)
        return
    cnt += 1
    for i in graph[x]:
        if visited[i] == 0:
            visited[i] = 1
            freind += 1
            dfs(i)
            
dfs(1)