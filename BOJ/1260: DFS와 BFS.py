import sys
from collections import deque
input = sys.stdin.readline

n, m, v= map(int, input().split())
graph = [[] for i in range(n+1)]
visited = [0]*(n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


# dfs
resultDFS = []
def dfs(k):
    resultDFS.append(k)
    visited[k] = 1
    graph[k].sort()
    for i in graph[k]:
        if visited[i] == 0:
            visited[i] = 1
            dfs(i)
dfs(v)

# bfs
resultBFS = []
visited = [0]*(n+1)
visited[v] = 1
Q = deque()
Q.append(v)
while Q:
    current = Q.popleft()
    resultBFS.append(current)
    for i in graph[current]:
        if visited[i] == 0:
            visited[i] = 1
            Q.append(i)

print(" ".join(map(str, resultDFS)))
print(" ".join(map(str, resultBFS)))